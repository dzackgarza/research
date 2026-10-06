# Isometries and arithmetic invariants {#sec-isometry}

## Isometries and automorphism groups {#sec-isometry-groups}

Let $\mathbf{Lat}_R^{\simeq}$ be the core of the category of $R$-lattices.
Its morphisms are isometries.
For lattices $L$ and $M$,
$$
\operatorname{Iso}(L,M)
=\Hom_{\mathbf{Lat}_R^{\simeq}}(L,M),
\qquad
O(L)=\Aut(L).
$$
When nonempty, $\operatorname{Iso}(L,M)$ is an $(O(M),O(L))$-bitorsor: $O(M)$ acts on the left by postcomposition and $O(L)$ acts on the right by precomposition.

::: {.definition #def:discriminant-rep title="Bilinear and quadratic discriminant representations"}

Let $L$ be an integral lattice and $\varphi\in\Orth(L)$. Scalar extension gives
$$
\varphi_\QQ\in\Orth(L_\QQ),
$$
and $\varphi_\QQ$ preserves $L^\#$, hence induces the bilinear isometry
$$
\bar\varphi\colon A_L\isoto A_L,
\qquad
\bar\varphi([x])=[\varphi_\QQ(x)].
$$
The **bilinear discriminant representation** is
$$
\rho_L\colon\Orth(L)\too\Orth(A_L),
\qquad
\varphi\longmapsto\bar\varphi.
$$
Define the stable discriminant kernel by the pullback
```tikzcd id="stable-orthogonal-pullback"
\widetilde\Orth(L) \arrow[r] \arrow[d] & \Orth(L) \arrow[d,"\rho_L"] \\
1 \arrow[r] & \Orth(A_L).
```
Write
$$
\Orth(L)\twoheadrightarrow I_L\injects\Orth(A_L)
$$
for the epi--mono factorization of $\rho_L$.

If $L$ is even, $\bar\varphi$ preserves the quadratic refinement and defines
$$
\rho_{L,q}\colon\Orth(L)\too\Orth(A_{L,q}).
$$
The forgetful monomorphism
$$
j_q\colon\Orth(A_{L,q})\injects\Orth(A_L)
$$
satisfies $\rho_L=j_q\circ\rho_{L,q}$.
Hence
$$
\ker(\rho_{L,q})=\widetilde\Orth(L).
$$
Write
$$
\Orth(L)\twoheadrightarrow I_{L,q}\injects\Orth(A_{L,q})
$$
for the epi--mono factorization of $\rho_{L,q}$.
:::

Let $f\colon(L,b_L)\to(M,b_M)$ be a morphism of $\mathcal B_{R,W}$ and let $b_L$ be nondegenerate.
Then $f$ is injective: if $f(x)=0$ then $b_L(x,y)=b_M(fx,fy)=0$ for every $y\in L$, so $x\in\radic(L)=0$.

Every object of $\mathbf{Lat}_R$ is nondegenerate, so every morphism of $\mathbf{Lat}_R$ is a monomorphism on underlying $R$-modules. The forgetful maps are injective maps of sets
$$
\operatorname{PrimEmb}(L,M)
\xrightarrow{\;j_{L,M}\;}
\Hom_{\mathbf{Lat}_R}(L,M)
\xrightarrow{\;U_{L,M}\;}
\Hom_{R\text{-}\mathbf{Mod}}(U L,U M).
$$
:::

::: {.definition #def:primitive-embedding title="Primitive embeddings"}

A morphism $f\colon L\to M$ of $\mathbf{Lat}_R$ is a *primitive embedding* when the cokernel object
$$
Q_f\definedas\coker_{R\text{-}\mathbf{Mod}}(U f)
$$
is torsion-free. Since $U f$ is a monomorphism, its canonical cokernel sequence is
$$
0\too L\xrightarrow{f}M\too Q_f\too0
$$
Write $\operatorname{PrimEmb}(L,M)$ for the set of morphisms satisfying this condition.
A subobject of $M$ (@def:subobject-relation) is *primitive* when any representing monomorphism has this property.

Identities are primitive, and primitivity is closed under composition.
For primitive $f\colon L\to M$ and $g\colon M\to P$, the canonical cokernel maps fit into the short exact sequence
$$
0\too Q_f\too Q_{gf}\too Q_g\too0.
$$
Since $Q_f$ and $Q_g$ are torsion-free, so is $Q_{gf}$.
Hence the primitive embeddings form a subcategory of $\mathbf{Lat}_R$ with the same objects.
:::

::: {.example #ex:primitive-and-scaled title="Primitive and nonprimitive embeddings"}
Let $U$ be the hyperbolic plane of @def:hyperbolic-plane on $e,f$, let $\langle1\rangle$ be the rank one lattice on $w$ with $b(w,w)=1$, and let $M=U\perp\langle1\rangle$.
Define
$$
\iota\colon U\too M,
\qquad
\iota(e)=e,
\qquad
\iota(f)=f.
$$
This is a morphism of $\mathbf{Lat}_{\bZ}$ and its cokernel sequence is
$$
0\too U\xrightarrow{\iota}M\too\bZ w\too0,
$$
so $\iota$ is primitive.
Define
$$
\jmath\colon U(4)\too M,
\qquad
\jmath(e)=2e,
\qquad
\jmath(f)=2f.
$$
Since $\jmath^*\beta_M=4\beta_U$, this is a morphism $U(4)\to M$ in $\mathbf{Lat}_{\bZ}$. Its cokernel sequence is
$$
0\too U(4)\xrightarrow{\jmath}M\too \bZ w\oplus(\bZ/2\bZ)^2\too0,
$$
so $\jmath$ is not primitive.
:::

## Adjoints, similarities and the index of an embedding {#sec-adjoint-similarity}

::: {.definition #def:adjoint-morphism title="The adjoint of a module morphism"}

Let $(M,b_M),(N,b_N)\in\mathcal B_{R,W}$ and let
$$
f\in\Hom_{R\text{-}\mathbf{Mod}}(M,N).
$$
Write
$$
f^\vee\definedas\Hom_{R\text{-}\mathbf{Mod}}(f,W)\colon
\Hom_{R\text{-}\mathbf{Mod}}(N,W)\too\Hom_{R\text{-}\mathbf{Mod}}(M,W).
$$
An **adjoint** of $f$ is a morphism $f^*\in\Hom_{R\text{-}\mathbf{Mod}}(N,M)$ making the square
```tikzcd id="adjoint-morphism-square"
N \arrow[r,"f^*"] \arrow[d,"b_N^\sharp"'] & M \arrow[d,"b_M^\sharp"] \\
\Hom_{R\text{-}\mathbf{Mod}}(N,W) \arrow[r,"f^\vee"'] & \Hom_{R\text{-}\mathbf{Mod}}(M,W)
```
commute.
If $b_M$ is nondegenerate, such an adjoint is unique when it exists. If $b_M$ is perfect, it exists and equals $(b_M^\sharp)^{-1}\circ f^\vee\circ b_N^\sharp$.
:::

::: {.proposition #prop:adjoint-matrix title="The adjoint in coordinates"}

Let $(M,b_M),(N,b_N)\in\mathcal B_{R,R}$ have finite free underlying $R$-modules. Choose ordered bases $B_M,B_N$ and write
$$
G_M\definedas[b_M]_{B_M},\qquad G_N\definedas[b_N]_{B_N},\qquad
A\definedas[f]_{B_N\leftarrow B_M}.
$$
If $b_M$ is perfect, then
$$
[f^*]_{B_M\leftarrow B_N}=G_M^{-1}A^{\mathsf T}G_N.
$$
When $M=N$, $B_M=B_N=B$, and $f\in\operatorname{End}_{R\text{-}\mathbf{Mod}}(M)$, one has $f\in O(M)$ exactly when $A^{\mathsf T}G_MA=G_M$; in that case
$$
A^{-1}=G_M^{-1}A^{\mathsf T}G_M.
$$
:::

::: {.definition #def:similarity title="Similarity morphisms"}

For $(M,b_M),(N,b_N)\in\mathcal B_{R,W}$ and $\lambda\in R$, define
$$
\operatorname{Sim}_\lambda(M,N)
\definedas
\Hom_{\mathcal B_{R,W}}\bigl(M(\lambda),N\bigr),
$$
where $M(\lambda)$ is the twist of @def:form-twist. An element of this Hom-set is a **similarity morphism of multiplier $\lambda$**.
For $W=R$, finite free $M,N$, and chosen bases $B_M,B_N$, a morphism $f\in\operatorname{Sim}_\lambda(M,N)$ with matrix $A=[f]_{B_N\leftarrow B_M}$ satisfies $A^{\mathsf T}G_NA=\lambda G_M$.
If $M$ and $N$ have equal rank $n$, then
$$
\det(A)^2\det(G_N)=\lambda^n\det(G_M).
$$
:::

::: {.proposition #prop:embedding-index title="The index of an embedding"}

Let $f\colon L\to M$ be a morphism of $\mathbf{Lat}_{\bZ}$ between lattices of the same rank $n$.
Then its cokernel sequence
$$
0\too L\xrightarrow{f}M\too Q_f\too0
$$
has a finitely generated torsion $\bZ$-module $Q_f$. Its cardinality is the index $[M:f(L)]$ of @def:index, and
$$
\det(b_L)=[M:f(L)]^{2}\det(b_M).
$$
Choose ordered bases $B_L,B_M$ and write $G_L=[b_L]_{B_L}$, $G_M=[b_M]_{B_M}$, and $A=[f]_{B_M\leftarrow B_L}$. Then
$$
G_L=A^{\mathsf T}G_MA,\qquad |\det A|=[M:f(L)].
$$
Index $1$ holds exactly for the isometries.
:::

## Reflections {#sec-reflections}

::: {.definition #def:reflection-in-a-vector title="Reflection in a vector"}

Let $R$ be a Dedekind domain with fraction field $K$, let $L\in\mathbf{Lat}_R$, and let $v\in L$ be anisotropic.
The *reflection in* $v$ is the endomorphism
$$
s_v\in\operatorname{End}_{K\text{-}\mathbf{Mod}}(L_K),
\qquad
s_v(x)=x-\frac{2\,\beta_{L_K}(x,v)}{\beta_L(v,v)}\,v,
$$
on the base change $L_K$ of @def:module-base-change.

It sends $v$ to $-v$, fixes $v^{\perp}$ pointwise, and squares to the identity.
It preserves $\beta_{L_K}$: writing $c=2\beta_{L_K}(x,v)/\beta_L(v,v)$ and $d=2\beta_{L_K}(y,v)/\beta_L(v,v)$,
$$
\beta_{L_K}(x-cv,\;y-dv)
=\beta_{L_K}(x,y)-d\,\beta_{L_K}(x,v)-c\,\beta_{L_K}(y,v)+cd\,\beta_L(v,v)
=\beta_{L_K}(x,y),
$$
the last two terms cancelling the first two.
So $s_v\in O(L_K)$.
:::

::: {.proposition #prop:reflection-integrality title="When a reflection is an isometry of $L$"}

Keep the notation of @def:reflection-in-a-vector and define the pairing ideal by the image factorization
$$
I_v\definedas\operatorname{im}\bigl(\beta_L(-,v)\colon U L\to R\bigr)\triangleleft R.
$$
Scalar extension induces
$$
\operatorname{bc}_{L,K}\colon
\operatorname{End}_{R\text{-}\mathbf{Mod}}(U L)
\too
\operatorname{End}_{K\text{-}\mathbf{Mod}}(L_K),
\qquad
f\longmapsto f\tensor_R K.
$$
Since $U L$ is finite projective, $\operatorname{End}_{R\text{-}\mathbf{Mod}}(U L)$ is torsion-free, so $\operatorname{bc}_{L,K}$ is a monomorphism.
Then
$$
s_v\in\operatorname{im}(\operatorname{bc}_{L,K})
\quad\Longleftrightarrow\quad
2I_v\iscontainedin\beta_L(v,v)R.
$$
Under this condition let $\widetilde s_v$ be the unique preimage. Faithfulness of scalar extension on these Hom-modules gives $\widetilde s_v^2=\id_L$ and $\widetilde s_v^*\beta_L=\beta_L$, hence $\widetilde s_v\in O(L)$.
For $R=\bZ$, @def:lattice-basic-invariants gives $I_v=\div_L(v)\bZ$. In particular the condition holds when $\beta_L(v,v)\in\{\pm1,\pm2\}$; hence reflections in roots of square $-2$ lie in $O(L)$.
:::

## Matrix realizations

::: {.proposition #prop:matrix-realizations title="Matrix realizations of isometry and automorphism groups"}
Let $L\in\mathbf{Lat}_R$ have free underlying module of rank $n$. Choose an ordered basis $B_L$ and write $G_L=[b_L]_{B_L}$. The corresponding coordinate isomorphism identifies
$$
O(L)\cong\{A\in\operatorname{GL}_n(R)\mid A^{\mathsf T}G_LA=G_L\}.
$$
Changing the basis conjugates this subgroup.
For a finitely generated torsion $\bZ$-module $A$, choose an invariant-factor decomposition $A\isoto\bigoplus_{i=1}^r\bZ/d_i\bZ$.
An element of $\operatorname{End}_{\bZ\text{-}\mathbf{Mod}}(A)$ is represented by a matrix $(a_{ij})$ whose entry $a_{ij}$ represents a morphism $\bZ/d_j\bZ\to\bZ/d_i\bZ$, equivalently $d_j a_{ij}=0$ in $\bZ/d_i\bZ$; the automorphisms are the units of this endomorphism ring.
In the homocyclic case this gives
$$
\Aut\bigl((\bZ/d\bZ)^n\bigr)
\cong\GL_n(\bZ/d\bZ).
$$
:::

## Isometries of a degenerate form {#sec-degenerate-isometries}

::: {.proposition #prop:orthogonal-group-degenerate title="The orthogonal group of a degenerate form"}

Let $R$ be a Dedekind domain and let $b$ be a symmetric bilinear form with values in $R$ on a finitely generated projective $R$-module $M$.
Every isometry of $(M,b)$ maps $\radic(M)$ onto itself, so it acts on the radical and on the radical quotient.
Fix a splitting $M=\radic(M)\oplus N$ as in @thm:radical-splits.
In block form with respect to that splitting an isometry is
$$
\begin{pmatrix}a&\varphi\\0&d\end{pmatrix},
\qquad
a\in\Aut_{R\text{-}\mathbf{Mod}}(\radic(M)),\quad
\varphi\in\Hom_{R\text{-}\mathbf{Mod}}(N,\radic(M)),\quad
d\in\Orth(N),
$$
with no condition relating the three, because every pairing involving $\radic(M)$ vanishes.
Hence
$$
\Orth(M)\;\cong\;\Hom_{R\text{-}\mathbf{Mod}}\bigl(N,\radic(M)\bigr)
\rtimes\bigl(\Aut_{R\text{-}\mathbf{Mod}}(\radic(M))\times\Orth(N)\bigr),
$$
and the subgroup fixing $\radic(M)$ pointwise is the preimage of $\{1\}\times\Orth(N)$.
:::

## Index

::: {.definition #def:index title="Index of a subgroup"}
For a subgroup $H\le G$, the *index* $[G:H]$ is the cardinality of the set of left cosets $G/H$.
If $G$ is finite, $[G:H]=|G|/|H|$.
In an abelian category, the analogous cardinality of a cokernel is used only after the relevant monomorphism and finiteness hypotheses have been stated.
:::

## The Miranda--Morrison sequence

::: {.theorem #thm:miranda-morrison title="The Miranda–Morrison exact sequence"}
Let $L$ be an even indefinite lattice of rank at least $3$. In the notation of [@MM09, Thm. V.5.1], let
$$
\delta_L\colon\Orth(A_{L,q})\too\operatorname{MM}(L)
$$
be the Miranda--Morrison connecting morphism and let $g(L)$ be the genus group. Then
$$
1\too\widetilde\Orth(L)
\too\Orth(L)
\xrightarrow{\rho_{L,q}}\Orth(A_{L,q})
\xrightarrow{\delta_L}\operatorname{MM}(L)
\too g(L)
\too1
$$
is exact.
If $K_L\injects\Sigma(L)$ denotes the pullback subgroup represented by $\Gamma_{\mathbb Q}\cap\Sigma(L)$ in [@MM09, Thm. V.5.1], then
$$
\operatorname{MM}(L)
\isoto
\Sigma(L)\big/\big(K_L\Sigma^\#(L)\big).
$$
Consequently the epi--mono factorization of @def:discriminant-rep satisfies
$$
I_{L,q}
\isoto
\ker(\delta_L)
\injects
\Orth(A_{L,q}).
$$
:::

::: {.corollary #cor:nikulin-mm-vanishing title="Nikulin stable-range vanishing"}
If $L$ satisfies the hypotheses of [@Nik80, Thm. 1.14.2], in particular
$$
\rank L\geq\ell(L^\#/L)+2,
$$
then
$$
\rho_{L,q}\colon\Orth(L)\twoheadrightarrow\Orth(A_{L,q})
$$
is surjective and the genus of $L$ has one integral isometry class. Hence
$$
\operatorname{MM}(L)=0,
\qquad
g(L)=1.
$$
:::

::: {.definition #def:genus title="Genus of a lattice"}

Two integral lattices lie in the same genus if they are isometric over $\bR$ and over $\bZ_p$ for every prime $p$.
Extension of scalars induces the map
$$
\pi_0(\mathbf{Lat}_{\bZ}^{\simeq})
\too
\pi_0\!\left(
\mathbf{Lat}_{\bR}^{\simeq}
\times\prod_p\mathbf{Lat}_{\bZ_p}^{\simeq}
\right).
$$
The genus of $L$ is the fiber of this map over the image of $[L]$.
It is a pointed set containing $[L]$.
Its relation to the components of the homotopy fiber is governed by the exact sequence in @sec-pi0-fiber.
:::
