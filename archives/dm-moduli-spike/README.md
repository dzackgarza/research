# Deligne–Mumford moduli spike (prior art)

Taken from branch `cursor/dm-compactification-spike-0d2c`, commits `bf773bea5`
(2026-07-11) through `4a1278752` (2026-07-17), with the uncommitted edits in
its Cursor worktree (stacks, atlas and instance modules, last touched
2026-07-12) applied on top. The branch and the worktree were deleted on
2026-09-25, after this copy was made.

- `spike/` was `computations/experiments/dm_moduli_spike/`. It contains:
  - stable graphs Γ_{g,n} with contractions, automorphisms, edge orbits and
    the symmetric Δ-complex;
  - the stratification poset of M̄_{g,n}, with a round trip to admcycles;
  - atlas charts for M_{0,n}, M̄_{0,n}, M_{1,n}, M_{2,n}, M_3 and M̄_4;
  - literature-cited oracle tests under `tests/literature/`
    (Harris–Morrison, Arbarello–Cornalba, Chan).
- `landscape/` was `computations/scripts/dm_moduli_landscape/`.

The code predates the owned-category architecture. It defines its own
categories and probes with `isinstance`, `hasattr` and `try`. Read it for
the mathematics and the cited values, not for its structure. The port is the
TODO node `optional-moduli-of-stable-curves`.
