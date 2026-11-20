# Higher categories and universes {#sec-higher-categories-universes}

::: {.definition #def:universe title="Universe and decoded objects" defines="$\mcu$-small morphism; decoded object; decoding functor $\operatorname{Dec}_{\mcu}$; $[x,y]_{\mcu}$"}

Work in an external cartesian closed (@def:closed-monoidal) $(\infty,\infty)$-category $\mck$ with pullbacks (@def:pullback-square) and terminal object (@def:initial-terminal) $*$.
Fix a monoidal closed $(\infty,\infty)$-category $\mcu$ internal to $\mck$, and use its canonical self-enrichment.
Fix a universe fibration
$$
p_{\mcu}\colon\widetilde{\mcu}\too\mcu.
$$
A morphism $q\colon E\to B$ in $\mck$ is *$\mcu$-small* if there is an arrow $\chi_q\colon B\to\mcu$ and a cartesian square

\begin{tikzcd}
E
  \arrow[r, "\widetilde\chi_q"]
  \arrow[d, "q"']
&
\widetilde{\mathcal U}
  \arrow[d, "p_{\mathcal U}"]
\\
B
  \arrow[r, "\chi_q"']
  \arrow[ru, phantom, very near start, "\lrcorner"]
&
\mathcal U.
\end{tikzcd}

The universe fibration classifies these morphisms: base change (@def:module-base-change) induces an equivalence (@def:equivalence-of-objects) of higher categories
$$
[B,\mcu]_{\mck}
\simeq
\mck^{\mcu\text{-small}}_{/B},
$$
where the right-hand side is the replete (@def:subcategory) full higher subcategory of $\mck_{/B}$ on the $\mcu$-small morphisms.

For a point $h_A\colon *\to\mcu$, define its decoded object by the cartesian square

\begin{tikzcd}
A:=\displaystyle\int_*h_A
  \arrow[r, "\widetilde h_A"]
  \arrow[d, "!_A"']
&
\widetilde{\mathcal U}
  \arrow[d, "p_{\mathcal U}"]
\\
*
  \arrow[r, "h_A"']
  \arrow[ru, phantom, very near start, "\lrcorner"]
&
\mathcal U.
\end{tikzcd}

Assume that these pullbacks extend to a decoding functor
$$
\operatorname{Dec}_{\mcu}\colon\mcu\too\mck,
\qquad
\operatorname{Dec}_{\mcu}(h_A)=A,
$$
which preserves the base-change squares used below.
An object of the internal category $\mcu$ is specified by a point $b\colon *\to\mcu$; below the same symbol $b$ denotes that internal object, while $\operatorname{Dec}_{\mcu}(b)$ denotes its external decoding in $\mck$.
A point of $A$ is a $1$-cell $a\colon *\to A$ in $\mck$.

For points $x,y\colon *\to\mcu$, the self-enriched hom functor supplies a classifying point
$$
h_{[x,y]_{\mcu}}:=[-,-]_{\mcu}(x,y)\colon *\too\mcu.
$$
Its external decoding, denoted $[x,y]_{\mcu}$, is defined by the cartesian square

\begin{tikzcd}
{\displaystyle [x,y]_{\mathcal U}:=\int_*h_{[x,y]_{\mathcal U}}}
  \arrow[r, "\widetilde h_{[x,y]_{\mathcal U}}"]
  \arrow[d, "!_{[x,y]_{\mathcal U}}"']
&
\widetilde{\mathcal U}
  \arrow[d, "p_{\mathcal U}"]
\\
*
  \arrow[r, "h_{[x,y]_{\mathcal U}}"']
  \arrow[ru, phantom, very near start, "\lrcorner"]
&
\mathcal U.
\end{tikzcd}

The size convention, the universe fibration, and the decoding functor are interpreted in the fixed external category $\mck$.
:::

::: {.definition #def:family-classifier title="Families and classifiers" defines="family over $b$; decoded arrow; $G^{\sharp}$; $\mathcal M$-family over $b$; $\mathcal M(b)$; classifier for $\mathcal M$"}

For points $b,c\colon *\to\mcu$, a *family over $b$* is a $1$-cell
$$
G\colon c\too b
$$
in $\mcu$.
Equivalently, it is a point $g\colon *\to[c,b]_{\mcu}$.
Writing $B:=\operatorname{Dec}_{\mcu}(b)$ and $C:=\operatorname{Dec}_{\mcu}(c)$, its decoded arrow is
$$
G^{\sharp}:=\operatorname{Dec}_{\mcu}(G)\colon C\too B.
$$
Let $\mathcal M$ be a replete (@def:subcategory) class of $1$-cells in $\mcu$ that is stable under base change (@def:module-base-change).
An *$\mathcal M$-family over $b$* is a family $G\colon c\to b$ that belongs to $\mathcal M$.
Write $\mathcal M(b)$ for the replete full higher subcategory of $\mcu_{/b}$ on the $\mathcal M$-families.

A *classifier for $\mathcal M$* is a $1$-cell
$$
p_{\mathcal M}\colon e_{\mathcal M}\too b_{\mathcal M}
$$
for which base change induces an equivalence (@def:equivalence-of-objects)
$$
[b,b_{\mathcal M}]_{\mcu}
\simeq
\mathcal M(b)
$$
naturally in $b$.
Explicitly, an $\mathcal M$-family $G\colon c\to b$ corresponds to a classifying $1$-cell $F\colon b\to b_{\mathcal M}$ and a cartesian square in $\mcu$

\begin{tikzcd}
c
  \arrow[r, "\widetilde F"]
  \arrow[d, "G"']
&
e_{\mathcal M}
  \arrow[d, "p_{\mathcal M}"]
\\
b
  \arrow[r, "F"']
  \arrow[ru, phantom, very near start, "\lrcorner"]
&
b_{\mathcal M}.
\end{tikzcd}

The representing equivalence includes arrows and all higher cells (@def:cells) between families, not only the existence of $F$.
:::

::: {.definition #def:higher-category title="The category of higher categories" defines="$\mathbf{Cat}_{\infty,\infty}$; $\widetilde{\mathbf{Cat}}_{\infty,\infty}$; $p_{\mathcal V}$; higher category; decoded higher category"}

Let $\mathcal M_{\mathrm{cocart}}$ be the replete (@def:subcategory) base-change-stable class of $1$-cells $G$ in $\mcu$ for which $\operatorname{Dec}_{\mcu}(G)$ is a $\mcu$-small cocartesian fibration in $\mck$.
Assume that it has a classifier
$$
p_{\mathcal M_{\mathrm{cocart}}}\colon
e_{\mathcal M_{\mathrm{cocart}}}
\too
b_{\mathcal M_{\mathrm{cocart}}}.
$$
Use the classifier objects as the internal codes
$$
h_{\mathbf{Cat}_{\infty,\infty}}
:=b_{\mathcal M_{\mathrm{cocart}}},
\qquad
h_{\widetilde{\mathbf{Cat}}_{\infty,\infty}}
:=e_{\mathcal M_{\mathrm{cocart}}}.
$$
Define their external decodings by
$$
\mathbf{Cat}_{\infty,\infty}
:=\operatorname{Dec}_{\mcu}(b_{\mathcal M_{\mathrm{cocart}}}),
\qquad
\widetilde{\mathbf{Cat}}_{\infty,\infty}
:=\operatorname{Dec}_{\mcu}(e_{\mathcal M_{\mathrm{cocart}}}).
$$
These decodings are exhibited by the cartesian squares

\begin{tikzcd}
\mathbf{Cat}_{\infty,\infty}
  \arrow[r, "\widetilde h_{\mathbf{Cat}_{\infty,\infty}}"]
  \arrow[d, "!_{\mathbf{Cat}_{\infty,\infty}}"']
&
\widetilde{\mathcal U}
  \arrow[d, "p_{\mathcal U}"]
\\
*
  \arrow[r, "h_{\mathbf{Cat}_{\infty,\infty}}"']
  \arrow[ru, phantom, very near start, "\lrcorner"]
&
\mathcal U
\end{tikzcd}

and

\begin{tikzcd}
\widetilde{\mathbf{Cat}}_{\infty,\infty}
  \arrow[r, "\widetilde h_{\widetilde{\mathbf{Cat}}_{\infty,\infty}}"]
  \arrow[d, "!_{\widetilde{\mathbf{Cat}}_{\infty,\infty}}"']
&
\widetilde{\mathcal U}
  \arrow[d, "p_{\mathcal U}"]
\\
*
  \arrow[r, "h_{\widetilde{\mathbf{Cat}}_{\infty,\infty}}"']
  \arrow[ru, phantom, very near start, "\lrcorner"]
&
\mathcal U.
\end{tikzcd}

Decode the universal classifier to obtain
$$
p_{\mcv}
:=
\operatorname{Dec}_{\mcu}(p_{\mathcal M_{\mathrm{cocart}}})
\colon
\widetilde{\mathbf{Cat}}_{\infty,\infty}
\too
\mathbf{Cat}_{\infty,\infty}.
$$
The representing equivalence (@def:equivalence-of-objects) determines $h_{\mathbf{Cat}_{\infty,\infty}}$, and hence $\mathbf{Cat}_{\infty,\infty}$, up to equivalence as the classifier of small cocartesian families.

A higher category is a point
$$
h_C\colon *\too\mathbf{Cat}_{\infty,\infty}.
$$
Its decoded higher category is defined by the cartesian square

\begin{tikzcd}
C:=\displaystyle\int_*h_C
  \arrow[r, "\widetilde h_C"]
  \arrow[d, "!_C"']
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

An object of $C$ is a point $x\colon *\to C$.
When $C=\mathbf{Cat}_{\infty,\infty}$, such a point is itself the classifying point of a higher category, which is decoded by the same pullback (@def:pullback-square).
More generally, a functor $R\colon C\to\mathbf{Cat}_{\infty,\infty}$ sends a point $x\colon *\to C$ to the classifying point $R\circ x$ of a higher category.
:::

::: {.definition #def:grothendieck-construction title="Categorical families and categories of elements" defines="$F^{\sharp}$; $\int_B F^{\sharp}$; fiber over $s$"}

Let $G\colon c\to b$ be a family in $\mcu$, and write
$$
C:=\operatorname{Dec}_{\mcu}(c),
\qquad
B:=\operatorname{Dec}_{\mcu}(b),
\qquad
G^{\sharp}:=\operatorname{Dec}_{\mcu}(G)\colon C\to B.
$$
It is an $\mathcal M_{\mathrm{cocart}}$-family precisely when it corresponds to a classifying $1$-cell
$$
F\colon b\too b_{\mathcal M_{\mathrm{cocart}}}.
$$
Write
$$
F^{\sharp}:=\operatorname{Dec}_{\mcu}(F)
\colon B\too\mathbf{Cat}_{\infty,\infty}.
$$
Define its category of elements (@def:category-of-elements) by the cartesian square

\begin{tikzcd}
\displaystyle\int_BF^{\sharp}
  \arrow[r, "\widetilde F^{\sharp}"]
  \arrow[d, "q_{F^{\sharp}}"']
&
\widetilde{\mathbf{Cat}}_{\infty,\infty}
  \arrow[d, "p_{\mathcal V}"]
\\
B
  \arrow[r, "F^{\sharp}"']
  \arrow[ru, phantom, very near start, "\lrcorner"]
&
\mathbf{Cat}_{\infty,\infty}.
\end{tikzcd}

Decoding the classifier square identifies $G^{\sharp}$ with $q_{F^{\sharp}}$ over $B$, and hence identifies
$$
C\simeq_B\int_BF^{\sharp}.
$$
For a point $s\colon *\to B$, the fiber (@def:fiber-cofiber) over $s$ is $\int_*(F^{\sharp}\circ s)$.
A point of the family over $s$ is a point
$$
x\colon *\too\int_*(F^{\sharp}\circ s).
$$
For $B=*$ and $F^{\sharp}=h_C$, this recovers the points $x\colon *\to C$ of @def:higher-category and [@nlab:grothendieck_construction].
:::

::: {.definition #def:internal-hom title="Local hom-objects" defines="local hom-object; $[x,y]_C$; hom bifunctor $[-,-]_C$; identity point $\id_x$; composition functor; functor higher category $[C,D]_{\mathbf{Cat}_{\infty,\infty}}$"}

For every decoded higher category (@def:higher-category) $C$ and points $x,y\colon *\to C$, fix a classifying point
$$
h_{[x,y]_C}\colon
*
\too
\mathbf{Cat}_{\infty,\infty}
$$
and write
$$
[x,y]_C:=\int_*h_{[x,y]_C}.
$$
These hom-objects form a bifunctor
$$
[-,-]_C\colon
C^{\opop}\times C
\too
\mathbf{Cat}_{\infty,\infty}.
$$
Its value at $(x,y)$ is the classifying point $h_{[x,y]_C}$.
They have identity points
$$
\id_x\colon *\too[x,x]_C
$$
and composition functors
$$
[y,z]_C\times[x,y]_C
\too
[x,z]_C.
$$
The associativity and unit cells and their higher coherences are part of the $(\infty,\infty)$-categorical structure (@def:property-structure-stuff).

For higher categories classified by $h_C,h_D\colon *\to\mathbf{Cat}_{\infty,\infty}$, let
$$
h_{[C,D]_{\mathbf{Cat}_{\infty,\infty}}}
:=
[-,-]_{\mathbf{Cat}_{\infty,\infty}}\circ(h_C,h_D)
\colon *\too\mathbf{Cat}_{\infty,\infty}
$$
be the classifying point supplied by the local hom bifunctor, and write
$$
[C,D]_{\mathbf{Cat}_{\infty,\infty}}
:=
\int_*h_{[C,D]_{\mathbf{Cat}_{\infty,\infty}}}
$$
for the decoded functor higher category (@def:higher-category).
Its points are functors $C\to D$.
For higher categories $A,C,D$, closedness gives
$$
[A\times C,D]_{\mathbf{Cat}_{\infty,\infty}}
\simeq
[A,[C,D]_{\mathbf{Cat}_{\infty,\infty}}]_{\mathbf{Cat}_{\infty,\infty}}.
$$
:::

::: {.definition #def:cells title="Higher cells" defines="$0$-cell; $1$-cell; $2$-cell; $3$-cell; higher cell"}

A $0$-cell of $C$ is a point $x\colon *\to C$.
For $0$-cells $x,y$, a $1$-cell is a point
$$
f\colon *\too[x,y]_C.
$$
For parallel $1$-cells $f,g$, a $2$-cell is a point
$$
\alpha\colon
*
\too
[f,g]_{[x,y]_C}.
$$
For parallel $2$-cells $\alpha,\beta$, a $3$-cell is a point
$$
\Gamma\colon
*
\too
[\alpha,\beta]_{[f,g]_{[x,y]_C}}.
$$
Iterating the same point and local hom-object (@def:internal-hom) constructions defines all higher cells.
:::

::: {.proposition #prop:iterated-hom-cells title="Cells of an iterated hom-object"}

Write $[x,y]^{(1)}_C:=[x,y]_C$ and, for a choice of parallel $k$-cells $u,v$ of $C$, write $[u,v]^{(k+1)}_C$ for the local hom-object formed at the $k$-th stage of @def:cells.
By construction the $n$-cells of $[u,v]^{(k)}_C$ are the $(n+k)$-cells of $C$ that are parallel over the chosen $u,v$; in particular its $0$-cells are the $k$-cells of $C$ between them.
Passing from $C$ to a local hom-object therefore lowers the dimension of every cell by one, and its adjoint (@def:adjoint-morphism) direction is $B_{01}\dashv\Omega_{01}$ (@def:B01-construction).
:::

::: {.proof}

Apply the adjunction characterizing the internal hom (@def:closed-monoidal) (@def:internal-hom) twice and the universal property (@def:property-structure-stuff) of the coproduct.
:::

::: {.definition #def:globular-boundary title="Sources and targets" defines="source; target"}

A $1$-cell $f\colon *\to[x,y]_C$ has *source* $x$ and *target* $y$; an $(n+1)$-cell, being a $1$-cell of an iterated hom-object $[u,v]^{(n)}_C$, has source $u$ and target $v$.
Source and target are defined for cells of positive dimension only, and $0$-cells have neither.
For every cell of dimension at least $2$,
$$
s(s(\xi))=s(t(\xi)),
\qquad
t(s(\xi))=t(t(\xi)),
$$
since $s(\xi)$ and $t(\xi)$ are parallel cells of the same iterated hom-object.
:::

::: {.definition #def:equivalence-of-categories title="Equivalences" defines="structure of reversibility; invertible cell; $C\simeq D$"}

A *structure of reversibility* is a family $\mcr$ of positive-dimensional cells in the iterated hom-objects such that, for every cell
$$
f\colon *\too[x,y]_C
$$
in $\mcr$, there is a cell
$$
g\colon *\too[y,x]_C
$$
in $\mcr$ and cells
$$
\eta\colon
*
\too
[g\circ f,\id_x]_{[x,x]_C},
\qquad
\epsilon\colon
*
\too
[f\circ g,\id_y]_{[y,y]_C}
$$
in $\mcr$.
A cell is *invertible* if it belongs to a structure of reversibility [@OR23, Definition 1.5.1].

An equivalence (@def:equivalence-of-objects) between higher categories $C$ and $D$ is an invertible point
$$
F\colon
*
\too
[C,D]_{\mathbf{Cat}_{\infty,\infty}}.
$$
Write $C\simeq D$ when such an equivalence has been chosen.
:::

::: {.definition #def:core title="Underlying homotopy type and core" defines="underlying homotopy type; $\Pi_\infty$; core; $C^{\simeq}$"}

Let $\mcs=\mathbf{Types}$ and let
$$
i\colon\mcs\hookrightarrow\mathbf{Cat}_{\infty,\infty}
$$
be the full inclusion of groupoidal higher categories.
Assume the adjunctions
$$
\Pi_\infty\dashv i\dashv(-)^\simeq.
$$
The left adjoint (@def:pairing-adjoints)
$$
\Pi_\infty\colon\mathbf{Cat}_{\infty,\infty}\too\mcs
$$
is the underlying homotopy type obtained by inverting every morphism.
The right adjoint (@def:pairing-adjoints) $C\mapsto C^\simeq$ is the core obtained by retaining every object and only the equivalences (@def:equivalence-of-objects) [@Lur18c, Tags 01DQ and 02F5].
:::

::: {.definition #def:bicomplete-cat-infinity title="Limits, loops, and suspensions" defines="loop object; $\Omega_xX$; $\Sigma A$"}

The higher category (@def:higher-category) $\mathbf{Cat}_{\infty,\infty}$ has an initial object (@def:initial-terminal) $\varnothing$ and a terminal object (@def:initial-terminal) $*$, and it is bicomplete (@def:complete).
For a pointed higher category $(X,x)$, where $x\colon *\to X$, define
$$
\Omega_xX:=*\times_X*.
$$
For a higher category $A$, define its suspension (@def:loops-suspension) by the pushout

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

::: {.definition #def:spheres title="Spheres" defines="sphere; $S^{-1}$; $S^{n}$"}

Define
$$
S^{-1}:=\varnothing,
\qquad
S^{n}:=\Sigma S^{n-1}\quad(n\geq0).
$$
Since the pushout (@def:pullback-square) of $*\from\varnothing\to*$ is the coproduct, $S^{0}=*\amalg*$, the bipointed object indexing the comma category (@def:comma-category) of @def:B01-construction.
:::

::: {.example #ex:initial-terminal-cat title="The initial and terminal higher categories"}

Closedness makes $-\times C$ a left adjoint (@def:internal-hom), so it preserves colimits and in particular the initial object:
$$
\varnothing\times C\simeq\varnothing,
\qquad
*\times C\simeq C,
\qquad
\varnothing\amalg C\simeq C.
$$
For hom-objects, $[\varnothing,C]\simeq*$ for every $C$, since $\varnothing$ is initial; $[C,\varnothing]\simeq\varnothing$ whenever $C$ has a point, since evaluating a point of $[C,\varnothing]$ at a point of $C$ would give a point of $\varnothing$, and a higher category with no points is $\varnothing$; and $[\varnothing,\varnothing]\simeq*$.
The coproduct $*\amalg*$ is neither initial nor terminal, so $\mathbf{Cat}_{\infty,\infty}$ has no zero object.
:::

::: {.definition #def:B01-construction title="The $B_{01}$ construction" defines="bipointed higher category; endpoint hom functor; $\Omega_{01}$; $B_{01}$"}

The higher category (@def:higher-category) of bipointed higher categories is the comma category (@def:comma-category)
$$
((*\amalg *)\downarrow\id_{\mathbf{Cat}_{\infty,\infty}}).
$$
Its objects are morphisms
$$
x_0\amalg x_1\colon *\amalg *\too X.
$$
The endpoint hom functor is
$$
\Omega_{01}\colon
((*\amalg *)\downarrow\id_{\mathbf{Cat}_{\infty,\infty}})
\too\mathbf{Cat}_{\infty,\infty},
\qquad
(X;x_0,x_1)\longmapsto[x_0,x_1]_X.
$$
Assume that $\Omega_{01}$ has a left adjoint (@def:pairing-adjoints)
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
The suspension (@def:loops-suspension) $\Sigma A$ is the pushout (@def:pullback-square) in @def:bicomplete-cat-infinity.
The object $B_{01}A$ is characterized by the adjunction $B_{01}\dashv\Omega_{01}$.
:::

::: {.definition #def:walking-arrow title="Walking arrows and ordinal categories" defines="$[0]$; $[1]$; $s$; $t$; ordinal category $[n]$; walking chain"}

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
where each pushout (@def:pullback-square) identifies the target (@def:globular-boundary) of one copy with the source (@def:globular-boundary) of the next.
For a higher category (@def:higher-category) $C$, the hom-object
$$
[[n],C]_{\mathbf{Cat}_{\infty,\infty}}
$$
is the higher category of functors $[n]\to C$ and their higher cells (@def:cells).
:::

::: {.definition #def:mapping-spaces title="Walking-arrow presentation and mapping types" defines="underlying mapping type; $\operatorname{Map}_C(x,y)$; $\operatorname{Map}_{\mathbf{Cat}_{\infty,\infty}}(C,D)$"}

Precomposition with $s$ and $t$ gives
$$
(s^*,t^*)\colon
[[1],C]_{\mathbf{Cat}_{\infty,\infty}}
\too
[[0],C]_{\mathbf{Cat}_{\infty,\infty}}
\times
[[0],C]_{\mathbf{Cat}_{\infty,\infty}}
\simeq
C\times C.
$$
For points $x,y\colon*\to C$, the local hom-object (@def:internal-hom) $[x,y]_C$ is the cartesian fiber

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

::: {.definition #def:initial-terminal title="Initial, terminal, and contractible objects" defines="terminal object; initial object; contractible higher category"}

An object $t\colon*\to C$ is terminal (@def:terminal-coble-surface) if $\operatorname{Map}_C(x,t)$ is contractible for every $x\colon*\to C$.
An object $i\colon*\to C$ is initial if $\operatorname{Map}_C(i,x)$ is contractible for every $x\colon*\to C$.
A higher category (@def:higher-category) is *contractible* when it is equivalent to $*$.
:::

::: {.definition #def:truncated title="Truncated objects and morphisms" defines="$n$-truncated object; $C_{/Y}$; $n$-truncated morphism; $n$-truncated type; $\tau_{\leq n}^C$"}

Let $C$ be a higher category (@def:higher-category).
For an integer $n\geq-2$, an object $X\colon*\to C$ is *$n$-truncated* if $\operatorname{Map}_C(Y,X)$ is an $n$-truncated type for every $Y\colon*\to C$.
The $(-2)$-truncated objects are the terminal objects (@def:initial-terminal).

For an object $Y\colon*\to C$, write $C_{/Y}:=(\id_C\downarrow Y)$ for the slice.
A morphism $f\colon X\to Y$ is *$n$-truncated* if it is an $n$-truncated object of $C_{/Y}$.
Equivalently, for every $Z\colon*\to C$ and every point of $\operatorname{Map}_C(Z,Y)$, the corresponding fiber (@def:fiber-cofiber) of
$$
\operatorname{Map}_C(Z,X)
\too
\operatorname{Map}_C(Z,Y)
$$
is an $n$-truncated type.
A $(-2)$-truncated morphism is an equivalence (@def:equivalence-of-objects).
When the required pullback (@def:pullback-square) exists and $n\geq-1$, the recursive criterion is
$$
f\text{ is }n\text{-truncated}
\quad\Longleftrightarrow\quad
\Delta_f\colon X\too X\times_YX
\text{ is }(n-1)\text{-truncated}
$$
[@Lur18c, Tags 05F8 and 05FS].

For a type $S$, $n$-truncation means $\pi_k(S,s)=0$ for every point $s$ and every $k>n$.
A $(-2)$-truncated type is contractible, a $(-1)$-truncated type is empty or contractible, and a $0$-truncated type is a set.
When the inclusion of $n$-truncated objects of $C$ is reflective (@def:reflective-lattice), write its reflector as $\tau_{\leq n}^C$.
:::

::: {.definition #def:infinity-category-universe title="The truncation tower" defines="$T_{\leq n}$; $\mathbf{Cat}_n$; $\iota_n$; $\tau_{\leq n}$; $\tau_{\leq n}^{\mathrm R}$; $n$-category structure; $\mathbf{Cat}_n^{\mathrm{loc}}$; $[C,D]_{\mathbf{Cat}_{\infty,\infty}}^{\leq n}$"}

For each integer $n\geq-2$, assume an idempotent truncation endomorphism
$$
T_{\leq n}\colon
\mathbf{Cat}_{\infty,\infty}
\too
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
\too
\mathbf{Cat}_{\infty,\infty}
$$
be the full inclusion, and write
$$
\tau_{\leq n}\colon
\mathbf{Cat}_{\infty,\infty}
\too
\mathbf{Cat}_n
$$
for the corestriction of $T_{\leq n}$ to its essential image.
Assume
$$
\tau_{\leq n}\dashv\iota_n.
$$
If $\iota_n$ also has a right adjoint (@def:pairing-adjoints), write
$$
\iota_n\dashv\tau_{\leq n}^{\mathrm R}.
$$
The tower is
$$
\mathbf{Cat}_{-2}\too
\mathbf{Cat}_{-1}\too
\mathbf{Cat}_0\too
\mathbf{Cat}_1\too\cdots\too
\mathbf{Cat}_n\too\cdots\too
\mathbf{Cat}_{\infty,\infty}.
$$
An *$n$-category structure (@def:property-structure-stuff)* on a higher category (@def:higher-category) $C=\int_*h_C$ is a lift

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

together with a specified equivalence (@def:equivalence-of-objects) $\iota_n\circ\widetilde h_C\simeq h_C$.

For $n\geq0$, a second construction begins with the full replete (@def:subcategory) subcategory
$$
\mathbf{Cat}_n^{\mathrm{loc}}
\iscontainedin
\mathbf{Cat}_{\infty,\infty}
$$
on the locally $(n-1)$-truncated higher categories [@Lur18c, Tag 05EA].
Its inclusion supplies $\iota_n$ after an equivalence $\mathbf{Cat}_n^{\mathrm{loc}}\simeq\mathbf{Cat}_n$ has been established.
Its left and [right adjoints]{.other-sense}, when they exist, supply $\tau_{\leq n}$ and $\tau_{\leq n}^{\mathrm R}$.

For higher categories $C,D$, define
$$
[C,D]_{\mathbf{Cat}_{\infty,\infty}}^{\leq n}
\hookrightarrow
[C,D]_{\mathbf{Cat}_{\infty,\infty}}
$$
to be the full replete subcategory on the $n$-truncated objects of $[C,D]_{\mathbf{Cat}_{\infty,\infty}}$.
These objects are the $n$-truncated morphisms $C\to D$ internal to the mapping higher category.
:::

::: {.example #ex:low-levels title="The bottom of the tower"}

By @def:truncated the $(-2)$-truncated objects of $\mathbf{Cat}_{\infty,\infty}$ are its terminal objects, so $\mathbf{Cat}_{-2}$ is spanned by $*$ and is contractible.
Both $\varnothing$ and $*$ are $(-1)$-truncated: $\operatorname{Map}(Y,*)$ is contractible for every $Y$, and $\operatorname{Map}(Y,\varnothing)$ is empty unless $Y\simeq\varnothing$, in which case it is contractible.
So $\mathbf{Cat}_{-1}$ contains the two truth values $\varnothing$ and $*$, and the map $\mathbf{Cat}_{-2}\to\mathbf{Cat}_{-1}$ of the tower is the inclusion of $*$.
:::

::: {.definition #def:equivalence-of-objects title="Equivalence of objects" defines="equivalence; $\operatorname{Equiv}_C(X,Y)$; $X\simeq Y$"}

Let $C$ be a higher category (@def:higher-category) and let $X,Y\colon*\to C$ be objects.
A morphism $f\colon X\to Y$ is an *equivalence* if the cell $f\colon*\to[X,Y]_C$ is invertible in the sense of @def:equivalence-of-categories.
Let
$$
\operatorname{Equiv}_C(X,Y)\subseteq\operatorname{Map}_C(X,Y)
$$
be the union of the components that consist of equivalences.
Write $X\simeq Y$ for the claim that $\operatorname{Equiv}_C(X,Y)$ is nonempty.
:::

::: {.definition #def:isomorphism-of-objects title="Isomorphisms and $n$-equivalences" defines="$0$-equivalence; $n$-equivalence; isomorphism; $\operatorname{Equiv}_{C,n}(X,Y)$; $\operatorname{Isom}_C(X,Y)$; $X\simeq_n Y$; $X\cong Y$"}

Let $C$ be a higher category (@def:higher-category) and let $f\colon x\to y$ be a cell of $C$, with $x,y$ in an iterated hom-object of $C$.
Define the $n$-equivalences by induction on $n\geq0$ [@OR23, Definitions 1.1.8 and 1.4.3]:

- $f$ is a *$0$-equivalence* if there is a cell $g\colon y\to x$ with $g\circ f=\id_x$ and $f\circ g=\id_y$;
- for $n\geq1$, $f$ is an *$n$-equivalence* if there are a cell $g\colon y\to x$ and $(n-1)$-equivalences
$$
\eta\colon\id_x\too g\circ f\ \text{in}\ [x,x]_C,
\qquad
\epsilon\colon f\circ g\too\id_y\ \text{in}\ [y,y]_C.
$$

The cell $f$ is an *isomorphism* if there is a cell $g\colon y\to x$ with $g\circ f=\id_x$ and $f\circ g=\id_y$ such that, for every $n\geq1$, $g$ together with the identity cells $\eta=\id_{\id_x}$ and $\epsilon=\id_{\id_y}$ exhibits $f$ as an $n$-equivalence.

For objects $X,Y\colon*\to C$, let $\operatorname{Equiv}_{C,n}(X,Y)\subseteq\operatorname{Map}_C(X,Y)$ be the union of the components that consist of $n$-equivalences, and let
$$
\operatorname{Isom}_C(X,Y)\subseteq\bigcap_{n\geq0}\operatorname{Equiv}_{C,n}(X,Y)
$$
be the union of the components that consist of isomorphisms.
Write $X\simeq_n Y$ when $\operatorname{Equiv}_{C,n}(X,Y)$ is nonempty, and $X\cong Y$ when $\operatorname{Isom}_C(X,Y)$ is nonempty.
:::

::: {.definition #def:equality-of-objects title="Equality" defines="definitional equality; $\operatorname{Eq}(X,Y)$; $X=Y$"}

Definitional equality is judgmental equality in the chosen formal language.
For objects $X,Y$, $\operatorname{Eq}(X,Y)$ is the proposition type of ways $X$ is equal to $Y$: a $(-1)$-truncated type (@def:truncated).
The notation $X=Y$ records that $\operatorname{Eq}(X,Y)$ is inhabited.
No univalence principle is assumed.
:::
