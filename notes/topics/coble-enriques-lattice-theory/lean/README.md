# Lean sources from the Coble corpus

Migrated 2026-08-20 from `~/gitclones/lattice-research/lean/CobleResearchLean/`.
Two files, kept as native Lean source. They are not built here: this repository
has no Coble Lean project, and its only Lean tree
(`computations/experiments/lean_category_dsl_spike/`) is about the category DSL.

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
