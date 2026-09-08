#!/usr/bin/env python3
"""Verify every style's token palette against the contrast floor it promises.

`design-tokens/TOKENS-GUIDE.md` rule 4 and `accessibility/ACCESSIBILITY.md`
both state that every text/background token pair used together must pass
WCAG AA. Nothing enforced it, so a style could ship a palette that fails its
own contract — which is how 13-y2k-retrofuturism's 1.1:1 hero headline
reached main.

    python3 scripts/check_contrast.py            # all styles, both themes
    python3 scripts/check_contrast.py 13         # one style
    python3 scripts/check_contrast.py --verbose  # show passing pairs too

Exits non-zero on any unwaived failure.

Dark themes are partial overrides: a token the dark block does not redefine
keeps its light value. The dark palette is therefore resolved as
light-then-dark, not read from the dark block alone — otherwise the pairs
most likely to fail are the ones never checked.
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

TEXT_AA = 4.5      # body text
LARGE_AA = 3.0     # large text, UI component boundaries, focus indicators

# (foreground, background, threshold, label)
#
# Deliberately NOT here: --color-border against bg/surface. WCAG 1.4.11 requires
# 3:1 for boundaries *needed to identify a component*, not for every hairline —
# section dividers and subtle card edges are exempt, and almost every design
# system uses a ~1.2:1 rule for them. Failing all 15 styles on that would get
# this check switched off, which costs more than it buys. Hairlines are reported
# as advisory under --verbose instead. What genuinely must pass 3:1 is the
# focus indicator, and that is checked separately below from --shadow-focus.
PAIRS = [
    ("text", "bg", TEXT_AA, "body text on page"),
    ("text", "surface", TEXT_AA, "body text on surface"),
    ("text-secondary", "bg", TEXT_AA, "secondary text on page"),
    ("text-secondary", "surface", TEXT_AA, "secondary text on surface"),
    ("primary-contrast", "primary", TEXT_AA, "label on primary action"),
    ("accent-contrast", "accent", TEXT_AA, "label on accent"),
]

# Advisory only — never fails the run.
ADVISORY = [
    ("border", "bg", LARGE_AA, "hairline on page"),
    ("border", "surface", LARGE_AA, "hairline on surface"),
]

# A waiver needs a reason, and the reason has to name the trade-off. A style
# that cannot pass a pair says so out loud — it does not silence the check.
# key: (style_slug, theme, fg, bg)
WAIVERS: dict[tuple[str, str, str, str], str] = {}


VAR_RE = re.compile(r"var\(\s*--color-([\w-]+)\s*\)")
LITERAL_RE = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\))")


def focus_color(shadows: dict, palette: dict) -> tuple[str, str] | None:
    """Resolve the color a style's focus ring actually paints.

    Returns (raw_value, resolved_color_string) or None. --shadow-focus is where
    the 3:1 non-text requirement really lands: it is the one boundary a keyboard
    user must be able to see.
    """
    raw = shadows.get("focus")
    if not raw:
        return None
    m = VAR_RE.search(raw)
    if m and m.group(1) in palette:
        return (raw, palette[m.group(1)])
    m = LITERAL_RE.search(raw)
    if m:
        return (raw, m.group(1))
    return None


def parse_color(value: str) -> tuple[float, float, float, float] | None:
    """Return (r, g, b, alpha) in 0-255 / 0-1, or None if not a solid color.

    Gradients, var() references and keywords are skipped rather than guessed at.
    """
    v = value.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        elif len(h) == 4:
            h = "".join(c * 2 for c in h)
        if len(h) == 6:
            return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 1.0)
        if len(h) == 8:
            return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16) / 255)
        return None
    m = re.fullmatch(r"rgba?\(([^)]+)\)", v)
    if m:
        parts = re.split(r"[,\s/]+", m.group(1).strip())
        parts = [p for p in parts if p]
        if len(parts) >= 3:
            try:
                rgb = [float(p.rstrip("%")) * (2.55 if p.endswith("%") else 1) for p in parts[:3]]
            except ValueError:
                return None
            a = 1.0
            if len(parts) >= 4:
                try:
                    a = float(parts[3].rstrip("%")) / (100 if parts[3].endswith("%") else 1)
                except ValueError:
                    a = 1.0
            return (rgb[0], rgb[1], rgb[2], a)
    return None


def composite(fg: tuple[float, float, float, float],
              bg: tuple[float, float, float, float]) -> tuple[float, float, float, float]:
    """Flatten a translucent foreground onto its background before measuring —
    a 60%-opacity label is not the color it was authored as."""
    a = fg[3]
    if a >= 1.0:
        return fg
    return tuple(fg[i] * a + bg[i] * (1 - a) for i in range(3)) + (1.0,)


def luminance(c: tuple[float, float, float, float]) -> float:
    def chan(x: float) -> float:
        x /= 255
        return x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    r, g, b = chan(c[0]), chan(c[1]), chan(c[2])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg: tuple, bg: tuple) -> float:
    fg = composite(fg, bg)
    l1, l2 = luminance(fg), luminance(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    paths = sorted(glob.glob("styles/*/tokens.json"))
    if args:
        paths = [p for p in paths
                 if any(os.path.basename(os.path.dirname(p)).startswith(a) for a in args)]
        if not paths:
            print(f"no style matched {args}", file=sys.stderr)
            return 2

    failures: list[str] = []
    waived: list[str] = []
    skipped: list[str] = []
    checked = 0

    for path in paths:
        slug = os.path.basename(os.path.dirname(path))
        data = json.load(open(path, encoding="utf-8"))
        light = data["light"].get("colors", {})
        # dark blocks are partial overrides — resolve against light
        dark = {**light, **data["dark"].get("colors", {})}

        light_shadows = data["light"].get("shadows", {})
        dark_shadows = {**light_shadows, **data["dark"].get("shadows", {})}

        rows: list[str] = []
        for theme, palette, shadows in (("light", light, light_shadows),
                                        ("dark", dark, dark_shadows)):
            # --- focus indicator: the boundary that must be visible (3:1) ---
            fc = focus_color(shadows, palette)
            if fc:
                raw, resolved = fc
                fg = parse_color(resolved)
                for bg_name in ("bg", "surface"):
                    if bg_name not in palette:
                        continue
                    bg = parse_color(palette[bg_name])
                    if fg is None or bg is None:
                        skipped.append(f"{slug} {theme} focus/{bg_name}: unresolvable ({raw})")
                        continue
                    checked += 1
                    r = ratio(fg, bg)
                    key = (slug, theme, "focus", bg_name)
                    if r >= LARGE_AA:
                        if verbose:
                            rows.append(f"       {theme:<5} {'focus/' + bg_name:<22} {r:5.2f}:1")
                    elif key in WAIVERS:
                        waived.append(f"{slug} · {theme} · focus/{bg_name} {r:.2f}:1 "
                                      f"(needs {LARGE_AA})")
                        rows.append(f"    ~  {theme:<5} {'focus/' + bg_name:<22} "
                                    f"{r:5.2f}:1  WAIVED")
                    else:
                        failures.append(f"{slug} · {theme} · focus ring on {bg_name} "
                                        f"= {r:.2f}:1, needs {LARGE_AA}:1 — keyboard focus "
                                        f"must be visible ({raw})")
                        rows.append(f"    x  {theme:<5} {'focus/' + bg_name:<22} "
                                    f"{r:5.2f}:1  needs {LARGE_AA}")

            # --- advisory hairlines: reported, never failing ---
            if verbose:
                for fg_name, bg_name, floor, label in ADVISORY:
                    if fg_name in palette and bg_name in palette:
                        fg, bg = parse_color(palette[fg_name]), parse_color(palette[bg_name])
                        if fg and bg:
                            rows.append(f"    ·  {theme:<5} "
                                        f"{fg_name + '/' + bg_name:<22} "
                                        f"{ratio(fg, bg):5.2f}:1  advisory ({label})")

            for fg_name, bg_name, floor, label in PAIRS:
                if fg_name not in palette or bg_name not in palette:
                    continue
                fg = parse_color(palette[fg_name])
                bg = parse_color(palette[bg_name])
                if fg is None or bg is None:
                    skipped.append(f"{slug} {theme} {fg_name}/{bg_name}: not a solid color")
                    continue
                checked += 1
                r = ratio(fg, bg)
                ok = r >= floor
                key = (slug, theme, fg_name, bg_name)
                if not ok and key in WAIVERS:
                    waived.append(f"{slug} · {theme} · {fg_name}/{bg_name} "
                                  f"{r:.2f}:1 (needs {floor}) — {label}")
                    rows.append(f"    ~  {theme:<5} {fg_name}/{bg_name:<16} "
                                f"{r:5.2f}:1  WAIVED")
                elif not ok:
                    failures.append(f"{slug} · {theme} · {fg_name} on {bg_name} "
                                    f"= {r:.2f}:1, needs {floor}:1 — {label} "
                                    f"({palette[fg_name]} on {palette[bg_name]})")
                    rows.append(f"    x  {theme:<5} {fg_name}/{bg_name:<16} "
                                f"{r:5.2f}:1  needs {floor}")
                elif verbose:
                    rows.append(f"       {theme:<5} {fg_name}/{bg_name:<16} {r:5.2f}:1")
        if rows:
            print(f"\n{slug}")
            print("\n".join(rows))

    print(f"\ncontrast check — {checked} token pairs across {len(paths)} style(s)")
    if skipped and verbose:
        for s in skipped:
            print(f"  SKIP  {s}")
    for w in waived:
        print(f"  WAIVED  {w}")
    for f in failures:
        print(f"  FAIL    {f}")

    if failures:
        print(f"\n{len(failures)} pair(s) below the floor.")
        print("Fix the token, or — if the style genuinely cannot pass — add a WAIVER "
              "in this script naming the trade-off, and say it in the style's §13.")
        return 1
    print(f"\nAll pairs pass"
          + (f" ({len(waived)} waived, each with a documented reason)" if waived else "")
          + ".")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
