# Rational Sextic Calculations

::: {.lemma #lem:rational_sextic_ten_nodes}

Let $C \subset \PP^2$ be an irreducible sextic curve with at worst $A_1$ singularities.
Then $C$ is a rational curve if and only if it has exactly ten $A_1$ singularities.
:::

::: {.proof}

Let $\nu\colon\widetilde C\to C$ be the normalization. For an integral plane curve of degree $d$, the plane genus formula gives $p_a(C)=(d-1)(d-2)/2$. The cokernel of $\OO_C\to\nu_*\OO_{\widetilde C}$ has length $\delta_p$ at each singular point $p$. Taking Euler characteristics gives
$$
g(\widetilde C)=p_a(C)-\sum_{p\in C^{\rm sing}}\delta_p.
$$
A node contributes one. Thus a sextic with $n$ nodes and no other singularities has arithmetic genus $10$ and normalization of genus $10-n$. Over $\CC$ the normalization is rational exactly when this genus is zero [@stacks-0CE0].
:::

::: {.example #ex:explicit-ten-nodal-sextic title="An explicit ten-nodal sextic and its K3 cover"}

Over $\CC$, consider the image of $\PP^1$ under the degree-six forms
$$
\begin{aligned}
f_0&=s^6+s^5t+2s^4t^2+3s^3t^3+2s^2t^4+st^5+t^6,\\
f_1&=2s^6+3s^5t+s^4t^2+2s^3t^3+3s^2t^4+st^5+2t^6,\\
f_2&=3s^6+2s^5t+3s^4t^2+s^3t^3+2s^2t^4+3st^5+t^6.
\end{aligned}
$$
Its reduced image $W$ is an irreducible rational sextic with exactly ten ordinary nodes. Its equation is $F=\sum_{i+j+k=6}a_{ijk}x^iy^jz^k$, where for $k=0,\ldots,6$ the following rows give $a_{6-k-j,j,k}$ in increasing order of $j$:
$$
\begin{array}{c|rrrrrrr}
k&\multicolumn{7}{c}{a_{6-k-j,j,k}}\\\hline
0&19783&-277523&1236290&-1155576&608968&-195808&26447\\
1&205052&-1702068&1686557&-1099558&366024&-45478\\
2&584140&-622975&609573&-130204&8334\\
3&3528&-73520&-118908&15408\\
4&-16747&89450&2144\\
5&-14520&-9276\\
6&2732
\end{array}
$$
The minimal resolution $X$ of the double plane $w^2=F(x,y,z)$ is a K3 surface. The pullbacks of a line and the ten exceptional curves on the blowup of the nodes span a primitive lattice in $\Pic(X)$ isometric to
$S_\Co\cong\generators{-2}\oplus E_{10}(2)$, whose orthogonal complement in $H^2(X,\bZ)$ is $T_\Co\cong\generators{2}\oplus E_{10}(2)$.

The parametrization and equation are recovered from the original lattice-research Task 1.1 example; the verification below is independent of the old singular-point transcript.

:::

::: {.proof}

First work over $\bZ_{(101)}$. The following exact computations, reproduced by [the arithmetic verification script](../scripts/certificates/rational_sextic_example.py), use only polynomial substitution, polynomial gcd, linear algebra and Gröbner bases.

1. Substitution gives $F(f_0,f_1,f_2)=0$ in $\bZ[s,t]$.
2. Over $\bF_{101}$, the gcd of $f_i(u,1)$ is $1$, and the forms do not vanish simultaneously at $[1:0]$. Thus the common-zero subscheme in the projective line has empty special fibre. By properness over $\bZ_{(101)}$, its generic fibre is empty as well: the closed image of a nonempty generic fibre would contain the closed point. The characteristic-zero forms are base-point free.
3. Over $\bF_{101}$ the $31\times21$ matrix whose columns are the coefficients of $f_0(u,1)^if_1(u,1)^jf_2(u,1)^l$, for $i+j+l=5$, has rank $21$. A nonzero maximal minor therefore also gives rank $21$ in characteristic zero. There is no nonzero homogeneous relation of degree five, hence none of smaller degree (multiply by a monomial to get degree five).
4. In each of the three affine coordinate charts of $\PP^2_{\bF_{101}}$, write $h(a,b)$ for the dehomogenization of $F$. In all three charts the ideal
$$
 (h,h_a,h_b,h_{aa}h_{bb}-h_{ab}^2)
$$
has reduced Gröbner basis $[1]$. Thus the special fibre has no singular point with degenerate quadratic part.

The image in characteristic zero is integral, since it is the reduced image of the integral projective line. The parametrization is nonconstant by the absence of degree-one relations. Let $d$ be its degree onto its image and let $e$ be the degree of that image. A general line pulls back to a divisor of degree six because the forms have degree six and no common zero. Hence $de=6$. By (3), $e\geq6$, so $e=6$ and $d=1$. The image is consequently rational, and the nonzero degree-six relation in (1) is its defining equation up to scalar.

For nodality, the bad singular-point scheme is closed in $\PP^2_{\bZ_{(101)}}$: it is given by $F$, its first partials and all the $2\times2$ minors of its homogeneous Hessian. At a singular point with representative $p$, the Hessian annihilates $p$ by the differentiated homogeneous Euler identity. On a chart with one coordinate of $p$ normalized to $1$, the two other coordinate directions and $p$ form a basis, and the Hessian has the chart Hessian as its upper $2\times2$ block and a zero last row and column. Thus the rank-at-most-one condition is precisely the vanishing in (4). The bad scheme has empty special fibre by (4), so its generic fibre is empty by properness. Since the characteristic is zero, a singular plane-curve point with nondegenerate quadratic part is an ordinary node. Now @lem:rational_sextic_ten_nodes gives exactly ten nodes.

Let $S$ be the blowup at these nodes and $B$ the strict transform of $W$. The local ordinary-node calculation shows that $B$ is smooth, and the blowup formula gives $B\sim-2K_S$ and $B^2=-4$ by @prop:coble-canonical-class and @prop:antibicanonical-curve. If another effective divisor is linearly equivalent to $B$, its intersection with $B$ is $-4$, so it must contain $B$; the effective difference is linearly equivalent to zero and hence zero on the projective surface. Thus $\abs{-2K_S}=\{B\}$ and $\abs{-K_S}=\varnothing$ (otherwise twice an effective anticanonical divisor would equal the reduced irreducible $B$). This is the terminal Coble surface with a single branch component.

The double cover $f:X\to S$ branched along $B$ is smooth and is a K3 surface by @prop:double-cover-is-k3. It resolves the double plane: the pullback of $W$ to $S$ is $B+2\sum_i E_i$, so normalization of the pulled-back double plane is the double cover branched along $B$, defined by the line bundle $\OO_S(3H-\sum_i E_i)=\OO_S(-K_S)$. This gives a proper birational morphism to the double plane that is an isomorphism off the ten nodes. Smoothness of $X$ gives a resolution, and adjunction with $K_X=0$ excludes exceptional $(-1)$-curves, so the resolution is minimal.

Finally @prop:coble-invariant-lattice applies to this particular one-component cover, identifying the lattice generated by $f^*H,f^*E_1,\ldots,f^*E_{10}$ with the primitive invariant lattice $S_\Co$, with Gram matrix $\operatorname{diag}(2,-2,\ldots,-2)$. The complement in the unimodular K3 lattice is the anti-invariant lattice of signature $(2,9)$, with discriminant form the negative of that of $S_\Co$. Its invariants are therefore $(11,11,1)_2$, which identify it with $\generators{2}\oplus E_{10}(2)$ by [@Nik80, Thm. 3.6.2], as in @prop:coble-period-domain. This is a construction on an actual explicitly specified double plane, not just an abstract pair of glued lattices.

:::

::: {.proposition #prop:rational-sextic-severi title="The Severi variety of rational sextics"}

1. Let $S_{6,0}\iscontainedin\PP^{27}$ be the Severi variety of rational plane sextics. It is irreducible of dimension $17$ and degree (@def:graded-object) (@def:numerical-polarization) $26312976$. Its general member has exactly $10$ nodes, and the set of these $10$ nodes determines the curve [@BHO+12, §4, proof of Thm. 2].
2. There is a rational cuspidal plane sextic over $\CC$ whose only singular point is a cusp with multiplicity sequence $[5]$ [@GK20, Thm. 1.1, Thm. 3.1]. It does not have ten $A_1$ singularities.

:::

::: {.question #qst:sextic-moduli-maps title="Can one recover a nodal plane sextic from its abstract curve or its pointed normalization?"}

Fix an irreducible plane sextic with $n$ ordinary nodes and no other singularities, and put $g=10-n$. Forgetting the plane gives a stable curve in $\overline{\mathcal M}_{10}$. Normalizing gives a smooth curve of genus $g$ with $n$ unordered pairs of distinct branch points. On the equinodal locus, label the nodes and order their branches étale locally. Changing these choices gives the action of $G_n=(\mathfrak S_2)^n\rtimes\mathfrak S_n$ on the markings. The two constructions fit into
$$
[\text{equinodal sextics}/\mathrm{PGL}_3]\longrightarrow
[\mathcal M_{g,2n}/G_n]\xrightarrow{\ \mathrm{glue\ the\ pairs}\ }
\overline{\mathcal M}_{10}.
$$
Gluing recovers the original abstract nodal curve. What are the fibres of these maps from the plane-curve stack? For a given pointed normalization, which base-point-free plane linear series of degree six identify just the prescribed pairs and give ordinary nodes? On which locus, if any, can the plane series be recovered up to projectivity from the abstract curve? This recovery is the issue in asking for an embedding into curve moduli.
:::

::: {.proposition #prop:coble-canonical-class title="Canonical class of the blowup of the ten nodes"}

Let $W\subset \PP^2$ be an irreducible sextic whose singular points are exactly ten $A_1$ singularities $p_1, \ldots, p_{10}$.
Let $\pi\colon S\to\PP^2$ be the blowup of $p_1, \ldots, p_{10}$, with geometric basis (@def:based-module) $e_0, \ldots, e_{10}$ as in @prop:blowup-geometric-basis, and let $C$ be the proper transform (@def:strict-transform) of $W$.
Then
$$
K_S = -3e_0 + \Sum_{k=1}^{10} e_k,
\qquad
K_S^2 = -1,
\qquad
C \sim 6e_0 - 2\Sum_{k=1}^{10} e_k = -2K_S
.
$$
The surface $S$ is a Coble surface (@def:coble-surface) [@DK13, §3].
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
The points $p_k$ are distinct points of $\PP^2$, so each blowup is an isomorphism (@def:isomorphism-of-objects) near the other points, and the proper transform of $W$ still has multiplicity $2$ at each point blown up later.
By [@Har77, V.3.6], the pullback (@def:pullback-square) of a curve under the blowup of a point of multiplicity $r$ on it is its proper transform plus $r$ times the exceptional curve.
Applied ten times, with $W\sim 6h$ for the class $h$ of a line [@Har77, II.6.4], this gives $6e_0 = C + 2\Sum_{k=1}^{10} e_k$ in $\Pic(S)$, so $C \sim 6e_0 - 2\Sum_k e_k = -2K_S$.

:::

::: {.proposition #prop:antibicanonical-curve title="Invariants of an antibicanonical curve"}

Let $S$ be a Coble surface (@def:coble-surface) of K3 type with $K_S^2 = -1$, and let $C\in\abs{-2K_S}$ be an integral curve.
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
A sextic singular at all ten points is a nonzero vector of its kernel (@def:kernel-cokernel), and the kernel is nonzero if and only if the rank is at most $27$.

The partial derivatives are homogeneous of degree (@def:graded-object) (@def:numerical-polarization) $5$, so replacing $\tilde p_i$ by $\lambda\tilde p_i$ multiplies three rows by $\lambda^5$ and does not change the rank.
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
Then $\PP\mcv_T$ (@not:sextic-singular-type) is a smooth irreducible quasi-projective variety (@def:projective-variety) of the expected dimension
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

Let $k$ be a field, let $F\in k[x_0, x_1, x_2]$ be homogeneous of degree (@def:graded-object) (@def:numerical-polarization) $n$, and let $p\in k^3$ be nonzero with
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
Since $p\neq 0$ the kernel (@def:kernel-cokernel) of $H(F)(p)$ is nonzero, so by rank-nullity in dimension $3$ the rank is at most $2$.
:::

