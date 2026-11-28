# T-0004: dependencies.md

## Prerequisite Tasks

- **T-0001 (G1.2)**: Gram matrices and invariants — provides T_Co lattice definition and
  confirms discriminant group structure.
  ✅ Complete.

## Mathematical Dependencies

- **Nikulin (1979)**: Classification of 2-elementary lattices.
  Establishes that T_Co is uniquely determined by its invariants (r=11, a=11, δ=1) and
  that A_T ≅ (Z/2Z)^11.
- **Discriminant form theory**: For a 2-elementary lattice L with Gram matrix G, the
  discriminant form q: L^*/L → Q/2Z is q(x) = x^T G^{-1} x mod 2Z.

## Algorithmic Dependencies

- **GAP `Orbits`**: Computes orbits of a group action on a set.
  Available in GAP 4.
- **GAP `GL(n, GF(p))`**: Constructs general linear group over finite field.
- **GAP `Stabilizer`**: Computes stabilizer subgroup of an element under group action.

## Code Dependencies

- `coble_geometry_foundation.sage`: Provides `T_Co_lattice()` constructor.
  Used only to confirm the lattice structure (already known analytically).
- `theory/gap_orbits.md`: Reference for GAP orbit computation patterns.

## Trusted References

- `GOAL.md` §2, Task 2.1
- `tasks/goal_expansion.md` G2.1
- `REFERENCES.md`: Nikulin (1979), Sterk (1991)
