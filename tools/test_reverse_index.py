#!/usr/bin/env python3
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import reverse_index


def write_page(root: Path, rel: str, slug: str, *, repo: str | None = None) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = "---\n"
    if repo is not None:
        frontmatter += f"repo: {repo}\n"
    frontmatter += "---\n\n"
    path.write_text(frontmatter, encoding="utf-8")
    return path


def write_index(root: Path, rel: str, rows: list[str]) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("| Option | Indexed | Note |\n|---|---|---|\n" + "\n".join(rows) + "\n", encoding="utf-8")
    return path


class ReverseIndexTest(unittest.TestCase):
    def test_slugify_normalizes_display_names(self) -> None:
        self.assertEqual(reverse_index.slugify("Claude Code Router"), "claude-code-router")
        self.assertEqual(reverse_index.slugify("`LiteLLM`"), "litellm")
        self.assertEqual(reverse_index.slugify("PR-Agent (Qodo)"), "pr-agent")

    def test_alternative_names_splits_composite_cells(self) -> None:
        self.assertEqual(
            reverse_index.alternative_names("Prefect / Dagster / Argo Workflows"),
            ["Prefect", "Dagster", "Argo Workflows"],
        )
        self.assertEqual(reverse_index.alternative_names("a, b; c"), ["a", "b", "c"])

    def test_repo_index_maps_repo_to_page(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_page(root, "categories/x/tool.md", "tool", repo="https://github.com/o/tool")
            write_page(root, "categories/x/other.md", "other", repo="https://github.com/o/other")
            write_index(root, "categories/x/INDEX.md", [])
            pages = reverse_index.load_pages(root)
            rows = reverse_index.repo_index_rows(root, pages)
            self.assertEqual(
                rows,
                [
                    ["https://github.com/o/other", "other", "x", "categories/x/other.md"],
                    ["https://github.com/o/tool", "tool", "x", "categories/x/tool.md"],
                ],
            )

    def test_full_mislabel_when_every_name_is_indexed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_page(root, "categories/x/foo-bar.md", "foo-bar", repo="https://github.com/o/foo-bar")
            write_index(root, "categories/x/INDEX.md", ["| Foo Bar | 未收录 | stale |"])
            pages = reverse_index.load_pages(root)
            slugs = {page.slug for page in pages if not page.is_index and page.slug}
            mentions = reverse_index.scan_mentions(root, pages, slugs)
            self.assertEqual(len(mentions), 1)
            self.assertTrue(mentions[0].all_indexed)
            self.assertFalse(mentions[0].partly_indexed)

    def test_partial_row_is_not_a_full_mislabel(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_page(root, "categories/x/foo-bar.md", "foo-bar", repo="https://github.com/o/foo-bar")
            write_index(root, "categories/x/INDEX.md", ["| Foo Bar / Baz Qux | 未收录 | mixed |"])
            pages = reverse_index.load_pages(root)
            slugs = {page.slug for page in pages if not page.is_index and page.slug}
            mentions = reverse_index.scan_mentions(root, pages, slugs)
            self.assertEqual(len(mentions), 1)
            self.assertFalse(mentions[0].all_indexed)
            self.assertTrue(mentions[0].partly_indexed)
            self.assertEqual(mentions[0].indexed_hits, ("foo-bar",))

    def test_short_or_unresolvable_names_do_not_count_as_indexed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_page(root, "categories/x/foo-bar.md", "foo-bar", repo="https://github.com/o/foo-bar")
            write_index(root, "categories/x/INDEX.md", ["| Foo Bar / TGI / … | 未收录 | mixed |"])
            pages = reverse_index.load_pages(root)
            slugs = {page.slug for page in pages if not page.is_index and page.slug}
            mentions = reverse_index.scan_mentions(root, pages, slugs)
            self.assertFalse(mentions[0].all_indexed)
            self.assertTrue(mentions[0].partly_indexed)

    def test_rendering_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_page(root, "categories/x/foo-bar.md", "foo-bar", repo="https://github.com/o/foo-bar")
            write_index(root, "categories/x/INDEX.md", ["| Foo Bar | 未收录 | stale |", "| Baz Qux | 未收录 | fresh |"])
            first = reverse_index.compute(root)[2]
            second = reverse_index.compute(root)[2]
            self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
