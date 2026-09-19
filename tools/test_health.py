#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import os
import sys
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
        with mock.patch("health.http_get_json", return_value=(200, [])):
            axis = health.axis_adoption(FakeRepo("app"))

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "no_package_structural")

    def test_adoption_lookup_failure_is_distinct_reason(self) -> None:
        with mock.patch("health.http_get_json", return_value=(0, None)):
            axis = health.axis_adoption(FakeRepo("library"))

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "registry_lookup_failed")

    def test_adoption_lookup_http_failure_is_distinct_reason(self) -> None:
        for status in (403, 429, 500):
            with self.subTest(status=status), mock.patch("health.http_get_json", return_value=(status, None)):
                axis = health.axis_adoption(FakeRepo("library"))

            self.assertEqual(axis.grade, "?")
            self.assertEqual(axis.reason, "registry_lookup_failed")
            self.assertIn(f"HTTP {status}", axis.evidence)

    def test_adoption_ambiguous_candidates_remains_unknown(self) -> None:
        candidates = [{"name": "other", "downloads": 1, "rank": 1, "registry": "pypi.org"}]
        with mock.patch("health.http_get_json", return_value=(200, candidates)):
            axis = health.axis_adoption(FakeRepo("library"))

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "ambiguous")

    def test_adoption_successful_empty_lookup_for_package_type_scores_e(self) -> None:
        with mock.patch("health.http_get_json", return_value=(200, [])):
            axis = health.axis_adoption(FakeRepo("library"))

        self.assertEqual(axis.grade, "E")
        self.assertEqual(axis.raw["dependent_repos_count"], 0)
        self.assertIsNone(axis.raw["downloads_last_month"])

    def test_adoption_missing_counts_does_not_silently_zero(self) -> None:
        package = {"name": "demo", "downloads": 1000, "rank": 1, "registry": "repo1.maven.org"}
        with mock.patch("health.http_get_json", return_value=(200, [package])):
            axis = health.axis_adoption(FakeRepo("library"))

        self.assertEqual(axis.grade, "?")
        self.assertEqual(axis.reason, "registry_no_counts")
        self.assertNotIn("dependent_repos_count", axis.raw)

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


if __name__ == "__main__":
    unittest.main()
