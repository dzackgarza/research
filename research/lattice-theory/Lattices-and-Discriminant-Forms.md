# Lattices and discriminant forms {#sec-lattices-discriminant}

Let $R$ be a Dedekind domain with fraction field $K$; the main case is $R=\bZ$ and $K=\bQ$.

::: {.definition #def:lattice title="Lattices"}

An $R$-**lattice** is a finitely generated projective $R$-module $L$ equipped with a symmetric bilinear form
$$
b\colon L\tensor_RL\too R
$$
whose adjoint
$$
b^\sharp\colon L\too L^*,
\qquad
L^*\definedas\Hom_{R\text{-}\mathbf{Mod}}(L,R),
$$
is a monomorphism.
The category $\mathbf{Lat}_R$ is the replete full subcategory of $\mathcal B_{R,R}$ on these objects [@Nik80].
:::

::: {.convention #conv:lattice-basis-choice title="Chosen bases of lattices"}
Over a principal ideal domain every lattice is free; any basis used below is chosen data rather than part of the lattice.
:::

::: {.example #ex:subobject-base-change title="Subobjects under extension of scalars"}
Let $L$ be an integral lattice and let $0\ne v\in L$.
The inclusion $\bZ v\hookrightarrow L$ represents a subobject of the underlying $\bZ$-module.
Since $\bR$ is flat over $\bZ$, extension of scalars from @def:module-base-change gives the monomorphism
$$
\bR v\hookrightarrow L\tensor_{\bZ}\bR.
$$
The two monomorphisms represent subobjects in different module categories.
:::

::: {.definition #def:unimodular title="Unimodular lattices"}

A lattice is *unimodular* if $b^\sharp$ is an isomorphism.
The unimodular lattices form a replete full subcategory with canonical inclusion
$$
\mathbf{Unimod}_R\hookrightarrow\mathbf{Lat}_R.
$$
:::

::: {.definition #def:even-lattice title="Even lattices"}

A $\bZ$-lattice is *even* if $b(x,x)\in2\bZ$ for every $x\in L$.
The even lattices form a replete full subcategory with canonical inclusion
$$
\mathbf{EvenLat}_{\bZ}\hookrightarrow\mathbf{Lat}_{\bZ}.
$$
:::

## Classification by signature {#sec-lattice-signature}

::: {.definition #def:signature-subcategories title="Signature subcategories"}

Fix an embedding $\sigma\colon R\hookrightarrow\bR$; for $R=\bZ$ it is the unique one.
Each definiteness condition of @def:definiteness is invariant under isometry, so each cuts out a replete full subcategory of $\mathbf{Lat}_R$:
$$
\mathbf{Def}_R,\quad
\mathbf{Def}^{+}_R,\quad
\mathbf{Def}^{-}_R,\quad
\mathbf{Indef}_R,\quad
\mathbf{Hyp}_R\hookrightarrow\mathbf{Indef}_R.
$$
Here $\mathbf{Hyp}_R$ consists of the lattices of signature $(1,n-1,0)$.
The definite lattices are the disjoint union of $\mathbf{Def}^{+}_R$ and $\mathbf{Def}^{-}_R$, and $\mathbf{Def}_R$ and $\mathbf{Indef}_R$ partition $\mathbf{Lat}_R$.

The twist of @def:form-twist by $-1$ sends $\mathbf{Def}^{+}_R$ to $\mathbf{Def}^{-}_R$ and is an isomorphism of categories, so a statement about positive definite lattices transports to negative definite lattices.
Under the sign convention of @def:definiteness the root lattices lie in $\mathbf{Def}^{-}_{\bZ}$.
:::

::: {.example #ex:parabolic-objects title="Parabolic forms and their radicals"}
A parabolic form has signature $(0,n-1,1)$, so its radical is nonzero and it is an object of $\mathcal B_{R,R}$ lying outside $\mathbf{Lat}_R$.
Take the forms on $\bZ^{2}$ and $\bZ^{3}$ with Gram matrices
$$
G_2=\begin{pmatrix}-2&2\\2&-2\end{pmatrix},
\qquad
G_3=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}.
$$
Both have determinant $0$; writing $J$ for the all-ones matrix, $G_3=J-3I$ has eigenvalues $-3,-3,0$, and $G_2$ has eigenvalues $-4,0$, so the signatures are $(0,1,1)$ and $(0,2,1)$.

Their radicals are spanned by $e_1+e_2$ and by $e_1+e_2+e_3$.
By @thm:radical-splits each is an orthogonal sum of its radical with a negative definite complement, and taking the complements spanned by $e_1$ and by $e_1,e_2$ gives
$$
G_2\ \text{splits as}\ \radic\perp\langle-2\rangle,
\qquad
G_3\ \text{splits as}\ \radic\perp\begin{pmatrix}-2&1\\1&-2\end{pmatrix},
$$
the second complement being the root lattice $A_2$ in the sign convention of @def:definiteness.
:::

::: {.definition #def:metric-dual title="Dual lattice"}

Extend $b$ to $b_K$ on $L_K=L\tensor_RK$. Let
$$
b_K^\sharp\colon L_K\isoto\Hom_R(L,K)
$$
be the adjoint isomorphism, and let $L^*\injects\Hom_R(L,K)$ be induced by $R\injects K$.
Define the **dual lattice** $L^\#$ by the pullback
```tikzcd id="metric-dual-pullback"
L^\# \arrow[r] \arrow[d] & L_K \arrow[d,"b_K^\sharp"] \\
L^* \arrow[r,hook] & \Hom_R(L,K).
```
The top horizontal morphism realizes $L^\#$ as a subobject of $L_K$.
:::

::: {.definition #def:dual-inclusion title="The canonical bilinear-module map to the dual lattice"}

Now specialize to an integral $\bZ$-lattice $L$.
Define the **bilinear denominator**
$$
N_b(L)\definedas\exp(L^\#/L).
$$
Equivalently, $N_b(L)$ is the least positive integer for which multiplication by $N_b(L)$ on $L^\#$ factors through
$$
\iota_L\colon L\injects L^\#.
$$
Hence
$$
\beta_{L_\bQ}(L^\#,L^\#)
\iscontainedin
\tfrac1{N_b(L)}\bZ.
$$
Hence
$$
(L,\bZ,\beta_L),
\qquad
\left(L^\#,\tfrac1{N_b(L)}\bZ,\beta_{L_\bQ}|_{L^\#}\right)
$$
are bilinear modules in the fibres of @conv:bilinear-module-fibration over $\bZ$ and $\tfrac1{N_b(L)}\bZ$, respectively.
The **canonical map to the dual lattice** is the bilinear-module morphism
$$
\boldsymbol\iota_L\colon
(L,\bZ,\beta_L)
\too
\left(L^\#,\tfrac1{N_b(L)}\bZ,\beta_{L_\bQ}|_{L^\#}\right),
$$
whose carrier morphism is the canonical monomorphism
$$
\iota_L\colon L\injects L^\#
$$
and whose value-module morphism is $\bZ\injects\tfrac1{N_b(L)}\bZ$.
:::

::: {.definition #def:discriminant title="Bilinear and quadratic discriminant forms"}

The **discriminant bilinear form** of $L$ is the cokernel in the abelian category of bilinear modules:
$$
A_L
\definedas
\coker_{\mathbf{BilMod}_{\bZ}}(\boldsymbol\iota_L).
$$
It is canonically represented by
$$
A_L
\isoto
\left(
L^\#/L,
\tfrac1{N_b(L)}\bZ/\bZ,
\bar\beta_L
\right),
$$
where

$$
\bar\beta_L\colon
(L^\#/L)\tensor_\bZ(L^\#/L)
\too
\tfrac1{N_b(L)}\bZ/\bZ,
\qquad
\bar\beta_L(x+L,y+L)
=
\beta_{L_\bQ}(x,y)+\bZ.
$$

Thus $A_L$ always denotes the bilinear discriminant object.

If $L$ is even, define its **quadratic level**
$$
N_q(L)
\definedas
\min\theset{
N>0
\st
N\,\beta_{L_\bQ}(x,x)\in2\bZ
\text{ for every }x\in L^\#
}.
$$
This is the arithmetic level of @def:lattice-level.
Its **quadratic discriminant form** is
$$
A_{L,q}
\definedas
\left(
L^\#/L,
\tfrac2{N_q(L)}\bZ/2\bZ,
q_L
\right),
$$
with
$$
q_L(x+L)
=
\beta_{L_\bQ}(x,x)+2\bZ.
$$
The quadratic level gives
$$
q_L(L^\#/L)\iscontainedin\tfrac2{N_q(L)}\bZ/2\bZ,
$$
and evenness makes this independent of the representative [@Nik80, §1.1].
:::

::: {.definition #def:discbil title="Discriminant bilinear forms"}

Let $\mathbf{DiscBil}_{\bZ}$ be the replete full subcategory of $\mathbf{BilMod}_{\bZ}$ on nondegenerate bilinear modules
$$
\left(G,\tfrac1N\bZ/\bZ,b\right)
$$
with $G$ a finite-length $\bZ$-module and $N>0$.
:::

::: {.definition #def:discquad title="Discriminant quadratic forms"}

Let $\mathbf{DiscQuad}_{\bZ}$ be the category of nondegenerate quadratic modules
$$
\left(G,\tfrac2N\bZ/2\bZ,q\right)
$$
with $G$ a finite-length $\bZ$-module and polarization an object of $\mathbf{DiscBil}_{\bZ}$.
:::

The discriminant constructions define functors
$$
\mathbf{Lat}_{\bZ}^{\simeq}
\too
\mathbf{DiscBil}_{\bZ}^{\simeq},
\qquad
L\longmapsto A_L,
$$
and
$$
\mathbf{EvenLat}_{\bZ}^{\simeq}
\too
\mathbf{DiscQuad}_{\bZ}^{\simeq},
\qquad
L\longmapsto A_{L,q}.
$$

## Elementary lattices {#sec-elementary-lattices}

::: {.definition #def:p-elementary title="$p$-elementary lattices"}

Let $p$ be a prime.
A $\bZ$-lattice $S$ is **$p$-elementary** when its discriminant carrier module is elementary:
$$
S^\#/S\isoto(\bZ/p\bZ)^a
$$
for some $a\geq0$.
Then
$$
\abs{\disc S}=p^a,
\qquad
a=\ell(S^\#/S).
$$
For $p=2$ this is Nikulin's $2$-elementary condition [@Nik80, §3.6.1].
The condition is invariant under isometry and defines a replete full subcategory of $\mathbf{Lat}_{\bZ}$.

For an even $2$-elementary lattice $S$, the coparity $\delta_S$ is the invariant of the quadratic discriminant form $A_{S,q}$ from [@Nik80, §3.6].
Let the signature of $S$ be $(t_{(+)},t_{(-)},0)$.
The genus is determined by $(\delta_S;t_{(+)},t_{(-)},a)$, and when $t_{(+)}>0$ and $t_{(-)}>0$ these invariants determine the integral isometry class [@Nik80, Thm. 3.6.2].
:::
::: {.example #ex:a3-not-two-elementary title="Determinant order does not imply 2-elementarity"}
Membership is a condition on the group $A_S$, which the order $|{\disc}\,S|$ alone leaves open.
In the sign convention of @def:definiteness the root lattice $A_3$ has Gram matrix
$$
G=\begin{pmatrix}-2&1&0\\1&-2&1\\0&1&-2\end{pmatrix},
\qquad
\det G=-4 .
$$
Write $d_1\mid d_2\mid d_3$ for the invariant factors of the carrier $A_3^\#/A_3$, so
$$
A_3^\#/A_3\isoto\bigoplus_i\bZ/d_i\bZ.
$$
Then $d_1$ is the greatest common divisor of the entries of $G$, and $d_1d_2$ is the greatest common divisor of the $2\times2$ minors; both are $1$.
Since $d_1d_2d_3=|\det G|=4$, one has
$$
A_3^\#/A_3\isoto\bZ/4\bZ.
$$
Thus the bilinear discriminant object $A_{A_3}$ is not $2$-elementary although $|\disc{A_3}|=2^2$.
:::

## Radical and unimodularity {#sec-radical-unimodularity}

::: {.definition #def:two-witnesses title="Radical and adjoint cokernel"}

For a symmetric bilinear form $b$ on a finitely generated projective $R$-module $M$, define $\radic(M)$ and the **adjoint cokernel** $Q_b$ by the exact sequence in $R\text{-}\mathbf{Mod}$
$$
0\too\radic(M)
\too M
\xrightarrow{b^\sharp}M^*
\too Q_b
\too0.
$$
Then $b$ is nondegenerate exactly when $\radic(M)=0$, and it is perfect exactly when both $\radic(M)$ and $Q_b$ vanish.

The object $Q_b$ is only the module cokernel of the adjoint. It is not the bilinear discriminant form $A_L$, which is the cokernel of $\boldsymbol\iota_L$ in $\mathbf{BilMod}_{\bZ}$ from @def:discriminant.
:::

::: {.theorem #thm:radical-splits title="The radical splits off"}

Let $R$ be a Dedekind domain, let $M$ be a finitely generated projective $R$-module, and let $b$ be a symmetric $R$-valued bilinear form on $M$.
There exists a monomorphism
$$
\nu\colon N\injects M
$$
such that the induced orthogonal-sum morphism is an isomorphism
$$
\radic(M)\perp N\isoto M,
$$
the restricted form $\nu^*b$ on $N$ is nondegenerate, and the quotient morphism induces an isometry
$$
N\isoto M/\radic(M)
$$
onto the radical quotient of @prop:quotient-form.
:::

::: {.proof}
The adjoint induces a monomorphism
$$
M/\radic(M)\injects\Hom_R(M,R).
$$
Hence $M/\radic(M)$ is finitely generated and torsion-free, therefore projective over the Dedekind domain $R$.
Choose a section
$$
\nu\colon N\isoto M/\radic(M)\too M
$$
of the quotient morphism.
Then the induced map
$$
\radic(M)\oplus N\too M
$$
is an isomorphism of $R$-modules, and orthogonality follows from the defining property of the radical.

The pullback
$$
N\mathbin{\times}_M\radic(M)
$$
is zero because the composite $N\xrightarrow{\nu}M\twoheadrightarrow M/\radic(M)$ is an isomorphism.
If $x$ lies in the radical of $\nu^*b$, then $\nu(x)$ pairs trivially with both $N$ and $\radic(M)$, hence with all of $M$.
Thus $\nu(x)$ factors through $\radic(M)\injects M$, so $x$ factors through the zero pullback above.
Therefore $x=0$ and $\nu^*b$ is nondegenerate.
:::

## Localization and comparison {#sec-discriminant}

::: {.theorem #thm:localization-les title="Localization exact sequences for lattices"}
For an $R$-module $M$, tensoring $0\to R\to K\to K/R\to0$ begins the exact sequence
$$
0\too\Tor_1^R(M,K/R)\too M
\too M\tensor_RK\too M\tensor_R(K/R)\too0.
$$
For a lattice $L$, projectivity makes the Tor term vanish, so the sequence becomes
$$
0\too L\too L_K
\too L\tensor_R(K/R)\too0,
$$
and applying $\Hom_R(L,-)$ gives
$$
0\too L^*\too\Hom_R(L,K)
\too\Hom_R(L,K/R)\too0.
$$
The second sequence is exact because $L$ is projective.
:::

::: {.theorem #thm:double-complex title="Discriminant comparison via localization"}
For nondegenerate $L$, the extension $b_K^\sharp$ is an isomorphism and the form gives the commutative diagram

```tikzcd id="discriminant-comparison"
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
```

The snake lemma identifies the module cokernel of the adjoint with the metric-dual quotient:
$$
\coker_{R\text{-}\mathbf{Mod}}(b^\sharp)
\isoto
L^\#/L.
$$
For $R=\bZ$, this is the carrier module of the bilinear discriminant object $A_L$.
On carriers the resulting exact sequence is
$$
0\too L^\#/L
\too L\tensor_R(K/R)
\too\Hom_R(L,K/R)
\too0.
$$
:::

These functors send an isometry of lattices to its induced isometry of discriminant forms.
