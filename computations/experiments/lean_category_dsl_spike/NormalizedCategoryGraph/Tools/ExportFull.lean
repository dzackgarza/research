/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Tools.ExportJson
import NormalizedCategoryGraph.Specimen.Register
import Lean.Data.Json

/-!
# Registry export (`ncg-export-full`)

Emits JSON from the Lean specimen registry (the same rows
`Specimen.Register` writes into `registryExt`). The executable reloads that
module and serializes `getRegistry`; it does not serialize `specimenSnapshot`.

Does **not** read the Python semantic seed / `Spec.SeedData`.
-/

open Lean Elab Command

-- Compile-time: Register must have populated getRegistry with the specimen.
run_cmd
  let env ← getEnv
  let s := NormalizedCategoryGraph.getRegistry env
  if s.categories.isEmpty then
    throwError "getRegistry empty after importing Specimen.Register"
  if s.categories.size != NormalizedCategoryGraph.Specimen.specimenSnapshot.categories.size then
    throwError
      s!"getRegistry categories ({s.categories.size}) ≠ specimenSnapshot ({NormalizedCategoryGraph.Specimen.specimenSnapshot.categories.size})"
  if s.categoryFamilies.size != NormalizedCategoryGraph.Specimen.specimenSnapshot.categoryFamilies.size then
    throwError
      s!"getRegistry category families ({s.categoryFamilies.size}) ≠ specimen snapshot ({NormalizedCategoryGraph.Specimen.specimenSnapshot.categoryFamilies.size})"
  if !(s.categoryFamilies.any fun family =>
      family.id == NormalizedCategoryGraph.CategoryFamilyId.modules) then
    throwError "getRegistry is missing the registered Modules family"
  let baseline := NormalizedCategoryGraph.Tools.snapshotManifestString
    (s.snapshot "0.1.0-specimen")
  if !baseline.contains "fam.modules" then
    throwError "registered Modules family is absent from the exported manifest"

namespace NormalizedCategoryGraph.Tools.ExportFull

open NormalizedCategoryGraph
open Tools

/-- Reload the compiled registry extension; this is the exporter data source. -/
def loadRegisteredSnapshot : IO RegistrySnapshot := do
  let appDir ← IO.appDir
  let buildOleanRoot := appDir.parent.get! / "lib" / "lean"
  let workspaceRoot := appDir.parent.get!.parent.get!.parent.get!
  let packageOleanRoots := [
    "mathlib", "batteries", "Qq", "aesop", "plausible", "LeanSearchClient",
    "proofwidgets", "importGraph",
  ].map fun package =>
    workspaceRoot / ".lake" / "packages" / package / ".lake" / "build" / "lib" / "lean"
  Lean.initSearchPath (← Lean.findSysroot) (buildOleanRoot :: packageOleanRoots)
  unsafe Lean.enableInitializersExecution
  let env ← Lean.importModules #[{ module := `NormalizedCategoryGraph.Specimen.Register }] {}
    (loadExts := true)
  pure ((getRegistry env).snapshot "0.1.0-specimen")

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
  let families ← j.getObjValAs? (Array Json) "categoryFamilies"
  if families.size != 1 then
    throw s!"expected exactly one registered family in the specimen, got {families.size}"
  let family := families[0]!
  let familyId ← family.getObjValAs? String "id"
  if familyId != "fam.modules" then
    throw s!"expected the Modules family, got {familyId}"
  let parameter ← family.getObjValAs? Json "parameter"
  let parameterKind ← parameter.getObjValAs? String "kind"
  if parameterKind != "RingCatObject" then
    throw s!"Modules family parameter must be a RingCat object, got {parameterKind}"
  let variance ← family.getObjValAs? String "variance"
  if variance != "restrictionOfScalarsContravariant" then
    throw s!"Modules family variance must be contravariant restriction of scalars, got {variance}"
  pure ()

def run : IO UInt32 := do
  let snapshot ← loadRegisteredSnapshot
  let manifest := snapshotManifestString snapshot
  match Json.parse manifest with
  | .error e =>
      IO.eprintln s!"JSON parse failed: {e}"
      return 1
  | .ok j =>
      match validate j with
      | .error e =>
          IO.eprintln e
          return 1
      | .ok () =>
          IO.println manifest
          pure 0

end NormalizedCategoryGraph.Tools.ExportFull

def main : IO UInt32 :=
  NormalizedCategoryGraph.Tools.ExportFull.run
