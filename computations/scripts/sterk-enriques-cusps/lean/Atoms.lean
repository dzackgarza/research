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

end Sterk
