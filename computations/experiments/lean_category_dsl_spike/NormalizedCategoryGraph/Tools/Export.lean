/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Tools.ExportJson

/-!
# Deterministic JSON export (specimen)

Interchange format is JSON. Sorted by stable ID. Does not parse Lean source.
Does not read the Python semantic seed.
-/

namespace NormalizedCategoryGraph.Tools

open NormalizedCategoryGraph
open Specimen

def main : IO UInt32 := do
  IO.println specimenManifestJson
  let cats := specimenSnapshot.categories
  let nComm := (cats.filter (·.id == CategoryId.commutativeRings)).size
  let nCRingsName := (cats.filter (·.canonicalName == "CRings")).size
  if nComm != 1 then
    IO.eprintln s!"expected 1 CommutativeRings, got {nComm}"
    return 1
  if nCRingsName != 0 then
    IO.eprintln "CRings must not appear as a category node"
    return 1
  if !(project specimenCtx exprFiniteFreeModules exprSets .none).isSome then
    IO.eprintln "project(FiniteFreeModules, Sets) failed"
    return 1
  if !(project specimenCtx exprGroups exprMagmas .none).isSome then
    IO.eprintln "project(Groups, Magmas) failed"
    return 1
  -- Rings is a derived refine tower, not the opaque M2O host.
  if !(project specimenCtx exprMagmasWithTwoOperations (.atom CategoryId.magmas)
        (.route RouteId.multiplicative)).isSome then
    IO.eprintln "project(M2O, Magmas, multiplicative) failed"
    return 1
  pure 0

end NormalizedCategoryGraph.Tools

/-- Lake executable entry point. -/
def main : IO UInt32 :=
  NormalizedCategoryGraph.Tools.main
