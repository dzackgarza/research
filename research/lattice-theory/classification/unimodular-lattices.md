# Classification of unimodular lattices {#sec:unimodular-lattice-classification}

::: {.theorem #thm:indefinite-unimodular-classification title="Classification of indefinite unimodular lattices"}

Let $L$ be an indefinite unimodular integral lattice of signature $(p,q)$.

If $L$ is odd, then
$$
L\isoto
\latI_{p,q}
\definedas
\generators{1}^{\perp p}
\perp
\generators{-1}^{\perp q}.
$$

If $L$ is even, then
$$
p-q\equiv0\pmod8
$$
and
$$
L\isoto\latII_{p,q},
$$
where
$$
\latII_{p,q}
\definedas
\begin{cases}
U^{\perp p}\perp E_8^{\perp(q-p)/8},&p<q,\\
U^{\perp q}\perp E_8(-1)^{\perp(p-q)/8},&p>q.
\end{cases}
$$
Thus signature and parity determine the integral isometry class [@Ser73, Ch. V; @MH73, Ch. II].
:::

::: {.theorem #thm:small-unimodular-classification title="Unimodular lattices of rank at most four"}

Let $0\neq L$ be unimodular with
$$
\rank_\bZL\leq4.
$$
If $L$ is odd, then
$$
L\isoto\latI_{p,q}
$$
for its signature $(p,q)$.
If $L$ is even, then
$$
L\isoto U
\qquad\text{or}\qquad
L\isoto U^{\perp2},
$$
according as $\rank_\bZL=2$ or $4$ [@MH73, Ch. II; @CS10, Ch. 15].
:::
