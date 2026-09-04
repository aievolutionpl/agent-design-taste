# Visual Language Foundations

Imagery, texture, light and icons. The style DNA chooses from this menu;
**consistency within one project is mandatory** — a page with three visual
languages has none.

The failure mode this file prevents: an agent that gets tokens right and then
drops a stock photo, a 3D blob and two icon families onto the same screen.

---

## 1. The four decisions, made once per project

Before generating any visual, commit to these. Write them into `DESIGN.md`.

| Decision | Options | Applies to |
|---|---|---|
| **Photography treatment** | natural · warm grade · cool grade · duotone · B&W · none | every photo |
| **Icon family** | one library, one weight, one fill style | every icon |
| **Illustration / 3D system** | flat vector · line art · character · clay 3D · glass 3D · chrome · none | every drawn asset |
| **Background treatment** | flat · subtle grain · single gradient · pattern · texture · none | every section |

Four answers. Then every asset either fits or does not get made.

---

## 2. Photography

| Mode | Looks like | Use for |
|---|---|---|
| **Documentary** | Real spaces, natural light, imperfect | Hospitality, restaurants, local business, NGOs |
| **Studio clean** | Consistent background, consistent angle, controlled shadow | E-commerce, product, hardware |
| **Candid human** | People mid-action, not posed at camera | SaaS trust sections, teams, careers |
| **Environmental portrait** | A person in their actual context | Founders, case studies, testimonials |
| **Architectural** | Hard geometry, strong lines, high contrast | Swiss, corporate, real estate |

**Cropping and focal point**
- Crop to the subject, not to the frame. A 16:9 hero becomes a 4:5 mobile crop
  centred on the face or the object — not the same image letterboxed.
- Place the focal point on a third-line, not dead centre, unless the composition
  is deliberately symmetrical.
- Leave a scrim zone: if text overlays the image, the crop must reserve a
  low-detail region for it, and the scrim is a gradient — never lowered text opacity.

**Slop signals** — people pointing at laptops · a diverse group laughing at a
whiteboard · anyone in a headset gesturing at a hologram · the same photo with
a different color overlay used as three "different" images.

---

## 3. Product screenshots — the highest-value visual you have

For most software, a real screenshot beats every illustration you could make.

- **Real > mock > nothing.** If you must mock, label it as a mock.
- **Frame consistently**: one browser or device chrome, one radius, one border,
  one shadow, across every screenshot on the site.
- **Crop for legibility.** A full 1440px dashboard placed in a 600px slot is
  texture. Crop to the region that makes the point, at readable scale.
- **Never fabricate numbers** in a screenshot that contradict the page's claims,
  and never invent metrics that imply real customers. 🔴 blocker.
- **Annotate sparingly**: 3–5 callouts, with the text also present in the DOM.

---

## 4. Illustration

| Mode | Specification | Fits |
|---|---|---|
| **Flat vector** | Consistent stroke weight, ≤5 palette colors from tokens | Education, explainers, onboarding |
| **Line art** | Single color, 2px stroke, no fill | Swiss, technical docs, diagrams |
| **Character** | One character universe: same proportions, same palette | Kids, wellness, consumer onboarding |
| **Isometric** | One projection angle, one light direction | Infrastructure, process, systems |

**Slop signal**: mixing generated illustration styles from page to page, or one
"hero illustration" whose visual language appears nowhere else on the site.

---

## 5. 3D

- **Purpose**: hero objects, product visualisation, spatial navigation. Not
  decoration on every card.
- **One material system** per project: clay *or* glass *or* chrome *or* matte.
  Mixed materials read as an asset-store shopping trip.
- **One light setup**: same key direction, same intensity, across all renders.
- **Performance**: a WebGL canvas on mobile costs battery and frames. Ship a
  static render below 768px unless interaction is the point.
- **Slop signal**: an abstract 3D blob floating behind a hero, representing
  nothing. 🟠 in every style except 3D/Spatial, where it still needs a reason.

---

## 6. Diagrams

Underused, and often the most honest visual a technical product can show.

- Use the project's tokens for color; a diagram in unrelated colors reads as
  imported.
- Label everything. An unlabeled arrow is decoration.
- One diagram makes one point. Two points need two diagrams.
- Keep them in the DOM (inline SVG with `<title>`) rather than as flat images,
  so text scales, themes, and reaches screen readers.

---

## 7. Iconography

- **ONE family per project.** Match stroke weight (1.5–2px), corner radius, and
  fill style. A filled icon beside an outlined one beside an emoji is 🟠 slop.
- **Sizes on the grid**: UI icons 20–24px, feature icons 24–32px, never 17px.
- **Optical alignment** beats mathematical alignment — a triangle "play" icon
  needs 1–2px of extra left padding to look centred.
- **Icons support labels; they do not replace them.** Icon-only controls need
  `aria-label`, and outside universal metaphors (search, close, menu) they are
  a guessing game.
- **Slop signal**: a 4×3 grid of twelve generic outline icons, each loosely
  related to its feature name, none of them necessary.

---

## 8. Texture, grain, lighting

- **Grain**: 2–5% opacity noise adds print warmth. Works in editorial,
  brutalist, Y2K. One opacity value across the project.
- **Gradients**: max 1–2 per page, low saturation, *behind* content and never
  under body text. A gradient must encode something — depth, state, brand.
- **Lighting direction**: soft studio (consumer, wellness, clay) · hard
  directional (brutalist, fashion) · rim/neon (gaming, Y2K) · flat (Swiss,
  editorial, corporate). Pick one and keep the key light in one place.

---

## 9. Empty space

Whitespace is a material, not what is left over.

- Section spacing should **vary with meaning**. Identical 96px gaps between
  every section is rhythm-free.
- Space *above* a heading belongs to the section it opens.
- A crowded page and an empty page fail identically: neither has a hierarchy.
- Density is a decision from the brief (`S1`), not a consequence of how much
  content someone handed you.

---

## 10. Image direction per style

The concrete answer to "what should the pictures look like?"

| Style | Photography | Illustration / 3D | Texture | Never |
|---|---|---|---|---|
| **01 Minimalism** | One strong image, natural, generous margin | None | None | Decorative clutter, gradient blobs, icon grids |
| **02 Glassmorphism** | Vivid, blurred, as the layer *behind* glass | Subtle geometric shapes | Soft blur only | Glass over busy imagery; text on unblurred photos |
| **03 Liquid Glass** | Bright, saturated, high-key | Fluid organic forms | Refraction, caustics | Hard-edged technical diagrams |
| **04 Bento Grid** | One photo per tile, one treatment across all tiles | Small spot illustrations | Flat | Different image styles in adjacent tiles |
| **05 Neo-Brutalism** | High-contrast, hard crops, raw | Thick-stroke, flat, unshaded | Solid blocks, halftone | Soft gradients, drop shadows, glow |
| **06 Brutalist / Anti-Grid** | Raw, unretouched, deliberately imperfect crops | Photocopy, collage, ASCII | Scan lines, xerox grain | Polished stock, gloss, bevels |
| **07 Neumorphism** | Avoid photography — it fights the surface | Extruded soft shapes only | None | Any high-contrast imagery |
| **08 Claymorphism** | Rarely; if used, bright and simple | Soft 3D clay characters, one universe | Matte, soft shadow | Photorealism, harsh light, dark scenes |
| **09 Skeuomorphism** | Material close-ups: wood, metal, leather | Realistic controls, real reflections | Brushed metal, grain, stitching | Flat vector icons on tactile surfaces |
| **10 Swiss** | Architectural, hard crops, neutral grade, on the grid | Line art, 2px stroke, single color | None | Soft-focus lifestyle, warm grading, emoji |
| **11 Editorial** | Documentary and portrait, editorial grading, generous scale | Occasional pen-and-ink | Paper grain | Glass, 3D, gradient backgrounds |
| **12 Maximalism** | Bold, saturated, layered, collaged | Anything — but layered deliberately | Pattern on pattern, controlled | Text on pattern without a solid plate |
| **13 Y2K / Retrofuturism** | Retro-processed, high gloss | Chrome, gloss, starbursts, retro UI chrome | Controlled visual noise, lens flare | Muted minimalism, neutral greys |
| **14 3D / Spatial** | Rare; environment plates only | One coherent 3D material system, one light rig | Depth-of-field, soft shadow | Flat 2D icons floating in the 3D scene |
| **15 Kinetic Typography** | Rare; type is the image | Type as object | Motion blur, ghosting | Illustration competing with the type |

If a needed asset does not exist, the honest options are: use a real
screenshot, use a diagram, use typography, or use nothing. Inventing a fake
one is a 🔴 blocker.

---

## Per-project checklist

- [ ] One photography treatment, named in `DESIGN.md`
- [ ] One icon family, one weight, one fill style
- [ ] One illustration or 3D system — or an explicit "none"
- [ ] Grain/texture at one opacity, or absent
- [ ] Screenshots share one frame, one radius, one shadow
- [ ] Every image has meaningful `alt` (or `alt=""` if truly decorative)
- [ ] Mobile crops are *different crops*, not scaled-down desktop images
- [ ] No asset depicts something that does not exist
