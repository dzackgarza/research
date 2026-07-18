# Mathematical Framework

The definitions and results that situate the Sage → Lean category conversion, in
dependency order. This is the framework that situates the conversion; it is mathematics,
not procedure. It is the single source for the classifier / transport / intersection
machinery; the detailed object-level theory (forms, lattices, the discriminant package)
is developed in [Mathematical Definitions](Mathematical-Definitions.md), the reader-facing
conventions that govern how to read every definition are the master rulings
[A1](Settled-Mathematical-Rulings.md#a1)–[A5](Settled-Mathematical-Rulings.md#a5), and the
authoring discipline is [Categorical Presentation Principles](../contributing/Categorical-Presentation-Principles.md).

Ambient conventions: $\mathbf{Cat}$ is the (2-)category of 1-categories, functors, natural
transformations. Every 1-category $\mathcal C$ has a nerve [@nlab:nerve] $N\mathcal C$, a
simplicial set that is an $\infty$-category (quasi-category [@nlab:quasi-category], inner
horns fill); it is a Kan complex [@nlab:kan_complex] iff $\mathcal C$ is a groupoid. All
constructions are taken up to equivalence ([A4](Settled-Mathematical-Rulings.md#a4)).

## Axiom classifiers {#sec-axiom-classifiers}

::: {#def-axiom-classifier}
## Axiom classifier

An *axiom classifier* on a category $\mathcal C$ is a functor
$\iota_A \colon \mathcal C.A \to \mathcal C$. The domain $\mathcal C.A$ is a category
defined by diagrammatic conditions (equations, existence of specified limits, commuting
diagrams); $\iota_A$ is the forgetful functor to the underlying category. An object of
$\mathcal C$ "satisfies $A$" iff the point it names, $\mathbf 1 \to \mathcal C$, lifts
through $\iota_A$.

There is no primitive notion of "underlying set," "predicate on objects," or
$\mathrm{Ob}(\mathcal C)/{\cong}$. All content is carried by the functor $\iota_A$ and its
properties.
:::

::: {#def-property-structure-stuff}
## Property, structure, stuff

The character of $A$ is read off $\iota_A$, following the stuff / structure / property
trichotomy [@BS07, §2; @nlab:stuff_structure_property]:

- $\iota_A$ full and faithful (equivalently, a replete full subcategory) $\Rightarrow$ $A$
  is a *property*; the fiber of $\iota_A$ over each object is empty or contractible, so
  "satisfies $A$" is a proposition and the lift is unique when it exists.
- $\iota_A$ faithful but not full $\Rightarrow$ $A$ is *structure*; fibers are (possibly
  nontrivial) groupoids of chosen structures, and a category may admit several distinct
  lifts (e.g. several monoidal structures on the same underlying category).
- $\iota_A$ general $\Rightarrow$ *stuff*.

The trichotomy is computed, never declared. The property case is the one where the
classifier behaves like a subcategory inclusion.
:::

::: {#def-transport-property}
## Transport of a property

For $F \colon \mathcal C \to \mathcal D$ and a classifier
$\iota_A \colon \mathcal D.A \to \mathcal D$, the induced classifier on $\mathcal C$ is the
pullback
$$
\mathcal C.A \;:=\; \mathcal C \times_{\mathcal D} \mathcal D.A \longrightarrow \mathcal C.
$$
In the property case this is the inverse image of the full subcategory: the full
subcategory of $\mathcal C$ on objects $X$ with $F X$ satisfying $A$. A property is
declared once, at the base category through which it factors, and pulled back everywhere
else ([A3](Settled-Mathematical-Rulings.md#a3)); a property not invariant under
isomorphism does not define a classifier.
:::

## The base graph and its towers {#sec-base-graph}

The named base categories carry only the **adjacent forgetful functors**; every other
functor between them is a composite. The forgetful chains
$$
R\text{-}\mathbf{Mod} \to \mathbf{Ab} \hookrightarrow \mathbf{Grp} \to \mathbf{Mon} \to
\mathbf{Mag} \to \mathbf{Set}, \qquad \mathbf{CommRing} \to \mathbf{Ab}, \ \dots
$$
are the towers. An axiom constraining an operation is owned at the lowest category in
which that operation is present (commutativity at $\mathbf{Mag}$, not at $\mathbf{Ring}$)
and pulled up by @def-transport-property. Whether a property transports is exactly whether
its predicate factors through the relevant forgetful; finite generation, freeness, and
torsion do not transport (they are structure-relative) and are owned at their structured
nodes.

$\mathbf{Mag}$ itself is the category of elements [@nlab:category_of_elements] of the
binary-operation presheaf $X \mapsto \mathrm{Hom}(X \times X, X)$ on $\mathbf{Set}$; the
tower bottoms out in Grothendieck constructions [@nlab:grothendieck_construction] over
$\mathbf{Set}$. Structure-on-an-object (a magma structure on a set: a lift of
$\mathbf 1 \to \mathbf{Set}$) and structure-on-a-category (an abelian structure on a
category: a lift of $\mathbf 1 \to \mathbf{Cat}$) are the same construction at successive
levels. The object-level realization of this graph — the module, form, and lattice
categories — is developed in [Mathematical Definitions](Mathematical-Definitions.md).

## Categorical intersection {#sec-intersection}

::: {#def-classifier-intersection}
## Intersection of classifiers

For classifiers $\iota_A \colon \mathcal C.A \to \mathcal C$ and
$\iota_B \colon \mathcal C.B \to \mathcal C$ their intersection is the pullback in
$\mathbf{Cat}$
$$
\mathcal C.A \times_{\mathcal C} \mathcal C.B \longrightarrow \mathcal C,
$$
the category of objects carrying both structures compatibly. It is again a classifier.
Iterating gives the intersection of any finite family.
:::

::: {#thm-intersection-terminal-cone}
## Intersection is the terminal cone

The intersection is the terminal cone over the cospan
$\mathcal C.A \to \mathcal C \leftarrow \mathcal C.B$ — equivalently the product in the
slice $\mathbf{Cat}_{/\mathcal C}$ [@nlab:over_category]. Its universal property (unique
compatible functor from any other category-with-both-structures) is what pins it uniquely;
this is why it must be *taken as a limit* to define a named category, and why merely
supplying two structure functors out of a category does not identify the intersection (a
strictly smaller category can carry both functors — e.g. "groups of order 2" maps to both
$\mathbf{Grp}$ and finite sets but is not the finite groups).
:::

::: {#thm-intersection-welldefined}
## Well-definedness

The pullback is invariant under equivalence of its legs when the legs are isofibrations
[@nlab:isofibration]. Replete full inclusions are isofibrations, so intersection of
*property* classifiers is well-defined up to equivalence as written, and strict pullback
agrees with pseudo-pullback there. For *structure* classifiers (non-full legs) the
pseudo-pullback [@nlab:2-pullback] is the correct construction. The general form of this
correction — why "up to equivalence" forces the isofibration/pseudo-pullback machinery —
is established in [Categorical Foundations](Categorical-Foundations.md#sec-pullback-cat).
:::

**There is no categorical union of classifiers.** "Carries an $A$- or $B$-structure" is a
disjunction with no classifier realization: a classifier carries no decomposition of its
axiom into removable pieces, so there is no operation on $\iota_A, \iota_B$ returning it.
(The coproduct $\mathcal C.A \sqcup \mathcal C.B \to \mathcal C$ tags objects by which
structure they carry and is not a subcategory-defining classifier; it is not this either.)

## SageCat and its limit-closure {#sec-sagecat}

::: {#def-sagecat}
## SageCat

$\mathbf{SageCat}$ is the (2-)category whose objects are the named categories together with
their axiom classifiers $\mathcal C.A \to \mathcal C$, and whose morphisms are the
forgetful/inclusion functors generated by parent relationships and axiom imposition,
together with a functor $\mathbf{SageCat} \to \mathbf{Cat}$. Axioms are identified by $A$
("Finite") or by $\mathcal C.A$ ("finite sets"); the label is an implementation
identifier, not a mathematical object. The concrete inventory of these categories, axioms,
and constructions is [Sage's category framework](../sage/Sage-Category-Framework-Inventory.md).
:::

::: {#def-limit-closure}
## Limit-closure

$\overline{\mathbf{SageCat}}$ is the closure of $\mathbf{SageCat}$ under the finite limits
of @sec-intersection — the categorical intersections of forgetful-closed finite diagrams.
It is the collection of categories Sage can support, freely extensible by manual
definitions.
:::

::: {#thm-sagecat-connectivity}
## Connectivity and weak contractibility

$\overline{\mathbf{SageCat}}$ has a terminal object, $\mathbf{Objects}()$ — every category
in the Sage system has a (unique) functor to it, since participation means being a
subcategory of $\mathbf{Objects}()$. Consequently:

- $\overline{\mathbf{SageCat}}$ is *connected*: no disjoint component is possible.
- $\overline{\mathbf{SageCat}}$ is *weakly contractible*:
  $\pi_*(\overline{\mathbf{SageCat}}) = 0$, because the terminal object makes the structure
  map $\overline{\mathbf{SageCat}} \to *$ a weak homotopy equivalence
  [@nlab:weak_homotopy_equivalence] (the natural transformation
  $\mathrm{id} \Rightarrow \mathrm{const}_{\mathbf{Objects}()}$ realizes to a contracting
  homotopy). Equivalently $\lvert N\overline{\mathbf{SageCat}}\rvert \simeq *$ [@nlab:nerve].
:::

**Weak contractibility is not categorical triviality.** $\overline{\mathbf{SageCat}}$ is
*not* equivalent as an $\infty$-category to the point $\Delta^0$: categorical equivalence
preserves the non-invertible forgetful functors, which $\Delta^0$ lacks. The distinction is
weak homotopy equivalence (holds; inverts/ignores directionality) versus categorical
equivalence (fails; preserves it). All the substantive content — the intersections above,
and the missing colimits — lives in the directed structure that $\pi_*$ discards, so
@thm-sagecat-connectivity is a connectivity statement only.

## Join and Meet {#sec-join-meet}

::: {#def-join-diagram}
## Join of a diagram

For a finite diagram $D$ in $\mathbf{Cat}$, $\mathrm{Join}(D) := \lim D$. For $D$ the
forgetful-closed diagram on classifiers $\{\mathcal C.A_i \to \mathcal C\}$,
$\mathrm{Join}(D)$ is their categorical intersection (@sec-intersection): the terminal
cone, the universal category satisfying the conjunction of the $A_i$ compatibly with all
forgetfuls.
:::

::: {#def-meet-diagram}
## Meet of a diagram

For the same diagram, $\mathrm{Meet}(D) := \mathrm{colim}\, D$, the initial cocone —
dually, $\mathrm{Meet}_{\mathbf{Cat}}(D) = (\lim_{\mathbf{Cat}^{op}} D^{op})^{op}$. Because
$D$ carries the forgetful functors, this colimit is the finest category through which all
the constituents factor — their common base / shared-structure category (e.g. the colimit
of the group and additive-monoid forgetful diagrams is $\mathbf{Set}$).
:::

::: {#thm-sagejoin}
## SageJoin

$\mathrm{SageJoin}(\{A_i\}) = \mathrm{Join}(D) = \lim D$. This is realizable in
$\overline{\mathbf{SageCat}}$: computing it adds one object — the limit apex — which
$\mathbf{Cat}$ always provides; it may coincide with an object already present. Two caveats
intrinsic to a blind conjunction: the result may be *empty* (the construction does not
check inhabitation), and it may be a *strict super-category* of the true intersection when
a needed inclusion is not present in $\mathbf{SageCat}$ (a conservative over-approximation).
`JoinCategory` is this limit; the name "join" is a documented misnomer for the categorical
meet-by-inclusion and collides with the topological join $C \star C'$
[@nlab:join_of_categories].
:::

::: {#thm-sagemeet}
## SageMeet

$\mathrm{SageMeet}$ *intends* $\mathrm{Meet}(D) = \mathrm{colim}\, D$, but takes the colimit
**in $\mathbf{SageCat}$**. The obstruction: $\mathbf{SageCat}$ is not cocomplete, and
$\overline{\mathbf{SageCat}}$ is closed under the @sec-intersection limits but *not* under
these colimits. So the colimit apex generally cannot be produced; Sage instead returns the
finest common super-category *already in the graph* — the greatest lower bound in the poset
of existing classifiers — which is a coarser object through which the true cocone factors
(an over-approximation on the colimit side, mirroring @thm-sagejoin). When no such node
exists the operation is undefined (`meet([])`, the empty colimit / initial object, is
absent).
:::

::: {#thm-join-meet-asymmetry}
## The asymmetry

Join and Meet are dual (co)limits over one forgetful-commuting diagram. The sole asymmetry
is realizability: $\overline{\mathbf{SageCat}}$ is closed under the limits but not the
colimits, so joins are *constructed* (add the limit apex) and meets are *searched for*
(traverse the existing graph). The realization gap on each side is Sage's documented "the
intersection might not be constructible."
:::

## Consequences for conversion {#sec-conversion-consequences}

Each Sage category maps to a Lean/Mathlib target through @sec-axiom-classifiers–@sec-join-meet,
in one of three registers:

- **Named Mathlib category present** ($\mathbf{Set}$, $\mathbf{Top}$, $\mathbf{Grp}$,
  $R\text{-}\mathbf{Mod}$, …): map directly. Equivalence is inherited from Mathlib's
  hierarchy; nothing is modeled as an intersection.
- **Base and axioms present, combination absent:** the category is the iterated pullback of
  its axiom classifiers (@sec-intersection), defined once per axiom and composed by
  transport (@def-transport-property). No bespoke class, hence no
  `pullback ≃ MathlibClass` obligation — the pullback *is* the definition.
- **Cross-tower combination absent from Mathlib** ($\mathrm{Mod}_{\mathbb Q} \wedge
  \mathbf{Semigroups}$ and the like): construct the intersection by hand (@sec-intersection),
  and record membership of a concrete object by supplying its structure functors and the
  commuting square (@thm-intersection-terminal-cone), leaving "satisfies the conjunction" a
  theorem rather than a definition.

SageJoins are constructions (@thm-sagejoin), carrying an equivalence obligation where a
Mathlib class coincides, a nonemptiness obligation where inhabitation matters, and a
fidelity obligation that the limit is the true intersection and not a missing-inclusion
over-approximation. SageMeets (@thm-sagemeet) are never construction targets: each is a
factorization through an existing coarser classifier — a discharged inclusion in the
Mathlib hierarchy, computed by instance resolution, never a colimit to build. Where the
true colimit is absent from Mathlib, that is recorded as a Sage-side over-approximation,
not reproduced as truth. The routing discipline this implies — wrap-first, contribute
upstream, synthetic only as a last resort — is the [Lean–Sage Integration Model](../lean/Lean-Sage-Integration-Model.md).

The invariants and functors of the objects being classified follow the same discipline:
$\mathrm{Aut}\colon \mathrm{Core}(\mathcal C) \to \mathbf{Grp}$ is a single generic functor
whose instances (orthogonal groups, unit groups) are never separate objects
([A2](Settled-Mathematical-Rulings.md#a2)); comparisons between constructions are natural
transformations (whiskerings), not edges; a construction functorial only for isomorphisms
is sited on $\mathrm{Core}$; an invariant is a function on $\pi_0$ of the core, and the
truncation level (set-level vs. groupoid-level, $\pi_0$ vs. homotopy pullback) is stated
wherever it is content ([A5](Settled-Mathematical-Rulings.md#a5),
[Categorical Foundations](Categorical-Foundations.md#sec-pi0-fiber)).
