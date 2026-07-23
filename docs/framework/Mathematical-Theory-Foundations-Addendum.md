---
title: "Addendum: Adjunctions, Free Objects, Essential Images, and Reflective Localizations"
subtitle: "Free module and algebra functors, restrictions and corestrictions, sheafification, and the Sage algebra construction"
date: 2026-07-23
status: "Normative mathematical addendum; supersedes informal descriptions of free constructions and functor images"
---

# Addendum: Adjunctions, Free Objects, Essential Images, and Reflective Localizations

## Status and scope

This addendum supplies general theory that was absent from *Mathematical Foundations of the Categorical Research Language*. It treats adjunctions, free objects, free algebraic constructions, essential images, restrictions of domain, corestrictions of codomain, reflective localizations, and functors obtained from these constructions by composition. It also gives the mathematical interpretation of Sage's functorial construction named `Algebras`.

The constructions treated in this addendum are named individually:

- the free monoid functor;
- the free group functor;
- the free abelian group functor;
- the free left \(R\)-module functor;
- the tensor algebra functor;
- the free associative \(R\)-algebra functor;
- the symmetric algebra functor;
- the free commutative \(R\)-algebra functor;
- the monoid algebra functor;
- the group algebra functor;
- sheafification and stackification.

These functors have different domains, codomains, universal properties, and essential images. They are not instances of an additional unnamed construction.

Throughout, the ambient universe is the universe-stratified \((\infty,2)\)-category \(\mathfrak{Cat}\) fixed in the foundations report. Mapping objects are \(\infty\)-categories. All definitions specialize to ordinary categories by truncation. Rings are associative and unital and ring homomorphisms preserve the unit. Whenever tensor products of left modules or bialgebras are used, the base ring \(R\) is commutative unless another monoidal base has been specified.

Standard references include Mac Lane, *Categories for the Working Mathematician*; Riehl, *Category Theory in Context*; Lurie, *Higher Algebra*; Kerodon, especially its treatments of adjunctions, essential images, Kan extensions, and localizations; the Stacks Project sections on sheafification, functoriality of presheaves, and free abelian sheaves; and standard texts on associative, commutative, and Hopf algebras such as Bourbaki, Sweedler, and Montgomery.

***

# Part I. Adjunctions and free objects

## 1. Adjunctions

### Definition 1.1 (Adjunction) {#def-adjunction}

Let \(\mathcal C,\mathcal D\in\mathfrak{Cat}\), and let
\[
F:\mathcal C\longrightarrow\mathcal D,
\qquad
U:\mathcal D\longrightarrow\mathcal C.
\]
An **adjunction** \(F\dashv U\) consists of a unit and a counit
\[
\eta:\operatorname{id}_{\mathcal C}\Longrightarrow UF,
\qquad
\varepsilon:FU\Longrightarrow\operatorname{id}_{\mathcal D},
\]
together with the standard coherent triangle identities. Equivalently, it consists of natural equivalences of mapping spaces
\[
\operatorname{Map}_{\mathcal D}(F X,Y)
\simeq
\operatorname{Map}_{\mathcal C}(X,UY)
\]
for \(X\in\mathcal C\) and \(Y\in\mathcal D\).

The functor \(F\) is the **left adjoint** and \(U\) is the **right adjoint**. The notation does not imply that \(U\) is forgetful. When \(U\) is a displayed projection from structured objects to their underlying objects, it is also called the forgetful functor.

### Lemma 1.2 (Composition of adjunctions) {#lem-composition-adjunctions}

Suppose
\[
F_1:\mathcal C\rightleftarrows\mathcal D:U_1,
\qquad
F_2:\mathcal D\rightleftarrows\mathcal E:U_2
\]
are adjunctions with \(F_i\dashv U_i\). Then
\[
F_2F_1\dashv U_1U_2.
\]

**Proof.** There are natural equivalences
\[
\operatorname{Map}_{\mathcal E}(F_2F_1X,Z)
\simeq
\operatorname{Map}_{\mathcal D}(F_1X,U_2Z)
\simeq
\operatorname{Map}_{\mathcal C}(X,U_1U_2Z).
\]
The coherent version follows from composition in the ambient \((\infty,2)\)-category. \(\square\)

### Definition 1.3 (Monad and comonad of an adjunction) {#def-monad-comonad-adjunction}

An adjunction \(F\dashv U\) determines a monad
\[
T:=UF
\]
on \(\mathcal C\) and a comonad
\[
G:=FU
\]
on \(\mathcal D\). The multiplication of \(T\) and comultiplication of \(G\) are induced by the counit and unit, respectively.

When \(U\) is monadic, \(\mathcal D\) is equivalent to the category of algebras for \(T\). The category of all \(T\)-algebras must not be identified with the essential image of the free functor \(F\): the latter consists only of free \(T\)-algebras.

### Remark 1.4 (Existence versus a chosen adjunction)

The assertion that a functor admits a left or right adjoint is property-like. A specified adjunction includes the adjoint functor, unit, counit, and coherent triangle data. In the foundations terminology, the category of chosen adjunctions over a fixed functor can have a nontrivial presentation even though adjoints, when they exist, are unique up to a contractible space of choices.

## 2. Free objects

### Definition 2.1 (Free object on a specified object) {#def-free-object-on-X}

Let \(F\dashv U\) be an adjunction. For \(X\in\mathcal C\), the object \(F(X)\in\mathcal D\), together with the unit map
\[
\eta_X:X\longrightarrow U(FX),
\]
is the **free \(\mathcal D\)-object on \(X\)** relative to the adjunction.

Its defining property is
\[
\operatorname{Map}_{\mathcal D}(FX,Y)
\simeq
\operatorname{Map}_{\mathcal C}(X,UY).
\]
The phrase “free on \(X\)” includes the specified generating object \(X\) and the universal map \(\eta_X\).

### Definition 2.2 (Free object) {#def-free-object-essential-image}

An object \(Y\in\mathcal D\) is **free relative to \(F\dashv U\)** if there exists \(X\in\mathcal C\) and an equivalence
\[
FX\simeq Y.
\]
Thus the free objects form the essential image of \(F\).

This is an existence statement. It does not select \(X\), an equivalence \(FX\simeq Y\), a basis, a family of generators, or any other presentation.

### Definition 2.3 (Chosen free presentation) {#def-chosen-free-presentation}

A **chosen free presentation** of \(Y\in\mathcal D\) is a pair
\[
(X,\phi),
\qquad
\phi:FX\overset{\sim}{\longrightarrow}Y.
\]
For a fixed \(Y\), chosen free presentations form the homotopy fiber of the induced map on cores
\[
F^{\simeq}:\mathcal C^{\simeq}\longrightarrow\mathcal D^{\simeq}
\]
over \(Y\).

The property that \(Y\) is free is the propositional truncation of the assertion that this fiber is inhabited. A chosen free presentation is structure, while freeness is a property.

### Remark 2.4 (The counit does not characterize free objects)

For a general free-forgetful adjunction, a free object \(Y\) need not satisfy
\[
\varepsilon_Y:F(UY)\overset{\sim}{\longrightarrow}Y.
\]
For example, if \(Y\) is a free \(R\)-module, \(F(UY)\) is the free module on the set of **all elements** of \(Y\), not the free module on a chosen basis. The counit is therefore almost never an isomorphism.

Fixed points of the unit or counit characterize reflective or coreflective localizations, not arbitrary free objects.

***

# Part II. Essential images, restrictions, and corestrictions

## 3. Essential images

### Definition 3.1 (Essential image) {#def-essential-image}

Let
\[
F:\mathcal C\longrightarrow\mathcal D
\]
be a functor. The **essential image** \(\operatorname{EssIm}(F)\) is the full replete subcategory of \(\mathcal D\) spanned by the objects equivalent to \(F(C)\) for some \(C\in\mathcal C\).

There is a factorization
\[
\mathcal C
\xrightarrow{F_{\mathrm{ess}}}
\operatorname{EssIm}(F)
\xrightarrow{j_F}
\mathcal D,
\]
where \(F_{\mathrm{ess}}\) is essentially surjective and \(j_F\) is fully faithful and replete.

This is the standard essential-image factorization of a functor. It is invariant under equivalence of categories and functors.

### Proposition 3.2 (Universal property of the essential image) {#prop-essential-image-universal}

Let \(i:\mathcal E\hookrightarrow\mathcal D\) be a replete full subcategory. If \(F\) factors through \(i\), then \(\operatorname{EssIm}(F)\) factors through \(\mathcal E\). Equivalently, \(\operatorname{EssIm}(F)\) is the least replete full subcategory of \(\mathcal D\) through which \(F\) factors.

The word “least” here abbreviates the displayed factorization property; it is not a claim that all classifier morphisms form a subobject lattice.

### Remark 3.3 (The source is not its essential image)

The functor
\[
F_{\mathrm{ess}}:\mathcal C\to\operatorname{EssIm}(F)
\]
is essentially surjective but need not be full or faithful. Consequently:

1. \(\mathcal C\) records the morphisms between input presentations;
2. \(\operatorname{EssIm}(F)\) contains all morphisms in \(\mathcal D\) between objects in the image;
3. the two categories are equivalent only under an additional theorem, for example when \(F\) is fully faithful.

This distinction is essential for free modules with chosen bases and for monoid algebras. A constructor category and the full category spanned by its values generally have different morphisms.

### Definition 3.4 (Presentation space of a functor value) {#def-presentation-space-functor}

For \(Y\in\mathcal D\), define
\[
\operatorname{Pres}_F(Y)
:=
\operatorname{hofib}_Y
\left(
F^{\simeq}:\mathcal C^{\simeq}\to\mathcal D^{\simeq}
\right).
\]
Its points are pairs \((X,\phi)\) with \(\phi:FX\simeq Y\), and its paths are equivalences of such presentations.

Then
\[
Y\in\operatorname{EssIm}(F)
\quad\Longleftrightarrow\quad
\left\|\operatorname{Pres}_F(Y)\right\|_{-1}
\text{ is inhabited}.
\]
Thus the essential image is the property obtained by propositionally truncating the category or space of chosen presentations.

## 4. Restriction of domain and corestriction of codomain

### Definition 4.1 (Precomposition) {#def-precomposition}

Given
\[
H:\mathcal C'\longrightarrow\mathcal C,
\qquad
F:\mathcal C\longrightarrow\mathcal D,
\]
the composite
\[
F\circ H:\mathcal C'\longrightarrow\mathcal D
\]
is obtained by **precomposition** with \(H\). When \(H\) is an inclusion, it is also called the restriction of \(F\) to \(\mathcal C'\).

For a general functor \(H\), “precomposition” is the unambiguous term. No inclusion is implied.

### Definition 4.2 (Corestriction) {#def-corestriction}

Let
\[
i:\mathcal D'\hookrightarrow\mathcal D
\]
be fully faithful. A **corestriction** of \(F:\mathcal C\to\mathcal D\) to \(\mathcal D'\) is a functor
\[
\overline F:\mathcal C\longrightarrow\mathcal D'
\]
together with an equivalence
\[
i\overline F\simeq F.
\]

A corestriction is therefore a factorization of the codomain. It is not obtained merely by changing the written codomain. Its existence is a mathematical assertion, and its specified factorization is data.

### Definition 4.3 (Inverse image of a classifier) {#def-inverse-image-classifier-functor}

Let \(q:\mathcal D.Q\to\mathcal D\) be a classifier and let \(F:\mathcal C\to\mathcal D\). The inverse image of \(q\) along \(F\) is the homotopy pullback
\[
\mathcal C.Q
:=
\mathcal C\times^h_{\mathcal D}\mathcal D.Q.
\]
It classifies pairs consisting of an object \(C\in\mathcal C\) and a chosen \(Q\)-lift of \(F(C)\).

This construction differs from corestriction. The inverse image may have only some objects of \(\mathcal C\), or may add choices over each object. A corestriction exists only when the entire functor \(F\) has been lifted through \(q\).

### Proposition 4.4 (Restriction of an adjunction) {#prop-restriction-adjunction}

Suppose \(F\dashv U\) and suppose
\[
j:\mathcal C'\hookrightarrow\mathcal C,
\qquad
i:\mathcal D'\hookrightarrow\mathcal D
\]
are fully faithful. Assume that there are corestrictions
\[
F':\mathcal C'\longrightarrow\mathcal D',
\qquad
U':\mathcal D'\longrightarrow\mathcal C'
\]
with
\[
iF'\simeq Fj,
\qquad
jU'\simeq Ui,
\]
and that the unit and counit of \(F\dashv U\) factor through these corestrictions. Then
\[
F'\dashv U'.
\]

Equivalently, the original mapping-space adjunction restricts to
\[
\operatorname{Map}_{\mathcal D'}(F'X,Y)
\simeq
\operatorname{Map}_{\mathcal C'}(X,U'Y).
\]

### Remark 4.5 (One-sided preservation is insufficient)

If \(F\) maps \(\mathcal C'\) into \(\mathcal D'\), it does not follow that the restricted functor has right adjoint \(U|_{\mathcal D'}\). The right adjoint must also preserve the selected subcategories, and the unit and counit must land there.

Likewise, precomposition of a left adjoint with an arbitrary functor need not remain a left adjoint. This point is load-bearing for Sage's `Algebras` construction: composing the free \(R\)-module functor with an arbitrary functor \(\mathcal C\to\mathbf{Set}\) produces a functor, but not automatically an adjunction.

## 5. Mates and base-change transformations

### Definition 5.1 (Mate of a natural transformation) {#def-mate-transformation}

Consider a square
\[
\begin{CD}
\mathcal C' @>{F'}>> \mathcal D'\\
@V{u}VV @VV{v}V\\
\mathcal C @>{F}>> \mathcal D
\end{CD}
\]
and a natural transformation
\[
\alpha:vF'\Longrightarrow Fu.
\]
If some or all of the functors admit adjoints, adjunction converts \(\alpha\) into corresponding natural transformations between composites of those adjoints. These are the **mates** of \(\alpha\).

A square satisfies the appropriate **Beck--Chevalley condition** when the relevant mate is an equivalence. This is the standard language for asking whether restriction, extension, pullback, pushforward, sheafification, or base change commute.

### Remark 5.2

Statements such as “the restricted free functor agrees with base change,” “sheafification commutes with inverse image,” or “extension of scalars preserves a chosen construction” should be formulated by a specified comparison transformation and, when true, the assertion that its mate is an equivalence. They are not consequences of shared notation.

***

# Part III. Reflective localizations and sheafification

## 6. Reflective localizations

### Definition 6.1 (Reflective localization) {#def-reflective-localization}

A full subcategory
\[
i:\mathcal D\hookrightarrow\mathcal C
\]
is **reflective** if \(i\) admits a left adjoint
\[
L:\mathcal C\longrightarrow\mathcal D.
\]
The composite
\[
\ell:=iL:\mathcal C\longrightarrow\mathcal C
\]
is the associated localization endofunctor.

The right adjoint \(i\) is fully faithful, so the counit
\[
Li\Longrightarrow\operatorname{id}_{\mathcal D}
\]
is an equivalence. The monad \(\ell=iL\) is idempotent.

### Proposition 6.2 (Local objects) {#prop-local-objects}

For \(X\in\mathcal C\), the following are equivalent:

1. \(X\) belongs to the essential image of \(i\);
2. the unit \(X\to iLX\) is an equivalence;
3. \(X\) is fixed by the localization endofunctor \(\ell\), up to equivalence.

Thus reflective localizations are precisely the setting in which the unit characterizes the selected objects.

### Remark 6.3 (Free objects are not generally local objects)

For a general free-forgetful adjunction \(F\dashv U\), the right adjoint \(U\) is not fully faithful. The essential image of \(F\) is therefore not generally a reflective subcategory, and free objects are not characterized as fixed points of \(FU\) or \(UF\).

### Proposition 6.4 (Composition with a reflector) {#prop-free-functor-reflector}

Let
\[
F:\mathcal C\rightleftarrows\mathcal D:U
\]
be an adjunction, and let
\[
L:\mathcal D\rightleftarrows\mathcal D':i
\]
be a reflective localization, with \(L\dashv i\). Then
\[
LF:\mathcal C\rightleftarrows\mathcal D':Ui
\]
is an adjunction.

**Proof.** This is Lemma 1.2 applied to the two adjunctions. \(\square\)

If \(F\) admits a corestriction \(\overline F:\mathcal C\to\mathcal D'\), then the counit equivalence \(Li\simeq\operatorname{id}_{\mathcal D'}\) gives a canonical equivalence
\[
LF\simeq\overline F.
\]
Without a reflector and without a corestriction theorem, the data of \(F:\mathcal C\to\mathcal D\) do not determine a functor \(\mathcal C\to\mathcal D'\).

## 7. Sheafification and stackification

### Theorem 7.1 (Sheafification) {#thm-sheafification-adjunction}

Let \((\mathcal C,J)\) be a site. The inclusion
\[
i_J:\operatorname{Sh}(\mathcal C,J)
\hookrightarrow
\operatorname{PSh}(\mathcal C)
\]
admits a left exact left adjoint
\[
a_J:\operatorname{PSh}(\mathcal C)
\longrightarrow
\operatorname{Sh}(\mathcal C,J).
\]
Thus the category of sheaves is a reflective localization of the category of presheaves.

The localization endofunctor is
\[
L_J:=i_Ja_J.
\]
A presheaf \(F\) is a sheaf if and only if the unit
\[
F\longrightarrow i_Ja_JF
\]
is an equivalence.

### Corollary 7.2 (Colimits of sheaves) {#cor-colimits-sheafification}

Colimits of sheaves are computed by taking the colimit in presheaves and then sheafifying:
\[
\operatorname*{colim}_{\operatorname{Sh}}F_i
\simeq
 a_J\left(
 \operatorname*{colim}_{\operatorname{PSh}}i_JF_i
 \right).
\]
This follows because sheafification is a left adjoint.

### Theorem 7.3 (Stackification) {#thm-stackification-adjunction}

Under the standard size hypotheses, the inclusion of stacks in prestacks admits a left adjoint, called **stackification**. In the higher-categorical formulation, stackification is sheafification for space-valued presheaves. Ordinary stacks in groupoids are obtained by the appropriate truncation.

### Definition 7.4 (Free abelian presheaf and free abelian sheaf) {#def-free-abelian-sheaf}

For a presheaf of sets \(F\), define the presheaf of abelian groups
\[
\mathbb Z[F](U):=\mathbb Z[F(U)]
\]
objectwise. This is the free abelian presheaf functor and is left adjoint to the objectwise forgetful functor
\[
\operatorname{PAb}(\mathcal C)	o\operatorname{PSh}(\mathcal C).
\]

The **free abelian sheaf** on \(F\) is
\[
\mathbb Z[F]^{\#}:=a_J^{\operatorname{Ab}}\bigl(\mathbb Z[F]\bigr).
\]
It is left adjoint to the underlying-set functor from abelian sheaves to presheaves of sets. Restricting the domain to sheaves of sets gives the corresponding free abelian sheaf functor on sheaves.

The sheafification is essential: the objectwise free abelian presheaf of a sheaf of sets need not already be a sheaf.

### Definition 7.5 (Change of site at the presheaf level) {#def-change-site-presheaf}

For a functor \(u:\mathcal C\to\mathcal D\), precomposition gives
\[
u^p:
\operatorname{PSh}(\mathcal D)
\longrightarrow
\operatorname{PSh}(\mathcal C),
\qquad
G\longmapsto G\circ u.
\]
This functor has left and right Kan extension adjoints under the standard size hypotheses.

Precomposition does not automatically carry sheaves to sheaves. If it does, it admits a corestriction to the sheaf categories. Otherwise the standard sheaf-valued construction is obtained by composing with sheafification, for example
\[
G\longmapsto a_{J_{\mathcal C}}(G\circ u).
\]
Whether sheafification is redundant is a theorem under continuity and cocontinuity hypotheses on \(u\), not a definitional simplification.

***

# Part IV. Standard free algebraic functors

## 8. Free monoids, groups, and abelian groups

### Definition 8.1 (Free monoid and free group) {#def-free-monoid-group}

The forgetful functors
\[
U_{\mathrm{Mon}}:\mathbf{Mon}\to\mathbf{Set},
\qquad
U_{\mathrm{Grp}}:\mathbf{Grp}\to\mathbf{Set}
\]
admit left adjoints
\[
X\longmapsto X^*,
\qquad
X\longmapsto F(X),
\]
the free monoid and free group functors.

The free monoid \(X^*\) consists of finite words in \(X\), including the empty word. The free group \(F(X)\) is characterized by
\[
\operatorname{Hom}_{\mathbf{Grp}}(F(X),G)
\cong
\operatorname{Map}_{\mathbf{Set}}(X,U_{\mathrm{Grp}}G).
\]

### Definition 8.2 (Free abelian group) {#def-free-abelian-group}

The free abelian group functor
\[
\mathbb Z[-]:\mathbf{Set}\longrightarrow\mathbf{Ab}
\]
is left adjoint to the underlying-set functor. It sends \(X\) to the direct sum
\[
\mathbb Z[X]
:=
\bigoplus_{x\in X}\mathbb Z.
\]

This is the special case \(R=\mathbb Z\) of the free \(R\)-module functor.

## 9. The free \(R\)-module functor

### Definition 9.1 (Free left \(R\)-module) {#def-free-R-module-functor}

Let \(R\) be a ring. Define
\[
F_R:\mathbf{Set}\longrightarrow R\text{-}\mathbf{Mod},
\qquad
F_R(X):=R^{(X)}:=\bigoplus_{x\in X}R.
\]
The basis vector indexed by \(x\) is denoted \([x]\).

The underlying-set functor is
\[
U_R:R\text{-}\mathbf{Mod}\longrightarrow\mathbf{Set}.
\]
There is an adjunction
\[
F_R\dashv U_R,
\]
with natural bijection
\[
\operatorname{Hom}_R(R^{(X)},M)
\cong
\operatorname{Map}(X,U_RM).
\]
A function \(f:X\to U_RM\) corresponds to the unique linear map satisfying \([x]\mapsto f(x)\).

### Corollary 9.2 (Free and finite free modules) {#cor-free-finite-free-essential-image}

The essential image of \(F_R\) is the category of free left \(R\)-modules. The essential image of the restriction
\[
F_R|_{\mathbf{FinSet}}:
\mathbf{FinSet}\longrightarrow R\text{-}\mathbf{Mod}
\]
is the category of finite free left \(R\)-modules.

A chosen basis is a presentation \(R^{(X)}\simeq M\); freeness is the propositional truncation of the existence of such a presentation.

### Remark 9.3 (Modules equipped with a basis: two morphism conventions)

There are two standard categories with modules equipped with a basis as objects.

1. If morphisms are arbitrary \(R\)-linear maps, then the free module functor lifts to the category of modules equipped with a basis, and the adjunction with the underlying-set functor remains valid. The chosen basis is structure on objects but imposes no restriction on morphisms.

2. If morphisms are required to carry basis vectors to basis vectors, then the resulting category is equivalent to \(\mathbf{Set}\), with the basis-index set as the inverse construction. Its forgetful functor to the underlying set of the module is not the right adjoint of this equivalence.

Therefore the phrase “modules with basis” never determines the morphisms by itself. Every use must specify whether morphisms are arbitrary linear maps or basis-preserving maps.

## 10. Tensor and symmetric algebras

### Definition 10.1 (Tensor algebra) {#def-tensor-algebra-functor}

Let \(R\) be commutative. The tensor algebra of an \(R\)-module \(M\) is
\[
T_R(M)
:=
\bigoplus_{n\ge0}M^{\otimes_R n},
\qquad
M^{\otimes 0}:=R,
\]
with multiplication by concatenation of tensors.

The tensor algebra functor
\[
T_R:R\text{-}\mathbf{Mod}
\longrightarrow
\mathbf{Alg}_R
\]
is left adjoint to the underlying-module functor
\[
U_{\mathrm{mod}}:\mathbf{Alg}_R\to R\text{-}\mathbf{Mod}.
\]
Here \(\mathbf{Alg}_R\) denotes associative unital \(R\)-algebras.

### Definition 10.2 (Free associative \(R\)-algebra on a set) {#def-free-associative-R-algebra-set}

By composition of adjunctions, the composite
\[
\mathbf{Set}
\xrightarrow{F_R}
R\text{-}\mathbf{Mod}
\xrightarrow{T_R}
\mathbf{Alg}_R
\]
is left adjoint to the underlying-set functor from \(R\)-algebras. Its value on \(X\) is the free associative \(R\)-algebra
\[
R\langle X\rangle:=T_R(R^{(X)}).
\]

As an \(R\)-module, \(R\langle X\rangle\) has basis the free monoid \(X^*\). There is therefore a canonical isomorphism
\[
R\langle X\rangle
\cong
R[X^*],
\]
where the expression on the right is the monoid algebra of the free monoid. This comparison does not identify the free algebra functor on sets with the monoid algebra functor on arbitrary monoids; it relates them after applying the free monoid functor.

### Definition 10.3 (Symmetric algebra and free commutative \(R\)-algebra) {#def-symmetric-algebra}

The symmetric algebra functor
\[
\operatorname{Sym}_R:
R\text{-}\mathbf{Mod}
\longrightarrow
\mathbf{CAlg}_R
\]
is left adjoint to the underlying-module functor from commutative \(R\)-algebras.

The free commutative \(R\)-algebra on a set \(X\) is
\[
R[X]
:=
\operatorname{Sym}_R(R^{(X)}),
\]
the polynomial algebra with variables indexed by \(X\). It is left adjoint to the underlying-set functor
\[
\mathbf{CAlg}_R\to\mathbf{Set}.
\]

The notations \(R[X]\) for a polynomial algebra and \(R[M]\) for a monoid algebra are standard but have different inputs and universal properties. The domain must always be clear.

## 11. Free operadic algebras

### Definition 11.1 (Free \(\mathcal O\)-algebra) {#def-free-operadic-algebra}

Let \(\mathcal V\) be a presentable symmetric monoidal \(\infty\)-category whose tensor product preserves colimits separately, and let \(\mathcal O\) be an \(\infty\)-operad. Under the standard hypotheses, the forgetful functor
\[
U_{\mathcal O}:\operatorname{Alg}_{\mathcal O}(\mathcal V)
\longrightarrow
\mathcal V
\]
admits a left adjoint
\[
\operatorname{Free}_{\mathcal O}:\mathcal V
\longrightarrow
\operatorname{Alg}_{\mathcal O}(\mathcal V).
\]

This is the higher-categorical free-algebra construction. It is distinct from the category \(\operatorname{Alg}_{\mathcal O}(\mathcal V)\) itself and from the essential image of \(\operatorname{Free}_{\mathcal O}\).

### Remark 11.2 (Algebra objects versus free algebras)

The notation \(\operatorname{Alg}_{\mathcal O}(\mathcal V)\) denotes a category of all \(\mathcal O\)-algebra objects. The functor \(\operatorname{Free}_{\mathcal O}\) constructs free objects in that category. Most algebra objects are not free. No category named “algebras” should be interpreted as the image of a free functor unless an explicit theorem says so.

***

# Part V. Monoid algebras, group algebras, and group-like elements

## 12. The free module functor as a strong symmetric monoidal functor

### Proposition 12.1 (Monoidal structure of the free module functor) {#prop-free-module-strong-monoidal}

Let \(R\) be commutative. The free \(R\)-module functor
\[
F_R:(\mathbf{Set},\times,*)
\longrightarrow
(R\text{-}\mathbf{Mod},\otimes_R,R)
\]
is strong symmetric monoidal. The structure equivalences are
\[
R^{(X\times Y)}
\overset{\sim}{\longrightarrow}
R^{(X)}\otimes_RR^{(Y)},
\qquad
[(x,y)]\longmapsto[x]\otimes[y],
\]
and
\[
R^{(*)}\simeq R.
\]

Consequently, for every suitable operad \(\mathcal O\), it induces a functor
\[
\operatorname{Alg}_{\mathcal O}(\mathbf{Set})
\longrightarrow
\operatorname{Alg}_{\mathcal O}(R\text{-}\mathbf{Mod}).
\]

This is the standard mechanism by which a multiplication, unit, commutativity, or other operadic structure on a set is extended \(R\)-multilinearly to the free \(R\)-module.

### Definition 12.2 (Canonical coalgebra on a free module) {#def-canonical-coalgebra-free-module}

Every set \(X\) is canonically a cocommutative comonoid in \((\mathbf{Set},\times)\), with diagonal and terminal map
\[
X\longrightarrow X\times X,
\qquad
X\longrightarrow *.
\]
Applying the strong symmetric monoidal functor \(F_R\) gives a cocommutative coalgebra structure on \(R^{(X)}\):
\[
\Delta([x])=[x]\otimes[x],
\qquad
\varepsilon([x])=1.
\]
For every \(x\in X\), the canonical generator \([x]\) is group-like.

This coalgebra structure is additional to the free-module adjunction but is canonically induced by the cartesian comonoid structure of a set.

## 13. Monoid and group algebras

### Definition 13.1 (Monoid algebra functor) {#def-monoid-algebra-functor}

Let \(M\) be a monoid. Its monoid algebra is the free \(R\)-module
\[
R[M]:=R^{(M)}
\]
with multiplication and unit
\[
[m]\,[n]=[mn],
\qquad
1=[1_M].
\]
The construction is functorial:
\[
R[-]:\mathbf{Mon}\longrightarrow\mathbf{Alg}_R.
\]

Together with the coalgebra of Definition 12.2, \(R[M]\) is a bialgebra:
\[
\Delta([m])=[m]\otimes[m],
\qquad
\varepsilon([m])=1.
\]
Hence there is a canonical lift
\[
R[-]:\mathbf{Mon}\longrightarrow\mathbf{Bialg}_R.
\]

### Definition 13.2 (Group algebra functor) {#def-group-algebra-functor}

For a group \(G\), the group algebra \(R[G]\) is the monoid algebra of its underlying monoid. It is a Hopf algebra with antipode
\[
S([g])=[g^{-1}].
\]
Thus
\[
R[-]:\mathbf{Grp}\longrightarrow\mathbf{HopfAlg}_R.
\]

### Definition 13.3 (Group-like elements) {#def-group-like-elements}

Let \(B\) be a bialgebra. An element \(b\in B\) is **group-like** if
\[
\Delta(b)=b\otimes b,
\qquad
\varepsilon(b)=1.
\]
The group-like elements form a monoid
\[
G(B).
\]
A bialgebra homomorphism preserves group-like elements, so this defines a functor
\[
G:\mathbf{Bialg}_R\longrightarrow\mathbf{Mon}.
\]

For a Hopf algebra \(H\), the antipode supplies inverses, so \(G(H)\) is a group and
\[
G:\mathbf{HopfAlg}_R\longrightarrow\mathbf{Grp}.
\]

### Theorem 13.4 (Monoid algebra adjunction to the multiplicative monoid) {#thm-monoid-algebra-adjunction-algebra}

Let
\[
U_{\times}:\mathbf{Alg}_R\longrightarrow\mathbf{Mon}
\]
send an \(R\)-algebra to its multiplicative monoid. Then
\[
R[-]:\mathbf{Mon}
\rightleftarrows
\mathbf{Alg}_R:U_{\times}
\]
is an adjunction:
\[
\operatorname{Hom}_{\mathbf{Alg}_R}(R[M],A)
\cong
\operatorname{Hom}_{\mathbf{Mon}}(M,U_{\times}A).
\]

**Proof.** An \(R\)-algebra map is determined by its values on the canonical basis, and the multiplicativity and unit conditions say exactly that those values form a monoid homomorphism. Conversely, every monoid homomorphism extends uniquely by \(R\)-linearity. \(\square\)

### Theorem 13.5 (Monoid algebra adjunction to group-like elements) {#thm-monoid-algebra-adjunction}

There is an adjunction
\[
R[-]:\mathbf{Mon}
\rightleftarrows
\mathbf{Bialg}_R:
G.
\]
Equivalently,
\[
\operatorname{Hom}_{\mathbf{Bialg}_R}(R[M],B)
\cong
\operatorname{Hom}_{\mathbf{Mon}}(M,G(B)).
\]

**Proof.** A bialgebra homomorphism \(\phi:R[M]\to B\) is determined by the elements \(\phi([m])\). Coalgebra compatibility makes these elements group-like, and algebra compatibility makes the assignment \(m\mapsto\phi([m])\) a monoid homomorphism. Conversely, a monoid homomorphism \(M\toG(B)\) extends uniquely by \(R\)-linearity to an algebra homomorphism \(R[M]\to B\), and the group-like identities imply compatibility with comultiplication and counit. \(\square\)

### Corollary 13.6 (Group algebra adjunctions) {#cor-group-algebra-adjunctions}

There is an adjunction
\[
R[-]:\mathbf{Grp}
\rightleftarrows
\mathbf{HopfAlg}_R:
G.
\]

After forgetting the coalgebra structure, the group algebra functor
\[
R[-]:\mathbf{Grp}\longrightarrow\mathbf{Alg}_R
\]
is left adjoint to the unit-group functor
\[
(-)^\times:\mathbf{Alg}_R\longrightarrow\mathbf{Grp}.
\]

### Remark 13.7 (The adjunction is not inherited from precomposition alone)

The underlying \(R\)-module of \(R[M]\) is the composite
\[
\mathbf{Mon}
\longrightarrow
\mathbf{Set}
\xrightarrow{F_R}
R\text{-}\mathbf{Mod}.
\]
The monoid-algebra adjunction does not follow merely by precomposing \(F_R\dashv U_R\) with \(\mathbf{Mon}\to\mathbf{Set}\). It follows from the lifted multiplication, coalgebra structure, and the separate universal properties of Theorems 13.4 and 13.5.

## 14. The essential image of the monoid algebra functor

The adjunction of Theorem 13.5 supplies the intrinsic recognition maps.  No condition on a chosen basis is taken as a primitive definition of a monoid algebra.

### Proposition 14.1 (Unit of the monoid-algebra adjunction) {#prop-monoid-algebra-unit}

For a monoid \(M\), the unit of the adjunction
\[
\eta_M:M\longrightarrow G(R[M])
\]
is the monoid homomorphism
\[
m\longmapsto [m].
\]

Let
\[
x=\sum_{m\in M}a_m[m]\in R[M]
\]
have finite support.  Then \(x\) is group-like if and only if
\[
a_m^2=a_m,
\qquad
a_ma_n=0\quad(m\ne n),
\qquad
\sum_m a_m=1.
\]

**Proof.** Comparing coefficients in
\[
\Delta(x)=x\otimes x
\]
gives the idempotence and orthogonality relations, while \(\varepsilon(x)=1\) gives the final equality.  Conversely these identities imply the two group-like equations. \(\square\)

### Corollary 14.2 (Connected base ring) {#cor-monoid-algebra-connected-base}

Assume that \(R\ne0\) and that \(R\) has no idempotents other than \(0\) and \(1\), equivalently that \(\operatorname{Spec}R\) is connected.  Then
\[
\eta_M:M\overset{\sim}{\longrightarrow}G(R[M])
\]
is an isomorphism for every monoid \(M\).  Consequently
\[
R[-]:\mathbf{Mon}\longrightarrow\mathbf{Bialg}_R
\]
is fully faithful.

**Proof.** Proposition 14.1 expresses a group-like element as a finite partition of \(1\) by pairwise orthogonal idempotents indexed by elements of \(M\).  Under the stated hypothesis exactly one coefficient is \(1\), and all others are \(0\).  The full-faithfulness statement follows because the unit of the adjunction is an isomorphism. \(\square\)

### Theorem 14.3 (Recognition by the counit) {#thm-monoid-algebra-counit}

Under the hypotheses of Corollary 14.2, a bialgebra \(B\) belongs to the essential image of the monoid algebra functor if and only if the counit
\[
\epsilon_B:R[G(B)]\longrightarrow B
\]
is an isomorphism of bialgebras.

**Proof.** For an adjunction with fully faithful left adjoint, the essential image of the left adjoint is precisely the full replete subcategory on the objects for which the counit is an equivalence. \(\square\)

### Remark 14.4 (Arbitrary base rings) {#rem-monoid-algebra-arbitrary-base}

If \(R\) has nontrivial idempotents, Proposition 14.1 shows that \(R[M]\) can have group-like elements other than the canonical generators \([m]\).  The unit \(M\to G(R[M])\) need not be an isomorphism, so the monoid algebra functor need not be fully faithful as a functor to all \(R\)-bialgebras, and the counit criterion of Theorem 14.3 is no longer an intrinsic characterization of its essential image.

In this generality the definition remains
\[
\operatorname{EssIm}\bigl(R[-]:\mathbf{Mon}\to\mathbf{Bialg}_R\bigr).
\]
A chosen presentation of \(B\) as a monoid algebra is standardly the data of a monoid \(M\) and a bialgebra isomorphism
\[
R[M]\overset{\sim}{\longrightarrow}B.
\]
If a target category retains the canonical basis of \(R[M]\), the isomorphism is required to respect that chosen basis.  This is presentation data attached to the monoid algebra construction, not a separately named class of bialgebras defined by adjectives about a basis.

### Remark 14.5 (The canonical basis) {#rem-monoid-algebra-canonical-basis}

The monoid algebra \(R[M]\) has its standard \(R\)-basis \(([m])_{m\in M}\).  The formulas
\[
[m][n]=[mn],
\qquad
\Delta([m])=[m]\otimes[m],
\qquad
\varepsilon([m])=1
\]
are consequences of the monoid algebra and canonical coalgebra constructions.  They may be used to compare Sage's chosen-basis presentation with the intrinsic functor \(R[-]\), but they do not supply a replacement definition of “monoid algebra.”
***

# Part VI. Functors induced by strong monoidal functors

## 15. Transport of algebra objects

### Proposition 15.1 (Functor induced on algebra objects) {#prop-induced-functor-algebras}

Let
\[
\Phi:\mathcal V\longrightarrow\mathcal W
\]
be a strong symmetric monoidal functor between suitable symmetric monoidal \(\infty\)-categories. For every \(\infty\)-operad \(\mathcal O\), there is an induced functor
\[
\operatorname{Alg}_{\mathcal O}(\Phi):
\operatorname{Alg}_{\mathcal O}(\mathcal V)
\longrightarrow
\operatorname{Alg}_{\mathcal O}(\mathcal W).
\]
It applies \(\Phi\) to the underlying objects, operations, and coherent cells.

For \(\Phi=F_R:\mathbf{Set}\to R\text{-}\mathbf{Mod}\), this recovers the bilinear extension of operations to free modules.

### Example 15.2

Under the standard identifications:

- monoid objects in \(\mathbf{Set}\) map to associative unital \(R\)-algebras;
- commutative monoid objects map to commutative \(R\)-algebras;
- group objects map to Hopf algebras after including the canonical cartesian comonoid structure;
- magmas map to \(R\)-modules equipped with a bilinear binary operation;
- semigroups map to associative, not necessarily unital, \(R\)-algebras.

The exact codomain is determined by the operations and coherences present in the source. It should be written explicitly rather than represented by one undifferentiated word “algebra.”

### Remark 15.3 (Choice of structural route)

An object can carry several operations whose underlying sets coincide. A ring, for example, has additive and multiplicative structures. To apply Proposition 15.1, one must select the functor to the category whose operation is to be extended.

Thus a construction from rings to monoid algebras requires the multiplicative route
\[
\mathbf{Ring}\longrightarrow\mathbf{Mon},
\]
while a construction from the additive group uses
\[
\mathbf{Ring}\longrightarrow\mathbf{Ab}.
\]
The two induced functors are different. The chosen structural route must therefore be specified.

***

# Part VII. Application to Sage's construction named `Algebras`

## 16. Mathematical interpretation

### Observation 16.1 (Sage's stated construction) {#obs-sage-algebras-source}

Sage defines the “algebra of a set \(S\) over \(R\)” as the free \(R\)-module with basis indexed by \(S\), equipped with whatever algebraic structure is induced from a selected structure on \(S\). Sage explicitly warns that the output need not be an \(R\)-algebra; for a bare set, its category is called “set algebras,” while the resulting object is not an object of Sage's category of \(R\)-algebras.

Accordingly, the Sage name `Algebras` is not a mathematical definition. Its normalized interpretation must name the actual functor in each domain.

### Definition 16.2 (Underlying free-module construction) {#def-sage-underlying-free-module}

Let
\[
U_{\mathcal C}:\mathcal C\longrightarrow\mathbf{Set}
\]
be the specified structural functor selected by the Sage construction. The underlying module of the Sage output is given by the composite
\[
\mathcal C
\xrightarrow{U_{\mathcal C}}
\mathbf{Set}
\xrightarrow{F_R}
R\text{-}\mathbf{Mod}.
\]

This composite is the free \(R\)-module functor applied to the selected underlying set. It is not, in general, a free \(R\)-algebra functor, and it is not automatically a left adjoint as a functor with domain \(\mathcal C\).

### Definition 16.3 (Lift determined by the selected structure) {#def-sage-algebras-lift}

When \(\mathcal C\) is a category of algebraic structures and the selected structural functor exhibits those structures as operadic algebras in \(\mathbf{Set}\), Proposition 15.1 gives a lift
\[
\widetilde F_{R,\mathcal C}:
\mathcal C\longrightarrow\mathcal D_{R,\mathcal C},
\]
where \(\mathcal D_{R,\mathcal C}\) is the category of the corresponding \(R\)-module-based structures.

The following cases are standard:

| source category | functor | mathematically natural codomain |
|---|---|---|
| \(\mathbf{Set}\) | \(X\mapsto R^{(X)}\) | free \(R\)-modules with their canonical bases; after applying the diagonal, canonical cocommutative coalgebras |
| magmas | bilinear extension of multiplication | \(R\)-modules with a bilinear binary operation and chosen basis |
| semigroups | semigroup algebra | associative nonunital \(R\)-algebras with chosen basis, together with the induced coalgebra when retained |
| monoids | monoid algebra \(M\mapsto R[M]\) | bialgebras with chosen basis |
| groups | group algebra \(G\mapsto R[G]\) | Hopf algebras with chosen basis |
| commutative monoids | commutative monoid algebra | commutative bialgebras with chosen basis |

Each row is a distinct functor or a restriction of a named functor. The table does not define a new common construction beyond the free \(R\)-module functor and the standard induced functors on algebra objects.

### Remark 16.4 (Set algebras)

For \(\mathcal C=\mathbf{Set}\), Sage's output is a free \(R\)-module on a set with its canonical basis. Applying the diagonal of the set gives the canonical cocommutative coalgebra structure of Definition 12.2. It is not an associative \(R\)-algebra unless the set has first been equipped with a suitable multiplication.

Therefore
\[
\mathbf{Set}.\mathrm{Algebras}(R)
\]
must not be normalized to \(\mathbf{Alg}_R\). The minimal codomain justified by this description is the category of free \(R\)-modules equipped with their canonical bases; a coalgebra codomain requires the additional coalgebra lift to be stated.

### Remark 16.5 (Monoid algebras)

For \(\mathcal C=\mathbf{Mon}\), the normalized functor is the monoid algebra functor
\[
R[-]:\mathbf{Mon}\longrightarrow\mathbf{Bialg}_R.
\]
Its category of values is the essential image of this functor. If \(R\ne0\) and \(\operatorname{Spec}R\) is connected, Theorem 14.3 characterizes that essential image by the counit
\[
R[G(B)]\longrightarrow B.
\]

When Sage retains a chosen basis, this is additional presentation data: an object is exhibited by a monoid \(M\) and an isomorphism from the standard monoid algebra \(R[M]\), respecting the chosen basis when the morphism convention requires it. No adjective-defined class of bases is introduced as a substitute for the monoid algebra construction.

## 17. Codomains and essential images

### Convention 17.1 (Codomain and essential image) {#conv-construction-codomain-first}

The codomain of a functor is part of its definition. For example,
\[
R[-]:\mathbf{Mon}\to\mathbf{Bialg}_R
\]
already states where every value lives.

A named category of values may additionally be defined as the essential image
\[
\operatorname{EssIm}(R[-])
\hookrightarrow
\mathbf{Bialg}_R.
\]
The essential image is not a substitute for the functor or its codomain; it is a property-like refinement of the codomain.

### Convention 17.2 (Source of presentations versus essential image) {#conv-source-versus-essential-image}

The source \(\mathcal C\) of a construction and \(\operatorname{EssIm}(F)\) answer different questions.

- \(\mathcal C\) records input objects and their morphisms.
- \(\operatorname{EssIm}(F)\) records all target morphisms between objects equivalent to construction values.
- the presentation fiber \(\operatorname{Pres}_F(Y)\) records the choices that exhibit \(Y\) as a construction value.

No two of these are identified without a comparison theorem.

### Convention 17.3 (Restrictions of a construction) {#conv-restrictions-construction}

For a construction \(F:\mathcal C\to\mathcal D\), the following operations are distinguished:

1. **precomposition** with \(H:\mathcal C'\to\mathcal C\), giving \(FH\);
2. **corestriction** through \(i:\mathcal D'\hookrightarrow\mathcal D\), requiring a specified factorization;
3. **inverse image of a target classifier**, giving \(\mathcal C\times_{\mathcal D}\mathcal D.Q\);
4. **restriction of an adjunction**, requiring both adjoints and their unit and counit to preserve the selected subcategories;
5. **restriction of scalars**, which is the separate standard functor attached to a ring homomorphism.

The bare word “restriction” should be accompanied by one of these meanings.

### Convention 17.4 (Characterization of an essential image is a theorem) {#conv-essential-image-characterization}

A statement of the form
\[
\operatorname{EssIm}(F)=\mathcal D.Q
\]
means:

1. \(F\) admits a corestriction to \(\mathcal D.Q\); and
2. the corestricted functor is essentially surjective.

These are theorem obligations. A displayed list of properties of construction values proves only containment in \(\mathcal D.Q\), not equality with it.

***

# Part VIII. Amendments to the foundations report

## 18. Required amendments

### Amendment 18.1 (General categorical foundations)

Insert Definitions 1.1--6.1 before the first use of free, forgetful, localization, image, restriction, or corestriction terminology. The original report currently uses adjunctions and essential images only incidentally and therefore does not support systematic reasoning about them.

### Amendment 18.2 (Module section)

After the total module family, add Definition 9.1 and Corollary 9.2. The statements “free module” and “finite free module” should be tied to the essential images of the free \(R\)-module functor and its restriction to finite sets.

The categories of modules equipped with bases must retain the morphism distinction in Remark 9.3.

### Amendment 18.3 (Algebra section)

The section on \(R\)-algebras should add:

- tensor algebra and its adjunction;
- the free associative \(R\)-algebra on a set;
- symmetric algebra and the free commutative \(R\)-algebra on a set;
- free \(\mathcal O\)-algebras in a monoidal \(\infty\)-category;
- the distinction between all algebra objects and free algebra objects.

### Amendment 18.4 (Sheafification section)

The sheafification theorem should be expanded to state that sheaves form a reflective localization of presheaves, with local objects characterized by the unit. Add the free abelian sheaf construction and the change-of-site contingency of Definition 7.5.

### Amendment 18.5 (Sage correspondence)

The Sage correspondence should replace any undifferentiated description of `C.Algebras(R)` by:

1. a chosen structural functor \(U_{\mathcal C}:\mathcal C\to\mathbf{Set}\);
2. the composite free \(R\)-module functor \(F_RU_{\mathcal C}\);
3. the specific lift induced by the selected algebraic structure, when it exists;
4. the codomain of that lift;
5. optionally, the essential image and a theorem characterizing it.

For monoids, the required objects are the monoid algebra functor, the functor of group-like elements, their adjunction, the essential-image factorization, and—under the connected-base hypothesis—the counit recognition theorem of Theorem 14.3.

### Amendment 18.6 (Prohibited ambiguous substitutions)

The following substitutions are invalid:

- “free \(R\)-module” for “free associative \(R\)-algebra”;
- “free associative \(R\)-algebra” for “monoid algebra”;
- “algebra objects in \(\mathcal C\)” for Sage's `C.Algebras(R)`;
- “essential image” for the source category of a construction;
- “restriction” without specifying precomposition, corestriction, inverse image, restriction of an adjunction, or restriction of scalars;
- a condition phrased only in terms of a chosen basis as a definition of “monoid algebra”; use the functor \(R[-]\), its essential image, or an explicit isomorphism \(R[M]\simeq B\).

***

# Reference guide

The following sources contain the standard constructions used above.

- **Adjunctions, monads, reflective subcategories, and essential images:** Mac Lane, *Categories for the Working Mathematician*; Riehl, *Category Theory in Context*; Kerodon, especially its sections on adjunctions, essentially surjective functors, essential images, Kan extensions, and localizations.
- **Free modules, tensor algebras, symmetric algebras, monoid algebras, and group algebras:** Bourbaki, *Algebra*; standard graduate algebra texts.
- **Bialgebras, Hopf algebras, and group-like elements:** Sweedler, *Hopf Algebras*; Montgomery, *Hopf Algebras and Their Actions on Rings*.
- **Free operadic algebras and induced functors on algebra objects:** Lurie, *Higher Algebra*.
- **Sheafification, free abelian sheaves, and change of site:** the Stacks Project, especially the sections on sheafification, functoriality of presheaves, cocontinuous functors, and abelian sheaves.
- **Sage's construction named `Algebras`:** the SageMath reference and source for `sage.categories.algebra_functor`, together with the named categories of monoid and group algebras.

***

# Concluding formulation

The mathematical hierarchy is
\[
\boxed{
\begin{gathered}
F\dashv U
\quad\Longrightarrow\quad
\text{free object on }X=F(X),
\\[1mm]
\text{free objects}
=
\operatorname{EssIm}(F),
\qquad
\text{chosen free presentations}
=
\operatorname{hofib}(F^{\simeq}),
\\[1mm]
\text{restriction of domain}
=
\text{precomposition},
\qquad
\text{restriction of codomain}
=
\text{corestriction},
\\[1mm]
\text{reflection into a reflective subcategory}
=
\text{composition with its reflector},
\\[1mm]
\text{operations on sets}
\longmapsto
\text{operations on free }R\text{-modules}
\end{gathered}
}
\]
through the strong symmetric monoidal free \(R\)-module functor.

In particular,
\[
\boxed{
\begin{aligned}
X&\longmapsto R^{(X)}
&&\text{is the free }R\text{-module functor},\\
X&\longmapsto R\langle X\rangle
&&\text{is the free associative }R\text{-algebra functor on sets},\\
X&\longmapsto R[X]
&&\text{is the free commutative }R\text{-algebra functor on sets},\\
M&\longmapsto R[M]
&&\text{is the monoid algebra functor},\\
G&\longmapsto R[G]
&&\text{is the group algebra functor},\\
F&\longmapsto F^{\#}
&&\text{is sheafification.}
\end{aligned}
}
\]

These constructions are related by adjunctions, composition, induced functors on algebra objects, and reflective localization. They remain mathematically distinct.
