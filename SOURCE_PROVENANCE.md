# Source provenance

CoreReplica v0.2.0 is derived from a reviewed snapshot of:

- Repository: `https://github.com/Jakeschincariol/replica-skill`
- Upstream commit: `77c9436fb3d18c3d58169efb8caf4fe906b0dc51`
- Upstream release description: Replica skill pack v1.0, eleven Claude skills
- Upstream license: MIT

## Reused/adapted code

The following deterministic helper families originate from the upstream project and retain MIT provenance:

- `replica-design/contrast.py` → `skills/corereplica-design/scripts/contrast.py`
- `replica-diff/imgdiff.py` → `skills/corereplica-verify/scripts/imgdiff.py`
- `replica-diff/parity.py` → concept retained but implementation contract rewritten for evidence-separated parity
- `replica-entrepreneur/reviews.py` → `skills/corereplica-market/scripts/reviews.py`
- `replica-brand/sweep.py` → `skills/corereplica-market/scripts/sweep.py` with CoreReplica planning-folder handling
- `replica-launch/listing.py` → `skills/corereplica-market/scripts/listing.py`

Templates/themes derived from upstream examples retain the same provenance.

## Architectural rewrite

CoreReplica does not preserve the upstream mandatory chain `recon -> architect -> design -> build -> backend -> test -> diff -> entrepreneur -> brand -> launch -> deploy` as governance.

The rewrite adds:

- material-triggered JIT routing;
- explicit `Reference Truth != Product Truth != Verification Truth` boundaries;
- Core-First owner/reuse/change routing instead of a parallel architecture skill;
- implementation-progress isolation from acceptance/parity;
- read-only verification with correction handoff;
- exact approval gate for consequential release transitions;
- provider-neutral plugin packaging and project-native validation.

## v0.1.1 pre-test hardening

No new upstream source was incorporated. v0.1.1 restores useful procedural depth from the already-attributed Replica v1.0 source as JIT references while preserving CoreReplica ownership boundaries. No Universal Modder content is copied into this release.

## v0.2.0 field-evaluation hardening

v0.2.0 is driven by the first staged CoreReplica field evaluation (ANotePortable) supplied by the project user. No third-party source code was incorporated for these corrections. The evaluation exposed provider-neutral gaps in workspace-shape assumptions, standalone degradation, side-effect-safe verification, non-visual evidence boundaries, deferred-scope schema semantics, autonomous provisional decisions, and verification-lane coordination.

The previously reviewed `universal-modder` material remains an external learning source only; no Universal Modder text/code/assets are copied into CoreReplica v0.2.0.
