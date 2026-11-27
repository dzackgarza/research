# Coble lattices {#sec-coble-lattice-table}

Let $S$ be a terminal Coble surface of K3 type with $\abs{-2K_S} = \theset{C}$, where $C = C_1 + \cdots + C_n$ is a disjoint union of $n$ $(-4)$-curves, and let $f\colon X\to S$ be its K3 double cover.
By @prop:coble-k3-cover, $S$ is the blowup of $\PP^2$ at a set $\Sigma$ of $\abs{\Sigma} = 9+n$ points, possibly infinitely near, and $K_S^2 = -n$.
For a very general such $S$, $\Pic(X)$ is a $2$-elementary lattice $M$ of rank $r = 10+n$ with $a(M) = 12-n$, and the ramification divisor of $f$ is as in @prop:nikulin-fixed-locus with $g = 0$ and $k = n-1$.
@tbl-coble-lattices lists these lattices $M$.
It is [@CDL25, Table 5.1, p. 553] with the entries at $n=2$ and $n=10$ corrected by @prop:coble-table-cdl-corrections.
@prop:coble-table-invariants gives the orthogonal complements $N$ of the lattices $M$ in $\lkt$.

| $n$ | $\abs{\Sigma}$ | $K_{\mathrm{V}}^{2}$ | $M = (r, l, \delta)$ | 2-elementary lattice $M$ | $N=M^{\perp}$ |
| :-- | :------------- | :------------------- | :------------------- | :-------------------------------------------------------------------------------- | :------------------------- |
| 1 | 10 | -1 | $(11,11,1)$ | $\mathrm{E}_{10}(2) \oplus \mathrm{A}_{1}$ | $\latI_{2,9}(2)$ |
| 2 | 11 | -2 | $(12,10,1)$ | $\mathrm{E}_{8}(2) \oplus \mathrm{U} \oplus \mathrm{A}_1^{\oplus 2}$ | $\latI_{2,8}(2)$ |
| 3 | 12 | -3 | $(13,9,1)$ | $\mathrm{D}_{4}^{\oplus 2} \oplus \mathrm{A}_{1}^{\oplus 3} \oplus \mathrm{U}(2)$ | $\latI_{2,7}(2)$ |
| 4 | 13 | -4 | $(14,8,1)$ | $\mathrm{E}_{7} \oplus \mathrm{A}_{1}^{\oplus 5} \oplus \mathrm{U}(2)$ | $\latI_{2,6}(2)$ |
| 5 | 14 | -5 | $(15,7,1)$ | $\mathrm{E}_{8} \oplus \mathrm{A}_{1}^{\oplus 5} \oplus \mathrm{U}(2)$ | $\latI_{2,5}(2)$ |
| 6 | 15 | -6 | $(16,6,1)$ | $\mathrm{E}_{10} \oplus \mathrm{A}_{1}^{\oplus 6}$ | $\latI_{2,4}(2)$ |
| 7 | 16 | -7 | $(17,5,1)$ | $\mathrm{E}_{8} \oplus \mathrm{D}_{6} \oplus \mathrm{A}_{1} \oplus \mathrm{U}(2)$ | $\latI_{2,3}(2)$ |
| 8 | 17 | -8 | $(18,4,0)$ | $\mathrm{E}_{8} \oplus \mathrm{D}_{8} \oplus \mathrm{U}(2)$ | $\mathrm{U}(2)^{\oplus 2}$ |
| 8 | 17 | -8 | $(18,4,1)$ | $\mathrm{E}_{10} \oplus \mathrm{D}_{6} \oplus \mathrm{A}_{1}^{\oplus 2}$ | $\latI_{2,2}(2)$ |
| 9 | 18 | -9 | $(19,3,1)$ | $\mathrm{E}_{10} \oplus \mathrm{D}_{8} \oplus \mathrm{A}_{1}$ | $\latI_{2,1}(2)$ |
| 10 | 19 | -10 | $(20,2,1)$ | $\mathrm{E}_{10} \oplus \mathrm{D}_{10}$ | $\latI_{2,0}(2)$ |

: Table of Coble lattices {#tbl-coble-lattices}

::: {.lemma #lem:coble-halving-the-form title="Halving the form on the complement"}

Let $N$ be an even $2$-elementary lattice with $a(N)=\rank N$. Then $N\cong L(2)$ for a unimodular lattice $L$ of the same signature. The lattice $L$ is even exactly when $\delta(N)=0$.

:::

::: {.proof}

Write $r=\rank N$. Since $N^\#/N\cong(\bZ/2)^r$, we have $2N^\#\subseteq N$, and both lattices have index $2^r$ in $N^\#$. Hence $N=2N^\#$. On the module $N$ put $b_L=b_N/2$. This form is integral because $x/2\in N^\#$ for every $x\in N$. Its determinant has absolute value $2^{-r}\abs{\disc N}=1$, so $L=(N,b_L)$ is unimodular and $N=L(2)$.

Every discriminant class has a representative $x/2$ with $x\in N$. Its value under $q_N$ is $b_L(x,x)/2\bmod 2\bZ$. Thus $q_N$ takes only integral values exactly when $L$ is even.

:::

::: {.proposition #prop:coble-table-invariants title="Invariants of the Coble lattices"}

Each row of the table satisfies $\rank M = 10+n$, $a(M)=12-n$, and $K_S^2=-n$, where $a=\dim_{\bF_2}(A_M/2A_M)$ is the generator length of @def:p-elementary; and the orthogonal complement $N=M^{\perp\lkt}$ has rank $22-(10+n)=12-n$ and is as listed.

:::

::: {.proof}

The invariants of an orthogonal sum (@def:orthogonal-sum) are the sums of those of the summands: ranks add, and $A_M$ is the orthogonal sum of the $A_{M_i}$ by @def:discriminant, so $a$ adds.
The summands needed are
$$
\rank,\ a\ \text{of}\ \ \mathrm{E}_8,\ \mathrm{E}_{10},\ \mathrm{U}:\ (8,0),\ (10,0),\ (2,0)
\qquad\text{(all unimodular)},
$$
$$
\mathrm{A}_1:\ (1,1),\qquad
\mathrm{E}_7:\ (7,1),\qquad
\mathrm{D}_{2m}:\ (2m,2),\qquad
\mathrm{E}_8(2):\ (8,8),\qquad
\mathrm{E}_{10}(2):\ (10,10),\qquad
\mathrm{U}(2):\ (2,2),
$$
the $D_{2m}$ entries because $\det D_{2m}=4$ with $A_{D_{2m}}\cong(\bZ/2)^2$, and the twisted entries because every $L$ they twist (@def:form-twist) is unimodular: for unimodular $L$, @prop:scaled-discriminant-ses gives $A_{L(2)}\cong L/2L\cong(\bZ/2)^{\rank L}$, so $a(L(2)) = \rank L$.
In general only the exact (@def:exact-complex) sequence $0\to L/2L\to A_{L(2)}\to A_L\to 0$ holds and the splitting can fail: for $L = \generators{2}$ the lattice $L(2) = \generators{4}$ has discriminant group (@def:group) $\bZ/4$, not $(\bZ/2)^2$.
Row by row this gives

- $n=1$: $11,0+1+10=11$;
- $n=2$: $12$, $a=8+0+2=10$;
- $n=3$: $13$, $a=2\cdot2+3+2=9$;
- $n=4$: $14$, $a=1+5+2=8$;
- $n=5$: $15$, $a=0+5+2=7$;
- $n=6$: $16$, $a=0+6=6$;
- $n=7$: $17$, $a=0+2+1+2=5$;
- $n=8$: $18$, $a=0+2+2=4$ and $a=0+2+2=4$ in the two rows;
- $n=9$: $19$, $a=0+2+1=3$;
- $n=10$: $20$, $a=0+2=2$.

So $a=12-n$ in every row, and $\rank M=10+n$.

For the complement, $M$ is primitive (@def:primitive-embedding) in $\lkt$ of rank $22$ and signature (@def:signature) $(3,19)$, so by @thm:orthogonal-decomposition $N$ has rank $22-(10+n) = 12-n$ and signature $(2,\,19-(9+n)) = (2,10-n)$.
By @cor:primitive-complement-signature, $N$ has the opposite discriminant form to $M$, hence the same $a$ and $\delta$. By @lem:coble-halving-the-form, $N=L(2)$ for a unimodular lattice $L$ that is even exactly when $\delta=0$. For $n<10$ its signature is indefinite, so @thm:indefinite-unimodular-classification gives the displayed complement in each row. For $n=10$ the complement is $\generators{2}^{\perp2}$ by [@CDL25, Table 5.1, p. 553].
Finally $K_S^2=-n$: since $-2K_S=C=C_1+\cdots+C_n$ with $C_i^2=-4$ and $C_i\cdot C_j=0$, $K_S^2=\tfrac14C^2=-\tfrac14\cdot4n=-n$, which is the entry in the $K_{\mathrm V}^2$ column, and $K_S^2=9-\abs{\Sigma}$ together with $K_S^2=-n$ fixes $\abs{\Sigma}=9+n$.
:::

::: {#not:coble-table-invariants .notation title="Coble table invariants" defines="$l$; $\delta$"}

In @tbl-coble-lattices, $l$ is the invariant $a(M)$ of @def:p-elementary and $\delta$ is the coparity $\delta_M$ of @def:p-elementary.
In [@CDL25, Table 5.1, p. 553] the number $n$ of components of $C$ is written $k$, the number $\abs{\Sigma}$ of blown-up points is written $N$, and $a(M)$ is written $l$.

:::

::: {.proposition #prop:coble-table-cdl-corrections title="The rows $n=2$ and $n=10$ of the Coble table"}

1. For a general $S$ with $n=2$, $\Pic(X)\cong\mathrm{E}_8(2)\oplus\mathrm{U}\oplus\mathrm{A}_1^{\oplus 2}$.
   The lattice $\mathrm{E}_{10}(2)\oplus\mathrm{A}_1^{\oplus 2}$ of the row $k=2$ of [@CDL25, Table 5.1, p. 553] has $a = 12$, so it does not have the invariants $(12,10,1)$ of that row.
2. For $n=10$, $\abs{\Sigma} = 19$.
   The row $k=10$ of [@CDL25, Table 5.1, p. 553] gives $N = 20$, which contradicts $K_{\mathrm V}^2 = -10$.

The other entries of @tbl-coble-lattices are those of [@CDL25, Table 5.1, p. 553]. At $n=10$ that table writes $N = M^\perp$ as $\generators{2}^{\oplus 2}$, which is $\latI_{2,0}(2)$.

:::

::: {.proof}

1. By @cor:coble-k3-cover-lattice-chain, for a general $S$ the lattice $f^*\Pic(S)\cong\latI_{1,11}(2)$ has finite index (@def:index) in $\Pic(X)$, so $\Pic(X)$ has signature (@def:signature) $(1,11)$.
   By @prop:coble-k3-cover (6), $\Pic(X)$ is $2$-elementary with $a = 12-n = 10$, and $\delta = 1$ is the entry of [@CDL25, Table 5.1, p. 553] at $k=2$.
   The lattice $L\definedas\mathrm{E}_8(2)\oplus\mathrm{U}\oplus\mathrm{A}_1^{\oplus 2}$ is even.
   It has signature $(0,8)+(1,1)+(0,2) = (1,11)$, and $a(L) = 8+0+2 = 10$ by the summand values in the proof of @prop:coble-table-invariants.
   The basis (@def:based-module) vector $x$ of $\mathrm{A}_1 = \generators{-2}$ gives the class of $x/2$ in $A_L$, with $q_L(x/2) = -\tfrac12\notin\bZ/2\bZ$, so $\delta(L) = 1$.
   By @thm:two-elementary-classification, the signature, $a$ and $\delta$ determine an indefinite (@def:definiteness) even $2$-elementary lattice up to isometry, so $\Pic(X)\cong L$.
   For the lattice of [@CDL25, Table 5.1, p. 553], $\mathrm{E}_{10}$ is unimodular, and @prop:scaled-discriminant-ses gives $A_{\mathrm{E}_{10}(2)}\cong(\bZ/2)^{10}$, so
   $$
   a\qty(\mathrm{E}_{10}(2)\oplus\mathrm{A}_1^{\oplus 2}) = 10+2 = 12 \neq 10
   .
   $$
2. By [@CDL25, (5.4.1), p. 552], $K_{\mathrm V}^2 = 9-N = -n$, so $n=10$ gives $N = 19$.
   This agrees with [@CDL25, Example 5.4.4 (2), p. 553], where the blowup of the $15$ intersection points of the ten lines on a quintic del Pezzo surface (@def:degree-of-del-pezzo-surface) has $N=19$ and realizes the bottom row of the table.
   The lattices $\generators{2}^{\oplus 2}$ and $\latI_{2,0}(2)$ have the same Gram matrix $\diag(2,2)$.

:::

## The two rows at $n=8$ {#sec-coble-two-rows-at-eight}

Let $f\colon X\to V$ be the canonical K3 cover of a complex terminal Coble surface with $n$ boundary components. Write $M=\Pic(X)_0$ for the lattice generated by $f^*\Pic(V)$ and the ramification curves, as in @prop:coble-k3-cover. For a very general member of each component, $M=\Pic(X)$ by @cor:coble-k3-cover-lattice-chain.

::: {.proposition #prop:coble-complement-is-scaled-unimodular title="Parity of the unimodular lattice underlying the complement"}

For each row of @tbl-coble-lattices the complement $N=M^\perp$ is $L(2)$ with $L$ unimodular of signature $(2,10-n)$. The only rows with the same $n$ and different values of $\delta(M)$ occur at $n=8$. Their lattices $L$ are $U^{\perp2}$ for $\delta=0$ and $\latI_{2,2}$ for $\delta=1$.

:::

::: {.proof}

By @prop:coble-table-invariants and @cor:primitive-complement-signature, $a(N)=12-n=\rank N$ and $q_N\cong-q_M$. Apply @lem:coble-halving-the-form. For $1\le n<10$, $L$ is indefinite. If $L$ is even, @thm:indefinite-unimodular-classification gives $n-8\equiv0\bmod 8$, hence $n=8$. In signature $(2,2)$ the same theorem gives the two stated isometry classes, and the table realizes both. Both complements split as orthogonal sums. For $n=10$, the table gives $N=\generators{2}^{\perp2}$, so $L=\generators{1}^{\perp2}$ is odd.

:::

::: {.lemma #lem:coble-eight-quadric-models title="The two branch configurations on the quadric"}

A general member of each component with $n=8$ has one of the following branch models on $Q=\PP^1\times\PP^1$.

(a) Four lines of each ruling.

(b) Three lines of each ruling and a smooth conic of bidegree $(1,1)$ through exactly one crossing of the lines.

In each case $V$ is the blowup of the double and triple points of this divisor. Over the triple point one also blows up the three tangent directions. The boundary consists of the strict transforms of the branch curves and, in (b), the strict transform of the first exceptional curve over the triple point.

:::

::: {.proof}

Dolgachev and Kondō construct a general member for $5\le n\le10$ on the degree-five del Pezzo surface, the blowup of $\PP^2$ at four points $p_i$ in general position [@DK25, §9.1]. In the geometric basis $e_0,\ldots,e_4$, one takes a conic from each of the four pencils $\abs{e_0-e_i}$ and from $\abs{2e_0-\sum_{i=1}^4 e_i}$. For $n=8$ three conics split. The two resulting configurations up to quadratic Cremona transformation are those of [@DK25, Fig. 9.1]. The pencils of lines through $p_3$ and $p_4$ give the two coordinates on $Q$ and carry these configurations to (a) and (b), respectively [@DK25, §9.1, immediately after Fig. 9.1].

The branch divisor on $Q$ has class $(4,4)=-2K_Q$. On blowing up a point of multiplicity $m$, the new anti-bicanonical divisor is the strict transform plus $(m-2)$ times the exceptional curve. At a double point this separates the branches. At the triple point it adds the exceptional curve, which meets the three strict transforms at distinct double points. Blowing up these three points separates all eight components.

:::

::: {.lemma #lem:coble-ruling-fibres title="Singular fibres of the two rulings"}

In either model of @lem:coble-eight-quadric-models, each ruling induces an elliptic fibration on $X$ with four sections given by ramification points. Its singular fibres are
$$
\begin{array}{c|l}
\text{branch model}&\text{Kodaira fibres}\\ \hline
\mathrm{(a)}&4I_0^*\\
\mathrm{(b)}&I_2^*+2I_0^*+2I_2 .
\end{array}
$$

:::

::: {.proof}

Fix a ruling with base coordinate $t$ and fibre coordinate $x$. The generic fibre is a double cover of the $x$-line branched at four rational points. Their preimages give the sections. In (a) the four points are constant. Each vertical branch line gives a ramified quadratic twist of a smooth fibre, hence an $I_0^*$ fibre [@SS10, §5.4, (16)]. Away from the four vertical lines the family is smooth.

In (b) take the conic as the diagonal $x=t$, the triple point as $(\infty,\infty)$, and the other horizontal lines as $x=0,1$. The other vertical lines are $t=a,b$, with $a,b$ distinct and outside $\{0,1,\infty\}$. The double cover has affine equation
$$
y^2=(t-a)(t-b)\,x(x-1)(x-t).
$$
The untwisted Legendre pencil has fibres $I_2$ at $0,1$ and $I_2^*$ at $\infty$ [@SS10, §7.11]. The twist ramifies only at $a,b$, turning those two smooth fibres into $I_0^*$ fibres. This gives the stated list for either ruling. It corrects the fibre types printed after Fig. 9.1 in [@DK25, §9.1].

:::

::: {.lemma #lem:coble-grid-kummer-cover title="The Kummer cover of the eight lines"}

For every configuration (a), let $E$ and $F$ be the double covers of the two ruling bases branched over their respective sets of four points. With a ramification point as origin on each curve, $X\cong\operatorname{Km}(E\times F)$. The deck involution is induced by $(x,y)\mapsto(x,-y)$. Conversely, this involution on every product Kummer surface gives configuration (a) on the quotient.

:::

::: {.proof}

Keum and Kondō identify the quotient by the sign change on one factor and its contraction to the quadric in [@KK01, §5, Case I]. The branch construction gives this quotient for arbitrary $E$ and $F$ as follows. Each double cover has genus one by Riemann–Hurwitz, and its deck map is negation for the chosen origin. The quotient of $E\times F$ by independent sign changes is $Q$. The intermediate quotient by simultaneous negation is the double cover of $Q$ branched along the eight lines. Its sixteen nodes lie under the pairs of two-torsion points [@KK01, §2].

Blow up the sixteen crossings on $Q$. Locally the double cover $z^2=uv$ then has normalization $w^2=s$ in the chart $v=us$, where $w=z/u$. It is smooth and branches along the strict transforms. This resolves the nodes and gives $\operatorname{Km}(E\times F)$ over $V$. Its branch divisor is the Coble boundary. Since $\Pic(V)$ is torsion free, $\OO_V(-K_V)$ is the unique square root of the boundary bundle. The cover is therefore the canonical one of @prop:coble-k3-cover. The remaining sign change induces its deck map. Starting with two elliptic curves and their quotients by negation gives the same eight lines and blowups.

:::

::: {.lemma #lem:coble-product-picard title="Picard and transcendental lattices of the product cover"}

In configuration (a), if $E$ and $F$ are non-isogenous, then $\Pic(X)=M$, $T_X\cong U(2)^{\perp2}$ and $\delta(M)=0$. For isogenous pairs, $M$ is a proper sublattice of $\Pic(X)$. In both cases the deck involution fixes $M$ pointwise and acts by $-1$ on $T_X$.

:::

::: {.proof}

Put $A=E\times F$, and let $U$ be the lattice spanned by the two factor classes. Both classes have square zero and their intersection is one. The correspondence theorem [@BL04, Thm. 11.5.1] identifies line bundles on $E\times F$ modulo pullbacks from the factors with homomorphisms $E\to F$, using the origins to identify the curves with their Jacobians. Since $\Pic^0(A)=\Pic^0(E)\times\Pic^0(F)$, this gives
$$
\operatorname{NS}(A)/U\cong\operatorname{Hom}(E,F).
$$

For non-isogenous factors the quotient vanishes. By Künneth, $T_A=U^\perp$ is the tensor product of the two integral first cohomology groups. Pairing symplectic bases gives $T_A\cong U^{\perp2}$. Morrison's Kummer isometry [@Mor84, Prop. 4.3(i)] now gives $T_X\cong T_A(2)\cong U(2)^{\perp2}$, as in [@KK01, §1, Case I]. By @cor:primitive-complement-signature, $\Pic(X)$ has rank $18$, discriminant of absolute value $16$, and $\delta=0$. The sublattice $M$ has the same rank and discriminant by @prop:coble-k3-cover, so its index is one.

For isogenous factors $\operatorname{Hom}(E,F)$ has positive rank. Thus $\rank\operatorname{NS}(A)>2$ and $\rank T_A<4$. The same Kummer isometry gives $\rank\Pic(X)>18$.

The deck involution fixes all pullbacks from $V$ and each ramification curve, hence fixes $M$ pointwise. On $A$ the map $(x,y)\mapsto(x,-y)$ acts by $-1$ on the tensor summand containing $T_A$. The Kummer isometry is induced by pushforward, so the action on $T_X$ is also $-1$. If $F=E$, the diagonal and the anti-diagonal give distinct smooth rational curves on $X$ that the involution exchanges. Their classes are distinct because a $(-2)$-curve has negative self-intersection and meets any other irreducible curve nonnegatively.

:::

::: {.theorem #thm:coble-eight-components title="The two components with eight boundary curves"}

The eight-line configuration gives a general member of the component $(18,4,0)$, and the six lines and conic give a general member of $(18,4,1)$. In the first component the general canonical cover, with its deck involution, is the product Kummer surface of @lem:coble-grid-kummer-cover.

:::

::: {.proof}

Dolgachev and Kondō distinguish the two components by their discriminant forms [@DK25, §9.1, after Fig. 9.1]. In (b) the blowups exhibit a discriminant class with half-integral square. Choose a vertical and a horizontal branch line away from the triple point. These two lines and the conic meet pairwise in three distinct double points. Let $D$ be the sum of the exceptional curves over those points on $V$. Then $D^2=-3$, and $D$ meets each of the three chosen boundary curves twice and every other boundary curve zero times. Thus $f^*D/2$ pairs integrally with both $f^*\Pic(V)$ and the ramification curves: for a boundary component $C_i$ the latter pairing is $D\cdot C_i/2$. These classes generate $M$. Consequently $f^*D/2\in M^\#$ has square $-3/2$, proving $\delta(M)=1$.

In (a) the four points in either ruling can vary independently, so one may choose non-isogenous factors. Then @lem:coble-product-picard gives $\delta(M)=0$. This value holds for every grid: in the ruling and exceptional basis of $\Pic(V)$ the boundary classes are the ruling classes minus the four exceptional classes on each line. Thus the lattice generated by the pullbacks and the half-pullbacks of these boundary classes has the same Gram form for every choice of the two quadruples. By @lem:coble-eight-quadric-models the two constructions give general members, and [@DK25, §9.1] gives exactly two irreducible components. The computed values of $\delta(M)$ distinguish them.

:::

::: {.corollary #cor:coble-eight-picard-presentations title="Picard lattices and fibre root lattices"}

For very general members of (a) and (b), respectively, the Picard lattices admit the presentations
$$
U\perp D_8^{\perp2},\qquad U\perp E_7^{\perp2}\perp A_1^{\perp2}.
$$
In (a) neither $D_8$ summand is the root lattice of a singular fibre of either ruling.

:::

::: {.proof}

Both lattices displayed in [@DK25, §9.1] have signature $(1,17)$ and discriminant group $(\bZ/2)^4$, with integral discriminant values for $D_8$ and a half-integral value on $A_1^\#/A_1$. By @thm:coble-eight-components and @thm:two-elementary-classification these invariants determine the two Picard lattices. By @lem:coble-ruling-fibres each singular fibre in (a) is $I_0^*$, with root lattice $D_4$.

:::
