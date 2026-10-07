# Orthogonal complements of lattice embeddings {#sec:lattice-orthogonal-complements}

::: {.definition #def:orthogonal-direct-sum-complement title="Orthogonal sums and complements"}

For integral lattices $L_1,L_2$, write
$$
L_1\perp L_2
$$
for their orthogonal sum from @def:orthogonal-sum.

Let
$$
\eta\colon M\injects L
$$
be a lattice morphism.
Pairing with $\eta$ defines
$$
\lambda_\eta\colon
L
\too
M^*,
\qquad
\lambda_\eta(x)(m)
=
\beta_L(x,\eta(m)).
$$
Define the orthogonal complement by the exact sequence
$$
0
\too
M^{\perp L}
\xrightarrow{\kappa_\eta}
L
\xrightarrow{\lambda_\eta}
\operatorname{im}(\lambda_\eta)
\too
0.
$$

Since $M$ is nondegenerate, the induced morphism
$$
j_\eta\colon
M\perp M^{\perp L}
\injects
L
$$
has full rank.
Hence its carrier cokernel is finite.

The discriminant functor is additive on orthogonal sums:
$$
A_{L_1\perp\cdots\perp L_n}
\isoto
A_{L_1}\perp\cdots\perp A_{L_n}.
$$
If all summands are even, the same statement holds for the quadratic refinements:
$$
A_{L_1\perp\cdots\perp L_n,q}
\isoto
A_{L_1,q}\perp\cdots\perp A_{L_n,q}.
$$
:::
