# Levels, modularity, and discriminant characters {#sec-lattice-levels-characters}

::: {.definition #def:lattice-level title="Arithmetic level" defines="quadratic level; bilinear denominator; $N_q(L)$; $N_b(L)$"}

Let $L$ be a nondegenerate (@def:polarization) integral lattice.
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
Equivalently, after choosing an ordered basis (@def:based-module) with Gram matrix $G_L$, the matrix $N_q(L)G_L^{-1}$ is integral with even (@def:form-axioms) diagonal (@def:polarization-functors).
For even $L$, this is the level used in the theory of theta series [@Han13; @SSP99].
Its **bilinear denominator** is the exponent of the finite group (@def:group) $L^\#/L$,
$$
N_b(L)\definedas\exp(L^\#/L),
$$
and
$$
N_q(L)\in\theset{N_b(L),\,2N_b(L)}.
$$
:::

::: {.definition #def:modular-lattice-global title="$N$-modular lattices" defines="$N$-modular lattice"}

Let $L$ be a nondegenerate (@def:polarization) integral lattice and $N>0$.
The lattice is **$N$-modular** when there exists an isometry
$$
\phi\colon L^\#(N)\isoto L.
$$
Equivalently, the rational quadratic space $L_\bQ$ admits a similarity of multiplier $N$ carrying the dual lattice onto $L$ [@Que95].
For $N=1$ this is unimodularity.
:::

::: {.definition #def:lattice-bad-primes title="Bad primes of an integral lattice" defines="bad prime; $\Sigma_L$; $L_{\bF_p}$"}

For a nondegenerate (@def:polarization) integral lattice $L$, define
$$
\Sigma_L
\definedas
\theset{p\text{ prime}\st p\mid2\disc{L}}.
$$
For every odd (@def:two-elementary-isotropic-types) prime $p\notin\Sigma_L$, the reduction
$$
L_{\bF_p}\definedas L\tensor_\bZ\bF_p
$$
is nondegenerate.
:::

::: {.definition #def:lattice-discriminant-character title="The discriminant quadratic character" defines="discriminant quadratic character; $\Delta_L$; $d_L$; $\chi_L$"}

Let $L$ be a nondegenerate (@def:polarization) integral lattice of even (@def:form-axioms) rank $2m$.
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

Let $p$ be an odd (@def:two-elementary-isotropic-types) prime with
$$
p\nmid2\disc{L}.
$$
Then $L_{\bF_p}$ is a nondegenerate (@def:polarization) quadratic space of dimension $2m$, and
$$
\chi_L(p)=1
$$
exactly when
$$
L_{\bF_p}\isoto H^{\perp m}
$$
is split (@def:hyperbolic-plane) [@CS10, Ch. 15].
:::

::: {.proof}

The space $H^{\perp m}$ has discriminant $(-1)^m$, and nondegenerate quadratic spaces over $\bF_p$ are classified by dimension and discriminant [@Ser73, Ch. IV §1.7, Prop. 5].
So $L_{\bF_p}$ is split exactly when $\Delta_L$ is a square modulo $p$.
The quotient $\Delta_L/d_L$ is a rational square and $p\nmid d_L$, so this holds exactly when $\left(\frac{d_L}{p}\right)=1$, that is, when $\chi_L(p)=1$.
:::

## Theta series

::: {.proposition #prop:positive-lattice-theta-modularity title="Theta series of an even positive-definite lattice"}

Let $L$ be an even (@def:form-axioms) positive-definite lattice of rank $2m$ and quadratic
level (@def:lattice-level) $N=N_q(L)$. Its theta series is
$$
\Theta_L(\tau)
\definedas
\sum_{x\in L}e^{\pi i\tau\beta(x,x)}
=\sum_{n\geq0}r_L(n)q^n,
\qquad
r_L(n)=\#\theset{x\in L\st\beta(x,x)=2n},
\quad q=e^{2\pi i\tau}.
$$
It is a holomorphic modular form of weight $m$ on $\Gamma_0(N)$
with discriminant character $\chi_L$ of
@def:lattice-discriminant-character [@Han13, §3].
The positive-definiteness assumption makes each coefficient finite.
For an indefinite (@def:definiteness) lattice, this unregularized series does not define
the same holomorphic modular form.
:::
