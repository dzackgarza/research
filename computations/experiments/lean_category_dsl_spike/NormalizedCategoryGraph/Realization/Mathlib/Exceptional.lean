/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Algebra.Category.Semigrp.Basic
import Mathlib.CategoryTheory.Category.Cat
import Mathlib.CategoryTheory.ConcreteCategory.Basic
import Mathlib.CategoryTheory.Limits.Shapes.Pullback.Categorical.Basic
import Mathlib.CategoryTheory.ObjectProperty.FullSubcategory
import Mathlib.CategoryTheory.Types.Basic
import NormalizedCategoryGraph.Realization.Mathlib.Foundation

/-!
# Exceptional hosts

* `MagmasWithTwoOperations` — categorical pullback
  `MagmaCat ×_{Type} MagmaCat` (two magma structures on one underlying set up to
  the structural isomorphism). Not the cartesian product of two magma categories.
* `distributive` — full subcategory of that pullback where the transported
  operations satisfy left and right distributivity.
* `Crystals` — combinatorial crystals as types with Kashiwara operators.
-/

namespace NormalizedCategoryGraph.Realization.Mathlib

open CategoryTheory CategoryTheory.Limits
open NormalizedCategoryGraph

universe u

set_option linter.checkUnivs false

/-- Forgetful functors used for the two-operation pullback. -/
noncomputable abbrev magmaForget : MagmaCat.{u} ⥤ Type u := forget MagmaCat.{u}

/-- Two-operation host: Magmas ×_Sets Magmas (categorical pullback). -/
noncomputable def MagmasWithTwoOperations : ObjCat.{u + 1, u} :=
  Cat.of (CategoricalPullback magmaForget magmaForget)

/-- Multiplicative port (first projection). -/
noncomputable def multiplicativePort : MagmasWithTwoOperations ⟶ Magmas :=
  (CategoricalPullback.π₁ magmaForget magmaForget).toCatHom

/-- Additive port (second projection). -/
noncomputable def additivePort : MagmasWithTwoOperations ⟶ Magmas :=
  (CategoricalPullback.π₂ magmaForget magmaForget).toCatHom

/-- Transport the second magma operation onto the first factor's carrier. -/
noncomputable def addOnFst (x : CategoricalPullback magmaForget magmaForget) :
    x.fst → x.fst → x.fst := fun a b =>
  x.iso.inv (x.iso.hom a * x.iso.hom b)

/-- Left and right distributivity of `*` over the transported `+`. -/
def IsDistributive (x : CategoricalPullback magmaForget magmaForget) : Prop :=
  (∀ a b c : x.fst,
      a * addOnFst x b c = addOnFst x (a * b) (a * c)) ∧
    (∀ a b c : x.fst,
      addOnFst x b c * a = addOnFst x (b * a) (c * a))

/-- Distributive two-operation objects as a full subcategory of the pullback. -/
abbrev DistributiveTwoOpCat : Type (u + 1) :=
  ObjectProperty.FullSubcategory
    (C := CategoricalPullback magmaForget magmaForget) IsDistributive

/-- Distributivity classifier on `MagmasWithTwoOperations`. -/
noncomputable def distributive : Classifier MagmasWithTwoOperations where
  total := Cat.of DistributiveTwoOpCat.{u}
  forget :=
    (ObjectProperty.ι
        (C := CategoricalPullback magmaForget magmaForget) IsDistributive).toCatHom

/-- Combinatorial crystal: underlying set with Kashiwara operators. -/
structure Crystal where
  carrier : Type u
  e : ℕ → carrier → Option carrier
  f : ℕ → carrier → Option carrier

namespace Crystal

/-- Morphisms are functions commuting with `e` and `f`. -/
@[ext]
structure Hom (X Y : Crystal.{u}) where
  toFun : X.carrier → Y.carrier
  map_e : ∀ i x, (X.e i x).map toFun = Y.e i (toFun x)
  map_f : ∀ i x, (X.f i x).map toFun = Y.f i (toFun x)

instance : Category Crystal.{u} where
  Hom := Hom
  id X :=
    { toFun := id
      map_e := by
        intro i x
        simp [Option.map_id]
      map_f := by
        intro i x
        simp [Option.map_id] }
  comp {X Y Z} f g :=
    { toFun := g.toFun ∘ f.toFun
      map_e := by
        intro i x
        calc
          Option.map (g.toFun ∘ f.toFun) (X.e i x)
              = Option.map g.toFun (Option.map f.toFun (X.e i x)) :=
                (Option.map_map g.toFun f.toFun (X.e i x)).symm
          _ = Option.map g.toFun (Y.e i (f.toFun x)) := by rw [f.map_e]
          _ = Z.e i (g.toFun (f.toFun x)) := g.map_e i (f.toFun x)
      map_f := by
        intro i x
        calc
          Option.map (g.toFun ∘ f.toFun) (X.f i x)
              = Option.map g.toFun (Option.map f.toFun (X.f i x)) :=
                (Option.map_map g.toFun f.toFun (X.f i x)).symm
          _ = Option.map g.toFun (Y.f i (f.toFun x)) := by rw [f.map_f]
          _ = Z.f i (g.toFun (f.toFun x)) := g.map_f i (f.toFun x) }

/-- Forgetful Crystal → Type. -/
def forgetFunctor : Crystal.{u} ⥤ Type u where
  obj X := X.carrier
  map {X Y} f := TypeCat.ofHom f.toFun

end Crystal

/-- Crystals category. -/
def Crystals : ObjCat.{u + 1, u} := Cat.of Crystal.{u}

/-- Crystals → Sets. -/
noncomputable def crystalsToSets : Crystals ⟶ Sets :=
  Crystal.forgetFunctor.toCatHom

/-- Exceptional atoms. -/
noncomputable def exceptionalAtoms : ExceptionalAtoms foundationAtoms where
  MagmasWithTwoOperations := MagmasWithTwoOperations
  additivePort := additivePort
  multiplicativePort := multiplicativePort
  distributive := distributive
  Crystals := Crystals
  crystalsToSets := crystalsToSets

end NormalizedCategoryGraph.Realization.Mathlib
