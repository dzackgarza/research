# Deligne–Mumford moduli spike (`dm_moduli_spike`)

## Mathematical contract

This package **implements**:

1. The finite category **Γ_{g,n}** of stable (n)-marked weighted dual graphs of genus g,
   with finite Hom-sets, identity morphisms, and composition (Chan–Galatius–Payne).
2. The **specialization poset** of graph strata — the thinification of Γ_{g,n} after
   passing to isomorphism classes — as a Sage `FinitePoset`.
3. **Formal graph-indexed stratum formulas** (clutching sources, codimension, automorphism
   actions) attached to stable graphs.

This package **does not implement**:

* The Deligne–Mumford stacks `\mathcal M_{g,n}`, `\overline{\mathcal M}_{g,n}` as
  algebraic stacks (no universal family, no stack structure).
* Coarse moduli schemes `M_{g,n}`, `\overline M_{g,n}` as schemes.
* Stable pointed curves, families `\pi:\mathcal C\to S`, or geometric specializations.

Notation (literature standard):

| Symbol | Meaning |
| --- | --- |
| `\mathcal M_{g,n}` | Fine moduli stack of smooth n-pointed genus-g curves |
| `\overline{\mathcal M}_{g,n}` | Deligne–Mumford compactification |
| `M_{g,n}`, `\overline M_{g,n}` | Coarse moduli **schemes** |
| `\mathcal M_G` | Stratum of curves with dual graph `G` |
| `Γ_{g,n}` | Finite category of stable dual graphs and contractions |

Vertex weights `w(v)` are **geometric genera** of the normalization components of the
corresponding irreducible pieces. The total graph genus is the **arithmetic genus**

```text
g(Γ) = b₁(Γ) + Σ_v w(v).
```

## Public entry point (combinatorial)

```python
from dm_moduli_spike import StableGraphCategory, StableGraphMorphism

Gamma = StableGraphCategory(1, 1)
G, H = Gamma.objects()[0], Gamma.objects()[1]
Hom = Gamma.hom(G, H)
P = Gamma.specialization_poset()   # Sage FinitePoset
```

## Private / legacy layers

| Layer | Status |
| --- | --- |
| `objects/gamma.py` | **Public center** — Γ_{g,n} |
| `objects/` (records, contractions, …) | Combinatorial kernel |
| `_landscape/` (`moduli`, `curves`, `geometry`, `stratification`) | **Private stubs** — typed placeholders, not geometry; not in `__all__` |
| `DMCompactificationModel` | **Being demoted** — enumerator behind stratification |

Literature oracle tests live in `tests/literature/` (tier 1). See evidence table below.

## Evidence hierarchy

| Tier | Meaning | Location |
| --- | --- | --- |
| 1 | Exact independent literature oracle | `tests/literature/` |
| 2 | Independent mathematical checksum | literature docstrings |
| 3 | CAS differential (`admcycles`) | `tests/core/test_backends.sage` |
| 4 | Internal consistency | `tests/core/` |
| 5 | Rank vectors / cardinalities (diagnostics) | `tests/core/test_acceptance_fixtures.sage` |

**Do not** compare `g>0` thin-poset order complexes to tropical homology without
automorphism quotient data. Use `SymmetricDeltaComplex.as_dm_boundary_complex()`
only for `g=0` — it raises for `g>0`.

Foundations remediation plan: agent-memory `PLAN-dm-moduli-foundations`.

Commit gate: `just test`. Push gate: `just test-ci`.
