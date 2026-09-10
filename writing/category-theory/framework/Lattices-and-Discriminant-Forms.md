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

## Classification by signature {#sec-lattice-signature}

::: {#def-signature-subcategories}
## Signature subcategories

Fix an embedding $\sigma\colon R\hookrightarrow\mathbb R$; for $R=\mathbb Z$ it is the unique one.
Each definiteness condition of @def-definiteness is invariant under isometry, so each cuts out a replete full subcategory of $\mathbf{Lat}_R$:
$$
\mathbf{Def}_R,\quad
\mathbf{Def}^{+}_R,\quad
\mathbf{Def}^{-}_R,\quad
\mathbf{Indef}_R,\quad
\mathbf{Hyp}_R\subseteq\mathbf{Indef}_R.
$$
Here $\mathbf{Hyp}_R$ consists of the lattices of signature $(1,n-1,0)$.
The definite lattices are the disjoint union of $\mathbf{Def}^{+}_R$ and $\mathbf{Def}^{-}_R$, and $\mathbf{Def}_R$ and $\mathbf{Indef}_R$ partition $\mathbf{Lat}_R$.

The twist of @def-form-twist by $-1$ sends $\mathbf{Def}^{+}_R$ to $\mathbf{Def}^{-}_R$ and is an isomorphism of categories, so a statement about positive definite lattices transports to negative definite lattices.
Under the sign convention of @def-definiteness the root lattices lie in $\mathbf{Def}^{-}_{\mathbb Z}$.
:::

::: {#exm-parabolic-objects}
**Example.** A parabolic form has signature $(0,n-1,1)$, so its radical is nonzero and it is an object of $\mathcal B_{R,R}$ lying outside $\mathbf{Lat}_R$.
Take the forms on $\mathbb Z^{2}$ and $\mathbb Z^{3}$ with Gram matrices
$$
G_2=\begin{pmatrix}-2&2\\2&-2\end{pmatrix},
\qquad
G_3=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}.
$$
Both have determinant $0$; writing $J$ for the all-ones matrix, $G_3=J-3I$ has eigenvalues $-3,-3,0$, and $G_2$ has eigenvalues $-4,0$, so the signatures are $(0,1,1)$ and $(0,2,1)$.

Their radicals are spanned by $e_1+e_2$ and by $e_1+e_2+e_3$.
By @thm-radical-splits each is an orthogonal sum of its radical with a negative definite complement, and taking the complements spanned by $e_1$ and by $e_1,e_2$ gives
$$
G_2\ \text{splits as}\ \operatorname{rad}\perp\langle-2\rangle,
\qquad
G_3\ \text{splits as}\ \operatorname{rad}\perp\begin{pmatrix}-2&1\\1&-2\end{pmatrix},
$$
the second complement being the root lattice $A_2$ in the sign convention of @def-definiteness.
:::

::: {#def-metric-dual}
## Dual lattice

Extend $b$ to $b_K$ on $L_K=L\otimes_RK$.
The dual lattice is
$$
L^\#=\{x\in L_K\mid b_K(x,L)\subseteq R\}.
$$
Nondegeneracy identifies $L^\#$ with the dual module $L^*$ through $x\mapsto b_K(x,-)|_L$, and $L\subseteq L^\#$.
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

::: {#def-dual-inclusion}
## The canonical map to the dual lattice

$L^{\#}$ is a finitely generated projective $R$-module equipped with the restriction of $b_K$, whose values lie in $K$; it is an object of $\mathcal B_{R,K}$, and the value module of its form is $K$.
Pushing the form of $L$ along $R\hookrightarrow K$ places $L$ in the same category, and the *canonical map to the dual lattice* is the morphism
$$
\iota_L\colon L\longrightarrow L^{\#}
$$
of $\mathcal B_{R,K}$ given by the inclusion $L\subseteq L^{\#}$, which preserves forms because $b_K$ restricts to $b$ on $L$.
Under the identification of @def-metric-dual it is the adjoint map $b^{\sharp}\colon L\to L^{*}$.

The image $\iota_L(L)$ is a subobject of $L^{\#}$ and its cokernel is the discriminant module $A_L$ of @def-discriminant.
For $R=\mathbb Z$ and $L$ free with Gram matrix $G$ in a chosen basis, the matrix of $b^{\sharp}$ with respect to that basis and the dual basis is $G$, so $A_L\cong\mathbb Z^{n}/G\mathbb Z^{n}$ and the index of the image is
$$
[\,L^{\#}:\iota_L(L)\,]=|A_L|=|\det G| .
$$

The morphism $\iota_L$ is injective, so it is an isomorphism exactly when $A_L=0$, which is exactly when $L$ is unimodular in the sense of @def-unimodular.
In that case $\iota_L$ is an isometry from $L$ onto $L^{\#}$, so $L$ and $L^{\#}$ are isometric objects of $\mathcal B_{R,K}$ with distinct underlying modules.
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

## Elementary lattices {#sec-elementary-lattices}

::: {#def-p-elementary}
## $p$-elementary lattices

Let $p$ be a prime.
A $\mathbb Z$-lattice $S$ is *$p$-elementary* if $A_S\cong(\mathbb Z/p\mathbb Z)^{a}$ for some $a\geq0$, so that $|{\operatorname{disc}}\,S|=p^{a}$; for $p=2$ this is Nikulin's definition of a *2-elementary* lattice [@Nik80, §3.6.1].
The integer $a$ is the minimal number of generators of $A_S$.
Each condition is invariant under isometry, so the $p$-elementary lattices form a replete full subcategory of $\mathbf{Lat}_{\mathbb Z}$.

For an even 2-elementary lattice $S$ put $\delta_S=0$ when $q_S$ is an orthogonal direct sum of discriminant forms of the types $u^{(2)}_{+}(2)$ and $v^{(2)}_{+}(2)$, and $\delta_S=1$ otherwise [@Nik80, §3.6].
Let the signature of $S$ be $(t_{(+)},t_{(-)},0)$ in the sense of @def-signature.
The genus of an even 2-elementary lattice is determined by $(\delta_S;t_{(+)},t_{(-)},a)$, and if $t_{(+)}>0$ and $t_{(-)}>0$ these invariants determine its isometry class [@Nik80, Thm. 3.6.2].
:::

::: {#exm-a3-not-two-elementary}
**Example.** Membership is a condition on the group $A_S$, which the order $|{\operatorname{disc}}\,S|$ alone leaves open.
In the sign convention of @def-definiteness the root lattice $A_3$ has Gram matrix
$$
G=\begin{pmatrix}-2&1&0\\1&-2&1\\0&1&-2\end{pmatrix},
\qquad
\det G=-4 .
$$
Write $d_1\mid d_2\mid d_3$ for its invariant factors, so that $A_{A_3}\cong\bigoplus_i\mathbb Z/d_i\mathbb Z$.
Then $d_1$ is the greatest common divisor of the entries, which is $1$, and $d_1d_2$ is the greatest common divisor of the $2\times2$ minors, which is again $1$ because the minor on rows $2,3$ and columns $1,2$ is $\left|\begin{smallmatrix}1&-2\\0&1\end{smallmatrix}\right|=1$.
Since $d_1d_2d_3=|\det G|=4$, the invariant factors are $1,1,4$ and $A_{A_3}\cong\mathbb Z/4\mathbb Z$.
So $A_3$ is not 2-elementary although $|{\operatorname{disc}}\,A_3|=2^{2}$.
:::

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

::: {#thm-radical-splits}
## The radical splits off

Let $R$ be a Dedekind domain, let $M$ be a finitely generated projective $R$-module, and let $b$ be a symmetric bilinear form on $M$ with values in $R$.
Then there is a submodule $N\subseteq M$ with
$$
M=\operatorname{rad}(M)\oplus N,
\qquad
b|_{\operatorname{rad}(M)}=0,
\qquad
b|_{N}\ \text{nondegenerate},
$$
and the projection $N\to M/\operatorname{rad}(M)$ is an isometry onto the radical quotient of @prp-quotient-form.

The adjoint $b^{\sharp}$ induces an injection $M/\operatorname{rad}(M)\hookrightarrow\operatorname{Hom}_R(M,R)$, whose target is finitely generated projective and therefore torsion-free; so $M/\operatorname{rad}(M)$ is finitely generated and torsion-free, hence projective over the Dedekind domain $R$, and
$$
0\longrightarrow\operatorname{rad}(M)\longrightarrow M\longrightarrow M/\operatorname{rad}(M)\longrightarrow0
$$
splits.
Take $N$ to be the image of a splitting.
Every element of $\operatorname{rad}(M)$ pairs to zero with every element of $M$, so the sum is orthogonal; and if $x\in N$ satisfies $b(x,N)=0$ then also $b(x,\operatorname{rad}(M))=0$, so $b(x,M)=0$ and $x\in N\cap\operatorname{rad}(M)=0$.

So a degenerate form over a Dedekind domain is the orthogonal sum of a zero form and a nondegenerate one, and its isometry class is determined by the rank of its radical together with the isometry class of its radical quotient.
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
