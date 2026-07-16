# Architecture: common Sets substrate + two mathematical packages

Authoritative ruling (2026-07-16, updated same day): PR [#182](https://github.com/dzackgarza/research/pull/182) is the **live** Sets / functor / Hom foundations vehicle (user fact: pointed at new foundations; supersedes any “frozen / to-be-dropped” posture).
Do **not** invent a parallel Sets/Hom stack inside this spike.
Do **not** extract `sage-stable-graphs` / `sage-dm-strata` until G1/G2 have artifact proof.

## Dependency on PR #182

| Fact | Evidence |
| --- | --- |
| PR | [#182](https://github.com/dzackgarza/research/pull/182) (branch family `feat/owned-sets-foundation*`, related `feat/category-foundations`) |
| Role | Owned algebraic category spine: `Sets()` axioms, set maps/homsets, Hom/End/Aut, actions, functorial constructions, magmas → modules. |
| State in this worktree (`cursor/dm-compactification-spike-0d2c`) | **Unwired.** No `sage_lattice_category_spike/sets/` tree on this branch’s merge base. |
| GitHub PR status (audit) | May show CLOSED/DRAFT while the foundations vehicle is still the dependency target — do not treat closure as permission to grow a competing substrate. |
| Current dm dependence | **None wired.** `dm_moduli_spike` still uses a lightweight `categories/foundation.ModuliCategory` tower and Sage `Homsets()` / `Sets()` directly. That parallel spine is **debt** to replace when #182’s surface is on the merge base — not a second foundation to expand. |

### Integration plan (when #182 surface is on the merge base)

1. Consume #182’s Sets / Hom / functor APIs; delete duplicate category-root inventions in `dm_moduli_spike/categories/foundation.py` that restate ownership already claimed by #182.

2. Keep **mathematical** ownership of stacks / moduli / strata / Γ distinct — DM does not absorb lattice axioms, and #182 does not grow scheme/stack geometry.

3. Do not invent a third Sets/Hom stack beside #182.

Until #182’s substrate is present here: keep fixing DM ontology **in place** without growing a competing Sets/Hom layer; wire imports only against the #182 surface (or its successor branch content landed on the base), never a local reinvention.

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
| `objects/edge_orbits.py` | Elementary contraction candidates |
| `objects/delta_complex.py` | Symmetric Δ-complex |
| `tests/core/test_gamma_category.sage` | Γ oracles |
| `tests/core/test_hom_composition.sage` | Public Hom composition + Hom-certified covers |
| `tests/core/test_contraction_transport.sage` | Canonical transport (private layer still present) |

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

3. Graph Hom morphisms still store private `_GraphRecord` internally (public `domain()`/`codomain()` return `StableGraph`).

4. ~~Uncertified specialization covers~~ — **remediated**: candidates from elementary one-edge contractions; each retained cover certified by `Hom(special, generic).cardinality() > 0`.

5. Unproved geometric axiom membership beyond constructor stamps.

6. Quotient-stack behavior insufficiently tested outside moduli examples.

7. #182 substrate not yet on this branch’s merge base (wiring blocked; do not invent a replacement).

## Forbidden until gates pass

- Speculative disk extraction of `sage-stable-graphs` / `sage-dm-strata` repositories or top-level packages.

- Building a second Sets/Hom category foundation inside this spike.

- Claiming extraction or “full ontology complete” without the gate artifacts above.
