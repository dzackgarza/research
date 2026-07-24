# Geometric preliminaries

::: {.remark}

Following [@Dol17 §5.1], Coble surfaces can be obtained by degenerating
$(X, \tau)$ a K3 with a fixed-point-free involution to a K3 surface
$(X_0, \tau_0)$ where the fixed locus of $\tau_0$ is a smooth rational curve.
The resulting quotient $X_0/\tau_0$ is a Coble surface.

A certain linear system $\abs{2f_i + 2f_j}$ defines a degree 2 map onto a
quartic del Pezzo surface $\phi_{ij}: S\to D$ with 4 $A_1$ singularities, as in
the case of Enriques surfaces, but this map is never finite in the Coble case.
The deck transformation of $\phi_{ij}$ is a biregular automorphism of $S$.
The $f_i$ come from an _isotropic sequence_ and are obtained by modifying the
basis $e_0,\dots, e_{10}$ of $K_S^{\perp \Num(S)} \cong E_{10}$ where
$e_0$ is the preimage of a hyperplane class and $e_1,\dots, e_{10}$ are the
classes of exceptional curves in the blowup of a plane sextic at 10 $A_1$
singularities.
:::

::: {.remark}

We recall the objects whose stable limits are taken.
A Coble surface is a smooth rational projective surface $S$ with
$\abs{-K_S} = \varnothing$ but $\abs{-2K_S} \neq \varnothing$ [@DM20; @DK25].
It is *terminal of K3 type* when $\abs{-2K_S}$ contains a reduced divisor
$C = C_1 + \cdots + C_n$ of disjoint smooth rational curves with $C_i^2 = -4$; the
$C_i$ are the *boundary components*, and one has
$$
n = -K_S^2, \qquad n \le 10
$$
[@DM20; @DK25].
In the case $n = 1$ studied here, the anti-bicanonical divisor is a single smooth
rational curve $C$ with $C^2 = -4$; this is the curve that reappears as the
contracted curve on the stable model.
:::

::: {.remark}

Such a terminal Coble surface is *basic rational*: it admits a birational morphism
to $\PP^2$ obtained by blowing up $N = 9 + n$ points [@DK25].
For $n = 1$ one recovers the classical Coble surface by blowing up the ten
$A_1$-singularities of an irreducible rational plane sextic, whose proper transform
then lies in $\abs{-2K_S}$ [@Cob19; @Cob29; @CDL25].
Coble surfaces are the anti-bicanonical analogue, among Cremona-special point
configurations, of the unnodal Halphen surfaces [@CD12], and every terminal Coble
surface of K3 type is tied to both a K3 double cover and an index-$2$ Halphen
surface [@DK25; @CD12].
:::

::: {.remark}

The polarization enters through the degree-$2$ numerically polarized Enriques
picture into which the Coble locus embeds.
A degree-$2$ numerically polarized Enriques surface is a pair $(Z, [\mathcal L_Z])$
with $[\mathcal L_Z] \in \Num(Z)$ an ample class of degree $2$; the system
$\abs{\mathcal L_Z^{\otimes 2}}$ is basepoint-free and realizes $Z$ as a double
cover $\rho\colon Z \to W$ of a quartic del Pezzo surface $W$ with singularities of
type $4A_1$ or $A_3 + 2A_1$, branched along a divisor $B \subset W$ [@CDL25].
This is the finite analogue of the map $\phi_{ij}$ above, which in the Coble case
fails to be finite.
The ramification divisor $R_Z = \rho^{-1}(B)$ is ample, $\QQ$-Cartier, and lies in
$\abs{\mathcal L_Z^{\otimes 2}}$, so $(Z, \varepsilon R_Z)$ is log canonical for
small $\varepsilon > 0$ [@CDL25].
It is the Coble descent of this ramification divisor that supplies the stable-pair
boundary of the KSBA stable limits.
:::
