# Distinguished functors and comparison {#sec-distinguished-functors}

## Specified factorizations {#sec-specified-factorizations}

::: {#def-distinguished-factorization}
A factorization of $F\colon C\to E$ through $D$ consists of functors
$H\colon C\to D$ and $G\colon D\to E$ together with an equality
$F=G\circ H$ or a specified natural isomorphism $F\Rightarrow G\circ H$. The source,
target, and comparison are part of the factorization.

The underlying-set functor of an $R$-module is the composite
$$
R\text{-}\mathbf{Mod}\longrightarrow\mathbf{Ab}
\longrightarrow\mathbf{Grp}\longrightarrow\mathbf{Set}.
$$
An alternative forgetful functor is accompanied by its comparison with this composite.
:::

## Parallel functors {#sec-parallel-functors}

Let $F,G\colon C\to D$ be parallel functors. A comparison is a natural transformation
$F\Rightarrow G$; an invertible comparison is a natural isomorphism. If no comparison is
specified, $F$ and $G$ remain distinct. For example, the additive and multiplicative
monoids of a ring define distinct functors $\mathbf{Ring}\to\mathbf{Mon}$.

## Comparison through a common target {#sec-comparison-common-target}

Suppose $X\in C$, $Y\in D$, and functors $F\colon C\to E$ and
$G\colon D\to E$ have been named. A relation or operation involving $X$ and $Y$ may be
formed in $E$ from $F(X)$ and $G(Y)$ when $E$ has the required relation or operation.
The resulting statement names $E$, $F$, and $G$.

When several targets are available, the comparison data include either a chosen target
or a functor comparing the targets. Their mere existence supplies no order relation
among them.

## Landing statements and constructions {#sec-statements-vs-constructions}

A theorem that $F\colon C\to D$ lands in a replete full subcategory
$i\colon D_P\hookrightarrow D$ is a factorization $F=i\circ\bar F$. This theorem does
not redefine $F$ or $D_P$.

Pulling back a property or a family along $F$ uses the square in
@sec-pullback-general. Applying a construction after $F$ uses the explicit composite;
the construction is not silently transferred to $C$.
