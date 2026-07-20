# Equality

What the framework encodes by "equality of objects" — more than a path, less than a strict identity — and how it reduces to the propositional equality that Lean and Sage actually compute with.
The construction is recorded from the design discussions; its one open point, a canonical equality-bearing universe, is marked as such.

## What equality should encode {#sec-equality-encodes}

Colloquially, $a = b$ should mean there is an *essentially unique* way to identify $a$ with $b$.
Two objects equal in several genuinely different ways is not a notion ordinary mathematics wants — it is hard to name an object one would want that of, and it is a focal point of contention in Mochizuki's work.
So equality is neither mere existence of an identification (inhabitedness of a path space) nor the demand that the whole space of identifications be contractible without regard to the symmetries of the endpoints.
The right notion sits between, and it must be compatible with reflexivity, $a = a$.

## The identification space {#sec-identification-space}

Work in the ambient $\mathbf{Cat}_\omega$ ([Framework](Ambient-Setting.md#sec-ambient)); the subcategory, quotient, and fiber constructions below are its [suspension–loop–fiber calculus](Loops-and-Suspension.md).
For objects $C, D$ write
$$
[C, D] := \operatorname{Fun}(C, D) \in \mathbf{Cat}_\omega
$$
for the internal hom ([Framework](Ambient-Setting.md#def-internal-hom)), and let
$$
\operatorname{Eq}(C, D) \hookrightarrow [C, D]
$$
be the full $\infty$-subcategory spanned by the *equivalences* $F \colon C \to D$ ([Framework](Ambient-Setting.md#def-equality-of-objects)). It retains every higher natural transformation between such functors — it is neither the core nor a truncation.
Inside it,
$$
\operatorname{Way}(C, D) \hookrightarrow \operatorname{Eq}(C, D)
$$
is the subcategory of equivalences that count as *literal identifications* of $C$ and $D$, stable under pre- and post-composition by the internal automorphism categories $\operatorname{Aut}(C) = \operatorname{Eq}(C, C)$ and $\operatorname{Aut}(D) = \operatorname{Eq}(D, D)$.

## The equality predicate {#sec-equality-predicate}

Form the homotopy double quotient
$$
Q(C, D) := \operatorname{Aut}(C) \,\backslash\, \operatorname{Way}(C, D) \,/\, \operatorname{Aut}(D).
$$
The first approximation, $C = D \iff Q(C, D) \simeq *$, says that modulo the automorphisms of the endpoints there is an essentially unique orbit of identifications.
It is refined to enforce compatibility with reflexivity: composition gives endpoint maps
$$
\bar s \colon Q(C, D) \to Q(C, C), \qquad \bar t \colon Q(C, D) \to Q(D, D),
$$
and $\operatorname{id}_C, \operatorname{id}_D$ pick out distinguished points of $Q(C, C)$ and $Q(D, D)$.
Setting
$$
Q^0(C, D) := * \times_{Q(C,C) \times Q(D,D)} Q(C, D)
$$
— the fiber over $(\operatorname{id}_C, \operatorname{id}_D)$ — the equality predicate is
$$
\boxed{\; C = D \iff Q^0(C, D) \simeq *. \;}
$$
Equality thus means: there is an essentially unique $\operatorname{Aut}(C)$–$\operatorname{Aut}(D)$ orbit of equivalences that count as literal identifications, and it is coherently compatible with the canonical reflexive identifications $C = C$ and $D = D$.

## Over an equality-bearing universe {#sec-equality-universe}

Which identifications *count* is fixed by placing the objects over a universe $U$, with $p_C \colon C \to U$ and $p_D \colon D \to U$, and taking $\operatorname{Way}(C, D)$ to be the equivalences in the slice $\mathbf{Cat}_\omega / U$ — those lifting $\operatorname{id}_U$, rather than arbitrary equivalences of $\mathbf{Cat}_\omega$.
This is what lets $C \simeq D$ hold while $C \ne D$: the equivalence need not lift the identity of $U$.

*Open.* A fully canonical construction of $U$, and hence of $\operatorname{Way}$, is not settled; the orbit-and-reflexivity predicate above is conditional on that subcategory.

## The reduction to Lean {#sec-equality-reduction}

Type theory is a shadow of higher-category theory: the homotopy-type functor $\Pi_\infty \colon \mathbf{Cat}_\omega \to \mathcal S = \mathbf{Types}$ ([Framework](Ambient-Setting.md#def-mapping-spaces)) strictly loses data.
The framework is therefore developed synthetically — in $\infty$-categories, not committed to a model such as simplicial sets and Kan complexes — and the encodable notions are recovered by applying that functor.
The equality above is then *relaxed*: for the $1$-categorical work that is almost all of the program (sets, rings, modules, algebras, lattices — all of SageCat), it truncates to Lean's propositional or definitional equality ([Framework](Ambient-Setting.md#def-equality-of-objects)), so that $\sqrt 2 = \sqrt{1 + 1}$ holds without an infinite tower of coherence obligations.
The full notion is recorded here so that its truncation is a deliberate concession rather than an accident; where it will bite is the identification of points carrying nontrivial automorphisms — inertia or stabilizers on a stack.
