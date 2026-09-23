# Geometric preliminaries

::: {.Remark}

Following [@Dol17 §5.1], Coble surfaces can be obtained by degenerating $(X, \tau)$ a K3 with a fixed-point-free involution to a K3 surface $(X_0, \tau_0)$ where the fixed locus of $\tau_0$ is a smooth rational curve.
The resulting quotient $X_0/\tau_0$ is a Coble surface.

A certain linear system $\abs{2f_i + 2f_j}$ defines a degree 2 map onto a quartic del Pezzo surface $\phi_{ij}: S\to D$ with 4 $A_1$ singularities, as in the case of Enriques surfaces, but this map is never finite in the Coble case.
The deck transformation of $\phi_{ij}$ is a biregular automorphism of $S$.
The $f_i$ come from an *isotropic sequence* and are obtained by modifying the basis $e_0,\dots, e_{10}$ of $K_S^{\perp \Num(S)} \cong E_{10}$ where $e_0$ is the preimage of a hyperplane class and $e_1,\dots, e_{10}$ are the classes of exceptional curves in the blowup of a plane sextic at 10 $A_1$ singularities.
:::

::: {.Remark}

We recall the objects whose stable limits are taken.
A Coble surface is a smooth rational projective surface $S$ with $\abs{-K_S} = \varnothing$ but $\abs{-2K_S} \neq \varnothing$ [@DM20; @DK25]. It is *terminal of K3 type* when $\abs{-2K_S}$ contains a reduced divisor $C = C_1 + \cdots + C_n$ of disjoint smooth rational curves with $C_i^2 = -4$; the $C_i$ are the *boundary components*, and one has
$$
n = -K_S^2, \qquad n \le 10
$$
[@DM20; @DK25]. In the case $n = 1$ studied here, the anti-bicanonical divisor is a single smooth rational curve $C$ with $C^2 = -4$; this is the curve that reappears as the contracted curve on the stable model.
:::

::: {.Remark}

Such a terminal Coble surface is *basic rational*: it admits a birational morphism to $\PP^2$ obtained by blowing up $N = 9 + n$ points [@DK25]. For $n = 1$ one recovers the classical Coble surface by blowing up the ten $A_1$-singularities of an irreducible rational plane sextic, whose proper transform then lies in $\abs{-2K_S}$ [@Cob19; @Cob29; @CDL25]. Coble surfaces are the anti-bicanonical analogue, among Cremona-special point configurations, of the unnodal Halphen surfaces [@CD12], and every terminal Coble surface of K3 type is tied to both a K3 double cover and an index-$2$ Halphen surface [@DK25; @CD12].
:::

::: {.Remark}

The polarization enters through the degree-$2$ numerically polarized Enriques picture into which the Coble locus embeds.
A degree-$2$ numerically polarized Enriques surface is a pair $(Z, [\mathcal L_Z])$ with $[\mathcal L_Z] \in \Num(Z)$ an ample class of degree $2$; the system $\abs{\mathcal L_Z^{\tensor 2}}$ is basepoint-free and realizes $Z$ as a double cover $\rho\colon Z \to W$ of a quartic del Pezzo surface $W$ with singularities of type $4A_1$ or $A_3 + 2A_1$, branched along a divisor $B \containedin W$ [@CDL25]. This is the finite analogue of the map $\phi_{ij}$ above, which in the Coble case fails to be finite.
The ramification divisor $R_Z = \rho\inv(B)$ is ample, $\QQ$-Cartier, and lies in $\abs{\mathcal L_Z^{\tensor 2}}$, so $(Z, \varepsilon R_Z)$ is log canonical for small $\varepsilon > 0$ [@CDL25]. It is the Coble descent of this ramification divisor that supplies the stable-pair boundary of the KSBA stable limits.
:::

## The components of a stable degeneration

::: {.Definition #def:ade-surfaces}
### ADE surfaces

The **ADE surfaces** are the irreducible components of the KSBA stable
degenerations of K3 surfaces with a nonsymplectic involution.
A Type III component is labelled by a Dynkin diagram $A_n$, $D_n$ or $E_n$, and a
Type II component by an affine diagram $\widetilde{A}_n$, $\widetilde{D}_n$ or
$\widetilde{E}_n$, matching the elliptic and parabolic subdiagrams of the Coxeter
diagram ([the elliptic-subdiagram definition](#def:elliptic-subdiagram)).
Each ADE surface $(X, D + \varepsilon R)$ comes with a double cover
$\pi\colon X\to Y$ onto a del Pezzo ADE surface
$\bigl(Y,\ C + \tfrac{1+\varepsilon}{2}B\bigr)$ of index $2$
[@AEGS25 §6].
:::

::: {.Definition #def:bcde-surfaces}
### BCDE surfaces and the folding labels

The **BCDE surfaces** are the quotients of ADE surfaces by involutions, and they
correspond to the foldings of the ADE Dynkin diagrams.
Type B components are the quotients by an Enriques involution
$\ien$, acting in suitable coordinates as
$(x, y, z)\mapsto (x\inv, -y, -z)$; type C components are the quotients by the
symplectic involution $\inik$.
The label
$$
\alpha : 2 = {}_2\beta \subset \gamma
$$
records three types at once: $\alpha$ is the ADE type of the double cover
$X\to Y$, $\gamma$ the ADE type of the symplectic quotient $Z'\to W$, and
${}_2\beta$ the ABCDE type of the index-two nonsymplectic quotient $Z\to W$
[@AEGS25 §6].
:::

::: {.Remark}

The stable limits of Coble surfaces are quotients of nodal K3 surfaces by an
involution with fixed points, so their components are read off this list in the
same way as for Enriques degenerations, with the Coble case distinguished by the
folding involution attached to its $0$-cusp.
Which foldings occur, and hence which BCDE types appear in a Coble stable limit,
is part of the *dlt*-model question recorded among the open problems.
:::
