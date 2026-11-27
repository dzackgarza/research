# Posets Triage

The promoted subtree now owns the order-theoretic surface separately from
ordinary sets. The current hierarchy distinguishes finite posets, finite
meet-semilattices, finite join-semilattices, and finite order-theoretic
lattices.

## Settled Mapping Items

- Poset constructors follow the repo constructor pattern: expose named,
  non-variadic constructors for each documented Sage input shape. The acyclic
  `DiGraph` constructor is the canonical constructor; the other documented
  Sage shapes are explicit adaptations or existing-poset refinements.
- Meet and join follow the global binary-operation pattern: expose the binary
  operation and a sequence overload that folds over it. Sage's
  `meet(x, y=None)` and `join(x, y=None)` spellings remain inventory evidence,
  not project signatures.
- Lattice congruences use set-theoretic vocabulary. A lattice congruence is an
  `EquivalenceRelation`, represented concretely by `SetPartition` where Sage
  returns one. The generated-congruence method is
  `congruence_generated_by(blocks)`, not a lattice-specific type name.
- Sage `certificate=True` paths map to separately named certificate methods.
  Boolean predicates stay boolean; certificate methods return the witness data
  documented by Sage.
- Graph, plotting, TikZ, polytope, order-complex, algebra, and polynomial
  surfaces are ownership/mapping work, not open design decisions. Ownership is
  determined by the target mathematical object or by display/interop status.

## Concrete Future NEEDS_DECISIONS Items

- Decide whether equivalence relations and set partitions need a first-class
  set subtree, or whether `SetPartition` should remain a centralized
  Sage-backed type alias until the set-partition inventory is done.

## Evidence Gaps

- Searched: local Sage category filenames under
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories`.
- Found: `posets.py`, `finite_posets.py`, `lattice_posets.py`, and
  `finite_lattice_posets.py`; no semilattice category module filename appeared
  in that directory.
- Conclusion: I believe Sage has concrete finite semilattice classes but no
  separate documented Sage semilattice category module in this installation.
- Confidence: Medium.
- Gaps: I did not complete an import-level Sage category introspection because
  local Sage imports failed before reaching poset category modules.

- Searched: `/home/dzack/miniforge3/envs/sage/bin/sage -python` import of
  `sage.combinat.posets.posets` and `sage.combinat.posets.lattices`.
- Found: import failed during Sage category initialization with
  `ImportError: cannot import name Category`.
- Conclusion: I believe the local Sage interpreter is not reliable for source
  introspection from this working directory/session.
- Confidence: Medium.
- Gaps: I did not debug the Sage environment because the task could proceed
  from published Sage documentation and local source paths.
