# T-0004: G2.1 — Orbit Enumeration in A_T

## Origin

- `GOAL.md` §2, Task 2.1: "Enumerate isotropic vectors in A_{T_Co} and compute their
  orbits under O(q_T)"
- `tasks/goal_expansion.md` G2.1

## Objective

Compute the orbits of isotropic vectors in the discriminant group A_{T_Co} ≅ (Z/2Z)^11
under the action of the orthogonal group O(q_T) of the discriminant form q_T.

The discriminant form q_T: (Z/2Z)^11 → Q/2Z is determined by T_Co = diag(2, 2, -2, ...,
-2) (two +2 entries, nine -2 entries).
For a 2-elementary lattice, q_T(x) = x^T G^{-1} x mod 2Z. With G = diag(2, 2, -2, ...,
-2), we have G^{-1} = diag(1/2, 1/2, -1/2, ..., -1/2), so q_T(x) = (1/2)(x_1^2 + x_2^2 -
x_3^2 - ... - x_11^2) mod 2Z. Since x_i ∈ {0,1}, we have x_i^2 = x_i, giving: q_T(x) =
(1/2)(x_1 + x_2 - x_3 - ... - x_11) mod 2Z.

**Critical:** The signs CANNOT be dropped.
While -1 ≡ 1 (mod 2) as integers, -(1/2) ≡ 3/2 (mod 2Z) ≠ 1/2 (mod 2Z). So q_T(x) ≠
(1/2)(x_1 + ... + x_11) mod 2Z.

An element x ∈ A_T is **isotropic** if q_T(x) = 0 mod 2Z, i.e., x_1 + x_2 - x_3 - ... -
x_11 ≡ 0 (mod 4). There are exactly 528 isotropic elements (verified independently in
T-0003 glue code check: q_T distribution is {0: 528, 1/2: 528, 1: 496, 3/2: 496}).

## Deliverable Type

Exact computation with certificate.

## Acceptance Criteria

1. The orthogonal group O(q_T) is constructed explicitly as a matrix group acting on
   (Z/2Z)^11 using a library function (GAP `GO`, `OrthogonalGroup`, or equivalent).
   If the library uses a different but equivalent quadratic form, prove equivalence by
   showing the polar forms match.
2. All 2^11 = 2048 elements of A_T are enumerated
3. Isotropic elements are identified (q_T(x) = 0 mod 2Z)
4. Orbits of isotropic elements under O(q_T) are computed using GAP `Orbits`
5. For each orbit: representative, orbit size, and stabilizer size are recorded
6. The orbit decomposition is verified: sum of orbit sizes = number of isotropic
   elements
7. Results are cross-checked: the number of isotropic elements should be 528 (verified
   independently in T-0003: q_T distribution {0: 528, 1/2: 528, 1: 496, 3/2: 496})

## Non-goals

- Lifting orbits to T_Co (that is T-0007 / G2.2)
- Computing orbits of non-isotropic elements
- Computing the full group O(T_Co) (only O(q_T) on the finite discriminant group)

## Allowed Dependencies

- `coble_geometry_foundation.sage` for T_Co lattice definition
- GAP (via `sage -sh` or direct `gap` call)
- `theory/gap_orbits.md` for GAP orbit computation patterns

## Required Conventions

- A_T is represented as F_2^11 with the quadratic form q_T(x) = (1/2)(x_1 + x_2 - x_3 -
  ... - x_11) mod 2Z where x_i ∈ {0,1}. Isotropic means x_1 + x_2 - x_3 - ... - x_11 ≡ 0
  (mod 4).
- O(q_T) = {g ∈ GL(11, F_2) : q_T(g·x) = q_T(x) for all x}

## Failure Conditions

- GAP cannot construct O(q_T) as a finite matrix group
- Orbit computation exceeds reasonable time/memory bounds
- The isotropic count does not match the verified prediction (528)

## Sufficiency Map

This task discharges GOAL.md Task 2.1 partially: it enumerates isotropic vectors and
computes O(q_T)-orbits in A_T. The lifting step (Task 2.2) is a separate task (T-0007).
