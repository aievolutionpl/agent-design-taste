#!/usr/bin/env python3
"""Structural validation for agent-design-taste.

    python3 scripts/validate.py            # full check (what CI runs)
    python3 scripts/validate.py --budget   # print the context-cost table

Checks:
  1.  every expected style folder exists, with all six required files
  2.  no duplicate or missing style ids
  3.  every style tokens.css defines the required token categories
  4.  generated files (tokens.json, tokens.tailwind.css, styles/index.json,
      design-taste.manifest.json) are in sync with their sources
  5.  every style README follows the canonical 24-section architecture
  6.  every required top-level document exists
  7.  README.md contains its required sections
  8.  every relative markdown link resolves to a real file
  9.  every path named in the manifest resolves
  10. every example.html parses and has no unbalanced tags
  11. no stale `375px` mobile-viewport references
"""
from __future__ import annotations

import glob
import html.parser
import io
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

ERRORS: list[str] = []
WARNINGS: list[str] = []
CHECKS = 0


def check(ok: bool, msg: str, warn: bool = False) -> bool:
    global CHECKS
    CHECKS += 1
    if not ok:
        (WARNINGS if warn else ERRORS).append(msg)
    return ok


STYLE_FILES = ["README.md", "tokens.css", "tokens.json", "tokens.tailwind.css",
               "prompts.md", "example.html"]

REQUIRED_TOKEN_CATEGORIES = {"colors", "fonts", "fontSizes", "spacing", "radius",
                             "shadows", "borders", "container", "motion", "motionEase"}

CANONICAL_SECTIONS = [
    "01 · Overview", "02 · Design philosophy", "03 · Visual principles",
    "04 · Typography", "05 · Layout & grid", "06 · Visual hierarchy",
    "07 · Color system", "08 · Components", "09 · Shape language",
    "10 · Imagery & visual direction", "11 · Motion", "12 · Responsive behaviour",
    "13 · Accessibility", "14 · When to use", "15 · When NOT to use",
    "16 · Do", "17 · Don't", "18 · Anti-slop", "19 · Style combinations",
    "20 · Signature move", "21 · When to break the rules", "22 · Example prompts",
    "23 · Design tokens", "24 · Example implementation",
]

REQUIRED_DOCS = [
    "README.md", "README.pl.md", "SKILL.md", "AGENT-BOOTSTRAP.md", "AGENTS.md",
    "CLAUDE.md", "DECISION-MATRIX.md", "ANTI-SLOP.md", "LAYOUT-PATTERNS.md",
    "STYLE-COMBINATIONS.md", "CONTRIBUTING.md", "CHANGELOG.md", "LICENSE",
    "design-taste.manifest.json", "styles/index.json",
    "docs/PRECEDENCE.md", "docs/CONTEXT-PROFILES.md", "docs/INTEGRATIONS.md",
    "docs/EXAMPLE-WORKFLOW.md", "docs/STYLE-TEMPLATE.md",
    "accessibility/ACCESSIBILITY.md", "responsive/RESPONSIVE-FOUNDATIONS.md",
    "typography/TYPOGRAPHY-FOUNDATIONS.md",
    "visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md",
    "motion/MOTION-FOUNDATIONS.md", "component-patterns/COMPONENT-PATTERNS.md",
    "layout-patterns/LAYOUT-FOUNDATIONS.md", "design-tokens/TOKENS-GUIDE.md",
    "evaluation/DESIGN-TASTE-SCORE.md", "evaluation/RENDERED-VERIFICATION.md",
    "evaluation/MODE-ROUTING.md", "evaluation/TASTE-LOOP.md",
    "prompts/DESIGN-CONTRACT.md", "prompts/PROMPT-LIBRARY.md",
    "adapters/AGENTS.md", "adapters/CLAUDE.md", "adapters/GEMINI.md",
    "adapters/cursor/agent-design-taste.mdc",
    "adapters/windsurf/agent-design-taste.md",
    "adapters/copilot/copilot-instructions.md",
    "scripts/gen_tokens.py", "scripts/gen_manifest.py", "scripts/install.sh",
    "scripts/screenshot.mjs", ".github/workflows/validate.yml", ".gitignore",
]

README_SECTIONS = [
    "For AI agents", "Install", "The 15 styles", "The workflow", "Why this exists",
]

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


class TagBalance(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, int]] = []
        self.problems: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                unclosed = self.stack[i + 1:]
                if unclosed:
                    self.problems.append(
                        f"</{tag}> at line {self.getpos()[0]} closes over unclosed "
                        + ", ".join(f"<{t}> (line {ln})" for t, ln in unclosed))
                del self.stack[i:]
                return
        self.problems.append(f"stray </{tag}> at line {self.getpos()[0]}")


def style_dirs() -> list[str]:
    return sorted(d for d in glob.glob("styles/*") if os.path.isdir(d))


def c1_style_folders(index):
    dirs = style_dirs()
    check(len(dirs) == 15, f"expected 15 style folders, found {len(dirs)}")
    slugs = {os.path.basename(d) for d in dirs}
    for entry in index["styles"]:
        check(entry["slug"] in slugs, f"index.json lists missing style folder: {entry['slug']}")
    for d in dirs:
        slug = os.path.basename(d)
        check(re.fullmatch(r"\d{2}-[a-z0-9-]+", slug) is not None,
              f"{slug}: folder name must be NN-kebab-case")
        for f in STYLE_FILES:
            check(os.path.exists(os.path.join(d, f)), f"{slug}: missing {f}")


def c2_ids(index):
    ids = [e["id"] for e in index["styles"]]
    dupes = {i for i in ids if ids.count(i) > 1}
    check(not dupes, f"duplicate style ids: {sorted(dupes)}")
    folder_ids = [os.path.basename(d).split("-")[0] for d in style_dirs()]
    check(sorted(ids) == sorted(folder_ids),
          f"index ids {sorted(ids)} do not match folder ids {sorted(folder_ids)}")
    all_aliases: dict[str, str] = {}
    for e in index["styles"]:
        for a in e["aliases"]:
            check(a not in all_aliases,
                  f"alias '{a}' claimed by both {all_aliases.get(a)} and {e['slug']}")
            all_aliases[a] = e["slug"]


def c3_token_categories():
    for d in style_dirs():
        slug = os.path.basename(d)
        p = os.path.join(d, "tokens.json")
        if not os.path.exists(p):
            continue
        light = json.load(open(p, encoding="utf-8")).get("light", {})
        missing = REQUIRED_TOKEN_CATEGORIES - set(light)
        check(not missing, f"{slug}: tokens.css missing categories {sorted(missing)}")
        shadows = light.get("shadows", {})
        check("focus" in shadows, f"{slug}: no --shadow-focus token (accessibility requirement)")


def c4_generated_in_sync():
    """Regenerate into a scratch copy of the repo and diff."""
    for script, outputs in (
        ("scripts/gen_tokens.py", [p for d in style_dirs()
                                   for p in (f"{d}/tokens.json", f"{d}/tokens.tailwind.css")]),
        ("scripts/gen_manifest.py", ["styles/index.json", "design-taste.manifest.json"]),
    ):
        before = {p: open(p, "rb").read() for p in outputs if os.path.exists(p)}
        r = subprocess.run([sys.executable, script], capture_output=True, text=True)
        if not check(r.returncode == 0, f"{script} failed: {r.stderr.strip()[:200]}"):
            continue
        stale = [p for p, data in before.items() if open(p, "rb").read() != data]
        check(not stale,
              f"generated files out of date — run `python3 {script}`: {stale[:4]}")


def c5_style_sections():
    for d in style_dirs():
        slug = os.path.basename(d)
        p = os.path.join(d, "README.md")
        if not os.path.exists(p):
            continue
        heads = [l[3:].strip() for l in open(p, encoding="utf-8") if l.startswith("## ")]
        check(len(heads) == 24, f"{slug}: expected 24 sections, found {len(heads)}")
        for i, want in enumerate(CANONICAL_SECTIONS):
            got = heads[i] if i < len(heads) else "<missing>"
            check(got.startswith(want), f"{slug}: section {i+1} is '{got}', expected '{want}…'")


def c6_required_docs():
    for p in REQUIRED_DOCS:
        check(os.path.exists(p), f"missing required file: {p}")


def c7_readme_sections():
    if not os.path.exists("README.md"):
        return
    text = open("README.md", encoding="utf-8").read().lower()
    for s in README_SECTIONS:
        check(s.lower() in text, f"README.md is missing a section about: {s}")


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})", re.M)


def strip_fences(text: str) -> str:
    """Remove fenced code blocks so template/example content is not link-checked."""
    out, fence = [], None
    for line in text.split("\n"):
        m = FENCE_RE.match(line)
        if m:
            marker = m.group(1)
            if fence is None:
                fence = marker[0] * len(marker)
            elif line.strip().startswith(fence):
                fence = None
            continue
        if fence is None:
            out.append(line)
    return "\n".join(out)


SKIP_DIRS = ("node_modules", ".git", "screenshots", "__pycache__", "dist", "build")


def skipped(path: str) -> bool:
    return any(part in SKIP_DIRS for part in path.split(os.sep))


def c8_links():
    for md in sorted(glob.glob("**/*.md", recursive=True)):
        if skipped(md):
            continue
        base = os.path.dirname(md)
        for raw in LINK_RE.findall(strip_fences(open(md, encoding="utf-8").read())):
            link = raw.split(" ")[0].strip()
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = os.path.normpath(os.path.join(base, link.split("#")[0]))
            if not target:
                continue
            check(os.path.exists(target), f"{md}: broken link → {link}")


def c9_manifest_paths(manifest):
    for group in ("entrypoints", "files", "adapters", "scripts"):
        for key, path in manifest.get(group, {}).items():
            check(os.path.exists(path), f"manifest.{group}.{key} → missing path: {path}")
    for s in manifest["styles"]:
        check(os.path.isdir(s["path"]), f"manifest style {s['id']} → missing dir: {s['path']}")


def c10_examples_parse():
    for p in sorted(glob.glob("styles/*/example.html")):
        raw = open(p, encoding="utf-8").read()
        parser = TagBalance()
        try:
            parser.feed(raw)
            parser.close()
        except Exception as exc:                       # pragma: no cover
            check(False, f"{p}: HTML parse error: {exc}")
            continue
        check(not parser.problems, f"{p}: {parser.problems[0] if parser.problems else ''}")
        check(not parser.stack,
              f"{p}: unclosed tags: {[t for t, _ in parser.stack][:4]}")
        check("<title>" in raw, f"{p}: no <title>")
        check("viewport" in raw, f"{p}: no viewport meta tag")
        check("prefers-reduced-motion" in raw or "@keyframes" not in raw,
              f"{p}: has animation but no prefers-reduced-motion block")


def c11_no_stale_viewport():
    for md in sorted(glob.glob("**/*.md", recursive=True)):
        if skipped(md) or md == "CHANGELOG.md":
            continue
        for n, line in enumerate(open(md, encoding="utf-8"), 1):
            if re.search(r"\b375\s*px\b|\b375\b(?=\s*(?:/|·|,))", line) \
                    and "360" not in line and "390" not in line:
                check(False, f"{md}:{n}: stale 375px reference — canonical mobile is 390px",
                      warn=True)


def budget():
    print(f"{'file':<52}{'~tokens':>9}")
    print("-" * 61)
    groups = [
        ("entry", ["AGENT-BOOTSTRAP.md", "SKILL.md"]),
        ("decide", ["DECISION-MATRIX.md", "STYLE-COMBINATIONS.md", "docs/PRECEDENCE.md"]),
        ("build", ["LAYOUT-PATTERNS.md", "component-patterns/COMPONENT-PATTERNS.md",
                   "typography/TYPOGRAPHY-FOUNDATIONS.md",
                   "visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md",
                   "motion/MOTION-FOUNDATIONS.md",
                   "responsive/RESPONSIVE-FOUNDATIONS.md",
                   "accessibility/ACCESSIBILITY.md"]),
        ("audit", ["ANTI-SLOP.md", "evaluation/DESIGN-TASTE-SCORE.md",
                   "evaluation/RENDERED-VERIFICATION.md"]),
    ]
    for name, files in groups:
        total = 0
        for f in files:
            if os.path.exists(f):
                t = round(len(open(f, encoding="utf-8").read()) / 4)
                total += t
                print(f"  {f:<50}{t:>9,}")
        print(f"  {'— ' + name + ' subtotal':<50}{total:>9,}\n")
    dna = [round(len(open(p, encoding="utf-8").read()) / 4)
           for p in glob.glob("styles/*/README.md")]
    tok = [round(len(open(p, encoding="utf-8").read()) / 4)
           for p in glob.glob("styles/*/tokens.css")]
    print(f"  {'one style DNA (avg)':<50}{round(sum(dna)/len(dna)):>9,}")
    print(f"  {'one style tokens.css (avg)':<50}{round(sum(tok)/len(tok)):>9,}")
    print(f"  {'ALL 15 style DNAs — never load this':<50}{sum(dna):>9,}")
    total = sum(round(len(open(p, encoding='utf-8').read()) / 4)
                for p in glob.glob('**/*.md', recursive=True) if not skipped(p))
    print(f"\n  {'whole repository (markdown)':<50}{total:>9,}")


def main() -> int:
    if "--budget" in sys.argv:
        budget()
        return 0

    for p in ("styles/index.json", "design-taste.manifest.json"):
        if not os.path.exists(p):
            print(f"FATAL: {p} missing — run `python3 scripts/gen_manifest.py`")
            return 1
    index = json.load(open("styles/index.json", encoding="utf-8"))
    manifest = json.load(open("design-taste.manifest.json", encoding="utf-8"))

    c1_style_folders(index)
    c2_ids(index)
    c3_token_categories()
    c4_generated_in_sync()
    c5_style_sections()
    c6_required_docs()
    c7_readme_sections()
    c8_links()
    c9_manifest_paths(manifest)
    c10_examples_parse()
    c11_no_stale_viewport()

    check(manifest["skillVersion"] in open("SKILL.md", encoding="utf-8").read(),
          "SKILL.md frontmatter version does not match manifest skillVersion")

    print(f"agent-design-taste validation — {CHECKS} checks")
    for w in WARNINGS:
        print(f"  WARN  {w}")
    for e in ERRORS:
        print(f"  FAIL  {e}")
    if ERRORS:
        print(f"\n{len(ERRORS)} error(s), {len(WARNINGS)} warning(s)")
        return 1
    print(f"\nAll {CHECKS} checks passed"
          + (f" ({len(WARNINGS)} warning(s))" if WARNINGS else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
