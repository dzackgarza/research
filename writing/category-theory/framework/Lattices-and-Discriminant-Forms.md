# Lattices and discriminant forms {#sec-lattices-discriminant}

Let $R$ be a Dedekind domain with fraction field $K$.
The main case is $R=\mathbb Z$ and $K=\mathbb Q$.

::: {#def-lattice}
## Lattices

An $R$-*lattice* is a finitely generated projective $R$-module $L$ equipped with a symmetric bilinear form $b\colon L\times L\to R$ whose adjoint map
$$
b^\sharp\colon L\longrightarrow L^*:=\operatorname{Hom}_R(L,R)
$$
is injective.
The category $\mathbf{Lat}_R$ is the replete full subcategory of $\mathcal B_{R,R}$ on these objects [@Nik80].

**Remark.** Positive definiteness and unimodularity are additional properties.
Freeness holds over a principal ideal domain; a basis is chosen data.
:::

::: {#exm-subobject-base-change}
**Example.** Let $L$ be an integral lattice and let $0\ne v\in L$.
The inclusion $\mathbb Zv\hookrightarrow L$ represents a subobject of the underlying $\mathbb Z$-module.
Since $\mathbb R$ is flat over $\mathbb Z$, extension of scalars from @def-module-base-change gives the monomorphism
$$
\mathbb Rv\hookrightarrow L\otimes_{\mathbb Z}\mathbb R.
$$
The two monomorphisms represent subobjects in different module categories.
:::

::: {#def-unimodular}
## Unimodular lattices

A lattice is *unimodular* if $b^\sharp$ is an isomorphism.
The unimodular lattices form a replete full subcategory $\mathbf{Unimod}_R\subseteq\mathbf{Lat}_R$.
:::

::: {#def-even-lattice}
## Even lattices

A $\mathbb Z$-lattice is *even* if $b(x,x)\in2\mathbb Z$ for every $x\in L$.
The even lattices form a replete full subcategory $\mathbf{EvenLat}_{\mathbb Z}\subseteq\mathbf{Lat}_{\mathbb Z}$.
:::

::: {#def-metric-dual}
## Dual lattice

Extend $b$ to $b_K$ on $L_K=L\otimes_RK$.
The dual lattice is
$$
L^\#=\{x\in L_K\mid b_K(x,L)\subseteq R\}.
$$
Nondegeneracy identifies $L^\#$ with $L^*$ through $x\mapsto b_K(x,-)|_L$, and $L\subseteq L^\#$.
:::

::: {#def-discriminant}
## The discriminant module and form

The *discriminant module* is
$$
A_L=L^\#/L\cong\operatorname{coker}(b^\sharp).
$$
It has a symmetric bilinear form
$$
\bar b_L\colon A_L\times A_L\longrightarrow K/R,
\qquad
\bar b_L(x+L,y+L)=b_K(x,y)+R.
$$
If $L$ is an even $\mathbb Z$-lattice, it also has the discriminant quadratic form
$$
q_L\colon A_L\longrightarrow\mathbb Q/2\mathbb Z,
\qquad
q_L(x+L)=b_{\mathbb Q}(x,x)+2\mathbb Z.
$$
The evenness hypothesis makes this formula independent of the representative [@Nik80].
:::

::: {#def-discbil}
## Discriminant bilinear forms

Let $\mathbf{DiscBil}_{\mathbb Z}$ be the replete full subcategory of $\mathcal B_{\mathbb Z,\mathbb Q/\mathbb Z}$ on finite abelian groups equipped with nondegenerate symmetric bilinear forms.
:::

::: {#def-discquad}
## Discriminant quadratic forms

Let $\mathbf{DiscQuad}_{\mathbb Z}$ be the category of finite abelian groups with $\mathbb Q/2\mathbb Z$-valued quadratic forms whose bilinearizations lie in $\mathbf{DiscBil}_{\mathbb Z}$.
Its morphisms are group homomorphisms that preserve the quadratic forms.
:::

The discriminant construction defines functors
$$
\mathbf{Lat}_{\mathbb Z}^{\simeq}\longrightarrow
\mathbf{DiscBil}_{\mathbb Z}^{\simeq}
\qquad\text{and}\qquad
\mathbf{EvenLat}_{\mathbb Z}^{\simeq}\longrightarrow
\mathbf{DiscQuad}_{\mathbb Z}^{\simeq}.
$$

## Radical and unimodularity {#sec-radical-unimodularity}

::: {#def-two-witnesses}
For any symmetric bilinear form on a finitely generated projective module, define
$$
\operatorname{rad}(L)=\ker(b^\sharp),
\qquad
\operatorname{disc}(L)=\operatorname{coker}(b^\sharp).
$$
Then $b$ is nondegenerate exactly when $\operatorname{rad}(L)=0$, and it is perfect exactly when both kernel and cokernel vanish.
The exact sequence is
$$
0\longrightarrow\operatorname{rad}(L)\longrightarrow L
\xrightarrow{b^\sharp}L^*\longrightarrow\operatorname{disc}(L)
\longrightarrow0.
$$
For a lattice, $\operatorname{disc}(L)=A_L$.
:::

## Localization and comparison {#sec-discriminant}

::: {#thm-localization-les}
For an $R$-module $M$, tensoring $0\to R\to K\to K/R\to0$ begins the exact sequence
$$
0\longrightarrow\operatorname{Tor}_1^R(M,K/R)\longrightarrow M
\longrightarrow M\otimes_RK\longrightarrow M\otimes_R(K/R)\longrightarrow0.
$$
For a lattice $L$, projectivity makes the Tor term vanish, so the sequence becomes
$$
0\longrightarrow L\longrightarrow L_K
\longrightarrow L\otimes_R(K/R)\longrightarrow0,
$$
and applying $\operatorname{Hom}_R(L,-)$ gives
$$
0\longrightarrow L^*\longrightarrow\operatorname{Hom}_R(L,K)
\longrightarrow\operatorname{Hom}_R(L,K/R)\longrightarrow0.
$$
The second sequence is exact because $L$ is projective.
:::

::: {#thm-double-complex}
For nondegenerate $L$, the extension $b_K^\sharp$ is an isomorphism and the form gives the commutative diagram

```{.tikz}
%%| filename: discriminant-comparison
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}[column sep=small]
0 \arrow[r] &
L \arrow[r] \arrow[d,"b^\sharp"'] &
L_K \arrow[r] \arrow[d,"b_K^\sharp\;(\sim)"'] &
L\otimes_R(K/R) \arrow[r] \arrow[d,"\bar b"] &
0\\
0 \arrow[r] &
L^* \arrow[r] &
\operatorname{Hom}_R(L,K) \arrow[r] &
\operatorname{Hom}_R(L,K/R) \arrow[r] &
0
\end{tikzcd}
```

The snake lemma identifies
$$
A_L\cong L^\#/L\cong\operatorname{coker}(b^\sharp)
$$
and gives
$$
0\longrightarrow A_L\longrightarrow L\otimes_R(K/R)
\longrightarrow\operatorname{Hom}_R(L,K/R)\longrightarrow0.
$$
:::

These functors send an isometry of lattices to its induced isometry of discriminant forms.
They are used in the next chapter.
