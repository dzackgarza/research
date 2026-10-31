# Backup of the `LatticeResearch` formalization

This directory is a **backup**, not the canonical home of these files.

The formalization lives in the repository `dzackgarza/lean-categories`, in the subtree
`LeanCategories/LatticeResearch/`, where it is committed and builds under the pinned
toolchain (`leanprover/lean4:v4.33.0`, Mathlib `db584cd6d46c`). The agent that wrote it had
no credentials for that repository and no GitHub connection authorized for it, so the work is
duplicated here so that it survives the container.

- Local commit in `lean-categories`: `430f6a6c1f109911dccd6c4b90116c7f24ac5595`
  ("Prove the bridge from discriminant-trivial to the congruence, and say what stays external"),
  with five commits before it.
- `lattice-research-commits.patch` is the output of `git format-patch -6` for those commits,
  and is the exact record; the two `.lean` files beside it are for reading.

## What is in it

`Divisibility.lean` formalizes the divide-and-conquer claims of the Coble cusp chapter that
the prose gets wrong at first pass:

- `divis G v`, the divisibility of a vector in a Gram-matrix lattice, and `divis_smul`;
- `divis_two_smul`: `div_{2G} = 2 div_G`, which is the book's `div_T = 2 div_L` for
  `T = L(2)`;
- `forall_dvd_form_iff`: the integral duality step, that for unimodular `G` divisibility of
  the functional `β_G(v, -)` by `m` is `v ∈ mL`, proved through the adjugate;
- `divis_two_smul_eq_two_iff_primitive`: **the theorem** — for an integral unimodular `G`,
  `divis (2 • G) v = 2 ↔ Primitive v`, where `Primitive` says `v` is no proper multiple
  `m • u`, `m > 1`; with `primitive_iff_isPrimitive` identifying that with the gcd condition;
- the non-unimodular counterexample `G2`, where the equivalence fails in both directions;
- `ActsTriviallyModTwo`, `actsTriviallyModTwo_iff_quotient`, and
  `span_single_ne_span_single_of_quotient_trivial`: the separation of two isotropic lines for
  an automorphism acting trivially on `B/2B`, which is the whole of the claim that the stable
  group has at least two orbits, hence that `F_Co` has at least two 0-cusps.

## What it does not do

It does not classify the `Γ_Co`-orbits, and nothing here counts cusps. The identification
`T_Co = B(2)` with `B = U ⊕ U ⊕ I_{0,7}`, the identification of the two basis vectors with
the isotropic generators of the `U(2)` summand, and the triviality of `Γ_Co`'s action on
`A_T` are supplied by the manuscript, not by Lean; they are named in the file's docstrings.

## Axioms

Every result listed above reports `[propext, Classical.choice, Quot.sound]` from
`#print axioms`; none depends on `sorryAx`.
