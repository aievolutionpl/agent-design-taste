# GEMINI.md

<!-- Agent Design Taste adapter for Gemini CLI.
     To use a single AGENTS.md instead, set in .gemini/settings.json:
       { "context": { "fileName": ["AGENTS.md", "GEMINI.md"] } } -->

## Design

This project uses **Agent Design Taste** at `./agent-design-taste/`.

**Before writing or changing any UI, read `agent-design-taste/AGENT-BOOTSTRAP.md`.**

### Workflow

```
UNDERSTAND → CHOOSE STYLE → TYPOGRAPHY → LAYOUT → TOKENS
    → BUILD → RENDER → AUDIT → REMOVE SLOP → POLISH
```

- State audience, product type, personality, density, primary action and target
  emotion before generating anything.
- Choose one dominant style with `agent-design-taste/DECISION-MATRIX.md`.
  Load only that style's `README.md` and `tokens.css` — never all 15.
- Precedence: `brand & legal ▸ accessibility ▸ product needs ▸ style DNA ▸
  repo tokens ▸ your taste`. Never repaint an existing design system —
  see `agent-design-taste/docs/PRECEDENCE.md`.
- Verify at **1440 / 768 / 390**. 390 is the primary mobile check.
- Audit with `ANTI-SLOP.md` before delivering. Zero 🔴 BLOCKERS.

### Never

Fake statistics, testimonials or logo walls · body text under 4.5:1 contrast ·
invisible focus states · horizontal scroll at 390px · animation with no
`prefers-reduced-motion` fallback.
