/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Tools.ExportJson
import Lean.Data.Json

/-!
# Registry export (`ncg-export-full`)

Emits JSON from **Lean registry data** (viability specimen snapshot), not from
the Python semantic seed / `Spec.SeedData`.

Growing this toward `getRegistry env` reflection is the next step; the Python
seed remains a migration oracle only.
-/

open Lean

namespace NormalizedCategoryGraph.Tools.ExportFull

open NormalizedCategoryGraph
open Tools

/-- Validate Lean-authored registry JSON. -/
def validate (j : Json) : Except String Unit := do
  let schema ← j.getObjValAs? String "schemaVersion"
  if schema.isEmpty then
    throw "missing schemaVersion"
  let source ← j.getObjValAs? String "source"
  if source != "lean-registry" then
    throw s!"expected source=lean-registry, got {source}"
  let cats ← j.getObjValAs? (Array Json) "categories"
  let aliases ← j.getObjValAs? (Array Json) "aliases"
  let names := cats.filterMap fun c => (c.getObjValAs? String "canonicalName").toOption
  for a in aliases do
    let spelling ← a.getObjValAs? String "spelling"
    if names.contains spelling then
      throw s!"alias spelling collides with category node: {spelling}"
  let opaques ← j.getObjValAs? (Array Json) "opaqueCategories"
  for o in opaques do
    let vis ← o.getObjValAs? String "visibility"
    if !vis.endsWith "semanticOnly" then
      throw s!"opaque host must be semanticOnly, got {vis}"
  pure ()

def run : IO UInt32 := do
  match Json.parse specimenManifestJson with
  | .error e =>
      IO.eprintln s!"JSON parse failed: {e}"
      return 1
  | .ok j =>
      match validate j with
      | .error e =>
          IO.eprintln e
          return 1
      | .ok () =>
          IO.println specimenManifestJson
          pure 0

end NormalizedCategoryGraph.Tools.ExportFull

def main : IO UInt32 :=
  NormalizedCategoryGraph.Tools.ExportFull.run
