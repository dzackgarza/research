---
title: CoxIter results for the Sterk cusps and the Coble/Enriques 0-cusp lattices
unit: computation
status: computed
tags:
  - coxiter
  - coxeter-diagrams
  - cusps
  - hyperbolic-lattices
---

# CoxIter results for the Sterk cusps and the 0-cusp lattices

**Provenance.** `/home/dzack/gitclones/diss/100-corpus/100-data/dzg-research/computational-research/canonical/reports/Sterk{1..5}Output.txt` and `.../coxeter-diagrams/coxiter/`. None of this appears in the dissertation: the strings "CoxIter", "f-vector", "growth rate" and "cocompact" occur nowhere in `dissertation/sections/`.

CoxIter is Guglielmetti's implementation for invariants of hyperbolic Coxeter groups.
All runs below are on the folded Coxeter diagrams of the five Sterk cusps of $\fentwo$, and on three 0-cusp lattices named by their $(r,a,\delta)$ invariants.

## The five Sterk cusps

Every run reports dimension 9, **non-cocompact with finite covolume**, and Euler characteristic 0.

| Cusp | Vertices | Gram field | Vertices at $\infty$ | Signature line | $f$-vector |
| --- | --- | --- | --- | --- | --- |
| Sterk 1 | 12 | $\QQ$ | 9 | $9,1,2$ | $(23,114,288,462,504,378,192,63,12,1)$ |
| Sterk 2 | 10 | $\QQ[\sqrt2]$ | 2 | $9,1,0$ | $(10,45,120,210,252,210,120,45,10,1)$ |
| Sterk 3 | 12 | $\QQ[\sqrt2]$ | 4 | $9,1,2$ | $(33,164,398,602,616,434,208,65,12,1)$ |
| Sterk 4 | 11 | $\QQ[\sqrt2]$ | 5 | $9,1,1$ | $(26,125,300,450,460,330,165,55,11,1)$ |
| Sterk 5 | 14 | $\QQ[\sqrt2]$ | 13 | $9,1,4$ | $(115,600,1352,1768,1508,875,346,90,14,1)$ |

::: {.Remark}
### Growth rate of Sterk 1

The Sterk 1 growth rate is
$$
2.6246613781819533651112379994955986218 ,
$$
classified by CoxIter as **Perron, not Pisot, not Salem**. Each output also lists every connected spherical subgraph by rank with its vertex set, and every spherical *product* with multiplicity $N$ and Weyl group order; for example Sterk 1 at rank 9 records $A_1 \oplus E_8$ with $N = 4$ and order $1393459200$.
:::

::: {.Remark}
### Consistency with the dissertation

The dissertation records for these cusps only the ray counts of the semifans (Cusp 1: 4 Type II + 4 Type III; Cusp 2: 2 + 8; Cusp 3: 3 + 15), which is a different quantity from any entry above.
Nothing in the dissertation contradicts these numbers, and nothing in it reproduces them.
:::

## The 0-cusp lattices

| Lattice $(r,a,\delta)$ | Diagram | Field | Dim | Vertices at $\infty$ | $f$-vector | $\chi$ |
| --- | --- | --- | --- | --- | --- | --- |
| $(9,9,1)_1$ | rank-9 chain, one label-4 edge | $\QQ[\sqrt2]$ | 8 | 1 | $(9,36,84,126,126,84,36,9,1)$ | $17/1393459200$ |
| $(10,8,0)_1$ | rank-10 chain, one label-4 edge | $\QQ[\sqrt2]$ | 9 | 2 | $(10,45,120,210,252,210,120,45,10,1)$ | $0$ |
| $(10,10,0)_1$ | rank-10, all edges label 3, $\tilde E_{10}$-shaped | $\QQ$ | 9 | 1 | $(10,45,120,210,252,210,120,45,10,1)$ | $0$ |

::: {.Remark}
### Why (9,9,1) matters here

$(9,9,1)$ is the **Coble 0-cusp lattice** named in this project's own text, alongside the 1-cusp $(7,7,1)$.
$(10,10,0)$ and $(10,8,0)$ are the two Enriques 0-cusps to which the Coble cusps are claimed to map.
So this table is direct computational evidence bearing on the cusp correspondence; see [the cusp-correspondence morphism chain](../coble-moduli/cusp-correspondence-morphism-chain.md).
:::

::: {.Remark}
### Benchmarks, not results

The same directory holds CoxIter runs on $E_6$, $F_4$ and $F_2$ (the last: 24 vertices, dimension 19, $\chi = -219323026921/45201995813229523107840000$). These are standard reference diagrams used to check the tool, not lattices of either project.
:::

## Elliptic subdiagram enumerations

The `reports/Sterk_N/` directories hold, per cusp, one PNG per connected elliptic subdiagram, with the mathematical data encoded in the filename (rank, type, index).
The counts are:

| Cusp | Elliptic subdiagrams | Node/rank range |
| --- | --- | --- |
| Sterk 1 | 121 | 0-8 |
| Sterk 2 | 65 | 0-9 |
| Sterk 3 | 67 | 0-8 |
| Sterk 4 | 78 | 0-8 |
| Sterk 5 | 119 | 0-8 |

Types appearing are the twisted mixed-norm systems $A_n(2)$, $B_n(2)$, $D_n(2)$, $E_n(2)$, $G_2$, consistent with the $-2$ / $-4$ mixed-norm root systems of the folded diagrams.
Sterk 1 for instance carries $A_8(2)\times4$, $E_8(2)\times4$, $D_8(2)\times8$ at rank 8.

::: {.Remark}
### These are not orbit representatives

The lists are the **full** sets of elliptic subdiagrams, before quotienting by diagram symmetry.
The notebook step that reduced them to orbits (`summarize_maximal_orbits`) has its outputs cleared, so the orbit counts do not survive; see [the computational toolchain and recipe](computational-toolchain-and-recipe.md).
:::

Related: [root vectors and folded Sterk diagrams](root-vectors-and-folded-sterk-diagrams.md), [computational toolchain and recipe](computational-toolchain-and-recipe.md), [Sterk root counts and computed chambers](sterk-root-counts-and-computed-chambers.md).
