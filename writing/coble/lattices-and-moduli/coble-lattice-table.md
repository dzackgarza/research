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
the $D_{2m}$ entries because $\det D_{2m}=4$ with $A_{D_{2m}}\cong(\bZ/2)^2$, and the twisted entries because twisting by $2$ multiplies the Gram matrix by $2$, so by @prop:scaled-discriminant-ses the discriminant group of $L(2)$ is $L/2L$ with $A_{L(2)}\cong(A_L)\oplus(L/2L)$.
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

::: {.remark title="What this table transcribes, and where it departs}

The rows are those of Table 5.1, p. 553, of [@CDL25], in the author-hosted draft of that book; the published printing has not been consulted here.
The source writes $\ell$ for the discriminant length where this book writes $a$, and $\mathrm{A}_1$ for what it elsewhere calls $\langle -2\rangle$.

Two rows of the source print entries that contradict their own invariants, and the table above prints what the invariants force.
The row $n=2$ prints $\mathrm{E}_{10}(2)\oplus \mathrm{A}_1^{\oplus 2}$, of length $12$ rather than the printed $10$; the lattice with those invariants is $\mathrm{E}_8(2)\oplus \mathrm{U}\oplus \mathrm{A}_1^{\oplus 2}$, which is printed here.
The last row prints $N=20$, where $K_V^2 = 9 - N = -10$ forces $N = 19$; the table prints $19$.
Both departures are from the printed entries, not from the printed invariants, and neither changes a lattice.

One row was for a time in the opposite situation.
An earlier version of this table had rows $n=4$ and $n=5$ with $\mathrm{U}$ and $\mathrm{U}(2)$ interchanged relative to the source, which the printed invariants detect; the repair of that then replaced row $n=4$ by $\mathrm{D}_4^{\oplus 2}\oplus \mathrm{A}_1^{\oplus 4}\oplus \mathrm{U}$.
That lattice has rank $14$, length $8$, signature $(1,13)$ and the same $\delta$, so by the uniqueness of the indefinite $2$-elementary lattice with given invariants [@Nik80] it is isometric to the source's $\mathrm{E}_7\oplus \mathrm{A}_1^{\oplus 5}\oplus \mathrm{U}(2)$; but it is not the source's decomposition, and a table that transcribes is not free to substitute an isometric lattice.
Row $n=4$ now carries the source's entry.

:::

For the complement, $M$ is primitive in $\lkt$ of rank $22$ and signature $(3,19)$, so by @thm:orthogonal-decomposition $N$ has rank $22-(10+n)$ and signature $(3-1,19-(\rank M-1))$; the listed $I_{2,12-n}(2)$ has exactly that rank and signature, and $a(N)=12-n$ with the parity recorded in $\delta$.
Finally $K_S^2=-n$: since $-2K_S=C=C_1+\cdots+C_n$ with $C_i^2=-4$ and $C_i\cdot C_j=0$, $K_S^2=\tfrac14C^2=-\tfrac14\cdot4n=-n$, which is the entry in the fourth column, and $K_S^2=9-\abs{\Sigma}$ together with $K_S^2=-n$ fixes $\abs{\Sigma}=9+n$.

Two rows of the source table carry the twisted summand where the untwisted one is meant: with $\mathrm{U}(2)$ in place of $\mathrm{U}$ at $n=4$ the generator length would be $10$ rather than $8$, and with $\mathrm{U}$ in place of $\mathrm{U}(2)$ at $n=5$ it would be $5$ rather than $7$.
The table above has them interchanged accordingly; every other row checks as printed.
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
