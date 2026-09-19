### Anticanonical Pairs and Kulikov Models

#### Charge

The components of certain singular fibers in degenerations are naturally described as log Calabi–Yau surfaces, also known as anticanonical pairs.

:::{.definition title="Anticanonical Pairs" #def:anticanonical-pairs}
Let $V$ be a smooth projective rational surface, and let $D = \sum_j D_j$ be a reduced divisor on $V$ with simple normal crossings. The pair $(V, D)$ is called an **anticanonical pair** if the log canonical divisor is $\QQ$-linearly trivial:

\begin{align*}
K_V + D \sim_{\QQ} 0.
.\end{align*}

Such pairs are also called **log Calabi-Yau surfaces**. If $V$ is a toric surface and $D = \partial V$ is its toric boundary divisor, $(V, D)$ is called a **toric anticanonical pair**. Common examples include pairs where $D$ is a smooth elliptic curve, a cycle of $n \ge 2$ smooth rational curves, or an irreducible rational nodal curve. For a classification of exceptional cases, see [@GHK15, Lem. 4.2].
The following is a numerical invariant that measures the deviation of an anticanonical pair from being toric.
:::


:::{.definition title="Charge of an Anticanonical Pair" #def:charge-anticanonical-pair}
Let $(V, D = \sum_j D_j)$ be an anticanonical pair. The **charge** of the pair is defined as

\begin{align*}
Q(V, D) \da  12 - \sum_j (D_j^2 + 3).
.\end{align*}

This quantity is a non-negative integer for all anticanonical pairs and is zero if and only if the pair $(V, D)$ is toric.
:::

The definition of charge can be restated using the adjunction formula, depending on the geometry of the boundary divisor $D$.

:::{.definition title="Alternative Formulas for Charge" #def:charge-alt-formulas}
Let $(V, D)$ be an anticanonical pair. If $D = \sum_j D_j$ is a nodal cycle of $n \ge 2$ rational components, the charge is $Q(V, D) = 12 + \sum_j (-D_j^2 - 3)$. If $D$ is an irreducible nodal curve, the charge is $Q(V, D) = 11 - D^2$.
:::

#### Toric Models and Blowups

Rational anticanonical pairs can be constructed from toric pairs via a sequence of two fundamental types of birational modifications.

:::{.definition title="Corner and Interior Blowups" #def:corner-interior-blowups}
Let $(V, D)$ be an anticanonical pair.

- A **corner blowup** is the blowup of $V$ at a node of $D$. If $\pi: V' \to V$ is such a blowup and $D'$ is the reduced total transform of $D$, then $(V', D')$ is an anticanonical pair with its charge preserved: $Q(V', D') = Q(V, D)$.

- An **interior blowup** is the blowup of $V$ at a smooth point of a component of $D$. If $D''$ is the union of the proper transform of $D$ and the exceptional divisor, then $(V'', D'')$ is an anticanonical pair whose charge increases by one: $Q(V'', D'') = Q(V, D) + 1$.
:::

Any rational anticanonical pair can be obtained from a toric pair (which has charge 0) by a sequence of corner blowups followed by a sequence of interior blowups [@GHK15].
In the context of K3 surface degenerations, these local invariants are subject to a global conservation law discovered by Friedman and Morrison.

:::{.theorem title="Friedman–Morrison Charge Theorem for Type $\III$ Degenerations" #thm:friedman-morrison-charge}
Let $\mcx \to \Delta$ be a Type $\III$ Kulikov degeneration of K3 surfaces, with $\mcx_0$ $\mcx_0 = \bigcup_{i=1}^n V_i$. For each component $V_i$, let $D_i = V_i \cap \overline{(\mcx_0 \setminus V_i)}$ be its boundary divisor, so that $(V_i, D_i)$ is an anticanonical pair. Then the sum of the charges of these pairs is constant:

\begin{align*}
\sum_{i=1}^n Q(V_i, D_i) = 24.
.\end{align*}

This imposes the constraint that at most 24 of the components $V_i$ can be non-toric, as toric pairs contribute zero to the sum. This result provides a rigidity condition on the combinatorics of K3 degenerations [@FM83, Thm. 2.2], [@Fri15].
:::

:::{.remark}
The conservation property constrains the possible combinatorial types of $\mcx_0$s and ensures that the total complexity of a degeneration, as measured by the charge, remains constant across the moduli space. This invariance establishes the relationship between the KSBA and Baily-Borel compactifications of the moduli space.
:::

