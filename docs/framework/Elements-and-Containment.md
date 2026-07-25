# Elements, subobjects, and scalar extension {#sec-elements-containment}

## Elements {#sec-elements}

For $X\in C$, a generalized element with domain $T$ is a morphism $T\to X$.
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
Two representatives $i\colon N\hookrightarrow M$ and $i'\colon N'\hookrightarrow M$ define the same subobject when there is an isomorphism $u\colon N\xrightarrow{\sim}N'$ with $i=i'\circ u$ [@Mac94, I.5].
:::

A factorization from the subobject represented by $i\colon N\hookrightarrow M$ to the one represented by $j\colon P\hookrightarrow M$ is a morphism $f\colon N\to P$ with $i=j\circ f$.

The assertion that some monomorphism $A\to B$ exists is a proposition.
A construction that uses an embedding names a particular monomorphism.

## Comparison after a named functor

Let $F\colon C\to E$ and $G\colon D\to E$.
A comparison between $X\in C$ and $Y\in D$ is made between $F(X)$ and $G(Y)$ in $E$.
A relation or morphism involving the images is formed in $E$ and does not identify either source object with its image.

## Solution functors {#sec-generic-solutions}

::: {#def-generic-solution}
Let $A,B\colon C^{\mathrm{op}}\to\mathbf{Set}$ be presheaves and let $\alpha,\beta\colon A\Rightarrow B$ be natural transformations.
Their equalizer
$$
\operatorname{Sol}:=\operatorname{Eq}(\alpha,\beta)
$$
is the presheaf of solutions of the corresponding equations.
If $\operatorname{Sol}\cong\operatorname{Hom}_C(-,X)$, the identity of $X$ determines its universal solution.
:::

## Disjunction and cases {#sec-case-decomposition}

For object properties $P$ and $Q$, the full subcategory defined by $P\lor Q$ is valid.
A proof by cases consists of implications $P\Rightarrow R$ and $Q\Rightarrow R$ together with the hypothesis $P\lor Q$.
For chosen structures, a coproduct or union of their domains does not automatically define a category of objects equipped with either structure; its morphisms and universal property must be specified.

## Scalar extension, localization, and completion {#sec-localization}

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
