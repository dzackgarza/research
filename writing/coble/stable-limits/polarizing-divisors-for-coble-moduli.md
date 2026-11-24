# Polarizing divisors for the moduli of Coble surfaces {#sec-coble-polarizing-divisors}

A KSBA compactification of a moduli space of K-trivial surfaces is the closure of a space of pairs $(X,\eps R)$, so it needs a polarizing divisor $R$ on each surface (@def:ksba-compactification).
In the sources the divisor is a *canonical choice*: a rational section of the projective bundle of a relatively big and nef line bundle over the moduli stack, equivalently an ample divisor on the generic surface [@AE23, Def. 6.1, arXiv v3 p. 16], or an algebraically varying big and nef divisor defined over a Zariski dense subset of the moduli space [@AEH24, Def. 3.3, arXiv v2 p. 8].
This page decides which polarizing divisors exist for the Coble surfaces with one boundary component.

The results of this page that are not attributed to a source are original to this volume, and each is proved here.
A statement that rests on another page of this volume, or on a published statement whose hypotheses are only checked here, says so in its text.

The results are these.

1. On $F^{\mathrm{un}}_\Co = \bD(T_\Co)/\Orth(T_\Co)$ no polarizing divisor exists. The classes that are invariant under the automorphisms of a general surface are the multiples of the canonical class (@thm:coble-invariant-classes), no line bundle among them is big (@cor:coble-no-canonical-polarization), and the period map of a family that has a polarization factors through a cover of $F^{\mathrm{un}}_\Co$ of degree divisible by $527$ (@thm:coble-polarized-family).
2. A polarization is an added structure. The surfaces with a polarization of a fixed type have a moduli space $\bD(T_\Co)/\Gamma_\lambda$, a finite cover of $F^{\mathrm{un}}_\Co$ (@prop:coble-polarized-moduli).
3. Two such structures occur in the sources: the plane model (@prop:coble-plane-model-space, @thm:coble-plane-model-compactification) and the numerical polarization of degree $2$ (@prop:coble-degree-two-space, @thm:coble-degree-two-compactification). Each gives a compact moduli space of KSBA-stable pairs for its cover.
4. For $F^{\mathrm{un}}_\Co$ itself each cover gives the finite map to the Baily--Borel compactification (@prop:coble-bb-finite). The semifans of the degree-$2$ structure computed in @thm:coble-pair-semifan are not $\Orth(T_\Co)$-invariant (@prop:coble-degree-two-semifan-not-invariant). For the plane model the same question is not decided (@rmk:coble-plane-model-invariance-open).

## The surface and its automorphisms

::: {.notation #not:coble-polarizing-setting title="The surface, its K3 cover and the level-two group" defines="$\bar C$; $S_\Co$; $e_0$; $\Lambda$; $x_A$; $\mathcal C_\Lambda$; level-two group; $\Gamma_2$"}

On this page $S = \Bl_{p_1,\dots,p_{10}}\PP^2$, the classes $H, E_1,\dots,E_{10}$ and the K3 double cover $f\colon X\to S$ are as in @not:coble-ten-point-blowup, where $p_1,\dots,p_{10}$ are the nodes of an irreducible rational plane sextic $B$ [@DK13, §3, arXiv v1 p. 5].
The curve $C\iscontainedin S$ is the proper transform (@def:strict-transform) of $B$. It is the only member of $\abs{-2K_S}$, it is a smooth rational curve, and $C = -2K_S$ in $\Pic(S)$, so $C^2 = -4$ (@def:coble-surface, @prop:canonical-perp-is-e10).
The involution $\sigma$ is the covering involution of $f$, and $\bar C\definedas f^{-1}(C)$ is its fixed curve, a $(-2)$-curve with $f^*C = 2\bar C$ (@prop:coble-k3-cover).
The lattice $S_\Co\definedas f^*\Pic(S)$ is the invariant lattice $H^2(X,\ZZ)^{\sigma}$, it is isometric to $\latI_{1,10}(2)$, and $T_\Co$ is its orthogonal complement in $H^2(X,\ZZ)$ (@prop:coble-invariant-lattice; [@DK13, (3.7), arXiv v1 p. 5]).
Put $e_0\definedas f^*H$.

Put $\Lambda\definedas K_S^{\perp}\iscontainedin\Pic(S)$.
Then $\Pic(S) = \ZZ K_S\perp\Lambda$ and $\Lambda\cong E_{10}$ (@prop:canonical-perp-is-e10 and its proof).
For an ample class $A$ on $S$ put $x_A\definedas A+(A\cdot K_S)K_S$. Then $x_A\cdot K_S = 0$ and $x_A^2 = A^2+(A\cdot K_S)^2>0$, because $K_S^2=-1$.
Let $\mathcal C_\Lambda$ be the connected component of $\theset{x\in\Lambda\tensor\RR\st x^2>0}$ that contains the classes $x_A$. The ample cone (@def:ample-cone) of $S$ is connected, so there is one such component.
The *level-two group* of $\Lambda$ is
$$
\Gamma_2\definedas\theset{g\in\Orth(\Lambda)\st g(\mathcal C_\Lambda)=\mathcal C_\Lambda,\ g(x)-x\in 2\Lambda\ \text{for all } x\in\Lambda}.
$$
:::

::: {.definition #def:picard-general-coble title="Picard-general Coble surface" defines="Picard-general"}

The surface $S$ of @not:coble-polarizing-setting is *Picard-general* if $\Pic(X) = f^*\Pic(S)$.
:::

Picard-general surfaces exist, and their periods are dense.
The periods of the surfaces $X$ fill an open subset of $\bD(T_\Co)/\Orth(T_\Co)$ [@DK13, Prop. 3.2, arXiv v1 p. 5].
The lattice $S_\Co$ is primitive, so $\Pic(X)\neq S_\Co$ exactly when the period of $X$ is orthogonal to a nonzero vector of $T_\Co$, and the periods with that property form a countable union of proper closed analytic subsets of $\bD(T_\Co)$.

::: {.lemma #lem:coble-k3-negative-curves title="Curves of negative square on the K3 cover, and the classes orthogonal to the canonical class"}

Let $S$ be Picard-general (@def:picard-general-coble).

1. An irreducible curve $D\iscontainedin X$ with $D^2<0$ is $\bar C$ or $f^*E$ for a $(-1)$-curve $E\iscontainedin S$.
2. For every $(-1)$-curve $E\iscontainedin S$ and every $x\in\mathcal C_\Lambda$ one has $x\cdot E>0$.
3. For every $x\in\mathcal C_\Lambda$ the class $f^*x$ is nef with $(f^*x)^2>0$, and $\bar C$ is the only irreducible curve $D$ with $f^*x\cdot D = 0$.
4. $S$ has no $(-2)$-curve.
:::

::: {.proof}

(1) By adjunction on the K3 surface $X$, $D^2 = 2p_a(D)-2\ge-2$, so $D$ is a $(-2)$-curve.
Its class lies in $\Pic(X) = f^*\Pic(S)$, on which $\sigma$ acts trivially, so $\sigma(D)$ and $D$ have the same class, $D\cdot\sigma(D) = D^2<0$, and $\sigma(D) = D$.
If $\sigma$ is the identity on $D$ then $D$ lies in the fixed locus of $\sigma$, and $D=\bar C$.
Otherwise put $E\definedas f(D)$. Then $f^{-1}(E) = D\cup\sigma(D) = D$, and $f$ is unramified at the generic point of $D$, so $f^*E = D$ and $2E^2 = (f^*E)^2 = -2$, that is $E^2=-1$.
The curve $E$ is irreducible and is not $C$, so $K_S\cdot E = -\tfrac12 C\cdot E\le0$. Adjunction on $S$ gives $2p_a(E)-2 = -1+K_S\cdot E$, so $K_S\cdot E$ is odd and at least $-1$; hence $K_S\cdot E=-1$ and $p_a(E)=0$. So $E$ is a $(-1)$-curve.

(2) Put $E'\definedas E-K_S$. Then $E'\cdot K_S = -1+1 = 0$, so $E'\in\Lambda$, and $E'^2 = -1+2-1 = 0$. The class $E'$ is not zero, because $E$ is effective and $K_S$ is not.
For $x\in\Lambda\tensor\RR$ one has $x\cdot E = x\cdot E'$.
The lattice $\Lambda$ has signature (@def:signature) $(1,9)$, so no vector of positive square is orthogonal to a nonzero isotropic vector (@def:isotropic-subspace): the form would be positive semidefinite (@def:calculus-real-positivity) on their span, of dimension $2$, and that span would meet a negative definite (@def:definiteness) subspace of dimension $9$.
So $x\mapsto x\cdot E'$ has no zero on the connected set $\mathcal C_\Lambda$.
At $x_A$ its value is $A\cdot E+(A\cdot K_S)(K_S\cdot E) = A\cdot E+\tfrac12A\cdot C>0$.

(3) One has $f^*x\cdot\bar C = x\cdot C = -2x\cdot K_S = 0$ and $f^*x\cdot f^*E = 2x\cdot E>0$ by (2), and $(f^*x)^2 = 2x^2>0$.
The class $f^*A$ is ample and $f^*x_A\cdot f^*A = 2(A^2+(A\cdot K_S)^2)>0$, so $f^*x_A$ lies in the component $\mathcal C_S$ of the positive cone of $\Pic(X)\tensor\RR$ that contains the ample cone (@lem:k3-positive-cone-component); $f^*\mathcal C_\Lambda$ is connected, so it lies in $\mathcal C_S$.
A class of $\mathcal C_S$ that is nonnegative on every $(-2)$-curve is nef [@AE22, §4D, arXiv v2 p. 17], and by (1) the $(-2)$-curves are $\bar C$ and the curves $f^*E$. So $f^*x$ is nef.
If $D$ is irreducible with $f^*x\cdot D=0$, then $D^2<0$ by the Hodge index theorem, and by (1) and the two intersection numbers $D=\bar C$.

(4) Let $G\iscontainedin S$ be a $(-2)$-curve. Then $G\neq C$ and $K_S\cdot G = 0$, so $G\cdot C = 0$ and $f$ is unramified over $G\cong\PP^1$. So $f^{-1}(G)$ is a disjoint union of two curves that $\sigma$ exchanges, each of square $-2$. By the proof of (1) every irreducible curve of negative square on $X$ is preserved by $\sigma$, which is a contradiction.
:::

::: {.lemma #lem:coble-hodge-isometries title="The Hodge isometries of the transcendental lattice"}

Let $S$ be Picard-general (@def:picard-general-coble). Then the group (@def:group) $G_X$ of Hodge isometries of $T_X = T_\Co$ (@not:k3-automorphism-data) is $\theset{\pm\id}$, and $\sigma_*$ acts on $T_X$ as $-\id$.
:::

::: {.proof}

Let $g\in G_X$ and let $\omega$ span $H^{2,0}(X)$.
The isometry $g$ preserves the real plane $(H^{2,0}\oplus H^{0,2})\intersect(T_X\tensor\RR)$, on which the form is positive definite (@def:definiteness), and its orthogonal complement in $T_X\tensor\RR$, on which the form is negative definite (@def:definiteness). So $g$ lies in a compact group and in the discrete group $\Orth(T_X)$, and has finite order.
Let $g\omega = \zeta\omega$, with $\zeta$ a primitive $m$-th root of unity, and let $K\iscontainedin T_X\tensor\QQ$ be the kernel (@def:kernel-cokernel) of $\Phi_m(g)$, for $\Phi_m$ the $m$-th cyclotomic polynomial.
Eigenvectors of an isometry for the eigenvalues $\mu,\mu'$ are orthogonal unless $\mu\mu'=1$, so the sum $K'$ of the kernels of the other cyclotomic factors is orthogonal to $K$ and to $\omega$.
The integral classes of $K'$ are then of type $(1,1)$, so they lie in $\Pic(X)\intersect T_X = 0$.
Hence $K = T_X\tensor\QQ$, the characteristic polynomial of $g$ is a power of $\Phi_m$, and $\varphi(m)$ divides $\rank T_X = 11$.
Since $\varphi(m)$ is even for $m>2$, this gives $m\in\theset{1,2}$ and $g=\pm\id$.

The involution $\sigma_*$ has invariant lattice $S_\Co$ (@prop:coble-invariant-lattice), which meets $T_X$ in $0$. So $\sigma_*$ has no nonzero fixed vector in $T_X$, and it is $-\id$ there.
:::

::: {.proposition #prop:coble-automorphisms title="The automorphism groups of a Picard-general Coble surface and of its K3 cover"}

Let $S$ be Picard-general (@def:picard-general-coble), and identify $\Pic(X)$ with $\Pic(S)(2) = (\ZZ K_S\perp\Lambda)(2)$ through $f^*$.

1. The map $\varphi\mapsto\varphi_*|_{\Pic(X)}$ has kernel (@def:kernel-cokernel) $\theset{\id,\sigma}$, and its image is the group (@def:group) $A_1 = P_S\intersect\widetilde\Orth(\Pic(X))$ of @cor:k3-aut-projection-kernels. So $\Aut(X)\cong A_1\times\generators{\sigma}$.
2. $A_1 = \theset{\id_{\ZZ K_S}\perp g\st g\in\Gamma_2}$.
3. Every automorphism of $X$ commutes (@def:commutative-diagram) with $\sigma$, and $\Aut(S)\cong\Aut(X)/\generators{\sigma}\cong\Gamma_2$. The group $\Aut(S)$ fixes $K_S$ and acts on $\Lambda$ through $\Gamma_2$.
4. $\Gamma_2$ has finite index (@def:index) in $\Orth(\Lambda)$.
:::

For the unnodal Coble surfaces the inclusion $\Aut(S)\supseteq W_{10}(2)$, with $W_{10}(2)$ the subgroup of the Weyl group of $E_{10}$ that acts trivially on $E_{10}/2E_{10}$, is [@CD12, Thm. 3.5, arXiv v2 p. 20], and the equality for a general surface is stated in [@CD12, Remark after the proof of Thm. 3.5, arXiv v2 p. 24]. The proposition does not use them.

::: {.proof}

(1) By @thm:k3-aut-fibre-product, $\varphi\mapsto(\varphi_*|_{\Pic(X)},\varphi_*|_{T_X})$ is an isomorphism from $\Aut(X)$ onto the fibre product $P_S\times_QG_X$.
By @lem:coble-hodge-isometries, $G_X=\theset{\pm\id}$. The group $A_{T_X}$ is $2$-elementary, so $-\id$ acts trivially on it and $b(\pm\id)=1$.
The fibre product is therefore $\ker a\times\theset{\pm\id} = A_1\times\theset{\pm\id}$, and $\sigma$ is the element $(\id,-\id)$ by @lem:coble-hodge-isometries.

(2) *The inclusion $\supseteq$.* Let $g'\in\Gamma_2$ and $g\definedas\id_{\ZZ K_S}\perp g'$.
The dual lattice of $\Pic(X) = \Pic(S)(2)$ is $\tfrac12\Pic(X)$, so $A_{\Pic(X)}\cong\Pic(S)/2\Pic(S)$, and $g$ acts trivially on it. So $g\in\widetilde\Orth(\Pic(X))$.
It remains to show that $g$ preserves $\Amp(X)$.
Let $\Delta$ be the set of classes of square $-2$ in $\Pic(X)$. A *chamber* is a connected component of the complement in $\mathcal C_S$ of the hyperplanes $\delta^{\perp}$, $\delta\in\Delta$, and $\Amp(X)$ is a chamber (@cons:chamber-cone).
For $\delta\in\Delta$ exactly one of $\pm\delta$ is effective, and an effective one is a sum of $(-2)$-curves [@AE22, §4D, arXiv v2 p. 17].

Let $x\in\mathcal C_\Lambda$ and $p\definedas f^*x$.
By @lem:coble-k3-negative-curves(3), $p$ is nef, and an effective class $\delta\in\Delta$ with $\delta\cdot p=0$ is a sum of copies of $\bar C$, so it is $\bar C$.
Only finitely many classes of $\Delta$ are orthogonal to a point of a compact neighbourhood $V$ of $p$ in $\mathcal C_S$: for $y\in V$ the form $N_y(v)\definedas 2(v\cdot y)^2/y^2-v^2$ is positive definite and depends continuously on $y$, and a class $\delta\in\Delta$ with $\delta\cdot y=0$ has $N_y(\delta)=2$, so these classes lie in a bounded subset of the lattice.
So $p$ has a convex open neighbourhood $U_p\iscontainedin\mathcal C_S$ that meets no hyperplane $\delta^{\perp}$, $\delta\in\Delta$, other than $\bar C^{\perp}$.
The half $U_p^+\definedas\theset{y\in U_p\st y\cdot\bar C>0}$ is convex and meets no hyperplane, so it lies in one chamber. For an ample class $A'$ and small $t>0$ the class $p+tA'$ is ample and lies in $U_p^+$. So $U_p^+\iscontainedin\Amp(X)$.

The class $p'\definedas g(p) = f^*(g'x)$ is of the same kind, because $g'x\in\mathcal C_\Lambda$. So $g$ preserves $\mathcal C_S$, it permutes the classes of $\Delta$, and it permutes the chambers.
Since $g$ fixes the class $\bar C = -f^*K_S$, the set $g(U_p^+)$ consists of classes that are positive on $\bar C$, and it contains points of $U_{p'}$; so it meets $U_{p'}^+\iscontainedin\Amp(X)$.
The chamber $g(\Amp(X))$ contains $g(U_p^+)$, so it meets $\Amp(X)$, and $g(\Amp(X))=\Amp(X)$, that is $g\in P_S$.

*The inclusion $\iscontainedin$.* Let $s\in A_1$, and let $\varphi\in\Aut(X)$ be the automorphism with $\varphi_* = s\perp\id_{T_X}$.
Then $\varphi_*$ commutes with $\sigma_*$, so $\varphi$ commutes with $\sigma$ by (1), and $\varphi$ preserves the fixed curve $\bar C$.
So $s$ fixes $f^*K_S = -\bar C$, and $s = \id_{\ZZ K_S}\perp s'$ with $s'\in\Orth(\Lambda)$.
The group $P_S$ preserves $\mathcal C_S$ (@lem:k3-positive-cone-component), and $f^*\mathcal C_\Lambda$ is the set of classes of $\mathcal C_S$ orthogonal to $\bar C$; so $s'(\mathcal C_\Lambda)=\mathcal C_\Lambda$.
Since $s$ acts trivially on $\Pic(S)/2\Pic(S)$ and $\Lambda$ is a direct summand of $\Pic(S)$, $s'$ acts trivially on $\Lambda/2\Lambda$. So $s'\in\Gamma_2$.

(3) By (1) the element $\sigma_*$ is central, and $\varphi\mapsto\varphi_*$ is injective, so every $\varphi\in\Aut(X)$ commutes with $\sigma$ and descends to $S = X/\sigma$. An automorphism of $X$ over $S$ is $\id$ or $\sigma$.
An automorphism $\psi$ of $S$ preserves $C$, the only member of $\abs{-2K_S}$. The cover $f$ is defined by the line bundle $\OO_S(-K_S)$ and a section of its square with zero locus $C$ (@prop:coble-k3-cover), and $\psi$ carries these data to themselves up to a scalar on the section; so $\psi$ lifts to $X$.
Hence $\Aut(S)\cong\Aut(X)/\generators{\sigma}\cong A_1$, and the action on $\Pic(S)$ is the one in (2), because $f^*\psi_* = \varphi_*f^*$ for a lift $\varphi$ of $\psi$.

(4) The kernel of $\Orth(\Lambda)\to\mathrm{GL}(\Lambda/2\Lambda)$ has finite index, and the subgroup of $\Orth(\Lambda)$ that preserves $\mathcal C_\Lambda$ has index $2$. $\Gamma_2$ is their intersection.
:::

::: {.lemma #lem:finite-index-no-finite-orbit title="A subgroup of finite index has no nonzero vector with a finite orbit"}

Let $G\iscontainedin\Orth(\Lambda)$ be a subgroup of finite index (@def:index), and let $v\in\Lambda\tensor\QQ$ have a finite $G$-orbit. Then $v=0$.
:::

::: {.proof}

The stabilizer (@def:group-orbit) of $v$ in $G$ has finite index in $\Orth(\Lambda)$, so it is enough to treat a vector $v$ that $G$ fixes.
Let $e\in\Lambda$ be isotropic (@def:orthogonal-complement) and $a\in\Lambda$ with $a\cdot e=0$. The Eichler--Siegel transvection $E_{e,a}$ of @def:eichler-siegel maps $\Lambda$ to itself, because $\Lambda$ is even (@def:form-axioms), and a substitution in its formula gives $E_{e,a}E_{e,b} = E_{e,a+b}$ for $a,b$ orthogonal to $e$.
So the elements $E_{e,ka}$, $k\in\ZZ$, form a cyclic subgroup, and $E_{e,Na}\in G$ for some $N\ge1$.
Then
$$
0 = E_{e,Na}(v)-v = N(e\cdot v)\,a-\bigl(N(a\cdot v)+\tfrac12N^2a^2(e\cdot v)\bigr)e.
$$
For $a$ not proportional to $e$ this gives $e\cdot v=0$ and then $a\cdot v=0$.
The vectors $a\in e^{\perp}$ not proportional to $e$ span $e^{\perp}$, so $v$ is orthogonal to $e^{\perp}$, that is $v\in\QQ e$.
The lattice $\Lambda\cong U\oplus E_8$ has two isotropic vectors (@def:isotropic-subspace) that are not proportional. So $v=0$.
:::

## No polarizing divisor on the unpolarized surfaces

::: {.theorem #thm:coble-invariant-classes title="The classes with a finite orbit are the multiples of the canonical class"}

Let $S$ be Picard-general (@def:picard-general-coble).

1. If the $\Aut(S)$-orbit of $L\in\Pic(S)\tensor\QQ$ is finite, then $L\in\QQ K_S$.
2. If the $\Aut(X)$-orbit of $L\in\Pic(X)\tensor\QQ$ is finite, then $L\in\QQ\bar C$.

In particular $(\Pic(S)\tensor\QQ)^{\Aut(S)} = \QQ K_S$ and $(\Pic(X)\tensor\QQ)^{\Aut(X)} = \QQ\bar C$.
:::

::: {.proof}

Write $L = aK_S+L'$ with $L'\in\Lambda\tensor\QQ$.
By @prop:coble-automorphisms(3), $\Aut(S)$ fixes $K_S$ and acts on $\Lambda$ through $\Gamma_2$, so the $\Gamma_2$-orbit of $L'$ is finite.
By @prop:coble-automorphisms(4) and @lem:finite-index-no-finite-orbit, $L'=0$.
For (2), $\Pic(X)\tensor\QQ = f^*\Pic(S)\tensor\QQ$, the group (@def:group) $\Aut(X)$ acts on it through $A_1$ (@prop:coble-automorphisms(1) and (2)), and $f^*K_S = -\bar C$.
:::

::: {.corollary #cor:coble-no-canonical-polarization title="No invariant big class, and the invariant effective divisors"}

Let $S$ be Picard-general (@def:picard-general-coble).

1. A line bundle on $S$ whose class is $\Aut(S)$-invariant is $\OO_S(aK_S)$, and $h^0(S,\OO_S(aK_S))\le1$ for every $a\in\ZZ$. So no such line bundle is big.
2. An effective divisor on $S$ that $\Aut(S)$ preserves is $mC$ with $m\ge0$.
3. A line bundle on $X$ whose class is $\Aut(X)$-invariant is $\OO_X(a\bar C)$. It is not big, and it is nef only for $a=0$. An effective divisor on $X$ that $\Aut(X)$ preserves is $m\bar C$ with $m\ge0$.
:::

::: {.proof}

(1) The class is $aK_S$ by @thm:coble-invariant-classes, and $K_S$ is primitive (@def:primitive-embedding) in $\Pic(S)$.
For $a>0$, $h^0(aK_S)=0$ on the rational surface $S$.
Let $a=-m<0$ and $D\in\abs{-mK_S}$. Then $D\cdot C = 2mK_S^2 = -2m<0$, so $C$ is a component of $D$ and $D-C\in\abs{-(m-2)K_S}$.
By induction, $\abs{-mK_S}=\theset{\tfrac m2C}$ for even $m$, and $\abs{-mK_S}$ is empty for odd $m$ because $\abs{-K_S}$ is empty.

(2) The class of the divisor is $-mK_S$ with $m\ge0$ by @thm:coble-invariant-classes, and (1) gives the divisor.

(3) The class is $a\bar C$ by @thm:coble-invariant-classes. The curve $\bar C$ is a $(-2)$-curve, so $h^0(a\bar C)\le1$ for all $a$, $\abs{m\bar C}=\theset{m\bar C}$ for $m\ge0$, and $a\bar C\cdot\bar C=-2a$, which is negative for $a>0$; for $a<0$ the class $a\bar C$ is negative on an ample class.
:::

::: {.remark #rmk:coble-canonical-means-invariant title="A canonical choice is invariant under automorphisms"}

A canonical choice of polarizing divisor is a section of a bundle over the moduli stack [@AE23, Def. 6.1, arXiv v3 p. 16], and where the stack has generic inertia the divisor "must be preserved" by it [@AE23, Rem. 6.10, arXiv v3 p. 17]; in [@AEH24, Def. 3.3 and Def. 3.4, arXiv v2 p. 8] it is a divisor in every flat family of K3 surfaces with automorphism.
For the K3 surfaces with an involution of type $(11,11,1)$ the coarse space of that stack is an open subset of $\bD(T_\Co)/\Orth(T_\Co)$ [@AE22, §2C, arXiv v2 p. 7], and the inertia group of the surface $(X,\sigma)$ is $\Aut(X,\sigma)$, which is $\Aut(X)$ for a Picard-general surface (@prop:coble-automorphisms(3)).
So a canonical choice on an open subset of that moduli space gives, on every Picard-general surface in it, an $\Aut(X)$-invariant big and nef divisor. By @cor:coble-no-canonical-polarization(3) there is none.
The fixed curve $\bar C$ is the one canonical effective divisor, and it fails the ampleness condition, which is @thm:coble-n-recognizable-verdict.

The following shorter argument reaches the same conclusion from three statements, and each of the three holds.
A canonical divisor is invariant under $\Aut(X,\sigma)$.
The automorphisms of a K3 surface that preserve a big and nef line bundle form a finite group; this is the step used in [@AEH24, Prop. 2.12 and its proof, arXiv v2 p. 6].
The general K3 surface of type $(11,11,1)$ has an infinite automorphism group: of the $75$ families, $51$ satisfy the genus assumption, and the only other family with $\abs{\Aut(X)}<\infty$ is $(g,k,\delta)=(1,9,1)$ [@AEH24, §1, arXiv v2 p. 2], while $(11,11,1)$ has $g=k=0$ (@prop:nikulin-fixed-locus); here it is @prop:coble-automorphisms(4).
@thm:coble-invariant-classes is sharper: it names the invariant classes, and it excludes a finite set of big classes that the automorphisms permute.
The same finiteness holds for stable pairs, whose automorphism groups are finite [@AE23, §6B, arXiv v3 p. 17].
:::

::: {.theorem #thm:coble-polarized-family title="A polarized family has a period map of degree divisible by $527$"}

Let $g\colon\mathcal X\to B$ be a smooth proper family of K3 surfaces over a connected complex manifold, with an involution $\sigma_B$ of $\mathcal X$ over $B$, such that every fibre $(X_b,\sigma_b)$ is the K3 cover of a Coble surface as in @not:coble-polarizing-setting.
Suppose that $\mathcal X$ has a line bundle that is big and nef on every fibre.
Then the period map (@def:period-map) $p\colon B\to\bD(T_\Co)/\Orth(T_\Co)$ factors through $\bD(T_\Co)/\Gamma'$ for a subgroup $\Gamma'\iscontainedin\Orth(T_\Co)$ that contains the discriminant kernel (@def:mm-integral-spinor-data) and whose index (@def:index) is divisible by $17\cdot31=527$.
In particular $p$ is not birational, and if $p$ is generically finite and dominant its degree (@def:graded-object) is divisible by $527$.
:::

::: {.proof}

Let $M$ be the line bundle. The class $\lambda\definedas c_1(M)+\sigma_B^*c_1(M)$ is a section of $R^2g_*\ZZ$ that is $\sigma_B$-invariant, and $\lambda_b^2>0$, because $\lambda_b$ is a sum of two big and nef classes (@def:nef-cone).
Fix $b\in B$, put $S_b\definedas H^2(X_b,\ZZ)^{\sigma_b}\cong S_\Co$ and $T_b\definedas S_b^{\perp}\cong T_\Co$, and let $\mu$ be the monodromy representation (@def:transport-and-monodromy) of $\pi_1(B,b)$ on $H^2(X_b,\ZZ)$.
It commutes (@def:commutative-diagram) with $\sigma_b^*$, so it preserves $S_b$ and $T_b$; write $\mu_S$ and $\mu_T$ for the two restrictions.
By @cor:lifting-unimodular the discriminant actions of $\mu_S(c)$ and $\mu_T(c)$ correspond under the gluing isometry $\gamma_q$, for every $c$.

The group (@def:group) $\mu_S(\pi_1(B,b))$ fixes $\lambda_b$, so it lies in $F\definedas\Stab_{\Orth(S_b)}(\lambda_b)$.
The lattice $S_b$ has signature $(1,10)$ and $\lambda_b^2>0$, so $F$ acts faithfully on the negative definite (@def:definiteness) lattice $\lambda_b^{\perp}\intersect S_b$, and $F$ is finite.
An element of prime order $\ell$ of $\mathrm{GL}_{11}(\ZZ)$ has a primitive $\ell$-th root of unity among its eigenvalues, so $\ell-1\le11$. So $F$ has no element of order $17$ or $31$, and $\abs F$ is prime to $17\cdot31$.
Let $\bar F$ be the image of $F$ in $\Orth(q_{S_b})$ and $\Gamma'\iscontainedin\Orth(T_b)$ the preimage of $\gamma_q\bar F\gamma_q^{-1}$ under $\rho\colon\Orth(T_b)\to\Orth(q_{T_b})$.
Then $\mu_T(\pi_1(B,b))\iscontainedin\Gamma'$ and $\ker\rho\iscontainedin\Gamma'$.
The map $\rho$ is surjective (@thm:two-elementary-surjectivity) and $\abs{\Orth(q_{T_\Co})} = 2^{21}\cdot3^5\cdot5^2\cdot7\cdot17\cdot31$ (@prop:coble-discriminant-group), so $[\Orth(T_b):\Gamma'] = \abs{\Orth(q_{T_b})}/\abs{\bar F}$ is divisible by $17\cdot31$.

On the universal cover of $B$ the local system $R^2g_*\ZZ$ is trivial, and the period map lifts to a map to $\bD(T_b)$ that is equivariant for $\mu_T$. So $p$ factors through $\bD(T_b)/\mu_T(\pi_1(B,b))$, and hence through $\bD(T_b)/\Gamma'$.
Both $\Gamma'$ and $\Orth(T_b)$ contain $-\id$, and $\Orth(T_b)/\theset{\pm\id}$ acts effectively on $\bD(T_b)$, so $\bD(T_b)/\Gamma'\to\bD(T_b)/\Orth(T_b)$ has degree $[\Orth(T_b):\Gamma']$.
:::

## Polarizations as added structures

Fix a primitive embedding $S_\Co\iscontainedin\lkt$ with orthogonal complement $T_\Co$, let $\rho\colon\Orth(T_\Co)\to\Orth(q_{T_\Co})$ be the discriminant representation, and let $a$ and $b$ be the maps of @not:k3-automorphism-data for the pair $(S_\Co,T_\Co)$: $a(s)$ is the discriminant action of $s\in\Orth(S_\Co)$, and $b(t)$ is the discriminant action of $t\in\Orth(T_\Co)$ transported to $A_{S_\Co}$ by the gluing isometry.

::: {.proposition #prop:coble-polarized-moduli title="The moduli space of Coble surfaces with a polarization of a fixed type"}

Let $\lambda\in S_\Co$ with $\lambda^2>0$, and put
$$
\Gamma_\lambda\definedas\theset{\gamma|_{T_\Co}\st\gamma\in\Orth(\lkt),\ \gamma(S_\Co)=S_\Co,\ \gamma(\lambda)=\lambda}.
$$
A pair $(S,\ell)$ of a Coble surface and a nef class (@def:nef-cone) $\ell\in\Pic(S)$ is *of type $\lambda$* if there is an isometry $\phi\colon H^2(X,\ZZ)\to\lkt$ with $\phi(f^*\Pic(S))=S_\Co$ and $\phi(f^*\ell)=\lambda$.

1. $\Gamma_\lambda = b^{-1}\bigl(a(\Stab_{\Orth(S_\Co)}(\lambda))\bigr)$. It contains $\ker\rho$, the group (@def:group) $\Stab_{\Orth(S_\Co)}(\lambda)$ is finite, and
$$
[\Orth(T_\Co):\Gamma_\lambda] = \frac{\abs{\Orth(q_{T_\Co})}}{\abs{a(\Stab_{\Orth(S_\Co)}(\lambda))}},
$$
which is divisible by $527$.
2. The period $\phi_\CC(H^{2,0}(X))$ of a pair of type $\lambda$ is well defined in $\bD(T_\Co)/\Gamma_\lambda$, and two pairs of type $\lambda$ with Picard-general (@def:picard-general-coble) surfaces are isomorphic if and only if their periods in $\bD(T_\Co)/\Gamma_\lambda$ are equal.
3. On a Picard-general surface $S$ whose K3 cover has a marking $\phi$ with $\phi(f^*\Pic(S))=S_\Co$, the nef classes $\ell$ with $(S,\ell)$ of type $\lambda$ form $[\Orth(T_\Co):\Gamma_\lambda]$ orbits (@def:group-orbit) of $\Aut(S)$, each of them infinite.
:::

::: {.proof}

(1) By @cor:lifting-unimodular, $s\perp t$ extends to $\lkt$ exactly when $a(s)=b(t)$, which is the first formula; it gives $\ker\rho=\ker b\iscontainedin\Gamma_\lambda$.
The stabilizer (@def:group-orbit) is finite, and the order of its image is prime to $17\cdot31$, by the argument of the proof of @thm:coble-polarized-family.
The map $b$ is surjective by @thm:two-elementary-surjectivity, which gives the index (@def:index), and the order of $\Orth(q_{T_\Co})$ is in @prop:coble-discriminant-group.

(2) Two markings as in the definition differ by an isometry of $\lkt$ that preserves $S_\Co$ and fixes $\lambda$, so the period is well defined modulo $\Gamma_\lambda$, and isomorphic pairs have the same period.
Conversely let $(S,\ell)$ and $(S',\ell')$ have markings $\phi,\phi'$ with the same period. Then $\psi\definedas\phi'^{-1}\phi$ is a Hodge isometry from $H^2(X,\ZZ)$ to $H^2(X',\ZZ)$ with $\psi(f^*\ell)=f'^*\ell'$ and $\psi(\Pic(X))=\Pic(X')$.
The classes $f^*\ell$ and $f'^*\ell'$ are nef of positive square, so $\psi$ carries the positive cone of $X$ to that of $X'$, and there is a unique $w$ in the group generated by the reflections in the $(-2)$-classes of $\Pic(X')$ such that $w\psi$ carries the Kähler cone (@def:closed-cone) of $X$ to that of $X'$ [@AE23, §2A, arXiv v3 p. 5].
Then $w\psi = \varphi_*$ for an isomorphism (@def:isomorphism-of-objects) $\varphi\colon X\to X'$ [@AE23, Thm. 2.3, arXiv v3 p. 5].
The classes $f'^*\ell'$ and $w(f'^*\ell')=\varphi_*(f^*\ell)$ are both nef, and the closure of $\Amp(X')$ is a fundamental domain (@def:fundamental-domain) for that reflection group (@def:reflection-group) [@PS24, Proposition 19.1.3(2)], so they are equal.
The isometry $\varphi_*$ carries $\sigma_*$, which is $\id\perp-\id$ on $\Pic(X)\perp T_X$ (@lem:coble-hodge-isometries), to $\sigma'_*$; so $\varphi$ commutes (@def:commutative-diagram) with the involutions, it descends to an isomorphism $S\to S'$, and that isomorphism carries $\ell$ to $\ell'$.

(3) Let $x\in\bD(T_\Co)$ be the period of $(X,\phi)$ and $t\in\Orth(T_\Co)$. The map $a$ is surjective (@thm:two-elementary-surjectivity), so $t$ extends to an isometry $\gamma$ of $\lkt$ that preserves $S_\Co$, and $\gamma\phi$ is a marking with period $tx$. The class $\phi^{-1}\gamma^{-1}(\lambda)$ lies in $\Pic(X)$ and has positive square; a product $w$ of reflections in $(-2)$-classes and of $\pm\id_{\Pic(X)}$ carries it to a nef class $f^*\ell$, and $\gamma\phi w^{-1}$ is a marking of $(S,\ell)$ with period $tx$, because $w$ acts trivially on the discriminant group and extends by the identity of $T_X$ or by $-\id$.
So every point of the fibre of $\bD(T_\Co)/\Gamma_\lambda\to\bD(T_\Co)/\Orth(T_\Co)$ over the class of $x$ is the period of a pair $(S,\ell)$, and by (2) the fibre is the set of $\Aut(S)$-orbits of such classes. Its cardinality is the index, the stabilizers in $\Orth(T_\Co)/\theset{\pm\id}$ of a Picard-general period being trivial by @lem:coble-hodge-isometries.
An orbit is infinite because the stabilizer of $\ell$ in $\Aut(S)$ is finite, as in (1), and $\Aut(S)$ is infinite (@prop:coble-automorphisms).
:::

::: {.proposition #prop:coble-plane-model-space title="The plane model"}

Let $\lambda = e_0 = f^*H$, of square $2$, and write $\Gamma_P\definedas\Gamma_{e_0}$.

1. $\Stab_{\Orth(S_\Co)}(e_0)$ is the group (@def:group) of signed permutations of $f^*E_1,\dots,f^*E_{10}$, its image under $a$ is the symmetric group $S_{10}$, and
$$
[\Orth(T_\Co):\Gamma_P] = \frac{2^{21}\cdot3^5\cdot5^2\cdot7\cdot17\cdot31}{10!} = 2^{13}\cdot3\cdot17\cdot31 = 12\,951\,552 .
$$
2. Let $F_2 = \bD(e_0^{\perp})/\theset{\gamma\in\Orth(\lkt)\st\gamma(e_0)=e_0}$ be the moduli space of polarized K3 surfaces of degree (@def:graded-object) $2$ [@AE23, Thm. 2.11, arXiv v3 p. 6]. The map $\bD(T_\Co)/\Gamma_P\to F_2$ is finite onto a closed subset (@def:closed-subset) $Z_P$ and injective (@def:injective-map) on the Picard-general (@def:picard-general-coble) periods. The general point of $Z_P$ is the double plane branched along an irreducible rational sextic with ten nodes.
3. $\bD(T_\Co)/\Gamma_P$ has exactly five $0$-cusps. In the basis (@def:based-module) $[\tfrac12e_0],[\tfrac12f^*E_1],\dots,[\tfrac12f^*E_{10}]$ of $A_{S_\Co}$ they are the $S_{10}$-orbits of the nonzero isotropic classes (@def:descent-class) $\sum_ka_k[\,\cdot\,]$, $a_k\in\theset{0,1}$, namely those with $a_0=0$ and $4$ or $8$ further coordinates equal to $1$, and those with $a_0=1$ and $1$, $5$ or $9$ further coordinates equal to $1$; the orbits (@def:group-orbit) have $210$, $45$, $10$, $252$ and $10$ elements.
:::

That $Z_P$ is an algebraic subvariety of $F_2$, and that $\bD(T_\Co)/\Gamma_P$ is its normalization, is the statement used for the Enriques locus in [@AEGS25, Lemma 2.8, arXiv v2 p. 6] and for the Heegner divisor in @thm:normalization; the proof below gives the analytic statement and does not prove algebraicity.

::: {.proof}

(1) An isometry of $S_\Co\cong\latI_{1,10}(2)$ that fixes $e_0$ is an isometry of $e_0^{\perp}\cong\generators{-2}^{10}$, and those are the signed permutations of the ten basis vectors; each of them extends by $e_0\mapsto e_0$.
A signed permutation acts on $A_{S_\Co}\cong\Pic(S)/2\Pic(S)$ by the underlying permutation of the classes of the $E_i$. So the image has order $10!=2^8\cdot3^4\cdot5^2\cdot7$, and @prop:coble-polarized-moduli(1) gives the index.

(2) An isometry of $\lkt$ preserves $S_\Co$ exactly when it preserves $T_\Co$, so $\Gamma_P$ is the image of the stabilizer of $T_\Co$ in the group of $F_2$, and the map is defined.
Put $N\definedas S_\Co\intersect e_0^{\perp}\cong\generators{-2}^{10}$.
A translate of $\bD(T_\Co)$ by an element $\gamma$ of the group of $F_2$ is $\bD(N'^{\perp})$ for $N'=\gamma(N)$, and $N'$ is spanned by ten vectors of square $-2$ that are orthogonal to every period of the translate.
For a compact set $K$ of periods, the vectors of square $-2$ of $e_0^{\perp}$ that are orthogonal to a point of $K$ are finitely many: such a vector $v$ is orthogonal to the positive definite plane $P_x$ spanned by the real and imaginary parts of the period $x$, the form $-v^2+2\abs{\operatorname{pr}_{P_x}v}^2$ is positive definite and continuous in $x$, and it takes the value $2$ at $v$.
So only finitely many translates meet $K$, the union of the translates is a closed analytic subset, and the map from $\bD(T_\Co)/\Gamma_P$ onto its image $Z_P$ is proper with finite fibres: the elements $\gamma$ with a given $\gamma(N)$ form one coset of the stabilizer of $T_\Co$.
If $x$ and $\gamma x$ are Picard-general periods in $\bD(T_\Co)$, then $\gamma$ carries $x^{\perp}\intersect\lkt=S_\Co$ to $(\gamma x)^{\perp}\intersect\lkt=S_\Co$, so $\gamma|_{T_\Co}\in\Gamma_P$.
The general point is the pair $(X,e_0)$ of @not:coble-polarizing-setting: the linear system $\abs{e_0}$ is the composite of $f$ with the blowdown $S\to\PP^2$, a double cover of $\PP^2$ branched along $B$ [@DK13, §3, arXiv v1 p. 5].

(3) $\Gamma_P$ contains $\ker\rho$, so by @thm:cusp-lifting(1) its orbits of primitive isotropic vectors correspond to the orbits of $\rho(\Gamma_P)$ on the nonzero isotropic classes of $A_{T_\Co}$, and by @prop:coble-polarized-moduli(1) and (1) these are the orbits of $S_{10}$ on the nonzero isotropic classes of $A_{S_\Co}$, the gluing isometry preserving isotropy.
The class with coordinates $a_k$ has $q$-value $\tfrac12\bigl(a_0-\sum_{i\ge1}a_i\bigr)$ modulo $2$, because $(\tfrac12e_0)^2=\tfrac12$ and $(\tfrac12f^*E_i)^2=-\tfrac12$. It is isotropic exactly when $a_0-\sum_{i\ge1}a_i$ is divisible by $4$, which gives the five orbits, and $\binom{10}4+\binom{10}8+\binom{10}1+\binom{10}5+\binom{10}9 = 527$, the number of nonzero isotropic classes (@thm:coble-zero-cusp-count(1)).
:::

::: {.proposition #prop:coble-degree-two-space title="The numerical polarization of degree $2$"}

Let $h = F_1+F_2\in\mathcal C_\Lambda$ with $F_1,F_2\in\Lambda$, $F_i^2=0$ and $F_1\cdot F_2=1$, a degree-$2$ numerical polarization (@def:coble-polarization-classes(2)), and $\lambda=\tilde h=f^*h$, of square $4$.
Take the embedding $S_\Co\iscontainedin\lkt$ and the vector $\delta$ of @def:gamma-co-groups, so that $\delta$ is the class of $\bar C$, $S_\En = \delta^{\perp}\intersect S_\Co = f^*\Lambda$ and $T_\Co=\delta^{\perp}\intersect T_\En$, with $\tilde h$ the polarization vector (@def:polarization-vector) of [@AEGS25, Def. 2.5, arXiv v2 p. 6].

1. On a Picard-general (@def:picard-general-coble) surface $h$ is nef and big, and $C$ is the only irreducible curve on which it is zero.
2. $\Gamma_{\tilde h} = R_{\gent}$, the restricted stabilizer (@def:group-orbit) of @def:gamma-co-groups(4). Its index in $\Orth(T_\Co)$ is $2^7\cdot17\cdot31 = 67\,456$, and $\bD(T_\Co)/R_{\gent}$ is the normalization of the Heegner divisor $\mch_{-2}/\gent$ of $\fentwo$ (@prop:gamma-co-images(3), @thm:normalization).
3. On a Picard-general surface the degree-$2$ numerical polarizations form $67\,456$ orbits (@def:group-orbit) of $\Aut(S)$.
:::

::: {.proof}

(1) is @lem:coble-k3-negative-curves(3), with the remark that an irreducible curve $G\iscontainedin S$ with $h\cdot G=0$ has $f^*h\cdot f^*G=0$.

(2) The group (@def:group) $\gent$ is the image in $\Orth(T_\En)$ of the isometries of $\lkt$ that commute with $I_\En$ and fix $\tilde h$, and $I_\En$ is $\id$ on $S_\En$ and $-\id$ on $T_\En$ [@AEGS25, Def. 2.3 and Def. 2.6, arXiv v2 pp. 5--6].
Let $\gamma\in\Orth(\lkt)$ preserve $S_\Co$ and fix $\tilde h$.
The orthogonal complement of $\tilde h$ in $S_\Co\cong(\ZZ K_S\perp\Lambda)(2)$ is isometric to $(\generators{-1}\perp\generators{-2}\perp E_8)(2)$, whose only vectors of square $-2$ are $\pm\delta$; so $\gamma(\delta)=\pm\delta$.
The reflection $s_\delta$ preserves $S_\Co$, fixes $\tilde h$ and acts trivially on $T_\Co$, so after composing with it $\gamma(\delta)=\delta$.
Then $\gamma$ preserves $S_\En$ and $T_\En$, commutes (@def:commutative-diagram) with $I_\En$, and its restriction to $T_\En$ is an element of $\gent$ that fixes $\delta$. So $\gamma|_{T_\Co}\in R_{\gent}$.
Conversely an element of $\Stab_{\gent}(\delta)$ is the restriction of an isometry $\gamma$ of $\lkt$ that commutes with $I_\En$ and fixes $\tilde h$; it preserves $T_\Co=\delta^{\perp}\intersect T_\En$, hence $S_\Co$, so its restriction to $T_\Co$ lies in $\Gamma_{\tilde h}$.
The index and the normalization are the cited statements.

(3) is @prop:coble-polarized-moduli(3). Every degree-$2$ numerical polarization $h' = F_1'+F_2'\in\mathcal C_\Lambda$ is nef by (1) and is of type $\tilde h$: the sublattice $\generators{F_1',F_2'}\cong U$ is unimodular, so $\Lambda$ is the orthogonal sum (@def:orthogonal-sum) of it and of an even unimodular negative definite (@def:definiteness) lattice of rank $8$, which is $E_8$, as in the proof of [@AEGS25, Lemma 2.4, arXiv v2 p. 6]. So an isometry $u$ of $\Lambda$ carries $F_i'$ to $F_i$; it preserves $\mathcal C_\Lambda$ because $h',h\in\mathcal C_\Lambda$, and $\id_{\ZZ K_S}\perp u$ extends to an isometry of $\lkt$ that preserves $S_\Co$, because $b$ is surjective.
:::

::: {.remark #rmk:coble-half-pencil title="A half-pencil alone is not a polarization"}

A primitive isotropic class $F\in\Lambda$ in the closure of $\mathcal C_\Lambda$ has an infinite stabilizer in $\Aut(S)$ for $S$ Picard-general: the transvections $E_{F,2a}$ of @def:eichler-siegel, with $a\in\Lambda$ orthogonal to $F$, fix $F$, act trivially on $\Lambda/2\Lambda$, and preserve $\mathcal C_\Lambda$ because they fix the boundary class $F$; so they lie in $\Gamma_2$, and for $a$ not proportional to $F$ they have infinite order.
The stabilizer of a class of positive square is finite (@prop:coble-polarized-moduli(1)). So no nef and big class is determined by the pair $(S,F)$, and the elliptic fibration $\abs{2F}$ needs a further choice before it gives a polarization. A second half-pencil $F'$ with $F\cdot F'=1$ gives the degree-$2$ polarization $F+F'$.
:::

## The two compactifications

::: {.lemma #lem:coble-hyperplane-class-nef title="The hyperplane class is nef on every $S_\Co$-quasipolarized surface"}

Let $\varepsilon_1,\dots,\varepsilon_{10}>0$ with $\sum_i\varepsilon_i^2<\tfrac15$, and $h_\varepsilon\definedas e_0-\sum_i\varepsilon_if^*E_i\in S_\Co\tensor\RR$.
Let $X'$ be a K3 surface and $j\colon S_\Co\to\NS(X')$ a primitive embedding (@def:primitive-embedding) with $j(h_\varepsilon)$ big and nef.
Then $j(e_0)$ is big and nef.
:::

::: {.proof}

Suppose a $(-2)$-curve $D$ has $D\cdot j(e_0)<0$, and let $v=c_0e_0+\sum_ic_if^*E_i$ be the orthogonal projection of $D$ to $j(S_\Co)\tensor\QQ$, written without $j$. Then $D\cdot e_0=2c_0$ and $D\cdot f^*E_i=-2c_i$, so $c_0\le-\tfrac12$.
The orthogonal complement of $j(S_\Co)$ in $\NS(X')$ is negative definite (@def:definiteness), so $v^2\ge D^2=-2$, that is $\sum_ic_i^2\le c_0^2+1\le5c_0^2$.
Since $j(h_\varepsilon)$ is nef, $0\le D\cdot h_\varepsilon = 2c_0+2\sum_i\varepsilon_ic_i$, so $\abs{c_0}\le\sum_i\varepsilon_ic_i\le\bigl(\sum_i\varepsilon_i^2\bigr)^{1/2}\sqrt5\,\abs{c_0}<\abs{c_0}$, which is a contradiction.
So $j(e_0)$ is nonnegative on every $(-2)$-curve, it has square $2$ and $j(e_0)\cdot j(h_\varepsilon)=2>0$, and it is nef and big.
:::

::: {.theorem #thm:coble-plane-model-compactification title="The compactification by the plane model"}

Let $\oF_2^R$ be the KSBA compactification of $F_2$ for the ramification divisor (@thm:degree-two-k3-semifan), and let $Z_P\iscontainedin F_2$ be as in @prop:coble-plane-model-space.

1. For a Picard-general (@def:picard-general-coble) surface, let $X\to\bar X$ be the contraction of the ten curves $f^*E_i$ and $\bar R\iscontainedin\bar X$ the image of $\bar C$. Then $\bar X$ is the double plane branched along $B$, $\bar R$ is the ramification divisor of $\bar X\to\PP^2$, its pullback to $X$ is $\bar C+\sum_if^*E_i\in\abs{3e_0}$, and $(\bar X,\eps\bar R)$ is the pair that $\oF_2^R$ assigns to $(X,e_0)$. It is KSBA-stable, and so is the pair $\bigl(\PP^2,\tfrac{1+\eps}2B\bigr)$.
2. The closure $\bar Z_P$ of $Z_P$ in $\oF_2^R$ is a closed subset (@def:closed-subset) of a projective variety (@def:projective-variety) whose points are KSBA-stable pairs, and $Z_P$ is open and dense in it.
:::

::: {.proof}

(1) The linear system $\abs{e_0}$ gives the double cover of $\PP^2$ branched along $B$, which factors through the contraction of the curves on which $e_0$ is zero. By @lem:coble-k3-negative-curves(1) such a curve is $\bar C$ or $f^*E$, and $e_0\cdot\bar C = H\cdot C = 6$, while $e_0\cdot f^*E = 2H\cdot E$ is zero exactly for the ten curves $E_i$ that $S\to\PP^2$ contracts. The covering involution of the double plane lifts to $\sigma$, whose fixed curve is $\bar C$, so the ramification divisor is the image of $\bar C$.
From $C = 6H-2\sum_iE_i$ one gets $3e_0 = f^*(\tfrac12C+\sum_iE_i) = \bar C+\sum_if^*E_i$.
The divisor on $(X,e_0)$ is the pullback of the ramification locus [@AE23, Ex. 9.20, arXiv v3 p. 33; @AET23, Thm. 1.2 and the paragraph before it, arXiv v3 p. 3].
A K3 surface with ADE singularities and an effective ample divisor gives a stable pair [@AEH24, §3A, arXiv v2 p. 7], and $(X,\eps R)$ is stable exactly when the branch pair is (@ex:degree-two-k3-branch-pair).

(2) $\oF_2^R$ is projective and its points are stable pairs [@AE23, Thm. 6.13, arXiv v3 p. 17], and it contains $F_2$ as an open subset because the ramification divisor is recognizable [@AE23, Prop. 6.12 and Ex. 9.20, arXiv v3 pp. 17, 33]. So $Z_P=\bar Z_P\intersect F_2$ is open in $\bar Z_P$.
:::

::: {.remark #rmk:coble-plane-model-semitoroidal title="The published restriction statement, with its hypotheses checked"}

[@AE23, Prop. 9.4, arXiv v3 p. 30] reads: for primitive hyperbolic sublattices $M\iscontainedin M'\iscontainedin\lkt$ and $L\in M$, if $R\in\abs L$ is recognizable for the stack of $M$-quasipolarized surfaces, then its restriction to the stack of $M'$-quasipolarized surfaces is recognizable, and the semifan for $M'$ is the restriction of the semifan for $M$ to the subspaces $\delta^{\perp}_{M'^{\perp}}/\delta$.
With [@AE23, Thm. 9.1, arXiv v3 p. 29] it gives a semitoroidal normalization.
For the plane model the hypotheses are these.

- $M=\ZZ e_0$ and $M'=S_\Co$ are primitive hyperbolic sublattices of $\lkt$, of ranks $1$ and $11$, and $L=3e_0\in M$.
- $R\in\abs{3e_0}$ is recognizable for $M$ [@AE23, Ex. 9.20, arXiv v3 p. 33], with semifan the one of [@AET23, Thm. 1.2, arXiv v3 p. 3] (@thm:degree-two-k3-semifan).
- The stack of $M'$-quasipolarized surfaces depends on a very irrational vector of $M'\tensor\RR$ [@AE23, Def. 2.6, arXiv v3 p. 5], and the map to the stack for $M$ needs $j(e_0)$ to be big and nef. For the vector $h_\varepsilon$ of @lem:coble-hyperplane-class-nef, with very irrational coordinates, it is.

The conclusion is a statement about $F_{S_\Co}=\bD(T_\Co)/\ker\rho$, the space of surfaces with the ten curves ordered, and not about $\bD(T_\Co)/\Gamma_P$: the map from $F_{S_\Co}$ to the pairs forgets the order, so it has degree $10!$ onto $Z_P$ and is not the embedding that [@AE23, Rem. 6.10 and Prop. 6.12, arXiv v3 p. 17] suppose. So [@AE23, Thm. 9.1] is to be read for the group $\Gamma_P$: the normalization of $\bar Z_P$ is the semitoroidal compactification of $\bD(T_\Co)/\Gamma_P$ for the restricted semifan, which is $\Gamma_P$-invariant because the semifan of $F_2$ is invariant under the group of $F_2$.
The proof in [@AE23] of the restriction statement is two sentences and rests on "the functoriality of the stable pair and semitoroidal constructions under restriction to Noether--Lefschetz subdomains"; the same step is used for the Enriques locus in the proof of [@AEGS25, Thm. 5.9, arXiv v2 p. 31], for a group that is also a stabilizer and not a pointwise stabilizer of $M'$.
This volume records that step as @prob:restricted-semifan. It is not proved on this page, and @thm:coble-plane-model-compactification does not use it.

A second published statement applies to the divisor of (1): for a K3 surface with a nonsymplectic group action, a combination of fixed curves and of $(-2)$-curves of the generic Picard lattice that is big and nef is said to be recognizable "with the same proof" [@AEH24, §5B, arXiv v2 p. 17]. The divisor $\bar C+\sum_if^*E_i$ is such a combination. The ten curves are not preserved by the monodromy of $\bD(T_\Co)/\Orth(T_\Co)$, so the statement is again one about a cover.
:::

::: {.theorem #thm:coble-degree-two-compactification title="The compactification by the degree-$2$ polarization"}

Let $\overline{\fentwo}$ be the KSBA compactification (@def:ksba-compactification) of [@AEGS25, Def. 2.10, arXiv v2 p. 8], let $\overline{\fentwo}^{\mcf}$ be the semitoroidal compactification (@def:semitoroidal-compactification) that is its normalization [@AEGS25, Thm. 5.9, arXiv v2 p. 31], and let $\Delta_2\definedas\mch_{-2}/\gent\iscontainedin\fentwo$ be the Coble divisor.

1. For an unnodal (@def:nodal-enriques-surface) surface $S$ with a degree-$2$ polarization $h$, the pair $\bigl(S,\tfrac12C+\eps W\bigr)$ of @thm:coble-pair-ksba is KSBA-stable, where $W$ is the fixed curve of the deck transformation of the map given by $\abs{2h}$. A Picard-general (@def:picard-general-coble) surface is unnodal (@lem:coble-k3-negative-curves(4)).
2. The image $\bar\Delta$ of the closure $W_\Delta$ of $\Delta_2$ in $\overline{\fentwo}^{\mcf}$ is a closed subset (@def:closed-subset) of the projective variety (@def:projective-variety) $\overline{\fentwo}$, whose points are KSBA-stable pairs (@def:ksba-compactification).
3. The normalization of $W_\Delta$ is a normal compactification of $\bD(T_\Co)/R_{\gent}$, and it maps finitely onto $\bar\Delta$. This map is birational exactly when the map $\fentwo\to\overline{\fentwo}$ is generically injective (@def:injective-map) on $\Delta_2$.
:::

::: {.proof}

(1) is @thm:coble-pair-ksba.
(2) The normalization map is finite, so the image of the closed set (@def:closed-subset) $W_\Delta$ is closed, and it is the closure of the image of $\Delta_2$.
(3) $\overline{\fentwo}^{\mcf}$ contains $\fentwo$ as an open subset, so $\Delta_2$ is open in $W_\Delta$, and the normalization of $W_\Delta$ contains the normalization of $\Delta_2$ as an open dense subset; the latter is $\bD(T_\Co)/R_{\gent}$ by @thm:normalization. The map to $\bar\Delta$ is the composite of two finite maps, and a finite surjective map of irreducible varieties is birational exactly when it is generically injective.
:::

The injectivity in (3) holds if the pair that $\overline{\fentwo}$ assigns to a general point of $\Delta_2$ is $(Z,\eps\bar W)$, where $S\to Z$ contracts $C$ and $\bar W$ is the image of $W$, as [@AEGS25, §2.3, arXiv v2 p. 6] describes the points of the discriminant divisor: that pair determines $S$, its minimal resolution, and the class $h$, since $W\equiv K_S+2h$ (@prop:coble-pair-class(1)), and $(S,h)$ determines the point of $\bD(T_\Co)/R_{\gent}$ by @prop:coble-polarized-moduli(2) and @prop:coble-degree-two-space(2).
The identification of the pairs over $\Delta_2$ is not proved in [@AEGS25] and is not proved here.
That the normalization of $W_\Delta$ is the semitoroidal compactification for the semifans of @thm:coble-pair-semifan is @prob:restricted-semifan.

The published theorem for a fixed curve of genus at least $2$ does apply to the K3 cover of a surface with a degree-$2$ polarization, for a second involution.
The K3 cover of a surface of @prop:coble-quarter-singularity is the minimal resolution of a double cover of $\PP^1\times\PP^1$ branched along a curve of bidegree $(4,4)$ with one node. Such resolutions, with the covering involution, form the family of type $(3,3,1)$: it is the $(+1,+1)$-move from $(2,2,0)$, on which the fixed curve of genus $9$ acquires a node and the fixed curve of the limit has genus $8$ [@AE22, Lemma 4.10, arXiv v2 p. 19].
So [@AEH24, Thm. 3.24, arXiv v2 p. 14] holds for that family, of dimension $17$. Its hypothesis fails for $\sigma$ itself, whose fixed curve $\bar C$ is rational.

## What the covers give for the unpolarized space

::: {.proposition #prop:coble-bb-finite title="The Baily--Borel compactifications"}

Let $\Gamma'\iscontainedin\Orth(T_\Co)$ be a subgroup that contains $\ker\rho$. Then the covering $\bD(T_\Co)/\Gamma'\to F^{\mathrm{un}}_\Co$ extends to a finite morphism of the Baily--Borel compactifications.
:::

::: {.proof}

Put $\Gamma=\Orth(T_\Co)$ and $N=\ker\rho$, a normal subgroup of finite index (@def:index), and for a group (@def:group) $G$ between $N$ and $\Gamma$ let $A(G)$ be the graded ring of $G$-automorphic forms on $\bD(T_\Co)$.
The Baily--Borel compactification of $\bD(T_\Co)/G$ is the projective spectrum of $A(G)$, the forms of degree (@def:graded-object) $k$ being the sections of the $k$-th power of an ample line bundle on it [@Loo02, Thm. 2.4], as in the proof of @cor:looijenga-empty-arrangement. So $A(G)$ is a finitely generated (@def:module-subcategories) algebra.
The finite group $\Gamma/N$ acts on $A(N)$ with ring of invariants $A(\Gamma)$, so $A(N)$ is a finite module over $A(\Gamma)$, and so is its subring $A(\Gamma')$.
A finite extension of graded rings induces a finite morphism of projective spectra, and on $\bD(T_\Co)/\Gamma'$ it is the covering.
:::

A semitoroidal compactification of $\bD(T_\Co)/\Gamma'$ maps to its Baily--Borel compactification (@cor:toroidal-to-baily-borel), and so to that of $F^{\mathrm{un}}_\Co$.
A $\Gamma'$-admissible semifan $\mcf'$ is the restriction of an $\Orth(T_\Co)$-admissible semifan exactly when $g(\mcf'_I)=\mcf'_{gI}$ for every $g\in\Orth(T_\Co)$ and every primitive isotropic line $I$; then it defines a semitoroidal compactification of $F^{\mathrm{un}}_\Co$ (@def:semitoroidal-compactification), and the compactification of the cover maps finitely onto it. Call $\mcf'$ *$\Orth(T_\Co)$-invariant* in that case.

::: {.proposition #prop:coble-degree-two-semifan-not-invariant title="The semifans of the degree-$2$ structure are not invariant"}

Let $\mcf_A$ be the collection of the semifans $\mcf^{k}\intersect\delta^{\perp}$, $k=2,3,4,5$, of @thm:coble-pair-semifan at the four $0$-cusps of $\bD(T_\Co)/R_{\gent}$.
Then $\mcf_A$ is not $\Orth(T_\Co)$-invariant.
:::

::: {.proof}

The primitive (@def:primitive-embedding) isotropic vectors (@def:isotropic-subspace) of $T_\Co$ form one orbit (@def:group-orbit) of $\Orth(T_\Co)$ (@thm:unpolarized-cusps), so an element $g$ carries the cusp over $k=2$ to the cusp over $k=3$, and it induces an isometry of their boundary lattices.
If $\mcf_A$ were invariant, this isometry would carry $\mcf^2\intersect\delta^{\perp}$ to $\mcf^3\intersect\delta^{\perp}$.
By @thm:coble-pair-semifan(3) the first is a fan and the second is not, and the image of a fan under an isometry is a fan.
:::

::: {.remark #rmk:coble-plane-model-invariance-open title="The plane model: invariance is not decided"}

The five $0$-cusps of $\bD(T_\Co)/\Gamma_P$ (@prop:coble-plane-model-space(3)) lie over the one $0$-cusp of $F^{\mathrm{un}}_\Co$ (@thm:unpolarized-cusps) and over the one $0$-cusp of $F_2$ [@AE23, Ex. 9.20, arXiv v3 p. 33].
The semifan that the restriction statement of @rmk:coble-plane-model-semitoroidal assigns to each of them is the intersection of the semifan of [@AET23, §4D, arXiv v3 p. 26], a decomposition of the positive cone of $U\oplus E_8^2\oplus A_1$, with the subspace spanned by the boundary lattice of $T_\Co$ at that cusp.
These five intersections have not been computed, and whether they are carried to one another by $\Orth(T_\Co)$ is not known.
The comparison that @prop:coble-degree-two-semifan-not-invariant makes for the degree-$2$ structure is the one to make.
:::

::: {.remark #rmk:coble-unpolarized-what-remains title="What is defined on the unpolarized space"}

On $F^{\mathrm{un}}_\Co$ the following are defined without a polarization: the Baily--Borel compactification, and the toroidal compactification for the Coxeter fan at its one $0$-cusp (@thm:coble-coxeter-semifan), which is invariant under the full isometry group of the boundary lattice.
No interpretation of that toroidal compactification by stable pairs is known; the marking that a generalized Coxeter semifan needs is the missing datum of @warn:coble-marking, and by @prop:coble-degree-two-semifan-not-invariant the degree-$2$ structure supplies four different markings over the one cusp. At the cusp over $k=2$ the semifan of the degree-$2$ structure is the coarsening of this Coxeter fan by one irrelevant wall (@thm:coble-pair-semifan(1) and (2)).

A statement about $\fco=\bD(T_\Co)/\Gamma_\Co$ (@def:gamma-co-groups(1)) depends on $\Gamma_\Co$.
On the labelled base of @def:coble-family-unpolarized the group is $\Gamma_\Co(B)$, and what is proved is $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1)). The statements of this paragraph about $\fco$ hold under $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$ (@conj:gamma-co-stable, research#780), and reading them off the labelled base needs in addition $\Gamma_\Co=\Gamma_\Co(B)$ (research#797, item 6): under those, every class of $S_\Co$ is invariant under the monodromy, $\fco$ maps finitely to $\bD(T_\Co)/\Gamma_P$ and to $\bD(T_\Co)/R_{\gent}$, each of the two structures is defined on $\fco$ itself, and its Baily--Borel boundary is that of the stable quotient.
Given the two inputs that theorem names --- the existence of the orbifold structure on $M_\Co$ and the properness of the complement of the image of $\per$ in the chosen component --- @thm:gamma-co-is-full gives the monodromy group of the descended local system $\Gamma^{\mathrm{desc}}_\Co=\Orth^+(T_\Co)$, the descent along the $2$-morphisms that the theorem needs being @thm:quotient-local-system-descent; this is a different group belonging to the coarse quotient $F^{\mathrm{un}}_\Co$ and not to $\Gamma_\Co$, and the results of this page stated for $F^{\mathrm{un}}_\Co$ are statements about that quotient.
By @thm:coble-polarized-family a family of Coble surfaces with a polarization has monodromy on $T_\Co$ whose image in $\Orth(q_{T_\Co})$ has order prime to $527$.

The question of @qst:coble-n-polarizing-divisor has, for $n=1$, the following answer: a divisor $R+a\,f^*H$ with $H$ ample depends on the class $H$, no class $H$ is invariant (@thm:coble-invariant-classes), and for the hyperplane class of a plane model the divisor $\bar C+\sum_if^*E_i$ is the ramification divisor of the double plane (@thm:coble-plane-model-compactification(1)).
:::
