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
| `atlas()` / `etale_atlas()` | **Deepened, still incomplete** — fail-closed `has_equation_level_etale_certificate()` (affine-cover + domain-matched ring certs; base Spec identity alone does not count; formal `AtlasChart` fail closed). Positive on: (i) `AffineAlgebraicSpace` covering + finite `G`; (ii) open proving-set moduli `M_{0,3}` (point), `M_{0,4}` (cross-ratio `Spec(R[λ]_{λ(λ-1)}) ≅ ℙ¹∖{0,1,∞}`), `M_{0,5}` (Knudsen configuration `Spec(R[λ,μ]_{λ(λ-1)μ(μ-1)(λ-μ)})`, `covering_kind=moduli_affine_etale_chart`), `M_{1,1}` with `2` invertible (Legendre `M(Γ(2))` finite étale cover of degree 6, `covering_kind=legendre_finite_etale_cover`, `S₃` groupoid stamps; **not** a scheme isomorphism) or with `2` not invertible and `3` invertible (Hesse `M(Γ(3))` chart `Spec(R[μ]_{μ³-1})`, degree `\|SL₂(𝔽₃)\|=24`, `covering_kind=hesse_finite_etale_cover`, including char 2), and open `M_{1,2}` under the same hypotheses (Legendre Weierstrass affine `Spec(R[λ,x,y]_{λ(λ-1)}/(y²-x(x-1)(x-λ)))` or Hesse affine `Spec(R[μ,x,y]_{μ³-1}/(x³+y³+1-3μxy))`, `covering_kind=legendre_universal_curve_finite_etale_cover` / `hesse_universal_curve_finite_etale_cover`); (iii) proper proving-set `Mbar_{0,3}` (point), `Mbar_{0,4}` (standard affine cover of `ℙ¹`, `covering_kind=moduli_scheme_affine_cover` — stack≅scheme, **not** the coarse map), `Mbar_{0,5}` (Kapranov `Bl₄(ℙ²)` at four points in general position; twelve successive-blowup `𝔸²` charts; `covering_kind=moduli_scheme_affine_cover` — stack≅scheme, **not** the coarse map), `Mbar_{1,1}` under the same Legendre / Hesse hypotheses (`Mbar(Γ(2))` or `Mbar(Γ(3)) ≅ ℙ¹`), and `Mbar_{1,2}` under the same hypotheses (compactified Legendre/Hesse universal-curve two-chart affine covers including nodal fibers; `covering_kind=legendre_compact_universal_curve_finite_etale_cover` / `hesse_compact_universal_curve_finite_etale_cover`). Fail-closed with inspectable `etale_atlas_gap()`: `(1,*)` when neither `2` nor `3` is a unit (prototype `Spec(ℤ)`; never on fields) owns Weierstrass `𝔾_m` via `weierstrass_gm_presentation()` as **owned_not_finite_etale** evidence (infinite group ⇒ smooth Artin cover, not finite étale equation-level; Igusa ordinary-only incomplete); remaining pre-#225 atlas debt is **general `(g,n)` only**. Proving-set certs: identity, `D(f)`, separable finite étale. **Still open:** owned affine étale presentations for general `(g,n)` |
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

7. Atlas/pullback/Aut/fiber-product: structural deepenings landed (quotient presentation, product étale atlas, `FiberProductStack`, mediating UP, Sage `Action`, proving-set étale certificates + finite étale groupoid flags, owned proving-set charts through `Mbar_{0,5}` Kapranov / Legendre–Hesse `(1,*)`, and owned Weierstrass `𝔾_m` fail-closed evidence when neither `2` nor `3` is a unit); equation-level étaleness on **general `(g,n)`** atlases, full 2-cat Hom UP, and #225 Actions wiring remain (named gaps, not wins).

## Forbidden

- Parallel Sets/Hom category foundation.

- Speculative package extraction before G1/G2.

- Compatibility wrappers that preserve duplicate ownership.

- Claiming #225 wiring complete while substrate is unwired.

- Claiming Wave 1 complete while atlas / pullback / Aut-on-product are unfinished.

- Treating `NotImplementedError` / identity morphisms as remediation.
