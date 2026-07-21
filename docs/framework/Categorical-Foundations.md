# Categorical constructions {#sec-constructions}

Fix the variance and universal properties of the categorical constructions used by the
algebraic and lattice chapters. Core and groupoid completion are defined in @def-core.

::: {#def-category-of-elements}
## Category of elements

Let $F\colon C^{\mathrm{op}}\to\mathbf{Set}$ be a presheaf. Its *category of
elements* $\operatorname{El}(F)$ has objects $(c,x)$ with $x\in F(c)$. A morphism
$(c,x)\to(d,y)$ is a morphism $f\colon c\to d$ satisfying $F(f)(y)=x$. The projection
$$
p_F\colon\operatorname{El}(F)\longrightarrow C,\qquad(c,x)\longmapsto c,
$$
is a discrete fibration [@nlab:category_of_elements; @Rie16, §2.4]. For a covariant
functor $C\to\mathbf{Set}$ the corresponding projection is a discrete opfibration.
:::

## Grothendieck construction

For a pseudofunctor $F\colon C^{\mathrm{op}}\to\mathbf{Cat}$, the Grothendieck
construction $\int_C F\to C$ is a fibration. The category of elements is its
$\mathbf{Set}$-valued special case [@nlab:grothendieck_construction]. A general
forgetful functor need not arise from a category of elements; later chapters specify
each forgetful functor directly.

::: {#def-subcategory}
## Full and replete subcategories

A subcategory $D\subseteq C$ is *full* if
$\operatorname{Hom}_D(X,Y)=\operatorname{Hom}_C(X,Y)$ for all objects $X,Y$ of $D$.
It is *replete* if every object of $C$ isomorphic to an object of $D$ is itself an
object of $D$. Thus an isomorphism-invariant property of objects of $C$ defines a
replete full subcategory [@stacks-001D; @nlab:replete_subcategory].
:::

::: {#def-concrete-category}
## Concrete categories

A *concrete category* is a category $C$ equipped with a faithful functor
$U\colon C\to\mathbf{Set}$. The set $U(X)$ is the underlying set of $X$. Any further
underlying-set construction is stated as a factorization through this functor.
:::

::: {#def-abelian-category}
## Abelian categories

An *abelian category* is an additive category in which every morphism has a kernel and
a cokernel and, for every morphism $f$, the canonical map
$$
\operatorname{Coim}(f)\longrightarrow\operatorname{Im}(f)
$$
is an isomorphism [@stacks-0109]. In an abelian category, a morphism is monic exactly
when its kernel is zero and epic exactly when its cokernel is zero.
:::

## Arrow and functor categories

For an ordinary category $C$, the arrow category is
$\operatorname{Fun}([1],C)$. Evaluation at the source and target gives a functor to
$C\times C$. Functor categories and arrow categories in $\mathbf{Cat}_\infty$ are the
quasicategories defined in @def-internal-hom.

## Pseudo-pullbacks {#sec-pullback-cat}

Given functors $F\colon A\to C$ and $G\colon B\to C$, their pseudo-pullback has
objects $(a,b,\alpha)$ with $\alpha\colon F(a)\xrightarrow{\sim}G(b)$ and the evident
compatible morphisms. It is the 2-categorical pullback up to equivalence
[@nlab:2-pullback].

If one leg is an isofibration, its strict pullback presents the pseudo-pullback up to
equivalence. A replete full inclusion is an isofibration [@nlab:isofibration]. Thus
strict pullbacks suffice for replete full subcategories, while forgetful functors from
chosen structures generally require pseudo-pullbacks.

## Connected components and fibers {#sec-pi0-fiber}

The functor $\pi_0\colon\mathcal S\to\mathbf{Set}$ sends a space to its set of
components. It does not preserve arbitrary homotopy pullbacks. For a fiber sequence
$F\to E\to B$, the associated exact sequence of pointed sets contains
$$
\pi_1(B,b)\longrightarrow\pi_0(F)\longrightarrow\pi_0(E)
\longrightarrow\pi_0(B).
$$
Consequently, the fiber of $\pi_0(E)\to\pi_0(B)$ need not equal $\pi_0(F)$
[@May99]. A set-valued invariant formed from this sequence must specify whether it uses
the fiber after $\pi_0$ or the components of the homotopy fiber.

## Generalized elements and representability

A *generalized element* of $X\in C$ with domain $T$ is a morphism $T\to X$. For a
presheaf $F\colon C^{\mathrm{op}}\to\mathbf{Set}$, an element $x\in F(T)$ is an
object $(T,x)$ of $\operatorname{El}(F)$.

The presheaf $F$ is representable if there is an object $X$ and a natural isomorphism
$F\cong\operatorname{Hom}_C(-,X)$. Under this isomorphism, $\operatorname{id}_X$
corresponds to the universal element. The dual convention applies to corepresentable
covariant functors.

::: {#def-el-convention}
## The $\operatorname{El}$ convention {#sec-el}

For every presheaf $F\colon C^{\mathrm{op}}\to\mathbf{Set}$, use the category of
elements and discrete-fibration convention of @def-category-of-elements.
Thus the projection $\operatorname{El}(F)\to C$ is a discrete fibration; no additional
opposite category is taken after forming $\operatorname{El}(F)$.
:::
