/-
A21 arithmetic core, machine-checked (Lean 4 + Mathlib, v4.33.1).

Finite integral statements about the lattice package of the labelled tuple
 𝔏_{Co,2} = (L_K3, I_Co, I_dP, H, α, c)
of writing/coble/heegner-report/coble-heegner-research-report.md, sec. "The Coble
lattice package" (commit cb48774f88).  Nothing here is geometric: the geometric
inputs are hypotheses of the statements in `report.md`.

Conventions: all Gram matrices are integer matrices; the bilinear form on ℤⁿ is
x ⬝ᵥ (G *ᵥ y), i.e. xᵀ G y.

  U      = [[0,1],[1,0]]                     (hyperbolic plane)
  U(2)   = [[0,2],[2,0]]
  E8(-m) = -m • (Cartan matrix of E8)        (negative definite, even, det m^8)
  S_dP   = U(2) ⊥ ⟨-2⟩                       (rank 3,  det -8)
  S_En   = U(2) ⊥ E8(-2)                     (rank 10, det -1024)
  T_En   = U ⊥ U(2) ⊥ E8(-2)                 (rank 12, det 1024)
  S_Co   = S_En ⊥ ⟨-2⟩                       (rank 11, det 2048)
  T_Co   = ⟨2⟩ ⊥ U(2) ⊥ E8(-2)               (rank 11, det -2048)
  L_K3   = U ⊥ U ⊥ U ⊥ E8(-1) ⊥ E8(-1)       (rank 22, det 1, unimodular)
-/
import Mathlib

namespace A21Arith

open Matrix

/-! ## The Cartan matrix of `E8` and the negative definite blocks -/

/-- Cartan matrix of `E8` (positive definite convention). -/
def cartanE8 : Matrix (Fin 8) (Fin 8) ℤ :=
  !![ 2, -1,  0,  0,  0,  0,  0,  0;
     -1,  2, -1,  0,  0,  0,  0,  0;
      0, -1,  2, -1,  0,  0,  0,  0;
      0,  0, -1,  2, -1,  0,  0,  0;
      0,  0,  0, -1,  2, -1,  0, -1;
      0,  0,  0,  0, -1,  2, -1,  0;
      0,  0,  0,  0,  0, -1,  2,  0;
      0,  0,  0,  0, -1,  0,  0,  2]

theorem det_cartanE8 : cartanE8.det = 1 := by native_decide

theorem cartanE8_even : ∀ i : Fin 8, cartanE8 i i % 2 = 0 := by native_decide

/-- `E8(-2)`, the negative definite even rank-8 block. -/
def E8m2 : Matrix (Fin 8) (Fin 8) ℤ := fun i j => -2 * cartanE8 i j

theorem E8m2_eq_smul : E8m2 = (-2 : ℤ) • cartanE8 := by
  ext i j; simp [E8m2]

theorem det_E8m2 : E8m2.det = 256 := by
  rw [E8m2_eq_smul, Matrix.det_smul, det_cartanE8]
  norm_num

/-- `E8(-1)`. -/
def E8m1 : Matrix (Fin 8) (Fin 8) ℤ := fun i j => -cartanE8 i j

theorem E8m1_eq_smul : E8m1 = (-1 : ℤ) • cartanE8 := by
  ext i j; simp [E8m1]

theorem det_E8m1 : E8m1.det = 1 := by
  rw [E8m1_eq_smul, Matrix.det_smul, det_cartanE8]
  norm_num

/-! ## The rank-3 del Pezzo package `S_dP = U(2) ⊥ ⟨-2⟩` -/

/-- `U(2)`. -/
def U2m : Matrix (Fin 2) (Fin 2) ℤ := !![0, 2; 2, 0]
/-- `U`. -/
def U1m : Matrix (Fin 2) (Fin 2) ℤ := !![0, 1; 1, 0]

theorem det_U2m : U2m.det = -4 := by native_decide
theorem det_U1m : U1m.det = -1 := by native_decide

/-- Gram matrix of `U(2) ⊥ ⟨-2⟩` in the basis `(h₁,h₂,α)`: `h₁² = h₂² = 0`,
`h₁·h₂ = 2`, `α² = -2`, `α ⊥ h₁, h₂`. -/
def G_dP : Matrix (Fin 3) (Fin 3) ℤ := !![0, 2, 0; 2, 0, 0; 0, 0, -2]

/-- The root `α`. -/
def alphaVec : Fin 3 → ℤ := ![0, 0, 1]

/-- The degree-4 class `H = π^*O(1,1) = h₁ + h₂`. -/
def Hvec : Fin 3 → ℤ := ![1, 1, 0]

theorem det_G_dP : G_dP.det = 8 := by native_decide

theorem G_dP_even : ∀ i : Fin 3, G_dP i i % 2 = 0 := by native_decide

theorem det_G_dP_not_unit : G_dP.det ≠ 1 ∧ G_dP.det ≠ -1 := by
  rw [det_G_dP]; decide

/-- **The degree-4 class is pinned by the root.**  In `U(2) ⊥ ⟨-2⟩` the only
classes of square `4` orthogonal to `α` are `± (h₁ + h₂)`. -/
theorem pinned (x : Fin 3 → ℤ)
    (hsq : x ⬝ᵥ (G_dP.mulVec x) = 4)
    (horth : x ⬝ᵥ (G_dP.mulVec alphaVec) = 0) :
    x = Hvec ∨ x = -Hvec := by
  have horth' : 2 * x 2 = 0 := by
    have h : x ⬝ᵥ (G_dP.mulVec alphaVec) = -(2 * x 2) := by
      simp [G_dP, alphaVec, Matrix.mulVec, dotProduct, Fin.sum_univ_succ]
      ring
    linarith
  have hsq' : 4 * (x 0 * x 1) - 2 * (x 2) ^ 2 = 4 := by
    have h : x ⬝ᵥ (G_dP.mulVec x) = 4 * (x 0 * x 1) - 2 * (x 2) ^ 2 := by
      simp [G_dP, Matrix.mulVec, dotProduct, Fin.sum_univ_succ]
      ring
    linarith
  have h2 : x 2 = 0 := by linarith
  rw [h2] at hsq'
  simp only [ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, mul_zero,
    sub_zero] at hsq'
  have hprod : x 0 * x 1 = 1 := by linarith
  have hunit := Int.mul_eq_one_iff_eq_one_or_neg_one.mp hprod
  rcases hunit with ⟨h0, h1⟩ | ⟨h0, h1⟩
  · left
    funext i
    fin_cases i <;> simp_all [Hvec]
  · right
    funext i
    fin_cases i <;> simp_all [Hvec]

/-! ## The rank-10, 11, 12 and 22 Gram matrices, and their determinants -/

theorem det_fromBlocks_block (m n : Type*) [Fintype m] [Fintype n]
    [DecidableEq m] [DecidableEq n]
    (A : Matrix m m ℤ) (D : Matrix n n ℤ) :
    (Matrix.fromBlocks A (0 : Matrix m n ℤ) (0 : Matrix n m ℤ) D).det
      = A.det * D.det :=
  Matrix.det_fromBlocks_zero₁₂ A 0 D

/-- `S_En = U(2) ⊥ E8(-2)`, rank 10. -/
def G_S_En : Matrix (Fin 2 ⊕ Fin 8) (Fin 2 ⊕ Fin 8) ℤ :=
  Matrix.fromBlocks U2m (0 : Matrix (Fin 2) (Fin 8) ℤ)
    (0 : Matrix (Fin 8) (Fin 2) ℤ) E8m2

theorem det_G_S_En : G_S_En.det = -1024 := by
  simp only [G_S_En, det_fromBlocks_block, det_U2m, det_E8m2]; norm_num

/-- `S_Co = U(2) ⊥ E8(-2) ⊥ ⟨-2⟩`, rank 11, the invariant lattice of `I_Co`. -/
def G_S_Co : Matrix ((Fin 2 ⊕ Fin 8) ⊕ Fin 1) ((Fin 2 ⊕ Fin 8) ⊕ Fin 1) ℤ :=
  Matrix.fromBlocks G_S_En (0 : Matrix (Fin 2 ⊕ Fin 8) (Fin 1) ℤ)
    (0 : Matrix (Fin 1) (Fin 2 ⊕ Fin 8) ℤ) !![(-2 : ℤ)]

theorem det_G_S_Co : G_S_Co.det = 2048 := by
  simp only [G_S_Co, det_fromBlocks_block, det_G_S_En, Matrix.det_fin_one]
  norm_num

/-- `T_Co = ⟨2⟩ ⊥ U(2) ⊥ E8(-2)`, rank 11, the anti-invariant lattice. -/
def G_T_Co : Matrix (Fin 1 ⊕ (Fin 2 ⊕ Fin 8)) (Fin 1 ⊕ (Fin 2 ⊕ Fin 8)) ℤ :=
  Matrix.fromBlocks !![(2 : ℤ)] (0 : Matrix (Fin 1) (Fin 2 ⊕ Fin 8) ℤ)
    (0 : Matrix (Fin 2 ⊕ Fin 8) (Fin 1) ℤ) G_S_En

theorem det_G_T_Co : G_T_Co.det = -2048 := by
  simp only [G_T_Co, det_fromBlocks_block, det_G_S_En, Matrix.det_fin_one]
  norm_num

/-- `T_En = U ⊥ U(2) ⊥ E8(-2)`, rank 12. -/
def G_T_En : Matrix ((Fin 2 ⊕ Fin 2) ⊕ Fin 8) ((Fin 2 ⊕ Fin 2) ⊕ Fin 8) ℤ :=
  Matrix.fromBlocks
    (Matrix.fromBlocks U1m (0 : Matrix (Fin 2) (Fin 2) ℤ) (0 : Matrix (Fin 2) (Fin 2) ℤ) U2m)
    (0 : Matrix (Fin 2 ⊕ Fin 2) (Fin 8) ℤ) (0 : Matrix (Fin 8) (Fin 2 ⊕ Fin 2) ℤ) E8m2

theorem det_G_T_En : G_T_En.det = 1024 := by
  simp only [G_T_En, det_fromBlocks_block, det_U1m, det_U2m, det_E8m2]
  norm_num

/-- `L_K3 = U³ ⊥ E8(-1)²`, rank 22, unimodular: `det = 1`. -/
def G_LK3 :
    Matrix (((Fin 2 ⊕ Fin 2) ⊕ Fin 2) ⊕ (Fin 8 ⊕ Fin 8))
      (((Fin 2 ⊕ Fin 2) ⊕ Fin 2) ⊕ (Fin 8 ⊕ Fin 8)) ℤ :=
  Matrix.fromBlocks
    (Matrix.fromBlocks
      (Matrix.fromBlocks U1m (0 : Matrix (Fin 2) (Fin 2) ℤ) (0 : Matrix (Fin 2) (Fin 2) ℤ) U1m)
      (0 : Matrix (Fin 2 ⊕ Fin 2) (Fin 2) ℤ) (0 : Matrix (Fin 2) (Fin 2 ⊕ Fin 2) ℤ) U1m)
    (0 : Matrix ((Fin 2 ⊕ Fin 2) ⊕ Fin 2) (Fin 8 ⊕ Fin 8) ℤ)
    (0 : Matrix (Fin 8 ⊕ Fin 8) ((Fin 2 ⊕ Fin 2) ⊕ Fin 2) ℤ)
    (Matrix.fromBlocks E8m1 (0 : Matrix (Fin 8) (Fin 8) ℤ) (0 : Matrix (Fin 8) (Fin 8) ℤ) E8m1)

theorem det_G_LK3 : G_LK3.det = -1 := by
  simp only [G_LK3, det_fromBlocks_block, det_U1m, det_E8m1]
  norm_num

/-- `L_K3` is unimodular (`|det| = 1`). -/
theorem G_LK3_unimodular : G_LK3.det = 1 ∨ G_LK3.det = -1 := by
  rw [det_G_LK3]; right; rfl

/-- `L_K3` is even: every diagonal entry of its Gram matrix is even. -/
theorem G_LK3_even : ∀ i, G_LK3 i i % 2 = 0 := by
  decide

/-! ## The root shapes in `T_En`: a counterexample to root uniqueness -/

/-- `T_En` written in a `Fin 12` basis `(e, f, u₁, u₂, r₁, …, r₈)`. -/
def G_T_En_fin : Matrix (Fin 12) (Fin 12) ℤ :=
  !![0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, -4, 2, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 2, -4, 2, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 2, -4, 2, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 2, -4, 2, 0, 0, 2;
     0, 0, 0, 0, 0, 0, 0, 2, -4, 2, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 2, -4, 2, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 2, -4, 0;
     0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, -4]

/-- `α = e - f`, the root of `U` used in the reflection twist. -/
def alphaT : Fin 12 → ℤ := ![1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

/-- `η = e + f`, of square `2`. -/
def etaT : Fin 12 → ℤ := ![1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

/-- The first simple root `r₁` of the `E8(-2)` block, of square `-4`. -/
def rootE8 : Fin 12 → ℤ := ![0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

/-- `β = η + r₁ = (e+f) + r₁`, a root of `T_En` of square `-2` outside the `U` summand. -/
def betaRoot : Fin 12 → ℤ := ![1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

theorem alphaT_sq : alphaT ⬝ᵥ (G_T_En_fin.mulVec alphaT) = -2 := by native_decide

theorem etaT_sq : etaT ⬝ᵥ (G_T_En_fin.mulVec etaT) = 2 := by native_decide

theorem rootE8_sq : rootE8 ⬝ᵥ (G_T_En_fin.mulVec rootE8) = -4 := by native_decide

theorem betaRoot_sq : betaRoot ⬝ᵥ (G_T_En_fin.mulVec betaRoot) = -2 := by native_decide

/-- `β` is not of the shape `± (e - f)`: it has a nonzero `E8(-2)` coordinate. -/
theorem betaRoot_not_U : betaRoot 4 = 1 := by native_decide

/-- The integral form of the corrected uniqueness statement: for a vector `β` of
`T_En` whose `E8` part and `U(2)` part vanish, the equation `(α·β) β = -2 α` — which
is exactly the condition that the twist `w_β ∘ I_En` fix `α` — forces `β = ±α`. -/
theorem twist_root_pinned (β : Fin 12 → ℤ)
    (h0 : (β 1 - β 0) * β 0 = -2)
    (h1 : (β 1 - β 0) * β 1 = 2)
    (hrest : ∀ i : Fin 12, 2 ≤ i.val → (β 1 - β 0) * β i = 0) :
    β = alphaT ∨ β = -alphaT := by
  have hs : (β 1 - β 0) * (β 1 - β 0) = 4 := by nlinarith
  have hne : β 1 - β 0 ≠ 0 := by
    rintro h; rw [h] at h0; omega
  have hval : β 1 - β 0 = 2 ∨ β 1 - β 0 = -2 := by
    have h1' : -(2 : ℤ) ≤ β 1 - β 0 := by nlinarith
    have h2' : β 1 - β 0 ≤ 2 := by nlinarith
    have h3 : β 1 - β 0 ≠ 1 := by intro h; rw [h] at hs; omega
    have h4 : β 1 - β 0 ≠ -1 := by intro h; rw [h] at hs; omega
    omega
  have hzero : ∀ i : Fin 12, 2 ≤ i.val → β i = 0 := by
    intro i hi
    have h := hrest i hi
    rcases mul_eq_zero.mp h with h' | h'
    · exact absurd h' hne
    · exact h'
  rcases hval with hv | hv
  · right
    have hb0 : β 0 = -1 := by nlinarith
    have hb1 : β 1 = 1 := by nlinarith
    funext i
    fin_cases i <;> simp_all [alphaT]
  · left
    have hb0 : β 0 = 1 := by nlinarith
    have hb1 : β 1 = -1 := by nlinarith
    funext i
    fin_cases i <;> simp_all [alphaT]


/-! ## No integral orthogonal splitting

The tuple's `H` and `α` lie in `S_dP = U(2) ⊥ ⟨-2⟩`, of determinant `8`.  Since a
unimodular lattice has summands of determinant `±1` in any orthogonal splitting,
`S_dP` cannot be an orthogonal direct summand of `L_K3`: this is the arithmetic
reason why the rational eigenspace splitting of `H²(X,ℤ)` is *not* integral, so no
argument may use `H²(X,ℤ) = S_dP ⊕ T_dP`. -/

theorem summand_det_unit {m n : Type*} [Fintype m] [Fintype n] [DecidableEq m]
    [DecidableEq n] (S : Matrix m m ℤ) (T : Matrix n n ℤ)
    (h : (Matrix.fromBlocks S (0 : Matrix m n ℤ) (0 : Matrix n m ℤ) T).det = 1 ∨
         (Matrix.fromBlocks S (0 : Matrix m n ℤ) (0 : Matrix n m ℤ) T).det = -1) :
    S.det = 1 ∨ S.det = -1 := by
  rcases h with h | h
  · rw [det_fromBlocks_block] at h
    rcases Int.mul_eq_one_iff_eq_one_or_neg_one.mp h with ⟨hS, _⟩ | ⟨hS, _⟩
    · exact Or.inl hS
    · exact Or.inr hS
  · rw [det_fromBlocks_block] at h
    have h2 : (-S.det) * T.det = 1 := by rw [neg_mul, h]; norm_num
    rcases Int.mul_eq_one_iff_eq_one_or_neg_one.mp h2 with ⟨hS, _⟩ | ⟨hS, _⟩ <;> omega

/-- `S_dP` is not unimodular, hence never a summand in an orthogonal splitting. -/
theorem S_dP_no_unit_det (h : G_dP.det = 1 ∨ G_dP.det = -1) : False := by
  rcases h with h | h <;> rw [det_G_dP] at h <;> omega


/-! ## Evenness of every Gram matrix

An integral lattice all of whose Gram matrix diagonal entries are even is even
(`x·x = Σᵢ xᵢ² Gᵢᵢ + 2 Σᵢ<ⱼ xᵢxⱼ Gᵢⱼ`).  The diagonals are checked here for every
lattice of the package; the composite lattices are given in explicit `Fin n`
coordinates for this check. -/

def G_S_En_fin : Matrix (Fin 10) (Fin 10) ℤ :=
  !![0, 2, 0, 0, 0, 0, 0, 0, 0, 0; 2, 0, 0, 0, 0, 0, 0, 0, 0, 0; 0, 0, -4, 2, 0, 0, 0, 0, 0, 0; 0, 0, 2, -4, 2, 0, 0, 0, 0, 0; 0, 0, 0, 2, -4, 2, 0, 0, 0, 0; 0, 0, 0, 0, 2, -4, 2, 0, 0, 0; 0, 0, 0, 0, 0, 2, -4, 2, 0, 2; 0, 0, 0, 0, 0, 0, 2, -4, 2, 0; 0, 0, 0, 0, 0, 0, 0, 2, -4, 0; 0, 0, 0, 0, 0, 0, 2, 0, 0, -4]

def G_S_Co_fin : Matrix (Fin 11) (Fin 11) ℤ :=
  !![0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0; 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0; 0, 0, -4, 2, 0, 0, 0, 0, 0, 0, 0; 0, 0, 2, -4, 2, 0, 0, 0, 0, 0, 0; 0, 0, 0, 2, -4, 2, 0, 0, 0, 0, 0; 0, 0, 0, 0, 2, -4, 2, 0, 0, 0, 0; 0, 0, 0, 0, 0, 2, -4, 2, 0, 2, 0; 0, 0, 0, 0, 0, 0, 2, -4, 2, 0, 0; 0, 0, 0, 0, 0, 0, 0, 2, -4, 0, 0; 0, 0, 0, 0, 0, 0, 2, 0, 0, -4, 0; 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2]

def G_T_Co_fin : Matrix (Fin 11) (Fin 11) ℤ :=
  !![2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0; 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0; 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0; 0, 0, 0, -4, 2, 0, 0, 0, 0, 0, 0; 0, 0, 0, 2, -4, 2, 0, 0, 0, 0, 0; 0, 0, 0, 0, 2, -4, 2, 0, 0, 0, 0; 0, 0, 0, 0, 0, 2, -4, 2, 0, 0, 0; 0, 0, 0, 0, 0, 0, 2, -4, 2, 0, 2; 0, 0, 0, 0, 0, 0, 0, 2, -4, 2, 0; 0, 0, 0, 0, 0, 0, 0, 0, 2, -4, 0; 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, -4]

theorem even_G_S_En : ∀ i : Fin 10, G_S_En_fin i i % 2 = 0 := by native_decide

theorem even_G_S_Co : ∀ i : Fin 11, G_S_Co_fin i i % 2 = 0 := by native_decide

theorem even_G_T_Co : ∀ i : Fin 11, G_T_Co_fin i i % 2 = 0 := by native_decide

theorem G_T_En_fin_even : ∀ i : Fin 12, G_T_En_fin i i % 2 = 0 := by native_decide

end A21Arith
