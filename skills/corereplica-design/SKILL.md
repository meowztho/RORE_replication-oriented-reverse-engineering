---
name: corereplica-design
description: Translate allowed visual/reference evidence into an independent semantic design system: layout roles, spacing/type scales, states, components, accessibility, and brand-input seams. Use for design-system reconstruction, UI consistency, visual hierarchy, tokens, responsive/component behavior, or comparison to reference screenshots. Do not copy proprietary assets/copy or let brand become a second design-system owner.
---

# CoreReplica Design

Own the **semantic Design-System contract** for CoreReplica fallback artifacts. Reference screenshots are evidence; they are not shippable assets or Product Truth.

## Boundary

```text
reference visual evidence
→ design semantics/roles
→ independent Design-System contract
← brand profile values/identity inputs
→ effective target UI
```

Market/brand may supply identity values and voice. It does not own component/state/layout semantics.

## Procedure

1. Read the applicable target product requirements first. Do not design every observed reference screen if the target product rejected/deferred it.
2. Measure/reference roles rather than copying signature values: information hierarchy, density, spacing rhythm, type roles, component states, responsive behavior, focus/error/loading/empty semantics.
3. Define semantic tokens such as `surface`, `text-muted`, `accent`, `danger`, spacing/type/radius/motion roles. Avoid target components hard-coding reference-specific values.
4. Use open/licensed fonts/icons/assets or original assets owned by the user. Write copy fresh.
5. Define component contracts once with variants, states, keyboard/screen-reader semantics and target requirement/surface usage.
6. If the project already has a Design System owner, extend/reuse it through Core-First rather than creating a CoreReplica-specific parallel component library.
7. Store brand identity separately when useful (`corereplica/market/BRAND_PROFILE.json`). Consume it through declared token/profile inputs.
8. Use the included `contrast.py` only as deterministic contrast evidence. Passing token pairs does not prove the rendered application is accessible.

## Fallback outputs

```text
corereplica/design/DESIGN_SYSTEM.md
corereplica/design/tokens.json
corereplica/design/COMPONENTS.md
```

For material visual/layout requirements, verification must later compare the real rendered target surface to the applicable target Design/Product authority, not merely to the reference screenshot.
