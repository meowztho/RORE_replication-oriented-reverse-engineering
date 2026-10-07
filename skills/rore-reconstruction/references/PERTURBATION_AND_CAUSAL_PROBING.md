# Perturbation and Causal Probing

Use deliberate authorized changes when passive observation cannot distinguish competing explanations.

This method borrows the **system-thinking** behind adversarial, CTF, pwn and patch-diff work while changing the objective: reveal mechanism and causality. It is not exploit development or exploit-impact maximization.

## Core loop

```text
1. establish baseline
2. state competing hypotheses
3. choose one material dimension / discriminating variable or boundary
4. perturb the smallest useful amount
5. observe direct + downstream differential
6. trace readers/writers/handlers/enforcement sites
7. corroborate against stable static/data/runtime anchors
8. restore state or record residue
9. record E/FIND/PATH and what remains unknown
```

## Useful perturbation families

Depending on the authorized target:
- value/range/shape boundaries;
- sequence, replay and omitted/repeated steps;
- timing/concurrency/state drift;
- parser/normalization/source-layer differentials;
- DOM/client-state or local runtime state variation;
- files/config/database state changes;
- memory/state mutation and reader/writer tracing;
- temporary local patch/hook to isolate an enforcement layer;
- controlled failure/interruption/recovery;
- before/after version differential;
- protocol/API field variation in a controlled environment.

## Interpretation discipline

A successful mutation proves that the changed boundary can influence the outcome. It does not automatically prove canonical ownership, complete mechanism coverage or safe generalization.

Map multiple enforcement sites when the rule may be layered. One bypassed/changed check can reveal a layer without proving there are no others.

## Stop condition

Stop at sufficient mechanism understanding: once the requested mechanism and its material causal structure are sufficiently understood. Do not continue into exploit stabilization, persistence, lateral movement, credential acquisition, destructive load or impact maximization merely because those techniques exist upstream.
