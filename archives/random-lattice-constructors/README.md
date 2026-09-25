# Random lattice constructors (prior art)

Taken from branch `feat/random-lattice-constructors-51` (PR #52, merged as
`ed9e28edd` on 2026-07-09 into a lineage that main's history no longer
contains). The branch was deleted on 2026-09-25, after this copy was made.

- `arithmetic.py` holds `random_gram_of_signature`,
  `random_unimodular_gram_of_signature`, `random_gram_of_determinant` and
  `random_gram_of_rank`. Each is a random SL(n, ZZ) congruence `AᵀGA` of a
  diagonal Gram matrix. Sylvester's law of inertia keeps the signature and
  det A = 1 keeps the determinant. Randomness is scoped with Sage's `seed()`.
- `discriminant_forms.py` holds `DiscriminantForm.random_isotropic_subgroup`,
  glue data for a random proper overlattice.
- `test_random_gram_generation.sage` is the spike's test file.

Every output is congruent over ZZ to a diagonal form, so the unimodular
generator gives only the odd lattices I_{p,q}. It never gives even ones
such as U or E8, and it is not a random lattice within a genus. The port is
the TODO node `optional-random-lattices-of-given-invariants`.
