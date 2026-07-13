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
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from dm_moduli_spike import (
    spec, scheme_over, spec_complex, M_gn, StablePointedCurves, DualGraphType,
    DeligneMumfordStacks, Varieties, StratifiedStacks,
)

Z = spec(ZZ)
XS = M_gn(1, 1)  # universal stack, structure morphism to Spec(ZZ)
cXS = XS.compactification(by=StablePointedCurves(1, 1))
S_strat = cXS.boundary().stratify(by=DualGraphType())
P = S_strat.stratification_poset(order="specialization")
Gamma = S_strat.indexing_category()

# Base change / S-points (same data): pull back along S -> Spec(ZZ)
Q_base = scheme_over(QQ, base_ring=ZZ)
XS_Q = XS.base_change(Q_base)  # object in stacks/Sch(Spec QQ)

# Symbolic C = R[x]/(x^2+1)
C = spec_complex()
```

`DMCompactificationModel` remains as the **internal combinatorial enumerator** behind
`StratifiedStack`; prefer `M_gn` for user-facing semantics.

## Package layout

| Package | Role |
| --- | --- |
| `categories/` | Sage categories: `Stacks`, `Varieties`, `DeligneMumfordStacks`, `StratifiedStacks` |
| `moduli/` | `M_gn`, `DeligneMumfordModuliStack`, moduli problems, families, coarse schemes |
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
