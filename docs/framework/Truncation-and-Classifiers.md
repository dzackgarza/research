# Truncation, Classifiers, and Filled Diagrams {#sec-truncation}

The general form of the classifier machinery: the primitive is the projection of a
category of elements, an axiom is imposed by pullback against the diagrams of composites
with a filler (the sketch of an algebraic theory), the property / structure /
stuff classification is the truncation level of the space of fillers, and coherence of
higher axioms is governed by an operad. The working 1-categorical statements of the
[Framework](Mathematical-Framework.md#sec-axiom-classifiers) are the low truncations
of the constructions below and agree with them on the nose; this page is what makes
that agreement a theorem rather than an analogy, and it is the precise sense in which
the program's presentation does not fix its categorical height.

Throughout, $\mathcal M$ is the ambient category in which the construction runs —
$\mathbf{Set}$, $\mathbf{Cat}_1$, or $\mathbf{Cat}_\omega$ — assumed to have finite
products and the limits named below; sizes follow the $\mathcal U$-smallness
convention of the
[Style Guide](../contributing/Mathematical-Language-Style-Guide.md#sec-formation-conventions).
Objects of $\mathcal M$ are selected by points $\mathbf 1 \to \mathcal M$ from the
terminal object; the initial object names nothing.

## Truncation {#sec-truncation-defs}

::: {#def-truncated-space}
## Truncated space

Truncation is intrinsically an endofunctor of $\mathbf{Cat}_\omega$
([Ambient setting](Ambient-Setting.md#def-truncated)); the classifier machinery reads off its
restriction to the filler *spaces* $\Phi_A(X)$ — the $\Pi_\infty$-image, where the level lives.
For $n \ge -2$, a space ($\infty$-groupoid) $S$ is *$n$-truncated* if
$\pi_i(S, s) = 0$ for every $i > n$ and every basepoint $s \in S$
[@nlab:truncated_object]. The low cases, unwound:

- $(-2)$-truncated iff contractible;
- $(-1)$-truncated iff empty or contractible — a *proposition*;
- $0$-truncated iff homotopy-discrete — a *set*;
- $1$-truncated iff equivalent to the nerve of a *groupoid*.

Write $\mathcal S_{\le n} \subseteq \mathcal S$ for the full subcategory of
$n$-truncated spaces.
:::

::: {#def-truncation-functor}
## Truncation functor

The inclusion $\mathcal S_{\le n} \hookrightarrow \mathcal S$ admits a left adjoint
$\tau_{\le n} \colon \mathcal S \to \mathcal S_{\le n}$ — the space-level restriction of the
intrinsic truncation endofunctor of $\mathbf{Cat}_\omega$
([Ambient setting](Ambient-Setting.md#def-truncated)) — with unit $S \to \tau_{\le n} S$
killing homotopy above level $n$; $S$ is $n$-truncated iff the unit is an equivalence. For an
object $X$ of a higher ambient, $n$-truncation is that intrinsic endofunctor; that $X$ is
$n$-truncated iff $\operatorname{Map}_{\mathcal E}(Y, X)$ is an $n$-truncated space for all $Y$
is then a *theorem* (probe detection), not the definition.
:::

::: {#def-truncated-morphism}
## Truncated morphism

A morphism $f \colon X \to Y$ is *$n$-truncated* if each homotopy fiber
$\operatorname{fib}_y(f)$ is an $n$-truncated space. In particular $f$ is
$(-1)$-truncated iff it is a monomorphism (propositional fibers), and $(-2)$-truncated
iff it is an equivalence. Since $n$-truncated $\Rightarrow$ $(n{+}1)$-truncated, the
conditions are nested, not exclusive.
:::

::: {#def-categorical-dimension}
## Categorical dimension

An ambient $\mathcal M$ is an *$(n,1)$-category* if all its mapping objects are
$(n{-}1)$-truncated spaces: $\mathbf{Set}$ is a $(1,1)$-category and $\mathbf{Cat}_1$ a
$(2,1)$-category, with mapping objects sets and groupoids, so the class of an axiom is read
directly off the truncation of the fibers — top level sets in $\mathbf{Set}$ (the classically
discrete case), groupoids in $\mathbf{Cat}_1$. The synthetic ambient $\mathbf{Cat}_\omega$
([Ambient setting](Ambient-Setting.md#def-ambient-categories)) is instead the weak
$\omega$-category $(\infty,\infty)$: its mapping objects $[C, D]$ are higher categories, not
spaces, so the class is read off the truncation of $\Pi_\infty$ applied to the filler object —
the derived mapping space ([Ambient setting](Ambient-Setting.md#def-mapping-spaces)) — and in
it nothing truncates (@thm-tower-stabilization). "Propositional" always means $(-1)$-truncated,
independent of the ambient.
:::

## Element projections {#sec-element-projections}

"Forgetful functor" has no intrinsic definition; the honest primitive is the
projection of a category of elements. For a presheaf
$\Phi \colon \mathcal C^{\mathrm{op}} \to \mathbf{Set}$ — more generally a
pseudofunctor valued in $\mathbf{Cat}_1$ or in spaces — the category of elements
$\int_{\mathcal C} \Phi$ and its projection
$\pi_\Phi \colon \int_{\mathcal C} \Phi \to \mathcal C$ are pinned, with citations and
the composite-variance convention, in
[Categorical Foundations](Categorical-Foundations.md#sec-constructions);
$\pi_\Phi$ is a discrete opfibration in the $\mathbf{Set}$-valued case and a
Grothendieck (op)fibration in general. The faithful or full behavior of $\pi_\Phi$ is
a *consequence* of the truncation of the fibers $\Phi(X)$, never an imposed property —
that consequence is @prp-truncation-classification.

## Axiom classifiers {#sec-axiom-classifiers-general}

::: {#def-axiom-classifier-general}
## Axiom classifier, general form

An *axiom classifier over $\mathcal C$* is a functor
$\iota_A \colon \mathcal C.A \to \mathcal C$ that is equivalent, over $\mathcal C$, to
the projection $\pi_{\Phi_A}$ of a category of elements for some pseudofunctor
$\Phi_A \colon \mathcal C^{\mathrm{op}} \to \mathcal M$ — the *classifying
pseudofunctor* of $A$, whose value $\Phi_A(X)$ is the space of $A$-data on $X$.
Equivalently, $\iota_A$ is the projection of a Grothendieck (op)fibration. This realizes
the universal property of @def-axiom-classifier: reindexing $\Phi_A$ along any
$F \colon \mathcal D \to \mathcal C$ is the pullback $\mathcal D.A$, so every
classifier of $A$ over $\mathcal C$ is a pullback of $\iota_A$. The definition is not
"any faithful functor": $\iota_A$ must arise as an element-projection, the classifying
pseudofunctor carries the mathematical content
(constructed in @sec-filled-diagrams from universal operations and filled diagrams),
and $\iota_A$ is derived from it. The *fiber* of $A$ over $X$ is $\Phi_A(X)$, with no
truncation restriction; $A$ is *$k$-truncated* when $\iota_A$ is a $k$-truncated
morphism (@def-truncated-morphism), equivalently when every fiber is
$\tau_{\le k}$-local.
:::

::: {#prp-truncation-classification}
## The classification is the truncation level of the fibers

Fix $\mathcal M$ an $(n,1)$-category. Then [@BS07, §2;
@nlab:stuff_structure_property]:

| fibers $\Phi_A(X)$ | $\iota_A$ | $A$ is |
|---|---|---|
| propositional ($\tau_{\le -1}$-local) | fully faithful; a monomorphism | a *property* |
| discrete ($\tau_{\le n-1}$-local) | faithful | *structure* |
| $\tau_{\le k}$-local, $k \ge n$ | — | *$k$-stuff* |
| unrestricted | arbitrary | *stuff* |

The classes are nested — property $\subseteq$ structure $\subseteq$ stuff — since
$k$-truncated implies $(k{+}1)$-truncated. The *property* threshold is absolute at
$-1$; the *structure* threshold is $n - 1$ and tracks the dimension of the ambient:
over $\mathbf{Set}$ structure means set-many choices, over $\mathbf{Cat}_1$ a groupoid
of choices. This single index shift is the entire mechanism by which the same axiom
changes class as the ambient grows (@prp-filler-truncation). In the 1-categorical
readout this recovers exactly the computed classification of the
[Framework](Mathematical-Framework.md#sec-axiom-classifiers): full and faithful
$\Leftrightarrow$ propositional fibers (property, a replete full subcategory);
faithful $\Leftrightarrow$ discrete fibers (structure); and "a property is a
proposition" is a lemma of fullness, not a convention. In a higher ambient, "fully
faithful" and "faithful" are meant in the local, top-dimensional sense appropriate to
$\mathcal M$.
:::

Representative classifiers, with their computed class:

| axiom | over | fiber $\Phi_A(X)$ | class |
|---|---|---|---|
| Finite | $\mathbf{Set}$ | empty or a point | property |
| binary operation | $\mathbf{Set}$ | $\operatorname{Hom}(X^2, X)$ | structure |
| associative, commutative | $\mathbf{Mag}$ | empty or a point | property |
| Free | $\operatorname{Mod}_R$ | empty or a point | property |
| chosen basis | $\operatorname{Mod}_R$ | the set of bases | structure |
| monoidal, symmetric monoidal | $\mathbf{Cat}_1$ | the groupoid of such structures | structure |
| Abelian | $\mathbf{Cat}_1$ | empty or contractible | property |
| $R$-module over varying $R$ | $\mathbf{Ab}$ | modules over each ring, with their maps | stuff |

The last row is why $\Phi_A$ is allowed arbitrary values: forgetting *which ring* one
is a module over drops morphisms, so the classifier is neither a property nor a
structure classifier — yet it is still an element-projection, hence a legitimate
classifier.

## Pullback and intersection, homotopy-invariantly {#sec-pullback-general}

For $F \colon \mathcal D \to \mathcal C$ and a classifier $\iota_A$ over $\mathcal C$,
the induced classifier on $\mathcal D$ is the homotopy pullback
[@nlab:homotopy_pullback]
$$
\mathcal D.A := \mathcal D \times^{h}_{\mathcal C} \mathcal C.A
\;\simeq\; \textstyle\int_{\mathcal D} (F^{*} \Phi_A),
$$
the elements of the reindexed pseudofunctor. Transport preserves the truncation
level of the fibers — property pulls back to property, structure to structure —
which is what makes base-and-pullback
([A1](Settled-Mathematical-Rulings.md#a1)/[A3](Settled-Mathematical-Rulings.md#a3))
class-stable. Intersection of classifiers is likewise the homotopy pullback over
$\mathcal C$, the terminal cone already established in the
[Framework](Mathematical-Framework.md#sec-intersection); there is no categorical
union. Homotopy limits throughout make every construction equivalence-invariant with
no isofibration side condition; in the 1-categorical strict setting, replete full
inclusions are isofibrations, so strict and homotopy pullbacks agree for property
classifiers, and structure classifiers require the pseudo-pullback — the compatibility
established in [Categorical Foundations](Categorical-Foundations.md#sec-pullback-cat).

## Operations as elements of hom-presheaves {#sec-operations}

::: {#def-operation-classifier}
## Operation classifier

For $\mathcal C$ with finite products, the *space of $n$-ary operations* is the
presheaf
$$
\operatorname{Op}_n(X) = \operatorname{Map}_{\mathcal C}(X^{\times n},\, X),
$$
and the *$n$-ary operation classifier* is
$\mathcal C.\mathrm{Op}_n := \int_{\mathcal C} \operatorname{Op}_n$ with its
projection. Objects are pairs $(X, \ast)$ with $\ast \colon X^n \to X$. Adding an
operation is *structure*: the fibers are genuine mapping spaces, discrete but not
propositional. The universal operation $\ast$ lives on the total category
$\mathcal C.\mathrm{Op}_n$ and is available *there* to build diagrams — it does not
exist on $\mathcal C$, which is why every equation on an operation is imposed over the
operation classifier, never on the base.
:::

$\mathbf{Mag}$ is exactly $\int_{\mathbf{Set}} \operatorname{Op}_2$, the bottom of the
tower of the [Framework](Mathematical-Framework.md#sec-base-graph); the same
construction one level up, $\int_{\mathbf{Cat}_1} \operatorname{Op}_2$, is the category
of categories-with-a-bifunctor. Structure on an object and structure on a category are
the same construction at successive levels — one recursive pattern with
$\mathcal M = \mathbf{Set}$ and $\mathcal M = \mathbf{Cat}_1$ as instances.

## Equations as filled diagrams {#sec-filled-diagrams}

An equation on an operation is not new data; it is the assertion that a diagram of
composites of the universal operation commutes. A functor out of a category already
sends commuting relations to commuting ones, so an equation cannot be imposed by
*choosing* a diagram; it is imposed by the standard device behind a sketch
[@nlab:sketch] and a Lawvere (algebraic) theory [@nlab:lawvere_theory]: form the
diagram of both composites freely, then restrict to the operations whose two composites
agree — those with a filler. This is the diagrammatic presentation of the axiom's
algebraic theory; its coherent form is algebras over an operad (@sec-operadic-tower).

::: {#def-built-diagram}
## The diagram of composites and its fillers

Let $\Sigma$ be the finite index category of the equation — its two parallel legs the
two composites of the operation, left unidentified — and
$\mathbf{Dia}_\Sigma(\mathcal C) := \operatorname{Fun}(\Sigma_{\mathrm{free}}, \mathcal C)$
the category of $\Sigma$-diagrams in $\mathcal C$. The universal operation determines a
functor
$$
R_\Sigma \colon \mathcal C.\mathrm{Op}_n \longrightarrow \mathbf{Dia}_\Sigma(\mathcal C),
\qquad (X, \ast) \longmapsto \text{the diagram of composites},
$$
whose corners are the cartesian powers of $X$ and whose edges are the prescribed
$\ast$-composites — it constructs the diagram rather than constraining a chosen one. A
*filler* of a $\Sigma$-diagram is a witness that its two parallel legs agree, of the
kind the ambient $\mathcal M$ supports: an equality in $\mathbf{Set}$
($\mathbf{Dia}^{=}$), a chosen natural isomorphism in $\mathbf{Cat}_1$
($\mathbf{Dia}^{\simeq}$), a coherent equivalence in $\mathbf{Cat}_\omega$. The diagrams
with a filler are the domain of a functor
$\mathbf{Dia}^{\mathrm{fill}}_\Sigma \to \mathbf{Dia}_\Sigma$ — a replete full inclusion in
$\mathbf{Set}$, a structure classifier in $\mathbf{Cat}_1$.
:::

::: {#def-equation-classifier}
## The equation classifier

The classifier imposing "the diagram of composites commutes" is the homotopy pullback
$$
\mathcal C.A := \mathcal C.\mathrm{Op}_n
\times^{h}_{\mathbf{Dia}_\Sigma(\mathcal C)} \mathbf{Dia}^{\mathrm{fill}}_\Sigma(\mathcal C)
$$
— the operations whose diagram of composites has a filler; equivalently, the algebras
of the sketch of @sec-filled-diagrams.
:::

::: {#prp-filler-truncation}
## Truncation reads off the filler space

The fiber of $\mathcal C.A$ over $(X, \ast)$ is the space of fillers of
$R_\Sigma(X, \ast)$. Hence: a $\tau_{\le -1}$-local filler space (identity fillers,
$\mathbf{Set}$) makes it a *property* classifier; a $\tau_{\le n-1}$-local filler
space (chosen isomorphism fillers, $\mathbf{Cat}_1$) makes it *structure*; higher
filler spaces make it $k$-stuff. Operations are structure classifiers
(@def-operation-classifier) and equations impose a property *exactly when the filler is
forced to be an identity*; the same equation adds structure in a higher ambient. This is the mechanism
behind commutativity-as-property on $\mathbf{Set}$ versus braiding-as-structure on
$\mathbf{Cat}_1$, and it is the content of the index shift in
@prp-truncation-classification.
:::

## Coherence and the operadic tower {#sec-operadic-tower}

A single filler is not the end: the filler must satisfy coherence (the pentagon for
an associator, the hexagons for a braiding), and in a higher ambient that coherence is
again a chosen filler rather than an equation. The data at every level is governed by
an operad [@nlab:operad], whose arity-$k$ space supplies the shape and whose
composition law ties each level to the previous ones.

::: {#def-matching-tower}
## Matching object and the operad-governed tower

For a shape $\Sigma_k$ with boundary $\partial \Sigma_k$ populated by the previously
chosen data, the *matching object* is the homotopy limit
$M_k := \operatorname*{holim}_{\partial \Sigma_k} (\text{lower data})$ — the boundary
data the level-$k$ filler must extend. For an operad $\mathcal O$ in $\mathcal M$
presented by generating shapes $\Sigma_k$ and boundary maps — the associahedra
[@nlab:associahedron] for $A_\infty$, the little $n$-cubes operad
[@nlab:little_cubes_operad] for $E_n$ — the *$\mathcal O$-algebra classifier* is the
homotopy limit of the tower of homotopy pullbacks
$$
\cdots \to \mathcal C.A^{(k)} \to \mathcal C.A^{(k-1)} \to \cdots \to
\mathcal C.\mathrm{Op}_n, \qquad
\mathcal C.A^{(k)} := \mathcal C.A^{(k-1)}
\times^{h}_{\mathbf{Dia}_{\Sigma_k}} \mathbf{Dia}^{\mathrm{fill}/M_k}_{\Sigma_k},
$$
each stage cutting the level-$k$ fillers extending $M_k$.
:::

::: {#thm-operad-coincidence}
## Coincidence with operad algebras

With the matching-object boundary conditions and homotopy limits throughout, the tower
is the cell-by-cell presentation of $\operatorname{Alg}_{\mathcal O}(\mathcal M)$, and
$\mathcal C.A \simeq \operatorname{Alg}_{\mathcal O}(\mathcal M)$ for the chosen
cofibrant model of $\mathcal O$; different cofibrant models give equivalent
classifiers, and the model choice is the only genuine input. Both amendments are
load-bearing: without the matching-object conditions the imposed fillers are incoherent
and the classifier is strictly larger than $\operatorname{Alg}_{\mathcal O}$; without
homotopy limits the tower's limit is not the correct one.
:::

::: {#thm-tower-stabilization}
## Truncation recovers the strict and finite cases

The truncation level of $\mathcal M$ fixes where the tower stabilizes:

- $\mathcal M = \mathbf{Set}$: all filler spaces above arity 2 are propositional, the
  tower collapses immediately, and the classifier is the strict algebra —
  $A_n = A_\infty = {}$strict associative; the $E_n$ tower stabilizes at
  $E_2 = E_\infty = {}$commutative.
- $\mathcal M = \mathbf{Cat}_1$: the tower stabilizes after one coherence layer —
  associator + pentagon (monoidal, $A_\infty$), braiding + hexagons (braided, $E_2$),
  symmetry (symmetric, $E_{\ge 3}$). The classical coherence theorems [@Mac94, ch.
  VII] are absorbed as the statement that this finite presentation suffices — that the
  associahedra / little-cubes resolution terminates at these cells in a 2-category.
- $\mathcal M = \mathbf{Cat}_\omega$: nothing truncates, and the classifier is the
  full $A_\infty$ / $E_n$ / $E_\infty$ algebra.
:::

## The two ambients side by side {#sec-worked-examples}

**In $\mathbf{Set}$.** $\mathbf{Mag} = \int_{\mathbf{Set}} \operatorname{Op}_2$;
associativity is the square shape with legs $\ast(\ast \times 1)$ and
$\ast(1 \times \ast) \colon X^3 \rightrightarrows X$, imposed against $\mathbf{Dia}^{=}$ —
a property, and the higher associahedra automatically impose contractible-filler
conditions, so semigroups are already the $A_\infty$-classifier in $\mathbf{Set}$.
Commutativity is the swap bigon with legs $\ast$ and $\ast \circ \tau$, again a
property; adjoining the unit (a nullary operation: structure, plus its two unit-law
properties) gives $\mathbf{Mon}$ and $\mathbf{CMon}$ as iterated intersections of
property classifiers over $\mathbf{Mag}$ — replete full, based at the magma level,
pulled up the towers
([A1](Settled-Mathematical-Rulings.md#a1)).

**In $\mathbf{Cat}_1$.** The same shapes one level up, with
$\operatorname{Op}_2(\mathcal A) = \operatorname{Fun}(\mathcal A \times \mathcal A, \mathcal A)$.
Imposing associativity against $\mathbf{Dia}^{=}$ (strict monoidal categories) is
legitimate but flagged by its artificially propositional fibers; the correct imposition
is against $\mathbf{Dia}^{\simeq}$ — a chosen associator, structure — followed by the
pentagon, an equation between 2-cells and hence a property over the matching
object assembled from the associator:
$$
\mathbf{MonCat} =
\big( \mathbf{BinopCat} \times^{h}_{\mathbf{Dia}_{\mathrm{assoc}}} \mathbf{Dia}^{\simeq} \big)
\times^{h}_{\mathbf{Dia}_{\mathrm{pent}}} \mathbf{Dia}^{=}_{/M_{\mathrm{pent}}},
$$
plus the unit object (structure) and triangle (property). Commutativity becomes the
braiding — a chosen isomorphism $\beta \colon \otimes \Rightarrow \otimes \circ
\mathrm{swap}$, structure — with the hexagons and then the symmetry
$\beta_{Y,X} \circ \beta_{X,Y} = \mathrm{id}$ as properties: braided monoidal
categories are the $E_2$-classifier and symmetric monoidal categories the
$E_{\ge 3}$-classifier in $\mathbf{Cat}_1$.

| axiom | in $\mathbf{Set}$ | in $\mathbf{Cat}_1$ |
|---|---|---|
| binary operation | structure | structure |
| associativity | property (identity filler) | structure (associator) + property (pentagon) |
| commutativity | property (identity filler) | structure (braiding) + property (hexagons; symmetry for $E_{\ge 3}$) |
| $A_\infty$ | $=$ strict associative | $=$ monoidal (stabilizes at the pentagon) |
| $E_\infty$ | $=$ commutative (at $E_2$) | $=$ symmetric (at $E_3$) |

The construction is identical in both columns — build the diagram from the universal
operation, land in the free diagram category, homotopy-pull-back the filled sub-family
with operad-governed boundaries — and the entire difference is the truncation level of
the ambient, which fixes the filler-space truncation (property versus structure at
each factor) and the stabilization level of the tower.
