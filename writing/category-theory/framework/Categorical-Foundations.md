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

A *subobject* of $Y\in\mathcal C$ is a monomorphism $m:X\to Y$ in $\mathcal C$; the datum is the arrow $m$, not merely the domain $X$ [@Lur18c, Tag 04VD]. Equivalently, $m$ is a subterminal object of the slice $\mathcal C_{/Y}$, and if the relevant pullback exists, $m$ is monic exactly when the diagonal $\Delta_m:X\to X\times_Y X$ is an equivalence.

For ordinary $\mathbf{Cat}$, a functor $F:\mathcal A\to\mathcal B$ is monic if and only if it is injective on objects and faithful; hence subobjects in $\mathbf{Cat}$ are ordinary subcategories, up to isomorphism over $\mathcal B$.
In $\operatorname{Cat}_{\infty,\infty}$, a monomorphism must also contain every equivalence between objects in its image, so not every ordinary subcategory remains a subobject after passing to $\operatorname{Cat}_{\infty,\infty}$.

A *full subcategory* $\mathcal D\subseteq\mathcal C$ is the special case where $m$ is fully faithful: a collection of objects of $\mathcal C$ with mapping spaces inherited from $\mathcal C$,
$$
\operatorname{Map}_{\mathcal D}(x,y)\simeq\operatorname{Map}_{\mathcal C}(x,y).
$$
It is *replete* if every object of $\mathcal C$ equivalent to an object of $\mathcal D$ also belongs to $\mathcal D$.
An isomorphism-invariant property of objects of $\mathcal C$ defines a replete full subcategory [@The25, Tag 001D; @nlab:replete_subcategory].
:::

::: {#def-concrete-category}
## Concrete categories

A *concrete category* is a category $C$ equipped with a faithful functor $U\colon C\to\mathbf{Set}$.
The set $U(X)$ is the underlying set of $X$.
Any further underlying-set construction is stated as a factorization through this functor.
:::

For a concrete category, a morphism whose underlying function is injective is monic, and one whose underlying function is surjective is epic; each converse is a separate claim about $U$.
When $U$ is corepresented by an object $P$ as in @def-element-functor, $U(f)=\operatorname{Hom}_C(P,f)$ and $f$ is monic exactly when $U(f)$ is injective: one direction applies the definition of a monomorphism to $P$, the other uses faithfulness.
The corresponding claim for epimorphisms fails: the inclusion $\mathbb Z\hookrightarrow\mathbb Q$ is monic and epic in $\mathbf{Ring}$, and it is neither surjective nor invertible [@Rie16, Example 1.2.10].
Invertibility is asked of the morphism, by exhibiting a two-sided inverse in $C$.

## Comma categories and universal arrows {#sec-comma}

::: {#def-comma-category}
## Comma categories

Let $T\colon\mathcal E\to\mathcal C$ and $S\colon\mathcal D\to\mathcal C$ be functors.
The *comma category* $(T\downarrow S)$ has as objects the triples $\langle e,d,f\rangle$ with $e\in\mathcal E$, $d\in\mathcal D$, and $f\colon Te\to Sd$ in $\mathcal C$, and as morphisms $\langle e,d,f\rangle\to\langle e',d',f'\rangle$ the pairs $\langle k\colon e\to e',\,h\colon d\to d'\rangle$ with
$$
f'\circ Tk=Sh\circ f.
$$
The two projections send $\langle e,d,f\rangle$ to $e$ and to $d$ [@Mac98, §II.6].

Taking $T$ or $S$ to be a functor $\mathbf 1\to\mathcal C$, that is an object of $\mathcal C$, gives the coslice $(b\downarrow S)$ and the slice $(T\downarrow a)$; taking both to be $\operatorname{id}_{\mathcal C}$ gives the arrow category $(\mathcal C\downarrow\mathcal C)$, whose objects are the morphisms of $\mathcal C$; taking both to be objects $a,b$ gives the discrete category $\operatorname{Hom}_{\mathcal C}(b,a)$.
:::

For an ordinary category $C$, the arrow category is also $[[1],C]$, and evaluation at the source and target gives a functor to $C\times C$.
Local hom-objects and walking-arrow categories in $\mathbf{Cat}_{\infty,\infty}$ are defined in @def-internal-hom and @def-mapping-spaces.

::: {#def-universal-arrow}
## Universal arrows

Let $S\colon\mathcal D\to\mathcal C$ and $c\in\mathcal C$.
A morphism $u\colon c\to Sr$ is *universal from $c$ to $S$* when, for every $d\in\mathcal D$ and every $f\colon c\to Sd$, there is a unique $g\colon r\to d$ with $Sg\circ u=f$.
Equivalently, $\langle r,u\rangle$ is an initial object of the comma category $(c\downarrow S)$, so it is unique up to a unique isomorphism of $(c\downarrow S)$ and $r$ is unique up to isomorphism in $\mathcal D$ [@Mac98, §III.1].
Dually, a morphism $v\colon Sr\to c$ is couniversal when $\langle r,v\rangle$ is terminal in $(S\downarrow c)$.
:::

Free constructions are of this form: the insertion of a graph into the underlying graph of the free category on it is universal from the graph to the forgetful functor $U\colon\mathbf{Cat}\to\mathbf{Grph}$ (@def-free-category).
The corepresenting objects listed in @def-element-functor are the values of the corresponding free constructions on a one-element set, and the universal arrow is the choice of that element.

## Additive and abelian categories {#sec-abelian}

::: {#def-preadditive}
## Preadditive and additive categories

A *preadditive category*, or $\mathbf{Ab}$-category, is a category $\mathcal A$ in which each $\operatorname{Hom}_{\mathcal A}(b,c)$ is an abelian group and composition is bilinear.
Its zero elements are the *zero morphisms* $0\colon b\to c$, and a composite with a zero morphism is zero.

In a preadditive category an object $z$ is initial exactly when it is terminal, exactly when $1_z=0$, and exactly when $\operatorname{Hom}_{\mathcal A}(z,z)$ is the zero group; such a $z$ is a *zero object* [@Mac98, §VIII.2, Proposition 1].

A *biproduct diagram* for $a,b\in\mathcal A$ consists of an object $c$ and morphisms
$$
i_1\colon a\to c,\quad i_2\colon b\to c,\quad p_1\colon c\to a,\quad p_2\colon c\to b
$$
satisfying
$$
p_1i_1=1_a,\qquad p_2i_2=1_b,\qquad i_1p_1+i_2p_2=1_c.
$$
Two objects of $\mathcal A$ have a product exactly when they have a biproduct, exactly when they have a coproduct; the biproduct object with $p_1,p_2$ is their product and with $i_1,i_2$ their coproduct, and it is written $a\oplus b$ [@Mac98, §VIII.2, Theorem 2].

An *additive category* is a preadditive category with a zero object and a biproduct for each pair of objects [@Mac98, §VIII.2].
:::

::: {#def-kernel-cokernel}
## Kernels and cokernels

In a category with a zero object, the *kernel* of $f\colon a\to b$ is the equalizer of the pair $f,0\colon a\to b$: a morphism $k\colon s\to a$ with $fk=0$ through which every $h$ with $fh=0$ factors uniquely.
The *cokernel* is the coequalizer of the same pair [@Mac98, §VIII.1].
:::

::: {#def-abelian-category}
## Abelian categories

An *abelian category* is an additive category in which every morphism has a kernel and a cokernel and, for every morphism $f$, the canonical map
$$
\operatorname{Coim}(f)\longrightarrow\operatorname{Im}(f)
$$
is an isomorphism [@The25, Tag 0109]. In an abelian category, a morphism is monic exactly when its kernel is zero and epic exactly when its cokernel is zero.

An equivalent axiomatization asks for a zero object, binary biproducts, kernels and cokernels of every morphism, and that every monomorphism be a kernel and every epimorphism a cokernel [@Mac98, §VIII.3].
Kernels and cokernels then supply the remaining finite limits and colimits: the equalizer of $f,g$ is the kernel of $f-g$, and biproducts are the finite products, so an abelian category is finitely complete and finitely cocomplete [@Mac98, §VIII.3].
:::

::: {#thm-canonical-factorization}
## The canonical factorization

In an abelian category every morphism $f$ factors as $f=me$ with $m$ monic and $e$ epic, where
$$
m=\ker(\operatorname{coker}f),
\qquad
e=\operatorname{coker}(\ker f),
$$
and the factorization is functorial: a commutative square from $f$ to $f'$ induces a unique morphism between the two factorizations commuting with both halves.
The object $\operatorname{Im}(f)$ is the domain of $m$ and $\operatorname{Coim}(f)$ the codomain of $e$ [@Mac98, §VIII.3, Proposition 1].
:::

::: {#thm-diagram-lemmas}
## Diagram lemmas

Let $\mathcal A$ be abelian.
For a morphism $\langle f,g,h\rangle$ of short exact sequences: if $f$ and $h$ are monic then $g$ is monic, and if $f$ and $h$ are epic then $g$ is epic (short five lemma); there is a connecting morphism $\delta\colon\ker h\to\operatorname{coker}f$ making
$$
\ker f\to\ker g\to\ker h
\xrightarrow{\;\delta\;}
\operatorname{coker}f\to\operatorname{coker}g\to\operatorname{coker}h
$$
exact (snake lemma).
In a commutative diagram with exact rows and five vertical morphisms, if the four outer ones are isomorphisms then so is the middle one (five lemma) [@Mac98, §VIII.4, Lemmas 1, 4, and 5].
:::

Exactness is a property of a composable pair: $a\xrightarrow{f}b\xrightarrow{g}c$ with $gf=0$ is exact at $b$ when the monomorphism $\operatorname{Im}(f)\to b$ and the kernel of $g$ represent the same subobject of $b$ (@def-subobject-relation).

## Endomorphisms and automorphisms {#sec-endomorphisms}

::: {#def-endomorphism-monoid}
## The endomorphism monoid and the automorphism group

For an object $X$ of a category $\mathcal C$, composition makes $\operatorname{Hom}_{\mathcal C}(X,X)$ a monoid with unit $\operatorname{id}_X$.
Its group of invertible elements is $\operatorname{Aut}_{\mathcal C}(X)$, the automorphism group of $X$, which is $\operatorname{Iso}_{\mathcal C}(X,X)$ in the notation of [Equivalences and witnesses](Identification.md#sec-equivalence-spaces).
When $\mathcal C$ is preadditive, $\operatorname{Hom}_{\mathcal C}(X,X)$ is a ring under composition and the group addition, and $\operatorname{Aut}_{\mathcal C}(X)$ is its group of units.
:::

The arity-$1$ term of the endomorphism operad of @sec-operations is this monoid; the higher arities record the operations $X^{\times n}\to X$ and are not composition.

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

::: {#def-generalized-element}
## Generalized elements

A *generalized element* of $X\in C$ with domain $T$ is a morphism $T\to X$.
For a presheaf $F\colon C^{\mathrm{op}}\to\mathbf{Set}$, an element $x\in F(T)$ is an object $(T,x)$ of $\int_C F$.
:::

::: {#def-representable-presheaf}
## Representable presheaves

The presheaf $F$ is *representable* if there is an object $X$ and a natural isomorphism $F\cong\operatorname{Hom}_C(-,X)$.
Under this isomorphism, $\operatorname{id}_X$ corresponds to the universal element.
The dual convention applies to corepresentable covariant functors.
:::

::: {#thm-yoneda}
## The Yoneda lemma

Let $C$ be locally small, $F\colon C\to\mathbf{Set}$ a functor, and $c\in C$.
Evaluation of a natural transformation at $\operatorname{id}_c$ is a bijection
$$
\operatorname{Nat}\bigl(\operatorname{Hom}_C(c,-),\,F\bigr)
\;\cong\;
F(c),
\qquad
\alpha\longmapsto\alpha_c(\operatorname{id}_c),
$$
natural in $c$ and in $F$ [@Rie16, Theorem 2.2.4; @Mac98, §III.2].
Consequently the Yoneda embeddings
$$
C\hookrightarrow\mathbf{Set}^{C^{\mathrm{op}}},
\qquad
C^{\mathrm{op}}\hookrightarrow\mathbf{Set}^{C}
$$
are fully faithful: natural transformations between represented functors correspond to morphisms between the representing objects [@Rie16, Corollary 2.2.8].
:::

A representation is therefore determined by its universal element, and two representations of the same functor are related by a unique isomorphism compatible with the universal elements.

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
| --- | --- | --- |
| Open immersions | Zariski | Schemes |
| Étale morphisms | Étale | Algebraic spaces, Deligne–Mumford stacks |
| Faithfully flat morphisms of finite presentation | fppf | Artin stacks |
| Faithfully flat quasi-compact morphisms | fpqc | fpqc sheaves |

The smooth manifold case uses $\mathscr{L} = \{M_n\}_{n \geq 0}$ and $\mathscr{A} =$ open immersions in $\mathsf{LRS}_{\mathbb{R}}$.
:::
