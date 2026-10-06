# Indefinite even $2$-elementary lattices {#sec:indefinite-two-elementary-lattices}

::: {.definition #def:two-elementary-isotropic-types title="Primitive isotropic-vector types"}

Let $L$ be an even $2$-elementary lattice.
For every primitive vector,
$$
\div_L(v)\in\theset{1,2}.
$$
Since $L^\#/L$ is $2$-elementary,
$$
N_b(L)=2.
$$
Let
$$
r_L\colon
\tfrac2{N_q(L)}\bZ/2\bZ
\too
\tfrac12\bZ/\bZ
$$
be the restriction of the canonical quotient $\bQ/2\bZ\to\bQ/\bZ$.

For $v$ with $\div_L(v)=2$, its discriminant class
$$
v^*\in L^\#/L
$$
from @def:lattice-basic-invariants is **characteristic** when
$$
r_L\bigl(q_L(x)\bigr)
=
\bar\beta_L(v^*,x)
\qquad
\text{for every }x\in L^\#/L.
$$
Otherwise $v^*$ is **ordinary**.

For
$$
e\in L^{\mathrm{prim}}[0],
$$
define its type by

1. **odd** when $\div_L(e)=1$;

2. **even ordinary** when $\div_L(e)=2$ and $e^*$ is ordinary;

3. **even characteristic** when $\div_L(e)=2$ and $e^*$ is characteristic.
:::

::: {.theorem #thm:two-elementary-classification title="Nikulin's classification of indefinite even $2$-elementary lattices"}

Let $L$ be an indefinite even $2$-elementary lattice.
Set
$$
r\definedas\rank_\bZL,
\qquad
a\definedas\dim_{\bF_2}(L^\#/L).
$$
Define
$$
\delta(L)=0
$$
when the quadratic morphism of $A_{L,q}$ factors through
$$
\bZ/2\bZ
\injects
\tfrac2{N_q(L)}\bZ/2\bZ,
$$
and set $\delta(L)=1$ otherwise.

Then the integral isometry class of $L$ is determined by its signature and
$$
(r,a,\delta(L)),
$$
subject to the admissibility conditions of [@Nik80, Thm. 3.6.2].
:::

::: {.theorem #thm:isotropic-trichotomy title="Primitive isotropic vectors in a hyperbolic $2$-elementary lattice"}

Let $S$ be an even hyperbolic $2$-elementary lattice with invariants $(r,a,\delta)$, and let
$$
v\in S^{\mathrm{prim}}[0].
$$
Let
$$
\generators{v}_\bZ\injects v^{\perp S}
$$
be the canonical primitive rank-one subobject, and define $\overline S_v$ by
$$
0
\too
\generators{v}_\bZ
\too
v^{\perp S}
\too
\overline S_v
\too
0.
$$
Then exactly one of the following holds [@AE22, Prop. 5.5]:

1. If $v$ is odd,
   $$
   S\isoto U\perp\overline S_v,
   $$
   and $\overline S_v$ has invariants $(r-2,a,\delta)$.

2. If $v$ is even ordinary,
   $$
   S\isoto U(2)\perp\overline S_v,
   $$
   and $\overline S_v$ has invariants $(r-2,a-2,\delta)$.

3. If $v$ is even characteristic,
   $$
   S\isoto\latI_{1,1}(2)\perp\overline S_v,
   $$
   necessarily $\delta=1$, and $\overline S_v$ has invariants $(r-2,a-2,0)$.

In every case $\overline S_v$ is even negative definite of rank $r-2$.
:::
