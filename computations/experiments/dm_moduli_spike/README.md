# Deligne–Mumford moduli spike (`dm_moduli_spike`)

## Architecture (authoritative)

See [ARCHITECTURE.md](ARCHITECTURE.md).
Short form:

1. **Depend on** PR [#182](https://github.com/dzackgarza/research/pull/182) as the live Sets / functor / Hom foundations vehicle (pointed at new foundations; not “frozen/dropped”). Do **not** grow a parallel category foundation inside this spike.

2. Target packages later: `sage-stable-graphs` (Γ + graphs) and `sage-dm-strata` (moduli, strata, clutching).
   Stay mathematically distinct **in-tree**; extract **only** after gates in ARCHITECTURE.md pass.

3. This worktree **does not yet contain** #182’s `sets/` package on the merge base.
   Dependency is therefore **unwired** — blocker is absence of the substrate here, not permission to reinvent it.

## Mathematical contract (in-spike)

This package **implements** (partial, under remediation):

1. Theorem-backed geometric parents in Sage’s category/parent/element/Hom style for DM moduli of curves (stacks, compactifications, stratifications, quotient strata).

2. Concrete `M_gI` / `Mbar_gI` with constructor-established axioms (stamps, not analytic proofs).

3. Combinatorial **Γ_{g,n}** and `StableGraphs(g,I)` as the dual-graph indexing layer, with public `StableGraphContraction` Hom elements.

4. Curve / family types including `Curve`, `NormalizationMorphism`, and dual-graph methods on stable fibers.

5. Symmetric Δ-complex of Γ (DM boundary identification only for `g=0`).

This package **does not claim**:

* Computational étale atlases or equation-level properness tests.

* A scheme-theoretic universal family over `\mathcal M_{g,n}`.

* Geometric nodal gluing beyond combinatorial dual graphs.

* That `X in DeligneMumfordStacks(k).Proper()` is a properness *proof* — membership is a constructor theorem stamp.

* Package extraction or independence from #182.

## Evidence status (extraction gates)

| Gate | Status | Evidence |
| --- | --- | --- |
| #182 substrate available here | **FAIL** | No `sage_lattice_category_spike/sets/` on this branch; depend on #182 without inventing a parallel stack |
| Composition laws on public Hom | **PASS** | `tests/core/test_hom_composition.sage` (identity, associativity chain, transport square) |
| Canonical transport (public API) | **PARTIAL** | Hom identity transport square in `test_hom_composition.sage`; private `_GraphRecord` transport tests remain in `test_contraction_transport.sage` |
| Specialization poset Hom-certified | **PASS** | Elementary contraction candidates; each cover retained only if `Hom(special, generic)` nonempty (`objects/gamma.py`) |
| QuotientStack outside moduli | **PARTIAL** | `test_quotient_stack_outside_moduli` exists; needs strengthening |
| Extraction of either package | **FAIL** | G1/G2 incomplete; #182 unwired |

## Public entry

```python
from dm_moduli_spike import M_gn, Mbar_gn, DeligneMumfordStacks, ModuliStacks, spec

k = spec(QQ)
XS = M_gn(1, 1, base=k)
assert XS in ModuliStacks(k)
c = XS.compactification()
XSbar = c.codomain()
```

Combinatorial Γ: `StableGraphCategory`.

## Evidence hierarchy

| Tier | Meaning | Location |
| --- | --- | --- |
| 1 | Literature oracles | `tests/literature/` |
| 2 | Independent checksums | literature docstrings |
| 3 | `admcycles` differential | `tests/core/test_admcycles_boundary.sage` |
| 4 | Geometric ontology + Γ oracles | `tests/core/test_geometric_ontology.sage`, `test_gamma_category.sage`, `test_hom_composition.sage` |
| 5 | Rank vectors / diagnostics | acceptance fixtures |

Plan cards: `PLAN-dm-moduli-foundations` / `PLAN-dm-moduli-residual-gaps` (architecture: depend on live #182; no parallel Sets/Hom).
