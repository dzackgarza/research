/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Algebra.Category.ModuleCat.Basic
import Mathlib.Algebra.Category.Ring.Basic
import Mathlib.LinearAlgebra.FreeModule.Basic
import Mathlib.RingTheory.Finiteness.Basic
import Mathlib.CategoryTheory.Category.Cat
import Mathlib.CategoryTheory.ObjectProperty.FullSubcategory
import NormalizedCategoryGraph.Realization.Mathlib.Algebra

/-!
# Mathlib module atoms

* `ModulesFamily` — `RingCat` as the category of base rings for `R ↦ Modules(R)`
* `ModulesOf` — fibre at an arbitrary ring object
* Provisional default fibre: `ModuleCat ℤ`

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
def ModulesFamily : ObjCat.{u + 1, u} := Cat.of RingCat.{u}

/-- Fibre of the parameterized family at an arbitrary ring object. -/
noncomputable def ModulesOf (R : RingCat.{u}) : ObjCat.{u + 1, u} :=
  Cat.of (ModuleCat.{u} R)

/-- The family value; this is not a covariant functor `RingCat ⥤ Cat`. -/
noncomputable def modulesFamilyValue : RingCat.{u} → ObjCat.{u + 1, u} := ModulesOf

example (R : RingCat.{u}) : modulesFamilyValue R = ModulesOf R := rfl

/-- Provisional fibre `Modules(ℤ)`. -/
def Modules : ObjCat.{u + 1, u} := Cat.of (ModuleCat.{u} ℤ)

/-- Free ℤ-modules. -/
abbrev FreeModuleCat : Type (u + 1) :=
  ObjectProperty.FullSubcategory
    (C := ModuleCat.{u} ℤ) (fun M : ModuleCat.{u} ℤ => Module.Free ℤ M)

/-- Finitely generated ℤ-modules (`Module.Finite`). -/
abbrev FinitelyGeneratedModuleCat : Type (u + 1) :=
  ObjectProperty.FullSubcategory
    (C := ModuleCat.{u} ℤ) (fun M : ModuleCat.{u} ℤ => Module.Finite ℤ M)

/-- Finite free rank: free with a finite basis index. Not `Module.Finite`. -/
def IsFiniteRank (M : ModuleCat.{u} ℤ) : Prop :=
  ∃ _ : Module.Free ℤ M, Finite (Module.Free.ChooseBasisIndex ℤ M)

abbrev FiniteRankModuleCat : Type (u + 1) :=
  ObjectProperty.FullSubcategory
    (C := ModuleCat.{u} ℤ) IsFiniteRank

/-- Free classifier on Modules. -/
noncomputable def free : Classifier Modules where
  total := Cat.of FreeModuleCat.{u}
  forget := (ObjectProperty.ι
      (C := ModuleCat.{u} ℤ) (fun M : ModuleCat.{u} ℤ => Module.Free ℤ M)).toCatHom

/-- Finitely-generated classifier (`Module.Finite`). Not finite rank. -/
noncomputable def finitelyGenerated : Classifier Modules where
  total := Cat.of FinitelyGeneratedModuleCat.{u}
  forget := (ObjectProperty.ι
      (C := ModuleCat.{u} ℤ) (fun M : ModuleCat.{u} ℤ => Module.Finite ℤ M)).toCatHom

/-- Finite free rank classifier. -/
noncomputable def finiteRank : Classifier Modules where
  total := Cat.of FiniteRankModuleCat.{u}
  forget := (ObjectProperty.ι (C := ModuleCat.{u} ℤ) IsFiniteRank).toCatHom

/-- Forgetful Modules → Sets. -/
noncomputable def modulesToSets : Modules ⟶ Sets :=
  (forget (ModuleCat.{u} ℤ)).toCatHom

/-- Module atoms over Mathlib foundations + algebra. -/
noncomputable def moduleAtoms : ModuleAtoms foundationAtoms algebraAtoms where
  ModulesFamily := ModulesFamily
  Modules := Modules
  free := free
  finitelyGenerated := finitelyGenerated
  finiteRank := finiteRank
  modulesToSets := modulesToSets

end NormalizedCategoryGraph.Realization.Mathlib
