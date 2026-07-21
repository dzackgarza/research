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

/-- Stable identifier represented by a heterogeneous registry entry. -/
def RegistryEntry.stableId : RegistryEntry → String
  | .category e => e.id.raw
  | .categoryFamily e => e.id.raw
  | .classifier e => e.id.raw
  | .alias e => e.id.raw
  | .opaque e => e.id.raw

/-- Lean declarations that must resolve before this row can be persisted. -/
def RegistryEntry.declarations : RegistryEntry → Array Name
  | .category e => #[e.declaration]
  | .categoryFamily e => #[e.declaration, e.fibreDeclaration]
  | .classifier e => #[e.declaration]
  | .alias e => #[e.declaration]
  | .opaque e => #[e.declaration] ++ e.ports.map (·.declaration)

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

/-- Whether this entry's typed stable ID has already been registered. -/
def RegistryState.hasEntryId : RegistryState → RegistryEntry → Bool
  | state, .category e => state.categories.any (·.id == e.id)
  | state, .categoryFamily e => state.categoryFamilies.any (·.id == e.id)
  | state, .classifier e => state.classifiers.any (·.id == e.id)
  | state, .alias e => state.aliases.any (·.id == e.id)
  | state, .opaque e => state.opaqueCategories.any (·.id == e.id)

initialize registryExt : SimplePersistentEnvExtension RegistryEntry RegistryState ←
  registerSimplePersistentEnvExtension {
    addEntryFn := RegistryState.apply
    addImportedFn := fun as =>
      mkStateFromImportedEntries RegistryState.apply {} as
  }

def getRegistry (env : Environment) : RegistryState :=
  registryExt.getState env

def addRegistryEntry (e : RegistryEntry) : CoreM Unit := do
  let env ← getEnv
  let state := getRegistry env
  if state.hasEntryId e then
    throwError "duplicate normalized-category-graph registry ID: {e.stableId}"
  for declaration in e.declarations do
    if declaration.isAnonymous then
      throwError "registry entry {e.stableId} has no declaration name"
    if (env.find? declaration).isNone then
      throwError "registry entry {e.stableId} refers to unknown declaration {declaration}"
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
