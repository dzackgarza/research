# Coble lattices {#sec-coble-lattice-table}

The following can be found in an unpublished note of Dolgachev.[^coble-note] Write $\abs{-2K_S} = \theset{C}$ where $C = C_1 + \cdots + C_n$ has $n$ irreducible components.
By adjunction, $C_i\cong \PP^1$ and $C_i^2 = -4$, so $K_S^2 = -n$.
Let $\Sigma$ be a general Coble set of points in $\PP^2$.
There are 10 irreducible families of K3s obtained as the double cover of $S$ branched over $C$, where the fixed point locus of the deck transformation consists of $n$ smooth rational curves.
Generally the rank of $\Pic(X)$ is $r=10+n$ and $\ell = 12-n$, and $K_S^2 = 9 - \abs{\Sigma} = -n$.

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

::: {.proposition #prop:coble-table-invariants title="The table is internally consistent"}

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

::: {.remark title="What this table transcribes, and where it departs"}

The rows are those of [@CDL25, Table 5.1, p. 553].
The source writes $\ell$ for the discriminant length where this book writes $a$, and $\mathrm{A}_1$ for what it elsewhere calls $\langle -2\rangle$.

Two rows of the source print entries that contradict their own invariants, and the table above prints what the invariants force.

The row $n=2$ prints $\mathrm{E}_{10}(2)\oplus \mathrm{A}_1^{\oplus 2}$.
Twisting a unimodular lattice multiplies its discriminant group by its own mod-$2$ reduction, so $a(L(2)) = \rank L$ for $L$ unimodular, by @prop:scaled-discriminant-ses; hence that lattice has $a = 10 + 2 = 12$, against the printed $(12,10,1)$.
The lattice with the printed invariants is $\mathrm{E}_8(2)\oplus \mathrm{U}\oplus \mathrm{A}_1^{\oplus 2}$, of $a = 8 + 0 + 2 = 10$, and it is printed here.
Which of the two printed entries is the error is not a matter of taste: the invariant is derived in the paragraph preceding the table, from $a(M) = a(\mathrm{I}_{1,N}(2)) - 2(n-1) = 12 - n$, while the summand decomposition is not, so it is the decomposition that is wrong.

The last row prints $N = 20$, while the source's own $K_V^2 = 9 - N$ with $K_V^2 = -10$ forces $N = 19$; the table prints $19$, for the same reason.

:::

For the complement, $M$ is primitive in $\lkt$ of rank $22$ and signature $(3,19)$, so by @thm:orthogonal-decomposition $N$ has rank $22-(10+n) = 12-n$ and signature $(2,\,19-(9+n)) = (2,10-n)$.
The lattice $\latI_{2,m}$ has rank $m+2$ and signature $(2,m)$, so the one of the listed shape with that rank is $\latI_{2,10-n}(2)$: it has rank $12-n$, signature $(2,10-n)$, and $a = 12-n$.
The exception is the row with $\delta = 0$, where $N$ is not of that shape but $\mathrm{U}(2)^{\oplus 2}$: this is the row $n=8$, where $12-8 = 4$ is the rank of $\mathrm{U}(2)^{\oplus 2}$ and $(2,10-8) = (2,2)$ its signature, so the rank and signature formulas hold there too while the shape differs and the parity is $0$ rather than $1$.
Equivalently, $\mathrm{U}(2)^{\oplus 2}$ is the only candidate of rank $4$ and signature $(2,2)$ available at that row, and it is not a twist of an indefinite odd unimodular lattice, which is why the complement changes shape exactly where $\delta$ changes.
Finally $K_S^2=-n$: since $-2K_S=C=C_1+\cdots+C_n$ with $C_i^2=-4$ and $C_i\cdot C_j=0$, $K_S^2=\tfrac14C^2=-\tfrac14\cdot4n=-n$, which is the entry in the fourth column, and $K_S^2=9-\abs{\Sigma}$ together with $K_S^2=-n$ fixes $\abs{\Sigma}=9+n$.

Every row of this table agrees with the invariants printed beside it in the source, with the two exceptions recorded above, where it is the source's printed summand decomposition rather than its printed invariants that is inconsistent.
:::

This table is reproduced in [@CDL25 Table 5.1, p.553].
The fixed point locus is described by [@CDL25 Eqn. 5.3.1]:

$$
X^{g}=\left\{\begin{array}{ll}
\emptyset & \text { if }(r, l, \delta)=\EnriquesInvariants, \\
C_{1}^{(1)}+C_{2}^{(1)} & \text { if }(r, l, \delta)=(10,8,0), \\
C^{(g)}+\Sum_{i=1}^{k} R_{i} & \text { otherwise }
\end{array}\right.
$$

where $C^{(g)}$ denotes a curve of genus $g \geq 0$, $R_{i}$ are disjoint $(-2)$-curves, and $$g=\frac{1}{2}(22-r-l), \quad k=\frac{1}{2}(r-l).$$

The ramification divisor for the involution on the K3 cover is described by $g=0$ and $k=n-1$ by [@CDL25 Def. 5.4.3].

[^coble-note]: <https://homepage.mi-ras.ru/~prokhoro/conf/isk20/Dolgachev.pdf>
