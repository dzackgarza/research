/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Specimen.Viability

/-!
# Shared JSON serialization for registry snapshots
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

/-- Deterministic manifest JSON from a registry snapshot. -/
def snapshotManifestJson (snap : RegistrySnapshot) : String :=
  let cats := snap.categories.qsort (fun a b => a.id.raw < b.id.raw)
  let clfs := snap.classifiers.qsort (fun a b => a.id.raw < b.id.raw)
  let als := snap.aliases.qsort (fun a b => a.id.raw < b.id.raw)
  let ops := snap.opaqueCategories.qsort (fun a b => a.id.raw < b.id.raw)
  let catJson := ",".intercalate (cats.map jsonCategory).toList
  let clfJson := ",".intercalate (clfs.map jsonClassifier).toList
  let alJson := ",".intercalate (als.map jsonAlias).toList
  let opJson := ",".intercalate (ops.map jsonOpaque).toList
  "{" ++
    s!"\"schemaVersion\":{jsonString snap.schemaVersion}," ++
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
    "\"presentationDispositions\":[]," ++
    "\"source\":\"lean-registry\"" ++
  "}"

/-- Lean specimen registry JSON (authoritative for exporters). -/
def specimenManifestJson : String :=
  snapshotManifestJson specimenSnapshot

end NormalizedCategoryGraph.Tools
