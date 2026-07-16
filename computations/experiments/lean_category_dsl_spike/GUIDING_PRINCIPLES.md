Lean 4's elaborator infrastructure is sufficient for this proof of concept.
No Lean fork, kernel change, or parser change is required.

The correct architecture is:

$$
\boxed{
\text{paper-like categorical syntax}
\longrightarrow
\text{typed categorical intermediate representation}
\longrightarrow
\text{Lean declarations and proof terms}
}
$$

Lean supplies parsing hooks, command and term elaborators, persistent environment extensions, Unicode notation, generated declarations, proof holes, and the final kernel check.
Custom command elaborators may add constants and extend compile-time tables, while environment extensions can persist the category graph and associated metadata across modules.
([Lean Language][1])

There are, however, three corrections needed.
The first two are mathematical errors in the toy example; the third is a correction to the vocabulary, which generalizes.

First, an arbitrary function

$$
X\longrightarrow \mathbb N
$$

does not witness countability: every nonempty set has a constant map to $\mathbb N$.
What is required is at least an injective numbering.
For an executable "nth element" interface, the appropriate data are

$$
\operatorname{number}_X:X\longrightarrow\mathbb N,
\qquad
\operatorname{nth}_X:\mathbb N\rightharpoonup X,
$$

with

$$
\operatorname{nth}_X(\operatorname{number}_X(x))=x.
$$

This equation implies that `number` is injective.
Mathlib's `Encodable` interface is almost exactly this: it supplies explicit encode and partial decode operations with inverse laws.
([Lean Community][2])

Second, there is no functor

$$
\operatorname{Mod}_R\longrightarrow \operatorname{Ring}
$$

**over $\mathbf{Set}$**: none commuting with the two $\mathbf{Set}$-realizations.
A module carries no multiplication and no multiplicative identity, so its own underlying set cannot be equipped with a ring structure naturally in $M$.

State it that way or not at all.
The unqualified claim — that no functor $\operatorname{Mod}_R\to\operatorname{Ring}$ exists — is simply false, and the counterexamples are not exotic.
The constant functor $M\mapsto R$, $f\mapsto\operatorname{id}_R$ is one.
The symmetric and tensor algebras

$$
\operatorname{Sym},\ T\ :\ \operatorname{Mod}_R\longrightarrow\operatorname{Ring}
$$

are non-trivial ones, and are canonical rather than pathological: they are left adjoint to the forgetful functors running the other way.
What no such functor does is preserve the underlying set, and preserving it is exactly what the $\mathbf F_2^2\cong\mathbf F_2\times\mathbf F_2$ comparison requires.

The honest way to reach a ring is therefore to *start* in a category whose objects already have one.
$\operatorname{CAlg}(R)\to\operatorname{Ring}$ is a genuine forgetful functor over $\mathbf{Set}$, because an $R$-algebra carries a ring structure by definition and its morphisms are ring maps.
§14 takes precisely this route.

The correct general path is

$$
\operatorname{Lat}_R
\longrightarrow
\operatorname{FreeFinMod}_R
\longrightarrow
\operatorname{Mod}_R
\longrightarrow
\operatorname{Set}.
$$

For the particular standard module $\mathbf F_2^2$, its chosen basis identifies its $\mathbf{Set}$-realization with the product of two copies of the $\mathbf{Set}$-realization of the ring $\mathbf F_2$.
If one specifically wants the ring $\mathbf F_2\times\mathbf F_2$, it should be constructed first as a product ring or $\mathbf F_2$-algebra and then realized both in modules and in sets.
That gives two compatible routes; it does not produce a module-to-ring functor.

Third, the vocabulary itself needs a correction, and the correction generalizes.

## 0. Realization

Say that an object "has an underlying set" and you have already made the error: you have named a *relationship* as though it were an attribute the object stores.
A lattice does not have an underlying module.
There is a functor

$$
\pi_R:\operatorname{Lat}(R)\longrightarrow\operatorname{FreeFinMod}(R),
\qquad
(L,b)\longmapsto L,
$$

and the module is its value.
The relationship is the functor; nothing is stored.

The general definition is modelled on geometric realization.
In $\infty$-category theory the functor

$$
|-|:\mathbf{Cat}_\infty\longrightarrow\mathbf{Spaces}
$$

is left adjoint to the fully faithful inclusion $\iota:\mathbf{Spaces}\hookrightarrow\mathbf{Cat}_\infty$; its counit is an equivalence, exhibiting $\mathbf{Spaces}$ as a reflective localization of $\mathbf{Cat}_\infty$, and it is cocontinuous and preserves finite products.

Generalizing the name rather than the axioms: fix a category $\mathcal C$.
A functor

$$
F:\mathcal C\longrightarrow\mathcal D
$$

is a **$\mathcal D$-realization functor** when it satisfies a set of properties **left undetermined here** — provisionally, any functor.
For $X\in\mathcal C$ write

$$
|X|_{\mathcal D}:=F(X)
$$

and call it the **$\mathcal D$-realization of $X$**.

This composes, which is the point.
Lattices have $\operatorname{Mod}(R)$-realizations; those have $\mathbf{Set}$-realizations; and $|X|_{\mathcal D}$ for a reachable $\mathcal D$ is exactly what the preferred-functor path resolver of §4 computes.
The word "underlying" then never needs to appear: every use of it was naming some $|X|_{\mathcal D}$ without saying which $\mathcal D$.

### Which properties?

The name is adopted now; the axioms are not.
But the candidates can be narrowed, because the examples already discriminate between them.

**Not a monomorphism.** The tempting reading is that $\operatorname{Mod}(R)\to\mathbf{Set}$ exhibits $\operatorname{Mod}(R)$ as a subcategory, so that $|M|_{\mathbf{Set}}$ is an image under a mono in $\mathbf{Cat}_\infty$.
This is too strong and fails for that very functor: a mono in $\mathbf{Cat}_\infty$ is fully faithful, and $\operatorname{Mod}(R)\to\mathbf{Set}$ is not full — most functions between modules are not linear.

**Not adjointness of either handedness.** $\operatorname{Ring}\to\mathbf{Set}$ is a right adjoint ($\text{Free}\dashv\text{Forget}$), so the algebraic examples suggest right-adjointness.
But $U_{\mathrm{count}}:\mathbf{CountableSet}\to\mathbf{Set}$ has no left adjoint at all — a free countable set on an uncountable $X$ would require $|FX|\cong X$ — so it is not a right adjoint, and the axiom is not uniform.
(Left and right adjointness are not exclusive: $\iota:\mathbf{Spaces}\hookrightarrow\mathbf{Cat}_\infty$ is both, sitting in $|-|\dashv\iota\dashv\operatorname{Core}$.
The objection is uniformity, not exclusivity.)

**Faithfulness is uniform.** Every realization functor named in this document is faithful:

| functor |  |
| --- | --- |
| $U_{\mathrm{count}},\ U_{\mathrm{fin}},\ \iota_{\mathrm{fc}}$ | fully faithful — §5 defines morphisms as *all* functions on both sides |
| $\operatorname{FreeFinMod}(R)\to\operatorname{Mod}(R)$ | fully faithful |
| $\operatorname{Ring}\to\mathbf{Set}$, $\operatorname{Mod}(R)\to\mathbf{Set}$, $U_R^{\mathrm{fin}}$ | faithful, not full |
| $\pi_R:\operatorname{Lat}(R)\to\operatorname{FreeFinMod}(R)$ | faithful — a lattice morphism is determined by its linear map |

A functor $U:\mathcal C\to\mathcal D$ that is faithful is exactly what makes $\mathcal C$ **concrete over $\mathcal D$** in the classical sense.
This is the natural candidate axiom: uniform across the examples, classical, and it delivers the subcategory-flavoured intuition without overclaiming a mono.

It also sharpens §5's design decision.
Because morphisms of $\mathbf{CountableSet}$ are all functions and need not preserve the enumeration, $U_{\mathrm{count}}$ is *fully* faithful and any two enumerations of $X$ are isomorphic; hence $\mathbf{CountableSet}$ is equivalent to the full subcategory of countable sets.
There the subcategory reading is literally correct.
For $\operatorname{Mod}(R)$ it never is.
That asymmetry is real and should not be smoothed over.

**The cost of the name.** $|-|$ itself is not faithful: it is a localization, it inverts morphisms, and naturally isomorphic functors induce homotopic maps.
So under a faithfulness axiom, geometric realization is not a realization functor.
Forgetting structure faithfully and inverting morphisms are different operations that share a target.
The notation is borrowed deliberately; the axioms must come from the examples, not from $|-|$.

Note also that §7 already relies on $\operatorname{Core}$ — the right adjoint in $|-|\dashv\iota\dashv\operatorname{Core}$ — for cardinality, not on $|-|$.

## 1. How to host the language in Lean

The first implementation should use one custom top-level command:

```text
mathematics FiniteLattices where
    ...
```

Its body belongs to custom syntax categories such as:

```lean
declare_syntax_cat mathTerm
declare_syntax_cat mathFormula
declare_syntax_cat mathStatement
```

Representative grammar productions would include:

```lean
syntax ident : mathTerm
syntax:70 mathTerm " × " mathTerm : mathTerm
syntax:70 mathTerm " ⊗ " mathTerm : mathTerm
syntax "∏" "[" ident " ∈ " mathTerm "]" mathTerm : mathTerm
syntax "{" ident " ∈ " mathTerm " | " mathFormula "}" : mathTerm
syntax "Hom_" mathTerm "(" mathTerm "," mathTerm ")" : mathTerm

syntax "let " ident " ∈ " mathTerm "." : mathStatement
syntax "let " ident " := " mathTerm " ∈ " mathTerm "." : mathStatement
syntax "assume " mathFormula "." : mathStatement
syntax "theorem " ident ":" mathFormula "." : mathStatement
```

Lean elaborators are registered only at the outer `command`, `term`, or `tactic` level, but this is not a limitation.
The `mathematics` command elaborator receives the complete nested mathematical syntax tree and invokes a separate `MathElabM` implementation on it.
Lean explicitly supports nested syntax and recursive elaboration of nested commands and terms.
([Lean Language][1])

The parser need not know which identifiers denote categories, functors, or objects.
It parses all identifiers uniformly.
Those distinctions are determined during semantic elaboration.

A standalone `.cat` file format would require only a trivial frontend that implicitly wraps the file in a `mathematics ... where` command.
This is not an extension to Lean's logic or elaborator API.

## 2. The proof-of-concept semantic backend

For the first implementation, the higher-facing interface should be backed by Mathlib's ordinary category theory.

Mathlib already provides:

* a bundled category `CategoryTheory.Cat`;

* categories as objects of `Cat`;

* functors as $1$-morphisms between those objects;

* categories of functors whose morphisms are natural transformations;

* hom-categories between objects of `Cat`, with natural transformations as $2$-morphisms.
  ([Lean Community][3])

Thus the proof-of-concept can support:

```text
let 𝒞 ∈ Cat.
let A ∈ 𝒞.
let F ∈ Fun(𝒞,𝒟).
let η ∈ Hom_{Fun(𝒞,𝒟)}(F,G).
```

without inventing a parallel category implementation.

The source-level higher-facing foundation should expose:

$$
\mathbf{Cat},\qquad
\mathbf{Space},\qquad
\mathbf{Set},\qquad
\operatorname{Maps}_{\mathcal C}(A,B),\qquad
\operatorname{Fun}(\mathcal C,\mathcal D),\qquad
\pi_0.
$$

The source notation

$$
\operatorname{Hom}_{\mathcal C}(A,B)
$$

always elaborates to

$$
\operatorname{Maps}_{\mathcal C}(A,B)\in\mathbf{Space}.
$$

For the Sage-like categories in the proof-of-concept, mapping spaces are marked locally $0$-truncated and implemented as discrete spaces on Mathlib hom-types.
Therefore implicit $\pi_0$ is harmless in this fragment.
Nothing in the source-level API should hard-code that all future mapping spaces are sets.

Universe indices remain internal:

$$
\mathbf{Cat}_u\in\mathbf{Cat}_{u+1}.
$$

The user sees `Cat`, while the universe elaborator inserts the required levels.

## 3. The persistent categorical registry

A `PersistentEnvExtension` should store the mathematical index used by the elaborator.
Lean environment extensions are designed for exactly this sort of compile-time table.
([Lean Language][4])

The registry should contain entries of the following forms.

```text
CategoryNode
    Lean declaration
    universe level
    locally-0-truncated marker

ObjectNode
    Lean declaration
    category of definition

FunctorEdge
    Lean declaration
    source category
    target category
    preferred flag
    path priority

ViewCoherence
    two functor paths
    natural isomorphism between them

ObjectConstructor
    input categories
    output category
    generated obligations

LiftRule
    base functor or construction
    lifted functor
    coherence with realization projections

Claim
    Lean declaration
    status: proved / sorry / axiom / assumed
```

The registry is an elaboration index.
It is not a second proof system.
Every mathematical entry points to an actual Lean declaration.

## 4. Membership and preferred functors

Each named object $A$ has a category of definition, denoted $\operatorname{home}(A)$.

The judgment

$$
A\in\mathcal C
$$

holds precisely when the preferred-functor graph contains a directed path

$$
\operatorname{home}(A)\rightsquigarrow\mathcal C.
$$

If

$$
p=
\left(
\mathcal C_0
\xrightarrow{F_1}
\mathcal C_1
\xrightarrow{F_2}
\cdots
\xrightarrow{F_n}
\mathcal C_n
\right),
$$

then the corresponding Lean object is

$$
F_n\bigl(\cdots F_2(F_1(A))\cdots\bigr).
$$

Multiple paths do not make membership ambiguous.
Membership is existential reachability.
The compiler chooses one path deterministically for term generation and records it.

Queries should expose this:

```text
#via Λ ∈ Set.
```

with output such as:

```text
Lat(R) ─π_R→ FreeFinMod(R) ─U_R^fin→ FiniteSet
       ─ι_fc→ CountableSet ─U_count→ Set
```

A specific path can be requested explicitly:

```text
Λ as Set via π_R ; U_R^fin ; ι_fc ; U_count
```

A natural isomorphism between two paths is needed only when a construction must compare their outputs.
It is not needed merely to establish `Λ ∈ Set`.

## 5. Obligations should be structured categories

The clean categorical formulation of "objects in this category must provide an implementation" is a structured or displayed category over a base category.

### Countable sets

Define the category `CountableSet` by:

$$
\operatorname{Ob}(\mathbf{CountableSet})
=
\left\{
(X,\nu,\delta)\ \middle|
\begin{array}{l}
X\in\mathbf{Set},\
\nu:X\to\mathbb N,\
\delta:\mathbb N\rightharpoonup X,\
\delta(\nu(x))=x\quad\forall x\in X
\end{array}
\right\}.
$$

Morphisms are all functions between the $\mathbf{Set}$-realizations.
They need not preserve the chosen enumeration.

There is a preferred projection

$$
U_{\mathrm{count}}:
\mathbf{CountableSet}\rightsquigarrow\mathbf{Set},
\qquad
(X,\nu,\delta)\longmapsto X.
$$

The requested "nth element obligation" is now honest data on an object of `CountableSet`.

To supply countability for a $\mathbf{Set}$-realization functor

$$
U:\mathcal C\to\mathbf{Set}
$$

means giving a lift

$$
\widetilde U:\mathcal C\to\mathbf{CountableSet}
$$

together with a specified natural isomorphism

$$
U_{\mathrm{count}}\circ\widetilde U
\cong
U.
$$

This is the exact categorical meaning of implementing the obligation.

### Finite sets

Define

$$
\operatorname{Ob}(\mathbf{FiniteSet})
=
\left\{
(X,n,e)
\ \middle|
X\in\mathbf{Set},
n\in\mathbb N,
e:X\overset{\sim}{\longrightarrow}[n]
\right\},
$$

where

$$
[n]=\{0,1,\ldots,n-1\}.
$$

Again, morphisms are all functions of $\mathbf{Set}$-realizations.

The equivalence $e$ produces:

$$
\operatorname{number}_X(x)=e(x),
$$

and

$$
\operatorname{nth}_X(k)=
\begin{cases}
e^{-1}(k),&k<n,\
\text{undefined},&k\geq n.
\end{cases}
$$

Hence there is a preferred functor

$$
\iota_{\mathrm{fc}}:
\mathbf{FiniteSet}\rightsquigarrow\mathbf{CountableSet}.
$$

There is also a preferred projection

$$
U_{\mathrm{fin}}:
\mathbf{FiniteSet}\rightsquigarrow\mathbf{Set}.
$$

The surface notation

```text
FiniteSet ↝ CountableSet ↝ Set
```

therefore means actual functors, not an informal class hierarchy.

## 6. Products of finite sets

The product operation in `Set` is a functor

$$
\times:
\mathbf{Set}\times\mathbf{Set}\longrightarrow\mathbf{Set}.
$$

The standard library should provide a lifted functor

$$
\widetilde{\times}:
\mathbf{FiniteSet}\times\mathbf{FiniteSet}
\longrightarrow
\mathbf{FiniteSet}
$$

whose $\mathbf{Set}$-realization is the Cartesian product.

Suppose

$$
X\simeq[m],
\qquad
Y\simeq[n].
$$

Use the standard mixed-radix equivalence

$$
[m]\times[n]\overset{\sim}{\longrightarrow}[mn],
\qquad
(i,j)\longmapsto ni+j.
$$

Thus:

$$
|X\times Y|=|X|\cdot|Y|,
$$

and, when $n>0$,

$$
\operatorname{number}_{X\times Y}(z)
=
n\operatorname{number}_X(\pi_1z)
+
\operatorname{number}_Y(\pi_2z).
$$

Injectivity follows because reducing modulo $n$ recovers the second coordinate and integer division by $n$ recovers the first.
When $n=0$, $Y$ and hence $X\times Y$ are empty, so the encoding condition is vacuous.

The partial inverse is:

$$
\operatorname{nth}_{X\times Y}(k)
=
\left(
\operatorname{nth}_X(\lfloor k/n\rfloor),
\operatorname{nth}_Y(k\bmod n)
\right)
$$

for $k<mn$, with the $n=0$ case treated as nowhere defined.

The Lean implementation should package these operations and prove the inverse laws once.
Every subsequent product object then satisfies the countability obligation by functor composition.

## 7. Cardinality

The foundational cardinality invariant should remain categorical:

$$
\#:\operatorname{Core}(\mathbf{Set})
\longrightarrow
\mathbf{Card}.
$$

For the executable finite fragment, also provide:

$$
\operatorname{size}:
\operatorname{Core}(\mathbf{FiniteSet})
\longrightarrow
\mathbb N_{\mathrm{disc}},
\qquad
(X,n,e)\longmapsto n.
$$

The standard library records the comparison

$$
\#(U_{\mathrm{fin}}X)
=
\operatorname{size}(X)
$$

after embedding natural numbers into cardinals, and the product law

$$
\operatorname{size}(X\times Y)
=
\operatorname{size}(X)\operatorname{size}(Y).
$$

The surface notation `|X|` uses the most informative reachable implementation:

* if $X\in\mathbf{FiniteSet}$, use `size`;

* otherwise use the general cardinality functor after passing to the core;

* if only an external implementation is available, invoke the boundary adapter.

This is not an informal observation.
Each law is a Lean proposition backed by a theorem, an assumption, an axiom, or `sorry`.

## 8. Algebraic categories in the proof of concept

The algebraic slice should contain at least:

$$
\mathbf{CRing},\quad
\mathbf{FiniteCRing},\quad
\operatorname{Mod}(R),\quad
\operatorname{FreeFinMod}(R),\quad
\operatorname{Lat}(R).
$$

Mathlib already supplies bundled ring categories, module categories, concrete forgetful functors, and limit constructions.
`ModuleCat R` is the bundled category of $R$-modules; it has all limits, with the forgetful functor preserving them.
Mathlib also supplies `RingCat`, `CommRingCat`, and the corresponding forgetful functors.
([Lean Community][5])

### Finite commutative rings

Define `FiniteCRing` as the structured pullback of the $\mathbf{Set}$-realization functor and the finite-set projection:

$$
\begin{CD}
\mathbf{FiniteCRing} @>{U_{\mathrm{finring}}}>>
\mathbf{FiniteSet}\
@V{\iota_{\mathrm{ring}}}VV
@VV{U_{\mathrm{fin}}}V\
\mathbf{CRing}
@>{U_{\mathrm{ring}}}>>
\mathbf{Set}.
\end{CD}
$$

An object consists of:

1. a commutative ring $R$;

2. a chosen finite set;

3. an identification of that finite set with $|R|_{\mathbf{Set}}$.

Both projections are preferred.

### Finite free modules

A mere proposition that $M$ is finite free is not sufficient to compute an enumeration.
A chosen finite basis is required.

Define:

$$
\operatorname{FreeFinMod}(R)
=
\left\{
(M,n,\beta)
\ \middle|
\begin{array}{l}
M\in\operatorname{Mod}(R),\
n\in\mathbb N,\
\beta:R^n\overset{\sim}{\longrightarrow}M
\text{ in }\operatorname{Mod}(R)
\end{array}
\right\}.
$$

Morphisms may be all $R$-linear maps; they need not preserve the chosen basis.

There is a preferred functor

$$
\iota_R:
\operatorname{FreeFinMod}(R)
\rightsquigarrow
\operatorname{Mod}(R),
\qquad
(M,n,\beta)\longmapsto M.
$$

If $R\in\mathbf{FiniteCRing}$, its finite-set realization produces a preferred lift

$$
U_R^{\mathrm{fin}}:
\operatorname{FreeFinMod}(R)
\rightsquigarrow
\mathbf{FiniteSet}.
$$

On an object $(M,n,\beta)$, use $\beta$ to transport the finite-set structure on $R^n$ to $M$.
Consequently:

$$
|M|=|R|^n.
$$

There should be a registered coherence isomorphism

$$
U_{\mathrm{fin}}\circ U_R^{\mathrm{fin}}
\cong
U_{\mathrm{mod}}\circ\iota_R.
$$

### Toy lattices

For this proof of concept, define an $R$-lattice as a finite free $R$-module equipped with a chosen *perfect* symmetric form — that is, a **unimodular** lattice:

$$
\operatorname{Lat}(R)
=
\left\{
(M,b)
\ \middle|
M\in\operatorname{FreeFinMod}(R),
b:M\overset{\sim}{\longrightarrow}M^\vee,
b=b^\vee
\right\}.
$$

Note carefully what $b:M\overset{\sim}{\to}M^\vee$ says.
It is not nondegeneracy.
Writing $\tilde b:M\to M^\vee$, $x\mapsto b(x,-)$:

* $\tilde b$ injective is **nondegeneracy**;

* $\tilde b$ an isomorphism is **perfectness**, i.e. **unimodularity**.

For finite-dimensional $M$ over a field these agree, so the $\mathbf F_2$ example is unaffected.
Over a general commutative ring they do not, and the gap is the whole subject: $\operatorname{coker}(\tilde b:L\hookrightarrow L^\vee)=L^\vee/L$ is the *discriminant group*, trivial exactly when $L$ is unimodular.
An earlier draft of this section called the condition "nondegenerate" while writing the condition for perfect.
As stated, $\operatorname{Lat}(R)$ therefore contains only unimodular lattices and defines discriminant forms out of existence.
A general lattice layer must weaken $b$ to a map with a separate nondegeneracy condition and recover the unimodular case as a specialisation.

The form is not negotiable, and an earlier draft of this document said it was: "the precise notion of form can be weakened if the example only needs a second field."
That sentence is struck.
It treats $b$ — the entire content of the word *lattice* — as arbitrary payload, and only the category graph as real.
It was duly taken as licence: the first implementation shipped

$$
b : M \overset{\sim}{\longrightarrow} M,
$$

a linear automorphism, and went on calling the result $\operatorname{Lat}(R)$.
That is not a weakened lattice; it is not a lattice at all.
$M^\vee$ is a *different object*, reached from $M$ by a functor, and replacing it with $M$ deletes the mathematics while preserving the spelling — including in the surface syntax, where `(𝔽₂², id)` reads identically whether `id` denotes the standard form or the identity automorphism.

A decorated category whose decoration is arbitrary demonstrates nothing about lattices; it demonstrates forgetting a second field.
If that is all the example needs, the category must be called $\operatorname{FramedFreeMod}(R)$ and the word *lattice* must not appear.

What matters for the category graph is the preferred projection

$$
\pi_R:
\operatorname{Lat}(R)
\rightsquigarrow
\operatorname{FreeFinMod}(R),
\qquad
(M,b)\longmapsto M.
$$

Thus the finite and countable implementations on lattices are composites:

$$
\operatorname{Lat}(R)
\xrightarrow{\pi_R}
\operatorname{FreeFinMod}(R)
\xrightarrow{U_R^{\mathrm{fin}}}
\mathbf{FiniteSet}
\xrightarrow{\iota_{\mathrm{fc}}}
\mathbf{CountableSet}.
$$

No lattice-specific enumeration code is needed.

## 9. The preferred-functor graph

The proof-of-concept graph should contain the following edges.

```text
Lat(R)
  ↝ FreeFinMod(R)
  ↝ Mod(R)
  ↝ Set

FiniteSet
  ↝ CountableSet
  ↝ Set

FiniteCRing
  ↝ CRing
  ↝ Ring
  ↝ Set

FiniteCRing
  ↝ FiniteSet

FreeFinMod(R)
  ↝ FiniteSet       when R ∈ FiniteCRing
```

For $R=\mathbf F_2$, this gives:

```text
Lat(𝔽₂)
  ─π→ FreeFinMod(𝔽₂)
  ─Uᶠⁱⁿ→ FiniteSet
  ─ι→ CountableSet
  ─U→ Set
```

There is also the ordinary $\mathbf{Set}$-realization path:

```text
Lat(𝔽₂)
  ─π→ FreeFinMod(𝔽₂)
  ─ι→ Mod(𝔽₂)
  ─U→ Set
```

These are two valid paths.
Their composites should be linked by the coherence isomorphism attached to $U_{\mathbf F_2}^{\mathrm{fin}}$.

## 10. Defining $\mathbf F_2$

A natural source declaration would be:

```text
let 𝟚 := {0,1} ∈ FiniteSet,
with
    |𝟚| := 2,
    number(0) := 0,
    number(1) := 1,
    nth(0) := 0,
    nth(1) := 1.

let 𝔽₂ :=
    the commutative ring on 𝟚
    with arithmetic modulo 2
    ∈ FiniteCRing.
```

The finite-set data satisfy:

$$
\operatorname{number}_{\mathbf F_2}(0)=0,
\qquad
\operatorname{number}_{\mathbf F_2}(1)=1,
$$

and

$$
|\mathbf F_2|=2.
$$

For the Lean realization, the elaborator can use `ZMod 2`, prove or import an equivalence of $|\mathbf F_2|_{\mathbf{Set}}$ with the displayed two-element finite set, and package it as a `FiniteCRing` object.

Alternatively, an external backend may return:

* the presentation of the set;

* addition and multiplication tables;

* the equivalence with $[2]$;

* a ring-law certificate.

Lean then checks the certificate.
In a trusted experimental mode, the certificate theorem may instead contain `sorry`.

## 11. Defining the lattice $L$

The user-facing source should be:

```text
let L := (𝔽₂², id) ∈ Lat(𝔽₂).
```

The expected category determines the meaning.

* `𝔽₂²` is the standard rank-two free $\mathbf F_2$-module.

* Its chosen basis identification
  $$
  \mathbf F_2^2\overset{\sim}{\longrightarrow}\mathbf F_2^2
  $$
  is the identity.

* `id` in the second component is the standard form with identity Gram matrix.

No internal implementation name such as `Fin(2)` or `regular_module` appears.

The elaborated object is conceptually:

$$
L=
\left(
\left(
\mathbf F_2^2,\,
2,\,
\operatorname{id}_{\mathbf F_2^2}
\right),
\operatorname{id\_form}
\right).
$$

Its category of definition is `Lat(𝔽₂)`.

## 12. Discharging the countability obligation

The query

```text
#via L ∈ CountableSet.
```

should return:

```text
L is defined in Lat(𝔽₂).

Preferred path:
    Lat(𝔽₂)
      ─π→ FreeFinMod(𝔽₂)
      ─Uᶠⁱⁿ→ FiniteSet
      ─ι→ CountableSet
```

The finite-set implementation for the module uses:

$$
\mathbf F_2^2
\cong
\mathbf F_2\times\mathbf F_2.
$$

For $a,b\in\mathbf F_2=\{0,1\}$,

$$
\operatorname{number}_L(a,b)
=
2\operatorname{number}_{\mathbf F_2}(a)
+
\operatorname{number}_{\mathbf F_2}(b)
=
2a+b.
$$

Thus:

$$
\begin{array}{c|c}
(a,b)&\operatorname{number}_L(a,b)\
\hline
(0,0)&0\
(0,1)&1\
(1,0)&2\
(1,1)&3
\end{array}
$$

The partial inverse is:

$$
\begin{aligned}
\operatorname{nth}_L(0)&=(0,0),\
\operatorname{nth}_L(1)&=(0,1),\
\operatorname{nth}_L(2)&=(1,0),\
\operatorname{nth}_L(3)&=(1,1),
\end{aligned}
$$

and it is undefined for $n\geq4$.

The bilinear-form component is discarded by $\pi_{\mathbf F_2}$.
No new enumeration code is written for `L`.

## 13. Computing the cardinality

The expression

```text
|L|
```

elaborates through the finite-set path:

$$
\begin{aligned}
|L|
&=
\left|
U_{\mathbf F_2}^{\mathrm{fin}}
\bigl(\pi_{\mathbf F_2}(L)\bigr)
\right|\
&=
|\mathbf F_2^2|\
&=
|\mathbf F_2|\cdot|\mathbf F_2|\
&=
2\cdot2\
&=
4.
\end{aligned}
$$

The trace should be displayed as:

```text
|L|

= |𝔽₂²|
    by the preferred projection Lat(𝔽₂) → FreeFinMod(𝔽₂)

= |𝔽₂|²
    by the FiniteSet-realization implementation for free modules

= 2²
    by the finite realization of 𝔽₂

= 4
    by natural-number computation
```

The second equality is justified by the chosen basis and the product implementation in `FiniteSet`. It is not an unchecked symbolic rewrite.

## 14. The optional ring realization of $\mathbf F_2^2$

To retain the ring intuition, one may separately write:

```text
let A := 𝔽₂ × 𝔽₂ ∈ CAlg(𝔽₂).

let M :=
    A viewed as an 𝔽₂-module
    ∈ FreeFinMod(𝔽₂).

let L := (M,id) ∈ Lat(𝔽₂).
```

Now $A$ has two preferred views:

$$
\operatorname{CAlg}(\mathbf F_2)
\longrightarrow
\operatorname{CRing}
\longrightarrow
\operatorname{Set},
$$

and

$$
\operatorname{CAlg}(\mathbf F_2)
\longrightarrow
\operatorname{Mod}(\mathbf F_2)
\longrightarrow
\operatorname{Set}.
$$

Their $\mathbf{Set}$-realization composites should carry a registered natural isomorphism.

This gives the intended ring computation without asserting a $\mathbf{Set}$-preserving functor $\operatorname{Mod}_{\mathbf F_2}\to\operatorname{Ring}$, which is the thing that does not exist.
(Functors $\operatorname{Mod}_{\mathbf F_2}\to\operatorname{Ring}$ do exist — see §0 — they simply do not preserve the underlying set, which is what this comparison needs.)

## 15. Claims and Lean proof status

The surface forms should map directly to Lean.

```text
assume statement.
```

introduces a local hypothesis or a field of the current synthetic theory.

```text
axiom name:
    statement.
```

generates a Lean axiom.

```text
theorem name:
    statement.

proof Lean « ... ».
```

generates a checked Lean theorem.

A theorem without a proof:

```text
theorem finite_product_cardinality:
    for every X,Y ∈ FiniteSet,
    |X × Y| = |X||Y|.
```

generates, in draft mode, a Lean theorem whose body is `sorry`.

Lean elaborates `sorry` and incomplete proofs to an axiom dependency that is detectable through `#print axioms`; Lean's documentation explicitly recommends auditing those dependencies.
([Lean Language][6])

The DSL should expose:

```text
#assumptions |L|.
#status finite_product_cardinality.
```

Certified mode rejects exported results whose transitive dependencies contain `sorryAx`, except for explicitly whitelisted foundational axioms.

## 16. Generated Lean representation

The user never sees this representation, but the proof-of-concept backend can use structures resembling:

```lean
structure CountableSetObj where
  set : Type u
  number  : set → Nat
  nth     : Nat → Option set
  nth_number : ∀ x, nth (number x) = some x

structure FiniteSetObj where
  set : Type u
  size    : Nat
  enumerate : set ≃ Fin size
```

Each field names the entity it holds.
The first is a set, so it is called `set`. It is not called `carrier` (a substrate that is not an entity of the theory) and not called `underlying` (a relationship, which is a functor and therefore a separate declaration).

The product implementation constructs:

```lean
FiniteSetObj.prod X Y
```

with set `X.set × Y.set`, size `X.size * Y.size`, and an equivalence with the corresponding finite ordinal.

A finite free module object can be represented by:

```lean
structure FreeFinModuleObj (R) where
  module : ModuleCat R
  rank   : Nat
  basisEquiv :
    (Fin rank → R) ≃ₗ[R] module
```

A lattice object adds its form.

The generated countable view of `L` is then essentially the composite of realization functors:

```text
finiteToCountable
  (moduleToFiniteSet
    (latticeToModule L))
```

The Lean kernel checks the types of every component and the laws of every generated structure.

## 17. Minimal implementation modules

A sensible repository layout is:

```text
DSL/
  Parser.lean
  Syntax.lean
  IR.lean
  Registry.lean
  Elab.lean
  Diagnostics.lean

DSL/Stdlib/
  Foundation.lean
  Categories.lean
  Functors.lean
  MappingSpaces.lean
  PreferredViews.lean
  StructuredCategories.lean
  Sets.lean
  CountableSets.lean
  FiniteSets.lean
  Cardinality.lean
  Rings.lean
  Modules.lean
  FreeFiniteModules.lean
  Lattices.lean

DSL/Examples/
  F2Lattice.lean
```

The proof-of-concept need not implement general colimits, derived categories, or arbitrary higher coherence.
It should establish the architecture with this vertical slice.

## 18. Proof-of-concept acceptance criteria

The implementation is successful when all of the following work.

1. The parser accepts paper-like Unicode syntax such as `let L := (𝔽₂²,id) ∈ Lat(𝔽₂).`

2. Every category is represented as an object of the bundled foundational `Cat`.

3. `Hom_𝒞(A,B)` elaborates through the mapping-space interface, even though the initial backend uses discrete mapping spaces.

4. `A ∈ 𝒞` is decided by reachability in the preferred-functor graph.

5. Multiple preferred paths do not make membership ambiguous.

6. `#via` reports the selected path and its constituent functors.

7. `CountableSet` objects contain an actual encode/decode implementation, not merely a proposition saying they are countable.

8. The product implementation on finite sets automatically supplies the countability implementation and cardinality formula.

9. `𝔽₂` has FiniteSet-realization `{0,1}`, cardinality $2$, and a checked enumeration.

10. `L := (\mathbf F_2^2,\mathrm{id})` reaches `CountableSet` without lattice-specific code.

11. The generated numbering is $2a+b$.

12. The generated cardinality is $4$.

13. An attempted declaration of a preferred functor `Mod(𝔽₂) ↝ Ring` is rejected unless the author actually constructs such a functor.

14. Theorems with proofs are kernel checked; omitted proofs are represented by `sorry` and visibly reported.

15. The same source can later replace the locally discrete Mathlib backend with a genuinely homotopy-aware backend without changing its category graph or obligation semantics.

The central categorical mechanism is not inheritance by class inclusion.
It is lifting and composition:

$$
\boxed{
\begin{aligned}
&\text{a capability category } \mathcal E\to\mathcal B,\
&\text{an implementation } \widetilde U:\mathcal C\to\mathcal E,\
&\text{a preferred realization functor }U:\mathcal C\to\mathcal B,\
&\text{and a coherence }p\widetilde U\cong U.
\end{aligned}
}
$$

For the toy example:

$$
\operatorname{Lat}(\mathbf F_2)
\longrightarrow
\operatorname{FreeFinMod}(\mathbf F_2)
\longrightarrow
\mathbf{FiniteSet}
\longrightarrow
\mathbf{CountableSet}
\longrightarrow
\mathbf{Set}
$$

is simultaneously the preferred-view path, the implementation path for enumeration, and the reduction path for cardinality.

[1]: https://lean-lang.org/doc/reference/latest/Notations-and-Macros/Elaborators/?utm_source=chatgpt.com "Elaborators"
[2]: https://leanprover-community.github.io/mathlib4_docs/Mathlib/Logic/Encodable/Basic.html?utm_source=chatgpt.com "Mathlib.Logic.Encodable.Basic"
[3]: https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Cat.html?utm_source=chatgpt.com "Mathlib.CategoryTheory.Category.Cat"
[4]: https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/?utm_source=chatgpt.com "2. Elaboration and Compilation"
[5]: https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/ModuleCat/Basic.html?utm_source=chatgpt.com "Mathlib.Algebra.Category.ModuleCat.Basic"
[6]: https://lean-lang.org/doc/reference/latest/ValidatingProofs/?utm_source=chatgpt.com "Validating a Lean Proof"
