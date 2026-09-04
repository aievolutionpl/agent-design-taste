# 08 · Claymorphism

**Overview:** Puffy, touchable 3D. Elements look like soft clay or marshmallow — inflated shapes with dual shadows (inner highlight + soft outer drop) on pastel backgrounds. Playful, friendly, toy-like but still structured.

**Visual principles:** puffy inflated surfaces · large radii (24–40px) · dual shadow trick (light inner top + colored soft outer) · soft pastel base with one saturated accent · chunky everything · flat pastel bg, no texture.

## Typography
- **Recommended families (Google Fonts):** Display: Baloo 2, Fredoka, Nunito. Body: Nunito Sans, Quicksand. Mono (rare): Space Mono.
- **Pairing:** Baloo 2 (H1–H3, 600–700) + Nunito Sans (body, 400/700 for emphasis).
- **Scale:** H1 52/60 · H2 36/44 · H3 26/34 · H4 20/28 · body 16/1.6 · small 14/1.5.
- **Body:** 16px, line-height 1.6, medium-to-round letterforms, measure 60–65ch.
- **Uppercase:** almost never — round fonts fight uppercase; only tiny badges, wide tracking.
- **CSS:**
```css
h1 { font: 700 52px/1.15 'Baloo 2'; letter-spacing: -0.01em; }
body { font: 400 16px/1.6 'Nunito Sans'; }
.btn { border-radius: 999px; box-shadow: inset 0 -4px 0 rgb(0 0 0 / .15), 0 12px 24px rgb(76 29 149 / .25); }
```
- **Typical mistakes:** sharp geometric sans (Inter everywhere) killing the softness; tiny dense type; ultra-bold 800 everywhere = balloon; thin weights (clay is chunky, never 300).

## Layout & Frames
- **Grid:** 12-col, max-width 1140px, gutters 24px. Cards float on pastel bg — spacing is generous, 80–96px between sections.
- **Spacing:** 8-base scale; clay needs air between puffy elements so shadows don't collide (min 24px gap between elevated cards).
- **Hero:** centered hero with one big puffy illustration/3D blob-object, or split hero with puffy card mockup.
- **Frame patterns:** centered hero, puffy card grids, stacked feature cards, CTA band as giant pill.
- **Responsive:** single column under 900px, H1→32px, cards full-width with 16px padding, shadows scale down (smaller y-offset).

## Visual hierarchy
- First seen: big rounded H1, then the puffy CTA (strongest shadow = strongest pull), then hero object. Eye path: headline → illustration → CTA → features. One saturated element per zone; everything else pastel.

## Color system
- **Light:** bg #F5F1FA (soft lilac) · surface #FFFFFF · text #2D2438 · secondary #6B5E7F · border rgba(0,0,0,.06) · primary #7C5CFC · accent #FF8FA3 (pink) · success #4ADE80.
- **Dark:** bg #1E1830 · surface #2A2142 · text #F3EFFA · secondary #B8A9D9 · shadows become deeper purple-black; keep the same pastel hues, dim surfaces not hues.
- Saturation: pastels for large fields (bg, sections), ONE saturated primary for CTAs, optional second pastel-hue accent. Avoid: neon, pure black text on pastel feels harsh — use deep desaturated plum.

## Components
Buttons: pill radius (999px) or 20px, 2px bottom inset shadow "press" look, active state pushes down (translateY 2px, inset deepens). Cards: 24–32px radius, `box-shadow: 8px 8px 24px <hue-tinted>, -8px -8px 24px #fff` (neumorphic-adjacent) or single soft drop + 1px inner top highlight. Navbar: floating pill, detached from top, 16px radius. Inputs: 20px radius, inner shadow inset 0 2px 6px, thick pastel focus ring. Tabs: puffy segmented control — active segment inflated. Pricing: puffy cards, popular plan lifted higher + saturated border. Badges: pill, tinted bg, no border. Toggle: clay pill with round knob casting its own shadow. Icons: filled, rounded-corner (Material Round), never sharp line icons.

## Shape language
Radius 20–40px everywhere; pills for actions; circles for avatars/badges. Depth = dual shadows (light from top-left, tinted drop bottom-right). NO sharp corners, NO 1px borders as primary device — shadow does separation. Illustration style: rounded blob characters, chunky 3D renders, thick rounded strokes.

## Visual direction
Fits: 3D clay renders, rounded blob illustrations, pastel gradient mesh backgrounds (subtle), filled rounded icons, emoji-scale mascots. Breaks cohesion: sharp line icons, hairline borders, photography (usually), brutalist type, neon gradients.

## Motion & Interaction
Bouncy but short: 250–350ms, spring-like ease `cubic-bezier(.34,1.56,.64,1)`. Hover: scale 1.03 + shadow lift; press: translateY(2px) + inset deepens. Entrance: pop-in scale 0.9→1 with overshoot, staggered 60ms. `prefers-reduced-motion`: all transforms off, opacity fades only. Never infinite bouncing loops — one overshoot, then rest.

## When to use
Kids/education apps, habit & wellness apps, consumer fintech for young audiences (pocket money apps), playful SaaS (design tools for beginners), game landing pages, NFT/web3 consumer products.

## When NOT to use
Enterprise, legal, healthcare-critical, B2B infrastructure, dev tools — puffy reads unserious; minimalism or Swiss styles convert better there. Also avoid for content-heavy products (news, docs) — clay shadows fight dense text.

## Do
- Dual-shadow recipe on every elevated surface
- 24px+ radius minimum, pills for buttons
- Pastel bg with ONE saturated CTA hue
- Round fonts (Baloo 2 / Fredoka / Nunito)
- Generous gaps so shadows don't collide
- Press-down active states (inset shadow deepens)
- Rounded filled icons only

## Don't
- Hairline borders + flat cards (that's minimalism, not clay)
- Sharp corners anywhere
- Thin/light font weights
- Neon saturation on large fields
- Six different pastel hues competing
- Real photography mixed with clay 3D
- Infinite bounce animations

## Anti AI-slop (claymorphism edition)
Purple-gradient hero + glass nav + emoji icons pasted on puffy cards = slop. Glassmorphism and clay don't mix — pick one. No random blob SVGs with no relationship to the clay system, no "10,000+ happy users!" pill confetti, no neon-on-pastel contrast crimes.

## Good vs Bad examples
- **Good:** a kids' pocket-money banking app — pastel lilac bg, puffy white cards with soft plum shadows, one coral CTA pill, round mascot, everything begs to be touched.
- **Bad:** pastel landing with glass nav, sharp Inter type, hairline-bordered cards, neon green gradient CTA — four styles, zero clay.