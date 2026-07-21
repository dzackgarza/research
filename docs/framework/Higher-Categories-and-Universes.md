# Higher categories and universes {#sec-higher-categories-universes}

::: {#def-universe}
## Universe and smallness

Fix a Grothendieck universe $\mathcal U$. Sets, categories, and simplicial sets are
*small* when their data lie in $\mathcal U$. A construction indexed by all
$\mathcal U$-small objects is formed in a larger universe.
:::

::: {#def-infinity-category-universe}
## The chosen model of higher categories

A higher category is modeled by a quasicategory: a simplicial set with fillers for
every inner horn. Write $\mathbf{Cat}_{\infty,\mathcal U}$ for the $\infty$-category of
$\mathcal U$-small quasicategories and $\mathcal S_{\mathcal U}$ for its full
subcategory of Kan complexes [@Lur26, Tag 003A].

Ordinary categories enter through the ordinary nerve
$N\colon\mathbf{Cat}_{\mathcal U}\to\mathbf{Cat}_{\infty,\mathcal U}$. When a chapter
uses only ordinary categories, its pullbacks and functor categories are formed in the
2-category $\mathbf{Cat}_{\mathcal U}$ of small categories, functors, and natural
transformations.
:::

::: {#def-core}
## Core and groupoid completion

For an $\infty$-category $C$, its *core* $C^{\simeq}$ is the maximal Kan complex in
$C$. The functor
$$
(-)^{\simeq}\colon\mathbf{Cat}_\infty\longrightarrow\mathcal S
$$
is right adjoint to the inclusion $\mathcal S\hookrightarrow\mathbf{Cat}_\infty$.

The *groupoid completion* $C^{\mathrm{gpd}}$ is the value of the left adjoint to the
same inclusion. For an ordinary category $A$, its classifying space is
$$
B A:=|N A|\simeq (N A)^{\mathrm{gpd}}.
$$
The core retains the invertible morphisms of $C$. Groupoid completion formally inverts
every morphism [@Lur26].
:::

::: {#def-internal-hom}
## Functor categories

For $C,D\in\mathbf{Cat}_{\infty,\mathcal U}$, the quasicategory
$\operatorname{Fun}(C,D)$ is characterized by
$$
\operatorname{Hom}_{\mathbf{sSet}}(K,\operatorname{Fun}(C,D))
\cong
\operatorname{Hom}_{\mathbf{sSet}}(K\times C,D).
$$
Its objects are functors $C\to D$, its 1-simplices are natural transformations, and
its higher simplices encode higher coherences. Thus
$\mathbf{Cat}_{\infty,\mathcal U}$ is cartesian closed [@Lur26].
:::

::: {#def-mapping-spaces}
## Mapping spaces

The *mapping space* between two small $\infty$-categories is
$$
\operatorname{Map}_{\mathbf{Cat}_\infty}(C,D)
:=\operatorname{Fun}(C,D)^{\simeq},
$$
the maximal Kan complex in the functor quasicategory. For objects $x,y\in C$, the
mapping space $\operatorname{Map}_C(x,y)$ is the homotopy fiber over $(x,y)$ of
$$
\operatorname{Fun}(\Delta^1,C)^{\simeq}\longrightarrow
C^{\simeq}\times C^{\simeq}.
$$
This construction uses the core $(-)^{\simeq}$ from @def-core. The left-adjoint
groupoid-completion functor plays a different role.
:::

::: {#def-cells}
## Arrows and higher simplices

The arrow $\infty$-category of $C$ is
$\operatorname{Arr}(C)=\operatorname{Fun}(\Delta^1,C)$. Evaluation at the two vertices
gives
$$
(s,t)\colon\operatorname{Arr}(C)\longrightarrow C\times C.
$$
A 1-simplex of $C$ is a morphism. Higher simplices encode composable strings,
composites, and their coherences in the quasicategory model.
:::

::: {#def-initial-terminal}
## Initial, terminal, and contractible objects

An object $t\in C$ is terminal if $\operatorname{Map}_C(x,t)$ is contractible for
every $x\in C$. An object $i\in C$ is initial if
$\operatorname{Map}_C(i,x)$ is contractible for every $x\in C$.

An $\infty$-category is *categorically contractible* when it is equivalent to
$\Delta^0$. Its groupoid completion may be contractible without the category being
equivalent to $\Delta^0$; a category with a terminal object is the standard example.
:::

::: {#def-truncated}
## Truncated objects and morphisms

Let $C$ be an $\infty$-category. An object $X\in C$ is *$n$-truncated* if
$\operatorname{Map}_C(Y,X)$ is an $n$-truncated space for every $Y\in C$. A morphism
$f\colon X\to Y$ is $n$-truncated if, for every $Z\in C$, the induced map
$$
\operatorname{Map}_C(Z,X)\longrightarrow\operatorname{Map}_C(Z,Y)
$$
is an $n$-truncated map of spaces [@Lur26].

For a space $S$, this specializes to the usual condition
$\pi_k(S,s)=0$ for $k>n$. When the inclusion of $n$-truncated objects admits a left
adjoint, that adjoint is denoted $\tau_{\le n}$. A $(-2)$-truncated space is
contractible, a $(-1)$-truncated space is empty or contractible, and a $0$-truncated
space is equivalent to a discrete space.
:::

::: {#def-ordinary-category-specialization}
## Ordinary categories as a specialization

The nerve of an ordinary category has discrete mapping spaces. A functor between
ordinary categories is an equivalence precisely when its nerve is an equivalence in
$\mathbf{Cat}_{\infty,\mathcal U}$. The ordinary category, its nerve, and its
groupoid completion remain distinct objects.
:::

::: {#def-equality-of-objects}
## Equality, isomorphism, and equivalence

Literal equality is equality in the underlying set or formal language in which an
object is presented. An isomorphism in an ordinary category is a morphism with a
two-sided inverse. A morphism in an $\infty$-category is an equivalence when it becomes
invertible in the homotopy category [@Lur26, Tag 01DQ].

The notation $a=b$, $a\cong b$, and $a\simeq b$ records these three different claims.
No univalence principle is assumed. Chosen comparison maps are treated in
[Equivalences and witnesses](Identification.md).
:::
