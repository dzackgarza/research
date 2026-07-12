# Deligne-Mumford compactification spike

Combinatorial model of `\overline{\mathcal M}_{g,n}`: stable-graph stratification, poset structure, and symbolic stack *signatures* (not full quotient stacks).

## Type hierarchy (report §1)

| Type | Role |
| --- | --- |
| `StableGraph` | **Labeled** half-edge representative. Flags, edges, `contract()`. |
| `StableGraphType` | **Isomorphism class** / stratum index. Invariant operations only. |
| `StableGraphTypes(g, n)` | Sage parent of graph types (`StableCurveTypes` alias). |
| `StableGraphContraction` | Morphism between labeled graphs. |
| `ContractionOrbit` | Elementary contraction at the type level with orbit size. |
| `DMStratum` | Geometric stratum descriptor (distinct from its graph type). |
| `QuotientStackSignature` / `ClutchingDatum` | Symbolic metadata + `AutomorphismAction`; primary clutching vocabulary. |
| `FactorSlot` | Local special-point coordinates on each moduli factor (legs and node branches). |

Representative-level work flows through `graph_type.canonical_representative()`. Legacy aliases `StableCurveType` and `clutching_morphism()` remain available but are not primary vocabulary.

## Quick start

```python
sage: from dm_moduli_spike import DMCompactificationModel
sage: M = DMCompactificationModel(0, 4)
sage: gamma = M.graph_types().from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
sage: graph = gamma.canonical_representative()
sage: generic, contraction = graph.contract(graph.internal_edges()[0])
sage: M.stratum(gamma).open_stack_presentation().automorphism_action()
```

## Backends

* `backend="auto"` (default) — `admcycles.decorated_graph` when present, else `admcycles.list_strata`, else pure-sage reference.
* `backend="pure-sage"` — reference enumerator.
* `backend="admcycles-stable"` — `admcycles.list_strata` adapter.
* `backend="admcycles-decorated"` — `admcycles.decorated_graph` adapter.
* `verify_against="pure-sage"` — optional cross-check; not run by default.

Install git `admcycles` for decorated-graph support:

```bash
sage -pip install --force-reinstall git+https://gitlab.com/modulispaces/admcycles.git
```

Covers are always recovered by contraction on canonical representatives.

## Tests

Whole-poset regression (genus-zero split oracle, Young diagrams, Petersen graph) plus `tests/core/test_mathematical_invariants.sage` for the type split, immutability, automorphism actions, completeness, and backend independence.
