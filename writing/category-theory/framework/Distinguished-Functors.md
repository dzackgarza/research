# Distinguished functors and comparison {#sec-distinguished-functors}

## Specified factorizations {#sec-specified-factorizations}

::: {#def-distinguished-factorization}
A factorization of $F\colon C\to E$ through $D$ consists of functors $H\colon C\to D$ and $G\colon D\to E$ together with an equality $F=G\circ H$ or a specified natural isomorphism $F\Rightarrow G\circ H$.
The source, target, and comparison are part of the factorization.

The underlying-set functor of an $R$-module is the composite
$$
R\text{-}\mathbf{Mod}\longrightarrow\mathbf{Ab}
\longrightarrow\mathbf{Grp}\longrightarrow\mathbf{Set}.
$$
An alternative forgetful functor is accompanied by its comparison with this composite.
:::

## Creation of limits {#sec-creation}

Preservation, reflection, and creation of limits by a functor are defined in @def-preserve-reflect-create.
A monadic functor $U\colon\mathcal A\to\mathcal C$ creates any limits that $\mathcal C$ has, and creates those colimits that $\mathcal C$ has and that the monad and its square preserve [@Rie16, Theorem 5.6.5].
The forgetful functors to $\mathbf{Set}$ from $\mathbf{Monoid}$, $\mathbf{Grp}$, $\mathbf{Ab}$, $\mathbf{Ring}$, $R\text{-}\mathbf{Mod}$, and $\mathbf{Vect}_k$ are monadic [@Rie16, Corollary 5.5.3].

Hence a limit in $R\text{-}\mathbf{Mod}$ is computed on underlying sets, and the module structure on the limit is the unique one lifting the limit cone.
The kernel of a module homomorphism is a limit — the equalizer of $f$ and $0$ (@def-kernel-cokernel) — so it is the set-theoretic kernel with its unique compatible module structure, and the same computation serves for the underlying abelian group.

Creation is a statement about limit cones: a subgroup of the underlying abelian group of an $R$-module need not be a submodule, while the underlying set of a kernel admits exactly one module structure making it the kernel in $R\text{-}\mathbf{Mod}$.
A construction whose value happens to agree on underlying sets across two categories names the functor along which it is created, since agreement of underlying data is not by itself a factorization (@sec-statements-vs-constructions).

## Parallel functors {#sec-parallel-functors}

Let $F,G\colon C\to D$ be parallel functors.
A comparison is a natural transformation $F\Rightarrow G$; an invertible comparison is a natural isomorphism.
A natural transformation is invertible exactly when each of its components is, the componentwise inverses then being the components of the inverse transformation [@Mac98, §I.4].
If no comparison is specified, $F$ and $G$ remain distinct.
For example, the additive and multiplicative monoids of a ring define distinct functors $\mathbf{Ring}\to\mathbf{Mon}$.

## Comparison through a common target {#sec-comparison-common-target}

Suppose $X\in C$, $Y\in D$, and functors $F\colon C\to E$ and $G\colon D\to E$ have been named.
A relation or operation involving $X$ and $Y$ may be formed in $E$ from $F(X)$ and $G(Y)$ when $E$ has the required relation or operation.
The resulting statement names $E$, $F$, and $G$.

When several targets are available, the comparison data include either a chosen target or a functor comparing the targets.
Their mere existence supplies no order relation among them.

## Landing statements and constructions {#sec-statements-vs-constructions}

A theorem that $F\colon C\to D$ lands in a replete full subcategory $i\colon D_P\hookrightarrow D$ is a factorization $F=i\circ\bar F$.
This theorem does not redefine $F$ or $D_P$.

Pulling back a property or a family along $F$ uses the square in @sec-pullback-general.
Applying a construction after $F$ uses the explicit composite; the construction is not silently transferred to $C$.
