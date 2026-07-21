/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Algebra.Category.ModuleCat.Basic
import Mathlib.LinearAlgebra.FreeModule.Basic
import Mathlib.RingTheory.Finiteness.Basic
import Mathlib.CategoryTheory.Category.Cat
import Mathlib.CategoryTheory.ObjectProperty.FullSubcategory
import NormalizedCategoryGraph.Realization.Mathlib.Algebra

/-!
# Mathlib module atoms

`Modules` is `ModuleCat ℤ`. Free / finite-rank are full subcategories;
`modulesToSets` is the concrete forgetful to `Type`.
-/

namespace NormalizedCategoryGraph.Realization.Mathlib

open CategoryTheory
open NormalizedCategoryGraph

universe u

set_option linter.checkUnivs false

/-- ℤ-modules. -/
def Modules : ObjCat.{u + 1, u} := Cat.of (ModuleCat.{u} ℤ)

/-- Free ℤ-modules. -/
abbrev FreeModuleCat : Type (u + 1) :=
  ObjectProperty.FullSubcategory
    (C := ModuleCat.{u} ℤ) (fun M : ModuleCat.{u} ℤ => Module.Free ℤ M)

/-- Finite ℤ-modules (`Module.Finite`). -/
abbrev FiniteModuleCat : Type (u + 1) :=
  ObjectProperty.FullSubcategory
    (C := ModuleCat.{u} ℤ) (fun M : ModuleCat.{u} ℤ => Module.Finite ℤ M)

/-- Free classifier on Modules. -/
noncomputable def free : Classifier Modules where
  total := Cat.of FreeModuleCat.{u}
  forget := (ObjectProperty.ι
      (C := ModuleCat.{u} ℤ) (fun M : ModuleCat.{u} ℤ => Module.Free ℤ M)).toCatHom

/-- Finite-rank classifier on Modules (finite as ℤ-module). -/
noncomputable def finiteRank : Classifier Modules where
  total := Cat.of FiniteModuleCat.{u}
  forget := (ObjectProperty.ι
      (C := ModuleCat.{u} ℤ) (fun M : ModuleCat.{u} ℤ => Module.Finite ℤ M)).toCatHom

/-- Forgetful Modules → Sets. -/
noncomputable def modulesToSets : Modules ⟶ Sets :=
  (forget (ModuleCat.{u} ℤ)).toCatHom

/-- Module atoms over Mathlib foundations + algebra. -/
noncomputable def moduleAtoms : ModuleAtoms foundationAtoms algebraAtoms where
  Modules := Modules
  free := free
  finiteRank := finiteRank
  modulesToSets := modulesToSets

end NormalizedCategoryGraph.Realization.Mathlib
