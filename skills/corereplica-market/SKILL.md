---
name: corereplica-market
description: Research sourced user feedback and alternatives, derive product-positioning opportunities, define an independent brand profile, and prepare launch/pricing/store material. Use for review analysis, "what users hate", differentiation, naming/brand voice, pricing, landing pages, app-store listings, or launch planning. Do not invent reviews/proof, treat current prices/store rules as timeless, or directly become the Design-System owner.
---

# CoreReplica Market

Own market/review evidence, positioning, brand identity/profile and launch material. Product scope changes that follow from this work remain Product Truth decisions and must be routed through `corereplica-product`.

Read only the material JIT reference:

- `references/REVIEW_RESEARCH.md` — sourced complaints/requests/opportunity analysis;
- `references/BRAND_AND_POSITIONING.md` — name/voice/brand-profile boundaries;
- `references/LAUNCH_AND_LISTING.md` — pricing, landing, store listings, current platform rules.

## Invariants

- Never invent reviews, quotes, user counts, ratings, testimonials, press logos or "trusted by" proof.
- Every external factual claim used for market decisions has a source; current prices/platform rules carry an observation date when material.
- Review research describes evidence about the market/reference; it does not silently add product requirements.
- Brand identity/profile is an input to the Design/Build path, not a second owner of component/layout semantics.
- A clean residue scan is narrow evidence only; it does not prove trademark/trade-dress/legal clearance.
- Trademark/domain/store/handle availability and current platform policies are current external facts: verify them with appropriate current sources before consequential use.

## Fallback outputs

```text
corereplica/market/FEEDBACK.md
corereplica/market/POSITIONING.md
corereplica/market/BRAND_PROFILE.json
corereplica/market/LAUNCH/landing.md
corereplica/market/LAUNCH/pricing.md
corereplica/market/LAUNCH/listing.json
corereplica/market/LAUNCH/launch-plan.md
```

Use the bundled deterministic helpers only for their narrow evidence roles:

- `reviews.py` analyses user-supplied/sourced review rows;
- `sweep.py` searches configured names/domains/colors in text/code paths;
- `listing.py` checks configured listing constraints and copy-residue rules.
