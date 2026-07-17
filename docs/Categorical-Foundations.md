---
title: "Categorical Foundations"
---

The [Mathematical Definitions](Mathematical-Definitions.html) build every object of the
program from a small fixed set of categorical constructions. This page pins each one: the
**precise variant** the program relies on (where a naive choice gives the wrong answer),
the **canonical citation**, and the **downstream definition** that consumes it. A
construction earns an entry here exactly when a wrong convention would silently corrupt a
theorem downstream — bare familiarity is not the bar; *auditability of the exact variant*
is.

Citations are drawn from the declared corpus (nLab, the Stacks Project, standard texts,
Mathlib as anchor). Per the [Style Guide](Mathematical-Language-Style-Guide.html) P1b,
Mathlib names appear only as code-formatted anchors, never as prose nouns. Bracketed codes
such as [`001D`](https://stacks.math.columbia.edu/tag/001D) are Stacks Project tags.

Two constructions are not citation lines but **full statements**, because in each the
naive construction gives the wrong answer and the correction is exactly what makes a
program ruling true: the isofibration/pseudo-pullback compatibility (§F.2) and the
$\pi_0$ fiber sequence (§F.3). A third, the composite $\operatorname{El}$ convention
(§F.4), is stated in full because Definition 3.2 turns on it.

## F.1 Index

| Construction | Consumed by |
|---|---|
| Category of elements $\operatorname{El}(P)$ | Def. 3.2 — $\mathcal B_{R,W},\ \mathcal Q_{R,W}$ |
| Grothendieck construction (fibration form) | §7.1 bitorsors, §8 genus |
| Replete (strictly full) subcategory | Def. 2.1, §3.3, §5 |
| Inverse image of an object property | Def. 2.2, every derived category in §5 |
| Pullback in $\mathbf{Cat}$ (§F.2) | Def. 2.2, 5.3, 5.5 |
| Stuff / structure / property | Def. 2.5; Style Guide P3–P4 |
| Core $\operatorname{Core}(\mathcal C)$ | §6.1, §7.1, §8 |
| Automorphism-group functor $\operatorname{Aut}$ | §7.1–7.2 |
| Torsor / bitorsor | §7.1 |
| $\pi_0$ (§F.3) | §8 genus, §9 |
| Opposite category, and $\operatorname{El}$ (§F.4) | Def. 3.2 |
| Limits / colimits (sited once) | §9 |
| Abelian category | §1.2, §6 |

## F.2 The constructions

**Category of elements.** For a presheaf $P\colon \mathcal C^{\mathrm{op}}\to\mathbf{Set}$,
the *category of elements* $\operatorname{El}(P)$ has as objects the pairs $(M, b)$ with
$M$ an object of $\mathcal C$ and $b\in P(M)$, and as a morphism $(M,b_M)\to(N,b_N)$ a
morphism $f\colon M\to N$ of $\mathcal C$ satisfying $P(f)(b_N)=b_M$ — writing $P(f)=f^*$,
the condition $f^*b_N=b_M$. The projection $(M,b)\mapsto M$ is a functor
$\operatorname{El}(P)\to\mathcal C$ (covariant, and a discrete fibration). The program's
$\mathcal B_{R,W}$ and $\mathcal Q_{R,W}$ are instances; the exact composite with $(-)^{\mathrm{op}}$
is fixed once in §F.4, because the two constructions each reverse variance and a careless
composite cancels. *Citation:* nLab, *category of elements*; Riehl,
*Category Theory in Context* §2.4; Mac Lane–Moerdijk, *Sheaves in Geometry and Logic* I.5.
Mathlib anchor: `CategoryTheory.CategoryOfElements` (whose `Functor.Elements` is the
covariant elements of a functor $\mathcal C\to\mathbf{Set}$).

**Grothendieck construction.** More generally, the Grothendieck construction realizes the
equivalence between pseudofunctors $\mathcal C^{\mathrm{op}}\to\mathbf{Cat}$ and fibrations
over $\mathcal C$; the category of elements is its discrete (i.e. $\mathbf{Set}$-valued)
special case. The program invokes the fibration picture only where a form category is read
as fibred over $\mathrm{Mod}_R$ (§7.1 bitorsors, §8 genus). **Boundary:** the program stays
strictly $1$-categorical here; the $\infty$-categorical straightening/unstraightening is
*not* invoked, and reaching for it would be a level-inflation error of the kind §F.3
guards against. *Citation:* Stacks Project, *Categories*, fibred categories, e.g.
[`003S`](https://stacks.math.columbia.edu/tag/003S) (categories fibred in groupoids);
nLab, *Grothendieck construction*.

**Replete (strictly full) subcategory.** A *replete full* — equivalently *strictly full* —
subcategory is a full subcategory whose objects form an isomorphism-closed class;
equivalently it is cut out by an isomorphism-invariant predicate on objects. This is the
meaning the program assigns to the arrow $\hookrightarrow$: an axiom (Def. 2.1) is such an
inclusion, and every membership claim is a factorization through it. *Citation:* Stacks
Project [`001D`](https://stacks.math.columbia.edu/tag/001D) (subcategory / full / strictly
full); nLab, *replete subcategory*. Mathlib anchor: `CategoryTheory.ObjectProperty` and
its full-subcategory construction.

**Inverse image of an object property.** For a functor $F\colon\mathcal C\to\mathcal D$
and a replete full $\mathcal D.P\hookrightarrow\mathcal D$, the *inverse image*
$\mathcal C\times_{\mathcal D}\mathcal D.P$ is the full subcategory of $\mathcal C$ on the
objects $X$ with $FX\in\mathcal D.P$. This is the pullback that Definition 2.2 uses to
*transport* a property along $F$, and it is the sole mechanism by which any derived
category in §5 acquires its defining conditions. *Citation:* nLab, *replete subcategory*
(pullback-stability); Mathlib anchor: `ObjectProperty.inverseImage`. The *legality* of a
given transport — that $P$ actually factors through the forgetful data $F$ sees — is a
separate ruling (see [Settled Rulings](Settled-Mathematical-Rulings.html); the
finitely-generated predicate is the boundary counterexample).

**Pullback in $\mathbf{Cat}$.** The strict pullback of categories is
equivalence-invariant **only** along isofibrations; for the non-full classifiers that
present *structure* it must be replaced by the pseudo-pullback. This is not a citation
line but a statement the program depends on; it is established in §F.3.1 below.

**Stuff, structure, property.** Given a classifier $\iota_A\colon\mathcal C.A\to\mathcal C$,
the trichotomy is *computed*, not declared: $\iota_A$ full and faithful makes $A$ a
**property** (each fibre is empty or contractible, so "$A$ holds" is a proposition);
$\iota_A$ merely faithful makes $A$ a **structure**; a general $\iota_A$ forgets **stuff**.
That "a property is a proposition" is then a *lemma* of fullness, not a convention.
*Citation:* Baez–Shulman, *Lectures on $n$-Categories and Cohomology* §2 (the canonical
source); nLab, *stuff, structure, property*. This is the content behind Def. 2.5 and
Style Guide P3–P4.

**Core.** The *core* $\operatorname{Core}(\mathcal C)$ is the maximal subgroupoid — all
objects, only the isomorphisms — and is the right adjoint to the inclusion
$\mathbf{Grpd}\hookrightarrow\mathbf{Cat}$, hence functorial. Its functoriality is precisely
why §6.1 can site the discriminant construction on cores: the assignment is functorial for
isometries even though it is not for arbitrary form-preserving maps. *Citation:* nLab,
*core (of a category)*; Mathlib anchor: `CategoryTheory.Core`.

**Automorphism-group functor.** $\operatorname{Aut}\colon\operatorname{Core}(\mathcal C)\to\mathbf{Grp}$
is a functor; $O(X):=\operatorname{Aut}(X)$ is therefore an *instance* of a generic
construction, never a primitive node, and the induced $O(L)\to O(q_L)$ is the whiskering of
$\operatorname{Aut}$ along the discriminant functor. *Citation:* nLab, *automorphism group*.

**Torsor and bitorsor.** A $(G,H)$-*bitorsor* is a set carrying commuting principal (free
and transitive) left $G$- and right $H$-actions. When nonempty, $\operatorname{Isom}(L,M)$
is an $(O(L),O(M))$-bitorsor; principality is the mathematical content of the claim.
*Citation:* nLab, *torsor* and *bitorsor*; Breen, *Bitorseurs et cohomologie non
abélienne*.

**$\pi_0$.** The connected-components functor $\pi_0\colon\mathbf{Grpd}\to\mathbf{Set}$ is
left adjoint to the discrete embedding and **does not preserve pullbacks**. This
non-preservation is exactly what makes the genus a set-level object; it is established in
§F.3.2. *Citation:* nLab, *connected components*.

**Limits and colimits.** The standard (co)limit notions are sited once, at the level of an
arbitrary category; each concrete instance then owes a *cited* isomorphism to that sited
construction — the "identification obligation" of §9 — rather than a re-definition.
$\mathrm{Mod}_R$, $\mathbf{Ab}$, and the form categories are complete and cocomplete.
*Citation:* Riehl ch. 3; module facts in Weibel, *An Introduction to Homological Algebra*
ch. 1–2; Mathlib anchor: `CategoryTheory.Limits`.

**Abelian category.** The ambient for the §6 exact sequences, and the boundary case for
property-vs-structure. An abelian category is an additive category with all kernels and
cokernels in which coimage and image agree
([`0109`](https://stacks.math.columbia.edu/tag/0109), Def. 12.5.1). Its additive
($\mathbf{Ab}$-enriched) structure is **property-like**: it is unique when it exists,
recovered from the finite biproducts every abelian category has (a category with finite
biproducts carries a canonical, unique commutative-monoid enrichment; when the hom-monoids
are groups this is the $\mathbf{Ab}$-enrichment). So *being abelian* is a **property** of
the bare category — no data is chosen — which is the reading Definition 2.5 needs. The
functors that make the §6 machinery functorial, however, are the **additive/exact** ones,
and abelian categories with exact functors form a subcategory of $\mathbf{Cat}$ that is
**not full**; this is the sense in which "abelian" is *structure*, and it is why Mathlib's
`CategoryTheory.Abelian` extends `CategoryTheory.Preadditive`
([`09SE`](https://stacks.math.columbia.edu/tag/09SE), preadditive/additive categories).
The two readings do not conflict once the morphisms are named: membership is a property
(unique enrichment), while the enrichment-preserving functors are a non-full class, so any
consumer of the exact-sequence machinery names that class as its section (§F.3.1, P4).

## F.3.1 Pullback in $\mathbf{Cat}$: isofibrations and pseudo-pullback

**Why this needs establishing.** Definition 2.2 transports a property by the strict
pullback $\mathcal C\times_{\mathcal D}\mathcal D.P$, and §5 builds every headline category
as such a pullback. But the strict pullback in $\mathbf{Cat}$ is **not** invariant under
equivalence of its input functors: replacing a leg by an equivalent functor can change the
strict pullback by more than an equivalence. Since the whole program is stated up to
equivalence (O5), an uncorrected strict pullback is ill-defined data.

**The correction.** A functor $p\colon\mathcal E\to\mathcal D$ is an **isofibration** when
every isomorphism $d\cong p(e)$ in $\mathcal D$ lifts to an isomorphism out of $e$ in
$\mathcal E$. The relevant facts:

- Strict pullback along an isofibration **is** equivalence-invariant, and coincides with
  the pseudo-pullback. (nLab, *isofibration* and *pseudopullback*; Johnstone, *Sketches of
  an Elephant* B1.1.)
- **Replete full inclusions are isofibrations.** Hence for *properties* — Def. 2.1, all of
  §3.3, and every §5 pullback along a property classifier — the strict pullback of
  Definition 2.2 is legitimate exactly as written. This is the theorem that licenses the
  program's notation.
- **Structure classifiers are not full**, so their legs are not covered by the above. For
  these — the monoidal structures $\otimes,\oplus$ and the orthogonal sum $\perp$ of Def.
  2.5, and abelian-over-preadditive — the correct construction is the **pseudo-pullback**
  ($2$-pullback). (nLab, *2-pullback*; Stacks $2$-fibre-product material, e.g.
  [`02XA`](https://stacks.math.columbia.edu/tag/02XA).)

**Ruling induced.** Read Definition 2.2 as: a pullback along a *property* classifier is
strict (equivalently pseudo, by the isofibration fact); a pullback along a *structure*
classifier is pseudo. The notation need not case-split, but §5.5 (DiscQuad as a pullback
along the bilinearization $\beta$) and every structure-consumer are read in the pseudo
sense. This is the compatibility the Definitions page otherwise assumes silently, and it is
forced by the "everything up to equivalence" premise (O5), which is why it is not optional.

## F.3.2 $\pi_0$ and the fiber sequence: why genus is set-level

**Why this needs establishing.** Definition 8 rules that the genus is a **set-level**
pullback and that $\pi_0$ does not commute with homotopy pullbacks. That is a theorem about
$\pi_0$, asserted on the Definitions page without grounding; left ungrounded, "genus" could
be read as a groupoid pullback, which produces an uncountable object (the error of earlier
drafts).

**The statement.** Let
$\operatorname{Loc}\colon\operatorname{Core}(\mathbf{Lat}_{\mathbb Z})\to\prod_v\operatorname{Core}(\mathbf{Lat}_{R_v})$
be the local-profile functor of groupoids. For a point $L$ there is a fiber sequence of
groupoids
$$
\operatorname{hofib}_{[L]}\longrightarrow \operatorname{Core}(\mathbf{Lat}_{\mathbb Z})
\xrightarrow{\ \operatorname{Loc}\ } \textstyle\prod_v\operatorname{Core}(\mathbf{Lat}_{R_v}),
$$
inducing the exact sequence of pointed sets
$$
\pi_1\!\Big(\textstyle\prod_v\operatorname{Core}(\mathbf{Lat}_{R_v}),\,\operatorname{Loc} L\Big)
\longrightarrow \pi_0(\operatorname{hofib}_{[L]})
\longrightarrow \pi_0\operatorname{Core}(\mathbf{Lat}_{\mathbb Z})
\longrightarrow \pi_0\!\textstyle\prod_v\operatorname{Core}(\mathbf{Lat}_{R_v}).
$$

The **genus** of $L$ is the fibre of the *right-hand* map — a map of sets — over the point
$\operatorname{Loc}(L)$ read in the codomain: the set of global isometry classes with the
same local profile as $L$ at every place. It is **pointed**, hence nonempty: it contains
$[L]$ by construction. Pointedness must be asserted, since an abstract fibre of a
$\pi_0$-map can be empty.

**The non-commutation.** $\pi_0(\operatorname{hofib})$ is generally **not** the genus: it
carries extra orbit data from $\pi_1$ of the base — concretely, over $[L]$ its components
are $O(L)\backslash\prod_v O(L_v)$, typically uncountable. So $\pi_0$ of the homotopy fibre
differs from the fibre of $\pi_0$; this is the non-preservation of pullbacks by $\pi_0$, and
it is why the genus is the set-level object rather than the groupoid one. If the genus
*groupoid* is ever wanted, it is the classical adelic double coset (with restricted products
doing essential work); the $1$-truncation is the content. *Citation:* May, *A Concise
Course in Algebraic Topology* (the fibration exact sequence of pointed sets); nLab, *fiber
sequence*; for the arithmetic double coset, Cassels, *Rational Quadratic Forms*, or
Conway–Sloane, *Sphere Packings, Lattices and Groups* [@CS10, ch. 15].

## F.4 The composite convention $\operatorname{El}$ (adopted)

Definition 3.2 forms the category of elements of a presheaf. Because $\operatorname{El}$
and $(-)^{\mathrm{op}}$ each reverse variance, an $\operatorname{El}(\cdot)^{\mathrm{op}}$
composite is ambiguous — under one reading the two reversals cancel — and the convention
must be fixed once, end to end.

**Adopted.** $\mathcal B_{R,W}:=\operatorname{El}(\operatorname{Bil}_{R,W})$, the category of
elements of the presheaf in the standard sense above (nLab; Riehl §2.4): objects $(M,b_M)$
with $b_M\in\operatorname{Bil}_{R,W}(M)$; a morphism $(M,b_M)\to(N,b_N)$ a module map
$f\colon M\to N$ with $f^*b_N=b_M$; covariant projection $\pi\colon\mathcal B_{R,W}\to\mathrm{Mod}_R$.
**No $(-)^{\mathrm{op}}$.** Likewise for $\mathcal Q_{R,W}$.

This is **forced, not preferred.** The defining datum of an object is the $W$-valued form
(O2), and a morphism of forms is a module map that pulls the target form back to the source
(O3, "restriction pulls back forms"); that is exactly the covariant category of elements
with projection to $\mathrm{Mod}_R$. Definition 3.2 is edited to match, and every use of the
morphism law cites this convention.

*Relation to the Mathlib anchor.* `CategoryTheory.Functor.Elements` is the *covariant*
category of elements of a functor $\mathcal C\to\mathbf{Set}$. Applied to the presheaf
$\operatorname{Bil}\colon\mathrm{Mod}_R^{\mathrm{op}}\to\mathbf{Set}$ it lives over
$\mathrm{Mod}_R^{\mathrm{op}}$, so the presheaf-elements used here is its opposite. An earlier
phrasing ("the opposite of Mathlib's covariant `Functor.Elements`") named the *same*
category by the Mathlib baseline; this page fixes the nLab baseline instead, so the
morphism law can be read straight off $\operatorname{El}$ with no compensating
$(-)^{\mathrm{op}}$, removing the double-variance hazard.
