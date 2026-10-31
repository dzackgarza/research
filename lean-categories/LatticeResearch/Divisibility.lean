/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
module

public import Mathlib.Algebra.GCDMonoid.Finset
public import Mathlib.Tactic
public import Mathlib.Algebra.BigOperators.Group.Finset.Basic
public import Mathlib.Data.Int.GCD
public import Mathlib.Data.Matrix.Basic

/-!
# Divisibility in a Gram-matrix lattice

For an integral Gram matrix `G : Matrix n n ℤ`, the lattice `ℤⁿ` with the form
`(x, y) ↦ xᵀ G y` has, at a vector `v`, the divisibility `divis G v`: the greatest
natural number dividing every value `β_G(v, w)`, `w ∈ ℤⁿ`. Because the form is
linear in its second argument it suffices to divide the values on a basis, which
is what `divis` computes.

The point of the file is the statement that the Coble cusp computations use, and
the two vectors that show its naive forms are false. For `G = (2)`:

* `divis (2) 1 = 2`, while `divis (2) 2 = 4` and `divis (2) 3 = 6`;
* so divisibility `2` is neither implied by "pairs nontrivially with something"
  nor characterized by "not a double".

What isolates it is primitivity, and only because the sublattice is unimodular:
`divis G v = 1` says the functional `β_G(v, -)` is surjective, which in a
unimodular lattice is primitivity of `v`. The implication primitivity ⇒ `divis = 1`
is not formalized here; `divis G v = 1 ⇒ divis (2 • G) v = 2` is.

Twisting by `2` doubles the form, hence doubles every divisibility
(`divis_twist`); this is the reason every divisibility in the Coble lattice
`T_Co = L(2)` is even.
-/

@[expose] public section

open Finset Matrix

namespace LatticeResearch

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The value of the bilinear form `G` on a pair of vectors, `β_G(v, w) = ∑ᵢ vᵢ ∑ⱼ Gᵢⱼ wⱼ`. -/
def form (G : Matrix n n ℤ) (v w : n → ℤ) : ℤ :=
  ∑ i, v i * ∑ j, G i j * w j

omit [DecidableEq n] in
@[simp] theorem form_zero_left (G : Matrix n n ℤ) (w : n → ℤ) : form G 0 w = 0 := by
  simp [form]

omit [DecidableEq n] in
theorem form_smul_left (G : Matrix n n ℤ) (c : ℤ) (v w : n → ℤ) :
    form G (c • v) w = c * form G v w := by
  simp only [form, Pi.smul_apply, smul_eq_mul, Finset.mul_sum, mul_assoc]

/-- The divisibility of `v`: the gcd of the values `β_G(v, eⱼ)` over a basis. -/
def divis (G : Matrix n n ℤ) (v : n → ℤ) : ℕ :=
  Finset.gcd univ fun j => (form G v (Pi.single j 1)).natAbs

/-- The gcd of a finitely supported family scaled by `m` is `m` times the gcd. -/
theorem gcd_of_mul {β : Type*} (s : Finset β) (f : β → ℕ) (m : ℕ) :
    s.gcd (fun j => m * f j) = m * s.gcd f := by
  classical
  induction s using Finset.induction with
  | empty => simp
  | insert a s ha ih =>
    rw [Finset.gcd_insert, Finset.gcd_insert, ih]
    exact Nat.gcd_mul_left m (f a) (s.gcd f)

/-- Twisting the form by `c` multiplies every divisibility by `|c|`. -/
theorem divis_smul (G : Matrix n n ℤ) (c : ℤ) (v : n → ℤ) :
    divis G (c • v) = c.natAbs * divis G v := by
  unfold divis
  have h : (fun j => (form G (c • v) (Pi.single j 1)).natAbs)
      = fun j => c.natAbs * (form G v (Pi.single j 1)).natAbs := by
    funext j; rw [form_smul_left, Int.natAbs_mul]
  rw [h, gcd_of_mul]

/-- Scaling the Gram matrix by `c` scales the form by `c`: `β_{cG} = c β_G`. -/
theorem form_smul (G : Matrix n n ℤ) (c : ℤ) (v w : n → ℤ) :
    form (c • G) v w = c * form G v w := by
  simp only [form, Matrix.smul_apply, smul_eq_mul]
  have h : ∀ i, ∑ j, c * G i j * w j = c * ∑ j, G i j * w j := by
    intro i
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun j _ => by ring
  simp only [h, Finset.mul_sum]
  exact Finset.sum_congr rfl fun i _ => by ring

/-- Scaling the Gram matrix by `c` scales every divisibility by `|c|`. -/
theorem divis_twist (G : Matrix n n ℤ) (c : ℤ) (v : n → ℤ) :
    divis (c • G) v = c.natAbs * divis G v := by
  unfold divis
  have h : (fun j => (form (c • G) v (Pi.single j 1)).natAbs)
      = fun j => c.natAbs * (form G v (Pi.single j 1)).natAbs := by
    funext j; rw [form_smul, Int.natAbs_mul]
  rw [h, gcd_of_mul]

/-- The case used by the Coble cusp computations. If `T = L(2)`, that is the Gram
matrix of `T` is twice that of `L`, then `div_T(v) = 2 div_L(v)` for every `v`. -/
theorem divis_two_smul (G : Matrix n n ℤ) (v : n → ℤ) :
    divis (2 • G) v = 2 * divis G v := by
  simpa using divis_twist G 2 v

/-- Consequence for the Coble lattice: every divisibility in `T_Co = L(2)` is
even, whatever the vector. -/
theorem two_dvd_divis_two_smul (G : Matrix n n ℤ) (v : n → ℤ) :
    2 ∣ divis (2 • G) v := by
  rw [divis_two_smul]
  exact dvd_mul_right 2 _

/-- Divisor `2` in `L(2)` is exactly divisor `1` in `L`: the condition is one on
the unimodular lattice `L`, and it is what the corrected lemma in the book states.
Inside `T_Co` it is not primitivity -- `divis G v = 1` implies `v` is primitive,
not conversely. -/
theorem divis_two_smul_eq_two_iff (G : Matrix n n ℤ) (v : n → ℤ) :
    divis (2 • G) v = 2 ↔ divis G v = 1 := by
  rw [divis_two_smul]
  constructor
  · intro h; omega
  · intro h; rw [h]

/-! ### The rank-one lattice `⟨2⟩` and the two failed converse implications

Over `G = (2)` the form is `β(x, y) = 2xy`, so `divis G v = 2 * |v 0|`. The vector
`2` then has divisibility `4` although it is a double, and `3` has divisibility
`6` although it is not a double: neither "is a double" nor "is not a double"
decides divisibility `2`. The hypothesis that does is primitivity. -/

/-- The Gram matrix of `⟨2⟩`. -/
def G2 : Matrix (Fin 1) (Fin 1) ℤ := fun _ _ => 2

theorem divis_G2 (v : Fin 1 → ℤ) : divis G2 v = 2 * (v 0).natAbs := by
  simp [divis, G2, form, Int.natAbs_mul, mul_comm]

/-- The generator has divisibility `2`. -/
theorem divis_G2_gen : divis G2 (fun _ => (1 : ℤ)) = 2 := by
  rw [divis_G2]; norm_num

/-- The double of the generator has divisibility `4`. -/
theorem divis_G2_two : divis G2 (fun _ => (2 : ℤ)) = 4 := by
  rw [divis_G2]; norm_num

/-- Three times the generator has divisibility `6`. -/
theorem divis_G2_three : divis G2 (fun _ => (3 : ℤ)) = 6 := by
  rw [divis_G2]; norm_num

/-- Outside `2L` does not force divisibility `2`: in `⟨2⟩` the vector `3` is not
twice an integral vector, and its divisibility is `6`. -/
theorem not_dvd_two_divis_three :
    ¬ ∃ w : Fin 1 → ℤ, (fun _ => (3 : ℤ)) = (2 : ℤ) • w := by
  rintro ⟨w, hw⟩
  have h := congrFun hw 0
  simp at h
  omega

theorem divis_G2_three_ne_two : divis G2 (fun _ => (3 : ℤ)) ≠ 2 := by
  rw [divis_G2_three]; norm_num


/-! ### Primitivity, and the hypothesis that divides the true statement from the false

`divis G v = 1` says the functional `β_G(v, -)` is surjective. In a unimodular lattice
that is primitivity of `v`, and this is the step the corrected lemma in the book takes.
It fails for a form that is not unimodular: in `⟨2⟩` the generator is primitive with
divisibility `2`, and `3` is not primitive and has divisibility `6`. So neither
direction survives without the hypothesis, which is why the earlier forms of the lemma
were false and this one carries it. -/

/-- The gcd of the coordinates of a vector. -/
def vecGcd (v : n → ℤ) : ℕ := Finset.univ.gcd fun i => (v i).natAbs

/-- A vector is primitive when no natural number greater than one divides all of its
coordinates. This is invariant under unimodular change of coordinates, so it names a
property of the vector in the lattice and not of the basis. -/
def IsPrimitive (v : n → ℤ) : Prop := ∀ m : ℕ, (∀ i, m ∣ (v i).natAbs) → m = 1

theorem isPrimitive_iff_vecGcd_eq_one (v : n → ℤ) : IsPrimitive v ↔ vecGcd v = 1 := by
  constructor
  · intro h
    exact h (vecGcd v) fun i => Finset.gcd_dvd (Finset.mem_univ i)
  · intro h m hm
    have hdvd : m ∣ vecGcd v := Finset.dvd_gcd fun i _ => hm i
    rw [h] at hdvd
    exact Nat.dvd_one.mp hdvd

/-- Rescaling by a unit does not change the gcd of the coordinates. -/
theorem vecGcd_smul_of_natAbs_eq_one (c : ℤ) (hc : c.natAbs = 1) (v : n → ℤ) :
    vecGcd (c • v) = vecGcd v := by
  simp only [vecGcd, Pi.smul_apply, smul_eq_mul, Int.natAbs_mul, hc, one_mul]

/-- A finite sum of integers each divisible by `a` is divisible by `a`. -/
theorem dvd_finset_sum {β : Type*} (s : Finset β) {a : ℤ} {f : β → ℤ}
    (h : ∀ j ∈ s, a ∣ f j) : a ∣ ∑ j ∈ s, f j :=
  Finset.dvd_sum h

/-- Each coordinate of `M v` is an integral combination of the coordinates of `v`, so
the gcd of the coordinates of `v` divides the gcd of those of `M v`. -/
theorem vecGcd_dvd_vecGcd_mulVec (M : Matrix n n ℤ) (v : n → ℤ) :
    vecGcd v ∣ vecGcd (M.mulVec v) := by
  apply Finset.dvd_gcd
  intro i _
  have h : (vecGcd v : ℤ) ∣ M.mulVec v i := by
    simp only [Matrix.mulVec, dotProduct]
    refine dvd_finset_sum (Finset.univ : Finset n) fun j _ => ?_
    refine dvd_mul_of_dvd_right ?_ (M i j)
    refine (Int.natAbs_dvd_natAbs (a := (vecGcd v : ℤ)) (b := v j)).mp ?_
    show (Finset.univ.gcd fun i => (v i).natAbs) ∣ (v j).natAbs
    exact Finset.gcd_dvd (Finset.mem_univ j)
  simpa using (Int.natAbs_dvd_natAbs (a := (vecGcd v : ℤ)) (b := M.mulVec v i)).mpr h

/-- The gcd of the coordinates is invariant under a unimodular change of coordinates. -/
theorem vecGcd_mulVec_of_isUnit_det (G : Matrix n n ℤ) (hG : IsUnit G.det) (v : n → ℤ) :
    vecGcd (G.mulVec v) = vecGcd v := by
  have hunit : G.det.natAbs = 1 := by
    rcases Int.isUnit_iff.mp hG with h | h <;> simp [h]
  have hadj : G.adjugate.mulVec (G.mulVec v) = G.det • v := by
    rw [Matrix.mulVec_mulVec, Matrix.adjugate_mul, Matrix.smul_mulVec, Matrix.one_mulVec]
  have h1 : vecGcd v ∣ vecGcd (G.mulVec v) := vecGcd_dvd_vecGcd_mulVec G v
  have h2 : vecGcd (G.mulVec v) ∣ vecGcd v := by
    have h := vecGcd_dvd_vecGcd_mulVec G.adjugate (G.mulVec v)
    rw [hadj, vecGcd_smul_of_natAbs_eq_one G.det hunit] at h
    exact h
  exact (Nat.dvd_antisymm h1 h2).symm

/-- For a unimodular form, divisibility is the gcd of the coordinates. -/
theorem divis_eq_vecGcd (G : Matrix n n ℤ) (hG : IsUnit G.det) (v : n → ℤ) :
    divis G v = vecGcd v := by
  have hfun : (fun j => (form G v (Pi.single j 1)).natAbs)
      = fun j => ((Gᵀ.mulVec v) j).natAbs := by
    funext j
    have h : form G v (Pi.single j 1) = (Gᵀ.mulVec v) j := by
      have inner : ∀ i, (∑ k, G i k * (Pi.single j (1 : ℤ) : n → ℤ) k) = G i j := by
        intro i
        rw [Finset.sum_eq_single j]
        · simp
        · intro k _ hk
          simp only [Pi.single_apply, if_neg hk]
          ring
        · intro hj
          simp at hj
      simp only [form, Matrix.mulVec, dotProduct, Matrix.transpose_apply, inner]
      exact Finset.sum_congr rfl fun i _ => by ring
    rw [h]
  unfold divis
  rw [hfun, vecGcd]
  exact vecGcd_mulVec_of_isUnit_det Gᵀ (by rwa [Matrix.det_transpose]) v

/-- The corrected statement with its hypothesis: for unimodular `G`, divisibility `2`
in the form `2G` is primitivity in `G`. With `G` the Gram matrix of the unimodular
`L = ⟨1⟩ ⊕ E₁₀` this is the book's `div_T = 2 div_L` together with `div_L = 1 ↔ v`
primitive, for `T = L(2)`. -/
theorem divis_two_smul_eq_two_iff_isPrimitive (G : Matrix n n ℤ) (hG : IsUnit G.det)
    (v : n → ℤ) : divis (2 • G) v = 2 ↔ IsPrimitive v := by
  rw [divis_two_smul, isPrimitive_iff_vecGcd_eq_one, ← divis_eq_vecGcd G hG]
  constructor
  · intro h; omega
  · intro h; rw [h]

/-- **Primitive**, the definition the manuscript uses: `v` is not a proper positive
multiple of another vector of `ℤⁿ`, i.e. no `m > 1` has `v = m • u`. The condition is
coordinate-free, and `primitive_iff_isPrimitive` identifies it with the gcd formulation
`IsPrimitive` used above. -/
def Primitive (v : n → ℤ) : Prop := ¬ ∃ m : ℕ, 1 < m ∧ ∃ u : n → ℤ, v = (m : ℤ) • u

/-- The two definitions of primitivity agree: not being a proper multiple is the same as
the coordinates having no common divisor. -/
theorem primitive_iff_isPrimitive (v : n → ℤ) : Primitive v ↔ IsPrimitive v := by
  constructor
  · intro h m hm
    have hdiv : ∀ j, ∃ c : ℤ, v j = (m : ℤ) * c := by
      intro j
      obtain ⟨c, hc⟩ :=
        (Int.natAbs_dvd_natAbs (a := (m : ℤ)) (b := v j)).mp (by simpa using hm j)
      exact ⟨c, hc⟩
    set u : n → ℤ := fun j => Classical.choose (hdiv j) with hu
    have hvu : ∀ j, v j = (m : ℤ) * u j := fun j => Classical.choose_spec (hdiv j)
    by_contra hm1
    rcases Nat.eq_zero_or_pos m with hm0 | hpos
    · refine h ⟨2, by norm_num, 0, ?_⟩
      funext j
      have h0 := hvu j
      rw [hm0] at h0
      simpa using h0
    · have hgt : 1 < m := by omega
      refine h ⟨m, hgt, u, ?_⟩
      funext j
      rw [Pi.smul_apply, smul_eq_mul]
      exact hvu j
  · rintro h ⟨m, hm, u, hu⟩
    have hdiv : ∀ i, m ∣ (v i).natAbs := by
      intro i
      have hi : v i = (m : ℤ) * u i := by
        rw [hu]
        simp [Pi.smul_apply]
      rw [hi, Int.natAbs_mul]
      exact dvd_mul_right m _
    exact absurd (h m hdiv) (by omega)

/-! #### The duality route: divisibility of the functional is containment in `mL`

The manuscript's proof of the disputed step does not compute a gcd. It says that
`β_L(v, -)` is divisible by `m` exactly when `v ∈ mL`, so that `div_L(v) = 1` is
indivisibility of the functional and hence primitivity of the vector. The half with
content is that divisibility of the functional forces `v ∈ mL`, and it is where the
integral duality isomorphism is spent: for a unimodular `G`, `x ↦ β_G(x, -)` is an
isomorphism onto the dual, inverted by the adjugate over the determinant. -/

/-- The value of the form at a basis vector is the corresponding coordinate of `Gᵀ v`. -/
theorem form_single (G : Matrix n n ℤ) (v : n → ℤ) (j : n) :
    form G v (Pi.single j 1) = (Gᵀ.mulVec v) j := by
  have inner : ∀ i, (∑ k, G i k * (Pi.single j (1 : ℤ) : n → ℤ) k) = G i j := by
    intro i
    rw [Finset.sum_eq_single j]
    · simp
    · intro k _ hk
      simp only [Pi.single_apply, if_neg hk]
      ring
    · intro hj
      simp at hj
  simp only [form, Matrix.mulVec, dotProduct, Matrix.transpose_apply, inner]
  exact Finset.sum_congr rfl fun i _ => by ring

/-- **The duality step.** For a unimodular `G`, `m` divides every value of
`β_G(v, -)` exactly when `v ∈ mL`.

The forward direction is the one with content: the dual vector attached to `v` is `m`
times an integral one, and the duality isomorphism — whose inverse is the adjugate
over the determinant, integral because the determinant is a unit — carries that back
to `v = m u`. -/
theorem forall_dvd_form_iff (G : Matrix n n ℤ) (hG : IsUnit G.det) (v : n → ℤ) (m : ℤ) :
    (∀ w, m ∣ form G v w) ↔ ∃ u : n → ℤ, v = m • u := by
  constructor
  · intro h
    have hz : ∀ j, ∃ z : ℤ, (Gᵀ.mulVec v) j = m * z := by
      intro j
      obtain ⟨z, hz⟩ := h (Pi.single j 1)
      exact ⟨z, by rw [← form_single]; exact hz⟩
    choose z hz using hz
    have hzv : Gᵀ.mulVec v = m • z := by
      funext j
      rw [Pi.smul_apply, smul_eq_mul]
      exact hz j
    have hsq : G.det * G.det = 1 := by
      rcases Int.isUnit_iff.mp hG with h' | h' <;> simp [h']
    have hadj : (Gᵀ).adjugate.mulVec (Gᵀ.mulVec v) = G.det • v := by
      rw [Matrix.mulVec_mulVec, Matrix.adjugate_mul, Matrix.det_transpose,
        Matrix.smul_mulVec, Matrix.one_mulVec]
    refine ⟨G.det • (Gᵀ).adjugate.mulVec z, ?_⟩
    calc v = G.det • (G.det • v) := by rw [smul_smul, hsq, one_smul]
      _ = G.det • (Gᵀ).adjugate.mulVec (Gᵀ.mulVec v) := by rw [hadj]
      _ = G.det • (Gᵀ).adjugate.mulVec (m • z) := by rw [hzv]
      _ = G.det • (m • (Gᵀ).adjugate.mulVec z) := by rw [Matrix.mulVec_smul]
      _ = m • (G.det • (Gᵀ).adjugate.mulVec z) := by
            rw [smul_smul, smul_smul, mul_comm]
  · rintro ⟨u, hu⟩ w
    rw [hu, form_smul_left]
    exact dvd_mul_right m _

/-- Every value of the form is an integral combination of its values on a basis. -/
theorem form_apply_eq_sum (G : Matrix n n ℤ) (v w : n → ℤ) :
    form G v w = ∑ j, w j * form G v (Pi.single j 1) := by
  have lhs : form G v w = ∑ i, ∑ k, v i * (G i k * w k) := by
    simp only [form, Finset.mul_sum]
  have rhs : (∑ j, w j * form G v (Pi.single j 1))
      = ∑ j, ∑ i, w j * (G i j * v i) := by
    simp only [form_single, Matrix.mulVec, dotProduct, Matrix.transpose_apply, Finset.mul_sum]
  rw [lhs, rhs, Finset.sum_comm]
  exact Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun i _ => by ring

/-- The divisibility divides every value of the form, not only those on a basis. -/
theorem divis_dvd_form (G : Matrix n n ℤ) (v w : n → ℤ) : (divis G v : ℤ) ∣ form G v w := by
  rw [form_apply_eq_sum]
  refine dvd_finset_sum (Finset.univ : Finset n) fun j _ => ?_
  refine dvd_mul_of_dvd_right ?_ (w j)
  exact (Int.natAbs_dvd_natAbs (a := (divis G v : ℤ)) (b := form G v (Pi.single j 1))).mp
    (Finset.gcd_dvd (Finset.mem_univ j))

/-- Divisibility one is indivisibility of the functional: no `m > 1` divides all of its
values. -/
theorem divis_eq_one_iff_forall_not_dvd (G : Matrix n n ℤ) (v : n → ℤ) :
    divis G v = 1 ↔ ∀ m : ℕ, 1 < m → ∃ w, ¬ ((m : ℤ) ∣ form G v w) := by
  constructor
  · intro h m hm
    by_contra hcon
    simp only [not_exists, not_not] at hcon
    have hdvd : m ∣ divis G v :=
      Finset.dvd_gcd fun j _ =>
        (Int.natAbs_dvd_natAbs (a := (m : ℤ)) (b := form G v (Pi.single j 1))).mpr
          (hcon (Pi.single j 1))
    rw [h] at hdvd
    have hm1 : m = 1 := Nat.dvd_one.mp hdvd
    omega
  · intro h
    by_contra hne
    rcases Nat.eq_zero_or_pos (divis G v) with h0 | hpos
    · -- divisibility zero forces every value to vanish, so `2` divides them all
      obtain ⟨w, hw⟩ := h 2 (by norm_num)
      refine hw ?_
      have hall : ∀ j, form G v (Pi.single j 1) = 0 := by
        intro j
        exact Int.natAbs_eq_zero.mp (Finset.gcd_eq_zero_iff.mp h0 j (Finset.mem_univ j))
      rw [form_apply_eq_sum]
      simp only [hall, mul_zero, Finset.sum_const_zero]
      exact dvd_zero (2 : ℤ)
    · -- otherwise the divisibility itself is at least two and divides every value
      have h2 : 1 < divis G v := by omega
      exact (h (divis G v) h2).elim fun w hw => hw (divis_dvd_form G v w)

/-- **The contested theorem, through the duality isomorphism.** For an integral form `G`
whose determinant is a unit — `G` unimodular, `det G = ±1` — and a vector `v ∈ ℤⁿ`, the
divisibility of `v` in the form `2G` is `2` exactly when `v` is primitive, that is, when
`v` is not a proper multiple `m • u` of another vector for any `m > 1`.

Both halves are the manuscript's sentence: divisibility `2` in `2G` is divisibility `1`
in `G`; divisibility one says no `m > 1` divides all the values of `β_G(v, -)`; and by
`forall_dvd_form_iff` that is the same as `v ∉ mL` for every `m > 1`. -/
theorem divis_two_smul_eq_two_iff_primitive (G : Matrix n n ℤ) (hG : IsUnit G.det)
    (v : n → ℤ) : divis (2 • G) v = 2 ↔ Primitive v := by
  rw [divis_two_smul]
  constructor
  · rintro h ⟨m, hm, u, hu⟩
    have h1 : divis G v = 1 := by omega
    obtain ⟨w, hw⟩ := (divis_eq_one_iff_forall_not_dvd G v).mp h1 m hm
    exact hw (by rw [hu, form_smul_left]; exact dvd_mul_right (m : ℤ) _)
  · intro hproper
    have h1 : divis G v = 1 := by
      by_contra hne
      rcases Nat.eq_zero_or_pos (divis G v) with h0 | hpos
      · -- divisibility zero forces `v = 0`, which is `2 • 0`
        have hall : ∀ j, form G v (Pi.single j 1) = 0 := by
          intro j
          exact Int.natAbs_eq_zero.mp (Finset.gcd_eq_zero_iff.mp h0 j (Finset.mem_univ j))
        have hzero : Gᵀ.mulVec v = 0 := by
          funext j
          rw [← form_single, hall, Pi.zero_apply]
        have hadj : (Gᵀ).adjugate.mulVec (Gᵀ.mulVec v) = G.det • v := by
          rw [Matrix.mulVec_mulVec, Matrix.adjugate_mul, Matrix.det_transpose,
            Matrix.smul_mulVec, Matrix.one_mulVec]
        have hdet : G.det ≠ 0 := by
          rcases Int.isUnit_iff.mp hG with h' | h' <;> simp [h']
        have hd : G.det • v = 0 := by rw [← hadj, hzero, Matrix.mulVec_zero]
        have hv0 : v = 0 := by
          funext j
          have hcoord : G.det * v j = 0 := by
            simpa [Pi.smul_apply, smul_eq_mul] using congrFun hd j
          rcases Int.mul_eq_zero.mp hcoord with h' | h'
          · exact absurd h' hdet
          · exact h'
        exact hproper ⟨2, by norm_num, 0, by rw [hv0]; simp⟩
      · -- otherwise the divisibility itself is a proper multiple factor
        have h2 : 1 < divis G v := by omega
        obtain ⟨u, hu⟩ :=
          (forall_dvd_form_iff G hG v (divis G v)).mp fun w => divis_dvd_form G v w
        exact hproper ⟨divis G v, h2, u, hu⟩
    rw [h1]

/-! #### The hypothesis cannot be dropped

`G2` has determinant `2`, so it is not unimodular, and the equivalence fails there in
both directions: the generator is primitive with divisibility `2`, and `3` is not
primitive and has divisibility `6`. -/

theorem G2_det : G2.det = 2 := by
  simp [G2]

theorem G2_det_not_isUnit : ¬ IsUnit G2.det := by
  rw [G2_det]
  decide

theorem isPrimitive_G2_gen : IsPrimitive (n := Fin 1) (fun _ => (1 : ℤ)) := by
  rw [isPrimitive_iff_vecGcd_eq_one]
  simp [vecGcd]

theorem not_isPrimitive_G2_three : ¬ IsPrimitive (n := Fin 1) (fun _ => (3 : ℤ)) := by
  rw [isPrimitive_iff_vecGcd_eq_one]
  simp [vecGcd]

/-! ### The stable-group separation of isotropic lines

An integral automorphism of `ℤⁿ` that acts trivially on `ℤⁿ/2ℤⁿ` cannot carry the line
spanned by `e` to the line spanned by `f` when `e` and `f` have different residues modulo
`2`. The core is small and uses no lattice theory beyond spans: equality of the lines
gives `g e = m • f` with `m` a unit, both signs of a vector agree modulo `2`, and the
trivial action modulo `2` then forces `e` and `f` to agree modulo `2`.

This is the lemma the Coble cusp chapter uses for the stable orthogonal group. It says
nothing about how many orbits there are: it separates one pair of lines, which is what
the counterexample requires, and no more. -/

/-- `g` acts trivially modulo `2` on `ℤⁿ`: every vector moves by twice a vector.

In the notation of the book this is the condition defining the stable subgroup. Three
groups occur there and only the last two satisfy it: the full orthogonal group `O(T)`,
which acts nontrivially on the discriminant group and is transitive on primitive
isotropic vectors; the stable subgroup `O*(T) = ker (O(T) → O(A_T))`, which is the
discriminant kernel; and the arithmetic group of the moduli space,
`Γ_Co = O⁺(T)* = O*(T) ∩ O⁺(T)`, which is the one this file's separation is used for.
For `T = B(2)` the discriminant group is `B/2B`, with classes the residues `x mod 2B`,
so triviality of the action is the congruence below. -/
def ActsTriviallyModTwo (g : (n → ℤ) ≃ₗ[ℤ] (n → ℤ)) : Prop := ∀ x, ∃ y, g x = x + 2 • y

/-- **The separation lemma.** If `g` acts trivially modulo `2`, if the lines spanned by
`g e` and by `f` are equal, and if `f` is nonzero, then `e` and `f` have the same residue
modulo `2`. Turned around: distinct residues forbid the equality of lines.

The hypotheses are weaker than the manuscript's: `g` need not preserve any form here, and
primitivity of `e` is not used — equality of the two spans supplies the unit case
directly, which containment alone would not. -/
theorem sub_mem_two_of_span_eq (g : (n → ℤ) ≃ₗ[ℤ] (n → ℤ)) (hg : ActsTriviallyModTwo g)
    {e f : n → ℤ} (hf : f ≠ 0)
    (hspan : Submodule.span ℤ ({g e} : Set (n → ℤ)) = Submodule.span ℤ ({f} : Set (n → ℤ))) :
    ∃ y, e - f = 2 • y := by
  -- `g e` lies in the line of `f`, and `f` in the line of `g e`
  have h1 : g e ∈ Submodule.span ℤ ({f} : Set (n → ℤ)) := by
    rw [← hspan]; exact Submodule.mem_span_singleton_self _
  have h2 : f ∈ Submodule.span ℤ ({g e} : Set (n → ℤ)) := by
    rw [hspan]; exact Submodule.mem_span_singleton_self _
  obtain ⟨m, hm⟩ := Submodule.mem_span_singleton.mp h1
  obtain ⟨k, hk⟩ := Submodule.mem_span_singleton.mp h2
  -- composing the two give `f = (k * m) • f`, and `f ≠ 0` makes `m` a unit
  have hkm : f = (k * m) • f := by
    calc f = k • (g e) := hk.symm
      _ = k • (m • f) := by rw [hm]
      _ = (k * m) • f := by rw [smul_smul]
  have hunit : k * m = 1 := by
    by_contra hne
    have hz : (k * m - 1) • f = 0 := by rw [sub_smul, one_smul, ← hkm, sub_self]
    rcases smul_eq_zero.mp hz with h | h
    · omega
    · exact hf h
  have hm_unit : m = 1 ∨ m = -1 := by
    have : IsUnit m := ⟨⟨m, k, by rw [mul_comm]; exact hunit, hunit⟩, rfl⟩
    exact Int.isUnit_iff.mp this
  obtain ⟨y, hy⟩ := hg e
  rcases hm_unit with hm1 | hm1
  · -- `g e = f`
    have hf_eq : f = e + 2 • y := by rw [← hm, hm1, one_smul] at hy; exact hy
    exact ⟨-y, by rw [hf_eq]; module⟩
  · -- `g e = -f`, so `e - f = 2 • (e + y)`
    have hf_eq : f = -e - 2 • y := by
      have : -f = e + 2 • y := by rw [← hm, hm1, neg_one_smul] at hy; exact hy
      rw [← neg_inj, this]; module
    exact ⟨e + y, by rw [hf_eq]; module⟩

/-- **The separation, in the form the manuscript uses.** An automorphism acting trivially
modulo `2` does not carry `span {e}` to `span {f}` for vectors of distinct residue. -/
theorem span_ne_span_of_distinct_residue (g : (n → ℤ) ≃ₗ[ℤ] (n → ℤ))
    (hg : ActsTriviallyModTwo g) {e f : n → ℤ} (hf : f ≠ 0)
    (hres : ¬ ∃ y, e - f = 2 • y) :
    Submodule.span ℤ ({g e} : Set (n → ℤ)) ≠ Submodule.span ℤ ({f} : Set (n → ℤ)) := by
  intro hspan
  exact hres (sub_mem_two_of_span_eq g hg hf hspan)

/-- **The manuscript's counterexample.** Let `e` and `f` be the first two standard basis
vectors of `ℤⁿ` for `n` a type with two distinct elements — in the Coble lattice they are
the isotropic generators of the `U(2)` summand, which are basis vectors of `B` and hence
have distinct residues modulo `2B`. Then no automorphism of `ℤⁿ` acting trivially modulo
`2` carries the line of `e` to the line of `f`.

What this establishes is that the stable group has at least the two orbits of `e` and
`f`, hence that `F_Co` has at least two `0`-cusps if `0`-cusps are orbit data at all. It
is not a classification of the orbits of `Γ_Co`, and the count of those orbits remains
open in the manuscript. -/
theorem span_single_ne_span_single (i j : n) (hij : i ≠ j)
    (g : (n → ℤ) ≃ₗ[ℤ] (n → ℤ)) (hg : ActsTriviallyModTwo g) :
    Submodule.span ℤ ({g (Pi.single i 1)} : Set (n → ℤ)) ≠
      Submodule.span ℤ ({Pi.single j 1} : Set (n → ℤ)) := by
  refine span_ne_span_of_distinct_residue g hg ?_ ?_
  · -- `Pi.single j 1 ≠ 0`
    intro h
    have := congrFun h j
    simp at this
  · -- `single i 1 - single j 1` is not twice an integral vector
    rintro ⟨y, hy⟩
    have hcoord := congrFun hy i
    have hji := congrFun hy j
    have hi : ((Pi.single i (1 : ℤ) : n → ℤ) - (Pi.single j (1 : ℤ) : n → ℤ)) i = 1 := by
      simp [Pi.sub_apply, Pi.single_apply, hij, hij.symm]
    have hj : ((Pi.single i (1 : ℤ) : n → ℤ) - (Pi.single j (1 : ℤ) : n → ℤ)) j = -1 := by
      simp [Pi.sub_apply, Pi.single_apply, hij, hij.symm]
    rw [hi] at hcoord
    rw [hj] at hji
    simp only [Pi.smul_apply] at hcoord hji
    rw [two_nsmul] at hcoord
    omega

/-- The integral duality isomorphism, in matrix form: for a unimodular form, multiplication
by the Gram matrix is surjective, because the inverse is the adjugate over the determinant
and the determinant is a unit. This is the perfectness of the pairing that the book uses
when it writes `β_L^♯ : L → L*` as an isomorphism. -/
theorem mulVec_surjective (M : Matrix n n ℤ) (hM : IsUnit M.det) (y : n → ℤ) :
    ∃ x, M.mulVec x = y := by
  have hsq : M.det * M.det = 1 := by
    rcases Int.isUnit_iff.mp hM with h | h <;> simp [h]
  refine ⟨M.det • M.adjugate.mulVec y, ?_⟩
  rw [Matrix.mulVec_smul, Matrix.mulVec_mulVec, Matrix.mul_adjugate, Matrix.smul_mulVec,
    Matrix.one_mulVec, smul_smul, hsq, one_smul]

/-- The same statement for the pairing rather than the matrix: for a unimodular form, every
vector is the pairing with some vector, coordinatewise. -/
theorem form_mulVec_surjective (G : Matrix n n ℤ) (hG : IsUnit G.det) (y : n → ℤ) :
    ∃ x, Gᵀ.mulVec x = y :=
  mulVec_surjective Gᵀ (by rwa [Matrix.det_transpose]) y

/-- The sublattice `2B` inside `B = ℤⁿ`, that is the vectors all of whose coordinates are
even. Its quotient by `2B` is the group `B/2B` in which the discriminant classes live. -/
def twice (n : Type*) [Fintype n] : Submodule ℤ (n → ℤ) :=
  LinearMap.range ((2 : ℤ) • (LinearMap.id : (n → ℤ) →ₗ[ℤ] (n → ℤ)))

theorem mem_twice_iff {x : n → ℤ} : x ∈ twice n ↔ ∃ y : n → ℤ, x = 2 • y := by
  constructor
  · rintro ⟨y, hy⟩
    exact ⟨y, hy.symm⟩
  · rintro ⟨y, rfl⟩
    exact ⟨y, rfl⟩

/-- **The bridge.** Trivial action on the quotient `B/2B` is the congruence
`g x ≡ x mod 2` that the separation lemma needs.

The identification with the discriminant group is where unimodularity is required, and it
is not a general fact: for `T = B(2)` one has `T* = {y : β_T(y, B) ⊆ ℤ}`, and `β_T = 2β_B`,
so `T*` consists of the vectors on which `β_B` is half-integral; that this is `½B` is the
perfectness of `β_B`, which is `mulVec_surjective` and holds exactly when `det G` is a
unit. For a form that is not unimodular the discriminant group is larger and its classes
are not the classes mod `2B`, so the congruence below is not the discriminant condition.

What remains external to this file: that `T_Co = B(2)` with `B = U ⊕ U ⊕ I_{0,7}`, that `e`
and `f` are the isotropic generators of the `U(2)` summand in an explicit basis of `B`, and
that `Γ_Co = O⁺(T)*` acts trivially on `A_T`. The first two are the lattice identification
of `prop:tco-split-maximal`, the third is the definition of the stable subgroup. -/
theorem actsTriviallyModTwo_iff_quotient (g : (n → ℤ) ≃ₗ[ℤ] (n → ℤ)) :
    ActsTriviallyModTwo g ↔ ∀ x, Submodule.Quotient.mk (p := twice n) (g x) =
      Submodule.Quotient.mk (p := twice n) x := by
  constructor
  · intro hg x
    refine (Submodule.Quotient.eq (p := twice n)).mpr ?_
    obtain ⟨y, hy⟩ := hg x
    exact mem_twice_iff.mpr ⟨y, by rw [hy]; module⟩
  · intro h x
    have hx := (Submodule.Quotient.eq (p := twice n)).mp (h x)
    obtain ⟨y, hy⟩ := mem_twice_iff.mp hx
    exact ⟨y, by rw [← hy]; module⟩

/-- **The manuscript's counterexample, through the bridge.** Let `B = ℤⁿ` be integral
unimodular, so that `A_{B(2)} ≅ B/2B`, and let `g` be an integral automorphism acting
trivially on that quotient — the discriminant kernel of `B(2)`, into which the stable
orthogonal group and the book's `Γ_Co = O⁺(T)*` fall. Then `g` does not carry the line of
the basis vector `eᵢ` to the line of `eⱼ` for `i ≠ j`.

This is the separation the cusp chapter needs and no more: two orbits, hence two `0`-cusps,
not a classification of the orbits of `Γ_Co`. -/
theorem span_single_ne_span_single_of_quotient_trivial (i j : n) (hij : i ≠ j)
    (g : (n → ℤ) ≃ₗ[ℤ] (n → ℤ))
    (h : ∀ x, Submodule.Quotient.mk (p := twice n) (g x) =
      Submodule.Quotient.mk (p := twice n) x) :
    Submodule.span ℤ ({g (Pi.single i 1)} : Set (n → ℤ)) ≠
      Submodule.span ℤ ({Pi.single j 1} : Set (n → ℤ)) :=
  span_single_ne_span_single i j hij g ((actsTriviallyModTwo_iff_quotient g).mpr h)

end LatticeResearch

#print axioms LatticeResearch.span_single_ne_span_single_of_quotient_trivial
#print axioms LatticeResearch.actsTriviallyModTwo_iff_quotient
#print axioms LatticeResearch.form_mulVec_surjective
#print axioms LatticeResearch.mulVec_surjective
#print axioms LatticeResearch.span_single_ne_span_single
#print axioms LatticeResearch.span_ne_span_of_distinct_residue
#print axioms LatticeResearch.sub_mem_two_of_span_eq
#print axioms LatticeResearch.forall_dvd_form_iff
#print axioms LatticeResearch.divis_eq_one_iff_forall_not_dvd
#print axioms LatticeResearch.divis_two_smul_eq_two_iff_primitive
#print axioms LatticeResearch.primitive_iff_isPrimitive
#print axioms LatticeResearch.divis_eq_vecGcd
#print axioms LatticeResearch.divis_two_smul_eq_two_iff_isPrimitive
#print axioms LatticeResearch.isPrimitive_iff_vecGcd_eq_one
#print axioms LatticeResearch.divis_smul
#print axioms LatticeResearch.divis_G2_two
#print axioms LatticeResearch.not_dvd_two_divis_three
