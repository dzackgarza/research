/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.CategoricalPullback
import NormalizedCategoryGraph.Core.Expr
import NormalizedCategoryGraph.Model.Atomic

/-!
# Interpretation — evaluate category expressions in an atomic model

Refinements are interpreted by `Classifier.reindex` (categorical pullback).
Magmas-hosted towers compose forgetfuls to `Magmas`; two-operation refinements
use the additive/multiplicative ports.
-/

namespace NormalizedCategoryGraph

open Normalized CategoryTheory

universe uObj uHom

/-- Interpret atoms of `M`. -/
noncomputable def evalAtom (M : AtomicModel.{uObj, uHom}) (id : CategoryId) :
    Option (ObjCat.{uObj, uHom}) :=
  if id == CategoryId.sets then some (Sets M)
  else if id == CategoryId.magmas then some (Magmas M)
  else if id == CategoryId.semigroups then some (Semigroups M)
  else if id == CategoryId.monoids then some (Monoids M)
  else if id == CategoryId.groups then some (Groups M)
  else if id == CategoryId.rings then some (Rings M)
  else if id == CategoryId.commutativeRings then some (CommutativeRings M)
  else if id == CategoryId.divisionRings then some (DivisionRings M)
  else if id == CategoryId.modulesR then some (Modules M)
  else if id == CategoryId.magmasWithTwoOperations then
    some (MagmasWithTwoOperations M)
  else if id == CategoryId.crystals then some M.exceptional.Crystals
  else none

/-- Magmas-hosted classifiers. -/
noncomputable def magmasClassifier (M : AtomicModel.{uObj, uHom}) (id : ClassifierId) :
    Option (Classifier (Magmas M)) :=
  if id == ClassifierId.magmasAssociative then some M.algebra.associative
  else if id == ClassifierId.magmasCommutative then some M.algebra.commutative
  else if id == ClassifierId.magmasUnital then some M.algebra.unital
  else if id == ClassifierId.magmasInverse then some M.algebra.inverse
  else none

/-- Sets-hosted classifiers. -/
noncomputable def setsClassifier (M : AtomicModel.{uObj, uHom}) (id : ClassifierId) :
    Option (Classifier (Sets M)) :=
  if id == ClassifierId.setsFinite then some M.foundations.finite
  else if id == ClassifierId.setsGraded then some M.foundations.graded
  else if id == ClassifierId.setsBinaryOperation then some M.foundations.binaryOperation
  else none

/-- Modules-hosted classifiers. -/
noncomputable def modulesClassifier (M : AtomicModel.{uObj, uHom}) (id : ClassifierId) :
    Option (Classifier (Modules M)) :=
  if id == ClassifierId.modulesFree then some M.modules.free
  else if id == ClassifierId.modulesFinitelyGenerated then some M.modules.finitelyGenerated
  else none

/-- M2O-hosted classifiers. -/
noncomputable def m2oClassifier (M : AtomicModel.{uObj, uHom}) (id : ClassifierId) :
    Option (Classifier (MagmasWithTwoOperations M)) :=
  if id == ClassifierId.m2oDistributive then some M.exceptional.distributive
  else if id == ClassifierId.ringsDivision then some M.exceptional.division
  else none

/-- A forgetful functor into `Magmas`, with its domain. -/
structure ForgetfulToMagmas (M : AtomicModel.{uObj, uHom}) where
  domain : ObjCat.{uObj, uHom}
  forget : domain ⟶ Magmas M

/-- A forgetful functor into `Modules`, with its domain. -/
structure ForgetfulToModules (M : AtomicModel.{uObj, uHom}) where
  domain : ObjCat.{uObj, uHom}
  forget : domain ⟶ Modules M

/-- Forgetful for named Magmas-tower atoms. -/
noncomputable def forgetfulToMagmasAtom (M : AtomicModel.{uObj, uHom}) (id : CategoryId) :
    Option (ForgetfulToMagmas M) :=
  if id == CategoryId.magmas then
    some ⟨Magmas M, CategoryTheory.CategoryStruct.id (Magmas M)⟩
  else if id == CategoryId.semigroups then
    some ⟨Semigroups M, semigroupsToMagmas M⟩
  else if id == CategoryId.monoids then
    some
      ⟨Monoids M,
        (Classifier.reindex (semigroupsToMagmas M) M.algebra.unital).baseProjection ≫
          semigroupsToMagmas M⟩
  else if id == CategoryId.groups then
    let monoidsToMagmas :=
      (Classifier.reindex (semigroupsToMagmas M) M.algebra.unital).baseProjection ≫
        semigroupsToMagmas M
    some
      ⟨Groups M,
        (Classifier.reindex monoidsToMagmas M.algebra.inverse).baseProjection ≫
          monoidsToMagmas⟩
  else
    none

/-- Composite forgetful from a Magmas-hosted expression down to `Magmas`. -/
noncomputable def forgetfulToMagmas (M : AtomicModel.{uObj, uHom}) :
    CategoryExpr → Option (ForgetfulToMagmas M)
  | .atom id => forgetfulToMagmasAtom M id
  | .classifierTotal id =>
      if id == ClassifierId.setsBinaryOperation then
        some ⟨Magmas M, CategoryTheory.CategoryStruct.id (Magmas M)⟩
      else
        none
  | .reference id => forgetfulToMagmasAtom M id
  | .refine base clf _ =>
      match magmasClassifier M clf, forgetfulToMagmas M base with
      | some A, some Fbase =>
          let R := Classifier.reindex Fbase.forget A
          some ⟨R.total, R.baseProjection ≫ Fbase.forget⟩
      | _, _ => none
  | _ => none

/-- Forgetful for the Modules atom. -/
noncomputable def forgetfulToModulesAtom (M : AtomicModel.{uObj, uHom}) (id : CategoryId) :
    Option (ForgetfulToModules M) :=
  if id == CategoryId.modulesR then
    some ⟨Modules M, CategoryTheory.CategoryStruct.id (Modules M)⟩
  else
    none

/-- Forgetful from a Modules-hosted expression to `Modules`. -/
noncomputable def forgetfulToModules (M : AtomicModel.{uObj, uHom}) :
    CategoryExpr → Option (ForgetfulToModules M)
  | .atom id => forgetfulToModulesAtom M id
  | .refine base clf _ =>
      match modulesClassifier M clf, forgetfulToModules M base with
      | some A, some Fbase =>
          let R := Classifier.reindex Fbase.forget A
          some ⟨R.total, R.baseProjection ≫ Fbase.forget⟩
      | _, _ => none
  | .reference id => forgetfulToModulesAtom M id
  | _ => none

/-- Evaluate a category expression to an actual `ObjCat`. -/
noncomputable def evalCategory (M : AtomicModel.{uObj, uHom}) :
    CategoryExpr → Option (ObjCat.{uObj, uHom})
  | .atom id => evalAtom M id
  | .opaque id => evalAtom M id
  | .reference id => evalAtom M id
  | .classifierTotal id =>
      match magmasClassifier M id with
      | some A => some A.total
      | none =>
          match setsClassifier M id with
          | some A => some A.total
          | none =>
              match modulesClassifier M id with
              | some A => some A.total
              | none =>
                  match m2oClassifier M id with
                  | some A => some A.total
                  | none => none
  | .refine base clf route =>
      match magmasClassifier M clf with
      | some A =>
          match forgetfulToMagmas M base with
          | some F => some (Classifier.reindex F.forget A).total
          | none =>
              match base with
              | .atom bid =>
                  if bid == CategoryId.magmasWithTwoOperations ∧
                      (route == some RouteId.additive ∨ route == none) then
                    some (Classifier.reindex (m2oToMagmasAdd M) A).total
                  else if bid == CategoryId.magmasWithTwoOperations ∧
                      route == some RouteId.multiplicative then
                    some (Classifier.reindex (m2oToMagmasMul M) A).total
                  else if bid == CategoryId.rings ∧
                      route == some RouteId.multiplicative then
                    some (Classifier.reindex (ringsToMagmasMul M) A).total
                  else if bid == CategoryId.rings ∧
                      route == some RouteId.additive then
                    some (Classifier.reindex (ringsToMagmasAdd M) A).total
                  else
                    none
              | _ => none
      | none =>
          match modulesClassifier M clf with
          | some A =>
              match forgetfulToModules M base with
              | some F => some (Classifier.reindex F.forget A).total
              | none => none
          | none =>
              match setsClassifier M clf with
              | some A =>
                  match base with
                  | .atom bid =>
                      if bid == CategoryId.magmas then
                        some (Classifier.reindex (magmasToSets M) A).total
                      else if bid == CategoryId.modulesR then
                        some (Classifier.reindex M.modules.modulesToSets A).total
                      else if bid == CategoryId.sets then
                        some
                          (Classifier.reindex
                            (CategoryTheory.CategoryStruct.id (Sets M)) A).total
                      else
                        none
                  | .classifierTotal cid =>
                      if cid == ClassifierId.setsBinaryOperation then
                        some (Classifier.reindex (magmasToSets M) A).total
                      else
                        none
                  | .refine .. =>
                      match forgetfulToModules M base with
                      | some Fm =>
                          some
                            (Classifier.reindex (Fm.forget ≫ M.modules.modulesToSets) A).total
                      | none =>
                          match forgetfulToMagmas M base with
                          | some Fmag =>
                              some
                                (Classifier.reindex (Fmag.forget ≫ magmasToSets M) A).total
                          | none => none
                  | _ => none
              | none =>
                  match m2oClassifier M clf with
                  | some A =>
                      match base with
                      | .atom bid =>
                          if bid == CategoryId.magmasWithTwoOperations then
                            some
                              (Classifier.reindex
                                (CategoryTheory.CategoryStruct.id
                                  (MagmasWithTwoOperations M))
                                A).total
                          else if bid == CategoryId.rings then
                            let ringsToM2O :=
                              ringsToRngs M ≫
                                rngsToMulAssoc M ≫
                                  m2oMulAssocToAddInv M ≫ m2oAddInvToM2O M
                            some (Classifier.reindex ringsToM2O A).total
                          else
                            none
                      | _ => none
                  | none => none
  | .familyApp _ _ => none
  | .constructor _ _ => none

end NormalizedCategoryGraph
