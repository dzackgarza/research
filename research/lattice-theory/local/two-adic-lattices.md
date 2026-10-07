# Local $2$-adic lattices {#sec:local-two-adic-lattices}

## Nikulin's $2$-adic lattices $V_k$ and $U_k$

::: {.definition #def:nikulin-Vk-Uk title="Nikulin's lattices $V_k$ and $U_k$"}

Let $\ZZ_2$ denote the ring of $2$-adic integers.
For an integer $k\geq 0$ define the rank-two $\ZZ_2$-lattices
$$
V_k \definedas \left(\ZZ_2^2,\ \begin{bmatrix} 2^{k+1} & 2^{k} \\ 2^{k} & 2^{k+1} \end{bmatrix}\right),
\qquad
U_k \definedas \left(\ZZ_2^2,\ \begin{bmatrix} 0 & 2^{k} \\ 2^{k} & 0 \end{bmatrix}\right)
.
$$
We abbreviate $V \definedas V_1$.
Each of $V_k$ and $U_k$ is even, nondegenerate, and of $2$-adic rank $2$.
:::

::: {.observation #obs:nikulin-local-lattice-properties title="Properties of $V_k$ and $U_k$"}

The lattice $U_k$ is the $2$-adic hyperbolic plane scaled by $2^k$: one has $U_0\cong U\tensor_\ZZ\ZZ_2$ and $U_1\cong U(2)\tensor_\ZZ\ZZ_2$.
The lattice $V_k$ has determinant $\det\begin{bmatrix} 2^{k+1} & 2^{k} \\ 2^{k} & 2^{k+1} \end{bmatrix} = 2^{2k+2} - 2^{2k} = 3\cdot 2^{2k}$, which is positive with positive diagonal entries, so its associated real form is positive definite of signature $(2, 0)$.
We caution that the symbol $U_k$ collides with the global notation $U$ for the hyperbolic plane over $\ZZ$; in the $2$-adic setting $U$ without a subscript is never used, and $U_k$ always denotes the $2$-adic form above.
These lattices are the local building blocks out of which the indecomposable factors of general even $2$-elementary lattices are assembled, in the sense of the decomposition below.
:::
