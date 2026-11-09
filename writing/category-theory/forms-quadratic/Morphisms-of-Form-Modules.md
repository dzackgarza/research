# Morphisms of form modules {#sec-form-morphisms}

Fix a commutative ring $R$ and an $R$-module $W$, and use the form category $\mathcal B_{R,W}$ of @def:form-categories.
A morphism $f\colon(M,b_M)\to(N,b_N)$ of $\mathcal B_{R,W}$ is an $R$-linear map with $f^{*}b_N=b_M$, that is,
$$
b_N\bigl(f(x),f(y)\bigr)=b_M(x,y)
\qquad(x,y\in M).
$$
For $R$ a Dedekind domain, the lattice category $\mathbf{Lat}_R$ of @def:lattice is a replete full subcategory of $\mathcal B_{R,R}$, so its morphisms are these maps.

## Injectivity {#sec-form-morphisms-injective}

::: {.proposition #prop:form-morphism-injective title="Kernels of form-preserving maps"}

Let $f\colon(M,b_M)\to(N,b_N)$ be a morphism of $\mathcal B_{R,W}$.
Then $\ker f\iscontainedin\ker b_M^{\sharp}$, with $b_M^{\sharp}$ the adjoint map of @def:polarization.
If $b_M$ is nondegenerate then $f$ is injective.
In particular every morphism of $\mathbf{Lat}_R^{\mathrm{nd}}$ is injective, hence a monomorphism.
:::

::: {.proof}

For $x\in\ker f$ and every $y\in M$,
$$
b_M(x,y)=b_N\bigl(f(x),f(y)\bigr)=b_N\bigl(0,f(y)\bigr)=0,
$$
so $b_M^{\sharp}(x)=0$ and $\ker f\iscontainedin\ker b_M^{\sharp}$.
By @def:polarization, nondegeneracy of $b_M$ is the vanishing of $\ker b_M^{\sharp}$, so a nondegenerate source has $\ker f=0$.

The restriction to nondegenerate sources is necessary, and a lattice of @def:lattice need not be one: on $(\bZ,0)$, the lattice with zero form, the zero map to itself satisfies $0^{*}0=0$ and is a morphism, and it is not injective.
The lattice category of @def:lattice is $\mathbf{Lat}_R$, with $\mathbf{Lat}_R^{\mathrm{nd}}$ the full subcategory cut out by nondegeneracy, which is where the assertion applies.
A morphism of $\mathbf{Lat}_R^{\mathrm{nd}}$ is monic in it because its underlying map is injective and the forgetful functor to $R\text{-}\mathbf{Mod}$ is faithful.
:::

## Pointwise sums {#sec-sums-of-form-morphisms}

::: {.proposition #prop:sum-of-form-morphisms title="The pullback of a form along a sum"}

Let $f,g\colon(M,b_M)\to(N,b_N)$ be morphisms of $\mathcal B_{R,W}$ and let $f+g$ be their sum in $\Hom_R(M,N)$.
Then
$$
(f+g)^{*}b_N(x,y)
=2\,b_M(x,y)+b_N\bigl(f(x),g(y)\bigr)+b_N\bigl(g(x),f(y)\bigr).
$$
:::

::: {.proof}

Expanding by bilinearity,
$$
(f+g)^{*}b_N(x,y)=b_N\bigl(f(x)+g(x),f(y)+g(y)\bigr)
=b_N(fx,fy)+b_N(fx,gy)+b_N(gx,fy)+b_N(gx,gy),
$$
and $b_N(fx,fy)=b_M(x,y)=b_N(gx,gy)$ because $f$ and $g$ are morphisms.
:::

::: {.example #ex:identity-plus-identity title="A sum of two isometries"}

Let $R=W=\bZ$ and let $(M,b_M)=(N,b_N)=(\bZ,b)$ with $b(x,y)=xy$.
Take $f=g=\id$.
Then $f+g$ is multiplication by $2$ and
$$
(f+g)^{*}b(1,1)=4,\qquad b(1,1)=1,
$$
so $f+g$ is not a morphism of $\mathcal B_{\bZ,\bZ}$.
:::

## Initial and terminal objects {#sec-form-initial-terminal}

::: {.proposition #prop:form-initial-object title="The zero form module is initial"}

The pair $(0,0)$, with $0$ the zero $R$-module and its unique bilinear form, is an initial object of $\mathcal B_{R,W}$.
For an object $(M,b_M)$, the set $\Hom_{\mathcal B_{R,W}}\bigl((M,b_M),(0,0)\bigr)$ has one element if $b_M=0$ and is empty otherwise.
:::

::: {.proof}

Let $j\colon 0\to M$ and $k\colon M\to0$ be the unique $R$-linear maps; there is exactly one of each, since the zero module is initial and terminal in $R\text{-}\mathbf{Mod}$.
The zero module carries exactly one bilinear form, so $j^{*}b_M$ is that form and $j$ is a morphism $(0,0)\to(M,b_M)$; being the only linear map $0\to M$, it is the only such morphism.
For the other direction, $k^{*}0=0$ by definition, and $0=b_M$ exactly when $b_M=0$.
So there is exactly one morphism out of $(0,0)$ into any object, and the pair is initial.
:::

::: {.proposition #prop:summand-functor-no-right-adjoint title="Adjoints of orthogonal sum with a fixed object"}

Let $M=(M,b_M)$ be an object of $\mathcal B_{R,W}$ with $b_M\neq0$ and let $F_M=-\perp M$ be the functor of @def:hyperbolic-stabilization.
Then $F_M$ does not preserve the initial object, so $F_M$ is neither a left adjoint nor an equivalence.
For $R$ a Dedekind domain and $M$ an $R$-lattice the same holds for $F_M$ on $\mathbf{Lat}_R$; in particular the hyperbolic stabilization $S=F_{H(R)}$ has no right adjoint.
:::

::: {.proof}

By @prop:form-initial-object the pair $(0,0)$ is initial in $\mathcal B_{R,W}$, and it is an $R$-lattice, so it is initial in the full subcategory $\mathbf{Lat}_R$ as well: the unique morphism out of it is the same map.
Now $0\perp M\cong M$, and $\Hom\bigl(M,(0,0)\bigr)$ is empty by @prop:form-initial-object, since $b_M\neq0$; an initial object admits a morphism to every object, so $M$ is not initial, and $F_M$ carries an initial object to a non-initial one.

A left adjoint preserves colimits, and the initial object is the colimit of the empty diagram, so a left adjoint preserves initial objects; an equivalence does too, being part of an adjoint equivalence.
Hence $F_M$ is neither.
A functor admits a right adjoint exactly when it is a left adjoint, so $F_M$ has no right adjoint either.
For $S=F_{H(R)}$ the hypothesis is $h_R\neq0$, which holds by @ex:hyperbolic-plane, so $S$ has no right adjoint.
:::

::: {.theorem #thm:invertible-summand title="Invertible summands and the Witt class"}

Let $R$ be a Dedekind domain.
The zero lattice lies in $\mathbf{Lat}_R$ and an orthogonal sum of $R$-lattices is an $R$-lattice, so the symmetric monoidal structure of @def:orthogonal-sum restricts to $(\mathbf{Lat}_R,\perp,0)$.

1. The only invertible object of $(\mathbf{Lat}_R,\perp,0)$ is the unit, and $[0]=0$ in $W(R)$.

2. If $M$ is a unimodular $R$-lattice with $b_M=0$, then $M=0$.

Consequently a unimodular $M$ with $[M]\neq0$ has $b_M\neq0$, so $F_M$ is not an equivalence of $\mathbf{Lat}_R$ by @prop:summand-functor-no-right-adjoint, while a unimodular $M$ for which $F_M$ is an equivalence has $[M]=0$ and induces the identity on $W(R)$ by @thm:witt-shift-by-summand.
:::

::: {.proof}

The zero module is finitely generated projective, so $(0,0)$ is an $R$-lattice and the unit of the monoidal structure lies in $\mathbf{Lat}_R$; the underlying module of $M\perp N$ is $M\oplus N$ by @def:orthogonal-sum, and a biproduct of finitely generated projective modules is finitely generated projective, so the orthogonal sum of lattices is a lattice.

For (1), an inverse of $M$ is a lattice $N$ with $M\perp N\cong0$.
An isomorphism of lattices is in particular an isomorphism of underlying modules, and $M\oplus N=0$ forces $M=0$.
The class of the zero lattice is zero in $W(R)$ by @prop:metabolic-witt-trivial, its lagrangian being $0$.

For (2), if $b_M=0$ then $b_M^{\sharp}=0$, and the zero map is injective only from the zero module, so $M=0$.
:::

::: {.theorem #thm:form-no-terminal title="Terminal objects"}

Suppose $4\cdot1_R\neq0$ in $R$.
Then $\mathcal B_{R,R}$ has no terminal object.
If $R$ is in addition a Dedekind domain, then $\mathbf{Lat}_R$ has no terminal object.
:::

::: {.proof}

Write $\langle1\rangle$ for the object $(R,b)$ with $b(x,y)=xy$; it lies in $\mathcal B_{R,R}$, and in $\mathbf{Lat}_R$ when $R$ is a Dedekind domain, $R$ being a finitely generated projective module over itself.

An $R$-linear map $u\colon R\to P$ is determined by $p=u(1)$.
If $u$ is a morphism $\langle1\rangle\to(P,c)$ then $c(u x,u y)=xy$ for all $x,y$, and $x=y=1$ gives $c(p,p)=1$; conversely $c(px,py)=xy\,c(p,p)=xy$ when $c(p,p)=1$.
Hence
$$
\Hom\bigl(\langle1\rangle,(P,c)\bigr)\;\cong\;\{p\in P\mid c(p,p)=1\},
$$
and this set is stable under $p\mapsto-p$, since $c(-p,-p)=c(p,p)$.

If $(P,c)$ were terminal, this hom-set would be a singleton, and in particular nonempty; taking $p$ in it, $-p$ is in it too, so $p=-p$ and $2p=0$.
Then
$$
0=c(2p,2p)=4\,c(p,p)=4\cdot1_R
$$
by bilinearity, against the hypothesis.
For $R$ a Dedekind domain the same argument runs in the full subcategory $\mathbf{Lat}_R$, since $\langle1\rangle$ lies there and a terminal object of $\mathbf{Lat}_R$ would give a singleton hom-set from it.
:::

::: {.theorem #thm:form-not-additive title="Additivity of the form categories"}

Suppose $4\cdot1_R\neq0$.
Then $\mathcal B_{R,R}$ has no zero object, so it is not additive, and by @def:abelian-category it is not abelian.
For $R$ a Dedekind domain with $4\cdot1_R\neq0$ the same conclusions hold for $\mathbf{Lat}_R$.
:::

::: {.proof}

An additive category is an $\mathbf{Ab}$-category with a zero object and finite products [@Wei94, §A.4].
A zero object is an object that is both initial and terminal, so a category with no terminal object has no zero object and is not additive.
By @thm:form-no-terminal this applies to $\mathcal B_{R,R}$, and to $\mathbf{Lat}_R$ when $R$ is a Dedekind domain, under the hypothesis $4\cdot1_R\neq0$.
An abelian category is additive by @def:abelian-category, so neither category is abelian.
:::

## Hypotheses of the homological constructions {#sec-additive-hypotheses}

The constructions of @sec-stable-duality each state a hypothesis on their base category.
A chain complex is a family $C_n$ with $d_{n-1}d_n=0$, an equation naming the zero morphism; the category $\mathbf{Ch}(\mca)$ and its homology functors are built for $\mca$ additive (@def:chain-complexes).
Normalization is an intersection of kernels and the Dold–Kan correspondence is stated for $\mca$ abelian (@thm:dold-kan).
The bar resolution is the augmented simplicial object of the comonad of an adjunction, in a module category, and it computes the derived functors of an additive functor out of that category (@def:comonad-resolution).
The projective model structure is stated for bounded-below complexes in an abelian category with enough projectives (@thm:projective-model-structure).
A stable $\infty$-category has a zero object (@def:stable-infinity-category), and a prespectrum object is a diagram whose off-diagonal values are zero objects (@def:prespectrum).

::: {.theorem #thm:no-heart title="Hearts of $t$-structures"}

Let $\mcc$ be a stable $\infty$-category with a $t$-structure and let $\mcc^{\heartsuit}$ be its heart.
Then $\mcc^{\heartsuit}$ is equivalent to the nerve of its homotopy category, and that homotopy category is abelian [@Lur09, Def. 6.11 and Rmk. 6.12].
Consequently, for $R$ with $4\cdot1_R\neq0$, no $t$-structure on a stable $\infty$-category has heart equivalent to the nerve of $\mathcal B_{R,R}$, or of $\mathbf{Lat}_R$ when $R$ is a Dedekind domain, by @thm:form-not-additive.
:::

::: {.proof}

The first two clauses are the cited result [@Lur09, Def. 6.11 and Rmk. 6.12]: the heart of a $t$-structure is equivalent to the nerve of its homotopy category, and that homotopy category is abelian.
Suppose $\mcc^{\heartsuit}\simeq\mathrm N(\mcb)$ with $\mcb$ one of $\mathcal{B}_{R,R}$ or $\mathbf{Lat}_R$; by the first clause $\mcc^{\heartsuit}\simeq\mathrm N(\operatorname{Ho}\mcc^{\heartsuit})$ as well, so $\mathrm N(\mcb)$ is equivalent to the nerve of an abelian category.
The nerve is fully faithful [@nlab:nerve], so that equivalence is induced by one of ordinary categories, giving $\mcb\simeq\operatorname{Ho}\mcc^{\heartsuit}$, and being abelian is invariant under equivalence.
Then $\mcb$ would be abelian, which @thm:form-not-additive forbids when $4\cdot1_R\neq0$.:::

In @sec-stable-duality a form is a morphism of an additive category, and the constructions above apply to that category.
