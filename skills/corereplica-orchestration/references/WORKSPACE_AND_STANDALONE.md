# Workspace Shape and Standalone Operation

Read when the target is not clearly a normal source repository, when CoreReplica artifacts could contaminate the runnable/shippable object, when no Git revision exists, or when Core-First Governance is unavailable.

## Classify the workspace before choosing paths

Use the smallest accurate shape:

- **source repository** — source + project metadata belong together;
- **binary/distribution package** — the directory contents may themselves be the product; extra files can invalidate packaging;
- **installed application** — installation state is evidence/input, not necessarily a writable project root;
- **artifact bundle** — document/media/config/package outputs with no repository semantics;
- **mixed workspace** — source/control plane and runnable/distributable targets are distinct.

Do not require Git merely because a procedure says `revision`. Use the strongest stable identity actually available: Git SHA, package/content hash, build ID/version, immutable evidence-run ID, or an explicitly local revision label tied to hashes. Never fabricate repository state.

## Separate control plane from product payload

CoreReplica fallback artifacts are project control metadata, not part of the replicated product unless the product contract explicitly requires them.

If placing `corereplica/` inside the target could change packaging, validation, signatures, runtime discovery, size, or user-visible contents, keep it outside the payload, for example in an adjacent project/control directory. Record the target path(s) and control-plane path in the project handoff.

## Companion mode

When Core-First Governance is available, use it for material architecture/ownership/reuse decisions and its verifier/OPV lanes on their actual triggers. CoreReplica remains the reference/product/parity procedure owner.

## Standalone mode

CoreReplica must still function without Core-First. Before an architecture-relevant build decision, perform only this compact safety fallback:

1. name the responsibility being changed;
2. identify any existing authoritative state/rule owner or mark it unresolved;
3. prefer reuse, configuration, correction or composition before adding a new owner/path;
4. reject a second authoritative state/rule path for the same responsibility unless explicitly justified;
5. keep external/provider/reference origin behind the same canonical product path;
6. if owner semantics remain materially unresolved, preserve that state and avoid irreversible architecture claims.

This fallback is intentionally smaller than Core-First. Do not fork the full Core-First method into CoreReplica.
