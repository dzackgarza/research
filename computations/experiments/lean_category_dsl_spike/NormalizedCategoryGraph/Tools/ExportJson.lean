/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Specimen.Viability
import Lean.Data.Json

/-!
# Shared JSON serialization for registry snapshots

The exporter constructs `Lean.Json` values directly.  In particular, symbolic
expressions and parameter-family metadata are structured JSON rather than
rendered `repr` text.
-/

namespace NormalizedCategoryGraph.Tools

open Lean
open NormalizedCategoryGraph
open Specimen

private def object (fields : List (String × Json)) : Json := Json.mkObj fields

private def parameterJson : ParameterExpr → Json
  | .ringVariable id => object [("tag", "ringVariable"), ("id", id.raw)]
  | .opposite p => object [("tag", "opposite"), ("of", parameterJson p)]

private def categoryExprJson : CategoryExpr → Json
  | .atom id => object [("tag", "atom"), ("id", id.raw)]
  | .familyApp family args =>
      object [
        ("tag", "familyApp"),
        ("family", family.raw),
        ("args", .arr (args.map parameterJson)),
      ]
  | .classifierTotal classifier =>
      object [("tag", "classifierTotal"), ("classifier", classifier.raw)]
  | .refine base classifier route =>
      object [
        ("tag", "refine"),
        ("base", categoryExprJson base),
        ("classifier", classifier.raw),
        ("route", match route with | some r => r.raw | none => Json.null),
      ]
  | .constructor constructor args =>
      object [
        ("tag", "constructor"),
        ("constructor", constructor.raw),
        ("args", .arr (args.map categoryExprJson)),
      ]
  | .opaque id => object [("tag", "opaque"), ("id", id.raw)]
  | .reference id => object [("tag", "reference"), ("id", id.raw)]

private def originJson : CategoryOrigin → Json
  | .root => "root"
  | .atomicClassifierTotal => "atomicClassifierTotal"
  | .derivedNamed => "derivedNamed"
  | .constructorValue => "constructorValue"
  | .opaqueCategory => "opaqueCategory"
  | .alias => "alias"

private def visibilityJson : Visibility → Json
  | .present => "present"
  | .semanticOnly => "semanticOnly"
  | .presentationHidden => "presentationHidden"

private def parameterKindJson : CategoryFamilyParameterKind → Json
  | .ringObject => "RingCatObject"

private def transportJson : CategoryFamilyTransport → Json
  | .restrictionOfScalarsContravariant => "restrictionOfScalarsContravariant"

private def categoryJson (e : NamedCategoryEntry) : Json :=
  object [
    ("id", e.id.raw),
    ("canonicalName", e.canonicalName),
    ("declaration", e.declaration),
    ("origin", originJson e.origin),
    ("visibility", visibilityJson e.visibility),
    ("expression", categoryExprJson e.expression),
  ]

private def categoryFamilyJson (e : CategoryFamilyEntry) : Json :=
  object [
    ("id", e.id.raw),
    ("canonicalName", e.canonicalName),
    ("declaration", e.declaration),
    ("parameter", object [
      ("name", e.parameter.name),
      ("kind", parameterKindJson e.parameter.kind),
    ]),
    ("fibreDeclaration", e.fibreDeclaration),
    ("transport", transportJson e.transport),
  ]

private def aliasJson (e : AliasEntry) : Json :=
  object [
    ("id", e.id.raw),
    ("spelling", e.spelling),
    ("aliasOf", e.aliasOf.raw),
  ]

private def classifierJson (e : ClassifierEntry) : Json :=
  object [
    ("id", e.id.raw),
    ("canonicalName", e.canonicalName),
    ("hostId", e.hostId.raw),
  ]

private def opaqueJson (e : OpaqueCategoryEntry) : Json :=
  object [
    ("id", e.id.raw),
    ("visibility", visibilityJson e.visibility),
    ("reason", e.reason),
    ("ports", .arr <| e.ports.map fun p => object [
      ("id", p.id.raw),
      ("source", p.source.raw),
      ("target", p.target.raw),
      ("role", p.role.raw),
      ("declaration", p.declaration),
      ("provenance", p.provenance),
    ]),
  ]

/-- Deterministic manifest JSON from a registry snapshot. -/
def snapshotManifestJson (snap : RegistrySnapshot) : Json :=
  let cats := snap.categories.qsort (fun a b => a.id.raw < b.id.raw)
  let families := snap.categoryFamilies.qsort (fun a b => a.id.raw < b.id.raw)
  let clfs := snap.classifiers.qsort (fun a b => a.id.raw < b.id.raw)
  let als := snap.aliases.qsort (fun a b => a.id.raw < b.id.raw)
  let ops := snap.opaqueCategories.qsort (fun a b => a.id.raw < b.id.raw)
  object [
    ("schemaVersion", snap.schemaVersion),
    ("universes", object []),
    ("categories", .arr (cats.map categoryJson)),
    ("classifiers", .arr (clfs.map classifierJson)),
    ("aliases", .arr (als.map aliasJson)),
    ("opaqueCategories", .arr (ops.map opaqueJson)),
    ("categoryFamilies", .arr (families.map categoryFamilyJson)),
    ("namedExpressions", .arr #[]),
    ("structuralPorts", .arr #[]),
    ("theoremInclusions", .arr #[]),
    ("coherences", .arr #[]),
    ("presentationDispositions", .arr #[]),
    ("source", "lean-registry"),
  ]

/-- Serialize a snapshot using Lean's JSON printer. -/
def snapshotManifestString (snap : RegistrySnapshot) : String :=
  (snapshotManifestJson snap).compress

/-- Lean specimen registry JSON (authoritative for the specimen exporter). -/
def specimenManifestJson : String :=
  snapshotManifestString specimenSnapshot

end NormalizedCategoryGraph.Tools
