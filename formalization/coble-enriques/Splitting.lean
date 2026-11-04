import Mathlib

/-!
# Integral orthogonal splitting

The step the manuscript needs is that a unimodular sublattice splits its ambient
lattice *integrally*, with no index.  Over `ℚ` nothing is at stake; the content is
that the coefficients are integers, i.e. that the complement is a genuine lattice
and not a rational (or scaled) one.
-/

namespace Coble

open Matrix

variable {ι κ : Type*}

/-- An integral covector on a lattice with unimodular Gram matrix is realised by an
integral vector.  `M⁻¹ = ±adjugate M` is integral exactly because `M.det = ±1`. -/
theorem exists_mulVec_eq_of_unimodular [Fintype κ] [DecidableEq κ]
    (M : Matrix κ κ ℤ) (h : M.det = 1 ∨ M.det = -1) (r : κ → ℤ) :
    ∃ u : κ → ℤ, M *ᵥ u = r := by
  have h2 : M.det * M.det = 1 := by rcases h with h | h <;> simp [h]
  refine ⟨M.det • (M.adjugate *ᵥ r), ?_⟩
  have key : M *ᵥ (M.det • (M.adjugate *ᵥ r)) = (M.det * M.det) • r := by
    rw [Matrix.mulVec_smul, Matrix.mulVec_mulVec, Matrix.mul_adjugate, Matrix.smul_mulVec,
      Matrix.one_mulVec, smul_smul]
  rw [key, h2, one_smul]

/-- Integral orthogonal splitting.  If the restriction of the form `B` to the span of
the columns of `C` is unimodular, then every integral vector is an integral
combination of those columns plus a vector orthogonal to all of them.  No index
enters: the decomposition is integral. -/
theorem splits_of_unimodular [Fintype ι] [Fintype κ] [DecidableEq κ]
    (B : Matrix ι ι ℤ) (C : Matrix ι κ ℤ)
    (h : (Cᵀ * B * C).det = 1 ∨ (Cᵀ * B * C).det = -1) (x : ι → ℤ) :
    ∃ u : κ → ℤ, Cᵀ *ᵥ (B *ᵥ (x - C *ᵥ u)) = 0 := by
  obtain ⟨u, hu⟩ := exists_mulVec_eq_of_unimodular (Cᵀ * B * C) h (Cᵀ *ᵥ (B *ᵥ x))
  refine ⟨u, ?_⟩
  have hsplit : Cᵀ *ᵥ (B *ᵥ (C *ᵥ u)) = (Cᵀ * B * C) *ᵥ u := by
    simp [Matrix.mulVec_mulVec, Matrix.mul_assoc]
  rw [Matrix.mulVec_sub, Matrix.mulVec_sub, hsplit, hu, sub_self]

/-- The determinant consequence.  If a unimodular change of basis `P` puts `B` in
block-diagonal form, the determinant of `B` is the product of the determinants of the
two blocks; with a unimodular block this says the complementary block has the same
determinant as `B` itself, up to sign. -/
theorem det_eq_mul_of_unimodular_block_diagonal [Fintype ι] [Fintype κ]
    [DecidableEq ι] [DecidableEq κ]
    (B P : Matrix (Sum ι κ) (Sum ι κ) ℤ) (M : Matrix ι ι ℤ) (N : Matrix κ κ ℤ)
    (hP : P.det = 1 ∨ P.det = -1) (hB : Pᵀ * B * P = Matrix.fromBlocks M 0 0 N) :
    B.det = M.det * N.det := by
  have hP2 : P.det * P.det = 1 := by rcases hP with h | h <;> simp [h]
  have hdet : (Pᵀ * B * P).det = P.det * B.det * P.det := by
    rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_transpose]
  rw [hB, Matrix.det_fromBlocks_zero₁₂] at hdet
  have hvol : P.det * B.det * P.det = B.det := by
    have : P.det * B.det * P.det = (P.det * P.det) * B.det := by ring
    rw [this, hP2, one_mul]
  rw [hvol] at hdet
  exact hdet.symm


/-! ## The application datum: `J ⊕ J′ = U ⊕ U` is unimodular, and a scaled pairing is not -/

/-- The hyperbolic plane. -/
def hyperbolicPlane : Matrix (Fin 2) (Fin 2) ℤ := !![0, 1; 1, 0]

/-- `U ⊕ U`, the shape of `J ⊕ J′` for a primitive isotropic plane `J` and a genuine
integral complementary isotropic plane `J′` pairing perfectly with it. -/
def hyperbolic4 : Matrix (Sum (Fin 2) (Fin 2)) (Sum (Fin 2) (Fin 2)) ℤ :=
  Matrix.fromBlocks hyperbolicPlane 0 0 hyperbolicPlane

theorem det_hyperbolicPlane : hyperbolicPlane.det = -1 := by
  rw [Matrix.det_fin_two]
  simp [hyperbolicPlane]

theorem det_hyperbolic4 : hyperbolic4.det = 1 := by
  simp [hyperbolic4, hyperbolicPlane, Matrix.det_fin_two]

/-- The twice-scaled pairing — the shape a *rational* or scaled complement would have —
has determinant `16`, so it satisfies no unimodularity hypothesis and the splitting it
gives is only over `ℚ`.  This is the distinction the integral hypothesis carries. -/
theorem det_two_hyperbolic4 : ((2 : ℤ) • hyperbolic4).det = 16 := by
  rw [Matrix.det_smul, det_hyperbolic4]
  norm_num

#print axioms Coble.exists_mulVec_eq_of_unimodular
#print axioms Coble.splits_of_unimodular
#print axioms Coble.det_eq_mul_of_unimodular_block_diagonal
#print axioms Coble.det_hyperbolic4
#print axioms Coble.det_two_hyperbolic4

/-! ## The null vectors of `N = H ⊕ E₈² ⊕ A₁` in coordinates

With `H = <e, f>`, a vector `e + n•f + w` is isotropic exactly when `w² = -2n`.  This is
the parametrization of the null rays of `N` used to read the four one-cusps off the
maximal parabolic subdiagrams of the Coxeter diagram, the `w = 0` case giving `v = e`
and `J^⊥/J = E₈² ⊕ A₁`. -/

/-- `e + n f + w` has square zero when `w² = -2n`, for the form on `H ⊕ W`. -/
theorem isotropic_of_hyperbolic_parametrization {W : Type*} (bW : W → W → ℤ) (w : W) (n : ℤ)
    (hw : bW w w = -2 * n) :
    (fun (x y : ℤ × ℤ × W) => x.1 * y.2.1 + y.1 * x.2.1 + bW x.2.2 y.2.2)
      (1, n, w) (1, n, w) = 0 := by
  simp only
  rw [hw]
  ring

#print axioms Coble.isotropic_of_hyperbolic_parametrization

end Coble
