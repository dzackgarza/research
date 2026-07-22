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

private partial def containsPullback : CategoryExpr → Bool
  | .pullback .. => true
  | .refine base _ _ => containsPullback base
  | .constructor _ args => (args.map containsPullback).any id
  | _ => false

run_cmd
  liftCoreM do
    for e in specimenSnapshot.categories do
      if !containsPullback e.expression then
        addRegistryEntry (.category e)
    for e in specimenSnapshot.categoryFamilies do
      addRegistryEntry (.categoryFamily e)
    for e in specimenSnapshot.classifiers do
      addRegistryEntry (.classifier e)
    for e in specimenSnapshot.opaqueCategories do
      addRegistryEntry (.opaque e)
    for e in specimenSnapshot.constructors do
      addRegistryEntry (.constructor e)
    for e in specimenSnapshot.finiteLimitCones do
      addRegistryEntry (.finiteLimitCone e)
    for e in specimenSnapshot.theoremInclusions do
      addRegistryEntry (.theoremInclusion e)
    for e in specimenSnapshot.functors do
      addRegistryEntry (.functor e)
    for e in specimenSnapshot.categories do
      if containsPullback e.expression then
        addRegistryEntry (.category e)
    for e in specimenSnapshot.aliases do
      addRegistryEntry (.alias e)
    for e in specimenSnapshot.coherences do
      addRegistryEntry (.coherence e)
    for e in specimenSnapshot.presentations do
      addRegistryEntry (.presentation e)
