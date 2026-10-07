# Safe Perturbation and Recovery

Before a probe that can mutate persistent state, identify:
1. the exact claim/hypothesis;
2. plausible side effects and residue;
3. the least invasive representative environment;
4. a baseline/snapshot where practical;
5. cleanup/recovery and failure handling;
6. the observation that would justify the probe.

Prefer reversible local copies, test profiles/accounts, snapshots, temp directories, sandbox services or controlled offline environments when they still exercise the required boundary.

After the probe, verify restoration or explicitly record residue. Tool/cleanup success is not proof that state returned to baseline.

If a material real-world side effect is not needed to learn the mechanism, do not create it.
