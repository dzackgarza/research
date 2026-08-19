# Coble And K3 Period-Domain Facts

This note records facts used when comparing Coble constructions with lattice-polarized
K3 period domains.

## Type IV Domain Dimension

Let $L$ be a rank-$r$ lattice with signature $(2,r-2)$. Its complexification $L_\mathbb{C}$
has dimension $r$, so $\mathbb{P}(L_\mathbb{C})$ has dimension $r-1$. The equation
$(z,z)=0$ cuts out a quadric hypersurface of dimension $r-2$, and the positivity
condition $(z,\bar z)>0$ selects an open component. Therefore the Type IV domain
$D_L$ has complex dimension $r-2$.

If the relevant period lattice has rank $11$, then $\dim D_L=9$.

## Standard K3 Moduli Input

The standard K3 object is the moduli space of primitively $M$-polarized K3 surfaces.
Here $M$ is a lattice embedded primitively into $\mathrm{Pic}(X)$, with the usual
positivity/ample-cone condition. A general point has $\mathrm{Pic}(X)=M$; special points
may have larger Picard lattice.

For an $M$-polarized K3 surface, the period domain is attached to
$T=M^\perp \subset \Lambda_{\mathrm{K3}}$. Its dimension is

$$
\dim D_T = \operatorname{rank}(T)-2 = 20-\operatorname{rank}(M).
$$

This is the K3-theory input to use, not a first-principles reconstruction of Torelli.

## Standard Coble-K3 Construction

Let $C \subset \mathbb{P}^2$ be a rational plane sextic with ordinary nodes
$p_1,\ldots,p_{10}$, and let

$$
\sigma:S=\operatorname{Bl}_{p_1,\ldots,p_{10}}\mathbb{P}^2\to\mathbb{P}^2
$$

be the blowup. Write $H=\sigma^*\mathcal{O}_{\mathbb{P}^2}(1)$ and write
$E_i$ for the exceptional divisors. Since
$\mathrm{Pic}(\mathbb{P}^2)=\mathbb{Z}[\mathcal{O}_{\mathbb{P}^2}(1)]$, the blowup
formula gives

$$
\mathrm{Pic}(S)=\mathbb{Z}H\oplus\bigoplus_{i=1}^{10}\mathbb{Z}E_i.
$$

The intersections are the standard blowup intersections:

$$
H^2=1,\qquad H\cdot E_i=0,\qquad E_i\cdot E_j=-\delta_{ij}.
$$

Thus $\mathrm{Pic}(S)$ is the explicit lattice

$$
\langle 1\rangle\oplus\langle -1\rangle^{10}
$$

in the basis $(H,E_1,\ldots,E_{10})$. The canonical class is

$$
K_S=\sigma^*K_{\mathbb{P}^2}+\sum_i E_i=-3H+\sum_i E_i.
$$

The strict transform $B$ of $C$ has class

$$
B=6H-2\sum_iE_i=-2K_S.
$$

Equivalently, $B\in |2L|$ for $L=-K_S=3H-\sum_iE_i$. A section of $L^{\otimes 2}$
with divisor $B$ defines the double cover

$$
\pi:X=\operatorname{Spec}_S(\mathcal{O}_S\oplus L^{-1})\to S,
$$

where multiplication on $L^{-1}$ is given by that section. The cover is branched along
$B$; its ramification divisor $R\subset X$ satisfies $\pi^*B=2R$.

The canonical bundle formula for a double cover gives

$$
K_X=\pi^*(K_S+L)=\pi^*(K_S-K_S)=0.
$$

Also

$$
\pi_*\mathcal{O}_X=\mathcal{O}_S\oplus L^{-1}
  =\mathcal{O}_S\oplus K_S.
$$

Since $S$ is rational, $h^1(\mathcal{O}_S)=0$. By Serre duality,
$h^1(K_S)=h^1(\mathcal{O}_S)=0$, so $h^1(\mathcal{O}_X)=0$. Similarly
$\chi(\mathcal{O}_S)=\chi(K_S)=1$, hence $\chi(\mathcal{O}_X)=2$, and with
$K_X=0$ this gives $p_g(X)=1$. Therefore the smooth double cover is a K3 surface.

Finally, pullback doubles intersections:

$$
\pi^*D\cdot\pi^*D'=2(D\cdot D')
$$

for divisors $D,D'$ on $S$. Hence the pullback of the blowup Picard lattice has basis
$(\pi^*H,\pi^*E_1,\ldots,\pi^*E_{10})$ and Gram matrix

$$
\operatorname{diag}(2,-2,\ldots,-2),
$$

so the computed pullback lattice is

$$
I_{1,10}(2)\cong \langle 2\rangle\oplus\langle -2\rangle^{10}.
$$
