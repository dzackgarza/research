# Elements, subobjects, and scalar extension {#sec-elements-containment}

## Elements {#sec-elements}

A generalized element of $X$ with domain $T$ is a morphism $T\to X$ (@def:generalized-element).
If $F\colon C^{\opop}\to\mathbf{Set}$ is a presheaf, an element $x\in F(T)$ is the object $(T,x)$ of $\int_C F$ defined in @def:category-of-elements.

::: {.definition #def:element-functor title="Elements as maps from a corepresenting object" defines="corepresenting object"}
If a concrete functor $U\colon C\to\mathbf{Set}$ is corepresented by $P$, a specified natural isomorphism (@def:isomorphism-of-objects)
$$
U\cong\Hom_C(P,-)
$$
identifies an element of $U(X)$ with a morphism $P\to X$.
The corepresenting objects are a singleton for $\mathbf{Set}$, $\bZ$ for $\mathbf{Grp}$, $R$ for $R\text{-}\mathbf{Mod}$, and $\bZ[x]$ for $\mathbf{CommRing}$.
:::

An isomorphism-invariant property $P$ defines the replete full subcategory $C_P$ of objects satisfying $P$.
A disjunction $P\lor Q$ defines the join of $C_P$ and $C_Q$ in the inclusion preorder (@def:join-diagram).
Categories of objects with chosen structure are instead described by their forgetful functors.

## Subobjects {#sec-containment}

::: {.definition #def:subobject-relation title="Subobjects as monomorphisms up to isomorphism" defines="subobject"}
A *subobject* of $M\in C$ is an isomorphism (@def:isomorphism-of-objects) class of monomorphisms $i\colon N\hookrightarrow M$.
A representative of the subobject is a specific monomorphism.
Two representatives $i\colon N\hookrightarrow M$ and $i'\colon N'\hookrightarrow M$ define the same subobject when there is an isomorphism $u\colon N\isoto N'$ with $i=i'\circ u$ [@MM12, I.5].
:::

A factorization from the subobject represented by $i\colon N\hookrightarrow M$ to the one represented by $j\colon P\hookrightarrow M$ is a morphism $f\colon N\to P$ with $i=j\circ f$.

The assertion that some monomorphism $A\to B$ exists is a proposition.
A construction that uses an embedding names a particular monomorphism.

::: {.example #ex:real-subsets-ambient-and-components title="A real subset and its interval components"}

For $A\subseteq X\subseteq\mathbb R$ with the induced topologies, the inclusion $A\hookrightarrow X$ determines the relative topology operations. For example,
$$
\overline A^{\,X}=X\cap\overline A^{\,\mathbb R}.
$$
Indeed a neighborhood of $x\in X$ in $X$ is the intersection with $X$ of an ambient neighborhood of $x$, and since $A\subseteq X$, either neighborhood meets $A$ exactly when its intersection with $X$ meets $A$. In particular $[0,1]$ is open in itself and has empty boundary there, whereas its boundary in $\mathbb R$ is $\{0,1\}$.

For a subset represented as a finite union of intervals, its maximal connected intervals form a finite set of components; these components are not the points of the subset. The subset $(0,1)\cup(2,3)$ has two interval components, but infinitely many points. The [Sage RealSet reference](https://doc.sagemath.org/html/en/reference/sets/sage/sets/real_set.html) provides interval-component iteration. The distinction between the two sets and their enumerations is the requirement recorded in the original [RealSet discussion](https://github.com/dzackgarza/research/blob/main/archives/provenance/lattice-research/realset_update_session.md). In the absolute real-line topology the boundary of the normalized union is the union of the component boundaries: the finite union of their closures is the closure, and a shared finite endpoint at which the union is a neighborhood would join the intervals into a single connected component.

The measure of a measurable subset is evaluated using a specified measure, here Lebesgue measure on $\mathbb R$; a sigma-algebra alone does not select such a measure. These requirements are recorded with their original constructor examples in [lean-categories #230](https://github.com/dzackgarza/lean-categories/issues/230).
:::

## Fibers of a morphism {#sec-fibers}

::: {.definition #def:fiber-over-point title="The fiber over a point" defines="fiber of $f$ over $y$"}

Let $C$ have a terminal object (@def:initial-terminal) $1$ and the relevant pullbacks (@def:pullback-square), let $f\colon X\to Y$, and let $y\colon 1\to Y$ be a point.
The *fiber of $f$ over $y$* is the apex of the cartesian square

\begin{tikzcd}
f^{-1}(y)
  \arrow[r]
  \arrow[d]
  \arrow[dr,phantom,very near start,"\lrcorner"] &
X \arrow[d,"f"]\\
1 \arrow[r,"y"'] & Y
\end{tikzcd}

In a concrete category (@def:concrete-category) whose underlying-set functor is corepresented as in @def:element-functor, its points are the elements of $X$ sent by $f$ to $y$.
When $C$ is pointed and $y$ is the zero point, this is the fiber of @def:fiber-cofiber.
:::

For $R$-modules the fiber over $y$ is empty unless $y$ lies in the image of $f$, and a point $x_0$ of it determines an isomorphism
$$
\ker f\;\xrightarrow{\ \sim\ }\;f^{-1}(y),
\qquad
k\longmapsto x_0+k .
$$
The elements of $\ker f$ act freely and transitively on the elements of $f^{-1}(y)$ by translation, so the fiber is a torsor under $\ker f$ [@nlab:torsor] and has no distinguished point.
Selecting a preimage of $y$ is therefore a choice in the sense of @sec-witnesses; the object that is choice-free is the fiber, and a construction that consumes a preimage names the one it uses.

## Comparison after a named functor

Let $F\colon C\to E$ and $G\colon D\to E$.
A comparison between $X\in C$ and $Y\in D$ is made between $F(X)$ and $G(Y)$ in $E$.
A relation or morphism involving the images is formed in $E$ and does not identify either source object with its image.

## Solution functors {#sec-solution-functors}

::: {.definition #def:solution-presheaf title="Solution presheaves as equalizers" defines="solution presheaf; $\operatorname{Sol}$; universal solution"}
Let $A,B\colon C^{\opop}\to\mathbf{Set}$ be presheaves and let $\alpha,\beta\colon A\Rightarrow B$ be natural transformations.
Their equalizer
$$
\operatorname{Sol}:=\operatorname{Eq}(\alpha,\beta)
$$
is the presheaf of solutions of the corresponding equations.
If $\operatorname{Sol}\cong\Hom_C(-,X)$, the identity of $X$ determines its universal solution.
:::

## Disjunction and cases {#sec-disjunction-and-cases}

For object properties $P$ and $Q$, the full subcategory defined by $P\lor Q$ is valid.
A proof by cases consists of implications $P\Rightarrow R$ and $Q\Rightarrow R$ together with the hypothesis $P\lor Q$.
For chosen structures, a coproduct or union of their domains does not automatically define a category of objects equipped with either structure; its morphisms and universal property must be specified.

## Scalar extension, localization, and completion {#sec-scalar-extension}

Extension of scalars along $\bZ\to\bZ_{(p)}$ is localization at the prime ideal $(p)$.
Extension of scalars along $\bZ\to\bZ_p$ sends a $\bZ$-module $L$ to $L\tensor_{\bZ}\bZ_p$.
If $L$ is finitely generated, the canonical map
$$
L\tensor_{\bZ}\bZ_p
\too
\projectivelim_n L/p^nL
$$
is an isomorphism, so this scalar extension computes the $p$-adic completion of $L$.
Without the finite-generation hypothesis, scalar extension and completion are distinct constructions.
A conclusion about $L$ from either image requires a stated descent or local-to-global theorem with its hypotheses.
