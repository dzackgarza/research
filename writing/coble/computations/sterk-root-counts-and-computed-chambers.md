---
title: Sterk's simple-root counts and the computed Vinberg chambers
unit: computation
status: open
tags:
  - sterk
  - vinberg
  - reflection-groups
  - cusps
---

# Sterk's simple-root counts and the computed Vinberg chambers

**Provenance.** `notes/computations/sterk-root-count-discrepancy.md`, recorded 2026-08-20 from the computation in `computations/scripts/init.sage`.
The CoxIter data quoted for comparison is that of [CoxIter results for cusp lattices](coxiter-results-for-cusp-lattices.md); the folded diagrams are those of [root vectors and folded Sterk diagrams](root-vectors-and-folded-sterk-diagrams.md).

## The lattices and the two computations

::: {.Remark}
### The five cusps and their hyperbolic quotients

Sterk's five cusp representatives are the primitive isotropic vectors
$$
\eta_1 = e,\quad
\eta_2 = e',\quad
\eta_3 = e'+f'+\omega,\quad
\eta_4 = e'+2f'+\alpha,\quad
\eta_5 = 2e+2f+\alpha
$$
of $\ten = U\oplus E_{10}(2)$, with $\omega = 2w_8$ and $\alpha = 2w_1$ in the dual basis ([Coble lattice isotropic candidates](coble-lattice-isotropic-candidates.md)).
Each determines a rank-$10$ hyperbolic lattice $\eta_j^{\perp}/\eta_j$, and hence a copy of $\HH^9$ (\longref{def:hyperbolic-model}) on which reflection groups act.
The isometry tests recorded with the computation give
$$
\eta_1^{\perp}/\eta_1 \cong U(2)\oplus E_8(2) = E_{10}(2),
\qquad
\eta_j^{\perp}/\eta_j \cong U\oplus E_8(2) \quad (j = 2,3,4,5),
$$
of two-elementary types $(10,10,0)$ and $(10,8,0)$ respectively.
:::

::: {.Remark}
### The counts

Sterk's published fundamental domains have $12, 10, 12, 11, 14$ walls, with the norm breakdowns
$12\times(-4)$; $9\times(-4)$, $1\times(-2)$; $10\times(-4)$, $2\times(-2)$; $9\times(-4)$, $2\times(-2)$; and $10\times(-4)$, $4\times(-2)$ [@Ste91].
Vinberg's algorithm run on the five quotient lattices returns $10$ roots for each, with $1$ ideal vertex for $\eta_1$ and $2$ for the others.
A second, independent implementation returns $9$ roots for $\eta_1$ and $10$ for the others.
:::

| Cusp | Published walls | Vinberg walls | Ideal vertices |
| --- | --- | --- | --- |
| 1 | 12 | 10 | 1 |
| 2 | 10 | 10 | 2 |
| 3 | 12 | 10 | 2 |
| 4 | 11 | 10 | 2 |
| 5 | 14 | 10 | 2 |

The two computed root sets, their coordinates in the recorded basis of each rank-$10$ quotient, and Sterk's own hand-entered root sets in both the $\ten$ and $L_{20,2,0}$ models are recorded in `computations/scripts/init.sage`.

## The computed chambers are hyperbolic simplices

::: {.Proposition #prop:nine-roots-insufficient}
### A finite-volume chamber in $\HH^9$ has at least ten walls

By \longref{thm:coxeter-polytope-volume}(1) a Coxeter polytope of finite volume in $\HH^n_L$ has, in the projective model, closure the convex hull of finitely many points of $\overline{\HH^n_L}$, so it is an $n$-dimensional convex polytope and has at least $n+1$ facets.
For $n = 9$ a fundamental chamber therefore has at least $10$ walls.
:::

::: {.Remark}
### Consequence for the two implementations

Vinberg's algorithm terminates when the accepted walls bound a polyhedron of finite volume (\longref{thm:vinberg-algorithm}), so a terminating run on a rank-$10$ hyperbolic lattice returns at least $10$ roots.
The nine-root output for $\eta_1$ therefore does not present a finite-volume chamber, and the ten-root output is the one to compare against.
:::

::: {.Observation #obs:chambers-are-simplices}
### Exactly ten walls means a simplex

A finite-volume polyhedron in $\HH^9$ with exactly $10$ facets is a $9$-simplex, the case of \longref{cor:coxeter-simplex-volume}, whose face numbers are $f_k = \binom{10}{k+1}$, that is
$$
(f_0,\dots,f_9) = (10, 45, 120, 210, 252, 210, 120, 45, 10, 1).
$$
This is the $f$-vector CoxIter reports for the folded Sterk 2 diagram and for both rank-$10$ $0$-cusp diagrams $(10,8,0)_1$ and $(10,10,0)_1$ ([CoxIter results for cusp lattices](coxiter-results-for-cusp-lattices.md)).
The Sterk 1, 3, 4 and 5 diagrams have $f$-vectors beginning $23, 33, 26, 115$, so those four polyhedra have more vertices than a simplex.
:::

::: {.Remark}
### The computed chambers match the CoxIter runs on the quotient lattices

CoxIter, run on the $0$-cusp diagram of $(10,10,0)_1$, reports dimension $9$, one vertex at infinity, Gram field $\QQ$, and the simplex $f$-vector; run on $(10,8,0)_1$ it reports dimension $9$, two vertices at infinity, Gram field $\QQ[\sqrt2]$, and the same $f$-vector.
Vinberg's algorithm on $\eta_1^{\perp}/\eta_1 \cong E_{10}(2)$, of type $(10,10,0)$, returns ten roots and one ideal vertex; on $\eta_j^{\perp}/\eta_j\cong U\oplus E_8(2)$, of type $(10,8,0)$, it returns ten roots and two ideal vertices for each of $j = 2,3,4,5$.
Wall count and ideal-vertex count agree in both cases.
:::

::: {.Remark}
### The shape of the computed root sets

In the recorded basis $\varepsilon_1,\dots,\varepsilon_{10}$ of $\eta_1^{\perp}/\eta_1$, the ten roots returned are
$$
-\varepsilon_3,\ -\varepsilon_4,\ \dots,\ -\varepsilon_{10},
\qquad
\varepsilon_1 - \varepsilon_2,
\qquad
\varepsilon_2 + 2\varepsilon_3 + 3\varepsilon_4 + 4\varepsilon_5 + 6\varepsilon_6 + 5\varepsilon_7 + 4\varepsilon_8 + 3\varepsilon_9 + 2\varepsilon_{10},
$$
and for $\eta_2^{\perp}/\eta_2$ the same list with the coefficient of $\varepsilon_2$ in the last root equal to $2$.
The coefficients $(2,3,4,6,5,4,3,2)$ on $\varepsilon_3,\dots,\varepsilon_{10}$ are the marks of the highest root of $E_8$, which is the affine extension pattern CoxIter records when it describes the $(10,10,0)_1$ diagram as $\widetilde E_{10}$-shaped.
:::

## The question the discrepancy poses

::: {.Question #qst:sterk-reflection-subgroup}
### Which reflection group does each published diagram bound a domain for?

The lattices $\eta_j^{\perp}/\eta_j$ for $j = 2,3,4,5$ are mutually isometric, so their full Weyl groups $W(\eta_j^{\perp}/\eta_j)$ (\longref{def:reflection}) are conjugate and their Vinberg chambers are isometric.
The published diagrams for those four cusps have $10, 12, 11, 14$ walls and $2, 4, 5, 13$ vertices at infinity, so no two of the last three are isometric to each other or to the ten-wall chamber.
A datum beyond the isometry class of $\eta_j^{\perp}/\eta_j$ therefore distinguishes them, and the candidate is the group: for each $j$, identify the subgroup $W_j \leq W(\eta_j^{\perp}/\eta_j)$ for which the published diagram is a Coxeter polytope (\longref{def:coxeter-polytope}), and exhibit the published domain as a union of chambers of the full group.

The natural candidate for $W_j$ is the reflection subgroup induced on $\eta_j^{\perp}/\eta_j$ by the stabilizer of $\eta_j$ in the arithmetic group acting on $\ten$, which depends on how the quotient sits inside $\ten$ and not only on its isometry class.
:::

::: {.Remark}
### The index is a covolume ratio, and the Euler characteristic does not supply it

If $W_j \leq W$ has finite index then
$$
\vol(\HH^9/W_j) = [W : W_j]\cdot \vol(\HH^9/W),
$$
so the index is determined by the two covolumes and is the sharpest available test of \longref{qst:sterk-reflection-subgroup}.
The Euler characteristic vanishes in odd dimension, and CoxIter reports $\chi = 0$ for all five nine-dimensional Sterk runs, so the Euler-characteristic route to the covolume gives no information here.
Settling the index requires either a direct covolume computation or a comparison of the growth series of the two Coxeter systems, of which CoxIter records one: the Sterk 1 growth rate $2.6246613781819533651112379994955986218$, Perron and neither Pisot nor Salem.
:::

::: {.Question #qst:sterk-ideal-vertices}
### How do the ideal vertices correspond?

The computed chambers have one or two isotropic rays, and the published diagrams have $9, 2, 4, 5, 13$ vertices at infinity.
Ideal vertices of a chamber correspond bijectively to the rank-$(n-1)$ parabolic subdiagrams of its Coxeter--Vinberg diagram (\longref{cor:ideal-vertices-are-parabolic}), hence to the $1$-cusps adjacent to the $0$-cusp in question (\longref{def:parabolic-subdiagram}).
Under a chamber decomposition answering \longref{qst:sterk-reflection-subgroup}, determine which ideal vertices of the union are ideal vertices of the constituent chambers and which arise on interior walls.
:::

::: {.Remark}
### Cusp 2 is the case where the two agree

The published Sterk 2 diagram has ten walls, two vertices at infinity, and the simplex $f$-vector, matching the Vinberg chamber of $U\oplus E_8(2)$ in every recorded invariant.
Cusp 2 is the Sterk cusp to which the Coble $0$-cusp is claimed to correspond ([cusp-correspondence morphism chain](../coble-moduli/cusp-correspondence-morphism-chain.md)), and it is the one cusp for which \longref{qst:sterk-reflection-subgroup} already has the answer $W_2 = W(\eta_2^{\perp}/\eta_2)$.
:::

::: {.Remark}
### The four cusps the Coble boundary sees are exactly the four that force the question

Every primitive isotropic vector of $T_\Co$ has divisibility $2$ (\longref{lem:divisibilityAlwaysTwoTco}), so the divisibility-one Sterk cusp $1$ does not occur on the polarized Coble boundary and only cusps $2$ to $5$ are in play there ([KSBA stable limits](../stable-limits/ksba.md)).
Those are exactly the four with mutually isometric quotients $\eta_j^{\perp}/\eta_j\cong U\oplus E_8(2)$ and pairwise inequivalent published diagrams, which is the configuration \longref{qst:sterk-reflection-subgroup} is about.
:::

## Hypotheses of the recorded runs

::: {.Warning}
### The sign convention of the recorded runs is not recorded

The Vinberg implementation used takes a lattice of signature $(n,1)$, while this project's convention is $(1,n)$ ([reflection groups and Vinberg](../compactifications/reflection-groups-and-vinberg.md)).
The intended transport negates the form before the call and negates the returned roots afterwards.
Which of $L$ and $L(-1)$ the recorded runs were given is not part of the record, and the roots quoted above should be reproduced with the convention fixed before they are used as input to a further computation.
:::

::: {.Remark}
### Gram fields

The base field of a Coxeter matrix is generated by the values $2\cos(\pi/m_{st})$ (\longref{def:coxeter-base-field}), and is a real cyclotomic field of the degree computed in \longref{prop:coxeter-base-field-degree}.
CoxIter reports Gram field $\QQ$ for the folded Sterk 1 diagram and for $(10,10,0)_1$, and $\QQ[\sqrt2]$ for the other four folded diagrams and for $(10,8,0)_1$ and $(9,9,1)_1$; the $\sqrt2$ is $2\cos(\pi/4)$, the label-$4$ bond of the $B$-type diagrams.
:::

Related: [CoxIter results for cusp lattices](coxiter-results-for-cusp-lattices.md), [root vectors and folded Sterk diagrams](root-vectors-and-folded-sterk-diagrams.md), [fundamental chamber polyhedra](fundamental-chamber-polyhedra.md), [cusp-correspondence morphism chain](../coble-moduli/cusp-correspondence-morphism-chain.md).
