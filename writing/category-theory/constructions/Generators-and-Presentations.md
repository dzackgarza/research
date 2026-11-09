# Generating families, presentations, and finiteness {#sec-generators-presentations}

Fix a commutative ring $R$.

## Generating frames {#sec-generating-frames}

::: {.definition #def:generating-frame title="Generating frames"}

Fix a set $I$ and write $R^{(I)}$ for the free $R$-module on $I$.
The comma category $\bigl(R^{(I)}\downarrow R\text{-}\mathbf{Mod}\bigr)$ has objects the pairs $(M,s)$ with $s\colon R^{(I)}\to M$ an $R$-linear map, and a morphism $(M,s)\to(N,t)$ is an $R$-linear map $f\colon M\to N$ satisfying $fs=t$.
Let
$$
\operatorname{GenFrame}_I(R)\iscontainedin\bigl(R^{(I)}\downarrow R\text{-}\mathbf{Mod}\bigr)
$$
be the full subcategory on the pairs with $s$ surjective.
A *generating frame* on $M$ indexed by $I$ is an object $(M,s)$ of this category; the image $s(e_i)$ of the $i$th standard generator is the $i$th member of the generating family.
:::

::: {.proposition #prop:generating-frame-homsets title="Hom-sets of $\operatorname{GenFrame}
_I(R)$"}

For objects $(M,s)$ and $(N,t)$ there is a morphism $(M,s)\to(N,t)$ exactly when $\ker s\iscontainedin\ker t$, and it is then the only one.
So $\operatorname{GenFrame}_I(R)$ is a preorder.
For $R=\bZ$ and $I=\{1,2\}$, some pairs of its objects admit no morphism in either direction.
:::

::: {.proof}
An $f$ with $fs=t$ is unique because $s$ is epic.
One exists exactly when $t$ factors through $s$, and since $s$ induces $R^{(I)}/\ker s\xrightarrow{\ \sim\ }M$ that happens exactly when $\ker s\iscontainedin\ker t$.
For emptiness take $R=\bZ$, $I=\{1,2\}$, $M=N=\bZ$, $s(a,b)=a$ and $t(a,b)=b$: both are surjective, $\ker s=0\oplus\bZ$ and $\ker t=\bZ\oplus0$, and neither contains the other, so both hom-sets between $(M,s)$ and $(N,t)$ are empty.
:::

::: {.proposition #prop:generating-frame-is-structure title="A generating frame is chosen structure"}
Write $U_I\colon\operatorname{GenFrame}_I(R)\to R\text{-}\mathbf{Mod}$ for the comma-category projection $(M,s)\mapsto M$.
Then $U_I$ is faithful and is not full, and its fibre over $M$ is the discrete category on the set of surjections $R^{(I)}\twoheadrightarrow M$.
Hence a generating frame is a chosen object of a fibre of $U_I$, and $M$ admits one exactly when that set is nonempty.
:::

::: {.proof}
A morphism of $\operatorname{GenFrame}_I(R)$ is an $R$-linear map subject to a condition, so $U_I$ is injective on morphisms and faithful.
It is not full: for $I$ a one-element set, $M=N=R$ and $s=t=\id_R$, multiplication by $r\in R$ is a morphism $(R,s)\to(R,t)$ only when $r=1$.
A morphism $(M,s)\to(M,s')$ over $\id_M$ is the identity of $M$ together with the requirement $s=s'$, so the fibre has no morphisms other than identities.
:::

::: {.definition #def:coordinatized-module title="The two morphism conventions"}

Let $\operatorname{Coord}_I(R)$ be the category with the same objects as $\operatorname{GenFrame}_I(R)$ in which a morphism $(M,s)\to(N,t)$ is an arbitrary $R$-linear map $M\to N$.
Its projection to $R\text{-}\mathbf{Mod}$ is fully faithful, so it is an equivalence onto the replete full subcategory of modules admitting an $I$-indexed generating frame, and by @def:property-structure-stuff it describes a property.
The identity on objects and the inclusion on morphisms give a faithful functor
$$
\operatorname{GenFrame}_I(R)\too\operatorname{Coord}_I(R).
$$

The frame-preserving one classifies a chosen frame as structure, by @prop:generating-frame-is-structure.
The coordinatized one is the setting for matrix calculus: a morphism there has a matrix relative to the two chosen frames, and change of frame acts by the congruence of @prop:gram-congruence.
The basis case of the pair is @def:based-module and @prop:basis-is-structure.
:::

::: {.definition #def:cyclic-module title="Cyclic and finitely generated modules"}

An $R$-module $M$ is *cyclic* if it admits a generating frame indexed by a one-element set, and *finitely generated* if it admits one indexed by a finite set.
A cyclic module is isomorphic to $R/\Ann_R(x)$ for the image $x$ of the standard generator, and the cyclic modules form a replete full subcategory of the finitely generated ones.
Finite generation is the property of @def:module-subcategories that asserts that the set of finite generating frames on $M$ is nonempty.
:::

::: {.definition #def:finite-module title="Finiteness of the underlying set"}

Finiteness of the underlying set is a property of objects of $\mathbf{Set}$; the modules with finite underlying set are its pullback along the underlying-set functor $R\text{-}\mathbf{Mod}\to\mathbf{Set}$ in the sense of @def:axiom-through-functor.
This property and finite generation are independent.
Over $R=\bZ$: the module $\bZ$ is finitely generated and has infinite underlying set, $\bQ/\bZ$ has infinite underlying set and admits no finite generating frame, and $\bZ/n\bZ$ has both properties.
:::

## Presentations {#sec-presentations}

::: {.definition #def:finite-presentation title="Finite presentations"}

A *finite presentation* of an $R$-module $M$ is an exact sequence
$$
R^{m}\xrightarrow{\ d_M\ }R^{n}\xrightarrow{\ q_M\ }M\too0
$$
with $m,n$ finite [@Wei94, §3.3].
It consists of a finite generating frame $q_M$ together with a finite generating frame for the module of relations $\ker q_M$.
The module $M$ is *finitely presented* if it admits a finite presentation.
:::

::: {.definition #def:presentation-category title="The category of finite presentations"}

Let $\operatorname{FinPres}(R)$ be the category whose objects are the finite presentations of @def:finite-presentation and whose morphisms are the commutative diagrams

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

::: {.proposition #prop:presentation-lift title="Lifting a morphism to presentations"}
Let finite presentations of $M$ and $N$ be given.
Every $R$-linear map $f\colon M\to N$ is the image of a morphism of $\operatorname{FinPres}(R)$.
:::

::: {.proof}
Since $R^{n}$ is projective and $q_N$ is surjective, $fq_M\colon R^{n}\to N$ factors as $q_NA_0$ for some $A_0\colon R^{n}\to R^{n'}$.
Then $q_NA_0d_M=fq_Md_M=0$, so $A_0d_M$ lands in $\ker q_N=\im d_N$; since $R^{m}$ is projective and $R^{m'}\to\im d_N$ is surjective, $A_0d_M$ factors as $d_NA_1$ for some $A_1\colon R^{m}\to R^{m'}$.
:::

::: {.example #ex:presentation-lift-not-unique title="Lifts to presentations are not unique"}

Let $R\neq0$.
Take the finite presentation $R\xrightarrow{\ \id\ }R\too0\too0$ of the zero module, with $m=n=1$, as both source and target, and let $f=0$.
For every $r\in R$ the pair $(A_1,A_0)=(r,r)$ is a morphism of $\operatorname{FinPres}(R)$ over $f$.
The left square commutes because $\id\circ r=r\circ\id$, and the right square commutes because both composites $R\to0$ are zero.
Since $0\neq1$ in $R$, the pairs $(0,0)$ and $(1,1)$ are two different lifts of $f$.
So the pair $(A_1,A_0)$ of @prop:presentation-lift is not determined by $f$.
:::

::: {.proposition #prop:presentation-lifts-homotopic title="Two lifts of one map are chain homotopic"}

Let $(A_1,A_0)$ and $(A_1',A_0')$ be morphisms of $\operatorname{FinPres}(R)$ between the same two finite presentations, both over $f\colon M\to N$.
Extend the presentation of $M$ to a projective resolution $P$ of $M$ with $P_1\to P_0$ equal to $d_M$, and the presentation of $N$ to a resolution $Q$ of $N$ with $Q_1\to Q_0$ equal to $d_N$.
Then each of the two morphisms extends to a chain map $P\to Q$ over $f$, and any two such chain maps are chain homotopic.
In particular $A_0-A_0'=d_Nh_0$ for some $R$-linear map $h_0\colon R^{n}\to R^{m'}$.
:::

::: {.proof}

The extensions exist: by @def:resolution the modules $\ker d_M$ and $\ker d_N$ have projective resolutions, and splicing them onto the presentations gives $P$ and $Q$.
The pair $(A_1,A_0)$ is a chain map $P\to Q$ in degrees $0$ and $1$ over $f$, because the two squares of @def:presentation-category commute.
For degree $2$, the composite $A_1d^P_2$ satisfies $d_NA_1d^P_2=A_0d_Md^P_2=0$, so it lands in $\ker d_N=\im d^Q_2$, by exactness of $Q$.
Since $P_2$ is projective, it lifts along $Q_2\twoheadrightarrow\im d^Q_2$ to $f_2$ with $d^Q_2f_2=A_1d^P_2$.
The higher degrees follow by the same induction as in the proof of @thm:resolution-comparison.
The same argument extends $(A_1',A_0')$.
Both chain maps lift $f$, so they are chain homotopic by @thm:resolution-comparison.
A chain homotopy $s$ satisfies $f_0-f_0'=d^Q_1s_0$ in degree $0$, because $P_{-1}=0$, and this is the last assertion with $h_0=s_0$.
:::

::: {.definition #def:fp-n title="Modules of type $FP_n$"}

For $n\ge0$, an $R$-module $M$ is of *type $FP_n$* if it admits a projective resolution (@def:resolution)
$$
\cdots\too P_1\too P_0\too M\too0
$$
in which $P_i$ is finitely generated for $0\le i\le n$.
Type $FP_0$ is finite generation and type $FP_1$ is finite presentation.
A chosen partial resolution finitely generated through degree $n$ is structure on $M$; type $FP_n$ is the property asserting that one exists.
:::

## Automorphisms acting on frames {#sec-frames-and-automorphisms}

::: {.proposition #prop:automorphisms-act-on-frames title="The action on the fibre"}
Let $I$ be a set and let $M$ be an $R$-module.
Precomposition, $(M,s)\cdot u=(M,su)$ for $u$ in the automorphism group $\Aut_R\bigl(R^{(I)}\bigr)$ of @def:endomorphism-monoid, is a right action of $\Aut_R\bigl(R^{(I)}\bigr)$ on the fibre $U_I^{-1}(M)$ of @prop:generating-frame-is-structure.
The stabilizer of $(M,s)$ is the subgroup of those $u$ with $(u-\id)\bigl(R^{(I)}\bigr)\subseteq\ker s$.
If $s$ and $s'$ are both isomorphisms, then $u=s^{-1}s'$ is the unique element with $su=s'$.
:::

::: {.proof}
The assignment is a right action because composition is associative, and $su$ is surjective when $s$ is.
The equation $su=s$ holds if and only if $s\circ(u-\id)=0$, that is, if and only if the image of $u-\id$ lies in $\ker s$.
For $s,s'$ isomorphisms, $s^{-1}s'$ is an automorphism of $R^{(I)}$ with $s(s^{-1}s')=s'$.
If also $su=s'$, then $u=s^{-1}s'$, because $s$ is monic.
:::

::: {.example #ex:frame-stabilizer-nontrivial title="A frame with a nontrivial stabilizer"}
Let $R\neq0$, let $I=\{1,2\}$, let $M=R$ and let $s\colon R^2\to R$ be $s(a,b)=a$.
The map $u(a,b)=(a,a+b)$ is an automorphism of $R^2$ with inverse $(a,b)\mapsto(a,b-a)$, and $u\neq\id$.
Since $su(a,b)=a=s(a,b)$, the element $u$ fixes $(M,s)$, so the action of @prop:automorphisms-act-on-frames is not free.
:::

## The free module functor {#sec-free-module-functor}

::: {.definition #def:free-module-functor title="Free modules on a set"}

Sending a set $I$ to $R^{(I)}$ and a function $\varphi\colon I\to J$ to the $R$-linear map $e_i\mapsto e_{\varphi(i)}$ defines a functor $R^{(-)}\colon\mathbf{Set}\to R\text{-}\mathbf{Mod}$, left adjoint to the underlying-set functor $U$:
$$
\adj{\mathbf{Set}}{R\text{-}\mathbf{Mod}}{R^{(-)}}{U},
\qquad
R^{(-)}\dashv U.
$$
The unit $\eta_I\colon I\to U\bigl(R^{(I)}\bigr)$ sends $i$ to $e_i$, and the adjunction states that composition with $\eta_I$ is a bijection
$$
\Hom_{R\text{-}\mathbf{Mod}}\bigl(R^{(I)},M\bigr)
\xrightarrow{\ \sim\ }
\Hom_{\mathbf{Set}}\bigl(I,U(M)\bigr).
$$
Under this bijection a generating frame indexed by $I$ (@def:generating-frame) is a family $(x_i)_{i\in I}$ of elements of $M$ whose associated $R$-linear map is surjective.
:::
