---
unit: computation
status: partial
tags:
  - sterk
  - vinberg
  - reflection-groups
  - cusps
notes: |-
  Provenance: the Sterk root-count discrepancy note, recorded 2026-08-20 from the Sage initialization computation. The comparison data are the CoxIter cusp-lattice results and the folded Sterk-diagram computations.
---

# Sterk's simple-root counts and the computed Vinberg chambers {#sec-sterk-root-counts-and-computed-chambers}


## The lattices and the two computations

::: {.remark title="The five cusps and their hyperbolic quotients"}

Sterk's five cusp representatives are the primitive isotropic vectors
$$
\eta_1 = e,\quad
\eta_2 = e',\quad
\eta_3 = e'+f'+\omega,\quad
\eta_4 = e'+2f'+\alpha,\quad
\eta_5 = 2e+2f+\alpha
$$
of $\ten = U\oplus E_{10}(2)$, with $\omega = 2w_8$ and $\alpha = 2w_1$ in the dual basis ([Coble lattice isotropic candidates](#sec-coble-lattice-isotropic-candidates)). Each determines a rank-$10$ hyperbolic lattice $\eta_j^{\perp}/\eta_j$, and hence a copy of $\HH^9$ (@def:hyperbolic-model) on which reflection groups act.
The isometry tests recorded with the computation give
$$
\eta_1^{\perp}/\eta_1 \cong U(2)\oplus E_8(2) = E_{10}(2),
\qquad
\eta_j^{\perp}/\eta_j \cong U\oplus E_8(2) \quad (j = 2,3,4,5),
$$
of two-elementary types $(10,10,0)$ and $(10,8,0)$ respectively.
:::

::: {.remark title="The counts"}

Sterk's published fundamental domains have $12, 10, 12, 11, 14$ walls, with the norm breakdowns $12\times(-4)$; $9\times(-4)$, $1\times(-2)$; $10\times(-4)$, $2\times(-2)$; $9\times(-4)$, $2\times(-2)$; and $10\times(-4)$, $4\times(-2)$ [@Ste91].
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

The two computed root sets, their coordinates in the recorded basis of each rank-$10$ quotient, and Sterk's own hand-entered root sets in both the $\ten$ and $L_{20,2,0}$ models are recorded in the Sage initialization computation.
That citation does not hold: the file it points at, `sage-init.sage`, is the session startup file --- a display hook for cell results --- and contains no root set, no basis and no lattice. So the coordinates $\eps_1,\dots,\eps_{10}$ in which the ten roots below are written are *not* defined in the tree: the two chambers are records for their wall counts and ideal vertices, not for their root coordinates, and $\eps_i\mapsto T_\En$ is owed.

## The computed chambers are hyperbolic simplices

::: {.proposition #prop:nine-roots-insufficient title="A finite-volume chamber in $\HH^9$ has at least ten walls"}

By @thm:coxeter-polytope-volume(1) a Coxeter polytope of finite volume in $\HH^n_L$ has, in the projective model, closure the convex hull of finitely many points of $\overline{\HH^n_L}$, so it is an $n$-dimensional convex polytope and has at least $n+1$ facets.
For $n = 9$ a fundamental chamber therefore has at least $10$ walls.
:::

::: {.proof}

By @thm:coxeter-polytope-volume(1), a Coxeter polytope of finite volume in $\HH^n_L$ has, in the projective model, closure equal to the convex hull of finitely many points of the boundary $\bd\HH^n_L$; in particular it is a bounded polytope in an affine chart and has at least $n+1$ facets.
Indeed a bounded $n$-dimensional polytope that is not a point has at least $n+1$ facets, since a vertex is the intersection of at least $n$ facets in a simple polytope and a bounded polytope has a vertex, or, equivalently, since with $k\leq n$ facets the polytope spans an affine subspace of dimension at most $k-1$.

With $n=9$ this gives at least $10$ facets, that is at least $10$ walls.
So an output of nine roots is not the correct set of walls of any finite-volume chamber in $\HH^9$: whatever reflection group those nine roots generate, the chamber they bound is not finite-volume, and the missing wall is a root the algorithm would have to find.
By @thm:vinberg-algorithm a terminating run on a rank-$10$ hyperbolic lattice returns at least ten roots.
:::

::: {.remark title="Consequence for the two implementations"}

Vinberg's algorithm terminates when the accepted walls bound a polyhedron of finite volume (@thm:vinberg-algorithm), so a terminating run on a rank-$10$ hyperbolic lattice returns at least $10$ roots.
The nine-root output for $\eta_1$ therefore does not present a finite-volume chamber, and the ten-root output is the one to compare against.
:::

::: {.observation #obs:chambers-are-simplices title="Exactly ten walls means a simplex"}

A finite-volume polyhedron in $\HH^9$ with exactly $10$ facets is a $9$-simplex, the case of @cor:coxeter-simplex-volume, whose face numbers are $f_k = \binom{10}{k+1}$, that is
$$
(f_0,\dots,f_9) = (10, 45, 120, 210, 252, 210, 120, 45, 10, 1).
$$
This is the $f$-vector CoxIter reports for the folded Sterk 2 diagram and for both rank-$10$ $0$-cusp diagrams $(10,8,0)_1$ and $(10,10,0)_1$ ([CoxIter results for cusp lattices](#sec-coxiter-results-for-cusp-lattices)). The Sterk 1, 3, 4 and 5 diagrams have $f$-vectors beginning $23, 33, 26, 115$, so those four polyhedra have more vertices than a simplex.
:::

::: {.remark title="The computed chambers match the CoxIter runs on the quotient lattices"}

CoxIter, run on the $0$-cusp diagram of $(10,10,0)_1$, reports dimension $9$, one vertex at infinity, Gram field $\QQ$, and the simplex $f$-vector; run on $(10,8,0)_1$ it reports dimension $9$, two vertices at infinity, Gram field $\QQ[\sqrt2]$, and the same $f$-vector.
Vinberg's algorithm on $\eta_1^{\perp}/\eta_1 \cong E_{10}(2)$, of type $(10,10,0)$, returns ten roots and one ideal vertex; on $\eta_j^{\perp}/\eta_j\cong U\oplus E_8(2)$, of type $(10,8,0)$, it returns ten roots and two ideal vertices for each of $j = 2,3,4,5$.
Wall count and ideal-vertex count agree in both cases.
:::

::: {.remark title="The shape of the computed root sets"}

In the recorded basis $\eps_1,\dots,\eps_{10}$ of $\eta_1^{\perp}/\eta_1$, the ten roots returned are
$$
-\eps_3,\ -\eps_4,\ \dots,\ -\eps_{10},
\qquad
\eps_1 - \eps_2,
\qquad
\eps_2 + 2\eps_3 + 3\eps_4 + 4\eps_5 + 6\eps_6 + 5\eps_7 + 4\eps_8 + 3\eps_9 + 2\eps_{10},
$$
and for $\eta_2^{\perp}/\eta_2$ the same list with the coefficient of $\eps_2$ in the last root equal to $2$.
The coefficients $(2,3,4,6,5,4,3,2)$ on $\eps_3,\dots,\eps_{10}$ are the marks of the highest root of $E_8$, which is the affine extension pattern CoxIter records when it describes the $(10,10,0)_1$ diagram as $\widetilde E_{10}$-shaped.
:::

## The question the discrepancy poses

::: {.question #qst:sterk-reflection-subgroup title="Which reflection group does each published diagram bound a domain for?"}

The lattices $\eta_j^{\perp}/\eta_j$ for $j = 2,3,4,5$ are mutually isometric, so their full Weyl groups $W(\eta_j^{\perp}/\eta_j)$ (@def:reflection) are conjugate and their Vinberg chambers are isometric.
The published diagrams for those four cusps have $10, 12, 11, 14$ walls and $2, 4, 5, 13$ vertices at infinity, so no two of the last three are isometric to each other or to the ten-wall chamber.
A datum beyond the isometry class of $\eta_j^{\perp}/\eta_j$ therefore distinguishes them, and the candidate is the group: for each $j$, identify the subgroup $W_j \leq W(\eta_j^{\perp}/\eta_j)$ for which the published diagram is a Coxeter polytope (@def:coxeter-polytope), and exhibit the published domain as a union of chambers of the full group.

The natural candidate for $W_j$ is the reflection subgroup induced on $\eta_j^{\perp}/\eta_j$ by the stabilizer of $\eta_j$ in the arithmetic group acting on $\ten$, which depends on how the quotient sits inside $\ten$ and not only on its isometry class.
:::

::: {.remark title="The index is a covolume ratio, and the Euler characteristic does not supply it"}

If $W_j \leq W$ has finite index then
$$
\vol(\HH^9/W_j) = [W : W_j]\cdot \vol(\HH^9/W),
$$
so the index is determined by the two covolumes and is the sharpest available test of @qst:sterk-reflection-subgroup.
The Euler characteristic vanishes in odd dimension, and CoxIter reports $\chi = 0$ for all five nine-dimensional Sterk runs, so the Euler-characteristic route to the covolume gives no information here.
Settling the index requires either a direct covolume computation or a comparison of the growth series of the two Coxeter systems, of which CoxIter records one: the Sterk 1 growth rate $2.6246613781819533651112379994955986218$, Perron and neither Pisot nor Salem.
:::

::: {.question #qst:sterk-ideal-vertices title="How do the ideal vertices correspond?"}

The computed chambers have one or two isotropic rays, and the published diagrams have $9, 2, 4, 5, 13$ vertices at infinity.
Ideal vertices of a chamber correspond bijectively to the rank-$(n-1)$ parabolic subdiagrams of its Coxeter--Vinberg diagram (@cor:ideal-vertices-are-parabolic), hence to the $1$-cusps adjacent to the $0$-cusp in question (@def:parabolic-subdiagram).
Under a chamber decomposition answering @qst:sterk-reflection-subgroup, determine which ideal vertices of the union are ideal vertices of the constituent chambers and which arise on interior walls.
:::

::: {.remark title="Cusp 2 is the case where the two agree"}

The published Sterk 2 diagram has ten walls, two vertices at infinity, and the simplex $f$-vector, matching the Vinberg chamber of $U\oplus E_8(2)$ in every recorded invariant.
Cusp 2 is the Sterk cusp to which the Coble $0$-cusp is claimed to correspond ([cusp-correspondence morphism chain](#sec-cusp-correspondence-morphism-chain)), and it is the one cusp for which @qst:sterk-reflection-subgroup already has the answer $W_2 = W(\eta_2^{\perp}/\eta_2)$.
:::

::: {.remark title="The four cusps the Coble boundary sees are exactly the four that force the question"}

Every primitive isotropic vector of $T_\Co$ has divisibility $2$ (@lem:divisibilityAlwaysTwoTco), so the divisibility-one Sterk cusp $1$ does not occur on the polarized Coble boundary and only cusps $2$ to $5$ are in play there ([KSBA stable limits](#sec-ksba)). Those are exactly the four with mutually isometric quotients $\eta_j^{\perp}/\eta_j\cong U\oplus E_8(2)$ and pairwise inequivalent published diagrams, which is the configuration @qst:sterk-reflection-subgroup is about.
:::

## The reflection subgroup of each stabilizer, computed

Sterk's five diagrams are described in his text as "the diagram of the reflection subgroup of $G_v$" (4.3.5--4.3.9, pp. 19--24), with $G_v = \rho(\Stab_\Gamma(v))$, $\Gamma = \gent$. A reflection of a quotient lattice, however, need not lift to a reflection of the ambient lattice in $\Gamma$, so before the subgroup can be computed the question is which reflections of $K_j$ have a lift in $\gent$. The next lemma settles the direction that is needed and says what it leaves open.

::: {.lemma #lem:sterk-reflection-lift-criterion title="Which reflections of the quotient are certified to lie in $G_v$"}
Let $\eta$ be a primitive isotropic vector of $T_\En$ with $\eta\in L^- = U(2)\oplus E_8(2)$, put $K = \eta^\perp/\ZZ\eta$, let $r\in K$ be a root, that is a vector with $r^2\in\set{-2,-4}$ whose reflection is integral on $K$, and let $\tilde r\in\eta^\perp\subset T_\En$ be a lift of $r$. Then

1. $s_{\tilde r}$ is an integral isometry of $T_\En$ fixing $\eta$, and it induces $s_r$ on $K$;
2. if $\rho(s_{\tilde r})$ preserves both summands of $A_{T_\En} = \frac12U(2)/U(2)\oplus\frac12E_8(2)/E_8(2)$, then $s_{\tilde r}\in\gent$, hence $s_r\in G_v$; and this hypothesis does not depend on the choice of lift;
3. the converse is **not** claimed, and it can fail: the kernel of $\Stab_{O(T_\En)}(\eta)\to O(K)$ consists of the shears $x\mapsto x+\ell(x)\eta$ on $\eta^\perp$ with $\ell\in\Hom(\eta^\perp/\ZZ\eta,\ZZ)$. The subfamily $\ell = c\,(\eta,\cdot)$ has trivial discriminant image, but the kernel is strictly larger, and an element of it can carry $\rho$ out of $M$; a reflection of $G_v$ all of whose lifts miss $M$ by such an element is therefore invisible to (2).
:::

::: {.proof}
For (1): on a $(-2)$-vector the reflection is $s_{\tilde r}(x) = x + (x,\tilde r)\tilde r$, integral because $T_\En$ is even; on a $(-4)$-one it is $s_{\tilde r}(x) = x + \tfrac12(x,\tilde r)\tilde r$, integral exactly when $(x,\tilde r)$ is even for every $x\in T_\En$, which holds because $\tilde r\perp U$ and $E_8(2)$ is even. Both fix $\eta$ because $\tilde r\perp\eta$, and both induce the reflection in $r$ on $\eta^\perp/\ZZ\eta$.

For (2): $\gent = \rho^{-1}(M)$ with $M$ the summand-preserving subgroup, by Sterk's Proposition 2.7 (p. 6), which identifies $F$ with exactly the isometries of $L^-$ whose induced map on $L_-^*/L_-$ respects the two summands, together with $A_{T_\En} = L_-^*/L_-$, which holds because $T_\En = U\oplus L^-$ with $U$ unimodular. So $\rho(s_{\tilde r})\in M$ means $s_{\tilde r}\in\gent$; it fixes $\eta$, so it lies in $\Stab_\gent(\eta)$ and its image $s_r$ is in $G_v$. Changing the lift to $\tilde r+k\eta$ changes $s_{\tilde r}$ by an element of the kernel of $\Stab_{O(T_\En)}(\eta)\to O(K)$, which acts trivially on $A_{T_\En}$ exactly for the subfamily in (3).

For (3): an isometry of $T_\En$ fixing $\eta$ and acting trivially on $\eta^\perp/\ZZ\eta$ maps $x\mapsto x+\ell(x)\eta$ on $\eta^\perp$ with $\ell$ a homomorphism. Writing $T_\En = \eta^\perp + \ZZ y_0$ with $(y_0,\eta) = d$ and $g(y_0) = y_0 + w$, the isometry conditions are $(w,x) = -d\,\ell(x)$ for $x\in\eta^\perp$ together with $2(y_0,w) + w^2 = 0$; the first determines $w$ modulo $\ZZ\eta$, and the second is one equation, so the kernel contains elements with $\ell$ outside the line $\ZZ(\eta,\cdot)$. Such an element acts on $A_{T_\En}$ through the class of $\ell$ in $T_\En^*/T_\En$, which is nonzero for $\ell$ outside that line, so it moves $\rho$ and the criterion of (2) is not necessary.
:::

::: {.theorem #thm:sterk-reflection-subgroups title="The five published diagrams, checked in Sterk's own representatives"}
Let $\eta_1,\dots,\eta_5$ be the representatives Sterk uses in 4.3.5--4.3.9, $K_j = \eta_j^\perp/\ZZ\eta_j$, and $R_j$ his printed root set beside Fig. 4, 6, 8, 10 or 12. Then

- the five cusps are the five $M$-orbits of isotropic classes of $A_{T_\En}$, of sizes $1,\,2,\,120,\,270,\,135$ for $j = 1,2,3,4,5$; the class $[\eta_j/2]$ of Sterk's representative and that of the representative written on this page lie in the same orbit for every $j$, and the cusp-$3$ class is not in the cusp-$5$ orbit. The class stabilizers have orders $\abs{\Stab_M([\eta_j/2])} = 696\,729\,600$, $348\,364\,800$, $5\,806\,080$, $2\,580\,480$, $5\,160\,960$;
- every vector of every $R_j$ lies in $\eta_j^\perp$, has square in $\set{-2,-4}$, and has its reflection certified to be in $\gent$ by @lem:sterk-reflection-lift-criterion(2); the walls bound a polytope of finite covolume, and its vertex counts are

| $j$ | $\abs{R_j}$ | finite vertices | ideal vertices | total | $f_0$ of the recorded CoxIter run |
|---|---|---|---|---|---|
| 1 | 12 | 14 | 9 | 23 | 23 |
| 2 | 10 | 8 | 2 | 10 | 10 |
| 3 | 12 | 29 | 4 | 33 | 33 |
| 4 | 11 | 21 | 5 | 26 | 26 |
| 5 | 14 | 102 | 13 | 115 | 115 |

and the weight multisets are $\set{3{:}10,\infty{:}3}$, $\set{3{:}8,4{:}1}$, $\set{3{:}7,4{:}4,\infty{:}1}$, $\set{3{:}8,4{:}2}$, $\set{3{:}8,4{:}8,\infty{:}1}$ for $j = 1..5$, those of the five published figures;
- at cusps $2$ and $5$ the subgroup generated by *all* roots that the criterion certifies has exactly the published chamber: $10$ walls with $2$ ideal vertices and $14$ walls with $13$, with the same weight multisets. At cusps $1$, $3$ and $4$ no such chamber is claimed: the algorithm's own construction (its integer-point box in those coordinates) did not return within this batch, and the transcript says so.
:::

::: {.proof}
$A_{T_\En} = \frac12(U(2)\oplus E_8(2))/(U(2)\oplus E_8(2))$ has $1024$ classes and $q([x]) = (x,x)\bmod 2\ZZ$; computing $q$ gives $528$ isotropic classes, $527$ of them nonzero. The nine recorded generators of $M$ --- the eight simple-root reflections of $E_8(2)$ and the reflection in $e'-f'$ --- preserve $q$ and both summands, and their orbits on the $528$ isotropic classes are $[270,135,120,2,1]$, the partition recorded in `computations/reports/coble_gammaEn2-subgroup-orbits.md`. The divisibility-two cusps have their classes $\frac12\eta_j$ in the four non-singleton orbits and $e$ has the zero class; the correspondence $v\mapsto[v/2]$ is $\gent$-equivariant and Sterk's Proposition 4.2.3 gives five pairwise inequivalent cusps, so the five classes are pairwise inequivalent. The orbit of each representative is printed in the transcript, in the same table as the orbit of the representative used on this page.

The five root sets are written from Sterk's closed forms (§2, p. 32 and 4.3.5--4.3.9) in the lattice $T_\En$; five of the twelve roots at cusp $3$ and six of the fourteen at cusp $5$ are not in the span of the quotient basis alone and are read off in the full frame $\eta^\perp = \ZZ\eta\oplus K_j$, which the transcript records. Each root's reflection is certified by @lem:sterk-reflection-lift-criterion(2), and the polytope's vertex rays are computed from the wall Gram; the totals in the table are the $f_0$ of the CoxIter runs recorded for the same figures in [@sec-coxiter-results-for-cusp-lattices]. For cusps $2$ and $5$ the restricted Vinberg search (the algorithm of @thm:vinberg-algorithm with the reflection set cut down to the certified roots, $-G_{K_j}$ handed to it and the roots negated back) closes with exactly the published wall and ideal-vertex counts.
:::

::: {.remark title="No disagreement with Sterk is claimed here"}
An earlier version of this page reported cusp $3$ as the cusp where the published figure and the computed chamber differ, on the strength of a $14$-wall certified chamber computed from this page's representative of $\eta_3$. That conclusion is withdrawn. What the computation supports is weaker and is stated in @thm:sterk-reflection-subgroups: his twelve walls bound a polytope of finite covolume with $33$ vertices, $4$ of them at infinity, all twelve of them certified in $\gent$; and the subgroup generated by *all* certified roots is strictly larger, its chamber having $14$ walls. The two statements are compatible, because the criterion is one-directional (@lem:sterk-reflection-lift-criterion(3)): a reflection of $G_v$ can be invisible to it. That the certified chamber at cusp $3$ has the invariants of the cusp-$5$ chamber is a further sign of the same coarseness --- a criterion that is only sufficient can fail to separate two cusps --- and it is not evidence about his figures.
:::

::: {.remark title="What remains of @qst:sterk-reflection-subgroup"}
Three things: the certified chamber at cusps $1$, $3$ and $4$, whose computation needs the algorithm's construction to return in those coordinates; the kernel of $\Stab_{O(T_\En)}(\eta_j)\to O(K_j)$ acting on $A_{T_\En}$, which is what decides whether a certified reflection is all of $G_v$'s reflection subgroup and hence whether the certified chamber is $W_j$'s; and the numerical index $[W(K_j):W_j]$, which the Euler characteristic does not supply in odd dimension, as the covolume remark above says.
:::

## Hypotheses of the recorded runs

::: {.warning title="The sign convention of the recorded runs is not recorded"}

The Vinberg implementation used takes a lattice of signature $(n,1)$, while this project's convention is $(1,n)$ ([reflection groups and Vinberg](#sec-reflection-groups-and-vinberg)). The intended transport negates the form before the call and negates the returned roots afterwards.
Which of $L$ and $L(-1)$ the recorded runs were given is not part of the record, and the roots quoted above should be reproduced with the convention fixed before they are used as input to a further computation.
:::

::: {.remark title="Gram fields"}

The base field of a Coxeter matrix is generated by the values $2\cos(\pi/m_{st})$ (@def:coxeter-base-field), and is a real cyclotomic field of the degree computed in @prop:coxeter-base-field-degree.
CoxIter reports Gram field $\QQ$ for the folded Sterk 1 diagram and for $(10,10,0)_1$, and $\QQ[\sqrt2]$ for the other four folded diagrams and for $(10,8,0)_1$ and $(9,9,1)_1$; the $\sqrt2$ is $2\cos(\pi/4)$, the label-$4$ bond of the $B$-type diagrams.
:::

Related: [CoxIter results for cusp lattices](#sec-coxiter-results-for-cusp-lattices), [root vectors and folded Sterk diagrams](#sec-root-vectors-and-folded-sterk-diagrams), [fundamental chamber polyhedra](#sec-fundamental-chamber-polyhedra), [cusp-correspondence morphism chain](#sec-cusp-correspondence-morphism-chain).
