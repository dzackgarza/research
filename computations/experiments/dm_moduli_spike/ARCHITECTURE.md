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
| `atlas()` / `etale_atlas()` | **Deepened, still incomplete** — single owned-presentation registry (`moduli/atlas_ownership.py`: `owned_etale_atlas_presentations()` / `dispatch_etale_atlas` / `etale_atlas_gap_from_registry`). Every `ModuliStack.etale_atlas()` goes through that dispatch: owned row → equation-level domain, else fail-closed `AtlasChart` + structured `etale_atlas_gap()`. Default cardinality **9** (parametric open Knudsen `M_{0,n}` for all `n≥3`; parametric open Legendre/Hesse `M_{1,n}` for all `n≥1`; parametric compact Legendre/Hesse `Mbar_{1,n}` for all `n≥1` via `_legendre_compact_M1n_covering_space` / `_hesse_compact_M1n_covering_space` (`ℙ¹` for `n=1`); plus parametric proper Kapranov `Mbar_{0,n}` for `3≤n≤8` via `kapranov_iterated_blowup_P_{n-3}`, specializing to point / `ℙ¹` / `Bl₄(ℙ²)` / `Bl(ℙ³)` / lazy `Bl(ℙ⁴)` / lazy `Bl(ℙ⁵)`; plus open unmarked Igusa `M_{2,0}` via `igusa_binary_sextic_PGL2` / Rosenhain `Spec(R[λ,μ,ν]_S)` with finite étale `S₆ ≅ Sp₄(𝔽₂)` under `2∈Rˣ`; plus proper unmarked `Mbar_2` via `igusa_mbar06_s6` = Kapranov `Mbar_{0,6}` / `S₆` (same groupoid, discriminant-zero charts included); plus parametric open marked Rosenhain `M_{2,n}` (`n≥1`) via `_igusa_open_M2n_affine_scheme`). Expand `expand_open_m0n_through=8` + `expand_open_m1n_through=4` + `expand_compact_m1n_through=4` + `expand_proper_m0n_through=8` + `expand_open_m2n_through=4` → **34** concrete rows / **26** type keys. Fail-closed: `(1,*)` when neither `2` nor `3` is a unit (Weierstrass `𝔾_m` evidence for `n≤2`); proper marked `Mbar_{2,n}` (`genus_2_igusa_compact_marked_unavailable`); Igusa types without `2` unit (`igusa_requires_two_invertible`); `Mbar_{0,n}` for `n>8` with named gap `kapranov_iterated_blowup_P_{n-3}` — **no invented charts**. Remaining pre-#225 atlas debt is **general `(g,n)` beyond open Knudsen / level genus-1 / proper genus-0 through `n=8` / owned Igusa open `M_{2,n}` + unmarked `Mbar_2`**. Wave 2 still waits on [#225](https://github.com/dzackgarza/research/pull/225) merge. |
| `pullback` / `fiber_product` | **Deepened, still incomplete** — `BaseChangeStack` mediating UP; `FiberProductStack` (not nameless shell) with projections + mediating leg recovery. Full Hom-category UP waits on #225 |
| Aut(Γ) on product strata | **Deepened, still incomplete** — Sage `Action` subclass; `QuotientStack` consumes action; equal-type 2-vertex swap. #225 `Actions` category wiring unfinished |
| Wave 1 overall | **Incomplete** — #225-blocked: Hom-category UP, Actions category, Cat/Sets substrate. Pre-#225 atlas: general `(g,n)` only (`(1,*)` without units `2`/`3` is sharper fail-closed via owned Weierstrass `𝔾_m` evidence, not equation-level) |

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

7. Atlas/pullback/Aut/fiber-product: structural deepenings landed (quotient presentation, product étale atlas, `FiberProductStack`, mediating UP, Sage `Action`, proving-set étale certificates + finite étale groupoid flags, owned proving-set charts through the atlas-ownership registry, and owned Weierstrass `𝔾_m` fail-closed evidence when neither `2` nor `3` is a unit); equation-level étaleness on **general `(g,n)`** atlases (register new rows only with literature-backed constructions — no fake charts), full 2-cat Hom UP, and #225 Actions wiring remain (named gaps, not wins).
   Wave 2 rebase waits on #225 merge.

## Forbidden

- Parallel Sets/Hom category foundation.

- Speculative package extraction before G1/G2.

- Compatibility wrappers that preserve duplicate ownership.

- Claiming #225 wiring complete while substrate is unwired.

- Claiming Wave 1 complete while atlas / pullback / Aut-on-product are unfinished.

- Treating `NotImplementedError` / identity morphisms as remediation.
