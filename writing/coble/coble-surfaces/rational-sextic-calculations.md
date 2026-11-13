# Rational Sextic Calculations

::: {.lemma #lem:rational_sextic_ten_nodes}

Let $C \subset \PP^2$ be an irreducible sextic curve with at worst $A_1$ singularities.
Then $C$ is a rational curve if and only if it has exactly ten $A_1$ singularities.
:::

::: {.proof}

Recall the genus–degree formula for singular plane curves:

$$
p_a(C) = {1\over 2}(d-1)(d-2) - \Sum_p \delta_p
$$

where the sum is over the singular locus of $C$.
Since $C$ has at worst $A_1$ singularities, each singularity contributes $\delta_p = 1$.
Noting that $d=6$, we obtain the geometric genus $g = 10 - k$, where $k$ is the number of $A_1$ singularities.
Thus $g = 0$ if and only if $k = 10$.
:::

::: {.proposition #prop:rational-sextic-severi title="The Severi variety of rational sextics"}

1. Let $S_{6,0}\iscontainedin\PP^{27}$ be the Severi variety of rational plane sextics. It is irreducible of dimension $17$ and degree $26312976$. Its general member has exactly $10$ nodes, and the set of these $10$ nodes determines the curve [@BHO+12, §4, proof of Thm. 2].
2. There is a rational cuspidal plane sextic over $\CC$ whose only singular point is a cusp with multiplicity sequence $[5]$ [@GK20, Thm. 1.1, Thm. 3.1]. It does not have ten $A_1$ singularities.

:::

::: {.proposition #prop:coble-canonical-class title="Canonical class of the blowup of the ten nodes"}

Let $W\subset \PP^2$ be an irreducible sextic whose singular points are exactly ten $A_1$ singularities $p_1, \ldots, p_{10}$.
Let $\pi\colon S\to\PP^2$ be the blowup of $p_1, \ldots, p_{10}$, with geometric basis $e_0, \ldots, e_{10}$ as in @prop:blowup-geometric-basis, and let $C$ be the proper transform of $W$.
Then
$$
K_S = -3e_0 + \Sum_{k=1}^{10} e_k,
\qquad
K_S^2 = -1,
\qquad
C \sim 6e_0 - 2\Sum_{k=1}^{10} e_k = -2K_S
.
$$
The surface $S$ is a Coble surface [@DK13, §3].
Coble studied the sets of ten nodes of rational sextics in [@Cob19].

:::

::: {.proof}

The formula for $K_S$ is @prop:blowup-geometric-basis (2).
By @prop:blowup-geometric-basis (1),
$$
K_S^2 = 9e_0^2 + \Sum_{k=1}^{10} e_k^2 = 9 - 10 = -1
.
$$
An $A_1$ singularity of a plane curve is a double point, so $W$ has multiplicity $2$ at each $p_k$.
The points $p_k$ are distinct points of $\PP^2$, so each blowup is an isomorphism near the other points, and the proper transform of $W$ still has multiplicity $2$ at each point blown up later.
By [@Har77, V.3.6], the pullback of a curve under the blowup of a point of multiplicity $r$ on it is its proper transform plus $r$ times the exceptional curve.
Applied ten times, with $W\sim 6h$ for the class $h$ of a line [@Har77, II.6.4], this gives $6e_0 = C + 2\Sum_{k=1}^{10} e_k$ in $\Pic(S)$, so $C \sim 6e_0 - 2\Sum_k e_k = -2K_S$.

:::

::: {.proposition #prop:antibicanonical-curve title="Invariants of an antibicanonical curve"}

Let $S$ be a Coble surface of K3 type with $K_S^2 = -1$, and let $C\in\abs{-2K_S}$ be an integral curve.
Then $C$ is a smooth rational curve and $C^2 = -4$.

:::

::: {.proof}

By [@Har77, V Ex. 1.3(a)], $2p_a(C) - 2 = C\cdot(C + K_S)$.
With $C \sim -2K_S$ this gives
$$
p_{a}(C)=1+\frac{1}{2}\qty{ C^{2}+C \cdot K_{S} } = 1 + \frac12\qty{4K_S^2 - 2K_S^2} = 1+K_{S}^{2}=0
.
$$
An integral projective curve with $p_a = 0$ is nonsingular and isomorphic to $\PP^1$ [@Har77, IV Ex. 1.8(b)].
Finally $C^2 = 4K_S^2 = -4$.

:::

## The configuration constraint on the ten nodes

::: {.proposition #prop:sextic-node-conditions title="Ten nodes impose more conditions than the linear system has"}

The space of plane sextics is
$$
\dim_\CC H^0\bigl(\PP^2, \OO_{\PP^2}(6)\bigr) = \binom{8}{2} = 28
,
$$
so sextic curves form a $\PP^{27}$.
Requiring a singular point at a prescribed $p\in\PP^2$ imposes at most three linear conditions on this space.
A sextic singular at all of $p_1, \ldots, p_{10}$ exists if and only if the resulting thirty conditions have rank at most $27$.
There is a nonempty Zariski-open subset $\mathcal U\iscontainedin(\PP^2)^{10}$ such that for $(p_1, \ldots, p_{10})\in\mathcal U$ the thirty conditions have rank $28$, and no sextic is singular at all ten points.
:::

::: {.proof}

The monomials $x^iy^jz^k$ with $i+j+k=6$ number $\binom{6+2}{2} = 28$, giving the stated dimension.
For a fixed $p$, singularity of $\theset{F = 0}$ at $p$ is the vanishing of the three partial derivatives $\del_x F(p)$, $\del_y F(p)$, $\del_z F(p)$; each is a linear condition on the coefficients of $F$, and $F(p) = 0$ follows from Euler's identity $\Sum_i x_i\,\del_i F = 6F$.
Choose representatives $\tilde p_i\in\CC^3\setminus\theset{0}$ of the points $p_i$.
The thirty conditions form the linear map $M(\tilde p_1, \ldots, \tilde p_{10})\colon H^0\bigl(\PP^2, \OO_{\PP^2}(6)\bigr)\cong\CC^{28}\to\CC^{30}$ that sends $F$ to the values of $\del_x F$, $\del_y F$, $\del_z F$ at the $\tilde p_i$.
A sextic singular at all ten points is a nonzero vector of its kernel, and the kernel is nonzero if and only if the rank is at most $27$.

The partial derivatives are homogeneous of degree $5$, so replacing $\tilde p_i$ by $\lambda\tilde p_i$ multiplies three rows by $\lambda^5$ and does not change the rank.
The locus where the rank is $28$ is the complement of the common zero set of the $28\times 28$ minors, which are polynomials in the coordinates of the $\tilde p_i$; it therefore descends to a Zariski-open subset $\mathcal U\iscontainedin(\PP^2)^{10}$.
The subset $\mathcal U$ is nonempty by @ex:sextic-node-conditions-rank.
:::

::: {.example #ex:sextic-node-conditions-rank title="Ten points at which the node conditions have full rank"}

For the ten points
$$
(1:0:0),\ (0:1:0),\ (0:0:1),\ (1:1:1),\ (1:2:3),\ (1:-1:2),\ (2:1:-1),\ (1:3:-2),\ (3:-2:1),\ (1:4:5)
$$
the $30\times 28$ matrix over $\QQ$ of the map $M$ of @prop:sextic-node-conditions, in the monomial basis $x^iy^jz^{6-i-j}$, has rank $28$.
This is a computation in SageMath with exact rational arithmetic.
:::

::: {.proposition #prop:sextic-equisingular-dimension title="Dimension of the space of sextics of a fixed singular type"}

Let $Z$ be a reduced plane sextic with only simple singularities, with root lattices $R_1, \ldots, R_m$, and let $T$ be its singular type.
Then $\PP\mcv_T$ (@not:sextic-singular-type) is a smooth irreducible quasi-projective variety of the expected dimension
$$
\binom{6+2}{2} - 1 - \Sum_{i=1}^m \rank(R_i) = 27 - \Sum_{i=1}^m \rank(R_i)
,
$$
and its points are stable for the action of $\SL_3$ on $\bigl(\PP H^0(\PP^2, \OO_{\PP^2}(6)), \OO(1)\bigr)$ [@YZZ25, §2.1].

:::

::: {.corollary #cor:ten-nodal-sextic-dimension title="Dimension of the space of ten-nodal sextics"}

For a singular type $T$ with root lattice $A_1^{\oplus 10}$, $\dim\PP\mcv_T = 17$.
This is the dimension of the Severi variety $S_{6,0}$ of @prop:rational-sextic-severi.

:::

::: {.proof}

Each $A_1$ has rank $1$, so $\Sum_i\rank(R_i) = 10$, and @prop:sextic-equisingular-dimension gives $27 - 10 = 17$.
The second statement is @prop:rational-sextic-severi (1).

:::

## A criterion for a node of a plane curve

::: {.proposition #prop:hessian-rank-at-singular-point title="Hessian rank at a singular point"}

Let $k$ be a field, let $F\in k[x_0, x_1, x_2]$ be homogeneous of degree $n$, and let $p\in k^3$ be nonzero with
$$
\del_j F(p) = 0
\qquad\text{for } j = 0, 1, 2
.
$$
Then the Hessian matrix $H(F)(p) = \bigl(\del_i\del_j F(p)\bigr)_{ij}$ satisfies $H(F)(p)\cdot p = 0$, and hence
$$
\rank H(F)(p) \leq 2
.
$$
:::

::: {.proof}

Euler's identity for a homogeneous polynomial of degree $n$ reads $\Sum_i x_i\,\del_i F = n F$.
Differentiating it by $\del_j$ gives the polynomial identity
$$
\Sum_i x_i\,\del_j\del_i F \;+\; \del_j F \;=\; n\,\del_j F
,
$$
that is $\Sum_i x_i\,\del_i\del_j F = (n-1)\,\del_j F$.
Evaluating at $p$, where every first partial vanishes, gives $H(F)(p)\cdot p = 0$.
Since $p\neq 0$ the kernel of $H(F)(p)$ is nonzero, so by rank-nullity in dimension $3$ the rank is at most $2$.
:::

