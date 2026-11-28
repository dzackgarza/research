# T-0004: provenance.md

## Origin

- **GOAL.md**: §2 "Isotropic Orbit Enumeration", Task 2.1
- **goal_expansion.md**: G2.1 — "Orbit Enumeration in A_T"
- **Preceding tasks**: T-0001 (G1.2) confirmed T_Co structure and discriminant group

## Mathematical Basis

- **Nikulin (1979)**: 2-elementary lattice classification → T_Co unique, A_T ≅ (Z/2Z)^11
- **Discriminant form**: q_T(x) = (1/2)·wt(x) mod 2Z for x ∈ F_2^11
- **Isotropic elements**: even-weight vectors in F_2^11, count = 2^10 = 1024

## Computational Basis

- **GAP 4**: Finite group orbit computation via `Orbits`
- **theory/gap_orbits.md**: GAP patterns for orbit computation

## Status

- Task specification: ✅ Complete (task.md, scope.yml, assumptions.md, dependencies.md,
  plan.md)
- PRE_AUDIT: Pending
- Implementation: Not started
