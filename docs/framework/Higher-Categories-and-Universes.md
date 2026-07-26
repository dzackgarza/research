# Higher categories and universes {#sec-higher-categories-universes}

::: {#def-universe}
## Universe fibrations

Work in an external cartesian closed $(\infty,\infty)$-category $\mathcal K$ with pullbacks and terminal object $*$.
Fix a monoidal closed $(\infty,\infty)$-category $\mathcal U$ internal to $\mathcal K$, and use its canonical self-enrichment.
Fix a universe fibration
$$
p_{\mathcal U}\colon\widetilde{\mathcal U}\longrightarrow\mathcal U.
$$
For a functor $F\colon B\to\mathcal U$, its category of elements is the cartesian pullback
\begin{tikzcd}
\displaystyle\int_BF
  \arrow[r]
  \arrow[d, "q_F"']
&
\widetilde{\mathcal U}
  \arrow[d, "p_{\mathcal U}"]
\\
B
  \arrow[r, "F"']
  \arrow[ru, phantom, very near start, "\lrcorner"]
&
\mathcal U .
\end{tikzcd}
A morphism over $B$ is $\mathcal U$-small if it is equivalent over $B$ to $q_F$ for some $F\colon B\to\mathcal U$.
The fibration $p_{\mathcal U}$ classifies these morphisms: base change induces an equivalence from $[B,\mathcal U]_{\mathcal K}$ to the replete full subcategory of $\mathcal K_{/B}$ on the $\mathcal U$-small morphisms.
For a point $h_A\colon *\to\mathcal U$, write
$$
A:=\int_*h_A.
$$
A point of the decoded object $A$ is a functor $a\colon *\to A$.
For points $x,y\colon *\to\mathcal U$, the self-enriched hom functor supplies a classifying point
$$
h_{[x,y]_{\mathcal U}}:=[-,-]_{\mathcal U}\circ(x,y)\colon *\longrightarrow\mathcal U,
$$
and its decoded internal hom-object is
$$
[x,y]_{\mathcal U}:=\int_*h_{[x,y]_{\mathcal U}}.
$$
The same definition applies to every decoded object, while a point of $\mathcal U$ is a functor $a\colon *\to\mathcal U$ in $\mathcal K$.
The size convention and the universe fibration are interpreted in the fixed external category $\mathcal K$.
:::

::: {#def-higher-category}
## The category of higher categories

Choose a point
$$
h_{\mathcal V}\colon *\longrightarrow\mathcal U
$$
and write
$$
\mathbf{Cat}_{\infty,\infty}
:=
\int_*h_{\mathcal V}.
$$
Equip $\mathbf{Cat}_{\infty,\infty}$ with a universe fibration
$$
p_{\mathcal V}\colon
\widetilde{\mathbf{Cat}}_{\infty,\infty}
\longrightarrow
\mathbf{Cat}_{\infty,\infty}.
$$
A higher category is a point
$$
h_C\colon *\longrightarrow\mathbf{Cat}_{\infty,\infty}.
$$
Its decoded higher category is the category of elements
\begin{tikzcd}
C:=\displaystyle\int_*h_C
  \arrow[r]
  \arrow[d]
&
\widetilde{\mathbf{Cat}}_{\infty,\infty}
  \arrow[d, "p_{\mathcal V}"]
\\
*
  \arrow[r, "h_C"']
  \arrow[ru, phantom, very near start, "\lrcorner"]
&
\mathbf{Cat}_{\infty,\infty}.
\end{tikzcd}
An object of $C$ is a point
$$
x\colon *\longrightarrow C.
$$
:::

::: {#def-grothendieck-construction}
## Families and their points

For a functor
$$
F\colon B\longrightarrow\mathbf{Cat}_{\infty,\infty},
$$
define $\int_BF\to B$ by pulling back $p_{\mathcal V}$ along $F$.
For a point $b\colon *\to B$, the fiber of $\int_BF\to B$ over $b$ is $\int_* (F\circ b)$.
A point of the family $F$ over $b$ is a point
$$
x\colon *\longrightarrow\int_*(F\circ b).
$$
For $B=*$ and $F=h_C$, this recovers the points $x\colon *\to C$ of @def-higher-category [@nlab:grothendieck_construction].
:::

::: {#def-internal-hom}
## Local hom-objects

For every decoded higher category $C$ and points $x,y\colon *\to C$, fix a classifying point
$$
h_{[x,y]_C}\colon
*
\longrightarrow
\mathbf{Cat}_{\infty,\infty}
$$
and write
$$
[x,y]_C:=\int_*h_{[x,y]_C}.
$$
These hom-objects form a bifunctor
$$
[-,-]_C\colon
C^{\mathrm{op}}\times C
\longrightarrow
\mathbf{Cat}_{\infty,\infty}.
$$
Its value at $(x,y)$ is the classifying point $h_{[x,y]_C}$.
They have identity points
$$
\operatorname{id}_x\colon *\longrightarrow[x,x]_C
$$
and composition functors
$$
[y,z]_C\times[x,y]_C
\longrightarrow
[x,z]_C.
$$
The associativity and unit cells and their higher coherences are part of the $(\infty,\infty)$-categorical structure.

For higher categories classified by $h_C,h_D\colon *\to\mathbf{Cat}_{\infty,\infty}$, let
$$
h_{[C,D]_{\mathbf{Cat}_{\infty,\infty}}}
:=
[-,-]_{\mathbf{Cat}_{\infty,\infty}}\circ(h_C,h_D)
\colon *\longrightarrow\mathbf{Cat}_{\infty,\infty}
$$
be the classifying point supplied by the local hom bifunctor, and write
$$
[C,D]_{\mathbf{Cat}_{\infty,\infty}}
:=
\int_*h_{[C,D]_{\mathbf{Cat}_{\infty,\infty}}}
$$
for the decoded functor higher category. Its points are functors $C\to D$.
For higher categories $A,C,D$, closedness gives
$$
[A\times C,D]_{\mathbf{Cat}_{\infty,\infty}}
\simeq
[A,[C,D]_{\mathbf{Cat}_{\infty,\infty}}]_{\mathbf{Cat}_{\infty,\infty}}.
$$
:::

::: {#def-cells}
## Higher cells

A $0$-cell of $C$ is a point $x\colon *\to C$.
For $0$-cells $x,y$, a $1$-cell is a point
$$
f\colon *\longrightarrow[x,y]_C.
$$
For parallel $1$-cells $f,g$, a $2$-cell is a point
$$
\alpha\colon
*
\longrightarrow
[f,g]_{[x,y]_C}.
$$
For parallel $2$-cells $\alpha,\beta$, a $3$-cell is a point
$$
\Gamma\colon
*
\longrightarrow
[\alpha,\beta]_{[f,g]_{[x,y]_C}}.
$$
Iterating the same point and local hom-object constructions defines all higher cells.
:::

::: {#def-equivalence-of-categories}
## Equivalences

A *structure of reversibility* is a family $\mathscr R$ of positive-dimensional cells in the iterated hom-objects such that, for every cell
$$
f\colon *\longrightarrow[x,y]_C
$$
in $\mathscr R$, there is a cell
$$
g\colon *\longrightarrow[y,x]_C
$$
in $\mathscr R$ and cells
$$
\eta\colon
*
\longrightarrow
[g\circ f,\operatorname{id}_x]_{[x,x]_C},
\qquad
\epsilon\colon
*
\longrightarrow
[f\circ g,\operatorname{id}_y]_{[y,y]_C}
$$
in $\mathscr R$.
A cell is *invertible* if it belongs to a structure of reversibility [@OR23, Definition 1.5.1].

An equivalence between higher categories $C$ and $D$ is an invertible point
$$
F\colon
*
\longrightarrow
[C,D]_{\mathbf{Cat}_{\infty,\infty}}.
$$
Write $C\simeq D$ when such an equivalence has been chosen.
:::

::: {#def-core}
## Underlying homotopy type and core

Let $\mathcal S=\mathbf{Types}$ and let
$$
i\colon\mathcal S\hookrightarrow\mathbf{Cat}_{\infty,\infty}
$$
be the full inclusion of groupoidal higher categories.
Assume the adjunctions
$$
\Pi_\infty\dashv i\dashv(-)^\simeq.
$$
The left adjoint
$$
\Pi_\infty\colon\mathbf{Cat}_{\infty,\infty}\longrightarrow\mathcal S
$$
is the underlying homotopy type obtained by inverting every morphism.
The right adjoint $C\mapsto C^\simeq$ is the core obtained by retaining every object and only the equivalences [@Lur26, Tags 01DQ and 02F5].
:::


::: {#def-bicomplete-cat-infinity}
## Limits, loops, and suspensions

The higher category $\mathbf{Cat}_{\infty,\infty}$ has an initial object $\varnothing$ and a terminal object $*$, and it is bicomplete.
For a pointed higher category $(X,x)$, where $x\colon *\to X$, define
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
((*\amalg *)\downarrow\operatorname{id}_{\mathbf{Cat}_{\infty,\infty}}).
$$
Its objects are morphisms
$$
x_0\amalg x_1\colon *\amalg *\longrightarrow X.
$$
The endpoint hom functor is
$$
\Omega_{01}\colon
((*\amalg *)\downarrow\operatorname{id}_{\mathbf{Cat}_{\infty,\infty}})
\longrightarrow\mathbf{Cat}_{\infty,\infty},
\qquad
(X;x_0,x_1)\longmapsto[x_0,x_1]_X.
$$
Assume that $\Omega_{01}$ has a left adjoint
$$
B_{01}\dashv\Omega_{01}.
$$
For a higher category $A=\int_*h_A$, the bipointed higher category $B_{01}A$ has distinguished objects $0,1$ and hom-objects displayed by
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

::: {#def-walking-arrow}
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
For a higher category $C$, the hom-object
$$
[[n],C]_{\mathbf{Cat}_{\infty,\infty}}
$$
is the higher category of functors $[n]\to C$ and their higher cells.
:::

::: {#def-mapping-spaces}
## Walking-arrow presentation and mapping types

Precomposition with $s$ and $t$ gives
$$
(s^*,t^*)\colon
[[1],C]_{\mathbf{Cat}_{\infty,\infty}}
\longrightarrow
[[0],C]_{\mathbf{Cat}_{\infty,\infty}}
\times
[[0],C]_{\mathbf{Cat}_{\infty,\infty}}
\simeq
C\times C.
$$
For points $x,y\colon*\to C$, the local hom-object $[x,y]_C$ is the cartesian fiber
\begin{tikzcd}
{[x,y]_C}
  \arrow[r]
  \arrow[d]
&
{[[1],C]_{\mathbf{Cat}_{\infty,\infty}}}
  \arrow[d, "{(s^*,t^*)}"]
\\
*
  \arrow[r, "{(x,y)}"']
  \arrow[ru, phantom, very near start, "\lrcorner"]
&
C\times C.
\end{tikzcd}
Its underlying mapping type is
$$
\operatorname{Map}_C(x,y):=\Pi_\infty[x,y]_C.
$$
Likewise,
$$
\operatorname{Map}_{\mathbf{Cat}_{\infty,\infty}}(C,D)
:=
\Pi_\infty[C,D]_{\mathbf{Cat}_{\infty,\infty}}.
$$
:::

::: {#def-initial-terminal}
## Initial, terminal, and contractible objects

An object $t\colon*\to C$ is terminal if $\operatorname{Map}_C(x,t)$ is contractible for every $x\colon*\to C$.
An object $i\colon*\to C$ is initial if $\operatorname{Map}_C(i,x)$ is contractible for every $x\colon*\to C$.
A higher category is *contractible* when it is equivalent to $*$.
:::

::: {#def-truncated}
## Truncated objects and morphisms

Let $C$ be a higher category.
For an integer $n\geq-2$, an object $X\colon*\to C$ is *$n$-truncated* if $\operatorname{Map}_C(Y,X)$ is an $n$-truncated type for every $Y\colon*\to C$.
The $(-2)$-truncated objects are the terminal objects.

For an object $Y\colon*\to C$, write $C_{/Y}:=(\operatorname{id}_C\downarrow Y)$ for the slice. A morphism $f\colon X\to Y$ is *$n$-truncated* if it is an $n$-truncated object of $C_{/Y}$.
Equivalently, for every $Z\colon*\to C$ and every point of $\operatorname{Map}_C(Z,Y)$, the corresponding fiber of
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
T_{\leq n}\colon
\mathbf{Cat}_{\infty,\infty}
\longrightarrow
\mathbf{Cat}_{\infty,\infty}.
$$
Define
$$
\mathbf{Cat}_n
:=\operatorname{EssIm}(T_{\leq n})
=:T_{\leq n}\mathbf{Cat}_{\infty,\infty}.
$$
Let
$$
\iota_n\colon
\mathbf{Cat}_n
\longrightarrow
\mathbf{Cat}_{\infty,\infty}
$$
be the full inclusion, and write
$$
\tau_{\leq n}\colon
\mathbf{Cat}_{\infty,\infty}
\longrightarrow
\mathbf{Cat}_n
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
\mathbf{Cat}_{\infty,\infty}.
$$
An *$n$-category structure* on a higher category $C=\int_*h_C$ is a lift
\begin{tikzcd}
&
\mathbf{Cat}_n
  \arrow[d, "\iota_n"]
\\
*
  \arrow[ur, "\widetilde h_C"]
  \arrow[r, "h_C"']
&
\mathbf{Cat}_{\infty,\infty}
\end{tikzcd}
together with a specified equivalence $\iota_n\circ\widetilde h_C\simeq h_C$.

For $n\geq0$, a second construction begins with the full replete subcategory
$$
\mathbf{Cat}_n^{\mathrm{loc}}
\subseteq
\mathbf{Cat}_{\infty,\infty}
$$
on the locally $(n-1)$-truncated higher categories [@Lur26, Tag 05EA].
Its inclusion supplies $\iota_n$ after an equivalence $\mathbf{Cat}_n^{\mathrm{loc}}\simeq\mathbf{Cat}_n$ has been established.
Its left and right adjoints, when they exist, supply $\tau_{\leq n}$ and $\tau_{\leq n}^{\mathrm R}$.

For higher categories $C,D$, define
$$
[C,D]_{\mathbf{Cat}_{\infty,\infty}}^{\leq n}
\hookrightarrow
[C,D]_{\mathbf{Cat}_{\infty,\infty}}
$$
to be the full replete subcategory on the $n$-truncated objects of $[C,D]_{\mathbf{Cat}_{\infty,\infty}}$.
These objects are the $n$-truncated morphisms $C\to D$ internal to the mapping higher category.
:::


::: {#def-ordinary-category-specialization}
## Ordinary categories

An *ordinary-category structure* on a higher category $C=\int_*h_C$ is a $1$-category structure on $C$: a point
$$
\widetilde h_C\colon*\longrightarrow\mathbf{Cat}_1
$$
together with a specified equivalence $\iota_1\circ\widetilde h_C\simeq h_C$.
An ordinary category may be presented by the point $\widetilde h_C$; its underlying higher category is decoded from $\iota_1\circ\widetilde h_C$.
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
