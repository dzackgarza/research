# Definite lattice theory {#sec:definite-lattice-theory}

::: {.proposition #prop:definite-finiteness title="Finiteness for definite lattices"}

If $L$ is definite, then $L[k]$ is finite for every $k\in\bZ$, and $\Orth(L)$ is finite.
:::

::: {.proof}
The scalar extension $L\injects L_\bR$ is discrete, and for fixed $k$ the shell $L[k]$ lies on a compact sphere for the positive-definite form $\beta_L$ or $-\beta_L$; hence $L[k]$ is finite.

Choose a $\bZ$-basis $e_1,\dots,e_r$ of $L$.
Evaluation on the basis gives a monomorphism of sets
$$
\Orth(L)
\injects
\prod_{i=1}^r L[e_i^2],
\qquad
g\longmapsto\qty(g(e_1),\dots,g(e_r)).
$$
Each factor is finite by the first assertion, so $\Orth(L)$ is finite.
:::

::: {.example #ex:indefinite-shells-infinite title="Indefinite shells and orthogonal groups can be infinite"}

For the hyperbolic plane $U=\generators{e,f}$,
$$
U[0]=\bZ e\union\bZ f,
$$
so $U[0]$ is infinite.

For $L=\generators{1}\perp\generators{-2}$ with Gram matrix $G=\operatorname{diag}(1,-2)$,
$$
L[1]=\theset{(x,y)\in\bZ^2\st x^2-2y^2=1}.
$$
The matrix
$$
M=\matt{3}{4}{2}{3}
$$
satisfies $M^{\mathsf T}GM=G$, hence $M\in\Orth(L)$.
Its real eigenvalue $3+2\sqrt2>1$ implies that $M$ has infinite order; therefore $\Orth(L)$ and the orbit $\theset{M^ne_1\st n\in\bZ}\subseteq L[1]$ are infinite.
:::

::: {.definition #def:definite-minimum-shell title="Minimum, minimal vectors, and kissing number"}

Let $L$ be definite.
The **minimum** is
$$
\mu(L)\definedas\min_{0\neq x\in L}|x^2|.
$$
The **minimal shell** is
$$
\operatorname{Min}(L)
\definedas
\begin{cases}
L[\mu(L)],&L\text{ positive definite},\\
L[-\mu(L)],&L\text{ negative definite},
\end{cases}
$$
and the **kissing number** is
$$
\tau(L)\definedas\cardinality{\operatorname{Min}(L)}.
$$
:::

::: {.definition #def:voronoi-perfect-lattice title="Voronoi-perfect lattices"}

Let $L$ be definite.
For $v\in L_\bQ$, let $v^{\otimes2}\in\operatorname{Sym}^2_\bQ(L_\bQ)$ be the corresponding rank-one symmetric tensor.
The lattice is **Voronoi-perfect** when
$$
\spanof_\bQ
\theset{v^{\otimes2}\st v\in\operatorname{Min}(L)}
=
\operatorname{Sym}^2_\bQ(L_\bQ).
$$
Equivalently, the values of the quadratic form on the minimal shell determine the form up to scale [@Mar03, Ch. 4].
:::

::: {.definition #def:regular-ternary-lattice title="Regular and spinor-regular ternary lattices"}

Let $L$ be a positive-definite integral ternary lattice, and let $\mathfrak s_L$ be the spinor genus containing $[L]$ in the partition of @def:spinor-genus-partition.
The lattice $L$ is **regular** when
$$
\bigcup_{[M]\in\operatorname{Gen}(L)}
\theset{n\in\bZ_{>0}\st M[n]\neq\varnothing}
=
\theset{n\in\bZ_{>0}\st L[n]\neq\varnothing}.
$$
It is **spinor regular** when
$$
\bigcup_{[M]\in\mathfrak s_L}
\theset{n\in\bZ_{>0}\st M[n]\neq\varnothing}
=
\theset{n\in\bZ_{>0}\st L[n]\neq\varnothing}.
$$
:::
