# Local $2$-adic lattices {#sec:local-two-adic-lattices}

## Nikulin's $2$-adic lattices $V_k$ and $U_k$

::: {.definition #def:nikulin-Vk-Uk title="Nikulin's lattices $V_k$ and $U_k$"}

For $k\in\bZ_{\geq0}$ define the rank-two $\padiccompletion{\bZ}{2}$-lattices
$$
V_k
\definedas
\left(
\padiccompletion{\bZ}{2}^{\,2},
\begin{bmatrix}
2^{k+1}&2^k\\
2^k&2^{k+1}
\end{bmatrix}
\right),
\qquad
U_k
\definedas
\left(
\padiccompletion{\bZ}{2}^{\,2},
\begin{bmatrix}
0&2^k\\
2^k&0
\end{bmatrix}
\right).
$$
Thus
$$
V_k\isoto V_0(2^k),
\qquad
U_k\isoto U_0(2^k).
$$
:::

::: {.proposition #prop:nikulin-local-lattice-properties title="Scalar extension and determinants of $V_k$ and $U_k$"}

There is an isometry
$$
U_0\isoto U\tensor_{\bZ}\padiccompletion{\bZ}{2},
$$
and hence
$$
U_k
\isoto
\qty{U\tensor_{\bZ}\padiccompletion{\bZ}{2}}(2^k).
$$
Moreover,
$$
\det(U_k)=-2^{2k},
\qquad
\det(V_k)=3\cdot2^{2k}.
$$
:::

::: {.proof}
The displayed Gram matrix of $U_0$ is the base change of the standard Gram matrix of $U$.
Twisting by $2^k$ gives the displayed Gram matrix of $U_k$.
The determinant formulas follow directly from the two defining matrices.
:::
