# CoreReplica Context Handoff — v0.2.0

## Current state

CoreReplica is a skills-only Agent Plugin derived from the MIT `replica-skill` source at commit `77c9436fb3d18c3d58169efb8caf4fe906b0dc51`.

v0.1 corrected the upstream structural failures: Reference Truth/Product Truth separation, builder status vs Verification Truth, removal of a parallel architecture owner, read-only verification, and exact release gates. v0.1.1 restored useful backend/verification/market/release procedure depth behind JIT owners.

## First empirical field evaluation

The first staged evaluation replicated the ANotePortable package. CoreReplica alone established the reference/product/evidence model and its verification discipline exposed three real launcher bugs despite an initially successful process exit. Adding Core-First found a missing crash-recovery responsibility and a fresh verifier found a Unicode path defect. Adding Agent Project Compiler produced a durable cross-session package.

The evaluation also exposed CoreReplica-specific gaps:

1. source-repository assumptions did not fit a binary/distribution package and control metadata risked contaminating the payload;
2. standalone operation was underspecified when Core-First was unavailable;
3. real-boundary verification lacked side-effect isolation/baseline/cleanup guidance;
4. non-visual boundaries such as process/registry/filesystem were under-emphasized;
5. deferred scope and priority were conflated by the sample schema/tool;
6. autonomous evaluation lacked a safe provisional user-decision state;
7. CoreReplica Verify, OPV and Core-First Verifier needed an explicit role matrix.

## v0.2.0 corrections

- workspace-shape classification replaces repository-as-default semantics;
- control-plane artifacts stay outside shippable/runnable payloads when contamination is possible;
- revision identity may be Git SHA, package/content hash, build ID or evidence-run identity;
- Core-First remains preferred but CoreReplica now defines a deliberately small standalone owner-safety fallback;
- verification gains side-effect-safe preflight and oracle-liveness guidance;
- process/filesystem/registry/database/network/external-service boundaries are first-class evidence;
- requirements gain `scope_status=active|deferred|out_of_scope` separate from active priority;
- autonomous runs may use `PROVISIONAL_INTERPRETATION` without fabricating USER authority;
- verification lane responsibilities are explicitly non-overlapping.

## Next work

Run a second field evaluation on a materially different target (for example a web/SaaS app or a multi-surface desktop app). Do not add further framework machinery unless the next failure demonstrates a reusable gap.
