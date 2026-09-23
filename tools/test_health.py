#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import json
import types
import os
import sys
import time
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

import health


class FakeRepo(health.RepoData):
    def __init__(self, ptype: str = "library") -> None:
        super().__init__("owner", "demo", ptype, dt.datetime(2026, 7, 4, tzinfo=dt.timezone.utc))
        self._core = health.GhResult(200, '{"archived": false}')


def graphql_result(repo_payload: dict) -> health.GhResult:
    return health.GhResult(200, health.json.dumps({"data": {"repository": repo_payload}}))


def pr_node(created: str, author: str, response: str | None, reviewer: str = "maintainer", *, comment: bool = False) -> dict:
    reviews = [] if response is None or comment else [{"createdAt": response, "author": {"login": reviewer}}]
    comments = [] if response is None or not comment else [{"createdAt": response, "author": {"login": reviewer}}]
    return {
        "createdAt": created,
        "author": {"login": author},
        "reviews": {"nodes": reviews},
        "comments": {"nodes": comments},
    }


def no_install_signals():
    """Silence the §2.3b fallback instruments.

    They reach the network (gh releases, Homebrew, Docker Hub); the registry-path tests
    below are about selection logic, not distribution channels, and must stay offline.
    """
    return mock.patch("health._adoption_from_install_signals", return_value=None)


class HealthMechanismTest(unittest.TestCase):
    def test_resolve_gh_cli_honors_env_override(self) -> None:
        with mock.patch.dict(os.environ, {"OSS_ATLAS_GH": "/tmp/custom-gh"}):
            self.assertEqual(health.resolve_gh_cli(), "/tmp/custom-gh")

    def test_resolve_gh_cli_uses_path_discovery(self) -> None:
        with mock.patch.dict(os.environ, {}, clear=True), mock.patch("health.shutil.which", return_value="/usr/bin/gh"):
            self.assertEqual(health.resolve_gh_cli(), "/usr/bin/gh")

    def test_gh_api_missing_cli_returns_explicit_transport_error(self) -> None:
        with mock.patch.dict(os.environ, {}, clear=True), mock.patch("health.shutil.which", return_value=None):
            result = health.gh_api("repos/owner/demo")

        self.assertEqual(result.status, 0)
        self.assertIn("gh CLI not found", result.body)

    def test_gh_api_uses_resolved_cli_for_graphql_and_rest(self) -> None:
        calls: list[list[str]] = []

        def fake_run(cmd, **_kwargs):
            calls.append(cmd)
            stdout = "HTTP/2.0 200 OK\n\n{}" if "graphql" not in cmd else "{}"
            return type("Proc", (), {"returncode": 0, "stdout": stdout, "stderr": ""})()

        with mock.patch.dict(os.environ, {"OSS_ATLAS_GH": "/tmp/gh"}), mock.patch("health.subprocess.run", side_effect=fake_run):
            health.gh_api("repos/owner/demo")
            health.gh_api("query", graphql=True, fields={"o": "owner"})

        self.assertTrue(calls)
        self.assertTrue(all(call[0] == "/tmp/gh" for call in calls))
        self.assertFalse(any(call[0] == "/opt/homebrew/bin/gh" for call in calls))

    def test_responsiveness_pr_fallback_scores_b_from_three_pr_reviews(self) -> None:
        repo_payload = {
            "hasIssuesEnabled": True,
            "isArchived": False,
            "createdAt": "2020-01-01T00:00:00Z",
            "issues": {"nodes": []},
            "pullRequests": {
                "nodes": [
                    pr_node("2026-06-01T00:00:00Z", "alice", "2026-06-01T10:00:00Z"),
                    pr_node("2026-06-02T00:00:00Z", "bob", "2026-06-02T12:00:00Z"),
                    pr_node("2026-06-03T00:00:00Z", "carol", "2026-06-03T14:00:00Z"),
                ]
            },
        }
        with mock.patch("health.gh_api", return_value=graphql_result(repo_payload)):
            axis = health.axis_responsiveness(FakeRepo("library"))

        self.assertEqual(axis.grade, "B")
        self.assertEqual(axis.raw["source"], "pr")
        self.assertEqual(axis.raw["qualifying_issues"], 3)

    def test_responsiveness_pr_fallback_can_score_a_with_five_pr_comments(self) -> None:
        repo_payload = {
            "hasIssuesEnabled": True,
            "isArchived": False,
            "createdAt": "2020-01-01T00:00:00Z",
            "issues": {"nodes": []},
            "pullRequests": {
                "nodes": [
                    pr_node("2026-06-01T00:00:00Z", "alice", "2026-06-01T10:00:00Z", comment=True),
                    pr_node("2026-06-02T00:00:00Z", "bob", "2026-06-02T12:00:00Z", comment=True),
                    pr_node("2026-06-03T00:00:00Z", "carol", "2026-06-03T14:00:00Z", comment=True),
                    pr_node("2026-06-04T00:00:00Z", "dana", "2026-06-04T16:00:00Z", comment=True),
                    pr_node("2026-06-05T00:00:00Z", "erin", "2026-06-05T18:00:00Z", comment=True),
                ]
            },
        }
        with mock.patch("health.gh_api", return_value=graphql_result(repo_payload)):
            axis = health.axis_responsiveness(FakeRepo("library"))

        self.assertEqual(axis.grade, "A")
        self.assertEqual(axis.raw["source"], "pr")
        self.assertEqual(axis.raw["qualifying_issues"], 5)

    def test_responsiveness_pr_fallback_ignores_self_and_bot_responses(self) -> None:
        repo_payload = {
            "hasIssuesEnabled": True,
            "isArchived": False,
            "createdAt": "2020-01-01T00:00:00Z",
            "issues": {"nodes": []},
            "pullRequests": {
                "nodes": [
                    pr_node("2026-06-01T00:00:00Z", "alice", "2026-06-01T10:00:00Z", reviewer="alice"),
                    pr_node("2026-06-02T00:00:00Z", "bob", "2026-06-02T12:00:00Z", reviewer="dependabot[bot]"),
                    pr_node("2026-06-03T00:00:00Z", "carol", "2026-06-03T14:00:00Z", reviewer="maintainer"),
                ]
            },
        }
        with mock.patch("health.gh_api", return_value=graphql_result(repo_payload)):
            axis = health.axis_responsiveness(FakeRepo("library"))

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "no_window_signal")

    def test_responsiveness_github_failure_is_not_no_traffic(self) -> None:
        with mock.patch("health.gh_api", return_value=health.GhResult(0, '{"_transport_error":"boom"}')):
            axis = health.axis_responsiveness(FakeRepo("library"))

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "github_unavailable")
        self.assertIn("GraphQL HTTP 0", axis.evidence)

    def test_responsiveness_genuine_no_traffic_remains_no_traffic(self) -> None:
        repo_payload = {
            "hasIssuesEnabled": True,
            "isArchived": False,
            "createdAt": "2020-01-01T00:00:00Z",
            "issues": {"nodes": []},
            "pullRequests": {"nodes": []},
        }
        with mock.patch("health.gh_api", return_value=graphql_result(repo_payload)):
            axis = health.axis_responsiveness(FakeRepo("library"))

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "no_traffic")

    def test_responsiveness_traffic_without_window_signal_is_distinct(self) -> None:
        repo_payload = {
            "hasIssuesEnabled": True,
            "isArchived": False,
            "createdAt": "2020-01-01T00:00:00Z",
            "issues": {"nodes": [{"createdAt": "2026-06-01T00:00:00Z", "author": {"login": "alice"}, "comments": {"nodes": []}, "timelineItems": {"nodes": []}}]},
            "pullRequests": {"nodes": [pr_node("2026-06-02T00:00:00Z", "bob", None), pr_node("2026-06-03T00:00:00Z", "carol", None), pr_node("2026-06-04T00:00:00Z", "dana", None)]},
        }
        with mock.patch("health.gh_api", return_value=graphql_result(repo_payload)):
            axis = health.axis_responsiveness(FakeRepo("library"))

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "no_window_signal")

    def test_adoption_structural_no_package_for_app(self) -> None:
        with no_install_signals(), mock.patch("health.http_get_json", return_value=(200, [])):
            axis = health.axis_adoption(FakeRepo("app"))

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "no_package_structural")

    def test_adoption_lookup_failure_is_distinct_reason(self) -> None:
        with no_install_signals(), mock.patch("health.http_get_json", return_value=(0, None)):
            axis = health.axis_adoption(FakeRepo("library"))

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "registry_lookup_failed")

    def test_adoption_lookup_http_failure_is_distinct_reason(self) -> None:
        for status in (403, 429, 500):
            with self.subTest(status=status), no_install_signals(), mock.patch("health.http_get_json", return_value=(status, None)):
                axis = health.axis_adoption(FakeRepo("library"))

            self.assertEqual(axis.grade, "?")
            self.assertEqual(axis.reason, "registry_lookup_failed")
            self.assertIn(f"HTTP {status}", axis.evidence)

    def test_adoption_ambiguous_candidates_remains_unknown(self) -> None:
        candidates = [{"name": "other", "downloads": 1, "rank": 1, "registry": "pypi.org"}]
        with no_install_signals(), mock.patch("health.http_get_json", return_value=(200, candidates)):
            axis = health.axis_adoption(FakeRepo("library"))

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "ambiguous")

    def test_adoption_successful_empty_lookup_for_package_type_scores_e(self) -> None:
        with no_install_signals(), mock.patch("health.http_get_json", return_value=(200, [])):
            axis = health.axis_adoption(FakeRepo("library"))

        self.assertEqual(axis.grade, "E")
        self.assertEqual(axis.raw["dependent_repos_count"], 0)
        self.assertIsNone(axis.raw["downloads_last_month"])

    def test_adoption_missing_counts_does_not_silently_zero(self) -> None:
        # Genuinely no counts of either kind -> `?`, never a zero-derived E.
        package = {"name": "demo", "downloads": None, "dependent_repos_count": None,
                   "registry": "repo1.maven.org"}
        with no_install_signals(), mock.patch("health.http_get_json", return_value=(200, [package])):
            axis = health.axis_adoption(FakeRepo("library"))

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "registry_no_counts")
        self.assertNotIn("dependent_repos_count", axis.raw)

    def test_downloads_are_tiered_even_on_an_unlisted_registry(self) -> None:
        # selenium reported 345,857,423 downloads/month on gem.coop, which had no anchor
        # row; the figure was dropped and the page scored E off dependents alone.
        package = {"name": "demo", "downloads": 345_857_423, "dependent_repos_count": 0,
                   "registry": "gem.coop"}
        with no_install_signals(), mock.patch("health.http_get_json", return_value=(200, [package])):
            axis = health.axis_adoption(FakeRepo("library"))

        self.assertEqual(axis.raw["volume_tier"], "A")
        self.assertEqual(axis.grade, "A")

    def test_risk_license_scores_gpl3_as_strong_copyleft(self) -> None:
        repo = FakeRepo("tool")
        license_result = health.GhResult(
            200,
            health.json.dumps({
                "license": {"spdx_id": "GPL-3.0-only", "key": "gpl-3.0"},
                "path": "LICENSE",
            }),
        )
        conditions = {"conditions": ["disclose-source", "same-license", "state-changes"], "limitations": []}

        with mock.patch("health.gh_api", return_value=license_result), \
                mock.patch("health._license_conditions", return_value=conditions), \
                mock.patch("health._detect_relicense", return_value=False):
            axis = health.axis_risk_license(repo)

        self.assertEqual(axis.grade, "D")
        self.assertEqual(axis.raw["permissiveness"], "strong_network_copyleft")

    def test_noassertion_composite_license_degrades_to_unknown(self) -> None:
        repo = FakeRepo("app")
        license_result = health.GhResult(
            200,
            health.json.dumps({
                "license": {"spdx_id": "NOASSERTION", "key": "other"},
                "path": "LICENSE.txt",
            }),
        )
        # Composite file shape (Mattermost's LICENSE.txt): preamble grants
        # MIT-for-binaries / AGPL-or-commercial-for-source, then embeds the full
        # Apache-2.0 text as the Admin Tools sub-license. The embedded template
        # must NOT be promoted to a permissive grade.
        composite_blob = (
            "Mattermost Licensing\n\n"
            "You are licensed to use compiled versions under an MIT LICENSE.\n"
            "You may be licensed to use source code under the GNU AGPL v3.0 "
            "or a commercial license.\n\n"
            "Apache License\nVersion 2.0, January 2004\n"
            "Licensed under the Apache License, Version 2.0\n"
            "http://www.apache.org/licenses/LICENSE-2.0\n"
        )

        with mock.patch("health.gh_api", return_value=license_result), \
                mock.patch("health._fetch_license_blob", return_value=composite_blob):
            axis = health.axis_risk_license(repo)

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "license_unparsed")

    def test_permissiveness_scores_lgpl_library_condition_as_weak_copyleft(self) -> None:
        conditions = ["disclose-source", "same-license--library", "state-changes"]

        self.assertEqual(health._classify_permissiveness(conditions), "weak_file_copyleft")

    def test_permissiveness_scores_mpl_file_condition_as_weak_copyleft(self) -> None:
        conditions = ["disclose-source", "same-license--file", "state-changes"]

        self.assertEqual(health._classify_permissiveness(conditions), "weak_file_copyleft")

    def test_declared_proprietary_license_scores_e_and_caps_non_skillpack(self) -> None:
        repo = FakeRepo("framework")
        repo.declared_license = "Proprietary"

        with mock.patch("health.gh_api", side_effect=AssertionError("declared proprietary must not call GitHub license API")):
            axis = health.axis_risk_license(repo)
        axes = {
            "maintenance": health.Axis("A", {}),
            "responsiveness": health.Axis("A", {}),
            "adoption": health.Axis("A", {}),
            "longevity": health.Axis("A", {}),
            "governance": health.Axis("A", {}),
            "risk_license": axis,
        }
        aggregate = health.aggregate(health._with_meta_type(axes, "framework"))

        self.assertEqual(axis.grade, "E")
        self.assertEqual(axis.raw["permissiveness"], "source_available")
        self.assertEqual(aggregate["overall"], "D")
        self.assertTrue(aggregate["capped"])


PAGE_WITH_BLOCK = """---
name: Demo
health:
  schema: 1
  computed_at: 2026-07-01T00:00:00Z
  overall: B
  axes:
    maintenance:
      grade: A
      raw: {}
    responsiveness:
      grade: "?"
      raw: {}
type: tool
---

# Demo
"""


class GradeChangeReportTest(unittest.TestCase):
    def test_extract_grades_reads_overall_and_axes(self) -> None:
        grades = health.extract_grades(PAGE_WITH_BLOCK)
        self.assertEqual(grades["overall"], "B")
        self.assertEqual(grades["maintenance"], "A")
        self.assertEqual(grades["responsiveness"], "?")

    def test_extract_grades_stops_at_next_top_level_key(self) -> None:
        # `type: tool` after the health block must not pollute the result.
        grades = health.extract_grades(PAGE_WITH_BLOCK)
        self.assertNotIn("type", grades)

    def test_extract_grades_on_fresh_page_is_empty(self) -> None:
        self.assertEqual(health.extract_grades("---\nname: Demo\n---\n\n# Demo\n"), {})

    def test_grade_changes_reports_only_moved_grades(self) -> None:
        old = {"overall": "A", "maintenance": "A", "adoption": "C"}
        new = {"overall": "B", "maintenance": "A", "adoption": "C", "longevity": "A"}
        self.assertEqual(health.grade_changes(old, new), [("overall", "A", "B")])

    def test_grade_changes_empty_old_reports_nothing(self) -> None:
        self.assertEqual(health.grade_changes({}, {"overall": "A"}), [])



class RateLimitTest(unittest.TestCase):
    """An exhausted quota must not reach the axes as an ordinary failure.

    Axis functions degrade an API error to `?`, so a 403 from a spent rate limit would be
    written to the page as "unmeasurable" — and across a 600-page batch it would overwrite
    hundreds of real grades with unknowns that look measured.
    """

    HEADERS = ("HTTP/2 403\r\n"
               "x-ratelimit-remaining: 0\r\n"
               "x-ratelimit-reset: {reset}\r\n\r\n{{}}")

    def test_exhausted_quota_is_detected(self) -> None:
        raw = self.HEADERS.format(reset=9999999999)
        self.assertTrue(health._rate_limited(403, raw))
        self.assertTrue(health._rate_limited(429, raw))

    def test_ordinary_403_is_not_treated_as_rate_limiting(self) -> None:
        raw = "HTTP/2 403\r\nx-ratelimit-remaining: 4500\r\n\r\n{}"
        self.assertFalse(health._rate_limited(403, raw))

    def test_absurd_reset_is_not_waited_on(self) -> None:
        # A clock skew or a bad header must not park the run for hours.
        raw = self.HEADERS.format(reset=int(time.time()) + 999_999)
        self.assertFalse(health._retry_after_reset(raw))

    def test_past_reset_needs_no_wait(self) -> None:
        raw = self.HEADERS.format(reset=int(time.time()) - 60)
        self.assertFalse(health._retry_after_reset(raw))


class CanonicalSelectionTest(unittest.TestCase):
    """Which package a repo's adoption number is read off.

    Picking the wrong candidate does not fail loudly — it reports a real measurement of
    the wrong thing, which is why each rule here is pinned by a case that shipped.
    """

    def test_go_pseudo_module_never_outranks_real_packages(self) -> None:
        # proxy.golang.org synthesizes `github.com/{owner}/{repo}` for ANY repo, so its
        # name always contains the repo name and always won the substring match.
        # material-ui scored D off a 2-dependent Go pseudo-module while its npm packages
        # carried 154k dependents.
        candidates = [
            {"name": "github.com/mui/material-ui", "downloads": None,
             "dependent_repos_count": 2, "registry": "proxy.golang.org"},
            {"name": "@mui/material", "downloads": 36_513_050,
             "dependent_repos_count": 163_982, "registry": "npmjs.org"},
        ]
        picked = health._select_canonical(candidates, "mui", "material-ui")
        self.assertEqual(picked["name"], "@mui/material")

    def test_lone_go_pseudo_module_is_not_a_package_for_a_python_repo(self) -> None:
        # The only "candidate" a package-less repo has is the Go proxy's synthetic module
        # with 0 dependents. Accepting it turned "no package anywhere" into a measured
        # E for 39 pages, swe-agent (Python) among them.
        candidates = [{"name": "github.com/swe-agent/swe-agent", "downloads": None,
                       "dependent_repos_count": 0, "registry": "proxy.golang.org"}]
        self.assertIsNone(
            health._select_canonical(candidates, "swe-agent", "swe-agent", "Python"))

    def test_lone_go_pseudo_module_is_kept_for_an_actual_go_repo(self) -> None:
        candidates = [{"name": "github.com/cli/cli", "downloads": None,
                       "dependent_repos_count": 4200, "registry": "proxy.golang.org"}]
        picked = health._select_canonical(candidates, "cli", "cli", "Go")
        self.assertIsNotNone(picked)

    def test_unrelated_package_is_not_adopted_on_volume_alone(self) -> None:
        # ecosyste.ms listed a NuGet package called `digitalbanking` under
        # jaegertracing/jaeger. Picking the highest-download candidate regardless of name
        # printed that stranger's package on the page as jaeger's canonical one.
        candidates = [{"name": "digitalbanking", "downloads": 1034,
                       "dependent_repos_count": 0, "registry": "nuget.org"}]
        self.assertIsNone(
            health._select_canonical(candidates, "jaegertracing", "jaeger", "Go"))

    def test_countless_distro_build_cannot_license_an_e_verdict(self) -> None:
        # An Ubuntu/Alpine/Nix entry with neither downloads nor dependents says only
        # "somebody packaged this once"; scoring E off it asserts a measurement nobody made.
        candidates = [{"name": "demo", "downloads": None, "dependent_repos_count": 0,
                       "registry": {"name": "ubuntu-23.04", "ecosystem": "ubuntu"}}]
        self.assertIsNone(health._select_canonical(candidates, "owner", "demo", "C"))

    def test_scoped_package_matches_on_repo_owner(self) -> None:
        # A monorepo publishes @scope/* where no package carries the repo's own name.
        candidates = [
            {"name": "@mui/types", "downloads": 54_061_754,
             "dependent_repos_count": 154_773, "registry": "npmjs.org"},
            {"name": "@mui/material", "downloads": 36_513_050,
             "dependent_repos_count": 163_982, "registry": "npmjs.org"},
        ]
        # Both are in scope, but only one also matches the repo name -> it wins on the
        # stronger claim, not on raw downloads.
        picked = health._select_canonical(candidates, "mui", "material-ui")
        self.assertEqual(picked["name"], "@mui/material")

    def test_primary_registry_outranks_a_mirror(self) -> None:
        # gem.coop mirrors RubyGems; letting it win canonical put selenium, asciidoctor
        # and loki on a registry whose counts the anchor table did not cover.
        candidates = [
            {"name": "selenium-webdriver", "downloads": 345_857_423,
             "dependent_repos_count": 0, "registry": "gem.coop"},
            {"name": "selenium-webdriver", "downloads": 9_000_000,
             "dependent_repos_count": 12_000, "registry": "rubygems.org"},
        ]
        picked = health._select_canonical(candidates, "SeleniumHQ", "selenium")
        self.assertEqual(health._registry_name(picked), "rubygems.org")

    def test_typosquats_still_lose_without_the_rank_filter(self) -> None:
        candidates = [
            {"name": "flask", "downloads": 133_128_741, "dependent_repos_count": 100,
             "registry": "pypi.org"},
            {"name": "f-ask", "downloads": 18, "dependent_repos_count": 0, "registry": "pypi.org"},
            {"name": "flask-mirror-upstream", "downloads": 17, "dependent_repos_count": 0,
             "registry": "pypi.org"},
        ]
        picked = health._select_canonical(candidates, "pallets", "flask")
        self.assertEqual(picked["name"], "flask")

    def test_null_rank_no_longer_discards_every_candidate(self) -> None:
        # ecosyste.ms returns rank: null for every candidate of every repo probed
        # (2026-09). The old `rank is not None` filter therefore dropped 100% of them.
        candidates = [{"name": "playwright", "downloads": 323_433_868,
                       "dependent_repos_count": 9_850, "rank": None, "registry": "npmjs.org"}]
        self.assertIsNotNone(health._select_canonical(candidates, "microsoft", "playwright"))

    def test_name_variants_strip_language_suffixes(self) -> None:
        # elasticsearch-dsl-py ships as `elasticsearch-dsl`; ecosyste.ms maps neither.
        self.assertIn("elasticsearch-dsl", health._name_variants("elasticsearch-dsl-py"))
        self.assertIn("requests", health._name_variants("python-requests"))
        self.assertEqual(health._name_variants("flask"), ["flask"])


class NotApplicableAxisTest(unittest.TestCase):
    def test_skill_pack_without_package_is_not_applicable_not_unknown(self) -> None:
        with mock.patch("health._adoption_from_install_signals", return_value=None), \
             mock.patch("health.http_get_json", return_value=(200, [])):
            axis = health.axis_adoption(FakeRepo("skill-pack"))
        self.assertEqual(axis.grade, "N/A")
        self.assertEqual(axis.reason, "no_install_channel")

    def test_app_without_package_stays_unknown_not_not_applicable(self) -> None:
        # An app CAN be adopted measurably (installers, images); failing to find the
        # number is our gap, not a statement that the question does not apply.
        with mock.patch("health._adoption_from_install_signals", return_value=None), \
             mock.patch("health.http_get_json", return_value=(200, [])):
            axis = health.axis_adoption(FakeRepo("app"))
        self.assertEqual(axis.grade, "?")

    def test_not_applicable_axis_shrinks_the_denominator(self) -> None:
        axes = {k: health.Axis("B", {}) for k in
                ("maintenance", "responsiveness", "longevity", "governance", "risk_license")}
        axes["adoption"] = health.Axis.not_applicable("no_install_channel")
        agg = health.aggregate(axes)
        self.assertEqual(agg["scored_axes"], 5)
        self.assertEqual(agg["applicable_axes"], 5)

    def test_unknown_axis_keeps_the_denominator(self) -> None:
        axes = {k: health.Axis("B", {}) for k in
                ("maintenance", "responsiveness", "longevity", "governance", "risk_license")}
        axes["adoption"] = health.Axis.unknown("ambiguous")
        agg = health.aggregate(axes)
        self.assertEqual(agg["scored_axes"], 5)
        self.assertEqual(agg["applicable_axes"], 6)

    def test_not_applicable_is_emitted_separately_from_unknowns(self) -> None:
        axes = {k: health.Axis("B", {}) for k in health.AXIS_ORDER}
        axes["adoption"] = health.Axis.not_applicable("no_install_channel")
        axes["responsiveness"] = health.Axis.unknown("no_traffic")
        out = health.emit_health_yaml(health.aggregate(dict(axes)), axes,
                                      "2026-09-22T00:00:00Z", False)
        self.assertIn("not_applicable:", out)
        self.assertIn("adoption: { reason: no_install_channel }", out)
        self.assertIn("responsiveness: { reason: no_traffic }", out)
        self.assertIn('grade: "N/A"', out)


class MaxAcrossChannelsTest(unittest.TestCase):
    """The axis takes the best of registry and install channels (spec §2.3b)."""

    def _axis(self, candidates, *, releases):
        with mock.patch("health._homebrew_installs", return_value=None), \
             mock.patch("health._release_downloads", return_value=(releases, 9)), \
             mock.patch("health._docker_pulls", return_value=(None, None)), \
             mock.patch("health.http_get_json", return_value=(200, candidates)):
            return health.axis_adoption(FakeRepo("tool"))

    def test_binary_first_project_is_not_held_down_by_a_token_package(self) -> None:
        # immich's shape: a token registry presence (6,496 downloads/month, no
        # dependents) next to 4.7M binary downloads. The registry alone scored it D.
        cands = [{"name": "demo", "downloads": 6_496, "dependent_repos_count": 3,
                  "registry": "npmjs.org"}]
        axis = self._axis(cands, releases=4_699_204)
        self.assertEqual(axis.grade, "B")
        self.assertEqual(axis.raw["tier_source"], "releases")
        self.assertEqual(axis.raw["release_downloads"], 4_699_204)

    def test_registry_first_project_is_not_inflated_by_a_dead_release_channel(self) -> None:
        # angular's shape: 24.6M npm downloads/month, 324 release-asset downloads.
        cands = [{"name": "demo", "downloads": 24_664_067,
                  "dependent_repos_count": 50_000, "registry": "npmjs.org"}]
        axis = self._axis(cands, releases=324)
        self.assertEqual(axis.grade, "A")
        self.assertEqual(axis.raw["tier_source"], "registry")

    def test_weak_install_channel_never_drags_a_grade_down(self) -> None:
        cands = [{"name": "demo", "downloads": 6_000_000,
                  "dependent_repos_count": 20_000, "registry": "npmjs.org"}]
        self.assertEqual(self._axis(cands, releases=12).grade, "A")


class InstallSignalCacheTest(unittest.TestCase):
    def test_empty_index_is_not_cached(self) -> None:
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            with mock.patch.object(health, "HEALTH_CACHE_DIR", Path(d)):
                health._cache_json("probe", 3600, lambda: {})
                self.assertFalse((Path(d) / "probe.json").exists())
                health._cache_json("probe", 3600, lambda: {"a/b": 5})
                self.assertTrue((Path(d) / "probe.json").exists())


class InstrumentTierTest(unittest.TestCase):
    def test_tier_from_anchors_maps_bands(self) -> None:
        anchors = (1000, 100, 10)
        self.assertEqual(health._tier_from_anchors(5000, anchors), "A")
        self.assertEqual(health._tier_from_anchors(100, anchors), "B")
        self.assertEqual(health._tier_from_anchors(10, anchors), "C")
        self.assertEqual(health._tier_from_anchors(5, anchors), "D")
        self.assertIsNone(health._tier_from_anchors(None, anchors))

    def test_install_signals_never_reach_e(self) -> None:
        # Asymmetry guard: a tiny release-asset count is not proof of non-adoption,
        # because the project's real distribution channel may be one we cannot read.
        anchors = (1000, 100, 10)
        self.assertEqual(health._tier_from_anchors(1, anchors), "D")
        self.assertEqual(health._tier_from_anchors(0, anchors), "D")

    def test_skill_pack_with_release_bundle_is_measured_not_na(self) -> None:
        # 18 of this index's 84 skill-packs publish downloadable bundles; conceding N/A
        # by type alone would have thrown those real numbers away.
        repo = FakeRepo("skill-pack")
        with mock.patch("health._homebrew_installs", return_value=None), \
             mock.patch("health._release_downloads", return_value=(120_000, 30)), \
             mock.patch("health._docker_pulls", return_value=(None, None)):
            axis = health._adoption_from_install_signals(repo, False)
        self.assertIsNotNone(axis)
        self.assertEqual(axis.grade, "C")
        self.assertEqual(axis.raw["signal_basis"], "releases")


class LicenseDetectionTest(unittest.TestCase):
    """"GitHub could not classify a license" must not be written as "there is none".

    `repos/{full}/license` 404s whenever GitHub's detector declines, which includes a real
    license in a place it does not look. apache/poi keeps Apache-2.0 at `legal/LICENSE`,
    and the old `404 -> NONE -> E` shortcut graded the ASF's flagship Java library as
    all-rights-reserved and capped the whole page to D. 33 pages carried that verdict.
    """

    def test_license_filenames_accepted(self) -> None:
        for name in ("LICENSE", "license", "LICENCE", "LICENSE.txt", "LICENSE.md",
                     "LICENSE.rst", "COPYING", "COPYING.txt", "UNLICENSE", "COPYRIGHT",
                     "LICENSE-APACHE", "LICENSE-MIT", "LICENSE-2.0.txt", "license-2.0"):
            with self.subTest(name=name):
                self.assertTrue(health._is_license_filename(name))

    def test_files_that_only_mention_licensing_are_rejected(self) -> None:
        """A policy doc or a source file must not count as the license text."""
        for name in ("LICENSING.md", "license_test.go", "LICENSE.py", "LICENSE.go",
                     "licenses.json", "licensed.rb", "copying_utils.py", "NOTICE",
                     "README.md", "THIRD-PARTY-LICENSES.csv"):
            with self.subTest(name=name):
                self.assertFalse(health._is_license_filename(name))

    def _repo(self):
        return types.SimpleNamespace(full="owner/demo")

    def test_finds_a_license_outside_the_root(self) -> None:
        calls = []

        def fake(path, **kw):
            calls.append(path)
            if path == "repos/owner/demo/contents":
                return health.GhResult(200, json.dumps(
                    [{"type": "file", "name": "README.md", "path": "README.md"},
                     {"type": "dir", "name": "legal", "path": "legal"}]))
            if path == "repos/owner/demo/contents/legal":
                return health.GhResult(200, json.dumps(
                    [{"type": "file", "name": "LICENSE", "path": "legal/LICENSE"}]))
            return health.GhResult(404, "")

        with mock.patch.object(health, "gh_api", side_effect=fake):
            self.assertEqual(health._find_license_path(self._repo()), ("legal/LICENSE", "file"))
        self.assertIn("repos/owner/demo/contents", calls)

    def test_root_license_short_circuits_the_directory_probe(self) -> None:
        """Cost control: the extra calls only happen when the root has nothing."""
        calls = []

        def fake(path, **kw):
            calls.append(path)
            return health.GhResult(200, json.dumps(
                [{"type": "file", "name": "LICENSE", "path": "LICENSE"}]))

        with mock.patch.object(health, "gh_api", side_effect=fake):
            self.assertEqual(health._find_license_path(self._repo()), ("LICENSE", "file"))
        self.assertEqual(calls, ["repos/owner/demo/contents"])

    def test_no_license_anywhere_returns_none(self) -> None:
        """The genuinely unlicensed case still has to be reachable — it earns a real E."""
        def fake(path, **kw):
            if path == "repos/owner/demo/contents":
                return health.GhResult(200, json.dumps(
                    [{"type": "file", "name": "README.md", "path": "README.md"}]))
            return health.GhResult(404, "")

        with mock.patch.object(health, "gh_api", side_effect=fake):
            self.assertEqual(health._find_license_path(self._repo()), (None, None))

    def test_reuse_style_license_directory_is_reported_as_such(self) -> None:
        """A per-SPDX `LICENSES/` tree lists bundled licenses too, so one file proves nothing.

        cockpit-project/cockpit declares LGPL-2.1-or-later and its first entry is
        `BSD-3-Clause.txt`; classifying from that would be a coin flip, and a bundled
        `SSPL-1.0.txt` would yield a confident, wrong E.
        """
        def fake(path, **kw):
            if path == "repos/owner/demo/contents":
                return health.GhResult(200, json.dumps(
                    [{"type": "dir", "name": "LICENSES", "path": "LICENSES"}]))
            if path == "repos/owner/demo/contents/licenses":
                return health.GhResult(200, json.dumps(
                    [{"type": "file", "name": "BSD-3-Clause.txt",
                      "path": "LICENSES/BSD-3-Clause.txt"}]))
            return health.GhResult(404, "")

        with mock.patch.object(health, "gh_api", side_effect=fake):
            path, how = health._find_license_path(self._repo())
        self.assertEqual(how, "dedicated_dir")
        self.assertEqual(path, "LICENSES/BSD-3-Clause.txt")

    def test_plain_license_in_a_dedicated_dir_is_still_classifiable(self) -> None:
        """`legal/LICENSE` is one file stating the terms — that one can be read."""
        def fake(path, **kw):
            if path == "repos/owner/demo/contents":
                return health.GhResult(200, json.dumps([]))
            if path == "repos/owner/demo/contents/legal":
                return health.GhResult(200, json.dumps(
                    [{"type": "file", "name": "LICENSE", "path": "legal/LICENSE"}]))
            return health.GhResult(404, "")

        with mock.patch.object(health, "gh_api", side_effect=fake):
            self.assertEqual(health._find_license_path(self._repo()),
                             ("legal/LICENSE", "file"))

    def test_declared_license_separates_unverifiable_from_all_rights_reserved(self) -> None:
        """No LICENSE file is not the same claim as no license.

        pygame ships LGPL-2.1 and openresty/lua-nginx-module BSD-2-Clause, both declared
        in the README with no file to find; swarm-forge really is all-rights-reserved.
        The page's own `license:` field is what tells them apart.
        """
        for declared in ("LGPL-2.1", "BSD-2-Clause", "MIT", "Apache-2.0", "GPL-3.0-or-later"):
            with self.subTest(declared=declared):
                self.assertTrue(health.DECLARED_REAL_LICENSE_RE.match(declared))
                self.assertFalse(health.DECLARED_NO_LICENSE_RE.match(declared))
        for declared in ("NONE", "NONE (no LICENSE file — all rights reserved)",
                         "Not declared (no LICENSE file in repo)", "Unlicensed"):
            with self.subTest(declared=declared):
                self.assertTrue(
                    health.DECLARED_NO_LICENSE_RE.match(declared)
                    or not health.DECLARED_REAL_LICENSE_RE.match(declared))

    def test_unreadable_listing_does_not_invent_a_license(self) -> None:
        with mock.patch.object(health, "gh_api",
                               side_effect=lambda path, **kw: health.GhResult(500, "")):
            self.assertEqual(health._find_license_path(self._repo()), (None, None))


if __name__ == "__main__":
    unittest.main()