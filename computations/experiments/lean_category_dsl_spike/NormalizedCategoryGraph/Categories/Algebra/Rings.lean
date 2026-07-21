/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Categories.Algebra.Magmas
import NormalizedCategoryGraph.Core.Ids
import NormalizedCategoryGraph.Specimen.Viability

/-!
# Rings cluster

Owns the two-operation host interface and ring names. Does **not** redeclare
`Commutative` as a ring classifier — applies the magma classifier along the
multiplicative port.
-/

namespace NormalizedCategoryGraph.Categories.Algebra.Rings

open NormalizedCategoryGraph
open Specimen
open Categories.Algebra.Magmas

/-- Rings as the opaque two-operation host (pending distributivity theory). -/
def Rings : CategoryExpr := exprRings

/-- CommutativeRings := Rings.Commutative[via := multiplicative]. -/
def CommutativeRings : CategoryExpr := exprCommRings

/-- Multiplicative port (not additive). Target is the named atom `cat.magmas`. -/
example :
    (project specimenCtx Rings (.atom CategoryId.magmas)
      (.route RouteId.multiplicative)).isSome = true := by
  native_decide

/-- Additive port is a distinct route. -/
example :
    (project specimenCtx Rings (.atom CategoryId.magmas)
      (.route RouteId.additive)).isSome = true := by
  native_decide

end NormalizedCategoryGraph.Categories.Algebra.Rings
