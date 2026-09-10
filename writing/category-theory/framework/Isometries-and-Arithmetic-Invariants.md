# Isometries and arithmetic invariants {#sec-isometry}

## Isometries and automorphism groups {#sec-isometry-groups}

Let $\mathbf{Lat}_R^{\simeq}$ be the core of the category of $R$-lattices.
Its morphisms are isometries.
For lattices $L$ and $M$,
$$
\operatorname{Iso}(L,M)
=\operatorname{Hom}_{\mathbf{Lat}_R^{\simeq}}(L,M),
\qquad
O(L)=\operatorname{Aut}(L).
$$
When nonempty, $\operatorname{Iso}(L,M)$ is an $(O(M),O(L))$-bitorsor: $O(M)$ acts on the left by postcomposition and $O(L)$ acts on the right by precomposition.

::: {#def-discriminant-rep}
## Discriminant representation

An isometry of $L$ induces an isometry of its discriminant form.
Hence the discriminant construction gives a homomorphism
$$
O(L)\longrightarrow O(A_L,q_L)
$$
for an even lattice, and the analogous map for the discriminant bilinear form in the general case.
Its kernel is the stable orthogonal group
$$
\widetilde O(L)=\ker\bigl(O(L)\to O(A_L,q_L)\bigr).
$$
If $L$ is even and indefinite and $\operatorname{rank}(L)\geq\ell(A_L)+2$, where $\ell(A_L)$ is the minimum number of generators of $A_L$, the homomorphism $O(L)\to O(A_L,q_L)$ is surjective [@Nik80].
:::

## Embeddings and primitive embeddings {#sec-embeddings}

::: {#prp-morphism-out-of-nondegenerate}
## Morphisms out of a nondegenerate object

Let $f\colon(L,b_L)\to(M,b_M)$ be a morphism of $\mathcal B_{R,W}$ and let $b_L$ be nondegenerate.
Then $f$ is injective: if $f(x)=0$ then $b_L(x,y)=b_M(fx,fy)=0$ for every $y\in L$, so $x\in\operatorname{rad}(L)=0$.

Every object of $\mathbf{Lat}_R$ is nondegenerate, so on $\mathbf{Lat}_R$ the morphisms and the injective morphisms are the same maps, and the hierarchy of morphism sets is
$$
\operatorname{PrimEmb}(L,M)\subseteq\operatorname{Hom}_{\mathbf{Lat}_R}(L,M)\subseteq\operatorname{Hom}_R(L,M).
$$
:::

::: {#def-primitive-embedding}
## Primitive embeddings

A morphism $f\colon L\to M$ of $\mathbf{Lat}_R$ is a *primitive embedding* if $\operatorname{coker}(f)$ is torsion-free.
Primitivity is a property of the morphism, and $\operatorname{PrimEmb}(L,M)$ is the subset of $\operatorname{Hom}_{\mathbf{Lat}_R}(L,M)$ it cuts out; a subobject of $M$ (@def-subobject-relation) is called primitive when a representing monomorphism has this property.

Identities are primitive, and primitivity is closed under composition.
For primitive $f\colon L\to M$ and $g\colon M\to P$ the inclusions $gf(L)\subseteq g(M)\subseteq P$ give the exact sequence
$$
0\longrightarrow g(M)/gf(L)\longrightarrow P/gf(L)\longrightarrow P/g(M)\longrightarrow0 .
$$
Its left term is isomorphic to $\operatorname{coker}(f)$ because $g$ is injective, and its right term is $\operatorname{coker}(g)$; an extension of a torsion-free module by a torsion-free module is torsion-free, so $\operatorname{coker}(gf)$ is torsion-free.
So the primitive embeddings form a subcategory of $\mathbf{Lat}_R$ with the same objects.
:::

::: {#exm-primitive-and-scaled}
**Example.** Let $U$ be the hyperbolic plane of @def-hyperbolic-plane on $e,f$, let $\langle1\rangle$ be the rank one lattice on $w$ with $b(w,w)=1$, and let $M=U\perp\langle1\rangle$.
The morphism $e\mapsto e$, $f\mapsto f$ has cokernel $\mathbb Zw$, which is torsion-free, so it is a primitive embedding.
The map $e\mapsto2e$, $f\mapsto2f$ multiplies pairings by $4$, so it is a morphism $U(4)\to M$ for the twist $U(4)$ of @def-form-twist.
Its image is $2U$ and its cokernel is $\mathbb Zw\oplus(\mathbb Z/2\mathbb Z)^{2}$, which has torsion, so it fails primitivity.
:::

## Adjoints, similarities and the index of an embedding {#sec-adjoint-similarity}

::: {#def-adjoint-morphism}
## The adjoint of a morphism

Let $f\colon(M,b_M)\to(N,b_N)$ be $R$-linear between modules with $W$-valued forms, and write $f^{\vee}\colon\operatorname{Hom}_R(N,W)\to\operatorname{Hom}_R(M,W)$ for the induced map.
An *adjoint* of $f$ is an $R$-linear map $f^{*}\colon N\to M$ with
$$
b_M^{\sharp}\circ f^{*}=f^{\vee}\circ b_N^{\sharp},
\qquad\text{equivalently}\qquad
b_M(x,f^{*}y)=b_N(fx,y)
$$
for all $x\in M$ and $y\in N$.

If $b_M$ is nondegenerate the adjoint is unique when it exists, because $b_M^{\sharp}$ is injective.
If $b_M$ is perfect it exists and equals $(b_M^{\sharp})^{-1}\circ f^{\vee}\circ b_N^{\sharp}$.
Nondegeneracy alone does not give existence, since $b_M^{\sharp}$ need not be surjective.
:::

::: {#prp-adjoint-matrix}
## The adjoint in coordinates

Let $M$ and $N$ be free with chosen bases, let $G_M$ and $G_N$ be the Gram matrices of @prp-gram-matrix-free-module, and let $A$ be the matrix of $f$ on column vectors.
If $G_M$ is invertible then
$$
f^{*}\ \text{has matrix}\ G_M^{-1}A^{\mathsf T}G_N .
$$
For $M=N$ with a perfect form and Gram matrix $G$, the endomorphism $f$ lies in $O(M)$ exactly when $A^{\mathsf T}GA=G$, and then
$$
A^{-1}=G^{-1}A^{\mathsf T}G,
$$
so an isometry is an endomorphism whose adjoint is its inverse.
The identity $A^{-1}=A^{\mathsf T}$ holds when $G$ is the identity matrix.
:::

::: {#def-similarity}
## Similarities

A *similarity of scale* $\lambda\in R$ from $(M,b_M)$ to $(N,b_N)$ is an $R$-linear map $f$ with
$$
b_N(fx,fy)=\lambda\,b_M(x,y),
$$
that is, a morphism $(M,b_M(\lambda))\to(N,b_N)$ of @def-form-categories for the twist $b_M(\lambda)$ of @def-form-twist.
The isometries are the similarities of scale $1$.
In bases this reads $A^{\mathsf T}G_NA=\lambda G_M$, so for modules of equal rank $n$,
$$
\det(A)^{2}\det(G_N)=\lambda^{\,n}\det(G_M).
$$
:::

::: {#prp-embedding-index}
## The index of an embedding

Let $f\colon L\to M$ be a morphism of $\mathbf{Lat}_{\mathbb Z}$ between lattices of the same rank $n$.
Then $\operatorname{coker}(f)$ is finite, its order is the index $[M:f(L)]$ of @def-index, and
$$
\det(b_L)=[M:f(L)]^{2}\det(b_M).
$$
The matrix $A$ of $f$ satisfies $G_L=A^{\mathsf T}G_MA$ and $|\det A|=[M:f(L)]$.
Index $1$ holds exactly for the isometries.
:::

## Reflections {#sec-reflections}

::: {#def-reflection}
## Reflection in a vector

Let $R$ be a Dedekind domain with fraction field $K$, let $L$ be an $R$-lattice, write $q(x)=b(x,x)$, and let $v\in L$ satisfy $q(v)\neq0$.
The *reflection in* $v$ is the $K$-linear map
$$
s_v\colon L_K\longrightarrow L_K,
\qquad
s_v(x)=x-\frac{2\,b_K(x,v)}{q(v)}\,v,
$$
on the base change $L_K$ of @def-module-base-change.

It sends $v$ to $-v$, fixes $v^{\perp}$ pointwise, and squares to the identity.
It preserves $b_K$: writing $c=2b_K(x,v)/q(v)$ and $d=2b_K(y,v)/q(v)$,
$$
b_K(x-cv,\;y-dv)
=b_K(x,y)-d\,b_K(x,v)-c\,b_K(y,v)+cd\,q(v)
=b_K(x,y),
$$
the last two terms cancelling the first two.
So $s_v\in O(L_K)$.
:::

::: {#prp-reflection-integrality}
## When a reflection is an isometry of $L$

Keep the notation of @def-reflection and let $b(L,v)\subseteq R$ be the ideal generated by the values $b(x,v)$ for $x\in L$; over $R=\mathbb Z$ its nonnegative generator is the divisibility of $v$ in $L$.

Then $s_v(L)\subseteq L$ if and only if
$$
2\,b(L,v)\subseteq q(v)R,
$$
that is, $2b(x,v)/q(v)\in R$ for every $x\in L$.
Since $s_v$ is an involution, $s_v(L)\subseteq L$ already gives $s_v\in O(L)$.

Base change along $R\hookrightarrow K$ gives an injective homomorphism $O(L)\to O(L_K)$, and $s_v$ lies in its image exactly under the displayed condition.
When the condition fails, $s_v$ is an automorphism of $L_K$ in $\mathbf{Lat}_K$ and has no preimage in $\operatorname{Aut}(L)$: the two automorphism groups belong to lattices over different rings.

For $R=\mathbb Z$ and $L$ integral the condition holds whenever $q(v)\in\{1,-1,2,-2\}$, since then $2b(x,v)/q(v)$ is $\pm2b(x,v)$ or $\pm b(x,v)$.
The reflections in the roots of a root lattice, which have $q(v)=-2$ in the sign convention of @def-definiteness, are therefore isometries of the lattice itself.
:::

## Matrix realizations

::: {#prp-matrix-realizations}
If $L$ is free and a basis has been chosen, its Gram matrix $B$ identifies
$$
O(L)=\{g\in\operatorname{GL}_n(R)\mid g^{\mathsf T}Bg=B\}.
$$
Changing the basis conjugates this subgroup.
For a finite module with mixed invariant factors, choose a decomposition $A=\bigoplus_{i=1}^r\mathbb Z/d_i\mathbb Z$.
An endomorphism is a matrix $(a_{ij})$ in which $a_{ij}$ represents a homomorphism $\mathbb Z/d_j\mathbb Z\to\mathbb Z/d_i\mathbb Z$, equivalently $d_j a_{ij}=0$ in $\mathbb Z/d_i\mathbb Z$; the automorphisms are exactly the invertible endomorphisms in this matrix ring.
In the homocyclic case this gives
$$
\operatorname{Aut}\bigl((\mathbb Z/d\mathbb Z)^n\bigr)
\cong\operatorname{GL}_n(\mathbb Z/d\mathbb Z).
$$
:::

## Isometries of a degenerate form {#sec-degenerate-isometries}

::: {#prp-orthogonal-group-degenerate}
## The orthogonal group of a degenerate form

Let $R$ be a Dedekind domain and let $b$ be a symmetric bilinear form with values in $R$ on a finitely generated projective $R$-module $M$.
Every isometry of $(M,b)$ maps $\operatorname{rad}(M)$ onto itself, so it acts on the radical and on the radical quotient.
Fix a splitting $M=\operatorname{rad}(M)\oplus N$ as in @thm-radical-splits.
In block form with respect to that splitting an isometry is
$$
\begin{pmatrix}a&\varphi\\0&d\end{pmatrix},
\qquad
a\in\operatorname{Aut}_R(\operatorname{rad}(M)),\quad
\varphi\in\operatorname{Hom}_R(N,\operatorname{rad}(M)),\quad
d\in O(N),
$$
with no condition relating the three, because every pairing involving $\operatorname{rad}(M)$ vanishes.
Hence
$$
O(M)\;\cong\;\operatorname{Hom}_R\bigl(N,\operatorname{rad}(M)\bigr)
\rtimes\bigl(\operatorname{Aut}_R(\operatorname{rad}(M))\times O(N)\bigr),
$$
and the subgroup fixing $\operatorname{rad}(M)$ pointwise is the preimage of $\{1\}\times O(N)$.
:::

## Index

::: {#def-index}
For a subgroup $H\le G$, the *index* $[G:H]$ is the cardinality of the set of left cosets $G/H$.
If $G$ is finite, $[G:H]=|G|/|H|$.
In an abelian category, the analogous cardinality of a cokernel is used only after the relevant monomorphism and finiteness hypotheses have been stated.
:::

## The Miranda--Morrison sequence

::: {#thm-miranda-morrison}
For an even indefinite lattice $L$ of rank at least $3$, the discriminant representation fits into the Miranda--Morrison exact sequence
$$
1\to\widetilde O(L)\to O(L)\to O(A_L,q_L)
\to
\Sigma(L)\big/\big((\Gamma_{\mathbb Q}\cap\Sigma(L))\Sigma^\#(L)\big)
\to0
$$
with the notation and local factors of [@MM09, Thm. V.5.1]. The last group measures the failure of the discriminant representation to be surjective.
It is distinct from $\operatorname{SO}(L)=\ker(\det)$.
:::

::: {#def-genus}
## Genus {#sec-genus-sec}

Two integral lattices lie in the same genus if they are isometric over $\mathbb R$ and over $\mathbb Z_p$ for every prime $p$.
Extension of scalars induces the map
$$
\pi_0(\mathbf{Lat}_{\mathbb Z}^{\simeq})
\longrightarrow
\pi_0\!\left(
\mathbf{Lat}_{\mathbb R}^{\simeq}
\times\prod_p\mathbf{Lat}_{\mathbb Z_p}^{\simeq}
\right).
$$
The genus of $L$ is the fiber of this map over the image of $[L]$.
It is a pointed set containing $[L]$.
Its relation to the components of the homotopy fiber is governed by the exact sequence in @sec-pi0-fiber.
:::
