# Coble lattices {#sec-coble-lattice-table}

Let $S$ be a terminal Coble surface of K3 type with $\abs{-2K_S} = \theset{C}$, where $C = C_1 + \cdots + C_n$ is a disjoint union of $n$ $(-4)$-curves, and let $f\colon X\to S$ be its K3 double cover.
By @prop:coble-k3-cover, $S$ is the blowup of $\PP^2$ at a set $\Sigma$ of $\abs{\Sigma} = 9+n$ points, possibly infinitely near, and $K_S^2 = -n$.
For a general such $S$, $\Pic(X)$ is a $2$-elementary lattice $M$ of rank $r = 10+n$ with $a(M) = 12-n$, and the ramification divisor of $f$ is as in @prop:nikulin-fixed-locus with $g = 0$ and $k = n-1$.
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
The lattice $\latI_{2,m}$ has rank $m+2$ and signature $(2,m)$, so the one of the listed shape with that rank is $\latI_{2,10-n}(2)$: it has rank $12-n$, signature $(2,10-n)$, and $a = 12-n$.
The exception is the row with $\delta = 0$, where $N$ is not of that shape but $\mathrm{U}(2)^{\oplus 2}$: this is the row $n=8$, where $12-8 = 4$ is the rank of $\mathrm{U}(2)^{\oplus 2}$ and $(2,10-8) = (2,2)$ its signature, so the rank and signature formulas hold there too, and the parity is $0$ rather than $1$.
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

At $n=8$ the table has two rows, and the moduli space of complex Coble surfaces with eight boundary components has two irreducible components [@DK25, §9.1].
@prop:coble-complement-is-scaled-unimodular gives the lattice reason for the two rows.
@rmk:coble-eight-boundary-configurations gives the geometric reason: two configurations of reducible conics on the quintic del Pezzo surface.
@prop:coble-kummer-product-row identifies the row with $\delta=0$ with the Kummer surfaces of products of two elliptic curves.

::: {.proposition #prop:coble-complement-is-scaled-unimodular title="The complement $N$ is a twisted unimodular lattice"}

In each row of @tbl-coble-lattices, $N\cong L(2)$ (@def:form-twist) for a unimodular (@def:unimodular) lattice $L$ of signature $(2,10-n)$, and $L$ is even (@def:even-lattice) if and only if $\delta=0$.
Hence $\delta=0$ only at $n=8$.
At $n=8$ the row with $\delta=0$ has $L\cong\latII_{2,2}=U^{\perp 2}$, and the row with $\delta=1$ has $L\cong\latI_{2,2}$.

:::

::: {.proof}

By @prop:coble-table-invariants, $N$ has rank $12-n$ and signature $(2,10-n)$.
By @cor:primitive-complement-signature, $A_{N,q}\cong A_{M,q}(-1)$.
So $N$ is $2$-elementary (@def:p-elementary) with $a(N)=a(M)=12-n=\rank N$, and $q_N$ takes values in $\bZ/2\bZ$ exactly when $q_M$ does, that is $\delta_N=\delta_M=\delta$.

Since $A_N^\sharp=N^\#/N$ is $2$-elementary, $2N^\#\subseteq N$.
The indices are $[N^\#:N]=2^{a(N)}=2^{\rank N}=[N^\#:2N^\#]$, so $N=2N^\#$.
Let $L$ be the $\bZ$-module $N^\#$ with the form $b_L(x,y)\definedas 2b_N(x,y)$.
The form $b_L$ is integral, because $2b_N(x,y)=b_N(2x,y)$ with $2x\in N$ and $y\in N^\#$.
The map $L(2)\to N$, $x\mapsto 2x$, is a bijection, and $b_N(2x,2y)=4b_N(x,y)=2b_L(x,y)$, so it is an isometry.
Also $\abs{\disc{L}}=2^{\rank N}\abs{\disc{N^\#}}=2^{\rank N}/\abs{\disc{N}}=1$, because $\abs{\disc{N}}=2^{a(N)}$.
So $L$ is unimodular, with the signature $(2,10-n)$ of $N$.

For $x\in N^\#$, $b_L(x,x)=2b_N(x,x)$, and $b_N(x,x)\bmod 2\bZ$ is $q_N(x+N)$.
So $L$ is even if and only if $q_N$ takes values in $\bZ/2\bZ$, that is, if and only if $\delta=0$ [@Nik80, §3.6].
The lattice $L$ is indefinite.
If $\delta=0$, @thm:indefinite-unimodular-classification gives $2-(10-n)=n-8\equiv0\pmod 8$, so $n=8$ for $1\le n\le 10$, and $L\cong\latII_{2,2}=U^{\perp2}$.
If $\delta=1$, the same theorem gives $L\cong\latI_{2,10-n}$.

:::

::: {.remark #rmk:coble-two-rows-parity title="Parity, not decomposability, separates the two rows"}

Both lattices $N$ at $n=8$ are orthogonal sums: $\mathrm{U}(2)\perp\mathrm{U}(2)$ and $\generators{2}^{\perp2}\perp\generators{-2}^{\perp2}$.
By @prop:coble-complement-is-scaled-unimodular, the two rows differ in the parity of $L=N(\tfrac12)$: $L$ is the even unimodular lattice $U^{\perp 2}$ in one row and the odd unimodular lattice $\latI_{2,2}$ in the other.
The even case is possible only where an even unimodular lattice of signature $(2,10-n)$ exists, and that is only at $n=8$.

:::

::: {.remark #rmk:coble-eight-boundary-configurations title="The two configurations of reducible conics"}

For $5\le n\le10$, [@DK25, §9.1] constructs a general Coble surface $V$ with $n$ boundary components as follows.
Let $\mathcal D_5$ be the del Pezzo surface (@def:degree-of-del-pezzo-surface) of degree $5$, the blowup of four points $p_1,\dots,p_4$ of $\PP^2$, no three collinear.
Let $e_0,\dots,e_4$ be the geometric basis of $\Pic(\mathcal D_5)$, and let $L_i\definedas\abs{e_0-e_i}$ for $i=1,\dots,4$ and $L_5\definedas\abs{2e_0-e_1-e_2-e_3-e_4}$ be the five pencils of conics.
Choose one conic $K_i\in L_i$ for each $i$.
Then $V$ is the blowup of the singular points of $K_1\cup\dots\cup K_5$, and the boundary of $V$ is the union of the proper transforms of the irreducible components of the $K_i$.
If all five conics are irreducible, $n=5$, and each reducible conic adds one boundary component.

At $n=8$, three of the five conics are reducible.
Up to quadratic Cremona transformations there are two configurations, (a) and (b) [@DK25, §9.1, Fig. 9.1].
The linear system of conics through $p_3,p_4$ gives a rational map $\PP^2\dashrightarrow Q=\PP^1\times\PP^1$.
On $Q$ the two configurations are:

(a) $V$ is the blowup of the intersection points of eight lines on $Q$, four from each ruling.

(b) $V$ is the blowup of the intersection points of six lines on $Q$, three from each ruling, and of a conic through one of these intersection points, together with the infinitely near points of the tangent directions of the two lines and the conic at that point.

The two rulings of $Q$ give two elliptic pencils on the K3 cover $X$ of $V$.
In case (a), a pencil has four fibres of type $\tilde{\mathrm D}_4$ and four disjoint sections, and $\Pic(X)\cong\mathrm U\oplus\mathrm D_8\oplus\mathrm D_8$.
In case (b), a pencil has two fibres of type $\tilde{\mathrm D}_6$, two fibres of type $\tilde{\mathrm A}_1$ and four sections, and $\Pic(X)\cong\mathrm U\oplus\mathrm E_7\oplus\mathrm E_7\oplus\mathrm A_1\oplus\mathrm A_1$.
In both cases $A_{\Pic(X)}\cong(\bZ/2)^4$, and the discriminant form is even in case (a) and odd in case (b) [@DK25, §9.1].
So case (a) is the row $(18,4,0)$ and case (b) is the row $(18,4,1)$.

The orthogonal sum decompositions of $M$ are not canonical.
By @thm:two-elementary-classification, the lattice $\mathrm U\oplus\mathrm D_8\oplus\mathrm D_8$ of case (a) is isometric to the lattice $\mathrm E_8\oplus\mathrm D_8\oplus\mathrm U(2)$ of @tbl-coble-lattices, because both are even $2$-elementary of signature $(1,17)$ with $a=4$ and $\delta=0$.
The presentation $\mathrm U\oplus\mathrm D_8\oplus\mathrm D_8$ comes from the configuration of fibres and sections of the elliptic pencil, and the presentation in the table comes from the classification.

:::

::: {.proposition #prop:coble-kummer-product-row title="The row $\delta=0$ is the Kummer-product locus"}

Let $V$ be a Coble surface of type (a) in @rmk:coble-eight-boundary-configurations.
Then there are elliptic curves $E$ and $F$ such that the K3 cover of $V$ is the Kummer surface $X=\operatorname{Km}(E\times F)$, and $V=X/\iota$ for the involution $\iota$ of $X$ induced by $(x,y)\mapsto(x,-y)$.
If $E$ and $F$ are not isogenous, then $T_X\cong\mathrm U(2)^{\oplus 2}$, which is the complement $N$ of the row $(18,4,0)$, and $\Pic(X)$ is the lattice $M$ of that row.

:::

::: {.proof}

Let the four lines of the first ruling of $Q=\PP^1\times\PP^1$ be $\{u_i\}\times\PP^1$ and the four lines of the second ruling be $\PP^1\times\{v_j\}$.
Let $E\to\PP^1$ be the double cover branched at $u_1,\dots,u_4$.
By Riemann–Hurwitz, $E$ has genus $1$.
With a ramification point as origin, the covering involution is $x\mapsto-x$, and its fixed points, the points over $u_1,\dots,u_4$, are the points of $E[2]$.
Define $F\to\PP^1$ from $v_1,\dots,v_4$ in the same way.

The group of automorphisms of $E\times F$ generated by $-1$ and $(x,y)\mapsto(x,-y)$ also contains $(x,y)\mapsto(-x,y)$, and the quotient of $E\times F$ by it is $(E/\pm1)\times(F/\pm1)=Q$.
On $X=\operatorname{Km}(E\times F)$, the involution $\iota$ induced by $(x,y)\mapsto(x,-y)$ fixes pointwise exactly eight smooth rational curves $E_1,\dots,E_4,F_1,\dots,F_4$, it acts as $1$ on $\Pic(X)$ and as $-1$ on $T_X$, and contracting the images of the sixteen exceptional curves $G_{ij}$ of $X$ on $X/\iota$ gives the smooth quadric $Q$ [@KK01, §5].
Write $E[2]=\{p_1,\dots,p_4\}$ and $F[2]=\{q_1,\dots,q_4\}$, with $p_i$ over $u_i$ and $q_j$ over $v_j$.
The curves $E_j$ and $F_i$ are the images of $E\times\{q_j\}$ and $\{p_i\}\times F$ [@KK01, §2], so they map to the lines $\PP^1\times\{v_j\}$ and $\{u_i\}\times\PP^1$.
The curve $G_{ij}$ lies over the point $(p_i,q_j)$, so its image is the exceptional curve over the intersection point $(u_i,v_j)$.
So $X/\iota$ is the blowup of $Q$ at the sixteen intersection points of the eight lines, which is $V$.

The double cover $X\to V$ is branched exactly along the images of the eight curves $E_i$ and $F_j$, which are the boundary components $C$ of $V$.
A double cover of $V$ branched along $C$ is given by a line bundle whose square is $\OO_V(C)$.
Such a line bundle is unique, because $V$ is rational and so $\Pic(V)$ is torsion free.
So $X$ is the K3 cover of $V$ in @prop:coble-k3-cover.

If $E$ and $F$ are not isogenous, then $T_X\cong\mathrm U(2)^{\oplus 2}$ [@KK01, §1, Case I].
This is $N$ in the row $(18,4,0)$ of @tbl-coble-lattices.
So $\Pic(X)$ is even and $2$-elementary of signature $(1,17)$ with $A_{\Pic(X),q}\cong A_{N,q}(-1)$ by @cor:primitive-complement-signature, and so $a=4$ and $\delta=0$.
By @thm:two-elementary-classification, $\Pic(X)$ is isometric to the lattice $M$ of that row.

:::

::: {.remark #rmk:coble-kummer-product-row-meaning title="The meaning of $N=\mathrm U(2)^{\oplus2}$"}

By @prop:coble-kummer-product-row, the complement $N=\mathrm U(2)^{\oplus 2}$ of the row $(18,4,0)$ is the transcendental lattice of the Kummer surface $\operatorname{Km}(E\times F)$ of a product of two non-isogenous elliptic curves.
The chain is:
reducible conics on $\mathcal D_5$; two configurations when three conics are reducible; two families of K3 covers at $n=8$; the rows $(18,4,0)$ and $(18,4,1)$; even and odd discriminant forms; $N=\mathrm U(2)^{\oplus2}$ and $N=\latI_{2,2}(2)$.
In the row $\delta=0$ this is: four lines from each ruling of $Q$; $\operatorname{Km}(E\times F)$; $T_X=\mathrm U(2)^{\oplus2}$.
So the two rows at $n=8$ are two different geometric components, and the component with $\delta=0$ is the locus of Kummer surfaces of products of two elliptic curves.

:::
