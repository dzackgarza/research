# Independent Attack Surface

The later adversarial audit for `T-0011` must attack the strongest admissible claim:
that the frozen candidate surface in `tasks/T-0011/admission_target.md` is the only
shared surface admitted, and that every admitted primitive is exact, backend-routed, and
free of banned surrogate behavior.

## Required attack directions

- diff attack: compare the implemented shared surface against the frozen candidate
  inventory and explicit exclusions;
- semantics attack: try to find any surviving bounded-search, fail-open, print-theater,
  ad hoc constructor, or task-shaped helper path in the admitted surface;
- backend-routing attack: test whether each admitted primitive is actually routed to the
  mature backend family promised in the task artifacts;
- replay attack: rerun the exact route fixed in `tasks/T-0011/replay_contract.md` and
  compare emitted certificates against the claimed admission surface;
- scope attack: inspect for collateral edits outside the allowed scope and for hidden
  new shared helpers not named in the frozen candidate inventory;
- burden-claim attack: compare the trusted-base admission record against the exact
  trust-budget movement fixed in `tasks/T-0011/admission_target.md` and reject any
  incremental laundering.
