# Lattice Feature Spike (the fork)

The **separate spike carrying the genuinely new mathematics** — things not in Sage
in any meaningful way yet, but that should be. It is the fork of the base parity
spike, per the ruling
[spike-scope-is-sage-parity-only-new-mathematics-forks-into-a-separate-spike].

This spike **imports** the base spike
(`computations/experiments/sage_lattice_category_spike/`) — "call the spike an
import for all future work." The base is the drop-in Sage replacement / parity
substrate; this package supplies engines and vocabulary that go **beyond** what
Sage can compute.

## Scope (the FORK bucket)

New mathematics only. Each item is a demand recorded in the gap ledger, **not** a
build license — see gating below.

- **Nikulin primitive embeddings** — existence / construction / uniqueness
  (Nikulin 1.12.2 / 1.12.3 / 1.14.4). No Sage analogue. Core Enriques-moduli
  demand. Second oracle: Oscar `primitive_embeddings` via the rack sage-julia
  bridge (`dzack@rack:~/sage-julia-bridge`). Cite Nik80 (Zotero `TTY9FFJS`,
  extraction `D7BP5F7Z`); verify against the paper, not memory.
- **Base-ring generalization Sage cannot do** — `Lattices(R)` over `ZZ_p` / `QQ_p`,
  general Dedekind `K`/`R`; base-change functors `Lattices(R) -> Lattices(S)`;
  pro/ind completion axioms. (Base rings Sage *does* support — `GF(p)`,
  `Integers(n)`, polynomial/fraction fields — are parity and live in the BASE
  spike, not here.)
- **Hyperbolic engines** (Weyl group, fundamental chamber, reflectivity, Vinberg).
  Branch-off: graduates into its **own** workstream plan with its own tree; the
  base spike keeps only the declared vocabulary stable.
- **Dual / functional machinery** — first-class `L^# -> L^*` module morphism,
  `as_homspace` / `as_functional`; metric-dual vs monoidal-dual reconciliation
  across base rings. Deferred unless it falls out naturally. Ground in Peters &
  Sterk 2024 (Zotero `TWBY2QDS`, extraction `PS24_extracted.md`).

**Explicitly NOT here** (reassigned to the BASE spike by the 2026-07-04 directive
"all follow-up plans confined to the spike instead of the fork"): the Dutour
Sikirić `INDEF_FORM` placement/equivalence adapter and other G1-adjacent
indefinite-isometry engines. Those land in the base spike codebase.

## Gating — no autonomous builds

Every engine here obeys the gap-ledger rule
[lattice-spike-gap-ledger-novel-work-requiring-human-oversight]:

1. an **interactive session** with the user (never an autonomous agent);
2. a **literature-backed correctness argument** (cited Zotero source,
   human-reviewed), not a theorem recalled from training data;
3. its **own test design reviewed by the user** (expected values from cited
   sources or an independent oracle, never from agent memory);
4. an explicit user **go**.

**Freeze precondition:** fork engines are built only after the base spike is
frozen externally, tested in real human research work, and clearly correct and at
parity. This directory and its roadmap may be provisioned before that gate; the
engines may not.

## Boundaries

- **Research package.** The root `dzack_research.feature` import exposes this fork
  for general research use. Its engines remain subject to the gates above.
- Nothing here migrates into the broader `projects/lattice-research` program
  implicitly.

## Layout

```
sage_lattice_feature_spike/
  __init__.py        imports the base spike as `base` (the defining property)
  pyproject.toml     workspace-member package metadata
  conftest.py        brings base + its sage_patches live for every test run
  justfile           `just test` -> sage -python -m pytest over tests/ (mirrors the base spike)
  tests/             one module per FORK milestone lands here as its session ships an engine:
                       test_import_wiring.py  scaffold guard (base import + a live <2> construction)
                       test_embeddings.py     (M1, when it opens)
                       test_base_rings.py     (M2)
                       test_hyperbolic.py     (M3)
                       test_duals.py          (M4)
```

Engine modules (embeddings / base-ring / hyperbolic / duals) are NOT stubbed
ahead of their sessions — the gating forbids autonomous builds, and empty
placeholders trip the repo hygiene sweep. Each milestone's module and test land
together when its interactive session runs.

## Roadmap plan

`agent-memory` plan `PLAN-lattice-feature-spike` (project
`github.com__dzackgarza__research`). Each FORK-bucket milestone spawns its own
interactive child plan when its session comes.
