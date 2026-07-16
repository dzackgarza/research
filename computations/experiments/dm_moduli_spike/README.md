# Deligne–Mumford moduli spike (`dm_moduli_spike`)

## Architecture (authoritative)

See [ARCHITECTURE.md](ARCHITECTURE.md).
Short form:

1. **Depend on** issue [#160](https://github.com/dzackgarza/research/issues/160) / PR [#225](https://github.com/dzackgarza/research/pull/225) for `Cat`, `Sets`, Hom/End/Aut, Actions, and standard constructions.
   Do **not** grow a parallel category foundation inside this spike.
   PR [#182](https://github.com/dzackgarza/research/pull/182) is obsolete.

2. Target packages later: `sage-stable-graphs` (Γ + graphs) and `sage-dm-strata` (moduli, strata, clutching).
   Stay mathematically distinct **in-tree**; extract **only** after gates in ARCHITECTURE.md pass.

3. This worktree **does not yet wire** #225’s landed surface (draft; CP3 in progress).
   Local `ModuliCategory` is **debt pending rebase**, not permission to reinvent Sets/Hom.

## Wave 1 status — **incomplete**

Wave 1 is **not complete**. Prior “honesty demotions” (`NotImplementedError` for atlases, nameless/identity pullbacks, half-edge set action as Aut-on-product) were **defects**, not remediations.

| Item | Status |
| --- | --- |
| Category / curve / stratification ontology fixes | Landed |
| `atlas()` / `etale_atlas()` as `U → X` | **Incomplete** — structured morphisms exist (coarse / `AtlasChart`; not self); full étale verification unfinished |
| Structured `pullback` (`PullbackStack`/`BaseChangeStack`) | **Incomplete** — `base_morphism` / `projections` / UniqueRepresentation exist; 2-categorical coherence unfinished |
| Aut(Γ) action on product strata | **Incomplete** — `AutProductStackAction` wired; #225 `Actions` wiring unfinished |

## Mathematical contract (in-spike)

This package **implements** (partial; Wave 1 incomplete on atlas/pullback/Aut):

1. Theorem-backed geometric parents for DM moduli of curves (stacks, compactifications, stratifications, quotient strata).

2. Concrete `M_gI` / `Mbar_gI` with constructor-established axioms (stamps, not analytic proofs).

3. Combinatorial **Γ_{g,I}** and `StableGraphs(g,I)` as the dual-graph indexing layer.

4. Curve / family types including nodal stable pointed curves (not forced under smooth).

5. Symmetric Δ-complex of Γ (DM boundary identification only for `g=0`).

This package **does not claim**:

* Computational equation-level étale/properness tests (theorem stamps only).

* A scheme-theoretic universal family over `\mathcal M_{g,n}`.

* That `ModuliStacks` is a subcategory of `DeligneMumfordStacks`.

* Package extraction, completed wiring to #225, or completed Wave 1.

## Evidence status (extraction gates)

| Gate | Status |
| --- | --- |
| #225 substrate wired here | **FAIL** (await merge + Wave 2 rebase) |
| Composition laws on public Hom | **PASS** (`test_hom_composition.sage`) |
| Canonical transport (public API) | **PARTIAL** |
| Specialization poset Hom-certified | **PASS** |
| Extraction of either package | **FAIL** |
| Wave 1 complete (incl. full coherence) | **FAIL** (structured atlas/pullback/Aut landed; coherence gaps remain) |

## Public entry

```python
from dm_moduli_spike import M_gn, Mbar_gn, DeligneMumfordStacks, ModuliStacks, spec

k = spec(QQ)
XS = M_gn(1, 1, base=k)
assert XS in ModuliStacks(k)
assert XS in DeligneMumfordStacks(k)
assert not ModuliStacks(k).is_subcategory(DeligneMumfordStacks(k))
```

## Evidence hierarchy

| Tier | Meaning | Location |
| --- | --- | --- |
| 1 | Literature oracles | `tests/literature/` |
| 2 | Independent checksums | literature docstrings |
| 3 | `admcycles` differential | `tests/core/test_admcycles_boundary.sage` |
| 4 | Geometric ontology + Γ | `tests/core/test_geometric_ontology.sage`, `test_gamma_category.sage`, `test_hom_composition.sage` |

Plan cards: `PLAN-dm-moduli-foundations` / `PLAN-dm-moduli-residual-gaps`.
