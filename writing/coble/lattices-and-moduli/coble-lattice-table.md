# Coble lattices {#sec-coble-lattice-table}

Let $S$ be a terminal Coble surface of K3 type with $\abs{-2K_S} = \theset{C}$, where $C = C_1 + \cdots + C_n$ is a disjoint union of $n$ $(-4)$-curves, and let $f\colon X\to S$ be its K3 double cover.
By @prop:coble-k3-cover, $S$ is the blowup of $\PP^2$ at a set $\Sigma$ of $\abs{\Sigma} = 9+n$ points, possibly infinitely near, and $K_S^2 = -n$.
For a general such $S$, $\Pic(X)$ is a $2$-elementary lattice $M$ of rank $r = 10+n$ with $a(M) = 12-n$, and the ramification divisor of $f$ is as in @prop:nikulin-fixed-locus with $g = 0$ and $k = n-1$.
@tbl-coble-lattices lists these lattices $M$ [@CDL25, Table 5.1, p. 553], and @prop:coble-table-invariants gives their orthogonal complements $N$ in $\lkt$.

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

The invariants of an orthogonal sum are the sums of those of the summands: ranks add, and $A_M$ is the orthogonal sum of the $A_{M_i}$ by @def:discriminant, so $a$ adds.
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
the $D_{2m}$ entries because $\det D_{2m}=4$ with $A_{D_{2m}}\cong(\bZ/2)^2$, and the twisted entries because every $L$ they twist is unimodular: for unimodular $L$, @prop:scaled-discriminant-ses gives $A_{L(2)}\cong L/2L\cong(\bZ/2)^{\rank L}$, so $a(L(2)) = \rank L$.
In general only the exact sequence $0\to L/2L\to A_{L(2)}\to A_L\to 0$ holds and the splitting can fail: for $L = \generators{2}$ the lattice $L(2) = \generators{4}$ has discriminant group $\bZ/4$, not $(\bZ/2)^2$.
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

For the complement, $M$ is primitive in $\lkt$ of rank $22$ and signature $(3,19)$, so by @thm:orthogonal-decomposition $N$ has rank $22-(10+n) = 12-n$ and signature $(2,\,19-(9+n)) = (2,10-n)$.
The lattice $\latI_{2,m}$ has rank $m+2$ and signature $(2,m)$, so the one of the listed shape with that rank is $\latI_{2,10-n}(2)$: it has rank $12-n$, signature $(2,10-n)$, and $a = 12-n$.
The exception is the row with $\delta = 0$, where $N$ is not of that shape but $\mathrm{U}(2)^{\oplus 2}$: this is the row $n=8$, where $12-8 = 4$ is the rank of $\mathrm{U}(2)^{\oplus 2}$ and $(2,10-8) = (2,2)$ its signature, so the rank and signature formulas hold there too, and the parity is $0$ rather than $1$.
Finally $K_S^2=-n$: since $-2K_S=C=C_1+\cdots+C_n$ with $C_i^2=-4$ and $C_i\cdot C_j=0$, $K_S^2=\tfrac14C^2=-\tfrac14\cdot4n=-n$, which is the entry in the $K_{\mathrm V}^2$ column, and $K_S^2=9-\abs{\Sigma}$ together with $K_S^2=-n$ fixes $\abs{\Sigma}=9+n$.
:::

::: {.notation title="Coble table invariants"}

In @tbl-coble-lattices, $l$ is the invariant $a(M)$ of @def:p-elementary and $\delta$ is the coparity $\delta_M$ of @def:p-elementary.
In [@CDL25, Table 5.1, p. 553] the number $n$ of components of $C$ is written $k$, the number $\abs{\Sigma}$ of blown-up points is written $N$, and $a(M)$ is written $l$.

:::

::: {.example #ex:coble-table-cdl-rows title="The rows $n=2$ and $n=10$ of the Coble table"}

The rows of @tbl-coble-lattices are those of [@CDL25, Table 5.1, p. 553] except in two entries.

1. The row $k=2$ of [@CDL25, Table 5.1] has invariants $(r,l,\delta)=(12,10,1)$ and lattice $\mathrm{E}_{10}(2)\oplus\mathrm{A}_1^{\oplus 2}$.
   Since $\mathrm{E}_{10}$ is unimodular, @prop:scaled-discriminant-ses gives $A_{\mathrm{E}_{10}(2)}\cong(\bZ/2)^{10}$, so
   $$
   a\qty(\mathrm{E}_{10}(2)\oplus\mathrm{A}_1^{\oplus 2}) = 10+2 = 12 \neq 10 .
   $$
   The value $l=12-n=10$ is the one forced by $l(D(M)) = l(\mathrm{I}^{1,N}(2)) - 2(n-1) = 21-N$ [@CDL25, p. 552].
   The lattice $\mathrm{E}_8(2)\oplus\mathrm{U}\oplus\mathrm{A}_1^{\oplus 2}$ has rank $8+2+2=12$ and $a=8+0+2=10$, and it is the entry of @tbl-coble-lattices at $n=2$.

2. The row $k=10$ of [@CDL25, Table 5.1] has $K_{\mathrm V}^2=-10$ and $N=20$.
   By [@CDL25, (5.4.1)], $K_{\mathrm V}^2 = 9-N = -n$, so $K_{\mathrm V}^2=-10$ gives $N=19$, the entry of @tbl-coble-lattices at $n=10$.
   This agrees with [@CDL25, Example 5.4.4], where the blow-up of the $15$ singular points of ten lines on a quintic del Pezzo surface has $N=19$ and realizes this row.

:::
