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

Define
$$
\Orth^+(L)\definedas\Theta_\bR(L).
$$
:::

::: {.convention #conv:spinor-positive-subgroup title="Spinor-positive subgroups"}

For a subgroup $G\le\Orth(L)$, define $G^+$ by the pullback
```tikzcd
G^+ \arrow[r] \arrow[d] \arrow[dr,phantom,very near start,"\lrcorner"] & G \arrow[d] \\
\Orth^+(L) \arrow[r] & \Orth(L)
```
[@GHS08, §1].
For $G=\SO_\bR(L)$ this defines $\SO^+(L)$, and for $G=\widetilde\Orth(L)$ it defines the simultaneous discriminant-and-spinor kernel
$$
\widetilde\Orth^+(L)
\definedas
\widetilde\Orth(L)\times_{\Orth(L)}\Orth^+(L),
$$
which is also the case $G=\Orth^+(L)$ of @conv:stable-subgroup.
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

## Orientation classes of a real quadratic space {#sec-orientation-classes}

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

::: {.definition #def:orientation-classes title="Orientation classes of maximal positive-definite subspaces"}

The two components of $\widetilde\Gr^+(V)$ are the *positive orientation classes* of $V$.
An isometry $g\in\Orth(V)$ *preserves the positive orientation classes* when it maps each of them to itself.
The *negative orientation classes* of $V$ are the positive orientation classes of the twist $V(-1)$ of @def:form-twist, under the equality $\Orth(V)=\Orth(V(-1))$.
:::

::: {.lemma #lem:orientation-classes-action title="The action of $\Orth(V)$ on the positive orientation classes"}

1. For every $W\in\Gr^+(V)$, an isometry $g\in\Orth(V)$ preserves the positive orientation classes exactly when
$$
\det\qty{\pi_W\circ g|_W\colon W\too W}>0.
$$
2. The isometries that preserve the positive orientation classes form a subgroup of $\Orth(V)$ of index at most $2$, and this subgroup contains $\Orth(V)^\circ$.
3. If $p=0$, then every $g\in\Orth(V)$ preserves the positive orientation classes.
:::

::: {.proof}

An isometry $g$ maps a maximal positive-definite subspace $W$ with orientation $o$ to the maximal positive-definite subspace $gW$ with orientation $g_*o$.
This is an action of $\Orth(V)$ on $\widetilde\Gr^+(V)$ by homeomorphisms, so $\Orth(V)$ acts on the two-element set of components.

For (1), let $o$ be an orientation of $W$.
By @lem:positive-grassmannian (3), the points $(gW,g_*o)$ and $(W,o)$ lie in the same component exactly when $\pi_W|_{gW}$ carries $g_*o$ to $o$, that is, when the automorphism $\pi_W\circ g|_W$ of $W$ preserves $o$.
An automorphism of a real vector space preserves an orientation exactly when its determinant is positive.

For (2), the subgroup is the kernel of the action on the two-element set of components, so its index is at most $2$.
For fixed $W$, the determinant in (1) is a continuous function of $g$, so the subgroup is open and closed in $\Orth(V)$; it contains $\id$, and hence it contains the connected component $\Orth(V)^\circ$.

For (3), if $p=0$ then $W=0$ is the only point of $\Gr^+(V)$, and $\pi_W\circ g|_W$ is the identity of the zero space, of determinant $1$.
:::

::: {.proposition #prop:spinor-norm-orientation-classes title="The real spinor norm and the orientation classes"}

Identify $\bR^\times/(\bR^\times)^2$ with $\theset{\pm1}$.

1. An isometry $g\in\Orth(V)$ satisfies $\spinornorm_\bR(g)=+1$ exactly when $g$ preserves the positive orientation classes of $V$.
2. For $g\in\Orth(V)=\Orth(V(-1))$, the real spinor norm of $g$ as an isometry of $V(-1)$ is $\det(g)\,\spinornorm_\bR(g)$. It is $+1$ exactly when $g$ preserves the negative orientation classes of $V$.
3. If $V=V_1\perp V_2$ and $g_i\in\Orth(V_i)$, then $\spinornorm_\bR(g_1\oplus g_2)=\spinornorm_\bR(g_1)\,\spinornorm_\bR(g_2)$.
4. If $L$ is a lattice with $L_\bR=V$, then $\Orth^+(L)$ is the subgroup of $\Orth(L)$ of isometries that preserve the positive orientation classes of $V$, and $\Orth^+(L(-1))$ is the subgroup of isometries that preserve the negative orientation classes of $V$.
:::

::: {.proof}

For (1), the action on the two positive orientation classes is a group morphism $\Orth(V)\to\theset{\pm1}$ (@lem:orientation-classes-action (2)), and so is $\spinornorm_\bR$.
The reflections generate $\Orth(V)$ [@Mei13, Theorem 1.1], so it suffices to compare the two morphisms on a reflection $s_w$.
If $\beta(w,w)>0$, choose $W\in\Gr^+(V)$ containing $w$.
Then $s_w$ preserves $W$ and acts on it with determinant $-1$, so $s_w(W,o)=(W,-o)$ and $s_w$ exchanges the two classes; also $\spinornorm_\bR(s_w)=[-\beta(w,w)/2]=-1$ (@def:spinor-norm).
If $\beta(w,w)<0$, the space $w^\perp$ has signature $(p,q-1)$; choose $W\in\Gr^+(V)$ inside $w^\perp$.
Then $s_w$ fixes $W$ pointwise, so it preserves the two classes; also $\spinornorm_\bR(s_w)=+1$.

For (2), the reflection in an anisotropic vector $w$ is the same isometry for $\beta$ and for $-\beta$, and its real spinor norm for $-\beta$ is $[\beta(w,w)/2]=-\spinornorm_\bR(s_w)=\det(s_w)\,\spinornorm_\bR(s_w)$.
Both sides of the stated equality are group morphisms that agree on the reflections, which generate $\Orth(V)$.
The second statement is (1) for $V(-1)$.

For (3), write each $g_i$ as a composite of reflections of $V_i$.
For $w\in V_1$, the isometry $s_w\oplus\id_{V_2}$ is the reflection of $V$ in $w$, and the value $\beta(w,w)$ is the same in $V_1$ and in $V$; the same holds for $w\in V_2$.

Statement (4) is (1) and (2) together with $\Orth^+(L)=\Theta_\bR(L)$ and $\Orth^+(L(-1))=\Theta_\bR(L(-1))$ from @def:lattice-spinor-kernels.
:::

::: {.proposition #prop:orth-plus-definite title="$\Orth^+$ of a definite lattice"}

Let $L$ be a lattice of signature $(p,q)$.

1. If $p=0$, then
$$
\Orth^+(L)=\Orth(L).
$$
2. If $q=0$, then
$$
\Orth^+(L)=\SO_\bR(L)=\theset{g\in\Orth(L)\st\det g=1}.
$$
:::

::: {.proof}

Put $V\definedas L_\bR$.

(1) If $p=0$, then every $g\in\Orth(V)$ preserves the positive orientation classes by @lem:orientation-classes-action (3), so $\Orth^+(L)=\Orth(L)$ by @prop:spinor-norm-orientation-classes (4).

(2) If $q=0$, then $V(-1)$ has signature $(0,p)$, and @lem:orientation-classes-action (3) for $V(-1)$ shows that every $g\in\Orth(V)$ preserves the negative orientation classes of $V$.
By @prop:spinor-norm-orientation-classes (2), $\det(g)\,\spinornorm_\bR(g)=+1$, so $\spinornorm_\bR(g)=\det(g)$ for every $g\in\Orth(V)$.
The kernel of $\det$ on $\Orth(L)$ is $\SO_\bR(L)$ (@def:lattice-spinor-kernels).
:::

::: {.lemma #lem:spinor-determinant-identity-component title="The common kernel of the determinant and the real spinor norm is the identity component"}

$$
\SO(V)\cap\Theta_\bR(V)=\Orth(V)^\circ.
$$
:::

::: {.proof}

By @prop:spinor-norm-orientation-classes (1) and (2), an isometry lies in $\SO(V)\cap\Theta_\bR(V)$ exactly when it preserves both the positive and the negative orientation classes of $V$.
The inclusion $\supseteq$ is therefore @lem:orientation-classes-action (2) for $V$ and for $V(-1)$.
Let $g\in\SO(V)\cap\Theta_\bR(V)$, fix $W\in\Gr^+(V)$, and let $\phi\colon W\to W^\perp$ be the linear map whose graph is $gW$ (@lem:positive-grassmannian).
For $t\in[0,1]$ let $W_t$ be the graph of $t\phi$; it lies in $\Gr^+(V)$, and $W_t^\perp$ is the graph of $t\phi^*\colon W^\perp\to W$, where $\beta(\phi x,y)=-\beta(x,\phi^*y)$.
Choose bases of $W$ and of $W^\perp$ that are orthonormal for $\beta$ and for $-\beta$.
Applying the Gram--Schmidt process to their images under $x\mapsto x+t\phi x$ and $y\mapsto y+t\phi^*y$ gives bases of $W_t$ and of $W_t^\perp$, orthonormal for $\beta$ and for $-\beta$, that depend continuously on $t$.
Let $h_t\in\Orth(V)$ carry the chosen bases to these.
Then $h_0=\id$, so $h_1\in\Orth(V)^\circ$, and $h_1W=gW$.

The isometry $h_1^{-1}g$ lies in $\SO(V)\cap\Theta_\bR(V)$ and preserves $W$ and $W^\perp$; write it as $a\oplus b$ with $a\in\Orth(W)$ and $b\in\Orth(W^\perp)$.
On the positive-definite space $W$ every reflection has real spinor norm $-1$ and determinant $-1$, so $\spinornorm_\bR(a)=\det a$.
On the negative-definite space $W^\perp$ every reflection has real spinor norm $+1$, so $\spinornorm_\bR(b)=+1$.
By @prop:spinor-norm-orientation-classes (3),
$$
\det a=\spinornorm_\bR(a)\,\spinornorm_\bR(b)=\spinornorm_\bR(h_1^{-1}g)=1,
\qquad
\det b=\det(h_1^{-1}g)\,(\det a)^{-1}=1.
$$
The group $\SO(W)\times\SO(W^\perp)$ is connected, so $h_1^{-1}g\in\Orth(V)^\circ$, and therefore $g\in\Orth(V)^\circ$.
:::
