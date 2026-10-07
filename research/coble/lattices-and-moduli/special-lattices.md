# K3 and Enriques lattice applications {#sec:k3-enriques-lattices}

The lattice definitions used here are collected in [[special-lattices-and-transformations|Special lattices and arithmetic transformations]]. This chapter records only their roles in the K3, Enriques, and Coble constructions.

## The Enriques lattice in geometry

::: {.remark title="Role in Enriques moduli"}

For an Enriques surface $Z$ the second integral cohomology carries a torsion summand,
$$
\NS(Z)\cong H^2(Z;\ZZ)\cong\ZZ^{10}\oplus\ZZ/2\ZZ,
$$
and the intersection pairing endows the free part $H^2(Z;\ZZ)_f$ with the structure of an even unimodular lattice of signature $(1,9)$.
By @def:enriques-lattice there is an isometry
$$
H^2(Z;\ZZ)_f\iso E_{10},
$$
and a **marking** of $Z$ is a choice of such an isometry [@CDL25].
The lattice $E_{10}$ is therefore the numerical lattice of an Enriques surface.
:::

::: {.remark title="The Enriques period lattice"}

The corresponding twist is $E_{10}(2)=U(2)\oplus E_8(2)$, whose $2$-elementary invariants are computed in the doubled-Enriques-lattice remark of [[special-lattices-and-transformations]].
This is the lattice denoted $\sen=E_{10}(2)$ in the lattice summary, and it recurs in the Coble tables as the base summand appearing alongside $U(2)$ and the root lattices; compare [[coble-lattice-table|the Coble lattice table]].
:::

## Degree $2d$ K3 periods

::: {.remark}

A primitive degree-$2d$ polarization class $h\in\lkt$ has orthogonal complement
$$
h^{\perp\lkt}\cong L_{\Kthree,2d}
$$
by @prop:degree-2d-k3-complement.
Thus the lattice $L_{\Kthree,2d}$ is the primitive period lattice for degree-$2d$ polarized K3 surfaces; its Hodge-theoretic use is developed in [[k3-periods-and-monodromy|K3 periods and monodromy]].
:::

## Coble instances of the $2$-elementary building blocks

::: {.remark}

The Coble lattices of [[coble-lattice-table|the Coble lattice table]] are instances of @thm:2elementary-building-blocks.
For example, the table contains
$$
E_8(2)\oplus U\oplus A_1^{\oplus2}
$$
at $n=2$ and
$$
E_8\oplus D_8\oplus U(2)
$$
at $n=8$.
These are applications of the general $2$-elementary decomposition, not additional definitions of the underlying lattices.
:::
