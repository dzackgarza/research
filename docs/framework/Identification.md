# Equivalences and witnesses {#sec-identification}

## Spaces of equivalences {#sec-equivalence-spaces}

For objects $X,Y$ of an $\infty$-category $C$, let $\operatorname{Eq}_C(X,Y)\subseteq\operatorname{Map}_C(X,Y)$ be the union of the components consisting of equivalences.
The automorphism space is $\operatorname{Aut}_C(X)=\operatorname{Eq}_C(X,X)$.

For an ordinary category, the corresponding set is $\operatorname{Iso}_C(X,Y)$.
Its nonemptiness asserts $X\cong Y$; a chosen element $f\in\operatorname{Iso}_C(X,Y)$ is additional data.

## Isomorphisms as data {#sec-witnesses}

If $\operatorname{Iso}_C(X,Y)$ is nonempty, postcomposition gives a free and transitive left action of $\operatorname{Aut}_C(Y)$ and precomposition gives a free and transitive right action of $\operatorname{Aut}_C(X)$.
These actions commute, so $\operatorname{Iso}_C(X,Y)$ is an $(\operatorname{Aut}_C(Y),\operatorname{Aut}_C(X))$-bitorsor [@nlab:torsor].

A construction that transports data from $X$ to $Y$ therefore names the isomorphism it uses unless the relevant comparison is uniquely determined.

## Canonical comparisons {#sec-canonical-identification}

A comparison is available without a new choice in either of the following situations:

1. a universal property supplies a unique comparison compatible with the specified structure;

2. the construction includes a distinguished isomorphism or natural isomorphism.

Associators, unitors, and comparison maps between two limits of the same diagram are examples.
Their naturality and coherence are part of the comparison.

## Images under functors {#sec-coarse-identification}

For a functor $F\colon C\to D$, an isomorphism or equivalence $X\to Y$ induces one $F(X)\to F(Y)$.
A weaker comparison obtained only after applying $F$ is written as a claim in $D$, for example $F(X)\cong F(Y)$.
Genus, stable equivalence, and isospectrality use different functors and therefore define different relations.

Literal equality, isomorphism, and equivalence retain the meanings fixed in @def-equality-of-objects.
No additional equality predicate is introduced.
