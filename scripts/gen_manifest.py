#!/usr/bin/env python3
"""Generate styles/index.json and design-taste.manifest.json.

Routing metadata lives here so the two JSON files cannot drift apart or from
the filesystem. Regenerate after adding a style:

    python3 scripts/gen_manifest.py
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_VERSION = "2.0.0"
REPO_VERSION = "2.0.0"

# slug: (name, identity, aliases, densities, recommendedFor, supporting, incompatible, vetoedBy, scoring)
STYLES = {
"01-minimalism": (
  "Minimalism", "Less, but better.",
  ["minimal", "minimalist", "clean", "less-is-more", "rams", "swiss-lite"],
  ["low", "medium"],
  ["b2b-saas", "fintech", "health", "corporate", "enterprise", "premium", "developer-docs"],
  ["10", "15", "08", "14"], ["13"], [],
  {"trust:critical": 3, "personality:premium": 3, "audience:professional": 2, "emotion:calm": 2,
   "a11y:elevated": 2, "density:medium": 1, "device:mobile-first": 1,
   "emotion:excitement": -2, "personality:playful": -2, "audience:child-family": -3}),
"02-glassmorphism": (
  "Glassmorphism", "Translucent. Layered. Modern.",
  ["glass", "frosted", "frosted-glass", "blur", "acrylic"],
  ["low", "medium"],
  ["dev-tools", "dashboards", "web3", "consumer-app"],
  ["04"], ["12", "11"], ["a11y:elevated"],
  {"personality:futuristic": 3, "audience:technical": 2, "device:desktop-first": 2,
   "density:medium": 1, "emotion:curiosity": 1,
   "a11y:elevated": -2, "trust:critical": -3, "density:high": -3}),
"03-liquid-glass": (
  "Liquid Glass", "Fluid light and motion.",
  ["liquid", "fluid-glass", "refraction", "spatial-glass"],
  ["low", "medium"],
  ["consumer-app", "creative-tools", "mobile-app", "media"],
  ["04"], ["11", "10"], [],
  {"audience:consumer": 3, "personality:futuristic": 3, "emotion:excitement": 2,
   "device:mobile-first": 2, "session:glance": 1,
   "density:high": -2, "complexity:dense-relational": -3, "trust:critical": -2}),
"04-bento-grid": (
  "Bento Grid", "Modular, organised blocks.",
  ["bento", "grid-tiles", "modular", "tiles", "dashboard-grid"],
  ["medium", "high"],
  ["feature-rich-products", "landing-pages", "ecommerce", "dev-tools", "analytics"],
  ["02", "05", "03"], ["06", "11"], [],
  {"density:high": 3, "complexity:layered": 3, "conversion:consider": 2,
   "audience:consumer": 2, "personality:precise": 2, "device:mixed": 1,
   "personality:literary": -2, "session:dwell": -2}),
"05-neo-brutalism": (
  "Neo-Brutalism", "Bold, raw, unconventional.",
  ["neubrutalism", "neo-brutalist", "hard-shadow", "bold-borders"],
  ["low", "medium"],
  ["youth-brands", "creator-tools", "creative-studios", "gen-z-apps"],
  ["04"], ["08", "07"], ["audience:child-family"],
  {"personality:bold": 3, "emotion:excitement": 3, "audience:creative": 2,
   "conversion:convert-now": 2, "session:glance": 1,
   "trust:critical": -2, "audience:child-family": -3, "a11y:elevated": -2}),
"06-brutalist-anti-grid": (
  "Brutalist / Anti-Grid", "Break the grid on purpose.",
  ["brutalist", "anti-grid", "raw", "web-brutalism", "deconstructed"],
  ["low"],
  ["portfolios", "agencies", "art-culture", "experimental"],
  ["11", "15"], ["08", "07", "04"],
  ["trust:critical", "a11y:elevated", "density:high", "audience:child-family", "device:mobile-first"],
  {"audience:creative": 3, "personality:bold": 3, "emotion:curiosity": 2,
   "density:low": 2, "device:desktop-first": 1,
   "density:high": -3, "trust:critical": -3, "a11y:elevated": -3, "device:mobile-first": -2}),
"07-neumorphism": (
  "Neumorphism (Soft UI)", "Soft extruded surfaces.",
  ["soft-ui", "neumorphic", "extruded", "soft-shadow"],
  ["low"],
  ["decorative-marketing-surfaces", "iot-companion-apps", "ambience-widgets"],
  ["01"], ["05", "06", "10", "12"],
  ["trust:critical", "a11y:elevated", "density:high", "complexity:dense-relational"],
  {"personality:premium": 2, "density:low": 1, "audience:consumer": 1,
   "a11y:elevated": -3, "density:high": -3, "trust:critical": -3, "device:mobile-first": -2}),
"08-claymorphism": (
  "Claymorphism", "Playful puffy 3D.",
  ["clay", "claymorphic", "puffy", "soft-3d"],
  ["low", "medium"],
  ["kids", "education", "wellness", "friendly-consumer-apps"],
  ["01", "12"], ["05", "06", "10"],
  ["density:high", "complexity:dense-relational"],
  {"audience:child-family": 3, "personality:playful": 3, "emotion:safety": 3,
   "audience:consumer": 2, "conversion:browse": 1,
   "density:high": -3, "audience:technical": -3, "trust:critical": -2}),
"09-skeuomorphism-tactile": (
  "Skeuomorphism / Tactile", "Looks like the real thing.",
  ["skeuomorphic", "tactile", "realistic", "material-mimicry", "instrument-ui"],
  ["medium", "high"],
  ["audio-tools", "finance-instruments", "retro-tools", "hardware-companions"],
  ["10"], ["02", "08"], ["audience:child-family"],
  {"complexity:dense-relational": 3, "personality:premium": 2, "emotion:competence": 2,
   "device:desktop-first": 2, "session:dwell": 1,
   "device:mobile-first": -2, "audience:child-family": -2, "conversion:convert-now": -1}),
"10-swiss-international": (
  "Swiss / International", "Grid, type, order.",
  ["swiss", "international", "international-typographic-style", "grid", "helvetica", "brockmann"],
  ["medium", "high"],
  ["dev-tools", "ai-platforms", "agencies", "architecture", "editorial", "corporate", "analytics", "developer-docs"],
  ["01", "09", "04"], ["13", "12"], [],
  {"density:high": 3, "personality:precise": 3, "complexity:dense-relational": 3,
   "audience:technical": 2, "trust:critical": 2, "emotion:competence": 2, "session:dwell": 1,
   "personality:playful": -2, "emotion:excitement": -2, "audience:child-family": -2}),
"11-editorial-magazine": (
  "Editorial / Magazine", "Reads like a magazine.",
  ["editorial", "magazine", "print", "long-form", "publication"],
  ["medium", "high"],
  ["media", "blogs", "long-form", "luxury", "restaurants", "culture"],
  ["06", "10"], ["02", "04"], [],
  {"personality:literary": 3, "session:dwell": 3, "complexity:layered": 3,
   "personality:premium": 2, "emotion:trust": 2, "conversion:browse": 1,
   "complexity:dense-relational": -2, "conversion:convert-now": -2, "audience:technical": -1}),
"12-maximalism": (
  "Maximalism", "More is more.",
  ["maximalist", "layered", "dense-decoration", "more-is-more"],
  ["high"],
  ["fashion", "events", "culture", "music", "campaigns"],
  ["13", "08"], ["02", "01", "10"],
  ["trust:critical", "a11y:elevated", "session:dwell"],
  {"personality:bold": 3, "emotion:excitement": 3, "audience:creative": 2,
   "session:glance": 2, "conversion:browse": 1,
   "trust:critical": -3, "a11y:elevated": -3, "session:dwell": -3, "density:high": -2}),
"13-y2k-retrofuturism": (
  "Y2K / Retrofuturism", "Chrome, bubble, optimism.",
  ["y2k", "retrofuturism", "chrome", "retro", "2000s", "frutiger"],
  ["medium", "high"],
  ["music", "streetwear", "gaming", "events", "drops"],
  ["12"], ["01", "10"],
  ["trust:critical", "session:dwell"],
  {"personality:nostalgic": 3, "emotion:excitement": 3, "audience:consumer": 2,
   "session:glance": 2, "conversion:convert-now": 1,
   "trust:critical": -3, "audience:professional": -3, "a11y:elevated": -2}),
"14-3d-spatial-ui": (
  "3D / Spatial UI", "Depth you can move through.",
  ["3d", "spatial", "depth", "webgl", "immersive", "z-space"],
  ["low", "medium"],
  ["web3", "product-launches", "immersive-tools", "hardware"],
  ["01", "02"], ["11", "10"],
  ["device:mobile-first"],
  {"personality:futuristic": 3, "emotion:curiosity": 3, "audience:creative": 2,
   "device:desktop-first": 2, "session:glance": 1,
   "device:mobile-first": -3, "density:high": -3, "a11y:elevated": -2}),
"15-expressive-kinetic-typography": (
  "Expressive / Kinetic Typography", "Type as the interface.",
  ["kinetic", "kinetic-typography", "expressive-type", "variable-type", "type-first"],
  ["low"],
  ["portfolios", "campaigns", "motion-first-brands", "agencies"],
  ["01", "06"], ["04"],
  ["a11y:elevated", "density:high", "complexity:dense-relational", "session:dwell"],
  {"audience:creative": 3, "personality:bold": 3, "emotion:curiosity": 2,
   "density:low": 2, "session:glance": 2,
   "complexity:dense-relational": -3, "a11y:elevated": -3, "session:dwell": -2}),
}

STYLE_FILES = ["README.md", "tokens.css", "tokens.json", "tokens.tailwind.css", "prompts.md", "example.html"]


def build_index():
    entries = []
    for slug, (name, identity, aliases, density, rec, support, incompat, vetoed, scoring) in STYLES.items():
        sid = slug.split("-")[0]
        path = f"styles/{slug}"
        missing = [f for f in STYLE_FILES if not os.path.exists(os.path.join(ROOT, path, f))]
        if missing:
            print(f"WARNING {slug}: missing {missing}", file=sys.stderr)
        entries.append({
            "id": sid,
            "slug": slug,
            "name": name,
            "identity": identity,
            "aliases": aliases,
            "path": path,
            "files": {
                "dna": f"{path}/README.md",
                "tokensCss": f"{path}/tokens.css",
                "tokensJson": f"{path}/tokens.json",
                "tokensTailwind": f"{path}/tokens.tailwind.css",
                "prompts": f"{path}/prompts.md",
                "example": f"{path}/example.html",
            },
            "densityFit": list(density),
            "recommendedFor": list(rec),
            "supportingStyles": list(support),
            "incompatibleWith": list(incompat),
            "vetoedBy": list(vetoed),
            "scoring": scoring,
        })
    entries.sort(key=lambda e: e["id"])
    return {
        "$comment": "Machine-readable style routing index. Generated by scripts/gen_manifest.py — do not edit by hand.",
        "version": REPO_VERSION,
        "count": len(entries),
        "signals": {
            "density": ["low", "medium", "high"],
            "audience": ["technical", "professional", "consumer", "creative", "child-family", "mixed-public"],
            "personality": ["precise", "bold", "warm", "premium", "playful", "nostalgic", "futuristic", "literary"],
            "trust": ["low", "medium", "critical"],
            "a11y": ["standard", "elevated"],
            "conversion": ["browse", "consider", "convert-now"],
            "complexity": ["simple", "layered", "dense-relational"],
            "device": ["desktop-first", "mobile-first", "mixed"],
            "session": ["glance", "task", "dwell"],
            "emotion": ["trust", "competence", "calm", "excitement", "status", "safety", "curiosity"],
        },
        "usage": {
            "algorithm": "1) drop every style whose vetoedBy contains a signal present in the brief; 2) sum scoring[signal] over all brief signals for each survivor; 3) highest total wins; 4) ties resolved by DECISION-MATRIX.md Part 5.",
            "rule": "Load exactly one dominant style DNA. A supporting style, if used, must come from that style's supportingStyles list.",
            "reference": "DECISION-MATRIX.md",
        },
        "defaultStyle": "01",
        "styles": entries,
    }


def build_manifest(index):
    return {
        "$comment": "Machine-readable repository manifest. Generated by scripts/gen_manifest.py — do not edit by hand.",
        "name": "agent-design-taste",
        "title": "Agent Design Taste",
        "tagline": "Design Intelligence for AI Agents",
        "repositoryVersion": REPO_VERSION,
        "skillVersion": SKILL_VERSION,
        "license": "MIT",
        "repository": "https://github.com/aievolutionpl/agent-design-taste",
        "entrypoints": {
            "agent": "AGENT-BOOTSTRAP.md",
            "skill": "SKILL.md",
            "human": "README.md",
            "humanPl": "README.pl.md",
            "styleIndex": "styles/index.json",
        },
        "workflow": [
            "understand", "choose-style", "typography", "layout", "tokens",
            "build", "render", "audit", "remove-slop", "polish",
        ],
        "precedence": [
            "brand-and-legal", "accessibility-floor", "product-needs",
            "style-dna", "repository-tokens", "agent-preference",
        ],
        "canonicalViewports": {
            "desktop": 1440, "tablet": 768, "mobile": 390, "narrowFloor": 360,
            "primaryVerification": 390,
        },
        "contextProfiles": {
            "light": {
                "use": "one component, one section, a copy or spacing fix",
                "load": ["ANTI-SLOP.md", "docs/PRECEDENCE.md", "component-patterns/COMPONENT-PATTERNS.md"],
                "approxTokens": 3000,
            },
            "standard": {
                "use": "a page: landing, pricing, marketing site, feature area",
                "load": ["SKILL.md", "DECISION-MATRIX.md", "styles/<chosen>/README.md",
                         "styles/<chosen>/tokens.css", "ANTI-SLOP.md", "LAYOUT-PATTERNS.md"],
                "approxTokens": 8000,
            },
            "full": {
                "use": "a whole product, a new identity, or a design system",
                "load": ["<standard>", "STYLE-COMBINATIONS.md", "styles/<supporting>/README.md",
                         "typography/TYPOGRAPHY-FOUNDATIONS.md",
                         "visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md",
                         "motion/MOTION-FOUNDATIONS.md",
                         "component-patterns/COMPONENT-PATTERNS.md",
                         "responsive/RESPONSIVE-FOUNDATIONS.md",
                         "accessibility/ACCESSIBILITY.md",
                         "design-tokens/TOKENS-GUIDE.md",
                         "evaluation/DESIGN-TASTE-SCORE.md",
                         "prompts/DESIGN-CONTRACT.md"],
                "approxTokens": 25000,
            },
            "neverLoad": ["all 15 style folders", "every example.html"],
        },
        "files": {
            "bootstrap": "AGENT-BOOTSTRAP.md",
            "skill": "SKILL.md",
            "decisionMatrix": "DECISION-MATRIX.md",
            "styleCombinations": "STYLE-COMBINATIONS.md",
            "layoutPatterns": "LAYOUT-PATTERNS.md",
            "antiSlop": "ANTI-SLOP.md",
            "precedence": "docs/PRECEDENCE.md",
            "contextProfiles": "docs/CONTEXT-PROFILES.md",
            "integrations": "docs/INTEGRATIONS.md",
            "exampleWorkflow": "docs/EXAMPLE-WORKFLOW.md",
            "styleTemplate": "docs/STYLE-TEMPLATE.md",
            "accessibility": "accessibility/ACCESSIBILITY.md",
            "responsive": "responsive/RESPONSIVE-FOUNDATIONS.md",
            "typography": "typography/TYPOGRAPHY-FOUNDATIONS.md",
            "visualLanguage": "visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md",
            "motion": "motion/MOTION-FOUNDATIONS.md",
            "components": "component-patterns/COMPONENT-PATTERNS.md",
            "layoutFoundations": "layout-patterns/LAYOUT-FOUNDATIONS.md",
            "tokensGuide": "design-tokens/TOKENS-GUIDE.md",
            "score": "evaluation/DESIGN-TASTE-SCORE.md",
            "renderedVerification": "evaluation/RENDERED-VERIFICATION.md",
            "modeRouting": "evaluation/MODE-ROUTING.md",
            "tasteLoop": "evaluation/TASTE-LOOP.md",
            "designContract": "prompts/DESIGN-CONTRACT.md",
            "promptLibrary": "prompts/PROMPT-LIBRARY.md",
        },
        "adapters": {
            "agents": "adapters/AGENTS.md",
            "claude": "adapters/CLAUDE.md",
            "gemini": "adapters/GEMINI.md",
            "cursor": "adapters/cursor/agent-design-taste.mdc",
            "windsurf": "adapters/windsurf/agent-design-taste.md",
            "copilot": "adapters/copilot/copilot-instructions.md",
        },
        "scripts": {
            "generateTokens": "scripts/gen_tokens.py",
            "generateManifest": "scripts/gen_manifest.py",
            "validate": "scripts/validate.py",
            "screenshot": "scripts/screenshot.mjs",
            "install": "scripts/install.sh",
        },
        "styleCount": index["count"],
        "styles": [
            {"id": s["id"], "slug": s["slug"], "name": s["name"], "path": s["path"],
             "aliases": s["aliases"], "identity": s["identity"]}
            for s in index["styles"]
        ],
    }


def main() -> int:
    index = build_index()
    manifest = build_manifest(index)
    with open(os.path.join(ROOT, "styles", "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False); f.write("\n")
    with open(os.path.join(ROOT, "design-taste.manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False); f.write("\n")
    print(f"ok styles/index.json ({index['count']} styles)")
    print("ok design-taste.manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
