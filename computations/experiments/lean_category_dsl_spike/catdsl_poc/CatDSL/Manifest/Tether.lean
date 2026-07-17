import CatDSL.Foundation
import Lean

/-!
# Tethers: checked ties between project notions and their Lean anchors

The alignment problem is not listing what we know (`ForMathlib/` is
known-missing by construction, prose markers are self-declared); it is
surfacing what we DON'T know:

  (A) which notions are **untethered** — tied to no Lean/Mathlib
      declaration at all; and
  (B) which notions are tethered **but diverge in convention** — silent
      local overrides.

Neither can be answered by grepping docstrings, because docstrings are
self-reports.  So the tie itself is a checked artifact:

    tether LocalName ~ AnchorName via WitnessName

elaborates only if all three names resolve and the witness's *type*
mentions both the local constant and the anchor — a connection theorem
(`index_toNat`-style, `rfl` for definitional wrappers) or a construction
(`CountableSetObj.encodable : Encodable X.set`).  The kind is computed,
never declared:

  * `exact`      — the witness is an equation whose two sides are headed by
                   the local and anchor constants directly: same convention.
  * `divergent`  — an equation, but a side is wrapped (e.g. `Cardinal.toNat`
                   around the local value): the wrapping IS the convention
                   divergence, machine-visible in the statement.
  * `structural` — a non-equation witness (a bundling construction between
                   a local structure and a Mathlib class).

(A) is then the **computed complement**: `untetheredIn` walks the
environment's declarations under given namespace roots and subtracts the
tethered set; `#tether_report` prints everything, and the test suite pins
the untethered list so a new unanchored notion reds until it is tethered or
consciously acknowledged.
-/

namespace CatDSL.Manifest

open Lean Meta Elab Command

inductive TetherKind
  | exact | divergent | structural
  deriving Inhabited, BEq, Repr

instance : ToString TetherKind where
  toString
    | .exact => "exact"
    | .divergent => "divergent"
    | .structural => "structural"

structure Tether where
  localDecl : Name
  anchor : Name
  witness : Name
  kind : TetherKind
  deriving Inhabited, BEq, Repr

private def insertTether (ts : Array Tether) (t : Tether) : Array Tether :=
  if ts.contains t then ts else ts.push t

initialize tetherExt :
    SimplePersistentEnvExtension Tether (Array Tether) ←
  registerSimplePersistentEnvExtension {
    name := `CatDSL.Manifest.tetherExt
    addEntryFn := insertTether
    addImportedFn := fun modules =>
      modules.foldl (init := #[]) fun ts entries =>
        entries.foldl (init := ts) insertTether
  }

/-- Every tether visible in this environment. -/
def tethers (env : Environment) : Array Tether :=
  tetherExt.getState env

/--
Classify a witness: an equation headed by local/anchor on its own sides is
an exact anchoring; an equation with a wrapped side records a convention
divergence; anything else is a structural bundling.
-/
def classifyWitness (localDecl anchor : Name) (witnessType : Expr) :
    MetaM TetherKind :=
  forallTelescopeReducing witnessType fun _ body => do
    if body.isAppOfArity ``Eq 3 then
      let args := body.getAppArgs
      let lhsHead := args[1]!.getAppFn
      let rhsHead := args[2]!.getAppFn
      let headed (e : Expr) (n : Name) : Bool := e.isConstOf n
      if (headed lhsHead localDecl && headed rhsHead anchor)
          || (headed lhsHead anchor && headed rhsHead localDecl) then
        return .exact
      else
        return .divergent
    else
      return .structural

/--
`tether Local ~ Anchor via Witness` — record a checked tie.  Rejects a
witness whose type does not mention both ends: a tether nobody could have
faked with prose.
-/
syntax (name := tetherCmd) "tether " ident " ~ " ident " via " ident : command

@[command_elab tetherCmd]
def elabTether : CommandElab := fun stx => do
  let localDecl ← liftTermElabM <|
    realizeGlobalConstNoOverloadWithInfo stx[1]
  let anchor ← liftTermElabM <|
    realizeGlobalConstNoOverloadWithInfo stx[3]
  let witness ← liftTermElabM <|
    realizeGlobalConstNoOverloadWithInfo stx[5]
  let env ← getEnv
  let some winfo := env.find? witness
    | throwError "witness '{witness}' not found"
  let used := winfo.type.getUsedConstants
  unless used.contains localDecl do
    throwError
      "witness '{witness}' does not mention '{localDecl}' in its type;\n\
       a tether must be witnessed, not asserted"
  unless used.contains anchor do
    throwError
      "witness '{witness}' does not mention the anchor '{anchor}' in its \
       type;\na tether must be witnessed, not asserted"
  let kind ← liftTermElabM <| classifyWitness localDecl anchor winfo.type
  modifyEnv fun env =>
    tetherExt.addEntry env { localDecl, anchor, witness, kind }
  logInfo m!"tether ({kind}): {localDecl} ~ {anchor} via {witness}"

/-- Auto-generated companions that are not notions in their own right. -/
private def generatedSuffixes : List String :=
  ["casesOn", "recOn", "rec", "below", "ibelow", "brecOn", "binductionOn",
   "noConfusion", "noConfusionType", "mk", "ofNat", "toCtorIdx", "ctorIdx"]

private def isGenerated (n : Name) : Bool :=
  match n with
  | .str _ s => generatedSuffixes.contains s || s.startsWith "proof_"
  | _ => true

/--
The computed complement: every declaration under `roots` that is a notion
(def / abbrev / structure / axiom — not a theorem, constructor, projection,
instance, or auto-generated companion) and is neither tethered nor itself a
tether witness.
-/
def untetheredIn (roots : Array Name) : MetaM (Array Name) := do
  let env ← getEnv
  let ts := tethers env
  let tethered : NameSet :=
    ts.foldl (init := {}) fun s t => s.insert t.localDecl
  let witnesses : NameSet :=
    ts.foldl (init := {}) fun s t => s.insert t.witness
  let mut out : Array Name := #[]
  for (n, info) in env.constants.toList do
    unless roots.any (·.isPrefixOf n) do continue
    if n.isInternalDetail || isGenerated n then continue
    match info with
    | .defnInfo _ | .inductInfo _ | .opaqueInfo _ | .axiomInfo _ => pure ()
    | _ => continue
    -- notation/macro plumbing, not notions
    if info.type.isConstOf ``Lean.ParserDescr
        || info.type.isConstOf ``Lean.TrailingParserDescr then continue
    if env.isProjectionFn n then continue
    if ← Meta.isInstance n then continue
    if tethered.contains n || witnesses.contains n then continue
    out := out.push n
  return out.qsort fun a b => a.toString < b.toString

/-- Print every tether by kind, then the untethered complement under the
given roots (defaults to `CatDSL.Categories` and the kernel vocabulary). -/
syntax (name := tetherReport) "#tether_report" : command

@[command_elab tetherReport]
def elabTetherReport : CommandElab := fun _ => do
  let env ← getEnv
  let ts := tethers env
  for kind in [TetherKind.exact, .divergent, .structural] do
    let group := ts.filter (·.kind == kind)
    logInfo m!"{kind} tethers ({group.size}):"
    for t in group do
      logInfo m!"  {t.localDecl} ~ {t.anchor}  via {t.witness}"
  let roots := #[`CatDSL.Categories]
  let un ← liftTermElabM <| untetheredIn roots
  logInfo m!"untethered under {roots} ({un.size}):"
  for n in un do
    logInfo m!"  {n}"

end CatDSL.Manifest
