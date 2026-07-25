# Loops and suspension {#sec-loops-suspension}

Let $\mathcal C$ be a pointed $\infty$-category, with zero object $*$, and suppose that it has the finite limits and colimits required below.

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

## Arrow categories and path spaces {#sec-interval-presentations}

For an $\infty$-category $C$, evaluation gives
$$
\operatorname{Fun}(\Delta^1,C)\longrightarrow C\times C.
$$
After taking cores, the homotopy fiber over $(x,y)$ is $\operatorname{Map}_C(x,y)$.
The fiber over $(x,x)$ is the space of endomorphisms of $x$; its union of equivalence components is the automorphism space of $x$.

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

## Fiber sequences

A composable pair $F\to E\to B$ is a fiber sequence when $F$ is equivalent to the homotopy fiber over a specified basepoint of $B$.
Applying homotopy groups gives the long exact sequence.
Its component-level portion is the pointed-set sequence recorded in @sec-pi0-fiber.
