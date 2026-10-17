.# Standard lattice examples {#sec:standard-lattice-examples}

## The hyperbolic plane and its orthogonal group

Let $U$ be the hyperbolic plane of @def:hyperbolic-plane and fix an ordered hyperbolic basis
$$
B_U=(e,f).
$$

::: {.proposition #prop:orthogonal-group-U title="Orthogonal group of the hyperbolic plane"}

Define $\sigma,\tau\in\Orth(U)$ by
$$
\sigma(e)=-e,
\qquad
\sigma(f)=-f,
$$
and
$$
\tau(e)=f,
\qquad
\tau(f)=e.
$$
Then
$$
\Orth(U)=\generators{\sigma,\tau}\isoto C_2\times C_2.
$$
Their matrices in $B_U$ are
$$
[\sigma]_{B_U}=-I_2,
\qquad
[\tau]_{B_U}=\begin{bmatrix}0&1\\1&0\end{bmatrix}.
$$

For $a,b\in\QQ^\times$, define
$$
i_a,j_b\in\operatorname{End}_{\QQ\text{-}\mathbf{Mod}}(U_\QQ)
$$
by the coordinate matrices
$$
[i_a]_{B_U}=\begin{bmatrix}a&0\\0&a^{-1}\end{bmatrix},
\qquad
[j_b]_{B_U}=\begin{bmatrix}0&b\\b^{-1}&0\end{bmatrix}.
$$
Then $i_a,j_b\in\Orth(U_\QQ)$.
:::

::: {.proof}

An isometry of $U$ permutes $U^{\mathrm{prim}}[0]=\theset{\pm e,\pm f}$ and is determined by its action on the ordered isotropic frame $(e,f)$.
Preservation of $ef = 1$ forces the image frame to be one of $(e, f), (-e, -f), (f, e), (-f, -e)$, giving the four listed matrices.
Over $\QQ$ the vectors $ae$ and $\inverseof{a} f$ are again isotropic with $(ae)(\inverseof{a} f) = ef = 1$, so $i_a\in\Orth(U_\QQ)$, and likewise $j_b(e) = \inverseof{b} f$, $j_b(f) = be$ satisfy $(\inverseof{b} f)(be) = fe = 1$, so $j_b\in\Orth(U_\QQ)$.
:::

## The scaled hyperbolic plane $U(2)$

::: {.proposition #prop:U2-discriminant title="Discriminant forms of $U(2)$"}

In the basis $B_U$,
$$
[\beta_{U(2)}]_{B_U}
=
\begin{bmatrix}0&2\\2&0\end{bmatrix},
\qquad
\disc{U(2)}=-4.
$$
Moreover,
$$
U(2)^\#\isoto\tfrac12U,
\qquad
A_{U(2)}^\sharp
\isoto
U/2U
\isoto
(\ZZ/2\ZZ)^2.
$$
Its bilinear value module is $\tfrac12\ZZ/\ZZ$, and $A_{U(2),q}$ has value module $\ZZ/2\ZZ$.
:::

::: {.proof}
By @prop:dual-properties and unimodularity of $U$,
$$
U(2)^\#
\isoto
U^\#(1/2)
\isoto
U(1/2).
$$
Multiplication by $2$ induces the displayed isomorphism
$$
A_{U(2)}^\sharp\isoto U/2U.
$$
Let
$$
\pi_{U(2)}\colon U(2)^\#\twoheadrightarrow A_{U(2)}^\sharp
$$
be the cokernel morphism of @def:metric-dual.
For $x=(ae+bf)/2\in U(2)^\#$,
$$
q_{U(2)}\qty{\pi_{U(2)}(x)}
=
ab+2\ZZ,
$$
so the quadratic value module is $\ZZ/2\ZZ$.
:::



## The lattice $E_8(2)$

::: {.proposition #prop:E8-2-discriminant title="Discriminant forms of $E_8(2)$"}

The scaled root lattice $E_8(2)$ satisfies
$$
\disc{E_8(2)}=2^8,
\qquad
(E_8(2))^\#\isoto\tfrac12E_8,
$$
and
$$
A_{E_8(2)}^\sharp
\isoto
E_8/2E_8
\isoto
(\ZZ/2\ZZ)^8.
$$
The bilinear value module is $\tfrac12\ZZ/\ZZ$, and
$$
\ell\qty{A_{E_8(2)}^\sharp}=8.
$$
Since $E_8$ is even, $A_{E_8(2),q}$ has value module $\ZZ/2\ZZ$.
:::

::: {.proof}

For any lattice $L$ of rank $r$ and any positive integer $m$ one has $\disc{L(m)}=m^r\disc{L}$, since the Gram matrix of $L(m)$ is $m$ times that of $L$.
Taking $L=E_8$, which is unimodular of rank $8$ with $\disc{E_8}=1$, gives $\disc{E_8(2)}=2^8$.
By @prop:dual-properties,
$$
(E_8(2))^\#\isoto\tfrac12E_8.
$$
Multiplication by $2$ induces
$$
A_{E_8(2)}^\sharp
\isoto
E_8/2E_8
\isoto
(\ZZ/2\ZZ)^8.
$$
:::



## The discriminant form of a twisted unimodular lattice

::: {.proposition #prop:twisted-unimodular-discriminant title="Discriminant forms of $M(2)$ for $M$ unimodular"}

Let $M$ be a unimodular integral lattice of rank $r$. Then
$$
(M(2))^\#\isoto\tfrac12M,
\qquad
A_{M(2)}^\sharp
\isoto
M/2M
\isoto
(\ZZ/2\ZZ)^r.
$$
Its bilinear value module is $\tfrac12\ZZ/\ZZ$.
In particular $M(2)$ is $2$-elementary and
$$
\ell\qty{A_{M(2)}^\sharp}=r.
$$

Let
$$
\pi_{M(2)}\colon(M(2))^\#\twoheadrightarrow A_{M(2)}^\sharp
$$
be the cokernel morphism of @def:metric-dual.
For $x\in M$,
$$
q_{M(2)}\qty{\pi_{M(2)}(x/2)}
=
\tfrac12\beta_M(x,x)+2\ZZ.
$$
Hence the quadratic value module is
$$
\begin{cases}
\ZZ/2\ZZ, & M\text{ even},\\
\tfrac12\ZZ/2\ZZ, & M\text{ odd},
\end{cases}
$$
and $\pi_{M(2)}(x/2)$ is isotropic exactly when
$$
\beta_M(x,x)\in4\ZZ.
$$
:::

::: {.proof}
By @prop:dual-properties,
$$
(M(2))^\#
\isoto
M^\#(1/2)
\isoto
M(1/2),
$$
because $M$ is unimodular.
Multiplication by $2$ induces
$$
A_{M(2)}^\sharp
\isoto
M/2M.
$$
The bilinear form on $A_{M(2)}$ is therefore $\tfrac12\ZZ/\ZZ$-valued.
Finally,
$$
\beta_{M(2)}(x/2,x/2)
=
\tfrac12\beta_M(x,x),
$$
which gives the displayed quadratic formula and the parity-dependent quadratic value module.
:::
