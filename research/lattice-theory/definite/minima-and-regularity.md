# Definite lattice theory {#sec:definite-lattice-theory}

::: {.proposition #prop:definite-finiteness title="Finiteness in the definite and indefinite cases"}

If $L$ is definite, then $L[k]$ is finite for every $k\in\bZ$.
Consequently $\Orth(L)$ is finite.

Neither conclusion holds for indefinite lattices.
For the hyperbolic plane $U=\generators{e,f}$,
$$
U[0]=\bZ e\union\bZ f
$$
is infinite.
For
$$
L=\generators{1}\perp\generators{-2},
$$
the shell $L[1]$ is the solution set of
$$
x^2-2y^2=1,
$$
and
$$
M=\matt{3}{4}{2}{3}
$$
has infinite order in $\Orth(L)$.
:::

::: {.proof}
For definite $L$, the real scalar extension of either $\beta_L$ or $-\beta_L$ is positive definite.
A fixed norm shell is therefore the intersection of the discrete lattice $L\injects L_\bR$ with a compact sphere, hence finite.
An isometry is determined by the images of a basis, and each basis vector has only finitely many possible images of the same norm, so $\Orth(L)$ is finite.

The indefinite examples are immediate from the displayed formulas.
:::

::: {.definition #def:definite-minimum-shell title="Minimum, minimal vectors, and kissing number"}

Let $L$ be definite and put
$$
\varepsilon_L
\definedas
\begin{cases}
1,&L\text{ positive definite},\\
-1,&L\text{ negative definite}.
\end{cases}
$$
The **minimum** is
$$
\mu(L)
\definedas
\min_{0\neq x\in L}\varepsilon_Lx^2
=
\min_{0\neq x\in L}|x^2|.
$$
The **minimal shell** is
$$
\operatorname{Min}(L)
\definedas
\theset{x\in L\sm\theset0\st \varepsilon_Lx^2=\mu(L)},
$$
and the **kissing number** is
$$
\tau(L)\definedas|\operatorname{Min}(L)|.
$$
For negative-definite $L$, these are the corresponding invariants of $T_{-1}(L)$ from @def:signature-subcategories.
:::

::: {.definition #def:voronoi-perfect-lattice title="Voronoi-perfect lattices"}

Let $L$ be definite.
For $v\in L_\bQ$, write
$$
v^{\otimes2}\in\operatorname{Sym}^2_\bQ(L_\bQ)
$$
for the corresponding rank-one symmetric tensor.
The lattice is **Voronoi-perfect** when
$$
\spanof_\bQ
\theset{v^{\otimes2}\st v\in\operatorname{Min}(L)}
=
\operatorname{Sym}^2_\bQ(L_\bQ).
$$
Equivalently, the values of the quadratic form on the minimal shell determine the form up to scale [@Mar03, Ch. 4].
:::

::: {.observation #obs:perfect-lattice-vs-form title="Perfect lattice versus perfect bilinear form"}

Voronoi perfectness is a spanning condition in $\operatorname{Sym}^2_\bQ(L_\bQ)$.
It is distinct from perfectness of a bilinear module, which requires the adjoint morphisms of @def:polarization to be isomorphisms.
:::

::: {.definition #def:regular-ternary-lattice title="Regular and spinor-regular ternary lattices"}

Let $L$ be a positive-definite integral ternary lattice.
It is **regular** when every positive integer represented by some lattice in the genus of $L$ is represented by $L$.
It is **spinor regular** when every positive integer represented by some lattice in the spinor genus of $L$ is represented by $L$.
For negative-definite $L$, apply these definitions to $T_{-1}(L)$.
:::
