# Coxeter working trees — provenance records

Thirteen documents, landed 2026-08-20 from `~/gitclones/Coxeter` and
`~/gitclones/Coxeter-v2` under `PLAN-coxeter-deletion-audit-registry`
(readers P2, V2). They are the maps of those two trees, kept so that the
routing decisions of the migration stay checkable after the trees are gone.

Nothing here states a fact about this repository. Read a claim in these files
as a claim about the source tree at the time it was written.

## What the two trees were

**`Coxeter` (v1)** — a research environment plus an implementation
environment, aimed at classifying maximal parabolic subdiagrams of hyperbolic
Coxeter diagrams. Its `implementation/` half held a docstring-first TDD corpus
(now maintained at `tests/coxeter_tdd_specs/`), its `research/` half the
theory prose (now `notes/topics/coxeter-reflection-groups/`), and its
`planning/` half the category-tree design (now
`notes/category-design/bilinear-module-tower/`).

**`Coxeter-v2`** — a consolidation pass over v1 plus its own source archives.
Its method was to route each notion from a legacy file into one of six
"authority documents". `coxeter-v2-MASTER_INVENTORY.md` is the record of that
routing, notion by notion, and is the single most useful file here: it is the
only place that says which legacy file each authority claim came from.

## Contents

| File | Origin | What it maps |
|---|---|---|
| `coxeter-v1-README.md` | `Coxeter/README.md` | The v1 tree as a whole: research vs implementation environments, mission. |
| `coxeter-v1-implementation-README.md` | `Coxeter/implementation/README.md` | The TDD environment: agent roles, the anti-gaming measures on the test corpus, pointers into the category design. |
| `coxeter-v1-research-README.md` | `Coxeter/research/README.md` | The research environment: foundations, explorations, literature. |
| `coxeter-v1-planning-MIGRATION_CHECKLIST.md` | `Coxeter/implementation/planning/MIGRATION_CHECKLIST.md` | Index of the `modules_bak` planning scheme (`RMod` / `BilRMod` / `SymmetricBilRMod`). |
| `coxeter-v1-tmp-restore-README.md`, `-docs-README.md`, `-research-README.md` | `Coxeter/tmp_restore/**` | The recovered earlier generation of the same three maps. |
| `coxeter-v1-content-audit.md` | `Coxeter/tmp_restore/content-audit.md` | A per-file audit of what that generation held. |
| `coxeter-v1-detailed-architecture-plan.md` | `Coxeter/tmp_restore/detailed-architecture-plan.md` | The v1 architecture plan in full. |
| `coxeter-v2-MASTER_INVENTORY.md` | `Coxeter-v2/MASTER_INVENTORY.md` | The consolidation routing map, legacy file → authority document, notion by notion. `Coxeter-v2/file_list.md` was byte-identical to it; one copy landed. |
| `coxeter-v2-cold-storage-README.md` | `Coxeter-v2/archive/cold_storage_pre_integration/README.md` | The corpus map of the pre-integration archive: reading order and mission. |
| `coxeter-v2-CORE_ARCHITECTURE.md` | `Coxeter-v2/docs/authority/CORE_ARCHITECTURE.md` | The v2 category-tree design, including the skew-symmetric and alternating branches. Superseded by the preamble's tree; the divergence is legible only against it. |
| `coxeter-v2-CATEGORY_IMPLEMENTATION.md` | `Coxeter-v2/docs/authority/CATEGORY_IMPLEMENTATION.md` | The legacy→category translation rules, plus two live deltas noted below. |

## Where the mathematics of these trees went

- theory prose → `notes/topics/coxeter-reflection-groups/`
- category-tree design → `notes/category-design/bilinear-module-tower/`,
  `core-category-theory/`, `conventions/`, `chain-complexes/`,
  `prior-art-hott/`, `sage-gaps/`
- stable-homotopy program → `notes/homotopy-bilinear-modules/`
- algorithm surveys → `notes/computations/coxeter-algorithms/`
- test corpus, conventions, citations and literature oracles →
  `tests/coxeter_tdd_specs/`
- the mathematics itself → the preamble, chiefly
  `categories/modules/framed/formed/` and its `integrallattice/` subtree

## Two claims in `coxeter-v2-CATEGORY_IMPLEMENTATION.md` that are not yet owned

Recorded here because this file is their only statement:

- **height-bounded isotropic-vector enumeration** — enumerate the vectors
  $v$ with $q(v) = 0$ inside a bounded box, which is what a light-cone walk
  needs. The preamble's `enumerate_short_vectors` is positive-definite-only,
  so no owned method answers this for a Lorentzian lattice.
- **interlacing-pruned parabolic search** — use Cauchy interlacing to cut the
  subdiagram search: a non-elliptic subdiagram admits no elliptic
  superdiagram. `vinberg_invariants.sage` enumerates the posets without this
  pruning.

## Errors recorded

`coxeter-v2-CORE_ARCHITECTURE.md` §3 asserts that $D(\mathrm{Bil}\,R\text{-}\mathrm{Mod})$
exists with a $t$-structure whose heart is the abelian category
$\mathrm{Bil}\,R\text{-}\mathrm{Mod}$. With form-preserving morphisms the
hom-sets carry no addition, so the category is not additive, hence not
abelian, and neither $\mathrm{Ch}$ nor $D$ is defined as stated. The same
claim recurs in `Coxeter-v2/docs/authority/CATEGORICAL_FOUNDATIONS.md`, landed
at `notes/homotopy-bilinear-modules/program/coxeter-v2-categorical-foundations.md`,
whose INDEX states the obstruction in full.
