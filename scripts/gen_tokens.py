#!/usr/bin/env python3
"""Generate tokens.json + tokens.tailwind.css from each style's tokens.css.

tokens.css is the single source of truth. Run this after editing any tokens.css:

    python3 scripts/gen_tokens.py

Tailwind v4 output maps our categories onto Tailwind's theme namespaces so the
variables actually generate utilities:

    --color-*   -> bg-*, text-*, border-*
    --font-*    -> font-*
    --text-*    -> text-* (font sizes)
    --spacing-* -> p-*, m-*, gap-*
    --radius-*  -> rounded-*
    --shadow-*  -> shadow-*
    --ease-*    -> ease-*
    --container-* -> max-w-*

Motion durations and border shorthands have no Tailwind namespace, so they are
emitted as plain custom properties in a :root block below the @theme block.
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CSS prefix -> (json category, tailwind namespace or None)
CATEGORIES = [
    ("--color-", "colors", "color"),
    ("--font-size-", "fontSizes", "text"),
    ("--font-", "fonts", "font"),
    ("--spacing-", "spacing", "spacing"),
    ("--radius-", "radius", "radius"),
    ("--shadow-", "shadows", "shadow"),
    ("--border-", "borders", None),
    ("--motion-ease", "motionEase", "ease"),
    ("--motion-", "motion", None),
    ("--container-", "container", "container"),
]


def strip_at_rules(css: str) -> str:
    """Drop @media/@supports blocks before parsing.

    A `:root` nested inside `@media (prefers-reduced-motion: reduce)` is not the
    light palette — it applies only to that media condition. Merging it in made
    a misplaced token look correct in the generated JSON while behaving
    differently in a browser, so the palette is read from top-level rules only.
    """
    out, i = [], 0
    pat = re.compile(r"@[a-zA-Z-]+[^{]*\{")
    while True:
        m = pat.search(css, i)
        if not m:
            out.append(css[i:])
            break
        out.append(css[i:m.start()])
        depth, j = 1, m.end()
        while j < len(css) and depth:
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
            j += 1
        i = j
    return "".join(out)


def parse_tokens(css_path: str) -> dict[str, dict[str, str]]:
    text = strip_at_rules(open(css_path, encoding="utf-8").read())
    blocks = re.findall(r'(:root|\[data-theme="dark"\])\s*\{([^}]+)\}', text)
    out: dict[str, dict[str, str]] = {}
    for name, body in blocks:
        theme = "light" if name == ":root" else "dark"
        toks = out.setdefault(theme, {})
        for k, v in re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", body):
            toks[k] = v.strip()
    return out


def categorize(tokens: dict[str, str]) -> dict:
    cats: dict[str, dict[str, str]] = {}
    for key, value in tokens.items():
        for prefix, cat, _ns in CATEGORIES:
            if key.startswith(prefix):
                name = key[len(prefix):].lstrip("-") or "default"
                cats.setdefault(cat, {})[name] = value
                break
    return cats


def tailwind(cats: dict) -> str:
    lines = ['@import "tailwindcss";', "", "@theme {"]
    for _prefix, cat, ns in CATEGORIES:
        if ns is None:
            continue
        entries = cats.get(cat) or {}
        if not entries:
            continue
        lines.append(f"  /* {cat} */")
        for name, value in entries.items():
            lines.append(f"  --{ns}-{name}: {value};")
    lines.append("}")

    extras = []
    for cat in ("motion", "borders"):
        for name, value in (cats.get(cat) or {}).items():
            prefix = "motion" if cat == "motion" else "border"
            extras.append(f"  --{prefix}-{name}: {value};")
    if extras:
        lines += ["", "/* No Tailwind namespace — use via var() */", ":root {", *extras, "}"]
    return "\n".join(lines) + "\n"


def main() -> int:
    paths = sorted(glob.glob(os.path.join(ROOT, "styles", "*", "tokens.css")))
    if not paths:
        print("no tokens.css found", file=sys.stderr)
        return 1
    for css in paths:
        style_dir = os.path.dirname(css)
        themes = parse_tokens(css)
        data = {
            "name": os.path.basename(style_dir),
            "source": "tokens.css",
            "light": categorize(themes.get("light", {})),
            "dark": categorize(themes.get("dark", {})),
        }
        with open(os.path.join(style_dir, "tokens.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        with open(os.path.join(style_dir, "tokens.tailwind.css"), "w", encoding="utf-8") as f:
            f.write(f"/* {os.path.basename(style_dir)} — generated from tokens.css. Do not edit by hand. */\n")
            f.write(tailwind(data["light"]))
        print("ok", os.path.relpath(style_dir, ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
