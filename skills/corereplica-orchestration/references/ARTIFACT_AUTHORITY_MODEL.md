# CoreReplica Artifact Authority Model

Use project-native authorities when they already exist. The `corereplica/` layout is a fallback namespace, not a demand to duplicate a mature project's truth.

## Truth layers

```text
Reference Truth
  observations about another product, sources, screenshots, inferred clues

Product Truth
  what this product should do/feel/include/exclude, including adopt/adapt/reject decisions

Implementation State
  current work/progress/revision; useful for execution but not acceptance authority

Verification Truth
  what current evidence proves on a specified boundary/revision

Release Approval
  authorization to cross a consequential transition; not implied by any other layer
```

Recommended fallback artifacts:

```text
corereplica/reference/REFERENCE_MODEL.md
corereplica/reference/FEATURE_OBSERVATIONS.csv
corereplica/reference/SOURCE_LOG.md

corereplica/product/PRODUCT_SCOPE.md
corereplica/product/REQUIREMENTS.csv

corereplica/design/DESIGN_SYSTEM.md
corereplica/design/tokens.json

corereplica/implementation/IMPLEMENTATION_STATUS.csv
corereplica/implementation/BUILD_LOG.md

corereplica/verification/EVIDENCE.json
corereplica/verification/FINDINGS.md
corereplica/verification/PARITY.md

corereplica/market/FEEDBACK.md
corereplica/market/BRAND_PROFILE.json
corereplica/market/LAUNCH/

corereplica/release/RELEASE_GATE.md
```

`REQUIREMENTS.csv` does not contain a builder-owned `done`, `clone`, or `verified` field. Implementation status and verification evidence are separate inputs.
