import Mathlib

/-!
# An involution that reverses the class of an effective curve

The manuscript's negative answer to A21 rests on one linear-algebraic step and one
positivity step:

* `slot_reverses_root` — the linear-algebra step.  Let `f` be an integral involution of
  the cohomology lattice commuting with the Coble involution, preserving the form `B`.
  Its fixed points in `S = ker (M - 1)` span the single line `ℚ H`, with `B H H ≠ 0`, and
  `f H = H`.  Then every `a ∈ S` orthogonal to `H` is negated: `f a = -a`.  The proof uses
  the ℚ-eigenspace decomposition of an involution only; no *integral* splitting of `S` is
  used, which is the point — the sum of the fixed and anti-fixed lattices has index 2 there.

* `not_preserves_effectivity_of_reversal` — the positivity step.  A map that carries an
  effective class to its negative cannot preserve effectivity, once a single linear
  functional `B · A` is positive on the nonzero effective classes; that functional is the
  degree against an ample class `A`.

* `no_automorphism_reverses_root` — the two together, with every hypothesis visible.

What is *not* formalized, and is a premise rather than a conclusion: that the induced
action of an automorphism of the surface preserves the effective cone, that the authored
class `α` is effective, and that a projective surface carries an ample class.  Those are
the geometric inputs; this file checks the logic that consumes them.
-/

namespace Coble

variable {V : Type*} [AddCommGroup V] [Module ℚ V]

/-- **The linear-algebra step.**  An involution preserving the form whose fixed points in
a stable subspace are the line spanned by a non-isotropic `H` negates every element of that
subspace orthogonal to `H`. -/
theorem slot_reverses_root
    (B : LinearMap.BilinForm ℚ V) (f : V ≃ₗ[ℚ] V)
    (hf : ∀ x, f (f x) = x)
    (hiso : ∀ x y, B (f x) (f y) = B x y)
    (S : Submodule ℚ V) (hS : ∀ x ∈ S, f x ∈ S)
    (H a : V) (hH : B H H ≠ 0) (hfH : f H = H)
    (hfix : ∀ x ∈ S, f x = x → ∃ c : ℚ, x = c • H)
    (ha : a ∈ S) (hHa : B a H = 0) :
    f a = -a := by
  have hsum_fix : f (f a + a) = f a + a := by
    rw [map_add, hf a, add_comm]
  have hsum_mem : f a + a ∈ S := S.add_mem (hS a ha) ha
  obtain ⟨c, hc⟩ := hfix (f a + a) hsum_mem hsum_fix
  have hfaH : B (f a) H = 0 := by
    have h1 : B (f a) (f H) = B a H := hiso a H
    rw [hfH, hHa] at h1
    exact h1
  have hkey : B (f a + a) H = 0 := by
    rw [map_add, LinearMap.add_apply, hfaH, hHa, add_zero]
  have hcH : B (f a + a) H = c * B H H := by
    rw [hc, map_smul, LinearMap.smul_apply, smul_eq_mul]
  have hzero : c * B H H = 0 := by rw [← hcH, hkey]
  have hc0 : c = 0 := by
    rcases mul_eq_zero.mp hzero with h | h
    · exact h
    · exact absurd h hH
  have hsum : f a + a = 0 := by rw [hc, hc0, zero_smul]
  rw [eq_neg_iff_add_eq_zero]
  exact hsum

/-- **The positivity step.**  If every nonzero class in a cone `C` has positive degree
against `A`, and a map preserving `C` sends `α ∈ C`, `α ≠ 0`, to `-α`, that is impossible. -/
theorem not_preserves_effectivity_of_reversal
    (B : LinearMap.BilinForm ℚ V) (g : V ≃ₗ[ℚ] V)
    (C : Set V) (A α : V)
    (hαC : α ∈ C) (hα0 : α ≠ 0)
    (hsep : ∀ x ∈ C, x ≠ 0 → 0 < B x A)
    (hpres : ∀ x ∈ C, g x ∈ C)
    (hrev : g α = -α) : False := by
  have hgα0 : g α ≠ 0 := by
    intro h
    apply hα0
    have hz : g α = g 0 := by rw [h, map_zero]
    exact g.injective hz
  have h1 : 0 < B α A := hsep α hαC hα0
  have h2 : 0 < B (g α) A := hsep (g α) (hpres α hαC) hgα0
  rw [hrev] at h2
  have h3 : 0 < -(B α A) := by simpa using h2
  linarith

/-- **The negative answer, with every premise visible.**  `f` is the induced action of an
automorphism of the cover: it is an integral isometry of the lattice (here `ℚ`-linear, as
the lattice is nondegenerate), it preserves the form, it commutes with the Coble involution
before quotienting — which is what makes `S` stable — its fixed points in `S` lie on the
line `ℚ H` (the rank-one case), and it fixes `H`.  `α` is the authored root: in `S`,
orthogonal to `H`, effective, and with nonzero degree against the ample class `A`.  Then
there is no such automorphism. -/
theorem no_automorphism_reverses_root
    (B : LinearMap.BilinForm ℚ V) (g : V ≃ₗ[ℚ] V)
    (hg : ∀ x, g (g x) = x)
    (hiso : ∀ x y, B (g x) (g y) = B x y)
    (S : Submodule ℚ V) (hS : ∀ x ∈ S, g x ∈ S)
    (H α : V) (hH : B H H ≠ 0) (hgH : g H = H)
    (hfix : ∀ x ∈ S, g x = x → ∃ c : ℚ, x = c • H)
    (hαS : α ∈ S) (hHα : B α H = 0)
    (C : Set V) (A : V) (hαC : α ∈ C) (hα0 : α ≠ 0)
    (hsep : ∀ x ∈ C, x ≠ 0 → 0 < B x A)
    (hpres : ∀ x ∈ C, g x ∈ C) : False :=
  not_preserves_effectivity_of_reversal B g C A α hαC hα0 hsep hpres
    (slot_reverses_root B g hg hiso S hS H α hH hgH hfix hαS hHα)

end Coble

namespace Coble

variable {V : Type*} [AddCommGroup V] [Module ℚ V]

/-- **The rank-two reduction.**  In the rank-two case the slot's invariant lattice is the whole
hyperbolic plane `⟨a₁, a₂⟩`, `H = ±(a₁ + a₂)`, and writing `α = p • (a₁ - a₂) + β` with `β`
orthogonal to the plane, the negative definiteness of `β`'s direction bounds `p`: the integer
`α · a₁ = -2p` can only be `-1`, `0` or `1`.  So the rank-two case is one integer away from the
same conclusion, and that integer is what the identification of the two constructions would fix. -/
theorem rank_two_narrowing
    (B : LinearMap.BilinForm ℚ V) (hsym : ∀ x y, B x y = B y x)
    (a1 a2 α β : V) (p : ℚ)
    (h11 : B a1 a1 = 0) (h22 : B a2 a2 = 0) (h12 : B a1 a2 = 2)
    (hα : α = p • (a1 - a2) + β)
    (hβ1 : B β a1 = 0) (hβ2 : B β a2 = 0)
    (hα2 : B α α = -2) (hneg : B β β ≤ 0) :
    p ^ 2 ≤ 1 / 2 := by
  have h21 : B a2 a1 = 2 := by rw [hsym a2 a1, h12]
  have hdiff : B (a1 - a2) (a1 - a2) = -4 := by
    rw [LinearMap.BilinForm.sub_left, LinearMap.BilinForm.sub_right,
      LinearMap.BilinForm.sub_right, h11, h22, h12, h21]
    norm_num
  have hcross : B (a1 - a2) β = 0 := by
    have e1 : B a1 β = 0 := by rw [hsym a1 β, hβ1]
    have e2 : B a2 β = 0 := by rw [hsym a2 β, hβ2]
    rw [LinearMap.BilinForm.sub_left, e1, e2]
    norm_num
  have hback : B β (a1 - a2) = 0 := by rw [hsym, hcross]
  have hexp : B α α = p ^ 2 * (-4) + B β β := by
    rw [hα, LinearMap.BilinForm.add_left, LinearMap.BilinForm.smul_left,
      LinearMap.BilinForm.add_right, LinearMap.BilinForm.add_right,
      LinearMap.BilinForm.smul_right, LinearMap.BilinForm.smul_right,
      hdiff, hcross, hback]
    ring
  nlinarith

end Coble
