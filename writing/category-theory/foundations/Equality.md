# Equality

## What equality should encode {#sec-equality-encodes}

Colloquially, $a = b$ should mean there is an *essentially unique* way to identify $a$ with $b$.
Two objects equal in several genuinely different ways is not a notion ordinary mathematics wants.
So equality is neither mere existence of an identification (inhabitedness of a path space) nor the demand that the whole space of identifications be contractible without regard to the symmetries of the endpoints.
The right notion sits between, and it must be compatible with reflexivity, $a = a$.

## The identification space {#sec-identification-space}

Work in $\mathbf{Cat}_{\infty,\infty}$ (@def:infinity-category-universe), with the subcategory, quotient, and fiber constructions of @sec-loops-suspension.
For objects $C,D$, let
$$
[C,D]_{\mathbf{Cat}_{\infty,\infty}}
\in
\mathbf{Cat}_{\infty,\infty}
$$
be the internal hom of @def:internal-hom, and let
$$
\operatorname{Eq}(C, D)
\hookrightarrow
[C,D]_{\mathbf{Cat}_{\infty,\infty}}
$$
be the full $\infty$-subcategory spanned by the *equivalences* $F \colon C \to D$ (@def:equality-of-objects).
It retains every higher natural transformation between such functors — it is neither the core nor a truncation.
Inside it,
$$
\operatorname{Way}(C, D) \hookrightarrow \operatorname{Eq}(C, D)
$$
is the subcategory of equivalences that count as *literal identifications* of $C$ and $D$, stable under pre- and post-composition by the internal automorphism categories $\Aut(C) = \operatorname{Eq}(C, C)$ and $\Aut(D) = \operatorname{Eq}(D, D)$.

## The equality predicate {#sec-equality-predicate}

Form the homotopy double quotient
$$
Q(C, D) := \Aut(C) \,\backslash\, \operatorname{Way}(C, D) \,/\, \Aut(D).
$$
The first approximation, $C = D \iff Q(C, D) \simeq *$, says that modulo the automorphisms of the endpoints there is an essentially unique orbit of identifications.
It is refined to enforce compatibility with reflexivity: composition gives endpoint maps
$$
\bar s \colon Q(C, D) \to Q(C, C), \qquad \bar t \colon Q(C, D) \to Q(D, D),
$$
and $\id_C, \id_D$ pick out distinguished points of $Q(C, C)$ and $Q(D, D)$.
Setting
$$
Q^0(C, D) := * \times_{Q(C,C) \times Q(D,D)} Q(C, D)
$$
— the fiber over $(\id_C, \id_D)$ — the equality predicate is
$$
\boxed{\; C = D \iff Q^0(C, D) \simeq *. \;}
$$
Equality thus means: there is an essentially unique $\Aut(C)$–$\Aut(D)$ orbit of equivalences that count as literal identifications, and it is coherently compatible with the canonical reflexive identifications $C = C$ and $D = D$.

## Presentation by the walking equivalence {#sec-walking-equivalence}

Let $\mathcal E$ be the walking adjoint equivalence: the category presented (@def:presented-category) by two objects $0,1$, morphisms $u\colon 0\to 1$ and $v\colon 1\to 0$, and the relations making $(u,v)$ an adjoint equivalence.
Evaluation at the two objects gives
$$
\ev_{0,1}\colon
[\mathcal E,\mathbf{Cat}_{\infty,\infty}]_{\mathbf{Cat}_{\infty,\infty}}
\longrightarrow
\mathbf{Cat}_{\infty,\infty}\times\mathbf{Cat}_{\infty,\infty},
\qquad
F\longmapsto(F(0),F(1)),
$$
and the fiber of $\ev_{0,1}$ over $(C,D)$ is the higher category of adjoint-equivalence data from $C$ to $D$.
Sending such data to its underlying functor $F(u)$ gives a map from that fiber to $\operatorname{Eq}(C,D)$ whose fiber over a functor is the space of adjoint-equivalence structures on it, which by @sec-inverse-data is contractible for an equivalence and empty otherwise.
The two presentations of $\operatorname{Eq}(C,D)$ may therefore be used interchangeably, and $\operatorname{Way}$, $Q$, and $Q^0$ may be computed from either.

## Properties of the predicate {#sec-equality-properties}

The predicate of @sec-equality-predicate inherits the following from the corresponding closure conditions on $\operatorname{Way}$.

- $C=C$, given that $\operatorname{Way}(C,C)$ contains $\id_C$: the identity is a point of $Q^0(C,C)$.

- $C=D$ implies $D=C$, given that $\operatorname{Way}$ is closed under inverses, which exchanges the two endpoint maps $\bar s$ and $\bar t$.

- $C=D$ and $D=E$ imply $C=E$, given that $\operatorname{Way}$ is closed under composition.

For the slice presentation of @sec-equality-universe all three conditions hold, since equivalences over $W$ contain the identities and are closed under composition and inverses.

Equality implies equivalence, since a point of $Q^0(C,D)$ lies over a point of $\operatorname{Eq}(C,D)$.
The converse fails: an equivalence $C\to D$ whose image under $(\bar s,\bar t)$ misses the component of $(\id_C,\id_D)$ contributes no point of $Q^0$.
If $C$ and $D$ are both terminal objects of the same category of cones, or more generally both satisfy a universal property that determines them up to a unique isomorphism, then the comparison between them is the unique one and $Q^0(C,D)\simeq*$.

## Over an equality-bearing universe {#sec-equality-universe}

Which identifications *count* is fixed by placing the objects over a higher category $W$, with $p_C \colon C \to W$ and $p_D \colon D \to W$, and taking $\operatorname{Way}(C, D)$ to be the equivalences in the slice $\mathbf{Cat}_{\infty,\infty}/W$.
Such an equivalence lifts $\id_W$.

::: {.question #qst:canonical-equality-universe title="A canonical equality-bearing universe"}
Is there a fully canonical choice of $W$, and hence of $\operatorname{Way}$?
The orbit-and-reflexivity predicate of @sec-equality-predicate depends on that subcategory.
:::

## Truncation to propositional equality {#sec-equality-reduction}

The homotopy-type functor $\Pi_\infty \colon \mathbf{Cat}_{\infty,\infty} \to \mathcal S = \mathbf{Types}$ (@def:core) strictly loses data.
For $1$-categories (sets, rings, modules, algebras, lattices), the equality above truncates to the propositional or definitional equality of @def:equality-of-objects, so that $\sqrt 2 = \sqrt{1 + 1}$ holds without an infinite tower of coherence obligations.
The truncation loses information exactly at the identification of points carrying nontrivial automorphisms — inertia or stabilizers on a stack.
