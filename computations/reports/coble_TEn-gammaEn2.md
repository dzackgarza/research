# $\Gamma_{\En,2}$ from AEGS 2025, and what the sandwich has to count

Source: `tmp/sources/aegs-2025-compact-moduli-of-enriques-surfaces-of-degree-2.pdf`,
Definitions 2.5–2.7 (article pp. 586–587). Transcribed, not paraphrased:

> **Definition 2.5.** … for a lattice $\Lambda$ of signature $(2,n)$ the period domain $D(\Lambda)$ is a
> connected component of $\{[x]\in \P(\Lambda\otimes\C) \mid x\cdot x = 0,\ x\cdot\bar x > 0\}$. Since
> $T_{\En}\subset T_{dP}$, one has $D(T_{\En})\subset D(T_{dP})$. The polarizations … are defined by
> the vector $h = e+f\in U(2) = S_{dP}\subset S_{\En}$, where $\{e,f\}$ is the basis of $U(2)$ with
> $e^2 = f^2 = 0$, $e\cdot f = 2$.
>
> **Definition 2.6.** Define the arithmetic group $\Gamma_{\En,2}$ as the image in $\O(T_{\En})$ of
> $\{g\in \O(L) \mid g\circ I_{\En} = I_{\En}\circ g \text{ and } g(h) = h\}$. Additionally, define
> $\Gamma_{\En} = \O(T_{\En})$ and $\Gamma_{dP} = \O(T_{dP})$. We have
> $\Gamma_{\En,2} = \Gamma_{\En}\cap\Gamma_{dP}$. Since $\O(L)\to\O(T_{\En})$ and $\O(L)\to\O(T_{dP})$
> are surjective by [38, Cor. 1.5.2, Thm. 3.6.3], the homomorphisms from the centralizer groups
> $Z_{\O(L)}(I_{\En})\to\Gamma_{\En}$ and $Z_{\O(L)}(I_{dP})\to\Gamma_{dP}$ are surjective.
>
> **Definition 2.7.** $F_{\En,2} = D(T_{\En})/\Gamma_{\En,2}$, $F_{(10,10,0)} = D(T_{\En})/\Gamma_{\En}$,
> $F_{(2,2,0)} = D(T_{dP})/\Gamma_{dP}$.

## Translation into the terms of `coble_TEn-sandwich.py`

In the coordinates of that record, $T_{\En} = U\oplus U(2)\oplus E_8(2)$ with slots $0$–$1$ the $U$
summand, $2$–$3$ the $U(2)$ summand, $4$–$11$ the $E_8(2)$ basis. The polarization of Def. 2.6 is

$$h = e+f = \text{slot } 2 + \text{slot } 3 ,\qquad h^2 = 2\cdot 2 = 4,\qquad \div_{T_{\En}}(h) = 2,$$

so $h/2\in T_{\En}^\#$ and its class $[h/2]\in A_{T_{\En}}$ has $q([h/2]) = h^2/4 = 1$.

Commutativity with $I_{\En}$ is automatic on the image: $T_{\En}$ is the coinvariant lattice of
$I_{\En}$ (AEGS, Lemma 3.4 / the chapter's `thm:three-lattice-involutions`), so every isometry of
$T_{\En}$ is the restriction of one commuting with $I_{\En}$, and $\Gamma_{\En,2}$ is

$$\Gamma_{\En,2} = \Stab_{\O(T_{\En})}(h) \le \Gamma_{\En} = \O(T_{\En}).$$

Since $\rho_{T_{\En}}\colon \O(T_{\En})\to \O(q_{T_{\En}})$ is onto (Nikulin 3.6.3,
`@thm:two-elementary-surjectivity`), its image is

$$\rho(\Gamma_{\En,2}) = \Stab_{\O(q)}([h/2]),\qquad
\abs{\Stab_{\O(q)}([h/2])} = \frac{\abs{\O(q)}}{\abs{\O(q)\cdot[h/2]}} = \frac{46\,998\,591\,897\,600}{496}
= 94\,755\,225\,600,$$

the orbit having $496$ elements because $q([h/2]) = 1$ and $496$ classes of $A_{T_{\En}}$ have value
$1$ — the same pair of numbers the Coble record `coble_isotropic-stabilizer-orbits.py` computes for
$T_{\Co}$, whose discriminant form is isomorphic.

## What is left to compute, and how

The $\widetilde\O$-orbits inside one $\O(T_{\En})$-orbit are the classes themselves: one orbit for the
div-$1$ class and $527$ for the div-$2$ class (step (iii)). So the $\Gamma_{\En,2}$-orbits of
primitive isotropic vectors are the orbits of $\Stab_{\O(q)}([h/2])$ on the $528$ isotropic classes of
$A_{T_{\En}}$, and the published count is **5** (AEGS §3.3 p. 590; Sterk 1991 Prop. 4.2.3 p. 16 for the
nine $1$-cusps). The computation is `A.orbits(group=H)` with $H$ the stabilizer of $[h/2]$, restricted
to the isotropic classes, exactly as `coble_isotropic-stabilizer-orbits.py` does it for $T_{\Co}$.

Not run: the stabilizer $H$ and its orbit decomposition; the nine plane orbits.
