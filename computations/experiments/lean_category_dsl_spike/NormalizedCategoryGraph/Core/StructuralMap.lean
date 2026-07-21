/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Normalize

/-!
# Structural projection

`project : CategoryExpr → CategoryExpr → RouteSelector → Option StructuralMapExpr`

Ordinary ancestry is recovered by structural recursion through the category's
definition — not by searching all functors in a graph.

Equations:
* `project(C, C) = id`
* `project(C.A, C) = π_{C.A,C}`
* `project(C.A, H) = π_{C.A,C} ; project(C, H)` when `H` is an ancestor of `C`
* `project(Name(C), H) = project(C, H)` via reference unfolding (registry)
-/

namespace NormalizedCategoryGraph

/-- Named-expression unfolding: registry resolves a category id to its body. -/
structure NamedExpressionTable where
  bodyOf : CategoryId → Option CategoryExpr

/-- Opaque ports available for projection. -/
structure OpaquePortTable where
  /-- Ports from an opaque source toward a target, keyed by route. -/
  port :
    CategoryId → CategoryId → RouteSelector → Option OpaquePortId

/-- Classifier ownership + refinement ids for certificate references. -/
structure ProjectionContext where
  hosts : ClassifierHostTable
  aliases : AliasTable
  named : NamedExpressionTable
  opaquePorts : OpaquePortTable
  /-- Assign a stable refinement id for `(baseExpr, classifier, route)`. -/
  refinementId : CategoryExpr → ClassifierId → Option RouteId → RefinementId

/-- Equality of category expressions up to the normalizer. -/
def categoryExprEq
    (ctx : ProjectionContext) (a b : CategoryExpr) : Bool :=
  let na := normalizeCategory ctx.hosts ctx.aliases a
  let nb := normalizeCategory ctx.hosts ctx.aliases b
  -- structural DecidableEq is not derived (arrays); compare via Repr strings for the specimen
  toString (repr na) == toString (repr nb)

/-- Unfold references / named atoms one step. -/
def unfoldOnce (ctx : ProjectionContext) : CategoryExpr → CategoryExpr
  | .atom id =>
      match ctx.named.bodyOf (ctx.aliases.canonicalize id) with
      | some e => e
      | none => .atom (ctx.aliases.canonicalize id)
  | .reference id =>
      match ctx.named.bodyOf (ctx.aliases.canonicalize id) with
      | some e => e
      | none => .reference (ctx.aliases.canonicalize id)
  | e => e

/-- Core structural projection (partial: returns `none` when unreachable). -/
partial def project
    (ctx : ProjectionContext) (src tgt : CategoryExpr) (route : RouteSelector) :
    Option StructuralMapExpr :=
  let srcN := normalizeCategory ctx.hosts ctx.aliases src
  let tgtN := normalizeCategory ctx.hosts ctx.aliases tgt
  if categoryExprEq ctx srcN tgtN then
    some (.identity srcN)
  else
    match srcN with
    | .refine base clf r =>
        let π := StructuralMapExpr.baseProjection (ctx.refinementId base clf r)
        if categoryExprEq ctx base tgtN then
          some π
        else
          match project ctx base tgtN route with
          | some rest => some (normalizeMap (.compose #[π, rest]))
          | none => none
    | .classifierTotal clf =>
        -- total(A) projects to host(A) via the classifier leg
        match ctx.hosts.hostOf clf with
        | none => none
        | some host =>
            let hostE : CategoryExpr := .atom host
            let π := StructuralMapExpr.classifierProjection
              (ctx.refinementId hostE clf none)
            if categoryExprEq ctx hostE tgtN then
              some π
            else
              match project ctx hostE tgtN route with
              | some rest => some (normalizeMap (.compose #[π, rest]))
              | none => none
    | .atom id =>
        let id' := ctx.aliases.canonicalize id
        -- named unfolding
        match ctx.named.bodyOf id' with
        | some body =>
            if categoryExprEq ctx body (.atom id') then
              -- opaque / root with no further body
              match srcN, tgtN with
              | .atom s, .atom t =>
                  match ctx.opaquePorts.port s t route with
                  | some p => some (.opaquePort p)
                  | none =>
                      if s == t then some (.identity srcN) else none
              | _, _ => none
            else
              project ctx body tgtN route
        | none =>
            match tgtN with
            | .atom t =>
                if id' == ctx.aliases.canonicalize t then
                  some (.identity srcN)
                else
                  match ctx.opaquePorts.port id' (ctx.aliases.canonicalize t) route with
                  | some p => some (.opaquePort p)
                  | none => none
            | _ => none
    | .opaque id =>
        match tgtN with
        | .atom t | .opaque t | .reference t =>
            match ctx.opaquePorts.port id (ctx.aliases.canonicalize t) route with
            | some p => some (.opaquePort p)
            | none =>
                if id == ctx.aliases.canonicalize t then some (.identity srcN) else none
        | _ => none
    | .reference _ =>
        project ctx (unfoldOnce ctx srcN) tgtN route
    | .familyApp .. | .constructor .. =>
        -- constructor / family: only via named unfolding or opaque ports
        none

end NormalizedCategoryGraph
