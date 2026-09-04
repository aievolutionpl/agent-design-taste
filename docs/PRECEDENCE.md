# Precedence — what wins when sources disagree

Two rules in this repository used to contradict each other:

- `SKILL.md`: *"never invent colors/fonts outside the chosen tokens"*
- `DECISION-MATRIX.md`: *"if the brand already has colors/fonts, keep them"*

Both are right. They just needed an order. This file is that order, and it is
the tie-breaker for every conflict in the system.

---

## The precedence chain

```
P1  BRAND & LEGAL          existing brand system, trademarks, compliance copy
        ▲ wins over
P2  ACCESSIBILITY FLOOR    WCAG 2.2 AA gates, keyboard, touch targets, motion
        ▲ wins over
P3  PRODUCT & USER NEEDS   the job the screen has to do; stated requirements
        ▲ wins over
P4  CHOSEN DESIGN DNA      styles/<style>/README.md — the style's rules
        ▲ wins over
P5  REPOSITORY TOKENS      styles/<style>/tokens.css — the style's defaults
        ▲ wins over
P6  AGENT PREFERENCE       what you, the agent, find attractive
```

Read it as: **a lower number never bends to a higher one.**

### P6 is not a tiebreaker, it is a last resort

If you are choosing between two options and your only reason is "this looks
better," you have not finished thinking. Go back up the chain and find the
level that actually decides it.

---

## The one collision that needs a rule: P1 vs P2

Brand outranks accessibility in this chain, and that surprises people. It does
**not** mean you may ship text that fails contrast. It means you may not throw
away someone's brand to fix a contrast problem.

When a brand color fails a contrast requirement:

| ❌ Wrong | ❌ Also wrong | ✅ Right |
|---|---|---|
| Ship `#7BC9F0` body text on white because it's the brand blue | Replace the brand blue with a generic accessible blue | Keep `#7BC9F0` for fills, borders, large display and the logo; derive `#0A6E9E` from the same hue for text and small UI, and register it as a token |

The rule: **preserve brand identity, derive accessible variants.** A brand is a
hue family and a personality, not one hex value. Deriving a darker or lighter
step inside that family keeps the brand and clears the gate.

Write the derivation down. In `DESIGN.md` (see `prompts/DESIGN-CONTRACT.md`):

```
--color-brand:        #7BC9F0   /* canonical, fills + large display only */
--color-brand-text:   #0A6E9E   /* derived: 4.6:1 on #FFFFFF — WCAG AA body */
```

If no accessible variant exists inside the brand family — a genuinely rare
case — say so explicitly and ask. Never decide it silently.

---

## Working inside an existing project: ANALYZE → MAP → ADAPT

Never repaint a product that already has a design system. Three phases, in order.

### 1. ANALYZE (read only — change nothing)

Find and report what already exists:

- [ ] Token source: `tailwind.config.*`, `@theme` block, `:root` CSS vars, a
      `tokens.json`, a theme provider, or a component library's config
- [ ] Type stack: which families load, from where, at what weights
- [ ] Color roles: background / surface / text / border / action / semantic
- [ ] Spacing scale and radius scale actually in use (not what the docs claim)
- [ ] Component library in play: shadcn/ui, MUI, Chakra, Mantine, in-house
- [ ] Dark mode mechanism, if any: `data-theme`, `.dark` class, media query

If the project has **no** design system, say so, and only then treat the style
DNA's tokens as the starting point.

### 2. MAP (translate, don't replace)

Write the correspondence between this repository's token names and theirs.
Their names win — you are adopting their vocabulary, not exporting yours.

| Agent Design Taste | This project | Action |
|---|---|---|
| `--color-bg` | `--background` | use theirs |
| `--color-text-secondary` | *missing* | **gap** — propose adding, don't invent silently |
| `--radius-lg` (12px) | `--radius` (8px) | use theirs; note the style's radius intent is unmet |

### 3. ADAPT (change the smallest thing that achieves the goal)

- Add tokens that are genuinely **missing**; do not redefine tokens that exist.
- Where the style DNA and the existing system disagree on a *value*, the
  existing system wins (P1 beats P4/P5).
- Where they disagree on a *principle* — the DNA says "borders, not shadows"
  and the project uses shadows everywhere — that is a design proposal, not a
  silent edit. Say what you would change and why, then let the human decide.
- Never introduce a second spacing scale, a second radius scale, or a third
  font family into a project that already has them.

---

## Coverage gaps: never invent policy from silence

If the existing system does not decide something — no dark mode spec, no focus
ring, no error state — that is a **gap to flag**, not a blank to fill from the
nearest exemplar. Pattern-matching a missing decision ships an accidental one.

State it: *"the project has no focus-visible style; I used the style DNA's
2px accent ring — confirm or replace."*

---

## Restated hard rule

The old rule *"never invent colors/fonts outside the chosen tokens"* now reads:

> **Every value in the output resolves to a token.** Tokens come from the
> precedence chain: the project's brand system first, this repository's style
> tokens as the greenfield default. A value that exists in neither is a bug —
> either it should be a token, or it should not exist.

That leaves brand preservation and token discipline saying the same thing.
