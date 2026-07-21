/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Spec.SeedData
import Lean.Data.Json

/-!
# Full semantic export from the generated seed specification

Emits the deterministic JSON embedded in `Spec.SeedData` (sorted at generation).
Also validates basic invariants: no alias category names, opaque hosts are
`semanticOnly`, schema present.
-/

open Lean

namespace NormalizedCategoryGraph.Tools.ExportFull

def validate (j : Json) : Except String Unit := do
  let schema ← j.getObjValAs? String "schemaVersion"
  if !schema.startsWith "0." then
    throw s!"unexpected schemaVersion {schema}"
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
    if vis != "semanticOnly" then
      throw s!"opaque host must be semanticOnly, got {vis}"
  pure ()

def run : IO UInt32 := do
  match Json.parse NormalizedCategoryGraph.Spec.seedManifestJson with
  | .error e =>
      IO.eprintln s!"JSON parse failed: {e}"
      return 1
  | .ok j =>
      match validate j with
      | .error e =>
          IO.eprintln e
          return 1
      | .ok () =>
          IO.println NormalizedCategoryGraph.Spec.seedManifestJson
          pure 0

end NormalizedCategoryGraph.Tools.ExportFull

def main : IO UInt32 :=
  NormalizedCategoryGraph.Tools.ExportFull.run
