import Mathlib

/-!
# Node Criteria for Plane Curves – Hessian Rank Bound

At a nonzero singular point of a homogeneous ternary polynomial the 3 × 3
Hessian matrix has rank at most 2.

## Proof idea
If `F` is homogeneous of degree `n`, then `∂F/∂xⱼ` is homogeneous of degree
`n − 1`. Euler's identity applied to `∂F/∂xⱼ` gives the polynomial identity

  `∑ i, X i * ∂²F/∂xᵢ∂xⱼ = (n − 1) • ∂F/∂xⱼ`.

Evaluating at a singular point `p` (where every first partial vanishes) shows
that the Hessian matrix `H(F)(p)` satisfies `H(F)(p) · p = 0`. Since `p ≠ 0`
the kernel of `H(F)(p)` is non-trivial, so its rank is at most 2.
-/

open MvPolynomial Matrix Finset

noncomputable section

/-- The Hessian matrix of a multivariate polynomial `F` evaluated at a point `p`.
    Entry `(i, j)` is `eval p (pderiv i (pderiv j F))`. -/
def hessianMatrixAt {k : Type*} [CommSemiring k]
    (F : MvPolynomial (Fin 3) k) (p : Fin 3 → k) : Matrix (Fin 3) (Fin 3) k :=
  Matrix.of fun i j => MvPolynomial.eval p (MvPolynomial.pderiv i (MvPolynomial.pderiv j F))

/-- A point `p` is a singular point of `F` when `F(p) = 0` and every first
    partial derivative vanishes at `p`. -/
def IsSingularPoint {k : Type*} [CommSemiring k]
    (F : MvPolynomial (Fin 3) k) (p : Fin 3 → k) : Prop :=
  MvPolynomial.eval p F = 0 ∧ ∀ j : Fin 3, MvPolynomial.eval p (MvPolynomial.pderiv j F) = 0

/-- At a singular point of a homogeneous polynomial, the Hessian matrix
    multiplied by the point vector is zero. -/
lemma hessian_mulVec_singular {k : Type*} [CommRing k]
    {F : MvPolynomial (Fin 3) k} {n : ℕ} {p : Fin 3 → k}
    (hF : F.IsHomogeneous n) (hs : IsSingularPoint F p) :
    (hessianMatrixAt F p).mulVec p = 0 := by
  ext j
  have h_euler : ∑ i, MvPolynomial.X i * MvPolynomial.pderiv i F = n • F := by
    convert MvPolynomial.IsHomogeneous.sum_X_mul_pderiv hF using 1
  have h_chain : ∑ i, MvPolynomial.X i * MvPolynomial.pderiv j (MvPolynomial.pderiv i F) +
      MvPolynomial.pderiv j F = n • MvPolynomial.pderiv j F := by
    convert congr_arg (pderiv j) h_euler using 1 <;> simp +decide [mul_comm]
    simp +decide [Finset.sum_add_distrib, Pi.single_apply]
  replace h_chain := congr_arg (MvPolynomial.eval p) h_chain
  simp_all +decide [Matrix.mulVec, dotProduct]
  simp_all +decide [mul_comm, hessianMatrixAt]
  have := hs.2 j
  aesop

/-- At a nonzero singular point of a homogeneous ternary polynomial,
    the Hessian matrix has rank at most 2. -/
theorem hessian_rank_le_two_of_singular {k : Type*} [Field k]
    {F : MvPolynomial (Fin 3) k} {n : ℕ} {p : Fin 3 → k}
    (hF : F.IsHomogeneous n) (hs : IsSingularPoint F p)
    (hp : p ≠ 0) :
    (hessianMatrixAt F p).rank ≤ 2 := by
  have h_mulVec_zero : (hessianMatrixAt F p).mulVec p = 0 :=
    hessian_mulVec_singular hF hs
  have h_kernel_nontrivial : LinearMap.ker (Matrix.mulVecLin (hessianMatrixAt F p)) ≠ ⊥ := by
    rw [Ne.eq_def, LinearMap.ker_eq_bot']
    aesop
  have := LinearMap.finrank_range_add_finrank_ker (Matrix.mulVecLin (hessianMatrixAt F p))
  simp_all +decide [Matrix.rank]
  linarith [show Module.finrank k (LinearMap.ker (Matrix.mulVecLin (hessianMatrixAt F p))) ≥ 1
    from Nat.pos_of_ne_zero (by aesop)]

end
