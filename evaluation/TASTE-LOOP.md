# The Taste Loop — preference learning for agents

Rules alone reach a ceiling: they forbid bad output but don't teach *why*.
The strongest upgrade is a **preference loop** — the same structure used in
RLHF, applied at project scale:

```
1. GENERATE    → 2-3 genuinely different directions (not variations of one)
2. RANK        → pick the strongest, explain WHY the others fail in this context
3. RECORD      → task, preferred output, rejected output, reasoning, principle
4. RETRIEVE    → load relevant past decisions BEFORE generating similar work
5. EVALUATE    → separate critique pass against recorded decisions
```

## File layout (add to any project using this skill)

```
taste/
├── taste.md              ← principles, distilled from decisions
├── accepted/             ← winning examples, tagged by surface
│   └── 2026-04-12-landing-editorial.md
└── rejected/             ← paired losing examples + why
    └── 2026-04-12-landing-bento.md
```

Each record:
```markdown
# 2026-04-12 · landing page · Ledgerly
## Chosen: Editorial hero (Fraunces + Inter)
## Rejected: Bento grid
## Why: freelancers are anxious about taxes; editorial warmth builds trust,
   bento's density signals complexity.
## Reusable principle: anxiety-driven audiences → warm editorial, not dense grids.
```

## Quality bar for the "Why"

"Too generic" teaches nothing. A usable explanation names the mechanism:
- ❌ "the bento looked cluttered"
- ✅ "the 12px radius on every surface makes the editor look like a settings
  panel; working surfaces need tighter corners, larger radii only on elevated
  containers"

## Rules

1. Explanations must name a **reusable principle**, not a verdict.
2. Retrieve before generating: 2-3 most relevant past decisions into context.
3. The final ship decision stays human. The loop informs, not decides.
4. Kill stale preferences — taste changes; archive decisions that no longer apply.
5. Generate the same brief twice (with and without the loop) and diff — if hex
   values and radii didn't move, the loop hasn't landed yet.
