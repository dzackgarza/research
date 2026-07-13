# Deligne-Mumford compactification spike

Combinatorial model of `\overline{\mathcal M}_{g,n}`: stable-graph stratification, poset structure, and symbolic stack *signatures* (not full quotient stacks).

## Type hierarchy

| Type | Role |
| --- | --- |
| `StableGraph` | **Labeled** half-edge representative. Flags, edges, `contract()`. |
| `StableGraphType` | **Isomorphism class** / stratum index. Invariant operations only. |
| `StableGraphTypes(g, n)` | Sage parent of graph types. |
| `StableGraphContraction` | Morphism between labeled graphs; transport via explicit isomorphisms. |
| `StableGraphIsomorphism` | Certified bijection preserving genus, incidence, involution, markings. |
| `DMStratum` | Geometric stratum descriptor (distinct from its graph type). |
| `QuotientStackPresentation` / `ClutchingMorphism` | Symbolic gluing and quotient-stack metadata; half-edges are primary coordinates. |

Representative-level work flows through `graph_type.canonical_representative()`.

Covers at the type level are **distinct contraction targets** `[\Gamma/e]`, one per `Aut(\Gamma)` edge orbit.
Use `edge_orbits()`, `contract()`, and `covers()` — not a separate public orbit wrapper.

## Quick start

```python
sage: from dm_moduli_spike import DMCompactificationModel
sage: M = DMCompactificationModel(0, 4)
sage: gamma = M.graph_types().from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
sage: graph = gamma.canonical_representative()
sage: generic, contraction = graph.contract(graph.internal_edges()[0])
sage: M.stratum(gamma).open_stack_presentation().automorphism_action()
```

## Stratification completeness

* `is_full_stratification()` — complete through ambient dimension.
* `is_codimension_truncation()` — `max_codim=k` complete through `k` but not global.
* `is_induced_subposet()` — Hasse diagram of a supplied type family (covers may be multi-edge).
* `complete_through_codim()` — highest fully enumerated codimension level.

## Backends

* `backend="auto"` (default) — `admcycles.decorated_graph` when present, else `admcycles.list_strata`, else pure-sage reference.
* `backend="pure-sage"` — reference enumerator.
* `backend="admcycles-stable"` — `admcycles.list_strata` adapter; attests full-cap exhaustive enumeration when available.
* `backend="admcycles-decorated"` — `admcycles.decorated_graph` adapter; orbit comparison via edge-orbit representatives.
* `verify_against="pure-sage"` — optional cross-check; not run by default.

Install git `admcycles` for decorated-graph support:

```bash
sage -pip install --force-reinstall git+https://gitlab.com/modulispaces/admcycles.git
```

Covers are always recovered by contraction on canonical representatives.

## Notebook

[`notebooks/highlights.ipynb`](notebooks/highlights.ipynb) — research walkthrough with Hasse-diagram poset plots and weighted dual-graph drawings.

## Tests and evidence hierarchy

| Tier | Meaning | Location |
| --- | --- | --- |
| 1 | Exact independent literature oracle | `tests/literature/` |
| 2 | Independently implemented mathematical oracle (e.g. Young checksum) | literature docstrings |
| 3 | CAS differential comparison (`admcycles`) | `tests/core/test_backends.sage`, orbit comparison |
| 4 | Internal consistency (Hasse=contraction, serialization, relabeling) | `tests/core/` |
| 5 | Rank vectors / cardinalities (diagnostics only) | never primary claims |

Tier-1 oracles include:

* `\overline{\mathcal M}_{0,n}` compatible-split whole posets (`test_lit_M0n_poset_oracle.sage`, CI-tier);
* Arbarello-Cornalba boundary divisors and clutching (`test_lit_boundary_divisors.sage`);
* Markwig/Chan complete small posets (`test_lit_semantic_covers.sage`, `test_lit_moduli_strata.sage`);
* published automorphism edge actions and Chan's `\overline{\mathcal M}_{1,3}` example.

**Do not** compare higher-genus thin-poset order complexes to published tropical homology: quotient/self-gluing data from `\operatorname{Aut}(\Gamma)` is required and is absent from the thin type poset.

Commit gate: `just test` (fast pytest, excludes `@pytest.mark.ci`). Push gate: `just test-ci` (full oracle suite + slop/coverage stack).
