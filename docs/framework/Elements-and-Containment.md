# Elements, subobjects, and hypotheses {#sec-elements-containment}

## Elements {#sec-elements}

For $X\in C$, a generalized element with domain $T$ is a morphism $T\to X$. If
$F\colon C^{\mathrm{op}}\to\mathbf{Set}$ is a presheaf, an element
$x\in F(T)$ is the object $(T,x)$ of $\operatorname{El}(F)$ defined in
@def-category-of-elements.

::: {#def-element-functor}
If a concrete functor $U\colon C\to\mathbf{Set}$ is corepresented by $P$, a specified
natural isomorphism
$$
U\cong\operatorname{Hom}_C(P,-)
$$
identifies an element of $U(X)$ with a morphism $P\to X$. The corepresenting objects are
a singleton for $\mathbf{Set}$, $\mathbb Z$ for $\mathbf{Grp}$, $R$ for
$R\text{-}\mathbf{Mod}$, and $\mathbb Z[x]$ for $\mathbf{CommRing}$.
:::

An isomorphism-invariant property $P$ defines the replete full subcategory $C_P$ of
objects satisfying $P$. A disjunction $P\lor Q$ defines the join of $C_P$ and $C_Q$ in
the inclusion preorder (@def-join-diagram). Categories of objects with chosen structure
are instead described by their forgetful functors.

## Subobjects {#sec-containment}

::: {#def-subobject-relation}
A *subobject* of $M\in C$ is an isomorphism class of monomorphisms
$i\colon N\hookrightarrow M$. A representative of the subobject is a specific
monomorphism. Two representatives $i\colon N\hookrightarrow M$ and
$i'\colon N'\hookrightarrow M$ define the same subobject when there is an isomorphism
$u\colon N\xrightarrow{\sim}N'$ with $i=i'\circ u$ [@Mac94, I.5].
:::

A factorization from the subobject represented by $i\colon N\hookrightarrow M$ to the
one represented by $j\colon P\hookrightarrow M$ is a morphism $f\colon N\to P$ with
$i=j\circ f$.

The assertion that some monomorphism $A\to B$ exists is a proposition. A construction
that uses an embedding names a particular monomorphism.

::: {#exm-subobject-base-change}
**Example.** Let $L$ be an integral lattice and $v\in L$. The inclusion
$\mathbb Zv\hookrightarrow L$ represents a subobject of the underlying
$\mathbb Z$-module. After base change, $\mathbb Rv\hookrightarrow
L\otimes_{\mathbb Z}\mathbb R$ represents a subspace. These monomorphisms belong to
different categories and are related by the base-change functor.
:::

## Comparison after a named functor

Let $F\colon C\to E$ and $G\colon D\to E$. A comparison between $X\in C$ and
$Y\in D$ is made between $F(X)$ and $G(Y)$ in $E$. For modules, base change is written
explicitly: a real line is compared with the real vector space
$L\otimes_{\mathbb Z}\mathbb R$; the integral lattice $L$ remains an object of
$\mathbb Z\text{-}\mathbf{Mod}$.

## Solution functors {#sec-generic-solutions}

::: {#def-generic-solution}
Let $A,B\colon C^{\mathrm{op}}\to\mathbf{Set}$ be presheaves and let
$\alpha,\beta\colon A\Rightarrow B$ be natural transformations. Their equalizer
$$
\operatorname{Sol}:=\operatorname{Eq}(\alpha,\beta)
$$
is the presheaf of solutions of the corresponding equations. If
$\operatorname{Sol}\cong\operatorname{Hom}_C(-,X)$, the identity of $X$ determines its
universal element. A "generic solution" is used only after this representability has been
proved.
:::

## Hypotheses {#sec-hypotheses}

A theorem records every hypothesis needed for its conclusion. A hypothesis may be an
object property, an equality of named morphisms, the existence of a limit, flatness, a
characteristic restriction, or another stated proposition. A later construction that
uses a witness names that witness instead of retaining only its existence.

## Disjunction and cases {#sec-case-decomposition}

For object properties $P$ and $Q$, the full subcategory defined by $P\lor Q$ is valid.
A proof by cases consists of implications $P\Rightarrow R$ and $Q\Rightarrow R$ together
with the hypothesis $P\lor Q$. For chosen structures, a coproduct or union of their
domains does not automatically define a category of objects equipped with either
structure; its morphisms and universal property must be specified.

## Localization and descent {#sec-localization}

Localization or completion is application of a named functor, such as
$L\mapsto L\otimes_{\mathbb Z}\mathbb Z_p$. A statement proved for the image is a
statement about that localized object. A conclusion about $L$ requires a stated descent
or local-to-global theorem with its hypotheses.
