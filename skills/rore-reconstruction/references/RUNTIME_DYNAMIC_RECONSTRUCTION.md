# Runtime / Dynamic Reconstruction

Use when effective behavior cannot be established from static artifacts alone.

Observe the closest practical authorized boundary: process tree, loaded modules/resources, files/config/registry, database/storage, network/IPC, DOM/runtime state, timing, persistence, recovery and user-visible results.

Classify content/state transitions where useful:

```text
PRESENT → REFERENCED → REACHABLE → EXERCISED → EFFECTIVE
```

Do not claim the rightmost state from evidence of a leftmost state.

Runtime observations should be back-annotated into stable static/data/runtime anchors when possible. If a symptom cannot be tied to a durable identity, record it as runtime-local/candidate rather than inventing ownership.

Failed launches, crashes and recovery paths can be informative evidence when the failure boundary is captured.
