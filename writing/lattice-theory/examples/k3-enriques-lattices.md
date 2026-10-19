# K3 and Enriques lattice examples {#sec:k3-enriques-lattice-examples}

## The Enriques lattice $E_{10}$ and its twist

::: {.definition #def:enriques-lattice title="The Enriques lattice"}

The **Enriques lattice** is
$$
E_{10} \definedas U\oplus E_8 \iso \latII_{1, 9}
,
$$
the orthogonal direct sum of the hyperbolic plane and the negative-definite $E_8$ lattice.
It is even, unimodular, of signature $(1,9)$, and is the unique even unimodular lattice of that signature up to isometry.
:::

::: {.proposition #prop:doubled-enriques-lattice title="The doubled Enriques lattice"}

Its twist
$$
E_{10}(2)=U(2)\oplus E_8(2)
$$
is even of signature $(1,9)$ and, because $E_{10}$ is unimodular of rank $10$, the scaled-discriminant exact sequence (@prop:scaled-discriminant-ses) gives
$$
A_{E_{10}(2)}\cong E_{10}/2E_{10}\cong(\ZZ/2\ZZ)^{10}.
$$
Thus $E_{10}(2)$ is $2$-elementary of type $(r,a,\delta)=\EnriquesInvariants$.
:::

## Degree $2d$ K3 lattices

::: {.definition #def:degree-2d-k3-lattice title="Degree $2d$ K3 lattices"}

For a positive integer $d$ and an integer $m\geq0$, define
$$
L_{\Kthree,2d}^{(m)}\definedas\generators{-2d}\oplus U^2\oplus E_8^m,
\qquad
L_{\Kthree,2d}\definedas L_{\Kthree,2d}^{(2)}.
$$
The distinguished case $m=2$ has signature $(2,19)$ and is called the **degree $2d$ K3 lattice**.
:::

::: {.proposition #prop:degree-2d-k3-complement title="The degree-$2d$ orthogonal complement"}

Let
$$
\lkt=U^3\oplus E_8^2=\latII_{3,19}
$$
and let $h=e+df$ be a primitive vector in one hyperbolic summand $U=\generators{e,f}$, so $h^2=2d$.
Then
$$
h^{\perp\lkt}\cong \generators{-2d}\oplus U^2\oplus E_8^2=L_{\Kthree,2d}.
$$
:::

::: {.proof}
The vector $e-df$ spans $h^{\perp U}$ and has square $-2d$.
Taking the orthogonal complement in the remaining two copies of $U$ and two copies of $E_8$ gives the displayed decomposition.
:::

## K3-embeddable $2$-elementary building blocks

::: {.example #ex:2elementary-k3-building-blocks title="K3-embeddable $2$-elementary building blocks"}
Nikulin's theory of even $2$-elementary hyperbolic lattices with primitive embeddings into $\lkt$ includes the basic summands
$$
A_1,\quad D_4,\quad D_6,\quad D_8,\quad E_7,\quad E_8,\quad E_8(2),\quad
\generators{2},\quad U,\quad U(2).
$$
These are representative building blocks rather than an exhaustive classification [@Nik80].
:::
