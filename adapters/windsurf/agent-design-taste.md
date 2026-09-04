# Agent Design Taste

<!-- Windsurf rule. Suggested activation mode: Glob on
     *.tsx, *.jsx, *.vue, *.svelte, *.astro, *.css, *.html
     (or Always On for a UI-heavy project). -->

This project uses Agent Design Taste at `agent-design-taste/`.

**Before generating or changing UI, read `agent-design-taste/AGENT-BOOTSTRAP.md`.**

## Workflow

UNDERSTAND → CHOOSE STYLE → TYPOGRAPHY → LAYOUT → TOKENS → BUILD → RENDER →
AUDIT → REMOVE SLOP → POLISH

1. State audience, product type, brand personality, content density, primary
   action and target emotion before writing any code.
2. Choose one dominant style with `agent-design-taste/DECISION-MATRIX.md`.
   Load only that style's `README.md` + `tokens.css` — never all 15.
3. Every value resolves to a token.
4. Verify at 1440 / 768 / 390. 390 is the primary mobile check.
5. Audit with `agent-design-taste/ANTI-SLOP.md` before delivering.

## Precedence

`brand & legal ▸ accessibility ▸ product needs ▸ style DNA ▸ repo tokens ▸ your taste`

An existing design system is analyzed and adapted, never overwritten.
See `agent-design-taste/docs/PRECEDENCE.md`.

## Never

Fake statistics or testimonials · body text under 4.5:1 · invisible focus
states · horizontal scroll at 390px · animation without a
`prefers-reduced-motion` fallback.
