# Numerical polarizations and Noether–Lefschetz loci

## Numerical polarizations

::: {.definition #def:numerical-polarization title="Numerical polarization"}

A **numerical polarization** $[h]$ on an algebraic surface $Z$ --- for instance an Enriques surface --- is the numerical class of $h \definedas c_1(\mcl)$ for an ample line bundle $\mcl\in\Pic(Z)$, often written $[\mcl]$.
The **degree** of $[h]$ is its self-intersection $h^2$, computed in $\Num(Z)$.
:::

## The Noether–Lefschetz locus for Enriques surfaces

::: {.proposition #prop:enriques-cover-two-involutions title="The two involutions on the K3 cover of a degree-$2$ polarized Enriques surface"}

Let $Z$ be an Enriques surface with a numerical polarization $[\mcl_Z]$ of degree $2$, and let $\pi\colon X\to Z$ be its canonical double cover.
Then the K3 surface $X$ has two commuting involutions: the fixed-point-free **Enriques involution** $\ien$, which is the deck transformation of $\pi$, and the **del Pezzo involution** $\idp$.
The surface $X$ and both involutions are determined by the pair $(Z,[\mcl_Z])$ [@AEGS25, §2.1, Rem. 2.2].
:::

::: {.definition #def:nl-locus-enriques title="Noether–Lefschetz locus \\mathrm{NL}_{S_{\\mathrm{En}}}"}

The moduli space $\fentwo$ of degree-$2$ numerically polarized Enriques surfaces embeds into the K3 moduli space $\fttz$ via a canonical map $j$.
Its image is the **Noether–Lefschetz locus** $\mathrm{NL}_{S_{\mathrm{En}}}$ defined by the primitive embedding of the **invariant** (algebraic) lattice of $\ien$,
$$
\sen = E_{10}(2) = U(2)\oplus E_8(2)
,
$$
the rank-$10$, $2$-elementary, signature-$(1,9)$ lattice of type $(10,10,0)$ (see the Enriques-lattice definition (@def:enriques-lattice) and the Special Lattices section).
The **Noether–Lefschetz closure** is the Zariski closure
$$
B \definedas \overline{j(\fentwo)}\iscontainedin \ksbacpt{\fttz}
.
$$
:::

## Two polarization classes on a Coble surface

::: {.notation #not:coble-ten-point-blowup title="The ten-point blowup and its K3 double cover"}

In this section, $S = \Bl_{p_1,\dots,p_{10}}\PP^2$ is the ten-point blowup, $\Pic(S) = \generators{H, E_1,\dots,E_{10}}\cong\latI_{1,10}$ is its Picard lattice with $H^2 = 1$, $E_i^2 = -1$ and $H\cdot E_i = E_i\cdot E_j = 0$ for $i\neq j$, and $f\colon X\to S$ is the K3 double cover.
:::

::: {.proposition #prop:canonical-perp-is-e10 title="The canonical complement is the Enriques lattice"}

In $\Pic(S)\cong\latI_{1,10}$ one has $K_S = -3H + \Sum_{i=1}^{10} E_i$, and a divisor $D = aH - \Sum_i b_i E_i$ lies in $K_S^{\perp}$ if and only if
$$
\Sum_{i=1}^{10} b_i = 3a
.
$$
The sublattice $K_S^{\perp}$ is even and unimodular of signature $(1, 9)$, hence
$$
K_S^{\perp} \cong E_{10} = U\oplus E_8
,
$$
the Enriques lattice of the Enriques-lattice definition (@def:enriques-lattice).
The anti-bicanonical curve $C \in \abs{-2K_S}$ has class
$$
C = 6H - 2\Sum_{i=1}^{10} E_i = -2K_S
.
$$
:::

::: {.proof}

The expression for $K_S$ is the blowup formula, and $D\cdot K_S = -3a + \Sum_i b_i$, which vanishes if and only if $\Sum_i b_i = 3a$.
Since $K_S^2 = 9 - 10 = -1$, the rank-one sublattice $\generators{K_S}\cong\generators{-1}$ is unimodular, so by the unimodular-splitting proposition (@prop:unimodular-splits) it splits $\Pic(S)$ and its complement $K_S^{\perp}$ is unimodular of signature $(1, 9)$.
That complement is even: for $D = aH - \Sum_i b_iE_i$ with $\Sum_i b_i = 3a$,
$$
D^2 = a^2 - \Sum_i b_i^2 \equiv a^2 - \Sum_i b_i = a^2 - 3a \equiv a(a-1) \equiv 0
\pmod 2
,
$$
using $b^2\equiv b\bmod 2$.
An even unimodular lattice of signature $(1,9)$ is isometric to $E_{10}$ by the indefinite unimodular classification (@thm:indefinite-unimodular-classification).
Finally $C = -2K_S = 6H - 2\Sum_i E_i$ by the description of $K_S$.
:::

::: {.definition #def:coble-polarization-classes title="The hyperplane class and the degree-2 numerical polarization"}

Let $f\colon X\to S$ be the K3 double cover.

1. The **hyperplane class** is $H\in\Pic(S)$, the pullback of $c_1(\OO_{\PP^2}(1))$, with $H^2 = 1$; its K3 pullback $e_0\definedas f^{*}H\in S_\Co$ has $e_0^2 = 2$ by the K3 double-cover proposition (@prop:double-cover-is-k3).

2. The **degree-$2$ numerical polarization** is a class $h_\Co\in K_S^{\perp}\iscontainedin\Pic(S)$ of Enriques type: in the non-degenerate case $h_\Co = F_1 + F_2$ with $F_1,F_2\in K_S^{\perp}$, $F_i^2 = 0$ and $F_1\cdot F_2 = 1$, so that $h_\Co^2 = 2$; its K3 pullback $\tilde h_\Co\definedas f^{*}h_\Co$ lies in $f^{*}(K_S^{\perp})\iscontainedin S_\Co$ and has $\tilde h_\Co^2 = 4$. Thus $\tilde h_\Co = f^*F_1 + f^*F_2$ is the sum of the standard basis of $\generators{f^*F_1, f^*F_2}\cong U(2)$, as for the vector $h = e + f$ of [@AEGS25, Def. 2.5].

3. Let $\mathcal C_X\iscontainedin\NS(X)\tensor\RR$ be the component of the positive cone that contains the ample cone $\Amp(X)$ (@lem:k3-positive-cone-component), and let $\Delta_X$ be the set of classes of square $-2$ that are effective on $X$. The **chamber** $\mathfrak c$ of $X$ is the component of $\mathcal C_X\setminus\bigcup_{\delta\in\Delta_X}\delta^{\perp}$ that contains $\Amp(X)$; it exists because $\Amp(X)$ is convex and every ample class is positive on every $\delta\in\Delta_X$.
:::

::: {.example #ex:coble-polarization-small-degree title="$h_\Co$ against $(-2)$-classes of $H$-degree at most $3$"}
Let $h_\Co = 6H-2\Sum_{i\le8}E_i-E_9-E_{10}$, as in @prop:coble-cover-marking.
On unnodal members $\abs{2h_\Co}$ is base-point-free [@CD12, Lemmas 3.7--3.10].

The class $h_\Co$ meets the exceptional curves as $h_\Co\cdot E_i = 2$ for $i\le8$ and $h_\Co\cdot E_i = 1$ for $i = 9,10$, and it meets the anti-bicanonical curve $C = 6H-2\Sum_iE_i$ as $h_\Co\cdot C = 36-32-4 = 0$.

Let $\delta = aH-\Sum_ib_iE_i\in\Pic(S)$ with $\delta^2 = -2$ and $0\le\delta\cdot H = a\le 3$, so that $\Sum_ib_i^2 = a^2+2$.
For $a = 0,1,2,3$ there are $180$, $960$, $16\,320$ and $175\,680$ such classes, $193\,140$ in all.
By Riemann--Roch, $\chi(\delta) = 1+\tfrac12\delta\cdot(\delta-K_S) = -\tfrac12\delta\cdot K_S$, and $h^0(K_S-\delta) = 0$ because $H$ is nef and $H\cdot(K_S-\delta) = -3-a<0$.
So $\delta$ is effective when $\delta\cdot K_S = \Sum_ib_i-3a\le-2$.
Among the $193\,140$ classes, those with $h_\Co\cdot\delta = 6a-2\Sum_{i\le8}b_i-b_9-b_{10}<0$ all have $\delta\cdot K_S\ge0$, and there are $61$ of them.

So $h_\Co$ is nonnegative on each $E_i$, on $C$, and on every class $\delta$ with $\delta^2=-2$, $0\le\delta\cdot H\le3$ and $\delta\cdot K_S\le-2$.
:::

::: {.lemma #lem:hyperplane-class-not-coble-polarization title="$H$ and $h_\Co$ are different classes"}
$H\cdot K_S = -3$ and $h_\Co\cdot K_S = 0$. So $H\notin K_S^{\perp}$ and $H\neq h_\Co$.
:::

::: {.proof}
By @prop:canonical-perp-is-e10, $K_S = -3H+\Sum_iE_i$, so $H\cdot K_S = -3$.
By @def:coble-polarization-classes, $h_\Co\in K_S^{\perp}$.
:::

