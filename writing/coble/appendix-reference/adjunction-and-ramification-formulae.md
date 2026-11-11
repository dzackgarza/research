# Formulae

::: {.proposition #prop:canonical-class-of-blowup title="Canonical class of a blowup"}

Let $X$ be a nonsingular variety, let $V\iscontainedin X$ be a nonsingular subvariety of codimension $r\geq 2$, let $f\colon Y = \Bl_V X\to X$ be the blowup of $X$ along $V$, and let $E = f^{-1}(V)$.
Then
$$
K_Y = f^* K_X + (r - 1)E
$$
[@Har10a, II Ex. 8.5(b)].
If $X$ is a nonsingular projective surface and $V$ is a point, then $K_Y = f^*K_X + E$ and $K_Y^2 = K_X^2 - 1$ [@Har10a, V.3.3].
:::

::: {.proposition #prop:ramification-formula-curves title="Canonical divisors under a finite separable morphism of curves"}

Let $k$ be an algebraically closed field, and let $f\colon Y\to X$ be a finite separable morphism of complete nonsingular curves over $k$.
The **ramification divisor** of $f$ is
$$
R \definedas \Sum_{p\in Y} \mathrm{len}\qty{\Omega_{Y/X, p}}\, p
.
$$
Then $K_Y \sim f^* K_X + R$ [@Har10a, IV.2.3 and the definition before it].
:::
