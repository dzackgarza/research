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

For a smooth complex Enriques surface $Z$, the canonical cover $q\colon X\to Z$ has the
intrinsic form
$$
X=\operatorname{Spec}_Z(\OO_Z\oplus\omega_Z),
$$
with multiplication determined by $\omega_Z^{\otimes2}\cong\OO_Z$.
It is étale. A *marking* of $Z$ is an isometry
$\phi\colon\operatorname{Num}(Z)\to E_{10}$. Pullback kills the
canonical torsion class and induces an isometric embedding
$$
q^*\colon\operatorname{Num}(Z)(2)\hookrightarrow H^2(X,\ZZ),
\qquad \operatorname{im}(q^*)=H^2(X,\ZZ)^{\iota^*=1}
$$
(@prop:enriques-cohomology, @prop:enriques-cover-eigenlattices).
Thus the induced K3 lattice polarization is by $E_{10}(2)$; the
period-domain description must also impose the Enriques open locus
of @prop:enriques-period-domain.

The diagonal model makes the factor of $2$ in the pullback explicit.
Set $M=U\oplus E_8$ and identify $H^2(X,\ZZ)$ with
$M\oplus M\oplus U$. In this marking, the Enriques involution acts by
$$
\iota^*(m,m',u)=(m',m,-u).
$$
Its invariant lattice is the diagonal copy
$\{(m,m,0):m\in M\}\cong M(2)$, since
$(m,m,0)^2=2m^2$. Its anti-invariant lattice is
$\{(m,-m,u):m\in M,\ u\in U\}\cong M(2)\oplus U$.
The negative sign on the third $U$ is required by these eigenspaces.

::: {.proposition #prop:k3-cover-p1xp1-involutions title="The K3 double cover of $\PP^1\times\PP^1$ and its involutions"}

Let $Y = \PP^1\times\PP^1$ and let $\tau$ be the involution
$$
\tau(x, y) = (-x, -y)
$$
of $Y$.
The fixed points of $\tau$ are the four torus-fixed points, those with $x, y\in\theset{0, \infty}$.
Let $B\in\abs{-2K_Y} = \abs{\OO_Y(4,4)}$ be a smooth $\tau$-invariant divisor that does not pass through these four points, and let $\pi\colon X\to Y$ be the double cover branched in $B$.
Write $X$ as the hypersurface $z^2 + f(x,y) = 0$, where $f$ is the $\tau$-invariant polynomial of bidegree $(4,4)$ that defines $B$.
Then the following hold [@AEGS25, Sec. 2.1].

1. $X$ is a K3 surface. The deck involution of $\pi$ is the **del Pezzo** involution $\idp(x,y,z) = (x,y,-z)$, and $X/\idp = Y$.

2. The involution $\tau$ has two lifts to $X$:
   - the **Enriques** involution $\ien(x,y,z) = (-x,-y,-z)$, which is fixed-point-free, and whose quotient $Z = X/\ien$ is an Enriques surface;
   - the **Nikulin** involution $\inik(x,y,z) = (-x,-y,z)$, whose quotient $Z' = X/\inik$ has eight $A_1$ singularities and a K3 minimal resolution.

3. The involutions $\idp$, $\ien$ and $\inik$ commute, and with the identity they form a Klein four-group in $\Aut(X)$.

4. Let $\omega$ be a nonvanishing $2$-form on $X$. Then $\idp^*\omega = \ien^*\omega = -\omega$ and $\inik^*\omega = \omega$. So $\idp$ and $\ien$ are nonsymplectic, and $\inik$ is symplectic.

5. The $\tau$-invariant polynomials $f$ of bidegree $(4,4)$ are the linear combinations of $13$ monomials. They define a point of an open subset $U\subset\PP^{12}$, and the quotient $U/(D_4 \semidirect (\CC^\times)^2)$ has dimension $10$.
:::

## Recovering the quotient diagram {#sec-intrinsic-enriques-quotients}

The double-cover diagram is related to the projective models of
[@Cos83, §6.3.1; @CD89, Corollary 4.7.2] and to Horikawa's explicit
period construction [@Hor78]. Its double-plane antecedent is Enriques'
construction [@Enr07]; [@CDL25] gives the broader historical account.

Let $(Z,[L])$ be a degree-two numerically polarized Enriques surface in
this construction, and work with its normal projective models. The
linear system $|L^{\otimes2}|$ determines the quotient surface $W$.
It is independent of the choice between $L$ and $L\otimes K_Z$, since
$2K_Z=0$. In the non-special case $W$ has four $A_1$ singularities;
in the special case it has singularities $A_3+2A_1$ and the intermediate
surface is $Y=\PP(1,1,2)$ [@AEGS25, §§2.1–2.2].

The intrinsic reconstruction uses the nonzero class
$A\in\operatorname{Cl}(W)_{\mathrm{tors}}\cong\ZZ/2$.
Put $M=\OO_W(A)$ and choose $M^{[2]}\cong\OO_W$, where brackets denote
reflexive powers. Then
$$
Y=\operatorname{Spec}_W(\OO_W\oplus M),\qquad
X=\operatorname{Norm}(Y\times_W Z).
$$
The algebra multiplication is the composite
$M\otimes M\to M^{[2]}\cong\OO_W$. This specifies the missing
multiplication data in the degree-two cover. Over $\CC$, rescaling the
chosen trivialization gives an isomorphic cover.

Normalization in the second formula is necessary. Near an $A_1$ point
of $W$, the two local index covers have a fiber product whose components
meet over that point, whereas their normalization separates the sheets.
On the open set where the quotient is free, the fiber product recovers
the Klein four-group cover; normalization extends it to the normal
models. The involutions and the third quotient $X/\iota_{\mathrm{Nik}}$
are then recovered from the two covering transformations. If $X$ has
ADE singularities, its minimal resolution gives the smooth K3 surface.

## The Horikawa parameter space {#sec-horikawa-parameters}

If the branch divisor has ADE singularities, the double cover can be singular:
its minimal resolution is a smooth K3 surface. The involutions lift to that
resolution. The quotient by the Enriques involution is then a smooth Enriques
surface, while the quotient of the unresolved cover is its ADE model
[@AEGS25, Sec. 2.1].

For the smooth branch curves in @prop:k3-cover-p1xp1-involutions, write
$$
f=\sum_{\substack{0\leq a,b\leq4\\a+b\equiv0\pmod2}}
c_{ab}X_0^{4-a}X_1^aY_0^{4-b}Y_1^b.
$$
The four coefficients $c_{00},c_{04},c_{40},c_{44}$ are nonzero precisely
when the branch curve avoids the fixed points of $\tau$. Let
$U\subset\PP^{12}$ be the open locus where these coefficients are nonzero
and $B_f$ is smooth. Its universal branch divisor is
$$
\mathcal B=V(f)\subset U\times(\PP^1\times\PP^1).
$$
This is the smooth Horikawa family of [@BHPV04, Chapter VIII, §15;
@AEGS25, §2.1].

::: {.proposition #prop:horikawa-monomials-normalizer title="Invariant monomials and coordinate changes"}
The invariant monomials are those with $(a,b)$ in
$$
\bigl(\{0,2,4\}\times\{0,2,4\}\bigr)
\;\amalg\;
\bigl(\{1,3\}\times\{1,3\}\bigr).
$$
The centralizer of $\tau$ in $\Aut(\PP^1\times\PP^1)$ is
$$
G=(\mathbb G_m^2)\rtimes
\bigl((\ZZ/2\ZZ)^2\rtimes\ZZ/2\ZZ\bigr).
$$
The finite factor is the dihedral group of order $8$: its generators
invert either coordinate and interchange the two factors. The generic
quotient of $U$ by $G$ has dimension $10$.
:::

::: {.proof}
The involution acts on the displayed monomial by $(-1)^{a+b}$, which gives
the two sets of exponent pairs. A projective transformation of $\PP^1$
commuting with $x\mapsto-x$ preserves its fixed set $\{0,\infty\}$,
so it is $x\mapsto ax$ or $x\mapsto a/x$. Applying this to each factor,
and adjoining their interchange, gives $G$. A general branch curve has
finite stabilizer, so the quotient dimension is $12-2=10$, as in
[@AEGS25, §2.1].
:::

::: {.proposition #prop:horikawa-pair-volumes title="The branch, K3, and Enriques pairs"}
Let $\pi\colon X\to Y=\PP^1\times\PP^1$ be a smooth member of this
family, let $q\colon X\to Z$ be its Enriques quotient, and let $R$ be the
ramification divisor of $\pi$. Put $R_Z=q(R)$ with its reduced structure.
For $0<\epsilon\ll1$,
$$
\begin{aligned}
K_X+\epsilon R
 &=\pi^*\left(K_Y+\frac{1+\epsilon}{2}B\right)
 =q^*(K_Z+\epsilon R_Z),\\
\left(K_Y+\frac{1+\epsilon}{2}B\right)^2&=8\epsilon^2,\\
(K_X+\epsilon R)^2&=16\epsilon^2,\\
(K_Z+\epsilon R_Z)^2&=8\epsilon^2.
\end{aligned}
$$
:::

::: {.proof}
The double-cover formula gives $K_X=\pi^*(K_Y+B/2)$ and
$\pi^*B=2R$. The map $q$ is étale and $q^*R_Z=R$
[@AEGS25, §2.1], so $K_X=q^*K_Z$ and the second covering equality
follows. On $Y$, $K_Y=(-2,-2)$ and $B=(4,4)$; hence
$K_Y+(1+\epsilon)B/2=(2\epsilon,2\epsilon)$ has square $8\epsilon^2$.
Pullback multiplies intersections by the degree of the cover, which
gives the remaining equalities.
:::

Let $\mathfrak U$ be the parameter stack on which the square-root line bundle of the universal branch divisor is chosen. Write $\mathcal X$, $\mathcal T$, and $\mathcal S$ for the branch-surface, K3-cover, and Enriques-quotient families over $\mathfrak U$. If $\mathcal B$ is the branch divisor, $\mathcal R$ its ramification preimage, and $\mathcal R_{\mathcal S}$ the reduced image on the Enriques family, the source-native covering square is:

::: {#fig-horikawa-family-cover-square .figure}
\input{tikz/dissertation/horikawa-family-cover-square.tex}

The double cover and Enriques quotient over the square-root parameter stack; the coefficients agree with @prop:horikawa-pair-volumes.
:::

The branch family defines a morphism from $U$ to the stack of stable
surface pairs with coefficient $(1+\epsilon)/2$ and volume
$8\epsilon^2$. The K3 and Enriques families define the corresponding
maps with coefficients $\epsilon$ and volumes $16\epsilon^2$ and
$8\epsilon^2$. For families of double covers these maps are taken on
the parameter stack where the square-root line bundle is part of the
data; the universal branch equation over projective coefficient space
alone does not choose that square root. Taking the closure of each
image in the coarse KSBA moduli space, then normalizing, gives the
branch, K3, and Enriques compactifications. The finite-cover comparison
is developed in @sec-abcde-surfaces and the classifying map in
@prop:enriques-involution-extends.

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
