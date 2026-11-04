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

## `EffectiveReversal.lean` — proved, no `sorry`

The two logical steps of the negative answer to A21, and their composite. They are
linear algebra plus one positivity statement, so they are formalized here rather than
argued in prose only.

**`slot_reverses_root`.** Let `B` be a `ℚ`-bilinear form on `V`, `f` an involution
preserving `B` (`∀ x y, B (f x) (f y) = B x y`), `S` an `f`-stable submodule, `H a ∈ V`
with `B H H ≠ 0`, `f H = H`, `a ∈ S`, `B a H = 0`, and suppose the fixed points of `f` in
`S` all lie on the line `ℚ H`. Then `f a = -a`.

The proof uses only the `ℚ`-eigenspace decomposition of an involution: `f a + a` is fixed
by `f` and lies in `S`, hence on the line; pairing it with `H` kills the `f a` term
because `f` is an isometry fixing `H`, so the coefficient vanishes since `B H H ≠ 0`.
**No integral splitting of `S` is used** — in the Coble case the fixed and anti-fixed
lattices span an index-2 sublattice, which is why the operator argument was the one that
could be made.

**`not_preserves_effectivity_of_reversal`.** If a map preserves a cone `C`, and every
nonzero element of `C` has positive pairing with a fixed `A` (`0 < B x A`), then no element
`α ∈ C`, `α ≠ 0`, is sent to `-α`. Positivity is used once in each direction.

**`no_automorphism_reverses_root`.** The two together, with every hypothesis of both in
the signature: `f` involutive, form-preserving, `S`-stable, its fixed points in `S` on the
line `ℚ H`; `α ∈ S` orthogonal to `H`; `α` in the cone `C` and nonzero; and `C` preserved.

**`rank_two_narrowing`.** The rank-two case, reduced to one integer. With `S'` the whole
hyperbolic plane `⟨a₁, a₂⟩`, `H = ±(a₁ + a₂)`, and `α = p • (a₁ - a₂) + β` with `β` orthogonal
to the plane, the expansion of `B α α` has no cross terms, so `β² = -2 + 4p²`; negative
semi-definiteness of `β`'s direction gives `p² ≤ 1/2`, and since `α · a₁ = -2p` is an integer
the rank-two case is one of `α · a₁ ∈ {-1, 0, 1}`. Which one is a property of the pair
`(α, S')` on the surface and not of the lattice; the manuscript's `prop:rank-two-slot-boundary`
says where it is known and where it is not.

Both `#print axioms` lines on the four theorems read
`[propext, Classical.choice, Quot.sound]`. Checked with

```
/opt/lean/bin/lean formalization/coble-enriques/EffectiveReversal.lean
```

Lean 4.33.1 against the Mathlib build under `/opt/mathlib` (`LEAN_PATH` as configured in
this container); exit 0, no diagnostics.

**Scope, and what stays a premise.** What is checked is the logic that consumes the
geometric inputs: that an automorphism of the surface preserves effectivity, that the
authored class `α` is effective, that a projective surface carries an ample class `A`, and
that the induced action of `I_dP` is an integral isometry commuting with `I_Co` with the stated fixed lattice, and that `H^⊥ ∩ S` is negative definite — on a K3 that
follows from `I_Co` being nonsymplectic and `H^2 > 0`, and it enters here as a hypothesis. Those are hypotheses here, not theorems; the sources for
them are the authored bullets of the tuple, `prop:coble-invariant-lattice`,
`prop:del-pezzo-placement` and the owner computations, and the manuscript's premise ledger
(`rmk:a21-premises`) says which source supplies which.
