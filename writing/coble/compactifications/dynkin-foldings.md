# Foldings of Dynkin diagrams {#sec-dynkin-foldings}

::: {.notation title="Sign convention"}

Root lattices are negative definite and roots have norm $-2$ (@def:root-lattice).
:::

## Foldings of simply-laced diagrams

::: {.proposition #prop:classical-foldings title="Classical foldings of Dynkin diagrams"}

Let $(X_N, r)$ be one of $(D_{n+1}, 2)$, $(A_{2n-1}, 2)$, $(E_6, 2)$ or $(D_4, 3)$, and let $\mu$ be the diagram automorphism of order $r$ of the simple Lie algebra $\mathfrak{g}(X_N)$.
Then the fixed point subalgebra $\mathfrak{g}(X_N)^{\mu}$ is the simple Lie algebra of type $B_n$, $C_n$, $F_4$ or $G_2$, respectively.
The simple roots of $X_N$ fixed by $\mu$ are long simple roots of $\mathfrak{g}(X_N)^{\mu}$, and the sum of the simple roots in a $\mu$-orbit of size $r$ is $r$ times a short simple root.
So the orbit sums of the simple roots of $X_N$ are the simple coroots $\Pi_\ell \cup r\Pi_s$ of $\mathfrak{g}(X_N)^{\mu}$ [@Kac90, Prop. 7.9(b), (e), (f)].
:::

::: {.proof}

This is [@Kac90, Prop. 7.9(b), (e), (f)].
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

Number the simple roots as in Bourbaki and write Gram matrices for the positive-definite root lattices; the Gram matrices in the convention of @def:root-lattice are their negatives.
For each diagram automorphism below, the simple roots in one orbit are pairwise orthogonal, and the folded roots of @def:folded-root have the following Gram matrices.

- **$A_5 \to B_3(2)$**: for the involution with orbits $\{\alpha_1, \alpha_5\}, \{\alpha_2, \alpha_4\}, \{\alpha_3\}$, the Gram matrix is $\begin{pmatrix} 4 & -2 & 0 \\ -2 & 4 & -2 \\ 0 & -2 & 2 \end{pmatrix} = 2\, G_{B_3}$ (norms $4, 4, 2$: two long, one short).

- **$D_4 \to C_3$**: for the involution with orbits $\{\alpha_1\}, \{\alpha_2\}, \{\alpha_3, \alpha_4\}$, the Gram matrix is $\begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -2 \\ 0 & -2 & 4 \end{pmatrix} = G_{C_3}$.

- **$D_4 \to G_2$**: for the automorphism of order $3$ with orbits $\{\alpha_2\}, \{\alpha_1, \alpha_3, \alpha_4\}$, the Gram matrix is $\begin{pmatrix} 2 & -3 \\ -3 & 6 \end{pmatrix} = G_{G_2}$.

- **$E_6 \to F_4(2)$**: for the involution with orbits $\{\alpha_1, \alpha_6\}, \{\alpha_3, \alpha_5\}, \{\alpha_4\}, \{\alpha_2\}$, the Gram matrix is $\begin{pmatrix} 4 & -2 & 0 & 0 \\ -2 & 4 & -2 & 0 \\ 0 & -2 & 2 & -1 \\ 0 & 0 & -1 & 2 \end{pmatrix} = 2\, G_{F_4}$.

Here $G_{B_3}$, $G_{C_3}$, $G_{G_2}$ and $G_{F_4}$ are the Gram matrices of the simple roots of the root systems in their Bourbaki coordinates, and the scaling notation $B_3(2)$ and $F_4(2)$ records the factor $2$.
In each case the type is the Langlands dual of the type of the fixed point subalgebra in @prop:classical-foldings, as the orbit sums are its simple coroots.
:::

## The root-folding criterion for $\tdp$

::: {.notation title="Short and long roots of $\tdp$"}

$\Phi^2$ denotes the **short roots** ($(-2)$-roots) and $\Phi^4$ the **long roots** ($(-4)$-roots, of divisibility $2$) of @def:k-root.
:::

::: {.lemma #lem:root-folding-tdp title="Root folding criterion"}

Let $\Phi(\tdp)$ be the root system of $\tdp$ and $I = -\Ien$ the induced involution on $\tdp$ whose fixed lattice is $\ten$.

The folded roots $\beta_{[v]} \in \Phi\left( \tdp^{\generators{I}} \right)$ arise in exactly one of the following ways:

1. $v \in \Phi^2(\tdp)$ and $\beta_{[v]} \in \Phi(\ten)$;

2. $v \in \Phi^4(\tdp)$ and $\beta_{[v]} \in \Phi(\ten)$; or

3. $v \in \Phi^2(\tdp) \intersect I(v)^{\perp \tdp}$, and so $\beta_{[v]} \definedas v + I(v) \in \Phi^4(\ten)$ is the sum of orthogonal roots in $\Phi^2(\tdp)$.
:::

::: {.proof}

The folded diagram is computed from the involution by the recipe of @def:folded-root: an orbit of roots under the involution is a single node of the folded diagram, and its bond order to another orbit is the number of simple reflections relating them.
:::

## Mirror moves

::: {.definition #def:mirror-move title="Mirror moves"}

A **mirror move** is a lattice-theoretic operation governed by the existence of a primitive isotropic vector $\eta \in T$ of a specified type and splitting:

- **Odd/simple:** $\div_T(\eta) = 1$, splitting as $T \cong U \oplus K$.
  The new invariants are $(r-2, a, 1)$.

- **Even, ordinary:** $\div_T(\eta) = 2$ and $\eta^*$ is ordinary, splitting as $T \cong U(2) \oplus K$.
  The new invariants are $(r-2, a-2, 1)$.

- **Even, characteristic:** $\div_T(\eta) = 2$ and $\eta^*$ is characteristic, splitting as $T \cong I_{1,1}(2) \oplus K$.
  The new invariants are $(r-2, a-2, 0)$.

The move replaces $T$ with $\overline{T}_\eta = \eta^{\perp T}/\eta$.
:::
