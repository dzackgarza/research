# Higher categories and universes {#sec-higher-categories-universes}

::: {#def-universe}
## The universe

Fix an axiomatic $(\infty,2)$-category $\mathcal U$, called the universe of the theory, with terminal object $*$.
The higher category of higher categories is a chosen object of $\mathcal U$, hence a point
$$
\mathbf{Cat}_\infty\colon *\longrightarrow\mathcal U.
$$
All categories below are small relative to $\mathcal U$.
:::

::: {#def-higher-category}
## Higher categories

A higher category is a point
$$
C\colon *\longrightarrow\mathbf{Cat}_\infty.
$$
For higher categories $C$ and $D$, a morphism $F\colon C\to D$ is a $2$-morphism in $\mathcal U$ between the corresponding points.
:::

::: {#def-equivalence-of-categories}
## Equivalences

A morphism $F\colon C\to D$ is an *equivalence* if there is a morphism $G\colon D\to C$ and invertible $2$-morphisms
$$
G\circ F\Longrightarrow\operatorname{id}_C,
\qquad
F\circ G\Longrightarrow\operatorname{id}_D.
$$
Write $C\simeq D$ when such an equivalence has been chosen.
:::

::: {#def-grothendieck-construction}
## Grothendieck constructions and objects

For a morphism $F\colon C\to\mathbf{Cat}_\infty$, assume its cocartesian Grothendieck construction exists in $\mathcal U$:
$$
q_F\colon\int_{c\in C}F(c)\longrightarrow C.
$$
Its fiber over a point $c\colon *\to C$ is equivalent to $F(c)$.
This defines the notation $\int_C F$ [@nlab:grothendieck_construction].

Apply this construction to the identity morphism of $\mathbf{Cat}_\infty$:
$$
p\colon
\int_{\mathbf{Cat}_\infty}\mathbf{Cat}_\infty
\longrightarrow
\mathbf{Cat}_\infty.
$$
For a higher category $C\colon *\to\mathbf{Cat}_\infty$, define $\int_C C$ by the cartesian square
\begin{tikzcd}
\int_C C
  \arrow[r]
  \arrow[d]
&
\int_{\mathbf{Cat}_\infty}\mathbf{Cat}_\infty
  \arrow[d, "p"]
\\
*
  \arrow[r, "C"']
  \arrow[ru, phantom, very near start, "\lrcorner"]
&
\mathbf{Cat}_\infty .
\end{tikzcd}
The fiber equivalence gives $\int_C C\simeq C$.
An object of $C$ is a point
$$
x\colon *\longrightarrow\int_C C.
$$
:::

::: {#def-internal-hom}
## Internal homs

The higher category $\mathbf{Cat}_\infty$ is cartesian closed.
Its internal hom is written
$$
[-,-]\colon
\mathbf{Cat}_\infty^{\mathrm{op}}\times\mathbf{Cat}_\infty
\longrightarrow\mathbf{Cat}_\infty.
$$
For higher categories $A,C,D$, there is a natural equivalence
$$
[A\times C,D]\simeq[A,[C,D]].
$$
A point of $[C,D]$ is a morphism $C\to D$; its higher morphisms are transformations and their higher transformations.

For each higher category $C$, assume a hom-object bifunctor
$$
[-,-]_C\colon
(\int_C C)^{\mathrm{op}}\times\int_C C
\longrightarrow\mathbf{Cat}_\infty.
$$
For points $x,y\colon *\to\int_C C$, its value is the point
$$
[x,y]_C\colon *\longrightarrow\mathbf{Cat}_\infty.
$$
Its endpoint-fiber presentation is given in @def-mapping-spaces.
:::

::: {#def-core}
## Underlying homotopy type and core

Let $\mathcal S=\mathbf{Types}$ and let
$$
i\colon\mathcal S\hookrightarrow\mathbf{Cat}_\infty
$$
be the full inclusion of groupoidal higher categories.
Assume the adjunctions
$$
\Pi_\infty\dashv i\dashv(-)^\simeq.
$$
The left adjoint
$$
\Pi_\infty\colon\mathbf{Cat}_\infty\longrightarrow\mathcal S
$$
is the underlying homotopy type obtained by inverting every morphism.
The right adjoint $C\mapsto C^\simeq$ is the core obtained by retaining every object and only the equivalences [@Lur26, Tags 01DQ and 02F5].
:::


::: {#def-bicomplete-cat-infinity}
## Limits, loops, and suspensions

The higher category $\mathbf{Cat}_\infty$ has an initial object $\varnothing$ and a terminal object $*$, and it is bicomplete.
For a pointed higher category $(X,x)$, where $x\colon *\to\int_X X\simeq X$, define
$$
\Omega_xX:=*\times_X*.
$$
For a higher category $A$, define its suspension by the pushout
\begin{tikzcd}
A
  \arrow[r]
  \arrow[d]
&
*
  \arrow[d]
\\
*
  \arrow[r]
  \arrow[ru, phantom, very near start, "\ulcorner"]
&
\Sigma A.
\end{tikzcd}
The two coprojections $*\to\Sigma A$ make $\Sigma A$ bipointed.
:::

::: {#def-B01-construction}
## The $B_{01}$ construction

The higher category of bipointed higher categories is the comma category
$$
((*\amalg *)\downarrow\operatorname{id}_{\mathbf{Cat}_\infty}).
$$
Its objects are morphisms
$$
x_0\amalg x_1\colon *\amalg *\longrightarrow X.
$$
The endpoint hom functor is
$$
\Omega_{01}\colon
((*\amalg *)\downarrow\operatorname{id}_{\mathbf{Cat}_\infty})
\longrightarrow\mathbf{Cat}_\infty,
\qquad
(X;x_0,x_1)\longmapsto[x_0,x_1]_X.
$$
Assume that $\Omega_{01}$ has a left adjoint
$$
B_{01}\dashv\Omega_{01}.
$$
For $A\colon *\to\mathbf{Cat}_\infty$, the bipointed higher category $B_{01}A$ has distinguished objects $0,1$ and hom-objects displayed by
\begin{tikzcd}[column sep=huge]
0
  \arrow[r, bend left=18, "A"]
  \arrow[loop left, "*"]
&
1
  \arrow[l, bend left=18, "\varnothing"]
  \arrow[loop right, "*"] .
\end{tikzcd}
Composition is given by the identity actions on $A$ and the unique morphisms from $\varnothing$.
The suspension $\Sigma A$ is the pushout in @def-bicomplete-cat-infinity. The object $B_{01}A$ is characterized by the adjunction $B_{01}\dashv\Omega_{01}$.
:::

::: {#def-cells}
## Walking arrows and ordinal categories

Define
$$
[0]:=*,
\qquad
[1]:=B_{01}*.
$$
Write $s,t\colon[0]\to[1]$ for the two distinguished objects.
For each integer $n\geq2$, define the ordinal category $[n]$, the walking chain of $n$ composable arrows, by
$$
[n]:=
\underbrace{[1]\amalg_{[0]}[1]\amalg_{[0]}\cdots\amalg_{[0]}[1]}_{n\text{ copies}},
$$
where each pushout identifies the target of one copy with the source of the next.
For a higher category $C$, the internal hom $[[n],C]$ is the higher category of morphisms $[n]\to C$ and their higher transformations.
:::

::: {#def-mapping-spaces}
## Arrows and mapping types

For a higher category $C$, define
$$
\operatorname{Arr}(C):=[[1],C].
$$
Precomposition with $s$ and $t$ gives
$$
(s^*,t^*)\colon[[1],C]
\longrightarrow
[[0],C]\times[[0],C]
\simeq
\int_C C\times\int_C C.
$$
For points $x,y\colon*\to\int_C C$, the hom-object $[x,y]_C$ is equivalently the cartesian fiber
\begin{tikzcd}
{[x,y]_C}
  \arrow[r]
  \arrow[d]
&
{[[1],C]}
  \arrow[d, "{(s^*,t^*)}"]
\\
*
  \arrow[r, "{(x,y)}"']
  \arrow[ru, phantom, very near start, "\lrcorner"]
&
\int_C C\times\int_C C.
\end{tikzcd}
Its underlying mapping type is
$$
\operatorname{Map}_C(x,y):=\Pi_\infty[x,y]_C.
$$
Likewise,
$$
\operatorname{Map}_{\mathbf{Cat}_\infty}(C,D):=\Pi_\infty[C,D].
$$
:::

::: {#def-initial-terminal}
## Initial, terminal, and contractible objects

An object $t\colon*\to\int_C C$ is terminal if $\operatorname{Map}_C(x,t)$ is contractible for every $x\colon*\to\int_C C$.
An object $i\colon*\to\int_C C$ is initial if $\operatorname{Map}_C(i,x)$ is contractible for every $x\colon*\to\int_C C$.
A higher category is *contractible* when it is equivalent to $*$.
:::

::: {#def-truncated}
## Truncated objects and morphisms

Let $C$ be a higher category.
For an integer $n\geq-2$, an object $X\colon*\to\int_C C$ is *$n$-truncated* if $\operatorname{Map}_C(Y,X)$ is an $n$-truncated type for every $Y\colon*\to\int_C C$.
The $(-2)$-truncated objects are the terminal objects.

For an object $Y\colon*\to\int_C C$, write $C_{/Y}:=(\operatorname{id}_C\downarrow Y)$ for the slice. A morphism $f\colon X\to Y$ is *$n$-truncated* if it is an $n$-truncated object of $C_{/Y}$.
Equivalently, for every $Z\colon*\to\int_C C$ and every point of $\operatorname{Map}_C(Z,Y)$, the corresponding fiber of
$$
\operatorname{Map}_C(Z,X)
\longrightarrow
\operatorname{Map}_C(Z,Y)
$$
is an $n$-truncated type.
A $(-2)$-truncated morphism is an equivalence.
When the required pullback exists and $n\geq-1$, the recursive criterion is
$$
f\text{ is }n\text{-truncated}
\quad\Longleftrightarrow\quad
\Delta_f\colon X\longrightarrow X\times_YX
\text{ is }(n-1)\text{-truncated}
$$
[@Lur26, Tags 05F8 and 05FS].

For a type $S$, $n$-truncation means $\pi_k(S,s)=0$ for every point $s$ and every $k>n$.
A $(-2)$-truncated type is contractible, a $(-1)$-truncated type is empty or contractible, and a $0$-truncated type is a set.
When the inclusion of $n$-truncated objects of $C$ is reflective, write its reflector as $\tau_{\leq n}^C$.
:::

::: {#def-infinity-category-universe}
## The truncation tower

For each integer $n\geq-2$, assume an idempotent truncation endomorphism
$$
T_{\leq n}\colon\mathbf{Cat}_\infty\longrightarrow\mathbf{Cat}_\infty.
$$
Define
$$
\mathbf{Cat}_n
:=\operatorname{EssIm}(T_{\leq n})
=:T_{\leq n}\mathbf{Cat}_\infty.
$$
Let
$$
\iota_n\colon\mathbf{Cat}_n\longrightarrow\mathbf{Cat}_\infty
$$
be the full inclusion, and write
$$
\tau_{\leq n}\colon\mathbf{Cat}_\infty\longrightarrow\mathbf{Cat}_n
$$
for the corestriction of $T_{\leq n}$ to its essential image.
Assume
$$
\tau_{\leq n}\dashv\iota_n.
$$
If $\iota_n$ also has a right adjoint, write
$$
\iota_n\dashv\tau_{\leq n}^{\mathrm R}.
$$
The tower is
$$
\mathbf{Cat}_{-2}\longrightarrow
\mathbf{Cat}_{-1}\longrightarrow
\mathbf{Cat}_0\longrightarrow
\mathbf{Cat}_1\longrightarrow\cdots\longrightarrow
\mathbf{Cat}_n\longrightarrow\cdots\longrightarrow
\mathbf{Cat}_\infty.
$$
An *$n$-category structure* on a higher category $C\colon*\to\mathbf{Cat}_\infty$ is a lift
\begin{tikzcd}
&
\mathbf{Cat}_n
  \arrow[d, "\iota_n"]
\\
*
  \arrow[ur, "\widetilde C"]
  \arrow[r, "C"']
&
\mathbf{Cat}_\infty
\end{tikzcd}
together with a specified equivalence $\iota_n\circ\widetilde C\simeq C$.

For $n\geq0$, a second construction begins with the full replete subcategory $\mathbf{Cat}_n^{\mathrm{loc}}\subseteq\mathbf{Cat}_\infty$ on the locally $(n-1)$-truncated higher categories [@Lur26, Tag 05EA].
Its inclusion supplies $\iota_n$ after an equivalence $\mathbf{Cat}_n^{\mathrm{loc}}\simeq\mathbf{Cat}_n$ has been established.
Its left and right adjoints, when they exist, supply $\tau_{\leq n}$ and $\tau_{\leq n}^{\mathrm R}$.

For higher categories $C,D$, define
$$
[C,D]^{\leq n}\hookrightarrow[C,D]
$$
to be the full replete subcategory on the $n$-truncated objects of $[C,D]$.
These objects are the $n$-truncated morphisms $C\to D$ internal to the mapping higher category.
:::


::: {#def-ordinary-category-specialization}
## Ordinary categories

An *ordinary-category structure* on a higher category $C\colon*\to\mathbf{Cat}_\infty$ is a $1$-category structure on $C$: a point
$$
\widetilde C\colon*\longrightarrow\mathbf{Cat}_1
$$
together with a specified equivalence $\iota_1\circ\widetilde C\simeq C$.
An ordinary category may be presented by the point $\widetilde C$; its underlying higher category is $\iota_1\circ\widetilde C$.
:::

::: {#def-equality-of-objects}
## Equality, isomorphism, and equivalence

Definitional equality is judgmental equality in the chosen formal language.
An isomorphism in an ordinary category is a morphism with a two-sided inverse.
An equivalence is a morphism satisfying @def-equivalence-of-categories.

The notation $a=b$, $a\cong b$, and $a\simeq b$ records these three claims.
No univalence principle is assumed.
Chosen comparison maps are treated in [Equivalences and witnesses](Identification.md).
:::
