/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Expr
import NormalizedCategoryGraph.Core.Ids
import NormalizedCategoryGraph.Core.StructuralMap
import NormalizedCategoryGraph.Specimen.Viability

/-!
# Magmas cluster — least-host ownership

Owns Magmas and the magma classifiers Associative / Commutative / Unital / Inverse,
plus standard names Semigroups / Monoids / Groups as expressions.
-/

namespace NormalizedCategoryGraph.Categories.Algebra.Magmas

open NormalizedCategoryGraph
open Specimen

/-- Magmas := total(BinaryOperation on Sets). -/
def Magmas : CategoryExpr := exprMagmas

def Associative : ClassifierId := ClassifierId.magmasAssociative
def Commutative : ClassifierId := ClassifierId.magmasCommutative
def Unital : ClassifierId := ClassifierId.magmasUnital
def Inverse : ClassifierId := ClassifierId.magmasInverse

def Semigroups : CategoryExpr := exprSemigroups
def Monoids : CategoryExpr := exprMonoids
def Groups : CategoryExpr := exprGroups

/-- Generated projection `Groups → Magmas` exists in the specimen context. -/
example : (project specimenCtx Groups Magmas .none).isSome = true := by
  native_decide

end NormalizedCategoryGraph.Categories.Algebra.Magmas
