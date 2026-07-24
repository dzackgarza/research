# Algebraic categories from operations {#sec-named-categories}

## Algebras for a signature

Let $\Sigma$ be a one-sorted algebraic signature.
A $\Sigma$-algebra in $\mathbf{Set}$ is a set $X$ together with one function $X^n\to X$ for every $n$-ary operation symbol of $\Sigma$.
A homomorphism is a function preserving every operation.
Equations between $\Sigma$-terms define a full subcategory of $\Sigma$-algebras.

::: {#def-operation-categories}
## Magmas

A *magma* is a set $X$ with a binary operation $\mu\colon X\times X\to X$.
A magma homomorphism $f\colon X\to Y$ satisfies
$$
f\circ\mu_X=\mu_Y\circ(f\times f).
$$
The resulting category is denoted $\mathbf{Mag}$.
The forgetful functor $\mathbf{Mag}\to\mathbf{Set}$ is faithful and is not full.
:::

::: {#def-operation-axioms}
## Associativity and commutativity

A magma is *associative* if
$$
\mu\circ(\mu\times\operatorname{id})
=\mu\circ(\operatorname{id}\times\mu)
\colon X^3\longrightarrow X.
$$
It is *commutative* if $\mu=\mu\circ\tau$, where $\tau(x,y)=(y,x)$.
These are isomorphism-invariant properties of magmas and define replete full subcategories of $\mathbf{Mag}$.
:::

::: {#def-semigroup-monoid}
## Semigroups and monoids

A *semigroup* is an associative magma.
A *monoid* is a tuple $(X,\mu,e)$ consisting of a semigroup and a chosen element $e\in X$ such that
$$
\mu(e,x)=x=\mu(x,e)
$$
for every $x\in X$.
A monoid homomorphism preserves both $\mu$ and $e$.

The functor $\mathbf{Mon}\to\mathbf{Semigrp}$ is faithful and is not full: a semigroup homomorphism between monoids need not preserve the unit.
Thus the unit is chosen structure, while the unit laws are properties of the pointed semigroup.
:::

::: {#def-group}
## Groups

A *group* is a monoid $(G,\mu,e)$ for which every $g\in G$ has an inverse.
The inverse is unique and is preserved by every monoid homomorphism.
Therefore $\mathbf{Grp}\to\mathbf{Mon}$ is fully faithful, with replete essential image the monoids in which every element is invertible.
:::

## Commutative algebraic categories

Commutative semigroups, commutative monoids, and abelian groups are obtained by imposing commutativity on semigroups, monoids, and groups.
Their inclusions are replete and full.
The category of abelian groups is equivalent to $\mathbb Z\text{-}\mathbf{Mod}$.

::: {#exm-ring}
## Rings

A ring is a tuple
$$
(R,0,1,+,-,\cdot)
$$
such that $(R,0,+,-)$ is an abelian group, $(R,1,\cdot)$ is a monoid, and multiplication distributes over addition.
A ring homomorphism preserves $0$, $1$, addition, negation, and multiplication.
A commutative ring also satisfies $xy=yx$.
:::

## Forgetful functors

::: {#def-tower}
The standard definitions give the composable forgetful functors
$$
\mathbf{Grp}\longrightarrow\mathbf{Mon}\longrightarrow
\mathbf{Semigrp}\longrightarrow\mathbf{Mag}\longrightarrow\mathbf{Set}
$$
and
$$
\mathbf{Ring}\longrightarrow\mathbf{Ab}\longrightarrow\mathbf{Grp}
\longrightarrow\mathbf{Set}.
$$
The additive and multiplicative functors from rings are distinct.
Comparisons or factorizations involving them use the named functor, as specified in [Distinguished functors and comparison](Distinguished-Functors.md).
:::

Combining two categories of structures over the same underlying category uses the pseudo-pullback of their forgetful functors.
Combining two object properties uses the intersection described in [Joins, meets, and closure](Joins-Meets-and-Closure.md).
