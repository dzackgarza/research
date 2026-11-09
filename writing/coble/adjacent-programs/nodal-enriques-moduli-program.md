---
unit: research-program
status: conjectural
tags:
  - nodal-enriques
  - non-2-elementary
  - moduli
---

# The nodal Enriques moduli program {#sec-nodal-enriques-moduli-program}

The lattices are defined in [Nodal Enriques lattices](#sec-nodal-enriques-lattices).

## Setting

::: {.definition title="Nodal and unnodal"}

An Enriques surface $Y$ is **nodal** if it contains a rational $(-2)$-curve, and **unnodal** otherwise.
A generic Enriques surface is unnodal, and $F_{\Nod}$ is an irreducible hypersurface in $\fen$.
:::

$$
S_{\Nod} = \generators{-4}\oplus U \oplus E_8(2),
\qquad
T_{\Nod} \definedas S_{\Nod}^\perp \cong \generators{4}\oplus U \oplus E_8(2),
$$
the generic Picard lattice of the K3 cover $X$ and its transcendental lattice.
$F_{\Nod}$ is realized as the divisor $\mch_{-4}/\Orth(\ten)$, a 9-dimensional irreducible quasiprojective variety.

::: {.remark title="Two forms of the embedding"}

[@CDL25, p. 561] gives the primitive embedding $\sen\injects S_{\Nod}$ as
$$
((e,f), x) \mapsto \big((2\tilde f + \tilde e + h,\ \tilde e),\ x\big),
$$
and [@CD89, Def. 5.6.3] gives it as
$$
((e,f), x) \mapsto \big((\tilde f,\ 2\tilde e + \tilde f + h),\ x\big),
$$
where $U(2) = \generators{e,f}$, $U = \generators{\tilde e,\tilde f}$ and $\generators{-4} = \generators{h}$.
Both are the identity on the $E_8(2)$ factor.
The second is the first composed with the isometry $e\leftrightarrow f$ of $U(2)$ on the source and the isometry $\tilde e\leftrightarrow\tilde f$ of $U$ on the target, so the two are the same embedding up to isometries of $\sen$ and of $S_{\Nod}$.
:::

## The program

::: {.conjecture title="Baily-Borel boundary by the same techniques"}

Orbits under $\Orth(T_{\Nod})$ of isotropic vectors and planes can be classified, yielding a boundary incidence diagram; and the lattice embedding above allows AEGS23 to be leveraged to construct the KSBA compactification, its dlt models, and the integral-affine structures classifying KSBA stable limits of nodal Enriques surfaces.
:::

::: {.remark title="Why this needs genuinely new machinery"}

$T_{\Nod}$ is **not 2-elementary**. The Sterk-Nikulin apparatus used here assumes 2-elementarity, so the classification of boundary components requires orbit techniques for non-2-elementary discriminant forms.
This is the single structural obstruction distinguishing the nodal case from every other family in this program, including the Coble families of [the Coble families research program](#sec-coble-families-research-program), which are all 2-elementary.
:::

## Literature anchors recorded with the program

- Cossec (1985) computes the automorphism group at a generic point of $F_{\Nod}$ by non-transcendental methods, showing it equals a normal subgroup of the Weyl group $W(T_{2,4,6})$ containing its 2-congruence subgroup, and that up to $\Aut(S)$ there is a unique smooth rational curve on such a surface.
  With Barth-Peters on the unnodal case this describes $\Aut$ at a generic point of $\fen$.

- Ingalls et al. (2015) study semiorthogonal decompositions of $D^b(Y)$ for nodal Enriques surfaces.

- Martin (2024) shows every nodal Enriques surface, not merely a generic one, is a **Reye congruence**: with $F_i^{\pm}$ the multiple fibers of the ten elliptic pencils, the image of the Fano model defined by $|\tfrac13\sum F_i^+|$ lies on a quadric.

- Dolgachev-Kondo (2013) show $F_{\Nod}$ is rational.

Related: [Coble families research program](#sec-coble-families-research-program), [Halphen index-2 moduli program](#sec-halphen-index-2-moduli-program).
