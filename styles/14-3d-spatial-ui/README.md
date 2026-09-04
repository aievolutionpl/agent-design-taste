# 14 · 3D Spatial UI

**Overview:** Interfaces built in depth, not just on a plane. Content lives on layers in a shared perspective space — the camera (scroll/cursor) moves, and the interface moves with it. Depth is used to explain relationships: foreground = interactive, background = context.

**Visual principles:** real perspective · layered z-space · parallax storytelling · one vanishing point · depth through position not decoration · vanilla CSS 3D transforms (no libraries required) · motion serves spatial comprehension.

## Typography
- **Recommended families (Google Fonts):** Display: Space Grotesk, Clash-adjacent — use Space Grotesk. Text: Inter. Mono: Space Mono, IBM Plex Mono.
- **Pairing:** Space Grotesk (H1–H2, 500–700) + Inter (H3–body) + Space Mono (labels/coordinates/depth data).
- **Scale:** H1 60/64 · H2 42/50 · H3 26/34 · H4 21/30 · H5 18/26 · H6 16/24 · body 17/1.6 · small 14/1.5.
- **Body:** 17px, line-height 1.6, letter-spacing 0. Measure 62ch. Headlines may get slight negative tracking (-0.02em); body never.
- **Uppercase:** 11–12px mono labels with +0.12em tracking for layer/coordinate annotations ("LAYER 02 · Z:-120PX") — a signature detail of the style.
- **CSS:**
```css
h1 { font: 700 60px/1.06 'Space Grotesk'; letter-spacing: -0.02em; }
body { font: 400 17px/1.6 'Inter'; }
.layer-label { font: 500 11px/1 'Space Mono'; letter-spacing: 0.12em; text-transform: uppercase; }
```
- **Typical mistakes:** italic faux-3D text; type rotated more than ~8°; headings transformed in Z until blurry; body copy inside tilted planes.

## Layout & Frames
- **Grid:** normal 12-col grid on the content plane; depth is added *around* the grid, not instead of it. Max-width 1200px.
- **3D stage:** a `.scene` wrapper gets `perspective: 1200px` (one per section — never competing perspectives), children get `transform-style: preserve-3d`.
- **Layers:** 2–4 meaningful layers per section (e.g. card at z:0, floating panel at z:60px, ambient shape at z:-150px). Beyond 4 layers it becomes noise.
- **Parallax:** scroll-driven translateZ/translateY offsets on layers; cursor-parallax only in the hero, ±10px max, lerped.
- **Hero:** full-viewport scene with a centered/exploded composition — product UI plane straight-on, supporting planes rotated on Y (rotateY ±12–20°) and offset in Z.
- **Frame patterns:** spatial hero, layered feature cards (stack in Z, fan out on hover/scroll), exploded diagram sections, flat-pricing (keep pricing FLAT — depth here hurts conversion), spatial footer.
- **Responsive:** below 900px collapse depth: remove rotateY, drop parallax, keep only soft shadow layering. Never make users scroll through mandatory 3D on mobile.

## Visual hierarchy
- First seen: the object closest to camera (hero plane), then H1, then CTA. Depth must reinforce hierarchy: the thing you want clicked is in front, larger, shadowed; context recedes. One primary CTA per view.

## Color system
- **Light:** bg #F4F4F0 (slightly warm so white planes float) · surface #FFFFFF · text #0E0E10 · secondary #5A5A5E · border #E3E3DE · accent #4F46E5 (indigo) used for interaction + depth-edges only.
- **Dark:** bg #060608 · surface #101014 · text #F2F2F0 · secondary #8E8E94 · border #1F1F26 · accent #8B8BF5. Dark mode is the natural home of this style — planes read as lit objects.
- Ambient/atmosphere layers may use large soft radial glows of the accent at ≤12% opacity. Avoid: rainbow depth (each layer a different hue), neon on light bg.

## Components
Buttons: solid primary with a 1px top-edge highlight (light inset line) to feel dimensional; hover lifts translateZ(8px)+shadow, 200ms. Cards: planes with real shadow depth (soft, large-blur, low-opacity — `0 24px 60px -24px rgb(0 0 0 / 0.25)`), tilt max 6° on hover. Navbar: flat, on the content plane — do not float the nav in 3D. Inputs: flat, 1px border; only focus state lifts. Modals: rise out of the page (scale 0.96→1 + translateY) not full rotateX flips. Badges/chips: flat. Depth annotations: mono micro-labels on layer edges. Never: text buttons rotated in 3D, 3D carousels for navigation.

## Shape language
Planes are rounded rectangles, radius 12–16px — radius does not grow with depth. Depth cues, in order of preference: (1) actual Z-position + perspective, (2) large soft shadow, (3) slight desaturation/blur of far layers, (4) scale. Corners of rotated planes may show 1px accent edge-light. No skeuomorphic bevels, no textured "3D" PNG blobs.

## Visual direction
Fits: product screenshots on tilted planes, isometric/exploded diagrams, subtle grid or dot floor extending to a horizon, gradient atmospheres (very restrained), soft glows. Breaks cohesion: flat illustrations competing with 3D planes, emoji, heavy skeuomorphism (wood, glass+metal mixed), more than one perspective per viewport.

## Motion & Interaction
Everything motion does should answer "how is this arranged in space?" Signature moves: scroll-driven layer parallax (staggered speeds), hover lift translateZ(8–12px), card fan-out (adjacent cards rotateY ∓6°, translateZ ∓40px), slow ambient rotation (60s+ loops, small amplitude). Durations 300–500ms, `cubic-bezier(0.16, 1, 0.3, 1)`. **Fallbacks are mandatory:** `@media (prefers-reduced-motion: reduce)` kills parallax/rotation and flattens transforms to static layering with shadows; also provide a JS-free static appearance if JS is off (CSS-only scroll effects). If WebGL is used it must be a decorative layer that can be removed with zero content loss — content stays in DOM/HTML.

## When to use
Product launches (especially dev tools, AR/VR/spatial apps, hardware, mapping), interactive storytelling, portfolio hero moments, feature explanations where "layers" is literally the product story. Audience expects wow and will tolerate scroll friction.

## When NOT to use
Dense B2B dashboards, docs, checkout, healthcare/finance trust-critical flows, accessibility-first products, anything users must scan fast all day — depth taxes reading speed.

## Do
- One perspective per section; one shared vanishing logic per page
- 2–4 layers max, each with a reason to exist in Z
- Depth reinforces hierarchy (front = action)
- Real CSS: `perspective`, `preserve-3d`, `translateZ`, `rotateY`
- Big soft shadows + far-layer desaturation as depth cues
- Mono coordinate/layer labels as a craft detail
- Dark mode first; light mode needs stronger shadows
- Ship the reduced-motion flattened version and test it

## Don't
- rotateX(45deg) walls of text
- Depth for decoration with no informational meaning
- Floating 3D stock blobs/illustrations pasted on a flat page
- Parallax on body text or navigation
- 3D-flip carousels as primary navigation
- Mandatory 3D interactions on mobile
- More than one accent color "per dimension"
- WebGL for content that could be a plane

## Anti AI-slop (3D spatial edition)
Random purple orbs, floating glass cubes, "3D abstract shapes" hero renders with no relation to content, every card rotateY(15deg), scroll-jacked full-page 3D scenes, Spline embeds where a screenshot would do. Slop = depth without meaning.

## Good vs Bad examples
- **Good:** Linear/Arc-style product heroes — a flat, readable UI plane, gently tilted, with supporting layers parallaxing behind; depth explains the product.
- **Bad:** a landing page where the entire content column is rotated in perspective, text blurs, and a purple 3D blob covers the CTA — motion sickness, zero comprehension.