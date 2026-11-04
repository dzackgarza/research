# K3 double covers and their involutions {#sec-k3-covers-involutions}

This section records the general machinery of the K3 double cover of a rational surface, the distinguished geometric involutions it carries, and the lattice involutions they induce on $H^2$ together with their invariant and coinvariant sublattices.
The Coble-specific instance of the double-cover construction — where the base is a terminal Coble surface and the branch locus is the anticanonical curve — is treated in the section on K3 covers of Coble surfaces; here we develop the construction for a general base and the involution-theoretic apparatus common to the del Pezzo, Enriques, and Nikulin quotients.
The general invariant/coinvariant lattice formalism $L^G$, $L_G$ is developed in the invariant/coinvariant-lattice definition (@def:invariant_coinvariant_lattices) and the involution-eigenspace proposition (@prop:involution_eigenspaces); we cross-reference it rather than restating it.

## The double cover construction

::: {.remark #rmk:k3-double-cover-construction title="The K3 double cover construction"}

A standard method to produce Calabi-Yau varieties involves taking a double cover $\pi: X \to Y$ branched over a reduced divisor $B$.
If $B \in \abs{-2K_Y}$, one takes $\mcl = -K_Y$.
The cover $X$ is defined via the $\OO_Y$-algebra
$$
\mca = \OO_Y \oplus \inverseof{\mcl}
.
$$

For the double cover branched along $B \in \abs{-2\mcl}$ the canonical bundle formula gives
$$
K_X = \pi^*(K_Y + \mcl)
,
$$
and substituting $\mcl = -K_Y$ gives $K_X = \OO_X$, so that $X$ has trivial canonical bundle.

Here $\tau$ is the involution
$$
\tau(x, y) = (-x, -y)
$$
of $Y = \PP^1\times\PP^1$, the involution covered by the Enriques and Nikulin involutions of the geometric-involutions remark (@rmk:geometric-involutions); the del Pezzo involution covers the identity.
Its fixed locus is the four torus-fixed points, those with $x, y\in\theset{0, \infty}$.
By taking $B \subset Y$ to be a smooth $\tau$-invariant curve in $\abs{-2K_Y} = \abs{\OO_Y(4,4)}$, we obtain a $10$-dimensional family of K3 surfaces, after quotienting by the toric automorphisms $D_4 \semidirect (\CC^\times)^2$.
:::

::: {.remark}

The specialization of the K3 double-cover construction (@rmk:k3-double-cover-construction) to a terminal Coble surface of K3 type is carried out in the section on K3 covers of Coble surfaces: there one takes $\mcl = \OO_S(-K_S)$ for $S$ the (rational) base and a section $s \in H^0(\mcl^{\tensor_{\OO_S} 2})$ cutting out the anticanonical curve $C$, and the resulting double cover $f: X \to S$ is a smooth K3 surface with $\Pic(X)$ a $2$-elementary lattice of invariants $(r,a,\delta)_1 = (10+n, 12-n, \delta)_1$ [@DK25 Prop. 9.1.1; @CDL25 Def. 5.4.3].
:::

## Geometric involutions on the double cover

::: {.remark #rmk:geometric-involutions title="Geometric involutions on the K3 double cover"}

For the K3 double cover $X \to Y = \PP^1\times\PP^1$, there are three distinguished involutions acting on the coordinates $(x,y,z)$:

- $\idp(x,y,z) = (x,y,-z)$: the **del Pezzo** (deck) involution, the generator of the deck transformations of the double cover.
  Its quotient is a K3 quotient and $\idp^*\omega_X = -\omega_X$.

- $\ien(x,y,z) = (-x,-y,-z)$: the **Enriques** involution, with smooth Enriques quotient $Z$, satisfying $\ien^*\omega_X = -\omega_X$.

- $\inik(x,y,z) = (-x,-y,z)$: the **Nikulin** involution, with singular K3 quotient $Z'$ carrying $\geq 8 A_1$ singularities, satisfying $\inik^*\omega_X = +\omega_X$.

These generate a faithful representation of the Klein four-group $\ZZ_2^2 \hookrightarrow \Aut(X)$.
The del Pezzo and Enriques involutions act on the holomorphic $2$-form by $-1$ (they are nonsymplectic), whereas the Nikulin involution acts by $+1$ (it is symplectic); consistently with the group law, $\ien\circ\idp = \inik$.
:::

## Induced lattice involutions on $H^2$

::: {.definition #def:lattice-involutions-k3 title="Lattice involutions for K3 covers"}

Fix a basis of the K3 lattice $\lkt$ corresponding to the decomposition $U^3 \oplus E_8^2$, and write a general vector as $(u_1, u_2, u_3, \alpha_1, \alpha_2)$ with $u_i \in U$ and $\alpha_j \in E_8$.
The three geometric involutions $\idp$, $\ien$, and $\inik$ of the geometric-involutions remark (@rmk:geometric-involutions) induce isometries of $\lkt$, denoted $\Idp$, $\Ien$, and $\Inik$ respectively, given in this basis by
$$
\begin{aligned}
    \Idp(u_1, u_2, u_3, \alpha_1, \alpha_2)        &= (-u_1,\, u_3,\, u_2,\, -\alpha_1,\, -\alpha_2), \\
    \Ien(u_1, u_2, u_3, \alpha_1, \alpha_2) &= (-u_1,\, u_3,\, u_2,\, \alpha_2,\, \alpha_1), \\
    \Inik(u_1, u_2, u_3, \alpha_1, \alpha_2) &= (u_1,\, u_2,\, u_3,\, -\alpha_2,\, -\alpha_1).
\end{aligned}
$$
:::

::: {.remark title="Properties of the lattice involutions"}

The lattice involutions satisfy the following.

- The group $\generators{\Idp, \Ien, \Inik}$ is isomorphic to $\ZZ_2^2$; in particular these involutions mutually commute, and $\Ien\circ \Idp = \Inik$.

- For each involution $I_\star$, the **invariant sublattice** is denoted $S_\star \definedas \lkt^{I_\star = 1}$ and the **coinvariant sublattice** is $T_\star \definedas \lkt^{I_\star = -1}$, in the sense of the invariant/coinvariant-lattice definition (@def:invariant_coinvariant_lattices): $S_\star$ is the $+1$-eigenlattice and $T_\star$ the $-1$-eigenlattice of $I_\star$, and by the involution-eigenspace proposition (@prop:involution_eigenspaces) these are orthogonal and rationally span $\lkt_\QQ$.

- The transcendental lattices $T_Z$ of the Enriques surfaces $Z$ primitively embed into these invariant sublattices.
:::

The isometry classes of the invariant and coinvariant sublattices of the three involutions, together with their $2$-elementary invariants $(r,a,\delta)_n$ (where $n = n_+$ is the number of positive eigenvalues) and discriminant groups $A_L$, are collected in @tbl-k3-cover-coinvariant-lattices.
For the del Pezzo and Enriques involutions these lattices also appear in @sec-lattices alongside the sequence of primitive embeddings (@lem:sequence_of_embeddings). The Enriques (co)invariant lattices are built from the twist $E_{10}(2) = U(2)\oplus E_8(2)$ ($\sen = E_{10}(2)$, $\ten = U\oplus E_{10}(2)$), whereas the del Pezzo lattices $\sdp = U(2)$, $\tdp = U\oplus U(2)\oplus E_8^2$ retain an untwisted $E_8^2$.
The $2$-elementarity of both $S_\star$ and $T_\star$ is the content of the coinvariant $2$-elementarity proposition (@prop:coinvariant_involution_2elementary), and their classification is Nikulin's [@Nik80].

| $L$ | Isometry class | $\rank_\ZZ(L)$ | $\operatorname{sig}(L)$ | $(r,a,\delta)_n$ | $A_L$ |
| --- | --- | --- | --- | --- | --- |
| $\sdp$ | $U(2)$ | $2$ | $(1,1)$ | $(2,2,0)_1$ | $\ZZ_2^2$ |
| $\tdp$ | $U \oplus U(2) \oplus E_8^2$ | $20$ | $(2,18)$ | $(20,2,0)_2$ | $\ZZ_2^2$ |
| $\sen$ | $U(2) \oplus E_8(2)$ | $10$ | $(1,9)$ | $\EnriquesInvariants_1$ | $\ZZ_2^{10}$ |
| $\ten$ | $U \oplus U(2) \oplus E_8(2)$ | $12$ | $(2,10)$ | $(12,10,0)_2$ | $\ZZ_2^{10}$ |
| $L_{\Nik}^{+}$ | $U^3 \oplus E_8(2)$ | $14$ | $(3,11)$ | $(14,8,0)_3$ | $\ZZ_2^8$ |
| $L_{\Nik}^{-}$ | $E_8(2)$ | $8$ | $(0,8)$ | $(8,8,0)_0$ | $\ZZ_2^8$ |

: Invariant sublattices $S_\star$ and coinvariant sublattices $T_\star$ of the
del Pezzo, Enriques, and Nikulin involutions on $\lkt = U^3 \oplus E_8^2$. For
the Nikulin involution the invariant and coinvariant lattices are written
$L_{\Nik}^{+}$ and $L_{\Nik}^{-}$; each complementary pair has
ranks summing to $22 = \rank\lkt$. {#tbl-k3-cover-coinvariant-lattices}

## Two constraints on involutions of a K3

The lattice decompositions above describe the abstract involutions of $\lkt$.
Whether a given K3 surface carries one of them as an automorphism is a separate question.
Two statements used elsewhere in the book are refined here: a necessary condition on the invariant lattice of a del Pezzo involution, which any representative of the Coble tuple's del Pezzo slot has to satisfy (@prop:coble-cover-marking), and the exact hypothesis under which a product of two involutions is again an involution, which is what any claim about the symplectic character of such a product has to carry.

::: {.proposition #prop:del-pezzo-invariant-has-no-roots title="The del Pezzo invariant lattice contains no class of square $-2$"}

Let $X$ be a K3 surface and let $\iota\in\Aut(X)$ be an involution whose invariant lattice is $H^2(X,\ZZ)^{\iota}\cong\sdp = U(2)$.
Then $H^2(X,\ZZ)^{\iota}$ contains no class of square $-2$, and consequently $\iota$ fixes no smooth rational curve on $X$.
:::

::: {.proof}

With isotropic generators $a,b$ of $U(2)$ satisfying $a\cdot b = 2$, the vectors are $ma+nb$ and have square $4mn$, so $-2$ is not attained; an integral class fixed by $\iota$ lies in $H^2(X,\ZZ)^{\iota}$, and the class of a smooth rational curve fixed by $\iota$ is such a class of square $-2$.
:::

::: {.remark title="What this does and does not rule out"}

The condition is necessary and not sufficient, and the hypothesis is that the invariant lattice *is* $\sdp$, of rank $2$: an involution whose invariant lattice merely contains $\sdp$ is not covered.
It says nothing against the existence of such an involution, because the anti-invariant lattice can itself contain classes of square $-2$: in $\tdp = U\oplus U(2)\oplus E_8^2$ the sum of $E+F$ for a hyperbolic basis of $U$, of square $2$, and of a vector of $U(2)$ of square $-4$ has square $-2$; the lemma constrains which rational curves are *fixed* and not which curves the surface carries.
:::

::: {.proposition #prop:product-of-involutions title="When a product of involutions is an involution"}

Let $X$ be a K3 surface and let $\iota,\iota'\in\Aut(X)$ be involutions.
Then $\iota\iota'$ is an involution if and only if $\iota$ and $\iota'$ commute.
If a generator $\sigma$ of $H^{2,0}(X)$ satisfies $\iota^*\sigma = \iota'^*\sigma = -\sigma$, then $(\iota\iota')^*\sigma = +\sigma$; with commutation as well, $\iota\iota'$ is therefore a symplectic involution.
The two conclusions are different claims: the second alone does not give the order.
:::

::: {.proof}

If $\iota\iota'$ is an involution then $\iota\iota'\iota\iota' = \id$, and multiplying on the left by $\iota$ and on the right by $\iota'$, both of which are their own inverses, gives $\iota'\iota = \iota\iota'$.
Conversely $(\iota\iota')^2 = \iota\iota'\iota\iota' = \iota^2\iota'^2 = \id$ whenever the two commute, the middle step being the only place commutation is used.
Independently of commutation, $(\iota\iota')^* = \iota'^*\circ\iota^*$, so $(\iota\iota')^*\sigma = \iota'^*(\iota^*\sigma) = \iota'^*(-\sigma) = \sigma$: the factor $H^{2,0}(X)$ is one dimensional and each involution acts on it by a scalar, so the product acts by $(-1)(-1) = +1$ whatever the order of composition.
:::

::: {.remark title="Why the order has to be stated"}
For a product of two involutions, being an involution and being symplectic are two different properties and the first is a hypothesis of the second as a statement about involutions.
The action on $H^{2,0}$ is forced by the nonsymplectic character of the factors and needs no commutation; the order is exactly equivalent to commutation.
So a tuple that lists a commuting pair of nonsymplectic involutions and then, separately, the symplectic character of their product, lists a consequence as though it were a condition; and a tuple that lists the symplectic character while leaving commutation open records a property of a product that need not be an involution at all.
:::
