# K3 double covers and their involutions {#sec:k3-covers-involutions}

This section records the general machinery of the K3 double cover of a rational surface, the distinguished geometric involutions it carries, and the lattice involutions they induce on $H^2$ together with their invariant and coinvariant sublattices.
The Coble-specific instance of the double-cover construction — where the base is a terminal Coble surface and the branch locus is the anticanonical curve — is treated in the section on K3 covers of Coble surfaces; here we develop the construction for a general base and the involution-theoretic apparatus common to the del Pezzo, Enriques, and Nikulin quotients.
The general invariant/coinvariant lattice formalism $L^G$, $L_G$ is developed in [the invariant/coinvariant-lattice definition](#def:invariant_coinvariant_lattices) and [the involution-eigenspace proposition](#prop:involution_eigenspaces); we cross-reference it rather than restating it.

## The double cover construction

::: {.Remark #rmk:k3-double-cover-construction}
### The K3 double cover construction

A standard method to produce Calabi-Yau varieties involves taking a double cover $\pi: X \to Y$ branched over a reduced divisor $B$.
If $B \in \abs{-2K_Y}$, one takes $\cL = -K_Y$.
The cover $X$ is defined via the $\OO_Y$-algebra
$$
\cA = \OO_Y \oplus \cL\inv
.
$$

Adjunction yields
$$
K_X = \pi^*(K_Y + \cL)
,
$$
and substituting $\cL = -K_Y$ gives $K_X = \OO_X$, so that $X$ has trivial canonical bundle.

Here $\tau$ is the involution
$$
\tau(x, y) = (-x, -y)
$$
of $Y = \PP^1\times\PP^1$, the involution covered by the Enriques and Nikulin involutions of [the geometric-involutions remark](#rmk:geometric-involutions); the del Pezzo involution covers the identity.
Its fixed locus is the four torus-fixed points, those with $x, y\in\ts{0, \infty}$.
By taking $B \subset Y$ to be a smooth $\tau$-invariant curve in $\abs{-2K_Y} = \abs{\OO_Y(4,4)}$, we obtain a $10$-dimensional family of K3 surfaces, after quotienting by the toric automorphisms $D_4 \semidirect (\CC^\times)^2$.
:::

::: {.Remark}

The specialization of [the K3 double-cover construction](#rmk:k3-double-cover-construction) to a terminal Coble surface of K3 type is carried out in the section on K3 covers of Coble surfaces: there one takes $\cL = \OO_S(-K_S)$ for $S$ the (rational) base and a section $s \in H^0(\cL^{\tensor 2})$ cutting out the anticanonical curve $C$, and the resulting double cover $f: X \to S$ is a smooth K3 surface with $\Pic(X)$ a $2$-elementary lattice of invariants $(r,a,\delta)_1 = (10+n, 12-n, \delta)_1$ [@DK25 Prop. 9.1.1; @CDL25 Def. 5.4.3].
:::

## Geometric involutions on the double cover

::: {.Remark #rmk:geometric-involutions}
### Geometric involutions on the K3 double cover

For the K3 double cover $X \to Y = \PP^1\times\PP^1$, there are three distinguished involutions acting on the coordinates $(x,y,z)$:

- $\idp(x,y,z) = (x,y,-z)$: the **del Pezzo** (deck) involution, the generator of the deck transformations of the double cover.
  Its quotient is a K3 quotient and $\idp^*\omega_X = -\omega_X$.

- $\ien(x,y,z) = (-x,-y,-z)$: the **Enriques** involution, with smooth Enriques quotient $Z$, satisfying $\ien^*\omega_X = -\omega_X$.

- $\inik(x,y,z) = (-x,-y,z)$: the **Nikulin** involution, with singular K3 quotient $Z'$ carrying $\geq 8 A_1$ singularities, satisfying $\inik^*\omega_X = +\omega_X$.

These generate a faithful representation of the Klein four-group $\ZZ_2^2 \hookrightarrow \Aut(X)$.
The del Pezzo and Enriques involutions act on the holomorphic $2$-form by $-1$ (they are nonsymplectic), whereas the Nikulin involution acts by $+1$ (it is symplectic); consistently with the group law, $\ien\circ\idp = \inik$.
:::

## Induced lattice involutions on $H^2$

::: {.Definition #def:lattice-involutions-k3}
### Lattice involutions for K3 covers

Fix a basis of the K3 lattice $\lkt$ corresponding to the decomposition $U^3 \oplus E_8^2$, and write a general vector as $(u_1, u_2, u_3, \alpha_1, \alpha_2)$ with $u_i \in U$ and $\alpha_j \in E_8$.
The three geometric involutions $\idp$, $\ien$, and $\inik$ of [the geometric-involutions remark](#rmk:geometric-involutions) induce isometries of $\lkt$, denoted $\Idp$, $\Ien$, and $\Inik$ respectively, given in this basis by
$$
\begin{aligned}
    \Idp(u_1, u_2, u_3, \alpha_1, \alpha_2)        &= (-u_1,\, u_3,\, u_2,\, -\alpha_1,\, -\alpha_2), \\
    \Ien(u_1, u_2, u_3, \alpha_1, \alpha_2) &= (-u_1,\, u_3,\, u_2,\, \alpha_2,\, \alpha_1), \\
    \Inik(u_1, u_2, u_3, \alpha_1, \alpha_2) &= (u_1,\, u_2,\, u_3,\, -\alpha_2,\, -\alpha_1).
\end{aligned}
$$
:::

::: {.Remark}
### Properties of the lattice involutions

The lattice involutions satisfy the following.

- The group $\gens{\Idp, \Ien, \Inik}$ is isomorphic to $\ZZ_2^2$; in particular these involutions mutually commute, and $\Ien\circ \Idp = \Inik$.

- For each involution $I_\star$, the **invariant sublattice** is denoted $S_\star \da \lkt^{I_\star = 1}$ and the **coinvariant sublattice** is $T_\star \da \lkt^{I_\star = -1}$, in the sense of [the invariant/coinvariant-lattice definition](#def:invariant_coinvariant_lattices): $S_\star$ is the $+1$-eigenlattice and $T_\star$ the $-1$-eigenlattice of $I_\star$, and by [the involution-eigenspace proposition](#prop:involution_eigenspaces) these are orthogonal and rationally span $\lkt_\QQ$.

- The transcendental lattices $T_Z$ of the Enriques surfaces $Z$ primitively embed into these invariant sublattices.
:::

The isometry classes of the invariant and coinvariant sublattices of the three involutions, together with their $2$-elementary invariants $(r,a,\delta)_n$ (where $n = n_+$ is the number of positive eigenvalues) and discriminant groups $A_L$, are collected in @tbl-k3-cover-coinvariant-lattices. For the del Pezzo and Enriques involutions these lattices also appear in [Period domain embeddings and normalization](lattices.md) alongside [the sequence of primitive embeddings](#lem:sequence_of_embeddings). The Enriques (co)invariant lattices are built from the twist $E_{10}(2) = U(2)\oplus E_8(2)$ ($\sen = E_{10}(2)$, $\ten = U\oplus E_{10}(2)$), whereas the del Pezzo lattices $\sdp = U(2)$, $\tdp = U\oplus U(2)\oplus E_8^2$ retain an untwisted $E_8^2$.
The $2$-elementarity of both $S_\star$ and $T_\star$ is the content of [the coinvariant $2$-elementarity proposition](#prop:coinvariant_involution_2elementary), and their classification is Nikulin's [@Nik80].

| $L$ | Isometry class | $\rank_\ZZ(L)$ | $\operatorname{sig}(L)$ | $(r,a,\delta)_n$ | $A_L$ |
| --- | --- | --- | --- | --- | --- |
| $\sdp$ | $U(2)$ | $2$ | $(1,1)$ | $(2,2,0)_1$ | $\ZZ_2^2$ |
| $\tdp$ | $U \oplus U(2) \oplus E_8^2$ | $20$ | $(2,18)$ | $(20,2,0)_2$ | $\ZZ_2^2$ |
| $\sen$ | $U(2) \oplus E_8(2)$ | $10$ | $(1,9)$ | $(10,10,0)_1$ | $\ZZ_2^{10}$ |
| $\ten$ | $U \oplus U(2) \oplus E_8(2)$ | $12$ | $(2,10)$ | $(12,10,0)_2$ | $\ZZ_2^{10}$ |
| $L_{\mathrm{Nik}}^{+}$ | $U^3 \oplus E_8(2)$ | $14$ | $(3,11)$ | $(14,8,0)_3$ | $\ZZ_2^8$ |
| $L_{\mathrm{Nik}}^{-}$ | $E_8(2)$ | $8$ | $(0,8)$ | $(8,8,0)_0$ | $\ZZ_2^8$ |

: Invariant sublattices $S_\star$ and coinvariant sublattices $T_\star$ of the
del Pezzo, Enriques, and Nikulin involutions on $\lkt = U^3 \oplus E_8^2$. For
the Nikulin involution the invariant and coinvariant lattices are written
$L_{\mathrm{Nik}}^{+}$ and $L_{\mathrm{Nik}}^{-}$; each complementary pair has
ranks summing to $22 = \operatorname{rank}\lkt$. {#tbl-k3-cover-coinvariant-lattices}
