# Levels, modularity, and discriminant characters {#sec:lattice-levels-characters}

::: {.definition #def:lattice-level title="Arithmetic level"}

Let $L$ be a nondegenerate integral lattice.
Its **quadratic level** is
$$
N_q(L)
\definedas
\min\theset{
N>0
\st
N\,\beta_{L_\bQ}(x,x)\in2\bZ
\text{ for every }x\in L^\#
}.
$$
Equivalently, after choosing an ordered basis with Gram matrix $G_L$, the matrix $N_q(L)G_L^{-1}$ is integral with even diagonal.
For even $L$, this is the level used in the theory of theta series [@Han13; @SSP99].
If
$$
N_b(L)\definedas\exp(L^\#/L)
$$
is the bilinear denominator of @def:discriminant, then
$$
N_q(L)\in\theset{N_b(L),\,2N_b(L)}.
$$
:::

::: {.definition #def:modular-lattice-global title="$N$-modular lattices"}

Let $L$ be a nondegenerate integral lattice and $N>0$.
The lattice is **$N$-modular** when there exists an isometry
$$
\phi\colon L^\#(N)\isoto L.
$$
Equivalently, the rational quadratic space $L_\bQ$ admits a similarity of multiplier $N$ carrying the dual lattice onto $L$ [@Que95].
For $N=1$ this is unimodularity.
:::

::: {.observation #obs:homothetic-modularity title="Homothetic modularity"}

The homothetic condition is stronger: multiplication by $N$ on $L^\#$ factors through $\iota_L\colon L\injects L^\#$ as an isomorphism
$$
h_N\colon L^\#\isoto L
$$
such that
$$
\iota_L\circ h_N=[N]_{L^\#}.
$$
This implies $N$-modularity but records a specified rational realization rather than only the similarity class.
:::

::: {.definition #def:lattice-bad-primes title="Bad primes of an integral lattice"}

For a nondegenerate integral lattice $L$, define
$$
\Sigma_L
\definedas
\Sigma_L\definedas\theset{p\text{ prime}\st p\mid2\disc{L}}.
$$
For every odd prime $p\notin\Sigma_L$, the reduction
$$
L_{\bF_p}\definedas L\tensor_\bZ\bF_p
$$
is nondegenerate.
:::

::: {.definition #def:lattice-discriminant-character title="The discriminant quadratic character"}

Let $L$ be a nondegenerate integral lattice of even rank $2m$.
Set
$$
\Delta_L\definedas(-1)^m\disc{L}.
$$
Let $d_L$ be the fundamental discriminant of $\bQ(\sqrt{\Delta_L})$, with $d_L=1$ when $\Delta_L$ is a square.
Define
$$
\chi_L\colon(\bZ/|d_L|\bZ)^\times\too\theset{\pm1},
\qquad
\chi_L(a)\definedas\left(\frac{d_L}{a}\right),
$$
using the Kronecker symbol.
:::

::: {.proposition #prop:discriminant-character-finite-field title="Finite-field characterization"}

Let $p$ be an odd prime with
$$
p\nmid2\disc{L}.
$$
Then $L_{\bF_p}$ is a nondegenerate quadratic space of dimension $2m$, and
$$
\chi_L(p)=1
$$
exactly when
$$
L_{\bF_p}\isoto H^{\perp m}
$$
is split [@CS10, Ch. 15].
:::
