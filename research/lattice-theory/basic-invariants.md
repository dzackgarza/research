# Basic lattice invariants {#sec:basic-lattice-invariants}

::: {.definition #def:lattice-basic-invariants title="Basic lattice invariants"}

Let $L\in\mathbf{Lat}_{\bZ}$.
Write
$$
vw\definedas\beta_L(v,w),
\qquad
v^2\definedas\beta_L(v,v),
$$
and define the norm map
$$
q\colon L\too\bZ,
\qquad
q(v)\definedas v^2.
$$
For $v\in L$, let
$$
i_v\colon\bZ\too L,
\qquad
i_v(1)=v.
$$
For $n\in\bZ$, define
$$
L[n]\definedas q^{-1}(n),
\qquad
L^{\mathrm{prim}}[n]
\definedas
\theset{v\in L[n]\st i_v\in\operatorname{PrimEmb}(\bZ,L)}.
$$

Define the **divisibility** $\div_L(v)\geq0$ by the image factorization
$$
\operatorname{im}\bigl(\beta_L(v,-)\colon L\to\bZ\bigr)
=
\div_L(v)\bZ.
$$
For nonzero primitive $v$, the morphism
$$
\bZ\too\bQ,
\qquad
1\longmapsto\frac1{\div_L(v)}
$$
and scalar extension of $v$ determine
$$
\frac{v}{\div_L(v)}\in L^\#.
$$
Let
$$
\pi_L\colon L^\#\twoheadrightarrow L^\#/L
$$
be the quotient map to the carrier of $A_L$.
Define the **discriminant class**
$$
v^*
\definedas
\pi_L\!\left(\frac{v}{\div_L(v)}\right)
\in
L^\#/L.
$$

For a scalar extension $\bZ\to R$, write
$$
L_R\definedas L\tensor_\bZ R
$$
and $\beta_{L_R}$ for the induced form.
The rank is
$$
\rank_\bZ L=\dim_\bQ L_\bQ,
$$
and the signature is the unique component of $\operatorname{sig}_\bZ(L,\beta_L)$ from @def:signature.
:::
