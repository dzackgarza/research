# Geometric preliminaries {#sec-geometric-preliminaries}

::: {.definition #def:coble-surface title="Coble surface"}

A **Coble surface** is a smooth projective rational surface $S$ with $\abs{-K_S} = \varnothing$ and $\abs{-2K_S} \neq \varnothing$.
It is **terminal of K3 type** when $\abs{-2K_S}$ contains a smooth divisor $C$.
Then $C$ is the only member of $\abs{-2K_S}$, and it is a disjoint union $C = C_1 + \cdots + C_n$ of smooth rational curves with $C_i^2 = -4$.
The curves $C_i$ are the **boundary components** of $S$ [@DM20, Sec. 5.1; @DK25, Sec. 9.1].
:::

::: {.proposition #prop:terminal-coble-basic-rational title="Numerical invariants and plane models of terminal Coble surfaces"}

Let $S$ be a terminal Coble surface of K3 type with $n$ boundary components.
Then
$$
K_S^2 = -n, \qquad e(S) = 12 + n, \qquad \rho(S) = b_2(S) = 10 + n, \qquad n \le 10
$$
[@DK25, Sec. 9.1 and Cor. 9.1.5].
The surface $S$ admits a birational morphism $\pi\colon S\to\PP^2$.
The image $\pi(C)$ is a plane sextic with only double points, possibly infinitely near, and each irreducible component of $\pi(C)$ is rational [@DK25, Prop. 9.1.3].
The morphism $\pi$ is the blowup of $N = 9 + n$ double points of $\pi(C)$, some possibly infinitely near [@Dol17, Sec. 5.1].
:::

::: {.proposition #prop:coble-sextic-model title="Coble surfaces with one boundary component"}

Let $S$ be a terminal Coble surface of K3 type with $n = 1$.
Then $\pi(C)$ is an irreducible rational plane sextic $B$, and $S$ is the blowup of $\PP^2$ at the $10$ double points of $B$ [@Dol17, Sec. 5.1].
The double points of $B$ are ordinary nodes or cusps, possibly infinitely near [@DK25, Ex. 9.1.7].
:::

::: {.proposition #prop:coble-enriques-degeneration title="Coble surfaces as degenerations of Enriques quotients"}

Let $S$ be a terminal Coble surface of K3 type with anti-bicanonical divisor $C$.
The double cover $X_0\to S$ branched along $C$ is a K3 surface, with covering involution $\tau_0$.
The pair $(X_0, \tau_0)$ is a degeneration of a pair $(X, \tau)$ of a K3 surface $X$ and a fixed-point-free involution $\tau$ [@Dol17, Sec. 5.1].
:::

::: {.proposition #prop:coble-bielliptic-map title="The bielliptic maps of a Coble surface with one boundary component"}

Let $S$ be a terminal Coble surface of K3 type with $n = 1$, and assume that the $10$ double points $p_1, \dots, p_{10}$ of $B = \pi(C)$ are nodes, none infinitely near.
Let $e_0$ be the class of the preimage of a line and let $e_1, \dots, e_{10}$ be the classes of the exceptional curves of $\pi$.
Then $K_S^{\perp}\iscontainedin\Num(S)$ is isometric to $E_{10}$.
For $i = 1, \dots, 10$, let
$$
f_i = 3e_0 - (e_1 + \cdots + e_{10}) + e_i
,
$$
the class of the proper transform of a plane cubic through the nine double points $p_j$, $j \neq i$.
For $i \neq j$, the linear system $\abs{2f_i + 2f_j}$ defines a degree-$2$ map
$$
\phi_{ij}\colon S \to D
$$
onto a quartic del Pezzo surface $D$ with four ordinary double points.
The map $\phi_{ij}$ is not finite: it contracts $C$ to one of the four double points of $D$.
The deck transformation of $\phi_{ij}$ is a biregular automorphism of $S$ [@Dol17, Sec. 5.1].
:::

::: {.proposition #prop:polarized-enriques-double-cover title="The double cover defined by a degree-$2$ numerical polarization"}

Let $Z$ be an Enriques surface with $ADE$ singularities, and let $[\mcl_Z]\in\Pic(Z)/\ZZ_2$ be an ample numerical polarization of degree $2$.
Let $\mathcal{M} = \mcl_Z^{\tensor_{\OO_Z} 2}$, a $2$-divisible polarization of degree $8$.
Then $\abs{\mathcal{M}}$ is basepoint-free and defines a double cover $\rho\colon Z\to W$ onto a quartic del Pezzo surface $W$ with singularities of type $4A_1$ or $A_3 + 2A_1$.
The ramification divisor $R_Z\in\abs{\mathcal{M}}$ of $\rho$ is ample, and the pair $(Z, \eps R_Z)$ is log canonical for $0 < \eps \ll 1$ [@AEGS25, Sec. 1].
:::

## The components of a stable degeneration

::: {.definition #def:ade-surfaces title="ADE surfaces"}

The **ADE surfaces** are the irreducible components of the KSBA stable degenerations of K3 surfaces with a nonsymplectic involution.
A Type III component is labelled by a Dynkin diagram $A_n$, $D_n$ or $E_n$, and a Type II component by an affine diagram $\wA_n$, $\wD_n$ or $\wE_n$, matching the elliptic and parabolic subdiagrams of the Coxeter diagram (@def:elliptic-subdiagram). Each ADE surface $(X, D + \eps R)$ comes with a double cover $\pi\colon X\to Y$ onto a del Pezzo ADE surface $\bigl(Y,\ C + \tfrac{1+\eps}{2}B\bigr)$ of index $2$ [@AEGS25 §6].
:::

::: {.definition #def:bcde-surfaces title="BCDE surfaces and the folding labels"}

The **BCDE surfaces** are the quotients of ADE surfaces by involutions, and they correspond to the foldings of the ADE Dynkin diagrams.
Type B components are the quotients by an Enriques involution $\ien$, acting in suitable coordinates as $(x, y, z)\mapsto (\inverseof{x}, -y, -z)$; type C components are the quotients by the symplectic involution $\inik$.
The label
$$
\alpha : 2 = {}_2\beta \subset \gamma
$$
records three types at once: $\alpha$ is the ADE type of the double cover $X\to Y$, $\gamma$ the ADE type of the symplectic quotient $Z'\to W$, and ${}_2\beta$ the ABCDE type of the index-two nonsymplectic quotient $Z\to W$ [@AEGS25 §6].
:::
