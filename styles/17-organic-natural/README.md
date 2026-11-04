# 17 · Organic / Natural

**Warm, earthy, handmade.**

## 01 · Overview

Warm paper tones, a soft serif, generous space and one irregular hand-cut shape per page. The style makes a product feel made by people, slowly, from real materials — it trades the precision of a grid for the reassurance of craft.

## 02 · Design philosophy

Borrowed from print for bakeries, farms, apothecaries and ceramicists: uncoated stock, earth pigments, type with a little softness in it. Its job is to lower the pulse and raise trust in the *origin* of something — food, skin care, a place to stay. It is FOR products whose value is in materials and patience, and it fails the moment it is used to make a generic SaaS feel "friendly".

**Design decisions explained — why, not just what**

- **Why these fonts:** a soft, ink-trap-free serif (Young Serif) reads as hand-set and warm without the formality of a fashion Didone; a friendly geometric-humanist sans (Figtree) keeps menus, prices and hours plainly legible
- **Why this radius:** 10–28px plus pill buttons — rounded the way river stones and loaves are; sharp corners would read industrial, and fully uniform 24px everywhere would read like an AI template, so the one organic blob does the expressive work
- **Why this density:** low-medium — calm needs air; the content is usually few things described well (five loaves, three rooms, one ritual)

## 03 · Visual principles

paper-warm canvas · soft serif display, humanist sans text · moss green for action, terracotta for one highlight · one hand-cut organic shape per page · wavy, not straight, section transitions · flat illustration in earth pigments · quiet paper grain.

## 04 · Typography

- **Recommended families (Google Fonts):** Display: Young Serif, Fraunces (soft, low optical size), Gloock. Text: Figtree, Karla, DM Sans. Mono: rarely — IBM Plex Mono for batch numbers only.
- **Pairing:** Young Serif 400 (H1–H3) + Figtree 400/500/600 (body, UI, prices, labels).
- **Scale:** H1 68/70 (−0.015em) · H2 44/48 · H3 26/32 · H4 21/28 · body 18/1.65 · small 15/1.5 · label 13 uppercase +0.12em.
- **Body:** 18px, line-height 1.65, measure 55–65ch. Never below 16px for menus or hours.
- **Uppercase:** small kicker labels only, letter-spaced; never headings.
- **CSS:**
```css
h1 { font: 400 68px/1.02 'Young Serif', Georgia, serif; letter-spacing: -0.015em; }
body { font: 400 18px/1.65 'Figtree', system-ui, sans-serif; }
.kicker { font: 600 13px/1 'Figtree'; letter-spacing: .12em; text-transform: uppercase; }
```
- **Typical mistakes:** script or "handwritten" fonts for headings (twee, illegible); a bold serif at every level; light grey body text on cream; italic overuse to fake warmth.

## 05 · Layout & grid

- **Grid:** 12-col, max-width 1180px, 24px gutters; asymmetric splits (1.05 / 1) rather than perfect halves.
- **Spacing:** 8px base, generous — sections 96–120px apart; banded sections separated by a wave, not a line.
- **Hero:** Split Hero with an illustration or photo masked in an organic blob; one rotated "stamp" label may overlap the mask.
- **Frame patterns:** Split Hero, three-step process with line icons, menu/price list with hairline rows, a story card on a surface band, info triplet (address · hours · orders).

## 06 · Visual hierarchy

First: the serif headline with its one terracotta word. Second: the blob-masked image. Third: the moss-green primary button. The eye then drops into the wave-banded process section; prices and hours are always findable in one scroll.

## 07 · Color system

- **Light:** bg #F6F1E7 (oat) · surface #EDE5D4 · text #2A271F (bark) · secondary #5C5647 · border #DACFBA · primary #3D5638 (moss) · accent #A44A26 (terracotta).
- **Dark:** bg #1B1A15 · surface #25231C · text #EFE8D7 · secondary #B5AD99 · border #3A372C · primary #A9C49B · accent #E39069.
- Illustration pigments stay inside the earth family (wheat #D9B26F, crust #B9773E, sage). Avoid: pure white, saturated "eco" greens (#00C853), blue anywhere prominent, gradients.

## 08 · Components

Buttons: pill, moss fill with white label for primary; 1.5px bark outline for secondary; hover lifts 2px. Cards: surface fill, 18–28px radius, no border or a 1.5px border — never both. Navbar: wordmark with a small line glyph, sans links with a drawn-in underline on hover. Inputs: 1.5px border, 10px radius, generous 48px height. Tags: pill, surface fill, uppercase micro label; one terracotta tag for the special item. Menus and pricing: serif item name, sans description, price right-aligned. Modals: oat panel, 28px radius, soft shadow.

Anatomy and the required state matrix (default / hover / focus-visible / active / disabled / loading / error / success) are universal — see `component-patterns/COMPONENT-PATTERNS.md`. This section defines the *skin*, not the behaviour.

## 09 · Shape language

Soft radii (10/18/28px, pills for actions), one irregular blob (`--radius-organic`) per page as an image mask, wavy SVG section edges. Depth is a single soft, warm shadow on floating labels only. Line icons: 2.5px stroke, round caps and joins — drawn, not engineered.

## 10 · Imagery & visual direction

Fits: natural-light photography of materials and hands at work, warm grading; flat illustration in earth pigments; botanical line drawings. Breaks cohesion: glossy 3D, neon, stock photos of smiling people holding salads, AI-generated "cozy" scenes with impossible hands.

Per-style image direction table: `visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md` § 10.

## 11 · Motion

180–600ms, soft ease-out (`cubic-bezier(.33,1,.68,1)`). Allowed: underline draw-in, a 2px button lift, slow fade-up of sections once. Forbidden: bouncing, parallax leaves, falling-petal particles. `prefers-reduced-motion`: all transitions off.

## 12 · Responsive behaviour

Verify at **1440 · 768 · 390** (canonical mobile) and once at **360** (narrow floor). Responsive means recomposition, not stacking — `responsive/RESPONSIVE-FOUNDATIONS.md`.

- **Adaptation:** the split hero becomes headline → blob image → actions; process steps stack with icons kept; the menu keeps price right-aligned; the info triplet becomes three cards.
- **Non-negotiable for this style:** hours, address and the order action must be reachable on mobile without hunting — warmth is not an excuse to bury practical information.

## 13 · Accessibility

- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every pair in this style's palette.
- Focus states: a 3px moss ring reads clearly on oat and on the surface band; pill buttons keep their pill-shaped ring.
- Motion: this style is tempted toward drifting leaves and parallax — keep it still.
- Common a11y failure in this style: beige-on-cream secondary text (#A39A86 on #F6F1E7 ≈ 2.6:1) and terracotta small text. Keep secondary at #5C5647 or darker; use terracotta for display words and fills with white labels, not for 14px copy. Paper grain must stay below perceptible contrast impact (opacity ≤ 0.09 alpha).

The universal floor — contrast, focus, keyboard, semantics, motion, touch targets, zoom — is in `accessibility/ACCESSIBILITY.md`. This section covers what *this style specifically* gets wrong.

## 14 · When to use

Food and beverage, bakeries and restaurants, farms and producers, skin care and wellness, hospitality, ceramics and craft, sustainability brands, local shops. Audiences who buy on origin, care and trust in the maker.

## 15 · When NOT to use

Dense dashboards, developer tools, fintech or anything where precision is the promise — it reads vague. Products with no material story (a generic SaaS made "friendly" with beige) — that is greenwashing by palette. High-urgency conversion pages and youth/streetwear brands that need energy.

## 16 · Do

- Use one organic blob mask per page, on the hero image
- Set headings in a soft serif, everything practical in sans
- Keep moss for actions and terracotta for one highlight word or tag
- Transition banded sections with a wave
- Draw icons with round caps at 2.5px
- Put hours, prices and address in plain, scannable rows
- Keep paper grain barely perceptible

## 17 · Don't

- Script or handwritten heading fonts
- Saturated "eco" greens or leaf emoji
- Blobs on every card
- Light beige text on cream
- Falling leaves, parallax petals, bouncy springs
- Stock "lifestyle" photography
- Beige applied to a product with no material story

## 18 · Anti-slop — Organic edition

Slop here: a beige SaaS template with a leaf emoji, a handwritten font for the H1, three blob-shaped cards with identical line icons, "Sustainably crafted with love 🌿", and a stock photo of hands holding a seedling. The fix is specificity — named farms, real prices, real hours, one shape that earns its irregularity.

**Good vs bad**

- **Good:** a bakery site whose hero is the loaf, whose copy names the grain and the hours of fermentation, and whose only irregular shape is the image mask.
- **Bad:** "organic" as a skin — blobs everywhere, beige everything, and nothing on the page you could actually buy or visit.

Universal severity levels (BLOCKER / STRONG / MINOR): `ANTI-SLOP.md`.

## 19 · Style combinations

One dominant + at most one supporting style. The supporting style owns exactly one layer — typography, one section type, or micro-motion — never structure.

- **Works with:** Editorial (11) — editorial owns long-form story pages and pull quotes · Minimalism (01) — restraint on checkout and account pages · Claymorphism (08) — one soft-3D product illustration for a family-facing brand
- **Avoid pairing with:** Terminal / Dev Dark (16) — cold precision against warmth · Y2K (13) — chrome kills the material story · 3D / Spatial (14) — rendered depth fights flat, hand-made illustration

Full rules: `STYLE-COMBINATIONS.md`.

## 20 · Signature move

**One hand-cut organic shape** — the hero image masked in an irregular blob (`border-radius: 58% 42% 47% 53% / 52% 46% 54% 48%`), with a single rotated stamp label overlapping its edge. Everything else on the page uses ordinary soft radii, which is what makes the blob read as deliberate.

Use it **once per page**, deliberately. A signature move repeated on every element is no longer a signature.

## 21 · When to break the rules

One crisp, information-dense block — the menu with prices, or the hours table — set with ruler-straight hairlines and tabular figures. Craft brands earn trust by being exact about the practical things.

## 22 · Example prompts

Ready-to-paste prompts for Codex, Claude, Lovable and v0: [`prompts.md`](prompts.md)

## 23 · Design tokens

- [`tokens.css`](tokens.css) — **canonical.** If this file and the prose above disagree, the token wins.
- [`tokens.json`](tokens.json) — generated, for design tools and JS
- [`tokens.tailwind.css`](tokens.tailwind.css) — generated, Tailwind v4 `@theme`

Regenerate the two derived files with `python3 scripts/gen_tokens.py` after editing `tokens.css`.

## 24 · Example implementation

[`example.html`](example.html) — a single-file, zero-dependency page built strictly from this style's DNA and tokens. Open it in a browser.

It is **one valid interpretation, not a spec.** Copying it wholesale is how every page ends up identical — read it, then compose something else.
