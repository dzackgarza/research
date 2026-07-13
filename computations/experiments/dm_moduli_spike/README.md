# Deligne-Mumford moduli landscape spike

Combinatorial and categorical model of `\overline{\mathcal M}_{g,n}` organized from
**general geometric objects downward**. Stable graphs index one boundary stratification;
they are not the ambient ontology.

## Semantic hierarchy (top → bottom)

```text
Schemes / AlgebraicSpaces / Varieties
        ↓
Stacks / DeligneMumfordStacks
        ↓
\mathcal M_{g,n}  --compactification-->  \overline{\mathcal M}_{g,n}
        ↓ coarse                          ↓ coarse
M_{g,n}  --------------------------->  \overline M_{g,n}
        ↓ boundary of compactification
StratifiedStacks  --stratify(by=DualGraphType())-->
        ↓ indexing_category()
StableGraphTypes(g,n)   --thinification-->   FinitePoset
```

## Public entry point

```python
from dm_moduli_spike import (
    ComplexNumbers, M_gn, StablePointedCurves, DualGraphType,
    DeligneMumfordStacks, Varieties, StratifiedStacks,
)

C = ComplexNumbers()
XS = M_gn(1, 1, base=C)
cXS = XS.compactification(by=StablePointedCurves(1, 1))
XSbar = cXS.codomain()
S = cXS.boundary().stratify(by=DualGraphType())
P = S.stratification_poset(order="specialization")  # Sage FinitePoset
Gamma = S.indexing_category()
```

`DMCompactificationModel` remains as the **internal combinatorial enumerator** behind
`StratifiedStack`; prefer `M_gn` for user-facing semantics.

## Package layout

| Package | Role |
| --- | --- |
| `categories/` | Sage categories: `Stacks`, `Varieties`, `DeligneMumfordStacks`, `StratifiedStacks` |
| `moduli/` | `M_gn`, `DeligneMumfordModuliStack`, moduli problems, families, coarse spaces |
| `geometry/` | `Compactification`, `OpenImmersion`, coarse moduli maps |
| `stratification/` | `StratifiedStack`, `DualGraphType`, boundary stratification |
| `curves/` | Pointed curve stubs with `dual_graph()` bridge |
| `objects/` | Half-edge stable graphs, enumeration, oracles (combinatorial backend) |

## Type hierarchy (combinatorial backend)

| Type | Role |
| --- | --- |
| `StableGraph` | Labeled half-edge representative |
| `StableGraphType` | Isomorphism class / stratum index |
| `StableGraphTypes(g, n)` | Parent; equals `DualGraphType().stable_graphs(g, n)` |
| `DMStratum` | Formal graph-indexed stratum descriptor (not a geometric stack) |

## Tests and evidence hierarchy

| Tier | Meaning | Location |
| --- | --- | --- |
| 1 | Exact independent literature oracle | `tests/literature/` |
| 2 | Independently implemented mathematical oracle (e.g. Young checksum) | literature docstrings |
| 3 | CAS differential comparison (`admcycles`) | `tests/core/test_backends.sage`, `tests/core/test_admcycles_orbit_comparison.sage` |
| 4 | Internal consistency (landscape API, Hasse=contraction, serialization) | `tests/core/` |
| 5 | Rank vectors / cardinalities (diagnostics only) | `tests/core/test_acceptance_fixtures.sage` |

**Do not** compare higher-genus (`g>0`) thin-poset order complexes to published tropical homology:
quotient/self-gluing data from `\operatorname{Aut}(\Gamma)` is required and is absent from the thin type poset.

Commit gate: `just test` (fast pytest, excludes `@pytest.mark.ci`). Push gate: `just test-ci` (full oracle suite).
