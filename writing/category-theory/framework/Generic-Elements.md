# Generic Elements, Hypotheses, and Localization {#sec-generic}

Three pieces of standard mathematics that govern how computed statements are formed: the generic solution of a defining equation, statements with hypotheses, and locality by base change.
None is an evaluation policy; each is a definition or a convention of ordinary mathematical practice, recorded here because computations consume them constantly.

## Generic solutions {#sec-generic-solutions}

::: {#def-generic-solution}
## Generic solution

A defining equation denotes its *generic solution*: the distinguished element of the object the equation presents.
The generic cube root of $2$ is the class of $x$ in $\mathbb Q[x]/(x^3 - 2)$; the generic root of a monic separable polynomial is an element of its étale algebra.
Because the generic solution is a single element, its occurrences are correlated: for $z$ the generic cube root, $z \cdot z^{-1} = 1$ and $z^3 = 2$ identically.
The individual values are the images of the generic solution under the embeddings of the presented object ($\mathbb Q[x]/(x^3-2) \to \mathbb C$, three of them); the *set* of values is the image of the generic solution under all embeddings — a different object, produced by a different question.
:::

A single value is obtained only by naming a morphism out of the presented object:

- **Stated membership** selects the unique compatible image where one exists — the real cube root is the image of the generic root under the unique embedding into $\mathbb R$.

- **A convention** (a principal branch, a sign normalization) is a declared selection, applied at the point of use and recorded on every statement that consumed it; it is a named morphism like any other, changeable without touching the presented object.

The presented object is primary and choice-free; every choice is a named morphism out of it.
This is the same discipline as @sec-witnesses for isomorphisms: existence answers and chosen data are different currencies.

## Hypotheses {#sec-hypotheses}

A computed statement may hold under hypotheses — nonvanishing, convergence, finiteness, flatness, characteristic restrictions, existence of a limit:
$$
\text{statement} \quad \text{provided} \quad C_1, \ldots, C_n.
$$
This is an ordinary implication whose hypotheses are formal propositions: discharged when they follow from memberships in scope ([Elements](Elements-and-Containment.md#sec-elements-containment)), carried on the statement when not.
Hypotheses are part of the statement, not commentary attached to it, and a statement is never displayed stripped of undischarged hypotheses.

A relational hypothesis among already-named objects — $g \circ f = \mathrm{id}$, an equation between named elements — is a formal proposition and may be carried as such.
When the relation is to be *consumed as data* rather than asserted — when later constructions depend on the retraction, not merely on its existence — the named objects are re-sited as a single object of the category of such diagrams (the retraction pair $(f, g, \, g \circ f = \mathrm{id})$ as an object of the category of retraction data), following the master principle that propositions become morphisms one level up ([Presentation Principles](../contributing/Categorical-Presentation-Principles.md#sec-master-principle)). The two forms are the hypothesis-level instance of the existence/data distinction of [Elements and Containment](Elements-and-Containment.md#sec-containment).

## Case decomposition {#sec-case-decomposition}

There is no categorical union of classifiers ([Joins, meets, and closure](Joins-Meets-and-Closure.md#sec-join-meet)), so "the $A$ case or the $B$ case" is not a membership statement about one object.
Case analysis is a family of implications: a stated decomposition of a classifier (the prime $2$ and the odd primes; a stratification by rank), one conditional statement per case (@sec-hypotheses), and the exhaustiveness of the decomposition as a proposition of its own — discharged or carried like any other hypothesis.
Nothing is concluded from an undischarged decomposition.

## Localization {#sec-localization}

A hypothesis is membership; there is no assumption form to localize.
Passage to a local setting is application of the named base-change functor, and the local invariants live on the local object: one does not "work $p$-adically" with $L$, one works with $L \otimes \mathbb Z_p$, an object of its own category reached by a distinguished 1-cell ([Distinguished Functors](Distinguished-Functors.md#sec-distinguished-functors)), and statements proved there are statements about $L \otimes \mathbb Z_p$.
Transferring a local statement back along the base change is a descent claim, stated and discharged as one — never an effect of closing a scope.
The genus construction is the worked instance: local profiles are read off the base changes, and the global-to-local comparison is the $\pi_0$ fiber-sequence machinery of [Categorical Foundations](Categorical-Foundations.md#sec-pi0-fiber).
