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
For an involution $I$, the orbit $[\alpha_i]$ is $\theset{\alpha_i}$ or $\theset{\alpha_i, I(\alpha_i)}$, so $\beta_{[\alpha_i]} = \alpha_i$ if $I(\alpha_i) = \alpha_i$ and $\beta_{[\alpha_i]} = \alpha_i + I(\alpha_i)$ otherwise.
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

Let $\Phi(\tdp) = \Phi^2(\tdp)\union\Phi^4(\tdp)$ be the set of roots of $\tdp$ (@def:2elementary-roots), let $I = -\Ien$ be the involution of $\tdp$ induced by $\Ien$, whose fixed lattice is $\ten$, and write $x\cdot y$ for the form of $\tdp$.
For $v\in\Phi(\tdp)$ let $\beta_{[v]}\in\ten$ be the folded vector of its $\generators{I}$-orbit (@def:folded-root): $\beta_{[v]} = v$ if $I(v) = v$, and $\beta_{[v]} = v + I(v)$ otherwise.
Then $\beta_{[v]}\in\Phi(\ten)$ if and only if exactly one of the following holds:

1. $I(v) = v$ and $v\in\Phi^2(\tdp)$, in which case $\beta_{[v]} = v\in\Phi^2(\ten)$;

2. $I(v) = v$ and $v\in\Phi^4(\tdp)$, in which case $\beta_{[v]} = v\in\Phi^4(\ten)$; or

3. $v\in\Phi^2(\tdp)$ and $v\cdot I(v) = 0$, in which case $\beta_{[v]} = v + I(v)\in\Phi^4(\ten)$ is the sum of two orthogonal roots in $\Phi^2(\tdp)$.

In particular, a long root $v\in\Phi^4(\tdp)$ with $I(v)\neq v$ never folds to a root of $\ten$.
:::

::: {.proof}

By @def:lattice-involutions-k3 [@AEGS25, Def. 2.3], $\tdp = \lkt^{\Idp = -1}$ consists of the vectors $(u_1, w, -w, \alpha_1, \alpha_2)$ with $u_1, w\in U$ and $\alpha_1,\alpha_2\in E_8$.
Write such a vector as $(u, \alpha_1, \alpha_2)$ with $u = (u_1, w, -w)$ in the sublattice $N\cong U\oplus U(2)$ formed by the first three coordinates, so that $\tdp = N\perp E_8\perp E_8$.
Then $I(u, \alpha_1, \alpha_2) = -\Ien(u, \alpha_1, \alpha_2) = (u, -\alpha_2, -\alpha_1)$, whose fixed vectors $(u, \alpha, -\alpha)$ form $\lkt^{\Ien = -1} = \ten$.
By @prop:k3-cover-eigenlattices both $\tdp$ and $\ten$ are even and $2$-elementary, so their roots are the two types of @def:2elementary-roots.

Suppose $I(v) = v$, so $\beta_{[v]} = v\in\ten$.
If $v = m y$ with $y\in\ten$ then $y\in\tdp$, so $v$ is primitive in $\ten$ because it is primitive in $\tdp$.
If $v^2 = -2$, then $v\in\Phi^2(\ten)$.
If $v^2 = -4$, then $v\cdot\ten\iscontainedin v\cdot\tdp\iscontainedin 2\ZZ$, so $v$ satisfies the integrality condition of @def:k-root in $\ten$, and $v\in\Phi^4(\ten)$ by @prop:root-integrality.
So in this case $\beta_{[v]}\in\Phi(\ten)$, and (1) or (2) holds according to $v^2$.

Suppose $I(v)\neq v$, so $\beta = \beta_{[v]} = v + I(v)$.
Because $I$ is an isometry,
$$
\beta^2 = 2v^2 + 2\,v\cdot I(v),
\qquad
\beta\cdot x = v\cdot x + v\cdot I(x) = 2\,v\cdot x
\quad\text{for } x\in\ten
.
$$
In coordinates $\beta = (2u, \alpha_1 - \alpha_2, \alpha_2 - \alpha_1)$, so $\beta^2 = 4u^2 + 2(\alpha_1-\alpha_2)^2\in 4\ZZ$, since $N$ and $E_8$ are even.
So $\beta^2\neq -2$, and by @def:2elementary-roots $\beta\in\Phi(\ten)$ exactly when $\beta^2 = -4$ and $\div_\ten(\beta) = 2$.
If $\beta^2 = -4$ and $\beta = m y$ with $y\in\ten$, then $y^2 = -4/m^2$ lies in $2\ZZ$, so $m = \pm1$ and $\beta$ is primitive; and $\beta\cdot\ten\iscontainedin 2\ZZ$ by the displayed identity, so $\div_\ten(\beta) = 2$.
Hence $\beta\in\Phi(\ten)$ if and only if $v^2 + v\cdot I(v) = -2$.

For $v\in\Phi^2(\tdp)$ this is the condition $v\cdot I(v) = 0$ of (3), and then $v$ and $I(v)$ are orthogonal roots in $\Phi^2(\tdp)$.
For $v\in\Phi^4(\tdp)$ it would require $v\cdot I(v) = 2$.
But $\div_\tdp(v) = 2$ gives $u\cdot N\iscontainedin 2\ZZ$ and $\alpha_j\cdot E_8\iscontainedin 2\ZZ$.
As $E_8$ is unimodular, $\alpha_j\in 2E_8$, so $\alpha_1\cdot\alpha_2\in 4\ZZ$.
Writing $u = u' + u''$ with $u'\in U$ and $u''\in U(2)$, unimodularity of $U$ gives $u'\in 2U$, so $u'^2\in 8\ZZ$, while $u''^2\in 4\ZZ$ because the form of $U(2)$ is twice an even form.
So $v\cdot I(v) = u^2 - 2\,\alpha_1\cdot\alpha_2\in 4\ZZ$, which excludes $v\cdot I(v) = 2$.

The three cases are mutually exclusive: (1) and (2) differ in $v^2$, and in (3) $v\cdot I(v) = 0\neq v^2$, so $I(v)\neq v$.
This is the forward direction of [@AEGS25, Lemma 3.4], which assumes in addition that $\beta_{[v]}^2 < 0$.
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
