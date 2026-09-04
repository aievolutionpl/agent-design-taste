# Style contribution template

Copy this structure exactly. All 15 style DNAs share it, and
`scripts/validate.py` enforces it — headings must match, in this order.

Replace every `<…>`. Delete nothing. A section you have nothing to say about
means the style has not been thought through yet.

See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the full checklist and the
files that must accompany this one.

---

````markdown
# NN · <Style Name>

**<Identity — three or four words. "Grid, type, order." "More is more.">**

## 01 · Overview

<Two or three sentences. What the style is and what it does to a page.>

## 02 · Design philosophy

<Where it comes from and what it believes. Two to four sentences. This is the
section that keeps the style from being a preset — say what it is FOR.>

**Design decisions explained — why, not just what**

- **Why these fonts:** <the reasoning, naming the audience emotion>
- **Why this radius:** <what the radius signals, and what the wrong one would say>
- **Why this density:** <why this style lives at this density>

## 03 · Visual principles

<Six to eight principles separated by · — the style's fingerprint in one line.>

## 04 · Typography

- **Recommended families (Google Fonts):** <by role: display / text / mono>
- **Pairing:** <the specific pairing, with weights>
- **Scale:** H1 … · H2 … · H3 … · body … · small …
- **Body:** <size, line-height, letter-spacing, measure>
- **Uppercase:** <where allowed, where forbidden>
- **CSS:**
```css
h1 { … }
body { … }
```
- **Typical mistakes:** <what agents get wrong in this style's typography>

## 05 · Layout & grid

- **Grid:** <columns, max-width, gutters>
- **Spacing:** <scale, section rhythm>
- **Hero:** <which hero patterns fit>
- **Frame patterns:** <named patterns from LAYOUT-PATTERNS.md>

## 06 · Visual hierarchy

<What is seen first, second, third. The intended eye path.>

## 07 · Color system

- **Light:** bg … · surface … · text … · secondary … · border … · accent …
- **Dark:** bg … · surface … · text … · border … · accent …
- <Saturation rules, what to avoid.>

## 08 · Components

<How this style skins buttons, cards, nav, inputs, tabs, pricing, dashboards,
modals, badges, tooltips, tables. Two to four sentences — appearance only.>

Anatomy and the required state matrix (default / hover / focus-visible / active
/ disabled / loading / error / success) are universal — see
`component-patterns/COMPONENT-PATTERNS.md`. This section defines the *skin*,
not the behaviour.

## 09 · Shape language

<Radius, borders, corners, how depth is expressed.>

## 10 · Imagery & visual direction

<What imagery fits. What breaks cohesion.>

Per-style image direction table: `visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md` § 10.

## 11 · Motion

<Durations, easing, what animates and what must not. Reduced-motion behaviour.>

## 12 · Responsive behaviour

Verify at **1440 · 768 · 390** (canonical mobile) and once at **360** (narrow
floor). Responsive means recomposition, not stacking —
`responsive/RESPONSIVE-FOUNDATIONS.md`.

- **Adaptation:** <what changes at each step down>
- **Non-negotiable for this style:** <the one thing that must survive to mobile,
  or the one thing that must be removed>

## 13 · Accessibility

- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every pair in this
  style's palette.
- Focus states: <what works in this style specifically>
- Motion: <what this style is tempted to over-animate>
- Common a11y failure in this style: <the specific one, with the fix>

The universal floor — contrast, focus, keyboard, semantics, motion, touch
targets, zoom — is in `accessibility/ACCESSIBILITY.md`. This section covers what
*this style specifically* gets wrong.

## 14 · When to use

<Product types, audiences, contexts. Be specific.>

## 15 · When NOT to use

<The honest failure modes. Reviewers read this section first. A style with no
"when not" has not been thought about.>

## 16 · Do

- <Six to eight concrete, checkable rules>

## 17 · Don't

- <Six to eight concrete, checkable prohibitions>

## 18 · Anti-slop — <style> edition

<What generic AI output looks like *in this style*, and what to do instead.>

**Good vs bad**

- **Good:** <a real, named example and why it works>
- **Bad:** <a specific failure mode and why it fails>

Universal severity levels (BLOCKER / STRONG / MINOR): `ANTI-SLOP.md`.

## 19 · Style combinations

One dominant + at most one supporting style. The supporting style owns exactly
one layer — typography, one section type, or micro-motion — never structure.

- **Works with:** <style (NN) — how it applies · …>
- **Avoid pairing with:** <style (NN) — why it fails · …>

Full rules: `STYLE-COMBINATIONS.md`.

## 20 · Signature move

**<The ONE element that makes a page instantly recognisable as this style.>**
<Concrete and implementable. "One accent color used only for actions" is a
signature move; "bold and modern" is not.>

Use it **once per page**, deliberately. A signature move repeated on every
element is no longer a signature.

## 21 · When to break the rules

<The one deliberate exception that makes the style read as intent rather than
as a template. Every style needs one.>

## 22 · Example prompts

Ready-to-paste prompts for Codex, Claude, Lovable and v0: [`prompts.md`](prompts.md)

## 23 · Design tokens

- [`tokens.css`](tokens.css) — **canonical.** If this file and the prose above disagree, the token wins.
- [`tokens.json`](tokens.json) — generated, for design tools and JS
- [`tokens.tailwind.css`](tokens.tailwind.css) — generated, Tailwind v4 `@theme`

Regenerate the two derived files with `python3 scripts/gen_tokens.py` after editing `tokens.css`.

## 24 · Example implementation

[`example.html`](example.html) — a single-file, zero-dependency page built
strictly from this style's DNA and tokens. Open it in a browser.

It is **one valid interpretation, not a spec.** Copying it wholesale is how
every page ends up identical — read it, then compose something else.
````
