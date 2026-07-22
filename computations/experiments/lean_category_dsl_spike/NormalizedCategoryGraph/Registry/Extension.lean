/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Registry.Entry
import NormalizedCategoryGraph.Core.Classifier
import NormalizedCategoryGraph.Model.Interpretation
import Lean

/-!
# Persistent registry extension

`addImportedFn` receives `Array (Array RegistryEntry)` from imported modules.
-/

namespace NormalizedCategoryGraph

open Lean
open Lean Meta
open Lean Elab Command

inductive RegistryEntry
  | category (e : NamedCategoryEntry)
  | categoryFamily (e : CategoryFamilyEntry)
  | classifier (e : ClassifierEntry)
  | functor (e : FunctorEntry)
  | constructor (e : ConstructorEntry)
  | finiteLimitCone (e : FiniteLimitConeEntry)
  | coherence (e : CoherenceEntry)
  | theoremInclusion (e : TheoremInclusionEntry)
  | alias (e : AliasEntry)
  | opaque (e : OpaqueCategoryEntry)
  | presentation (e : PresentationEntry)
  deriving Repr

/-- Stable identifier represented by a heterogeneous registry entry. -/
def RegistryEntry.stableId : RegistryEntry → String
  | .category e => e.id.raw
  | .categoryFamily e => e.id.raw
  | .classifier e => e.id.raw
  | .functor e => e.id.raw
  | .constructor e => e.id.raw
  | .finiteLimitCone e => e.id.raw
  | .coherence e => e.id.raw
  | .theoremInclusion e => e.id.raw
  | .alias e => e.id.raw
  | .opaque e => e.id.raw
  | .presentation e => e.id.raw

/-- Lean declarations that must resolve before this row can be persisted. -/
def RegistryEntry.declarations : RegistryEntry → Array Name
  | .category e => #[e.declaration] ++ e.realization.toArray
  | .categoryFamily e => #[e.declaration, e.fibreDeclaration]
  | .classifier e => #[e.declaration]
  | .functor e => #[e.declaration]
  | .constructor e => #[e.declaration]
  | .finiteLimitCone e => #[e.declaration]
  | .coherence e => #[e.declaration]
  | .theoremInclusion e => #[e.declaration]
  | .alias e => #[e.declaration]
  | .opaque e => #[e.declaration] ++ e.ports.map (·.declaration)
  | .presentation e => #[e.declaration]

structure RegistryState where
  categories : Array NamedCategoryEntry := #[]
  categoryFamilies : Array CategoryFamilyEntry := #[]
  classifiers : Array ClassifierEntry := #[]
  functors : Array FunctorEntry := #[]
  constructors : Array ConstructorEntry := #[]
  finiteLimitCones : Array FiniteLimitConeEntry := #[]
  coherences : Array CoherenceEntry := #[]
  theoremInclusions : Array TheoremInclusionEntry := #[]
  aliases : Array AliasEntry := #[]
  opaqueCategories : Array OpaqueCategoryEntry := #[]
  presentations : Array PresentationEntry := #[]
  deriving Inhabited

/-- Registered functor lookup by stable ID. -/
def RegistryState.functor? (state : RegistryState) (id : FunctorId) : Option FunctorEntry :=
  state.functors.find? fun entry => entry.id == id

/-- Typed opaque-port lookup by stable ID. -/
def RegistryState.opaquePort? (state : RegistryState) (id : OpaquePortId) : Option StructuralPortEntry :=
  state.opaqueCategories.foldl (fun found category =>
    match found with
    | some _ => found
    | none => category.ports.find? fun port => port.id == id) none

/-- Theorem-backed inclusion lookup by stable ID. -/
def RegistryState.theoremInclusion? (state : RegistryState) (id : StructuralTheoremId) :
    Option TheoremInclusionEntry :=
  state.theoremInclusions.find? fun entry => entry.id == id

/-- Finite-limit cone lookup by stable ID. -/
def RegistryState.finiteLimitCone? (state : RegistryState) (id : ConeCertificateId) :
    Option FiniteLimitConeEntry :=
  state.finiteLimitCones.find? fun entry => entry.id == id

/-- Constructor lookup by stable ID. -/
def RegistryState.constructor? (state : RegistryState) (id : ConstructorId) : Option ConstructorEntry :=
  state.constructors.find? fun entry => entry.id == id

/-- Whether two symbolic category endpoints are syntactically identical. -/
def sameEndpoint (left right : CategoryExpr) : Bool :=
  left.syntacticEq right

/-- Whether an expression denotes the stable category ID of an opaque port endpoint. -/
def denotesCategory (expression : CategoryExpr) (id : CategoryId) : Bool :=
  match expression with
  | .atom value | .opaque value | .reference value => value == id
  | _ => false

/-- Validate references within a typed functor expression against prior persistent entries. -/
partial def FunctorExpr.referencesValid (state : RegistryState)
    {source target : CategoryExpr} : FunctorExpr source target → Bool
  | .identity _ => true
  | .named id =>
      match state.functor? id with
      | some entry => sameEndpoint entry.source source && sameEndpoint entry.target target
      | none => false
  | .baseProjection _ | .classifierProjection _ => true
  | .opaquePort id =>
      match state.opaquePort? id with
      | some entry => denotesCategory source entry.source && denotesCategory target entry.target
      | none => false
  | .theoremInclusion id =>
      match state.theoremInclusion? id with
      | some entry => sameEndpoint entry.source source && sameEndpoint entry.target target
      | none => false
  | .finiteLimitLift id =>
      match state.finiteLimitCone? id with
      | some entry => sameEndpoint entry.source source && sameEndpoint entry.target target
      | none => false
  | .constructorMap id =>
      match state.constructor? id with
      | some entry => sameEndpoint entry.source source && sameEndpoint entry.target target
      | none => false
  | .compose first second => first.referencesValid state && second.referencesValid state

/-- Validate the cospan references of a pullback category before it is persisted. -/
partial def CategoryExpr.referencesValid (state : RegistryState) : CategoryExpr → Bool
  | .atom _ | .familyApp _ _ | .classifierTotal _ | .opaque _ | .reference _ => true
  | .refine base _ _ => base.referencesValid state
  | .constructor _ args => (args.map (·.referencesValid state)).all id
  | .pullback left right over =>
      match state.functor? left, state.functor? right with
      | some leftEntry, some rightEntry =>
          over.referencesValid state && sameEndpoint leftEntry.target over &&
            sameEndpoint rightEntry.target over
      | _, _ => false

def RegistryState.apply : RegistryState → RegistryEntry → RegistryState
  | s, .category e => { s with categories := s.categories.push e }
  | s, .categoryFamily e => { s with categoryFamilies := s.categoryFamilies.push e }
  | s, .classifier e => { s with classifiers := s.classifiers.push e }
  | s, .functor e => { s with functors := s.functors.push e }
  | s, .constructor e => { s with constructors := s.constructors.push e }
  | s, .finiteLimitCone e => { s with finiteLimitCones := s.finiteLimitCones.push e }
  | s, .coherence e => { s with coherences := s.coherences.push e }
  | s, .theoremInclusion e => { s with theoremInclusions := s.theoremInclusions.push e }
  | s, .alias e => { s with aliases := s.aliases.push e }
  | s, .opaque e => { s with opaqueCategories := s.opaqueCategories.push e }
  | s, .presentation e => { s with presentations := s.presentations.push e }

/-- Whether this entry's typed stable ID has already been registered. -/
def RegistryState.hasEntryId : RegistryState → RegistryEntry → Bool
  | state, .category e => state.categories.any (·.id == e.id)
  | state, .categoryFamily e => state.categoryFamilies.any (·.id == e.id)
  | state, .classifier e => state.classifiers.any (·.id == e.id)
  | state, .functor e => state.functors.any (·.id == e.id)
  | state, .constructor e => state.constructors.any (·.id == e.id)
  | state, .finiteLimitCone e => state.finiteLimitCones.any (·.id == e.id)
  | state, .coherence e => state.coherences.any (·.id == e.id)
  | state, .theoremInclusion e => state.theoremInclusions.any (·.id == e.id)
  | state, .alias e => state.aliases.any (·.id == e.id)
  | state, .opaque e => state.opaqueCategories.any (·.id == e.id)
  | state, .presentation e => state.presentations.any (·.id == e.id)

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
  match e with
  | .category entry =>
      if !entry.expression.referencesValid state then
        throwError "category entry {entry.id.raw} has an unresolved or ill-typed functor reference"
  | .functor entry =>
      if !entry.source.referencesValid state || !entry.target.referencesValid state ||
          !entry.expression.referencesValid state then
        throwError "functor entry {entry.id.raw} has an unresolved or ill-typed functor reference"
  | .constructor entry =>
      if !entry.source.referencesValid state || !entry.target.referencesValid state then
        throwError "constructor entry {entry.id.raw} has an unresolved category endpoint"
  | .finiteLimitCone entry =>
      if !entry.source.referencesValid state || !entry.target.referencesValid state ||
          !entry.apex.referencesValid state then
        throwError "finite-limit cone entry {entry.id.raw} has an unresolved category endpoint"
  | .theoremInclusion entry =>
      if !entry.source.referencesValid state || !entry.target.referencesValid state then
        throwError "theorem inclusion entry {entry.id.raw} has an unresolved category endpoint"
  | .coherence entry =>
      if (state.functor? entry.source).isNone || (state.functor? entry.target).isNone then
        throwError "coherence entry {entry.id.raw} refers to an unregistered functor"
  | _ => pure ()
  for declaration in e.declarations do
    if declaration.isAnonymous then
      throwError "registry entry {e.stableId} has no declaration name"
    if (env.find? declaration).isNone then
      throwError "registry entry {e.stableId} refers to unknown declaration {declaration}"
  modifyEnv (registryExt.addEntry · e)

/-- The result type of a declaration after exposing all of its parameters. -/
private def declarationResultType (declaration : Name) : MetaM Expr := do
  let info ← getConstInfo declaration
  forallTelescopeReducing info.type fun _ result => pure result

/-- Require a declaration to return an actual category object. -/
private def ensureCategoryDeclaration (declaration : Name) : MetaM Unit := do
  let result ← declarationResultType declaration
  unless result.isConstOf ``NormalizedCategoryGraph.ObjCat do
    throwError "registry declaration {declaration} must return ObjCat, but returns {result}"

/-- Require an optional category-realization declaration to have the typed witness form. -/
private def ensureCategoryRealization (realization : Name) : MetaM Unit := do
  let result ← declarationResultType realization
  unless result.isAppOfArity ``NormalizedCategoryGraph.CategoryRealization 5 do
    throwError
      "registry realization {realization} must return CategoryRealization ..., but returns {result}"

/-- Require a declaration to return a classifier after its parameters are supplied. -/
private def ensureClassifierDeclaration (declaration : Name) : MetaM Unit := do
  let result ← declarationResultType declaration
  unless result.isAppOfArity ``NormalizedCategoryGraph.Classifier 1 do
    throwError "registry declaration {declaration} must return Classifier _, but returns {result}"

/-- Require a declaration to elaborate to an actual functor between categories. -/
private def ensureFunctorDeclaration (declaration : Name) : MetaM Unit := do
  let result ← whnf (← declarationResultType declaration)
  unless result.isAppOfArity ``CategoryTheory.Functor 4 ||
      result.isAppOfArity ``CategoryTheory.Cat.Hom 2 do
    throwError
      "registry declaration {declaration} must return a categorical functor, but returns {result}"

/-- Inspect declaration types before atomically persisting a registry entry. -/
def validateRegistryEntryDeclaration (entry : RegistryEntry) : MetaM Unit := do
  match entry with
  | .category e => do
      ensureCategoryDeclaration e.declaration
      if let some realization := e.realization then
        ensureCategoryRealization realization
  | .categoryFamily e => do
      ensureCategoryDeclaration e.declaration
      ensureCategoryDeclaration e.fibreDeclaration
  | .classifier e => ensureClassifierDeclaration e.declaration
  | .functor e => ensureFunctorDeclaration e.declaration
  | .constructor e => ensureFunctorDeclaration e.declaration
  | .finiteLimitCone _ => pure ()
  | .coherence _ => pure ()
  | .theoremInclusion e => ensureFunctorDeclaration e.declaration
  | .alias _ => pure ()
  | .opaque e => do
      ensureCategoryDeclaration e.declaration
      for port in e.ports do
        ensureFunctorDeclaration port.declaration
  | .presentation _ => pure ()

/-- Validate the elaborated declaration and persist exactly one registry entry. -/
def addRegistryEntryChecked (entry : RegistryEntry) : MetaM Unit := do
  validateRegistryEntryDeclaration entry
  addRegistryEntry entry

/--
Atomically elaborate and register one authored registry declaration.

The command is deliberately entry-by-entry: an imported module contributes its own
declarations directly to the persistent environment extension instead of assembling a
second in-memory manifest and replaying it later.
-/
syntax (name := normalizedRegistryEntry) "normalized_registry " term : command

elab_rules : command
  | `(normalized_registry $entry) => do
      let command ← `(run_cmd
        liftTermElabM do
          addRegistryEntryChecked $entry)
      elabCommand command

/-- Materialize the registered state for a Lean-authored export. -/
def RegistryState.snapshot (state : RegistryState) (schemaVersion : String) : RegistrySnapshot where
  schemaVersion
  categories := state.categories
  categoryFamilies := state.categoryFamilies
  classifiers := state.classifiers
  functors := state.functors
  constructors := state.constructors
  finiteLimitCones := state.finiteLimitCones
  coherences := state.coherences
  theoremInclusions := state.theoremInclusions
  aliases := state.aliases
  opaqueCategories := state.opaqueCategories
  equivalences := #[]
  presentations := state.presentations

end NormalizedCategoryGraph
