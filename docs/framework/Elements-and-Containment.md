# Elements and Containment {#sec-elements-containment}

Elementhood and containment are category-relative notions, and each is a definition, not a convention of reading: an element is a morphism from a corepresenting object, a subobject is a carried monomorphism, and set-level containment is containment of images under the distinguished underlying-set factorization.
The statement $x \in C$ therefore has several inequivalent meanings, each defined below, and which one is in force is determined by what stands on the right-hand side: a category ($X \in \mathcal C$: an object), a classifier domain ($X \in \mathcal C.A$: a lift, per @prp-membership-proposition), or an object ($x \in X$: an element, per @def-element-functor and @def-generalized-element).
Hom-objects are objects like any other: $f \in \operatorname{Hom}_{\mathcal C}(X, Y)$ is elementhood in the hom-set, and the arrow declarations $f \colon X \to Y$, $\alpha \colon F \Rightarrow G$ denote exactly this membership.

## Elements {#sec-elements}

::: {#def-element-functor}
## Element functor

Let $\mathcal C$ be a category of the base diagram with distinguished underlying-set
factorization $U \colon \mathcal C \to \mathbf{Set}$
([Framework](Mathematical-Framework.md#sec-base-graph)). When $U$ is corepresentable,
its corepresenting object $P$ is part of the presentation of $\mathcal C$, via a
specified natural isomorphism $U \cong \operatorname{Hom}_{\mathcal C}(P, -)$. An
*element* of $X \in \mathcal C$ is a morphism $P \to X$; the notation $x \in X$ denotes
exactly this, and every operation on elements is an operation on such morphisms.

| $\mathcal C$ | corepresenting object $P$ |
|---|---|
| $\mathbf{Set}$ | the singleton $\ast$ |
| $\mathbf{Grp}$ | $\mathbb Z$ |
| $\operatorname{Mod}_R$ | $R$ |
| $\mathbf{CommRing}$ | $\mathbb Z[x]$ |
:::

The corepresenting object is declared, never derived from the terminal object: in $\mathbf{Grp}$ the trivial group is a zero object, so $\operatorname{Hom}_{\mathbf{Grp}}(1, G)$ is a singleton for every $G$, while the elements of $G$ are $\operatorname{Hom}_{\mathbf{Grp}}(\mathbb Z, G)$.

::: {#def-generalized-element}
## Generalized element

When the underlying-set factorization of $\mathcal C$ is not corepresentable by a
single object — relative schemes are the standing example — an element of
$X \in \mathcal C$ is a *generalized element* [@nlab:generalized_element]: an object $(T, \, x \in X(T))$ of
the category of elements [@nlab:category_of_elements] of the functor of points of
$X$. The
statement $x \in X$ denotes a generalized element; $x \in X(T)$ names its stage. Every
statement depending on a generalized element carries the stage it depends on. The
points of the underlying topological space $|X|$ form a different object, reached by
the underlying-space functor, and are written as membership in $|X|$.
:::

::: {#prp-membership-proposition}
## Membership in a classifier is a proposition exactly in the property case

For a classifier $\iota_A \colon \mathcal C.A \to \mathcal C$
([Framework](Mathematical-Framework.md#sec-axiom-classifiers)), the statement
$X \in \mathcal C.A$ — the point naming $X$ lifts through $\iota_A$ — is a proposition
if and only if $A$ is a property: $\iota_A$ full and faithful, the fiber over each
object empty or contractible. When $A$ is structure, the fiber is a groupoid of
inequivalent lifts and a truth value is the wrong shape of answer: the content of
"membership" is the fiber itself, presented through its named lifts
([Style Guide P4](../contributing/Mathematical-Language-Style-Guide.md#sec-governing-principles)).
:::

Because there is no categorical union of classifiers ([Framework](Mathematical-Framework.md#sec-intersection)), there is no membership statement for a disjunction of axioms; case decompositions are handled at the level of statements ([Generic Elements](Generic-Elements.md#sec-case-decomposition)).

## Containment {#sec-containment}

::: {#def-subobject-relation}
## Subobject

A *subobject* of $M \in \mathcal C$ is an object $N$ together with a carried
monomorphism $N \to M$ in $\mathcal C$; the relation is written $N \le M$ and its
content is the carried morphism, not a property of $N$ alone. Every operation on
subobjects — primitivity, saturation, orthogonal complement — consumes the carried
monomorphism. For a bare object $N$ with no carried monomorphism, $N \le M$ is not a
statement; the neighboring existence question is @def-embedding-existence.
:::

::: {#def-underlying-containment}
## Underlying containment

For $A$ and $B$ admitting a common base $\mathcal E$ — their Meet along distinguished
factorizations ([Distinguished Functors](Distinguished-Functors.md#sec-resolution-site)) —
the *underlying containment* $A \subseteq B$ is containment of the images of $A$ and
$B$ under the composites to $\mathcal E$ followed by its underlying-set factorization.
The relation is a statement about those images, and it is stated — and displayed —
together with $\mathcal E$ and the factorizations used.
:::

::: {#def-embedding-existence}
## Embedding existence

The question "does a monomorphism $A \to B$ exist" is the nonemptiness of the relevant
set of monomorphisms — in the isomorphism-onto-a-subobject form, nonemptiness of a
torsor of isomorphisms [@nlab:torsor]. It is a genuine proposition with genuine
obstructions (cardinality, rank, form invariants), and it is distinct from both
@def-subobject-relation (which asserts carried data) and @def-underlying-containment.
A negative answer contradicts no carried subobject elsewhere, and a positive answer
yields a subobject only by naming a chosen monomorphism
([Identification](Identification.md#sec-witnesses)).
:::

## Well-formedness {#sec-containment-wf}

A containment relation is defined only where its terms admit a common category along distinguished factorizations.
Where none exists the expression is not a statement, and the defect is the absence of the factorization — a different failure from falsity, which requires evaluation in a named category.
With $L \in \mathbf{Lat}_{\mathbb Z}$, $v \in L$, and the distinguished base change $-\otimes_{\mathbb Z}\mathbb R$:

| expression | status |
| --- | --- |
| $v \in L$ | true — an element (@def-element-functor) |
| $\mathbb Z v \le L$ | true with its carried inclusion — a rank-one subobject |
| $\mathbb R v \le L$ | not a statement — $\mathbb R v$ is not an object of $\mathbf{Lat}_{\mathbb Z}$ |
| $\mathbb R v \subseteq L$ | false, evaluated in $L \otimes \mathbb R$: the image of $L$ contains no line |
| $\mathbb R v \le L \otimes \mathbb R$ | true with its carried inclusion of subspaces |
| $\mathbb R_{\ge 0} v \in L \otimes \mathbb R$ | not a statement — a cone is not an element; $\mathbb R_{\ge 0} v$ is a polyhedral cone in the $\mathbb R$-vector space $L \otimes \mathbb R$ |

Evaluation after transport is governed by the single asymmetry of [Distinguished Functors](Distinguished-Functors.md#sec-statements-vs-constructions): a statement may be evaluated after passage along distinguished factorizations and then carries its category of evaluation; a construction never passes silently.
