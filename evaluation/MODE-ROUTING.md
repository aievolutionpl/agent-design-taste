# Mode Routing — load the right slice

Loading the whole skill for every prompt causes scope creep: the agent audits
when asked to implement, and rewrites copy when asked to harden. Resolve the
mode from the user's verb and artifact **before** loading any reference.

Mode answers *what to do*. Profile answers *how much to load*
(`docs/CONTEXT-PROFILES.md`). You need both.

| User verb / artifact | Mode | Load | Profile |
|---|---|---|---|
| "design", "explore", "concept" | **Shape** | SKILL.md steps 1–4 + DECISION-MATRIX + one style README | STANDARD |
| "build", "implement", "make the page" | **Implement** | style tokens + COMPONENT-PATTERNS + LAYOUT-PATTERNS + ANTI-SLOP | STANDARD |
| "review", "audit", "critique" | **Review** | DESIGN-TASTE-SCORE + ANTI-SLOP + the style's Do/Don't | LIGHT |
| "rewrite copy", "the words" | **Copy** | content-honesty rules from ANTI-SLOP only | LIGHT |
| "polish", "harden", "tighten" | **Harden** | DESIGN-TASTE-SCORE + TASTE-LOOP records + motion foundations | LIGHT |
| "redesign everything", "new identity" | **Rebuild** | the FULL profile — see `docs/CONTEXT-PROFILES.md` | FULL |

## Observable rules only

Encode guidance as **checkable predicates**, never adjectives:

- ✅ "Destructive actions use Verb + Noun" ("Delete project", not "Are you sure?")
- ✅ "Body text ≥ 16px, contrast ≥ 4.5:1, one H1 per page"
- ❌ "Buttons should feel clear and modern" — unverifiable, wastes context.

Practical consequence: keep the Do lists short and let the Don't lists carry
the weight. "Not like this" removes a whole region of the solution space;
"like this" only gestures at a point inside it.

## Coverage gaps — never invent policy from silence

If a project's design file doesn't decide something (e.g. no dark-mode spec),
the agent must **ask or flag it**, not pattern-match from the nearest exemplar
and ship an accidental decision.
