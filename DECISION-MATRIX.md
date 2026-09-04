# Product → Style Decision Engine

Do not pick a style because it "looks cool". Pick it because the product,
audience, and brand personality demand it. Work top-down:

```
Product type → Audience → Brand personality → Content density
→ Emotion → Dominant style → (optional) Supporting style → Visual direction
```

## 1. Decision table

| Product type | Audience | Personality | Density | Recommended dominant | Supporting | Avoid |
|---|---|---|---|---|---|---|
| B2B SaaS | managers, teams | trustworthy, clear | medium | Minimalism (01) | Swiss (10) | Maximalism, Y2K |
| Dev tool / AI platform | developers | technical, fast, precise | medium-high | Swiss (10) | subtle Brutalism (06) | Claymorphism, pastel gradients |
| Fintech / banking | professionals | secure, precise | medium-high | Minimalism (01) | Swiss (10) | Neo-Brutalism, Y2K |
| E-commerce (mass) | everyone | friendly, clear | high | Bento Grid (04) | Minimalism (01) | Anti-Grid, Skeuomorphism |
| Luxury / fashion | high-income | exclusive, refined | low | Editorial (11) | Minimalism (01) | Neon anything, gradients |
| Agency / studio | creative clients | bold, original | low-medium | Brutalist/Anti-Grid (06) | Kinetic Typography (15) | Neumorphism, Bento |
| Portfolio (designer) | art directors | expressive, memorable | low | Kinetic Typography (15) | Anti-Grid (06) | Dashboard layouts |
| Media / magazine | readers | intelligent, literary | high | Editorial (11) | Swiss (10) | Glassmorphism overload |
| Consumer app (social/lifestyle) | 18-35 | modern, fluid | medium | Liquid Glass (03) | Bento (04) | Skeuomorphism (heavy) |
| Kids / education | children, parents | playful, safe | medium | Claymorphism (08) | Maximalism (12) | Brutalism, dark modes |
| Web3 / metaverse | early adopters | futuristic, immersive | medium | 3D/Spatial (14) | Glassmorphism (02) | Editorial serif |
| Music / events / gaming | fans | loud, nostalgic | high | Y2K (13) | Maximalism (12) | Minimalism |
| Health / wellness | broad | calm, human | low-medium | Minimalism (01) | Claymorphism (08) | Neon, harsh contrast |
| Restaurant / local biz | locals | appetizing, warm | medium | Editorial (11) | Neo-Brutalism (05) | 3D spatial, dark SaaS |
| Corporate / enterprise | executives | serious, stable | high | Swiss (10) | Minimalism (01) | Y2K, Maximalism |

## 2. Personality → style shortcuts

- "technical / fast / precise" → Swiss + mono accents
- "bold / rebellious" → Neo-Brutalism or Anti-Grid
- "premium / exclusive" → Editorial with generous whitespace
- "friendly / approachable" → Claymorphism or rounded Bento
- "futuristic / immersive" → Spatial 3D or Liquid Glass
- "nostalgic / fun" → Y2K
- "human / literary" → Editorial
- "organized / structured" → Bento or Swiss

## 3. Content density override

- **Low density + few screens** → allow expressive styles (15, 06, 12, 13).
- **High density (dashboards, tables)** → structural styles only (01, 04, 10);
  expressiveness goes into micro-interactions, not layout.
- If a client demands an expressive style for a dense product → keep layout
  structural, apply the expressive style to hero and marketing pages only.

## 4. Worked example

Input: *"AI coding platform for developers"*

```
Audience: developers
Brand personality: technical / fast / precise
Content density: medium-high
Primary action: start free trial
Recommended style: Swiss (10) + subtle Brutalist accents (06)
Typography: Inter (UI) + JetBrains Mono (code, labels)
Visual direction: real product UI, terminal windows, technical diagrams
Avoid: clay characters, pastel gradients, excessive glass, neon purple
```

Notice: the answer is a **brief**, not a stylesheet. That's the point.

## 5. Tie-breakers

1. If two styles score equally → pick the one with better accessibility.
2. If the brand already has colors/fonts → keep them, choose the style that
   accommodates them.
3. If still unsure → Minimalism. It is the neutral default that rarely fails.
