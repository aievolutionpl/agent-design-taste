# AGENTS.md

<!-- Agent Design Taste adapter. If this project already has an AGENTS.md,
     copy the "## Design" section below into it instead of replacing the file. -->

## Design

This project uses **Agent Design Taste** — a design decision system for AI
agents. It lives at `./agent-design-taste/`.

**Before writing or changing any UI, read `agent-design-taste/AGENT-BOOTSTRAP.md`.**
Do not generate interface code first and consult it afterwards.

### The workflow

```
UNDERSTAND → CHOOSE STYLE → TYPOGRAPHY → LAYOUT → TOKENS
    → BUILD → RENDER → AUDIT → REMOVE SLOP → POLISH
```

1. State the audience, product type, brand personality, content density,
   primary action and target emotion — in writing, before any code.
2. Choose **one** dominant style using `agent-design-taste/DECISION-MATRIX.md`,
   and say why the runner-up loses.
3. Load **only** that style's `README.md` and `tokens.css`.
   Never load all 15 styles.
4. Build from tokens. Every color, space, radius and duration resolves to one.
5. Render at **1440 / 768 / 390** and look at it. Code review is not visual review.
6. Audit with `evaluation/DESIGN-TASTE-SCORE.md` and `ANTI-SLOP.md`.

### Precedence — what wins when sources disagree

```
brand & legal ▸ accessibility ▸ product needs ▸ style DNA ▸ repo tokens ▸ your taste
```

If this project already has a design system, **do not repaint it.** Run
ANALYZE → MAP → ADAPT from `agent-design-taste/docs/PRECEDENCE.md`. Style
tokens are defaults for greenfield work, not permission to replace a brand.

### Hard rules

- No fake statistics, testimonials or logos. Ever.
- Body text ≥ 4.5:1 contrast. Visible `:focus-visible` on every control.
- No horizontal scroll at 390px. Touch targets ≥ 44×44px.
- Every animation handles `prefers-reduced-motion`.
- Never claim a design works without having rendered and looked at it.

### Do not load

All 15 style folders · every `example.html` · `styles/*/prompts.md` (unless
prompting another tool) · `docs/INTEGRATIONS.md` (installation only).
