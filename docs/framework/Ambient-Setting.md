# Ambient setting {#sec-ambient}

The framework is developed *synthetically*: it works inside an ambient weak higher category
$\mathbf{Cat}_\omega$ and its internal constructions, taking no simplicial, quasicategorical, or
type-theoretic model as primitive [@Lur26]. The organizing principle is that higher structure
stays *internal* to $\mathbf{Cat}_\omega$; passing to spaces, cores, or components is a separate,
information-losing operation, and equality — below and on the [Equality](Equality.md) page — is
extra rigidity imposed on that internal structure rather than a form of equivalence.

::: {#def-universe}
## Universe and smallness

Fix a Grothendieck universe $\mathcal U$ [@nlab:universe]; an object is *small* when it lies in
$\mathcal U$, and constructions are carried out for small inputs, enlarging $\mathcal U$ when a
construction must range over all small objects. One presentation of $\mathbf{Cat}_\omega$ is
simplicial — $\mathbf{sSet} = \operatorname{Fun}(\mathbf\Delta^{\mathrm{op}}, \mathbf{Set})$,
with $\infty$-categories the simplicial sets filling inner horns and *spaces* the Kan complexes
[@Lur26, Tag 003A] — but no such model is primitive here.
:::

::: {#def-ambient-cat-w}
## The ambient weak higher category $\mathbf{Cat}_\omega$

Work in an ambient *weak higher category* $\mathbf{Cat}_\omega$: its objects are the small weak
higher categories, and it comes equipped with internal functor objects, limits, pullbacks,
homotopy quotients, walking cell shapes, and adjunctions. These internal constructions —
together with (co)ends, Grothendieck constructions, and Day convolution — are the tools the
framework builds from, and each object and property below is *defined* by such a universal
construction rather than *detected* by probing a model.
:::

::: {#def-internal-hom}
## Internal hom

The fundamental hom-object of $C, D \in \mathbf{Cat}_\omega$ is the *internal hom*
$$
[C, D] := \operatorname{Fun}(C, D) \in \mathbf{Cat}_\omega,
$$
itself a weak higher category whose cells are the functors, natural transformations,
modifications, and their higher analogues. It is cartesian closed,
$$
[X \times C, D] \simeq [X, [C, D]],
$$
and there is no second, space-valued primitive hom-object.
:::

::: {#def-cells}
## Cells, arrows, and hom-objects

A *$0$-cell* of $C$ is a map $x \colon * \to C$. Writing $I$ for the walking arrow, the *arrow
object* is $\operatorname{Arr}(C) := [I, C]$, with source and target
$(s, t) \colon \operatorname{Arr}(C) \to C \times C$, and the hom-object between $0$-cells
$x, y$ is the pullback
$$
\operatorname{Hom}_C(x, y) := * \times_{C \times C} \operatorname{Arr}(C).
$$
A $k$-cell of $C$ is a $(k-1)$-cell of $\operatorname{Hom}_C(x, y)$ — a $1$-cell is a map
$x \to y$, a $2$-cell a map between two such — and composable arrows are
$\operatorname{Arr}(C) \times_C \operatorname{Arr}(C)$. The total family
$\operatorname{Hom}_C(-, -) \colon C^{\mathrm{op}} \times C \to \mathbf{Cat}_\omega$ packages every
hom-object at once; its Grothendieck construction is a total category of the arrows of $C$
whose fibers recover the individual $\operatorname{Hom}_C(x, y)$. The suspension–loop–fiber
calculus on these hom-objects is [Loops and suspension](Loops-and-Suspension.md).
:::

::: {#def-mapping-spaces}
## Mapping spaces are derived

Let $\Pi_\infty \colon \mathbf{Cat}_\omega \rightleftarrows \mathcal S : i$ send a higher category to
its homotopy type in *spaces* $\mathcal S = \mathbf{Grpd}_\infty$, right adjoint to the
inclusion $i$. The *mapping space* is the derived object
$$
\operatorname{Maps}(C, D) := \Pi_\infty[C, D].
$$
Spaces arise only after applying $\Pi_\infty$; this is not to be silently identified with
taking a core, a nerve, or a truncation of $[C, D]$.
:::

::: {#def-initial-terminal}
## Terminal and initial objects, contractibility

Universal properties are conditions on internal hom-objects. An object $T$ is *terminal* when
$[D, T] \simeq *$ for every $D$, and dually $\varnothing$ is *initial* when
$[\varnothing, D] \simeq *$ for every $D$; these are the empty limit and empty colimit, each
unique up to equivalence. Such a property pins an object only up to equivalence — a concrete
construction chooses a representative, whose literal value is not to be replaced by an
equivalent model when an on-the-nose computation is asked for. An object $C$ is *contractible*
when $C \to *$ is an equivalence in $\mathbf{Cat}_\omega$, not merely when $\Pi_\infty C$ is
contractible; likewise a localization $L_W C$ and a cofiber $* \amalg_W C$ stay distinct even
where $\Pi_\infty$ identifies them. In $\mathbf{Cat}_\omega$ the terminal object is the *point* $*$
— one object and only its identity — and the initial object the *empty* higher category
$\varnothing$; under $\Pi_\infty$ these give the point and the empty space of $\mathcal S$.
:::

::: {#def-truncated}
## Truncation

For each $n \ge -2$, *$n$-truncation* is an endofunctor
$\tau_{\le n} \colon \mathbf{Cat}_\omega \to \mathbf{Cat}_\omega$, and an object $C$ is
*$n$-truncated* iff the unit $C \to \tau_{\le n} C$ is an equivalence. Along $\Pi_\infty$
(@def-mapping-spaces) it restricts to the classical truncation of *spaces*: a space $S$ is
$n$-truncated iff $\pi_i(S, s) = 0$ for every $i > n$ and basepoint $s$
[@nlab:truncated_object], the reflection
$$
\adj{\mathcal S}{\mathcal S_{\le n}}{\tau_{\le n}}{\iota}, \qquad \tau_{\le n} \dashv \iota,
$$
onto the $n$-truncated spaces $\mathcal S_{\le n}$; on low levels
$\mathcal S_{\le -1} \simeq \{\varnothing, *\}$, $\mathcal S_{\le 0} \simeq \mathbf{Set}$, and
$\mathcal S_{\le 1} \simeq \mathbf{Grpd}$, and a space is *propositional* if it is
$(-1)$-truncated and *discrete* if it is $0$-truncated. That $C$ is $n$-truncated iff
$\Pi_\infty[D, C]$ is an $n$-truncated space for every $D$ — equivalently, the representable
$\Pi_\infty[-, C]$ is valued in $n$-truncated spaces — is a *theorem*, probe detection, not the
definition. A morphism $f$ is $n$-truncated when its fibers are; the $(-1)$-truncated morphisms
are the monomorphisms and the $(-2)$-truncated ones the equivalences. Truncation is nested,
$n$-truncated implies $(n{+}1)$-truncated, and is distinct from the enrichment tower
(@def-ambient-categories) and from passage to a core.
:::

::: {#def-ambient-categories}
## The enrichment tower and categories

The dimension tower is a *tower of fibrations*
$$
\cdots \longrightarrow \mathbf{Cat}_2 \longrightarrow \mathbf{Cat}_1 \longrightarrow \mathbf{Cat}_0 = \mathbf{Set},
$$
in which $\mathbf{Cat}_n$ is *enriched* in $\mathbf{Cat}_{n-1}$ — the hom-objects of an
$n$-category are $(n-1)$-categories — and each level is *defined* from the one below as the
fiber of its fibration; read the other way, as identity higher cells are added along the
sections $\mathbf{Cat}_{n-1} \hookrightarrow \mathbf{Cat}_n$, the passage is a cofiber. This is
what makes it a genuine tower rather than a free coherent completion that would replace
equations by new witnesses. Its limit $\mathbf{Cat}_\omega := \lim_n \mathbf{Cat}_n$, the weak
$\omega$-categories, is the ambient — the top of the tower, not a separate object. This dimension
truncation, the homotopy truncation of spaces (@def-truncated), and passage to a core are three
different operations. A *category* is an object of $\mathbf{Cat}_1$ (enriched in
$\mathbf{Cat}_0 = \mathbf{Set}$, so its hom-objects are sets); $\mathbf{Set}$ itself is an
object of $\mathbf{Cat}_1$, and the $1$-categorical work that is almost all of the framework
lives there. From here on every category is, implicitly, an object of $\mathbf{Cat}_\omega$.
:::

::: {#def-equality-of-objects}
## Isomorphism, equivalence, and equality

In a $1$-category, a morphism $f \colon a \to b$ is an *isomorphism* if it has a two-sided
inverse $g$ ($gf = \mathrm{id}_a$, $fg = \mathrm{id}_b$). In an $\infty$-category
$\mathcal C$, a morphism $f$ is an *equivalence* if its image $[f]$ is invertible in the
homotopy category $h\mathcal C$ [@Lur26, Tag 01DQ] — a homotopy inverse and a $2$-cell, the
higher coherences then following; a functor is an *equivalence of $\infty$-categories* if it
admits a homotopy inverse [@Lur26, Tag 01DY]. A *weak equivalence* is a map inducing an
equivalence of underlying homotopy types; it *inverts* directionality, whereas an equivalence
of $\infty$-categories *preserves* it (a category with a terminal object is weakly
contractible but not equivalent to the point).

*Equality* is separate and strict, and is Lean's: propositional equality $a = b$ (the type
$\operatorname{Eq}(a, b)$, itself a proposition) or definitional equality $a \equiv b$
(judgmental identity). Univalence is *not* assumed — it is unavailable in Lean's kernel
without significant upstream cost, and identifying isomorphic objects is rejected here on
philosophical grounds — so $a = b$ is never a synonym for isomorphism or equivalence:
isomorphic-but-unequal objects are the rule, and where objects agree only up to isomorphism
one writes $a \cong b$, never $a = b$. Constructions are stated up to equivalence with named
witnesses ([A4](Settled-Mathematical-Rulings.md#a4)); the symbols $\cong$, $\simeq$ and the
discipline for supplying and transporting a witness are [Identification](Identification.md).
The fuller $\infty$-categorical notion of equality that this strict version reduces from is
developed in [Equality](Equality.md).
:::

*Remark (elements).* An *element* of a functor $F \colon \mathcal C^{\mathrm{op}} \to
\mathbf{Set}$ is an object of its category of elements $\int F$ (@def-category-of-elements),
and two elements are equal iff they are equal there. For a scheme $X$, taking
$F = h_X = \operatorname{Hom}_{\mathbf{Sch}}(-, X)$ recovers the elements of $X$ as the objects
of $\int h_X$ — its $T$-points $\operatorname{Spec} T \to X$
([Elements](Elements-and-Containment.md#sec-elements)).
