# Determinant and spinor norm {#sec-lattice-spinor-norm}

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

For every indefinite $L$ define
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

::: {.lemma #lem:minus-identity-spinor-norm title="The spinor norm of $-\id$"}

Let $L$ be a lattice of signature $(p,q)$. Then
$$
\spinornorm_\bR(-\id_L) = [(-1)^p],
$$
and consequently $-\id_L\in\Orth^+(L)$ exactly when $p$ is even.
:::

::: {.proof}

Since $\bR^*/(\bR^*)^2=\theset{\pm1}$ and $2>0$, the class $[(-1)^p/2^{p+q}]$ is $[(-1)^p]$.
Diagonalising $L_\bR$ presents it as $\generators{1}^p\perp\generators{-1}^q$ with orthogonal basis $f_1,\dots,f_{p+q}$, and $-\id_L=s_{f_1}\circ\cdots\circ s_{f_{p+q}}$.
Multiplicativity of $\spinornorm_\bR$ over the composition and $\spinornorm_\bR(s_w)=[-\beta(w,w)/2]$ give
$$
\spinornorm_\bR(-\id_L)
=\prod_{i=1}^{p}\qty[-\tfrac12]\prod_{j=p+1}^{p+q}\qty[\tfrac12]
=\qty[\frac{(-1)^p}{2^{p+q}}],
$$
which is $[(-1)^p]$.
:::

::: {.proposition #prop:spinor-plus-cone-components title="$\Orth^+$ in signature $(1,n)$ preserves each component of the positive cone"}

Let $L$ be a lattice of signature $(1,n)$ and let
$$
C(L)\definedas\theset{x\in L\otimes\bR \st x^2>0}
$$
be its positive cone, which has two components.
Then $\Orth^+(L)=\Theta_\bR(L)$ is the subgroup of $\Orth(L)$ preserving each component of $C(L)$.
:::

::: {.proof}

Write $\chi\colon\Orth(L)\to\theset{\pm1}$ for the action on the two components of $C(L)$; it is a homomorphism because composition of linear maps is composition of permutations of a two-element set.
Restriction of $\spinornorm_\bR$ to $\Orth(L)$ also takes values in $\theset{\pm1}\subset\bR^*/(\bR^*)^2$, since $\bR^*/(\bR^*)^2=\theset{\pm1}$, so $\chi$ and $\spinornorm_\bR$ are two homomorphisms $\Orth(L)\to\theset{\pm1}$.

They agree on every reflection. For $w$ with $w^2<0$ one has $\spinornorm_\bR(s_w)=[-\tfrac12 w^2]=[1/2]=1$, and $s_w$ preserves $C(L)$ and each of its components: for $x\in C(L)$ the identity $s_w(x)^2=x^2>0$ keeps $x$ inside $C(L)$, and for a timelike $e$ one computes $\beta(e,s_we)=e^2-2\beta(e,w)^2/w^2>e^2>0$, so $s_we$ stays in the component of $e$. For $w$ with $w^2>0$ one has $\spinornorm_\bR(s_w)=[-\tfrac12 w^2]=[-1/2]=-1$, and $s_w(w)=-w$ carries the component containing $w$ to the other one, so $s_w$ exchanges the two components.

By Cartan--Dieudonne the reflections generate $\Orth(L_\bR)$, so the two homomorphisms agree on $\Orth(L_\bR)$ and hence on $\Orth(L)$: $\chi=\spinornorm_\bR$ there, and $\Orth^+(L)=\Theta_\bR(L)=\ker\spinornorm_\bR=\ker\chi$ preserves each component.
:::
