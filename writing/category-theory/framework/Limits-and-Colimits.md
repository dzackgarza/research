# Limits and colimits {#sec-limits-colimits}

Limits, colimits, products, and coproducts are defined once for an arbitrary category, and each particular category supplies its instances.
Throughout, $\mathcal C$ is a category and $J$ is a small category, the *shape* of the diagrams considered.
The higher-categorical constructions of the same names are in [Higher categories and universes](Higher-Categories-and-Universes.md) and [Loops and suspension](Loops-and-Suspension.md).

## Diagrams and cones {#sec-diagrams-cones}

::: {#def-diagram}
## Diagrams and the diagonal functor

A *diagram of shape $J$* in $\mathcal C$ is a functor $D\colon J\to\mathcal C$.
For an object $c\in\mathcal C$, the *constant functor* $\Delta c\colon J\to\mathcal C$ sends every object of $J$ to $c$ and every morphism of $J$ to $\operatorname{id}_c$.
The assignment $c\mapsto\Delta c$, together with the constant natural transformation on a morphism $f\colon c\to c'$, is the *diagonal functor*
$$
\Delta\colon\mathcal C\longrightarrow\mathcal C^{J}
$$
[@Rie16, Definition 3.1.1].
:::

::: {#def-cone}
## Cones and cocones

A *cone over $D$ with apex $c$* is a natural transformation $\lambda\colon\Delta c\Rightarrow D$.
Its components $\lambda_j\colon c\to D(j)$ are its *legs*, and naturality says that
$$
D(u)\circ\lambda_j=\lambda_k
\qquad\text{for every }u\colon j\to k\text{ in }J.
$$
A *cocone under $D$ with nadir $c$* is a natural transformation $\mu\colon D\Rightarrow\Delta c$, so that $\mu_k\circ D(u)=\mu_j$ for every $u\colon j\to k$ [@Rie16, Definition 3.1.2; @Mac98, §III.4].

Precomposition with $h\colon c'\to c$ sends a cone with apex $c$ to one with apex $c'$, so the cones over $D$ assemble into a presheaf
$$
\operatorname{Cone}(-,D)\colon\mathcal C^{\mathrm{op}}\longrightarrow\mathbf{Set},
$$
and dually the cocones under $D$ into a covariant functor $\operatorname{Cone}(D,-)$.
The category of elements $\int_{\mathcal C}\operatorname{Cone}(-,D)$ of @def-category-of-elements is the *category of cones over $D$*: its objects are the cones, and a morphism from $\lambda$ with apex $c$ to $\lambda'$ with apex $c'$ is a morphism $h\colon c\to c'$ with $\lambda'_j\circ h=\lambda_j$ for every $j$.
:::

## Limits {#sec-limits}

::: {#def-limit}
## Limits and colimits

A *limit of $D$* is a representation of $\operatorname{Cone}(-,D)$ (@def-representable-presheaf): an object $\lim D$ together with a cone $\lambda\colon\Delta\lim D\Rightarrow D$ inducing a natural isomorphism
$$
\operatorname{Hom}_{\mathcal C}(-,\lim D)\;\cong\;\operatorname{Cone}(-,D).
$$
The cone $\lambda$ is the *limit cone*, and it is the universal element of the representation.
Equivalently, $\lambda$ is a terminal object of the category of cones over $D$.
Dually, a *colimit* of $D$ is a representation of $\operatorname{Cone}(D,-)$, equivalently an initial object of the category of cocones under $D$ [@Rie16, Definitions 3.1.5 and 3.1.6].

Limits of $D$ are unique up to a unique isomorphism compatible with the limit cones, since terminal objects are.
:::

**Remark.** The universal property is the natural isomorphism: it names the morphism that factors a given cone, and its naturality identifies the factorization of a cone with the factorization of any cone obtained from it by composing with a morphism of apexes.
The same standard governs classifying objects in @def-classifying-object.

## Named shapes {#sec-named-shapes}

Each standard construction is the limit or colimit of a diagram of a specific shape [@Rie16, Definitions 3.1.9–3.1.23; @Mac98, §III.3–4].

| Shape $J$ | Limit | Colimit |
| --- | --- | --- |
| empty | terminal object | initial object |
| discrete on a set $I$ | product $\prod_{i\in I}D_i$ | coproduct $\coprod_{i\in I}D_i$ |
| parallel pair $\bullet\rightrightarrows\bullet$ | equalizer | coequalizer |
| $\bullet\to\bullet\leftarrow\bullet$ | pullback | — |
| $\bullet\leftarrow\bullet\to\bullet$ | — | pushout |
| $\omega^{\mathrm{op}}$ | inverse limit of a tower | — |
| $\omega$ | — | colimit of a sequence |

A cone over the empty diagram is an object with no further data, so the category of such cones is $\mathcal C$ itself and the limit is a terminal object of $\mathcal C$ [@Mac98, §III.4].
A cone over a parallel pair $f,g\colon A\to B$ is determined by a single morphism $a\colon C\to A$ with $fa=ga$, its leg at $B$ being the common composite [@Rie16, Definition 3.1.13].

::: {#def-pullback-square}
## Pullbacks

For morphisms $f\colon X\to Z$ and $g\colon Y\to Z$, the limit of the diagram they form has apex written $X\times_ZY$ and legs $p,q$, displayed by the cartesian square

```{.tikz}
%%| filename: general-pullback-square
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}
X\times_Z Y
  \arrow[r,"q"]
  \arrow[d,"p"']
  \arrow[dr,phantom,very near start,"\lrcorner"] &
Y \arrow[d,"g"]\\
X \arrow[r,"f"'] & Z
\end{tikzcd}
```

The leg at $Z$ is the common composite $fp=gq$, so a cone with apex $W$ is a pair $(h\colon W\to X,\;k\colon W\to Y)$ with $fh=gk$, and the universal property is the bijection
$$
\operatorname{Hom}_{\mathcal C}(W,X\times_ZY)
\;\cong\;
\{(h,k)\;:\;fh=gk\},
$$
natural in $W$ [@Rie16, Definition 3.1.15].
The dual construction, the colimit of $X\leftarrow Z\to Y$, is the pushout $X\amalg_ZY$, displayed by the cocartesian square

```{.tikz}
%%| filename: general-pushout-square
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}
Z \arrow[r,"g"] \arrow[d,"f"'] &
Y \arrow[d,"i_Y"]\\
X \arrow[r,"i_X"']
  \arrow[ur,phantom,very near end,"\ulcorner"] &
X\amalg_Z Y
\end{tikzcd}
```
:::

The equality $fh=gk$ is part of the datum of the cone with apex $W$.

## Shape categories {#sec-shape-categories}

::: {#def-preorder-category}
## Preorders and thin categories

A *preorder* is a category $P$ with at most one morphism $p\to p'$ for each pair of objects.
Writing $p\leq p'$ when such a morphism exists gives a reflexive transitive relation on the objects, and every reflexive transitive relation arises this way from a unique preorder.
A preorder is a *poset* when the relation is antisymmetric, so that $p\leq p'$ and $p'\leq p$ imply $p=p'$ [@Mac98, §I.2].
:::

The shapes for products, pullbacks, pushouts, and towers are posets.
The parallel pair is not a preorder, since it has two distinct morphisms between the same pair of objects; it is obtained instead by the following construction.

::: {#def-free-category}
## Free categories on graphs

A *directed graph* $G$ consists of a set $O$ of vertices, a set $A$ of edges, and functions $\partial_0,\partial_1\colon A\to O$ assigning to each edge its source and target; a morphism of graphs is a pair of functions commuting with $\partial_0$ and $\partial_1$.
Every category $\mathcal C$ has an underlying graph $U\mathcal C$ with the same objects and morphisms, and this defines $U\colon\mathbf{Cat}\to\mathbf{Grph}$.

The *free category* $F(G)$ on a graph $G$ has the vertices of $G$ as objects and the finite paths of $G$ as morphisms, with composition given by concatenation and the empty path at a vertex as its identity.
The insertion $\eta\colon G\to UF(G)$ is universal: every morphism of graphs $G\to U\mathcal C$ extends along $\eta$ to a unique functor $F(G)\to\mathcal C$, so that
$$
\adj{\mathbf{Grph}}{\mathbf{Cat}}{F}{U},
\qquad F\dashv U
$$
[@Mac98, §II.7].
:::

::: {#def-presented-category}
## Presented categories

Let $G$ be a graph and let $R$ be a set of pairs of parallel paths of $G$.
The category presented by $(G,R)$ is the quotient of $F(G)$ by the congruence generated by $R$: its morphisms are the classes of paths under the smallest equivalence relation containing $R$ and compatible with composition [@Mac98, §II.8].
A functor out of the presented category is a graph morphism $G\to U\mathcal C$ whose extension identifies the two sides of each pair in $R$.
:::

In $\mathbf{Cat}$ the walking arrow $[1]$ is the free category on the graph with two vertices and one edge, and the ordinal category $[n]$ of @def-walking-arrow is the free category on the linear graph with $n$ edges; the walking isomorphism is presented by two edges $f,g$ in opposite directions with the relations $gf=\operatorname{id}$ and $fg=\operatorname{id}$.
Each of these represents a functor on $\mathbf{Cat}$: $[0]$ represents the object functor, $[1]$ the morphism functor, and $[n]$ the functor sending a small category to its set of paths of $n$ composable morphisms [@Rie16, Example 2.1.5].
A commutative square is presented by the four-edge square graph with the relation identifying its two paths; the free category on that graph, without the relation, has two distinct morphisms between the opposite corners.

## Existence {#sec-completeness}

::: {#def-complete}
## Complete and cocomplete categories

$\mathcal C$ is *complete* when every diagram of small shape has a limit, *cocomplete* when every such diagram has a colimit, and *bicomplete* when both hold.
It is *finitely complete* when every diagram of finite shape has a limit, and *finitely cocomplete* dually.
:::

::: {#thm-limits-from-products-equalizers}
## Limits from products and equalizers

Let $\mathcal C$ have equalizers of all parallel pairs and products indexed by $\operatorname{ob}J$ and $\operatorname{ar}J$.
Then every diagram $D\colon J\to\mathcal C$ has a limit, namely the equalizer of the two morphisms
$$
f,g\colon\prod_{j\in J}D_j\longrightarrow\prod_{u\in\operatorname{ar}J}D_{\operatorname{cod}u},
\qquad
p_uf=p_{\operatorname{cod}u},
\quad
p_ug=D(u)\circ p_{\operatorname{dom}u},
$$
with limit cone $\lambda_j=p_j\circ e$ for the equalizer $e$.
Consequently a category with equalizers and all small products is complete, and a category with a terminal object, binary products, and equalizers is finitely complete [@Mac98, §V.2, Theorem 1 and Corollaries 1–2].
:::

A terminal object and pullbacks also suffice for finite completeness: the product $X\times Y$ is the pullback of $X\to *\leftarrow Y$, and the equalizer of $f,g\colon X\to Y$ is the pullback of $(\operatorname{id},f)$ and $(\operatorname{id},g)\colon X\to X\times Y$.
Completeness is a stronger hypothesis than finite completeness, and a small category that is complete is a preorder with all small meets [@Mac98, §V.2, Proposition 3].

## Preservation, reflection, and creation {#sec-preservation}

::: {#def-preserve-reflect-create}
## Preservation, reflection, and creation of limits

Let $F\colon\mathcal C\to\mathcal D$ and fix a class of diagrams in $\mathcal C$.
$F$ *preserves* those limits when the image of a limit cone over $K$ is a limit cone over $FK$.
$F$ *reflects* them when a cone over $K$ whose image is a limit cone over $FK$ is already a limit cone.
$F$ *creates* them when, whenever $FK$ has a limit in $\mathcal D$, some limit cone over $FK$ lifts to a limit cone over $K$, and $F$ reflects those limits.
The dual conditions define preservation, reflection, and creation of colimits [@Rie16, Definition 3.3.1].

If $F$ creates limits of a class of diagrams and $\mathcal D$ has those limits, then $\mathcal C$ has them and $F$ preserves them [@Rie16, Proposition 3.3.3].
:::

Which forgetful functors create which limits is recorded in [Distinguished functors and comparison](Distinguished-Functors.md#sec-creation).

## Kan extensions {#sec-kan}

::: {#def-kan-extension}
## Right and left Kan extensions

Let $K\colon M\to\mathcal C$ and $T\colon M\to\mathcal A$ be functors, and let $\mathcal A^{K}\colon\mathcal A^{\mathcal C}\to\mathcal A^{M}$ be the functor given by precomposition with $K$.
A *right Kan extension of $T$ along $K$* is a pair
$$
\bigl(\operatorname{Ran}_KT\in\mathcal A^{\mathcal C},\quad
\varepsilon\colon(\operatorname{Ran}_KT)\circ K\Rightarrow T\bigr)
$$
that is universal among arrows from $\mathcal A^{K}$ to $T$: every pair $(S,\sigma\colon S\circ K\Rightarrow T)$ factors as $\sigma=\varepsilon\cdot(\alpha K)$ for a unique $\alpha\colon S\Rightarrow\operatorname{Ran}_KT$.
Dually, a *left Kan extension* is a pair $(\operatorname{Lan}_KT,\;\eta\colon T\Rightarrow(\operatorname{Lan}_KT)\circ K)$ universal among arrows from $T$ to $\mathcal A^{K}$ [@Mac98, §X.3].
When these exist for every $T$, they are the adjoints of precomposition:
$$
\adj{\mathcal A^{M}}{\mathcal A^{\mathcal C}}{\operatorname{Lan}_K}{\mathcal A^{K}},
\qquad
\adj{\mathcal A^{\mathcal C}}{\mathcal A^{M}}{\mathcal A^{K}}{\operatorname{Ran}_K},
\qquad
\operatorname{Lan}_K\dashv\mathcal A^{K}\dashv\operatorname{Ran}_K .
$$

When the relevant limits exist, the right Kan extension is computed pointwise as
$$
(\operatorname{Ran}_KT)(c)\;=\;\lim\bigl((c\downarrow K)\longrightarrow M\xrightarrow{\;T\;}\mathcal A\bigr),
$$
the limit over the comma category $(c\downarrow K)$ of @def-comma-category, and dually $(\operatorname{Lan}_KT)(c)$ is the colimit over $(K\downarrow c)$ [@Mac98, §X.3, Theorem 1 and §X.5].
:::

::: {#thm-limits-as-kan}
## Limits as Kan extensions

Let $!\colon J\to\mathbf 1$ be the unique functor to the terminal category.
A functor $\mathbf 1\to\mathcal A$ is an object of $\mathcal A$, and a natural transformation $T\Rightarrow S\circ{!}$ is a cocone under $T$ with nadir the object $S$.
Hence the left Kan extension $\operatorname{Lan}_{!}T$ is the colimit of $T$, with its universal transformation the colimit cocone, and dually $\operatorname{Ran}_{!}T$ is the limit of $T$ [@Mac98, §X.7].
:::
