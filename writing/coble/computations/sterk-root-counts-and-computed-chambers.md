---
unit: computation
status: partial
tags:
  - sterk
  - vinberg
  - reflection-groups
  - cusps
notes: |-
  Provenance: the Sterk root-count discrepancy note, recorded 2026-08-20 from the Sage initialization computation. The comparison data are the CoxIter cusp-lattice results and the folded Sterk-diagram computations. The criterion for the reflection subgroup at a cusp is Alexeev--Engel--Garza--Schaffler, Nagoya Math. J. 259 (2025), Definition 3.6, Lemma 3.4, Corollary 3.12 and §3.8; the lift and divisibility computations are `computations/reports/coble_sterk-root-lifts.py` and its transcript, the polytope and orbit computations `computations/reports/coble_sterk-reflection-subgroups.py` and its transcript.
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

## The criterion of the source, and the five diagrams compared

Sterk describes each of his five diagrams as the diagram of the reflection subgroup of $G_v$ (4.3.5--4.3.9, pp. 19--24), with $G_v = \rho(\Stab_\Gamma(v))$ for $\Gamma = \gent$ and $v$ his isotropic representative. In the notation of [@AEGS25] that group is $\Gamma_{\En,2,v}$: with $\Gamma_\En = \Orth(T_\En)$, $\Gamma_\dP = \Orth(T_\dP)$ and $\gent = \Gamma_\En\cap\Gamma_\dP$ (Definition 2.6), the stabilizer of a primitive isotropic $v$ fits into
$$
0 \to U_v \to \Stab_{\gent}(v) \to \Gamma_{\En,2,v} \to 0,
$$
where $U_v$ acts trivially on $\bar T_\En = v^\perp(\text{in } T_\En)/\ZZ v$ (Definition 3.6). Two statements of that source fix the group and its generating set, and they replace the lift criterion this page carried before.

::: {.lemma #lem:sterk-reflection-lift-criterion title="The reflection subgroup at a cusp, after [@AEGS25]"}
Let $v$ be a primitive isotropic vector of $T_\En$, put $K = v^\perp/\ZZ v$ and $G_v = \Gamma_{\En,2,v}$. Then

1. $W(G_v)$ is generated by the reflections $s_\alpha$ in the roots $\alpha\in T_\En$ with $(\alpha,v) = 0$ ([@AEGS25], Definition 3.6). Each $s_\alpha$ is an isometry of $T_\En$ fixing $v$, hence acts on $K$; no lift of a root of $K$, and no condition on a discriminant image, is part of the definition.
2. The roots that occur are of the three types of ([@AEGS25], Lemma 3.4): a $(-2)$-root of $T_\dP$ lying in $T_\En$; a $(-4)$-root of $T_\dP$ lying in $T_\En$; and the folded vector $\alpha + I(\alpha)$ of a $(-2)$-root $\alpha$ of $T_\dP$ with $\alpha\cdot I(\alpha) = 0$, of square $-4$ in $T_\En$, which is a root of $T_\En$ and not of $T_\dP$.
3. The lifts in $v^\perp$ of a root $r$ of $K$ are $r + kv$, $k\in\ZZ$, and every one of them induces $s_r$ on $K$. Whether a lift is certified to lie in $\gent$ by the discriminant test --- that $\rho$ of it preserve both summands of $A_{T_\En} = \frac12U(2)/U(2)\oplus\frac12E_8(2)/E_8(2)$, which is Sterk's Proposition 2.7 --- need not be independent of $k$: at cusps $2$, $3$, $4$ and $5$ the record finds printed roots whose verdict changes with the lift, and at each of those cusps an element $u = s_{\alpha+kv}s_\alpha^{-1}$ which fixes $v$, acts trivially on $K$ and moves classes of $A_{T_\En}$, so that the kernel of $\Stab_{\Orth(T_\En)}(v)\to\Orth(K)$ has nontrivial image in $\Orth(A_{T_\En})$. (That $u$ fails the discriminant test itself, so it lies in this kernel and not necessarily in $U_v$; the image of $U_v$ is not computed here; it is one of the two operations owed below.) The discriminant verdict is therefore a property of a lift and not of the class, and no criterion stated on a single lift is the criterion.
:::

::: {.proof}
For (1) and (2) the citations are the whole proof: Definition 3.6 defines $W(\Gamma_{\En,2,v})$ as the group generated by the reflections in the roots of $T_\En$ orthogonal to $v$, and Lemma 3.4 classifies those roots. That $G_v$ is $\Gamma_{\En,2,v}$ is Sterk's identification of his $\Gamma$ with the level-two subgroup ([@Ste91], Proposition 2.7).

For (3), with $v = \eta_j$, the transcript `coble_sterk-root-lifts-run.txt` prints for each cusp and each of Sterk's printed roots the set of $k$ at which $r+kv$ is a root of $T_\En$, the set at which it is a root of $T_\dP$, and the set at which the discriminant test passes. The verdict on a printed root changes with the lift at the roots numbered $1$ to $9$ of cusp $2$, the roots $1$ to $7$ and $11$ of cusp $3$, the roots $1$ to $7$, $9$ and $11$ of cusp $4$ and the roots $7$ and $9$ of cusp $5$; at cusp $3$ the roots $6$, $7$ and $11$, and at cusp $4$ the roots $2$, $7$ and $11$, pass exactly at the lifts of odd $k$ and fail at $k = 0$. Every condition involved is a parity condition in $k$ --- the reflection in a vector of square $q<0$ is an integral isometry of a lattice exactly when $(-q/2)$ divides all its pairings with that lattice --- and the $E_8(2)$ coordinates shift by $k$ times those of $v$, so the set of admissible $k$ is empty, one parity class or all of $\ZZ$, and the swept range $[-6,6]$ decides it for every $k$. For the last clause the transcript verifies $uv = v$ and $ub - b\in\ZZ v$ for the ten basis vectors of $K$, then prints $\rho(u)$ on the ten classes of $A_{T_\En}$: at cusp $3$ the images are $\{334,333,4,8,347,32,64,128,256,847\}$ against $\{1,2,4,8,16,32,64,128,256,512\}$ for the identity, which is nontrivial and does not preserve the two summands.
:::

::: {.remark title="Two withdrawn statements of this page"}
An earlier version of @lem:sterk-reflection-lift-criterion asked whether a *lift* of a root of $K$ has a discriminant image preserving the two summands, presented that as a sufficient condition for $s_r\in G_v$, asserted the answer independent of the choice of lift, and described a subfamily of the kernel as $\ell = c\,(\eta,\cdot)$; that subfamily is the zero map, since $(\eta,x) = 0$ for every $x\in\eta^\perp$, so it certifies nothing. Under (1) the criterion needs no lift at all, and under (3) the independence the lemma claimed is exactly what the record refutes. Both statements are withdrawn.
:::

::: {.theorem #thm:sterk-reflection-subgroups title="The five published diagrams are the five Enriques folded diagrams"}
Let $\eta_1,\dots,\eta_5$ be the representatives Sterk uses in 4.3.5--4.3.9, put $K_j = \eta_j^\perp/\ZZ\eta_j$, and let $R_j$ be his printed root set beside Fig. 4, 6, 8, 10 or 12. Then

- the five cusps are the five $M$-orbits of isotropic classes of $A_{T_\En}$, of sizes $1,\,2,\,120,\,270,\,135$ for $j = 1,\dots,5$; his representative and the representative written on this page lie in the same orbit at every $j$; and the class stabilizers have orders $696\,729\,600$, $348\,364\,800$, $5\,806\,080$, $2\,580\,480$, $5\,160\,960$;
- every vector of every $R_j$ lies in $\eta_j^\perp$ and has square in $\set{-2,-4}$, and its reflection is an integral isometry of $T_\En$ --- the divisibility in $T_\En$ of a $(-4)$-root is $2$ and that of a $(-2)$-root $1$ --- so it is a root of $T_\En$ and a member of the generating set of @lem:sterk-reflection-lift-criterion(1) at its own cusp;
- the Coxeter diagram of $W(G_v)$ at cusp $j$ is the folded diagram $G(\bar T_\dP)^{J_j}$ of [@AEGS25], folded from the two diagrams $G(\bar T_\dP)$ of their Fig. 5: $J_2$ is the reflection $J\colon\alpha_k\mapsto\alpha_{20-k}$ on the diagram of $(18,0,0)_1$ in their Lemma 3.9, with the folded diagram in their Fig. 7, and $J_1, J_3, J_4, J_5$ are the four involutions of the diagram of $(18,2,0)_1$ in their Lemma 3.10, with the folded diagrams in their Fig. 8; their Corollary 3.12 states that these five folded diagrams are exactly the diagrams of the five groups $W(\Gamma_{\En,2,e})$, and §3.8 states that they are the diagrams Sterk computed;
- against his printed roots the identification holds in every invariant the record computes:

| $j$ | Sterk's figure | $\abs{R_j}$ | certified at $k = 0$ | certified only at $k\neq0$ | weights | finite $+$ ideal vertices | $f_0$ of the recorded CoxIter run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 12 | 12 | --- | $\set{3{:}10,\infty{:}3}$ | $14+9$ | 23 |
| 2 | 6 | 10 | 10 | --- | $\set{3{:}8,4{:}1}$ | $8+2$ | 10 |
| 3 | 8 | 12 | 9 | $6,7,11$ | $\set{3{:}7,4{:}4,\infty{:}1}$ | $29+4$ | 33 |
| 4 | 10 | 11 | 8 | $2,7,11$ | $\set{3{:}8,4{:}2}$ | $21+5$ | 26 |
| 5 | 12 | 14 | 14 | --- | $\set{3{:}8,4{:}8,\infty{:}1}$ | $102+13$ | 115 |

and these are the vertex counts of the polytopes his walls bound, the totals being the $f_0$ of the CoxIter runs recorded for the same figures in [@sec-coxiter-results-for-cusp-lattices].
:::

::: {.proof}
The orbits, the representatives' classes and the stabilizer orders are in `coble_sterk-reflection-subgroups-run.txt`, which prints them from the nine recorded elements generating $M$; the squares, the divisibilities in $T_\En$ and the two certification columns are in `coble_sterk-root-lifts-run.txt`, whose rows are Sterk's printed roots in the frame $\eta_j^\perp = \ZZ\eta_j\oplus K_j$. The weights, the finite and ideal vertex counts are in the first transcript: for a set of roots of $K_j$ the vertex rays of $\set{x : b(x,r)\le 0}$ are the extreme rays of the polar of the cone the roots positively span, which the record obtains from the `Cone(...).dual()` call, and a ray is finite or ideal according as its square is negative or zero. The identification of the diagrams is the cited statement of [@AEGS25] and is not re-derived here.
:::

::: {.remark title="Third-type roots need no divisibility condition"}
Let $\alpha$ be a $(-2)$-root of $T_\dP$ with $\alpha\cdot I(\alpha) = 0$ and let $\alpha_I = \alpha + I(\alpha)$ be the folded vector of @lem:sterk-reflection-lift-criterion(2): a root of $T_\En$ of square $-4$ whose divisibility in $T_\dP$ is $1$, so that $s_{\alpha_I}$ is not itself an isometry of $T_\dP$. The product $s_\alpha s_{I(\alpha)}$ is one --- both factors are $(-2)$-reflections of $T_\dP$ --- and it commutes with $I$, since $I s_\alpha I = s_{I(\alpha)}$ and the two factors commute because $\alpha\cdot I(\alpha) = 0$. It therefore preserves $T_\En = T_\dP^{I=1}$; and for $x\in T_\En$ one has $x\cdot I(\alpha) = I(x)\cdot I(\alpha) = x\cdot\alpha$, so
$$
s_\alpha s_{I(\alpha)}(x) = x + (x\cdot\alpha)\,\alpha + (x\cdot\alpha)\,I(\alpha) = x + \tfrac12 (x\cdot\alpha_I)\,\alpha_I = s_{\alpha_I}(x).
$$
So $s_{\alpha_I}$ extends to an isometry of $T_\dP$, and lies in $\gent$ by Definition 2.6 of [@AEGS25] --- the extension being the product and not the reflection --- and the divisibility of $\alpha_I$ in $T_\dP$ is irrelevant to that. The record repeats the construction at a printed root of this type at each cusp: it builds $\alpha$ from $\alpha_I$ in the block form of ([@AEGS25], Definition 2.3), checks $\alpha^2 = -2$, $\alpha\cdot I(\alpha) = 0$ and $\alpha + I(\alpha) = \alpha_I$, and verifies that the product is an integral isometry of $T_\dP$ commuting with $I$ and acting on $T_\En$ as $s_{\alpha_I}$. What the record does record, and what (3) says, is the different fact that the *discriminant* verdict on a lift is lift-dependent: that is a property of the test, not of membership in $\gent$.
:::

::: {.remark title="The chambers owed at cusps 1, 3 and 4"}
The record gives, at every cusp, Sterk's wall set, the Gram matrix of those walls and the vertex counts of the polytope they bound. It does not give the polyhedron as a chamber of the group in the coordinates of this tree at cusps $1$, $3$ and $4$: that needs two library operations which do not exist, the group $G_v$ together with the image of $U_v$ ([sage-extensions#312](https://github.com/dzackgarza/sage-extensions/issues/312)) and a chamber for a prescribed subgroup ([sage-extensions#297](https://github.com/dzackgarza/sage-extensions/issues/297)). At cusps $2$ and $5$ the recorded restricted search, with the reflection set cut down to the printed roots, does close with the published wall and ideal-vertex counts.
:::

::: {.remark title="No disagreement with Sterk is claimed here"}
An earlier version of this page reported cusp $3$ as the cusp where the published figure and a computed chamber differ, on the strength of a $14$-wall chamber obtained by searching for the roots that the discriminant criterion certified as it was then stated. That criterion is withdrawn (@lem:sterk-reflection-lift-criterion(3)) and the search with it: under @thm:sterk-reflection-subgroups his twelve walls are the walls of the diagram $G(\bar T_\dP)^{J_3}$, and no larger certified set is compared with his figure here.
:::

::: {.remark title="What remains of @qst:sterk-reflection-subgroup"}
The identification of $W_j$ is the source's, by @thm:sterk-reflection-subgroups; what @qst:sterk-reflection-subgroup asks for beyond that is the index $[W(\eta_j^\perp/\eta_j) : W_j]$, a covolume ratio which the Euler characteristic does not supply in odd dimension, and the writing of the published domain as a union of chambers of the full group, which needs a chamber at cusps $1$, $3$ and $4$ (the two operations cited above).
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
