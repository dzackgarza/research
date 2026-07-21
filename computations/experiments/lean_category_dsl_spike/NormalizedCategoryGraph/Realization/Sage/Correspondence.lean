/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Expr

/-!
# Sage realization — typed correspondence interface

The versioned Sage observation and correspondence records live outside Lean source.
Lean declarations must remain independent of those backend records.
-/

namespace NormalizedCategoryGraph.Realization.Sage

open NormalizedCategoryGraph

/-- Stable identity from a pinned Sage observation. -/
structure SageCategoryId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- Stable identity of a Sage axiom from a pinned observation. -/
structure SageAxiomId where
  raw : String
  deriving DecidableEq, Repr, Hashable

/-- A Sage category observation interpreted as one normalized category expression.
Nested refinements retain the ordered classifiers and route selectors. The concrete
rows belong to the versioned correspondence artifact. -/
structure CategoryCorrespondence where
  observed : SageCategoryId
  normalized : CategoryExpr

/-- A functor reference whose source and target expressions are part of its type. -/
structure StructuralTransport (source target : CategoryExpr) where
  functor : FunctorId

/-- Rehosting disposition for a Sage axiom whose defining host differs from its
normalized least host. -/
inductive AxiomRehosting (source target : CategoryExpr)
  | identical (witness : source = target)
  | transported (map : StructuralTransport source target)

/-- A Sage axiom observation interpreted as one normalized classifier, with the
host comparison and transport needed to make that interpretation explicit. -/
structure AxiomCorrespondence where
  observed : SageAxiomId
  classifier : ClassifierId
  sageHost : CategoryCorrespondence
  normalizedHost : CategoryExpr
  rehosting : AxiomRehosting sageHost.normalized normalizedHost

end NormalizedCategoryGraph.Realization.Sage
