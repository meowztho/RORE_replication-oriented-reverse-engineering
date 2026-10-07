# Workspace and Target Identity

Keep these roles distinct where material:

```text
raw/reference evidence
scratch/intermediate derivatives
RORE control/evidence graph
actual analyzed target/runtime
```

Do not contaminate a binary/package/install merely by placing RORE metadata inside it.

Bind analysis state to the strongest practical target identity available: SHA-256/content hash, signed build ID, package version plus hash, Git revision, URL+deployment/environment identity, dataset revision, or a generated evidence-run identity with recorded hashes.

A previous workspace from another version is evidence/history, not current truth. Re-resolve semantic anchors before carrying names, offsets, structure or findings forward.
