# Nonsymplectic K3 stable models {#sec-nonsymplectic-k3-models}

## Equivariant periods and cusp parity

Fix an involution $\rho\in O(\lkt)$ with hyperbolic invariant lattice
$S=\lkt^\rho$ and orthogonal complement $T=S^\perp$. A *$\rho$-marking*
of $(X,\iota)$ is an isometry $\phi\colon H^2(X,\ZZ)\to\lkt$ such that
$\phi\iota^*=\rho\phi$. The corresponding period space is
$$
\Omega_T=\{[\omega]\in\PP(T_\CC):
 (\omega,\omega)=0,\ (\omega,\bar\omega)>0\},
\qquad
\Gamma_\rho=\{\gamma\in O(\lkt):\gamma\rho=\rho\gamma\}.
$$
The smooth involution locus is obtained by removing the relevant
root hyperplanes from $\Omega_T$ and taking the quotient by the
restriction of $\Gamma_\rho$ [@AE22, §2]. The roots excluded here lie
in $T$, not in $S$: every vector in $S$ is already perpendicular to
the entire domain.

A primitive isotropic cusp vector $e\in T$ is *odd* when
$\operatorname{div}_T(e)=1$ and *even* when
$\operatorname{div}_T(e)=2$. In the even case the class
$e/2\in T^*/T$ can be characteristic or noncharacteristic; this
distinction gives the two even mirror moves of [@AE22, §5A]. The
hyperbolic quotient $\bar T=e^\perp/\ZZ e$ determines the reflection
chamber used to construct the degeneration.

## Pumpkin and smashed-pumpkin surfaces

Consider the Type III Kulikov models with nonsymplectic involution
constructed in [@AE22, §8], and suppose the ramification divisor has
a component $C_g$ of genus $g\ge2$. Write
$C_{g,i}=C_g|_{V_i}$ on each normalized component. The stable model
contracts by this nef divisor after the modifications making it nef.

::: {.definition #def:pumpkin-model title="Pumpkin type"}
A stable surface is of *pumpkin type* if its normalized components
$\bar V_i$ have two boundary sides
$\bar D_{i,\mathrm{left}}+\bar D_{i,\mathrm{right}}$, glued cyclically,
and every side joins the same two points, the north and south poles
[@AE22, Definition 9.8].
:::

::: {.definition #def:smashed-pumpkin-model title="Smashed-pumpkin type"}
A *smashed pumpkin* is the stable surface obtained from a pumpkin by
contracting a short side, thereby identifying the two poles
[@AE22, Definition 9.8].
:::

Here short and long sides are measured on the K3 component by
$C_{g,i}\cdot D=1$ and $2$, respectively. This differs from the
polarization $-2(K_Y+C)$ on the quotient ADE surface.

The contraction has two local forms. If
$$
V_i=\mathbb F_1,\qquad D_1\sim f,\qquad
D_2\sim2s+2f,\qquad C_{g,i}\sim f,
$$
where $s^2=-1$ and $f$ is a ruling fiber, the whole component contracts
by $V_i\to\PP^1$. The adjacent component's long side is then folded
two-to-one onto itself, giving a nonnormal double curve. When
$C_{g,i}^2\ge2$, only the short side contracts; the resulting component
is normal in codimension one, with the two poles identified
[@AE22, Definition 9.8].

For these constructed Kulikov models, [@AE22, Theorem 9.9] identifies
the normalizations of the stable components with the ADE surfaces
with involution of [@AT17, Table 2]. An odd cusp gives pumpkin type;
an even cusp gives smashed-pumpkin type. The assertion follows by
applying the contraction defined by $C_{g,i}$ to the components in
the construction: the odd case retains the cyclic sides, while the
even case has a zero-length side and the contraction described above.
The ADE shapes with a contracted side are exactly the indicated
double-prime or $+$ shapes in that table.

In the maximally degenerate odd model, the equatorial cycle has
$2\bar k$ edges. Its components are $2\bar k$ copies of
$(\PP^2,\text{line}+\text{conic})$. Singly circled odd vertices record
the lines and doubly circled even vertices the conics. The maximally
degenerate smashed model has $2\bar k-2$ components: $2\bar k-4$
ordinary line–conic pairs and two whose conic side is folded onto
itself. For nongeneric monodromy $\lambda$, an equatorial vertex in
$V_2(\lambda)$ smooths the corresponding side; an off-equator vertex
connected to such an equatorial vertex changes the component type
and increases the charge of its minimal resolution
[@AE22, §9B, following Theorem 9.9].

The Enriques quotient components and their equations are described
in @sec-abcde-surfaces.

## ADE quotients and priming

For an ADE quotient pair $(Y,C)$, put $L=-2(K_Y+C)$. A branch
divisor $B\in|L|$ gives the stable pair
$$
\left(Y,C+\frac{1+\epsilon}{2}B\right),\qquad 0<\epsilon\ll1,
$$
provided it is log canonical. Its double-cover construction is the
one in @sec-abcde-surfaces. The boundary $C$ is not an extra arbitrary
choice of branch divisor; the cover and its boundary obey that
construction.

The pure shapes are polarized toric surfaces with lattice polytopes
in $M_\RR$. For example,
$$
\begin{array}{c|c|c|c}
\text{shape}&Y&C&L\\\hline
D_4&\PP^1\times\PP^1&\text{two incident ruling curves}&\OO(2,2)\\
A_1&\PP^2&\text{two coordinate lines}&\OO(2)
\end{array}
$$
[@AT17, §3A, Table 1]. On these quotient surfaces a side is long
when its $L$-degree is even and short when it is odd. A superscript
$-$ marks the position of a short side. Euclidean length in a chosen
drawing does not determine the label: $A_3$ has two long sides,
whereas $A_2^-$ has a long left side and a short right side.

Priming is the weighted blowup and contraction of @def:priming.
Locally its ideal is $(y,x^2)$: it is resolved by two ordinary
blowups followed by contraction of a $(-2)$-curve to an $A_1$
singularity. For a pair, its centers lie at the transverse
intersections $B\cap C$. A prime records priming on a long side;
on a short side the sign changes from $-$ to $+$. The nefness and
bigness conditions in @def:priming are necessary: the weighted
blowup alone need not produce an admissible shape
[@AT17, §3C, Definitions 3.13 and 3.15].
