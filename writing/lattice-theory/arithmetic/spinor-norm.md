# Determinant and spinor norm {#sec-lattice-spinor-norm}

::: {.definition #def:spinor-norm title="Determinant and spinor-norm exact sequences"}

Let $F$ be a field of characteristic different from $2$, and let $(V,\beta)$ be a finite-dimensional nondegenerate symmetric $F$-bilinear space.
For anisotropic $w\in V$, define the reflection
$$
s_w(x)
\definedas
x-2\frac{\beta(x,w)}{\beta(w,w)}w.
$$
By the Cartan--Dieudonné theorem, these reflections generate the group $\Orth(V)$ [@Mei13, Theorem 1.1].

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

By the Cartan--Dieudonné theorem [@Mei13, Theorem 1.1] the reflections generate $\Orth(L_\bR)$, so the two homomorphisms agree on $\Orth(L_\bR)$ and hence on $\Orth(L)$: $\chi=\spinornorm_\bR$ there, and $\Orth^+(L)=\Theta_\bR(L)=\ker\spinornorm_\bR=\ker\chi$ preserves each component.
:::

## Orientation characters of a real quadratic space {#sec-orientation-characters}

Throughout this section $(V,\beta)$ is a finite-dimensional nondegenerate symmetric $\bR$-bilinear space of signature $(p,q)$ in the sense of @def:signature.
Write $\Gr^+(V)$ for the set of $p$-dimensional subspaces of $V$ on which $\beta$ is positive definite, topologized as a subset of the Grassmannian of $p$-planes in $V$, and write
$$
\widetilde\Gr^+(V)\too\Gr^+(V)
$$
for the restriction to $\Gr^+(V)$ of the two-sheeted covering of that Grassmannian by the Grassmannian of oriented $p$-planes; its fibre over $W$ is the set of the two orientations of $W$ modulo $\bR_{>0}$ (@def:free-module-orientation).
The zero space has $\det(0)=\bR$ and hence the two orientation classes of $\pm1$, so the covering is defined for $p=0$ too.
The group $\Orth(V)$ acts continuously on both spaces, by $g\cdot(W,o)=(gW,g_*o)$.
When the form must be named, these spaces are written $\Gr^+(V,\beta)$ and $\widetilde\Gr^+(V,\beta)$.

::: {.lemma #lem:positive-grassmannian title="Maximal positive-definite subspaces form a contractible space"}

Let $W_0\in\Gr^+(V)$, and let $\pi_{W_0}\colon V\to W_0$ be the projection with kernel $W_0^\perp$.

1. For every $W\in\Gr^+(V)$, the restriction $\pi_{W_0}|_W\colon W\to W_0$ is an isomorphism.
2. The space $\Gr^+(V)$ is contractible, and $\widetilde\Gr^+(V)$ has exactly two connected components.
3. Two points $(W,o)$ and $(W',o')$ of $\widetilde\Gr^+(V)$ lie in the same component exactly when $\pi_W|_{W'}\colon W'\to W$ carries $o'$ to $o$.
:::

::: {.proof}

By @thm:sylvester, $\beta$ is negative definite on $W_0^\perp$.
A vector of $W\cap W_0^\perp$ has both nonnegative and nonpositive square, so it is zero; since $\dim W=\dim W_0$, this proves (1).

By (1), every $W\in\Gr^+(V)$ is the graph of a unique linear map $\phi_W\colon W_0\to W_0^\perp$.
The graph of $\phi$ is positive definite exactly when
$$
-\beta(\phi x,\phi x)<\beta(x,x)
\qquad\text{for all }0\neq x\in W_0,
$$
which says that $\phi$ has operator norm less than $1$ for the Euclidean norms $\beta|_{W_0}$ and $-\beta|_{W_0^\perp}$.
The map $W\mapsto\phi_W$ is therefore a homeomorphism from $\Gr^+(V)$ onto an open ball of $\Hom_\bR(W_0,W_0^\perp)$.
A covering of a contractible space is trivial, so $\widetilde\Gr^+(V)$ has two components, and they are exchanged by $(W,o)\mapsto(W,-o)$.

For (3), define $c\qty{(W,o),(W',o')}\in\theset{\pm1}$ to be $+1$ when $\pi_W|_{W'}$ carries $o'$ to $o$ and $-1$ otherwise.
By (1) this function is defined on all of $\widetilde\Gr^+(V)\times\widetilde\Gr^+(V)$.
The isomorphism $\pi_W|_{W'}$ depends continuously on $(W,W')$, so $c$ is locally constant, and it is constant on each of the four components of the product.
It equals $+1$ on the diagonal and changes sign when $o'$ is replaced by $-o'$.
Hence $c=+1$ exactly on the two components of the product that meet the diagonal.
:::

::: {.definition #def:orientation-characters title="Orientation characters"}

The two components of $\widetilde\Gr^+(V)$ are the *orientation classes of maximal positive-definite subspaces* of $V$.
The *positive orientation character* of $(V,\beta)$ is the map
$$
\sigma_+\colon\Orth(V)\too\theset{\pm1}
$$
with $\sigma_+(g)=+1$ exactly when $g$ maps each orientation class to itself.
The *negative orientation character*
$$
\sigma_-\colon\Orth(V)\too\theset{\pm1}
$$
is the positive orientation character of $(V,-\beta)$, under the equality $\Orth(V,\beta)=\Orth(V,-\beta)$.
For a sign $\epsilon\in\theset{\pm1}$, write $\sigma_\epsilon$ for $\sigma_+$ when $\epsilon=+1$ and for $\sigma_-$ when $\epsilon=-1$.
:::

The maps $\sigma_\pm$ are group morphisms, because $\Orth(V)$ acts on the two-element set of orientation classes.
By @lem:positive-grassmannian (3), for every $W\in\Gr^+(V)$ and every $g\in\Orth(V)$,
$$
\sigma_+(g)=\sgn\det\qty{\pi_W\circ g|_W\colon W\too W},
$$
so $\sigma_+$ and $\sigma_-$ are continuous, and both are trivial on the identity component $\Orth(V)^\circ$.
The character $\sigma_+$ is trivial when $p=0$, and $\sigma_-$ is trivial when $q=0$.

::: {.proposition #prop:orientation-characters-reflections title="Orientation characters, the determinant, and the real spinor norm"}

1. For anisotropic $w\in V$,
$$
\sigma_+(s_w)=-\sgn\beta(w,w),
\qquad
\sigma_-(s_w)=\sgn\beta(w,w).
$$
2. Under the identification $\bR^\times/(\bR^\times)^2=\theset{\pm1}$,
$$
\sigma_+=\spinornorm_\bR,
\qquad
\sigma_+\sigma_-=\det.
$$
3. If $V=V_1\perp V_2$ and $g_i\in\Orth(V_i)$, then $\sigma_\pm(g_1\oplus g_2)=\sigma_\pm(g_1)\,\sigma_\pm(g_2)$.
4. If $L$ is an indefinite lattice, then $\Orth^+(L)$ is the kernel of the restriction of $\sigma_+$ to $\Orth(L)\iscontainedin\Orth(L_\bR)$.
:::

::: {.proof}

Let $w$ be anisotropic.
If $\beta(w,w)>0$, choose $W\in\Gr^+(V)$ containing $w$.
Then $s_w$ preserves $W$ and acts on it with determinant $-1$, so $s_w(W,o)=(W,-o)$ and $\sigma_+(s_w)=-1$.
If $\beta(w,w)<0$, the space $w^\perp$ has signature $(p,q-1)$; choose $W\in\Gr^+(V)$ inside $w^\perp$.
Then $s_w$ fixes $W$ pointwise, so $\sigma_+(s_w)=+1$.
The values of $\sigma_-$ follow by replacing $\beta$ with $-\beta$, which does not change $s_w$.

For (2), @def:spinor-norm gives $\spinornorm_\bR(s_w)=[-\beta(w,w)/2]$, which is $-1$ exactly when $\beta(w,w)>0$, and $\det s_w=-1$.
By (1), the two sides of each equality agree on every reflection, and the reflections generate $\Orth(V)$ by the Cartan--Dieudonné theorem [@Mei13, Theorem 1.1].

For (3), write each $g_i$ as a composite of reflections $s_w$ of $V_i$.
For $w\in V_1$, the isometry $s_w\oplus\id_{V_2}$ is the reflection of $V$ in $w$, and likewise for $w\in V_2$; the claim follows from (1).

Statement (4) is (2) together with $\Orth^+(L)=\Theta_\bR(L)$ from @def:lattice-spinor-kernels.
:::

::: {.lemma #lem:orientation-characters-identity-component title="The common kernel of the orientation characters is the identity component"}

$$
\ker\sigma_+\cap\ker\sigma_-=\Orth(V)^\circ.
$$
:::

::: {.proof}

The inclusion $\supseteq$ was shown after @def:orientation-characters.
Let $g\in\ker\sigma_+\cap\ker\sigma_-$, fix $W\in\Gr^+(V)$, and let $\phi\colon W\to W^\perp$ be the linear map whose graph is $gW$ (@lem:positive-grassmannian).
For $t\in[0,1]$ let $W_t$ be the graph of $t\phi$; it lies in $\Gr^+(V)$, and $W_t^\perp$ is the graph of $t\phi^*\colon W^\perp\to W$, where $\beta(\phi x,y)=-\beta(x,\phi^*y)$.
Choose bases of $W$ and of $W^\perp$ that are orthonormal for $\beta$ and for $-\beta$.
Applying the Gram--Schmidt process to their images under $x\mapsto x+t\phi x$ and $y\mapsto y+t\phi^*y$ gives bases of $W_t$ and of $W_t^\perp$, orthonormal for $\beta$ and for $-\beta$, that depend continuously on $t$.
Let $h_t\in\Orth(V)$ carry the chosen bases to these.
Then $h_0=\id$, so $h_1\in\Orth(V)^\circ$, and $h_1W=gW$.

The isometry $h_1^{-1}g$ preserves $W$ and $W^\perp$; write it as $a\oplus b$ with $a\in\Orth(W)$ and $b\in\Orth(W^\perp)$.
On the positive-definite space $W$ every reflection has $\sigma_+=-1$ and $\sigma_-=+1$, so $\sigma_+(a)=\det a$ and $\sigma_-(a)=1$; likewise $\sigma_-(b)=\det b$ and $\sigma_+(b)=1$.
By @prop:orientation-characters-reflections (3),
$$
\det a=\sigma_+(h_1^{-1}g)=1,
\qquad
\det b=\sigma_-(h_1^{-1}g)=1.
$$
The group $\SO(W)\times\SO(W^\perp)$ is connected, so $h_1^{-1}g\in\Orth(V)^\circ$, and therefore $g\in\Orth(V)^\circ$.
:::
