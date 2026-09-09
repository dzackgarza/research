# Mechanisms to adopt, not norms to re-derive

Taken from `anthropics/fermats-last-theorem` — the released artifact of the
11-day run — rather than from descriptions of it.  Each item is a concrete
device that solved a problem the run hit, and each is cheap to adopt here.  The
point is that these are *enforced*, not agreed to: a norm ("check that the proof
matches the statement") is worth nothing, and `#p2m_type_eq` is worth
everything.

## 1. The statement is a separate file, and the proof discharges it

`Theorems/Thm_fermat_last_theorem.lean`, in full but for the long attribute
line:

```lean
import Mathlib.NumberTheory.FLT.Basic
import P2M.Util
import P2M.Sol.S_fermat_last_theorem
attribute [-instance] instDecEqAlgebraicClosureRat …   -- ~50 instances switched off

theorem fermat_last_theorem (n : ℕ) (hn : 3 ≤ n) (a b c : ℕ)
    (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) : a ^ n + b ^ n ≠ c ^ n := by
  p2m_exact_reverting @_root_.P2MW.S_fermat_last_theorem.solution
```

and the solution lives in `P2M/Sol/S_fermat_last_theorem.lean` as
`theorem solution` in its own namespace, under

```lean
set_option autoImplicit false
set_option maxHeartbeats 800000
set_option synthInstance.maxHeartbeats 80000
```

The statement file is the authority; the solution file cannot alter it.  This is
the mechanized form of the definition/theorem boundary that `FRM-01` states as a
rule — here the rule is a file layout that makes the violation impossible rather
than merely forbidden.

**The import list is the citation list.** From `PROOF-PATH.md`: a theorem `X.y`
is stated in `Theorems/Thm_X_y.lean` and proved in `P2M/Sol/S_X_y.lean`, "whose
`import Theorems.Thm_…` lines are exactly the theorems it cites".  Dependency
edges are therefore machine-extractable and cannot drift from the prose.

## 2. `p2m_exact_reverting`: the proof must close the *stated* goal

```lean
elab "p2m_exact_reverting " e:term : tactic => do
  let g ← getMainGoal
  … revert every non-implementation-detail hypothesis, preserving order …
  let v ← Term.withSynthesize <| elabTermEnsuringType e tgt
  let v ← instantiateMVars v
  if v.hasExprMVar then throwError "p2m_exact_reverting: unassigned metavariables remain"
  g'.assign v
```

Everything is reverted, the candidate term is elaborated against the *whole*
stated goal, and leftover metavariables are refused.  A proof of something
adjacent — with an extra hypothesis, a specialised instance, a partially
instantiated statement — does not typecheck.

## 3. `#p2m_type_eq`: and it must not be less general than the card

```lean
elab "#p2m_type_eq " a:ident b:ident : command => …
  if ← isDefEq ta tb then
    … if any of the statement's universe parameters had to be specialised …
      throwError m!"P2M_UNDERGENERAL: the statement's universes {pinned} had to be
                    specialised to match the proof — the proof is less general than the card"
    else logInfo m!"P2M_TYPE_EQ {a} {b}"
  else throwError m!"P2M_TYPE_MISMATCH\n  {a} : {ta}\n  {b} : {tb}"
```

`P2M_UNDERGENERAL` is a named, mechanized error for **proving something weaker
than the stated goal** — the failure mode this repository committed by hand.
It is caught at elaboration, by the checker, with a diagnostic naming which
universe parameters had to be pinned.

## 4. Environment freezing, so a card compiles the same in isolation

`attribute [-instance] …` lists switched off per file, `p2m_ns` / `p2m_open` /
`p2m_export_all` for controlled namespace opening, explicit `maxHeartbeats` and
`synthInstance.maxHeartbeats`, and `autoImplicit false`.  This is what lets
thousands of cards be proved concurrently by agents that never see one another's
files.

Its price is published: 31% of the released bytes are these generated preambles,
11,700 files set their own heartbeat limits, and one toolchain bump changed 26%
of proof files with 19% needing individual repair.  Worth paying at 30,000 cards
concurrently; probably not worth paying at a few hundred, where the same
determinism can come from a shared, small, pinned preamble.

## 5. The axiom guard is a build target

`FinalCheck.lean`, the default build target:

```lean
/-- info: 'fermat_last_theorem' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms fermat_last_theorem
```

"so the build fails unless the proof rests on exactly Lean's three standard
axioms (no `sorry`, no added `axiom`, no `native_decide`)".  It also derives
Mathlib's own `FermatLastTheorem` from the proved statement.

Two mechanisms in four lines: the axiom set is checked by CI rather than
asserted in prose, and the result is tied back to an independently-written
statement of the same theorem.

## 6. An independently-written challenge statement

`verification/comparator/Challenge.lean` states the theorem using only Mathlib;
`leanprover/comparator` confirms that the proved statement and every constant it
mentions are identical to the challenge, that no other axiom is used, and
replays the whole proof through the kernel.  `nanoda`, an independent Rust
reimplementation of Lean's kernel, then accepts every declaration.

The Navier–Stokes repository does the same and goes further: its challenge
statements are adapted from DeepMind's Formal Conjectures, so the people who
proved the theorem did not write the statement of it.

## 7. Documents that state the strength of what was proved

- **`PROOF-PATH.md`** — every step of the informal argument named, with the Lean
  theorem that carries it, and a closing section saying exactly what strength
  each named classical theorem was proved in.  It opens with a precedence rule:
  "Where this prose and the Lean differ, the Lean is right."
- **`docs/limitations.md`** — "Our 'Ribet', 'Wiles', 'Mazur' and
  'Langlands–Tunnell' are restricted versions"; none "should be cited as a
  formalisation of the general classical theorem".
- **`docs/verification.md`** — the tree "has not been refereed as mathematics".
- **`ATTRIBUTION.md`** — file by file, the 106 files adapted from the Imperial
  project and flt-regular, with upstream copyright holders reproduced.
- **`formalization.yaml`** (in the Navier–Stokes repo) — machine-readable
  `sorry_count`, `sorry_in_definitions`, and per-result `axioms`.

## What to adopt here, in order

1. The file layout with statements separate from proofs, and imports as the
   citation list — the Prove2Me workspace already has `Definitions/`,
   `Theorems/`, `Solutions/`, and its three gating rules (`theorem solution`;
   never import your own target; no `sorry` in your own file) are this mechanism
   in its platform form.
2. A `FinalCheck.lean` in the workspace from the first node, so the axiom set is
   a build failure rather than a claim.
3. A challenge statement for our target written against Mathlib alone, ideally
   by someone other than whoever writes the development.
4. `PROOF-PATH.md` and a limitations file from the first node, not at the end —
   the strength of each result is decided when it is stated, and Sterk's chapter
   is full of results we will state in restricted form.
5. A shared pinned preamble rather than per-file environment freezing, at our
   scale.
6. `#p2m_type_eq`-style checking if we ever generate statements and proofs in
   separate contexts.
