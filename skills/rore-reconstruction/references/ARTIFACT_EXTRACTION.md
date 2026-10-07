# Artifact / Extraction Reconstruction

Use format-first dispatch.

1. identify container/file/package type and strongest target identity;
2. inventory before deep extraction;
3. choose a compatible extractor/parser;
4. validate semantic output, not just exit status;
5. use bounded fallback/alternate providers if expected information value remains high;
6. recurse through nested containers intentionally while preserving parent→child lineage;
7. keep originals authoritative and derived outputs reproducible/disposable where practical.

`extractor exit 0 != meaningful extraction success`.

Record failed extraction/parser attempts when they narrow the format hypothesis. Preserve source/layer precedence for base + patch/override/resource combinations.
