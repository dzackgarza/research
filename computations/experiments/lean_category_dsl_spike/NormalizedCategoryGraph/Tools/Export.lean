/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Specimen.Viability

/-!
# Deterministic JSON export (specimen)

Interchange format is JSON. Sorted by stable ID. Does not parse Lean source.
-/

namespace NormalizedCategoryGraph.Tools

open NormalizedCategoryGraph
open Specimen

def escapeJson (s : String) : String :=
  s.replace "\\" "\\\\"
    |>.replace "\"" "\\\""
    |>.replace "\n" "\\n"
    |>.replace "\r" "\\r"
    |>.replace "\t" "\\t"

def jsonString (s : String) : String :=
  s!"\"{escapeJson s}\""

def jsonCategory (e : NamedCategoryEntry) : String :=
  "{" ++
    s!"\"id\":{jsonString e.id.raw}," ++
    s!"\"canonicalName\":{jsonString e.canonicalName}," ++
    s!"\"declaration\":{jsonString e.declaration}," ++
    s!"\"origin\":{jsonString (toString (repr e.origin))}," ++
    s!"\"visibility\":{jsonString (toString (repr e.visibility))}," ++
    s!"\"expression\":{jsonString (toString (repr e.expression))}" ++
  "}"

def jsonAlias (e : AliasEntry) : String :=
  "{" ++
    s!"\"id\":{jsonString e.id.raw}," ++
    s!"\"spelling\":{jsonString e.spelling}," ++
    s!"\"aliasOf\":{jsonString e.aliasOf.raw}" ++
  "}"

def jsonClassifier (e : ClassifierEntry) : String :=
  "{" ++
    s!"\"id\":{jsonString e.id.raw}," ++
    s!"\"canonicalName\":{jsonString e.canonicalName}," ++
    s!"\"hostId\":{jsonString e.hostId.raw}" ++
  "}"

def jsonOpaque (e : OpaqueCategoryEntry) : String :=
  "{" ++
    s!"\"id\":{jsonString e.id.raw}," ++
    s!"\"visibility\":{jsonString (toString (repr e.visibility))}," ++
    s!"\"reason\":{jsonString e.reason}," ++
    s!"\"ports\":{e.ports.size}" ++
  "}"

def sortById (ids : Array String) : Array String :=
  ids.qsort (· < ·)

/-- Deterministic manifest JSON from the viability specimen snapshot. -/
def specimenManifestJson : String :=
  let cats := specimenSnapshot.categories.qsort (fun a b => a.id.raw < b.id.raw)
  let clfs := specimenSnapshot.classifiers.qsort (fun a b => a.id.raw < b.id.raw)
  let als := specimenSnapshot.aliases.qsort (fun a b => a.id.raw < b.id.raw)
  let ops := specimenSnapshot.opaqueCategories.qsort (fun a b => a.id.raw < b.id.raw)
  let catJson := ",".intercalate (cats.map jsonCategory).toList
  let clfJson := ",".intercalate (clfs.map jsonClassifier).toList
  let alJson := ",".intercalate (als.map jsonAlias).toList
  let opJson := ",".intercalate (ops.map jsonOpaque).toList
  "{" ++
    s!"\"schemaVersion\":{jsonString specimenSnapshot.schemaVersion}," ++
    "\"universes\":{}," ++
    s!"\"categories\":[{catJson}]," ++
    s!"\"classifiers\":[{clfJson}]," ++
    s!"\"aliases\":[{alJson}]," ++
    s!"\"opaqueCategories\":[{opJson}]," ++
    "\"categoryFamilies\":[]," ++
    "\"namedExpressions\":[]," ++
    "\"structuralPorts\":[]," ++
    "\"theoremInclusions\":[]," ++
    "\"coherences\":[]," ++
    "\"presentationDispositions\":[]" ++
  "}"

def main : IO UInt32 := do
  IO.println specimenManifestJson
  -- Basic invariants for the executable gate
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
  pure 0

end NormalizedCategoryGraph.Tools

/-- Lake executable entry point. -/
def main : IO UInt32 :=
  NormalizedCategoryGraph.Tools.main
