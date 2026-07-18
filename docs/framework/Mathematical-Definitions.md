# Mathematical Definitions

The dependency tree of the program's mathematical objects, stated as definitions in standard language.
Every settled design ruling is **seated** under one of these definitions: the definition says what the object *is*; the [Settled Mathematical Rulings](Settled-Mathematical-Rulings.md) say which choices about it are closed, with their supersession trails.
The generation calculus (classify, factor, lift; property vs structure; transport as factorization) is owned by [Categorical Presentation Principles](../contributing/Categorical-Presentation-Principles.md); vocabulary is governed by the [Mathematical Language Style Guide](../contributing/Mathematical-Language-Style-Guide.md); Sage's actual category framework is enumerated in the [Sage Category Framework Inventory](../sage/Sage-Category-Framework-Inventory.md).
Provenance for everything here is the [#251](https://github.com/dzackgarza/research/issues/251) record.

Throughout, $R$ is a commutative ring — the arithmetic fibers take $R$ a PID or Dedekind domain with fraction field $K$ — and $W$ is an $R$-module, the **value module** of a form.
Notation carries claims: $\hookrightarrow$ asserts a replete full subcategory.

## Module categories {#sec-module-categories}

::: {#def-module-family}
## One module family

For a ring $A$, $\mathrm{Mod}_A$ is the category of left $A$-modules.
Right $R$-modules are $\mathrm{Mod}_{R^{\mathrm{op}}}$ — the same parameterized family at a different ring, never a separate primitive kind.
Bimodules carry two forgetful functors

$$
\mathrm{Mod}_R \xleftarrow{\;U_L\;} {}_{R}\mathrm{BiMod}_S \xrightarrow{\;U_R\;} \mathrm{Mod}_{S^{\mathrm{op}}},
$$

and for commutative $R$ the identification $\mathrm{Mod}_R \simeq \mathrm{Mod}_{R^{\mathrm{op}}}$ is a hypothesis-bearing equivalence witnessed by a natural isomorphism, not an equality.
:::

::: {#def-tower}
## The tower

The algebraic tower is generated from magmas by four subcategory inclusions — associativity, commutativity, unitality, inverses — with monoids, groups, and abelian groups arising as intersections, never as new declarations.
The abelian landing is *equivalent to* the $\mathbb{Z}$-fiber of the module family — $\mathbf{Ab} \simeq \mathrm{Mod}_{\mathbb{Z}}$, a canonical equivalence with a named witness, not an identity — and $\mathbb{Z}$ initial in rings gives base change $\mathrm{Mod}_{\mathbb{Z}} \to \mathrm{Mod}_R$ along the unique $\mathbb{Z} \to R$.
:::

::: {#def-module-subcategories}
## Module subcategories

The module properties the program pulls back are declared as replete full subcategories of $\mathrm{Mod}_R$: **free** $\subseteq$ **projective** (the inclusion a theorem), **finitely generated**, **torsion**, and **torsion-free**. These are *structure-relative* — they do not factor through the underlying set (Rulings [A3](Settled-Mathematical-Rulings.md#a3)) — so they are owned here and only pulled back along $\pi$ below, never re-declared.
:::

*Seated rulings:* [left/right modules are distinct categories](Settled-Mathematical-Rulings.md#invariants-and-their-evaluation).

## Axioms as subcategories; transport {#sec-axioms}

The axiom-classifier, transport, and property/structure machinery is the [Mathematical Framework](Mathematical-Framework.md#sec-axiom-classifiers): an axiom is a classifier $\iota_A : \mathcal{C}.A \to \mathcal{C}$ (@def-axiom-classifier), in the property case a replete full subcategory cut out at the node that owns the property; a property transports by pullback along a forgetful functor (@def-transport-property), declared at the highest node where it is well defined and pulled back below; and whether a lift is property or structure is computed from the classifier, never declared (@def-property-structure-stuff). This section applies that calculus to modules and forms; the two inclusions it needs beyond the generic machinery are:

::: {#def-derived-expressions}
## Derived expressions

Categories built from declared axioms by intersection, pullback, and the constructors of @sec-constructors are **expressions**; they are never re-declared as primitive nodes.
:::

::: {#def-theorem-witness}
## Theorem-witness inclusions

Inclusions such as $\mathrm{PID} \subset \mathrm{UFD} \subset \mathrm{Dom}$ are full subcategory inclusions whose witness is a theorem rather than a defining axiom; they are recorded as such.
:::

*Seated rulings:* the calculus itself is in [Categorical Presentation Principles](../contributing/Categorical-Presentation-Principles.md); [relation kinds are not fungible](Settled-Mathematical-Rulings.md#relation-kinds-are-not-fungible). The **abelian** boundary case — additive enrichment is property-like (membership a property), while the exact functors carrying the discriminant machinery are a non-full class (a structure a consumer names) — is developed in [Categorical Foundations](Categorical-Foundations.md#sec-constructions).

## Bilinear and quadratic form categories {#sec-forms}

::: {#def-form-presheaves}
## The presheaves

The two generating objects of the forms frame are the presheaves

$$
\operatorname{Bil}_{R,W},\ \operatorname{Quad}_{R,W} \;:\; \mathrm{Mod}_R^{\mathrm{op}} \longrightarrow \mathbf{Set},
$$

sending a module to its $W$-valued bilinear forms, respectively quadratic maps, acting by pullback along module maps.
:::

::: {#def-form-categories}
## Categories of elements

The total form categories are the categories of elements of these presheaves,

$$
\mathcal{B}_{R,W} \;=\; \operatorname{El}\!\big(\operatorname{Bil}_{R,W}\big),
\qquad
\mathcal{Q}_{R,W} \;=\; \operatorname{El}\!\big(\operatorname{Quad}_{R,W}\big),
$$

with covariant projection $\pi : \mathcal{B}_{R,W} \to \mathrm{Mod}_R$.
A morphism $(M, b_M) \to (N, b_N)$ is a module map $f : M \to N$ with $f^{*} b_N = b_M$ — an underlying map in the same direction as $\pi$, pulling the target form back to the source.
The defining datum is always the $W$-valued form; the map-to-dual picture appears only as the derived polarization of @def-polarization.
The convention for $\operatorname{El}$ — the standard category of elements of a presheaf, with **no** $(-)^{\mathrm{op}}$ — is fixed, and shown to be forced, in @sec-el.
:::

::: {#def-form-axioms}
## Form axioms at the total

Owned at $\mathcal{B}_{R,W}$, each a property-defined replete full subcategory: symmetric, skew-symmetric, alternating ($b(x,x) = 0$), nondegenerate, perfect, and even ($b(x,x) \in 2W$). The implications

$$
\mathrm{Perfect} \Rightarrow \mathrm{Nondegenerate},
\qquad
\mathrm{Alternating} \Rightarrow \mathrm{SkewSymmetric}
$$

hold unconditionally, and skew-symmetric implies alternating exactly when multiplication by $2$ is injective on $W$.
Even is nontrivial only where $2W \neq W$ (e.g. $W = R = \mathbb{Z}$, the even lattices); on a divisible value module such as $W = \mathbb{Q}/\mathbb{Z}$ it is vacuous ($2W = W$), and the torsion-side content passes instead to the quadratic refinement over $\mathbb{Q}/2\mathbb{Z}$ (@sec-polarization-functors, @def-discquad).
:::

::: {#def-polarization}
## Polarization; nondegenerate; perfect

For $(M, b)$, currying gives the **polarization**

$$
\tilde b : M \longrightarrow \operatorname{Hom}_R(M, W),
$$

requiring no freeness. The form is **nondegenerate** when $\tilde b$ is injective and **perfect (unimodular)** when $\tilde b$ is an isomorphism.
:::

::: {#def-orthogonal-sum}
## Orthogonal sum

The form categories carry a symmetric monoidal structure, the **orthogonal sum**: $(M, b_M) \perp (N, b_N) = (M \oplus N,\, b_M \oplus b_N)$ with vanishing cross terms. Being a *structure* (not a property), it is a named section $\mathcal{B}_{R,W}^{(\perp)}$ ([P4](../contributing/Mathematical-Language-Style-Guide.md#p4)), consumed by the bitorsor composition of @def-isometry-groups and the adelic product of @sec-genus-sec, which reference the named lift rather than "the" monoidal structure.
:::

*Seated rulings:* [the W-valued form is the defining datum](Settled-Mathematical-Rulings.md#forms-and-lattices) · [the total category and its variance](Settled-Mathematical-Rulings.md#forms-and-lattices) · [alternating vs skew-symmetric](Settled-Mathematical-Rulings.md#forms-and-lattices) · [nondegenerate is not unimodular](Settled-Mathematical-Rulings.md#forms-and-lattices).

## The polarization functors {#sec-polarization-functors}

::: {#def-polarization-functors}
Between the symmetric-bilinear and quadratic hierarchies:

$$
\operatorname{diag} : \mathrm{SymBil}_{R,W} \to \mathcal{Q}_{R,W},
\quad b \mapsto \big(x \mapsto b(x,x)\big);
\qquad
\operatorname{polar} : \mathcal{Q}_{R,W} \to \mathrm{SymBil}_{R,W},
\quad q \mapsto \big((x,y) \mapsto q(x{+}y) - q(x) - q(y)\big),
$$

satisfying

$$
\operatorname{polar} \circ \operatorname{diag} \;=\; 2 \;=\; \operatorname{diag} \circ \operatorname{polar},
$$

hence mutually inverse equivalences exactly when $2$ is invertible on $W$.
The two hierarchies are genuinely parallel wherever $W$ has $2$-torsion.
On the discriminant fiber the **bilinearization**

$$
\beta \;=\; \big(\tfrac{1}{2}\big)_{*} \circ \operatorname{polar}
\;:\; \mathcal{Q}_{\mathbb{Z},\, \mathbb{Q}/2\mathbb{Z}} \longrightarrow \mathrm{SymBil}_{\mathbb{Z},\, \mathbb{Q}/\mathbb{Z}}
$$

composes the generic polarization with pushforward along $\mathbb{Q}/2\mathbb{Z} \xrightarrow{\;\sim\;} \mathbb{Q}/\mathbb{Z}$, $w \mapsto w/2$.
:::

*Seated rulings:* [bilinear and quadratic are parallel hierarchies](Settled-Mathematical-Rulings.md#forms-and-lattices).

## Derived arithmetic categories {#sec-derived}

All of the program's headline categories are expressions in the frame above (@def-derived-expressions); none is declared.

::: {#def-lattice}
## Lattices

$$
\mathbf{Lat}_R \;=\; \mathcal{B}_{R,R}\big[\, \mathrm{Symmetric} \wedge \mathrm{Nondegenerate} \wedge \pi^{*}(\text{f.g.} \wedge \text{projective}) \,\big],
$$

the value module being $R$ itself; over a PID, finitely generated projective means finitely generated free.
The AG **negative-definite convention** ($A_n$ negative-definite) is a normalization on objects, not a change of category.
:::

::: {#def-unimodular}
## Unimodular lattices

$\mathbf{Unimod}_R$ replaces Nondegenerate by Perfect in @def-lattice (which implies it).
:::

::: {#def-even-lattice}
## Even lattices

$\mathbf{EvenLat}_{\mathbb{Z}} = \mathbf{Lat}_{\mathbb{Z}} \cap \mathcal{B}[\mathrm{Even}]$, the intersection taken inside $\mathcal{B}_{\mathbb{Z},\mathbb{Z}}$.
:::

::: {#def-discbil}
## Discriminant bilinear forms

$$
\mathbf{DiscBil}_{\mathbb{Z}} \;=\; \mathcal{B}_{\mathbb{Z},\, \mathbb{Q}/\mathbb{Z}}\big[\, \mathrm{Symmetric} \wedge \mathrm{Nondegenerate} \wedge (U \circ \pi)^{*}(\mathrm{Finite}) \,\big],
$$

the finiteness axiom pulled back from sets through the underlying-set functor (@def-transport-property). In general the torsion fiber takes $W = K/R$, and the same expression defines $\mathbf{DiscBil}_R$ — the codomain of the @def-discriminant discriminant functor for general $R$, not only $\mathbb{Z}$.
:::

::: {#def-discquad}
## Discriminant quadratic forms

The quadratic discriminant category is the pullback of $\mathbf{DiscBil}_{\mathbb{Z}}$ along the bilinearization $\beta$ of @sec-polarization-functors — quadratic objects whose bilinearization is a discriminant form, **not** an even cut of bilinear objects.
:::

*Seated rulings:* [derived categories are expressions, never declared](Settled-Mathematical-Rulings.md#forms-and-lattices).

## The discriminant construction and the exact-sequence package {#sec-discriminant}

::: {#def-discriminant}
## Discriminant form of a lattice

For a nondegenerate lattice $L$ the discriminant is the object exhibited by the comparison of @def-metric-dual and @thm-double-complex,

$$
A_L \;:=\; L^{\#}/L \;\cong\; \operatorname{coker}\big(\tilde b : L \to \operatorname{Hom}(L, R)\big),
$$

carrying the $K/R$-valued form induced from $b_K \bmod R$ on $L^{\#}$.
Presenting $A_L$ this way — as a quotient inside the two-sequence comparison, with the isomorphism to $\operatorname{coker}\tilde b$ a *theorem* (the map $\beta$ of @def-metric-dual) — is what makes the $K/R$-valuation manifest rather than asserted before the comparison that licenses it.
The discriminant construction is the functor $L \mapsto A_L$; its **domain of functoriality is $\operatorname{Core}$** (@sec-isometry) — it is functorial for isometries, not for arbitrary form-preserving maps, and that named restriction is the content, not a caveat.
:::

::: {#def-two-witnesses}
## Two witnesses of the polarization; regularity is vanishing

The polarization $\tilde b : L \to L^* = \operatorname{Hom}_R(L, R)$ carries two functorial witness objects, and the form's regularity conditions are the **vanishing** of those objects — never predicates asserted directly:

$$
\operatorname{rad}(L) := \ker \tilde b, \qquad A_L := \operatorname{coker} \tilde b .
$$

$b$ is **nondegenerate** $:\!\iff \operatorname{rad}(L) = 0$; $b$ is **perfect (unimodular)** $:\!\iff \tilde b$ is an isomorphism, i.e. $\operatorname{rad}(L) = 0$ *and* $A_L = 0$. Thus $\operatorname{rad}(L)$ is the obstruction to nondegeneracy, and — once it vanishes — $A_L$ is the remaining obstruction to unimodularity. Neither condition is a property read off the object; each is the vanishing of a carried object. The radical sequence names both witnesses at once (here $W = R$; in general $L^* = \operatorname{Hom}(L, W)$):

$$
0 \to \operatorname{rad}(L) \to L \xrightarrow{\ \tilde b\ } L^* \to A_L \to 0 .
$$
:::

::: {#thm-localization-les}
## The localization long exact sequence

The base-change map $L \to L \otimes_R K$ is the truncation of $L \otimes_R (-)$ applied to $0 \to R \to K \to K/R \to 0$. Since $K$ is flat ($\operatorname{Tor}_1^R(L, K) = 0$), the sequence continues to

$$
0 \to \operatorname{Tor}_1^R(L,\, K/R) \to L \to L \otimes_R K \to L \otimes_R (K/R) \to 0,
$$

with the identification $\operatorname{Tor}_1^R(L, K/R) \cong T(L)$, the torsion submodule. For a lattice ($L$ f.g. projective, hence torsion-free) it collapses to $0 \to L \to L_K \to L \otimes (K/R) \to 0$.
:::

::: {#def-metric-dual}
## Metric dual and the comparison witness

Inside $L_K = L \otimes_R K$ the **metric dual**

$$
L^{\#} := \{\, x \in L_K : b_K(x, L) \subseteq R \,\}
$$

is *always* an honest $R$-submodule containing $L$ — the inclusion $L^{\#} \hookrightarrow L_K$ is injective by construction (a lattice is f.g. projective over the domain $R$, hence torsion-free, so $L \hookrightarrow L_K$; for a module with torsion, $L^{\#}$ is the dual of $L/T(L)$). Writing $\tilde b_K : L_K \to (L_K)^* = \operatorname{Hom}_K(L_K, K)$ for the rational polarization, one has $L^{\#} = \tilde b_K^{-1}(L^*)$, and the comparison map

$$
\beta := \tilde b_K|_{L^{\#}} : L^{\#} \to L^*, \qquad x \mapsto b_K(x, -)|_L
$$

is the restriction of $\tilde b_K$. The obstruction to $\beta$ (equivalently to $\tilde b_K$) being an isomorphism is the object

$$
\operatorname{rad}(L_K) = \ker \tilde b_K = \operatorname{rad}(L) \otimes_R K,
$$

whose **vanishing is nondegeneracy** (over the field $K$, injective $\iff$ bijective; and for torsion-free $L$, $\operatorname{rad}(L_K) = 0 \iff \operatorname{rad}(L) = 0$). When it vanishes, $\beta : L^{\#} \xrightarrow{\ \sim\ } L^*$, and the discriminant is computed either way:

$$
A_L = L^*/\tilde b(L) \;\cong\; L^{\#}/L .
$$

This isomorphism, realizing $L^* \cong L^{\#}$ inside the rational span, is the **once-only** sanctioned use of the ambient $L_K$; everything downstream consumes the abstract objects and canonical maps.
:::

::: {#thm-double-complex}
## The double complex

For nondegenerate $L$ the radical obstruction vanishes, so the polarization is a morphism of short exact sequences (top the localization LES of @thm-localization-les, bottom its $\operatorname{Hom}_R(L, -)$-dual, exact because $\operatorname{Ext}^1_R(L, R) = 0$ for $L$ projective) whose **middle vertical $\tilde b_K$ is an isomorphism**:

$$
\begin{array}{ccccccccc}
0 &\to& L &\to& L_K &\to& L \otimes (K/R) &\to& 0\\[2pt]
&& \downarrow{\scriptstyle\,\tilde b} && \downarrow{\scriptstyle\,\tilde b_K} && \downarrow{\scriptstyle\,\bar b} &&\\[2pt]
0 &\to& L^* &\to& \operatorname{Hom}(L, K) &\to& \operatorname{Hom}(L, K/R) &\to& 0
\end{array}
$$

The snake lemma reads the discriminant off the connecting map — $A_L = \operatorname{coker} \tilde b \cong \ker \bar b$ — and yields the dual presentation

$$
0 \to A_L \to L \otimes (K/R) \xrightarrow{\ \bar b\ } \operatorname{Hom}(L,\, K/R) \to 0 .
$$

These are kernel-checked diagram lemmas, never re-encoded informally: the two witnesses of @def-two-witnesses, the localization LES, and this comparison are the highest-drift-risk material in the program.
:::

*Seated rulings:* [the discriminant construction and the exact-sequence package](Settled-Mathematical-Rulings.md#the-discriminant-construction-and-the-exact-sequence-package).

## Isometry groupoids and automorphism groups {#sec-isometry}

::: {#def-isometry-groups}
## Core; isometries

$\operatorname{Core}(\mathcal{C})$ is the maximal subgroupoid.
Isometries and orthogonal groups are instances of generic constructions, never nodes:

$$
\operatorname{Isom}(X, Y) \;=\; \operatorname{Hom}_{\operatorname{Core}(\mathcal{C})}(X, Y),
\qquad
O(X) \;=\; \operatorname{Aut}(X).
$$

When nonempty, $\operatorname{Isom}(L, M)$ is an $(O(L), O(M))$-bitorsor.
:::

::: {#def-discriminant-rep}
## Discriminant representation

Applying $\operatorname{Aut}$ to the discriminant functor (@def-discriminant) yields the reduction

$$
O(L) \longrightarrow O(A_L, q_{A_L}),
$$

the **discriminant representation**. Its kernel is the **stable orthogonal group** $\widetilde O(L) := \ker\big(O(L) \to O(A_L, q_{A_L})\big)$ — named as a kernel in this sequence, not as "the isometries acting trivially." Surjectivity is *not* automatic: when it holds it is Nikulin's theorem under hypotheses (indefinite, $\operatorname{rank} L \ge \ell(A_L) + 2$), and in general the cokernel is the Miranda–Morrison genus / spinor-genus obstruction.
:::

::: {#prp-matrix-realizations}
## Matrix realizations

On the free restriction a choice of basis induces the faithful representation $O(L) \hookrightarrow \mathrm{GL}_n(R)$ — the precise sense in which $O(L)$ "is" a matrix group.
On the torsion side, for $A = \mathbb{Z}^n / D\mathbb{Z}^n$ with mixed invariant factors, $O(A)$ is canonically a **quotient** of a congruence-type matrix group and not a subgroup of any $\mathrm{GL}_n$; the homocyclic case $A \cong (\mathbb{Z}/d)^n$ is the genuine exception, with $O(q) \le \mathrm{GL}_n(\mathbb{Z}/d)$.
:::

::: {#def-index}
## Index

Index is an invariant on **monomorphisms** — its domain of definition is the subcategory of monos, a named restriction, not a prose qualification — with value the cardinality of the coset object $G/H$.
Its identity with a cokernel cardinality is a theorem under the abelian hypothesis, not a definition.
:::

::: {#thm-miranda-morrison}
## The Miranda–Morrison sequence

For an even lattice $L$ that is **indefinite of rank $\ge 3$**, the discriminant representation extends to the exact sequence

$$
1 \to \widetilde O(L) \to O(L) \to O(A_L, q_{A_L}) \to \Sigma(L)\big/\big((\Gamma_{\mathbb{Q}} \cap \Sigma(L)) \cdot \Sigma^{\#}(L)\big) \to 0,
$$

whose cokernel is a finite group of spinor/determinant data [@MM09, Thm. V.5.1], computable by Legendre symbols — the genus / spinor-genus obstruction (Rulings [A5](Settled-Mathematical-Rulings.md#a5), [H3](Settled-Mathematical-Rulings.md#h3)/[H7](Settled-Mathematical-Rulings.md#h7)). Notation caveat: the kernel is $\widetilde O(L) = \mathcal{O}^{\#}(L)$ (isometries trivial on the discriminant), **not** $\mathcal{O}^{+}(L) = \ker\det$; the two are distinct subgroups.
:::

*Seated rulings:* [O is an instance, never a node](Settled-Mathematical-Rulings.md#automorphism-groups) · [the torsion side is a quotient of a matrix group](Settled-Mathematical-Rulings.md#automorphism-groups) · [index](Settled-Mathematical-Rulings.md#invariants-and-their-evaluation).

## Genus {#sec-genus-sec}

::: {#def-genus}
For each place $v$ let $R_v$ be the corresponding completion.
The local profile of $L \in \mathbf{Lat}_{\mathbb{Z}}$ is its image under $\operatorname{Core}(\mathbf{Lat}_{\mathbb{Z}}) \to \prod_v \operatorname{Core}(\mathbf{Lat}_{R_v})$.
The genus of $L$ is the fiber

$$
\operatorname{gen}(L) \;=\; \text{fiber over } [\,\mathrm{profile}(L)\,] \text{ of }\;
\pi_0 \operatorname{Core}(\mathbf{Lat}_{\mathbb{Z}}) \longrightarrow \pi_0 \prod_v \operatorname{Core}(\mathbf{Lat}_{R_v}),
$$

a **set-level** pullback: two lattices are in one genus exactly when their local profiles agree up to isometry, equivalently when they become isometric adelically.
If the genus *groupoid* is wanted, it is the classical adelic double coset with restricted products doing real work; $\pi_0$ does not commute with homotopy pullbacks, and the 1-truncation is the content.
:::

*Seated rulings:* [genus is set-level](Settled-Mathematical-Rulings.md#invariants-and-their-evaluation).

## Constructors {#sec-constructors}

The generation calculus uses a fixed small set of category-level constructors, each a standard construction applied — never a new notion:

- $\operatorname{El}$ — the category of elements (Grothendieck construction) of a presheaf, generating the form categories of @sec-forms;

- $\operatorname{Core}$ — the maximal subgroupoid, generating isometry groupoids (@sec-isometry) and the domains of core-sited functors (@sec-discriminant, @sec-genus-sec);

- $\pi_0$ — connected components, landing invariants at the set level (@sec-genus-sec);

- pullback of a replete full subcategory along a functor — the transport rule (@def-transport-property);

- intersection of replete full subcategories — derived nodes (@def-derived-expressions).

(Co)limits, products, and coproducts are sited once at the category-theory level with concrete categories as instances; universal-property witnesses are identification obligations, not constructors.

*Seated rulings:* [(co)limits are sited at the category-theory level](Settled-Mathematical-Rulings.md#invariants-and-their-evaluation) · [cardinality is total on Sets](Settled-Mathematical-Rulings.md#invariants-and-their-evaluation).
