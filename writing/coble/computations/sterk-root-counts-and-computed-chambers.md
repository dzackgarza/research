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

Sterk's five diagrams are described in his text as "the diagram of the reflection subgroup of $G_v$" (4.3.5--4.3.9, pp. 19--24), so @qst:sterk-reflection-subgroup is not about a group still to be invented: $G_v$ is the image in $O(K_j)$ of $\Stab_\Gamma(\eta_j)$ with $\Gamma = \gent$, and $\gent$ sits in $O(T_\En)$ rather than in $O(L^-)$, so a reflection of $K_j$ belongs to $G_v$ exactly when it lifts to a reflection of $T_\En$ lying in $\gent$. The next lemma says which reflections those are, by the discriminant class of the root; the subgroup is therefore a finite computation on the $1024$ classes of $A_{T_\En}$, and its chamber is then Vinberg's algorithm run with the reflection set so restricted.

::: {.lemma #lem:sterk-reflection-lift-criterion title="A reflection of the quotient is in $G_v$ exactly when its discriminant class is allowed"}
Let $\eta$ be a primitive isotropic vector of $T_\En$ with $\eta\in L^- = U(2)\oplus E_8(2)$, put $K = \eta^\perp/\ZZ\eta$, and let $r\in K$ be a root, that is a vector with $r^2\in\set{-2,-4}$ whose reflection is integral on $K$. Let $\tilde r\in\eta^\perp\subset T_\En$ be a lift of $r$. Then

1. $s_{\tilde r}$ is an integral isometry of $T_\En$ fixing $\eta$, and it induces $s_r$ on $K$;
2. if $g\in\Stab_{O(T_\En)}(\eta)$ induces $s_r$ on $K$, then $gs_{\tilde r}^{-1}$ acts trivially on $K$, hence is a shear $u_c(x) = x + c\,(x,\eta)\,\eta$, and $\rho(u_c)$ is the class of $c\eta$, which is trivial because $\eta$ is a vector of $T_\En$;
3. consequently $s_r\in G_v$ if and only if $s_{\tilde r}\in\gent$, if and only if $\rho(s_{\tilde r})$ preserves both summands of $A_{T_\En} = \frac12U(2)/U(2)\oplus\frac12E_8(2)/E_8(2)$; and by (2) none of this depends on the choice of lift $\tilde r$.
:::

::: {.proof}
For (1): on a $(-2)$-vector the reflection is $s_{\tilde r}(x) = x + (x,\tilde r)\tilde r$, integral because $T_\En$ is even; on a $(-4)$-one it is $s_{\tilde r}(x) = x + \tfrac12(x,\tilde r)\tilde r$, integral exactly when $(x,\tilde r)$ is even for every $x\in T_\En$, which holds here because $\tilde r\perp U$ and $E_8(2)$ is even. Both formulas fix $\eta$ because $\tilde r\perp\eta$, and both induce the reflection in $r$ on $\eta^\perp/\ZZ\eta$.

For (2): an isometry of a lattice acting trivially on $\eta^\perp/\ZZ\eta$ maps $x\mapsto x+\ell(x)\eta$ with $\ell$ a homomorphism, and requiring $(x+\ell(x)\eta,\,y+\ell(y)\eta) = (x,y)$ for all $x,y$ in the lattice forces $\ell = c(\eta,\cdot)$, since $\eta$ is isotropic. As a functional on $T_\En$ that is $c\eta$, whose class in $A_{T_\En}$ vanishes because $\eta\in T_\En$; so $\rho(u_c) = 1$.

For (3): $\gent = \rho^{-1}(M)$ with $M$ the subgroup of $O(A_{T_\En},q)$ preserving the two summands, by Sterk's Proposition 2.7 (p. 6), which identifies $F$ with exactly the isometries of $L^-$ whose induced map on $L_-^*/L_-$ respects the two summands, together with $A_{T_\En} = L_-^*/L_-$, which holds because $T_\En = U\oplus L^-$ with $U$ unimodular. If $s_r\in G_v$ comes from $g\in\Stab_\gent(\eta)$, then $\rho(g) = \rho(s_{\tilde r})$ by (2), so $\rho(s_{\tilde r})\in M$. Conversely if $\rho(s_{\tilde r})\in M$ then $s_{\tilde r}\in\gent$ and it fixes $\eta$, so $s_{\tilde r}\in\Stab_\gent(\eta)$ and its image $s_r$ is in $G_v$.
:::

::: {.theorem #thm:sterk-reflection-subgroups title="The cusps are the $M$-orbits of isotropic classes, and the diagrams generate subgroups of $W_j$"}
Let $\eta_1,\dots,\eta_5$ be Sterk's cusp representatives, $K_j = \eta_j^\perp/\ZZ\eta_j$, and let $W_j\leq O(K_j)$ be generated by the reflections in the roots of $K_j$ that satisfy @lem:sterk-reflection-lift-criterion. Then:

- the five cusps correspond bijectively to the five $M$-orbits of isotropic classes of $A_{T_\En}$; the orbit sizes are $1, 2, 120, 270, 135$ for $j = 1,2,3,4,5$ and the class stabilizers have orders $\abs{\Stab_M([\eta_j/2])} = \abs{M}/\abs{\text{orbit}} = 696\,729\,600$, $348\,364\,800$, $5\,806\,080$, $2\,580\,480$, $5\,160\,960$;
- every one of the $12+10+12+11+14$ roots Sterk prints beside his five figures has its reflection in $\gent$, so each published diagram is the Coxeter diagram of a subgroup of $W_j$;
- for $j = 2, 3, 5$ the group $W_j$ has finite covolume, and its Vinberg chamber has

| $j$ | $K_j$ | walls of $W_j$ | ideal vertices | finite vertices | published walls | published ideal vertices | |
|---|---|---|---|---|---|---|---|
| 2 | $U\oplus E_8(2)$ | 10 | 2 | 8 | 10 | 2 | agrees |
| 3 | $U\oplus E_8(2)$ | 14 | 13 | 102 | 12 | 4 | **does not agree** |
| 5 | $U\oplus E_8(2)$ | 14 | 13 | 102 | 14 | 13 | agrees |

with Coxeter weight multisets $\set{3:8,\,4:1}$ for $j=2$ and $\set{3:8,\,4:8,\,\infty:1}$ for $j = 3$ and $j = 5$;
- for $j = 1$ and $j = 4$ no chamber is claimed: at cusp $4$ the run did not return from the engine within the decomposition bound set in the record's script (`BOUNDS` in `computations/reports/coble_sterk-reflection-subgroups.py`) and its section of the transcript ends at the initialization, and cusp $1$ is last in the script's order and was not reached. Those two cusps, and the numerical index of the remark below, are what remains of @qst:sterk-reflection-subgroup.
:::

::: {.proof}
$A_{T_\En} = \frac12(U(2)\oplus E_8(2))/(U(2)\oplus E_8(2))$ has $1024$ classes and $q([x]) = (x,x)\bmod 2\ZZ$; computing $q$ gives $528$ isotropic classes, $527$ of them nonzero. The nine recorded generators of $M$ --- the eight simple-root reflections of $E_8(2)$ and the reflection in $e'-f'$ --- preserve $q$ and both summands, and their orbits on the $528$ isotropic classes are $[270,135,120,2,1]$, the partition recorded in `computations/reports/coble_gammaEn2-subgroup-orbits.md`. The four divisibility-two cusps have their classes $\frac12\eta_j$ in the four non-singleton orbits and the divisibility-one cusp $e$ has the zero class. The correspondence $v\mapsto[v/2]$ is $\gent$-equivariant, and Sterk's Proposition 4.2.3 gives five pairwise inequivalent cusps, so the five classes are pairwise inequivalent and the correspondence is a bijection.

The criterion of @lem:sterk-reflection-lift-criterion is applied root by root, and Vinberg's algorithm is run on $K_j$ with the reflection set restricted to the accepted roots, from scratch, in the sign convention of the record: the algorithm is handed $-G_{K_j}$, of signature $(9,1)$, and the roots it returns are negated back and re-verified against $G_{K_j}$ ($r^2\in\set{-2,-4}$, and the wall Gram recomputed from $G_{K_j}$). Each closed run is Vinberg's termination certificate and therefore gives finite covolume. The wall counts, the norm and weight multisets and the vertex counts are those printed in `computations/reports/coble_sterk-reflection-subgroups-run.txt`, which also re-derives Sterk's own figures from the roots he prints: the multisets $\set{3:8,4:1}$ (Fig. 6, cusp 2), $\set{3:7,4:4,\infty:1}$ (Fig. 8, cusp 3), $\set{3:8,4:2}$ (Fig. 10, cusp 4) and $\set{3:8,4:8,\infty:1}$ (Fig. 12, cusp 5).
:::

::: {.remark title="Cusp 3 is where the published diagram is not the reflection subgroup's chamber"}
At cusps $2$ and $5$ the computed chamber and Sterk's figure agree in the wall count, the ideal-vertex count, the norm breakdown and the weight multiset, so @qst:sterk-reflection-subgroup is answered there in the affirmative, and it is answered in the affirmative at cusp $2$ by $W_2 = W(\eta_2^\perp/\eta_2)$, as the record above already had. At cusp $3$ they do not agree: his Fig. 8 has $12$ walls and $4$ vertices at infinity, while $W_3$ has $14$ walls, $13$ of them at infinity, and $102$ finite vertices, with the weight multiset of his own Fig. 12. Since his twelve printed roots do have their reflections in $\gent$ (@thm:sterk-reflection-subgroups), they generate a proper subgroup of $W_3$; his Fig. 8 is therefore a fundamental domain for that proper subgroup and not for the reflection subgroup of $G_v$ that he says it diagrams. The same computation reproduces his cusps $2$ and $5$ exactly, which is what puts the discrepancy at the figure rather than at the method, and the reflection subgroups at cusps $3$ and $5$ then have isometric chambers, so no diagram attached to the stabilizer subgroups separates those two cusps.
:::

::: {.remark title="What the index $[W(K_j):W_j]$ would still need"}
@qst:sterk-reflection-subgroup asks for the index as a covolume ratio. The wall sets computed here answer the question combinatorially --- the two chambers are different polytopes exactly when the index is not one --- but the numerical index still needs a covolume, and the Euler characteristic does not supply it in odd dimension, as the record above says. What the computation adds to that remark is that the index is not one at cusp $3$: the computed chamber has $14$ walls and the published one $12$, and two chambers of one reflection group are $W$-conjugate and hence have the same number of facets, so $\langle R_3\rangle$ is a proper subgroup of $W_3$.
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
