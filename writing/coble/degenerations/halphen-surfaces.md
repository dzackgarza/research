# Halphen surfaces {#sec-halphen-surfaces}

::: {.proposition #prop:halphen-surface-fibres title="Fibres of Halphen surfaces"}

A relatively minimal rational elliptic surface $V$ is a **Halphen surface of index $n$** if the class of its fibre is $-nK_V$.
Every relatively minimal rational elliptic surface is a Halphen surface of some index $n$.

1. A Halphen surface of index $1$ is a Jacobian rational elliptic surface: its fibration has no multiple fibres, equivalently it has a section.

2. A Halphen surface of index $n\geq2$ has a unique multiple fibre $nF_1'$, of multiplicity $n$, and $\abs{-iK_V} = \theset{iF_1'}$ for $1\leq i\leq n-1$

[@DZ99, §2.4].
:::

::: {.proposition #prop:terminal-coble-halphen-blowup title="Terminal Coble surfaces as blowups of Halphen surfaces"}

Let $V$ be a terminal Coble surface of K3 type (@def:coble-surface).
Then $V$ is isomorphic to one of the following:

1. the blowup of a Halphen surface of index $1$ at singular points of two simple reduced fibres;

2. the blowup of a Halphen surface of index $2$ at singular points of one simple reduced fibre.

If the fibre is of type $\tilde A_1^*$ or $\tilde A_2^*$, the blowup is done twice or four times, respectively [@DK25, Prop. 9.1.4].
In case 2 the fibre is of type $\tilde A_k$ with $k\leq8$, and in case 1 the two fibres are of types $\tilde A_k$ and $\tilde A_m$, or their degenerations $\tilde A_k^*$ and $\tilde A_m^*$, with $k + m\leq8$ [@DK25, proof of Cor. 9.1.5].
:::

::: {.proposition #prop:coble-sextic-halphen-pencil title="The Halphen pencil of a Coble sextic"}

Let $V$ be a terminal Coble surface of K3 type with $n = 1$, and let $W = V(F_6)$ be the irreducible plane sextic of @prop:coble-sextic-model, with $10$ ordinary nodes or cusps, possibly infinitely near.
Choose $9$ of the $10$ double points of $W$.
Then a plane cubic $V(F_3)$ passes through them, and the pencil $V(\lambda F_6 + \mu F_3^2)$ is a Halphen pencil of index $2$.
The minimal resolution of its base points is a Halphen surface of index $2$, and $V$ is the blowup of a singular point of an irreducible simple fibre of this pencil.

Let $F$ be a reducible simple fibre of the pencil.
The blowup of a singular point of $F$ is a non-terminal Coble surface of K3 type with $n = 1$, whose anti-bicanonical curve is the proper transform of $F$.
The blowup of the singular points of this curve is a terminal Coble surface of K3 type whose number $n$ of boundary components is the number of components of $F$ [@DK25, Ex. 9.1.7].
:::

::: {.proposition #prop:terminal-coble-deformations title="Deformations of terminal Coble surfaces"}

Let $k$ be the base field, of characteristic $p\neq2$.
Let $V$ be a terminal Coble surface of K3 type with $K_V^2 = -n$ and anti-bicanonical curve $C$.
Then
$$
h^i(\Theta_{V/k}) = \begin{cases} 10 + 2n & i = 1, \\ 0 & \text{otherwise} \end{cases}
$$
[@DK25, Prop. 9.1.8].
The number of moduli of Coble surfaces with $n$ boundary components is
$$
h^1(\Theta_{V/k}(-C)) = 10 - n
.
$$
For $n = 1$ it is $9$, the number of moduli of general Halphen surfaces of index $2$ [@DK25, Rem. 9.1.9].
:::

::: {.lemma #lem:coble_halphen_blowdown title="Cobles to Halphens"}

Let $X$ be a smooth rational surface with $\abs{-K_X} = \varnothing$, $K_X^2 = -1$, and $\abs{-2K_X} = \theset{C}$ with $C$ an irreducible curve.
Let $\pi_{E}\colon X \to Y$ be the blowing down of a $(-1)$-curve $E$.
Then

- $Y$ is a Halphen surface of index 2;

- $C$ is the proper transform of the fiber $F$ containing $y_{0}=\pi_{E}(E)$;

- the fiber $F$ is irreducible, and $y_{0}$ is its unique singular point.

Conversely, the blow-up of a singular point of an irreducible non-multiple fiber of a Halphen surface of index 2 is a surface $X$ with these properties [@CD12, Prop. 3.1].
:::

::: {.proof}

The proof follows [@CD12, §3.1 and proof of Prop. 3.1].

By adjunction, $p_a(C) = 1 + \tfrac12(C^2 + C\cdot K_X) = 1 + K_X^2 = 0$.
So $C$ is a smooth rational curve with $C^2 = 4K_X^2 = -4$.

Since $K_X^2 = -1$, $K_Y^2 = 0$.
Let $F = \pi_E(C)$.
Since $C$ is irreducible, so is $F$.
Since $C\cdot E = -2K_X\cdot E = 2$, the curve $F$ is singular at $y_0$, and $\pi_E^*(F) = C + 2E$.
From $K_X = \pi_E^*K_Y + E$ and $C\sim-2K_X$,
$$
\pi_E^*(F) = C + 2E \sim -2\pi_E^*K_Y
,
$$
so $F$ is an irreducible curve in $\abs{-2K_Y}$.
In particular $F^2 = 4K_Y^2 = 0$, and $-K_Y$ is nef.
The morphism $\pi_E$ is an isomorphism away from $E$, and $C$ is smooth, so $y_0$ is the unique singular point of $F$.

By Riemann--Roch, $h^0(-K_Y) > 0$.
If $h^0(-K_Y) > 1$, there is a curve $G\in\abs{-K_Y}$ through $y_0$.
Then $\pi_E^*(G) - E$ is effective and lies in $\abs{-K_X}$, which contradicts $\abs{-K_X} = \varnothing$.
Thus $h^0(-K_Y) = 1$, and the unique effective divisor $F_0\in\abs{-K_Y}$ does not pass through $y_0$.
So $\abs{-2K_Y}$ contains the two linearly independent divisors $2F_0$ and $F$, and $h^0(-2K_Y)\geq2$.
Since $K_Y^2 = 0$, the divisors $2F_0$ and $F$ are disjoint, and $\abs{-2K_Y}$ has no fixed components.
It contains the reduced irreducible curve $F$, so it is an irreducible pencil.
Thus $Y$ is a Halphen surface of index $2$, $F$ is a fibre of its Halphen fibration through $y_0$, and $C$ is the proper transform of $F$.

Conversely, let $Y$ be a Halphen surface of index $2$, let $F$ be an irreducible non-multiple fibre, let $y_0$ be a singular point of $F$, and let $\pi_E\colon X\to Y$ be the blowup of $y_0$.
Then $K_X^2 = K_Y^2 - 1 = -1$.
Since $F\in\abs{-2K_Y}$ and its singular point is blown up, $\abs{-2K_X}$ is not empty and contains the proper transform $C$ of $F$, which is a smooth rational curve.
Since $C$ is irreducible and $C^2 = 4K_X^2 = -4 < 0$, every $D\in\abs{-2K_X}$ satisfies $D\cdot C = C^2 < 0$, so $C$ is a component of $D$ and $D - C\sim 0$ is effective; thus $\abs{-2K_X} = \theset{C}$.
The linear system $\abs{-K_X}$ is empty, because $\abs{-K_Y}$ consists of the unique multiple fibre $F_0$ of $Y$, and $F_0$ does not pass through $y_0$.
:::

::: {.conjecture #conj:coble-halphen-moduli-correspondence title="Coble and Halphen moduli"}

The constructions of @lem:coble_halphen_blowdown and @prop:terminal-coble-halphen-blowup give a correspondence between the moduli spaces of Coble surfaces with $n$ boundary components and the moduli spaces of index $2$ Halphen pencils on the $g=0$ line of Nikulin's diagram of $2$-elementary lattices, whose vertices are the triples $(r, a, \delta)$.
Under this correspondence the cusp diagrams of the two moduli spaces coincide.
:::
