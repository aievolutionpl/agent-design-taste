# CLAUDE.md

<!-- Agent Design Taste adapter for Claude Code.
     If this project already has an AGENTS.md, replace the section below with:
        @AGENTS.md
     Claude Code reads CLAUDE.md, not AGENTS.md, but supports @path imports. -->

## Design work

This project uses **Agent Design Taste** at `./agent-design-taste/`.

**Before writing or changing any UI, read
`agent-design-taste/AGENT-BOOTSTRAP.md`.** Not after — before.

If the skill is installed, `/agent-design-taste` loads the full workflow.

### Non-negotiable

1. Answer audience / product / personality / density / action / emotion in
   writing before generating anything.
2. Choose one dominant style via `agent-design-taste/DECISION-MATRIX.md`, and
   state why the runner-up loses. Load only that style's `README.md` +
   `tokens.css` — never all 15.
3. Precedence when sources disagree:
   `brand & legal ▸ accessibility ▸ product needs ▸ style DNA ▸ repo tokens ▸ your taste`.
   An existing design system is analyzed and adapted, never overwritten —
   see `agent-design-taste/docs/PRECEDENCE.md`.
4. Every value resolves to a token. A hard-coded `13px` or `#7c3aed` is a bug.
5. Render at **1440 / 768 / 390** with a real browser and look at the result
   before claiming it works. If you cannot render, say so explicitly.
6. Audit with `evaluation/DESIGN-TASTE-SCORE.md` (≥75) and `ANTI-SLOP.md`
   (zero 🔴 BLOCKERS) before delivering.

### Never

Fake statistics or testimonials · body text under 4.5:1 · invisible focus
states · horizontal scroll at 390px · animation without a
`prefers-reduced-motion` fallback · loading all 15 style folders into context.
