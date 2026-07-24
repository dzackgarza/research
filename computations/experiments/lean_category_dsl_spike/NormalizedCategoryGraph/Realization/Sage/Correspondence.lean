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

/-- **Observation record** (decision record 3 §4). A reference to a Sage functor
*claimed* to transport `source` to `target`, carrying only its `FunctorId` — not the
functor itself, nor a proof that it realizes `source → target` or performs the rehosting.
The type parameters record the claimed endpoints; the agreement is an obligation, not
evidence. The proof-carrying alternative indexes this by a normalized declaration
imported from lean-lattices (blocked on the pinned release, dzackgarza/lean-lattices#4). -/
structure ObservedTransport (source target : CategoryExpr) where
  observedFunctor : FunctorId

/-- Rehosting disposition for a Sage axiom whose defining host differs from its
normalized least host. `identical` carries a genuine proof `source = target`;
`transported` is an observation record (see `ObservedTransport`) whose agreement is an
obligation, not a proof. -/
inductive AxiomRehosting (source target : CategoryExpr)
  | identical (witness : source = target)
  | transported (map : ObservedTransport source target)

/-- A Sage axiom observation interpreted as one normalized classifier, with the
host comparison and transport needed to make that interpretation explicit. -/
structure AxiomCorrespondence where
  observed : SageAxiomId
  classifier : ClassifierId
  sageHost : CategoryCorrespondence
  normalizedHost : CategoryExpr
  rehosting : AxiomRehosting sageHost.normalized normalizedHost

end NormalizedCategoryGraph.Realization.Sage
