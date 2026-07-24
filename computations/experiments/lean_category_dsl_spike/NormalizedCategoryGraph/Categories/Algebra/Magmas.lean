/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Expr
import NormalizedCategoryGraph.Core.Ids

/-!
# Magmas cluster — least-host ownership

Owns Magmas and the magma classifiers Associative / Commutative / Unital / Inverse,
plus standard names Semigroups / Monoids / Groups as expressions.
-/

namespace NormalizedCategoryGraph.Categories.Algebra.Magmas

open NormalizedCategoryGraph
/-- Magmas := total(BinaryOperation on Sets). -/
def Magmas : CategoryExpr := .classifierTotal ClassifierId.setsBinaryOperation

def Associative : ClassifierId := ClassifierId.magmasAssociative
def Commutative : ClassifierId := ClassifierId.magmasCommutative
def Unital : ClassifierId := ClassifierId.magmasUnital
def Inverse : ClassifierId := ClassifierId.magmasInverse

def Semigroups : CategoryExpr := .refine Magmas Associative none
def Monoids : CategoryExpr := .refine Semigroups Unital none
def Groups : CategoryExpr := .refine Monoids Inverse none

end NormalizedCategoryGraph.Categories.Algebra.Magmas
