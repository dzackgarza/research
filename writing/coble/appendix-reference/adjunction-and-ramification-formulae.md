# Formulae

## Divisors and intersection numbers

For a morphism $f:Y\to X$ and a Cartier divisor $D$ whose pullback is
defined, $f^*\OO_X(D)\cong\OO_Y(f^*D)$. If $f$ is a finite surjective
morphism of smooth projective surfaces of degree $d$, then
$$
f_*f^*D=dD,\qquad (f^*D\cdot f^*E)_Y=d(D\cdot E)_X.
$$
The second equality follows from the first and the projection formula.
For a smooth curve $C\subset X$, $(D\cdot C)=\deg\OO_X(D)|_C$
[@Bea96, Chapter I].

If distinct curves have local equations $a,b$ at an isolated intersection
point $p$ on a smooth surface, their local intersection multiplicity is
$\operatorname{length}(\OO_{X,p}/(a,b))$. It equals one precisely when
$a,b$ form a regular system of parameters, which means the curves are
smooth and transverse at $p$ [@Bea96, Chapter I].

For a rank-$r$ vector bundle $E$ on a smooth projective surface,
Hirzebruch–Riemann–Roch gives
$$
\chi(E)=r\chi(\OO_X)+\frac12c_1(E)\cdot(c_1(E)-K_X)-c_2(E).
$$
On an Enriques surface $K_X$ is numerically trivial and
$\chi(\OO_X)=1$. For rank two this becomes
$\chi(E)=2+\tfrac12c_1(E)^2-c_2(E)$.
On a K3 surface $\chi(\OO_X)=2$ and $K_X=0$, so for any rank $r$
the formula is
$$
\chi(E)=2r+\frac12c_1(E)^2-c_2(E).
$$
For a line bundle $L$ this gives $\chi(L)=2+L^2/2$.

The exponential sequence identifies
$\operatorname{Pic}^0(X)=H^1(X,\OO_X)/\operatorname{im}H^1(X,\ZZ)$.
For a smooth projective surface this is a complex torus of dimension
$q(X)$; the image of integral cohomology is a full lattice
[@Bea96, Chapter I].

## Canonical and ramification divisors

::: {.proposition #prop:canonical-class-of-blowup title="Canonical class of a blowup"}

Let $X$ be a nonsingular variety, let $V\iscontainedin X$ be a nonsingular subvariety of codimension $r\geq 2$, let $f\colon Y = \Bl_V X\to X$ be the blowup of $X$ along $V$, and let $E = f^{-1}(V)$.
Then
$$
K_Y = f^* K_X + (r - 1)E
$$
[@Har77, II Ex. 8.5(b)].
If $X$ is a nonsingular projective (@def:module-subcategories) surface and $V$ is a point, then $K_Y = f^*K_X + E$ and $K_Y^2 = K_X^2 - 1$ [@Har77, V.3.3].
:::

::: {.proposition #prop:ramification-formula-curves title="Canonical divisors under a finite separable morphism of curves"}

Let $k$ be an algebraically closed (@def:closed-monoidal) field, and let $f\colon Y\to X$ be a finite separable morphism of complete (@def:complete) nonsingular curves over $k$.
The **ramification divisor** of $f$ is
$$
R \definedas \Sum_{p\in Y} \mathrm{len}\qty{\Omega_{Y/X, p}}\, p
.
$$
Then $K_Y \sim f^* K_X + R$ [@Har77, IV.2.3 and the definition before it].
:::
