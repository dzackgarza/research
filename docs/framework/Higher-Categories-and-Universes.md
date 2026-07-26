# Higher categories and universes {#sec-higher-categories-universes}

::: {#def-universe}
## The universe

Fix an axiomatic higher universe $\mathcal U$, regarded as an $(\infty,2)$-category, with terminal object $*$.
The category of higher categories is a point
$$
\mathbf{Cat}_\infty\colon *\longrightarrow\mathcal U.
$$
All categories considered below are small relative to $\mathcal U$.
:::

::: {#def-infinity-category-universe}
## The truncation tower

Fix truncation functors forming a tower in $\mathcal U$:
$$
\mathbf{Cat}_{-2}\longrightarrow
\mathbf{Cat}_{-1}\longrightarrow
\mathbf{Cat}_0\longrightarrow
\mathbf{Cat}_1\longrightarrow\cdots\longrightarrow
\mathbf{Cat}_n\longrightarrow\cdots\longrightarrow
\mathbf{Cat}_\infty.
$$
A higher category is a point
$$
C\colon *\longrightarrow\mathbf{Cat}_\infty.
$$
It is an $n$-category when this point factors through $\mathbf{Cat}_n$.
In particular, points of $\mathbf{Cat}_1$ represent ordinary categories.
:::

::: {#def-objects-of-category}
## Objects of a category

For a category $C\colon *\to\mathbf{Cat}_\infty$, an object of $C$ is a point
$$
X\colon *\longrightarrow\int_C C.
$$
The canonical projection from the category of elements exhibits $X$ itself as a point of $\mathbf{Cat}_\infty$; thus every object is a higher category, possibly one factoring through a discrete stage of the truncation tower.
:::

::: {#def-internal-hom}
## Internal hom

The point $\mathbf{Cat}_\infty$ is cartesian closed.
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
The objects of $[C,D]$ are morphisms $C\to D$; its higher morphisms are the transformations between them.
:::

::: {#def-core}
## Underlying homotopy type

Let $\mathcal S=\mathbf{Types}$ and let
$$
i\colon\mathcal S\hookrightarrow\mathbf{Cat}_\infty
$$
include homotopy types as higher groupoids.
Assume that this inclusion has a left adjoint
$$
\Pi_\infty\colon\mathbf{Cat}_\infty\longrightarrow\mathcal S,
\qquad
\Pi_\infty\dashv i.
$$
The type $\Pi_\infty C$ is obtained from $C$ by inverting every morphism.
No relation between $\Pi_\infty$ and a core construction is assumed here.
:::

::: {#def-bicomplete-cat-infinity}
## Initial and terminal categories

The higher category $\mathbf{Cat}_\infty$ has an initial object $\varnothing$ and a terminal object $*$, and it is bicomplete.
For a pointed higher category $(X,x)$, where $x\colon *\to X$ in $\mathbf{Cat}_\infty$, define
$$
\Omega_xX:=*\times_X*.
$$
For a higher category $A$, define its suspension by
$$
\Sigma A:=*\amalg_A*.
$$
The two coprojections make $\Sigma A$ bipointed.
:::

::: {#def-directed-delooping}
## The $B_{01}$ construction

Let $\mathbf{Cat}_\infty^{\partial}$ be the higher category of bipointed higher categories $(X;x_0,x_1)$.
Define the endpoint hom functor by
$$
\Omega_{01}(X;x_0,x_1):=[x_0,x_1]_X.
$$
For $A\in\mathbf{Cat}_\infty$, define $B_{01}A$ to have two objects $0,1$ and hom-objects
$$
[0,0]_{B_{01}A}=*,\qquad
[1,1]_{B_{01}A}=*,\qquad
[0,1]_{B_{01}A}=A,\qquad
[1,0]_{B_{01}A}=\varnothing.
$$
Composition is determined by the two identity actions on $A$ and the unique maps from $\varnothing$.
There is an adjunction
$$
B_{01}\dashv\Omega_{01}.
$$
:::

::: {#def-cells}
## Walking arrows and strings

Define the walking object and walking arrow by
$$
[0]:=*,
\qquad
[1]:=B_{01}*.
$$
Write $s,t\colon[0]\to[1]$ for its two objects.
For $n\geq2$, define
$$
[n]:=
\underbrace{[1]\amalg_{[0]}[1]\amalg_{[0]}\cdots\amalg_{[0]}[1]}_{n\text{ copies}},
$$
where each pushout identifies the target of one copy with the source of the next.
The objects $[[n],C]$ classify coherent strings of $n$ composable arrows in $C$.
The cosimplicial structure belongs to the walking categories $[n]$; the category $C$ remains a point of $\mathbf{Cat}_\infty$.
:::

::: {#def-mapping-spaces}
## Arrows and mapping types

For a higher category $C$, define
$$
\operatorname{Arr}(C):=[[1],C].
$$
Precomposition with $s$ and $t$ gives
$$
(s^*,t^*)\colon[[1],C]\longrightarrow
\int_C C\times\int_C C.
$$
For objects $x,y\colon*\to\int_C C$, their hom-category is the fiber
$$
[x,y]_C:=
*\times_{\int_C C\times\int_C C}[[1],C]
$$
over $(x,y)$.
Its underlying homotopy type is
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
An object $X\colon*\to\int_C C$ is *$n$-truncated* if $\operatorname{Map}_C(Y,X)$ is an $n$-truncated type for every $Y\colon*\to\int_C C$.
A morphism $f\colon X\to Y$ is $n$-truncated if, for every $Z\colon*\to\int_C C$, the induced map
$$
\operatorname{Map}_C(Z,X)\longrightarrow\operatorname{Map}_C(Z,Y)
$$
is an $n$-truncated map of types.

For a type $S$, this specializes to $\pi_k(S,s)=0$ for $k>n$.
When the inclusion of $n$-truncated objects admits a left adjoint, denote that adjoint by $\tau_{\le n}$.
A $(-2)$-truncated type is contractible, a $(-1)$-truncated type is empty or contractible, and a $0$-truncated type is equivalent to a discrete type.
:::

::: {#def-ordinary-category-specialization}
## Ordinary categories

An ordinary category is a point
$$
C\colon*\longrightarrow\mathbf{Cat}_1.
$$
Its image in $\mathbf{Cat}_\infty$ is obtained through the truncation tower.
:::

::: {#def-equality-of-objects}
## Equality, isomorphism, and equivalence

Literal equality is equality in the underlying set or formal language in which an object is presented.
An isomorphism in an ordinary category is a morphism with a two-sided inverse.
An equivalence in a higher category is a morphism admitting an inverse up to coherent higher equivalence.

The notation $a=b$, $a\cong b$, and $a\simeq b$ records these three claims.
No univalence principle is assumed.
Chosen comparison maps are treated in [Equivalences and witnesses](Identification.md).
:::
