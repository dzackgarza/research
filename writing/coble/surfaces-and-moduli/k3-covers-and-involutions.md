# K3 double covers and their involutions {#sec-k3-covers-involutions}

## The double cover construction

::: {.proposition #prop:double-cover-canonical-bundle title="Canonical bundle of a double cover"}

Let $Y$ be a smooth projective surface, let $B\subset Y$ be a smooth divisor, and let $\mcl$ be a line bundle on $Y$ with $\mcl^{\tensor 2}\cong\OO_Y(B)$.
Let $\pi\colon X\to Y$ be the double cover branched along $B$ and determined by $\mcl$.
Then $\pi_*\OO_X\cong\OO_Y\oplus\inverseof{\mcl}$ and
$$
K_X = \pi^*(K_Y + \mcl)
.
$$
In particular, if $B\in\abs{-2K_Y}$ and $\mcl = -K_Y$, then $K_X = \OO_X$.
:::

::: {.proof}

The first two statements are the case $n = 2$ of [@BHPV04, Lemmas I.17.1(iii) and I.17.2].
Substituting $\mcl = -K_Y$ gives $K_X = \pi^*(K_Y - K_Y) = \OO_X$.
:::

::: {.proposition #prop:coble-canonical-cover title="The canonical cover of a terminal Coble surface"}

Let $S$ be a terminal Coble surface of K3 type over $\CC$, with $\abs{-2K_S} = \theset{C}$ and $C = C_1+\cdots+C_n$ a disjoint union of $n$ smooth rational curves of square $-4$.
Let $\mcl = \OO_S(-K_S)$, let $s\in H^0(\mcl^{\tensor_{\OO_S} 2})$ be a section with zero locus $C$, and let $f\colon X\to S$ be the double cover defined by $(\mcl, s)$.
Then $X$ is a smooth K3 surface [@DK25, Prop. 9.1.1].
For a general such $S$, $\Pic(X)$ is a $2$-elementary lattice of rank $10+n$ whose discriminant group has rank $12-n$ over $\FF_2$ [@CDL25, Sec. 5.4].
:::

## Geometric involutions on the double cover

::: {.proposition #prop:k3-cover-p1xp1-involutions title="The K3 double cover of $\PP^1\times\PP^1$ and its involutions"}

Let $Y = \PP^1\times\PP^1$ and let $\tau$ be the involution
$$
\tau(x, y) = (-x, -y)
$$
of $Y$.
The fixed points of $\tau$ are the four torus-fixed points, those with $x, y\in\theset{0, \infty}$.
Let $B\in\abs{-2K_Y} = \abs{\OO_Y(4,4)}$ be a $\tau$-invariant divisor with at worst ADE singularities that does not pass through these four points, and let $\pi\colon X\to Y$ be the double cover branched in $B$.
Write $X$ as the hypersurface $z^2 + f(x,y) = 0$, where $f$ is the $\tau$-invariant polynomial of bidegree $(4,4)$ that defines $B$.
Then the following hold [@AEGS25, Sec. 2.1].

1. $X$ is a K3 surface. The deck involution of $\pi$ is the **del Pezzo** involution $\idp(x,y,z) = (x,y,-z)$, and $X/\idp = Y$.

2. The involution $\tau$ has two lifts to $X$:
   - the **Enriques** involution $\ien(x,y,z) = (-x,-y,-z)$, which is basepoint-free, and whose quotient $Z = X/\ien$ is an Enriques surface;
   - the **Nikulin** involution $\inik(x,y,z) = (-x,-y,z)$, whose quotient $Z' = X/\inik$ is a K3 surface with eight $A_1$ singularities and possibly more.

3. The involutions $\idp$, $\ien$ and $\inik$ commute, and with the identity they form a Klein four-group in $\Aut(X)$.

4. Let $\omega$ be a nonvanishing $2$-form on $X$. Then $\idp^*\omega = \ien^*\omega = -\omega$ and $\inik^*\omega = \omega$. So $\idp$ and $\ien$ are nonsymplectic, and $\inik$ is symplectic.

5. The $\tau$-invariant polynomials $f$ of bidegree $(4,4)$ are the linear combinations of $13$ monomials. They define a point of an open subset $U\subset\PP^{12}$, and the quotient $U/(D_4 \semidirect (\CC^\times)^2)$ has dimension $10$.
:::

## Induced lattice involutions on $H^2$

::: {.definition #def:lattice-involutions-k3 title="Lattice involutions for K3 covers"}

Fix a basis of the K3 lattice $\lkt$ corresponding to the decomposition $U^3 \oplus E_8^2$, and write a general vector as $(u_1, u_2, u_3, \alpha_1, \alpha_2)$ with $u_i \in U$ and $\alpha_j \in E_8$.
The three geometric involutions $\idp$, $\ien$, and $\inik$ of @prop:k3-cover-p1xp1-involutions induce isometries of $\lkt$, denoted $\Idp$, $\Ien$, and $\Inik$ respectively, given in this basis by
$$
\begin{aligned}
    \Idp(u_1, u_2, u_3, \alpha_1, \alpha_2)        &= (-u_1,\, u_3,\, u_2,\, -\alpha_1,\, -\alpha_2), \\
    \Ien(u_1, u_2, u_3, \alpha_1, \alpha_2) &= (-u_1,\, u_3,\, u_2,\, \alpha_2,\, \alpha_1), \\
    \Inik(u_1, u_2, u_3, \alpha_1, \alpha_2) &= (u_1,\, u_2,\, u_3,\, -\alpha_2,\, -\alpha_1)
\end{aligned}
$$
[@AEGS25, Def. 2.3].
:::

::: {.proposition #prop:k3-cover-lattice-involutions-klein title="The lattice involutions form a Klein four-group"}

The isometries $\Idp$, $\Ien$ and $\Inik$ of @def:lattice-involutions-k3 are involutions that commute pairwise, and $\Ien\circ\Idp = \Idp\circ\Ien = \Inik$.
So $\theset{\id, \Idp, \Ien, \Inik}$ is a subgroup of $\Orth(\lkt)$ isomorphic to $\ZZ_2^2$.
:::

::: {.proof}

Each formula in @def:lattice-involutions-k3 changes signs of summands and exchanges two summands of the same isometry class, so its square is the identity.
For $v = (u_1, u_2, u_3, \alpha_1, \alpha_2)$, the formulas give
$$
\begin{aligned}
\Ien(\Idp v) &= \Ien(-u_1, u_3, u_2, -\alpha_1, -\alpha_2) = (u_1, u_2, u_3, -\alpha_2, -\alpha_1) = \Inik v, \\
\Idp(\Ien v) &= \Idp(-u_1, u_3, u_2, \alpha_2, \alpha_1) = (u_1, u_2, u_3, -\alpha_2, -\alpha_1) = \Inik v.
\end{aligned}
$$
Because $\Idp$ and $\Ien$ are involutions, $\Idp\circ\Inik = \Ien = \Inik\circ\Idp$ and $\Ien\circ\Inik = \Idp = \Inik\circ\Ien$.
So the four elements are closed under composition, they commute, and every element has order at most $2$.
The three involutions are distinct and nontrivial: $\Idp$ and $\Ien$ send $(u_1, 0, 0, 0, 0)$ to $(-u_1, 0, 0, 0, 0)$ and $\Inik$ fixes it, and $\Idp$ sends $(0, 0, 0, \alpha_1, 0)$ to $(0, 0, 0, -\alpha_1, 0)$ while $\Ien$ sends it to $(0, 0, 0, 0, \alpha_1)$.
A group of order $4$ in which every element has order at most $2$ is isomorphic to $\ZZ_2^2$.
:::

::: {.notation title="Invariant and coinvariant sublattices of the lattice involutions"}

For $\star\in\theset{\dP, \En, \Nik}$, write $S_\star \definedas \lkt^{I_\star = 1}$ for the invariant sublattice and $T_\star \definedas \lkt^{I_\star = -1}$ for the coinvariant sublattice of $I_\star$, in the sense of @def:invariant_coinvariant_lattices.
For the Nikulin involution these are also written $L_{\Nik}^{+} = S_{\Nik}$ and $L_{\Nik}^{-} = T_{\Nik}$.
By @prop:involution_eigenspaces, $S_\star$ and $T_\star$ are orthogonal and rationally span $\lkt_\QQ$.
:::

::: {.proposition #prop:k3-cover-eigenlattices title="Eigenlattices of the lattice involutions"}

The invariant and coinvariant sublattices of $\Idp$, $\Ien$ and $\Inik$ are even and $2$-elementary.
Their isometry classes and their invariants $(r,a,\delta)_n$, where $n = n_+$ is the number of positive eigenvalues, are the following [@AEGS25, Sec. 2.3].

| $L$ | Isometry class | $\rank_\ZZ(L)$ | $\operatorname{sig}(L)$ | $(r,a,\delta)_n$ | $A_L$ |
| --- | --- | --- | --- | --- | --- |
| $\sdp$ | $U(2)$ | $2$ | $(1,1)$ | $(2,2,0)_1$ | $\ZZ_2^2$ |
| $\tdp$ | $U \oplus U(2) \oplus E_8^2$ | $20$ | $(2,18)$ | $(20,2,0)_2$ | $\ZZ_2^2$ |
| $\sen$ | $U(2) \oplus E_8(2)$ | $10$ | $(1,9)$ | $\EnriquesInvariants_1$ | $\ZZ_2^{10}$ |
| $\ten$ | $U \oplus U(2) \oplus E_8(2)$ | $12$ | $(2,10)$ | $(12,10,0)_2$ | $\ZZ_2^{10}$ |
| $L_{\Nik}^{+}$ | $U^3 \oplus E_8(2)$ | $14$ | $(3,11)$ | $(14,8,0)_3$ | $\ZZ_2^8$ |
| $L_{\Nik}^{-}$ | $E_8(2)$ | $8$ | $(0,8)$ | $(8,8,0)_0$ | $\ZZ_2^8$ |
:::

## Two constraints on involutions of a K3

::: {.proposition #prop:del-pezzo-invariant-has-no-roots title="The del Pezzo invariant lattice contains no class of square $-2$"}

Let $X$ be a K3 surface and let $\iota\in\Aut(X)$ be an involution whose invariant lattice is $H^2(X,\ZZ)^{\iota}\cong\sdp = U(2)$.
Then $H^2(X,\ZZ)^{\iota}$ contains no class of square $-2$, and consequently $\iota$ fixes no smooth rational curve on $X$.
:::

::: {.proof}

With an isotropic basis $a,b$ of $U(2)$ satisfying $a\cdot b = 2$, the vectors are $ma+nb$ and have square $4mn$, so $-2$ is not attained; an integral class fixed by $\iota$ lies in $H^2(X,\ZZ)^{\iota}$, and the class of a smooth rational curve fixed by $\iota$ is such a class of square $-2$.
:::

::: {.example title="A class of square $-2$ in $\tdp$"}

Let $E,F$ be a hyperbolic basis of $U$ and $a,b$ an isotropic basis of $U(2)$ with $a\cdot b=2$.
In $\tdp=U\oplus U(2)\oplus E_8^2$ the class $E+F+a-b$ has square $2-4=-2$.
So the anti-invariant lattice of an involution as in @prop:del-pezzo-invariant-has-no-roots can contain classes of square $-2$.
:::

::: {.proposition #prop:product-of-involutions title="When a product of involutions is an involution"}

Let $X$ be a K3 surface and let $\iota,\iota'\in\Aut(X)$ be involutions.
Then $\iota\iota'$ is an involution if and only if $\iota$ and $\iota'$ commute.
If a generator $\sigma$ of $H^{2,0}(X)$ satisfies $\iota^*\sigma = \iota'^*\sigma = -\sigma$, then $(\iota\iota')^*\sigma = +\sigma$; with commutation as well, $\iota\iota'$ is therefore a symplectic involution.
:::

::: {.proof}

If $\iota\iota'$ is an involution then $\iota\iota'\iota\iota' = \id$, and multiplying on the left by $\iota$ and on the right by $\iota'$, both of which are their own inverses, gives $\iota'\iota = \iota\iota'$.
Conversely $(\iota\iota')^2 = \iota\iota'\iota\iota' = \iota^2\iota'^2 = \id$ whenever the two commute, the middle step being the only place commutation is used.
Independently of commutation, $(\iota\iota')^* = \iota'^*\circ\iota^*$, so $(\iota\iota')^*\sigma = \iota'^*(\iota^*\sigma) = \iota'^*(-\sigma) = \sigma$: the factor $H^{2,0}(X)$ is one dimensional and each involution acts on it by a scalar, so the product acts by $(-1)(-1) = +1$ whatever the order of composition.
:::
