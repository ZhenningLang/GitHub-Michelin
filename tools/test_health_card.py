#!/usr/bin/env python3
"""Card rendering: the unscored states must stay visually distinguishable.

The SVG is what a reader actually looks at. If `?` and `N/A` render identically there,
splitting them in the data model bought nothing.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import health_card as hc

AXES = ["maintenance", "responsiveness", "adoption", "longevity", "governance", "risk_license"]


def render(grades, overall="B", scored="4", applicable=None, lang="en"):
    return hc.render(lang, "Demo", grades, overall, "", ["MIT"], scored, applicable)


class UnscoredStatesTest(unittest.TestCase):
    def test_unknown_and_not_applicable_use_different_ink(self) -> None:
        both = render(["A", "B", "N/A", "C", "?", "A"], scored="4", applicable="5")
        self.assertIn(hc.TIER["?"][1], both)       # the dashed-ghost gray
        self.assertIn(hc.TIER["N/A"][1], both)     # the flat dim gray
        self.assertNotEqual(hc.TIER["?"][1], hc.TIER["N/A"][1])

    def test_not_applicable_marker_is_a_square_not_a_dashed_circle(self) -> None:
        na = render(["A", "B", "N/A", "C", "D", "A"], scored="5", applicable="5")
        unknown = render(["A", "B", "?", "C", "D", "A"], scored="5", applicable="6")
        self.assertIn("<rect", na)
        self.assertIn('stroke-dasharray="2 2"', unknown)
        self.assertNotIn('stroke-dasharray="2 2"', na)

    def test_denominator_reflects_applicable_axes(self) -> None:
        self.assertIn("4/5", render(["A", "B", "N/A", "C", "?", "A"], scored="4", applicable="5"))
        self.assertIn("5/6", render(["A", "B", "?", "C", "D", "A"], scored="5", applicable="6"))

    def test_denominator_defaults_to_counting_applicable_axes(self) -> None:
        # Older blocks carry no applicable_axes; the card must still not print "/6" for a
        # page whose axis does not apply.
        self.assertIn("5/5", render(["A", "B", "N/A", "C", "D", "A"], scored="5"))

    def test_na_label_is_escaped_and_present(self) -> None:
        svg = render(["N/A", "B", "C", "D", "E", "A"], scored="5", applicable="5")
        self.assertIn("N/A", svg)
        self.assertTrue(svg.strip().endswith("</svg>"))

    def test_every_grade_renders_in_both_languages(self) -> None:
        for lang in ("en", "zh"):
            for g in ["A", "B", "C", "D", "E", "?", "N/A"]:
                with self.subTest(lang=lang, grade=g):
                    svg = render([g] * 6, overall=g, scored="6", applicable="6", lang=lang)
                    self.assertTrue(svg.startswith("<svg"))
                    self.assertTrue(svg.strip().endswith("</svg>"))


if __name__ == "__main__":
    unittest.main()
