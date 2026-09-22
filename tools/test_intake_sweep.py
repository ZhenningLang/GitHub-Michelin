#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import intake_sweep


def write_page(root: Path, rel: str, body: str = "") -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    slug = path.name.removesuffix(".md")
    path.write_text(
        f"""---
name: {slug}
slug: {slug}
repo: https://github.com/example/{slug}
category: {path.parent.name}
tags: [demo]
language: Python
license: MIT
maturity: active
last_verified: 2026-09-22
type: tool
---

# {slug}

{body}
""",
        encoding="utf-8",
    )
    return path


class IntakeSweepTest(unittest.TestCase):
    def test_split_names_handles_slash_and_ideographic_comma(self) -> None:
        self.assertEqual(intake_sweep.split_names("GSAP / Motion / Theatre.js"), ["GSAP", "Motion", "Theatre.js"])
        self.assertEqual(intake_sweep.split_names("Slidev、Marp"), ["Slidev", "Marp"])
        self.assertEqual(intake_sweep.split_names("[verl](verl.md) / HF TRL"), ["verl", "HF TRL"])

    def test_search_match_reports_confidence(self) -> None:
        exact = {"items": [{"name": "rq", "full_name": "rq/rq", "stargazers_count": 1}]}
        likely = {"items": [{"name": "server", "full_name": "nextcloud/server", "stargazers_count": 1}]}
        weak = {"items": [{"name": "motion-canvas", "full_name": "org/motion-canvas", "stargazers_count": 1}]}
        empty: dict = {"items": []}

        self.assertEqual(intake_sweep.search_match("RQ", exact)[1], "exact")
        self.assertEqual(intake_sweep.search_match("Nextcloud", likely)[1], "likely")
        self.assertEqual(intake_sweep.search_match("Motion", weak)[1], "weak")
        self.assertEqual(intake_sweep.search_match("CapCut", empty), (None, "none"))

    def test_build_skips_placeholders_and_aliases_and_records_non_repo(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/alpha.md")
            (root / "categories" / "demo" / "INDEX.md").write_text(
                "# demo\n\n## Comparison matrix\n\n"
                "| Option | Indexed | Health | One-line tradeoff |\n"
                "| --- | --- | --- | --- |\n"
                "| Gamma / Delta | 未收录 | — | Two repositories named by the pages. |\n"
                "| alpha | 未收录 | — | Already has a page: the row is stale. |\n"
                "| CapCut / G HUB | 未收录（非仓库） | — | Legacy combined spelling; both are closed products. |\n"
                "| Kibana / Datadog | 非仓库 | — | Already out of scope, so not backlog debt. |\n"
                "| (alternatives named across the pages) | 未收录 | — | Placeholder row. |\n",
                encoding="utf-8",
            )

            items, notes = intake_sweep.build_items(root, "matrix")
            by_id = {item.id: item for item in items}

            # A pure `非仓库` row is already resolved and never enters the queue.
            self.assertEqual(set(by_id), {"gamma", "delta", "capcut", "g-hub"})
            self.assertEqual(by_id["gamma"].status, "todo")
            self.assertEqual(by_id["gamma"].target_category, "demo")
            self.assertEqual(by_id["capcut"].status, "non_repo")
            self.assertEqual(by_id["capcut"].reason, "row already marked 非仓库")
            self.assertEqual(len(notes), 2)  # the alias and the placeholder row
            self.assertTrue(any("alias of an indexed page" in note for note in notes))
            self.assertTrue(any("placeholder row skipped" in note for note in notes))

    def test_ledger_round_trip_is_resumable(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "categories" / "demo").mkdir(parents=True)
            (root / "categories" / "demo" / "INDEX.md").write_text(
                "# demo\n\n## Comparison matrix\n\n"
                "| Option | Indexed | Health | One-line tradeoff |\n"
                "| --- | --- | --- | --- |\n"
                "| Gamma | 未收录 | — | A repository. |\n",
                encoding="utf-8",
            )

            items, _notes = intake_sweep.build_items(root, "matrix")
            intake_sweep.save_ledger(root, "9", {item.id: item for item in items})

            # classify --offline must not touch the network and must not invent matches
            intake_sweep.classify_items(root, "9", None, offline=True)
            loaded = intake_sweep.load_ledger(root, "9")
            self.assertEqual(loaded["gamma"].repo, "")

            loaded["gamma"].status = "done"
            loaded["gamma"].evidence.append("page added")
            intake_sweep.save_ledger(root, "9", loaded)

            again, _ = intake_sweep.build_items(root, "matrix")
            merged = intake_sweep.load_ledger(root, "9")
            for item in again:
                merged.setdefault(item.id, item)
            self.assertEqual(merged["gamma"].status, "done")
            self.assertEqual(merged["gamma"].evidence, ["page added"])

            raw = intake_sweep.ledger_path(root, "9").read_text(encoding="utf-8").splitlines()
            self.assertEqual(json.loads(raw[0])["id"], "gamma")

    def test_worker_brief_names_both_outcomes(self) -> None:
        item = intake_sweep.Item(
            id="gamma",
            name="Gamma",
            row="| Gamma | 未收录 | — | A repository. |",
            target_category="demo",
            sources=["categories/demo/INDEX.md:8"],
            repo="org/gamma",
            stars=12,
            confidence="likely",
            evidence=["GitHub search: org/gamma stars=12"],
        )

        brief = intake_sweep.worker_brief(item, Path("."))

        self.assertIn("REAL REPOSITORY", brief)
        self.assertIn("Confidence: likely", brief)
        self.assertIn("not a repository", brief)
        self.assertIn("categories/demo/", brief)


if __name__ == "__main__":
    unittest.main()
