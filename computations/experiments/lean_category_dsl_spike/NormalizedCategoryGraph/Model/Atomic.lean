/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.CategoricalPullback
import NormalizedCategoryGraph.Core.Ids

/-!
# Atomic model (model-parametric semantics)

Semantic definitions typecheck for every `M : AtomicModel`. The Mathlib
instance is `Realization.Mathlib.atomicModel`.
-/

namespace NormalizedCategoryGraph

open CategoryTheory

universe uObj uHom

set_option linter.checkUnivs false

/-- Irreducible foundation atoms. -/
structure FoundationAtoms where
  Sets : ObjCat.{uObj, uHom}
  finite : Classifier Sets
  graded : Classifier Sets
  binaryOperation : Classifier Sets

/-- Algebra classifiers whose least host is Magmas. -/
structure AlgebraAtoms (F : FoundationAtoms.{uObj, uHom}) where
  associative : Classifier F.binaryOperation.total
  commutative : Classifier F.binaryOperation.total
  unital : Classifier F.binaryOperation.total
  inverse : Classifier F.binaryOperation.total

/-- Module atoms. -/
structure ModuleAtoms (F : FoundationAtoms.{uObj, uHom}) (_A : AlgebraAtoms F) where
  Modules : ObjCat.{uObj, uHom}
  free : Classifier Modules
  finiteRank : Classifier Modules
  modulesToSets : Modules ⟶ F.Sets

/-- Exceptional opaque hosts with typed ports. -/
structure ExceptionalAtoms (F : FoundationAtoms.{uObj, uHom}) where
  MagmasWithTwoOperations : ObjCat.{uObj, uHom}
  additivePort : MagmasWithTwoOperations ⟶ F.binaryOperation.total
  multiplicativePort : MagmasWithTwoOperations ⟶ F.binaryOperation.total
  Crystals : ObjCat.{uObj, uHom}
  crystalsToSets : Crystals ⟶ F.Sets

/-- Full atomic model. -/
structure AtomicModel where
  foundations : FoundationAtoms.{uObj, uHom}
  algebra : AlgebraAtoms foundations
  modules : ModuleAtoms foundations algebra
  exceptional : ExceptionalAtoms foundations

namespace Normalized

variable (M : AtomicModel.{uObj, uHom})

def Sets : ObjCat.{uObj, uHom} := M.foundations.Sets

def Magmas : ObjCat.{uObj, uHom} := M.foundations.binaryOperation.total

def magmasToSets : Magmas M ⟶ Sets M :=
  M.foundations.binaryOperation.forget

/-- Semigroups := Magmas.Associative (exact-host → classifier total). -/
def Semigroups : ObjCat := M.algebra.associative.total

def semigroupsToMagmas : Semigroups M ⟶ Magmas M :=
  M.algebra.associative.forget

/-- Monoids := Semigroups.Unital via reindex of Unital along Semigroups → Magmas. -/
noncomputable def Monoids : ObjCat :=
  (Classifier.reindex (semigroupsToMagmas M) M.algebra.unital).total

noncomputable def monoidsToSemigroups : Monoids M ⟶ Semigroups M :=
  (Classifier.reindex (semigroupsToMagmas M) M.algebra.unital).baseProjection

/-- Groups := Monoids.Inverse. -/
noncomputable def Groups : ObjCat :=
  let monoidsToMagmas :=
    (Classifier.reindex (semigroupsToMagmas M) M.algebra.unital).baseProjection ≫
      semigroupsToMagmas M
  (Classifier.reindex monoidsToMagmas M.algebra.inverse).total

/-- Rings as the two-operation host (`MagmasWithTwoOperations`). -/
def Rings : ObjCat := M.exceptional.MagmasWithTwoOperations

def ringsToMagmasMul : Rings M ⟶ Magmas M :=
  M.exceptional.multiplicativePort

def ringsToMagmasAdd : Rings M ⟶ Magmas M :=
  M.exceptional.additivePort

/-- CommutativeRings := Rings.Commutative[via := multiplicative]. -/
noncomputable def CommutativeRings : ObjCat :=
  (Classifier.reindex (ringsToMagmasMul M) M.algebra.commutative).total

def Modules : ObjCat := M.modules.Modules

def FreeModules : ObjCat := M.modules.free.total

/-- `Modules(R).Free.Finite` — Finite from Sets along Free → Modules → Sets. -/
noncomputable def FiniteFreeModules : ObjCat :=
  (Classifier.reindex
      (M.modules.free.forget ≫ M.modules.modulesToSets)
      M.foundations.finite).total

end Normalized

end NormalizedCategoryGraph
