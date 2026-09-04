# 01 · Minimalism

**Overview:** Less but better. Every element earns its place through function; whitespace, type and one accent color do all the expressive work.

**Visual principles:** extreme restraint · generous whitespace · one accent color · typography-led hierarchy · invisible chrome · content is the interface.

## Typography
- **Recommended families (Google Fonts):** Text/Sans: Inter, Instrument Sans, Jakarta Sans. Grotesk: Archivo. Serif accent (optional): Newsreader. Mono: IBM Plex Mono.
- **Pairing:** Archivo (H1–H2, 600) + Inter (H3–body) + IBM Plex Mono (labels/data).
- **Scale:** H1 56/64 · H2 40/48 · H3 28/36 · H4 22/30 · H5 18/26 · H6 16/24 · body 17/1.6 · small 14/1.5.
- **Body:** 17px, line-height 1.6, letter-spacing 0. Measure 65ch.
- **Uppercase:** only 11–12px eyebrow labels, +0.1em tracking, never headings.
- **CSS:**
```css
h1 { font: 600 56px/1.15 'Archivo'; letter-spacing: -0.02em; }
body { font: 400 17px/1.6 'Inter'; }
.eyebrow { font: 500 12px/1 'IBM Plex Mono'; letter-spacing: 0.1em; text-transform: uppercase; }
```
- **Typical mistakes:** thin (200) weights on dark bg; centered paragraphs; 6 weights in play; decoration instead of hierarchy.

## Layout & Frames
- **Grid:** 12-col, max-width 1200px, gutters 24px. Freeform only in hero.
- **Spacing:** 8-base scale; sections 96–128px apart.
- **Hero:** split hero or centered hero with one large image. Nothing floats.
- **Frame patterns:** split hero, centered hero, alternating features, full-bleed image sections.
- **Responsive:** drop gutters to 16px, H1→34px mobile, stack split heroes.

## Visual hierarchy
- First seen: H1, then primary CTA, then hero visual. One primary action per screen. Eye path: headline → sub → CTA → proof.

## Color system
- **Light:** bg #FFFFFF · surface #F7F7F5 · text #111111 · secondary #555555 · border #E5E5E2 · primary action #111111 · accent #2563EB (one only).
- **Dark:** bg #0A0A0A · surface #161616 · text #F5F5F4 · border #262626 · accent same.
- Saturation near-zero except accent. Avoid: pastel gradients, second accent, colored section backgrounds.

## Components
Buttons: solid black (or white on dark), 12px radius max, no shadows. Cards: flat, 1px border, no elevation. Navbar: 64px, logo left, 3–5 links, text CTA. Inputs: 1px border, 8px radius, label above. Tabs: underline indicator. Pricing: whitespace separates plans, no "most popular" confetti. Dashboards: border-separated, not shadow-separated. Modals: plain panel, dim backdrop. Badges: outline only. Tooltips: dark, minimal. Tables: hairline rows.

## Shape language
Radius 8–12px (or 0 for sharp minimal). Borders over shadows. Depth = spacing, not elevation. No strokes on icons > 1.5px relative weight.

## Visual direction
Fits: real photography (one treatment), line icons, no illustration, no 3D, no grain. Breaks cohesion: gradients, mixed icon fills, decorative blobs, emoji.

## Motion & Interaction
Minimal: hover 150ms ease-out (opacity/border), reveals translateY 16px/400ms once. `prefers-reduced-motion`: disable all. If it needs motion to be interesting, the design failed.

## When to use
SaaS, fintech, health, corporate, enterprise, premium/luxury-adjacent, dev docs. Audience expects clarity and trust.

## When NOT to use
Youth brands needing personality, events, gaming, kids products — minimalism reads cold; maximal/expressive styles convert better there.

## Do
- One accent color, used for actions only
- Whitespace at section level (96px+)
- Real photography, single treatment
- Hairline borders, flat surfaces
- Typography carries hierarchy
- Left-align body text
- One primary CTA per view
- Kill any element you can't justify

## Don't
- Gradients "for depth"
- Three font families
- Decorative illustration
- Colored info-box sections
- Shadow stacking
- Uppercase headings
- More than one accent
- Fake stats filling whitespace

## Anti AI-slop (minimalism edition)
Purple accents, glass cards, gradient text, "Trusted by 50,000+ teams" walls, floating 3D shapes — all slop here. In minimalism slop = anything added without function.

## Good vs Bad examples
- **Good:** Stripe docs — flat surfaces, hairlines, one blue, type does everything.
- **Bad:** minimalist landing with glass nav, gradient blob hero and neon CTA — three styles fighting, zero restraint.
