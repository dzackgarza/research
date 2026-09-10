/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Atoms of the Sterk boundary-complex graph: the definitions its leaves rest on
that exist in no Lean code anywhere -- not in Mathlib at db584cd6d4, not in the
277 repositories the lean-categories registry links, not in the 734-package
Reservoir clone, and not in the live Reservoir index.  See DAG.md, "The leaves,
clause by clause".

Each declaration here closes one clause of one leaf.  The clause it closes is
named above it.
-/
module

public import Mathlib.LinearAlgebra.BilinearForm.Basic
public import Mathlib.Algebra.Module.Equiv.Basic
public import Mathlib.Data.Matrix.Block
public import Mathlib.Logic.Equiv.Basic
public import Mathlib.Topology.Instances.AddCircle.Defs
public import Mathlib.Topology.Covering.Basic
public import Mathlib.LinearAlgebra.QuadraticForm.Basic
public import Mathlib.LinearAlgebra.QuadraticForm.Prod
public import Mathlib.LinearAlgebra.QuadraticForm.IsometryEquiv
public import Mathlib.LinearAlgebra.Pi
public import Mathlib.Logic.Equiv.Fin.Basic
public import Mathlib.NumberTheory.Padics.PadicIntegers
public import Mathlib.AlgebraicGeometry.Scheme
public import Mathlib.Order.KrullDimension
public import Mathlib.Data.Finsupp.Defs
public import Mathlib.Algebra.Order.BigOperators.Ring.Finset
public import Mathlib.Analysis.Convex.Topology
public import Mathlib.Analysis.SpecialFunctions.Complex.CircleAddChar
public import Mathlib.Algebra.BigOperators.Ring.Finset

@[expose] public section

namespace Sterk

universe u v w

section OrthogonalGroup

variable {R : Type u} {M : Type v} [CommRing R] [AddCommGroup M] [Module R M]

/-- **F1.13.**  The orthogonal group of a bilinear form: the module automorphisms
that preserve it, as a subgroup of the automorphism group of `M`.

Mathlib has `LinearMap.BilinForm.IsometryEquiv`, a structure carrying `refl`,
`symm` and `trans`, and `Matrix.orthogonalGroup`, which is `unitaryGroup` and so
the orthogonal group of the *identity* Gram matrix.  Neither is `O(L)` for a
given form, and no `Group` instance sits over the isometries, which is why
F2.1's `τ : O(L) → O(G_L)` could not be stated. -/
def orthogonalGroup (B : LinearMap.BilinForm R M) : Subgroup (M ≃ₗ[R] M) where
  carrier := {f | ∀ x y, B (f x) (f y) = B x y}
  mul_mem' {f g} hf hg := fun x y => by
    show B (f (g x)) (f (g y)) = B x y
    rw [hf (g x) (g y), hg x y]
  one_mem' := fun _ _ => rfl
  inv_mem' {f} hf := fun x y => by
    have h := hf (f.symm x) (f.symm y)
    simp only [LinearEquiv.apply_symm_apply] at h
    exact h.symm

@[simp]
theorem mem_orthogonalGroup_iff {B : LinearMap.BilinForm R M} {f : M ≃ₗ[R] M} :
    f ∈ orthogonalGroup B ↔ ∀ x y, B (f x) (f y) = B x y := Iff.rfl

end OrthogonalGroup

section Indecomposable

variable {n : Type u} {α : Type v}

/-- **V1.**  A matrix is *decomposable* when some re-indexing of its index set
splits it into a block-diagonal matrix with both blocks nonempty; it is
*indecomposable* otherwise.  Vinberg's `C⁺`-matrices are the indecomposable
positive ones.

`Matrix.blockDiagonal` builds block matrices; nothing in Mathlib says a matrix
is not one after a permutation. -/
def Matrix.IsDecomposable [Zero α] (A : Matrix n n α) : Prop :=
  ∃ (ι κ : Type u) (_ : Nonempty ι) (_ : Nonempty κ) (e : n ≃ ι ⊕ κ),
    ∀ i j, (A (e.symm (Sum.inl i)) (e.symm (Sum.inr j)) = 0) ∧
           (A (e.symm (Sum.inr j)) (e.symm (Sum.inl i)) = 0)

/-- **V1.**  Indecomposability, the condition on a `C⁺`-matrix. -/
def Matrix.IsIndecomposable [Zero α] (A : Matrix n n α) : Prop :=
  ¬ Matrix.IsDecomposable A

end Indecomposable

section Doubling

/-- **F1.15.**  The doubling map from `AddCircle (1 : ℚ)` to `AddCircle (2 : ℚ)`,
that is from `ℚ/ℤ` to `ℚ/2ℤ`: multiplication by two on the quotients.

F1.9's second axiom relates a `ℚ/2ℤ`-valued quadratic form to a `ℚ/ℤ`-valued
bilinear one through this map, and without it the axiom cannot be stated.
Mathlib has both value groups as `AddCircle` and no map between them. -/
noncomputable def doubling : AddCircle (1 : ℚ) →+ AddCircle (2 : ℚ) :=
  QuotientAddGroup.map _ _ (AddMonoidHom.mulLeft (2 : ℚ)) <| by
    rw [AddSubgroup.zmultiples_le]
    refine AddSubgroup.mem_comap.mpr ?_
    show (2 : ℚ) * 1 ∈ AddSubgroup.zmultiples (2 : ℚ)
    simp

end Doubling

section Deck

variable {E X : Type u} [TopologicalSpace E] [TopologicalSpace X]

/-- **E14.**  A deck transformation of a covering `f : E → X`: a homeomorphism of
the total space commuting with the projection.

`rg -i deck` over `Mathlib/Topology/Covering/` returns nothing. -/
structure DeckTransformation (f : E → X) where
  /-- The underlying homeomorphism of the total space. -/
  toHomeomorph : E ≃ₜ E
  /-- It lies over the identity of the base. -/
  over_base : ∀ e, f (toHomeomorph e) = f e

namespace DeckTransformation

variable {f : E → X}

instance : CoeFun (DeckTransformation f) fun _ => E → E := ⟨fun d => d.toHomeomorph⟩

/-- The identity deck transformation. -/
protected def id : DeckTransformation f where
  toHomeomorph := Homeomorph.refl E
  over_base _ := rfl

/-- **E14.**  A deck transformation is an *involution* when it squares to the
identity.  The covering involution of a two-sheeted covering is what E2's `K3`
double cover carries. -/
def IsInvolution (d : DeckTransformation f) : Prop :=
  ∀ e, d.toHomeomorph (d.toHomeomorph e) = e

omit [TopologicalSpace X] in
/-- An involutive deck transformation is its own inverse. -/
theorem IsInvolution.symm_apply {d : DeckTransformation f} (h : d.IsInvolution) (e : E) :
    d.toHomeomorph.symm e = d.toHomeomorph e := by
  have h2 : d.toHomeomorph (d.toHomeomorph e) = e := h e
  calc d.toHomeomorph.symm e
      = d.toHomeomorph.symm (d.toHomeomorph (d.toHomeomorph e)) := by rw [h2]
    _ = d.toHomeomorph e := d.toHomeomorph.symm_apply_apply _

end DeckTransformation

end Deck

section QuadraticIsometries

variable {R : Type u} {M : Type v} {N : Type w}
variable [CommRing R] [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]

/-- **F2.14.**  The orthogonal group of a quadratic map: the automorphisms of `M`
preserving `Q`, as a subgroup of the automorphism group.

At `Q = q_L` on the discriminant group this is `O(G_L)`, the codomain of F2.1's
`τ`.  `QuadraticMap.IsometryEquiv` carries `refl`, `symm` and `trans` and no
`Group` instance. -/
def quadraticOrthogonalGroup (Q : QuadraticMap R M N) : Subgroup (M ≃ₗ[R] M) where
  carrier := {f | ∀ x, Q (f x) = Q x}
  mul_mem' {f g} hf hg := fun x => by
    show Q (f (g x)) = Q x
    rw [hf (g x), hg x]
  one_mem' := fun _ => rfl
  inv_mem' {f} hf := fun x => by
    have h := hf (f.symm x)
    simpa using h.symm

@[simp]
theorem mem_quadraticOrthogonalGroup_iff {Q : QuadraticMap R M N} {f : M ≃ₗ[R] M} :
    f ∈ quadraticOrthogonalGroup Q ↔ ∀ x, Q (f x) = Q x := Iff.rfl

end QuadraticIsometries

section Divisor

variable {R : Type u} {M : Type v} [CommRing R] [AddCommGroup M] [Module R M]

/-- **F1.14.**  The *divisor ideal* of a vector: the image of `fun y => B v y`,
as an ideal of `R`.  Over `ℤ` its positive generator is Scattone's `div(v)`, the
`d` with `(v, L) = dℤ`.

Mathlib's `BilinForm.dualSubmodule` gives `L*` and says nothing about `div`. -/
def divisorIdeal (B : LinearMap.BilinForm R M) (v : M) : Ideal R :=
  LinearMap.range (B v)

@[simp]
theorem mem_divisorIdeal_iff {B : LinearMap.BilinForm R M} {v : M} {r : R} :
    r ∈ divisorIdeal B v ↔ ∃ y, B v y = r := Iff.rfl

/-- **F1.14.**  A vector has divisor one exactly when its divisor ideal is all of
`R`; for `L` over `ℤ` this is `(v, L) = ℤ`, the hypothesis of Sterk 3.2.1. -/
def HasDivisorOne (B : LinearMap.BilinForm R M) (v : M) : Prop :=
  divisorIdeal B v = ⊤

end Divisor

section PadicSemigroup

variable (p : ℕ) [Fact p.Prime]

/-- **Pa1.**  A `p`-adic quadratic form, on a *chosen* free module of finite
rank.

Nikulin's `qu(ℤ_p)` ranges over forms on all finitely generated `ℤ_p`-modules,
which is not a set.  Fixing the underlying module to `Fin n → ℤ_[p]` makes it
one, and that choice is the content of this definition. -/
structure PadicForm where
  /-- The rank of the underlying free module. -/
  rank : ℕ
  /-- The form itself. -/
  form : QuadraticMap ℤ_[p] (Fin rank → ℤ_[p]) ℤ_[p]

namespace PadicForm

/-- Isometry of `p`-adic forms of possibly different ranks. -/
def Isometric (A B : PadicForm p) : Prop :=
  Nonempty (A.form.IsometryEquiv B.form)

theorem Isometric.refl (A : PadicForm p) : Isometric p A A :=
  ⟨QuadraticMap.IsometryEquiv.refl A.form⟩

theorem Isometric.symm {A B : PadicForm p} (h : Isometric p A B) : Isometric p B A :=
  ⟨h.some.symm⟩

theorem Isometric.trans {A B C : PadicForm p} (h : Isometric p A B) (h' : Isometric p B C) :
    Isometric p A C :=
  ⟨h.some.trans h'.some⟩

/-- Isometry is an equivalence relation on `p`-adic forms. -/
def isometricSetoid : Setoid (PadicForm p) where
  r := Isometric p
  iseqv := ⟨Isometric.refl p, Isometric.symm p, Isometric.trans p⟩

/-- The orthogonal sum of two `p`-adic forms: `QuadraticMap.prod` carried onto a
module of the summed rank along `finSumFinEquiv`. -/
noncomputable def orthogonalSum (A B : PadicForm p) : PadicForm p where
  rank := A.rank + B.rank
  form := (A.form.prod B.form).comp <|
    ((LinearEquiv.funCongrLeft ℤ_[p] ℤ_[p] (finSumFinEquiv (m := A.rank) (n := B.rank))).trans
      (LinearEquiv.sumArrowLequivProdArrow (Fin A.rank) (Fin B.rank) ℤ_[p] ℤ_[p])).toLinearMap

end PadicForm

/-- **Pa1.**  `qu(ℤ_p)`: the isometry classes of `p`-adic quadratic forms.  The
semigroup operation is `PadicForm.orthogonalSum` on representatives. -/
def PadicFormClasses : Type _ := Quotient (PadicForm.isometricSetoid p)

end PadicSemigroup

section WeilDivisor

open AlgebraicGeometry

/-- **E15.**  The codimension-one points of a scheme.

Mathlib's `specializationPreorder` has `x ≤ y ↔ y ⤳ x`, so a generic point is a
greatest element and codimension is measured **upwards**: the codimension of `x`
is the length of the longest chain of specializations from `x` towards the
generic point, which is `Order.coheight` in that preorder and not
`Order.height`. -/
def codimOnePoints (X : Scheme) : Set X :=
  {x | @Order.coheight X (specializationPreorder X) x = 1}

/-- **E15.**  The Weil divisors of a scheme: the free abelian group on its
codimension-one points.

`rg -i 'WeilDivisor|CartierDivisor|Chow|algebraicCycle'` finds nothing in the
pinned Mathlib, in the 277 repositories the registry links, or in the
734-package Reservoir clone. -/
def WeilDivisor (X : Scheme) : Type _ := (codimOnePoints X) →₀ ℤ

noncomputable instance (X : Scheme) : AddCommGroup (WeilDivisor X) :=
  inferInstanceAs (AddCommGroup ((codimOnePoints X) →₀ ℤ))

/-- The divisor of a single codimension-one point, with multiplicity one. -/
noncomputable def WeilDivisor.single {X : Scheme} (x : codimOnePoints X) : WeilDivisor X :=
  Finsupp.single x 1

end WeilDivisor

section LorentzCone

/-- **Lo1, Lo10.**  The standard Lorentzian form on `Fin (n+1) → ℝ`: minus the
square of the zeroth coordinate plus the squares of the rest.  This is Vinberg's
`E^{n,1}`, the form of negative inertial index one his §3 works in. -/
def lorentz {n : ℕ} (x : Fin (n + 1) → ℝ) : ℝ :=
  -(x 0) ^ 2 + ∑ i ∈ Finset.univ.erase 0, (x i) ^ 2

/-- **Lo1.**  The negative cone `V = {x : (x,x) < 0}`. -/
def negativeCone (n : ℕ) : Set (Fin (n + 1) → ℝ) := {x | lorentz x < 0}

/-- The upper sheet `V₊`. -/
def negativeCone.upper (n : ℕ) : Set (Fin (n + 1) → ℝ) :=
  {x | lorentz x < 0 ∧ 0 < x 0}

/-- The lower sheet `V₋`. -/
def negativeCone.lower (n : ℕ) : Set (Fin (n + 1) → ℝ) :=
  {x | lorentz x < 0 ∧ x 0 < 0}

theorem lorentz_continuous {n : ℕ} : Continuous (lorentz (n := n)) := by
  unfold lorentz
  fun_prop

/-- On the negative cone the zeroth coordinate never vanishes: if it did, the
form would be a sum of squares there. -/
theorem ne_zero_of_mem_negativeCone {n : ℕ} {x : Fin (n + 1) → ℝ}
    (hx : x ∈ negativeCone n) : x 0 ≠ 0 := by
  intro h0
  have hsum : 0 ≤ ∑ i ∈ Finset.univ.erase (0 : Fin (n + 1)), (x i) ^ 2 :=
    Finset.sum_nonneg fun i _ => sq_nonneg _
  have hval : lorentz x = ∑ i ∈ Finset.univ.erase (0 : Fin (n + 1)), (x i) ^ 2 := by
    unfold lorentz; rw [h0]; ring
  have hlt : lorentz x < 0 := hx
  rw [hval] at hlt
  exact absurd hlt (not_lt.mpr hsum)

/-- **Lo10, the separation half.**  The two sheets are disjoint, open, and cover
the cone, so the cone is disconnected by the sign of the zeroth coordinate.

The remaining half of Lo10 — that each sheet is *connected*, so that there are
exactly two components — is the convexity of a Lorentzian half-cone and is not
proved here. -/
theorem negativeCone_eq_union (n : ℕ) :
    negativeCone n = negativeCone.upper n ∪ negativeCone.lower n := by
  ext x
  constructor
  · intro hx
    rcases lt_or_gt_of_ne (ne_zero_of_mem_negativeCone hx) with h | h
    · exact Or.inr ⟨hx, h⟩
    · exact Or.inl ⟨hx, h⟩
  · rintro (⟨hx, _⟩ | ⟨hx, _⟩) <;> exact hx

theorem negativeCone.upper_disjoint_lower (n : ℕ) :
    Disjoint (negativeCone.upper n) (negativeCone.lower n) := by
  rw [Set.disjoint_left]
  rintro x ⟨-, hpos⟩ ⟨-, hneg⟩
  exact absurd hpos (not_lt.mpr hneg.le)

theorem negativeCone.isOpen_upper (n : ℕ) : IsOpen (negativeCone.upper n) := by
  have h1 : IsOpen {x : Fin (n + 1) → ℝ | lorentz x < 0} :=
    isOpen_lt lorentz_continuous continuous_const
  have h2 : IsOpen {x : Fin (n + 1) → ℝ | 0 < x 0} :=
    isOpen_lt continuous_const ((continuous_apply 0))
  exact h1.inter h2

theorem negativeCone.isOpen_lower (n : ℕ) : IsOpen (negativeCone.lower n) := by
  have h1 : IsOpen {x : Fin (n + 1) → ℝ | lorentz x < 0} :=
    isOpen_lt lorentz_continuous continuous_const
  have h2 : IsOpen {x : Fin (n + 1) → ℝ | x 0 < 0} :=
    isOpen_lt ((continuous_apply 0)) continuous_const
  exact h1.inter h2

end LorentzCone

section LorentzConvexity

variable {n : ℕ}

/-- The Lorentzian pairing whose diagonal is `lorentz`. -/
def lorentzPair (x y : Fin (n + 1) → ℝ) : ℝ :=
  -(x 0 * y 0) + ∑ i ∈ Finset.univ.erase 0, x i * y i

theorem lorentz_eq_lorentzPair_self (x : Fin (n + 1) → ℝ) : lorentz x = lorentzPair x x := by
  unfold lorentz lorentzPair
  simp only [sq]

/-- The form expands on a linear combination through the pairing. -/
theorem lorentz_smul_add (a b : ℝ) (x y : Fin (n + 1) → ℝ) :
    lorentz (a • x + b • y)
      = a ^ 2 * lorentz x + b ^ 2 * lorentz y + 2 * a * b * lorentzPair x y := by
  unfold lorentz lorentzPair
  have hpt : ∀ i : Fin (n + 1),
      ((a • x + b • y) i) ^ 2
        = a ^ 2 * (x i) ^ 2 + b ^ 2 * (y i) ^ 2 + 2 * a * b * (x i * y i) := by
    intro i; simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]; ring
  rw [Finset.sum_congr rfl (fun i _ => hpt i)]
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum,
    ← Finset.mul_sum]
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  ring

/-- The spatial part of a vector on the cone is shorter than its time part. -/
theorem sum_sq_lt_sq_of_mem_negativeCone {x : Fin (n + 1) → ℝ} (hx : x ∈ negativeCone n) :
    ∑ i ∈ Finset.univ.erase (0 : Fin (n + 1)), (x i) ^ 2 < (x 0) ^ 2 := by
  have h : lorentz x < 0 := hx
  unfold lorentz at h
  linarith

/-- **Lo10.**  The pairing of two future-directed vectors of the cone is
negative: the reverse Cauchy–Schwarz inequality for a form of index one. -/
theorem lorentzPair_neg_of_mem_upper {x y : Fin (n + 1) → ℝ}
    (hx : x ∈ negativeCone.upper n) (hy : y ∈ negativeCone.upper n) :
    lorentzPair x y < 0 := by
  obtain ⟨hxc, hx0⟩ := hx
  obtain ⟨hyc, hy0⟩ := hy
  set S := Finset.univ.erase (0 : Fin (n + 1)) with hS
  have hxs : ∑ i ∈ S, (x i) ^ 2 < (x 0) ^ 2 := sum_sq_lt_sq_of_mem_negativeCone hxc
  have hys : ∑ i ∈ S, (y i) ^ 2 < (y 0) ^ 2 := sum_sq_lt_sq_of_mem_negativeCone hyc
  have hxnn : (0:ℝ) ≤ ∑ i ∈ S, (x i) ^ 2 := Finset.sum_nonneg fun i _ => sq_nonneg _
  have hynn : (0:ℝ) ≤ ∑ i ∈ S, (y i) ^ 2 := Finset.sum_nonneg fun i _ => sq_nonneg _
  have hcs : (∑ i ∈ S, x i * y i) ^ 2 ≤ (∑ i ∈ S, (x i) ^ 2) * ∑ i ∈ S, (y i) ^ 2 :=
    Finset.sum_mul_sq_le_sq_mul_sq S x y
  have hprod : (∑ i ∈ S, (x i) ^ 2) * (∑ i ∈ S, (y i) ^ 2) < (x 0 * y 0) ^ 2 := by
    have h1 : (∑ i ∈ S, (x i) ^ 2) * (∑ i ∈ S, (y i) ^ 2) ≤ (x 0) ^ 2 * ∑ i ∈ S, (y i) ^ 2 :=
      mul_le_mul_of_nonneg_right hxs.le hynn
    have h2 : (x 0) ^ 2 * (∑ i ∈ S, (y i) ^ 2) < (x 0) ^ 2 * (y 0) ^ 2 := by
      have hx0sq : (0:ℝ) < (x 0) ^ 2 := by positivity
      exact mul_lt_mul_of_pos_left hys hx0sq
    calc (∑ i ∈ S, (x i) ^ 2) * (∑ i ∈ S, (y i) ^ 2) ≤ (x 0) ^ 2 * ∑ i ∈ S, (y i) ^ 2 := h1
      _ < (x 0) ^ 2 * (y 0) ^ 2 := h2
      _ = (x 0 * y 0) ^ 2 := by ring
  have hsq : (∑ i ∈ S, x i * y i) ^ 2 < (x 0 * y 0) ^ 2 := lt_of_le_of_lt hcs hprod
  have hpos : (0:ℝ) < x 0 * y 0 := mul_pos hx0 hy0
  have habs : ∑ i ∈ S, x i * y i < x 0 * y 0 := by
    nlinarith [hsq, hpos]
  unfold lorentzPair
  linarith

/-- **Lo10.**  The upper sheet is convex, hence connected. -/
theorem convex_upper (n : ℕ) : Convex ℝ (negativeCone.upper n) := by
  intro x hx y hy a b ha hb hab
  have hpair : lorentzPair x y < 0 := lorentzPair_neg_of_mem_upper hx hy
  obtain ⟨hxc, hx0⟩ := hx
  obtain ⟨hyc, hy0⟩ := hy
  have hxl : lorentz x < 0 := hxc
  have hyl : lorentz y < 0 := hyc
  constructor
  · show lorentz (a • x + b • y) < 0
    rw [lorentz_smul_add]
    rcases eq_or_lt_of_le ha with rfl | ha'
    · have hb1 : b = 1 := by linarith
      subst hb1; norm_num; exact hyl
    · rcases eq_or_lt_of_le hb with rfl | hb'
      · have ha1 : a = 1 := by linarith
        subst ha1; norm_num; exact hxl
      · have t1 : a ^ 2 * lorentz x < 0 := mul_neg_of_pos_of_neg (by positivity) hxl
        have t2 : b ^ 2 * lorentz y < 0 := mul_neg_of_pos_of_neg (by positivity) hyl
        have t3 : 2 * a * b * lorentzPair x y < 0 :=
          mul_neg_of_pos_of_neg (by positivity) hpair
        linarith
  · show 0 < (a • x + b • y) 0
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    rcases eq_or_lt_of_le ha with rfl | ha'
    · have hb1 : b = 1 := by linarith
      subst hb1; simpa using hy0
    · have u1 : 0 < a * x 0 := mul_pos ha' hx0
      have u2 : 0 ≤ b * y 0 := mul_nonneg hb hy0.le
      linarith

/-- The form is invariant under negation. -/
theorem lorentz_neg (z : Fin (n + 1) → ℝ) : lorentz (-z) = lorentz z := by
  unfold lorentz
  have h0 : ((-z) 0) ^ 2 = (z 0) ^ 2 := by
    simp only [Pi.neg_apply]; ring
  have hi : ∀ i : Fin (n + 1), ((-z) i) ^ 2 = (z i) ^ 2 := by
    intro i; simp only [Pi.neg_apply]; ring
  rw [h0, Finset.sum_congr rfl (fun i _ => hi i)]

/-- **Lo10.**  The lower sheet is convex too, being the image of the upper under
negation. -/
theorem convex_lower (n : ℕ) : Convex ℝ (negativeCone.lower n) := by
  intro x hx y hy a b ha hb hab
  have hx' : -x ∈ negativeCone.upper n := by
    obtain ⟨hxc, hx0⟩ := hx
    refine ⟨?_, ?_⟩
    · show lorentz (-x) < 0
      rw [lorentz_neg]; exact hxc
    · simpa using hx0
  have hy' : -y ∈ negativeCone.upper n := by
    obtain ⟨hyc, hy0⟩ := hy
    refine ⟨?_, ?_⟩
    · show lorentz (-y) < 0
      rw [lorentz_neg]; exact hyc
    · simpa using hy0
  have hcomb := convex_upper n hx' hy' ha hb hab
  obtain ⟨hc, h0⟩ := hcomb
  refine ⟨?_, ?_⟩
  · show lorentz (a • x + b • y) < 0
    have heq : a • (-x) + b • (-y) = -(a • x + b • y) := by
      ext i; simp only [Pi.add_apply, Pi.smul_apply, Pi.neg_apply, smul_eq_mul]; ring
    rw [heq, lorentz_neg] at hc
    exact hc
  · show (a • x + b • y) 0 < 0
    have heq : (a • (-x) + b • (-y)) 0 = -((a • x + b • y) 0) := by
      simp only [Pi.add_apply, Pi.smul_apply, Pi.neg_apply, smul_eq_mul]; ring
    rw [heq] at h0; linarith

/-- **Lo10, complete.**  The negative cone of the standard form of index one has
exactly two connected components: the two sheets, each convex hence connected,
disjoint, open, and covering the cone. -/
theorem negativeCone_two_components (n : ℕ) :
    IsPreconnected (negativeCone.upper n) ∧ IsPreconnected (negativeCone.lower n) ∧
      negativeCone n = negativeCone.upper n ∪ negativeCone.lower n ∧
      Disjoint (negativeCone.upper n) (negativeCone.lower n) ∧
      IsOpen (negativeCone.upper n) ∧ IsOpen (negativeCone.lower n) :=
  ⟨(convex_upper n).isPreconnected, (convex_lower n).isPreconnected,
    negativeCone_eq_union n, negativeCone.upper_disjoint_lower n,
    negativeCone.isOpen_upper n, negativeCone.isOpen_lower n⟩

end LorentzConvexity

section DiscriminantGaussSum

/-- **F1.16.**  The comparison `ℚ/2ℤ → ℝ/2ℤ`, induced by the inclusion of the
rationals.  A discriminant form takes values in `AddCircle (2 : ℚ)`, and the
additive character to the circle group that a Gauss sum needs is stated for
`AddCircle (T : ℝ)`, so this map is the bridge between them. -/
noncomputable def ratCircleToRealCircle : AddCircle (2 : ℚ) →+ AddCircle ((2 : ℚ) : ℝ) :=
  QuotientAddGroup.map _ _ (Rat.castHom ℝ).toAddMonoidHom <| by
    rw [AddSubgroup.zmultiples_le]
    refine AddSubgroup.mem_comap.mpr ?_
    show ((2 : ℚ) : ℝ) ∈ AddSubgroup.zmultiples ((2 : ℚ) : ℝ)
    exact AddSubgroup.mem_zmultiples _

/-- **F1.16.**  The Gauss sum of a `ℚ/2ℤ`-valued form on a finite abelian group:
`∑ a, e(q a)` for the additive character `e` of the circle.

This is the quantity Milgram's theorem evaluates, and the object F1.16 is stated
over.  Mathlib has `gaussSum` for a `MulChar`/`AddChar` pair on a finite ring; a
discriminant form is not that, and no Gauss sum of one exists anywhere. -/
noncomputable def discriminantGaussSum {A : Type u} [AddCommGroup A] [Fintype A]
    (q : A → AddCircle (2 : ℚ)) : ℂ :=
  ∑ a : A, (AddCircle.toCircle_addChar (ratCircleToRealCircle (q a)) : ℂ)

/-- The Gauss sum of the zero form counts the group: every term is the character
at zero, which is one. -/
theorem discriminantGaussSum_zero (A : Type u) [AddCommGroup A] [Fintype A] :
    discriminantGaussSum (fun _ : A => (0 : AddCircle (2 : ℚ))) = Fintype.card A := by
  unfold discriminantGaussSum
  simp

/-- **F1.16, the statement.**  Milgram's theorem: for an even lattice with
discriminant form `q` and signature `σ = n₊ - n₋`, the normalized Gauss sum of
`q` is the eighth root of unity `exp(2πi σ / 8)`.  Specialized to a unimodular
lattice, where the discriminant group is trivial and the sum is one, it gives
`σ ≡ 0 (mod 8)`, which is F1.4's last clause.

This is the *statement*, as a proposition about the data.  It is **not proved
here**: the proof needs the absolute value of the Gauss sum and a reduction to
the `p`-adic pieces, and it is the hardest single item in the Sterk graph. -/
def MilgramStatement {A : Type u} [AddCommGroup A] [Fintype A]
    (q : A → AddCircle (2 : ℚ)) (σ : ℤ) : Prop :=
  discriminantGaussSum q
    = (Real.sqrt (Fintype.card A) : ℂ) *
      Complex.exp (2 * Real.pi * Complex.I * (σ : ℂ) / 8)

end DiscriminantGaussSum

section MilgramSteps

variable {A : Type u} [AddCommGroup A] [Fintype A]

/-- One term of the Gauss sum: the circle character at a value of the form. -/
noncomputable def gaussTerm (v : AddCircle (2 : ℚ)) : ℂ :=
  (AddCircle.toCircle_addChar (ratCircleToRealCircle v) : ℂ)

theorem discriminantGaussSum_eq_sum_gaussTerm (q : A → AddCircle (2 : ℚ)) :
    discriminantGaussSum q = ∑ a : A, gaussTerm (q a) := rfl

/-- **F1.16, step one.**  Each term of the Gauss sum has modulus one: it is a
point of the circle group. -/
theorem norm_gaussTerm (v : AddCircle (2 : ℚ)) : ‖gaussTerm v‖ = 1 := by
  unfold gaussTerm
  exact Circle.norm_coe _

/-- **F1.16, step two.**  The Gauss sum times its conjugate expands over pairs.
This is the identity Milgram's proof starts from: the next step substitutes
`b = a + c` and uses the polar identity of F1.15 to separate the `c`-sum, which
`AddChar.sum_eq_ite` then evaluates. -/
theorem discriminantGaussSum_mul_conj (q : A → AddCircle (2 : ℚ)) :
    discriminantGaussSum q * (starRingEnd ℂ) (discriminantGaussSum q)
      = ∑ a : A, ∑ b : A, gaussTerm (q a) * (starRingEnd ℂ) (gaussTerm (q b)) := by
  rw [discriminantGaussSum_eq_sum_gaussTerm, map_sum, Finset.sum_mul_sum]

/-- **F1.16, step three.**  The character is additive, so a difference of values
of the form contributes a single term.  This is what turns the double sum of
step two into a sum over the difference. -/
theorem gaussTerm_add (v w : AddCircle (2 : ℚ)) :
    gaussTerm (v + w) = gaussTerm v * gaussTerm w := by
  unfold gaussTerm
  rw [map_add]
  rw [AddChar.map_add_eq_mul]
  push_cast
  ring

theorem gaussTerm_zero : gaussTerm (0 : AddCircle (2 : ℚ)) = 1 := by
  unfold gaussTerm
  rw [map_zero, AddChar.map_zero_eq_one]
  simp

/-- **F1.16, step four.**  Conjugation inverts a term, since the terms lie on the
circle: `conj (e v) = e (-v)`.  With step three this rewrites step two's double
sum as a sum over the difference `q a - q b`, which is where the polar identity
of F1.15 enters. -/
theorem conj_gaussTerm (v : AddCircle (2 : ℚ)) :
    (starRingEnd ℂ) (gaussTerm v) = gaussTerm (-v) := by
  have hns : Complex.normSq (gaussTerm v) = 1 := by
    have hn : ‖gaussTerm v‖ = 1 := norm_gaussTerm v
    rw [Complex.normSq_eq_norm_sq, hn]
    norm_num
  have h1 : gaussTerm v * (starRingEnd ℂ) (gaussTerm v) = 1 := by
    rw [Complex.mul_conj, hns]; norm_num
  have h2 : gaussTerm v * gaussTerm (-v) = 1 := by
    rw [← gaussTerm_add]; simp [gaussTerm_zero]
  have hne : gaussTerm v ≠ 0 := by
    intro h
    rw [h] at h1
    simp at h1
  exact mul_left_cancel₀ hne (h1.trans h2.symm)


/-- **F1.16, step five.**  A difference of values contributes one term. -/
theorem gaussTerm_sub (v w : AddCircle (2 : ℚ)) :
    gaussTerm (v - w) = gaussTerm v * (starRingEnd ℂ) (gaussTerm w) := by
  rw [sub_eq_add_neg, gaussTerm_add, conj_gaussTerm]

/-- **F1.16, step six.**  The inner sum is reindexed by `b = a + c`. -/
theorem sum_gaussTerm_reindex (q : A → AddCircle (2 : ℚ)) (a : A) :
    ∑ c : A, gaussTerm (q a - q (a + c)) = ∑ b : A, gaussTerm (q a - q b) :=
  Fintype.sum_equiv (Equiv.addLeft a) _ _ (fun _ => rfl)

/-- **F1.16, step seven.**  Steps two, five and six together: the squared modulus
of the Gauss sum is a double sum over a point and a *difference*.  This is the
form Milgram's proof factors. -/
theorem discriminantGaussSum_mul_conj_eq_sum_diff (q : A → AddCircle (2 : ℚ)) :
    discriminantGaussSum q * (starRingEnd ℂ) (discriminantGaussSum q)
      = ∑ a : A, ∑ c : A, gaussTerm (q a - q (a + c)) := by
  rw [discriminantGaussSum_mul_conj]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [sum_gaussTerm_reindex q a]
  exact Finset.sum_congr rfl fun b _ => (gaussTerm_sub (q a) (q b)).symm

/-- **F1.16, step eight.**  Under the polar identity — which is exactly what
F1.15's doubling map makes sayable — the `a`-sum factors: the term depending on
`c` alone comes out, and what is left is a character sum in `a`.

The polar identity is a hypothesis here rather than an assumption about `q`,
so this step is exactly as strong as its input. -/
theorem sum_gaussTerm_diff_factor (q : A → AddCircle (2 : ℚ))
    (pol : A → A → AddCircle (2 : ℚ))
    (hpol : ∀ x y, q (x + y) = q x + q y + pol x y) (c : A) :
    ∑ a : A, gaussTerm (q a - q (a + c))
      = gaussTerm (-q c) * ∑ a : A, gaussTerm (-(pol a c)) := by
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  have hval : q a - q (a + c) = -q c + -(pol a c) := by
    rw [hpol a c]; abel
  rw [hval, gaussTerm_add]


end MilgramSteps

end Sterk
