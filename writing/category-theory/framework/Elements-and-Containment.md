# Elements, subobjects, and scalar extension {#sec-elements-containment}

## Elements {#sec-elements}

A generalized element with domain $T$ is defined in @def-generalized-element; it is a morphism $T\to X$.
If $F\colon C^{\mathrm{op}}\to\mathbf{Set}$ is a presheaf, an element $x\in F(T)$ is the object $(T,x)$ of $\int_C F$ defined in @def-category-of-elements.

::: {#def-element-functor}
If a concrete functor $U\colon C\to\mathbf{Set}$ is corepresented by $P$, a specified natural isomorphism
$$
U\cong\operatorname{Hom}_C(P,-)
$$
identifies an element of $U(X)$ with a morphism $P\to X$.
The corepresenting objects are a singleton for $\mathbf{Set}$, $\mathbb Z$ for $\mathbf{Grp}$, $R$ for $R\text{-}\mathbf{Mod}$, and $\mathbb Z[x]$ for $\mathbf{CommRing}$.
:::

An isomorphism-invariant property $P$ defines the replete full subcategory $C_P$ of objects satisfying $P$.
A disjunction $P\lor Q$ defines the join of $C_P$ and $C_Q$ in the inclusion preorder (@def-join-diagram).
Categories of objects with chosen structure are instead described by their forgetful functors.

## Subobjects {#sec-containment}

::: {#def-subobject-relation}
A *subobject* of $M\in C$ is an isomorphism class of monomorphisms $i\colon N\hookrightarrow M$.
A representative of the subobject is a specific monomorphism.
Two representatives $i\colon N\hookrightarrow M$ and $i'\colon N'\hookrightarrow M$ define the same subobject when there is an isomorphism $u\colon N\xrightarrow{\sim}N'$ with $i=i'\circ u$ [@MM12, I.5].
:::

A factorization from the subobject represented by $i\colon N\hookrightarrow M$ to the one represented by $j\colon P\hookrightarrow M$ is a morphism $f\colon N\to P$ with $i=j\circ f$.

The assertion that some monomorphism $A\to B$ exists is a proposition.
A construction that uses an embedding names a particular monomorphism.

## Fibers of a morphism {#sec-fibers}

::: {#def-fiber-over-point}
## The fiber over a point

Let $C$ have a terminal object $1$ and the relevant pullbacks, let $f\colon X\to Y$, and let $y\colon 1\to Y$ be a point.
The *fiber of $f$ over $y$* is the apex of the cartesian square

```{.tikz}
%%| filename: fiber-over-a-point
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}
f^{-1}(y)
  \arrow[r]
  \arrow[d]
  \arrow[dr,phantom,very near start,"\lrcorner"] &
X \arrow[d,"f"]\\
1 \arrow[r,"y"'] & Y
\end{tikzcd}
```

In a concrete category whose underlying-set functor is corepresented as in @def-element-functor, its points are the elements of $X$ sent by $f$ to $y$.
When $C$ is pointed and $y$ is the zero point, this is the fiber of @def-fiber-cofiber.
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

::: {#def-solution-presheaf}
Let $A,B\colon C^{\mathrm{op}}\to\mathbf{Set}$ be presheaves and let $\alpha,\beta\colon A\Rightarrow B$ be natural transformations.
Their equalizer
$$
\operatorname{Sol}:=\operatorname{Eq}(\alpha,\beta)
$$
is the presheaf of solutions of the corresponding equations.
If $\operatorname{Sol}\cong\operatorname{Hom}_C(-,X)$, the identity of $X$ determines its universal solution.
:::

## Disjunction and cases {#sec-disjunction-and-cases}

For object properties $P$ and $Q$, the full subcategory defined by $P\lor Q$ is valid.
A proof by cases consists of implications $P\Rightarrow R$ and $Q\Rightarrow R$ together with the hypothesis $P\lor Q$.
For chosen structures, a coproduct or union of their domains does not automatically define a category of objects equipped with either structure; its morphisms and universal property must be specified.

## Scalar extension, localization, and completion {#sec-scalar-extension}

Extension of scalars along $\mathbb Z\to\mathbb Z_{(p)}$ is localization at the prime ideal $(p)$.
Extension of scalars along $\mathbb Z\to\mathbb Z_p$ sends a $\mathbb Z$-module $L$ to $L\otimes_{\mathbb Z}\mathbb Z_p$.
If $L$ is finitely generated, the canonical map
$$
L\otimes_{\mathbb Z}\mathbb Z_p
\longrightarrow
\varprojlim_n L/p^nL
$$
is an isomorphism, so this scalar extension computes the $p$-adic completion of $L$.
Without the finite-generation hypothesis, scalar extension and completion are distinct constructions.
A conclusion about $L$ from either image requires a stated descent or local-to-global theorem with its hypotheses.
