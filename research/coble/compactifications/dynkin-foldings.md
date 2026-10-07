# Foldings of Dynkin diagrams

::: {.remark title="Orientation"}

This section collects the folding constructions that produce non-simply-laced root systems from simply-laced ones by summing the roots in each orbit of a diagram automorphism, together with the specific root-folding criterion governing the involution $I = -\Ien$ on $\tdp$ and the *mirror moves* used to navigate the pyramid of $2$-elementary lattices.
As in the root systems material we work in the algebraic-geometry sign convention: root lattices are negative definite and roots have norm $-2$ (see @def:root-lattice).
:::

## Foldings of simply-laced diagrams

::: {.remark #rmk:classical-foldings title="Classical foldings of Dynkin diagrams"}

The process of folding by nontrivial diagram automorphisms produces non-simply-laced root systems from simply-laced diagrams.
The roots in the same orbit under the folding group must be orthogonal.

Classical examples of foldings of simply-laced Dynkin diagrams include:

- $A_{2n-1} \to C_n$ via $S_2$ (horizontal reflection);

- $D_{n+1} \to B_n$ via $S_2$ (vertical reflection);

- $D_4 \to G_2$ via $S_3$ (rotation by $2\pi/3$);

- $E_6 \to F_4$ via $S_2$ (horizontal reflection).

These arise as the fixed-point subalgebras $\mathfrak{g}^\sigma$.
The orbit-sum construction of @def:folded-root instead produces the **Langlands-dual** root system in types $B$/$C$; accordingly the explicit foldings computed below yield $B_n$ from $A_{2n-1}$ and $C_n$ from $D_{n+1}$ (types $F_4$ and $G_2$ are self-dual and unaffected).
:::

## Folded roots and folded root systems

::: {.definition #def:folded-root title="Folded root systems"}

Let $L$ be a lattice containing a root system $\Phi$ and $G \subset \Orth(L)$ a finite group preserving $\Phi$.
Given a simple root $\alpha_i \in \Phi$, let $[\alpha_i] \subset \Phi$ denote its $G$-orbit.

The associated **folded root** and **folded root system** are defined by
$$
\beta_{[\alpha_i]} \definedas \Sum_{\alpha_j \in [\alpha_i]} \alpha_j \in L^G,
\qquad
\Phi^G \definedas \theset{ \beta_{[\alpha_i]} \in L^G \mid [\alpha_i] \in \Phi/G }
.
$$

Each folded root corresponds to a folded node in the Dynkin diagram.
For an involution $I$, $\beta_{[\alpha_i]} = \alpha_i + I(\alpha_i) \in L^G$.
:::

## Examples

::: {.example #ex:classical-foldings title="Examples of classical foldings"}

Folding produces scaled root systems in the invariant lattice $L^G$.
Explicit examples computed via @def:folded-root:

- **$A_5 \to B_3(2)$**: under horizontal reflection ($G = S_2$), $\Phi(A_5^G)$ has Gram matrix $G_{B_3(2)} = 2 \cdot G_{B_3} = \begin{pmatrix} 4 & -2 & 0 \\ -2 & 4 & -2 \\ 0 & -2 & 2 \end{pmatrix}$ (norms $4, 4, 2$: two long, one short).

- **$D_4 \to C_3$**: under vertical reflection ($G = S_2$), $\Phi(D_4^G)$ has Gram matrix equal to $G_{C_3}$.

- **$D_4 \to G_2$**: under rotation by $2\pi/3$ ($G = \ZZ/3\ZZ$), $\Phi(D_4^G)$ has Gram matrix equal to $G_{G_2}$.

- **$E_6 \to F_4(2)$**: under horizontal reflection ($G = S_2$), $\Phi(E_6^G)$ has Gram matrix equal to $G_{F_4(2)}$.

Here the scaling notation $B_3(2)$ and $F_4(2)$ records that the invariant-lattice Gram matrix equals the corresponding root-system Gram matrix rescaled by $2$.
(These Gram matrices are written in the standard positive-definite normalization; negate for the AG convention of @def:root-lattice.)
:::

## The root-folding criterion for $\tdp$

The criterion below is stated in terms of the short and long roots of $\tdp$: $\Phi^2$ denotes the **short roots** (norm $-2$) and $\Phi^4$ the **long roots** (norm $-4$ with divisor $2$), in the $k$-root sense of the root systems material.

::: {.lemma #lem:root-folding-tdp title="Root folding criterion"}

Let $\Phi(\tdp)$ be the root system of $\tdp$ and $I = -\Ien$ the induced involution on $\tdp$ whose fixed lattice is $\ten$.

The folded roots $\beta_{[v]} \in \Phi\left( \tdp^{\generators{I}} \right)$ arise in exactly one of the following ways:

1. $v \in \Phi^2(\tdp)$ and $\beta_{[v]} \in \Phi(\ten)$;

2. $v \in \Phi^4(\tdp)$ and $\beta_{[v]} \in \Phi(\ten)$; or

3. $v \in \Phi^2(\tdp) \intersect I(v)^{\perp \tdp}$, and so $\beta_{[v]} \definedas v + I(v) \in \Phi^4(\ten)$ is the sum of orthogonal roots in $\Phi^2(\tdp)$.
:::

This criterion governs how roots in the boundary lattices at the $0$-cusps of $\fttz$ descend or combine when passing to the $I$-invariant sublattices corresponding to $\fentwo$.

## Mirror moves

::: {.definition #def:mirror-move title="Mirror moves"}

A **mirror move** is a lattice-theoretic operation governed by the existence of a primitive isotropic vector $\eta \in T$ of a specified type and splitting:

- **Odd/simple:** $\div_T(\eta) = 1$, splitting as $T \cong U \oplus K$.
  The new invariants are $(r-2, a, 1)$.

- **Even, ordinary:** $\div_T(\eta) = 2$ and $\eta^*$ is ordinary, splitting as $T \cong U(2) \oplus K$.
  The new invariants are $(r-2, a-2, 1)$.

- **Even, characteristic:** $\div_T(\eta) = 2$ and $\eta^*$ is characteristic, splitting as $T \cong I_{1,1}(2) \oplus K$.
  The new invariants are $(r-2, a-2, 0)$.

The move replaces $T$ with $\overline{T}_\eta = \eta^{\perp T}/\eta$, navigating Nikulin's pyramid of $2$-elementary lattices to compute cusp diagrams when $\Gamma = \Orth^+(T)$.
:::
