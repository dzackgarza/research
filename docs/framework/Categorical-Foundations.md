# Categorical constructions {#sec-constructions}

Fix the variance and universal properties of the categorical constructions used by the algebraic and lattice chapters.
Core and groupoid completion are defined in @def-core.

::: {#def-category-of-elements}
## Category of elements

Let $F\colon C^{\mathrm{op}}\to\mathbf{Set}$ be a presheaf.
Its *category of elements* $\int_C F$ has objects $(c,x)$ with $x\in F(c)$.
A morphism $(c,x)\to(d,y)$ is a morphism $f\colon c\to d$ satisfying $F(f)(y)=x$.
The projection
$$
p_F\colon\int_C F\longrightarrow C,\qquad(c,x)\longmapsto c,
$$
is a discrete fibration [@nlab:category_of_elements; @Rie16, §2.4]. For a covariant functor $C\to\mathbf{Set}$ the corresponding projection is a discrete opfibration.
:::

## Grothendieck construction

For a pseudofunctor $F\colon C^{\mathrm{op}}\to\mathbf{Cat}$, the Grothendieck construction $\int_C F\to C$ is a fibration.
The category of elements is its $\mathbf{Set}$-valued special case [@nlab:grothendieck_construction]. A general forgetful functor need not arise from a category of elements; later chapters specify each forgetful functor directly.

::: {#def-subcategory}
## Subobjects, full and replete subcategories

A *subobject* of $Y\in\mathcal C$ is a monomorphism $m:X\to Y$ in $\mathcal C$; the datum is the arrow $m$, not merely the domain $X$ [@Lur26, Tag 04VD]. Equivalently, $m$ is a subterminal object of the slice $\mathcal C_{/Y}$, and if the relevant pullback exists, $m$ is monic exactly when the diagonal $\Delta_m:X\to X\times_Y X$ is an equivalence.

For ordinary $\mathbf{Cat}$, a functor $F:\mathcal A\to\mathcal B$ is monic if and only if it is injective on objects and faithful; hence subobjects in $\mathbf{Cat}$ are ordinary subcategories, up to isomorphism over $\mathcal B$.
In $\operatorname{Cat}_{\infty,\infty}$, a monomorphism must also contain every equivalence between objects in its image, so not every ordinary subcategory remains a subobject after passing to $\operatorname{Cat}_{\infty,\infty}$.

A *full subcategory* $\mathcal D\subseteq\mathcal C$ is the special case where $m$ is fully faithful: a collection of objects of $\mathcal C$ with mapping spaces inherited from $\mathcal C$,
$$
\operatorname{Map}_{\mathcal D}(x,y)\simeq\operatorname{Map}_{\mathcal C}(x,y).
$$
It is *replete* if every object of $\mathcal C$ equivalent to an object of $\mathcal D$ also belongs to $\mathcal D$.
An isomorphism-invariant property of objects of $\mathcal C$ defines a replete full subcategory [@stacks-001D; @nlab:replete_subcategory].
:::

::: {#def-concrete-category}
## Concrete categories

A *concrete category* is a category $C$ equipped with a faithful functor $U\colon C\to\mathbf{Set}$.
The set $U(X)$ is the underlying set of $X$.
Any further underlying-set construction is stated as a factorization through this functor.
:::

::: {#def-abelian-category}
## Abelian categories

An *abelian category* is an additive category in which every morphism has a kernel and a cokernel and, for every morphism $f$, the canonical map
$$
\operatorname{Coim}(f)\longrightarrow\operatorname{Im}(f)
$$
is an isomorphism [@stacks-0109]. In an abelian category, a morphism is monic exactly when its kernel is zero and epic exactly when its cokernel is zero.
:::

## Arrow and functor categories

For an ordinary category $C$, the arrow category is $[[1],C]$.
Evaluation at the source and target gives a functor to $C\times C$.
Local hom-objects and walking-arrow categories in $\mathbf{Cat}_{\infty,\infty}$ are defined in @def-internal-hom and @def-mapping-spaces.

## Pseudo-pullbacks {#sec-pullback-cat}

Given functors $F\colon A\to C$ and $G\colon B\to C$, their pseudo-pullback has objects $(a,b,\alpha)$ with $\alpha\colon F(a)\xrightarrow{\sim}G(b)$ and the evident compatible morphisms.
It is the 2-categorical pullback up to equivalence [@nlab:2-pullback].

If one leg is an isofibration, its strict pullback presents the pseudo-pullback up to equivalence.
A replete full inclusion is an isofibration [@nlab:isofibration]. Thus strict pullbacks suffice for replete full subcategories, while forgetful functors from chosen structures generally require pseudo-pullbacks.

## Connected components and fibers {#sec-pi0-fiber}

The functor $\pi_0\colon\mathcal S\to\mathbf{Set}$ sends a space to its set of components.
It does not preserve arbitrary homotopy pullbacks.
For a fiber sequence $F\to E\to B$, the associated exact sequence of pointed sets contains
$$
\pi_1(B,b)\longrightarrow\pi_0(F)\longrightarrow\pi_0(E)
\longrightarrow\pi_0(B).
$$
Consequently, the fiber of $\pi_0(E)\to\pi_0(B)$ need not equal $\pi_0(F)$ [@May99]. A set-valued invariant formed from this sequence must specify whether it uses the fiber after $\pi_0$ or the components of the homotopy fiber.

## Generalized elements and representability

A *generalized element* of $X\in C$ with domain $T$ is a morphism $T\to X$.
For a presheaf $F\colon C^{\mathrm{op}}\to\mathbf{Set}$, an element $x\in F(T)$ is an object $(T,x)$ of $\int_C F$.

The presheaf $F$ is representable if there is an object $X$ and a natural isomorphism $F\cong\operatorname{Hom}_C(-,X)$.
Under this isomorphism, $\operatorname{id}_X$ corresponds to the universal element.
The dual convention applies to corepresentable covariant functors.

::: {#def-el-convention}
## The $\int_C F$ convention {#sec-el}

For every presheaf $F\colon C^{\mathrm{op}}\to\mathbf{Set}$, use the category of elements and discrete-fibration convention of @def-category-of-elements.
Thus the projection $\int_C F\to C$ is a discrete fibration; no additional opposite category is taken after forming $\int_C F$.
:::

::: {#def-smooth-manifold}
## Smooth manifolds as locally ringed spaces

Let $\mathsf{LRS}_{\mathbb{R}}$ denote the category of locally $\mathbb{R}$-ringed spaces: topological spaces equipped with a sheaf of $\mathbb{R}$-algebras whose stalks are local rings [@nlab:locally_ringed_space]. The standard local model of dimension $n$ is
$$
M_n := (\mathbb{R}^n,\, C^\infty_{\mathbb{R}^n}),
$$
the Euclidean space with its sheaf of smooth real-valued functions.

A *smooth atlas* for an object $X \in \mathsf{LRS}_{\mathbb{R}}$ is a morphism $p\colon U \to X$ such that:

1. $U$ is isomorphic to a coproduct of local models: $U \cong \coprod_{i \in I} M_{n_i}$.

2. For every component inclusion $\iota_i\colon M_{n_i} \hookrightarrow U$, the composite $p \circ \iota_i\colon M_{n_i} \to X$ is an open immersion.

3. $p$ is an effective epimorphism: it is the coequalizer of its kernel pair
$$
U \times_X U \;\rightrightarrows\; U \;\xrightarrow{p}\; X.
$$

A *smooth manifold* is an object $X \in \mathsf{LRS}_{\mathbb{R}}$ that admits a smooth atlas [@nlab:effective_epimorphism; @nlab:smooth_manifold].

The data encode the classical construction as follows.
The object $U$ is the disjoint union of charts.
The fibered product $U \times_X U$ represents the pairwise intersections of charts in $X$.
The two projections $\pi_1, \pi_2\colon U \times_X U \to U$ encode the transition functions.
The coequalizer condition forces $X$ to be the colimit obtained from charts glued along their transitions: the classical manifold, recovered without point-set intersections.
:::

::: {#def-scheme-as-lrs}
## Schemes as locally ringed spaces

The smooth manifold definition of @def-smooth-manifold transfers to algebraic geometry by substituting the ambient category and local models.

Let $\mathsf{LRS}$ denote the category of all locally ringed spaces.
The local models are affine schemes: for a commutative ring $A$, write
$$
M_A := (\operatorname{Spec}(A),\, \mathcal{O}_{\operatorname{Spec}(A)}).
$$
A *Zariski atlas* for an object $X \in \mathsf{LRS}$ is a morphism $p\colon U \to X$ such that:

1. $U$ is isomorphic to a coproduct of affine schemes: $U \cong \coprod_{i \in I} M_{A_i}$.
2. For every component inclusion $\iota_i\colon M_{A_i} \hookrightarrow U$, the composite $p \circ \iota_i\colon M_{A_i} \to X$ is an open immersion.
3. $p$ is an effective epimorphism: it is the coequalizer of its kernel pair
$$
U \times_X U \;\rightrightarrows\; U \;\xrightarrow{p}\; X.
$$

A *scheme* is an object $X \in \mathsf{LRS}$ that admits a Zariski atlas.

The coequalizer is essential in algebraic geometry because the intersection of two affine open subschemes need not be affine.
The fibered product $U \times_X U$ encodes the scheme-theoretic intersections of the affine covers without requiring the intersections themselves to be local models.
:::

::: {#def-grothendieck-topology-generalization}
## Generalization by Grothendieck topology

The formulation of @def-smooth-manifold and @def-scheme-as-lrs admits a uniform generalization.
Fix a category $\mathcal{C}$ of locally ringed spaces, a class $\mathscr{L}$ of local models, and a class $\mathscr{A}$ of admissible morphisms.
A *$\mathscr{A}$-atlas* for $X \in \mathcal{C}$ is an effective epimorphism $p\colon \coprod_{i \in I} L_i \to X$ with each $L_i \in \mathscr{L}$ and each component an $\mathscr{A}$-morphism.
Different choices of $\mathscr{A}$ yield different Grothendieck topologies and geometric objects:

| Admissible morphisms $\mathscr{A}$ | Topology | Geometric objects |
|---|---|---|
| Open immersions | Zariski | Schemes |
| Étale morphisms | Étale | Algebraic spaces, Deligne–Mumford stacks |
| Faithfully flat morphisms of finite presentation | fppf | Artin stacks |
| Faithfully flat quasi-compact morphisms | fpqc | fpqc sheaves |

The smooth manifold case uses $\mathscr{L} = \{M_n\}_{n \geq 0}$ and $\mathscr{A} =$ open immersions in $\mathsf{LRS}_{\mathbb{R}}$.
:::
