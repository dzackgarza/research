# Framework

The axiom-classifier and intersection machinery for the Sage → Lean category
conversion, developed inside the [ambient setting](Ambient-Setting.md). The object-level
theory (forms, lattices, the discriminant construction and its exact sequences) is
developed in [Definitions](Mathematical-Definitions.md); the
conventions for reading the definitions are the master rulings
[A1](Settled-Mathematical-Rulings.md#a1)–[A5](Settled-Mathematical-Rulings.md#a5); and the
authoring discipline is [Categorical Presentation Principles](../contributing/Categorical-Presentation-Principles.md).

## The category of elements {#sec-elements-projection}

::: {#def-category-of-elements}
## Category of elements and forgetful functors

For a category $\mathcal C$ and a pseudofunctor $\Phi \colon \mathcal C^{\mathrm{op}} \to
\mathcal M$ into the ambient (@def-ambient-categories) — a presheaf when
$\mathcal M = \mathbf{Set}$, a pseudofunctor to $\mathbf{Cat}_1$ or to spaces when higher —
the *category of elements* $\int_{\mathcal C} \Phi$ has objects $(X, s)$ with
$X \in \mathcal C$ and $s \in \Phi(X)$, and a morphism $(X, s) \to (Y, t)$ is a map
$f \colon X \to Y$ of $\mathcal C$ with $\Phi(f)(t) = s$. Its *projection*
$$
\pi_\Phi \colon \int_{\mathcal C} \Phi \longrightarrow \mathcal C, \qquad (X, s) \mapsto X,
$$
is a Grothendieck opfibration [@nlab:grothendieck_construction], discrete when $\Phi$ is
$\mathbf{Set}$-valued. This projection is the primitive that the informal *forgetful
functor* names: whether $\pi_\Phi$ is faithful, or fully faithful, is a consequence of the
truncation of the fibers $\Phi(X)$ (@def-truncated) — a $\mathbf{Set}$-valued
$\Phi$ makes it faithful, a propositional $\Phi$ fully faithful — never an imposed
condition, and there is no notion of forgetful functor apart from such a projection.
:::

## Axiom classifiers {#sec-axiom-classifiers}

::: {#def-axiom-classifier}
## Axiom

An *axiom* $A$ is a universal fibration $u_A \colon E_A \to B_A$ — the projection
(@def-category-of-elements) of the category of elements of the *classifying pseudofunctor*
$\Phi_A \colon B_A^{\mathrm{op}} \to \mathbf{Cat}_1$, whose value $\Phi_A(X)$ is the space of
$A$-data on $X$. Its *classifying category* $B_A$ is the category on which $A$ is primitively
defined — the limit of the categories on which $A$ could be defined — and its *total
category* $E_A = \int_{B_A} \Phi_A$ is the category of objects of $B_A$ together with a
choice of $A$-data (a lift through $u_A$). It is universal as a universal bundle is: $u_A$
classifies $A$-data, every instance a pullback of it. The *axiom $A$ on a category
$\mathcal C$* — the axiom on the objects of $\mathcal C$ — is the pullback
$\iota_A \colon \mathcal C.A \to \mathcal C$ of $u_A$ along the classifying functor
$c_{\mathcal C} \colon \mathcal C \to B_A$ (equivalently, $\Phi_A$ reindexed along
$c_{\mathcal C}$):

```{.tikz}
%%| filename: axiom-classifier-pullback
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
\mathcal{C}.A \arrow[r] \arrow[d, "\iota_A"'] \arrow[dr, phantom, "\lrcorner", very near start] & E_A \arrow[d, "u_A"] \\
\mathcal{C} \arrow[r, "c_{\mathcal{C}}"'] & B_A
\end{tikzcd}
```

The shorthand $\mathcal C.A = c_{\mathcal C}^{\,*}\, u_A = \mathcal C \times_{B_A} E_A$ thus
names the domain of the classifier over $\mathcal C$; at
$\mathcal C = B_A$ it is $E_A$ itself ($B_A.A = E_A$). It is in turn universal over
$\mathcal C$: each $\mathcal D.A$, for a functor
$\mathcal D \to \mathcal C$, is a further pullback of $\iota_A$. An object of $\mathcal C$
satisfies $A$ iff its point $\mathbf 1 \to \mathcal C$ lifts through $\iota_A$. The class of
$u_A$ (@def-property-structure-stuff) is fixed and preserved by pullback, so $\iota_A$ has
the same class over every $\mathcal C$. There is no primitive notion of "predicate on
objects" or $\mathrm{Ob}(\mathcal C)/{\cong}$: $\Phi_A$ and its universal property are the
whole content.

The classifying category is the level at which the axiom's data first exist: $\mathrm{Finite}$
has classifying category $\mathbf{Set}$ — the level at which cardinality first exists — and
total category $\mathbf{FinSet}$; $\mathbf{Ring}.\mathrm{Finite}$ is the pullback along
$\mathbf{Ring} \to \mathbf{Set}$, and there is no finer one. A *binary operation* has
classifying category $\mathbf{Set}$ and total category
$\mathbf{Mag} = \mathrm{Op}_2 = \int_{\mathbf{Set}} \operatorname{Op}_2$ (@def-operation-categories);
*associativity* has classifying category $\mathbf{Mag}$ and total category
$\mathbf{Semigrp} = \mathbf{Mag}.\mathrm{Assoc}$; *commutativity* has classifying category
$\mathbf{Mag}$ and total category $\mathbf{CMag}$. Axioms accumulate by iterated pullback
(@sec-named-categories): $\mathbf{Mon}$ adjoins to $\mathbf{Semigrp}$ a unit — a nullary
operation, hence structure — and its unit laws, and adjoining commutativity gives
$\mathbf{CMon}$; each added property is an intersection (@sec-intersection) of classifiers
over its classifying category, presented as a sketch
([Truncation](Truncation-and-Classifiers.md#sec-filled-diagrams)).
:::

::: {#def-property-structure-stuff}
## Property, structure, stuff

The *class* of an axiom $A$ on $\mathcal C$ (@def-axiom-classifier) is the truncation level
of its fibers — the space of $A$-data $\Phi_A(X)$ over each object $X$ (@def-truncated),
equivalently the level of $\iota_A$ as a morphism (@def-truncated) [@BS07, §2;
@nlab:stuff_structure_property]. In an $(n,1)$-ambient:

- $A$ is a *property* when the fibers are propositional ($(-1)$-truncated): $\iota_A$ is
  fully faithful — a monomorphism — and $\mathcal C.A \hookrightarrow \mathcal C$ is a
  replete full subcategory;
- $A$ is a *structure* when the fibers are discrete ($(n-1)$-truncated): $\iota_A$ is
  faithful, and the $A$-data is a genuine collection of choices;
- $A$ is *stuff* otherwise: the fibers retain morphisms of their own.

The classes are nested — property $\subseteq$ structure $\subseteq$ stuff — because
$k$-truncated implies $(k+1)$-truncated. The property threshold is absolute at $-1$; the
structure threshold $n-1$ tracks the ambient's dimension, so the same axiom changes class as
the ambient grows (structure over $\mathbf{Set}$ is a set of choices, over $\mathbf{Cat}_1$
a groupoid of them). The class is fixed by $\Phi_A$ and preserved by pullback, hence the
same over every $\mathcal C$, and it is *computed*, never declared.
:::

*Remark.* Uniqueness of the lift is a consequence, not an assumption. In the property case
the fibers are propositional, so "$X$ satisfies $A$" is a proposition and a lift is unique
when it exists; in the structure case the fibers are genuine groupoids and an object may
admit several inequivalent lifts (several monoidal structures on one category), each a
separate witness. This is the $1$-categorical reading of the truncation-theoretic account of
[Truncation, Classifiers, and Filled Diagrams](Truncation-and-Classifiers.md).

::: {#def-subcategory}
## Subcategory

A *subcategory* of $\mathcal C$ is an axiom $A$ on $\mathcal C$ whose classifier $\iota_A$ is
a *property* (@def-property-structure-stuff) — equivalently, whose fibers are propositional,
so $\iota_A \colon \mathcal C.A \to \mathcal C$ is fully faithful and replete and presents
$\mathcal C.A$ as a replete full subcategory. Not every axiom is a subcategory: a *structure*
classifier is faithful but not full, a genuine fibration that adjoins data (the unit of a
monoid, @exm-monoid), and *stuff* keeps morphisms in its fibers — these add to $\mathcal C$
rather than cut it down. The replete full subcategories are exactly the property-case axioms,
which is why the classifier $\iota_A$, not "subcategory," is the primitive: it is defined for
every class, and $\mathbf{Cat}_1$ has no subobject classifier for a monomorphism notion of
subcategory to rest on.
:::

::: {#def-concrete-category}
## Concrete categories and underlying sets

The *concrete categories* are the objects of the closure, under pullback in $\mathbf{Cat}_1$,
of the categories reachable from $\mathbf{Set}$ by axiom classifiers
(@def-axiom-classifier) — the categories of elements built over $\mathbf{Set}$
(@def-category-of-elements) and their iterated pullbacks. Each is therefore a composite of
element-projections, so a concrete category $\mathcal C$ carries a canonical *underlying-set
functor* $U_{\mathcal C} \colon \mathcal C \to \mathbf{Set}$ — the composite projection to
$\mathbf{Set}$ — and the *underlying set* of an object $X$ is $U_{\mathcal C}(X)$. The functor to
$\mathbf{Set}$ is not a separate datum: it is the projection the construction provides, so
"forgetful to $\mathbf{Set}$" and "underlying set" are determined, never chosen.
:::

::: {#def-axiom-through-functor}
## The axiom on a category through a functor

The axiom $A$ on a category is a pullback (@def-axiom-classifier), and pullbacks compose:
for $F \colon \mathcal C \to \mathcal D$, the axiom $A$ on $\mathcal C$ is the pullback along
$F$ of the axiom $A$ on $\mathcal D$ — equally, the pullback of $u_A$ along
$c_{\mathcal D} \circ F = c_{\mathcal C}$:

```{.tikz}
%%| filename: transport-pullback
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
\mathcal{C}.A \arrow[r] \arrow[d] \arrow[dr, phantom, "\lrcorner", very near start] & \mathcal{D}.A \arrow[d, "\iota_A"] \\
\mathcal{C} \arrow[r, "F"'] & \mathcal{D}
\end{tikzcd}
```

with $\mathcal C.A := \mathcal C \times_{\mathcal D} \mathcal D.A$. In the property case it is
the inverse image of the full subcategory: the objects $X$ of $\mathcal C$ with $F X$
satisfying $A$. When $F$ is a forgetful functor, this pullback is the property $A$ read on
$\mathcal C$ exactly when $A$ factors through $F$
([A3](Settled-Mathematical-Rulings.md#a3)); an axiom not invariant under isomorphism does
not define a classifier.
:::

## The named categories as iterated pullbacks {#sec-named-categories}

The named algebraic categories are the classical ones — magmas, semigroups, monoids,
groups, rings — defined in the standard way by axioms on their objects. We recall each
classical definition, stating every axiom first as an equation on elements and then as the
commuting diagram it becomes, and recover the category as a pullback of a universal
classifier (@def-axiom-classifier), drawn as the square it is (@sec-draw-the-square). Two
single-operation towers run in parallel from $\mathbf{Set}$ — a multiplicative one through
$\mathbf{Mag}$ and an additive one through $\mathbf{AddMag}$, the same construction under
two names as distinct parallel functors to $\mathbf{Set}$
([Distinguished Functors](Distinguished-Functors.md#sec-parallel-functors)).

::: {#exm-finite}
## A property over $\mathbf{Set}$: finiteness

$\mathrm{Finite}$ has classifying category $\mathbf{Set}$ —
the level at which cardinality exists — and universal total
$\mathbf{FinSet} = \mathbf{Set}.\mathrm{Finite}$, the replete full subcategory of finite
sets. For any $\mathcal C$ with underlying-set functor $U \colon \mathcal C \to \mathbf{Set}$,
the finite objects of $\mathcal C$ are the pullback of
$\mathbf{FinSet} \hookrightarrow \mathbf{Set}$ along $U$:

```{.tikz}
%%| filename: finite-classifier
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
\mathcal{C}.\mathrm{Finite} \arrow[r] \arrow[d] \arrow[dr, phantom, "\lrcorner", very near start] & \mathbf{FinSet} \arrow[d, hook] \\
\mathcal{C} \arrow[r, "U"'] & \mathbf{Set}
\end{tikzcd}
```

so $\mathbf{FinGrp} = \mathbf{Grp}.\mathrm{Finite}$ and
$\mathbf{FinRing} = \mathbf{Ring}.\mathrm{Finite}$ are instances of the one classifier.
:::

::: {#def-operation-categories}
## The operation categories $\mathrm{Op}_n$

For $n \ge 0$, let $\mathrm{Op}_n := \int_{\mathbf{Set}} \operatorname{Op}_n$ be the category
of elements [@nlab:category_of_elements] of the presheaf
$\operatorname{Op}_n \colon X \mapsto \mathrm{Hom}_{\mathbf{Set}}(X^n, X)$ of $n$-ary
operations: an object is a set with a chosen $n$-ary operation, a morphism a map commuting
with the operations. The forgetful $\mathrm{Op}_n \to \mathbf{Set}$ is faithful and not full,
so an $n$-ary operation is *structure* on a set (@def-property-structure-stuff), its fiber
over $X$ the set $\mathrm{Hom}(X^n, X)$. The low cases are the standard categories:
$\mathrm{Op}_0 = \mathbf{Set}^{\bullet}$ is the pointed sets (a chosen element
$\mathbf 1 \to X$), and $\mathrm{Op}_2$ is the *magmas* — a set with one binary operation —
written $\mathbf{Mag}$ from here on.
:::

::: {#def-operation-axioms}
## Axioms on a binary operation

Let $(X, \mu)$ be a magma, $\mu \colon X \times X \to X$, written $\mu(a, b) = a \cdot b$.
Each axiom is an equation on elements that is the commuting of a diagram built from $\mu$.

*Associativity* is $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a, b, c$ — the
commuting of the square

```{.tikz}
%%| filename: associativity-square
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
X \times X \times X \arrow[r, "\mu \times \mathrm{id}"] \arrow[d, "\mathrm{id} \times \mu"'] & X \times X \arrow[d, "\mu"] \\
X \times X \arrow[r, "\mu"'] & X
\end{tikzcd}
```

*Commutativity* is $a \cdot b = b \cdot a$ — the commuting of

```{.tikz}
%%| filename: commutativity-bigon
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
X \times X \arrow[rr, "\tau"] \arrow[dr, "\mu"'] & & X \times X \arrow[dl, "\mu"] \\
& X &
\end{tikzcd}
```

with $\tau(a, b) = (b, a)$ the swap. Each such diagram is a pair of parallel composites
$X^{\times k} \rightrightarrows X$ built from $\mu$, and the axiom it names is the classifier
$\mathbf{Mag}.A \to \mathbf{Mag}$ whose fiber over $(X, \mu)$ is the space of *fillers* —
witnesses that the two composites agree (@def-axiom-classifier). So associativity is the full
subcategory $\mathbf{Mag}.\mathrm{Assoc}$ of $\mathbf{Mag}$ where
$\mu(\mu \times \mathrm{id}) = \mu(\mathrm{id} \times \mu)$, and commutativity the full
subcategory $\mathbf{Mag}.\mathrm{Comm}$ where $\mu = \mu\tau$ — each the equalizer of two
composite operations. Over $\mathbf{Set}$ the filler space is propositional (the composites
agree or not), so the *class* of each is *property* (@def-property-structure-stuff) —
computed, not stipulated; in a higher ambient the fillers form the space whose truncation
level is the class ([Truncation](Truncation-and-Classifiers.md#sec-filled-diagrams)).
:::

::: {#def-semigroup-monoid}
## Semigroups and monoids

A *semigroup* is a magma satisfying associativity; $\mathbf{Semigrp}$ is the category of
semigroups and magma homomorphisms. A *monoid* $(X, \mu, \eta)$ is a semigroup with a chosen
*unit* — a nullary operation $\eta \colon \mathbf 1 \to X$ with value $e = \eta(\ast)$ —
satisfying the *unit laws* $e \cdot a = a = a \cdot e$, the commuting of

```{.tikz}
%%| filename: unit-laws
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
\mathbf 1 \times X \arrow[r, "\eta \times \mathrm{id}"] \arrow[dr, "\lambda"'] & X \times X \arrow[d, "\mu"] & X \times \mathbf 1 \arrow[l, "\mathrm{id} \times \eta"'] \arrow[dl, "\rho"] \\
& X &
\end{tikzcd}
```

with $\lambda \colon \mathbf 1 \times X \xrightarrow{\sim} X$ and
$\rho \colon X \times \mathbf 1 \xrightarrow{\sim} X$ the projections. A *monoid
homomorphism* preserves $\mu$ and $\eta$; $\mathbf{Mon}$ is the category of monoids and these
maps. The unit is data that morphisms respect, not a property of the underlying semigroup
(@exm-monoid).
:::

*Remark (the unit, categorified).* The unit is *structure*, and its shape is clearest one
level up. A unit for a functor $\otimes \colon \mathcal C \times \mathcal C \to \mathcal C$
is a unit object $I$ with unitors that are natural *isomorphisms*
$\lambda_A \colon I \otimes A \xrightarrow{\sim} A$ and
$\rho_A \colon A \otimes I \xrightarrow{\sim} A$. Without an associator the unit laws reduce
to the single compatibility $\lambda_I = \rho_I \colon I \otimes I \to I$,

```{.tikz}
%%| filename: unit-coherence
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
I \otimes I \arrow[r, "\lambda_I"] \arrow[d, "\mathrm{id}"'] & I \arrow[d, "\mathrm{id}"] \\
I \otimes I \arrow[r, "\rho_I"'] & I
\end{tikzcd}
```

whose sides are identities — the only condition linking the two unitors. On an object the
unitors are equalities and this square is the pair of unit laws above; on a category they
are isomorphisms and it is their coherence: the same nullary-operation structure at
successive levels ([Truncation](Truncation-and-Classifiers.md#sec-worked-examples)).

::: {#def-group}
## Groups

A *group* is a monoid in which every element has an inverse — a unary operation
$\nu \colon X \to X$, $\nu(a) = a^{-1}$, with $a \cdot a^{-1} = e = a^{-1} \cdot a$, the
commuting of

```{.tikz}
%%| filename: inverse-law
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
X \arrow[r, "\varepsilon"] \arrow[d, "{(\mathrm{id},\,\nu)}"'] & \mathbf 1 \arrow[d, "\eta"] \\
X \times X \arrow[r, "\mu"'] & X
\end{tikzcd}
```

with $\varepsilon \colon X \to \mathbf 1$ and $(\mathrm{id}, \nu) \colon X \to X \times X$,
$a \mapsto (a, a^{-1})$ (and its mirror for the left inverse). The inverse is unique when it
exists and is preserved by every monoid homomorphism, so *invertibility* is a property of a
monoid; $\mathbf{Grp}$ is the replete full subcategory of invertible monoids.
:::

::: {#exm-single-op}
## The classifying category: semigroups and commutative magmas

$\mathbf{Mag}$ is the base $B_A$ of every
axiom $A$ constraining a single binary operation: the most general category on which such an
$A$ is a well-formed predicate. Its classifier square at $\mathcal C = \mathbf{Mag} = B_A$
has classifying functor $c \simeq \mathrm{id}$, so both horizontals are equivalences and the
classifier over $\mathbf{Mag}$ is the universal total itself:

```{.tikz}
%%| filename: universal-base-square
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
\mathbf{Mag}.A \arrow[r, "\sim"] \arrow[d, "\iota_A"'] \arrow[dr, phantom, "\lrcorner", very near start] & E_A \arrow[d, "u_A"] \\
\mathbf{Mag} \arrow[r, "\sim"'] & B_A
\end{tikzcd}
```

The classical semigroups and commutative magmas (@def-semigroup-monoid,
@def-operation-axioms) are these universal totals: associativity and commutativity are
properties over $\mathbf{Mag}$, so
$$
\mathbf{Semigrp} = \mathbf{Mag}.\mathrm{Assoc} = E_{\mathrm{Assoc}}, \qquad
\mathbf{CMag} = \mathbf{Mag}.\mathrm{Comm} = E_{\mathrm{Comm}}.
$$
:::

::: {#exm-commutative-semigroup}
## Commutative semigroups

Axioms over a common classifying category combine by intersection (@def-classifier-intersection).
Commutative semigroups are the intersection of the two properties over $\mathbf{Mag}$:

```{.tikz}
%%| filename: commutative-semigroup
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
\mathbf{CSgrp} \arrow[r] \arrow[d] \arrow[dr, phantom, "\lrcorner", very near start] & \mathbf{CMag} \arrow[d, hook] \\
\mathbf{Semigrp} \arrow[r, hook] & \mathbf{Mag}
\end{tikzcd}
```

Both legs are replete full inclusions, so
$\mathbf{CSgrp} = \mathbf{Semigrp} \times_{\mathbf{Mag}} \mathbf{CMag}$ is again a full
subcategory of $\mathbf{Mag}$; the bottom-right corner is the shared classifying category $\mathbf{Mag}$.
:::

::: {#exm-monoid}
## Monoids: the unit as structure

A two-sided unit is unique when it
exists, so "unital" is a proposition on objects; but a monoid homomorphism must *preserve*
the unit, and preservation is not automatic — the map from the one-element monoid to
$(\mathbb Z, \times)$ sending the point to $0$ is a semigroup homomorphism that misses the
unit. So the forgetful $\mathbf{Mon} \to \mathbf{Semigrp}$ is faithful and not full: the
unit is *structure*. It enters as a nullary operation $e \colon \mathbf 1 \to X$ — the
classifier $\mathbf{Set}^{\bullet} = \int_{\mathbf{Set}} \operatorname{Op}_0$ of *pointed
sets* over $\mathbf{Set}$ — adjoined to semigroups by the pullback

```{.tikz}
%%| filename: unit-structure
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
\mathbf{Semigrp}^{\bullet} \arrow[r] \arrow[d] \arrow[dr, phantom, "\lrcorner", very near start] & \mathbf{Set}^{\bullet} \arrow[d] \\
\mathbf{Semigrp} \arrow[r, "U"'] & \mathbf{Set}
\end{tikzcd}
```

Monoids are then the property, over these pointed semigroups, that $e$ is a two-sided
identity: $\mathbf{Mon} = \mathbf{Semigrp}^{\bullet}.\mathrm{UnitLaws}$. The unit laws are
sited over $\mathbf{Semigrp}^{\bullet}$, not over $\mathbf{Mag}$ — structure moves the classifying category.
:::

::: {#exm-group}
## Groups

In a monoid an inverse is unique when it exists, and a
monoid homomorphism between groups preserves it automatically, so *invertibility* is a
property: $\mathbf{Grp} = \mathbf{Mon}.\mathrm{Inverse}$, a replete full subcategory of
$\mathbf{Mon}$. Commutative groups are $\mathbf{Ab} = \mathbf{Grp}.\mathrm{Comm}$, written
additively along the parallel tower through $\mathbf{AddMag}$.
:::

::: {#exm-ring}
## Rings: two operations

A ring has an additive and a multiplicative operation on one set, so its classifying category
is the pullback of the two single-operation towers over their common $\mathbf{Set}$:

```{.tikz}
%%| filename: ring-two-operations
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
\mathbf{AddMag} \times_{\mathbf{Set}} \mathbf{Mag} \arrow[r] \arrow[d] \arrow[dr, phantom, "\lrcorner", very near start] & \mathbf{Mag} \arrow[d, "U_\cdot"] \\
\mathbf{AddMag} \arrow[r, "U_+"'] & \mathbf{Set}
\end{tikzcd}
```

On the apex — a set with two operations — the additive-group and multiplicative-semigroup
axioms are properties, and *distributivity* is the first axiom depending on both, sited
there and on neither tower:
$$
\mathbf{Rng} = \big((\mathbf{AddMag} \times_{\mathbf{Set}} \mathbf{Mag}).(\mathrm{AbGp}_{+}
\wedge \mathrm{Sgp}_{\cdot})\big).\mathrm{Distrib},
$$
with $\mathbf{Ring} = \mathbf{Rng}.\mathrm{Unital}_{\cdot}$ adjoining a multiplicative unit
(structure again) and $\mathbf{CRing} = \mathbf{Ring}.\mathrm{Comm}_{\cdot}$. The SageMeet /
SageJoin realizability caveats (@thm-sagejoin, @thm-sagemeet) bite exactly at this
cross-tower step, where Sage records the combination as a join.
:::

Each named category is thus an iterated pullback of classifiers; the table indexes each by
the square it is the apex of.

| category | classifying category of the added axiom(s) | construction |
|---|---|---|
| $\mathbf{FinSet}$ | $\mathbf{Set}$ | $\mathbf{Set}.\mathrm{Finite}$ |
| $\mathbf{CountSet}$ | $\mathbf{Set}$ | $\mathbf{Set}.\mathrm{Countable}$ |
| $\mathbf{Mag}$ (magmas) | $\mathbf{Set}$ | $\int_{\mathbf{Set}} \operatorname{Op}_2$ |
| $\mathbf{Semigrp}$ | $\mathbf{Mag}$ | $\mathbf{Mag}.\mathrm{Assoc}$ |
| $\mathbf{Mon}$ | $\mathbf{Semigrp}^{\bullet}$ | $\mathbf{Semigrp}^{\bullet}.\mathrm{UnitLaws}$ |
| $\mathbf{CMon}$ | $\mathbf{Mag}$ | $\mathbf{Mon} \times_{\mathbf{Mag}} \mathbf{CMag}$ |
| $\mathbf{Grp}$ | $\mathbf{Mon}$ | $\mathbf{Mon}.\mathrm{Inverse}$ |
| $\mathbf{Ab}$ | $\mathbf{Grp}$ | $\mathbf{Grp}.\mathrm{Comm}$ (additive) |
| $\mathbf{Rng}$ | $\mathbf{AddMag} \times_{\mathbf{Set}} \mathbf{Mag}$ | $(\mathbf{Ab}$ on $+) \times_{\mathbf{Set}} (\mathbf{Semigrp}$ on $\cdot)$, refined by $\mathrm{Distrib}$ |
| $\mathbf{Ring}$ | mult. unit | $\mathbf{Rng}.\mathrm{Unital}_{\cdot}$ |
| $\mathbf{CRing}$ | mult. comm. | $\mathbf{Ring}.\mathrm{Comm}_{\cdot}$ |
| $\operatorname{Mod}_R$ | $\mathbf{Ab}$ | $\mathbf{Ab}$ with an $R$-action $R \to \operatorname{End}(M)$ — the fibre over $R$ of $\operatorname{Mod}_{(-)}$ (@def-modules-over-ring) |
| ${}_R\mathbf{BiMod}_S$ | $\mathbf{Ab}$ | $\operatorname{Mod}_R \times_{\mathbf{Ab}} \operatorname{Mod}_{S^{\mathrm{op}}} = \operatorname{Mod}_{R \otimes_{\mathbb Z} S^{\mathrm{op}}}$ |
| $\mathbf{Alg}_R$ | $\mathbf{Ring}$ | $\mathbf{Ring} \times_{\mathbf{Ab}} \operatorname{Mod}_R$ with $R$ central — a monoid object in $\operatorname{Mod}_R$ |

## The base graph and its towers {#sec-base-graph}

Having constructed the named categories, collect their declared forgetful functors. The
named categories have only the adjacent forgetful functors declared; every other functor
between them is a composite. These forgetfuls and the towers they form — $\mathbf{Set}$ at
the foot, the magma and additive towers, the rings, modules, and forms — are the
[category graph](../lean/Category-Graph.md), rendered from its GraphViz manifest; the chains
$R\text{-}\mathbf{Mod} \to \mathbf{Ab} \hookrightarrow \mathbf{Grp} \to \mathbf{Mon} \to
\mathbf{Mag} \to \mathbf{Set}$ and $\mathbf{CommRing} \to \mathbf{Ab}$ are paths in it. An
axiom constraining an operation has classifying category the lowest category in which that
operation is present (commutativity over $\mathbf{Mag}$, not over $\mathbf{Ring}$); on any
category above, the axiom is the pullback (@def-axiom-classifier). A predicate is the
pullback of one on the underlying data exactly when it factors through the forgetful; finite
generation, freeness, and torsion do not (they are structure-relative) and are defined over
their structured categories.

The multiplicative tower bottoms out in $\mathbf{Mag}$ (@def-operation-categories), the category of a set with
one binary operation, and in Grothendieck constructions [@nlab:grothendieck_construction]
over $\mathbf{Set}$. Structure-on-an-object (a magma structure on a set: a lift of
$\mathbf 1 \to \mathbf{Set}$) and structure-on-a-category (an abelian structure on a
category: a lift of $\mathbf 1 \to \mathbf{Cat}_1$) are the same construction at successive
levels. The object-level realization of this graph — the module, form, and lattice
categories — is developed in [Definitions](Mathematical-Definitions.md).

## Categorical intersection {#sec-intersection}

::: {#def-classifier-intersection}
## Intersection of classifiers

For classifiers $\iota_A \colon \mathcal C.A \to \mathcal C$ and
$\iota_B \colon \mathcal C.B \to \mathcal C$ their intersection is the pullback in
$\mathbf{Cat}_1$ of the cospan $\mathcal C.A \to \mathcal C \leftarrow \mathcal C.B$:

```{.tikz}
%%| filename: intersection-pullback
%%| additionalPackages: \usepackage{tikz-cd} \usepackage{amssymb}
\begin{tikzcd}
\mathcal{C}.A \times_{\mathcal C} \mathcal{C}.B \arrow[r] \arrow[d] \arrow[dr, phantom, "\lrcorner", very near start] & \mathcal{C}.B \arrow[d, "\iota_B"] \\
\mathcal{C}.A \arrow[r, "\iota_A"'] & \mathcal{C}
\end{tikzcd}
```

the apex $\mathcal C.A \times_{\mathcal C} \mathcal C.B$ being the category of objects with compatible $A$- and $B$-structures. It is again a classifier.
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

**There is no categorical union of classifiers.** "Has an $A$- or $B$-structure" is a
disjunction with no classifier realization: a classifier carries no decomposition of its
axiom into removable pieces, so there is no operation on $\iota_A, \iota_B$ returning it.
(The coproduct $\mathcal C.A \sqcup \mathcal C.B \to \mathcal C$ tags objects by which
structure they have and is not a subcategory-defining classifier; it is not this either.)

## SageCat and its limit-closure {#sec-sagecat}

::: {#def-sagecat}
## SageCat

$\mathbf{SageCat}$ is the (2-)category whose objects are the named categories together with
their axiom classifiers $\mathcal C.A \to \mathcal C$, and whose morphisms are the
forgetful/inclusion functors generated by parent relationships and axiom imposition,
together with a functor $\mathbf{SageCat} \to \mathbf{Cat}_1$. Axioms are identified by $A$
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

For a finite diagram $D$ in $\mathbf{Cat}_1$, $\mathrm{Join}(D) := \lim D$. For $D$ the
forgetful-closed diagram on classifiers $\{\mathcal C.A_i \to \mathcal C\}$,
$\mathrm{Join}(D)$ is their categorical intersection (@sec-intersection): the terminal
cone, the universal category satisfying the conjunction of the $A_i$ compatibly with all
forgetfuls.
:::

::: {#def-meet-diagram}
## Meet of a diagram

For the same diagram, $\mathrm{Meet}(D) := \mathrm{colim}\, D$, the initial cocone —
dually, $\mathrm{Meet}_{\mathbf{Cat}_1}(D) = (\lim_{\mathbf{Cat}_1^{op}} D^{op})^{op}$. Because
$D$ carries the forgetful functors, this colimit is the finest category through which all
the constituents factor — their common base / shared-structure category (e.g. the colimit
of the group and additive-monoid forgetful diagrams is $\mathbf{Set}$).
:::

::: {#thm-sagejoin}
## SageJoin

$\mathrm{SageJoin}(\{A_i\}) = \mathrm{Join}(D) = \lim D$. This is realizable in
$\overline{\mathbf{SageCat}}$: computing it adds one object — the limit apex — which
$\mathbf{Cat}_1$ always provides; it may coincide with an object already present. Two caveats
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
  pullback (@def-axiom-through-functor). No bespoke class, hence no
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
