---
title: Coble lattice table
tags:
  - subject/algebraic-geometry
  - subject/lattice-theory
  - surface/coble
  - type/table
aliases:
  - Coble lattice families
  - Coble lattice table
created: 2026-05-10
---

> [!table] Coble lattice table
> For a Coble surface with $n$ boundary components, there are 10 irreducible families of K3 covers obtained by branching along the anti-bicanonical divisor.
> The corresponding invariant lattice $M$ and orthogonal complement $N=M^\perp$ are [@DM19; @CDL24]:

| $n$ | $\abs{\Sigma}$ | $K_{\mathrm{V}}^{2}$ | $M = (r,l,\delta)$ | 2-elementary lattice $M$ | $N=M^\perp$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 10 | -1 | $(11,11,1)$ | $\mathrm{E}_{10}(2) \oplus \mathrm{A}_{1}$ | $\latI_{2,9}(2)$ |
| 2 | 11 | -2 | $(12,10,1)$ | $\mathrm{E}_{8}(2) \oplus \mathrm{U} \oplus \mathrm{A}_1^{\oplus 2}$ | $\latI_{2,8}(2)$ |
| 3 | 12 | -3 | $(13,9,1)$ | $\mathrm{D}_{4}^{\oplus 2} \oplus \mathrm{A}_{1}^{\oplus 3} \oplus \mathrm{U}(2)$ | $\latI_{2,7}(2)$ |
| 4 | 13 | -4 | $(14,8,1)$ | $\mathrm{D}_{4}^{\oplus 2} \oplus \mathrm{A}_{1}^{\oplus 4} \oplus \mathrm{U}(2)$ | $\latI_{2,6}(2)$ |
| 5 | 14 | -5 | $(15,7,1)$ | $\mathrm{E}_{8} \oplus \mathrm{A}_{1}^{\oplus 5} \oplus \mathrm{U}$ | $\latI_{2,5}(2)$ |
| 6 | 15 | -6 | $(16,6,1)$ | $\mathrm{E}_{10} \oplus \mathrm{A}_{1}^{\oplus 6}$ | $\latI_{2,4}(2)$ |
| 7 | 16 | -7 | $(17,5,1)$ | $\mathrm{E}_{8} \oplus \mathrm{D}_{6} \oplus \mathrm{A}_{1} \oplus \mathrm{U}(2)$ | $\latI_{2,3}(2)$ |
| 8 | 17 | -8 | $(18,4,0)$ | $\mathrm{E}_{8} \oplus \mathrm{D}_{8} \oplus \mathrm{U}(2)$ | $\mathrm{U}(2)^{\oplus 2}$ |
| 8 | 17 | -8 | $(18,4,1)$ | $\mathrm{E}_{10} \oplus \mathrm{D}_{6} \oplus \mathrm{A}_{1}^{\oplus 2}$ | $\latI_{2,2}(2)$ |
| 9 | 18 | -9 | $(19,3,1)$ | $\mathrm{E}_{10} \oplus \mathrm{D}_{8} \oplus \mathrm{A}_{1}$ | $\latI_{2,1}(2)$ |
| 10 | 19 | -10 | $(20,2,1)$ | $\mathrm{E}_{10} \oplus \mathrm{D}_{10}$ | $\latI_{2,0}(2)$ |

## Fixed-locus formulas

The fixed locus of the covering involution is described by [@CDL24]
$$
X^g =
\left\{
\begin{array}{ll}
\emptyset & \text{if }(r,l,\delta)=(10,10,0), \\
C_1^{(1)} + C_2^{(1)} & \text{if }(r,l,\delta)=(10,8,0), \\
C^{(g)} + \sum_{i=1}^k R_i & \text{otherwise,}
\end{array}
\right.
$$
where
$$
g = \frac{1}{2}(22-r-l), \qquad k = \frac{1}{2}(r-l).
$$

For Coble surfaces one has $g=0$ and $k=n-1$, so the ramification divisor consists of a rational curve together with $n-1$ disjoint $(-2)$-curves in the non-Enriques cases [@CDL24].
