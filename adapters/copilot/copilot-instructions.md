# Copilot instructions

<!-- Copy to .github/copilot-instructions.md
     For UI-only scoping, use .github/instructions/ui.instructions.md with an
     applyTo glob in its frontmatter instead. -->

## Design

This project uses **Agent Design Taste** at `agent-design-taste/`.

**Before generating or changing any UI, read
`agent-design-taste/AGENT-BOOTSTRAP.md`.**

### Workflow

UNDERSTAND → CHOOSE STYLE → TYPOGRAPHY → LAYOUT → TOKENS → BUILD → RENDER →
AUDIT → REMOVE SLOP → POLISH

- State audience, product type, brand personality, content density, primary
  action and target emotion before writing code.
- Choose one dominant style using `agent-design-taste/DECISION-MATRIX.md`.
  Load only that style's `README.md` and `tokens.css` — never all 15.
- Every color, space, radius and duration resolves to a token.
- Verify at 1440 / 768 / 390. 390 is the primary mobile check.

### Precedence

`brand & legal ▸ accessibility ▸ product needs ▸ style DNA ▸ repo tokens ▸ your taste`

Never repaint an existing design system. See
`agent-design-taste/docs/PRECEDENCE.md`.

### Hard rules

- No fake statistics, testimonials or logo walls
- Body text ≥ 4.5:1 contrast; visible `:focus-visible` on every control
- No horizontal scroll at 390px; touch targets ≥ 44×44px
- Every animation handles `prefers-reduced-motion`
