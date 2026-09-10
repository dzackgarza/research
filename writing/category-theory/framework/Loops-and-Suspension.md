# Loops and suspension {#sec-loops-suspension}

Let $\mathcal C$ be a pointed $\infty$-category, with zero object $*$, and suppose that it has the finite limits and colimits required below.

::: {#def-fiber-cofiber}
## Fibers and cofibers {#sec-cobase-changes}

For $f\colon X\to Y$, its fiber over the canonical basepoint $0\colon *\to Y$ is defined by the cartesian square

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

The pushout notation for its apex is
$$
\operatorname{Cof}(f)=Y\amalg_X *.
$$
These definitions specialize in pointed spaces to the usual homotopy fiber and homotopy cofiber.
:::

::: {#def-loops-suspension}
## Loops and suspension

For an object $X$ of $\mathcal C$, loops are defined by the pullback square

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

Suspension is defined by the pushout square

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

## Arrow categories and path spaces {#sec-interval-presentations}

For a higher category $C$, evaluation at the endpoints of the constructed walking arrow gives
$$
[[1],C]\longrightarrow C\times C.
$$

The fiber over $(x,y)$ is the hom-category $[x,y]_C$; applying $\Pi_\infty$ gives $\operatorname{Map}_C(x,y)$.
The fiber over $(x,x)$ is the endomorphism category of $x$, and its full subcategory on the invertible objects is the automorphism category of $x$.

## The suspension-loop adjunction {#sec-adjunctions}

When $\mathcal C$ has finite limits and colimits, suspension is left adjoint to loops:
$$
\adj{\mathcal C}{\mathcal C}{\Sigma}{\Omega},
\qquad \Sigma\dashv\Omega.
$$
For $\mathcal C=\mathcal S_*$, the $\infty$-category of pointed spaces, this recovers the classical adjunction
$$
\operatorname{Map}_*(\Sigma X,Y)\simeq
\operatorname{Map}_*(X,\Omega Y).
$$

::: {#def-fiber-sequence}
## Fiber sequences

A composable pair $F\to E\to B$ is a *fiber sequence* when $F$ is equivalent to the homotopy fiber over a specified basepoint of $B$.
Applying homotopy groups gives the long exact sequence.
Its component-level portion is the pointed-set sequence recorded in @sec-pi0-fiber.
:::

## Extending the sequences {#sec-extended-sequences}

For $f\colon X\to Y$ the fiber square of @def-fiber-cofiber may be extended to the left, since the fiber of $\operatorname{Fib}(f)\to X$ is computed by a pasted pullback square and is $\Omega Y$:
$$
\cdots\longrightarrow
\Omega X\longrightarrow
\Omega Y\longrightarrow
\operatorname{Fib}(f)\longrightarrow
X\xrightarrow{\;f\;}Y .
$$
Dually the cofiber square extends to the right,
$$
X\xrightarrow{\;f\;}Y\longrightarrow
\operatorname{Cof}(f)\longrightarrow
\Sigma X\longrightarrow
\Sigma Y\longrightarrow\cdots,
$$
each stage being the fiber or cofiber of the preceding morphism [@nlab:fiber_sequence].

::: {#def-homotopy-groups}
## Homotopy groups of a pointed space

Let $\mathcal S_*$ be the $\infty$-category of pointed spaces.
For $(X,x)\in\mathcal S_*$ and $n\geq0$, set
$$
\pi_n(X,x):=\pi_0\bigl(\Omega^n_xX\bigr),
$$
where $\Omega^0_xX:=X$ and $\Omega^{n}_xX:=\Omega_x\Omega^{n-1}_xX$, each loop object taken at the basepoint supplied by the previous stage.
For $n\geq1$ the composition of loops makes $\pi_n(X,x)$ a group, and for $n\geq2$ an abelian group.
These are the groups appearing in the truncation conditions of @def-truncated and in the long exact sequence of a fiber sequence.
:::
