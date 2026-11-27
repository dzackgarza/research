# Loops and suspension {#sec-loops-suspension}

Let $\mcc$ be a pointed $\infty$-category, with zero object $*$, and suppose that it has the finite limits and colimits required below.

::: {.definition #def:fiber-cofiber title="Fibers and cofibers" defines="fiber; cofiber; $\operatorname{Fib}(f)$; $\operatorname{Cof}(f)$"}
[]{#sec-cobase-changes}

For $f\colon X\to Y$, its fiber over the zero morphism $0\colon *\to Y$ is defined by the cartesian square

```{.tikz}
%%| filename: fiber-square
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}
\operatorname{Fib}(f)
  \arrow[r,"p_X"]
  \arrow[d,"p_*"']
  \arrow[dr,phantom,very near start,"\lrcorner"] &
X \arrow[d,"f"]\\
* \arrow[r,"0"'] & Y
\end{tikzcd}
```

The fiber-product notation for its apex is
$$
\operatorname{Fib}(f)=X\times_Y *.
$$
The cofiber is defined by the cocartesian square

```{.tikz}
%%| filename: cofiber-square
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}
X
  \arrow[r,"f"]
  \arrow[d,"0"']
  \arrow[dr,phantom,very near end,"\ulcorner"] &
Y \arrow[d,"i_Y"]\\
* \arrow[r,"i_*"'] & \operatorname{Cof}(f)
\end{tikzcd}
```

The pushout (@def:pullback-square) notation for its apex is
$$
\operatorname{Cof}(f)=Y\amalg_X *.
$$
These definitions specialize in pointed spaces to the usual homotopy fiber and homotopy cofiber.
:::

::: {.definition #def:loops-suspension title="Loops and suspension" defines="loop object; suspension object; $\Omega X$; $\Sigma X$"}

For an object $X$ of $\mcc$, loops (@def:based-loop) are defined by the pullback (@def:pullback-square) square

```{.tikz}
%%| filename: loop-square
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}
\Omega X
  \arrow[r,"\operatorname{pr}_2"]
  \arrow[d,"\operatorname{pr}_1"']
  \arrow[dr,phantom,very near start,"\lrcorner"] &
* \arrow[d,"0"]\\
* \arrow[r,"0"'] & X
\end{tikzcd}
```

Suspension is defined by the pushout (@def:pullback-square) square

```{.tikz}
%%| filename: suspension-square
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}
X
  \arrow[r,"0"]
  \arrow[d,"0"']
  \arrow[dr,phantom,very near end,"\ulcorner"] &
* \arrow[d,"j_1"]\\
* \arrow[r,"j_2"'] & \Sigma X
\end{tikzcd}
```

Thus
$$
\Omega X=*\times_X *,
\qquad
\Sigma X=*\amalg_X *.
$$
In pointed spaces these are the usual loop-space and reduced-suspension constructions.
:::

## Evaluation with a variable point {#sec-evaluation-variable-point}

Let $\mathcal C$ be a cartesian closed category with pullbacks and terminal object $1$. The identity of $B^A$ corresponds under the exponential adjunction (@def:closed-monoidal) to $\mathrm{ev}\colon B^A\times A\to B$. Equivalently, internal composition gives $B^A\times A^1\to B^1$ under the canonical isomorphisms $A^1\cong A$ and $B^1\cong B$. For any test object $U$, evaluation sends a pair $f\colon U\times A\to B$, $a\colon U\to A$ to $f\circ(\mathrm{id}_U,a)\colon U\to B$. This formula commutes with precomposition in $U$.

A point $a\colon1\to A$ alone gives $\mathrm{ev}_a\colon B^A\to B$ by restriction along $(\mathrm{id},a\circ !)$. A point $b\colon1\to B$ alone gives a pullback with two projections:
$$
B^A\xleftarrow{\ \mathrm{pr}_1\ } E_b=(B^A\times A)\times_B1
\xrightarrow{\ \mathrm{pr}_2\ } A.
$$
Over a point $f\colon1\to B^A$ corresponding to $\bar f\colon A\to B$, the fibre of $E_b\to B^A$ is $A\times_{B}1$ along $\bar f$ and $b$. Over $a\colon1\to A$, the fibre of $E_b\to A$ is $B^A\times_{B}1$ along $\mathrm{ev}_a$ and $b$. These identifications follow by pasting pullbacks (@def:pullback-square). In sets, the first projection sends $(f,a)$ with $f(a)=b$ to $f$. Its image consists of the maps that hit $b$, whereas its fibre over $f$ retains every choice of preimage. The second projection has as its fibre over $a$ the maps $(A,a)\to(B,b)$.

External global points $\Gamma=\operatorname{Hom}_{\mathcal C}(1,-)$ preserve pullbacks. Applied to the defining square of $E_b$, this gives
$$
\Gamma(E_b)\cong
\bigl(\operatorname{Hom}_{\mathcal C}(A,B)\times\Gamma(A)\bigr)
\times_{\Gamma(B)}\Gamma(1).
$$
Here $\Gamma(B^A)\cong\operatorname{Hom}_{\mathcal C}(A,B)$ by adjunction. The two maps to $\Gamma(B)$ send $(f,a)$ to $f\circ a$ and the unique element of $\Gamma(1)$ to $b$, respectively. In a cartesian closed $\infty$-category with pullbacks, external points form mapping spaces and the displayed pullback is a homotopy pullback. A point of this fibre includes a path from $f\circ a$ to $b$.

For an interval presented by a factorization $1\amalg1\xrightarrow{j}I\to1$, its endpoints are $a_i=j\circ\iota_i$ for the coprojections $\iota_i\colon1\to1\amalg1$. Hence a path starting at $b$ is represented by the pullback of $\mathrm{ev}_{a_0}\colon B^I\to B$ along $b$. Letting the point of $I$ vary instead gives paths equipped with a point at which they take the value $b$.

## Arrow categories and path spaces {#sec-interval-presentations}

For a higher category $C$, evaluation at the endpoints of the constructed walking arrow gives
$$
[[1],C]\too C\times C.
$$

The fiber over $(x,y)$ is the hom-category $[x,y]_C$; applying $\Pi_\infty$ gives $\operatorname{Map}_C(x,y)$.
The fiber over $(x,x)$ is the endomorphism category of $x$, and its full subcategory on the invertible objects is the automorphism category of $x$.

::: {.question #qst:arrow-fibre-fullness title="In what sense does the arrow category contain a hom-category?"}

For an ordinary category $C$, the endpoint functor $\operatorname{Fun}([1],C)\to C\times C$ sends a commutative square to its two vertical maps. Its strict fibre over $(x,y)$ contains the arrows $x\to y$. A square in that fibre must have vertical maps $\id_x,\id_y$, so its two horizontal arrows agree. The fibre is the discrete category on $\Hom_C(x,y)$.

Is it full on those objects? In vector spaces the square from $\id_V$ to itself with both vertical maps zero commutes. For $V\ne0$, the square lies outside the endpoint fibre. In a strict $2$-category there is a further choice. Strictly commuting squares with identity endpoints still impose equality of the horizontal arrows. A lax square with the same endpoints can carry a specified $2$-cell between them; reversing the lax convention reverses its direction. Which arrow construction and which cells over the identities recover the intended hom-category? This choice is part of interpreting the endpoint square in @def:mapping-spaces.
:::

## The suspension-loop adjunction {#sec-adjunctions}

When $\mcc$ is pointed and has finite limits and colimits, suspension is left adjoint to loops:
$$
\adj{\mcc}{\mcc}{\Sigma}{\Omega},
\qquad \Sigma\dashv\Omega.
$$
For $\mcc=\mcs_*$, the $\infty$-category of pointed spaces, this recovers the classical adjunction
$$
\operatorname{Map}_*(\Sigma X,Y)\simeq
\operatorname{Map}_*(X,\Omega Y).
$$

::: {.question #qst:loops-derived-endomorphisms title="Which object is being looped when endomorphisms appear?"}

In a stable $\infty$-category $\mathcal C$, the loop object $\Omega B=0\times_B0$ belongs to $\mathcal C$. The mapping spectrum $\operatorname{map}_{\mathcal C}(A,-)$ preserves this pullback. Hence
$$
\operatorname{map}_{\mathcal C}(A,\Omega B)\simeq\Omega\operatorname{map}_{\mathcal C}(A,B).
$$
For the derived $\infty$-category of an ordinary ring $R$, put a module $A$ in degree zero. With cohomological shift $[n]$, its derived endomorphisms give
$$
\pi_{-n}\operatorname{map}(A,A)=\Hom_{D(R)}(A,A[n])=\operatorname{Ext}^n_R(A,A),\qquad n\ge0 .
$$

What does a loop *at* $A$ in the space of objects give? The core $\mathcal C^\simeq$ retains only equivalences, so $\Omega_A(\mathcal C^\simeq)\simeq\operatorname{Aut}_{\mathcal C}(A)$. Inside $\Omega^\infty\operatorname{map}(A,A)$ this is the union of components invertible under composition. Thus shifting an object, taking homotopy groups of its endomorphism spectrum, and following an equivalence around a loop at that object answer different questions.
:::

::: {.definition #def:fiber-sequence title="Fiber sequences" defines="fiber sequence"}

A composable pair $F\to E\to B$ is a *fiber sequence* when $F$ is equivalent to the homotopy fiber (@def:fiber-cofiber) over a specified basepoint of $B$.
Applying homotopy groups (@def:homotopy-groups) gives the long exact (@def:exact-complex) sequence.
Its component-level portion is the pointed-set sequence of @sec-pi0-fiber.
:::

## The spaces of the sphere spectrum {#sec-sphere-spectrum-spaces}

::: {.definition #def:q-construction title="The infinite loop space $QX$" defines="$QX$"}
For a based CW complex $X$, put
$$
QX=\operatorname*{colim}_{r\geq 0}\Omega^r\Sigma^r X .
$$
The transition map at stage $r$ is $\Omega^r$ applied to the unit $\Sigma^r X\to\Omega\Sigma(\Sigma^r X)$ of the suspension-loop adjunction (@sec-adjunctions) [@May99, p. 233].
:::

::: {.question #qst:stable-stem-from-qs title="Can the geometry of $QS^n$ compute a stable stem independently?"}
For $n\geq0$ and $k>0$, take the constant loop as basepoint. The definition gives [@May99, p. 233]
$$
\pi_{n+k}(QS^n)\cong\operatorname*{colim}_r\pi_{n+k+r}(S^{n+r})
=\pi_k^{\mathrm s}(S^0).
$$
For which $k$ can one compute the left side from a geometric model of $QS^n$ (@def:q-construction)? In a model by configurations of points labelled in $S^n$, which attaching maps or operations determine a homotopy class and its order? For $n=0$, which positive stems can one obtain from the ordinary homotopy of the degree-zero component $Q_0S^0$ after group completion?
:::

::: {.example #ex:qs-zero-first-stem title="The first stable stem from permutations"}
Under disjoint union, the groupoid of finite sets and bijections has classifying space $\coprod_{m\geq0}B\mathfrak S_m$. The Barratt–Priddy–Quillen theorem identifies its group completion with $QS^0$ [@Seg74, Prop. 3.5 and §4]. On components, group completion sends cardinality in $\mathbb N$ to degree in $\ZZ$. In degree zero it gives a homology isomorphism $B\mathfrak S_\infty\to Q_0S^0$, where $\mathfrak S_\infty=\bigcup_m\mathfrak S_m$ under the inclusions fixing the new letter.

The transpositions generate $\mathfrak S_\infty$, are conjugate, and have order two. The sign map detects their common class in the abelianization. Hence $H_1(B\mathfrak S_\infty;\ZZ)=\ZZ/2$. The fundamental group of the infinite loop space $Q_0S^0$ is abelian, so its degree-one Hurewicz map is an isomorphism. This computes $\pi_1(Q_0S^0)=\ZZ/2$ from permutations and gives $\pi_1^{\mathrm s}(S^0)=\ZZ/2$ by @qst:stable-stem-from-qs.
:::

## Extending the sequences {#sec-extended-sequences}

For $f\colon X\to Y$ the fiber square of @def:fiber-cofiber may be extended to the left, since the fiber of $\operatorname{Fib}(f)\to X$ is computed by a pasted pullback square and is $\Omega Y$:
$$
\cdots\too
\Omega X\too
\Omega Y\too
\operatorname{Fib}(f)\too
X\xrightarrow{\;f\;}Y .
$$
Dually the cofiber square extends to the right,
$$
X\xrightarrow{\;f\;}Y\too
\operatorname{Cof}(f)\too
\Sigma X\too
\Sigma Y\too\cdots,
$$
each stage being the fiber or cofiber of the preceding morphism [@nlab:fiber_sequence].

::: {.definition #def:homotopy-groups title="Homotopy groups of a pointed space" defines="homotopy group; $\pi_n(X,x)$; $\Omega^n_xX$"}

Let $\mcs_*$ be the $\infty$-category of pointed spaces.
For $(X,x)\in\mcs_*$ and $n\geq0$, set
$$
\pi_n(X,x):=\pi_0\bigl(\Omega^n_xX\bigr),
$$
where $\Omega^0_xX:=X$ and $\Omega^{n}_xX:=\Omega_x\Omega^{n-1}_xX$, each loop object (@def:bicomplete-cat-infinity) taken at the basepoint supplied by the previous stage.
For $n\geq1$ the composition of loops (@def:based-loop) (@def:loops-suspension) makes $\pi_n(X,x)$ a group (@def:group), and for $n\geq2$ an abelian group.
These are the groups appearing in the truncation conditions of @def:truncated and in the long exact (@def:exact-complex) sequence of homotopy groups.
:::
