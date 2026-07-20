# Loops and suspension

The internal suspension–loop–fiber–cofiber calculus of the ambient $\mathbf{Cat}_\omega$ ([Framework](Ambient-Setting.md#sec-ambient)). Every limit and colimit below is taken in $\mathbf{Cat}_\omega$; spaces appear only after applying $\Pi_\infty$ ([Framework](Ambient-Setting.md#def-mapping-spaces)). These are the constructions the framework builds from, and the ones inside which the equality predicate ([Equality](Equality.md)) lives.
Some points are marked *Open* where a construction was fixed only in low degree.

## Fundamental (co)base changes {#sec-cobase-changes}

For a morphism $f \colon X \to Y$, the loop and suspension of $f$ are the pullback and pushout
$$
\Omega_f := X \times_Y X, \qquad \Sigma_f := Y \amalg_X Y.
$$
Their principal special cases are
$$
\Sigma C := * \amalg_C *, \qquad \Omega_x C := * \times_C *,
$$
and, for a point $y \colon * \to Y$, the fiber and cofiber
$$
\operatorname{Fib}_y(f) := X \times_Y *, \qquad \operatorname{Cof}(f) := Y \amalg_X *.
$$
The asymmetry is structural: $C \to *$ is canonical, so suspension and cofiber are *unpointed*; $* \to C$ selects an object, so loops and fibers are *based*.

## Interval presentations {#sec-interval-presentations}

Let $I$ be the walking arrow with its two endpoints, and write
$$
e_Y = (\operatorname{ev}_0, \operatorname{ev}_1) \colon Y^I \longrightarrow Y \times Y
$$
for the endpoint evaluation on the cotensor $Y^I = [I, Y]$.
The path-object presentations are
$$
\operatorname{Cocyl}(f) = Y^I \times_Y X, \qquad
\operatorname{Cocone}_y(Y) = Y^I \times_Y *,
$$
$$
L_a(Y) = Y^I \times_{Y \times Y} X \quad (a \colon X \to Y \times Y), \qquad
\operatorname{Paths}_{(y_0, y_1)}(Y) = Y^I \times_{Y \times Y} *,
$$
and the fiber is recovered as
$$
\operatorname{Fib}_y(f) \simeq Y^I \times_{Y \times Y} (X \times *),
$$
where $X \times * \to Y \times Y$ is $(f, y)$.
Dually, with the tensor $I \times X$,
$$
\operatorname{Cyl}(f) = (I \times X) \amalg_X Y, \qquad
\operatorname{Cone}(X) = (I \times X) \amalg_X *, \qquad
\operatorname{Cof}(f) = Y \amalg_X *,
$$
and suspension has the double-cone presentation
$$
\Sigma X = * \amalg_X * \simeq \operatorname{Cone}(X) \amalg_X \operatorname{Cone}(X).
$$
These are constructions in $\mathbf{Cat}_\omega$, not strict pullbacks or pushouts of underlying sets.

## Loops and hom-objects {#sec-loops-hom}

The *free loop category* uses the diagonal $Y \to Y \times Y$:
$$
\mathcal L Y := Y^I \times_{Y \times Y} Y,
$$
and its based fiber, at the endpoint pair $(y, y)$, is
$$
\Omega_y Y := \mathcal L Y \times_Y * \simeq * \times_Y * \simeq Y^I \times_{Y \times Y} *.
$$
The hom-object of $C$ between $x, y$ (@sec-cobase-changes) is the same construction with endpoints $(x, y) \colon * \to C \times C$,
$$
\operatorname{Hom}_C(x, y) = [I, C] \times_{C \times C} *,
$$
a full higher category whose $n$-cells are the $(n+1)$-cells of $C$ with the prescribed endpoints (this refines the arrow-object presentation of [Framework](Ambient-Setting.md#def-cells)). At the first loop level,
$$
\Omega_x C = \operatorname{End}_C(x) = \operatorname{Hom}_C(x, x).
$$
No invertibility is imposed; applying $\Pi_\infty$ afterward produces a loop space.

## Spheres and globular suspension {#sec-spheres-suspension}

Spheres are generated from the empty and two-point objects by suspension:
$$
S^{-1} := \varnothing, \qquad S^0 := * \amalg *, \qquad S^{n+1} := \Sigma S^n.
$$
A globular model of $\Sigma C$ has two objects $v_-, v_+$, shifts every cell of $C$ up one degree, and satisfies
$$
\operatorname{Hom}_{\Sigma C}(v_-, v_+) \simeq C.
$$
The pushout $* \amalg_C *$, the double-cone presentation (@sec-interval-presentations), and this minimal two-object globular presentation are equivalent models of $\Sigma C$, not necessarily identical cell complexes.

## Deloopings {#sec-deloopings}

The delooping tower distinguishes the one-object case from the canonical suspension:

- $BC = B^1 C$: the one-object delooping, defined when $C$ is monoidal, so that its objects compose as endomorphisms.

- $B^2 C$: canonical for arbitrary $C$, with two objects $0, 1$ and $\operatorname{Hom}(0, 1) = C$.
  This is the globular suspension (@sec-spheres-suspension).

- $B^3 C$: the walking $2$-cell with parallel $f, g \colon 0 \to 1$, its top $2$-cell replaced by $C$.

- In general, $B^{n+1} C$ retains the lower boundary of the walking $n$-cell and replaces its top cell by $C$, so that
  $$
  \operatorname{Mor}^{n+k}(B^{n+1} C) \cong \operatorname{Mor}^k(C).
  $$

*Open.* A uniform formula $B^{n+1} C = I^n \otimes C$ is not settled: the required general cellwise tensor is unsettled.

## Three adjunctions {#sec-adjunctions}

Three distinct adjunctions are kept separate.
The cartesian one,
$$
\adj{\mathbf{Cat}_\omega}{\mathbf{Cat}_\omega}{K \times (-)}{(-)^K}, \qquad K \times (-) \dashv (-)^K,
$$
gives free loops when $K = S^1$.
In the pointed setting,
$$
\adj{(\mathbf{Cat}_\omega)_*}{(\mathbf{Cat}_\omega)_*}{(-) \wedge S^1}{\Omega}, \qquad (-) \wedge S^1 \dashv \Omega.
$$
The globular adjunction into bipointed categories,
$$
\adj{\mathbf{Cat}_\omega}{(\mathbf{Cat}_\omega)_{**}}{\Sigma}{\operatorname{Hom}}, \qquad \Sigma \dashv \operatorname{Hom},
$$
with $\operatorname{Hom}(D; x_-, x_+) = \operatorname{Hom}_D(x_-, x_+)$, is the categorical dimension-shift used throughout these foundations.

## The calculus and equality {#sec-calculus-equality}

The equality construction is expressed entirely in this calculus: $\operatorname{Eq}(C, D)$, the automorphism quotients, and $Q^0(C, D)$ ([Equality](Equality.md#sec-equality-predicate)) are subcategories, colimits, and fibers inside $\mathbf{Cat}_\omega$, not operations on mapping spaces.

*Open.* The compatible definition of every iterated $\Omega_x^k C$, and the reconstruction
$$
\langle x \rangle \simeq \Omega_x^\infty C
$$
of the one-object higher subcategory on $x$, are not formalized.
The first loop-and-hom level is settled; the infinite tower is not.
