# Architecture: common Sets substrate + two mathematical packages

Authoritative ruling (2026-07-16): do **not** finish PR #111 as a monolith ontology independent of the shared Sets/functor/Hom foundation.
Do **not** extract packages until the gates below have artifact proof.

## Dependency on PR #182

| Fact | Evidence |
| --- | --- |
| PR | [#182](https://github.com/dzackgarza/research/pull/182) `feat/owned-sets-foundation-complete` |
| State in this worktree | **Absent.** This branch has no `sage_lattice_category_spike/sets/` tree. |
| State upstream | OPEN **DRAFT**, `mergeable=MERGEABLE` (not merged to `main`). |
| Intended public substrate | Owned `Sets()` / `Finite`/`Countable`/`Infinite`/`Uncountable` axioms; `SetObject` / `SetMap` / `SetEquivalence`; standard Hom / End / Aut; functorial constructions; algebraic spine through magmas → modules. Location on #182: `computations/experiments/sage_lattice_category_spike/sets/` (+ `objects/functors.py`, `morphisms/homsets.py`, category axiom nodes). |
| Current dm dependence | **None wired.** `dm_moduli_spike` still owns a parallel lightweight `categories/foundation.ModuliCategory` tower and attaches parents to Sage `Homsets()` / `Sets()` directly. That parallel spine is **debt**, not the target foundation. |

### Integration plan (when #182 is on the merge base)

1. Consume #182’s Sets / Hom / functor APIs; delete duplicate category-root inventions in `dm_moduli_spike/categories/foundation.py` that restate ownership already claimed by #182.

2. Keep **mathematical** ownership of stacks / moduli / strata / Γ distinct — DM does not absorb lattice axioms, and #182 does not grow scheme/stack geometry.

3. Do not invent a third Sets/Hom stack beside #182.

Until #182 lands on the base used by this spike: **blocker** — wire against the best in-tree shared foundation only if it is already the #182 surface; otherwise document the missing import and keep fixing DM math in place without growing a competing substrate.

## Target packages (extract only after gates)

Still **in-tree** under `computations/experiments/dm_moduli_spike/` until gates pass.

### `sage-stable-graphs` (combinatorial)

Owns stable marked weighted graphs and the finite category Γ:

| Path | Role |
| --- | --- |
| `objects/records.py` | Private `_GraphRecord` |
| `objects/canonical.py` | Canonical labelling |
| `objects/contractions.py` | Private contraction witnesses |
| `objects/isomorphisms.py` | Labeled-record isomorphisms + transport |
| `objects/stable_graphs.py` | `StableGraphs` / `StableGraph` + typed V/H/E/L |
| `objects/gamma.py` | `StableGraphCategory`, Hom, morphisms |
| `objects/edge_orbits.py` | Elementary contraction data |
| `objects/delta_complex.py` | Symmetric Δ-complex |
| `tests/core/test_gamma_category.sage` | Γ oracles |
| `tests/core/test_contraction_transport.sage` | Canonical transport (private layer) |

### `sage-dm-strata` (geometric)

Owns moduli parents, stratifications, clutching, and geometric categories:

| Path | Role |
| --- | --- |
| `categories/` | Stacks / schemes / curves / stratified (must eventually sit on #182, not parallel Sets) |
| `geometry/` | Stacks, immersions, compactifications, stratifications, quotients |
| `moduli/` | Moduli problems + `M_gI` / `Mbar_gI` |
| `curves/` | Pointed curves / families |
| `tests/core/test_geometric_ontology.sage` | Geometric acceptance smoke |

## Extraction gates (non-negotiable)

### Gate G1 — stable-graph layer

Extract `sage-stable-graphs` **only after**:

1. **Morphism composition fully proved** — tests for identity laws and associativity of `StableGraphMorphism.compose` on public Hom elements (not only helper paths).

2. **Canonical transport fully proved** — transport of contractions along isomorphisms, with domain/codomain as public `StableGraph` / Hom morphisms (not APIs that require callers to hold `_GraphRecord`).

### Gate G2 — DM layer

Extract `sage-dm-strata` **only after**:

1. G1 package installs and is dependable.

2. DM spike **installs and tests independently** against that dependency (separate `pyproject`, QC green with only that combinatorial dep + #182 substrate).

**Neither gate is claimed complete.** See README “Evidence status”.

## Known structural failures (must remediate, not paper over)

1. Shell-like `Compactifications` / `Stratifications` parents.

2. Boolean / frozenset axiom geometry flags (`declared_axioms` stamps) — keep theorem-stamp honesty; do not fake proof.

3. Graph Hom objects storing / leaking `_GraphRecord`.

4. `specialization_poset()` computed from elementary contractions; docstring claims Hom-order thinification but covers are **not** enumerated from nonempty Hom-sets.

5. Unproved geometric axiom membership beyond constructor stamps.

6. Quotient-stack behavior insufficiently tested outside moduli examples.

## Forbidden until gates pass

- Speculative disk extraction of `sage-stable-graphs` / `sage-dm-strata` repositories or top-level packages.

- Building a second Sets/Hom category foundation inside this spike.

- Claiming extraction or “full ontology complete” without the gate artifacts above.
