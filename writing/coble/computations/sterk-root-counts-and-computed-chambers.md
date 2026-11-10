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

::: {.proposition #prop:sterk-cusp-quotients title="The five cusps and their hyperbolic quotients"}

Let $\Gamma$ be Sterk's group, identified with $\gent$ in @prop:sterk-group-identification.
Every primitive isotropic vector of $\ten = U\oplus E_{10}(2)$ lies in the $\Gamma$-orbit of exactly one of
$$
\eta_1 = e,\quad
\eta_2 = e',\quad
\eta_3 = e'+f'+\omega,\quad
\eta_4 = e'+2f'+\alpha,\quad
\eta_5 = 2e+2f+\alpha,
$$
with $\omega = 2w_8$ and $\alpha = 2w_1$ in the dual basis ([Coble lattice isotropic candidates](#sec-coble-lattice-isotropic-candidates)) [@Ste91, Prop. 4.2.3].
Each quotient $\eta_j^{\perp}/\eta_j$ is a hyperbolic lattice of rank $10$, so it determines a copy of $\HH^9$ (@def:hyperbolic-model), and
$$
\eta_1^{\perp}/\eta_1 \cong U(2)\oplus E_8(2) = E_{10}(2),
\qquad
\eta_j^{\perp}/\eta_j \cong U\oplus E_8(2) \quad (j = 2,3,4,5)
$$
[@Ste91, Lem. 4.3.4].
These lattices are even and $2$-elementary (@def:p-elementary) of types $(10,10,0)$ and $(10,8,0)$ respectively.
:::

::: {.proof}

The orbit statement and the two isometries are the cited results.
For an even unimodular lattice $N$, the discriminant group of $N(2)$ is $\tfrac12 N(2)/N(2)\cong(\ZZ/2)^{\rank N}$, and its quadratic form takes the value $\tfrac12 y^2_N\in\ZZ$ on the class of $\tfrac12 y$, because $N$ is even.
The lattice $U$ is unimodular, and $U(2)$ and $E_8(2)$ are of the form $N(2)$, so $A_{U(2)\oplus E_8(2)}\cong(\ZZ/2)^{10}$ and $A_{U\oplus E_8(2)}\cong(\ZZ/2)^{8}$, both with quadratic values in $\ZZ/2\ZZ\subseteq\QQ/2\ZZ$.
By the definition of the coparity in @thm:two-elementary-classification, $\delta = 0$ in both cases.
:::

::: {.proposition #prop:sterk-reflection-subgroup-diagrams title="Sterk's diagrams of the reflection subgroups"}

For $v = \eta_j$, let $G_v$ be the image in $\Orth(v^{\perp}/\ZZ v)$ of the stabilizer of $v$ in $\Gamma$, and let $W_v\leq G_v$ be its reflection subgroup.
The Coxeter diagram of $W_{\eta_j}$ has $12, 10, 12, 11, 14$ nodes for $j = 1,\dots,5$.
The squares of the corresponding roots are, in the same order,
$12\times(-4)$; $9\times(-4)$ and $1\times(-2)$; $10\times(-4)$ and $2\times(-2)$; $9\times(-4)$ and $2\times(-2)$; and $10\times(-4)$ and $4\times(-2)$
[@Ste91, §§4.3.5--4.3.9, Figs. 4, 6, 8, 10, 12].
:::

| Cusp | Nodes of the Sterk diagram | Vinberg walls | Ideal vertices of the Vinberg chamber |
| --- | --- | --- | --- |
| 1 | 12 | 10 | 1 |
| 2 | 10 | 10 | 2 |
| 3 | 12 | 10 | 2 |
| 4 | 11 | 10 | 2 |
| 5 | 14 | 10 | 2 |

## The computed chambers are hyperbolic simplices

::: {.proposition #prop:nine-roots-insufficient title="A finite-volume chamber in $\HH^9$ has at least ten walls"}

Let $P\iscontainedin\HH^n_L$ be a Coxeter polytope (@def:coxeter-polytope) of finite volume. Then $P$ has at least $n+1$ walls. In particular a finite-volume Coxeter polytope in $\HH^9_L$ has at least $10$ walls.
:::

::: {.proof}

Fix $v_0\in C_L^+$ and use the affine chart $A\definedas\theset{v\in L_\RR \mid \beta_L(v,v_0) = 1}\cong\RR^n$ of $\PP(L_\RR)$. It meets every line of the closed positive cone in one point, so the projective model $\BB^n_L$ of @def:hyperbolic-model is an open ball $B\iscontainedin A$ with boundary sphere $\partial B$, the image of the isotropic cone. Let $\alpha_1,\dots,\alpha_k$ be the roots of the walls of $P$ and $\ell_i\definedas\beta_L(\cdot,\alpha_i)$, affine functions on $A$, signed so that $P = B\intersect Q$ with $Q\definedas\theset{x\in A \mid \ell_i(x)\geq0 \text{ for all } i}$.

*The closure is a polytope.* By @thm:coxeter-polytope-volume(1) the closure $\overline P$ of $P$ in $A$ is the convex hull of finitely many points, so it is a polytope [@Zie95, Thm. 2.15]. It is $n$-dimensional, because $P$ is a fundamental domain of a properly discontinuous action and so has nonempty interior.

*Each facet lies in a wall.* Let $F$ be a facet of $\overline P$, with affine hull the hyperplane $\operatorname{aff}F$. The set $\operatorname{aff}F\intersect\partial B$ is a sphere of dimension at most $n-2$ or empty, so it has empty interior in $\operatorname{aff}F$, and the relative interior of $F$ contains a point $x\in B$. Near $x$ the sets $\overline P$ and $Q$ agree, because $\overline P\intersect B = P = B\intersect Q$; so $x$ lies in the boundary of $Q$ and $\ell_i(x) = 0$ for some $i$. The same holds at every point of the dense open subset $F^\circ\setminus\partial B$ of the relative interior $F^\circ$ of $F$, so the closed subsets $F\intersect\theset{\ell_i = 0}$, $1\leq i\leq k$, cover $F$. One of them has nonempty interior in $F$, and then $\operatorname{aff}F = \theset{\ell_i = 0}$. Distinct facets have distinct affine hulls, so $F\mapsto\alpha_i$ is an injection from the set of facets of $\overline P$ to the set of walls of $P$.

*An $n$-polytope has at least $n+1$ facets.* By [@Zie95, Thm. 2.15(7)], $\overline P = \theset{x \mid u_j(x)\leq c_j,\ 1\leq j\leq m}$, one inequality for each of its $m$ facets, with $u_j$ linear. Suppose $m\leq n$. If $u_1,\dots,u_m$ span a subspace of dimension less than $n$, choose $d\neq0$ with $u_j(d) = 0$ for all $j$; otherwise $m = n$, the $u_j$ form a basis of the dual space, and there is $d$ with $u_j(d) = -1$ for all $j$. In both cases $x+td\in\overline P$ for every $x\in\overline P$ and $t\geq0$, which contradicts boundedness. So $m\geq n+1$.

Hence $k\geq m\geq n+1$, and $k\geq10$ when $n = 9$.
:::

::: {.corollary #cor:ten-walls-is-simplex title="Exactly ten walls means a simplex"}

A finite-volume Coxeter polytope in $\HH^9$ with exactly $10$ walls is a $9$-simplex, the case of @cor:coxeter-simplex-volume.
Its face numbers are $f_k = \binom{10}{k+1}$, that is
$$
(f_0,\dots,f_9) = (10, 45, 120, 210, 252, 210, 120, 45, 10, 1).
$$
:::

::: {.proof}

By @thm:coxeter-polytope-volume(1) the closure $\overline P$ of the polytope in the projective model is a compact convex $9$-dimensional polytope with $10$ facets.
In an affine chart with an interior point of $\overline P$ as origin, the polar polytope of $\overline P$ is a $9$-dimensional polytope with one vertex for each facet of $\overline P$, so it has $10$ vertices.
Ten points that span an affine space of dimension $9$ are affinely independent, so the polar polytope is a $9$-simplex, and $\overline P$, the polar of a simplex, is a $9$-simplex.
The $k$-faces of a $9$-simplex correspond to the $(k+1)$-element subsets of its $10$ vertices, which gives $f_k = \binom{10}{k+1}$.
:::

::: {.example #ex:coxiter-f-vectors-of-sterk-diagrams title="Face numbers of the folded Sterk diagrams"}

CoxIter returns the simplex $f$-vector of @cor:ten-walls-is-simplex for the folded Sterk 2 diagram and for both rank-$10$ $0$-cusp diagrams $(10,8,0)_1$ and $(10,10,0)_1$ ([CoxIter results for cusp lattices](#sec-coxiter-results-for-cusp-lattices)).
For the Sterk 1, 3, 4 and 5 diagrams it returns $f_0 = 23, 33, 26, 115$, so those four polyhedra have more vertices than a simplex.
:::

::: {.example #ex:vinberg-chambers-of-cusp-quotients title="Chambers of the rank-$10$ quotient lattices"}

CoxIter, run on the $0$-cusp diagram of $(10,10,0)_1$, returns dimension $9$, one vertex at infinity, Gram field $\QQ$, and the simplex $f$-vector; run on $(10,8,0)_1$ it returns dimension $9$, two vertices at infinity, Gram field $\QQ[\sqrt2]$, and the same $f$-vector.
Vinberg's algorithm on $\eta_1^{\perp}/\eta_1 \cong E_{10}(2)$, of type $(10,10,0)$, returns ten roots and one ideal vertex; on $\eta_j^{\perp}/\eta_j\cong U\oplus E_8(2)$, of type $(10,8,0)$, it returns ten roots and two ideal vertices for each of $j = 2,3,4,5$.
:::

::: {.lemma #lem:computed-chamber-roots-gram title="The ten roots and their Gram matrix"}

Let $E_8$ be negative-definite, let $N_1 = U(2)\oplus E_8(2)$ and $N_2 = U\oplus E_8(2)$, and for $c = 1,2$ let $\eps_1,\eps_2$ be the isotropic basis of the hyperbolic summand of $N_c$, so that $\eps_1\cdot\eps_2 = 2$ in $N_1$ and $\eps_1\cdot\eps_2 = 1$ in $N_2$.
Let $\eps_{2+i} = \alpha_i$ for the simple roots $\alpha_1,\dots,\alpha_8$ of $E_8(2)$ in Bourbaki numbering, and set
$$
r_c = c\,\eps_2 + 2\eps_3 + 3\eps_4 + 4\eps_5 + 6\eps_6 + 5\eps_7 + 4\eps_8 + 3\eps_9 + 2\eps_{10}.
$$
The coefficients $(2,3,4,6,5,4,3,2)$ are the marks of the highest root of $E_8$.
Consider the ten vectors
$$
-\eps_3,\ -\eps_4,\ \dots,\ -\eps_{10},
\qquad
\eps_1 - \eps_2,
\qquad
r_c
$$
of $N_c$.

1. In $N_1$ all ten have square $-4$ and divisibility $2$, so they are long roots (@def:2elementary-roots). They form a $\ZZ$-basis of $N_1$, and their Coxeter diagram is $T_{2,3,7}$ with every edge of label $3$.
2. In $N_2$ the vector $\eps_1-\eps_2$ has square $-2$ and is a short root, and the other nine have square $-4$ and divisibility $2$ and are long roots. They span a sublattice of index $2$ in $N_2$. Their Coxeter diagram has the same underlying graph as in (1), with label $4$ on the edge joining $\eps_1-\eps_2$ and $r_2$ and label $3$ on every other edge.
3. In both cases distinct vectors of the list have products in $\{0,2\}$.
:::

::: {.proof}

Order the vectors as $-\eps_3,\dots,-\eps_{10},\ \eps_1-\eps_2,\ r_c$.
In $N_1$ their Gram matrix is
$$
\begin{pmatrix}
-4 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & -4 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0\\
2 & 0 & -4 & 2 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 2 & 2 & -4 & 2 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 2 & -4 & 2 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 2 & -4 & 2 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 2 & -4 & 2 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 2 & -4 & 0 & 2\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & -4 & 2\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 2 & -4
\end{pmatrix},
$$
and in $N_2$ it is the same matrix with the entry in position $(9,9)$ replaced by $-2$.
The matrix expressing the ten vectors in the basis $\eps_1,\dots,\eps_{10}$ has determinant $1$ for $c=1$ and $2$ for $c=2$, which gives the $\ZZ$-basis in (1) and the index in (2).

Every product of two vectors of $N_1 = (U\oplus E_8)(2)$ is even, so every vector of $N_1$ has even divisibility; the ten vectors are primitive, so each has divisibility $2$.
In $N_2$ the vectors $-\eps_{2+i}$ are orthogonal to $U$ and pair evenly with $E_8(2)$, and $r_2$ has $r_2\cdot\eps_1 = 2$, $r_2\cdot\eps_2 = 0$ and pairs evenly with $E_8(2)$; so these nine vectors have divisibility $2$.

The bond invariant of @def:bond-invariant is $t = 4\cdot 2^2/((-4)(-4)) = 1$ for two vectors of square $-4$ with product $2$, which is label $3$, and $t = 4\cdot 2^2/((-2)(-4)) = 2$ for $\eps_1-\eps_2$ and $r_2$ in $N_2$, which is label $4$.
The nonzero off-diagonal entries join $-\eps_3,-\eps_5,-\eps_6,-\eps_7,-\eps_8,-\eps_9,-\eps_{10},\ r_c,\ \eps_1-\eps_2$ in a chain, with $-\eps_4$ attached to $-\eps_6$.
The three arms at $-\eps_6$ have $2$, $3$ and $7$ nodes counted with $-\eps_6$, which is the graph $T_{2,3,7}$.
:::

::: {.example #ex:computed-chamber-simple-roots title="The simple roots of the computed chambers"}

Under the isometries of @prop:sterk-cusp-quotients, $\eta_1^{\perp}/\eta_1\cong N_1$ and $\eta_2^{\perp}/\eta_2\cong N_2$ in the notation of @lem:computed-chamber-roots-gram.
The ten roots that Vinberg's algorithm returns for $\eta_1^{\perp}/\eta_1$ are the ten vectors of @lem:computed-chamber-roots-gram with $c = 1$, and those for $\eta_2^{\perp}/\eta_2$ are the ten vectors with $c = 2$.
For $\eta_2$ the squares are $9\times(-4)$ and $1\times(-2)$, the same as for Sterk's cusp-$2$ diagram in @prop:sterk-reflection-subgroup-diagrams.
:::

## The question the discrepancy poses

::: {.question #qst:sterk-reflection-subgroup title="Which reflection group does each published diagram bound a domain for?"}

The lattices $\eta_j^{\perp}/\eta_j$ for $j = 2,3,4,5$ are mutually isometric, so their full Weyl groups $W(\eta_j^{\perp}/\eta_j)$ (@def:reflection) are conjugate and their Vinberg chambers are isometric.
The published diagrams for those four cusps have $10, 12, 11, 14$ walls and $2, 4, 5, 13$ vertices at infinity, so no two of the last three are isometric to each other or to the ten-wall chamber.
A datum beyond the isometry class of $\eta_j^{\perp}/\eta_j$ therefore distinguishes them, and the candidate is the group: for each $j$, identify the subgroup $W_j \leq W(\eta_j^{\perp}/\eta_j)$ for which the published diagram is a Coxeter polytope (@def:coxeter-polytope), and exhibit the published domain as a union of chambers of the full group.

The natural candidate for $W_j$ is the reflection subgroup induced on $\eta_j^{\perp}/\eta_j$ by the stabilizer of $\eta_j$ in the arithmetic group acting on $\ten$, which depends on how the quotient sits inside $\ten$ and not only on its isometry class.
:::

::: {.question #qst:sterk-ideal-vertices title="How do the ideal vertices correspond?"}

The computed chambers have one or two isotropic rays, and the published diagrams have $9, 2, 4, 5, 13$ vertices at infinity.
For a chamber of finite volume, the ideal vertices correspond bijectively to the maximal parabolic subdiagrams of its Coxeter--Vinberg diagram, all of rank $n-1$, and each is the line of a primitive isotropic vector of $\eta_j^{\perp}/\eta_j$; the orbits, under the arithmetic group acting on $\ten$, of the corresponding primitive totally isotropic sublattices of rank $2$ containing $\ZZ\eta_j$ are the $1$-cusps incident to the $0$-cusp of $\eta_j$ (@prop:maximal-parabolic-ideal-vertices).
Under a chamber decomposition answering @qst:sterk-reflection-subgroup, determine which ideal vertices of the union are ideal vertices of the constituent chambers and which arise on interior walls.
:::

::: {.example #ex:gram-fields-of-sterk-diagrams title="Gram fields of the folded Sterk diagrams"}

CoxIter returns Gram field $\QQ$ for the folded Sterk 1 diagram and for $(10,10,0)_1$, and $\QQ[\sqrt2]$ for the other four folded diagrams and for $(10,8,0)_1$ and $(9,9,1)_1$.
Here $\sqrt2 = 2\cos(\pi/4)$ comes from the label-$4$ bonds of these diagrams.
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

Related: [CoxIter results for cusp lattices](#sec-coxiter-results-for-cusp-lattices), [root vectors and folded Sterk diagrams](#sec-root-vectors-and-folded-sterk-diagrams), [fundamental chamber polyhedra](#sec-fundamental-chamber-polyhedra), [cusp-correspondence morphism chain](#sec-cusp-correspondence-morphism-chain).
