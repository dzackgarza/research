# Components

Reusable computational pieces factored out of scratchpad work or named computation
threads. A component should exist because code is reused across computations, not
because a mathematical subject deserves a category.

- `automorphism-groups/`: Sage/GAP automorphism-group helpers and proof-oriented checks.
- `coxeter-vinberg/`: Coxeter/Vinberg plotting and Lorentzian reflection scratch code.
- `hodge-periods/`: Singular and related code for Hodge-theoretic period computations.
- `monodromy/`: monodromy-specific Singular and Sage notes.

## Relation to the preamble, and the gaps that remain

`automorphism-groups/aut_group_any.sage` is superseded: the preamble owns one spelling of
`Aut` across Sage's group types in `categories/group/groups.sage`, delegating to GAP's
`AutomorphismGroup` from `categories/group/group_morphisms.sage`.

Three things here have no owner on the preamble surface, and are recorded as gaps rather
than as work already done:

- `automorphism-groups/automorphism_guarantees.py` classifies Sage's group constructions
  by whether the automorphism group is computable, likely computable, restricted, or
  unavailable. The preamble's doctrine is to own the name and state the gap, so this
  survey is the raw material for the declared gaps on `Aut`; no such statement exists on
  the owned interface yet.
- `automorphism-groups/automorphism_assertions.py` and `../AutGroupTests.sage` assert a
  wider literature table than `tests/test_known_mathematics.sage` carries. Rows with no
  owned counterpart: `Aut(C_n)` as the unit group of `Z/nZ`; `Aut(D_n)` as the holomorph
  of `C_n` for odd `n`; `|Aut(C_2 x C_4)| = 8`; `Aut(C_2 x C_3) = C_2`; `Aut(GL(2,2)) =
  S_3`; and the automorphism-group orders of the complete graphs, the cycle graphs, the
  Petersen graph and the 3-cube. Each needs its source named before it is admitted to
  that file.
- `hodge-periods/` and `monodromy/` have no counterpart at all: the preamble owns no
  Hodge, period, or connection surface. `foliation.lib` is Movasati's published Singular
  library, kept reachable as third-party code and never absorbed; `compute_monodromy.sing`
  is the local driver over it. The two extraction specs under
  `notes/computations/extraction-specs/` analyse what of that library and of Lairez's
  periods package is worth reimplementing.

`coxeter-vinberg/Vinberg_L_2_1.py` is an early prototype over the diagonal form
`diag(-1,1,1)`: it is mathematically defective and is kept only as a record of the earlier
attempt. The preamble owns the operation correctly in
`categories/modules/framed/formed/integrallattice/hyperbolic_lattices.sage`.
