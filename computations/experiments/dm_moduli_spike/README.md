# Deligne–Mumford moduli spike (`dm_moduli_spike`)

## Architecture (authoritative)

See [ARCHITECTURE.md](ARCHITECTURE.md).
Short form:

1. **Depend on** PR [#182](https://github.com/dzackgarza/research/pull/182) owned Sets / functor / Hom substrate.
   Do **not** grow a parallel category foundation inside this spike.

2. Target packages later: `sage-stable-graphs` (Γ + graphs) and `sage-dm-strata` (moduli, strata, clutching).
   Stay mathematically distinct **in-tree**; extract **only** after gates in ARCHITECTURE.md pass.

3. This worktree **does not yet contain** #182’s `sets/` package.
   Dependency is therefore **unwired** — blocker: #182 still DRAFT / not on this branch’s merge base.

## Mathematical contract (in-spike)

This package **implements** (partial, under remediation):

1. Theorem-backed geometric parents in Sage’s category/parent/element/Hom style for DM moduli of curves (stacks, compactifications, stratifications, quotient strata).

2. Concrete `M_gI` / `Mbar_gI` with constructor-established axioms (stamps, not analytic proofs).

3. Combinatorial **Γ_{g,n}** and `StableGraphs(g,I)` as the dual-graph indexing layer.

4. Symmetric Δ-complex of Γ (DM boundary identification only for `g=0`).

This package **does not claim**:

* Computational étale atlases or equation-level properness tests.

* A scheme-theoretic universal family over `\mathcal M_{g,n}`.

* Geometric nodal gluing beyond combinatorial dual graphs.

* That `X in DeligneMumfordStacks(k).Proper()` is a properness *proof* — membership is a constructor theorem stamp.

* Package extraction or independence from #182.

## Evidence status (extraction gates)

| Gate | Status | Evidence |
| --- | --- | --- |
| #182 substrate available here | **FAIL** | No `sage_lattice_category_spike/sets/` on this branch; #182 DRAFT |
| Composition laws on public Hom | **FAIL** | `compose` exists in `objects/gamma.py`; no identity/associativity tests found under `tests/` |
| Canonical transport (public API) | **PARTIAL** | `tests/core/test_contraction_transport.sage` proves private `_GraphRecord` / `_StableGraphContraction` transport; not yet a public Hom-only API |
| Specialization poset from Hom | **FAIL** | `specialization_poset()` uses `_elementary_contraction_data`, not Hom nonempty-ness |
| QuotientStack outside moduli | **PARTIAL** | `test_quotient_stack_outside_moduli` exists; needs strengthening |
| Extraction of either package | **FAIL** | Gates above incomplete |

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
| 4 | Geometric ontology + Γ oracles | `tests/core/test_geometric_ontology.sage`, `test_gamma_category.sage` |
| 5 | Rank vectors / diagnostics | acceptance fixtures |

Plan cards: `PLAN-dm-moduli-foundations` / `PLAN-dm-moduli-residual-gaps` (architecture updated to depend on #182).
