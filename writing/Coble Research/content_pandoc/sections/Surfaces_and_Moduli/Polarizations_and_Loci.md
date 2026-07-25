# Numerical polarizations and Noether–Lefschetz loci

## Numerical polarizations

::: {.definition title="Numerical polarization" ref="def:numerical-polarization"}

A **numerical polarization** $[h]$ on an algebraic surface $Z$ --- for instance
an Enriques surface --- is the numerical class of $h \da c_1(\cL)$ for an ample
line bundle $\cL\in\Pic(Z)$, often written $[\cL]$.
:::

::: {.remark title="Numerical classes on an Enriques surface"}

For an Enriques surface $Z$ the first Chern class induces an isomorphism
$$
c_1\colon \Pic(Z)\xrightarrow{\ \sim\ } H^2(Z; \ZZ)
,
$$
so that the free part $H^2(Z; \ZZ)_f$ is identified with the group of numerical
divisor classes $\Num(Z)$.
Under the intersection pairing this free part is the even unimodular lattice of
signature $(1, 9)$, i.e. the Enriques lattice $E_{10}$ of
\cref{def:enriques-lattice} [@CDL25]; the numerical polarization $[h]$ is thus
an ample class in $\Num(Z)\iso E_{10}$.
:::

::: {.remark title="Degree of a numerical polarization"}

The **degree** of a numerical polarization $[h]$ is its self-intersection $h^2$
computed in $\Num(Z)$.
We are primarily interested in the **degree-$2$** case $h^2 = 2$; the
corresponding moduli space of degree-$2$ numerically polarized Enriques surfaces
is the space $F_{\En, 2}$ appearing below.
:::

## The Noether–Lefschetz locus for Enriques surfaces

::: {.remark title="The canonical cover and its involutions"}

The canonical double cover $\pi\colon X\to Z$ of a degree-$2$ polarized Enriques
surface yields a K3 surface $X$ carrying two commuting involutions: the
fixed-point-free **Enriques involution** $\iota_{\En}$ (the deck transformation
of the canonical cover) and the **del Pezzo involution** $\iota_{\operatorname{dP}}$
[@AEGS25].
\todo{The two source notes (Numerical polarization; Noether--Lefschetz Locus for
Enriques Surfaces) carried no inline citations. The attributions here
($\cL,\Num$ marking $\to$ CDL25; the canonical cover, its two involutions, the
map $j\colon F_{\En,2}\to F_{(2,2,0)}$, the locus $\mathrm{NL}_{S_{\mathrm{En}}}$,
and the KSBA-limit closure $B$ $\to$ AEGS25) are supplied as the standard
sources for the concepts the notes name; the author should confirm the intended
primary references.}
:::

::: {.definition title="Noether–Lefschetz locus $\mathrm{NL}_{S_{\mathrm{En}}}$" ref="def:nl-locus-enriques"}

The moduli space $F_{\En, 2}$ of degree-$2$ numerically polarized Enriques
surfaces embeds into the K3 moduli space $F_{(2,2,0)}$ via a canonical map $j$.
Its image is the **Noether–Lefschetz locus** $\mathrm{NL}_{S_{\mathrm{En}}}$
defined by the primitive embedding of the **invariant** (algebraic) lattice of
$\iota_\En$,
$$
S_{\mathrm{En}} = E_{10}(2) = U(2)\oplus E_8(2)
,
$$
the rank-$10$, $2$-elementary, signature-$(1,9)$ lattice of type $(10,10,0)$
(see \cref{def:enriques-lattice} and the Special Lattices section).
The appearance of these extra invariant classes in $\NS$ is what cuts out the
locus.
:::

::: {.remark title="KSBA limits and non-normality"}

The Zariski closure
$$
B \da \overline{j(F_{\En, 2})}\subseteq \overline{F_{(2,2,0)}}
$$
parameterizes all KSBA limits of these double covers.
The space fails to be normal along the boundary, due to branching and boundary
divisor intersections.
:::
