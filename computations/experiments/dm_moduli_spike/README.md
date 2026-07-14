# Deligne–Mumford moduli spike (`dm_moduli_spike`)

## Mathematical contract

This package **implements**:

1. A **theorem-backed geometric ontology** in Sage’s category / parent / element / Hom framework: stacks, moduli stacks, coarse spaces, compactifications, boundaries, stratifications, product/quotient stacks, and curve/family types.
2. Concrete moduli objects `M_gI` / `Mbar_gI` (and `M_gn` / `Mbar_gn`) with constructor-established smooth/proper/dimension/coarse-space properties.
3. The finite combinatorial category **Γ_{g,n}** and `StableGraphs(g,I)` as the dual-graph indexing layer beneath geometric stratifications.
4. The symmetric Δ-complex of Γ (DM boundary identification only for `g=0`).

This package **does not claim**:

* Computational étale atlases or equation-level decision procedures for arbitrary stacks.
* A scheme-theoretic universal family over `\mathcal M_{g,n}`.
* Geometric nodal gluing beyond theorem-backed dual graphs (smooth proving-set fibers use Sage `Curve_generic`).

Formal morphisms (atlases, diagonals, clutching) carry correct domain/codomain and Hom-set membership.

## Organizing chain

```text
moduli problem → moduli stack → coarse space → compactification
  → boundary → stratification → Sage FinitePoset
```

with stable curves, dual graphs, quotient strata, and clutching as the `\overline{\mathcal M}_{g,n}` realization.

## Public entry

```python
from dm_moduli_spike import M_gn, Mbar_gn, DeligneMumfordStacks, ModuliStacks, spec

k = spec(QQ)
XS = M_gn(1, 1, base=k)
assert XS in ModuliStacks(k)
c = XS.compactification()
XSbar = c.codomain()
```

Combinatorial Γ remains available via `StableGraphCategory`.

## Evidence hierarchy

| Tier | Meaning | Location |
| --- | --- | --- |
| 1 | Literature oracles | `tests/literature/` |
| 2 | Independent checksums | literature docstrings |
| 3 | `admcycles` differential | `tests/core/test_backends.sage` |
| 4 | Geometric ontology + Γ oracles | `tests/core/test_geometric_ontology.sage`, `test_gamma_category.sage` |
| 5 | Rank vectors / diagnostics | acceptance fixtures |

Foundations plan: agent-memory geometric ontology / `PLAN-dm-moduli-foundations`.
