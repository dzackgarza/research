---
title: "Mathematical Foundations of the Categorical Research Language"
subtitle: "Classifiers, higher-categorical constructions, forms, lattices, geometric objects, and categorical computation"
date: 2026-07-23
---

# Mathematical Foundations of the Categorical Research Language

## Status and scope

This document collects the mathematical theory developed across the attached conversations and presents it as a single coherent account. It is a foundations document, not an implementation plan. Its purpose is to fix the mathematical objects, morphisms, universal constructions, variance conventions, truncations, and exact sequences that later formalization and computation are intended to realize.

The conversations form a derivation record rather than a linear manuscript. Many provisional constructions were explicitly retracted. In particular, this account does **not** adopt the following superseded positions:

- that the ambient universe may be restricted semantically to ordinary categories;
- that every classifier is itself a Grothendieck fibration over all morphisms of its base;
- that binary operations form the category of elements of the assignment \(X\mapsto \operatorname{Map}(X^2,X)\) over arbitrary maps;
- that equations should be defined primarily by equifiers of two selected composites;
- that properties, structures, and stuff are mutually exclusive classes;
- that a synthetic lattice of axiom labels is a mathematical replacement for categories and functors;
- that a separate mathematical universe of “computational categories” is needed;
- that pointwise constructions such as \(O(L)\) should be primitive nodes;
- that a theorem such as “alternating implies skew-symmetric” should be encoded by nesting one definition inside another;
- that the genus is obtained by applying \(\pi_0\) to a homotopy fiber;
- that the algebraic-geometric sign convention takes \(E_8\) positive definite;
- that the negative-definite ADE lattices are defined by negated Cartan matrices rather than constructed from root realizations;
- that a morphism of generated or presented modules is defined by a matrix, rather than represented by a compatible matrix lift that descends;
- that the opposite-ring involution alone yields a functor from left modules to right modules, or that an \((R,\mathbb Z)\)-bimodule carries a noncontractible choice of \(\mathbb Z\)-action;
- that the functors forgetting one bimodule action are natural for simultaneous extension of scalars in both rings; they are natural for restriction and only lax for extension.

The settled framework is instead organized by a small number of standard constructions: higher categories, mapping categories, arrow and diagram categories, homotopy limits, classifiers, lifts, categories of elements where an actual functor is present, exact sequences, cores, automorphism groups, and standard geometric categories. The report uses the mathematical vocabulary of higher category theory, homotopy theory, algebra, arithmetic lattices, and algebraic geometry. No terminology from programming-language theory, implementation architecture, or proof-assistant internals is needed for the mathematical account.

The definitions are intended to be stable under later extensions to monoidal and operadic algebra, schemes and stacks, derived and spectral geometry, and genuine synthetic \(\infty\)-category theory. Ordinary categories and current formal libraries are regarded as truncated realizations of this ambient theory, not as its semantic ceiling.

### Reference conventions

Precise bibliographic pinning is deferred. The following are the standard reference families intended whenever the indicated terminology occurs.

- Higher categories, truncation, (co)cartesian fibrations, comma objects, and homotopy limits: Lurie, *Higher Topos Theory* and *Higher Algebra*; Kerodon; Riehl–Verity, *Infinity Category Theory from Scratch* and *Elements of \(\infty\)-Category Theory*.
- Ordinary and enriched category theory: Mac Lane, *Categories for the Working Mathematician*; Riehl, *Category Theory in Context*; Kelly, *Basic Concepts of Enriched Category Theory*.
- Stuff, structure, and property: Baez–Shulman, *Lectures on \(n\)-Categories and Cohomology*; the corresponding nLab entry.
- Grothendieck constructions, fibred categories, sites, sheaves, and algebraic stacks: the Stacks Project; SGA; Giraud.
- Operads and coherent algebra: Stasheff; Boardman–Vogt; May; Lurie, *Higher Algebra*.
- Integral lattices and discriminant forms: Serre, *A Course in Arithmetic*; Milnor–Husemoller; O'Meara; Conway–Sloane; Nikulin.

When a term has several standard meanings, the definition adopted here is stated explicitly.

***

# Part I. The higher-categorical ambient

## 1. Universes and the category of categories

### Definition 1.1 (Universe convention) {#def-universe}

Fix Grothendieck universes
\[
\mathcal U\in \mathcal V.
\]
An object, category, or diagram is called **small** without qualification when it is \(\mathcal U\)-small. The collection of \(\mathcal U\)-small \(\infty\)-categories is \(\mathcal V\)-large.

### Definition 1.2 (The ambient \((\infty,2)\)-category) {#def-ambient-cat}

Let
\[
\mathfrak{Cat}_{\mathcal U}
\]
denote a chosen model of the \((\infty,2)\)-category whose objects are \(\mathcal U\)-small \(\infty\)-categories, whose \(1\)-morphisms are functors, and whose mapping objects
\[
\operatorname{Fun}(\mathcal C,\mathcal D)
\]
are \(\infty\)-categories of functors, natural transformations, and higher modifications.

The theory is model-independent: one may work with scaled simplicial sets, complete Segal \(2\)-spaces, an \(\infty\)-cosmos and its homotopy \(2\)-category, or another equivalent presentation, provided that the following constructions exist at the required size:

1. internal functor \(\infty\)-categories;
2. opposites, products, arrow categories, slices, coslices, and comma categories;
3. the finite and small homotopy limits used below;
4. cores and truncation functors;
5. operadic algebra categories.

### Remark 1.3 (Underlying truncations)

Several familiar categorical universes occur as truncations or subobjects of \(\mathfrak{Cat}_{\mathcal U}\):

- \(\mathcal S_{\mathcal U}\), the \(\infty\)-category of spaces or \(\infty\)-groupoids;
- \(\mathbf{Set}_{\mathcal U}=\tau_{\le 0}\mathcal S_{\mathcal U}\), the category of sets;
- \(\mathbf{Grpd}_{\mathcal U}=\tau_{\le 1}\mathcal S_{\mathcal U}\), the \(2\)-category or \((2,1)\)-category of groupoids;
- \(\mathbf{Cat}_{1,\mathcal U}\), the \(2\)-category of ordinary categories, functors, and natural transformations.

The distinguished object \(\mathbf{Set}\) remains part of ordinary mathematical parlance. Saying that sets are \(0\)-truncated spaces, or discrete \(\infty\)-categories, does not eliminate the category of sets as a named mathematical object.

### Definition 1.4 (Points and objects) {#def-point}

Let \(\mathbf 1\) denote the terminal \(\infty\)-category. A **point** of an \(\infty\)-category \(\mathcal C\) is a functor
\[
x:\mathbf 1\longrightarrow \mathcal C.
\]
Equivalently, it is an object \(x\in\mathcal C\). A category \(\mathcal C\) itself is selected as an object of \(\mathfrak{Cat}_{\mathcal U}\) by a point
\[
c_{\mathcal C}:\mathbf 1\longrightarrow \mathfrak{Cat}_{\mathcal U}.
\]

This convention is the mathematical meaning of declarations of the form “let \(x\in\mathcal C\).”

## 2. Mapping objects, cores, components, and loops

### Definition 2.1 (Mapping \(\infty\)-category and mapping space) {#def-mapping}

For \(\mathcal C,\mathcal D\in\mathfrak{Cat}_{\mathcal U}\), the internal hom
\[
\operatorname{Fun}(\mathcal C,\mathcal D)
\]
is the mapping \(\infty\)-category. For \(x,y\in\mathcal C\), write
\[
\operatorname{Map}_{\mathcal C}(x,y)
\]
for the mapping space between \(x\) and \(y\).

In a \((2,1)\)-category such as the ordinary theory of stacks in groupoids, the hom-object between two objects is a category: its objects are \(1\)-morphisms and its arrows are \(2\)-isomorphisms. It is not replaced by a set unless a truncation is explicitly applied.

### Definition 2.2 (Core) {#def-core}

The **core** or maximal \(\infty\)-groupoid of \(\mathcal C\) is
\[
\mathcal C^{\simeq}\subseteq \mathcal C,
\]
the sub-\(\infty\)-category containing every object and only equivalences. The construction
\[
(-)^{\simeq}:\mathfrak{Cat}_{\mathcal U}\longrightarrow \mathcal S_{\mathcal U}
\]
is functorial.

### Definition 2.3 (Connected components) {#def-pi0}

For a space or \(\infty\)-groupoid \(X\), its set of connected components is
\[
\pi_0(X)=\tau_{\le 0}X.
\]
For an \(\infty\)-category \(\mathcal C\), the set of equivalence classes of objects is
\[
\pi_0(\mathcal C^{\simeq}).
\]
This notation is used only after taking the core. No set of “objects modulo isomorphism” is taken as a primitive for an arbitrary large or nonconcrete category.

### Definition 2.4 (Automorphism object) {#def-aut}

For \(x\in\mathcal C\), define
\[
\operatorname{Aut}_{\mathcal C}(x)
:=
\Omega_x(\mathcal C^{\simeq})
=
\operatorname{Map}_{\mathcal C^{\simeq}}(x,x).
\]
This is a group object in spaces. In an ordinary category it is the usual automorphism group.

An equivalence \(u:x\simeq y\) induces conjugation
\[
\operatorname{Aut}_{\mathcal C}(x)
\overset{\sim}{\longrightarrow}
\operatorname{Aut}_{\mathcal C}(y),
\qquad
g\longmapsto ugu^{-1}.
\]
Thus automorphism groups form a functor on the core, understood up to the natural higher coherence.

### Definition 2.5 (Isomorphism torsor) {#def-isom-torsor}

For \(x,y\in\mathcal C\), define
\[
\operatorname{Isom}_{\mathcal C}(x,y)
:=
\operatorname{Map}_{\mathcal C^{\simeq}}(x,y).
\]
When nonempty, it carries commuting left and right actions by \(\operatorname{Aut}(y)\) and \(\operatorname{Aut}(x)\), and is a bitorsor in the ordinary \(1\)-categorical case.

### Definition 2.6 (Loop object in an \(\infty\)-category) {#def-loop-object}

Let \((\mathcal C,*)\) be a pointed \(\infty\)-category with finite limits. For a pointed object \(*\to X\), its loop object is the pullback
\[
\Omega X
:=
*\times_X *.
\]
Equivalently, it is the limit of the cospan \(*\to X\leftarrow *\). This definition applies in spaces, spectra, stable \(\infty\)-categories, and any other pointed \(\infty\)-category with finite limits.

## 3. Truncation

### Definition 3.1 (Truncated spaces) {#def-truncated-space}

For \(n\ge -2\), a space \(X\) is **\(n\)-truncated** if every homotopy group \(\pi_i(X,x)\) vanishes for \(i>n\). The low-dimensional cases are:

- \((-2)\)-truncated: contractible;
- \((-1)\)-truncated: empty or contractible, also called propositional;
- \(0\)-truncated: a set;
- \(1\)-truncated: a groupoid.

The inclusion \(\mathcal S_{\le n}\hookrightarrow\mathcal S\) has a left adjoint
\[
\tau_{\le n}:\mathcal S\longrightarrow \mathcal S_{\le n}.
\]

### Definition 3.2 (Truncated morphism) {#def-truncated-morphism}

A morphism \(f:X\to Y\) in an \(\infty\)-category with pullbacks is **\(n\)-truncated** if every homotopy fiber of \(f\) is \(n\)-truncated. The conditions are cumulative:
\[
(-2)\text{-truncated}
\Longrightarrow
(-1)\text{-truncated}
\Longrightarrow
0\text{-truncated}
\Longrightarrow\cdots.
\]

### Definition 3.3 (Locally truncated categories) {#def-locally-truncated}

An \(\infty\)-category \(\mathcal C\) is **locally \(n\)-truncated** if each mapping space \(\operatorname{Map}_{\mathcal C}(x,y)\) is \(n\)-truncated. An ordinary category is locally \(0\)-truncated; a \((2,1)\)-category is locally \(1\)-truncated.

### Remark 3.4 (Why truncation is recorded)

Truncation is not a display convention. A set of equivalence classes, a groupoid of objects and isomorphisms, and a full homotopy fiber are different mathematical objects. Passing to the core or to \(\pi_0\) is therefore always stated explicitly.

## 4. Arrow, slice, comma, and diagram categories

### Definition 4.1 (Arrow category) {#def-arrow-category}

For an \(\infty\)-category \(\mathcal C\), its arrow category is
\[
\operatorname{Ar}(\mathcal C)
:=
\operatorname{Fun}(\Delta^1,\mathcal C).
\]
The endpoint evaluations are
\[
\operatorname{ev}_0,\operatorname{ev}_1:
\operatorname{Ar}(\mathcal C)\longrightarrow\mathcal C.
\]

### Definition 4.2 (Slice and coslice) {#def-slice}

For \(x\in\mathcal C\), the slice and coslice are the comma \(\infty\)-categories
\[
\mathcal C_{/x}
\,=\,
(\operatorname{id}_{\mathcal C}\downarrow x),
\qquad
\mathcal C_{x/}
\,=\,
(x\downarrow\operatorname{id}_{\mathcal C}).
\]

### Definition 4.3 (Comma category) {#def-comma}

For functors \(F:\mathcal A\to\mathcal C\) and \(G:\mathcal B\to\mathcal C\), the comma \(\infty\)-category
\[
(F\downarrow G)
\]
is the homotopy pullback
\[
\mathcal A
\times_{\mathcal C,\operatorname{ev}_0}
\operatorname{Ar}(\mathcal C)
\times_{\operatorname{ev}_1,\mathcal C}
\mathcal B.
\]

### Definition 4.4 (Diagram category) {#def-diagram-category}

For a small \(\infty\)-category \(K\), the category of \(K\)-shaped diagrams in \(\mathcal C\) is
\[
\operatorname{Fun}(K,\mathcal C).
\]
A limit is a terminal cone and a colimit is an initial cocone. Unless a strict model is specifically selected, limits and pullbacks in this report mean homotopy-coherent limits in the relevant \(\infty\)-category.

### Definition 4.5 (Full and replete subcategory) {#def-full-replete-subcategory}

A **full subcategory** \(\mathcal D\subseteq\mathcal C\) is specified by a collection of
objects of \(\mathcal C\), with mapping spaces inherited from \(\mathcal C\):
\[
\operatorname{Map}_{\mathcal D}(x,y)
\simeq
\operatorname{Map}_{\mathcal C}(x,y).
\]
It is **replete** if every object of \(\mathcal C\) equivalent to an object of
\(\mathcal D\) also belongs to \(\mathcal D\).

This terminology is local to a fixed category. It does not assert that
\(\mathfrak{Cat}\) has a subobject classifier or that every classifier is a monomorphism.
Replete full subcategories arise as the ordinary categorical presentations of property
classifiers.

### Definition 4.6 (Grothendieck construction) {#def-grothendieck-construction}

Let \(\Phi:\mathcal C^{\mathrm{op}}\to\mathfrak{Cat}_{\mathcal U}\) be a functor.
Under straightening--unstraightening, \(\Phi\) classifies a cartesian fibration
\[
p_\Phi:\int_{c\in\mathcal C}\Phi(c)\longrightarrow\mathcal C.
\]
The total \(\infty\)-category is the **Grothendieck construction** of \(\Phi\), and its
fiber over \(c\) is equivalent to \(\Phi(c)\). A covariant functor
\(\Psi:\mathcal C\to\mathfrak{Cat}_{\mathcal U}\) similarly classifies a cocartesian
fibration.

The construction is cited in the sense of Grothendieck fibrations, the Stacks Project, and
higher-categorical straightening/unstraightening. A classifier need not itself arise this
way over all arrows of its base; when it does, the fibration is additional structure.

### Definition 4.7 (Category of elements) {#def-category-elements}

For a presheaf of spaces \(P:\mathcal C^{\mathrm{op}}\to\mathcal S\), its
**category of elements** is the Grothendieck construction
\[
\int_{c\in\mathcal C}P(c)\longrightarrow\mathcal C.
\]
For an ordinary presheaf \(P:\mathcal C^{\mathrm{op}}\to\mathbf{Set}\), this category has
objects \((c,x)\) with \(x\in P(c)\), and a morphism
\[
(c,x)\longrightarrow(d,y)
\]
is a morphism \(f:c\to d\) satisfying
\[
x=P(f)(y).
\]
This convention fixes the variance used for the form categories of Part IV.

### Remark 4.8 (When no category of elements exists)

The formula \(X\mapsto\operatorname{Map}(X^n,X)\) is not functorial on arbitrary maps
\(X\to Y\): its source varies contravariantly and its target covariantly. Consequently,
the category of \(n\)-ary operations is not defined as an ordinary category of elements of
this assignment. Definition 8.1 instead uses the invariant arrow-category pullback.

***

# Part II. Classifiers, lifts, and diagrammatic axioms

## 5. Classifiers

### Definition 5.1 (Classifier over a category) {#def-classifier}

Let \(\mathcal C\in\mathfrak{Cat}_{\mathcal U}\). A **classifier over \(\mathcal C\)** is a morphism
\[
p:\mathcal E\longrightarrow\mathcal C
\]
in \(\mathfrak{Cat}_{\mathcal U}\), regarded as an object of the slice \((\infty,2)\)-category \(\mathfrak{Cat}_{/\mathcal C}\).

Its homotopy fiber over \(x\in\mathcal C\) is denoted
\[
\mathcal E_x
:=
\mathbf 1\times^{h}_{\mathcal C}\mathcal E.
\]
It is the moduli object of lifts of \(x\) to \(\mathcal E\).

### Definition 5.2 (Axiom classifier) {#def-axiom-classifier}

An **axiom classifier** is a classifier
\[
p_A:\mathcal C.A\longrightarrow\mathcal C
\]
whose total category \(\mathcal C.A\), morphisms, and projection are defined by an explicit mathematical construction representing specified data, equations, limit conditions, or coherent fillers on objects of \(\mathcal C\).

Thus “axiom” is not an independent token or truth-valued predicate. It is shorthand for the displayed classifying morphism together with the construction of its total category.

The definition deliberately does **not** require \(p_A\) itself to be a cartesian or cocartesian fibration over every morphism of \(\mathcal C\). Many natural classifiers, including the classifier of binary operations on sets, admit no canonical pushforward or pullback of their data along an arbitrary map. What is always available is reindexing of the classifier itself by homotopy pullback.

### Definition 5.3 (Lift and section) {#def-lift-section}

Let \(x:\mathbf 1\to\mathcal C\) be a point. An **\(A\)-structure on \(x\)** is a lift
\[
\begin{array}{ccc}
&\mathcal C.A&\\
&\nearrow&\downarrow p_A\\
\mathbf 1&\xrightarrow{x}&\mathcal C.
\end{array}
\]
Equivalently, it is a point of the fiber \((\mathcal C.A)_x\).

For a functor \(F:\mathcal D\to\mathcal C\), an **\(A\)-structure on \(F\)** is a lift \(\widehat F:\mathcal D\to\mathcal C.A\) together with a specified equivalence
\[
p_A\widehat F\simeq F.
\]
When \(F=\operatorname{id}_{\mathcal C}\), such a lift is a section of \(p_A\).

### Remark 5.4 (Assertions as factorizations)

Statements such as “\(\mathcal C\) is monoidal,” “\(X\) is finite,” or “\(M\) has a chosen basis” are represented by lifts through their respective classifiers. The construction records both existence and, when the fiber is noncontractible, the actual chosen structure.

### Definition 5.5 (Forgetful structural morphism) {#def-forgetful-morphism}

The adjective **forgetful** is used only relative to specified structure. A functor
\[
U:\mathcal E\longrightarrow\mathcal C
\]
is called forgetful in this report when \(\mathcal E\) has been constructed as objects of
\(\mathcal C\) equipped with named additional data or axioms, and \(U\) is the displayed
projection that discards precisely those data. Equivalently, \(U\) is part of the
classifier presentation, not an arbitrary functor subsequently declared to be forgetful.

Faithfulness, fullness, conservativity, and fibrational properties are theorems about a
particular forgetful morphism. None of them alone is the definition.

## 6. Property, structure, and stuff

### Definition 6.1 (Truncation class of a classifier) {#def-classifier-truncation}

An axiom classifier \(p_A\) is **\(n\)-truncated** if it is an \(n\)-truncated morphism in the underlying \((\infty,1)\)-category of \(\mathfrak{Cat}\). Equivalently, each classifying fiber \((\mathcal C.A)_x\) is \(n\)-truncated, with the corresponding local condition on morphisms.

### Definition 6.2 (Property classifier) {#def-property-classifier}

A **property classifier** is a \((-1)\)-truncated axiom classifier. Its classifying fiber over any object is empty or contractible. Consequently, an object either does not admit the property or admits it uniquely up to contractible choice.

In an ordinary \(1\)-categorical presentation, a property classifier is represented by a replete full inclusion
\[
\mathcal C.A\hookrightarrow\mathcal C.
\]

### Definition 6.3 (Structure classifier) {#def-structure-classifier}

Suppose the ambient is locally \(n\)-truncated. A **structure classifier** is an axiom classifier whose fibers are at most \(n\)-truncated, so that the moduli of structures have no higher cells beyond those naturally visible in the ambient.

In the ordinary \(1\)-categorical shadow, this is the “forgets at most structure” case of Baez–Shulman and is represented by a faithful functor. In the \((2,1)\)-categorical setting, the fiber may be a groupoid of choices.

### Definition 6.4 (Stuff) {#def-stuff}

A general axiom classifier, with no prescribed truncation on its fibers, may forget **stuff**. The three terms form a cumulative hierarchy:
\[
\text{property}\subseteq\text{structure}\subseteq\text{stuff}.
\]
They are not mutually exclusive labels.

### Example 6.5

1. Finiteness of a set is a property.
2. A binary operation on a set is structure: the fiber is the set \(\operatorname{Hom}(X^2,X)\).
3. Associativity of a chosen binary operation on a set is a property.
4. A chosen basis of a module is structure; freeness without a chosen basis is a property.
5. A monoidal structure on a category is structure: the fiber is a groupoid or higher moduli object of tensors, units, associators, and coherence data.
6. The abelian axioms are property-like **relative to a chosen preadditive/additive structure**. The additive enrichment itself is structure and must not be silently omitted.

### Remark 6.6 (Named choices)

A construction consuming a noncontractible classifying fiber must name the chosen lift. A category may carry several inequivalent monoidal structures, for example \(\otimes\), \(\oplus\), products, or coproducts. These are distinct points of one monoidal-structure fiber; they are not distinct classifier categories.

## 7. Reindexing and intersection

### Definition 7.1 (Reindexing) {#def-reindexing}

Let \(F:\mathcal D\to\mathcal C\) and let \(p_A:\mathcal C.A\to\mathcal C\) be a classifier. Its **reindexing along \(F\)** is the homotopy pullback
\[
F^*(\mathcal C.A)
:=
\mathcal D\times^{h}_{\mathcal C}\mathcal C.A
\longrightarrow
\mathcal D.
\]
An object is a pair consisting of \(d\in\mathcal D\) and an \(A\)-structure on \(F(d)\), together with the required coherence.

### Definition 7.2 (Categorical intersection or conjunction) {#def-intersection}

For classifiers \(p_A:\mathcal C.A\to\mathcal C\) and \(p_B:\mathcal C.B\to\mathcal C\), their **categorical intersection** is
\[
\mathcal C.(A\wedge B)
:=
\mathcal C.A\times^{h}_{\mathcal C}\mathcal C.B
\longrightarrow\mathcal C.
\]
It is the product of the two objects in the slice \(\mathfrak{Cat}_{/\mathcal C}\), hence the terminal cone over the cospan. It classifies objects carrying both structures compatibly.

Finite conjunctions are defined by finite homotopy limits over the complete diagram of the participating classifiers and their structural maps. This universal property is essential: a merely chosen category mapping to the classifier totals need not be the universal category of all compatibly structured objects.

### Proposition 7.3 (Stability of truncation)

Reindexing preserves the truncation class of a classifier. In particular, the inverse image of a property classifier is a property classifier, and the intersection of property classifiers is a property classifier.

**Proof sketch.** Homotopy fibers are preserved under base change. The fiber of \(F^*p_A\) over \(d\) is equivalent to the fiber of \(p_A\) over \(F(d)\). The assertion follows from stability of truncated morphisms under pullback. \(\square\)

### Remark 7.4 (Strict, pseudo, and homotopy pullbacks)

A strict pullback in ordinary \(\mathbf{Cat}\) is not invariant under replacement of a leg by an equivalent functor. Replete full inclusions are isofibrations, and strict pullbacks along them model the corresponding pseudo-pullbacks. The invariant default of this report is the homotopy pullback; strict pullbacks are used only after a comparison theorem licenses them.

### Remark 7.5 (No generic disjunction from naked classifier arrows)

The pair of arrows \(\mathcal C.A\to\mathcal C\leftarrow\mathcal C.B\) canonically determines their conjunction by a limit. It does not, by itself, determine a classifier of “the axioms common to \(A\) and \(B\)” or of “\(A\) or \(B\).” Such an operation requires additional presentation data. The Sage-specific colimit construction of Part VIII depends on a complete chosen diagram, not merely on two naked classifier arrows.

### Definition 7.6 (Inherited classifier and site of definition) {#def-inherited-classifier}

Let \(F:\mathcal C\to\mathcal D\), let \(p_A:\mathcal D.A\to\mathcal D\), and let
\(q:\mathcal E\to\mathcal C\) be classifiers. The classifier \(q\) is **inherited from**
\(p_A\) along \(F\) if there is an equivalence in the slice over \(\mathcal C\)
\[
\mathcal E
\simeq
\mathcal C\times^h_{\mathcal D}\mathcal D.A.
\]
A **site of definition** for the datum or axiom \(A\) is a category on which its classifier
is defined directly; occurrences on categories mapping to that site are obtained by
reindexing.

For example, commutativity is defined on binary operations and pulled back to monoids,
groups, rings, and algebras. Finite generation of modules is defined at the module level and
is not inherited from the underlying additive monoid. The phrase “lowest level” refers to
this factorization property, not to an externally imposed hierarchy of names.

### Definition 7.7 (Implication between classifiers) {#def-classifier-implication}

An **implication** from an \(A\)-classifier to a \(B\)-classifier over the same base is a
functor
\[
\mathcal C.A\longrightarrow\mathcal C.B
\]
over \(\mathcal C\). It is theorem data witnessing that every \(A\)-object canonically
carries a \(B\)-structure. An implication is not incorporated into either definition unless
it is part of the defining universal property.

Thus alternating and skew-symmetric forms are defined independently; Lemma 16.2 supplies the
implication functor. Similarly, perfectness implies radical-freeness through the defect exact
sequence rather than by defining perfect forms inside the radical-free classifier.

## 8. Classifiers of operations

### Definition 8.1 (Operation classifier) {#def-operation-classifier}

Let \(\mathcal E\) be an \(\infty\)-category with finite products, and let \(n\ge 0\). Define
\[
\gamma_n:\mathcal E\longrightarrow\mathcal E\times\mathcal E,
\qquad
X\longmapsto (X^n,X).
\]
Let
\[
(\operatorname{ev}_0,\operatorname{ev}_1):
\operatorname{Ar}(\mathcal E)
\longrightarrow
\mathcal E\times\mathcal E
\]
be endpoint evaluation. The category of objects equipped with an \(n\)-ary operation is
\[
\operatorname{Op}_n(\mathcal E)
:=
\mathcal E
\times^{h}_{\mathcal E\times\mathcal E}
\operatorname{Ar}(\mathcal E).
\]
The projection
\[
U_n:\operatorname{Op}_n(\mathcal E)\longrightarrow\mathcal E
\]
is the operation classifier.

An object is \((X,\mu)\) with
\[
\mu:X^n\longrightarrow X.
\]
The pullback carries a universal operation
\[
\boldsymbol\mu:U_n^n\Longrightarrow U_n
\]
in the appropriate higher-categorical sense.

### Example 8.2

For \(\mathcal E=\mathbf{Set}\) and \(n=2\), \(\operatorname{Op}_2(\mathbf{Set})\) is the category of magmas. A morphism
\[
f:(X,\mu)\longrightarrow(Y,\nu)
\]
is a function satisfying
\[
f\circ\mu=\nu\circ(f\times f).
\]

### Remark 8.3 (No transport along arbitrary maps)

The projection \(\operatorname{Op}_2(\mathbf{Set})\to\mathbf{Set}\) is not a cartesian or cocartesian fibration over arbitrary functions. Given \(f:Y\to X\) and \(\mu:X^2\to X\), the composite
\[
Y^2\xrightarrow{f^2}X^2\xrightarrow{\mu}X
\]
does not land in \(Y\), and therefore does not define an operation on \(Y\). Dually, an operation on \(X\) need not descend along a quotient map. Canonical transport exists along equivalences, so the restriction to cores has the expected moduli interpretation.

### Definition 8.4 (Operations on the image of a functor) {#def-relative-operation}

For \(F:\mathcal C\to\mathcal E\), define
\[
\mathcal C.\operatorname{Op}_n
:=
\mathcal C\times^{h}_{\mathcal E}\operatorname{Op}_n(\mathcal E).
\]
It is the category of objects \(c\in\mathcal C\) equipped with an \(n\)-ary operation on \(F(c)\).

## 9. Diagram-extension classifiers

### Definition 9.1 (Boundary-extension datum) {#def-boundary-extension}

Let \(j:\partial K\to K\) be a morphism of small higher-categorical diagram shapes. Let \(\mathcal E\) be an ambient \(\infty\)-category, and let \(\mathcal B\) be a category already carrying the operations needed to construct a boundary diagram. A **boundary-extension datum** consists of a functor
\[
R_A:\mathcal B\longrightarrow\operatorname{Fun}(\partial K,\mathcal E).
\]
Restriction along \(j\) gives
\[
j^*:\operatorname{Fun}(K,\mathcal E)
\longrightarrow
\operatorname{Fun}(\partial K,\mathcal E).
\]

### Definition 9.2 (Diagram-extension classifier) {#def-diagram-extension-classifier}

The classifier of extensions of the \(A\)-boundary is the homotopy pullback
\[
\mathcal B.A
:=
\mathcal B
\times^{h}_{\operatorname{Fun}(\partial K,\mathcal E)}
\operatorname{Fun}(K,\mathcal E).
\]
An object is \(b\in\mathcal B\), a \(K\)-diagram \(\widetilde R_b\), and an equivalence
\[
j^*\widetilde R_b\simeq R_A(b).
\]
The fiber over \(b\) is the moduli space or moduli category of fillers of the operation-built boundary.

### Remark 9.3 (Why the whole boundary is used)

In a \(0\)-truncated setting, a commutative square can be expressed as equality of two composites, and an equifier gives an equivalent low-dimensional presentation. This ceases to be the appropriate primitive when fillers are nonidentity \(2\)-cells or when a coherence condition involves an entire polygon or higher cell. The boundary-extension construction retains the complete diagram and therefore extends uniformly to associators, braidings, pentagons, hexagons, and higher operadic coherences.

### Proposition 9.4 (Classification by the filler)

If the extension fiber over every \(b\) is \((-1)\)-truncated, then \(\mathcal B.A\to\mathcal B\) is property-like. If the extension fiber is a nontrivial set, groupoid, or higher category of choices, the classifier carries structure or stuff at the corresponding truncation level.

## 10. Operadic matching and coherent algebra

### Definition 10.1 (Operadic algebra classifier) {#def-operadic-classifier}

Let \(\mathcal M\) be a symmetric monoidal \(\infty\)-category and let \(\mathcal O\) be an \(\infty\)-operad. The category of \(\mathcal O\)-algebras is
\[
\operatorname{Alg}_{\mathcal O}(\mathcal M).
\]
The forgetful functor
\[
\operatorname{Alg}_{\mathcal O}(\mathcal M)
\longrightarrow
\mathcal M
\]
is the corresponding operadic classifier.

### Definition 10.2 (Cellular or matching-object presentation) {#def-matching-presentation}

Choose a cofibrant cellular presentation of \(\mathcal O\). At each stage \(r\), the lower operations determine a boundary in a matching object \(M_r\), defined as the homotopy limit over the proper faces of the \(r\)-th generating cell. The next stage is obtained by the homotopy pullback selecting fillers extending this prescribed boundary. The full category of algebras is the homotopy limit of the resulting tower.

The matching condition is essential: independent fillers of each shape need not satisfy operadic composition laws. Homotopy limits are essential: strict limits may not have the invariant homotopy type.

### Theorem 10.3 (Comparison with the standard operadic definition)

For a fixed cofibrant presentation of \(\mathcal O\), the matching-object tower presents a category equivalent to \(\operatorname{Alg}_{\mathcal O}(\mathcal M)\).

**Proof sketch.** A cellular operad is assembled by attaching operations along their operadically prescribed boundaries. Mapping it into the endomorphism operad of an object converts each attachment into a homotopy fiber of the corresponding matching map. Iterating and taking the homotopy limit gives precisely the derived mapping object of operads \(\operatorname{Map}(\mathcal O,\operatorname{End}(X))\). Varying \(X\) yields \(\operatorname{Alg}_{\mathcal O}(\mathcal M)\). \(\square\)

### Remark 10.4 (Dependence on an operad model)

Different cofibrant models of \(A_\infty\), \(E_n\), or \(E_\infty\) yield equivalent categories of algebras under the standard hypotheses, but not identical cell presentations. The chosen operad is mathematical data and should be named.

## 11. Grounding examples

### Example 11.1 (Associative operations on sets)

Let \(\mathcal B=\operatorname{Op}_2(\mathbf{Set})\), with universal multiplication \(\mu\). The associativity boundary is the square
\[
\begin{CD}
X^3 @>{\mu\times 1}>> X^2\\
@V{1\times\mu}VV @VV{\mu}V\\
X^2 @>{\mu}>> X.
\end{CD}
\]
The classifier is the pullback of the category of filled squares along the functor that builds this square from \((X,\mu)\). Since \(\mathbf{Set}\) has no nontrivial higher cells, the filler exists precisely when
\[
\mu(\mu\times 1)=\mu(1\times\mu),
\]
and is unique when it exists. Associativity is therefore a property of a chosen binary operation.

Adding a nullary operation \(e:\mathbf 1\to X\) and imposing the two unit diagrams gives monoids.

### Example 11.2 (Commutative operations on sets)

The commutativity boundary is
\[
\begin{CD}
X^2 @>{\tau}>> X^2\\
@V{\mu}VV @VV{\mu}V\\
X @>{1_X}>> X,
\end{CD}
\]
where \(\tau\) exchanges the factors. Again the filler is propositional, so commutativity is a property. The category of commutative monoids is obtained by the corresponding iterated homotopy pullbacks: first adjoin the binary and nullary operations, and then reindex the associativity, unit, and commutativity classifiers along the resulting structural functors.

### Example 11.3 (Monoidal categories)

Take \(\mathcal E=\mathbf{Cat}_{1}\). A binary operation is a bifunctor
\[
\otimes:\mathcal A\times\mathcal A\longrightarrow\mathcal A.
\]
The two reassociation composites are no longer required to be equal. An extension of the associativity boundary is a chosen natural isomorphism
\[
\alpha_{X,Y,Z}:(X\otimes Y)\otimes Z
\overset{\sim}{\longrightarrow}
X\otimes(Y\otimes Z).
\]
The associator is structure. Its pentagon is a further property classifier, obtained from the boundary of the associahedral coherence cell. A unit object and unitors are further structure; the triangle identity is a property. The resulting operadic category is the category of monoidal categories and strong monoidal functors for the chosen morphism convention.

### Example 11.4 (Braided and symmetric monoidal categories)

A braiding is a chosen natural isomorphism
\[
\beta_{X,Y}:X\otimes Y\overset{\sim}{\longrightarrow}Y\otimes X,
\]
hence structure. The hexagon identities are property classifiers. Symmetry imposes
\[
\beta_{Y,X}\circ\beta_{X,Y}=1_{X\otimes Y}.
\]
The operadic formulations are \(E_2\)-monoidal and \(E_\infty\)-monoidal categories, respectively.

### Remark 11.5 (Intermediate \(E_n\)-structures)

The exact stabilization stage of the \(E_n\)-tower in a truncated ambient is a theorem depending on the adopted operadic model and coherence conventions. The definitions in this report are the standard operadic definitions; no exact stabilization index beyond the grounding identifications \(E_2\) with braided and \(E_\infty\) with symmetric is built into the foundations.

***
# Part III. The algebraic categorical spine

## 12. Algebraic structures from operations and axioms

### Definition 12.1 (Magmas, semigroups, monoids, and groups) {#def-algebraic-tower}

The category of magmas is
\[
\mathbf{Mag}
:=
\operatorname{Op}_2(\mathbf{Set}).
\]
The category of semigroups is obtained by the associativity classifier. The category of monoids is obtained by adjoining a nullary operation and imposing associativity and the unit diagrams. The category of groups is obtained by adjoining an inverse operation and imposing the two inverse diagrams.

Each stage carries the canonical forgetful functor to the preceding one. Distant forgetful functors are composites, not additional primitive morphisms.

### Definition 12.2 (Operation roles) {#def-operation-role}

Let
\[
\mathsf{Role}:=\{\mathsf{add},\mathsf{mul}\}_{\mathrm{disc}}
\]
be the discrete two-point category. The category of role-decorated magmas is
\[
\mathsf{Role}\times\mathbf{Mag}.
\]
Its two components are denoted \(\mathbf{AddMag}\) and \(\mathbf{MulMag}\). Each is equivalent to \(\mathbf{Mag}\), but they are distinct objects in the normalized diagram because a ring has two structurally different operations.

Associativity, commutativity, units, and inverses are defined once on the undecorated operation theory and transported to each role component.

### Definition 12.3 (Rings) {#def-rings}

A ring is a set equipped with:

1. an additive abelian-group structure;
2. a multiplicative monoid structure;
3. left and right distributivity diagrams;
4. the usual compatibility of zero with multiplication, derived from distributivity and the additive group laws.

The category \(\mathbf{Ring}\) has ring homomorphisms as morphisms. It carries two distinguished structural functors
\[
U_{+}:\mathbf{Ring}\longrightarrow\mathbf{AddAbGrp},
\qquad
U_{\times}:\mathbf{Ring}\longrightarrow\mathbf{MulMon}.
\]
Their composites to \(\mathbf{Set}\) are canonically equivalent. A commutative ring is obtained by reindexing the commutativity classifier along \(U_{\times}\).

### Remark 12.4 (The ring diamond)

The additive and multiplicative routes are genuine parallel functors. The agreement of their underlying sets is coherence data. Replacing the two legs by one direct ring-to-set arrow hides this structure and prevents the multiplicative constructions, such as the unit group, from being recovered functorially.

### Remark 12.5 (Semirings and related algebraic objects)

Replacing the additive group in Definition 12.3 by a commutative additive monoid gives the
standard category of semirings. Nonunital rings, rngs, and other familiar variants are
obtained by omitting the corresponding operation or unit classifier. These are variations
of the same operation-and-diagram construction, not new foundational mechanisms.

## 13. Families of modules

### Definition 13.1 (The module category) {#def-module-category}

For a ring \(R\), let
\[
R\text{-}\mathbf{Mod}
\]
denote the category of left \(R\)-modules and \(R\)-linear maps. Right \(R\)-modules are left modules over the opposite ring:
\[
\mathbf{Mod}\text{-}R
:=
R^{\mathrm{op}}\text{-}\mathbf{Mod}.
\]
When \(R\) is commutative, the standard equivalence
\[
R\text{-}\mathbf{Mod}
\simeq
R^{\mathrm{op}}\text{-}\mathbf{Mod}
\]
is recorded as an equivalence, not as an equality of categories.

For general \(R\), no side-changing functor
\(R\text{-}\mathbf{Mod}\to R^{\mathrm{op}}\text{-}\mathbf{Mod}\) is supplied by the
opposite-ring involution alone; such a functor requires a chosen anti-homomorphism, and an
equivalence a chosen anti-isomorphism (Proposition 91.1). The commutative case above is the
canonical special instance (Corollary 91.2).

### Definition 13.2 (The total family of modules) {#def-total-module-family}

Let \(\mathbf{Ring}^{\simeq}\) be the core of the category of rings. Extension of scalars along ring isomorphisms gives a functor
\[
\mathbf{Ring}^{\simeq}
\longrightarrow
\mathfrak{Cat},
\qquad
R\longmapsto R\text{-}\mathbf{Mod}.
\]
Its Grothendieck construction is the category of pairs \((R,M)\), with \(M\) an \(R\)-module, and is denoted
\[
\int_{R\in\mathbf{Ring}^{\simeq}}R\text{-}\mathbf{Mod}.
\]
More generally, allowing arbitrary ring homomorphisms requires a choice of variance: restriction of scalars is contravariant in the ring, while extension of scalars is covariant and pseudofunctorial. The chosen variance must be stated whenever the total family is used. The two variances unstraighten to a cocartesian and a cartesian fibration over \(\mathbf{Ring}\) respectively; the precise four module-family functors and their total categories are Proposition 83.4 and Section 84, and the bimodule analogue over \(\mathbf{Ring}\times\mathbf{Ring}\) is Section 86.

### Definition 13.3 (Regular module section) {#def-regular-module}

The assignment
\[
R\longmapsto {}_RR
\]
defines the regular-module section of the module family. It is the mathematical reason that a ring is canonically a module over itself. This is not an additional forgetful functor from rings to a fixed module category; the codomain varies with \(R\).

### Definition 13.4 (Module-theoretic classifiers) {#def-module-classifiers}

The following are classifiers over \(R\text{-}\mathbf{Mod}\):

- finitely generated modules;
- finitely presented modules;
- projective modules;
- finite projective modules;
- free modules;
- finite-rank free modules;
- torsion modules and torsion-free modules, when \(R\) is a domain.

These conditions are owned at the module level. They are not obtained by pulling set-level conditions back along the underlying-set functor. For example, finite generation of an abelian group does not imply finite generation of its underlying additive monoid.

### Definition 13.5 (Framed generators and framed bases) {#def-module-generators-bases}

Fix \(n\ge0\). The comma category
\[
(R^n\downarrow R\text{-}\mathbf{Mod})
\]
has objects \((M,s)\) with \(s:R^n\to M\), and a morphism
\((M,s)\to(N,t)\) is a linear map \(f:M\to N\) satisfying \(fs=t\).
Define
\[
\operatorname{GenFrame}_n(R)
\subseteq
(R^n\downarrow R\text{-}\mathbf{Mod})
\]
to be the replete locus where \(s\) is surjective, and
\[
\operatorname{BasisFrame}_n(R)
\subseteq
(R^n\downarrow R\text{-}\mathbf{Mod})
\]
to be the locus where \(s\) is an isomorphism.

Thus a framed generating family is a chosen surjection from a standard free module, while a
framed basis is a chosen isomorphism from a standard free module. Morphisms preserve the
chosen frame. The projections to \(R\text{-}\mathbf{Mod}\) are the canonical comma-category
projections.

These fixed-source comma categories are the **strict frame-preserving** categories. They are
one of three distinct morphism conventions for modules with chosen generators: abstract
module maps (Definition 73.3), chosen free lifts (Definition 73.4), and strictly
frame-preserving maps as here. Strict frame preservation is the special case of a free lift
in which the upper map is the identity; see Remark 73.5. The general descent theory of
matrices through generating presentations is Section 74.

### Definition 13.6 (Coordinatized modules) {#def-coordinatized-module}

There is a second standard category with the same objects as
\(\operatorname{BasisFrame}_n(R)\): a morphism from \((M,e)\) to \((N,f)\) is an
arbitrary \(R\)-linear map \(M\to N\). Call this category \(\operatorname{Coord}_n(R)\).

The morphism is the abstract linear map; its matrix relative to the two chosen bases is a
derived representative, obtained by evaluating the bases. That every abstract morphism of
based free modules corresponds to exactly one matrix is the basis-case comparison theorem,
Corollary 74.5 — the kernel-zero special case of general matrix descent, not a definition.

The two categories answer different questions.

- \(\operatorname{BasisFrame}_n(R)\) classifies a basis as structure and uses
  basis-preserving morphisms.
- \(\operatorname{Coord}_n(R)\) is the category appropriate for matrix calculus and
  change of coordinates; its morphisms need not preserve either basis.

There is a faithful identity-on-objects functor from framed bases to coordinatized modules,
but the two categories are not identified.

### Remark 13.7 (Freeness versus a chosen basis)

For a module \(M\), let
\[
\operatorname{Basis}(M)
:=
\coprod_{n\ge 0}
\bigl(\operatorname{BasisFrame}_n(R)\bigr)_M
\]
be the space of finite ordered bases of \(M\). A chosen basis is a point of this space.
Freeness is the propositional truncation of the assertion that \(\operatorname{Basis}(M)\)
is inhabited. Thus freeness is a property, whereas a basis is structure. A category of
coordinatized modules is useful for matrix calculus but should not be substituted for the
basis-frame classifier.

The same property-versus-structure pattern governs the whole finiteness hierarchy: finite
generation is the truncation of the classifier of chosen generating presentations
(Definition 73.6), finite presentation of chosen finite presentations (Definition 75.4), and
the \(FP_n\) conditions of chosen partial finite projective resolutions (Definition 76.3).
Sections 73--77 develop this uniform theory and the accompanying descent of matrices.

The conversations used “based,” “with generators,” and “with basis” in several provisional
senses. This report therefore names the morphism convention whenever it matters.

### Definition 13.8 (Bimodules) {#def-bimodule-category}

For rings \(R\) and \(S\), an \((R,S)\)-bimodule is an abelian group \(M\) equipped with a
left \(R\)-action and a right \(S\)-action satisfying
\[
(rm)s=r(ms).
\]
Write
\[
{}_R\mathbf{Bimod}_S
\]
for the category of bimodules and bimodule homomorphisms: a morphism is a unary additive
map preserving both actions, not a “bilinear map.” The two actions are structure, their
coexistence on one additive group is the homotopy pullback
\(\mathbf{BiAct}(R,S)=R\text{-}\mathbf{Mod}\times^h_{\mathbf{Ab}}S^{\mathrm{op}}\text{-}\mathbf{Mod}\),
and their commutation is an additional property classifier (Definitions 85.2--85.3). There
is an unconditional canonical equivalence
\[
{}_R\mathbf{Bimod}_S
\simeq
(R\otimes_{\mathbb Z}S^{\mathrm{op}})\text{-}\mathbf{Mod}
\]
(Proposition 85.4); no centrality hypothesis is required.

The forgetful functors to \(R\text{-}\mathbf{Mod}\) and \(S^{\mathrm{op}}\text{-}\mathbf{Mod}\)
have canonically equivalent underlying additive-group composites (Proposition 87.2). They
are natural for restriction of scalars and only lax for simultaneous extension of scalars
(Theorem 88.1, Proposition 89.1). Extension and restriction of scalars for bimodules, their
adjunction, and the cocartesian and cartesian total families over
\(\mathbf{Ring}\times\mathbf{Ring}\) are Section 86. A unital \(\mathbb Z\)-action is
unique — the structure fiber over a fixed module is a singleton (Proposition 90.1.2) — so
\({}_R\mathbf{Bimod}_{\mathbb Z}\simeq R\text{-}\mathbf{Mod}\) canonically
(Corollary 90.2); an \((R,R)\)-bimodule is an \(R\)-module with an additional commuting
action, not an \(R\)-module (Proposition 92.1). Intrinsically, bimodules are the
\(1\)-morphisms of the Morita \((\infty,2)\)-category, whose hom categories from and to the
monoidal unit \(\mathbb Z\) recover the left and right module categories
(Definition 93.1, Proposition 93.2).

### Definition 13.9 (Algebras over a commutative ring) {#def-algebra-category}

Let \(R\) be commutative and endow \(R\text{-}\mathbf{Mod}\) with its tensor monoidal
structure. An associative unital \(R\)-algebra is an \(E_1\)-algebra object in this monoidal
category; a commutative \(R\)-algebra is a commutative or \(E_\infty\)-algebra object in the
appropriate truncation. Write
\[
\mathbf{Alg}_R,
\qquad
\mathbf{CAlg}_R
\]
for the corresponding categories. Their structural functors to modules, rings, and sets are
induced by the operadic forgetful morphisms and the algebraic spine.

## 14. Structures on categories

### Definition 14.1 (Preadditive, additive, and abelian categories) {#def-abelian-structure}

A preadditive category is a category enriched in abelian groups. An additive category is a preadditive category with finite biproducts. An abelian category is an additive category with kernels and cokernels such that every monomorphism and epimorphism is normal.

The forgetful map from categories with chosen preadditive structure to categories is a structure classifier. Relative to a chosen preadditive structure, the further additive and abelian axioms are property-like limit and exactness conditions. Thus the phrase “being abelian is a property” is always understood relative to the additive enrichment that makes the axioms meaningful.

### Definition 14.2 (Monoidal structures) {#def-monoidal-structure}

A monoidal structure on \(\mathcal C\) consists of a bifunctor \(\otimes\), a unit object, associator and unitors, and the pentagon and triangle coherences. Monoidal categories, strong monoidal functors, and monoidal natural transformations form a higher category
\[
\mathbf{MonCat}\longrightarrow\mathfrak{Cat}.
\]
The fiber over a fixed category can contain several inequivalent monoidal structures. A consumer must therefore specify the chosen lift, for example \(\otimes_R\) or \(\oplus\) on \(R\text{-}\mathbf{Mod}\).

### Definition 14.3 (Dualizable object) {#def-dualizable-object}

Let \((\mathcal C,\otimes,\mathbf 1)\) be a monoidal \(\infty\)-category. An object \(X\)
is **dualizable** if there exists an object \(X^\vee\) and morphisms
\[
\operatorname{coev}:\mathbf 1\to X\otimes X^\vee,
\qquad
\operatorname{ev}:X^\vee\otimes X\to\mathbf 1
\]
satisfying the two triangle identities. A choice of \(X^\vee\), evaluation, and coevaluation
is duality structure; dualizability itself is its propositional truncation. Perfect
complexes are the principal geometric example under the standard hypotheses.

### Remark 14.4 (Properties of categories as classifiers)

Properties such as “has finite limits,” “has kernels,” or “is idempotent complete” are represented by classifiers over \(\mathfrak{Cat}\). Chosen limits or chosen adjunctions may form nontrivial structure fibers even when mere existence is property-like. The report distinguishes these by the classifying fiber rather than by an informal label.

***

# Part IV. Bilinear and quadratic forms

## 15. Categories of forms

### Definition 15.1 (Bilinear forms with values in a module) {#def-bilinear-form}

Let \(R\) be a commutative ring, let \(M\) and \(W\) be \(R\)-modules. An \(R\)-bilinear form with values in \(W\) is an \(R\)-linear map
\[
b:M\otimes_R M\longrightarrow W,
\]
equivalently a map \(b:M\times M\to W\) linear in each variable.

The value module \(W\) is part of the defining data. The map from \(M\) to a dual module is derived from \(b\); it is not the definition of the form.

### Definition 15.2 (The bilinear-form category) {#def-bilinear-category}

Define \(\mathbf{Bil}_{R,W}\) as follows.

- An object is a pair \((M,b)\), where \(M\in R\text{-}\mathbf{Mod}\) and \(b:M\otimes_RM\to W\) is bilinear.
- A morphism
  \[
  f:(M,b_M)\longrightarrow(N,b_N)
  \]
  is an \(R\)-linear map \(f:M\to N\) such that
  \[
  b_M=b_N\circ(f\otimes f).
  \]

The projection
\[
\pi_{\mathrm{Bil}}:\mathbf{Bil}_{R,W}\longrightarrow R\text{-}\mathbf{Mod}
\]
forgets the form.

Equivalently, \(\mathbf{Bil}_{R,W}\) is the category of elements of the contravariant functor
\[
\operatorname{Bil}_{R,W}:
(R\text{-}\mathbf{Mod})^{\mathrm{op}}
\longrightarrow R\text{-}\mathbf{Mod},
\qquad
M\longmapsto\operatorname{Hom}_R(M\otimes_RM,W),
\]
after applying the underlying-space or underlying-set functor. The explicit definition above fixes the variance convention: morphisms preserve the source form by pullback.

### Definition 15.3 (Quadratic map) {#def-quadratic-map}

A quadratic map \(q:M\to W\) is a function satisfying
\[
q(rx)=r^2q(x)
\]
for \(r\in R\), and such that its raw polarization
\[
\beta_q(x,y)
:=
q(x+y)-q(x)-q(y)
\]
is \(R\)-bilinear. The precise definition may be adjusted to the conventional notion of quadratic map over a general base ring; the bilinearity of \(\beta_q\) is the datum used below.

### Definition 15.4 (The quadratic-form category) {#def-quadratic-category}

Define \(\mathbf{Quad}_{R,W}\) to have objects \((M,q)\) and morphisms \(f:M\to N\) satisfying
\[
q_M=q_N\circ f.
\]
It carries the projection
\[
\pi_{\mathrm{Quad}}:\mathbf{Quad}_{R,W}\longrightarrow R\text{-}\mathbf{Mod}.
\]

### Definition 15.5 (Change of values) {#def-change-values}

For an \(R\)-linear map \(u:W\to W'\), postcomposition defines functors
\[
u_*:\mathbf{Bil}_{R,W}\longrightarrow\mathbf{Bil}_{R,W'},
\qquad
u_*:\mathbf{Quad}_{R,W}\longrightarrow\mathbf{Quad}_{R,W'}.
\]
The functoriality in \(W\) is part of the parameterized theory of forms.

### Definition 15.6 (Base change) {#def-form-base-change}

For a homomorphism of commutative rings \(R\to S\), extension of scalars defines, under the standard tensor-product hypotheses, functors
\[
S\otimes_R-:
\mathbf{Bil}_{R,W}
\longrightarrow
\mathbf{Bil}_{S,S\otimes_R W}
\]
and similarly for quadratic maps. The scalar-extended form is characterized by
\[
(S\otimes b)((s\otimes x),(t\otimes y))
=st\otimes b(x,y).
\]

### Definition 15.7 (Hermitian and sesquilinear forms) {#def-hermitian-form}

Let \(R\) be a commutative ring equipped with an involution \(r\mapsto\bar r\). A
sesquilinear form on an \(R\)-module \(M\), with values in an involutive \(R\)-module
\(W\), is additive in each variable and satisfies
\[
h(rx,sy)=r\,h(x,y)\,\bar s.
\]
It is **Hermitian** if
\[
h(y,x)=\overline{h(x,y)}.
\]
Hermitian modules and form-preserving linear maps form a category
\(\mathbf{Herm}_{R,W}\) with a structural functor to \(R\text{-}\mathbf{Mod}\). The
construction is the sesquilinear analogue of Definitions 15.1--15.2 and supplies the standard
home for unitary lattices when they are needed.

## 16. Symmetry conditions

### Definition 16.1 (Symmetric, skew-symmetric, and alternating) {#def-form-symmetries}

For \((M,b)\in\mathbf{Bil}_{R,W}\), define:

\[
\begin{aligned}
\operatorname{Sym}(b)
&:\Longleftrightarrow
b(x,y)=b(y,x),\\
\operatorname{Skew}(b)
&:\Longleftrightarrow
b(x,y)=-b(y,x),\\
\operatorname{Alt}(b)
&:\Longleftrightarrow
b(x,x)=0
\quad\text{for all }x.
\end{aligned}
\]

Each condition defines a property classifier over \(\mathbf{Bil}_{R,W}\). They are defined independently at the bilinear-form level.

### Lemma 16.2 (Alternating implies skew-symmetric) {#lem-alt-skew}

Every alternating bilinear form is skew-symmetric.

**Proof.** Expanding \(b(x+y,x+y)=0\) and using alternation on \(x\) and \(y\) gives
\[
b(x,y)+b(y,x)=0.
\]
\(\square\)

### Lemma 16.3 (Converse under injectivity of two) {#lem-skew-alt}

If multiplication by \(2\) on \(W\) is injective, every skew-symmetric form is alternating.

**Proof.** Skew-symmetry gives \(b(x,x)=-b(x,x)\), hence \(2b(x,x)=0\). Injectivity implies \(b(x,x)=0\). \(\square\)

### Remark 16.4

The implication in Lemma 16.2 is a theorem, not part of the definition of alternating forms. In characteristic \(2\), or whenever \(W\) has \(2\)-torsion, alternating and skew-symmetric forms remain distinct.

## 17. Diagonal, polarization, and quadratic refinements

### Definition 17.1 (Diagonal and polarization functors) {#def-diag-polar}

The diagonal construction sends a symmetric bilinear form to the quadratic map
\[
\operatorname{diag}(b)(x):=b(x,x).
\]
The polarization construction sends a quadratic map to the symmetric bilinear form
\[
\operatorname{polar}(q):=\beta_q.
\]
These are induced by natural transformations at the functor level and hence define functors between the corresponding categories.

### Lemma 17.2 (The factor of two) {#lem-factor-two}

For a symmetric bilinear form \(b\),
\[
\operatorname{polar}(\operatorname{diag}(b))=2b.
\]
For a quadratic map \(q\) satisfying \(q(2x)=4q(x)\),
\[
\operatorname{diag}(\operatorname{polar}(q))=2q.
\]

**Proof.** The first identity is the bilinear expansion
\[
b(x+y,x+y)-b(x,x)-b(y,y)=2b(x,y).
\]
The second is
\[
\beta_q(x,x)=q(2x)-2q(x)=2q(x).
\]
\(\square\)

### Proposition 17.3 (Equivalence when two is invertible) {#prop-quad-sym-equivalence}

If multiplication by \(2\) is invertible on \(W\), diagonal and half-polarization define inverse equivalences between the appropriate categories of quadratic forms and symmetric bilinear forms:
\[
q\longmapsto \tfrac12\operatorname{polar}(q),
\qquad
b\longmapsto \operatorname{diag}(b).
\]

### Definition 17.4 (Quadratic refinement classifier) {#def-quadratic-refinement}

Let \((M,b)\) be a symmetric bilinear form. A **quadratic refinement** of \(b\) is a quadratic map \(Q:M\to W\) together with an identification
\[
\operatorname{polar}(Q)=b.
\]
The total category of refined forms is the homotopy pullback of the polarization functor along the inclusion of the chosen symmetric form.

The classifying fiber over \(b\) is the moduli object of its quadratic refinements. It can be empty, contractible, or nontrivial. Consequently, “having a quadratic refinement” is property-like only under hypotheses guaranteeing uniqueness.

### Definition 17.5 (Even integral form) {#def-even-form}

For a symmetric integral bilinear form \(b:M\times M\to\mathbb Z\), define
\[
\operatorname{Even}(b)
:\Longleftrightarrow
b(x,x)\in2\mathbb Z
\quad\text{for every }x\in M.
\]
Equivalently, \(b\) admits the integral quadratic refinement
\[
Q_b(x)=\frac{b(x,x)}2,
\qquad
\operatorname{polar}(Q_b)=b.
\]
The quotient by two is exact divisibility data; it is not integer truncation. This equivalence uses the injectivity of multiplication by \(2\) on \(\mathbb Z\).

### Remark 17.6 (Two quadratic conventions)

Two related quadratic objects must not be confused.

1. For an even integral lattice,
   \[
   Q_L(x)=\frac{b(x,x)}2\in\mathbb Z,
   \qquad
   Q_L(x+y)-Q_L(x)-Q_L(y)=b(x,y).
   \]
2. For its finite discriminant group,
   \[
   q_L(\bar x)=b_K(x,x)\bmod 2\mathbb Z,
   \]
   and
   \[
   q_L(a+b)-q_L(a)-q_L(b)=2b_L(a,b)
   \quad\text{in }\mathbb Q/2\mathbb Z.
   \]

The first refines an integral bilinear form; the second is a finite quadratic form valued modulo \(2\mathbb Z\).

## 18. Adjoint maps, radicals, and perfectness

### Definition 18.1 (Adjoint of a bilinear form) {#def-form-adjoint}

For \(b:M\otimes_RM\to W\), define its adjoint
\[
\widetilde b:M\longrightarrow\operatorname{Hom}_R(M,W),
\qquad
x\longmapsto b(x,-).
\]
This is derived from the \(W\)-valued form by currying.

### Definition 18.2 (Radical and defect module) {#def-radical-defect}

Define
\[
\operatorname{rad}(M,b):=\ker(\widetilde b),
\qquad
\operatorname{Def}(M,b):=\operatorname{coker}(\widetilde b).
\]
These objects occur in the canonical exact sequence
\[
0\longrightarrow
\operatorname{rad}(M,b)
\longrightarrow M
\xrightarrow{\widetilde b}
\operatorname{Hom}_R(M,W)
\longrightarrow
\operatorname{Def}(M,b)
\longrightarrow0.
\]
The sequence, rather than the isolated map \(\widetilde b\), is the governing object.

### Definition 18.3 (Radical-free and perfect form) {#def-nondegenerate-perfect}

A form is **radical-free** or **separating** if
\[
\operatorname{rad}(M,b)=0.
\]
It is **perfect** if \(\widetilde b\) is an isomorphism, equivalently if
\[
\operatorname{rad}(M,b)=0
\quad\text{and}\quad
\operatorname{Def}(M,b)=0.
\]
For an integral lattice, perfectness is also called unimodularity.

### Remark 18.4 (Terminology “nondegenerate”)

The literature uses “nondegenerate” for several related conditions: trivial radical, injective adjoint, perfect pairing, or nondegeneracy after extension to a fraction field. This report always names the precise condition. In the arithmetic lattice category below, **generically nondegenerate** means nondegenerate after extending scalars to the fraction field.

***

# Part V. Intrinsic lattices and their enhancements

## 19. Intrinsic lattices

### Definition 19.1 (Arithmetic base) {#def-arithmetic-base}

Let \(R\) be a Dedekind domain with fraction field \(K\). The principal examples are \(R=\mathbb Z\) and rings of integers in number fields.

### Definition 19.2 (Intrinsic \(R\)-lattice) {#def-intrinsic-lattice}

An **intrinsic \(R\)-lattice** is a pair \((L,b)\) such that:

1. \(L\) is a finite projective \(R\)-module;
2. \(b:L\otimes_RL\to R\) is symmetric;
3. the scalar extension
   \[
   b_K:(L\otimes_RK)\otimes_K(L\otimes_RK)\longrightarrow K
   \]
   is nondegenerate.

The category \(\mathbf{Lat}_R\) has intrinsic lattices as objects and form-preserving \(R\)-linear maps as morphisms:
\[
b_L(x,y)=b_M(fx,fy).
\]
The core \(\mathbf{Lat}_R^{\simeq}\) is the isometry groupoid.

### Remark 19.3 (Natural generality)

Finite projectivity is the intrinsic arithmetic condition. Freeness and a chosen basis are further enhancements. Over a principal ideal domain, finite projective modules are free, but the definition is not specialized to that case.

### Proposition 19.4 (Adjoint sequence for a lattice)

For an intrinsic lattice, the adjoint
\[
\widetilde b:L\longrightarrow L^*:=\operatorname{Hom}_R(L,R)
\]
is injective and has a finitely generated torsion cokernel.

**Proof sketch.** After tensoring with \(K\), \(\widetilde b\) becomes an isomorphism by generic nondegeneracy. Since \(L\) is projective and therefore torsion-free, the kernel vanishes. The cokernel is finitely generated and becomes zero after tensoring with \(K\), hence is a finite-length torsion module. Its underlying set is finite only under additional arithmetic hypotheses, for example when the relevant residue rings are finite. \(\square\)

### Definition 19.5 (Even and unimodular lattices) {#def-even-unimodular-lattice}

For \(R=\mathbb Z\), an intrinsic lattice is **even** if its bilinear form is even in the sense of Definition 17.5. It is **unimodular** if the adjoint \(L\to L^*\) is an isomorphism.

The corresponding categories are reindexings of the evenness and perfectness classifiers along \(\mathbf{Lat}_{\mathbb Z}\to\mathbf{SymBil}_{\mathbb Z,\mathbb Z}\).

## 20. Signature and definiteness

### Definition 20.1 (Signature) {#def-signature}

For an integral lattice \(L\), extend scalars to \(\mathbb R\). By Sylvester's law of inertia, the real symmetric bilinear form is congruent to a diagonal form with \(p\) positive and \(q\) negative entries. The pair
\[
\operatorname{sig}(L)=(p,q)
\]
is the signature.

The terms positive definite, negative definite, and indefinite refer to \((p,0)\), \((0,q)\), and \(p,q>0\), respectively. A hyperbolic lattice is an indefinite lattice in the specified hyperbolic class; the word is not used as a synonym for every indefinite lattice.

### Remark 20.2

A rational or integral certificate for the signature may be used to verify a computation, but the mathematical definition is the inertia of the real scalar extension.

## 21. Framed, coordinatized, and Gram descriptions

### Definition 21.1 (Framed and coordinatized lattices) {#def-framed-coordinatized-lattice}

Let
\[
U:\mathbf{Lat}_R\longrightarrow R\text{-}\mathbf{Mod}
\]
be the underlying-module functor. Define the categories of lattices with frame-preserving
generators and bases by the homotopy pullbacks
\[
\mathbf{Lat}^{\operatorname{genfr},n}_R
:=
\mathbf{Lat}_R
\times^{h}_{R\text{-}\mathbf{Mod}}
\operatorname{GenFrame}_n(R),
\]
and
\[
\mathbf{Lat}^{\operatorname{basfr},n}_R
:=
\mathbf{Lat}_R
\times^{h}_{R\text{-}\mathbf{Mod}}
\operatorname{BasisFrame}_n(R).
\]
An object of the first is a lattice with an ordered generating frame; an object of the
second is a lattice with an ordered basis, and morphisms preserve that basis.

For matrix calculus, define instead
\[
\mathbf{Lat}^{\operatorname{coord},n}_R
:=
\mathbf{Lat}_R
\times^{h}_{R\text{-}\mathbf{Mod}}
\operatorname{Coord}_n(R).
\]
Its objects also carry ordered bases, but its morphisms are arbitrary form-preserving maps
represented by matrices relative to the chosen bases. The framed and coordinatized categories
must not be conflated.

### Definition 21.2 (Symmetric matrix category) {#def-symmetric-matrix-category}

Fix \(n\). Let \(\mathbf{SymMat}_n(R)\) be the category whose objects are symmetric matrices
\[
G\in\operatorname{Mat}_n(R)
\]
and whose morphisms \(A:G\to H\) are matrices satisfying
\[
A^{\mathsf T}HA=G.
\]
Restricting to matrices nondegenerate over \(K\) gives \(\mathbf{SymMat}_n(R)^{\operatorname{nd}}\).

This matrix category is explicitly a skeletal coordinate presentation of the category of
symmetric forms on the standard free module \(R^n\); it is not a second kind of mathematical
object. Its comparison with the category of coordinatized forms is the named equivalence of
Definition 21.3, whose morphisms are abstract form-preserving linear maps with matrices
obtained by applying the chosen source and target bases (Corollary 74.5).

### Definition 21.3 (Gram constructor) {#def-gram-constructor}

Define the category of coordinatized bilinear forms by
\[
\mathbf{Bil}^{\operatorname{coord},n}_{R,R}
:=
\mathbf{Bil}_{R,R}
\times^h_{R\text{-}\mathbf{Mod}}
\operatorname{Coord}_n(R).
\]
The Gram constructor is the functor
\[
\operatorname{Gram}_n:
\mathbf{SymMat}_n(R)
\longrightarrow
\mathbf{Bil}^{\operatorname{coord},n}_{R,R}
\]
that sends \(G\) to the standard module \(R^n\), its standard basis, and the form
\[
b_G(x,y)=x^{\mathsf T}Gy.
\]
After restricting to \(\mathbf{SymMat}_n(R)^{\operatorname{nd}}\), it lands in coordinatized lattices.

Conversely, a coordinatized form \((L,b,e_1,\ldots,e_n)\) determines its Gram matrix
\[
G_{ij}=b(e_i,e_j).
\]
These constructions give a named equivalence theorem between coordinatized bilinear forms of
rank \(n\) and Gram matrices. The morphisms of the coordinatized category are abstract
form-preserving linear maps; a matrix is obtained from a morphism by applying the chosen
source and target bases, and represents it by the basis-case comparison of Corollary 74.5.
The basis-preserving framed category has a different, stricter morphism convention.

For the named ADE lattices the Gram constructor is used only after the root-presentation
Gram matrix has been derived from a chosen root realization, and its output is compared to
the root lattice by Theorem 72.2. It constructs coordinatized forms in general; it is not
the ontology of the named root lattices.

### Remark 21.4 (Intrinsic object versus constructor)

A Gram matrix is not an alternative kind of lattice. It is a coordinate description of an object in the category of coordinatized lattices. The composite
\[
\mathbf{SymMat}_n(R)^{\operatorname{nd}}
\longrightarrow
\mathbf{Lat}^{\operatorname{coord},n}_R
\longrightarrow
\mathbf{Lat}_R
\]
constructs the corresponding intrinsic lattice while retaining a distinguished basis in the first codomain.

## 22. Orthogonal sum, scaling, and duality of sign

### Definition 22.1 (Orthogonal sum) {#def-orthogonal-sum}

For lattices \((L,b_L)\) and \((M,b_M)\), define
\[
L\perp M
:=
(L\oplus M,b_L\oplus b_M),
\]
where the two summands are orthogonal. This gives a symmetric monoidal structure on the lattice category under the appropriate morphism convention.

### Remark 22.2 (Not generally a categorical coproduct)

Orthogonal sum is not automatically the categorical coproduct in the category of form-preserving maps: a pair of maps out of \(L\) and \(M\) extends to a form-preserving map from \(L\perp M\) only when the two images are orthogonal. It is therefore recorded as a monoidal product, not identified with a coproduct without a theorem.

### Definition 22.3 (Scaling) {#def-lattice-scaling}

For \(a\in R\), define
\[
L(a):=(L,a\,b_L).
\]
When \(a\ne0\), generic nondegeneracy is preserved. The sign reversal is
\[
-L:=L(-1).
\]

## 23. Standard lattices and the sign convention

### Definition 23.1 (Rank-one and hyperbolic lattices) {#def-rank-one-U}

The rank-one lattice \(\langle a\rangle\) has Gram matrix \([a]\). The hyperbolic plane \(U\) has Gram matrix
\[
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

### Definition 23.2 (ADE root lattices) {#def-ade-lattices}

The project adopts the algebraic-geometric convention that all simply-laced ADE root
lattices are **negative definite**. A named ADE lattice is the root lattice of a chosen
standard root realization (Construction 68.6): the intrinsic lattice is the integral span of
the roots with the restricted ambient form, after the negative sign convention. The root
basis and the ambient embedding are additional data, and the Gram matrix is derived from the
chosen root basis (Definition 69.2). The construction order is fixed by Convention 72.3.

The standard realizations are those of Section 71:
\[
A_n\subset I_{n+1}^-,
\qquad
D_n\subset I_n^-,
\qquad
E_8\subset\mathbb Q^8
\]
with integral-or-half-integral coordinates and even coordinate sum for \(E_8\), and
\(E_7,E_6\) the orthogonal-complement root sublattices of \(E_8\) from Definition 71.4. Bare
ADE names denote these negative-definite lattices (Convention 71.5).

In particular, \(E_8\) denotes the negative-definite even unimodular lattice of rank \(8\).
Its positive-definite sign reversal is \(-E_8\).

The lattices are **not** defined by their Cartan matrices. The equality \(G_\Delta=-C_\Delta\)
of a simple-root Gram matrix with the negated Cartan matrix in simply-laced type is the
derived comparison theorem of Proposition 70.2, valid only after a simple-root basis,
normalization, and sign convention have been chosen; Cartan matrices have no role in the
primary construction (Convention 70.4).

### Definition 23.3 (Even unimodular indefinite lattices) {#def-IIpq}

Write \(II_{p,q}\) for the standard even unimodular lattice of signature \((p,q)\), when it exists. Write \(L^{\perp m}\) for the \(m\)-fold orthogonal sum of a lattice \(L\). With the negative-definite convention for \(E_8\), one may take
\[
II_{p,q}
=
\begin{cases}
U^{\perp p}\perp E_8^{\perp (q-p)/8},&p\le q,\\
U^{\perp q}\perp (-E_8)^{\perp (p-q)/8},&p\ge q,
\end{cases}
\]
when \(p-q\equiv0\pmod 8\).

The congruence condition and uniqueness up to isometry are classification theorems; they are not built into the definition of lattice.

### Convention 23.4 (K3 and Enriques lattices) {#conv-k3-lattice}

Under the adopted convention,
\[
\Lambda_{K3}=II_{3,19}=U^{\perp 3}\perp E_8^{\perp 2},
\]
and
\[
II_{1,9}=U\perp E_8.
\]
Writing \(E_8(-1)\) in the first formula would reverse an already negative-definite lattice and is therefore incompatible with this convention.

***
# Part VI. Duality, discriminant forms, and lattice constructions

## 24. Module duals and metric duals

### Definition 24.1 (Module dual) {#def-module-dual}

For an \(R\)-module \(M\), its module dual is
\[
M^*:=\operatorname{Hom}_R(M,R).
\]
This definition is independent of any bilinear form.

### Definition 24.2 (Rational span) {#def-rational-span}

For a finite projective module \(L\) over the Dedekind domain \(R\), define
\[
V_L:=L\otimes_RK.
\]
The natural map \(L\to V_L\) is injective.

### Definition 24.3 (Metric dual) {#def-metric-dual}

Let \((L,b)\) be an intrinsic \(R\)-lattice. Its metric dual is
\[
L^{\#}
:=
\{x\in V_L\mid b_K(x,L)\subseteq R\}.
\]
More generally, if \(W\subseteq W_K\) is a chosen value lattice in a \(K\)-vector space and \(b_K:V_L\times V_L\to W_K\), define
\[
L^{\#}_{b,W}
:=
\{x\in V_L\mid b_K(x,L)\subseteq W\}.
\]
The usual metric dual is the case \(W=R\).

### Proposition 24.4 (Comparison with the module dual) {#prop-metric-module-dual}

Generic nondegeneracy of \(b\) induces an isomorphism
\[
L^{\#}\overset{\sim}{\longrightarrow}L^*,
\qquad
x\longmapsto b_K(x,-)|_L.
\]
Under this isomorphism, the inclusion \(L\hookrightarrow L^{\#}\) corresponds to the adjoint \(\widetilde b:L\to L^*\).

**Proof sketch.** The map \(V_L\to V_L^*\) induced by \(b_K\) is an isomorphism. The inverse image of \(L^*\subseteq V_L^*\) is precisely the defining integrality condition for \(L^{\#}\). \(\square\)

### Definition 24.5 (Discriminant module) {#def-discriminant-module}

The discriminant module of \(L\) is
\[
A_L:=L^{\#}/L.
\]
It is a finitely generated torsion \(R\)-module, hence of finite length. By Proposition 24.4 there is a canonical isomorphism
\[
A_L\simeq\operatorname{coker}(\widetilde b).
\]
The quotient \(L^{\#}/L\) is the definition; the cokernel description is a comparison theorem arising from the governing diagram.

### Diagram 24.6 (The comparison of exact sequences) {#diag-dual-comparison}

The two presentations fit into a commutative diagram with exact rows
\[
\begin{CD}
0@>>>L@>>>L^{\#}@>>>A_L@>>>0\\
@.@|@V{\sim}VV@V{\sim}VV@.\\
0@>>>L@>{\widetilde b}>>L^*@>>>\operatorname{coker}(\widetilde b)@>>>0.
\end{CD}
\]
This diagram is the natural home of the discriminant module and the comparison isomorphism.

## 25. Discriminant bilinear and quadratic forms

### Definition 25.1 (Discriminant bilinear form) {#def-discriminant-bilinear-form}

Let \(L\) be an intrinsic \(R\)-lattice. The discriminant bilinear form is
\[
b_L:A_L\times A_L\longrightarrow K/R,
\qquad
b_L(x+L,y+L)=b_K(x,y)\bmod R.
\]
This is well-defined because \(x,y\in L^{\#}\), and changing either lift by an element of \(L\) changes the value by an element of \(R\).

### Proposition 25.2 (Perfectness of the discriminant pairing) {#prop-discriminant-perfect}

The pairing \(b_L\) is perfect in the torsion sense: the adjoint
\[
A_L\longrightarrow\operatorname{Hom}_R(A_L,K/R)
\]
is an isomorphism.

This is the finite-length torsion counterpart of generic nondegeneracy of \(L\).

### Definition 25.3 (Category of discriminant bilinear forms) {#def-discbil-category}

Let \(\mathbf{DiscBil}_R\) be the category whose objects are finitely generated torsion \(R\)-modules \(A\) equipped with a symmetric perfect pairing
\[
b:A\times A\longrightarrow K/R,
\]
and whose morphisms are pairing-preserving \(R\)-linear maps.

For \(R=\mathbb Z\), the value group is \(\mathbb Q/\mathbb Z\).

### Definition 25.4 (Finite quadratic form) {#def-finite-quadratic-form}

A finite quadratic form is a finite abelian group \(A\) together with a map
\[
q:A\longrightarrow\mathbb Q/2\mathbb Z
\]
such that the expression
\[
q(x+y)-q(x)-q(y)
\]
is the double of a symmetric bilinear form
\[
b_q:A\times A\longrightarrow\mathbb Q/\mathbb Z.
\]
Equivalently, using the canonical isomorphism
\[
\mathbb Q/\mathbb Z
\overset{\times2}{\longrightarrow}
\mathbb Q/2\mathbb Z,
\]
\(b_q\) is obtained by inverse bilinearization. The form is nondegenerate if \(b_q\) is perfect.

### Definition 25.5 (Category of discriminant quadratic forms) {#def-discquad-category}

The category \(\mathbf{DiscQuad}_{\mathbb Z}\) is the pullback
\[
\mathbf{Quad}_{\mathbb Z,\mathbb Q/2\mathbb Z}
\times^{h}_{\mathbf{SymBil}_{\mathbb Z,\mathbb Q/\mathbb Z}}
\mathbf{DiscBil}_{\mathbb Z}
\]
along bilinearization. Thus a quadratic discriminant form is a quadratic object whose bilinearization is a finite nondegenerate bilinear discriminant form. It is not defined as an “even bilinear form.”

### Definition 25.6 (Discriminant quadratic form of an even lattice) {#def-lattice-discriminant-quadratic}

If \(L\) is even, define
\[
q_L:A_L\longrightarrow\mathbb Q/2\mathbb Z,
\qquad
q_L(x+L)=b_K(x,x)\bmod2\mathbb Z.
\]
The evenness of \(L\) is exactly what makes this independent of the choice of lift. Its bilinearization is \(b_L\).

## 26. Discriminant functors and automorphism groups

### Definition 26.1 (Discriminant functors) {#def-discriminant-functors}

The discriminant constructions are functorial under isometries and therefore define functors on cores:
\[
\operatorname{Disc}_{\mathrm{bil}}:
\mathbf{Lat}_{R}^{\simeq}
\longrightarrow
\mathbf{DiscBil}_{R}^{\simeq},
\]
and
\[
\operatorname{Disc}_{\mathrm{quad}}:
\mathbf{EvenLat}_{\mathbb Z}^{\simeq}
\longrightarrow
\mathbf{DiscQuad}_{\mathbb Z}^{\simeq}.
\]

The foundational domain is the core. Arbitrary form-preserving embeddings do not canonically induce morphisms of discriminant forms in the same direction.

### Definition 26.2 (Orthogonal group) {#def-orthogonal-group}

For a lattice \(L\), its orthogonal group is
\[
O(L):=\operatorname{Aut}_{\mathbf{Lat}_R}(L).
\]
For a discriminant form \((A,q)\), define
\[
O(A,q):=\operatorname{Aut}_{\mathbf{DiscQuad}}(A,q).
\]
These are values of the generic automorphism construction, not separate categorical primitives.

### Definition 26.3 (Discriminant representation and stable orthogonal group) {#def-stable-orthogonal}

Applying automorphisms to the discriminant functor gives the discriminant representation
\[
\rho_L:O(L)\longrightarrow O(A_L,q_L)
\]
for an even lattice. The stable orthogonal group is
\[
\widetilde O(L):=\ker(\rho_L).
\]
No surjectivity of \(\rho_L\) is part of the definition.

### Remark 26.4 (Coordinatized matrix representation)

A chosen basis of a free lattice of rank \(n\) identifies every isometry with its matrix and
gives an injective representation
\[
O(L)\hookrightarrow GL_n(R).
\]
This representation is attached to a coordinatized lift of \(L\), whose morphisms are not
required to fix the basis. In the basis-frame category, by contrast, automorphisms preserve
the chosen frame and are generally much smaller. The matrix realization is therefore not an
intrinsic identification of \(O(L)\) independent of coordinates.

### Remark 26.5 (Automorphisms of finitely generated torsion modules)

A finitely generated torsion module with invariant factors need not be free over a single quotient ring. Consequently its automorphism group, and the orthogonal group of a general discriminant form, need not be canonically a subgroup of one \(GL_n(R/I)\). In general it is naturally obtained as a quotient of a congruence-type stabilizer group. In the homocyclic case \(A\simeq(R/I)^n\), the familiar matrix subgroup description is valid.

This distinction is mathematical: replacing a quotient presentation by a matrix subgroup can change the group.

## 27. Overlattices and gluing

### Definition 27.1 (Overlattice) {#def-overlattice}

Let \(L\) be an integral lattice with rational span \(V_L\). An **overlattice** of \(L\) is an integral lattice \(L'\subseteq V_L\) such that
\[
L\subseteq L'\subseteq L^{\#}
\]
and \(L'/L\) is finite. It is even if the restricted form on \(L'\) is even.

Overlattices can be organized as a locus in the arrow category of lattices, or as a category over \(L\) whose morphisms are isometries compatible with the inclusions.

### Definition 27.2 (Isotropic subgroup) {#def-isotropic-subgroup}

Let \((A,q)\) be a finite quadratic form. A subgroup \(H\subseteq A\) is **isotropic** if
\[
q|_H=0.
\]
For a bilinear discriminant form, isotropic means \(b|_{H\times H}=0\).

### Construction 27.3 (Overlattice from a subgroup) {#construction-overlattice-subgroup}

For \(H\subseteq A_L=L^{\#}/L\), define
\[
L_H:=\{x\in L^{\#}\mid x+L\in H\}.
\]
Then \(L\subseteq L_H\subseteq L^{\#}\) and \(L_H/L\simeq H\).

### Theorem 27.4 (Overlattice–isotropic subgroup correspondence) {#thm-overlattice-isotropic}

For an even lattice \(L\), the construction \(H\mapsto L_H\) gives a correspondence between even overlattices of \(L\) and isotropic subgroups of \((A_L,q_L)\). Moreover,
\[
A_{L_H}\simeq H^{\perp}/H
\]
with the induced quadratic form.

This is a classical theorem of discriminant-form theory. It is not part of the definition of an overlattice or of an isotropic subgroup.

### Definition 27.5 (Anti-isometry) {#def-anti-isometry}

Let \((A_1,q_1)\) and \((A_2,q_2)\) be finite quadratic forms. An **anti-isometry** between subgroups \(H_i\subseteq A_i\) is an isomorphism
\[
\varphi:H_1\overset{\sim}{\longrightarrow}H_2
\]
satisfying
\[
q_2(\varphi x)=-q_1(x).
\]

### Construction 27.6 (Gluing) {#construction-gluing}

The graph
\[
\Gamma_{\varphi}
:=
\{(x,\varphi x)\mid x\in H_1\}
\subseteq
A_1\oplus A_2
\]
is isotropic for \(q_1\oplus q_2\). The corresponding overlattice of \(L_1\perp L_2\) is the lattice obtained by gluing \(L_1\) and \(L_2\) along \(\varphi\).

The equivalence between suitable gluing data and suitable overlattices is a theorem constructed from Theorem 27.4.

## 28. Embeddings, markings, and actions

### Definition 28.1 (Primitive embedding) {#def-primitive-embedding}

An isometric embedding
\[
i:L\hookrightarrow M
\]
is **primitive** if the cokernel of the underlying module map is torsion-free. Primitive embeddings form a locus in the arrow category \(\operatorname{Ar}(\mathbf{Lat}_R)\).

### Definition 28.2 (Orthogonal complement) {#def-orthogonal-complement}

For an isometric embedding \(i:L\hookrightarrow M\), define
\[
i(L)^{\perp}
:=
\{m\in M\mid b_M(m,i(L))=0\}.
\]
Under the usual nondegeneracy and projectivity hypotheses this is a lattice. Its relation to \(L\), \(M\), and their discriminant forms is theorem-level gluing data.

### Definition 28.3 (Marking) {#def-marking}

Fix a reference lattice \(\Lambda\). A **marking** of a lattice \(L\) is an isometry
\[
\eta:\Lambda\overset{\sim}{\longrightarrow}L.
\]
Marked lattices form the appropriate coslice or comma category over the core of lattices.

### Definition 28.4 (Group action and involution) {#def-lattice-action}

For a group \(G\), a \(G\)-action on a lattice is a functor
\[
BG\longrightarrow\mathbf{Lat}_R^{\simeq}.
\]
An involution is the case \(G=C_2\); equivalently, it is an isometry \(\sigma:L\to L\) with \(\sigma^2=1\).

## 29. Localizations and genera

### Definition 29.1 (Local profile) {#def-local-profile}

For an integral lattice \(L\), let \(L_v\) denote its scalar extension to the appropriate completion at a place \(v\), including the real place. The local-profile functor is
\[
\operatorname{Loc}:
\mathbf{Lat}_{\mathbb Z}^{\simeq}
\longrightarrow
\prod_v\mathbf{Lat}_{\mathbb Z_v}^{\simeq},
\]
with a restricted product used when the arithmetic setting requires it.

### Definition 29.2 (Genus) {#def-genus}

The genus of \(L\) is the fiber of the map of sets
\[
\pi_0(\operatorname{Loc}):
\pi_0(\mathbf{Lat}_{\mathbb Z}^{\simeq})
\longrightarrow
\pi_0\!\left(\prod_v\mathbf{Lat}_{\mathbb Z_v}^{\simeq}\right)
\]
over the point \([\operatorname{Loc}(L)]\). Thus
\[
\operatorname{genus}(L)
=
\{[M]\mid M_v\simeq L_v\text{ for every }v\}.
\]
It is a pointed set, pointed by \([L]\).

### Proposition 29.3 (Genus is not \(\pi_0\) of the homotopy fiber) {#prop-genus-not-hofib}

In general,
\[
\pi_0\operatorname{hofib}_{\operatorname{Loc}(L)}(\operatorname{Loc})
\not\simeq
\operatorname{genus}(L).
\]
There is instead an exact sequence of pointed sets
\[
\pi_1(B,\operatorname{Loc}(L))
\longrightarrow
\pi_0(\operatorname{hofib})
\longrightarrow
\pi_0(E)
\longrightarrow
\pi_0(B),
\]
where \(E=\mathbf{Lat}_{\mathbb Z}^{\simeq}\) and \(B=\prod_v\mathbf{Lat}_{\mathbb Z_v}^{\simeq}\). The first term acts on the components of the homotopy fiber. The genus is the fiber of the last map, after quotienting the extra automorphism data.

### Remark 29.4

The distinction exemplifies the general rule that truncation level is mathematical content. The groupoid of local identifications, the homotopy fiber, and the set of global isometry classes in the genus are related but not identical.

***
# Part VII. Sites, sheaves, stacks, and geometric categories

The preceding constructions are internal to the higher category of categories.  Algebraic
geometry enters by choosing distinguished sites and then forming categories of sheaves and
stacks on them.  The conversations fixed the categorical placement of these objects more
firmly than any one model of derived geometry.  Accordingly, the definitions below use the
standard Stacks Project and higher-topos-theoretic formulations.  Where the discussions did
not select a unique derived or spectral model, that choice is stated as unresolved rather
than hidden.

## 30. Sites and sheaves

### Definition 30.1 (Sieve) {#def-sieve}

Let \(\mathcal C\) be an ordinary category and \(U\in\mathcal C\).  A **sieve** \(S\) on
\(U\) is a full subcategory of \(\mathcal C_{/U}\) closed under precomposition: whenever
\(V\to U\) belongs to \(S\) and \(W\to V\) is any morphism, the composite \(W\to U\)
belongs to \(S\).

Equivalently, a sieve is a subpresheaf of the representable presheaf \(h_U\).  See the
Stacks Project treatment of sites and sieves.

### Definition 30.2 (Grothendieck topology and site) {#def-site}

A **Grothendieck topology** \(J\) on \(\mathcal C\) assigns to each object \(U\) a collection
\(J(U)\) of covering sieves satisfying maximality, stability under pullback, and transitivity.
A **site** is a pair \((\mathcal C,J)\).

A Grothendieck pretopology may be used to generate \(J\); the invariant object is the
resulting topology, not the chosen list of covering families.

### Definition 30.3 (Presheaves and sheaves of spaces) {#def-sheaf}

Let \((\mathcal C,J)\) be a site.  The \(\infty\)-category of presheaves of spaces is
\[
\operatorname{PSh}(\mathcal C)
:=
\operatorname{Fun}(\mathcal C^{\mathrm{op}},\mathcal S).
\]
A presheaf \(F\) is a **sheaf** if, for every covering sieve \(S\hookrightarrow h_U\), the
canonical map
\[
F(U)
\longrightarrow
\lim_{(V\to U)\in S^{\mathrm{op}}}F(V)
\]
is an equivalence.  Write
\[
\operatorname{Sh}(\mathcal C,J)
\subseteq
\operatorname{PSh}(\mathcal C)
\]
for the full \(\infty\)-subcategory of sheaves.

For set-valued or groupoid-valued sheaves this definition is truncated in the corresponding
way.  Ordinary sheaves and stacks are therefore truncations of one sheaf-of-spaces
construction.

### Theorem 30.4 (Sheafification) {#thm-sheafification}

Under the usual smallness hypotheses, the inclusion
\[
\operatorname{Sh}(\mathcal C,J)
\hookrightarrow
\operatorname{PSh}(\mathcal C)
\]
admits a left exact left adjoint
\[
a_J:\operatorname{PSh}(\mathcal C)\longrightarrow\operatorname{Sh}(\mathcal C,J),
\]
called **sheafification**.

This is standard in topos theory and higher topos theory.  Left exactness is the property
that permits finite-limit constructions to be performed before or after sheafification.

### Definition 30.5 (Yoneda embedding and representability) {#def-yoneda-representable}

The Yoneda embedding is
\[
y:\mathcal C\longrightarrow\operatorname{PSh}(\mathcal C),
\qquad
U\longmapsto h_U:=\operatorname{Map}_{\mathcal C}(-,U).
\]
A presheaf or sheaf \(F\) is **representable** if there exists \(U\in\mathcal C\) and an
equivalence \(F\simeq h_U\).  A representing object is unique up to a contractible space of
choices.

### Definition 30.6 (Subcanonical topology) {#def-subcanonical}

A Grothendieck topology is **subcanonical** if every representable presheaf is a sheaf.  The
Zariski, étale, smooth, fppf, and fpqc topologies on the usual categories of schemes are
subcanonical.

### Remark 30.7 (Big and small sites)

For a scheme or stack \(X\), one distinguishes its small site, whose objects are morphisms
of a selected class into \(X\), from its big site, whose objects range over a larger category
of test schemes over \(X\).  The exact choice is part of the definition whenever
quasi-coherent sheaves, torsors, or representability are discussed.  The fppf site is the
basic default for algebraic stacks in this report.

### Definition 30.8 (Infinity-topos and geometric morphism) {#def-infinity-topos}

An **\(\infty\)-topos** is an accessible left exact localization of a presheaf
\(\infty\)-category \(\operatorname{PSh}(\mathcal C)\). The sheaf category
\(\operatorname{Sh}(\mathcal C,J)\) is the basic example.

A **geometric morphism** \(f:\mathcal X\to\mathcal Y\) is an adjunction
\[
f^*:\mathcal Y\rightleftarrows\mathcal X:f_*
\]
in which \(f^*\) is left exact. Ringed topoi and their morphisms are obtained by adjoining
commutative ring objects and compatible maps of structure sheaves. This is the higher-topos
framework used by the ringed and derived constructions below.

## 31. Fibred categories and stacks

### Definition 31.1 (Cartesian morphism) {#def-cartesian-morphism}

Let \(p:\mathcal X\to\mathcal C\) be a functor of ordinary categories.  A morphism
\(\phi:x'\to x\) over \(f:U'\to U\) is **cartesian** if, for every \(z\in\mathcal X\) over
\(V\), composition with \(\phi\) induces the usual pullback universal bijection between
morphisms \(z\to x'\) over \(g:V\to U'\) and morphisms \(z\to x\) over \(fg\).

The \(\infty\)-categorical definition replaces this bijection by an equivalence of mapping
spaces.

### Definition 31.2 (Fibred category) {#def-fibred-category}

A functor \(p:\mathcal X\to\mathcal C\) is a **category fibred in groupoids** if:

1. every morphism \(f:U'\to U\) and every \(x\in\mathcal X_U\) admit a cartesian lift
   \(f^*x\to x\); and
2. every morphism in \(\mathcal X\) is cartesian.

Equivalently, after a choice of cleavage, it is the Grothendieck construction of a
pseudofunctor
\[
\mathcal C^{\mathrm{op}}
\longrightarrow
\mathbf{Grpd}.
\]
This is the standard Stacks Project convention.

### Definition 31.3 (Descent datum) {#def-descent-datum}

Let \(\{U_i\to U\}\) be a covering family.  A **descent datum** for a fibred category
\(\mathcal X\to\mathcal C\) consists of objects \(x_i\in\mathcal X(U_i)\), isomorphisms
between their pullbacks to \(U_i\times_U U_j\), and the cocycle condition on triple fiber
products.

In the \(\infty\)-categorical setting, descent data form the homotopy limit of the Čech
nerve diagram rather than a set of strictly commuting equations.

### Definition 31.4 (Prestack and stack) {#def-prestack-stack}

A category fibred in groupoids \(\mathcal X\to\mathcal C\) is a **prestack** for \(J\) if
isomorphism presheaves satisfy descent.  It is a **stack** if every descent datum is effective;
equivalently, the pseudofunctor of fibers satisfies descent for objects and morphisms.

In higher language, a stack is simply a sheaf of spaces on \((\mathcal C,J)\).  A
\(1\)-stack is a \(1\)-truncated such sheaf.  This identifies ordinary stacks in groupoids
with the \((2,1)\)-truncation of the general sheaf-of-spaces theory.

### Theorem 31.5 (Stackification) {#thm-stackification}

The inclusion of stacks into prestacks admits a left adjoint, **stackification**, under the
standard size hypotheses.  In the \(\infty\)-categorical formulation this is the restriction
of sheafification to groupoid-valued presheaves.

### Definition 31.6 (The 2-category of stacks) {#def-stack-2-category}

For a site \((\mathcal C,J)\), write
\[
\mathbf{St}(\mathcal C,J)
\]
for the \((2,1)\)-category whose objects are stacks in groupoids, whose \(1\)-morphisms are
cartesian functors, and whose \(2\)-morphisms are natural isomorphisms.  More generally,
\(\operatorname{Sh}(\mathcal C,J)\) is the ambient \(\infty\)-category of stacks of spaces.

### Theorem 31.7 (2-Yoneda) {#thm-2-yoneda}

For a stack \(\mathcal X\) and an object \(U\in\mathcal C\), evaluation at the identity of
\(U\) induces the 2-Yoneda equivalence
\[
\operatorname{Hom}(h_U,\mathcal X)
\simeq
\mathcal X(U).
\]
The higher Yoneda lemma gives the corresponding equivalence of mapping spaces for stacks of
spaces.

## 32. Representable morphisms and geometric properties

### Definition 32.1 (Representable morphism) {#def-representable-morphism}

Let \(f:\mathcal X\to\mathcal Y\) be a morphism of stacks on a site of schemes.  The
morphism \(f\) is **representable by schemes** if, for every scheme \(T\) and every morphism
\(T\to\mathcal Y\), the homotopy pullback
\[
\mathcal X\times_{\mathcal Y}T
\]
is representable by a scheme.  Replacing “scheme” by “algebraic space” gives
representability by algebraic spaces.

### Definition 32.2 (A geometric property of morphisms) {#def-geometric-property}

Let \(P\) be a property of morphisms of schemes stable under base change.  A representable
morphism of stacks \(f:\mathcal X\to\mathcal Y\) has property \(P\) if every base change
\[
\mathcal X\times_{\mathcal Y}T\longrightarrow T
\]
has property \(P\) for every scheme \(T\to\mathcal Y\).

Examples include affine, finite, proper, separated, quasi-compact, smooth, étale, unramified,
flat, and locally of finite presentation, with the hypotheses customary in the Stacks
Project.

### Remark 32.3 (Properties live on arrow categories)

A property of morphisms is naturally represented by a classifier over the arrow category,
not by a property attached independently to source and target.  Its pullback stability is a
statement about reindexing along base-change squares.  Composition stability and locality on
the target are separate theorem-level properties of the classifier.

### Definition 32.4 (Structural morphism) {#def-structural-morphism}

For an object \(X\) over a base \(S\), its **structural morphism** is the chosen map
\[
X\longrightarrow S.
\]
An object is proper, smooth, finite type, or separated over \(S\) when this structural
morphism has the corresponding property.  These are derived uses of morphism properties;
they are not separately primitive object predicates.

### Definition 32.5 (Diagonal and inertia) {#def-diagonal-inertia}

For a stack \(\mathcal X\), its diagonal is
\[
\Delta_{\mathcal X}:\mathcal X
\longrightarrow
\mathcal X\times\mathcal X.
\]
Its inertia stack is the pullback
\[
I_{\mathcal X}
:=
\mathcal X
\times_{\mathcal X\times\mathcal X}
\mathcal X,
\]
where both maps are the diagonal.  Over a point \(x\), the fiber of \(I_{\mathcal X}\to
\mathcal X\) is the automorphism group object of \(x\).

### Definition 32.6 (Compactification and boundary) {#def-compactification}

A **compactification** of a morphism \(X\to S\) is a factorization
\[
X\xrightarrow{j}\overline X\xrightarrow{\overline f}S
\]
with \(j\) an open immersion and \(\overline f\) proper.  The **boundary** is the closed
complement \(\overline X\setminus X\), with whatever scheme, stack, divisor, or logarithmic
structure is part of the selected category.

The words Baily--Borel, toroidal, semitoroidal, or KSBA denote particular compactification
functors only after their additional defining data have been supplied; they are not generic
synonyms for Definition 32.6.

## 33. Schemes, algebraic spaces, and algebraic stacks

### Definition 33.1 (Scheme over a base) {#def-scheme-over-base}

Let \(S\) be a scheme.  The category
\[
\mathbf{Sch}_{/S}
\]
is the slice category of schemes over \(S\).  Its morphisms are commuting triangles over
\(S\).

### Definition 33.2 (Algebraic space) {#def-algebraic-space}

An **algebraic space** over \(S\) is an fppf sheaf \(X\) on \(\mathbf{Sch}_{/S}\) such that:

1. the diagonal \(X\to X\times_S X\) is representable by schemes; and
2. there exists a scheme \(U\) and a surjective étale morphism \(U\to X\).

Equivalent standard variants may replace the fppf site by the étale site and adjust the
representability hypotheses accordingly.

### Definition 33.3 (Algebraic stack) {#def-algebraic-stack}

An **algebraic stack** over \(S\) is a stack in groupoids \(\mathcal X\) for the fppf
topology such that:

1. the diagonal \(\Delta_{\mathcal X}\) is representable by algebraic spaces; and
2. there exists a scheme \(U\) and a smooth surjective morphism \(U\to\mathcal X\).

The morphism \(U\to\mathcal X\) is an **atlas**.

### Definition 33.4 (Deligne--Mumford stack) {#def-dm-stack}

A **Deligne--Mumford stack** is an algebraic stack admitting an étale surjective atlas by a
scheme.  Equivalently, under the customary hypotheses, its diagonal is unramified.

Thus there are structural functors
\[
\mathbf{Sch}_{/S}
\longrightarrow
\mathbf{AlgSp}_{/S}
\longrightarrow
\mathbf{DM}_{/S}
\longrightarrow
\mathbf{AlgSt}_{/S},
\]
understood up to the standard fully faithful embeddings.

### Definition 33.5 (Higher geometric stack) {#def-n-geometric-stack}

Let a geometric context be fixed, consisting of affine objects, an admissible class of
morphisms, and a Grothendieck topology.  An **\(n\)-geometric stack** and an **\(n\)-representable
morphism** are defined recursively: \((-1)\)-geometric objects are affine; an \(n\)-geometric
stack has \((n-1)\)-representable diagonal and admits an atlas by affines through admissible
\((n-1)\)-representable morphisms.

This is the standard derived-algebraic-geometric extension of algebraic stacks.  The
conversations settled the need for this ambient, but did not choose one unique model of
derived affines or one admissible topology.  Those choices are therefore parameters of the
theory, not fixed silently here.

## 34. Group actions, torsors, and quotient stacks

### Definition 34.1 (Group object and action) {#def-group-object-action}

Let \(\mathcal C\) have finite products.  A **group object** \(G\) is an internal group in
\(\mathcal C\).  An action of \(G\) on \(X\) is a morphism
\[
a:G\times X\longrightarrow X
\]
satisfying the unit and associativity diagrams.

Equivalently, an action is a functor
\[
BG\longrightarrow\mathcal C
\]
selecting \(X\), where \(BG\) is the one-object groupoid associated with \(G\), interpreted
internally when necessary.

### Definition 34.2 (Torsor) {#def-geometric-torsor}

Let \(G\) be a sheaf of groups on a site.  A **right \(G\)-torsor** over \(T\) is a sheaf
\(P\to T\) with a right \(G\)-action such that:

1. \(P\to T\) is locally nonempty for the chosen topology; and
2. the map
   \[
   P\times G\longrightarrow P\times_TP,
   \qquad (p,g)\longmapsto(p,pg),
   \]
   is an equivalence.

### Definition 34.3 (Action groupoid and nerve) {#def-action-groupoid}

For a group action \(G\curvearrowright X\), the **action groupoid** is the internal groupoid
\[
G\times X\rightrightarrows X,
\]
with source the projection and target the action.  Its nerve is the simplicial object
\[
X
\leftleftarrows
G\times X
\triplearrows
G^2\times X
\cdots.
\]

### Definition 34.4 (Classifying stack and quotient stack) {#def-quotient-stack}

The **classifying stack** \(BG\) sends a test object \(T\) to the groupoid of \(G\)-torsors
on \(T\).  The **quotient stack**
\[
[X/G]
\]
is the stackification of the action groupoid, equivalently the stack whose objects over
\(T\) are pairs \((P,u)\) consisting of a \(G\)-torsor \(P\to T\) and a \(G\)-equivariant
map \(P\to X\).

The coarse orbit sheaf \(X/G\), when it exists, is not in general equivalent to the quotient
stack; the latter retains stabilizer groups.

## 35. Moduli problems and families

### Definition 35.1 (Moduli problem) {#def-moduli-problem}

A **moduli problem** on a site \((\mathcal C,J)\) is a pseudofunctor
\[
\mathcal M:\mathcal C^{\mathrm{op}}\longrightarrow\mathbf{Grpd}
\]
or, more invariantly, a stack of spaces after imposing descent.  An object of
\(\mathcal M(T)\) is a family over \(T\); pullback along \(T'\to T\) is base change of the
family.

### Definition 35.2 (Fine moduli object) {#def-fine-moduli}

A moduli problem \(\mathcal M\) is **finely represented** by \(M\in\mathcal C\) if
\[
\mathcal M\simeq h_M.
\]
The identity point of \(h_M(M)\) corresponds to a universal family over \(M\).

### Definition 35.3 (Coarse moduli space) {#def-coarse-moduli}

Let \(\mathcal X\) be a stack.  A **coarse moduli space** is a morphism
\[
\pi:\mathcal X\longrightarrow X
\]
to an algebraic space satisfying the standard universal property for maps to algebraic
spaces and inducing the prescribed bijection on geometric isomorphism classes.  The exact
additional hypotheses are those of the relevant coarse-moduli theorem.

A coarse moduli space truncates automorphism information; it is not a replacement for the
stack.

### Definition 35.4 (Relative curves and stable objects) {#def-relative-curves}

A family of curves over \(T\) is a proper flat finitely presented morphism \(C\to T\) of
relative dimension one, with the selected geometric-fiber conditions.  Stable curves,
stable pairs, polarized varieties, and KSBA objects are defined by further classifiers on
the arrow category of such families.  Their moduli categories are stacks when the relevant
descent theorem is established.

The conversations did not settle a complete self-contained definition of the KSBA or MMP
classifiers.  Those terms therefore remain names for standard downstream theories rather
than primitives of the present foundations.

## 36. Ringed geometry and quasi-coherent sheaves

### Definition 36.1 (Ringed site and ringed topos) {#def-ringed-site}

A **ringed site** is a site \((\mathcal C,J)\) together with a sheaf of rings
\(\mathcal O\).  A **ringed \(\infty\)-topos** is an \(\infty\)-topos \(\mathcal X\) together
with a ring object \(\mathcal O_{\mathcal X}\).

### Definition 36.2 (Modules over the structure sheaf) {#def-mod-structure-sheaf}

For a ringed site or ringed stack \((X,\mathcal O_X)\), let
\[
\operatorname{Mod}(\mathcal O_X)
\]
denote the category or stable \(\infty\)-category of sheaves of \(\mathcal O_X\)-modules.
Pullback and pushforward along a morphism of ringed spaces or stacks are the standard
functors, with derived functors used when required.

### Definition 36.3 (Quasi-coherent module) {#def-quasi-coherent}

For a scheme \(X\), an \(\mathcal O_X\)-module \(\mathcal F\) is **quasi-coherent** if it is
locally associated with a module on affine opens.  For an algebraic stack, quasi-coherence is
defined by smooth, fppf, or lisse-étale descent, equivalently by quasi-coherence after
pullback to an atlas with the usual descent datum.

Write
\[
\operatorname{QCoh}(X)
\subseteq
\operatorname{Mod}(\mathcal O_X)
\]
for the corresponding category.  In derived geometry, \(\operatorname{QCoh}(X)\) is a
stable presentable \(\infty\)-category.

### Definition 36.4 (Sheaf of algebras and graded algebra) {#def-sheaf-algebra}

A **quasi-coherent \(\mathcal O_X\)-algebra** is a commutative algebra object in
\(\operatorname{QCoh}(X)\).  A graded quasi-coherent algebra is a graded commutative algebra
object, with the grading category stated explicitly.

### Definition 36.5 (Relative spectrum) {#def-relative-spec}

For a quasi-coherent commutative \(\mathcal O_X\)-algebra \(\mathcal A\), the **relative
spectrum**
\[
\underline{\operatorname{Spec}}_X(\mathcal A)
\longrightarrow X
\]
is the affine morphism representing the functor of \(X\)-schemes
\[
T\longmapsto
\operatorname{Hom}_{\mathcal O_T\text{-alg}}
(f^*\mathcal A,\mathcal O_T).
\]
Equivalently, relative spectrum gives the standard contravariant equivalence
\[
\operatorname{QCohAlg}(X)^{\mathrm{op}}
\simeq
\mathbf{Aff}_{/X},
\]
under the usual hypotheses, with quasi-inverse sending an affine morphism
\(f:Y\to X\) to \(f_*\mathcal O_Y\).

### Definition 36.6 (Relative Proj) {#def-relative-proj}

For an appropriately generated graded quasi-coherent algebra \(\mathcal A\), the **relative
Proj** \(\underline{\operatorname{Proj}}_X(\mathcal A)\to X\) is defined by gluing the
standard affine charts \(D_+(f)\), or by its standard moduli/universal property.  The precise
hypotheses on grading, generation, and base are part of the definition.

The general-base construction depends on the quasi-coherent algebra theory of Definitions
36.3--36.4; it cannot be replaced by unconstrained types or propositions.

### Definition 36.7 (Derived category and perfect complexes) {#def-derived-qcoh}

For a ringed space or stack \(X\), write \(D_{\mathrm{qc}}(X)\) for the derived
\(\infty\)-category of complexes with quasi-coherent cohomology.  A complex is **perfect** if
it is locally equivalent to a bounded complex of finite-rank vector bundles, or equivalently
is dualizable in \(\operatorname{QCoh}(X)\) under the standard hypotheses.

### Definition 36.8 (Coherent sheaf) {#def-coherent-sheaf}

Let \(X\) be a locally Noetherian scheme or algebraic stack in a setting where coherence is
local for the chosen topology. A quasi-coherent sheaf \(\mathcal F\) is **coherent** if it is
locally finitely presented; equivalently in the usual Noetherian setting, it is locally of
finite type and kernels of maps from finite free modules are locally of finite type. Write
\[
\operatorname{Coh}(X)
\subseteq
\operatorname{QCoh}(X)
\]
for the full subcategory of coherent sheaves. Outside the Noetherian setting the precise
finiteness condition must be stated rather than imported from this equivalence.

## 37. Deformation theory

The project discussions require deformation groupoids, tangent spaces, obstruction spaces,
and cotangent complexes to have principled categorical homes.  They did not settle a
special-purpose alternative to the standard derived deformation theory, so the following is
the canonical completion of the recorded requirement.

### Definition 37.1 (Square-zero extension) {#def-square-zero-extension}

Let \(A\) be a commutative ring or derived commutative ring and \(M\) an \(A\)-module.  A
**square-zero extension** of \(A\) by \(M\) is an extension
\[
0\longrightarrow M\longrightarrow A'\longrightarrow A\longrightarrow0
\]
in which \(M^2=0\), with the corresponding derived definition when \(A\) is simplicial or
spectral.

### Definition 37.2 (Deformation groupoid) {#def-deformation-groupoid}

Let \(\mathcal M\) be a moduli stack and let \(x\in\mathcal M(A)\).  For a square-zero
extension \(A'\to A\), the **deformation groupoid** of \(x\) to \(A'\) is the homotopy fiber
\[
\operatorname{Def}_x(A')
:=
\mathcal M(A')
\times^h_{\mathcal M(A)}
\{x\}.
\]
Its objects are lifts of \(x\), its morphisms are isomorphisms of lifts, and its higher
homotopy groups record higher automorphisms when the moduli problem is genuinely derived.

### Definition 37.3 (Cotangent complex) {#def-cotangent-complex}

For a morphism \(f:X\to Y\) in a derived geometric context, the **cotangent complex**
\(L_{X/Y}\in\operatorname{QCoh}(X)\) represents derivations: for
\(M\in\operatorname{QCoh}(X)\), there is a natural equivalence
\[
\operatorname{Map}_{\operatorname{QCoh}(X)}(L_{X/Y},M)
\simeq
\operatorname{Der}_Y(X,M).
\]
This universal property is the definition; any explicit complex is a model of the
representing object.

### Definition 37.4 (Tangent complex, tangent space, and obstruction group) {#def-tangent-obstruction}

At a point \(x:\operatorname{Spec}k\to X\), the **tangent complex** is
\[
T_xX
:=
\operatorname{RHom}_k(x^*L_X,k).
\]
We use cohomological grading. For a square-zero extension by a \(k\)-module \(M\),
automorphisms of a lift are governed by
\(\operatorname{Ext}^{-1}(x^*L_X,M)\), the set of lifts, when nonempty, is a torsor under
\(\operatorname{Ext}^{0}(x^*L_X,M)\), and the primary obstruction lies in
\(\operatorname{Ext}^{1}(x^*L_X,M)\). In particular, the ordinary Zariski tangent space is
\[
H^0(T_xX)=\operatorname{Ext}^{0}(x^*L_X,k).
\]
Higher and negative cohomology record derived deformation and automorphism data according to
the same convention.

### Remark 37.5 (The governing exact triangle)

For composable morphisms \(X\to Y\to Z\), the transitivity triangle
\[
f^*L_{Y/Z}
\longrightarrow
L_{X/Z}
\longrightarrow
L_{X/Y}
\longrightarrow
f^*L_{Y/Z}[1]
\]
is the governing object.  Definitions of relative smoothness, unramifiedness, and
obstruction classes should be stated through this triangle or through the represented
derivation functor, rather than by a disconnected list of Ext groups.

## 38. Stratifications and incidence

### Definition 38.1 (Finite stratification) {#def-stratification}

A **finite stratification** of a space, scheme, or stack \(X\) consists of:

1. a finite poset \(P\);
2. locally closed monomorphisms \(i_p:X_p\hookrightarrow X\) for \(p\in P\);
3. pairwise disjoint images whose union is \(X\); and
4. the frontier condition
   \[
   \overline{X_p}
   \subseteq
   \bigcup_{q\le p}X_q,
   \]
   with the chosen orientation of \(P\) stated explicitly.

A stratified object is the pair \((X,\{X_p\}_{p\in P})\); it is not merely an object with an
unconstrained map to a poset.

### Definition 38.2 (Incidence category and specialization preorder) {#def-incidence-category}

The **incidence category** of a poset \(P\) is the thin category having one morphism
\(p\to q\) exactly when \(p\le q\).  For a topological space, specialization gives a
preorder on points; quotienting by mutual specialization gives its associated poset, called
the **thinification** of the specialization preorder.

### Definition 38.3 (Constructible object) {#def-constructible-object}

Let \(X\) be stratified by \(P\).  An object of a sheaf-theoretic category on \(X\) is
**constructible with respect to the stratification** if its restriction to each stratum has
the specified local constancy and finiteness property.  The exact target category—sets,
spaces, modules, complexes, or spectra—is part of the definition.

## 39. Derived and spectral variants

### Definition 39.1 (Derived affine object) {#def-derived-affine}

Choose a category \(\mathbf{CAlg}^{\mathrm{der}}\) of derived commutative algebras, such as
simplicial commutative rings in an appropriate characteristic regime, connective
\(E_\infty\)-rings, or another specified model.  The category of derived affine schemes is
\[
\mathbf{dAff}
:=
(\mathbf{CAlg}^{\mathrm{der}})^{\mathrm{op}}.
\]

### Definition 39.2 (Derived stack) {#def-derived-stack}

Fix a Grothendieck topology on \(\mathbf{dAff}\).  A **derived stack** is a sheaf of spaces
\[
F:\mathbf{dAff}^{\mathrm{op}}\longrightarrow\mathcal S.
\]
Geometricity is defined recursively as in Definition 33.5.  A **spectral stack** is defined
similarly using connective \(E_\infty\)-rings or the selected spectral affine category.

### Remark 39.3 (Unresolved model choice)

The conversations require derived stacks, spectra, and genuine synthetic
\(\infty\)-categorical constructions to fit without changing the foundations.  They do not
select a unique model of derived commutative algebra, a unique topology, or a unique notion
of geometricity.  Therefore Definitions 39.1--39.2 are parameterized by those standard
choices.  Any later theory must name them before making comparison claims.

***
# Part VIII. The mathematical category associated with Sage

The Sage category framework is treated here as an object of mathematics in its own right.
Its registered classes and parent relations are not identified definitionally with the
normalized categories of Parts I--VII.  They form a separate category equipped with a
comparison functor.  Every claim that a Sage construction realizes a normalized one is an
equivalence theorem.

## 40. The category of registered Sage categories

### Definition 40.1 (The category \(\mathbf{SageCat}\)) {#def-sagecat}

A **Sage category diagram** consists of an ordinary category
\[
\mathbf{SageCat}
\]
together with a functor
\[
\rho:\mathbf{SageCat}
\longrightarrow
\mathbf{Cat}_{1}
\hookrightarrow
\mathfrak{Cat}_{\mathcal U}.
\]

The objects of \(\mathbf{SageCat}\) are registered Sage category objects.  Its morphisms are
the registered structural functors between them, with their stated composites and coherence
relations.  The functor \(\rho\) assigns to each registered object the ordinary mathematical
category it purports to represent and to each registered arrow its corresponding functor.

The definition separates three notions:

1. a **Sage name**, which is an external identifier in the Sage category system;
2. an object of \(\mathbf{SageCat}\), which is a vertex in the registered categorical
   diagram; and
3. its realization \(\rho(C)\), which is an actual category.

A bijection of names is therefore not a mathematical equivalence of categories.

### Definition 40.2 (Sage axiom name and registered classifier) {#def-sage-axiom}

A **Sage axiom name** is a label such as `Finite`, `Commutative`, or `Associative`.  It has no
mathematical meaning by itself.

A **registered Sage classifier** over \(C\in\mathbf{SageCat}\) is a distinguished morphism
\[
i_A:C.A\longrightarrow C
\]
in \(\mathbf{SageCat}\), together with a proposed comparison of
\[
\rho(i_A):\rho(C.A)\longrightarrow\rho(C)
\]
with a mathematically defined classifier in the sense of Definition 5.2.

The label \(A\) indexes the registered morphism; it does not replace the morphism or its
mathematical construction.

### Definition 40.3 (Full diagram generated by registered objects) {#def-full-sage-diagram}

Let \(I\) be a finite collection of registered objects and classifier arrows in
\(\mathbf{SageCat}\).  The **full diagram generated by \(I\)** is the full subcategory
\[
D_I\subseteq\mathbf{SageCat}
\]
on every source, target, and intermediate registered object required by \(I\), retaining
every morphism of \(\mathbf{SageCat}\) between those objects.

The realization of this diagram is
\[
\rho_I:D_I\longrightarrow\mathfrak{Cat}_{\mathcal U}.
\]
Retaining the full diagram is essential.  A limit over only the visibly selected cospan can
fail to impose compatibility with other registered structural functors between the same
constituents.

## 41. Normalized limits and colimits

### Definition 41.1 (Normalized Sage intersection) {#def-normalized-sage-intersection}

For a finite generated diagram \(D_I\), define its **normalized intersection** by
\[
\operatorname{Join}_{\mathfrak{Cat}}(I)
:=
\lim_{D_I}\rho_I.
\]
The notation records the historical Sage operation only in this section; mathematically it
is the limit of the realized full diagram.  It is the terminal cone and hence the universal
category carrying all constituent structures with every displayed compatibility.

When \(D_I\) is the cospan
\[
C.A\longrightarrow C\longleftarrow C.B,
\]
this limit is the categorical intersection
\[
C.A\times_C^h C.B.
\]

### Definition 41.2 (Normalized common quotient) {#def-normalized-sage-colimit}

For the same diagram, define
\[
\operatorname{Meet}_{\mathfrak{Cat}}(I)
:=
\operatorname*{colim}_{D_I}\rho_I.
\]
It is the initial cocone receiving compatible functors from all constituents of the full
diagram.

This is the categorical dual of Definition 41.1.  It should not be described as the class of
objects satisfying an informal disjunction of axioms.  Its meaning is exactly its colimit
universal property, and it depends on the complete chosen diagram.

### Remark 41.3 (Terminological collision)

The words *join* and *meet* are overloaded among:

- Sage's methods;
- order-theoretic joins and meets under two opposite order conventions; and
- the topological or categorical join \(\mathcal C\star\mathcal D\).

Outside this part, the constructions are called **limit**, **colimit**, **categorical
intersection**, or **full-diagram colimit**.  Ordering language such as “largest” or
“smallest” is derivative and is not used as a definition.

### Proposition 41.4 (The cospan case) {#prop-sage-cospan}

Let \(i_A:C.A\to C\) and \(i_B:C.B\to C\) be registered classifiers whose realization is
mathematically correct.  Then the normalized Sage intersection for the full cospan is the
homotopy pullback
\[
\rho(C.A)\times^h_{\rho(C)}\rho(C.B).
\]

If both classifiers are property classifiers, this behaves as the intersection of two
conditions.  If either carries genuine structure, an object of the pullback includes both
chosen structures and their comparison over \(C\).

## 42. Closure and comparison with the Sage operations

### Definition 42.1 (Limit closure) {#def-sagecat-closure}

Let
\[
\overline{\mathbf{SageCat}}
\]
denote the closure of the realized Sage diagram under the selected finite limits of
Definitions 41.1 and 7.2, together with the structural functors generated by their universal
properties.  An object in the closure need not have existed as a named Sage class before the
limit was formed.

No colimit closure is included in this definition.

### Definition 42.2 (Sage join datum) {#def-sage-join-datum}

A **Sage join datum** for \(I\) is a registered object \(J_I\), together with a cone from
\(\rho(J_I)\) to \(\rho_I\) that is claimed to realize the terminal cone of Definition 41.1.
It is **exact** if the induced comparison with
\(\operatorname{Join}_{\mathfrak{Cat}}(I)\) is an equivalence.

The exactness assertion is a theorem.  It is not supplied by the fact that Sage printed a
`JoinCategory`, nor by equality of axiom-name lists.

### Remark 42.3 (Possible failures of a Sage join)

Two independent failures are possible.

1. The registered cone may omit a mathematically necessary structural functor or coherence
   relation, so it is not a cone over the intended full diagram.
2. The cone may be valid but not terminal, because Sage lacks an inclusion or equivalence
   needed to reduce the formal intersection to the true one.

A normalized bridge records these as missing comparison theorems.  It does not declare the
Sage object correct by definition.  The limit itself may also be empty; existence of a
category as a limit does not imply existence of an object carrying all imposed structures.

### Definition 42.4 (Sage meet datum) {#def-sage-meet-datum}

A **Sage meet datum** for \(I\) is a registered object \(M_I\), together with a cocone
\[
\rho_I\Longrightarrow \rho(M_I)
\]
selected from the existing Sage parent diagram.  The universal colimit determines a
comparison
\[
\operatorname{Meet}_{\mathfrak{Cat}}(I)
\longrightarrow
\rho(M_I).
\]
The datum is **exact** if this comparison is an equivalence.

Sage commonly obtains \(M_I\) by searching its existing supercategory graph.  Such a search
constructs a cocone in the registered diagram; it does not by itself prove the initial
universal property.

### Proposition 42.5 (Limit--colimit asymmetry) {#prop-sage-asymmetry}

The mathematical asymmetry in the Sage framework is:

\[
\overline{\mathbf{SageCat}}
\text{ is closed under the selected limits but is not assumed closed under the dual
colimits.}
\]

Consequently, the normalized intersection can be adjoined by its limit construction, whereas
the normalized full-diagram colimit may lie outside the registered or limit-closed diagram.
When this happens, an existing common supercategory is only an approximation to the colimit,
with exactness measured by Definition 42.4.

### Definition 42.6 (Terminal object of the Sage diagram) {#def-sage-objects-terminal}

Assume the registered Sage diagram contains an object \(\mathbf{Objects}\) and that every
object has a unique structural morphism to it, coherently with composition.  Then
\(\mathbf{Objects}\) is terminal in \(\mathbf{SageCat}\) and in its limit closure.

### Corollary 42.7 (Weak contractibility) {#cor-sagecat-contractible}

Under Definition 42.6, the groupoid completion or classifying space of
\(\overline{\mathbf{SageCat}}\) is contractible.

This does not imply
\(\overline{\mathbf{SageCat}}\simeq\mathbf 1\) as a category.  The noninvertible structural
functors, and hence the limit and colimit theory, remain nontrivial after the classifying
space has forgotten their direction.

## 43. Correspondence with normalized mathematics

### Definition 43.1 (Correspondence object) {#def-sage-correspondence}

A **correspondence** from a registered Sage category \(C\) to a normalized category
\(\mathcal N\) is an equivalence
\[
\epsilon_C:\rho(C)\overset{\sim}{\longrightarrow}\mathcal N
\]
together with specified compatibility equivalences for every registered structural functor
used by the correspondence.

For a family of categories, the compatibility data form a pseudonatural comparison of the
corresponding diagrams, not merely a table of object names.

### Definition 43.2 (Exact classifier correspondence) {#def-exact-classifier-correspondence}

A registered classifier \(i_A:C.A\to C\) corresponds exactly to a normalized classifier
\(p_A:\mathcal N.A\to\mathcal N\) if there is an equivalence of arrows in the slice
\[
\begin{array}{ccc}
\rho(C.A)&\xrightarrow{\sim}&\mathcal N.A\\
\downarrow&&\downarrow\\
\rho(C)&\xrightarrow{\sim}&\mathcal N
\end{array}
\]
commuting up to a specified invertible \(2\)-cell.

### Theorem 43.3 (Limits preserve exact correspondences) {#thm-correspondence-limits}

A pseudonatural equivalence between two finite diagrams induces an equivalence between their
homotopy limits.  Hence exact correspondences for the constituents and all structural
functors induce an exact correspondence for their normalized categorical intersection.

**Proof sketch.** Homotopy limits are invariant under equivalence of diagrams.  Apply this
to the pseudonatural comparison and use the universal property of the two limits. \(\square\)

### Remark 43.4 (Observation versus construction)

For a named category already available independently, one may define the normalized target
directly and prove its correspondence with Sage.  For an unnamed combination of structures,
the normalized target may instead be the limit expression itself.  These are two
presentations of the same mathematical task; the choice should minimize duplicate
definitions, not alter the semantics.

***
# Part IX. Mathematical semantics of the computational language

The computational language does not introduce a second ontology. Its judgements are points,
functors, lifts, sections, limits, and evaluations in the single mathematical universe
already defined. This part records only their mathematical denotations.

## 44. Contexts and membership

### Definition 44.1 (Mathematical context) {#def-mathematical-context}

A **context** is a finite higher-categorical diagram of previously chosen objects, morphisms,
higher cells, and classifier lifts.  Extending a context by a declaration
\[
\text{let }x\in\mathcal C
\]
means adjoining a point
\[
x:\mathbf 1\longrightarrow\mathcal C.
\]
If \(\mathcal C\) depends on objects already in the context, the declaration is a section of
the corresponding family over that context.

### Definition 44.2 (Defined object) {#def-defined-object}

A declaration
\[
\text{define }x\in\mathcal C\text{ by }x=t
\]
means that the point \(x:\mathbf 1\to\mathcal C\) is equipped with a specified equivalence to
the point denoted by \(t\).  In a \(0\)-truncated category this is ordinary equality; in a
higher category it is the appropriate equivalence datum.

### Definition 44.3 (Membership in a classifier) {#def-membership-classifier}

Let \(p_A:\mathcal C.A\to\mathcal C\) be a classifier and \(x\in\mathcal C\).  The judgement
\[
x\in\mathcal C.A
\]
means that a point of the homotopy fiber \((\mathcal C.A)_x\) has been supplied.  Thus:

- for a property classifier, it is a proposition;
- for a structure classifier, it includes the chosen structure;
- for a general classifier, it may include higher data.

A mere proof that the fiber is inhabited and a named point of a noncontractible fiber are
not interchangeable.

### Definition 44.4 (Morphisms and higher cells as membership) {#def-morphism-membership}

For \(x,y\in\mathcal C\), a declaration of a morphism is a point
\[
f\in\operatorname{Map}_{\mathcal C}(x,y).
\]
For functors \(F,G:\mathcal C\to\mathcal D\), a natural transformation is a point of the
mapping object
\[
\alpha\in
\operatorname{Map}_{\operatorname{Fun}(\mathcal C,\mathcal D)}(F,G).
\]
Higher modifications are treated recursively in the same way.

### Remark 44.5 (Sets remain explicit)

The judgement \(x\in X\) for a set \(X\) is the special case in which \(X\) is a
\(0\)-truncated object of \(\mathcal S\).  The higher-categorical interpretation does not
replace the ordinary language of sets; it explains its truncation level.

## 45. Functorial recognition and structural routes

### Definition 45.1 (Structural route) {#def-structural-route}

A **structural route** from \(\mathcal C\) to \(\mathcal D\) is a specified composite functor
\[
F:\mathcal C\longrightarrow\mathcal D.
\]
For \(x\in\mathcal C\), its image is the point \(F(x)\in\mathcal D\).

If two distinct routes have the same source and target, they are not identified unless a
specified natural equivalence relates them.  This is essential for rings, whose additive and
multiplicative routes lead to different algebraic structures despite having equivalent
underlying sets.

### Definition 45.2 (Recognition through a functor) {#def-recognition-through-functor}

A judgement that an object \(x\in\mathcal C\) is recognized in \(\mathcal D\) through
\(F:\mathcal C\to\mathcal D\) means the object \(F(x)\).  When the route is omitted, the
judgement is defined only if the context specifies a unique distinguished route up to a
contractible space of choices.

### Example 45.3 (A ring and its group structures)

For \(R\in\mathbf{Ring}\), there are canonical judgements
\[
U_+(R)\in\mathbf{AddAbGrp},
\qquad
U_\times(R)\in\mathbf{MulMon},
\qquad
R^\times\in\mathbf{Grp}.
\]
The unqualified statement “\(R\) is a group” is ambiguous: it could refer to the additive
group, the multiplicative monoid, or the unit group.  Role decoration and the actual functor
resolve the ambiguity.

### Example 45.4 (A ring as a module over itself)

For \(R\in\mathbf{Ring}\), the statement
\[
R\in R\text{-}\mathbf{Mod}
\]
is interpreted through the regular-module section of Definition 13.3.  It is not obtained by
forgetting ring structure to a fixed module category.

## 46. Constructions and invariants

### Definition 46.1 (Construction) {#def-dsl-construction}

A **construction** is a functor or higher functor
\[
T:\mathcal C_1\times\cdots\times\mathcal C_n
\longrightarrow
\mathcal D.
\]
Evaluating the construction on declared objects gives another declared object.  Tensor
products, quotients, kernels, cokernels, relative spectra, orthogonal complements, and
pullbacks are examples, with their natural domains explicitly stated.

### Definition 46.2 (Invariant) {#def-invariant}

Let \(S\) be a set, regarded as a discrete space. A **set-valued invariant** of objects of
\(\mathcal C\) is a functor
\[
I:\mathcal C^{\simeq}\longrightarrow S.
\]
Equivalently, it is a function
\[
\pi_0(\mathcal C^{\simeq})\longrightarrow S.
\]
More generally, a categorified invariant may take values in any specified target category,
but then it is not determined by \(\pi_0\). Cardinality, rank, determinant, signature, and
isometry-class invariants are set-valued invariants on their natural domains.

### Definition 46.3 (Operation with noncanonical output) {#def-noncanonical-output}

Suppose \(p:\mathcal E\to\mathcal C\) is a structure classifier.  An operation that chooses
additional data on \(x\in\mathcal C\) returns a point of the fiber \(\mathcal E_x\).  Examples
are:

- a basis of a free module;
- a finite generating family;
- an ordering or enumeration of a finite set;
- a trivialization of a torsor;
- a monoidal structure on a category.

Such an output is not an invariant unless the fiber is contractible.  Different algorithms
may legitimately return different points of the same fiber.

### Definition 46.4 (Property query) {#def-property-query}

For a property classifier \(p_A:\mathcal C.A\to\mathcal C\), a query whether \(x\) has
property \(A\) asks whether the fiber \((\mathcal C.A)_x\) is inhabited.  A positive answer
is a lift; a negative answer is evidence that the fiber is empty.  Failure to determine
either is not a third mathematical truth value; it is absence of a decision procedure.

### Remark 46.5 (Calculation and proof)

A calculation is the evaluation of a mathematically typed construction or invariant.  The
mathematical value may be accompanied by a proof, a checkable certificate, or only an
experimental provenance record.  These are different epistemic statuses of the same typed
output, not different mathematical codomains.

## 47. Functorial inheritance of constructions

### Proposition 47.1 (Inheritance by composition) {#prop-inheritance-composition}

Let \(F:\mathcal C\to\mathcal D\) be a structural functor and let
\(T:\mathcal D\to\mathcal E\) be a construction.  Then
\[
T\circ F:\mathcal C\longrightarrow\mathcal E
\]
is the induced construction on \(\mathcal C\).

No separate definition of \(T\) on \(\mathcal C\) is required.  All functoriality and
coherence laws are inherited from composition.

### Corollary 47.2 (Underlying invariants)

If \(I:\mathcal D^{\simeq}\to S\) is an invariant, then
\[
I\circ F^{\simeq}:\mathcal C^{\simeq}\to S
\]
is the inherited invariant.  For example, cardinality of a ring or module whose underlying set is finite is the composite
of its structural functor to finite sets with the cardinality invariant.

### Remark 47.3 (Domain of functoriality)

Composition is permitted only when the domain and codomain match. The discriminant functor
is defined on the core of lattices; the Gram-matrix functor is defined on coordinatized
forms; an index is defined on subgroup inclusions; a numbering is defined on enumerated
sets. The domain restriction is part of the construction, not an informal warning.

## 48. Finite and enumerated objects

### Definition 48.1 (Finite set and cardinality) {#def-finite-cardinality}

A set \(X\) is finite if it is equivalent to \(\operatorname{Fin}(n)\) for some natural
number \(n\).  Its cardinality
\[
|X|=n
\]
is the corresponding invariant on the core of finite sets.

### Definition 48.2 (Enumeration) {#def-enumeration}

An **enumeration** of a set \(X\) is explicit chosen data exhibiting \(X\) as finite or
countable.  In the finite case it is an equivalence
\[
e:\operatorname{Fin}(n)\overset{\sim}{\longrightarrow}X.
\]
In a countable setting it may be an equivalence with a subset of \(\mathbb N\), or a pair of
partial inverse maps
\[
\operatorname{number}:X\longrightarrow\mathbb N,
\qquad
\operatorname{nth}:\mathbb N\longrightarrow X\sqcup\{\bot\}
\]
satisfying the specified inverse laws.

Finiteness and countability are properties.  A chosen enumeration is structure.

### Proposition 48.3 (Product enumeration) {#prop-product-enumeration}

Chosen finite enumerations of \(X\) and \(Y\) induce a chosen enumeration of \(X\times Y\)
by mixed radix.  Chosen countable enumerations induce a countable enumeration by any fixed
pairing bijection \(\mathbb N^2\simeq\mathbb N\).

This is the mathematical source of inherited enumeration of finite products, finite free
modules over finite rings, and finite based bilinear spaces.

## 49. Ideals and quotient rings

### Definition 49.1 (Category of ideals) {#def-ideal-category}

For a commutative ring \(R\), let \(\operatorname{Ideal}(R)\) denote the poset category of
ideals ordered by inclusion.  A selected ideal is a point \(I\in\operatorname{Ideal}(R)\).

### Definition 49.2 (Quotient ring) {#def-quotient-ring}

The quotient construction assigns to \((R,I)\) the commutative ring
\[
R/I.
\]
A morphism of pairs \((R,I)\to(S,J)\) is a ring homomorphism carrying \(I\) into \(J\); it
induces the quotient homomorphism \(R/I\to S/J\).  Thus quotient is a functor from the
corresponding category of ring--ideal pairs to commutative rings.

### Example 49.3

Let
\[
R=\mathbb Z,
\qquad
I=(2),
\qquad
Q=R/I.
\]
Then the structural functors and quotient construction give
\[
Q\in\mathbf{CommRing},
\quad
U_+(Q)\in\mathbf{AddAbGrp},
\quad
U(Q)\in\mathbf{FiniteSet},
\]
and hence
\[
|Q|=2.
\]
The class of \(1\) is a generator of the additive group, but a command returning generators
returns chosen structure and is not required to choose this particular representative.

## 50. One mathematical diagram, not a second computational ontology

### Principle 50.1 (Single categorical semantics) {#principle-single-semantics}

Every category used to state the domain of a calculation is an ordinary mathematical
category or higher category constructed by Parts I--VIII. Framed modules, coordinatized
modules, Gram matrices, finite enumerations, presentations, and coordinate systems are
genuine mathematical structures represented by classifiers, comma categories, arrow
categories, and functors.

There is no second mathematical category graph whose objects exist only to host algorithms.
A calculation may require choosing a point of a presentation fiber, but the mathematical
object remains the original object together with the chosen lift and all structural functors
available in the single diagram.

### Example 50.2 (Gram construction)

A symmetric matrix \(G\in\operatorname{SymMat}_n(R)\) determines a point of the category of
coordinatized symmetric forms by the Gram functor of Definition 21.3. Forgetting the
coordinates gives an intrinsic form. Calculations with \(G\) are calculations with the
chosen coordinatized lift of that same form, not with an object in an unrelated universe.

### Example 50.3 (A finite coordinatized bilinear space)

Let \(k=\mathbb F_2\), let \(M=k^2\) with its standard basis, and let \(G\) be a symmetric
\(2\times2\) matrix.  The resulting point belongs simultaneously to:

- the category of coordinatized symmetric bilinear spaces over \(k\);
- the category of finite-dimensional \(k\)-modules;
- the category of finite sets after forgetting structure;
- the category of enumerated finite sets after choosing the product enumeration.

Consequently determinant, radical, isotropic vectors, cardinality, numbering, and partial
inverse enumeration are evaluations of constructions inherited through the same categorical
diagram.

***
# Part X. Presentations of categories and higher categories

The normalized category diagram is itself most naturally specified by generators and
relations.  This is independent of any implementation language.  It is the usual
mathematical distinction between a presentation and a multiplication table.

## 51. Generated categorical diagrams

### Definition 51.1 (Generating higher diagram) {#def-generating-higher-diagram}

Let \(\mathcal K\) be an \((\infty,2)\)-category.  A **generating higher diagram** consists
of:

1. a collection of objects of \(\mathcal K\);
2. specified generating \(1\)-morphisms between them;
3. specified generating \(2\)-morphisms and higher coherence cells; and
4. a declared collection of categorical operations under which the diagram is to be closed,
   such as composition, opposites, comma objects, homotopy pullbacks, categories of elements,
   or operadic algebra constructions.

Its **generated sub-\((\infty,2)\)-category** is the smallest subobject of \(\mathcal K\)
containing the generators and closed under the specified operations, understood up to the
selected equivalence relation on presentations.

### Definition 51.2 (Derived morphism) {#def-derived-morphism}

A morphism is **derived** from a generating diagram if it is obtained by composition,
whiskering, a universal projection, a universal comparison map, or another declared closure
operation.  It is not an additional generator.

For example, a composite
\[
R\text{-}\mathbf{Mod}
\longrightarrow
\mathbf{AddAbGrp}
\longrightarrow
\mathbf{Set}
\]
is derived from the adjacent structural functors.  Recording a second independent direct
arrow would require a comparison \(2\)-cell and would enlarge the presentation.

### Definition 51.3 (Relation and coherence) {#def-presentation-relation}

A **relation** in a categorical presentation is a specified equivalence between two
composites of generators.  In a \(2\)-categorical presentation it is a \(2\)-cell; in an
\((\infty,2)\)-presentation it may carry higher coherences.

The additive and multiplicative routes from rings to sets, the two module routes from a
bimodule, and alternative constructions of the same pullback are related by such cells,
not by erasing one route from the mathematics.

### Definition 51.4 (Inclusion-minimal generating presentation) {#def-minimal-presentation}

Fix:

1. a target higher diagram \(D\);
2. permitted closure operations; and
3. an equivalence relation on presentations.

A generating subdiagram \(G\) is **inclusion-minimal** if its closure contains a diagram
equivalent to \(D\), and no proper subdiagram of \(G\) has that property.

Such a presentation need not be unique.  There is no unqualified “minimal category graph.”

## 52. Free and presented categories

### Definition 52.1 (Free category on a directed graph) {#def-free-category}

For a directed graph \(Q\), the **free category** \(\operatorname{Path}(Q)\) has the vertices
of \(Q\) as objects and finite composable paths as morphisms, with concatenation as
composition and length-zero paths as identities.

### Definition 52.2 (Presented category) {#def-presented-category}

A **presentation of a category** consists of a directed graph \(Q\) and a congruence
\(\sim\) on the morphisms of \(\operatorname{Path}(Q)\), compatible with source, target, and
composition.  The presented category is
\[
\langle Q\mid R\rangle
:=
\operatorname{Path}(Q)/{\sim_R},
\]
where \(\sim_R\) is the least congruence containing the stated relations \(R\).

### Remark 52.3

The quotient in Definition 52.2 is a quotient by an explicitly generated congruence in the
category of small categories.  It is not a generic “quotient category classifier” in
\(\mathfrak{Cat}\).  The data of the congruence and its universal property are part of the
construction.

## 53. Globular presentations of \(2\)-categories

### Definition 53.1 (Globular \(2\)-graph) {#def-globular-2-graph}

A **globular \(2\)-graph** consists of:

- a set \(G_0\) of \(0\)-cells;
- a set \(G_1\) of generating \(1\)-cells with source and target in \(G_0\); and
- a set \(G_2\) of generating \(2\)-cells whose source and target are **parallel** paths in
  the free category on \(G_1\).

Parallelism is mandatory: a globular \(2\)-cell can relate only \(1\)-morphisms with the
same source and target.

### Definition 53.2 (Free strict \(2\)-category and computad) {#def-computad}

The **free strict \(2\)-category** on a globular \(2\)-graph is generated by:

- the paths in the free \(1\)-category;
- identity \(2\)-cells;
- vertical and horizontal composites of the generating \(2\)-cells; and
- whiskerings,

subject only to the strict \(2\)-category axioms and interchange law.  A globular
presentation of this sort is commonly called a **\(2\)-computad**.

A presented strict \(2\)-category is obtained by imposing an explicitly generated
congruence on \(2\)-cells.  Bicategorical or \(\infty\)-categorical presentations replace
strict equations by coherent higher cells.

### Definition 53.3 (Object equivalence in a bicategory) {#def-object-equivalence-bicategory}

Objects \(x,y\) of a bicategory are **equivalent** if there exist \(1\)-morphisms
\[
f:x\to y,
\qquad
g:y\to x
\]
and invertible \(2\)-cells
\[
gf\Rightarrow 1_x,
\qquad
fg\Rightarrow 1_y,
\]
satisfying the triangle coherences, or equivalently an adjoint equivalence.

In a raw \(2\)-graph, existence of paths in both directions is insufficient; the witnessing
\(2\)-cells are essential.

### Remark 53.4 (CW-language versus globular language)

A \(2\)-cell attached to a topological loop and a globular \(2\)-cell between parallel
\(1\)-morphisms are related but not identical data.  A CW-style filling of a closed edge path
must first be translated into a globular presentation, for example by selecting two parallel
paths with the same endpoints.  The translation is part of the mathematical input.

### Proposition 53.5 (Conditional decision by convergent rewriting) {#prop-rewriting-decision}

Suppose a finite presentation of a category or strict \(2\)-category admits a terminating
and confluent rewriting system on its path expressions, compatible with all contexts and
whiskerings.  Then equality of represented \(1\)-morphisms is decidable by comparison of
normal forms, and equality proofs are furnished by rewrite certificates.

The existence of such a rewriting system is not automatic.  The word problem for finitely
presented semigroups and categories is undecidable in general.  A normalization procedure is
therefore a theorem under convergence hypotheses, not a universal feature of finite
presentation.

***
# Part XI. Exact, fiber, and obstruction-theoretic packages

Several central notions in the lattice and geometric theories are not adequately specified
by naming a single morphism and asserting that it is injective, surjective, or an
isomorphism.  The kernels, cokernels, connecting maps, fibers, and obstruction classes are
mathematical objects used downstream.  This part records the general constructions that
organize them.

## 54. Canonical exact sequences of a morphism

### Definition 54.1 (Kernel, cokernel, image, and coimage) {#def-kernel-cokernel-package}

Let \(f:X\to Y\) be a morphism in an abelian category.  Define
\[
\ker(f)\longrightarrow X,
\qquad
Y\longrightarrow\operatorname{coker}(f),
\]
and
\[
\operatorname{coim}(f):=\operatorname{coker}(\ker(f)\to X),
\qquad
\operatorname{im}(f):=\ker(Y\to\operatorname{coker}(f)).
\]
There is a canonical factorization
\[
X\twoheadrightarrow\operatorname{coim}(f)
\overset{\sim}{\longrightarrow}
\operatorname{im}(f)\hookrightarrow Y.
\]

### Definition 54.2 (Defect package of a morphism) {#def-defect-package}

The **defect package** of \(f\) is the exact sequence
\[
0\longrightarrow
\ker(f)
\longrightarrow
X
\longrightarrow
Y
\longrightarrow
\operatorname{coker}(f)
\longrightarrow0,
\]
together with the image/coimage factorization and every comparison map relevant to the
ambient construction.

Properties of \(f\) are then positions in this package:

- monic iff \(\ker(f)=0\);
- epic iff \(\operatorname{coker}(f)=0\);
- an isomorphism iff both vanish.

### Example 54.3 (The radical--discriminant sequence)

For the adjoint of a bilinear form,
\[
\widetilde b:M\to M^*,
\]
Definition 18.2 is the defect package
\[
0\to\operatorname{rad}(M,b)
\to M
\xrightarrow{\widetilde b}M^*
\to\operatorname{def}(M,b)
\to0.
\]
Radical-freeness, perfectness, and the discriminant module are therefore aspects of one
exact sequence rather than unrelated predicates.

## 55. Derived functors and connecting morphisms

### Definition 55.1 (Governing long exact sequence) {#def-governing-les}

Let
\[
0\longrightarrow A\longrightarrow B\longrightarrow C\longrightarrow0
\]
be a short exact sequence in an abelian category, and let \(T\) be a left or right exact
functor with derived functors.  The **governing long exact sequence** is the complete exact
sequence containing the derived terms and connecting morphisms, for example
\[
0\to T(A)\to T(B)\to T(C)
\xrightarrow{\delta}
R^1T(A)\to R^1T(B)\to\cdots.
\]

The connecting morphism \(\delta\) is part of the data that locates obstructions.  A
truncated initial segment is insufficient whenever the obstruction lies later in the
sequence.

### Definition 55.2 (Obstruction object and obstruction class) {#def-obstruction-class}

An **obstruction object** is a named object \(O\) in an exact, fiber, or cofiber sequence
whose vanishing is equivalent to the existence of a desired lift or extension.  An
**obstruction class** is a distinguished point
\[
\operatorname{ob}(x)\in O
\]
whose vanishing is equivalent to solvability for the particular datum \(x\).

The location of \(O\) and the construction of \(\operatorname{ob}(x)\) in the governing
sequence are part of the definition.

### Example 55.3 (Deformations)

For a square-zero extension, the cotangent complex and the transitivity triangle produce
obstruction classes in the appropriate Ext group.  Merely listing a tangent space and an
obstruction space does not specify the boundary map that sends a deformation problem to its
obstruction.

## 56. Fibers, cofibers, and truncation

### Definition 56.1 (Homotopy fiber and cofiber) {#def-homotopy-fiber-cofiber}

For a pointed morphism \(f:X\to Y\) in an \(\infty\)-category with finite limits, its
homotopy fiber is
\[
\operatorname{fib}(f)
:=
X\times_Y *.
\]
In a pointed \(\infty\)-category with finite colimits, the homotopy cofiber is
\[
\operatorname{cofib}(f)
:=
*\sqcup_XY.
\]
In a stable \(\infty\)-category these fit into a fiber/cofiber sequence and determine one
another up to shift.

### Proposition 56.2 (Exact sequence of homotopy groups) {#prop-homotopy-exact-sequence}

A fiber sequence of pointed spaces
\[
F\longrightarrow E\longrightarrow B
\]
induces the long exact sequence of homotopy groups and, in low degrees, the exact sequence of
pointed sets
\[
\pi_1(B)
\longrightarrow
\pi_0(F)
\longrightarrow
\pi_0(E)
\longrightarrow
\pi_0(B).
\]
The first term acts on \(\pi_0(F)\).  Therefore the fiber of
\(\pi_0(E)\to\pi_0(B)\) is generally an orbit set rather than \(\pi_0(F)\) itself.

### Remark 56.3 (Set-level invariants)

When the intended invariant is a set of equivalence classes, the truncation to \(\pi_0\) is
part of the definition.  Replacing the set-level fiber by a homotopy fiber adds automorphism
and path data.  The genus construction of Section 29 is the principal arithmetic example.

## 57. Functorial domains and restrictions

### Definition 57.1 (Domain of functoriality) {#def-domain-functoriality}

Let a rule \(T\) assign an object \(T(x)\) to each object of \(\mathcal C\).  A **domain of
functoriality** for \(T\) is a specified subcategory or classifier total
\(\mathcal C_T\to\mathcal C\) on which the assignment extends to a functor
\[
T:\mathcal C_T\longrightarrow\mathcal D.
\]

The domain may be the core, the category of monomorphisms, the finite-free locus, the based
locus, or another mathematically defined category.  The phrase “\(T\) is natural” is not a
substitute for this domain.

### Example 57.2

- The discriminant form is functorial on the isometry core.
- A Gram matrix is functorial on the coordinatized form category.
- Index is an invariant of subgroup inclusions, not of arbitrary pairs of groups.
- The quotient \(G/H\) is functorial on the category of normal subgroup inclusions if a
  group quotient is required.
- The metric dual is functorial only for the selected class of isometries or compatible
  embeddings.

***
# Part XII. Convex, reflection, period, and degeneration geometry

The attached planning record requires cones, fans, reflection arrangements, period domains,
and moduli compactifications to occur as genuine mathematical categories.  The discussions
settled their categorical placement and their dependence on the lattice theory of Parts
V--VI, but did not settle every model of compactification or degeneration.  The definitions
below give the standard intrinsic objects at their natural generality.  More specialized
comparison theorems are deliberately not incorporated into the definitions.

## 58. Rational cones and fans

### Definition 58.1 (Lattice vector space and dual) {#def-lattice-vector-space}

Let \(N\) be a lattice, meaning a finite-rank free abelian group for the purposes of toric
geometry.  Put
\[
N_{\mathbb Q}:=N\otimes_{\mathbb Z}\mathbb Q,
\qquad
M:=\operatorname{Hom}_{\mathbb Z}(N,\mathbb Z),
\qquad
M_{\mathbb Q}:=M\otimes\mathbb Q.
\]
The natural pairing is
\[
\langle-,-\rangle:M_{\mathbb Q}\times N_{\mathbb Q}\to\mathbb Q.
\]

### Definition 58.2 (Rational polyhedral cone) {#def-rational-cone}

A **rational polyhedral cone** in \(N_{\mathbb Q}\) is a subset
\[
\sigma
=
\mathbb Q_{\ge0}v_1+\cdots+\mathbb Q_{\ge0}v_r
\]
for finitely many \(v_i\in N\).  It is **strongly convex**, **pointed**, or **salient** if
\[
\sigma\cap(-\sigma)=\{0\}.
\]
Its linear span and dimension are taken inside \(N_{\mathbb Q}\).

The cone is the intrinsic convex subset.  A chosen list \((v_1,\ldots,v_r)\) is a generating
presentation and is additional structure.

### Definition 58.3 (Dual cone and face) {#def-dual-cone-face}

The dual cone is
\[
\sigma^\vee
:=
\{u\in M_{\mathbb Q}\mid
\langle u,v\rangle\ge0\text{ for every }v\in\sigma\}.
\]
For \(u\in\sigma^\vee\), the subset
\[
\tau
:=
\sigma\cap u^\perp
\]
is a **face** of \(\sigma\).  Write \(\tau\preceq\sigma\).  Faces, with inclusion, form a
finite poset for a rational polyhedral cone.

### Definition 58.4 (Fan) {#def-fan}

A **rational fan** \(\Sigma\) in \(N_{\mathbb Q}\) is a collection of strongly convex
rational polyhedral cones such that:

1. every face of a cone in \(\Sigma\) belongs to \(\Sigma\); and
2. for \(\sigma,\tau\in\Sigma\), the intersection \(\sigma\cap\tau\) is a face of each.

A fan is finite, complete, simplicial, regular, or projective according to the standard
conditions.  A morphism of fans is a homomorphism of lattices carrying every cone of the
source into a cone of the target.

### Definition 58.5 (Semifan) {#def-semifan}

The discussions use **semifan** for a collection of rational polyhedral cones intended to
control only part of a compactification and not necessarily satisfying every axiom of a fan.
No single standard definition was fixed.  Consequently, “semifan” is not a primitive in this
report.  Any later use must state explicitly which face, intersection, local finiteness, and
group-invariance axioms are imposed.

## 59. Toric constructions

### Definition 59.1 (Affine toric monoid and affine toric scheme) {#def-affine-toric}

For a rational polyhedral cone \(\sigma\subseteq N_{\mathbb Q}\), define the commutative
monoid
\[
S_\sigma
:=
\sigma^\vee\cap M.
\]
For a commutative base ring \(k\), the associated affine toric scheme is
\[
U_\sigma
:=
\operatorname{Spec}k[S_\sigma].
\]

A face inclusion \(\tau\preceq\sigma\) induces an open immersion
\[
U_\tau\hookrightarrow U_\sigma.
\]

### Definition 59.2 (Toric scheme of a fan) {#def-toric-scheme}

For a fan \(\Sigma\), the **toric scheme** \(X_\Sigma\) is the colimit obtained by gluing the
\(U_\sigma\) along the open subschemes \(U_{\sigma\cap\tau}\):
\[
X_\Sigma
:=
\operatorname*{colim}_{\sigma\in\Sigma}U_\sigma
\]
in the category of schemes, with the diagram oriented by face inclusions.

A morphism of fans induces a toric morphism.  Thus the toric construction is a functor after
the direction conventions are fixed.

### Remark 59.3 (Intrinsic versus presented cones)

Algorithms may receive generators, inequalities, or a face lattice.  These are different
presentations of the same cone only after comparison theorems such as Minkowski--Weyl.  The
category of cones is defined intrinsically; generated and inequality presentations are
structured categories over it.

## 60. Roots, reflections, and Coxeter data

### Definition 60.1 (Integral reflection vector) {#def-integral-reflection-vector}

Let \((L,b)\) be a nondegenerate integral lattice and let \(r\in L\) with \(b(r,r)\ne0\).
The rational reflection in \(r\) is
\[
s_r(x)
:=
x-\frac{2b(x,r)}{b(r,r)}r.
\]
The vector \(r\) is an **integral reflection vector** if
\[
\frac{2b(x,r)}{b(r,r)}\in\mathbb Z
\qquad
\text{for all }x\in L,
\]
so that \(s_r\in O(L)\).

When a root convention imposes a prescribed norm, such as \(b(r,r)=-2\), that norm is part
of the selected root classifier rather than the general definition of an integral reflection
vector.

### Definition 60.2 (Root system in a lattice) {#def-lattice-root-system}

A **root system** in \(L\) is a subset \(\Phi\subseteq L\setminus\{0\}\) satisfying the
selected finiteness, spanning, integrality, and reflection-stability axioms.  In a
negative-definite ADE lattice, the roots of norm \(-2\) recover the usual simply-laced root
system under the sign convention of Section 23.

### Definition 60.3 (Reflection group and arrangement) {#def-reflection-group}

For a chosen root set \(\Phi\), the **reflection group** is
\[
W(\Phi)
:=
\langle s_r\mid r\in\Phi\rangle
\subseteq O(L).
\]
The associated hyperplane arrangement in \(L_{\mathbb R}\) is
\[
\mathcal H_\Phi
:=
\bigcup_{r\in\Phi}r^\perp.
\]
A **chamber** is a connected component of the complement of this arrangement in a selected
positive or negative cone.

### Definition 60.4 (Coxeter system and Coxeter diagram) {#def-coxeter-system}

A **Coxeter system** \((W,S)\) is a group with presentation
\[
W
=
\left\langle S\mid (st)^{m_{st}}=1\right\rangle,
\]
where \(m_{ss}=1\) and \(m_{st}\in\{2,3,\ldots,\infty\}\) for \(s\ne t\).  The Coxeter
diagram records the matrix \((m_{st})\) in the standard way.

For a chamber bounded by reflecting hyperplanes, the simple wall reflections form a Coxeter
system when the usual angle and discreteness hypotheses hold.  Establishing that a computed
set of walls is complete or that an algorithm terminates is theorem-level and is not part of
the definition.

### Definition 60.5 (Lorentzian reflection datum) {#def-lorentzian-reflection-datum}

A **Lorentzian reflection datum** consists of:

1. a lattice \(L\) of signature \((1,n)\) or \((n,1)\), with the sign convention stated;
2. a chosen component \(\mathcal C^+\) of its positive or negative cone;
3. a chosen control vector or initial chamber datum; and
4. a specified set of admissible reflection norms.

This is the natural domain for a particular form of Vinberg's algorithm.  Different variants
use different data and should therefore be represented by different classifier totals or
functors, not by one undefined operation on all lattices.

## 61. Hodge structures and Type-IV domains

### Definition 61.1 (Pure Hodge structure) {#def-hodge-structure}

A **pure integral Hodge structure of weight \(n\)** is a finitely generated abelian group
\(H_{\mathbb Z}\), usually torsion-free, together with a decomposition
\[
H_{\mathbb C}
=
\bigoplus_{p+q=n}H^{p,q}
\]
satisfying
\[
\overline{H^{p,q}}=H^{q,p}.
\]
Equivalently, it is a decreasing Hodge filtration \(F^\bullet H_{\mathbb C}\) satisfying the
usual opposedness condition.

Morphisms preserve the integral structure and the Hodge decomposition, or equivalently the
filtration.

### Definition 61.2 (Polarized Hodge structure) {#def-polarized-hodge-structure}

A **polarization** is a nondegenerate bilinear form \(Q\) of parity \((-1)^n\) satisfying
the Hodge orthogonality and Hodge--Riemann positivity conditions.  A polarized Hodge
structure is a Hodge structure together with such a chosen \(Q\).

### Definition 61.3 (Type-IV period domain) {#def-type-iv-domain}

Let \(T\) be an integral lattice of signature \((2,n)\).  Its Type-IV domain is
\[
\Omega_T
:=
\left\{
[\omega]\in\mathbb P(T_{\mathbb C})
\ \middle|\
(\omega,\omega)=0,
\quad
(\omega,\overline\omega)>0
\right\}.
\]
It has two connected components.  Choosing one component is additional data.

Equivalently, \(\Omega_T\) is the space of oriented positive-definite real \(2\)-planes in
\(T_{\mathbb R}\).

### Definition 61.4 (Arithmetic quotient) {#def-arithmetic-period-quotient}

Let \(\Gamma\subseteq O^+(T)\) be an arithmetic subgroup preserving the chosen component.
The natural quotient object is the quotient stack
\[
[\Omega_T/\Gamma].
\]
Its coarse analytic quotient \(\Gamma\backslash\Omega_T\), when formed, forgets stabilizer
data and is generally an orbifold rather than a manifold.

### Definition 61.5 (Period map) {#def-period-map}

Let \(\mathcal M\) be a moduli stack of varieties or marked varieties whose cohomology carries
a polarized Hodge structure with lattice \(T\).  A **period map** is a morphism of stacks or
analytic stacks
\[
\mathcal P:\mathcal M
\longrightarrow
[\Omega_T/\Gamma]
\]
induced functorially by the Hodge filtration.  In a marked moduli problem the target may be
\(\Omega_T\) itself.

Torelli, surjectivity, extension to a compactification, and compatibility with boundary
strata are theorems about \(\mathcal P\), not fields in its definition.

### Definition 61.6 (Heegner divisor) {#def-heegner-divisor}

For a \(\Gamma\)-orbit of negative-norm vectors \(v\in T^\vee\) satisfying the chosen
integrality condition, the associated **Heegner divisor** is the image in
\([\Omega_T/\Gamma]\) of
\[
\bigcup_{\gamma\in\Gamma}
\left(\Omega_T\cap\mathbb P((\gamma v)^\perp_{\mathbb C})\right).
\]
The norm, divisibility, and orbit are part of the label of the divisor.

## 62. Compactifications and degenerations

### Definition 62.1 (Baily--Borel compactification) {#def-baily-borel}

For an arithmetic quotient of a Hermitian symmetric domain, the **Baily--Borel
compactification** is the canonical projective compactification obtained as the Proj of the
graded ring of automorphic forms, under the standard finite-generation theorem.

Its boundary strata are indexed by rational boundary components.  For Type-IV domains these
are determined by rational isotropic subspaces of the lattice.

### Definition 62.2 (Toroidal compactification datum) {#def-toroidal-data}

A toroidal compactification requires, at every rational boundary component, an admissible
\(\Gamma\)-invariant rational polyhedral cone decomposition compatible under incidence.  The
compactification is obtained by replacing neighborhoods of the Baily--Borel boundary by the
corresponding torus embeddings.

The cone decomposition is chosen data.  Independence, comparison, refinement, and
projectivity are theorem-level properties.

### Definition 62.3 (Log pair and KSBA-stable pair) {#def-ksba-pair}

A **log pair** \((X,\Delta)\) consists of a normal variety or suitable demi-normal variety
\(X\) and an effective \(\mathbb Q\)-divisor \(\Delta\) such that \(K_X+\Delta\) is
\(\mathbb Q\)-Cartier.

A **KSBA-stable pair** is, in the standard form, a projective semi-log-canonical pair
\((X,\Delta)\) for which \(K_X+\Delta\) is ample.  A family of stable pairs is required to
satisfy the standard flatness, \(\mathbb Q\)-Gorenstein, and base-change conditions.

The precise coefficient set, dimension, polarization, and allowed singularities are
parameters of the moduli category.

### Definition 62.4 (dlt pair and dlt model) {#def-dlt-model}

A **divisorial log terminal pair** is a log pair satisfying the standard discrepancy and
simple-normal-crossing conditions of the minimal model program.  A **dlt model** of a pair is
a proper birational dlt pair mapping to it, usually with a crepant relation for the log
canonical divisor.

Existence and uniqueness properties of dlt modifications are theorems of birational
geometry, not part of the definition.

### Definition 62.5 (Kulikov degeneration) {#def-kulikov-degeneration}

A **Kulikov degeneration** of K3 surfaces over a disc is a semistable degeneration
\[
\pi:\mathcal X\longrightarrow\Delta
\]
whose general fiber is a smooth K3 surface and whose total space has trivial relative
canonical bundle, subject to the conventional regularity hypotheses.  Its Type I, II, or III
classification is determined by the nilpotency index of monodromy, equivalently by the
standard combinatorial type of the central fiber.

The existence of a Kulikov model after base change and modification is a theorem.  The
category of such degenerations is defined by the displayed geometric data and morphisms over
the disc.

### Definition 62.6 (Integral-affine dual complex) {#def-integral-affine-dual-complex}

For a suitable normal-crossings or dlt degeneration, the **dual complex** is the cell complex
whose vertices, edges, and higher cells record intersections of irreducible boundary
components.  An **integral-affine structure with singularities** on it is an atlas away from
a singular locus with transition maps in
\[
\operatorname{GL}(n,\mathbb Z)\ltimes\mathbb R^n.
\]
The affine structure is additional geometric data derived from the degeneration under the
relevant hypotheses; it is not determined by the abstract incidence complex alone.

### Remark 62.7 (Semitoroidal compactifications)

The discussions require compactifications intermediate between Baily--Borel and toroidal
ones, governed by partial cone data or semifans.  No single general definition was settled.
A future definition must specify the admissible cone collections, local models, group action,
and universal comparison maps.  Until then, “semitoroidal compactification” is a named
research target rather than a primitive of this foundation.

***
# Part XIII. Status of the theory and reference map

## 63. Source status of the parts

### Remark 63.1 (Conversation-derived theory)

The following parts directly record explicit late-stage rulings in the attached discussions:

- the \((\infty,2)\)-categorical ambient and the use of ordinary categories as truncations;
- classifiers, lifts, property/structure/stuff by fiber truncation, and reindexing by homotopy
  pullback;
- operation classifiers as arrow-category pullbacks;
- diagram-extension classifiers and operadic matching towers;
- the algebraic role-decorated spine;
- \(W\)-valued bilinear and quadratic categories;
- the independent symmetry conditions and their implication theorems;
- exact divisibility for evenness;
- intrinsic lattices, framed/coordinatized enhancements, negative-definite ADE conventions,
  discriminant forms, cores, automorphism groups, gluing, and set-level genera;
- \(\mathbf{SageCat}\), full diagrams, limit/colimit normalization, and the asymmetry between
  limit closure and absent colimit closure;
- category-directed mathematical computation in one categorical universe.

### Remark 63.2 (Standard completions)

The conversations also required principled categories of schemes, stacks, derived stacks,
quasi-coherent sheaves, deformation objects, cones, fans, reflection data, period domains,
and compactifications, but did not always select one detailed model.  Parts VII and XII
complete those requirements with their standard definitions from the Stacks Project, higher
topos theory, toric geometry, Hodge theory, and birational geometry.  Every place where a
model remains genuinely unselected is marked as a parameter or unresolved choice.

### Remark 63.3 (Superseded derivations)

The derivation record contains statements that were later rejected, including several
1-categorical operation classifiers, synthetic axiom lattices, mutually exclusive
property/structure labels, a positive-definite \(E_8\) convention, a homotopy-fiber
definition of genus, a Cartan-matrix definition of the ADE lattices, a matrix
definition of morphisms of presented modules, an involution-induced side-changing functor
for modules, bimodule morphisms described as bilinear maps, and an extension-side
naturality claim for the bimodule forgetful functors.  They are not alternative
conventions of this report.  The lattice and matrix statements are corrected by Parts XIV
and XV; the module and bimodule statements by Parts XVIII--XXIII.

## 64. Settled mathematical conventions

### Convention 64.1 (Ambient level)

The semantic universe is an \((\infty,2)\)-category of \(\infty\)-categories.  An ordinary
\(2\)-category of ordinary categories may be used as a truncated model, but not as the
permanent semantic ceiling.

### Convention 64.2 (Equivalence rather than equality)

Categories and universal constructions are compared up to equivalence.  Equalities of
categories are used only inside a chosen strict presentation after a comparison theorem.
Natural equivalences and higher coherence cells are named when parallel routes are used.

### Convention 64.3 (Classifier primitive)

An axiom or additional datum is represented by a mathematically constructed classifier
\(\mathcal C.A\to\mathcal C\).  Labels, predicates, and lists of axioms are not substitutes
for the classifying morphism.

### Convention 64.4 (Truncation hierarchy)

Property, structure, and stuff are cumulative classes read from the classifying fibers.  A
property is a special case of structure.  Chosen data are named whenever the fiber is not
contractible.

### Convention 64.5 (Conjunction)

Simultaneous structure is the homotopy pullback of classifiers.  The terminal universal
property is part of the definition of the named intersection category.

### Convention 64.6 (Operations and equations)

Operations are classified by arrow-category pullbacks.  Equations and coherences are
classified by extension of operation-built boundary diagrams.  Operadically interacting
coherences use matching objects and homotopy limits.

### Convention 64.7 (Forms)

A form is the \(W\)-valued bilinear or quadratic datum itself.  The adjoint to a dual module,
radical, defect module, and discriminant are derived objects in named exact sequences.

### Convention 64.8 (Lattices)

An intrinsic arithmetic lattice is a finite projective module over a Dedekind domain with a
symmetric generically nondegenerate form.  Freeness, bases, generators, Gram matrices, and
enumerations are additional mathematical structures or constructors.

### Convention 64.9 (Signs)

All ADE lattices are negative definite.  In particular,
\[
\Lambda_{K3}=U^{\perp 3}\perp E_8^{\perp 2}
\]
with \(E_8\) already negative definite.

### Convention 64.10 (Quadratic discriminant values)

Integral quadratic refinements take values in \(\mathbb Z\) and polarize to the integral
bilinear form.  Finite discriminant quadratic forms take values in \(\mathbb Q/2\mathbb Z\)
and bilinearize to twice the \(\mathbb Q/\mathbb Z\)-valued discriminant pairing.

### Convention 64.11 (Functorial domains)

Discriminants are functorial on isometry cores; index on subgroup inclusions; enumeration
on enumerated objects.  These domains are part of the definitions.

Gram matrices are evaluations on chosen frames.  Matrices of morphisms are evaluations on
chosen free coordinates.  For quotient or presented objects, a matrix represents a lift on
free modules and descends only under the kernel or chain conditions of the presentation
(Sections 74 and 78).  The intrinsic morphism is the descended map or homotopy class, not
the matrix.

### Convention 64.12 (Homological presentation)

A vanishing property governed by a kernel, cokernel, fiber, cofiber, or Ext class is presented
through the complete exact or fiber sequence containing the named obstruction object and
connecting map.

### Convention 64.13 (Sage normalization)

A Sage category is mapped to a genuine category, a registered axiom name to a genuine
classifier arrow, a Sage `JoinCategory` claim to a finite-limit comparison theorem, and a
Sage meet claim to a full-diagram colimit comparison theorem.  No label computation is
accepted as a mathematical proof.

### Convention 64.14 (Property versus chosen presentation)

Finite generation, finite presentation, \(FP_n\), and perfectness are properties.  A
generating frame, finite presentation, projective resolution, basis, root basis, or ambient
embedding is chosen structure.  Each property is obtained by truncating the corresponding
category of choices.

### Convention 64.15 (Presentation descent)

A morphism between presented objects is defined abstractly.  Free-level matrices are
representatives.  Descent conditions, quotient relations, and chain homotopies are
theorem-level structures that compare representatives with intrinsic hom-spaces.

### Convention 64.16 (Derived semantic ceiling)

For homological constructions, the intrinsic semantic object is the appropriate stable or
derived \(\infty\)-category.  Chain complexes and resolutions are standard presentations and
computational models.  Their use never changes the intrinsic object being studied.

## 65. Choices that remain parameters

### Remark 65.1 (Model of \(\mathfrak{Cat}\))

No single model of the ambient \((\infty,2)\)-category has been fixed.  A formal development
must choose one or provide a sufficiently model-independent interface.

### Remark 65.2 (Morphisms of structured categories)

For categories of monoidal, braided, symmetric monoidal, enriched, triangulated, or derived
categories, the class of \(1\)-morphisms—strict, strong, lax, oplax, exact, or otherwise—is
part of the definition.  This report uses strong monoidal functors in the grounding example
but does not impose that convention globally.

### Remark 65.3 (Operad models)

A cofibrant model of each operad \(A_\infty\), \(E_n\), or \(E_\infty\) must be named when a
cellular matching presentation is used.  Equivalent models give equivalent algebra
categories, not identical presentations.

### Remark 65.4 (Families over changing rings)

The total module and algebra families depend on whether restriction or extension of scalars
is used and on the class of ring morphisms.  No variance-free total family is assumed.

### Remark 65.5 (Derived geometry)

The category of derived affines, its topology, admissible morphisms, and geometricity level
are parameters.  Simplicial commutative rings and connective \(E_\infty\)-rings provide
standard but not definitionally identical models.

### Remark 65.6 (Special compactifications)

Semifans, semitoroidal compactifications, specific KSBA categories, Kulikov boundary
comparisons, and period-map extension theorems require additional definitions and hypotheses.
They are not completed by the generic compactification definitions alone.

### Remark 65.7 (Arithmetic specialization)

Over a general Dedekind domain, a finitely generated torsion module need not have a finite
underlying set.  Statements using cardinality, finite automorphism groups, or enumeration
must include the corresponding finiteness hypotheses on residue rings or specialize to
\(\mathbb Z\) and number-ring settings where the assertion is valid.

## 66. Reference map

The following references are intended as general anchors for terminology and constructions.
They are not an exhaustive bibliography.

### Higher category theory and homotopy theory

- Jacob Lurie, *Higher Topos Theory*.
- Jacob Lurie, *Higher Algebra*.
- Kerodon, especially the sections on \(\infty\)-categories, fibrations, limits, and
  operadic algebra.
- Emily Riehl and Dominic Verity, *Elements of \(\infty\)-Category Theory* and
  *Infinity Category Theory from Scratch*.
- J. Peter May, *A Concise Course in Algebraic Topology*.

### Ordinary and enriched category theory

- Saunders Mac Lane, *Categories for the Working Mathematician*.
- Emily Riehl, *Category Theory in Context*.
- G. M. Kelly, *Basic Concepts of Enriched Category Theory*.
- Ross Street and Stephen Lack on \(2\)-categories, weighted limits, computads, and
  categorical coherence.

### Classifiers, truncation, and structured objects

- John Baez and Michael Shulman, *Lectures on \(n\)-Categories and Cohomology*, for
  stuff/structure/property.
- nLab entries on stuff, structure, property; core; automorphism group; torsor; category of
  elements; Grothendieck construction; and pseudopullback.

### Sheaves, stacks, and algebraic geometry

- The Stacks Project, especially the chapters on sites, fibred categories, stacks, algebraic
  spaces, algebraic stacks, quasi-coherent modules, and deformation theory.
- SGA 1 and SGA 4; Jean Giraud, *Cohomologie non abélienne*.
- Martin Olsson, Laumon--Moret-Bailly, and standard texts on algebraic stacks.
- Bertrand Toën and Gabriele Vezzosi; Jacob Lurie, for derived algebraic geometry.

### Algebra and homological algebra

- Charles Weibel, *An Introduction to Homological Algebra*.
- Cartan--Eilenberg and standard references on derived functors and obstruction sequences.
- Eilenberg--Mac Lane, Lawvere, and standard references on algebraic theories and operads.

### Operads and coherence

- James Stasheff on associahedra and \(A_\infty\)-spaces.
- Boardman--Vogt and J. Peter May on operads.
- Mac Lane and Joyal--Street on monoidal and braided coherence.

### Lattices and quadratic forms

- Jean-Pierre Serre, *A Course in Arithmetic*.
- John Milnor and Dale Husemoller, *Symmetric Bilinear Forms*.
- O. T. O'Meara, *Introduction to Quadratic Forms*.
- Conway and Sloane, *Sphere Packings, Lattices and Groups*.
- V. V. Nikulin on integral symmetric bilinear forms and discriminant forms.

### Convex, toric, reflection, and period geometry

- Fulton, *Introduction to Toric Varieties*; Cox--Little--Schenck, *Toric Varieties*.
- Bourbaki and Humphreys on root systems and Coxeter groups.
- Vinberg on hyperbolic reflection groups.
- Griffiths on period domains; Baily--Borel on arithmetic quotients.
- Ash--Mumford--Rapoport--Tai and standard texts on toroidal compactifications.
- Kollár--Mori and Kollár on singularities, the minimal model program, and stable pairs.

### Root realizations, presentations, and descent

- Bourbaki, *Groupes et algèbres de Lie*, Chapters IV--VI, and Humphreys, *Reflection Groups
  and Coxeter Groups*, for root systems, simple roots, root lattices, Cartan matrices, and the
  finite ADE classification; the root-pairing literature summarized in Mathlib's
  `LinearAlgebra.RootSystem` development.
- Conway--Sloane, *Sphere Packings, Lattices and Groups*, for the coordinate realizations of
  \(A_n,D_n,E_6,E_7,E_8\); standard tables in Bourbaki.
- Stacks Project, Section 10.5, “Finite modules and finitely presented modules,” for finite
  generation and finite presentation.
- Weibel, *An Introduction to Homological Algebra*, and the Stacks Project chapters on
  projective resolutions and derived categories, for complexes, homotopy categories, and the
  comparison theorem.
- Lurie, *Higher Algebra*, and Kerodon, for stable \(\infty\)-categories, module categories,
  perfect objects, and operadic algebras.

### Modules, bimodules, and Morita theory

- Kerodon, Chapter 5, for straightening, unstraightening, and the module cocartesian
  fibration.
- Lurie, *Higher Algebra*, for module \(\infty\)-categories and relative tensor products.
- Haugseng, *The Higher Morita Category of \(E_n\)-Algebras*, for the Morita
  \((\infty,2)\)-category.
- The Stacks Project sections on bimodules, tensor products, and derived tensor products.

***

# Part XIV. Intrinsic lattices, root realizations, and numerical matrices

This part and the three that follow develop the corrected theory of root realizations,
presentations, and matrix descent. They replace the superseded Cartan-matrix construction of
the ADE lattices and supply the descent theory referred to by Definitions 13.5--13.7,
Definitions 21.2--21.3, Definition 23.2, and Convention 64.11. Two principles govern the
material. First, intrinsic objects precede presentations: a named ADE lattice is first an
intrinsic lattice obtained from a root realization, and an embedding, a simple-root basis, its
coordinate matrix, its Gram matrix, and its Cartan matrix are successive additional or derived
data. Second, matrices live on free objects and descend: for modules given by generators or
presentations, matrices represent lifts on free modules, induce abstract module maps only
after satisfying a descent condition, and different matrices may represent the same abstract
morphism.

## 67. Ambient quadratic modules

### Definition 67.1 (Standard odd unimodular lattice) {#def-odd-unimodular-lattice}

For integers \(p,q\ge 0\), let
\[
I_{p,q}:=\mathbb Z^{p+q}
\]
with symmetric bilinear form
\[
(x,y)_{p,q}
=
\sum_{i=1}^{p}x_i y_i-
\sum_{i=p+1}^{p+q}x_i y_i.
\]
Thus \(I_{p,q}\) is the standard **odd** unimodular lattice of signature \((p,q)\). Write
\[
I_N^+:=I_{N,0},
\qquad
I_N^-:=I_{0,N}.
\]

### Definition 67.2 (Ambient quadratic realization) {#def-ambient-quadratic-realization}

Let \((L,b_L)\) be an integral lattice. An **ambient quadratic realization** of \(L\) is an isometric embedding
\[
i:(L,b_L)\hookrightarrow (J,b_J)
\]
into another integral lattice, or more generally an isometric embedding
\[
i:L\hookrightarrow V
\]
into a rational quadratic space \((V,b_V)\), such that \(b_V\) is integral on \(i(L)\).

The ambient object \(J\) or \(V\), the embedding \(i\), and any coordinates on the ambient object are additional data. They are not part of the definition of an intrinsic lattice.

### Remark 67.3 (No uniform rank-preserving embedding into \(I_{p,q}\))

There is no uniform convention under which every ADE lattice of rank \(r\) is defined by an isometric embedding into \(I_{r,0}\) or \(I_{0,r}\).

- The standard coordinate realization of \(A_n\) has rank \(n\) but lies naturally in \(I_{n+1}^+\), as the sum-zero sublattice.
- The standard realization of \(D_n\) lies in \(I_n^+\).
- The \(E_8\) lattice is the even unimodular lattice \(II_{8,0}\), not the odd lattice \(I_{8,0}\). In its standard Euclidean coordinate realization it contains half-integral vectors.

In particular, an isometric full-rank embedding \(E_8\hookrightarrow I_{8,0}\) cannot exist. Indeed, its image would have finite index \(d\), so
\[
\det(E_8)=d^2\det(I_{8,0}).
\]
Both determinants are \(1\), hence \(d=1\), which would identify the even lattice \(E_8\) with the odd lattice \(I_{8,0}\), a contradiction.

Consequently the correct uniform datum is an embedding into a **specified ambient quadratic module**, not necessarily a standard odd unimodular lattice of the same rank.

## 68. Roots and root lattices

### Definition 68.1 (Root of an integral lattice) {#def-root-of-integral-lattice}

Let \((L,b)\) be a nondegenerate integral lattice. A **root of norm \(-2\)** is an element \(r\in L\) satisfying
\[
b(r,r)=-2
\]
for which the reflection
\[
s_r(x):=x-\frac{2b(x,r)}{b(r,r)}r=x+b(x,r)r
\]
preserves \(L\).

For an integral lattice, the final condition is automatic for a vector of norm \(-2\), since \(b(x,r)\in\mathbb Z\).

### Definition 68.2 (Root system in a quadratic space) {#def-root-system-quadratic-space}

Let \(V\) be a finite-dimensional rational or real quadratic space. A finite subset
\[
\Phi\subset V\setminus\{0\}
\]
is a reduced crystallographic **root system** if it spans \(V\), is stable under the reflections \(s_\alpha\), contains no scalar multiples of a root other than \(\pm\alpha\), and satisfies the usual integrality condition
\[
\frac{2(\beta,\alpha)}{(\alpha,\alpha)}\in\mathbb Z
\qquad
(\alpha,\beta\in\Phi).
\]

Compare Definition 60.2, which axiomatizes root systems inside an integral lattice; the present definition works in the ambient quadratic space.

A **simple system** or **base** is a subset \(\Delta\subseteq\Phi\) which is a basis of \(V\) and with respect to which every root is an integral linear combination whose coefficients have one sign.

### Definition 68.3 (Root lattice) {#def-root-lattice}

The **root lattice** of \(\Phi\) is
\[
Q(\Phi):=\mathbb Z\Phi\subset V
\]
with the restricted bilinear form. If \(\Delta\) is a simple system, then
\[
Q(\Phi)=\mathbb Z\Delta,
\]
and \(\Delta\) is a \(\mathbb Z\)-basis of the root lattice.

Under the algebraic-geometric sign convention used by the project, the Euclidean form is multiplied by \(-1\), so all finite ADE root lattices are negative definite and their roots have norm \(-2\).

### Definition 68.4 (Root presentation) {#def-root-presentation}

Let \((J,b_J)\) be an ambient integral lattice or rational quadratic space, let \(S\) be a finite set, and let
\[
\rho:S\longrightarrow J
\]
be a family of vectors. Write
\[
F_S:=\mathbb Z^{(S)}
\]
for the free module on \(S\), and let
\[
u_\rho:F_S\longrightarrow J,
\qquad
[e_s]\longmapsto \rho(s)
\]
be the induced map.

The **lattice generated by the root presentation** is
\[
L_\rho:=\operatorname{im}(u_\rho)
\]
with the restricted form. The presentation is:

- a **root frame** if every \(\rho(s)\) is a root;
- a **root basis** if \(u_\rho:F_S\to L_\rho\) is an isomorphism;
- a **simple-root presentation** if the family is the ordered image of a simple system of a root system;
- an **embedded root presentation** if the inclusion \(L_\rho\hookrightarrow J\) is retained as part of the datum.

The forgetful sequence is therefore
\[
\{
\text{embedded simple-root presentations}
\}
\longrightarrow
\{
\text{lattices with a chosen root basis}
\}
\longrightarrow
\mathbf{Lat}_{\mathbb Z}.
\]
Neither arrow is generally an equivalence: the first forgets an ambient realization and the second forgets the root basis.

### Definition 68.5 (Categories of root frames and embedded root realizations) {#def-root-frame-categories}

Fix a finite indexing set \(S\). Let
\[
\mathbf{RootFrame}_S
\longrightarrow
\mathbf{Lat}_{\mathbb Z}
\]
be the Grothendieck construction whose fiber over \(L\) is the groupoid of \(S\)-indexed root
frames in \(L\). Concretely, an object is \((L,\rho)\), and a morphism
\[
(L,\rho)\longrightarrow(L',\rho')
\]
is an isometry \(f:L\to L'\) satisfying \(f\rho=\rho'\).

Let
\[
\mathbf{RootBasis}_S
\longrightarrow
\mathbf{RootFrame}_S
\]
be the locus on which \(u_\rho:\mathbb Z^{(S)}\to L\) is an isomorphism. For a fixed finite
Dynkin type \(\Gamma\) on \(S\), let
\[
\mathbf{RootBasis}_\Gamma
\longrightarrow
\mathbf{RootBasis}_S
\]
be the locus on which the root frame is a simple system of type \(\Gamma\).

An **embedded root realization** is an object of the corresponding locus in the arrow category
\[
\operatorname{Ar}(\mathbf{Lat}_{\mathbb Z})
\]
consisting of an isometric embedding \(i:L\hookrightarrow J\) together with a root basis on
\(L\), or equivalently its image in \(J\). The forgetful functors discard, successively, the
ambient embedding, the root basis, and the type certificate.

These are ordinary mathematical classifier categories. A named ADE construction is a chosen
point of an embedded-root-realization category followed by these forgetful functors.

### Construction 68.6 (Named root lattice from a presentation) {#construction-named-root-lattice}

A named ADE lattice is constructed by specifying a cited root realization
\[
(J_\Gamma,\Phi_\Gamma,\Delta_\Gamma)
\]
of the required Dynkin type \(\Gamma\), forming
\[
L_\Gamma:=Q(\Phi_\Gamma)=\mathbb Z\Delta_\Gamma,
\]
and then applying the negative sign convention to the form.

The intrinsic named lattice is the image in \(\mathbf{Lat}_{\mathbb Z}\). The ambient realization and ordered simple roots may be retained in enhanced categories when a later construction uses them.

### Theorem 68.7 (Independence of the standard realization) {#thm-standard-realization-independence}

Any two irreducible reduced crystallographic root systems of the same finite ADE type give isometric root lattices after the same normalization and sign choice.

This is a classification theorem of finite root systems. It is the comparison theorem that licenses the use of a convenient standard coordinate realization; it is not part of the definition of an arbitrary lattice.

## 69. Gram matrices and coordinate matrices

### Definition 69.1 (Coordinate matrix of a root frame) {#def-coordinate-matrix-root-frame}

Suppose the ambient lattice \(J\) has an ordered basis \(e=(e_1,\ldots,e_N)\), and the root frame is ordered as
\[
\Delta=(\alpha_1,\ldots,\alpha_r).
\]
The **coordinate matrix** of \(\Delta\) in \(e\) is the \(N\times r\) matrix \(R_\Delta\) whose \(j\)-th column is the coordinate vector of \(\alpha_j\).

This matrix records the embedding of the free module on the roots into the ambient free module. It is not the Gram matrix.

### Definition 69.2 (Gram matrix of a frame) {#def-gram-matrix-frame}

For a lattice \((L,b)\) with ordered frame \(v=(v_1,\ldots,v_r)\), its **Gram matrix** is
\[
G_v=(b(v_i,v_j))_{i,j}.
\]
If \(v\) is a basis, \(G_v\) is the matrix of the adjoint map
\[
\widetilde b:L\longrightarrow L^*
\]
relative to the basis \(v\) and its dual basis.

### Proposition 69.3 (Gram matrix from an ambient realization) {#prop-gram-from-ambient}

Let \(B_J\) be the matrix of the ambient form on \(J\) in the basis \(e\). Then
\[
\boxed{
G_\Delta=R_\Delta^{\mathsf T}B_JR_\Delta.
}
\]

Thus the Gram matrix is derived from:

1. the ambient quadratic form;
2. the chosen root vectors; and
3. the chosen ordering of those vectors.

It neither determines nor remembers the ambient embedding by itself.

### Remark 69.4 (A Gram matrix is not an embedded realization)

Two embeddings of an abstract lattice can induce the same Gram matrix on a chosen basis. Conversely, a Gram matrix constructs a coordinatized abstract lattice on \(\mathbb Z^r\), but does not supply an embedding of that lattice into a separately specified ambient lattice. The ambient coordinate matrix \(R_\Delta\), together with the equation
\[
R_\Delta^{\mathsf T}B_JR_\Delta=G_\Delta,
\]
is the additional realization datum.

## 70. Cartan matrices are derived root--coroot data

### Definition 70.1 (Cartan matrix) {#def-cartan-matrix}

Let \(\Delta=(\alpha_1,\ldots,\alpha_r)\) be a simple system, with coroots
\[
\alpha_j^\vee:=\frac{2\alpha_j}{(\alpha_j,\alpha_j)}.
\]
The **Cartan matrix** is
\[
C_\Delta=(\langle\alpha_i,\alpha_j^\vee\rangle)_{i,j}
=
\left(
\frac{2(\alpha_i,\alpha_j)}{(\alpha_j,\alpha_j)}
\right)_{i,j}.
\]

Intrinsically this is the matrix of the root--coroot pairing after choosing the simple-root and simple-coroot bases. Equivalently, it is the matrix of a homomorphism from the root lattice to the dual of the coroot lattice after those bases are chosen.

It is not, in general, the Gram matrix of a symmetric form on the root lattice. In nonsimply-laced types it is generally nonsymmetric.

### Proposition 70.2 (Simply-laced comparison) {#prop-simply-laced-comparison}

Suppose all simple roots have Euclidean squared length \(2\). Then
\[
C_\Delta=G_\Delta
\]
for the positive-definite Euclidean form. With the project's negative-definite form \(b=-(\ ,\ )\),
\[
\boxed{G_\Delta=-C_\Delta.}
\]

**Proof.** Equal root lengths make \(\alpha_j^\vee=\alpha_j\) in the positive normalization, so the root--coroot pairing is the inner product. Negating the form negates the Gram matrix while leaving the conventional Cartan entries \(2,-1,0\) unchanged. \(\square\)

### Remark 70.3 (Logical status of the comparison)

The equality \(G_\Delta=-C_\Delta\) in finite simply-laced type is not the definition of an ADE lattice. It is a derived comparison theorem after a simple-root basis, normalization, and sign convention have been chosen.

Nor is it an accidental numerical coincidence: it follows formally from equality of root lengths and the root--coroot formula. The error in the superseded form of Definition 23.2 was not the numerical equality; it was promoting this derived equality to the primary construction of the lattice.

### Convention 70.4 (Cartan matrices in this project) {#conv-cartan-matrices}

Cartan matrices have no role in the primary construction of named lattices, in the input to a Gram constructor, or in the definition of the lattice category. They may appear only as optional derived root-theoretic comparisons after the root realization and the Gram matrix have already been defined.

A formalization may omit Cartan matrices from the named-lattice modules entirely.

## 71. Standard negative-definite ADE realizations

The following coordinate models give canonical convenient points of the corresponding root-presentation categories. Other cited standard models are compared to them by isometry.

### Definition 71.1 (The lattice \(A_n^-\)) {#def-lattice-an-neg}

For \(n\ge1\), let
\[
A_n^-:=
\left\{
(x_1,\ldots,x_{n+1})\in\mathbb Z^{n+1}
\ \middle|\
\sum_{i=1}^{n+1}x_i=0
\right\}
\]
with the negative of the standard Euclidean form. The inclusion
\[
A_n^-\hookrightarrow I_{n+1}^-
\]
is part of its standard embedded realization.

A standard simple-root basis is
\[
\alpha_i=e_i-e_{i+1},
\qquad 1\le i\le n.
\]
The Gram matrix in this basis has diagonal entries \(-2\), adjacent entries \(1\), and all other entries \(0\).

### Definition 71.2 (The lattice \(D_n^-\)) {#def-lattice-dn-neg}

For \(n\ge4\), let
\[
D_n^-:=
\left\{
(x_1,\ldots,x_n)\in\mathbb Z^n
\ \middle|\
\sum_{i=1}^n x_i\in2\mathbb Z
\right\}
\]
with the negative Euclidean form. It is a sublattice of \(I_n^-\).

One may take
\[
\alpha_i=e_i-e_{i+1}
\quad(1\le i<n),
\qquad
\alpha_n=e_{n-1}+e_n,
\]
with the usual adjustment of indexing at the branching vertex.

### Definition 71.3 (The lattice \(E_8^-\)) {#def-lattice-e8-neg}

Let
\[
E_8^+
:=
\left\{
 x=(x_i)\in
 \mathbb Z^8\cup(\mathbb Z+\tfrac12)^8
 \ \middle|\
 \sum_{i=1}^8x_i\in2\mathbb Z
\right\}
\subset\mathbb Q^8
\]
with the standard Euclidean form, and define
\[
E_8^-:=-E_8^+
\]
by negating the form.

This is the even unimodular rank-eight lattice. It is not the even-coordinate sublattice of \(\mathbb Z^8\); that integral-coordinate sublattice is \(D_8\). Rather,
\[
E_8^+=D_8+\mathbb Z\cdot\tfrac12(1,1,1,1,1,1,1,1)
\]
inside \(\mathbb Q^8\), with the standard parity convention.

### Definition 71.4 (The lattices \(E_7^-\) and \(E_6^-\)) {#def-lattices-e7-e6-neg}

Inside the standard \(E_8^+\) realization, set
\[
u=e_1-e_2,
\qquad
v=e_2-e_3.
\]
Then \(u,v\) are adjacent roots spanning a copy of \(A_2\). Define
\[
E_7^+:=u^\perp\cap E_8^+,
\qquad
E_6^+:=(\mathbb Zu+\mathbb Zv)^\perp\cap E_8^+,
\]
and negate the forms to obtain \(E_7^-\) and \(E_6^-\).

The assertions that these have root-system types \(E_7\) and \(E_6\), and that alternate standard choices give isometric lattices, are comparison theorems.

### Convention 71.5 (Bare ADE notation) {#conv-bare-ade-notation}

In the project,
\[
A_n:=A_n^-,
\quad
D_n:=D_n^-,
\quad
E_6:=E_6^-,
\quad
E_7:=E_7^-,
\quad
E_8:=E_8^-.
\]
Thus
\[
\Lambda_{K3}=U^{\perp3}\perp E_8^{\perp2}.
\]

## 72. Relation to the Gram constructor

### Construction 72.1 (The general Gram constructor remains valid) {#construction-gram-constructor-role}

For a symmetric matrix \(G\in\operatorname{Mat}_r(R)\), the Gram constructor of Definition 21.3 produces the coordinatized form
\[
(R^r,b_G,e_1,\ldots,e_r),
\qquad
b_G(x,y)=x^{\mathsf T}Gy.
\]
This is a general construction of coordinatized forms. It remains useful and mathematically correct.

### Theorem 72.2 (Root presentation--Gram comparison) {#thm-root-gram-comparison}

Let \((L,\Delta)\) be a lattice with ordered root basis \(\Delta=(\alpha_1,\ldots,\alpha_r)\), and let \(G_\Delta\) be its Gram matrix. The basis isomorphism
\[
\mathbb Z^r\overset{\sim}{\longrightarrow}L,
\qquad
e_i\longmapsto\alpha_i
\]
is an isometry
\[
\operatorname{Gram}_r(G_\Delta)
\overset{\sim}{\longrightarrow}
(L,\Delta)
\]
in the category of coordinatized lattices.

After forgetting coordinates, it gives an isometry of intrinsic lattices.

### Convention 72.3 (Named ADE construction order) {#conv-ade-construction-order}

For a named ADE lattice the order of construction is:

1. specify the standard root realization;
2. take the integral span of its roots or simple roots;
3. obtain the intrinsic lattice by restriction of the ambient form;
4. choose a simple-root basis when coordinates are required;
5. derive its Gram matrix;
6. optionally compare that Gram matrix with the Cartan matrix in simply-laced type; and
7. optionally compare the intrinsic lattice with the output of the general Gram constructor.

The reverse order is not used as the mathematical definition of the named lattice.

***

# Part XV. Generators, presentations, and matrix descent

## 73. Finite generation as property and chosen generators as structure

### Definition 73.1 (Finite free modules) {#def-finite-free-modules}

Let \(R\) be a ring. Write
\[
F_n:=R^n.
\]
The standard basis of \(F_n\) identifies abstract linear maps by the canonical isomorphism
\[
\boxed{
\operatorname{Hom}_R(F_n,F_m)
\simeq
\operatorname{Mat}_{m\times n}(R).
}
\]

The left side is primary. The right side is its coordinate realization.

### Definition 73.2 (Chosen finite generating presentation) {#def-generating-presentation}

A **finite generating presentation** of an \(R\)-module \(M\) is a surjection
\[
q:F_n\twoheadrightarrow M
\]
for some \(n\ge0\).

The elements \(q(e_1),\ldots,q(e_n)\) are the chosen ordered generators. Conversely, an ordered generating family defines such a surjection.

### Definition 73.3 (Generated modules with abstract morphisms) {#def-genpres-abs}

Let
\[
\operatorname{GenPres}^{\mathrm{abs}}(R)
\]
be the category whose objects are finite generating presentations
\[
q:F_n\twoheadrightarrow M,
\]
and whose morphisms
\[
(q:F_n\twoheadrightarrow M)
\longrightarrow
(r:F_m\twoheadrightarrow N)
\]
are the completely general abstract module maps
\[
f:M\longrightarrow N.
\]
No condition is imposed on \(f\) by the chosen generators. Identities and composition are those of
\(R\text{-}\mathbf{Mod}\).

This is the analogue, for generating presentations, of the coordinatized-basis category of
Definition 13.6: presentations are retained on objects so that a morphism can be represented
and computed, but the morphism itself is the abstract map of modules.

The projection
\[
U_{\mathrm{abs}}:
\operatorname{GenPres}^{\mathrm{abs}}(R)
\longrightarrow
R\text{-}\mathbf{Mod}
\]
is the identity on morphisms and forgets the chosen presentation on objects.

### Definition 73.4 (Free-lift category) {#def-genpres-lift}

Let
\[
\operatorname{GenPres}^{\mathrm{lift}}(R)
\]
be the full locus in the arrow category
\[
\operatorname{Ar}(R\text{-}\mathbf{Mod})
\]
on the epimorphisms
\[
q:F_n\twoheadrightarrow M
\]
with finite standard free source.

A morphism from \(q:F_n\twoheadrightarrow M\) to \(r:F_m\twoheadrightarrow N\) is a commutative square
\[
\begin{CD}
F_n @>{A}>> F_m\\
@V{q}VV @VV{r}V\\
M @>{f}>> N.
\end{CD}
\]
The upper map \(A\) is a chosen free lift of the abstract lower map \(f\).

There is a functor
\[
\Pi:
\operatorname{GenPres}^{\mathrm{lift}}(R)
\longrightarrow
\operatorname{GenPres}^{\mathrm{abs}}(R)
\]
which is the identity on objects and sends \((A,f)\) to \(f\). The matrix-descent theorem below
describes this functor on every hom-space.

### Remark 73.5 (Strict frame preservation is a further restriction)

The fixed-source comma category
\[
(F_n\downarrow R\text{-}\mathbf{Mod})
\]
of Definition 13.5 uses morphisms \(f\) satisfying \(fq=r\). It is the special case of the lift category in which the
upper map is fixed to be \(1_{F_n}\), and hence requires equal frame size. It classifies strictly
frame-preserving maps.

The three morphism conventions must be distinguished:

1. abstract maps \(f:M\to N\) in \(\operatorname{GenPres}^{\mathrm{abs}}(R)\);
2. chosen free lifts \((A,f)\) in \(\operatorname{GenPres}^{\mathrm{lift}}(R)\); and
3. strictly frame-preserving maps in the fixed-source comma category.

Matrices describe the second convention. The first is the intrinsic hom-space.

### Definition 73.6 (Finite generation property) {#def-finite-generation-property}

The module \(M\) is **finitely generated** if the fiber over \(M\) of the object projection
\[
\operatorname{GenPres}^{\mathrm{lift}}(R)
\longrightarrow
R\text{-}\mathbf{Mod}
\]
is inhabited. Equivalently,
\[
M\text{ is finitely generated}
\quad\Longleftrightarrow\quad
\exists n\;\exists q:F_n\twoheadrightarrow M.
\]

Categorically, the finite-generation property is the \((-1)\)-truncation of the classifier of
chosen finite generating presentations. A chosen generating family is a point of the untruncated
fiber; finite generation remembers only its existence.

This is the required distinction:
\[
\boxed{
\text{finitely generated}
\ne
\text{finitely generated with chosen generators}.
}
\]

## 74. Descent of matrices through generating presentations

Let
\[
q:F_n\twoheadrightarrow M,
\qquad
r:F_m\twoheadrightarrow N
\]
be finite generating presentations, and set
\[
K_q:=\ker(q),
\qquad
K_r:=\ker(r).
\]

### Definition 74.1 (Compatible free lift) {#def-compatible-free-lift}

A linear map
\[
A:F_n\longrightarrow F_m
\]
is **compatible with the presentations** if
\[
A(K_q)\subseteq K_r.
\]
Write
\[
\operatorname{Comp}(q,r)
:=
\{A\in\operatorname{Hom}_R(F_n,F_m)\mid A(K_q)\subseteq K_r\}.
\]

Under standard bases, \(\operatorname{Comp}(q,r)\) is a submodule of
\[
\operatorname{Mat}_{m\times n}(R).
\]

### Proposition 74.2 (Descent criterion) {#prop-descent-criterion}

A map \(A:F_n\to F_m\) induces a unique map
\[
\overline A:M\longrightarrow N
\]
satisfying
\[
\overline A\,q=rA
\]
if and only if
\[
A(K_q)\subseteq K_r.
\]

**Proof.** The composite \(rA\) factors through the quotient \(F_n/K_q\simeq M\) exactly when it vanishes on \(K_q\), equivalently when \(A(K_q)\subseteq\ker(r)=K_r\). Uniqueness follows from surjectivity of \(q\). \(\square\)

### Theorem 74.3 (Matrix-descent exact sequence) {#thm-matrix-descent}

There is a natural short exact sequence of \(R\)-modules
\[
\boxed{
0
\longrightarrow
\operatorname{Hom}_R(F_n,K_r)
\longrightarrow
\operatorname{Comp}(q,r)
\xrightarrow{\;\operatorname{desc}\;}
\operatorname{Hom}_R(M,N)
\longrightarrow
0.
}
\]

The first map is postcomposition with the inclusion \(K_r\hookrightarrow F_m\), and \(\operatorname{desc}(A)=\overline A\).

**Proof sketch.** Proposition 74.2 defines the middle map. Given \(f:M\to N\), the composite \(fq:F_n\to N\) lifts through the surjection \(r:F_m\twoheadrightarrow N\), since \(F_n\) is projective. Any such lift automatically preserves the kernels and hence descends to \(f\). The kernel consists exactly of maps whose image lies in \(K_r\). \(\square\)

### Corollary 74.4 (Precise matrix semantics) {#cor-matrix-semantics}

After choosing standard bases:

1. not every matrix \(A\in\operatorname{Mat}_{m\times n}(R)\) descends;
2. a matrix descends exactly when it preserves the relation submodules;
3. every abstract morphism \(M\to N\) is represented by at least one compatible matrix; and
4. two compatible matrices represent the same morphism exactly when their difference has image in \(K_r\).

Thus matrices form a space of representatives of abstract morphisms, not the definition of those morphisms.

### Corollary 74.5 (Basis case) {#cor-matrix-descent-basis-case}

If \(q:F_n\overset\sim\to M\) and \(r:F_m\overset\sim\to N\) are basis frames, then
\[
K_q=K_r=0,
\]
so Theorem 74.3 reduces to the canonical isomorphism
\[
\operatorname{Hom}_R(M,N)
\simeq
\operatorname{Hom}_R(F_n,F_m)
\simeq
\operatorname{Mat}_{m\times n}(R).
\]

The coordinate description of morphisms of based free modules in Definition 13.6 is therefore the kernel-zero special case of general matrix descent.

## 75. Finite presentations

### Definition 75.1 (Chosen finite presentation) {#def-finite-presentation}

A **finite presentation** of an \(R\)-module \(M\) is an exact sequence
\[
F_m
\xrightarrow{d_M}
F_n
\xrightarrow{q_M}
M
\longrightarrow0.
\]
It consists of chosen generators together with chosen finite generators for the module of relations.

### Definition 75.2 (Finite-presentation objects and abstract morphisms) {#def-finpres-abs}

Let
\[
\operatorname{FinPres}^{\mathrm{abs}}(R)
\]
be the category whose objects are exact diagrams
\[
F_m\xrightarrow{d_M}F_n\xrightarrow{q_M}M\longrightarrow0
\]
with \(m,n<\infty\), and whose morphisms are the completely general abstract module maps
\[
f:M\longrightarrow N.
\]
The chosen presentations are retained on objects, but no lift is built into the definition of an
abstract morphism.

### Definition 75.3 (Lifted morphisms of finite presentations) {#def-finpres-lift}

Let \(J_{\mathrm{pres}}\) be the diagram shape
\[
2\longrightarrow1\longrightarrow0.
\]
The category
\[
\operatorname{FinPres}^{\mathrm{lift}}(R)
\]
is the exactness locus in the corresponding diagram category whose objects are the same finite
presentations. A morphism is a natural transformation, equivalently a commutative diagram
\[
\begin{CD}
F_m @>{d_M}>> F_n @>{q_M}>> M @>>> 0\\
@V{A_1}VV @V{A_0}VV @V{f}VV \\
F_{m'} @>{d_N}>> F_{n'} @>{q_N}>> N @>>> 0.
\end{CD}
\]

There is an identity-on-objects functor
\[
\operatorname{FinPres}^{\mathrm{lift}}(R)
\longrightarrow
\operatorname{FinPres}^{\mathrm{abs}}(R)
\]
forgetting \(A_1,A_0\). The maps \(A_1,A_0\) have matrix realizations after the standard free
bases are used; \(f\) is the abstract module morphism they present.

### Definition 75.4 (Finite presentation property) {#def-finite-presentation-property}

The module \(M\) is **finitely presented** if the fiber of
\[
\operatorname{FinPres}^{\mathrm{lift}}(R)
\longrightarrow
R\text{-}\mathbf{Mod},
\qquad
(F_m\to F_n\to M)\longmapsto M,
\]
is inhabited.

Equivalently,
\[
M\text{ is finitely presented}
\quad\Longleftrightarrow\quad
\exists m,n\;
F_m\to F_n\to M\to0
\text{ exact}.
\]

Again, a chosen finite presentation is structure; finite presentation is its propositional truncation.

### Proposition 75.5 (Lifting a morphism to finite presentations) {#prop-presentation-lift}

Let finite presentations of \(M\) and \(N\) be fixed. Every module map
\[
f:M\longrightarrow N
\]
admits a morphism of presentation diagrams lifting \(f\).

**Proof sketch.** Lift \(fq_M:F_n\to N\) through \(q_N:F_{n'}\twoheadrightarrow N\) using projectivity of \(F_n\), obtaining \(A_0\). The composite \(A_0d_M\) lands in \(\ker q_N=\operatorname{im}d_N\), and projectivity of \(F_m\) lifts it through \(d_N\), producing \(A_1\). \(\square\)

### Remark 75.6 (Nonuniqueness at the presentation level)

The lift in Proposition 75.5 is not canonical. A two-term finite presentation does not by itself provide the complete homotopy relation that identifies all lifts of the same abstract morphism. That relation is naturally expressed after extending the presentations to projective resolutions.

## 76. Partial resolutions and the \(FP_n\) hierarchy

### Definition 76.1 (Augmented chain complex) {#def-augmented-chain-complex}

An **augmented chain complex over \(M\)** is a sequence
\[
\cdots
\longrightarrow
P_2
\xrightarrow{d_2}
P_1
\xrightarrow{d_1}
P_0
\xrightarrow{\epsilon}
M
\longrightarrow0
\]
with
\[
d_i d_{i+1}=0,
\qquad
\epsilon d_1=0.
\]
It is a **resolution** if the augmented sequence is exact.

### Definition 76.2 (Free and projective resolution) {#def-projective-resolution}

A resolution is:

- **free** if every \(P_i\) is free;
- **projective** if every \(P_i\) is projective;
- **finite in degree \(i\)** if \(P_i\) is finitely generated;
- **finite free in degree \(i\)** if \(P_i\) is finite-rank free.

A chosen resolution is a point of a category of exact augmented complexes. It is additional data, not an intrinsic replacement for \(M\).

### Definition 76.3 (Modules of type \(FP_n\)) {#def-fp-n}

For \(n\ge0\), an \(R\)-module \(M\) is of type \(FP_n\) if it admits a projective resolution
\[
\cdots\to P_1\to P_0\to M\to0
\]
in which \(P_i\) is finitely generated for \(0\le i\le n\).

Under the standard module conventions,
\[
FP_0=\text{finitely generated},
\qquad
FP_1=\text{finitely presented}.
\]
The property \(FP_n\) is the propositional truncation of the category of chosen partial finite projective resolutions through degree \(n\).

### Remark 76.4 (A generating surjection does not canonically determine a resolution)

A surjection
\[
P_0\twoheadrightarrow M
\]
determines its kernel \(K_1\), but it does not canonically choose a free or projective module \(P_1\) mapping onto \(K_1\). To continue, one chooses a surjection
\[
P_1\twoheadrightarrow K_1,
\]
then repeats with its kernel.

Thus a generating frame can be extended to a free resolution when enough free objects and the required choices are available, but the extension is not implicit or canonical. The iterated syzygies and the choices of their generators are part of the resolution datum.

### Remark 76.5 (A chain complex is not a DGA)

A chain complex carries only additive and differential data. A differential graded algebra is a chain complex equipped with an associative multiplication and unit compatible with the differential. In the symmetric monoidal category of chain complexes,
\[
\mathbf{DGA}_R
=
\operatorname{Alg}_{E_1}(\operatorname{Ch}(R)).
\]

DGAs become relevant when the presentation or resolution must carry multiplicative structure. They are not required for the general theory of module generators, relations, or projective resolutions.

## 77. The chain-complex construction as a categorical functor

### Definition 77.1 (Chain-complex functor) {#def-chain-complex-functor}

Let \(\mathbf{AddCat}\) denote the higher category of additive categories, additive functors, and their higher transformations. The assignment
\[
\mathcal A
\longmapsto
\operatorname{Ch}(\mathcal A)
\]
extends degreewise to a functor
\[
\operatorname{Ch}:
\mathbf{AddCat}
\longrightarrow
\mathbf{AddCat}.
\]

It is not defined on an arbitrary category without additive structure, because the equation \(d^2=0\) uses zero morphisms and addition of morphisms.

### Definition 77.2 (Termwise properties and lifted complex structure) {#def-termwise-classifier}

Let
\[
p:\mathcal A.P\longrightarrow\mathcal A
\]
be a classifier over an additive category.

If \(p\) is a property classifier represented by a replete full additive subcategory, then for a
set of degrees \(S\subseteq\mathbb Z\) the condition that a complex \(K\) have \(P\) in every
degree of \(S\) is the homotopy intersection of the pullbacks
\[
\operatorname{ev}_i^*p
\qquad(i\in S),
\]
where
\[
\operatorname{ev}_i:
\operatorname{Ch}(\mathcal A)
\longrightarrow
\mathcal A
\]
is degree evaluation. For \(S=\mathbb Z\), this is the category of complexes whose terms all lie
in \(\mathcal A.P\).

If \(p\) carries nontrivial structure, termwise lifts alone do not ensure that the differentials
preserve that structure. When \(\mathcal A.P\) is additive and \(p\) is additive, the correct
classifier is instead
\[
\operatorname{Ch}(p):
\operatorname{Ch}(\mathcal A.P)
\longrightarrow
\operatorname{Ch}(\mathcal A),
\]
or the corresponding homotopy pullback of the whole complex diagram. This retains the lifted
differentials and their compatibility data.

### Definition 77.3 (Resolution classifier) {#def-resolution-classifier}

Let \(\operatorname{AugCh}(R)\) be the category of augmented chain complexes of \(R\)-modules. The category of projective resolutions is the intersection of:

1. the exactness classifier for the augmented complex;
2. the termwise projective classifier in all nonnegative degrees.

The category of finite free resolutions through degree \(n\) is obtained by additionally imposing finite freeness in degrees \(0,\ldots,n\).

The projection to the augmentation target
\[
\operatorname{Res}_R
\longrightarrow
R\text{-}\mathbf{Mod}
\]
is the classifier whose fiber over \(M\) is the category of chosen resolutions of \(M\).

### Remark 77.4 (Finite generation and finite presentation as truncations of one theory)

Finite generation, finite presentation, \(FP_n\), and \(FP_\infty\) are successive truncations of the resolution theory:

- finite generation inspects a finite free degree-zero object and surjective augmentation;
- finite presentation also controls the first syzygy by a finite free degree-one object;
- \(FP_n\) controls finite projective objects through degree \(n\);
- a chosen resolution retains the entire untruncated diagram and its morphisms.

This is the uniform theory of which the finiteness notions of Section 13 are the truncations.

## 78. Comparison theorem and matrix complexes

### Theorem 78.1 (Comparison theorem for projective resolutions) {#thm-resolution-comparison}

Let
\[
P_\bullet\twoheadrightarrow M,
\qquad
Q_\bullet\twoheadrightarrow N
\]
be projective resolutions. Every module morphism
\[
f:M\longrightarrow N
\]
lifts to a chain map
\[
F_\bullet:P_\bullet\longrightarrow Q_\bullet,
\]
and any two chain maps lifting the same \(f\) are chain homotopic.

Consequently,
\[
\boxed{
\operatorname{Hom}_R(M,N)
\simeq
\operatorname{Hom}_{K(R)}(P_\bullet,Q_\bullet),
}
\]
where the right side consists of augmentation-compatible chain maps modulo chain homotopy.

This is the full generalization of the degree-zero matrix-descent theorem.

### Definition 78.2 (Matrix representative of a chain map) {#def-matrix-chain-map}

Suppose each \(P_i\) and \(Q_i\) is equipped with a finite basis. A chain map is represented degreewise by matrices
\[
A_i:P_i\longrightarrow Q_i
\]
satisfying
\[
d_QA_i=A_{i-1}d_P.
\]
A chain homotopy from \(A\) to \(B\) is represented by matrices \(H_i:P_i\to Q_{i+1}\) satisfying
\[
A-B=d_QH+Hd_P.
\]

Thus morphisms in the homotopy or derived category are represented by matrix complexes modulo the homotopy relation. The matrices are representatives on chosen free resolutions; the abstract morphisms are the resulting homotopy classes.

### Corollary 78.3 (No category of “matrix morphisms” is foundational) {#cor-no-matrix-category}

A matrix category may be used as a skeletal presentation of standard finite free modules or of based finite free complexes. The foundational categories retain abstract linear maps or chain maps. Equivalences with matrix presentations are named comparison theorems.

***

# Part XVI. Stable and derived formulation

## 79. Derived module categories

### Definition 79.1 (Derived \(\infty\)-category of a ring) {#def-derived-category-ring}

Let \(R\) be an ordinary ring. Let \(W\) be the class of quasi-isomorphisms of chain complexes of \(R\)-modules. The derived \(\infty\)-category is
\[
\mathcal D(R)
:=
N_{\mathrm{dg}}(\operatorname{Ch}(R))[W^{-1}],
\]
or any equivalent stable \(\infty\)-categorical model.

For an ordinary ring this is equivalent to the stable \(\infty\)-category of modules over the Eilenberg--Mac Lane \(E_1\)-ring \(HR\). For an \(E_1\)-ring spectrum \(A\), the intrinsic replacement is directly
\[
\operatorname{Mod}_A.
\]

### Remark 79.2 (The derived category is the semantic object)

Chain complexes, projective resolutions, injective resolutions, and cofibrant replacements are presentations of objects and morphisms in the derived category. They are indispensable computational models, but the intrinsic object is the point of the stable \(\infty\)-category.

Accordingly, a derived implementation should expose the stable object while retaining the chosen resolution as a lift through a presentation classifier.

### Definition 79.3 (Perfect object) {#def-perfect-object}

An object \(P\in\mathcal D(R)\) is **perfect** if it is compact. For an ordinary ring, the perfect objects are precisely those represented by bounded complexes of finitely generated projective modules.

A chosen bounded finite-projective complex is a presentation of a perfect object. Perfectness is the corresponding intrinsic property.

### Remark 79.4 (Finite presentation is not perfectness)

A finitely presented module, regarded as an object of the heart of the standard \(t\)-structure on \(\mathcal D(R)\), need not be perfect. Perfectness requires a bounded finite-projective resolution, not merely a finite presentation.

The hierarchy must therefore retain the distinctions
\[
\text{finite generation},
\quad
\text{finite presentation},
\quad
FP_n,
\quad
\text{perfectness}.
\]

## 80. Derived presentations and cells

### Definition 80.1 (Presentation category over a stable \(\infty\)-category) {#def-cellular-presentation}

Let \(\mathcal C\) be a presentable stable \(\infty\)-category and let \(\mathcal G\subseteq\mathcal C\) be a selected class of compact or projective generators. A **cellular presentation** of \(X\in\mathcal C\) is a chosen filtered or simplicial resolution of \(X\) whose stages are assembled from objects of \(\mathcal G\) by the permitted finite sums, shifts, and cofibers.

The category of such presentations maps to \(\mathcal C\) by geometric realization or totalization. Its fiber over \(X\) is the moduli category of chosen presentations of \(X\).

This is the derived analogue of the category of finite free presentations of an ordinary module.

### Remark 80.2 (Classical chain complexes as one model)

The classical chain-complex functor is an appropriate concrete model for ordinary modules and additive categories. It should not be promoted to a variance-free functor on every object of the ambient \((\infty,2)\)-category.

The general semantic layer is stable or derived. A chosen dg, model-categorical, spectral, or simplicial presentation is additional mathematical data whose comparison with the stable object is a theorem.

### Definition 80.3 (DG algebras and derived algebra objects) {#def-dga-derived-algebra}

For an ordinary commutative ring \(R\), a differential graded associative algebra is an \(E_1\)-algebra object in the monoidal category of chain complexes:
\[
\mathbf{DGA}_R
=
\operatorname{Alg}_{E_1}(\operatorname{Ch}(R)).
\]
After localization, the intrinsic derived notion is an \(E_1\)-algebra in \(\mathcal D(R)\) or an \(E_1\)-ring spectrum. Commutative derived algebras are governed by the corresponding \(E_\infty\)-operad.

This operadic construction is used only when multiplicative structure is actually part of the object.

***

# Part XVII. Categorical synthesis of presentations

## 81. One presentation calculus

The root-lattice correction and the matrix-descent correction are instances of the same categorical pattern.

### Principle 81.1 (Free source, relation object, and descent) {#principle-presentation-descent}

A presentation of an object \(X\) consists of:

1. a free, projective, or otherwise controlled source \(P\);
2. a morphism \(P\to X\), often an epimorphism;
3. the kernel, relation object, or higher syzygies governing descent; and
4. an exact or homotopy-coherent diagram recording these data.

A coordinate matrix describes a morphism between the controlled free sources. It represents a morphism between the presented objects precisely when it respects the relation objects. The quotient by changes through the target relations, or by chain homotopy in a full resolution, produces the intrinsic morphism.

### Example 81.2 (Root presentation)

For an ordered simple-root system \(\Delta\), the free source is
\[
\mathbb Z^{(\Delta)}.
\]
The map to the ambient quadratic module sends basis elements to roots. When \(\Delta\) is a simple-root basis, the kernel vanishes, so the Gram matrix gives a complete coordinate description of the intrinsic root lattice. The ambient embedding remains additional data.

### Example 81.3 (Generated module)

For a generating presentation \(F_n\twoheadrightarrow M\), the relation object is \(K_q\). A matrix \(F_n\to F_m\) descends precisely when it sends \(K_q\) into \(K_r\). The quotient exact sequence of Theorem 74.3 gives the intrinsic hom-space.

### Example 81.4 (Projective resolution)

For a projective resolution, the relation data continue through every syzygy. Degreewise matrices define a chain map; the chain-map equations enforce descent at every stage; chain homotopy identifies representatives of the same derived morphism.

### Principle 81.5 (No presentation artifact is promoted) {#principle-no-promotion}

The following are never promoted to intrinsic definitions when a lower-level construction exists:

- a Cartan matrix in place of a root realization;
- a Gram matrix in place of a lattice with a chosen basis;
- a matrix in place of an abstract linear map;
- a two-term presentation in place of a module;
- a projective resolution in place of a derived object;
- a chain complex in place of a DGA when multiplication is required; or
- a DGA in place of its derived \(E_1\)-algebra object.

Each presentation is retained when computations require it, and its comparison with the intrinsic object is a named theorem.

***

# Part XVIII. Conventions and scalar change for modules

This part and the five that follow develop the corrected theory of module and bimodule
families, scalar change, and Morita 2-geometry. They replace the superseded form of
Definition 13.8 and make precise the variance warning of Definition 13.2: the assignment
\(R\mapsto R\text{-}\mathbf{Mod}\) has two standard variances, covariant extension of
scalars and contravariant restriction of scalars, whose unstraightenings are respectively
cocartesian and cartesian fibrations; the same distinction governs bimodules over
\(\mathbf{Ring}\times\mathbf{Ring}\). The fiberwise functors forgetting one bimodule
action are natural for restriction of scalars but only lax or oplax for simultaneous
extension. The intrinsic higher-categorical home is the Morita
\((\infty,2)\)-category, in which rings are objects, bimodules are 1-morphisms,
composition is relative tensor product, and left and right module categories are the hom
\(\infty\)-categories from and to the monoidal unit \(\mathbb Z\).

## 82. Rings and the opposite involution

### Definition 82.1 (The category of rings) {#def-ring-category}

Let \(\mathbf{Ring}\) denote the category of associative unital rings and unital ring homomorphisms. We use the same symbol for its image in \(\mathbf{Cat}_\infty\).

### Definition 82.2 (Opposite-ring involution) {#def-opposite-ring-involution}

The **opposite-ring functor** is the involutive equivalence
\[
(-)^{\mathrm{op}}:\mathbf{Ring}\longrightarrow\mathbf{Ring},
\qquad
R\longmapsto R^{\mathrm{op}},
\qquad
f\longmapsto f^{\mathrm{op}}.
\]
There is a canonical equivalence
\[
(R^{\mathrm{op}})^{\mathrm{op}}\simeq R.
\]

### Remark 82.3 (A functor is not a family of arrows to its values)

The functor \((-)^{\mathrm{op}}\) does not supply a morphism
\[
R\longrightarrow R^{\mathrm{op}}
\]
for every ring \(R\). Such a family would be additional data, namely a natural transformation from the identity functor to the opposite-ring functor. For a fixed ring, a homomorphism \(R\to R^{\mathrm{op}}\) is an anti-homomorphism of the underlying ring, and an isomorphism \(R\simeq R^{\mathrm{op}}\) is an anti-isomorphism.

## 83. Left and right modules

### Convention 83.1 (One module convention) {#conv-left-module-convention}

The notation
\[
R\text{-}\mathbf{Mod}
\]
always denotes the category of **left** \(R\)-modules and \(R\)-linear maps.

The category of right \(R\)-modules is defined by
\[
\mathbf{Mod}\text{-}R
:=
R^{\mathrm{op}}\text{-}\mathbf{Mod}.
\]
Thus right modules are not a second primitive family; they are left modules over the opposite ring. This restates the convention of Definition 13.1.

### Definition 83.2 (Extension and restriction of scalars: left modules) {#def-scalar-change-left}

Let \(f:R\to S\) be a ring homomorphism. Regard \(S\) as an \((S,R)\)-bimodule by left multiplication and by the right action
\[
s\cdot r:=s f(r).
\]
Define
\[
f_!^L:R\text{-}\mathbf{Mod}\longrightarrow S\text{-}\mathbf{Mod},
\qquad
M\longmapsto {}_S S_R\otimes_R M.
\]
This is **extension of scalars**.

Define
\[
f^{*L}:S\text{-}\mathbf{Mod}\longrightarrow R\text{-}\mathbf{Mod}
\]
by restricting the left action along \(f\). There is an adjunction
\[
f_!^L\dashv f^{*L}.
\]

### Definition 83.3 (Extension and restriction of scalars: right modules) {#def-scalar-change-right}

For a right \(R\)-module \(N\), define
\[
f_!^R(N):=N\otimes_R {}_R S_S,
\]
a right \(S\)-module. Restriction along \(f\) defines
\[
f^{*R}:\mathbf{Mod}\text{-}S\longrightarrow\mathbf{Mod}\text{-}R,
\]
and
\[
f_!^R\dashv f^{*R}.
\]

### Proposition 83.4 (The four module-family functors) {#prop-module-family-functors}

Scalar change defines coherent functors
\[
\mathbf{LMod}_!: \mathbf{Ring}\longrightarrow\mathbf{Cat}_\infty,
\qquad
R\longmapsto R\text{-}\mathbf{Mod},
\qquad
f\longmapsto f_!^L,
\]
\[
\mathbf{LMod}^{*}: \mathbf{Ring}^{\mathrm{op}}\longrightarrow\mathbf{Cat}_\infty,
\qquad
f^{\mathrm{op}}\longmapsto f^{*L},
\]
\[
\mathbf{RMod}_!: \mathbf{Ring}\longrightarrow\mathbf{Cat}_\infty,
\qquad
R\longmapsto\mathbf{Mod}\text{-}R,
\qquad
f\longmapsto f_!^R,
\]
and
\[
\mathbf{RMod}^{*}: \mathbf{Ring}^{\mathrm{op}}\longrightarrow\mathbf{Cat}_\infty,
\qquad
f^{\mathrm{op}}\longmapsto f^{*R}.
\]
Moreover,
\[
\mathbf{RMod}_!\simeq \mathbf{LMod}_!\circ(-)^{\mathrm{op}},
\qquad
\mathbf{RMod}^{*}\simeq \mathbf{LMod}^{*}\circ(-)^{\mathrm{op}}
\]
after applying the canonical equivalence between right \(R\)-modules and left \(R^{\mathrm{op}}\)-modules.

### Remark 83.5 (Coherence rather than strict equality)

For composable homomorphisms \(R\xrightarrow f S\xrightarrow g T\), there is a canonical equivalence
\[
T\otimes_S(S\otimes_R M)\simeq T\otimes_RM,
\]
not a preferred literal equality. The functor to \(\mathbf{Cat}_\infty\) records these associativity equivalences and their higher coherence. This is the basic example motivating the Grothendieck construction of module categories.

## 84. Grothendieck constructions of module families

### Definition 84.1 (Cocartesian total category of left modules) {#def-lmod-cocartesian}

Let
\[
\pi_L^!:
\int\mathbf{LMod}_!
\longrightarrow
\mathbf{Ring}
\]
be the unstraightening of \(\mathbf{LMod}_!\). It is a cocartesian fibration.

An object of \(\int\mathbf{LMod}_!\) is a pair \((R,M)\), where \(M\) is a left \(R\)-module. A morphism over \(f:R\to S\) can be represented equivalently as
\[
\varphi:S\otimes_RM\longrightarrow N
\]
in \(S\text{-}\mathbf{Mod}\), or as an additive map
\[
\widetilde\varphi:M\longrightarrow N
\]
satisfying
\[
\widetilde\varphi(rm)=f(r)\widetilde\varphi(m).
\]
The cocartesian morphism with source \((R,M)\) over \(f\) has target \((S,S\otimes_RM)\).

### Definition 84.2 (Cartesian total category of left modules) {#def-lmod-cartesian}

Let
\[
\pi_L^*:
\int\mathbf{LMod}^{*}
\longrightarrow
\mathbf{Ring}
\]
be the unstraightening of the contravariant restriction functor. It is a cartesian fibration. Its cartesian transport along \(f:R\to S\) is
\[
f^{*L}:S\text{-}\mathbf{Mod}\longrightarrow R\text{-}\mathbf{Mod}.
\]

The analogous constructions are denoted
\[
\pi_R^!:
\int\mathbf{RMod}_!\to\mathbf{Ring},
\qquad
\pi_R^*:
\int\mathbf{RMod}^{*}\to\mathbf{Ring}.
\]

### Proposition 84.3 (Fibers over points) {#prop-module-family-fibers}

Let \(\iota_R:*\to\mathbf{Ring}\) be the point classifying \(R\). Then
\[
*\times^h_{\mathbf{Ring}}\int\mathbf{LMod}_!
\simeq
(\pi_L^!)^{-1}(R)
\simeq
R\text{-}\mathbf{Mod},
\]
and similarly for the cartesian total category and for right modules.

The fiber is independent of whether extension or restriction is chosen for transport; the choice changes the morphisms between different fibers, not the fiber over a fixed ring.

### Remark 84.4 (Terminology)

The Grothendieck construction is the total category \(\int\mathbf{LMod}\), not the individual category \(R\text{-}\mathbf{Mod}\). The latter is a fiber of the former. This makes precise the variance warning of Definition 13.2.

***

# Part XIX. Bimodule categories and their total families

## 85. Bimodules as compatible pairs of actions

### Definition 85.1 (Bimodule) {#def-bimodule-actions}

Let \(R,S\) be rings. An **\((R,S)\)-bimodule** is an abelian group \(M\) equipped with a left \(R\)-action and a right \(S\)-action satisfying
\[
(rm)s=r(ms)
\qquad
(r\in R,\ m\in M,\ s\in S).
\]
A morphism of \((R,S)\)-bimodules is an additive map preserving both actions. Write
\[
{}_R\mathbf{Bimod}_S
\]
for the resulting category.

The phrase “bilinear map” is not used for a morphism in this category: a bimodule homomorphism is a unary additive map linear for both actions.

### Definition 85.2 (The category of two unconstrained actions) {#def-biact}

Let
\[
U_R:R\text{-}\mathbf{Mod}\to\mathbf{Ab},
\qquad
U_S:\mathbf{Mod}\text{-}S\to\mathbf{Ab}
\]
be the underlying-additive-group functors. Define
\[
\mathbf{BiAct}(R,S)
:=
R\text{-}\mathbf{Mod}
\times^h_{\mathbf{Ab}}
\mathbf{Mod}\text{-}S.
\]
An object is an abelian group equipped with a left \(R\)-action and a right \(S\)-action, together with the comparison identifying the two underlying additive groups. No commutation of the actions is imposed.

### Definition 85.3 (Commutation classifier) {#def-commutation-classifier}

On an object of \(\mathbf{BiAct}(R,S)\), the two composites
\[
R\otimes_{\mathbb Z}M\otimes_{\mathbb Z}S
\rightrightarrows
M
\]
are
\[
r\otimes m\otimes s\longmapsto (rm)s,
\qquad
r\otimes m\otimes s\longmapsto r(ms).
\]
The full replete locus on which these maps agree is \({}_R\mathbf{Bimod}_S\). Hence there is a property classifier
\[
{}_R\mathbf{Bimod}_S
\longrightarrow
\mathbf{BiAct}(R,S).
\]

Thus the two actions are structure, their coexistence on one additive group is a pullback of structure classifiers, and their commutation is an additional diagrammatic property.

### Proposition 85.4 (Enveloping-ring description) {#prop-enveloping-ring}

There is a canonical equivalence
\[
{}_R\mathbf{Bimod}_S
\simeq
(R\otimes_{\mathbb Z}S^{\mathrm{op}})\text{-}\mathbf{Mod}.
\]
The left action of \(R\otimes S^{\mathrm{op}}\) is
\[
(r\otimes s^{\mathrm{op}})m:=rms.
\]
Conversely, restricting an \(R\otimes S^{\mathrm{op}}\)-action along the two canonical ring maps gives commuting left \(R\)- and right \(S\)-actions.

No additional centrality hypothesis is required for ordinary unital rings over \(\mathbb Z\).

## 86. Scalar change for bimodules

### Definition 86.1 (Simultaneous extension of scalars) {#def-bimodule-extension}

Let \(f:R\to R'\) and \(g:S\to S'\). Define
\[
(f,g)_!:{}_R\mathbf{Bimod}_S
\longrightarrow
{}_{R'}\mathbf{Bimod}_{S'}
\]
by
\[
(f,g)_!M
:=
{}_{R'}R'_R\otimes_R M\otimes_S{}_SS'_{S'}.
\]
Equivalently,
\[
(f,g)_!M=R'\otimes_RM\otimes_SS'.
\]

### Definition 86.2 (Simultaneous restriction of scalars) {#def-bimodule-restriction}

For \(N\in{}_{R'}\mathbf{Bimod}_{S'}\), define
\[
(f,g)^*N\in{}_R\mathbf{Bimod}_S
\]
by
\[
r\cdot n\cdot s:=f(r)n g(s).
\]
There is an adjunction
\[
(f,g)_!\dashv(f,g)^*.
\]

### Proposition 86.3 (Bimodule-family functors) {#prop-bimodule-family-functors}

The constructions above define coherent functors
\[
\mathbf{BiMod}_!:
\mathbf{Ring}\times\mathbf{Ring}
\longrightarrow
\mathbf{Cat}_\infty,
\qquad
(R,S)\longmapsto{}_R\mathbf{Bimod}_S,
\]
and
\[
\mathbf{BiMod}^{*}:
(\mathbf{Ring}\times\mathbf{Ring})^{\mathrm{op}}
\longrightarrow
\mathbf{Cat}_\infty.
\]
Their unstraightenings are respectively a cocartesian fibration
\[
\pi_{\mathrm{Bi}}^!:
\int\mathbf{BiMod}_!
\longrightarrow
\mathbf{Ring}\times\mathbf{Ring}
\]
and a cartesian fibration
\[
\pi_{\mathrm{Bi}}^*:
\int\mathbf{BiMod}^{*}
\longrightarrow
\mathbf{Ring}\times\mathbf{Ring}.
\]

### Definition 86.4 (Morphisms in the cocartesian total category) {#def-bimodule-cocartesian-morphisms}

An object of \(\int\mathbf{BiMod}_!\) is a triple \((R,S,M)\). A morphism
\[
(R,S,M)\longrightarrow(R',S',N)
\]
over \((f,g)\) may be represented by a bimodule map
\[
R'\otimes_RM\otimes_SS'
\longrightarrow
N
\]
in \({}_{R'}\mathbf{Bimod}_{S'}\). By adjunction, it is equivalently an \((R,S)\)-bimodule map
\[
M\longrightarrow(f,g)^*N.
\]

A morphism is cocartesian precisely when the displayed map from the simultaneous extension of scalars to its target is an equivalence.

### Proposition 86.5 (Fibers of the bimodule total category) {#prop-bimodule-fibers}

For the point
\[
\iota_{R,S}:*\longrightarrow\mathbf{Ring}\times\mathbf{Ring},
\qquad
*\longmapsto(R,S),
\]
there are canonical equivalences
\[
*\times^h_{\mathbf{Ring}\times\mathbf{Ring}}
\int\mathbf{BiMod}_!
\simeq
{}_R\mathbf{Bimod}_S
\]
and
\[
*\times^h_{\mathbf{Ring}\times\mathbf{Ring}}
\int\mathbf{BiMod}^{*}
\simeq
{}_R\mathbf{Bimod}_S.
\]

***

# Part XX. Forgetting one action and the variance obstruction

## 87. Fiberwise forgetful functors

### Definition 87.1 (Forgetting the right or left action) {#def-forget-one-action}

For each pair \((R,S)\), define
\[
U_L^{R,S}:{}_R\mathbf{Bimod}_S
\longrightarrow
R\text{-}\mathbf{Mod}
\]
by forgetting the right \(S\)-action, and
\[
U_R^{R,S}:{}_R\mathbf{Bimod}_S
\longrightarrow
\mathbf{Mod}\text{-}S
=
S^{\mathrm{op}}\text{-}\mathbf{Mod}
\]
by forgetting the left \(R\)-action.

Equivalently, under Proposition 85.4 these are restriction-of-scalars functors along
\[
R\longrightarrow R\otimes S^{\mathrm{op}},
\qquad
r\longmapsto r\otimes1,
\]
and
\[
S^{\mathrm{op}}\longrightarrow R\otimes S^{\mathrm{op}},
\qquad
s^{\mathrm{op}}\longmapsto1\otimes s^{\mathrm{op}}.
\]

### Proposition 87.2 (The additive-group square) {#prop-additive-group-square}

The two composites to \(\mathbf{Ab}\) are canonically equivalent:
\[
\begin{CD}
{}_R\mathbf{Bimod}_S @>{U_L^{R,S}}>> R\text{-}\mathbf{Mod}\\
@V{U_R^{R,S}}VV @VV{U_{\mathrm{add}}^R}V\\
\mathbf{Mod}\text{-}S @>{U_{\mathrm{add}}^S}>> \mathbf{Ab}.
\end{CD}
\]
The comparison \(2\)-cell identifies both routes with the underlying abelian group of the bimodule.

This square does not by itself define bimodules: its homotopy pullback is \(\mathbf{BiAct}(R,S)\), and the commutation of the two actions remains an additional property as in Definition 85.3.

## 88. Naturality for restriction of scalars

### Theorem 88.1 (Forgetful transformations on the restriction side) {#thm-restriction-naturality}

Let
\[
p_1,p_2:\mathbf{Ring}\times\mathbf{Ring}\longrightarrow\mathbf{Ring}
\]
be the projections. The fiberwise forgetful functors assemble into natural transformations
\[
U_L^*:
\mathbf{BiMod}^{*}
\Longrightarrow
\mathbf{LMod}^{*}\circ p_1^{\mathrm{op}},
\]
\[
U_R^*:
\mathbf{BiMod}^{*}
\Longrightarrow
\mathbf{RMod}^{*}\circ p_2^{\mathrm{op}}.
\]

For \((f,g):(R,S)\to(R',S')\), the naturality equivalences are
\[
U_L^{R,S}\bigl((f,g)^*N\bigr)
\simeq
f^{*L}\bigl(U_L^{R',S'}N\bigr),
\]
\[
U_R^{R,S}\bigl((f,g)^*N\bigr)
\simeq
g^{*R}\bigl(U_R^{R',S'}N\bigr).
\]
They follow by forgetting one of the two restricted actions.

### Corollary 88.2 (Morphisms of cartesian fibrations) {#cor-cartesian-fibration-morphisms}

Under straightening--unstraightening, Theorem 88.1 yields cartesian-edge-preserving functors
\[
\int\mathbf{BiMod}^{*}
\longrightarrow
p_1^*\!\left(\int\mathbf{LMod}^{*}\right)
\]
and
\[
\int\mathbf{BiMod}^{*}
\longrightarrow
p_2^*\!\left(\int\mathbf{RMod}^{*}\right)
\]
over \(\mathbf{Ring}\times\mathbf{Ring}\). Composing with the base-change projections gives the familiar squares over \(p_1\) and \(p_2\).

Thus the strict \(2\)-morphism-level organization proposed for the forgetful projections is correct on the restriction-of-scalars side.

## 89. Failure of pseudonaturality for simultaneous extension

### Proposition 89.1 (The proposed covariant natural transformation does not exist) {#prop-extension-nonnaturality}

In general, the functors \(U_L^{R,S}\) do not assemble into a pseudonatural transformation
\[
\mathbf{BiMod}_!
\Longrightarrow
\mathbf{LMod}_!\circ p_1.
\]
Indeed, for \((f,g):(R,S)\to(R',S')\), the two relevant objects are
\[
f_!^L\bigl(U_L^{R,S}M\bigr)
=
R'\otimes_RM
\]
and
\[
U_L^{R',S'}\bigl((f,g)_!M\bigr)
=
R'\otimes_RM\otimes_SS'.
\]
They are not generally equivalent.

For example, take
\[
R=R'=S=\mathbb Z,
\qquad
S'=\mathbb Z/2,
\qquad
f=\operatorname{id},
\qquad
M=\mathbb Z.
\]
Then the first route gives \(\mathbb Z\), while the second gives \(\mathbb Z/2\).

The analogous claim for \(U_R\) also fails when the left ring is changed.

### Corollary 89.2 (No morphism of cocartesian fibrations) {#cor-no-cocartesian-morphism}

There is a functor on the total categories which forgets an action and lies over \(p_1\) or \(p_2\), but it does not preserve all cocartesian edges. Hence it is not a morphism of cocartesian fibrations and does not correspond to a natural transformation of the covariant straightened functors.

For an arrow \((\operatorname{id}_R,g)\), a cocartesian bimodule edge
\[
M\longrightarrow M\otimes_SS'
\]
would have to map to a cocartesian edge over the identity of \(R\). Such an edge must be an equivalence in the fiber \(R\text{-}\mathbf{Mod}\), which is false in general.

### Definition 89.3 (The covariant comparison cell) {#def-covariant-comparison-cell}

There is nevertheless a canonical comparison map
\[
f_!^LU_L^{R,S}(M)
\longrightarrow
U_L^{R',S'}(f,g)_!M,
\]
namely
\[
R'\otimes_RM
\longrightarrow
R'\otimes_RM\otimes_SS',
\qquad
x\longmapsto x\otimes1.
\]
Likewise,
\[
g_!^RU_R^{R,S}(M)
\longrightarrow
U_R^{R',S'}(f,g)_!M.
\]
These comparison maps are generally noninvertible. They define a lax or oplax transformation according to the selected convention; the displayed direction is the mathematical datum and should always be written explicitly.

### Proposition 89.4 (Mixed variance restores pseudonaturality) {#prop-mixed-variance}

There are mixed-variance functors
\[
\mathbf{BiMod}_{!,*}:
\mathbf{Ring}\times\mathbf{Ring}^{\mathrm{op}}
\longrightarrow
\mathbf{Cat}_\infty
\]
and
\[
\mathbf{BiMod}_{*,!}:
\mathbf{Ring}^{\mathrm{op}}\times\mathbf{Ring}
\longrightarrow
\mathbf{Cat}_\infty,
\]
where the first extends the left scalar and restricts the right scalar, while the second restricts the left scalar and extends the right scalar.

Then forgetting the right action is pseudonatural for \(\mathbf{BiMod}_{!,*}\), and forgetting the left action is pseudonatural for \(\mathbf{BiMod}_{*,!}\). This is the covariant formulation appropriate when one wishes to preserve one chosen module leg exactly.

***

# Part XXI. The unit ring, opposite rings, and diagonal bimodules

## 90. The monoidal unit \(\mathbb Z\)

### Theorem 90.1 (A \(\mathbb Z\)-action is unique) {#thm-z-action-unique}

For every abelian group \(M\), there is a unique unital right \(\mathbb Z\)-module structure, given by
\[
m\cdot n:=nm.
\]
Likewise there is a unique unital left \(\mathbb Z\)-module structure.

**Proof.** Unitality forces \(m\cdot1=m\). Additivity in the scalar then forces
\[
m\cdot n=m\cdot(1+\cdots+1)=nm
\]
for \(n\ge0\), and the negative integers are forced by additive inverses. \(\square\)

### Lemma 90.1.1 (Negation does not twist the integer action) {#lem-negation-no-twist}

The map
\[
\tau:\mathbb Z\longrightarrow\mathbb Z,
\qquad
\tau(n)=-n,
\]
is an automorphism of the underlying additive group, but it is not a ring homomorphism. Indeed,
\[
\tau(1)=-1\ne1
\]
under the unital convention, and even without invoking preservation of the unit,
\[
\tau(1\cdot1)=-1
\qquad\text{whereas}\qquad
\tau(1)\tau(1)=1.
\]
Consequently, precomposing a right \(\mathbb Z\)-action with \(\tau\) does not produce another module action. Explicitly, the proposed formula
\[
m\star n:=m\cdot(-n)
\]
violates the unit axiom, since \(m\star1=-m\) rather than \(m\). If \(-m=m\) for every \(m\), then the proposed action coincides with the canonical action and still does not give a distinct point of the structure space.

More generally, every ring endomorphism of \(\mathbb Z\) is the identity. This follows either from initiality of \(\mathbb Z\) in unital rings or directly from
\[
\varphi(n)=n\varphi(1)=n.
\]

### Proposition 90.1.2 (The fiber over a fixed left module) {#prop-z-action-fiber}

Let
\[
F:{}_R\mathbf{Bimod}_{\mathbb Z}\longrightarrow R\text{-}\mathbf{Mod}
\]
forget the right \(\mathbb Z\)-action. For a fixed left \(R\)-module \(M\), the strict fiber of \(F\) over \(M\) is the terminal category. Equivalently, its homotopy fiber is a contractible discrete space.

Indeed, a compatible right action on \(M\) is the same as a unital ring homomorphism
\[
\mathbb Z^{\mathrm{op}}
\longrightarrow
\operatorname{End}_R(M).
\]
Since \(\mathbb Z^{\mathrm{op}}=\mathbb Z\) is initial, this mapping set has exactly one element, namely
\[
n\longmapsto n\,\operatorname{id}_M.
\]
The forgetful functor is faithful, so the fiber has no nonidentity morphisms. Hence contractibility here is stronger than mere uniqueness up to unspecified equivalence: the action map itself is unique.

### Remark 90.1.3 (Contractibility versus strict uniqueness)

For a general classifier, a contractible homotopy fiber means that its objects form a nonempty space with a contractible space of coherent identifications; it need not mean that all raw presentations are definitionally equal. In the present case the fiber is \(0\)-truncated, because an action on a fixed module is ordinary algebraic data and the forgetful functor is faithful. A contractible \(0\)-truncated space is a singleton. Thus the general homotopical statement and the elementary uniqueness theorem agree exactly here.

### Corollary 90.2 (Modules as unit-ended bimodules) {#cor-unit-ended-bimodules}

There are canonical equivalences
\[
{}_R\mathbf{Bimod}_{\mathbb Z}
\simeq
R\text{-}\mathbf{Mod}
\]
and
\[
{}_{\mathbb Z}\mathbf{Bimod}_S
\simeq
\mathbf{Mod}\text{-}S
=
S^{\mathrm{op}}\text{-}\mathbf{Mod}.
\]
Equivalently, by Proposition 85.4,
\[
R\otimes\mathbb Z^{\mathrm{op}}\simeq R,
\qquad
\mathbb Z\otimes S^{\mathrm{op}}\simeq S^{\mathrm{op}}.
\]

Thus \((R,\mathbb Z)\)-bimodules may formally record a right \(\mathbb Z\)-action, but this field carries no additional mathematical choice: over each fixed left \(R\)-module the structure fiber is a singleton. The forgetful functor is therefore an equivalence, not merely a functor equipped with a preferred section.

### Proposition 90.3 (Initiality and the extension--restriction adjunction) {#prop-unit-extension-restriction}

Let \(\eta_S:\mathbb Z\to S\) be the unique unital ring homomorphism. Extension and restriction in the right scalar give an adjunction
\[
-\otimes_{\mathbb Z}S:
{}_R\mathbf{Bimod}_{\mathbb Z}
\rightleftarrows
{}_R\mathbf{Bimod}_S
:
\eta_S^*.
\]
Under Corollary 90.2, the right adjoint is precisely
\[
U_L^{R,S}:{}_R\mathbf{Bimod}_S\to R\text{-}\mathbf{Mod}.
\]
The left adjoint freely adjoins a right \(S\)-action:
\[
M\longmapsto M\otimes_{\mathbb Z}S.
\]

Similarly, forgetting the left \(R\)-action is restriction along \(\mathbb Z\to R\), and its left adjoint freely adjoins the left action.

### Remark 90.4 (The ordinary and spectral units must not be conflated)

The preceding equivalence is a theorem about ordinary unital rings and ordinary modules, regarded inside \(\mathbf{Cat}_\infty\) through their nerves. In a different symmetric monoidal \(\infty\)-category, the analogous statement uses the initial \(E_1\)-algebra, equivalently the monoidal unit under the standard hypotheses. For spectra this role is played by the sphere spectrum \(\mathbb S\), not by \(H\mathbb Z\). Thus one must not transfer the ordinary formula
\[
{}_R\mathbf{Bimod}_{\mathbb Z}\simeq R\text{-}\mathbf{Mod}
\]
verbatim to spectral algebra by replacing \(\mathbb Z\) with \(H\mathbb Z\). The correct unit-ended statement there is formulated with \(\mathbb S\).

## 91. Left modules versus right modules

### Proposition 91.1 (No side-changing functor from the opposite involution alone) {#prop-no-side-change}

The opposite-ring functor does not canonically define a functor
\[
R\text{-}\mathbf{Mod}
\longrightarrow
R^{\mathrm{op}}\text{-}\mathbf{Mod}.
\]
A chosen ring homomorphism
\[
\sigma:R\longrightarrow R^{\mathrm{op}}
\]
induces an extension-of-scalars functor
\[
\sigma_!:R\text{-}\mathbf{Mod}
\longrightarrow
R^{\mathrm{op}}\text{-}\mathbf{Mod}.
\]
Dually, a chosen ring homomorphism
\[
\tau:R^{\mathrm{op}}\longrightarrow R
\]
induces a restriction-of-scalars functor
\[
\tau^*:R\text{-}\mathbf{Mod}
\longrightarrow
R^{\mathrm{op}}\text{-}\mathbf{Mod}.
\]
Either datum is anti-multiplicative when regarded as a map on the underlying ring. If \(\sigma\) or \(\tau\) is an isomorphism, the induced side-changing functor is an equivalence. No such map is supplied merely by the existence of the object-level involution \(R\mapsto R^{\mathrm{op}}\).

### Corollary 91.2 (Commutative rings) {#cor-commutative-side-change}

If \(R\) is commutative, the identity map identifies \(R\simeq R^{\mathrm{op}}\), and there is a canonical equivalence
\[
R\text{-}\mathbf{Mod}
\simeq
R^{\mathrm{op}}\text{-}\mathbf{Mod}.
\]
This is the special case in which left and right module categories may be identified without naming additional data.

### Remark 91.3 (A ring homomorphism does not produce \(S\)-left-to-right conversion)

A homomorphism \(f:R\to S\) produces extension and restriction functors between the left module categories of \(R\) and \(S\), and separately between the right module categories. It does not produce a canonical functor
\[
S\text{-}\mathbf{Mod}
\longrightarrow
S^{\mathrm{op}}\text{-}\mathbf{Mod}.
\]
Such a functor again requires anti-multiplicative data on \(S\).

## 92. \((R,R)\)-bimodules

### Proposition 92.1 (An \((R,R)\)-bimodule is additional structure) {#prop-rr-bimodule-structure}

The forgetful functor
\[
U_L^{R,R}:{}_R\mathbf{Bimod}_R\to R\text{-}\mathbf{Mod}
\]
is not generally an equivalence. Its fiber over a left module \(M\) is the moduli of right \(R\)-actions on \(M\) commuting with the left action. In ordinary algebra, such an action is equivalently a ring homomorphism
\[
R^{\mathrm{op}}
\longrightarrow
\operatorname{End}_R(M).
\]

### Definition 92.2 (Central bimodule over a commutative ring) {#def-central-bimodule}

Suppose \(R\) is commutative. An \((R,R)\)-bimodule \(M\) is **central** if
\[
rm=mr
\qquad
(r\in R,\ m\in M).
\]
Every left \(R\)-module has a canonical central bimodule structure by setting \(mr:=rm\). This defines a fully faithful functor
\[
c_R:R\text{-}\mathbf{Mod}
\longrightarrow
{}_R\mathbf{Bimod}_R
\]
whose essential image is the central bimodules. It is a section of \(U_L^{R,R}\); after the canonical equivalence between left and right modules for commutative \(R\), it also supplies a section of \(U_R^{R,R}\). It is not essentially surjective onto all \((R,R)\)-bimodules.

***

# Part XXII. The Morita \((\infty,2)\)-category

## 93. Rings and bimodules as a higher category

### Definition 93.1 (Morita \((\infty,2)\)-category) {#def-morita-category}

Let \(\mathbf{Mor}_{\mathbb Z}\) denote the Morita \((\infty,2)\)-category of associative unital rings. Its:

1. objects are rings;
2. \(1\)-morphisms \(S\to R\) are \((R,S)\)-bimodules;
3. \(2\)-morphisms are bimodule homomorphisms, with their higher homotopies in the derived or spectral setting;
4. composition is relative tensor product:
   \[
   {}_R M_S\circ{}_S N_T
   :=
   {}_R(M\otimes_SN)_T;
   \]
5. identity \(1\)-morphism of \(R\) is the regular bimodule \({}_RR_R\).

With this orientation,
\[
\operatorname{Map}_{\mathbf{Mor}_{\mathbb Z}}(S,R)
\simeq
{}_R\mathbf{Bimod}_S.
\]

Associativity and unitality hold up to the standard coherent equivalences of relative tensor product. Haugseng's higher Morita construction gives the corresponding \((\infty,2)\)-category for \(E_1\)-algebras in a monoidal \(\infty\)-category.

### Proposition 93.2 (Module categories as hom categories from the unit) {#prop-modules-as-homs}

The monoidal unit is \(\mathbb Z\). Corollary 90.2 becomes
\[
R\text{-}\mathbf{Mod}
\simeq
\operatorname{Map}_{\mathbf{Mor}_{\mathbb Z}}(\mathbb Z,R),
\]
\[
\mathbf{Mod}\text{-}R
\simeq
\operatorname{Map}_{\mathbf{Mor}_{\mathbb Z}}(R,\mathbb Z).
\]
Thus left and right module categories are not unrelated families attached externally to rings. They are the incoming and outgoing hom \(\infty\)-categories at the monoidal unit in the Morita \((\infty,2)\)-category.

## 94. Ring homomorphisms as companion and conjoint bimodules

### Definition 94.1 (The two bimodules attached to a ring map) {#def-companion-conjoint}

Let \(f:R\to S\). Define
\[
{}_SS_R
\]
using the regular left \(S\)-action and right \(R\)-action through \(f\), and define
\[
{}_RS_S
\]
using the left \(R\)-action through \(f\) and regular right \(S\)-action.

In \(\mathbf{Mor}_{\mathbb Z}\), these are \(1\)-morphisms
\[
F_f:R\longrightarrow S,
\qquad
G_f:S\longrightarrow R.
\]

### Proposition 94.2 (Adjunction in the Morita category) {#prop-morita-adjunction}

There is an adjunction
\[
F_f\dashv G_f.
\]
The unit is the bimodule map
\[
{}_RR_R
\longrightarrow
{}_RS_S\otimes_S{}_SS_R
\simeq
{}_RS_R
\]
induced by \(f\), and the counit is multiplication
\[
{}_SS_R\otimes_R{}_RS_S
\simeq
{}_S(S\otimes_RS)_S
\longrightarrow
{}_SS_S.
\]
The triangle identities are the associativity and unitality identities for tensor product and multiplication.

### Corollary 94.3 (Extension and restriction from Morita composition) {#cor-scalar-change-morita}

Postcomposition on hom categories from \(\mathbb Z\) gives
\[
R\text{-}\mathbf{Mod}
\longrightarrow
S\text{-}\mathbf{Mod},
\qquad
M\longmapsto{}_SS_R\otimes_RM,
\]
which is extension of scalars.

Postcomposition with \(G_f\) gives
\[
S\text{-}\mathbf{Mod}
\longrightarrow
R\text{-}\mathbf{Mod},
\qquad
N\longmapsto{}_RS_S\otimes_SN,
\]
which is restriction of scalars. The unit and counit \(2\)-morphisms of Proposition 94.2 induce the ordinary extension--restriction adjunction.

The analogous statement on hom categories into \(\mathbb Z\) gives scalar change for right modules.

### Remark 94.4 (The relevant triangles)

The triangles associated to a ring homomorphism are not triangles
\[
{}_R\mathbf{Bimod}_S,
\quad
R\text{-}\mathbf{Mod},
\quad
S\text{-}\mathbf{Mod}
\]
connected by a hypothetical left-to-right conversion. They are the adjunction triangles of the companion and conjoint bimodules \({}_SS_R\) and \({}_RS_S\) in the Morita \((\infty,2)\)-category. Their fillers are the unit and counit bimodule maps.

## 95. Relation to the bifunctorial Grothendieck construction

### Remark 95.1 (Two complementary organizations)

There are two related but distinct mathematical organizations.

1. The functor
   \[
   \mathbf{BiMod}_!:\mathbf{Ring}\times\mathbf{Ring}\to\mathbf{Cat}_\infty
   \]
   organizes **base change of both endpoint rings** and unstraightens to a cocartesian fibration.
2. The Morita \((\infty,2)\)-category organizes bimodules as **morphisms between rings**, with relative tensor product as composition.

The first records how hom categories vary under ring homomorphisms. The second records the composition law internal to the collection of rings and bimodules. Neither replaces the other.

### Remark 95.2 (Hom bifunctor and variance)

The genuine hom bifunctor of the Morita category is
\[
\operatorname{Map}_{\mathbf{Mor}_{\mathbb Z}}(-,-):
\mathbf{Mor}_{\mathbb Z}^{\mathrm{op}}\times
\mathbf{Mor}_{\mathbb Z}
\longrightarrow
\mathbf{Cat}_\infty.
\]
Our notation satisfies
\[
{}_R\mathbf{Bimod}_S
\simeq
\operatorname{Map}_{\mathbf{Mor}_{\mathbb Z}}(S,R).
\]
This contravariant--covariant variance is the intrinsic variance of a hom object. The separately defined covariant functor \(\mathbf{BiMod}_!\) is a base-change construction obtained from extension of scalars in both endpoint rings.

### Theorem 95.3 (Correct form of the proposed \(2\)-morphism principle) {#thm-two-morphism-principle}

Most of the module and bimodule diagrammatics are indeed generated at the level of higher morphisms, provided the variance is fixed correctly:

1. restriction-of-scalars gives natural transformations
   \[
   U_L^*,U_R^*
   \]
   and therefore morphisms of cartesian fibrations;
2. simultaneous extension gives noninvertible comparison \(2\)-cells, hence lax or oplax transformations rather than pseudonatural transformations;
3. the equality of the two underlying additive groups is an invertible \(2\)-cell;
4. a ring map gives companion and conjoint bimodules, whose unit and counit are \(2\)-morphisms in the Morita category;
5. after unstraightening and pullback along points, these global higher morphisms recover the familiar fiberwise forgetful functors, scalar-change functors, and adjunctions.

Thus the proposed organizing principle is correct after replacing the undifferentiated phrase “a \(2\)-morphism between \(\mathbf{BiMod}\) and \(\mathbf{Mod}\)” by the exact one of:

- a pseudonatural transformation with restriction variance;
- a lax comparison with extension variance;
- a morphism of cartesian or cocartesian fibrations, with preservation of the distinguished edges stated;
- or a \(2\)-morphism in the Morita \((\infty,2)\)-category.

***

# Part XXIII. Derived and spectral form

## 96. Relative tensor products in a monoidal \(\infty\)-category

### Definition 96.1 (General ambient) {#def-morita-general-ambient}

Let \(\mathcal V\) be a presentable symmetric monoidal \(\infty\)-category whose tensor product preserves colimits separately in each variable. Replace ordinary rings by \(E_1\)-algebras in \(\mathcal V\). For \(A,B\in\operatorname{Alg}_{E_1}(\mathcal V)\), let
\[
{}_A\mathbf{Bimod}_B(\mathcal V)
\]
be the \(\infty\)-category of \((A,B)\)-bimodule objects.

Relative tensor product gives composition, and the resulting higher Morita category has the same formal structure as Part XXII.

### Example 96.2 (Ordinary and spectral rings)

- For \(\mathcal V=\mathbf{Ab}\), one recovers ordinary rings and ordinary bimodules.
- For \(\mathcal V=\mathbf{Sp}\), one obtains \(E_1\)-ring spectra and module spectra.
- The Eilenberg--Mac Lane functor sends an ordinary ring \(R\) to \(HR\) and identifies the derived \(\infty\)-category of \(R\)-modules with the appropriate module \(\infty\)-category over \(HR\).

### Remark 96.3 (Derived scalar change)

All tensor products in the derived or spectral setting are relative tensor products in the ambient \(\infty\)-category. No separate projective-resolution choice appears in the intrinsic definition. Chain complexes and resolutions are presentations used to compute these relative tensor products.

***

# Concluding formulation

The mathematical foundation can be summarized without reference to any implementation.
There is one universe of higher categories.  Additional data and axioms are represented by
classifying morphisms; membership is a lift; simultaneous structure is a homotopy limit;
operations are arrow-category pullbacks; equations and coherence are extension problems for
operation-built diagrams; interacting coherences are governed by operadic matching objects.
Algebraic, arithmetic, geometric, and computational objects are obtained by applying these
constructions at the lowest level where their defining data exist.

Bilinear forms are \(W\)-valued forms, lattices are finite-projective arithmetic forms,
discriminants sit in the radical--dual exact sequence, and automorphism groups are values of
the generic automorphism construction.  Schemes, stacks, quotient stacks, quasi-coherent
algebras, deformation groupoids, cones, fans, reflection arrangements, period domains, and
compactifications occupy their standard categorical homes.  The Sage category system is a
separate diagram mapped into this universe and compared by equivalence theorems.  A
mathematical computation is an evaluation of a functor, invariant, lift, or section already
present in the same diagram.

This is the complete ontology presently supported by the conversations.  Further research
should extend it by standard mathematical definitions and comparison theorems, not by adding
a second informal taxonomy beside it.

The presentation calculus of Parts XIV--XVII fixes the corrected hierarchy
\[
\boxed{
\begin{gathered}
\text{root realization}
\longrightarrow
\text{intrinsic root lattice}
\longrightarrow
\text{chosen root basis}
\longrightarrow
\text{Gram matrix},
\\[2mm]
\text{root--coroot pairing}
\longrightarrow
\text{Cartan matrix},
\\[2mm]
\text{chosen free presentation}
\longrightarrow
\text{matrix lifts}
\longrightarrow
\text{descent modulo relations}
\longrightarrow
\text{abstract morphism},
\\[2mm]
\text{chosen projective resolution}
\longrightarrow
\text{matrix chain maps}
\longrightarrow
\text{chain homotopy class}
\longrightarrow
\text{derived morphism}.
\end{gathered}
}
\]

Every arrow forgets data or applies a comparison theorem.  No object on the right is
substituted definitionally for the object on its left.

The module and bimodule geometry of Parts XVIII--XXIII fixes the corrected hierarchy
\[
\boxed{
\begin{gathered}
\mathbf{Ring}
\xrightarrow{\mathbf{LMod}_!,\,\mathbf{RMod}_!}
\mathbf{Cat}_\infty,
\qquad
\mathbf{Ring}^{\mathrm{op}}
\xrightarrow{\mathbf{LMod}^{*},\,\mathbf{RMod}^{*}}
\mathbf{Cat}_\infty,
\\[2mm]
\mathbf{Ring}\times\mathbf{Ring}
\xrightarrow{\mathbf{BiMod}_!}
\mathbf{Cat}_\infty,
\qquad
(\mathbf{Ring}\times\mathbf{Ring})^{\mathrm{op}}
\xrightarrow{\mathbf{BiMod}^{*}}
\mathbf{Cat}_\infty,
\\[2mm]
\text{unstraightening}
\Longrightarrow
\text{cocartesian or cartesian total categories},
\qquad
\text{point pullback}
\Longrightarrow
\text{fixed-ring fibers},
\\[2mm]
{}_R\mathbf{Bimod}_S
\longrightarrow
R\text{-}\mathbf{Mod}
\times^h_{\mathbf{Ab}}
S^{\mathrm{op}}\text{-}\mathbf{Mod}
\quad
\text{with commuting actions imposed},
\\[2mm]
R\text{-}\mathbf{Mod}
\simeq
\operatorname{Map}_{\mathbf{Mor}_{\mathbb Z}}(\mathbb Z,R),
\qquad
S^{\mathrm{op}}\text{-}\mathbf{Mod}
\simeq
\operatorname{Map}_{\mathbf{Mor}_{\mathbb Z}}(S,\mathbb Z),
\\[2mm]
{}_R\mathbf{Bimod}_S
\simeq
\operatorname{Map}_{\mathbf{Mor}_{\mathbb Z}}(S,R).
\end{gathered}
}
\]

The Grothendieck-construction picture controls variation in the endpoint rings.  The Morita
picture controls composition of bimodules.  The natural transformations between the
corresponding functors, together with the unit and counit \(2\)-morphisms attached to ring
homomorphisms, generate the required module and bimodule diagrams without identifying
mathematically distinct categories.
