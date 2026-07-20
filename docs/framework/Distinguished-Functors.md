# Distinguished Functors {#sec-distinguished-functors}

The generated 2-diagram of the base categories carries, beyond the classifier pullbacks of the [Framework](Mathematical-Framework.md#sec-base-graph), the machinery that makes mixed expressions meaningful: distinguished factorizations, the discipline for parallel functors, and the common-base (Meet) resolution of cross-category operations.
Declared 1-cells are adjacent forgetful functors only; every other functor is generated — a composite, an inverse image, a Grothendieck construction, or an induced/whiskered functor, marked as generated ([Presentation Principles](../contributing/Categorical-Presentation-Principles.md#sec-generation-discipline)). Identity of categories in the diagram is identity of declared objects of the presentation; no construction tests equivalence of categories to locate an expression, and the equivalences that matter (commutativity of $R$ identifying left and right modules) are declared, hypothesis-bearing 1-cells like any other.
The discrete embedding $\mathbf{Set} \to \mathbf{Cat}_1$ is one of the declared 1-cells: where a categorical context consumes a set, the set passes through it as through any distinguished functor, so ordinary set-theoretic statements coexist with the categorical ones without a separate regime.

::: {#def-distinguished-factorization}
## Distinguished factorization

For each category of the diagram, the *distinguished underlying-set factorization* is
the named composite of adjacent forgetfuls to $\mathbf{Set}$ — for modules the additive
composite $\operatorname{Mod}_R \to \mathbf{Ab} \to \mathbf{Grp} \to \mathbf{Set}$.
Element functors ([Elements](Elements-and-Containment.md#sec-elements)) and underlying
containment ([Elements](Elements-and-Containment.md#sec-containment)) read through this
factorization. More generally, wherever parallel functors coexist, exactly one
factorization per purpose is distinguished; the others remain available by name.
:::

## Parallel functors {#sec-parallel-functors}

Two functors with common source and target stand in exactly one of three declared relations:

1. **Generated coincidence.** One is defined as the other's composite; they agree by generation.

2. **Named comparison.** Both are present and a commutative square is declared — strict, or up to a specified natural isomorphism, and the statement says which.
   Comparison 2-cells compose along factorizations; this is what makes transport independent of the path chosen ([Identification](Identification.md#sec-canonical-identification)).

3. **Distinct functors.** No comparison is declared because none is true: the multiplicative monoid of a ring and the monoid underlying its additive group are different functors $\mathbf{Ring} \to \mathbf{Mon}$; the two module structures of a bimodule are different functors to $\operatorname{Mod}_R$ and $\operatorname{Mod}_{S^{\mathrm{op}}}$.
   Such functors are kept under distinct names with exactly one distinguished per purpose (for bimodules, the left-module leg).

An expression requiring passage along one of two undistinguished parallel functors is not yet a statement; the defect names both candidates.
An adjunction contributes two directional 1-cells — extension and restriction of scalars — neither inverse to the other; distinguished status is held per direction, and no resolution composes an adjunction into an identity.

## The resolution site {#sec-resolution-site}

::: {#def-resolution-site}
## The resolution site

A mixed expression — an operation or relation whose arguments lie in different
categories — denotes its value at the Meet of the argument categories
([Framework](Mathematical-Framework.md#def-meet-diagram)): the common base reached from
all arguments along the distinguished functors, on which the operation is declared. This
is the searched-for greatest-lower-bound node of the $\overline{\mathbf{SageCat}}$ closure
([Framework](Mathematical-Framework.md#thm-sagemeet)), not a fresh construction. So
$M \otimes N$ with $M \in \operatorname{Mod}_R$, $N \in \mathbf{Ab}$ denotes the tensor
product in $\mathbf{Ab}$ of the images, and $\mathbb R v \subseteq L$ is evaluated in
$L \otimes \mathbb R$
([Elements](Elements-and-Containment.md#sec-containment-wf)). When no node of the closure
declares the operation, the expression is not a statement, and the defect names the
missing declaration ("it is not declared that $\mathcal C$ has products"). When two
incomparable nodes declare it, the expression is not a statement until one is named;
nothing is selected by search order. Numerals follow the same rule: a literal denotes an
element of the Meet its context supplies, fixed by stated membership where context does
not determine it.
:::

## Statements and constructions {#sec-statements-vs-constructions}

The single asymmetry in how the diagram is used:

- A *statement* — a truth-valued or invariant-valued claim — may be evaluated after passage along distinguished factorizations, and is then a claim about the images, stated and displayed together with its category of evaluation and the factorizations used.
  "False, evaluated in $L \otimes \mathbb R$" is a complete answer; "false" is not.

- A *construction* — a definition, a rewriting step, the formation of a new object — is a function of explicitly named data.
  It never passes along a functor silently: it requires the named functor, the named witness ([Identification](Identification.md#sec-witnesses)), or the explicit image ($v \otimes 1$, not $v$).

Statements evaluated after transport carry their context and cannot contaminate later work; constructions become later work, and therefore carry only identifications that were named.

## Axioms through functors {#sec-axioms-through-functors}

The axiom on a category is the pullback of its classifier; the classifying category is the lowest category where the constrained operation exists, and the axiom is pulled back everywhere else ([Framework](Mathematical-Framework.md#sec-base-graph); Settled Rulings [A1](Settled-Mathematical-Rulings.md#a1), [A3](Settled-Mathematical-Rulings.md#a3)); the pullback is strict along property classifiers and pseudo along structure classifiers ([Categorical Foundations](Categorical-Foundations.md#sec-pullback-cat)). Convenience delegation — an invariant of $L \otimes \mathbb Z_p$ exposed as if attached to $L$ — is a named composite through the base-change functor and belongs to the implementation map; each invariant lives where it is defined.
