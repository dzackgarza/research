# Identification {#sec-identification}

Every claim that two things are the same names the kind of sameness and the category in
which it holds. The symbols are typed claims
([Style Guide P5](../contributing/Mathematical-Language-Style-Guide.md#sec-governing-principles)):
$x := t$ is definitional; $a = b$ is equality of elements (morphisms from a common
corepresenting object, @def-element-functor, that coincide) or definitional
coincidence; $X \cong Y$ is isomorphism in a named category; $\mathcal C \simeq
\mathcal D$ is equivalence one level up. A bare $=$ between objects of a category is
never asserted ([Framework](Mathematical-Framework.md), ambient conventions), and
distinctions of height — equality, isomorphism, equivalence, weak equivalence — are
never collapsed. Two definitional bindings with the same normal form name the same
object; a distinguished representative of an isomorphism class (a chosen
$\operatorname{Free}(\{0, \dots, n-1\})$) is a definitional anchor only, never assumed
strictly preserved by functors.

## Isomorphism is data {#sec-witnesses}

::: {#prp-witness-torsor}
## The witnesses form a torsor

For $X, Y \in \mathcal C$, the isomorphisms $X \to Y$, when any exist, form a torsor
over $\operatorname{Aut}(X)$ [@nlab:torsor]: except where automorphisms are trivial
there are many, and they are inequivalent as data. A claim $X \cong Y$ therefore has
two inequivalent forms — the *truncated* claim that the torsor is nonempty, and a
*witness*, a named isomorphism $w \colon X \to Y$. Only a witness supports transport:
carrying structure or statements across the identification is transport along $w$,
and the result depends on $w$ whenever $\operatorname{Aut}(X) \ne 1$.
:::

Identifying two copies of a lattice inside an overlattice is the standing example: the
glued object depends on the chosen isometry, not merely on the fact of isometry. The
truncated claim and the witnessed claim are kept separate everywhere — a nonemptiness
answer is never upgraded to a witness, and every transport step records the witness it
used.

## Canonical identification {#sec-canonical-identification}

::: {#def-canonical-identification}
## Canonical identification

Two expressions are identified without further data in exactly two situations:

1. **Contractible comparison.** The space of comparison isomorphisms is contractible —
   associators, unitors, the comparisons of universal constructions, every
   identification unique up to unique isomorphism. Here the truncated and witnessed
   claims coincide.
2. **Distinguished comparison.** The presentation names a distinguished isomorphism
   between the two expressions, as a natural isomorphism with its coherence.
   Distinguished comparisons compose: the composite of distinguished comparisons along
   a factorization is the distinguished comparison of the composite, stated as
   commutative squares with named 2-cells
   ([Distinguished Functors](Distinguished-Functors.md#sec-parallel-functors)), so
   transport is independent of the factorization chosen.

No identification is inferred from equality of invariants, equality of names, or bare
existence of an unspecified isomorphism.
:::

A rewriting step — replacing a subexpression along an identification — is legal exactly
when the identification is: definitional (unfolding, normal forms), canonical in the
sense above, or witnessed by a named isomorphism in scope; each nontrivial step records
which, and chains compose their witnesses. Confluence of distinguished comparisons is
the coherence requirement of @def-canonical-identification, discharged in the
presentation rather than assumed.

## Sameness after a functor {#sec-coarse-identification}

::: {#def-coarse-identification}
## Coarse identification

Every notion of sameness coarser than isomorphism is isomorphism after a named functor,
and the functor is part of the claim: genus is isomorphism after adelic base change,
taken at $\pi_0$ of the cores
([Definitions](Mathematical-Definitions.md#sec-genus-sec),
[Categorical Foundations](Categorical-Foundations.md#sec-pi0-fiber)); isospectrality is
isomorphism of images under the theta-series construction; stable equivalence is
isomorphism after a named stabilization. Distinct coarse identifications are never
merged into one symbol, and none is written $\cong$ bare: the claim is
$F(X) \cong F(Y)$ or its named abbreviation.
:::

The category of evaluation is content, not bookkeeping: deciding sameness-in-genus and
deciding isometry are different problems with divergent costs (complete local
invariants versus a search), and the truth itself moves with the category — over a ring
without invariant basis number $R^3 \cong R^4$ in $\operatorname{Mod}_R$, while
$\mathbb Z^3 \not\cong \mathbb Z^4$. Likewise $\mathbb R/\mathbb Z$ and $S^1$ are
distinct objects of $\mathbf{Grp}$ related by a distinguished isomorphism; the
identification is available because the comparison is named, not because the objects
coincide.
