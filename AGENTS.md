# AGENTS.md

You are in **Agent Design Taste** — a design decision system for AI coding
agents. Two things you might be here to do:

---

## A · You want to USE this system to design something

Read [`AGENT-BOOTSTRAP.md`](AGENT-BOOTSTRAP.md) first. It is 75 lines and it
tells you everything: the 10-step workflow, what to load, and what not to.

Short version:

```
UNDERSTAND → CHOOSE STYLE → TYPOGRAPHY → LAYOUT → TOKENS
    → BUILD → RENDER → AUDIT → REMOVE SLOP → POLISH
```

- Answer audience / product / personality / density / action / emotion **in
  writing** before generating anything.
- Choose **one** dominant style via [`DECISION-MATRIX.md`](DECISION-MATRIX.md).
  Load only that style's `README.md` + `tokens.css`. **Never all 15.**
- Precedence: `brand & legal ▸ accessibility ▸ product needs ▸ style DNA ▸
  repo tokens ▸ your taste` — [`docs/PRECEDENCE.md`](docs/PRECEDENCE.md).
- Render at **1440 / 768 / 390** and look at it before claiming it works.
- Audit with [`ANTI-SLOP.md`](ANTI-SLOP.md) (zero 🔴 blockers) and
  [`evaluation/DESIGN-TASTE-SCORE.md`](evaluation/DESIGN-TASTE-SCORE.md) (≥ 75).

To install it into a project, see [`docs/INTEGRATIONS.md`](docs/INTEGRATIONS.md).

---

## B · You are working ON this repository

### Layout

```
AGENT-BOOTSTRAP.md   entry point        SKILL.md            the workflow
DECISION-MATRIX.md   style scoring      ANTI-SLOP.md        quality gate
LAYOUT-PATTERNS.md   43 patterns        STYLE-COMBINATIONS.md
docs/                precedence, context profiles, integrations, templates
styles/NN-slug/      the 15 style DNAs + tokens + prompts + example
accessibility/ responsive/ typography/ visual-language/ motion/
component-patterns/ layout-patterns/ design-tokens/   cross-style foundations
evaluation/          score, rendered verification, mode routing, taste loop
adapters/            copy-paste instruction files for each coding agent
scripts/             gen_tokens.py · gen_manifest.py · validate.py · install.sh
```

### Rules for changes

1. **`tokens.css` is the source of truth.** `tokens.json` and
   `tokens.tailwind.css` are generated — never hand-edit them. After changing
   any `tokens.css`, run `python3 scripts/gen_tokens.py`.
2. **`styles/index.json` and `design-taste.manifest.json` are generated.** Edit
   the data in `scripts/gen_manifest.py`, then run it.
3. **All 15 style READMEs share one 24-section architecture.** Adding or
   renaming a section means doing it in all 15. See
   [`docs/STYLE-TEMPLATE.md`](docs/STYLE-TEMPLATE.md).
4. **Run `python3 scripts/validate.py` before committing.** It is what CI runs.
5. **Do not make unsupported claims.** No invented citations, no integration
   mechanisms that were not checked against the tool's own documentation, no
   statistics without a source.
6. **Do not rename core directories.** External installations reference these
   paths by name.
7. **390px is the canonical mobile viewport** throughout. Do not reintroduce
   375 or any other number.

Full contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md).
