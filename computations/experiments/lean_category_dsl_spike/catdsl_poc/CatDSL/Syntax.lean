import CatDSL.Registry
import CatDSL.Categories.Lattices

/-!
# Surface syntax

Only the forms the registry can actually back:

    let X ∈ 𝒞
    let X := t ∈ 𝒞
    prefer F
    #via X ∈ 𝒞

`|X|`, `number(X,x)`, and `nth[n](X)` are deliberately absent.  They require
*operation-implementation* resolution, which is a different search from the
membership resolution `resolvePath` performs — the shortest path to `Set`
need not pass through any implementation of cardinality.  Adding them as
textual macros over `resolvePath` would paper over that.

Division of labour:
  * macros            — context-free textual expansion (`let`)
  * command elaborators — declarations or registry state (`prefer`, `#via`)
  * term elaborators   — where the expected category changes meaning

## No trailing `.`

`GUIDING_PRINCIPLES.md` specifies a paper-like sentence terminator
(`let L := (𝔽₂², id) ∈ Lat(𝔽₂).`).  It is not implementable in Lean 4 as
written, so commands end at the newline instead.  `.` is field-projection
syntax and the lexer takes it greedily, differently by spacing:

  * `Lat(𝔽₂).`  — the `.` binds as a projection on the preceding term, then
    fails looking for a field name: "Invalid field notation: Identifier or
    numeral expected".
  * `Lat(𝔽₂) .` — the `.` is read as anonymous-constructor dot-notation, so
    the category is applied to it: "Function expected at Lattices 𝔽₂".

It also cannot be pattern-matched in a quotation at all.  Minimal repro:

    syntax "mycmd " ident " ∈ " term "." : command
    macro_rules | `(command| mycmd $n:ident ∈ $c:term .) => ...
    -- unexpected token ')'; expected '.'
    -- the same syntax WITHOUT the "." matches fine

Making it work needs a custom token or `checkNoWsBefore`-style guards at
every position a term may end — a frontend problem in its own right.

The rules below destructure `stx` positionally rather than quoting, which is
both what works today and the pattern that would survive reinstating a
terminator later.
-/

namespace CatDSL.DSL

open Lean Meta Elab Term Command
open CatDSL CatDSL.Registry

/-!
## `prefer F.`

A command elaborator, not a macro: it mutates registry state.
-/

syntax (name := dslPrefer) "prefer " ident : command

@[command_elab dslPrefer]
def elabPrefer : CommandElab := fun stx => do
  -- stx: "prefer " ident   -- positional; see "The trailing `.`" above
  let edge : Ident := ⟨stx[1]⟩
  let edgeName ← liftCoreM <| realizeGlobalConstNoOverloadWithInfo edge
  -- reject by TYPE, not by target: any genuine functor may be preferred.
  liftTermElabM <| Registry.checkPreferredFunctor edgeName
  liftCoreM <| Registry.addPreferredFunctor edgeName

/-!
## `#via X ∈ 𝒞.`

Reports the preferred path the resolver selects, and its constituent
functors.  Membership is existential reachability; the path is reported for
provenance, not because it is unique.
-/

syntax (name := dslVia) "#via " ident " ∈ " term : command

@[command_elab dslVia]
def elabVia : CommandElab := fun stx => do
  -- stx: "#via " ident " ∈ " term
  let x : Ident := ⟨stx[1]⟩
  let category : Term := ⟨stx[3]⟩
  let xName ← liftCoreM <| realizeGlobalConstNoOverloadWithInfo x
  liftTermElabM do
    let home ← Registry.objectHome xName
    let target ← instantiateMVars (← Term.elabTerm category none)
    let path ← Registry.resolvePath home target
    let names := Registry.pathNames path
    if names.isEmpty then
      logInfo m!"{xName} is already in {target}"
    else
      logInfo m!"{xName} is defined in {home}\n  ⇝ {target} via {names}"

/-!
## `#home X.`
-/

syntax (name := dslHome) "#home " ident : command

@[command_elab dslHome]
def elabHome : CommandElab := fun stx => do
  -- stx: "#home " ident
  let x : Ident := ⟨stx[1]⟩
  let xName ← liftCoreM <| realizeGlobalConstNoOverloadWithInfo x
  liftTermElabM do
    logInfo m!"{xName} is defined in {← Registry.objectHome xName}"

/-!
## Declarations

`let X := t ∈ 𝒞.` is context-free: all mathematical content is carried by
the ordinary Lean declaration it expands to.  The generated type is
`Object 𝒞`, whose head symbol is how `Registry.objectHome` later recovers
`𝒞` without a second table.

Two parser hazards, both of which the previous version tripped over:

* the value must be `term:51`.  `∈` is itself a term-level infix at
  precedence 50, so a bare `term` swallows `∈ 𝒞` and the rule never matches.
* this block is declared LAST in the file.  Registering a command whose
  leading token is `let` makes every subsequent `let x ← e` in a `do` block
  try to parse as this command ("unexpected token '←'; expected ':=' or
  '∈'"), so it must come after the elaborators.
-/

syntax (name := dslLetDef)
  "let " ident " := " term:51 " ∈ " term : command

syntax (name := dslLetAbstract)
  "let " ident " ∈ " term : command

@[command_elab dslLetDef]
def elabLetDef : CommandElab := fun stx => do
  -- stx: "let " ident " := " term:51 " ∈ " term
  let name : Ident := ⟨stx[1]⟩
  let value : Term := ⟨stx[3]⟩
  let category : Term := ⟨stx[5]⟩
  elabCommand (← `(command|
    noncomputable def $name : CatDSL.Object $category := $value))

@[command_elab dslLetAbstract]
def elabLetAbstract : CommandElab := fun stx => do
  -- stx: "let " ident " ∈ " term
  let name : Ident := ⟨stx[1]⟩
  let category : Term := ⟨stx[3]⟩
  elabCommand (← `(command| axiom $name : CatDSL.Object $category))


end CatDSL.DSL
