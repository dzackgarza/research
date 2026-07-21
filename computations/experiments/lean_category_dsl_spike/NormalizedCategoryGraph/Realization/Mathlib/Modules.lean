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

Provisional fibre: `ModuleCat ℤ`. This is a specialization of the intended
family `R ↦ Modules(R)`, not the family itself.

* `free` — `Module.Free`
* `finitelyGenerated` — `Module.Finite` (Mathlib's finitely generated modules)

`FiniteRank` is **not** realized here: it is not `Module.Finite`.
-/

namespace NormalizedCategoryGraph.Realization.Mathlib

open CategoryTheory
open NormalizedCategoryGraph

universe u

set_option linter.checkUnivs false

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

/-- Forgetful Modules → Sets. -/
noncomputable def modulesToSets : Modules ⟶ Sets :=
  (forget (ModuleCat.{u} ℤ)).toCatHom

/-- Module atoms over Mathlib foundations + algebra. -/
noncomputable def moduleAtoms : ModuleAtoms foundationAtoms algebraAtoms where
  Modules := Modules
  free := free
  finitelyGenerated := finitelyGenerated
  modulesToSets := modulesToSets

end NormalizedCategoryGraph.Realization.Mathlib
