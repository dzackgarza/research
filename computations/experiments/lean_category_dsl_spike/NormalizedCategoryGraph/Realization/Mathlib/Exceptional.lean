/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Algebra.Category.Semigrp.Basic
import Mathlib.CategoryTheory.Category.Cat
import Mathlib.CategoryTheory.ConcreteCategory.Basic
import Mathlib.CategoryTheory.Products.Basic
import Mathlib.CategoryTheory.Types.Basic
import NormalizedCategoryGraph.Realization.Mathlib.Foundation

/-!
# Exceptional opaque hosts

* `MagmasWithTwoOperations` — product of two magma categories (two operations,
  no distributivity imposed), with multiplicative / additive ports the projections.
* `Crystals` — combinatorial crystals as types equipped with Kashiwara operators
  `eᵢ`, `fᵢ` (indexed by `ℕ`); morphisms commute with the operators.
-/

namespace NormalizedCategoryGraph.Realization.Mathlib

open CategoryTheory
open NormalizedCategoryGraph

universe u

set_option linter.checkUnivs false

/-- Two-operation host before distributivity: a pair of magmas. -/
def MagmasWithTwoOperations : ObjCat.{u + 1, u} :=
  Cat.of (MagmaCat.{u} × MagmaCat.{u})

/-- Multiplicative port (first factor). -/
noncomputable def multiplicativePort : MagmasWithTwoOperations ⟶ Magmas :=
  (CategoryTheory.Prod.fst MagmaCat.{u} MagmaCat.{u}).toCatHom

/-- Additive port (second factor). -/
noncomputable def additivePort : MagmasWithTwoOperations ⟶ Magmas :=
  (CategoryTheory.Prod.snd MagmaCat.{u} MagmaCat.{u}).toCatHom

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
  Crystals := Crystals
  crystalsToSets := crystalsToSets

end NormalizedCategoryGraph.Realization.Mathlib
