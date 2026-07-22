import NormalizedCategoryGraph
import NormalizedCategoryGraph.Realization.Mathlib.Foundation
import NormalizedCategoryGraph.Realization.Mathlib.Atomic
import NormalizedCategoryGraph.Realization.Mathlib.Algebra
import NormalizedCategoryGraph.Realization.Mathlib.Modules
import NormalizedCategoryGraph.Realization.Mathlib.Exceptional
import NormalizedCategoryGraph.Realization.Sage.Correspondence
import NormalizedCategoryGraph.Specimen.Viability
import NormalizedCategoryGraph.Specimen.Register
import NormalizedCategoryGraph.Tools.ExportJson
import NormalizedCategoryGraph.Tools.ExportFull
import LeanCategoryDslSpike
import CatDSL
import CatDSL.Example.F2Semantic
import CatDSL.Example.RegistryTest
import CatDSL.Example.SurfaceTest
import Lean.Util.CollectAxioms

open Lean Elab Command

namespace ResearchLeanAxiomAudit

def permitted : Array Name := #[``propext, ``Classical.choice, ``Quot.sound]

def auditedNamespaces : Array Name := #[`NormalizedCategoryGraph, `LeanCategoryDslSpike, `CatDSL]

def audit : CommandElabM Unit := do
  let env ← getEnv
  let names := env.constants.toList.map Prod.fst |>.filter fun name =>
    auditedNamespaces.any fun namespaceName => namespaceName.isPrefixOf name
  let mut violations : Array (Name × Array Name) := #[]
  for name in names do
    let assumptions ← collectAxioms name
    let unexpected := assumptions.filter fun assumption => !permitted.contains assumption
    if !unexpected.isEmpty then
      violations := violations.push (name, unexpected.qsort Name.lt)
  if !violations.isEmpty then
    throwError m!"nonstandard axiom dependencies: {violations.toList}"

run_cmd audit

end ResearchLeanAxiomAudit
