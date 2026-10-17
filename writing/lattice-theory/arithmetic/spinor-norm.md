# Determinant and spinor norm {#sec:lattice-spinor-norm}

::: {.definition #def:spinor-norm title="Determinant and spinor-norm exact sequences"}

Let $F$ be a field of characteristic different from $2$, and let $(V,\beta)$ be a finite-dimensional nondegenerate symmetric $F$-bilinear space.
For anisotropic $w\in V$, define the reflection
$$
s_w(x)
\definedas
x-2\frac{\beta(x,w)}{\beta(w,w)}w.
$$
By Cartan--Dieudonne, these reflections generate $\Orth(V)$.

The normalized spinor norm is
$$
\spinornorm_F\colon
\Orth(V)
\too
F^\times/(F^\times)^2,
$$
with
$$
\spinornorm_F(s_w)
=
\left[-\frac{\beta(w,w)}2\right].
$$
Define $\SO(V)$ and $\Theta_F(V)$ by the short exact sequences
$$
1
\too
\SO(V)
\too
\Orth(V)
\xrightarrow{\det}
\operatorname{im}(\det)
\too
1
$$
and
$$
1
\too
\Theta_F(V)
\too
\Orth(V)
\xrightarrow{\spinornorm_F}
\operatorname{im}(\spinornorm_F)
\too
1.
$$
:::

::: {.definition #def:lattice-spinor-kernels title="Spinor kernels of an integral lattice"}

Let $L$ be an integral lattice and let $F$ be a field equipped with a ring morphism
$$
\bZ\too F.
$$
Scalar extension induces
$$
\Orth(L)\too\Orth(L_F).
$$
Composing with determinant and spinor norm defines short exact sequences
$$
1
\too
\SO_F(L)
\too
\Orth(L)
\too
\operatorname{im}(\det_F|_{\Orth(L)})
\too
1
$$
and
$$
1
\too
\Theta_F(L)
\too
\Orth(L)
\too
\operatorname{im}(\spinornorm_F|_{\Orth(L)})
\too
1.
$$

For signature $(2,n)$ define
$$
\Orth^+(L)\definedas\Theta_\bR(L),
$$
and define the simultaneous discriminant-and-spinor kernel by the pullback
$$
\widetilde\Orth^+(L)
\definedas
\widetilde\Orth(L)\times_{\Orth(L)}\Orth^+(L).
$$
:::
