# Mode Routing — load the right slice

Loading the whole skill for every prompt causes scope creep (the agent audits
when asked to implement, rewrites copy when asked to harden). Resolve the mode
from the user's verb + artifact BEFORE loading references.

| User verb / artifact | Mode | Load |
|---|---|---|
| "design", "explore", "koncepcja" | **Shape** | SKILL.md steps 1-4 + DECISION-MATRIX + style README |
| "build", "implement", "zrób stronę" | **Implement** | style tokens + COMPONENT-PATTERNS + LAYOUT-PATTERNS + ANTI-SLOP |
| "review", "audit", "oceń" | **Review** | DESIGN-TASTE-SCORE + ANTI-SLOP + style Do/Don't |
| "rewrite copy", "texty" | **Copy** | content honesty rules from ANTI-SLOP only |
| "polish", "harden", "dopracuj" | **Harden** | DESIGN-TASTE-SCORE + TASTE-LOOP records + motion foundations |

## Observable rules only

Encode guidance as **checkable predicates**, never adjectives:

- ✅ "Destructive actions use Verb + Noun" ("Delete project", not "Are you sure?")
- ✅ "Body text ≥ 16px, contrast ≥ 4.5:1, one H1 per page"
- ❌ "Buttons should feel clear and modern" — unverifiable, wastes context.

Research note (SWE-bench, Zhang et al. 2026): negative constraints help;
individually-piled positive directives degrade output. Keep the Do lists short;
let the Don't lists do the work.

## Coverage gaps — never invent policy from silence

If a project's design file doesn't decide something (e.g. no dark-mode spec),
the agent must **ask or flag it**, not pattern-match from the nearest exemplar
and ship an accidental decision.
