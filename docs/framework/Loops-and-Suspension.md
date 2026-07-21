# Loops and suspension {#sec-loops-suspension}

Let $\mathcal C$ be a pointed $\infty$-category with zero object $*$ and the finite
limits and colimits required by the stated constructions.

## Fibers and cofibers {#sec-cobase-changes}

For $f\colon X\to Y$ and a point $y\colon *\to Y$, the fiber is the pullback
$$
\operatorname{Fib}_y(f)=X\times_Y *.
$$
The cofiber is the pushout
$$
\operatorname{Cof}(f)=Y\amalg_X *.
$$
These definitions specialize in pointed spaces to the usual homotopy fiber and homotopy
cofiber.

## Loops and suspension

For a pointed object $X$, define
$$
\Omega X=*\times_X *,
\qquad
\Sigma X=*\amalg_X *.
$$
The two maps $*\to X$ in the pullback are the chosen basepoint; the two maps
$X\to *$ in the pushout are unique. In pointed spaces these are the usual loop-space
and reduced-suspension constructions.

## Arrow categories and path spaces {#sec-interval-presentations}

For an $\infty$-category $C$, evaluation gives
$$
\operatorname{Fun}(\Delta^1,C)\longrightarrow C\times C.
$$
After taking cores, the homotopy fiber over $(x,y)$ is
$\operatorname{Map}_C(x,y)$. The fiber over $(x,x)$ is the space of endomorphisms of
$x$; its union of equivalence components is the automorphism space of $x$.

## The suspension-loop adjunction {#sec-adjunctions}

When $\mathcal C$ has finite limits and colimits, suspension is left adjoint to loops:
$$
\adj{\mathcal C_*}{\mathcal C_*}{\Sigma}{\Omega},
\qquad \Sigma\dashv\Omega.
$$
For $\mathcal C=\mathcal S$, this recovers the classical adjunction
$$
\operatorname{Map}_*(\Sigma X,Y)\simeq
\operatorname{Map}_*(X,\Omega Y).
$$

## Fiber sequences

A composable pair $F\to E\to B$ is a fiber sequence when $F$ is equivalent to the
homotopy fiber over a specified basepoint of $B$. Applying homotopy groups gives the
long exact sequence. Its component-level portion is the pointed-set sequence recorded
in @sec-pi0-fiber.
