# Anti AI-Slop Rules

Universal rules that kill generic AI-generated UI. Run this checklist on every
design before delivery. **Any hit = fix before shipping.**

## The slop patterns

### Color & gradient
- [ ] **No gradient blobs without purpose.** Purple-to-blue mesh gradient behind a hero "because it looks AI-premium" = slop. A gradient must encode meaning (state, depth, brand).
- [ ] **No default neon purple (#8B5CF6-family) as the primary brand color.** It is the most statistically over-used AI color. If purple is genuinely on-brand, use a specific, chosen shade — not the default Tailwind violet.
- [ ] **No low-contrast gray-on-gray text.** All body text ≥ 4.5:1 contrast.
- [ ] **No more than 2 accent colors** on one screen.

### Cards & surfaces
- [ ] **Not every card has the same border-radius.** Uniform 24px radius on everything is a fingerprint of AI output. Radius should vary by hierarchy (or be consistently sharp).
- [ ] **No more than 2 glass/translucent surfaces per view.** Glassmorphism ≠ 30 frosted cards.
- [ ] **No floating cards with large soft shadows for no reason.** Shadow = elevation semantics, not decoration.
- [ ] **No identical 3-column feature card rows.** Vary composition: bento, alternating, editorial split, numbered list.

### Layout & composition
- [ ] **Not everything is centered.** Left-aligned layouts with strong ragged-right text are a design decision; universal centering is a default.
- [ ] **No same hero every time.** Check LAYOUT-PATTERNS.md — rotate split hero, editorial hero, product screenshot hero, etc.
- [ ] **No dead whitespace rhythm.** Spacing must follow one scale (4/8/12/16/24/32/48/64/96...), not random 18px/37px gaps.
- [ ] **No fake "app store" 5-column footer** on a product that has 5 links total.

### Typography
- [ ] **No Inter/Roboto as an unconsidered default.** If a grotesk is right for the style, fine — but it must be a decision from the style DNA.
- [ ] **No single-size body text everywhere.** Hierarchy needs ≥ 3 distinct type roles per screen.
- [ ] **No ALL-CAPS paragraphs.** Uppercase is for labels/eyebrows only, never body.
- [ ] **No fake letter-spacing on serif display faces** (unless the style demands it).

### Content honesty
- [ ] **No invented fake statistics** ("99.9% uptime", "10x faster", "Trusted by 50,000+ teams") unless real numbers exist. Fake precision reads as slop instantly.
- [ ] **No random testimonials with stock-photo names.** "Sarah J., CEO" with no company = slop.
- [ ] **No logo walls of companies that never agreed to it.**
- [ ] **No lorem ipsum or filler copy.** Every heading should be real, specific, and benefit-led.

### Icons & imagery
- [ ] **No mismatched icon families** (mixing filled, outlined, and 3D icons on one screen).
- [ ] **No random emoji as feature icons** in a professional context.
- [ ] **No AI-generated abstract 3D shapes floating in the hero** unless the style is explicitly 3D/Spatial.
- [ ] **No screenshots of a product that doesn't exist** dressed up as "real UI" — label mock UI as such.

### Motion
- [ ] **No animations without reduced-motion fallback** (`prefers-reduced-motion`).
- [ ] **No 900ms ease transitions on hover.** Hover feedback: 150-250ms.
- [ ] **No parallax on dense content pages** — motion belongs in heroes and storytelling sections.

## Scoring the checklist

- 0 hits → ship.
- 1-2 hits on decoration patterns → fix and ship.
- Any hit on fake statistics / fake testimonials / lorem ipsum → mandatory fix, these destroy trust.
- 3+ hits → the design has not been designed. Return to SKILL.md step 1.
