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

## Inverse data and coherence {#sec-inverse-data}

Let $F\colon C\to D$ be an equivalence with a chosen inverse $G$ and chosen isomorphisms $\eta\colon 1_C\cong GF$ and $\epsilon\colon FG\cong 1_D$.
Such a triple $(G,\eta,\epsilon)$ need not satisfy the triangle identities, and any one that does not may be replaced by one that does: redefining either $\eta$ or $\epsilon$ promotes the triple to an *adjoint equivalence*, in which $\eta$ and $\epsilon$ are the unit and counit of $F\dashv G$ [@Rie16, Proposition 4.4.5].

The distinction between the two kinds of datum is a difference in truncation level.
For a map $f\colon A\to B$ of types with an inverse, the type of triples $(g,\eta,\epsilon)$ is equivalent to $\prod_{x:A}(x=x)$ [@Uni13, Lemma 4.1.1], which is not in general contractible, so such a triple is a choice.
Adding the coherence datum relating $\eta$ and $\epsilon$ gives the type of half-adjoint equivalence data, which is inhabited whenever an inverse exists [@Uni13, Theorem 4.2.3] and is a mere proposition [@Uni13, Theorem 4.2.13].
Being an equivalence is therefore a property of $f$, while a chosen inverse together with uncohered isomorphisms is data of the kind named in @sec-witnesses.

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
