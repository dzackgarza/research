/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Registry.Entry
import Lean

/-!
# Persistent registry extension

`addImportedFn` receives `Array (Array RegistryEntry)` from imported modules.
-/

namespace NormalizedCategoryGraph

open Lean

inductive RegistryEntry
  | category (e : NamedCategoryEntry)
  | categoryFamily (e : CategoryFamilyEntry)
  | classifier (e : ClassifierEntry)
  | alias (e : AliasEntry)
  | opaque (e : OpaqueCategoryEntry)
  deriving Repr

structure RegistryState where
  categories : Array NamedCategoryEntry := #[]
  categoryFamilies : Array CategoryFamilyEntry := #[]
  classifiers : Array ClassifierEntry := #[]
  aliases : Array AliasEntry := #[]
  opaqueCategories : Array OpaqueCategoryEntry := #[]
  deriving Inhabited

def RegistryState.apply : RegistryState → RegistryEntry → RegistryState
  | s, .category e => { s with categories := s.categories.push e }
  | s, .categoryFamily e => { s with categoryFamilies := s.categoryFamilies.push e }
  | s, .classifier e => { s with classifiers := s.classifiers.push e }
  | s, .alias e => { s with aliases := s.aliases.push e }
  | s, .opaque e => { s with opaqueCategories := s.opaqueCategories.push e }

initialize registryExt : SimplePersistentEnvExtension RegistryEntry RegistryState ←
  registerSimplePersistentEnvExtension {
    addEntryFn := RegistryState.apply
    addImportedFn := fun as =>
      mkStateFromImportedEntries RegistryState.apply {} as
  }

def getRegistry (env : Environment) : RegistryState :=
  registryExt.getState env

def addRegistryEntry (e : RegistryEntry) : CoreM Unit := do
  modifyEnv (registryExt.addEntry · e)

/-- Materialize the registered state for a Lean-authored export. -/
def RegistryState.snapshot (state : RegistryState) (schemaVersion : String) : RegistrySnapshot where
  schemaVersion
  categories := state.categories
  categoryFamilies := state.categoryFamilies
  classifiers := state.classifiers
  aliases := state.aliases
  opaqueCategories := state.opaqueCategories
  equivalences := #[]

end NormalizedCategoryGraph
