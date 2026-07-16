# Architecture: PR #225 foundation + DM geometry on #111

Authoritative ruling (2026-07-16, review of #111 vs #160/#225):

```text
PR #225  →  Cat, Sets, Hom, End, Aut, Actions, Subobjects, Quotients, CartesianProducts
PR #111  →  Stacks, curves, moduli, compactifications, strata, Γ  built on that foundation
```

- Issue [#160](https://github.com/dzackgarza/research/issues/160) / draft PR [#225](https://github.com/dzackgarza/research/pull/225) (`feat/category-foundations`) own the category kernel.

- PR [#182](https://github.com/dzackgarza/research/pull/182) is **obsolete** (closed unmerged); do not treat it as a live dependency.

- Do **not** invent a parallel Sets/Hom stack inside this spike.

- Do **not** extract `sage-stable-graphs` / `sage-dm-strata` until G1/G2 have artifact proof.

## Dependency on PR #225

| Fact | Evidence |
| --- | --- |
| PR | [#225](https://github.com/dzackgarza/research/pull/225) (branch `feat/category-foundations`) |
| Ledger | Issue [#160](https://github.com/dzackgarza/research/issues/160) |
| Role | Owned `Cat()`, `Sets()`, Hom/End/Aut, actions, construction categories |
| State | **OPEN draft**; CP3 (Hom/Actions/constructions) still landing |
| Current dm dependence | **Unwired.** Local `ModuliCategory` tower in `categories/foundation.py` is **debt pending Wave 2 rebase**, not a second foundation to expand. |

### Wave 1 — **INCOMPLETE** (reopened 2026-07-16; deepened 2026-07-16)

Independent DM math corrections that do not wait on #225. Status after deepen:

| Surface | Status |
| --- | --- |
| Equipped `ModuliStacks` (not ⊆ DM), curve hierarchy, stratified objects, coarse AlgebraicSpaces-first, Γ indexing, restrict | Landed |
| `atlas()` / `etale_atlas()` | **Deepened, still incomplete** — quotient atlases expose `(U, G)` presentation with domain = covering space; product étale atlas = product of factor étale atlases; coarse vs étale structurally distinguished; `AtlasEvidence` wires DM diagonal unramified+representable stamps; proving-set `FormallyEtaleSchemeCertificate` on identity `Spec(R)→Spec(R)`. Full equation-level étaleness on arbitrary atlases unfinished (Sage scheme morphisms lack `is_etale`) |
| `pullback` | **Deepened, still incomplete** — `BaseChangeStack.mediating_morphism(a, b)` returns `PullbackMediatingMorphism` with recorded legs; formal `π₁∘m` / `π₂∘m` recover legs (2-cell check). Full 2-categorical Hom-category UP waits on #225 |
| Aut(Γ) on product strata | **Deepened, still incomplete** — `AutProductStackAction` is a Sage `Action` subclass (`_act_` / overridden `act`); `QuotientStack` consumes action for covering autos / presentation uniqueness; equal-type 2-vertex swap hardened. #225 `Actions` category wiring unfinished |
| Wave 1 overall | **Incomplete** — remaining blockers that truly need #225: Hom-category composition laws, Actions category membership, Cat/Sets substrate. Local structural deepenings above are not wins for Wave 1 completion |

**Trap:** honesty demotion (`NotImplementedError`, identity morphisms, formal empty shells) is **not** remediation for PR #111 Wave 1.

### Wave 2 (after #225 merges) — **BLOCKED** until [#225](https://github.com/dzackgarza/research/pull/225) merges

Status (2026-07-16): #225 is still an **OPEN draft**; CP3 unfinished.
Do not rebase or delete the local foundation yet.

1. Rebase #111 onto the #225 merge commit.

2. Delete `categories/foundation.py`, local axiom/membership duplicates, local `Schemes` ownership, local Hom/Actions/product/quotient kernels.

3. Import landed `Cat` / `Sets` / `Hom` / `End` / `Aut` / `Actions` / construction categories.

4. Assert geometry categories are objects of `Cat()`; no second objects named Sets/Hom/Aut/Actions.

Until then: correct DM mathematics **in place** without growing the parallel kernel.

## Target packages (extract only after gates)

Still **in-tree** under `computations/experiments/dm_moduli_spike/` until gates pass.

### `sage-stable-graphs` (combinatorial)

Owns stable marked weighted graphs and Γ (`objects/`, Γ Hom tests).

### `sage-dm-strata` (geometric)

Owns moduli parents, stratifications, clutching, geometric categories (`categories/`, `geometry/`, `moduli/`, `curves/`).

## Extraction gates

### Gate G1 — stable-graph layer

1. Morphism composition proved on public Hom.

2. Canonical transport on public `StableGraph` / Hom APIs.

### Gate G2 — DM layer

1. G1 package installable.

2. DM installs/tests against that dep + #225 substrate.

**Neither gate claims package extraction complete.**

## Known structural debt

1. Local `ModuliCategory` foundation (Wave 2 delete).

2. Stack-as-pseudofunctor / fiber groupoids (Wave 3).

3. Γ as object of `Cat()` (Wave 3).

4. Shell-like Compactifications/Stratifications parents.

5. Hom morphisms store `_GraphRecord` internally.

6. Axiom membership = theorem stamps (honest; not analytic proof).

7. Atlas/pullback/Aut: structural deepenings landed (quotient presentation, product étale atlas, mediating UP, Sage `Action` subclass); equation-level étaleness on general atlases, full 2-cat Hom UP, and #225 Actions wiring remain (named gaps, not wins).

## Forbidden

- Parallel Sets/Hom category foundation.

- Speculative package extraction before G1/G2.

- Compatibility wrappers that preserve duplicate ownership.

- Claiming #225 wiring complete while substrate is unwired.

- Claiming Wave 1 complete while atlas / pullback / Aut-on-product are unfinished.

- Treating `NotImplementedError` / identity morphisms as remediation.
