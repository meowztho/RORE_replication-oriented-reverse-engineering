# Brand and Positioning

Brand work must create an identity distinguishable from the reference and coherent with the target product's own audience/value proposition.

Recommended `BRAND_PROFILE.json` fields:

```json
{
  "name": null,
  "positioning": null,
  "voice": [],
  "palette_roles": {},
  "asset_direction": null,
  "avoid": [],
  "domains": [],
  "reference_colors": []
}
```

`palette_roles` supplies values/identity guidance to the Design-System owner; it does not redefine component semantics.

## Naming/identity screen

Generate enough candidates to compare distinct naming directions, then reject candidates that are confusingly close to the reference or obviously crowded in the same category. Before consequential spend/launch, verify current trademark, domain, store and relevant handle facts with dated sources. These are screening checks, not legal clearance.

## Voice and assets

Define a small voice contract with positive/negative examples and rewrite high-visibility target strings freshly. For an independent target, default logo/icon/illustration direction to independently created or appropriately licensed material and distinguish it from the reference where that is part of Product Truth. Reuse of existing identity/content requires the canonical source/use/distribution basis for the intended use. Preserve usable small-size/icon constraints where relevant.

## Residue sweep

Use `sweep.py` only as a narrow deterministic residue detector for configured names/domains/colors. A clean sweep does not prove trademark, trade-dress or broader legal clearance; visual/manual review still matters.
