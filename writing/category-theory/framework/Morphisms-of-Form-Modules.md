# Morphisms of form modules {#sec-form-morphisms}

Fix a commutative ring $R$ and an $R$-module $W$, and use the form category $\mathcal B_{R,W}$ of @def-form-categories.
A morphism $f\colon(M,b_M)\to(N,b_N)$ of $\mathcal B_{R,W}$ is an $R$-linear map with $f^{*}b_N=b_M$, that is,
$$
b_N\bigl(f(x),f(y)\bigr)=b_M(x,y)
\qquad(x,y\in M).
$$
For $R$ a Dedekind domain, the lattice category $\mathbf{Lat}_R$ of @def-lattice is a replete full subcategory of $\mathcal B_{R,R}$, so its morphisms are these maps.

## Injectivity {#sec-form-morphisms-injective}

::: {#prp-form-morphism-injective}
## Kernels of form-preserving maps

Let $f\colon(M,b_M)\to(N,b_N)$ be a morphism of $\mathcal B_{R,W}$.
Then $\ker f\subseteq\ker b_M^{\sharp}$, with $b_M^{\sharp}$ the adjoint map of @def-polarization.
If $b_M$ is nondegenerate then $f$ is injective.
In particular every morphism of $\mathbf{Lat}_R$ is injective, hence a monomorphism.
:::

For $x\in\ker f$ and every $y\in M$,
$$
b_M(x,y)=b_N\bigl(f(x),f(y)\bigr)=b_N\bigl(0,f(y)\bigr)=0,
$$
so $b_M^{\sharp}(x)=0$.
Nondegeneracy of $b_M$ is injectivity of $b_M^{\sharp}$, and the lattices of @def-lattice are nondegenerate by definition.

## Pointwise sums {#sec-sums-of-form-morphisms}

::: {#prp-sum-of-form-morphisms}
## The pullback of a form along a sum

Let $f,g\colon(M,b_M)\to(N,b_N)$ be morphisms of $\mathcal B_{R,W}$ and let $f+g$ be their sum in $\operatorname{Hom}_R(M,N)$.
Then
$$
(f+g)^{*}b_N(x,y)
=2\,b_M(x,y)+b_N\bigl(f(x),g(y)\bigr)+b_N\bigl(g(x),f(y)\bigr).
$$
:::

Expanding $b_N(f(x)+g(x),f(y)+g(y))$ by bilinearity gives four terms, of which $b_N(f(x),f(y))$ and $b_N(g(x),g(y))$ both equal $b_M(x,y)$.

::: {#exm-identity-plus-identity}
## A sum of two isometries

Let $R=W=\mathbb Z$ and let $(M,b_M)=(N,b_N)=(\mathbb Z,b)$ with $b(x,y)=xy$.
Take $f=g=\operatorname{id}$.
Then $f+g$ is multiplication by $2$ and
$$
(f+g)^{*}b(1,1)=4,\qquad b(1,1)=1,
$$
so $f+g$ is not a morphism of $\mathcal B_{\mathbb Z,\mathbb Z}$.
:::

## Initial and terminal objects {#sec-form-initial-terminal}

::: {#prp-form-initial-object}
## The zero form module is initial

The pair $(0,0)$, with $0$ the zero $R$-module and its unique bilinear form, is an initial object of $\mathcal B_{R,W}$.
For an object $(M,b_M)$, the set $\operatorname{Hom}_{\mathcal B_{R,W}}\bigl((M,b_M),(0,0)\bigr)$ has one element if $b_M=0$ and is empty otherwise.
:::

Let $j\colon 0\to M$ and $k\colon M\to0$ be the unique $R$-linear maps.
Then $j^{*}b_M$ is the unique form on the zero module, so $j$ is a morphism $(0,0)\to(M,b_M)$, and it is the only one.
And $k^{*}0=0$, which equals $b_M$ exactly when $b_M=0$.

::: {#prp-summand-functor-no-right-adjoint}
## Adjoints of orthogonal sum with a fixed object

Let $M=(M,b_M)$ be an object of $\mathcal B_{R,W}$ with $b_M\neq0$ and let $F_M=-\perp M$ be the functor of @def-hyperbolic-stabilization.
Then $F_M$ does not preserve the initial object, so $F_M$ is neither a left adjoint nor an equivalence.
For $R$ a Dedekind domain and $M$ an $R$-lattice the same holds for $F_M$ on $\mathbf{Lat}_R$; in particular the hyperbolic stabilization $S=F_{H(R)}$ has no right adjoint.
:::

By @prp-form-initial-object the pair $(0,0)$ is initial in $\mathcal B_{R,W}$, and it is an $R$-lattice, so it is also initial in the full subcategory $\mathbf{Lat}_R$.
Now $F_M(0,0)=M$, and $\operatorname{Hom}\bigl(M,(0,0)\bigr)$ is empty by @prp-form-initial-object, since $b_M\neq0$.
An initial object admits a morphism to every object, so $M$ is not initial.
A left adjoint preserves colimits, and an initial object is the colimit of the empty diagram; an equivalence preserves initial objects as well.
For $S$ the hypothesis holds because $h_R\neq0$.

::: {#thm-invertible-summand}
## Invertible summands and the Witt class

Let $R$ be a Dedekind domain.
The zero lattice lies in $\mathbf{Lat}_R$ and an orthogonal sum of $R$-lattices is an $R$-lattice, so the symmetric monoidal structure of @def-orthogonal-sum restricts to $(\mathbf{Lat}_R,\perp,0)$.

1. The only invertible object of $(\mathbf{Lat}_R,\perp,0)$ is the unit, and $[0]=0$ in $W(R)$.

2. If $M$ is a unimodular $R$-lattice with $b_M=0$, then $M=0$.

Consequently a unimodular $M$ with $[M]\neq0$ has $b_M\neq0$, so $F_M$ is not an equivalence of $\mathbf{Lat}_R$ by @prp-summand-functor-no-right-adjoint, while a unimodular $M$ for which $F_M$ is an equivalence has $[M]=0$ and induces the identity on $W(R)$ by @thm-witt-shift-by-summand.
:::

For (1), an inverse of $M$ is a lattice $N$ with $M\perp N\cong0$; the underlying module of $M\perp N$ is $M\oplus N$, so $M=0$.
For (2), if $b_M=0$ then $b_M^{\sharp}=0$, and a zero map that is an isomorphism has zero source, so $M=0$.

::: {#thm-form-no-terminal}
## Terminal objects

Suppose $4\cdot1_R\neq0$ in $R$.
Then $\mathcal B_{R,R}$ has no terminal object.
If $R$ is in addition a Dedekind domain, then $\mathbf{Lat}_R$ has no terminal object.
:::

Write $\langle1\rangle$ for the object $(R,b)$ with $b(x,y)=xy$; it lies in $\mathcal B_{R,R}$, and in $\mathbf{Lat}_R$ when $R$ is a Dedekind domain, since $b^{\sharp}$ is the canonical isomorphism $R\cong R^{*}$.
An $R$-linear map $u\colon R\to P$ is determined by $p=u(1)$, and $u$ is a morphism $\langle1\rangle\to(P,c)$ exactly when $c(p,p)=1$.
Hence
$$
\operatorname{Hom}\bigl(\langle1\rangle,(P,c)\bigr)\;\cong\;\{p\in P\mid c(p,p)=1\},
$$
and this set is stable under $p\mapsto-p$.
If $(P,c)$ were terminal the set would be a singleton, forcing $p=-p$ and hence $2p=0$, so
$$
0=c(2p,2p)=4\,c(p,p)=4\cdot1_R,
$$
against the hypothesis.

::: {#thm-form-not-additive}
## Additivity of the form categories

Suppose $4\cdot1_R\neq0$.
Then $\mathcal B_{R,R}$ has no zero object, so it is not additive, and by @def-abelian-category it is not abelian.
For $R$ a Dedekind domain with $4\cdot1_R\neq0$ the same conclusions hold for $\mathbf{Lat}_R$.
:::

An additive category is an $\mathbf{Ab}$-category with a zero object and finite products [@Wei94, §A.4], and a zero object is terminal, which @thm-form-no-terminal excludes.
An abelian category is additive by @def-abelian-category.

## Hypotheses of the homological constructions {#sec-additive-hypotheses}

The constructions of @sec-stable-duality each state a hypothesis on their base category.
A chain complex is a family $C_n$ with $d_{n-1}d_n=0$, an equation naming the zero morphism; the category $\mathbf{Ch}(\mathcal A)$ and its homology functors are built for $\mathcal A$ additive (@def-chain-complexes).
Normalization is an intersection of kernels and the Dold–Kan correspondence is stated for $\mathcal A$ abelian (@thm-dold-kan).
The bar resolution is the augmented simplicial object of the comonad of an adjunction, taken in an abelian category with enough projectives (@def-comonad-resolution).
The projective model structure is stated for bounded-below complexes in an abelian category with enough projectives (@thm-projective-model-structure).
A stable $\infty$-category has a zero object (@def-stable-infinity-category), and a prespectrum object is a diagram whose off-diagonal values are zero objects (@def-prespectrum).

::: {#thm-no-heart}
## Hearts of $t$-structures

Let $\mathcal C$ be a stable $\infty$-category with a $t$-structure and let $\mathcal C^{\heartsuit}$ be its heart.
Then $\mathcal C^{\heartsuit}$ is equivalent to the nerve of its homotopy category, and that homotopy category is abelian [@Lur09, Def. 6.11 and Rmk. 6.12].
Consequently, for $R$ with $4\cdot1_R\neq0$, no $t$-structure on a stable $\infty$-category has heart equivalent to the nerve of $\mathcal B_{R,R}$, or of $\mathbf{Lat}_R$ when $R$ is a Dedekind domain, by @thm-form-not-additive.
:::

In @sec-stable-duality a form is a morphism of an additive category, and the constructions above apply to that category.
