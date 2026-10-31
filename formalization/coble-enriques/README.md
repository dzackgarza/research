# Lean sources from the Coble corpus

Migrated 2026-08-20 from `~/gitclones/lattice-research/lean/CobleResearchLean/`.
Lean files kept as native source. They are not built here: this repository has no
Coble Lean project, and its only Lean tree
(`computations/experiments/lean_category_dsl_spike/`) is about the category DSL.
Each file below says how it was checked.

## `NodeCriteria.lean` — proved, no `sorry`

The node-detection criterion for the 10-nodal plane sextic, and the one fully
formalized result in the corpus.

**Theorem** (`hessian_rank_le_two_of_singular`). Let $k$ be a field, let
$F \in k[x_0, x_1, x_2]$ be homogeneous of degree $n$, and let $p \neq 0$ be a
singular point of $F$ — that is, $F(p) = 0$ and $\partial_j F(p) = 0$ for every
$j$. Then the Hessian matrix $H(F)(p)$, with entries
$\bigl(\partial_i \partial_j F\bigr)(p)$, has rank at most $2$.

**Proof.** Euler's identity for the homogeneous polynomial $F$ of degree $n$ is
$\sum_i x_i\, \partial_i F = n F$. Differentiating it by $\partial_j$ gives the
polynomial identity
$$\sum_i x_i\, \partial_j \partial_i F \;+\; \partial_j F \;=\; n\, \partial_j F,$$
so $\sum_i x_i\, \partial_i \partial_j F = (n-1)\, \partial_j F$. Evaluating at
$p$, where every first partial vanishes, gives $H(F)(p)\cdot p = 0$. Since
$p \neq 0$ the kernel of $H(F)(p)$ is nontrivial, so by rank-nullity in
dimension $3$ the rank is at most $2$. $\square$

The formalization states this over a `CommRing` for the vanishing lemma
(`hessian_mulVec_singular`) and over a `Field` for the rank bound, and uses
Mathlib's `MvPolynomial.IsHomogeneous.sum_X_mul_pderiv` for Euler's identity.

## `IsotropicPlanes.lean` — every proof `sorry`

Statements only, and both of them are wrong as written: the file models
$T_{\mathrm{Co}}$ by a diagonal form that is a different lattice, and its proof
sketch classifies orbits by the Arf invariant, which does not classify integral
lattices. The corrected mathematics, the claim's open status, and the owned
surface on which it can be decided are in
`notes/topics/isotropic-vector-orbits/tco-isotropic-plane-orbit-claim.md`.
The file is kept only as the record of what was attempted.

## `Splitting.lean` — proved, no `sorry`

The integral orthogonal-splitting step the Scattone chapter needs. Nothing is at stake
over $\mathbb{Q}$; the content is that the coefficients are integers, so that the
complement is a genuine lattice and not a rational or scaled one.

- `exists_mulVec_eq_of_unimodular`. If `M : Matrix κ κ ℤ` has `M.det = ±1`, then every
  `r : κ → ℤ` is `M *ᵥ u` for some `u : κ → ℤ`. The witness is
  `u = M.det • (M.adjugate *ᵥ r)`, integral because `M⁻¹ = ±M.adjugate` when
  `M.det = ±1`.
- `splits_of_unimodular`. If the restriction of an integral form `B` to the span of the
  columns of `C` is unimodular, then every integral `x` is `C *ᵥ u` plus a vector
  orthogonal to all the columns, with `u` integral. No index enters.
- `det_eq_mul_of_unimodular_block_diagonal`. In a unimodular basis in which `B` is block
  diagonal, `B.det` is the product of the two block determinants.
- `det_hyperbolic4`, `det_two_hyperbolic4`. `U ⊕ U` has determinant `1`, which is the
  hypothesis; the twice-scaled `2 • (U ⊕ U)` has determinant `16`, so a scaled pairing
  satisfies no such hypothesis and its splitting is only over $\mathbb{Q}$.
- `isotropic_of_hyperbolic_parametrization`. On $H \oplus W$ with $H = \langle e,f\rangle$,
  the vector $e + nf + w$ is isotropic as soon as $w^2 = -2n$; this is the parametrization
  of the null rays of $N = H \oplus E_8^{\oplus 2} \oplus A_1$ by which the four
  one-cusps are read off the maximal parabolic subdiagrams of the Coxeter diagram.

Every theorem depends on `[propext, Classical.choice, Quot.sound]` and on nothing else;
the `#print axioms` output is at the end of the file. Checked with

```
/opt/lean/bin/lean formalization/coble-enriques/Splitting.lean
```

which needs `import Mathlib` on `LEAN_PATH` and prints five clean axiom lines.

**Scope.** This file certifies the splitting and the determinant consequence. It does not
certify which even overlattice of a given root lattice a particular $1$-cusp carries; that
needs quotient-lattice and overlattice computations run through `sage-extensions`, and
`writing/dissertation/GAPS.md` records, with reproducers, why that run is not possible in
this container.

## `CoxeterRim.lean` — proved, no `sorry`

One of the four one-cusps at degree two, from the printed figure rather than from a label.
Alexeev--Engel--Thompson's Figure 1 (p. 22) prints the Coxeter diagram `G_cox` of
`N = H ⊕ E₈² ⊕ A₁` on 24 nodes in a triangular lattice; the first of the four small figures
beside it has exactly the rim of that triangle black. The rim, in the cyclic order
`12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11`, is an 18-cycle of single
edges, hence an affine `A₁₇`, whose marks are all `1`.

- `rimGRAM`: that 18 × 18 Gram matrix.
- `rimMarks`: the all-ones mark vector.
- `rim_mulVec_marks`, `rim_marks_isotropic`, `rim_marks_ne_zero`: the mark vector is in the
  kernel of the rim form and is isotropic and nonzero, so the sum of the eighteen rim roots
  spans a null ray of `N`.

Both `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. Checked with

```
/opt/lean/bin/lean formalization/coble-enriques/CoxeterRim.lean
```

**Scope.** This certifies the arithmetic of the figure reading, not the cusp: primitivity of
the sum in `N`, and the identification of `v^⊥/Zv` with `A₁₇`, are the library computation
that is still pending, as is the reading of the other two subdiagrams' vertex sets.
