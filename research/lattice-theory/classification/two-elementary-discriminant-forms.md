# Classification of $2$-elementary discriminant forms {#sec:two-elementary-discriminant-classification}

## Decomposability of even $2$-elementary lattices

::: {.theorem #thm:2elementary-decomposition title="Decomposition of $2$-elementary discriminant forms"}

Let $L$ be an even $2$-elementary lattice.
Then the discriminant quadratic form on $A_L$ is an orthogonal direct sum of the four elementary discriminant forms $p$, $q$, $u$, $v$, subject only to the relations
$$
\begin{aligned}
u^{\oplus 2} &= v^{\oplus 2}, &
p^{\oplus 4} &= q^{\oplus 4}, \\
u\oplus p &= (p\oplus q)\oplus p, &
u\oplus q &= (p\oplus q)\oplus q, \\
v\oplus p &= q^{\oplus 3}, &
v\oplus q &= p^{\oplus 3}
.
\end{aligned}
$$
Here $p$ and $q$ are the two rank-one forms on $\ZZ/2\ZZ$, realized as the discriminant forms of $\generators{2}$ and $\generators{-2}$, while $u$ and $v$ are the two rank-two forms on $(\ZZ/2\ZZ)^2$, realized as the discriminant forms of $U(2)$ and of $V = V_1$ respectively.
:::

::: {.proof}

The relations record the coincidences among finite $2$-adic quadratic forms established by Nikulin [@Nik80]: for instance $u^{\oplus 2} = v^{\oplus 2}$ expresses that two orthogonal copies of the even rank-two form agree with two copies of the odd one, and $v\oplus p = q^{\oplus 3}$ resolves the odd rank-two form against the rank-one forms.
Together they present the semigroup of $2$-elementary discriminant forms under orthogonal sum, so that every $A_L$ has a normal form in the generators $p, q, u, v$.
:::
