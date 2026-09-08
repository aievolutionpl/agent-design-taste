# Changelog

All notable changes to this project are documented here. The **skill** follows
[semantic versioning](https://semver.org/): the current version is in the
`SKILL.md` frontmatter and in `design-taste.manifest.json`.

For a skill, "breaking" means: a renamed or moved file that installations
reference, a changed workflow contract, or a removed rule an agent may be
relying on.

## [2.1.0] — 2026-09-08

Enforcement release. 2.0.0 wrote the accessibility rules down; this one measures
them. Both new checks found real failures in this repository on their first run.

### Added
- `scripts/check_contrast.py` — measures every style palette against WCAG AA:
  text pairs at 4.5:1, focus indicators at 3:1, in both themes. It resolves dark
  as light-then-dark (dark blocks are partial overrides, so the pairs most
  likely to fail were the ones never being checked) and composites translucent
  colors before measuring. Waivers require a written reason.
- CI now runs the contrast check, and **renders all 15 example pages** at
  1440/768/390/360 with `scripts/screenshot.mjs`, failing on mobile overflow and
  uploading the screenshots as an artifact. The render check existed in 2.0.0
  but only ever ran by hand.

### Fixed
- **Focus rings were invisible across 14 of 15 styles.** Every one used a
  translucent color (alpha 0.30–0.45), compositing to 1.2–1.8:1 against its own
  background — the exact 🔴 BLOCKER `ANTI-SLOP.md` defines. All are now solid.
  Two styles were also contradicting their own §13: 05 documents a "thick black
  outline" and shipped a pink ring at 1.98:1; 06 documents a "high-contrast
  outline" and shipped neon yellow at 1.04:1. Both now use their text color.
- **14 of 15 example pages had no authored focus style at all** — no
  `:focus-visible`, no `:focus`, no `outline`. Each now ships one, using a
  palette color verified at 3:1 against that page's own background.
- **11 button/label pairs failed 4.5:1** — white-on-mid-tone labels at 1.86–4.48:1.
  Fixed by adapting the label where the fill is a light tint, and by an
  imperceptible darkening of the fill elsewhere; brand hues are preserved.
- **Glassmorphism's accent was `#8B5CF6`** — the exact hex `ANTI-SLOP.md` names
  as the over-used default violet, and it failed contrast at 4.23:1. Now
  `#7C3AED`: still unmistakably violet, off the flagged default, 5.70:1.
- `scripts/gen_tokens.py` treated **every** `:root` as the light palette,
  including one nested inside `@media (prefers-reduced-motion: reduce)`. A token
  misplaced there looked correct in the generated JSON while applying only to
  reduced-motion users in a browser. At-rule blocks are now excluded.
- Example palettes re-synced to the corrected tokens, so no reference page
  demonstrates a failure the tokens no longer have.

### Changed
- `design-tokens/TOKENS-GUIDE.md`, `accessibility/ACCESSIBILITY.md`,
  `CONTRIBUTING.md` and both READMEs document the enforced checks — including
  why `--color-border` is deliberately *not* held to 3:1 (WCAG 1.4.11 exempts
  boundaries not needed to identify a component; failing all 15 styles on
  hairlines would get the check switched off).

## [2.0.0] — 2026-09-04

The onboarding and routing release. The design knowledge was already here; this
release makes it installable, routable and internally consistent.

### Added
- `AGENT-BOOTSTRAP.md` — a 75-line universal entry point for any agent.
- `docs/PRECEDENCE.md` — the explicit precedence chain
  (`brand ▸ accessibility ▸ product ▸ style DNA ▸ tokens ▸ agent taste`)
  and the ANALYZE → MAP → ADAPT process for existing design systems.
- `docs/CONTEXT-PROFILES.md` — LIGHT / STANDARD / FULL loading profiles with
  measured per-file token costs.
- `docs/INTEGRATIONS.md` — per-agent installation for Claude Code, Codex,
  Cursor, Windsurf, GitHub Copilot, Gemini CLI, Lovable and v0, written against
  each tool's own documented conventions.
- `docs/EXAMPLE-WORKFLOW.md` — one brief followed end to end, with the actual
  context cost at the bottom.
- `docs/STYLE-TEMPLATE.md` — the required structure for a new style.
- `adapters/` — copy-paste instruction files (`AGENTS.md`, `CLAUDE.md`,
  `GEMINI.md`, Cursor `.mdc`, Windsurf rule, Copilot instructions).
- `scripts/install.sh` — installs the right adapter into a project.
- `scripts/gen_manifest.py`, `design-taste.manifest.json`, `styles/index.json` —
  machine-readable routing: ids, aliases, paths, scoring weights, veto
  conditions, incompatible and supporting styles.
- `scripts/validate.py` + GitHub Actions workflow — structural validation of
  every style folder, link, generated file and required README section.
- `accessibility/ACCESSIBILITY.md` — accessibility as a quality gate, with a
  per-style failure table.
- `responsive/RESPONSIVE-FOUNDATIONS.md` — recomposition, not stacking.
- `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE`.
- `README.pl.md` — Polish translation, with a language switch in both files.
- Each style DNA gained: design philosophy, responsive behaviour, style
  combinations, a real signature move, and pointers to prompts, tokens and
  example.

### Changed
- **BREAKING — canonical mobile viewport is now 390px** (with 360 as the narrow
  floor). The repository previously said `390px first` in one place and `375px`
  in another. Anything pinned to 375 should move to 390.
- **BREAKING — `SKILL.md` hard rule 3 rewritten.** "Never invent colors/fonts
  outside the chosen tokens" conflicted with "preserve existing brand
  colors/fonts". It now reads: *every value resolves to a token; tokens come
  from the precedence chain, brand first, style DNA as the greenfield default.*
- **BREAKING — all 15 style READMEs restructured** into one 24-section
  architecture. Content preserved; heading names and order changed. Anything
  that deep-links to a style README anchor needs updating.
- `DECISION-MATRIX.md` — added 11 brief signals, absolute veto gates, and a
  weighted scoring card per style. The agent must now be able to say why the
  runner-up loses.
- `ANTI-SLOP.md` — added BLOCKER / STRONG SMELL / MINOR SMELL severity, and
  new detections (every section in a card, generic icon grids, meaningless
  metric cards, generic marketing copy, desktop stacked onto mobile).
- `evaluation/DESIGN-TASTE-SCORE.md` — 13 weighted categories summing to 100,
  with 8 hard blockers that fail a design regardless of total. Accessibility
  now carries the highest single weight.
- `LAYOUT-PATTERNS.md` — 43 patterns became a decision library: when to use,
  density, fitting and conflicting styles, mobile recomposition, CTA placement,
  accessibility notes, and the common AI mistake for each.
- `typography/`, `visual-language/`, `component-patterns/` — substantially
  expanded (typeface signals and metrics, language support, font-loading
  performance; per-style image direction; 19 components with a required state
  matrix).
- `evaluation/RENDERED-VERIFICATION.md` — explicit protocol, and an honest
  fallback for agents without browser access.
- `evaluation/MODE-ROUTING.md` — modes mapped to context profiles; removed an
  unverifiable research citation.

### Fixed
- `scripts/gen_tokens.py` produced invalid Tailwind v4 output: doubled prefixes
  (`--color--bg`), a truncated namespace (`--radiu--sm`), and camelCase keys
  (`--fontSize--h1`). Now emits correct `--color-*`, `--text-*`, `--radius-*`,
  `--shadow-*`, `--ease-*`, `--container-*` namespaces.
- `tokens.json` keys had leading dashes (`"-bg"`). Now clean (`"bg"`).
- Scripts had a hard-coded absolute path from the author's machine.
- Five styles were missing token categories they were documented as having;
  `15-expressive-kinetic-typography` had no `--shadow-focus` at all, which is an
  accessibility requirement.
- The README structure diagram omitted `tokens.json` and `tokens.tailwind.css`
  and referenced an `assets/decision-tree.png` that does not exist.
- **The repository's own example pages failed its own gates**, found by running
  `scripts/screenshot.mjs` against them:
  - Horizontal overflow at 390px in `07-neumorphism`, `11-editorial-magazine`
    and `14-3d-spatial-ui` (nav bars with no mobile treatment) — a 🔴 blocker.
  - Horizontal overflow at 360px in `12-maximalism`, and page-level scroll from
    the deliberate 120% headline bleed in `06-brutalist-anti-grid` (now clipped
    at the hero, so the bleed reads as intent rather than as a scrollbar).
  - `03-liquid-glass`, `04-bento-grid`, `05-neo-brutalism`, `08-claymorphism`
    and `13-y2k-retrofuturism` deleted their nav links below 900px with no
    replacement — the "desktop stripped for mobile" failure. The link row now
    moves to its own line and keeps a 44px tap height.
  - Touch targets under 44px in `05`, `07` and `10`.
  - `13-y2k-retrofuturism`'s chrome hero headline measured **1.1:1** against
    the light sky — the exact failure `accessibility/ACCESSIBILITY.md` names
    for that style. It now sits on a dark `--ink` plate (3.8:1 at the gradient's
    darkest stop), which is also the style's own documented signature move.
- `07-neumorphism` had a duplicated "When NOT to use" section and a vague
  citation.

## [1.1.0] — 2026

### Added
- Taste loop, mode routing, the `DESIGN.md` contract, rendered verification,
  per-style accessibility notes and design-decision reasoning, live preview
  gallery.

## [1.0.0] — 2026

### Added
- Initial release: `SKILL.md`, `DECISION-MATRIX.md`, `ANTI-SLOP.md`,
  `LAYOUT-PATTERNS.md`, `STYLE-COMBINATIONS.md`, 15 design styles with tokens,
  prompts and working example pages, and the cross-style foundations.
