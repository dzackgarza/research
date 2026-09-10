# Sterk's boundary complex, formalized

The target, fixed and not subject to renegotiation:

> The boundary complex of the Baily–Borel compactification of $\Omega_-/\Gamma$
> for the period space of degree-2 almost polarized Enriques surfaces —
> equivalently $\Gamma\backslash\mathcal{T}(G)$ for
> $G = \mathrm{O}(L_-\otimes\mathbb{Q})$ — is the explicit finite bipartite graph
> with five vertices of one type, nine of the other, and the incidences of
> Sterk (3.4).

Source: H. Sterk, *Compactifications of the period space of Enriques surfaces*,
Chap. 2 (Zotero `Ste88a`/`Ste91`/`Ste95a`; see `../../computations/scripts/sterk-enriques-cusps/REFERENCES.md`).

**Where this prose and the Lean differ, the Lean is right.**

## Layout

Mirrors the Prove2Me workspace, which is the same mechanism the FLT artifact
uses: the statement is one file, the proof is another, and the statement file is
the authority.

```
Definitions/Def_<name>.lean     one definition, one citation with a locator
Theorems/Thm_<slug>.lean        one statement; body `by sorry` until proved
Solutions/Sol_<slug>.lean       `theorem solution`, discharging the statement
verification/                   the axiom check and the challenge statement
```

A solution file's `import Theorems.Thm_…` lines are exactly the theorems it
cites, so the dependency edges are machine-extractable and cannot drift from the
graph.

These files are authored here, under version control, and symlinked into
`../prove2me_workspace` for building — the workspace is a submodule tracking
someone else's repository and nothing authored may live only there.

## The graph

The dependency graph is `../../computations/scripts/sterk-enriques-cusps/DAG.md`:
strata A (arithmetic of $L_-$), B (isotropic sublattices), C (Vinberg and the
five diagrams), D (sublattices to boundary components), E (the geometric layer),
F (the foundations Mathlib lacks).  Every gap found between the target and
Mathlib adds nodes; the target never moves.

Node status, per node, lives in `PROOF-PATH.md`.

## Every node, before it is proved

1. Its statement is written with a citation carrying a locator (`FRM-02`).
2. Its statement is read back blind by an agent that did not write it, and
   audited against the five semantic-hallucination patterns (`FSV-04`, `FSV-05`).
3. Its strength is recorded in `PROOF-PATH.md` — a result stated in the
   restricted form the argument needs is recorded as such, and `LIMITATIONS.md`
   says it is not citable as the general theorem.
4. Only then is a proof attempted.

## Every node, after it is proved

`just check` runs `verification/check_axioms.sh`, which fails if any theorem
depends on an axiom outside `propext`, `Classical.choice`, `Quot.sound`, or if
any `sorry` appears outside a `Theorems/` statement file.

## What exists so far

Nothing is proved.  The mathematical content presently in hand is the
reconstruction of four of Sterk's five Coxeter diagrams
(`../../computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage`),
verified against the printed figures; the fifth, (3.3.12), disagrees and is
open.
