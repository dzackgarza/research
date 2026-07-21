/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Specimen.Viability
import NormalizedCategoryGraph.Registry.Extension

/-!
# Register the viability specimen into the Lean environment

Elaborator-time registration populates `registryExt` so `getRegistry env`
recovers the same rows the exporters serialize. Import this module when
reflecting the registry via `importModules`.
-/

open Lean Elab Command
open NormalizedCategoryGraph
open NormalizedCategoryGraph.Specimen

run_cmd
  liftCoreM do
    for e in specimenSnapshot.categories do
      addRegistryEntry (.category e)
    for e in specimenSnapshot.categoryFamilies do
      addRegistryEntry (.categoryFamily e)
    for e in specimenSnapshot.classifiers do
      addRegistryEntry (.classifier e)
    for e in specimenSnapshot.aliases do
      addRegistryEntry (.alias e)
    for e in specimenSnapshot.opaqueCategories do
      addRegistryEntry (.opaque e)
