/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Algebra.Category.ModuleCat.Basic
import Mathlib.Algebra.Category.Ring.Basic
import Mathlib.LinearAlgebra.FreeModule.Basic
import Mathlib.RingTheory.Finiteness.Basic
import Mathlib.Algebra.Ring.Opposite
import Mathlib.CategoryTheory.Category.Cat
import Mathlib.CategoryTheory.ObjectProperty.FullSubcategory
import NormalizedCategoryGraph.Realization.Mathlib.Algebra

/-!
# Mathlib module atoms

* `RingObjects` — `RingCat` as the category of base rings for `R ↦ Modules(R)`
* `ModulesOf` — fibre at an arbitrary ring object

* `free` — `Module.Free`
* `finitelyGenerated` — `Module.Finite`
* `finiteRank` — free with a **finite** basis index. This is **not** `Module.Finite`:
  finitely generated modules need not be free / finite-rank.
-/

namespace NormalizedCategoryGraph.Realization.Mathlib

open CategoryTheory
open NormalizedCategoryGraph

universe u

set_option linter.checkUnivs false

/-- Category of base rings for the family `R ↦ Modules(R)`. -/
def RingObjects : ObjCat.{u + 1, u} := Cat.of RingCat.{u}

/-- Fibre of the parameterized family at an arbitrary ring object. -/
noncomputable def ModulesOf (R : RingCat.{u}) : ObjCat.{u + 1, u} :=
  Cat.of (ModuleCat.{u} R)

/-- The family value; this is not a covariant functor `RingCat ⥤ Cat`. -/
noncomputable def modulesFamilyValue : RingCat.{u} → ObjCat.{u + 1, u} := ModulesOf

example (R : RingCat.{u}) : modulesFamilyValue R = ModulesOf R := rfl

/-! ## Fibrewise classifiers -/

/-- Free `R`-modules. -/
abbrev FreeModuleCat (R : RingCat.{u}) : Type (u + 1) :=
  ObjectProperty.FullSubcategory
    (C := ModuleCat.{u} R) (fun M : ModuleCat.{u} R => Module.Free R M)

/-- Finitely generated `R`-modules (`Module.Finite`). -/
abbrev FinitelyGeneratedModuleCat (R : RingCat.{u}) : Type (u + 1) :=
  ObjectProperty.FullSubcategory
    (C := ModuleCat.{u} R) (fun M : ModuleCat.{u} R => Module.Finite R M)

/-- Finite free rank: free with a finite basis index. Not `Module.Finite`. -/
def IsFiniteRank (R : RingCat.{u}) (M : ModuleCat.{u} R) : Prop :=
  ∃ _ : Module.Free R M, Finite (Module.Free.ChooseBasisIndex R M)

abbrev FiniteRankModuleCat (R : RingCat.{u}) : Type (u + 1) :=
  ObjectProperty.FullSubcategory
    (C := ModuleCat.{u} R) (IsFiniteRank R)

/-- Free classifier on `Modules(R)`. -/
noncomputable def free (R : RingCat.{u}) : Classifier (ModulesOf R) where
  total := Cat.of (FreeModuleCat R)
  forget := (ObjectProperty.ι
      (C := ModuleCat.{u} R) (fun M : ModuleCat.{u} R => Module.Free R M)).toCatHom

/-- Finitely-generated classifier (`Module.Finite`). Not finite rank. -/
noncomputable def finitelyGenerated (R : RingCat.{u}) : Classifier (ModulesOf R) where
  total := Cat.of (FinitelyGeneratedModuleCat R)
  forget := (ObjectProperty.ι
      (C := ModuleCat.{u} R) (fun M : ModuleCat.{u} R => Module.Finite R M)).toCatHom

/-- Finite free rank classifier. -/
noncomputable def finiteRank (R : RingCat.{u}) : Classifier (ModulesOf R) where
  total := Cat.of (FiniteRankModuleCat R)
  forget := (ObjectProperty.ι (C := ModuleCat.{u} R) (IsFiniteRank R)).toCatHom

/-- Forgetful `Modules(R) → Sets`. -/
noncomputable def modulesToSets (R : RingCat.{u}) : ModulesOf R ⟶ Sets :=
  (forget (ModuleCat.{u} R)).toCatHom

/-- Opposite-ring substitution for right-module family expressions. -/
noncomputable def oppositeRing (R : RingCat.{u}) : RingCat.{u} := RingCat.of Rᵐᵒᵖ

/-- Right `R`-modules, represented as left modules over the opposite ring. -/
noncomputable def RightModulesOf (R : RingCat.{u}) : ObjCat.{u + 1, u} :=
  ModulesOf (oppositeRing R)

example (R : RingCat.{u}) : RightModulesOf R = ModulesOf (oppositeRing R) := rfl

/-- Module atoms over Mathlib foundations + algebra. -/
noncomputable def moduleAtoms : ModuleAtoms foundationAtoms algebraAtoms where
  RingObjects := RingObjects
  modules := ModulesOf
  oppositeRing := oppositeRing
  free := free
  finitelyGenerated := finitelyGenerated
  finiteRank := finiteRank
  modulesToSets := modulesToSets

end NormalizedCategoryGraph.Realization.Mathlib
