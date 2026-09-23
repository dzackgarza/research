# Numerical polarizations and Noether–Lefschetz loci

## Numerical polarizations

::: {.Definition #def:numerical-polarization}
### Numerical polarization

A **numerical polarization** $[h]$ on an algebraic surface $Z$ --- for instance
an Enriques surface --- is the numerical class of $h \da c_1(\cL)$ for an ample
line bundle $\cL\in\Pic(Z)$, often written $[\cL]$.
:::

::: {.Remark}
### Numerical classes on an Enriques surface

For an Enriques surface $Z$ the first Chern class induces an isomorphism
$$
c_1\colon \Pic(Z)\xrightarrow{\ \sim\ } H^2(Z; \ZZ)
,
$$
so that the free part $H^2(Z; \ZZ)_f$ is identified with the group of numerical
divisor classes $\Num(Z)$.
Under the intersection pairing this free part is the even unimodular lattice of
signature $(1, 9)$, i.e. the Enriques lattice $E_{10}$ of
[the Enriques-lattice definition](#def:enriques-lattice) [@CDL25]; the numerical polarization $[h]$ is thus
an ample class in $\Num(Z)\iso E_{10}$.
:::

::: {.Remark}
### Degree of a numerical polarization

The **degree** of a numerical polarization $[h]$ is its self-intersection $h^2$
computed in $\Num(Z)$.
We are primarily interested in the **degree-$2$** case $h^2 = 2$; the
corresponding moduli space of degree-$2$ numerically polarized Enriques surfaces
is the space $\fentwo$ appearing below.
:::

## The Noether–Lefschetz locus for Enriques surfaces

::: {.Remark}
### The canonical cover and its involutions

The canonical double cover $\pi\colon X\to Z$ of a degree-$2$ polarized Enriques
surface yields a K3 surface $X$ carrying two commuting involutions: the
fixed-point-free **Enriques involution** $\ien$ (the deck transformation
of the canonical cover) and the **del Pezzo involution** $\idp$
[@AEGS25].

::: {.Remark}
The numerical polarization and the $\Num$ marking are those of [@CDL25]; the canonical
cover with its two involutions, the map $j\colon \fentwo\to \fttz$, the locus
$\mathrm{NL}_{S_{\mathrm{En}}}$ and the KSBA-limit closure $B$ are those of [@AEGS25].
:::
:::

::: {.Definition #def:nl-locus-enriques}
### Noether–Lefschetz locus $\mathrm{NL}_{S_{\mathrm{En}}}$

The moduli space $\fentwo$ of degree-$2$ numerically polarized Enriques
surfaces embeds into the K3 moduli space $\fttz$ via a canonical map $j$.
Its image is the **Noether–Lefschetz locus** $\mathrm{NL}_{S_{\mathrm{En}}}$
defined by the primitive embedding of the **invariant** (algebraic) lattice of
$\ien$,
$$
\sen = E_{10}(2) = U(2)\oplus E_8(2)
,
$$
the rank-$10$, $2$-elementary, signature-$(1,9)$ lattice of type $(10,10,0)$
(see [the Enriques-lattice definition](#def:enriques-lattice) and the Special Lattices section).
The appearance of these extra invariant classes in $\NS$ is what cuts out the
locus.
:::

::: {.Remark}
### KSBA limits and non-normality

The Zariski closure
$$
B \da \overline{j(\fentwo)}\containedin \ksbacpt{\fttz}
$$
parameterizes all KSBA limits of these double covers.
The space fails to be normal along the boundary, due to branching and boundary
divisor intersections.
:::

## Two polarization classes on a Coble surface

::: {.Remark}

On the K3 cover of a Coble surface with $n = 1$ there are two distinct divisor classes of square $2$, and
the K3 cover, and a third class of square $4$; keeping them apart is what makes
the comparison with $F_{\En, 2}$ well posed.
Throughout, $S = \Bl_{p_1,\dots,p_{10}}\PP^2$ is the ten-point blowup,
$\Pic(S) = \gens{H, E_1,\dots,E_{10}}\cong\latI_{1,10}$ is its Picard lattice with
$H^2 = 1$, $E_i^2 = -1$ and $H\cdot E_i = E_i\cdot E_j = 0$ for $i\neq j$, and
$f\colon X\to S$ is the K3 double cover.
:::

::: {.Proposition #prop:canonical-perp-is-e10}
### The canonical complement is the Enriques lattice

In $\Pic(S)\cong\latI_{1,10}$ one has $K_S = -3H + \Sum_{i=1}^{10} E_i$, and a
divisor $D = aH - \Sum_i b_i E_i$ lies in $K_S^{\perp}$ if and only if
$$
\Sum_{i=1}^{10} b_i = 3a
.
$$
The sublattice $K_S^{\perp}$ is even and unimodular of signature $(1, 9)$, hence
$$
K_S^{\perp} \cong E_{10} = U\oplus E_8
,
$$
the Enriques lattice of [the Enriques-lattice definition](#def:enriques-lattice).
The Coble boundary curve has class
$$
C = 6H - 2\Sum_{i=1}^{10} E_i = -2K_S
.
$$
:::

::: {.proof}

The expression for $K_S$ is the blowup formula, and
$D\cdot K_S = -3a - \Sum_i(-b_i)(-1)\cdot(-1)$ evaluates to $3a - \Sum_i b_i$ up to
sign, giving the stated condition.
Since $K_S^2 = 9 - 10 = -1$, the rank-one sublattice $\gens{K_S}\cong\gens{-1}$ is
unimodular, so by [the unimodular-splitting proposition](#prop:unimodular-splits) it splits $\Pic(S)$ and its
complement $K_S^{\perp}$ is unimodular of signature $(1, 9)$.
That complement is even: for $D = aH - \Sum_i b_iE_i$ with $\Sum_i b_i = 3a$,
$$
D^2 = a^2 - \Sum_i b_i^2 \equiv a^2 - \Sum_i b_i = a^2 - 3a \equiv a(a-1) \equiv 0
\pmod 2
,
$$
using $b^2\equiv b\bmod 2$.
An even unimodular lattice of signature $(1,9)$ is isometric to $E_{10}$ by
[the indefinite unimodular classification](#thm:indefinite-unimodular-classification).
Finally $C = -2K_S = 6H - 2\Sum_i E_i$ by the description of $K_S$.
:::

::: {.Definition #def:coble-polarization-classes}
### The plane class and the degree-$2$ Coble polarization

The two classes to be distinguished are:

1.  the **plane class** $H\in\Pic(S)$, the pullback of a line, with $H^2 = 1$; its
    K3 pullback $e_0\da f^{*}H\in S_\Co$ has $e_0^2 = 2$ by
    [the K3 double-cover proposition](#prop:double-cover-is-k3);

2.  the **degree-$2$ Coble polarization**
    $h_\Co\in K_S^{\perp}\containedin\Pic(S)$, of Enriques type: in the
    non-degenerate case $h_\Co = F_1 + F_2$ with $F_i^2 = 0$ and
    $F_1\cdot F_2 = 1$, so that $h_\Co^2 = 2$; its K3 pullback
    $\tilde h_\Co\da f^{*}h_\Co$ lies in $f^{*}(K_S^{\perp})\containedin S_\Co$ and
    has $\tilde h_\Co^2 = 4$.
:::

::: {.Remark}
### Why the two must not be identified

Both $H$ and $h_\Co$ have square $2$ after pullback and square $2$ downstairs
respectively, so the numerical coincidence is easy to mistake for an identity.
They are different classes: $H\notin K_S^{\perp}$, since
$H\cdot K_S = -3\neq 0$, whereas $h_\Co$ lies in $K_S^{\perp}$ by definition, and
their pullbacks have different squares, $e_0^2 = 2$ against
$\tilde h_\Co^2 = 4$.

The analogue of the Enriques degree-$2$ polarization is $h_\Co$:
polarization: for a degree-$2$ Enriques surface the numerical polarization has
$h^2 = 2$ in $\Num(Z)\cong E_{10}$ while the K3-side vector
$h = e + f\in U(2)$ has $h^2 = 4$ ([the discriminant description of $\Gamma_{\En,2}$](#prop:gamma-en-two-gluing)), exactly the
pattern of $h_\Co$ and $\tilde h_\Co$.
Any comparison of Coble and Enriques polarized moduli, and any pairing of a
polarization class against roots of a Coxeter diagram, must first record which of
these classes is meant and in which lattice it lives.
:::
