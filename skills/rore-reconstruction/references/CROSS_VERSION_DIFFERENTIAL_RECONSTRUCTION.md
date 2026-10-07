# Cross-Version / Differential Reconstruction

Use changed builds, patches, old/new binaries, schemas or behavior to reveal semantics.

Bind each side to a strong identity. Align using semantic anchors rather than raw addresses:
- exports/symbols;
- strings and xrefs;
- constants/magic values;
- types/vtables/schema fields;
- call relationships;
- code/control patterns;
- data references;
- runtime behavior.

Diffs can reveal newly added validation, locks, zeroing, bounds, state transitions or removed paths. Infer the mechanism cautiously: a patch pattern suggests a hypothesis, not automatically the complete root cause.

Names recovered from an older symbolized build may be useful hypotheses for a newer build, but re-establish the mapping in the current artifact before promoting them.

Never transplant old raw offsets as durable truth merely because nearby code looks similar.
