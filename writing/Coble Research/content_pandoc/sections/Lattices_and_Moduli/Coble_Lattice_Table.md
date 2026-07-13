# Coble lattices

The following can be found in an unpublished note of Dolgachev [@DM19]. Write $\abs{-2K_S} = \ts{C}$ where $C = C_1 + \cdots + C_n$ has $n$ irreducible components.
By adjunction, $C_i\cong \PP^1$ and $C_i^2 = -4$, so $K_S^2 = -n$.
Let $\Sigma$ be a general Coble set of points in $\PP^2$.
There are 10 irreducible families of K3s obtained as the double cover of $S$ branched over $C$, where the fixed point locus of the deck transformation consists of $n$ smooth rational curves.
Generally the rank of $\Pic(X)$ is $r=10+n$ and $\ell = 12-n$, and $K_S^2 = 9 - \abs{\Sigma} = -n$.

| $n$ | $\abs{\Sigma}$ | $K_{\mathrm{V}}^{2}$ | $M = (r, l, \delta)$ | 2-elementary lattice $M$ | $N=M^{\perp}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 10 | -1 | $(11,11,1)$ | $\mathrm{E}*{10}(2) \oplus \mathrm{A}*{1}$ | $\latI_{2,9}(2)$ |
| 2 | 11 | -2 | $(12,10,1)$ | $\mathrm{E}_{8}(2) \oplus \mathrm{U} \oplus \mathrm{A}_1^{\oplus 2}$ | $\latI_{2,8}(2)$ |
| 3 | 12 | -3 | $(13,9,1)$ | $\mathrm{D}*{4}^{\oplus 2} \oplus \mathrm{A}*{1}^{\oplus 3} \oplus \mathrm{U}(2)$ | $\latI_{2,7}(2)$ |
| 4 | 13 | -4 | $(14,8,1)$ | $\mathrm{D}*{4}^{\oplus 2} \oplus \mathrm{A}*{1}^{\oplus 4} \oplus \mathrm{U}(2)$ | $\latI_{2,6}(2)$ |
| 5 | 14 | -5 | $(15,7,1)$ | $\mathrm{E}*{8} \oplus \mathrm{A}*{1}^{\oplus 5} \oplus \mathrm{U}$ | $\latI_{2,5}(2)$ |
| 6 | 15 | -6 | $(16,6,1)$ | $\mathrm{E}*{10} \oplus \mathrm{A}*{1}^{\oplus 6}$ | $\latI_{2,4}(2)$ |
| 7 | 16 | -7 | $(17,5,1)$ | $\mathrm{E}*{8} \oplus \mathrm{D}*{6} \oplus \mathrm{A}_{1} \oplus \mathrm{U}(2)$ | $\latI_{2,3}(2)$ |
| 8 | 17 | -8 | $(18,4,0)$ | $\mathrm{E}*{8} \oplus \mathrm{D}*{8} \oplus \mathrm{U}(2)$ | $\mathrm{U}(2)^{\oplus 2}$ |
| 8 | 17 | -8 | $(18,4,1)$ | $\mathrm{E}*{10} \oplus \mathrm{D}*{6} \oplus \mathrm{A}_{1}^{\oplus 2}$ | $\latI_{2,2}(2)$ |
| 9 | 18 | -9 | $(19,3,1)$ | $\mathrm{E}*{10} \oplus \mathrm{D}*{8} \oplus \mathrm{A}_{1}$ | $\latI_{2,1}(2)$ |
| 10 | 19 | -10 | $(20,2,1)$ | $\mathrm{E}*{10} \oplus \mathrm{D}*{10}$ | $\latI_{2,0}(2)$ |

\label{table:coble-lattices}

This table is reproduced in [@CDL24 Table 5.1, p.553]. The fixed point locus is described by [@CDL24 Eqn. 5.3.1]:

$$
X^{g}=\left\{\begin{array}{ll}
\emptyset & \text { if }(r, l, \delta)=(10,10,0), \\
C_{1}^{(1)}+C_{2}^{(1)} & \text { if }(r, l, \delta)=(10,8,0), \\
C^{(g)}+\sum_{i=1}^{k} R_{i} & \text { otherwise }
\end{array}\right.
$$

where $C^{(g)}$ denotes a curve of genus $g \geq 0$, $R_{i}$ are disjoint $(-2)$-curves, and $$g=\frac{1}{2}(22-r-l), \quad k=\frac{1}{2}(r-l).$$

The ramification divisor for the involution on the K3 cover is described by $g=0$ and $k=n-1$ by [@CDL24 Def. 5.4.3].
