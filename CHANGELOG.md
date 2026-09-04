# Changelog

All notable changes to this project are documented here. The **skill** follows
[semantic versioning](https://semver.org/): the current version is in the
`SKILL.md` frontmatter and in `design-taste.manifest.json`.

For a skill, "breaking" means: a renamed or moved file that installations
reference, a changed workflow contract, or a removed rule an agent may be
relying on.

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
