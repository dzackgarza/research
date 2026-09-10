# Generating families, presentations, and finiteness {#sec-generators-presentations}

Fix a commutative ring $R$.
The isomorphism-invariant properties of $R$-modules used below are @def-module-subcategories.
Whether a lift along a forgetful functor is a property or a chosen structure is decided by @def-property-structure-stuff.

## Generating frames {#sec-generating-frames}

::: {#def-generating-frame}
## Generating frames

Fix a set $I$ and write $R^{(I)}$ for the free $R$-module on $I$.
The comma category $\bigl(R^{(I)}\downarrow R\text{-}\mathbf{Mod}\bigr)$ has objects the pairs $(M,s)$ with $s\colon R^{(I)}\to M$ an $R$-linear map, and a morphism $(M,s)\to(N,t)$ is an $R$-linear map $f\colon M\to N$ satisfying $fs=t$.
Let
$$
\operatorname{GenFrame}_I(R)\subseteq\bigl(R^{(I)}\downarrow R\text{-}\mathbf{Mod}\bigr)
$$
be the full subcategory on the pairs with $s$ surjective.
A *generating frame* on $M$ indexed by $I$ is an object $(M,s)$ of this category; the image $s(e_i)$ of the $i$th standard generator is the $i$th member of the generating family.
:::

::: {#prp-generating-frame-homsets}
## Hom-sets of $\operatorname{GenFrame}_I(R)$

For objects $(M,s)$ and $(N,t)$ there is a morphism $(M,s)\to(N,t)$ exactly when $\ker s\subseteq\ker t$, and it is then the only one.
So $\operatorname{GenFrame}_I(R)$ is a preorder, and its hom-sets are genuinely sometimes empty.

*Proof.*
An $f$ with $fs=t$ is unique because $s$ is epic.
One exists exactly when $t$ factors through $s$, and since $s$ induces $R^{(I)}/\ker s\xrightarrow{\ \sim\ }M$ that happens exactly when $\ker s\subseteq\ker t$.
For emptiness take $R=\mathbb Z$, $I=\{1,2\}$, $M=N=\mathbb Z$, $s(a,b)=a$ and $t(a,b)=b$: both are surjective, $\ker s=0\oplus\mathbb Z$ and $\ker t=\mathbb Z\oplus0$, and neither contains the other, so both hom-sets between $(M,s)$ and $(N,t)$ are empty. $\square$
:::

::: {#prp-generating-frame-is-structure}
## A generating frame is chosen structure

Write $U_I\colon\operatorname{GenFrame}_I(R)\to R\text{-}\mathbf{Mod}$ for the comma-category projection $(M,s)\mapsto M$.
Then $U_I$ is faithful and is not full, and its fibre over $M$ is the discrete category on the set of surjections $R^{(I)}\twoheadrightarrow M$.
Hence a generating frame is a chosen object of a fibre of $U_I$, and $M$ admits one exactly when that set is nonempty.

*Proof.*
A morphism of $\operatorname{GenFrame}_I(R)$ is an $R$-linear map subject to a condition, so $U_I$ is injective on morphisms and faithful.
It is not full: for $I$ a one-element set, $M=N=R$ and $s=t=\operatorname{id}_R$, multiplication by $r\in R$ is a morphism $(R,s)\to(R,t)$ only when $r=1$.
A morphism $(M,s)\to(M,s')$ over $\operatorname{id}_M$ is the identity of $M$ together with the requirement $s=s'$, so the fibre has no morphisms other than identities. $\square$
:::

::: {#def-coordinatized-module}
## The two morphism conventions

Let $\operatorname{Coord}_I(R)$ be the category with the same objects as $\operatorname{GenFrame}_I(R)$ in which a morphism $(M,s)\to(N,t)$ is an arbitrary $R$-linear map $M\to N$.
Its projection to $R\text{-}\mathbf{Mod}$ is fully faithful, so it is an equivalence onto the replete full subcategory of modules admitting an $I$-indexed generating frame, and by @def-property-structure-stuff it describes a property.
The identity on objects and the inclusion on morphisms give a faithful functor
$$
\operatorname{GenFrame}_I(R)\longrightarrow\operatorname{Coord}_I(R).
$$

The two categories answer different questions.
The frame-preserving one classifies a chosen frame as structure, by @prp-generating-frame-is-structure.
The coordinatized one is the setting for matrix calculus: a morphism there has a matrix relative to the two chosen frames, and change of frame acts by the congruence of @prp-gram-congruence.
The basis case of the pair is @def-based-module and @prp-basis-is-structure.
:::

::: {#def-cyclic-module}
## Cyclic and finitely generated modules

An $R$-module $M$ is *cyclic* if it admits a generating frame indexed by a one-element set, and *finitely generated* if it admits one indexed by a finite set.
A cyclic module is isomorphic to $R/\operatorname{Ann}_R(x)$ for the image $x$ of the standard generator, and the cyclic modules form a replete full subcategory of the finitely generated ones.
Finite generation is the property recorded in @def-module-subcategories: it asserts that the set of finite generating frames on $M$ is nonempty, and it retains none of the data of a chosen frame.
:::

::: {#def-finite-module}
## Finiteness of the underlying set

Finiteness of the underlying set is a property of objects of $\mathbf{Set}$; the modules with finite underlying set are its pullback along the underlying-set functor $R\text{-}\mathbf{Mod}\to\mathbf{Set}$ in the sense of @def-axiom-through-functor.
This property and finite generation are independent.
Over $R=\mathbb Z$: the module $\mathbb Z$ is finitely generated and has infinite underlying set, $\mathbb Q/\mathbb Z$ has infinite underlying set and admits no finite generating frame, and $\mathbb Z/n\mathbb Z$ has both properties.
:::

## Presentations {#sec-presentations}

::: {#def-finite-presentation}
## Finite presentations

A *finite presentation* of an $R$-module $M$ is an exact sequence
$$
R^{m}\xrightarrow{\ d_M\ }R^{n}\xrightarrow{\ q_M\ }M\longrightarrow0
$$
with $m,n$ finite [@Wei94, §3.3].
It consists of a finite generating frame $q_M$ together with a finite generating frame for the module of relations $\ker q_M$.
The module $M$ is *finitely presented* if it admits a finite presentation.
:::

::: {#def-presentation-category}
## The category of finite presentations

Let $\operatorname{FinPres}(R)$ be the category whose objects are the finite presentations of @def-finite-presentation and whose morphisms are the commutative diagrams

```{.tikz}
%%| filename: finite-presentation-morphism
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}
R^{m} \arrow[r,"d_M"] \arrow[d,"A_1"'] &
R^{n} \arrow[r,"q_M"] \arrow[d,"A_0"'] &
M \arrow[r] \arrow[d,"f"] &
0\\
R^{m'} \arrow[r,"d_N"'] &
R^{n'} \arrow[r,"q_N"'] &
N \arrow[r] &
0
\end{tikzcd}
```

so the datum of a morphism includes the pair $(A_1,A_0)$ of maps of free modules.
Relative to the standard bases, $A_1$ and $A_0$ are matrices over $R$, and $f$ is the $R$-linear map they present.
The projection $\operatorname{FinPres}(R)\to R\text{-}\mathbf{Mod}$ sends the diagram to $f$.
:::

::: {#prp-presentation-lift}
## Lifting a morphism to presentations

Let finite presentations of $M$ and $N$ be given.
Every $R$-linear map $f\colon M\to N$ is the image of a morphism of $\operatorname{FinPres}(R)$.

*Proof.*
Since $R^{n}$ is projective and $q_N$ is surjective, $fq_M\colon R^{n}\to N$ factors as $q_NA_0$ for some $A_0\colon R^{n}\to R^{n'}$.
Then $q_NA_0d_M=fq_Md_M=0$, so $A_0d_M$ lands in $\ker q_N=\operatorname{im}d_N$; since $R^{m}$ is projective and $R^{m'}\to\operatorname{im}d_N$ is surjective, $A_0d_M$ factors as $d_NA_1$ for some $A_1\colon R^{m}\to R^{m'}$. $\square$

The pair $(A_1,A_0)$ produced by this argument is not determined by $f$.
The relation identifying two lifts of one $R$-linear map is the chain homotopy of @thm-resolution-comparison, which is stated for resolutions rather than for two-term presentations.

Forgetting $A_1$ and $A_0$ gives the category on the same objects whose morphisms are the $R$-linear maps alone.
That is the distinction of @def-coordinatized-module one level up: the lifted morphisms carry the matrices, the abstract ones carry only the module map they present.
:::

::: {#def-fp-n}
## Modules of type $FP_n$

For $n\ge0$, an $R$-module $M$ is of *type $FP_n$* if it admits a projective resolution (@def-resolution)
$$
\cdots\longrightarrow P_1\longrightarrow P_0\longrightarrow M\longrightarrow0
$$
in which $P_i$ is finitely generated for $0\le i\le n$.
Type $FP_0$ is finite generation and type $FP_1$ is finite presentation.
A chosen partial resolution finitely generated through degree $n$ is structure on $M$; type $FP_n$ is the property asserting that one exists.
:::

## Automorphisms acting on frames {#sec-frames-and-automorphisms}

The endomorphism monoid $\operatorname{Hom}_{\mathcal C}(X,X)$ and the automorphism group $\operatorname{Aut}_{\mathcal C}(X)$ of an object are defined at @def-endomorphism-monoid; for a lattice $L$ the instance $O(L)=\operatorname{Aut}(L)$ is in @sec-isometry-groups.

::: {#prp-automorphisms-act-on-frames}
## The action on the fibre

Let $I$ be a set and let $M$ be an $R$-module.
Precomposition, $(M,s)\cdot u=(M,su)$ for $u\in\operatorname{Aut}_R\bigl(R^{(I)}\bigr)$, is a right action of $\operatorname{Aut}_R\bigl(R^{(I)}\bigr)$ on the fibre $U_I^{-1}(M)$ of @prp-generating-frame-is-structure, and the action is free.
If $s$ and $s'$ are both isomorphisms, then $u=s^{-1}s'$ is the unique element with $su=s'$.

*Proof.*
The assignment is a right action because composition is associative, and $su$ is surjective when $s$ is.
If $su=s$ then $u=\operatorname{id}$, because $s$ is epic; so the action is free.
For $s,s'$ isomorphisms, $s^{-1}s'$ is an automorphism of $R^{(I)}$ with $s(s^{-1}s')=s'$, and it is unique by freeness. $\square$
:::

## The free module functor {#sec-free-module-functor}

::: {#def-free-module-functor}
## Free modules on a set

Sending a set $I$ to $R^{(I)}$ and a function $\varphi\colon I\to J$ to the $R$-linear map $e_i\mapsto e_{\varphi(i)}$ defines a functor $R^{(-)}\colon\mathbf{Set}\to R\text{-}\mathbf{Mod}$, left adjoint to the underlying-set functor $U$:
$$
\adj{\mathbf{Set}}{R\text{-}\mathbf{Mod}}{R^{(-)}}{U},
\qquad
R^{(-)}\dashv U.
$$
The unit $\eta_I\colon I\to U\bigl(R^{(I)}\bigr)$ sends $i$ to $e_i$, and the adjunction states that composition with $\eta_I$ is a bijection
$$
\operatorname{Hom}_{R\text{-}\mathbf{Mod}}\bigl(R^{(I)},M\bigr)
\xrightarrow{\ \sim\ }
\operatorname{Hom}_{\mathbf{Set}}\bigl(I,U(M)\bigr).
$$
Under this bijection a generating frame indexed by $I$ (@def-generating-frame) is a family $(x_i)_{i\in I}$ of elements of $M$ whose associated $R$-linear map is surjective.
:::
