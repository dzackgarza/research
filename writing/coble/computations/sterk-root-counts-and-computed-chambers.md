---
unit: computation
status: open
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

Related: [CoxIter results for cusp lattices](#sec-coxiter-results-for-cusp-lattices), [root vectors and folded Sterk diagrams](#sec-root-vectors-and-folded-sterk-diagrams), [fundamental chamber polyhedra](#sec-fundamental-chamber-polyhedra), [cusp-correspondence morphism chain](#sec-cusp-correspondence-morphism-chain).
