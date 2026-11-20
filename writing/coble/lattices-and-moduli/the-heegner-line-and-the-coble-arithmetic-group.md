# The Heegner line and the stable orthogonal group {#sec-heegner-line}

## The Heegner vector inside $\ten$

::: {.lemma #lem:coble-heegner-vector title="An explicit $(-2)$ vector with Coble complement"}

Write $\ten = U\oplus U(2)\oplus E_8(2)$ and let $U = \ZZ u\oplus\ZZ w$ be the unimodular hyperbolic (@def:definiteness) summand, so $u^2 = w^2 = 0$ and $u\cdot w = 1$.
Set
$$
\delta \definedas u - w,
\qquad
\zeta \definedas u + w
.
$$
Then $\delta^2 = -2$, $\zeta^2 = 2$ and $\delta\cdot\zeta = 0$, and
$$
\delta^{\perp \ten} = \ZZ\zeta\oplus U(2)\oplus E_8(2)
\cong \generators{2}\oplus U(2)\oplus E_8(2)
= \generators{2}\oplus E_{10}(2)
= T_\Co
.
$$
The sublattice $\ZZ\delta\oplus\delta^{\perp\ten}$ has index $2$ in $\ten$, the missing generator being $u = \tfrac{1}{2}(\delta + \zeta)$, and the associated gluing class in $A_{\delta^{\perp\ten}}$ is $\tfrac{1}{2}\zeta$.
:::

::: {.proof}

The three pairings are immediate from $u^2 = w^2 = 0$ and $u\cdot w = 1$.
A vector $x\in \ten$ decomposes as $x = au + bw + y$ with $y\in U(2)\oplus E_8(2)$, and $x\cdot\delta = a\,\bigl(u\cdot(u-w)\bigr) + b\,\bigl(w\cdot(u-w)\bigr) = -a + b$, so $x\in\delta^{\perp\ten}$ if and only if $a = b$, that is $x\in\ZZ\zeta\oplus U(2)\oplus E_8(2)$.
Since $\zeta^2 = 2$, this sublattice is $\generators{2}\oplus E_{10}(2) = T_\Co$ by @def:enriques-lattice.

For the index, $\delta$ and $\zeta$ have coordinate matrix $\begin{bmatrix}1 & -1\\ 1 & 1\end{bmatrix}$ of determinant $2$ in the basis (@def:based-module) $(u, w)$, so $\ZZ\delta\oplus\ZZ\zeta$ has index $2$ in $U$ and hence $\ZZ\delta\oplus\delta^{\perp\ten}$ has index $2$ in $\ten$; the class of $u = \tfrac12(\delta+\zeta)$ generates the quotient.
By Nikulin's gluing theorem (@thm:nikulin-gluing) the corresponding isotropic subgroup of $A_{\ZZ\delta}\oplus A_{\delta^{\perp\ten}}$ is the graph of the isometry sending $\tfrac12\delta$ to $\tfrac12\zeta$, whose component in $A_{\delta^{\perp\ten}}$ is the stated class.
:::

::: {.corollary #cor:eta-is-heegner-complement title="The embedding $\eta$ is the inclusion of $\delta^{\perp\ten}$"}

Take $(u,w) = (\tilde e,\tilde f)$.
The primitive embedding $\eta\colon T_\Co\injects\ten$ of @lem:primitive_embedding_eta has image $\delta^{\perp\ten}$, and the gluing class of $\eta(T_\Co)\subset\ten$ is $\tfrac12\eta(h) = \tfrac12\zeta$.
:::

::: {.proof}

The map $\eta$ sends $h$ to $\tilde e+\tilde f = u+w = \zeta$ and is the identity on the summand $E_{10}(2) = U(2)\oplus E_8(2)$.
So $\eta(T_\Co) = \ZZ\zeta\oplus U(2)\oplus E_8(2)$, which is $\delta^{\perp\ten}$ with gluing class $\tfrac12\zeta$ by @lem:coble-heegner-vector.
:::

## Uniqueness of the Heegner line

::: {.theorem #thm:coble-heegner-line-unique title="The Coble Heegner line is unique up to $\gent$"}

By @lem:coble-heegner-vector, the line $\ZZ\delta\subset\ten$ represents the unique $\gent$-orbit of lines spanned by a $(-2)$ vector of $\ten$.
:::

::: {.proof}

There is a single $\Orth(\ten)$-orbit of $(-2)$ vectors in $\ten$ [@Nam85, Thm. 2.13], so it suffices to show that this orbit (@def:group-orbit) does not split (@def:hyperbolic-plane) under the subgroup $\gent\leq\Orth(\ten)$.

Write $\mathcal A\definedas\im\bigl(\gent\to\Orth(A_{\ten}, q_{\ten})\bigr)$, so that $\gent\iscontainedin\Orth_{\mathcal A}(\ten)\definedas \theset{\, g\in\Orth(\ten) \mid \bar g\in\mathcal A \,}$.
By @prop:sterk-group-identification(2) the image $\rho(\gent)$ is $M = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ and $\gent = \rho^{-1}(M)$, so $\Orth_{\mathcal A}(\ten) = \rho^{-1}(\mathcal A) = \gent$: the preimage subgroup and the polarized group coincide.
[@Daw22, Alg. 2.2] decides $\Orth_{\mathcal A}(\ten)$-equivalence of non-isotropic vectors under three hypotheses: the vector is non-isotropic, its orthogonal complement is indefinite (@def:definiteness), and $\Orth(\ten)\to\Orth(q_{\ten})$ is surjective.
All three hold here.
Indeed $\delta^2 = -2\neq 0$; the complement $\delta^{\perp\ten} = T_\Co$ has signature $(2,9)$; and $\ten$ is an indefinite $2$-elementary lattice, so $\Orth(\ten)\to\Orth(q_{\ten})$ is surjective by @thm:two-elementary-surjectivity.
The test the algorithm applies is the discriminant-gluing condition of Nikulin's gluing theorem (@thm:nikulin-gluing) for the rank-one sublattice $\ZZ\delta$ and its complement: an isometry of $\delta^{\perp\ten}$ extends over the line $\ZZ\delta$ exactly when it preserves the gluing class $\tfrac12\zeta\in A_{\delta^{\perp\ten}}$ of @lem:coble-heegner-vector.

That condition is vacuous here.
The class $\tfrac12\zeta$ satisfies $q_{T_\Co}(\tfrac12\zeta) = \tfrac12$, and by @prop:coble-discriminant-group every isometry of $q_{T_\Co}$ preserves the orthogonal decomposition $A_{T_\Co} = \ZZ\tfrac12\zeta\perp A^0$ and fixes $\tfrac12\zeta$, so
$$
\Stab_{\Orth(A_{T_\Co}, q_{T_\Co})}\bigl(\tfrac12\zeta\bigr)
= \Orth(A_{T_\Co}, q_{T_\Co})
.
$$
The double coset set controlling the split of the full $\Orth(\ten)$-orbit by the preimage subgroup is therefore a singleton, and the orbit does not split.
:::

## The stable orthogonal group induced from the Enriques side

::: {.definition #def:gamma-co-en title="The induced Coble subgroup" defines="induced Coble subgroup; $\widetilde\Orth^+(T_\Co)^\En(\delta)$"}

For the Heegner vector $\delta$ of @lem:coble-heegner-vector, define
$$
\widetilde\Orth^+(T_\Co)^\En(\delta)
\definedas \im\Bigl(
\Stab_{\gent}(\ZZ\delta)
\too
\Orth\bigl(\delta^{\perp \ten}\bigr) = \Orth(T_\Co)
\Bigr)
,
$$
the group (@def:group) of restrictions to $\delta^{\perp\ten}$ of those elements of $\gent$ that preserve the line $\ZZ\delta$.
:::

::: {.proposition #prop:gamma-en-two-gluing title="Discriminant description of $\gent$"}

Let $\sen = U(2)\oplus E_8(2)$ and $\ten$ be the invariant and coinvariant lattices of the Enriques involution (@def:enriques-surface) on $\lkt$, and let
$$
\gamma\colon A_{\sen}\iso A_{\ten},
\qquad
q_{\ten}\circ\gamma = -q_{\sen}
$$
be the gluing anti-isometry supplied by the embedding-gluing description (@cons:embedding-gluing-data) for the primitive embedding $\sen\injects\lkt$ with complement $\ten$.
Then
$$
\gent
= \theset{\,
g_T\in\Orth(\ten)
\;\middle|\;
\exists\, g_S\in\Orth(\sen) \text{ with } g_S(h) = h
\textand \bar g_T\circ\gamma = \gamma\circ\bar g_S
\,}
,
$$
where $h = e + f\in U(2) = \sdp\iscontainedin \sen$ is the degree-$2$ polarization vector (@def:polarization-vector), with $e^2 = f^2 = 0$ and $e\cdot f = 2$, so that $h^2 = 4$ [@AEGS25 Def. 2.5 and Def. 2.6].
Equivalently, the image of $\gent$ in $\Orth(q_{\ten})$ is the $\gamma$-transport of the image of $\Stab_{\Orth(\sen)}(h)$ in $\Orth(q_{\sen})$.
:::

::: {.proof}

By definition $\gent$ is the image in $\Orth(\ten)$ of the isometries of $\lkt$ that commute with $\Ien$ and fix $h$ [@AEGS25 Def. 2.6].
An isometry of $\lkt$ commuting with $\Ien$ is the same as a pair $(g_S, g_T)\in\Orth(\sen)\times\Orth(\ten)$ preserving the two eigenlattices, and by Nikulin's gluing theorem (@thm:nikulin-gluing) such a pair extends over the overlattice $\lkt$ of $\sen\oplus \ten$ exactly when it preserves the graph of $\gamma$, that is when $\bar g_T\circ\gamma = \gamma\circ\bar g_S$.
The polarization $h$ lies in $\sen$, so the condition $g(h) = h$ on $\lkt$ is the condition $g_S(h) = h$.
:::

::: {.proposition #prop:polarization-stabilizer-enriques title="The integral stabilizer of the degree-$2$ polarization"}

Write $\sen = C(2)$ with $C = U\oplus E_8$ even unimodular of signature (@def:signature) $(1,9)$, and let $h\in \sen$ be the polarization (@def:numerical-polarization) vector of the discriminant description of $\gent$ (@prop:gamma-en-two-gluing), so that $h = u_0 + w_0$ for a basis (@def:based-module) $u_0, w_0$ of the $U$ summand of $C$ with $u_0\cdot w_0 = 1$.
After identifying $\Orth(\sen)=\Orth(C)$, restriction to $h^{\perp C}$ gives an isomorphism
$$
\Stab_{\Orth(\sen)}(h)
\;\iso\;
\Orth\bigl(\generators{-2}\oplus E_8\bigr)
= \theset{\pm 1}\times W(E_8)
,
$$
of order $2\abs{W(E_8)} = 1\,393\,459\,200$, and the element $\id_U\oplus(-\id_{E_8})$ lies in the kernel of the reduction $\Stab_{\Orth(\sen)}(h)\to\Orth(A_{\sen}, q_{\sen})$.
:::

::: {.proof}

Twisting does not change the isometry group (@def:group), so $\Orth(\sen) = \Orth(C)$ and $\Stab_{\Orth(\sen)}(h) = \Stab_{\Orth(C)}(h)$.
Computing in $C$, one has $h^2 = 2$ and $h^{\perp C} = \ZZ(u_0 - w_0)\oplus E_8$ with $(u_0-w_0)^2 = -2$, so $h^{\perp C}\cong\generators{-2}\oplus E_8$.
An isometry fixing $h$ preserves $h^{\perp C}$, giving the restriction homomorphism, which is injective (@def:injective-map) because $C_\QQ = \QQ h\oplus (h^{\perp C})_\QQ$.
It is surjective: $A_{h^{\perp C}}\cong A_{\generators{-2}}\cong\ZZ/2\ZZ$ has trivial automorphism group (@def:endomorphism-monoid), so every isometry of $h^{\perp C}$ preserves the gluing class of the index-two overlattice $C$ of $\ZZ h\oplus h^{\perp C}$ and extends over $C$ fixing $h$, by Nikulin's gluing theorem (@thm:nikulin-gluing).
The lattice $\generators{-2}\oplus E_8$ is negative definite (@def:definiteness) and generated by its $(-2)$ vectors, whose root system (@def:root-system-base) is $A_1\oplus E_8$; no isometry mixes summands of different ranks, so its isometry group is $\Orth(\generators{-2})\times\Orth(E_8) = \theset{\pm1}\times W(E_8)$.

For the last claim, $\id_U\oplus(-\id_{E_8})$ fixes $h\in U$ and acts on $A_{\sen}\cong C/2C$ as in @prop:twisted-unimodular-discriminant, by the identity on $U/2U$ and by $x\mapsto -x\equiv x$ on $E_8/2E_8$.
:::

::: {.lemma #lem:gco-orbit-transfer title="The $G_\Co$ orbit decomposition lives on the $S_\En$ summand"}

By @prop:tco-as-twist $T_\Co = B(2) = \generators{2}\oplus U(2)\oplus E_8(2)$, so $T_\Co = \generators{\zeta}\perp S_\En$ with $\zeta^2 = 2$ and $S_\En = U(2)\oplus E_8(2)$, and discriminant forms add over orthogonal sums (@def:orthogonal-sum):
$$
A_{T_\Co} = A_{\generators{2}}\perp A_{S_\En},
\qquad
q_{T_\Co} = q_{\generators{2}} + q_{S_\En},
$$
with $q_{\generators{2}}$ taking the value $\tfrac12$ on the nonzero class and $q_{S_\En}$ taking values in $\ZZ/2\ZZ$.
Then the isotropic classes (@def:descent-class) of $A_{T_\Co}$ are exactly the classes whose $A_{\generators{2}}$-coordinate vanishes, and they number $528$, the same as the isotropic classes of $A_{S_\En}$.
Each of the nine group (@def:group) generators of $G_\Co$ is the reflection in a vector of $S_\En$, hence fixes $\zeta$, preserves the splitting, and acts on $A_{T_\Co}$ as $\id\oplus\rho_{S_\En}(g_i)$.
Consequently the orbits (@def:group-orbit) of $G_\Co$ on the isotropic classes of $A_{T_\Co}$ are its orbits on the isotropic classes of $A_{S_\En}$, with the same sizes.
:::

::: {.proof}

The splitting is the one displayed; $q_{\generators{2}}(\tfrac12\zeta) = \tfrac14\zeta^2 = \tfrac12$, and the values of $q_{S_\En}$ are integers.
A class $(a, y)$ with $a\in\{0,1\}$ has $q_{T_\Co}(a,y) = \tfrac{a}{2} + q_{S_\En}(y)$, which vanishes in $\QQ/2\ZZ$ only if $a = 0$ and $q_{S_\En}(y) = 0$: for $a = 1$ it would require $q_{S_\En}(y) = -\tfrac12$, and no class of $A_{S_\En}$ has that value.
So the isotropic classes of $A_{T_\Co}$ are the isotropic classes of $A_{S_\En}$ with first coordinate $0$, and their number is the one recorded for $A_{S_\En}$.
The nine vectors generating $G_\Co$ are $u_0 - w_0$ and the eight simple roots of $E_8(2)$ (@prop:polarization-stabilizer-enriques), all of them in the $S_\En$ summand, hence orthogonal to $\zeta$; so each reflection fixes $\zeta$ and acts as $\id\oplus\rho_{S_\En}(g_i)$ on the discriminant module.
An orbit of $G_\Co$ on $A_{T_\Co}$ therefore stays in its first coordinate, and on the first coordinate $0$ it is an orbit on $A_{S_\En}$.
:::

::: {.theorem #thm:coble-heegner-finite-orbits title="The finite image and its isotropic orbits"}

With the notation of @prop:polarization-stabilizer-enriques and @lem:coble-heegner-vector:

1. the image of the integral stabilizer (@def:group-orbit) in the discriminant group,
   $$
   G \definedas \im\bigl(\Stab_{\Orth(\sen)}(h)\to\Orth(A_{\sen}, q_{\sen})\bigr)
   ,
   $$
   has order $\abs{W(E_8)} = 696\,729\,600$, and is generated by the images of the swap of the two isotropic basis (@def:isotropic-basis-hyperbolic-plane) vectors $u_0, w_0$ of the $U$ summand of $C$, which fixes $h$, and of the reflections in the simple roots of the $E_8$ summand;

2. the corresponding group $G_\Co\leq\Orth(A_{T_\Co}, q_{T_\Co})$, obtained by transporting $G$ along $\gamma$ and restricting to the Coble Heegner complement $\delta^{\perp\ten} = T_\Co$, has order $\abs{W(E_8)}$ and acts on the $528$ isotropic classes of $A_{T_\Co}$ with orbit (@def:group-orbit) lengths
   $$
   [\,1,\ 2,\ 120,\ 135,\ 270\,]
   ;$$

3. let $c\in A_{T_\Co}$ be the class of the transported polarization, the image of the class $[h/2]\in A_{\sen}$ under $\gamma$; the finite stabilizer $H\definedas\Stab_{\Orth(q_{T_\Co})}(c)$ has order $94\,755\,225\,600$, contains $G_\Co$ with index $136$, and acts on the same $528$ isotropic classes with orbit lengths $[\,1,\ 255,\ 272\,]$.
:::

::: {.proof}

Let $A^0\subset A_{T_\Co}$ be the index-$2$ subgroup of @prop:coble-discriminant-group, identified with $A_{\ten}$ as in the proof of @prop:gamma-co-in-heegner-group.
An isotropic class has $q_{T_\Co} = 0\in\ZZ/2\ZZ$, so it lies in $A^0$, and restriction to $A^0$ is an isomorphism $\Orth(q_{T_\Co})\iso\Orth(q_{T_\Co}|_{A^0})$ by @prop:coble-discriminant-group.
The forms $q_{\sen}$ and $q_{T_\Co}|_{A^0}$ take values in $\ZZ/2\ZZ$, where $-1 = 1$, so the anti-isometry $\gamma\colon A_{\sen}\iso A^0$ is an isometry.
Conjugation by $\gamma$ therefore carries $G$ to $G_\Co$, the stabilizer of $[h/2]$ to $H$, and the isotropic classes of $A_{\sen}$ to those of $A_{T_\Co}$.
So all three items may be computed on $A_{\sen} = A_{U(2)}\perp A_{E_8(2)}$, and since $\gamma$ is a bijection, $\abs{G_\Co} = \abs{G}$.

(1) By @prop:polarization-stabilizer-enriques, $\Stab_{\Orth(\sen)}(h) = \theset{\pm1}\times W(E_8)$.
The first factor is generated by the reflection $s_{u_0-w_0}$, which in $C$ sends $u_0$ to $u_0 + \bigl(u_0\cdot(u_0-w_0)\bigr)(u_0-w_0) = w_0$ and so is the swap $u_0\leftrightarrow w_0$; the second is generated by the reflections in the simple roots of $E_8$.
So the images of these isometries generate $G$, and $\abs{G} = \abs{W(E_8)}$ is the last step of the proof of @prop:gamma-co-heegner-strict.
Each of these isometries preserves the splitting $A_{\sen} = A_{U(2)}\perp A_{E_8(2)}$, so $G\leq P\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$; by @prop:gamma-cong-eq-heegner(1), $\abs{P} = \abs{W(E_8)} = \abs{G}$, hence $G = P$.

(2) By the proof of @prop:gamma-cong-eq-heegner(1), $q_{U(2)}$ takes the values $0, 0, 1$ on the nonzero classes $[u_0/2]$, $[w_0/2]$, $[h/2]$, and $\Orth(q_{U(2)})$ has the orbits $\theset{0}$, $\theset{[h/2]}$ and $\theset{[u_0/2], [w_0/2]}$.
By the proof of @prop:coble-q-fibers, $q_{E_8(2)}$ is a nondegenerate quadratic form of plus type on the $8$-dimensional $\bF_2$-space $E_8/2E_8$ with $136$ zeros, so it has $135$ nonzero singular vectors and $256 - 136 = 120$ nonsingular vectors.
Witt's extension theorem, applied as in the proof of @thm:coble-isotropic-class-orbits, makes $\Orth(q_{E_8(2)})$ transitive on each of these two sets; its orbits are $\theset{0}$, the $135$ nonzero singular vectors and the $120$ nonsingular vectors.
The orbits of the product $P$ on $A_{U(2)}\perp A_{E_8(2)}$ are the products of these orbits, and a class $(a,y)$ is isotropic exactly when $q_{U(2)}(a) = q_{E_8(2)}(y)$.
The isotropic orbits are therefore

| $a$ | $y$ | orbit length |
| --- | --- | --- |
| $0$ | $0$ | $1$ |
| $[u_0/2]$ or $[w_0/2]$ | $0$ | $2$ |
| $[h/2]$ | nonsingular | $120$ |
| $0$ | nonzero singular | $135$ |
| $[u_0/2]$ or $[w_0/2]$ | nonzero singular | $2\cdot 135 = 270$ |

and their lengths sum to $528$, the number of isotropic classes in @prop:coble-q-fibers.

(3) $G$ fixes $[h/2]$, since it is the image of the stabilizer of $h$, so $G_\Co\leq H$.
The class $c$ has $q_{T_\Co}(c) = -q_{\sen}([h/2]) = -1 = 1$ in $\ZZ/2\ZZ$.
The classes of $A_{T_\Co}$ with $q_{T_\Co} = 1$ lie in $A^0$ and are the $496$ classes of the fiber $\inverseof{Q}(2)$ of @prop:coble-q-fibers.
The form $q_{T_\Co}|_{A^0}\cong q_{E_{10}(2)}$ is nondegenerate, so by Witt's extension theorem $\Orth(q_{T_\Co})$ is transitive on these $496$ classes, and by @prop:coble-discriminant-group
$$
\abs{H} = \frac{46\,998\,591\,897\,600}{496} = 94\,755\,225\,600,
\qquad
[H:G_\Co] = \frac{94\,755\,225\,600}{696\,729\,600} = 136
.$$
For the orbits, work in $A_{\sen}$ with $c = [h/2]$.
A nonzero isotropic class $x$ is not $[h/2]$, because $q([h/2]) = 1$, so $x$ and $[h/2]$ span a plane, whose quadratic form is fixed by $q(x) = 0$, $q([h/2]) = 1$ and the value $b(x, [h/2])\in\theset{0,\tfrac12}$.
By Witt's extension theorem, two nonzero isotropic classes with the same value of $b(x,[h/2])$ are exchanged by an isometry fixing $[h/2]$, so the nonzero isotropic classes form at most two $H$-orbits, indexed by that value.
For $x = (a,y)$ one has $b(x,[h/2]) = b(a,[h/2])$, which is $0$ for $a\in\theset{0,[h/2]}$ and $\tfrac12$ for $a\in\theset{[u_0/2],[w_0/2]}$, because distinct nonzero classes of $A_{U(2)}$ pair to $\tfrac12$.
By the table in (2), the first value occurs on $135 + 120 = 255$ classes and the second on $2 + 270 = 272$ classes, so the $H$-orbits have lengths $1$, $255$ and $272$.
:::

::: {.corollary #cor:coble-heegner-orbit-refinement title="How the two orbit decompositions refine one another"}

In the notation of @thm:coble-heegner-finite-orbits, the $H$-orbit of length $255$ is the union of the $G_\Co$-orbits of lengths $135$ and $120$, and the $H$-orbit of length $272$ is the union of those of lengths $2$ and $270$.
For an isotropic class $x$ whose $G_\Co$-orbit has length $n$ and whose $H$-orbit has length $m$,
$$
[\Stab_H(x):\Stab_{G_\Co}(x)] = \frac{136\,n}{m},
$$
which is $1$ for $n = 2$, $135$ for $n = 270$, $72$ for $n = 135$ and $64$ for $n = 120$.
:::

::: {.proof}

The first claim is the last step of the proof of @thm:coble-heegner-finite-orbits(3).
For the indices, $\abs{\Stab_H(x)} = \abs{H}/m$ and $\abs{\Stab_{G_\Co}(x)} = \abs{G_\Co}/n$, and $\abs{H}/\abs{G_\Co} = 136$.
The four values are $136\cdot 2/272 = 1$, $136\cdot 270/272 = 135$, $136\cdot 135/255 = 72$ and $136\cdot 120/255 = 64$.
:::

## The sign involution of the Coble primitive embedding

::: {.proposition #prop:theta-co-exists title="The sign involution of the Coble primitive embedding"}

Let $S_\Co\injects\lkt$ be the primitive embedding from @prop:coble-invariant-lattice, with complement $T_\Co = S_\Co^{\perp\lkt}$, and let
$$
\gamma_\Co\colon A_{S_\Co}\iso A_{T_\Co},
\qquad
q_{T_\Co}\circ\gamma_\Co = -q_{S_\Co}
$$
be the associated gluing anti-isometry.
Then the pair $(-\id_{S_\Co}, \id_{T_\Co})$ preserves the graph of $\gamma_\Co$ and therefore defines an isometry
$$
\theta_\Co\in\Orth(\lkt),
\qquad
\restrictionof{\theta_\Co}{S_\Co} = -\id,
\qquad
\restrictionof{\theta_\Co}{T_\Co} = \id
,
$$
whose $(+1)$ and $(-1)$ eigenlattices are $T_\Co$ and $S_\Co$.
An isometry of $\lkt$ commutes (@def:commutative-diagram) with $\theta_\Co$ if and only if it preserves both eigenlattices.
:::

::: {.proof}

Both $A_{S_\Co}$ and $A_{T_\Co}$ are $2$-elementary, so $-\id$ and $\id$ agree on each of them; the pair therefore acts as the identity on the graph of $\gamma_\Co$ and by Nikulin's gluing theorem (@thm:nikulin-gluing) extends over the overlattice $\lkt$ of $S_\Co\oplus T_\Co$.
The eigenlattice description is the definition of the extension.
For the last claim, an isometry commuting with an involution preserves its eigenspaces, which by @prop:involution_eigenspaces are the rational spans of $T_\Co$ and $S_\Co$; conversely an isometry preserving both eigenlattices commutes with $\theta_\Co$ on each of them and hence on $\lkt$.
:::

::: {.proposition #prop:unnodal-coble-polarization-nef title="The degree-$2$ polarization of an unnodal Coble surface is nef and big"}

Let $S$ be an unnodal (@def:nodal-enriques-surface) Coble surface (@def:coble-surface), that is one with no $(-2)$-curves, let $F_1\in\abs{f_1}$ and $F_2\in\abs{f_2}$ be half-fibres of its two Halphen fibrations of index (@def:index) (@def:halphen-surface-index) $2$, and put $h = F_1+F_2$, so that $F_i^2 = 0$, $F_1\cdot F_2 = 1$ and $h^2 = 2$.
Then $\abs{2h}$ has no base points (@def:complete-linear-system), and $h$ is nef and big.
:::

::: {.proof}

By [@CD12, Lemma 3.7], $\abs{2h}$ has no base points; the proof there uses only the intersection numbers of $f_1, f_2, K_S$ and the equalities $\abs{f_i} = \set{F_i}$, and not the effectivity of $-2K_S$ [@CD12, Remark 3.8].
A base-point-free class is nef, so $2h$ and hence $h$ are nef, and $h^2 = 2>0$ makes $h$ big by @prop:nef-big-finite-cover.
:::

::: {.construction #cons:cd12-double-plane title="The double-plane model of an unnodal Coble surface [@CD12, §3]" defines="double-plane model of an unnodal Coble surface; $\mathfrak C$; $\pi$; $\widetilde X$; $I_\Co$; $R_\pi$; $\phi_h$; $\mathsf D$; $\mathrm{bl}_q$; $\mathsf D'$; $E_q$; $\phi'$; $\tau$; $\overline W$; $\mathsf H$; $E_8$"}

Let $S$ and $h$ be as in @prop:unnodal-coble-polarization-nef.

1. $\mathfrak C\subset S$ is the unique curve in $\abs{-2K_S}$; it is a smooth rational curve with $\mathfrak C^2 = -4$ [@CD12, §3.2].
2. $\pi\colon\widetilde X\to S$ is the K3 double cover (@not:coble-ten-point-blowup) branched along $\mathfrak C$, with $\pi_*\OO_{\widetilde X} = \OO_S\oplus\OO_S(K_S)$; $I_\Co$ is its deck involution, and $R_\pi\definedas\pi^{-1}(\mathfrak C)$ is the fixed curve of $I_\Co$.
3. $\phi_h\colon S\to\mathsf D\subset\PP^4$ is the morphism defined by $\abs{2h}$. It is $2$-to-$1$ onto a del Pezzo surface (@def:degree-of-del-pezzo-surface) $\mathsf D$ of degree (@def:graded-object) $4$ with four ordinary (@def:two-elementary-isotropic-types) double points [@CD12, Lemmas 3.9, 3.10], and it contracts $\mathfrak C$ to one of them, $q$, because $h\cdot\mathfrak C = h\cdot(-2K_S) = 0$.
4. $\mathrm{bl}_q\colon\mathsf D'\to\mathsf D$ is the blowup of $q$, with exceptional curve $E_q$, and $\phi'\colon S\to\mathsf D'$ is the induced finite double cover, so that $\mathfrak C = \phi'^{-1}(E_q)$; $\tau\in\Aut(S)$ is its deck involution.
5. The fixed locus of $\tau$ is a smooth curve $\overline W\subset S$ of genus $4$ together with three isolated points, and $\overline W$ meets $\mathfrak C$ in two points [@DK13, §8].
6. $\mathsf H\definedas\langle f_1, f_2\rangle\subset K_S^{\perp}$ and $E_8\definedas\mathsf H^{\perp K_S^{\perp}}$. The classes $f_1, f_2, K_S$ are $\tau$-invariant, and $\tau^* = \id_{\mathsf H}\oplus(-\id_{E_8})$ on $K_S^{\perp}\otimes\QQ$ [@CD12, proof of Theorem 3.5].

The automorphism $I_\Co$ acts on $\widetilde X$ and $\tau$ acts on $S$; the curve $\overline W$ lies on $S$, and the curve $R_\pi$ lies on $\widetilde X$.
:::

::: {.proposition #prop:involution-lifting-double-cover title="Lifting an involution through a branched double cover, and when the lift is an involution"}

Let $S$ be a smooth projective surface (@def:smooth-projective-surface) over $\CC$, let $\mcl$ be a line bundle, let $s\in H^0(\mcl^{\otimes2})$ be a section cutting out a smooth curve $B$, and let $\pi\colon\widetilde X\to S$ be the double cover with $\pi_*\OO_{\widetilde X} = \OO_S\oplus\mcl^{-1}$ and multiplication given by $s$; let $\iota$ be the deck involution, $+1$ on $\OO_S$ and $-1$ on $\mcl^{-1}$.
Let $\tau\in\Aut(S)$ be an involution with $\tau(B) = B$, and let $\lambda\colon\tau^*\mcl\to\mcl$ be an isomorphism (@def:isomorphism-of-objects) with $\lambda(\tau^*s) = c\,s$ for some $c\in\CC^\times$; rescaling $\lambda$ by a square root of $c$ normalizes $c = 1$, and leaves the choice $\pm\lambda$. Then:

1. $\tau$ lifts to an automorphism $\tilde\tau$ of $\widetilde X$ with $\pi\tilde\tau = \tau\pi$, and the lifts of $\tau$ are exactly $\tilde\tau$ and $\tilde\tau\iota$;
2. $\tilde\tau^2\in\set{\id,\iota}$, and $(\tilde\tau\iota)^2 = \tilde\tau^2$;
3. let $p\in B$ be a fixed point of $\tau$ and let $\sigma\in\set{\pm1}$ be the sign by which $\tau$ acts on the normal line $N_{B/S,p}$. Then $\tilde\tau^2 = \id$ if $\sigma = +1$, and $\tilde\tau^2 = \iota$ if $\sigma = -1$; in particular, if a fixed curve of $\tau$ passes through $p$ transversally to $B$, then $\tilde\tau$ is an involution.
:::

::: {.proof}

(1) The $\ZZ/2$-graded algebra $\mca = \OO_S\oplus\mcl^{-1}$ has $\Spec_S\mca = \widetilde X$. The action of $\tau$ on it is the identity in degree (@def:graded-object) $0$ and $\mcl^{-1}\to\tau_*\mcl^{-1} = \tau_*(\tau^*\mcl)^{-1}\xrightarrow{\lambda^{-1}}\tau_*\mcl^{-1}$ in degree $1$; it is multiplicative because $\lambda(\tau^*s) = cs$ sends the structure section to a scalar multiple of itself. Any two such actions agree on $\OO_S$, so their quotient is an automorphism over $\OO_S$, that is an element of the deck group (@def:group) $\set{\id,\iota}$ ($\widetilde X$ being connected as $B\neq\emptyset$).
(2) $\tilde\tau^2$ satisfies $\pi\tilde\tau^2 = \pi$, so it is a deck transformation. Since $\iota$ is central in $\Aut(\widetilde X/S)$, $(\tilde\tau\iota)^2 = \tilde\tau\iota\tilde\tau\iota = \tilde\tau^2\iota^2 = \tilde\tau^2$.
(3) Take coordinates $(u,v)$ at $p$ with $B = \set{u = 0}$ and $\mcl$ trivialized so that $s = u$; then $\widetilde X$ is $\set{w^2 = u}$ over that neighbourhood, and $\tau^*(u) = \sigma u + O(u^2)$ because $\tau$ fixes $p$ and preserves $B$. A lift acts by $\tau^*(w) = \epsilon w$ with $\epsilon^2 w^2 = \tau^*(u)$, that is $\epsilon^2 = \sigma$. Then $\tilde\tau^2$ acts on $w$ by $\epsilon^2 = \sigma$, whereas $\iota$ acts by $-1$; so $\tilde\tau^2 = \id$ exactly when $\sigma = +1$, and when $\sigma = -1$ one has $\epsilon = \pm i$ and $\tilde\tau^2 = \iota$. If a fixed curve $C'$ of $\tau$ passes through $p$ transversally to $B$, then $T_pC' = N_{B/S,p}$ and $\tau$ fixes $C'$ pointwise, so $\sigma = +1$.
:::

::: {.corollary #cor:lift-in-cd12-model title="The lift of the deck transformation $\tau$ is an involution"}

In @cons:cd12-double-plane take $B = \mathfrak C$ and $\mcl = \OO_S(-K_S)$.
Then $\tau$ lifts to $\widetilde X$, every lift $\tilde\tau$ is an involution commuting with $I_\Co$, and the three isolated fixed points of $\tau$ do not lie on $\mathfrak C$.
:::

::: {.proof}

The hypotheses of @prop:involution-lifting-double-cover hold: $\tau$ is an involution, $\mathfrak C$ is smooth, $\tau(\mathfrak C) = \mathfrak C$ because $\mathfrak C = \phi'^{-1}(E_q)$ and $\tau$ acts fibrewise over $\mathsf D'$, and $\tau^*\mcl\cong\mcl$ because $K_S$ is $\tau$-invariant (@cons:cd12-double-plane(6)).
The sections $s$ and $\tau^*s$ cut out the same divisor $\mathfrak C\in\abs{\mcl^{\otimes 2}}$, so they differ by a constant $c\in\CC^\times$.
So $\tau$ lifts, and the lifts are $\tilde\tau$ and $\tilde\tau I_\Co$.
Each lift $\tilde\tau$ commutes (@def:commutative-diagram) with $I_\Co$: $\pi\tilde\tau I_\Co\tilde\tau^{-1} = \tau\pi I_\Co\tilde\tau^{-1} = \tau\pi\tilde\tau^{-1} = \pi$, so $\tilde\tau I_\Co\tilde\tau^{-1}$ is a deck transformation different from $\id$, that is $I_\Co$.

Let $p$ be one of the two points of $\overline W\cap\mathfrak C$ (@cons:cd12-double-plane(5)).
Since $\overline W$ is fixed pointwise, $\tau$ acts by $+1$ on $T_p\overline W$.
On $\mathfrak C\cong\PP^1$ the involution $\tau$ is not the identity: otherwise $\mathfrak C$ would lie in the fixed locus, so it would be $\overline W$, of genus $4$, or one of three points.
So $\tau$ acts by $-1$ on $T_p\mathfrak C$, the two tangent lines at $p$ are different eigenlines, and $T_p\overline W$ is the normal line $N_{\mathfrak C/S,p}$.
Hence $\sigma = +1$ at $p$, and $\tilde\tau^2 = \id$ by @prop:involution-lifting-double-cover(3); by part (2) of that proposition the other lift has the same square.

At an isolated fixed point $p'$ of $\tau$ on $\mathfrak C$, both eigenvalues of $\tau$ on $T_{p'}S$ would be $-1$, so $\sigma = -1$ and $\tilde\tau^2 = \iota$ by @prop:involution-lifting-double-cover(3), which contradicts $\tilde\tau^2 = \id$.
:::

The Coble surface $S$ is the blowup of $\PP^2$ at the ten nodes of a rational plane sextic [@DK13, §3].

::: {.proposition #prop:cd12-lift-on-lattice title="The lift of $\tau$ on the pulled-back lattice"}

In @cons:cd12-double-plane let $\tilde\tau$ be a lift of $\tau$ (@cor:lift-in-cd12-model). Then:

1. $\tilde\tau$ and $\tilde\tau I_\Co$ agree on $\pi^*\Pic(S)$; they fix $\pi^*\mathsf H$ and $\pi^*K_S$ and negate $\pi^*E_8$;
2. $\pi^*\mathsf H\cong U(2)$ and $(\pi^*K_S)^2 = -2$, so the invariant lattice (@def:invariant_coinvariant_lattices) of $\tilde\tau$ contains $\pi^*\mathsf H\oplus\ZZ\pi^*K_S$, of rank $3$, and is not $\sdp\cong U(2)$;
3. $I_\Co$ acts by $-1$ on $H^{2,0}(\widetilde X)$, so exactly one of $\tilde\tau$ and $\tilde\tau I_\Co$ is nonsymplectic.
:::

::: {.proof}

(1) $I_\Co$ acts trivially on $\pi^*\Pic(S)$, and $\tilde\tau(\pi^*D) = \pi^*(\tau D)$ for every divisor class $D$ on $S$.
So the two lifts act on $\pi^*\Pic(S)$ through $\tau^*$, which by @cons:cd12-double-plane(6) fixes $\mathsf H$ and $K_S$ and negates $E_8$.

(2) Pullback (@def:pullback-square) along the double cover multiplies intersection numbers by $2$.
So $(\pi^*f_i)^2 = 0$ and $\pi^*f_1\cdot\pi^*f_2 = 2$, which is $U(2)$, and $(\pi^*K_S)^2 = 2K_S^2 = -2$, because $K_S^2 = 9 - 10 = -1$ on the blowup of $\PP^2$ at ten points.
The class $K_S$ is orthogonal to $\mathsf H\subset K_S^{\perp}$, so the sum is orthogonal, and its rank $3$ exceeds the rank $2$ of $\sdp$.

(3) With $\mcl = \OO_S(-K_S)$ the canonical bundle $K_{\widetilde X} = \pi^*(K_S + \mcl)$ is trivial (@prop:double-cover-canonical-bundle), so $H^{2,0}(\widetilde X)$ is spanned by a nowhere vanishing $2$-form.
At a point of $R_\pi$, in coordinates with $\mathfrak C = \set{u = 0}$ and $\widetilde X = \set{w^2 = u}$, the functions $(w,v)$ are local coordinates on $\widetilde X$, $I_\Co$ sends $w$ to $-w$, and the local generator $dw\wedge dv$ goes to $-dw\wedge dv$.
So $I_\Co$ acts by $-1$ on $H^{2,0}(\widetilde X)$, and the two lifts, which differ by $I_\Co$, act on it with opposite signs.
:::

::: {.proposition #prop:nef-big-finite-cover title="Nefness under a finite cover, and bigness on a projective surface"}

Let $f\colon X\to S$ be a finite surjective morphism of projective varieties over $\CC$ and let $L$ be a line bundle on $S$.
Then $f^*L$ is nef if and only if $L$ is nef.
If $S$ is a projective surface and $D$ is a nef divisor class with $D^2>0$, then $D$ is big.
:::

::: {.proof}

For a curve $C'\subset X$ the projection formula gives $f^*L\cdot C' = L\cdot f_*C'$, and $f_*C'$ is a nonzero effective $1$-cycle because $f$ is finite, so $L$ nef implies $f^*L$ nef.
Conversely, for a curve $C\subset S$ one has $\deg(f)\,(L\cdot C) = f^*L\cdot f^*C$, where $f^*C$ is a nonzero effective $1$-cycle and $f^*L$ is nef, so $L\cdot C\ge 0$ and $L$ is nef.
For the surface statement, $(K_S-nD)\cdot A<0$ against an ample $A$ once $n\gg0$, and a nonzero effective class has nonnegative intersection with $A$, so $K_S-nD$ is not effective and $h^2(nD) = h^0(K_S-nD) = 0$; Riemann–Roch then gives $h^0(nD)\ge\chi(nD) = \tfrac12D^2n^2 + O(n)$, which is unbounded because $D^2>0$.
:::

::: {.proposition #prop:coble-cover-marking title="The marking of the Coble cover and the del Pezzo slot"}

In the model of [@DK13, §3] let $S$ be the blowup of $\PP^2$ at the ten nodes of an irreducible plane sextic $C$ and let $f\colon X\to S$ be the double cover branched along the proper transform (@def:strict-transform) $\tilde C\in\abs{-2K_S}$, so that $X$ is a K3 surface.
Then the invariant lattice of the covering involution is $f^*\Pic(S)$, spanned by $e_0 = f^*H$ and $e_i = f^*E_i$ for $i = 1,\dots,10$, with $e_0^2 = 2$ and $e_i^2 = -2$; this lattice is $M_X$, it equals $S_\Co$, $N_X = T_\Co$, and the covering involution acts on $H^2(X,\ZZ)\cong\lkt$ as $I_\Co^* = -\theta_\Co$ (@prop:theta-co-exists).
In that basis (@def:based-module)
$$
H = \tilde h_\Co = 6e_0 - 2\Sum_{i\le 8}e_i - e_9 - e_{10},
\qquad
\alpha = 3e_0 - \Sum_{i=1}^{10}e_i,
$$
and the two isotropic classes (@def:descent-class) $f^*F_1 = 3e_0-\Sum_{i\le9}e_i$ and $f^*F_2 = 3e_0-\Sum_{i\le8}e_i-e_{10}$ span a primitive $U(2)$ inside $S_\Co$ with $H = f^*F_1+f^*F_2$.
Taking $+1$ on that $U(2)$, $-1$ on its orthogonal complement $N\definedas\langle f^*F_1,f^*F_2\rangle^{\perp S_\Co}$ inside $S_\Co$, and $-\id$ on $T_\Co$ defines an integral isometry $\phi$ of $\lkt$: its $(+1)$-eigenspace is $\langle f^*F_1,f^*F_2\rangle\cong U(2)$, its $(-1)$-eigenspace is the negative definite (@def:definiteness) rank-$9$ lattice $N$ together with $T_\Co$, it fixes $H$, and it reverses $\alpha$.
:::

::: {.proof}

$\tilde C\cdot E_i = (6H - 2\Sum_j E_j)\cdot E_i = 2$, so $f^{-1}(E_i)\to E_i\cong\PP^1$ is a double cover branched at two points, hence a connected smooth rational curve; $E_i$ lies outside the branch locus, so $f^*E_i = [f^{-1}(E_i)]$ and $(f^*E_i)^2 = \deg(f)\,E_i^2 = -2$.
The span of the $e_i$ is $f^*\Pic(S)$, contained in $H^2(X,\ZZ)^{I_\Co}$; that group has rank $b_2(S) = 11$ by $\pi^*\pi_* = \id+\iota^*$ over $\QQ$, and $f^*\Pic(S)$ has rank $11$ and determinant $2^{11}\det\Pic(S) = 2^{11}$, which is also $\det S_\Co$ — since $\det T_\Co = 2^{11}$ and $[S_\Co\oplus T_\Co:\lkt] = 2^{11}$ — so the containment is an equality, and the coordinates of $H$ and $\alpha$ are those of $f^*(F_1+F_2)$ and $f^*(3H-\Sum_iE_i)$.
The covering involution is $+1$ on its invariant lattice $S_\Co$ and $-1$ on the orthogonal complement $T_\Co$ (@prop:involution_eigenspaces), which is $-\theta_\Co$.
The classes $f^*F_1, f^*F_2$ are isotropic with $f^*F_1\cdot f^*F_2 = 2$: in the display, $(f^*F_1)^2 = 18-18 = 0$, $(f^*F_2)^2 = 18-18 = 0$ and $f^*F_1\cdot f^*F_2 = 18-16 = 2$, and the pair is primitive in $S_\Co$ because $kv = ma+nb$ forces $k\mid m,n$ and then $v\in\langle a,b\rangle$.
The decomposition $S_\Co = \langle f^*F_1,f^*F_2\rangle\perp N$ is an orthogonal direct sum, because $\det\langle f^*F_1,f^*F_2\rangle\cdot\det N = (-4)(-512) = 2^{11} = \det S_\Co$.
On the two summands $\phi$ acts by $+1$ and by $-1$.
The discriminant groups $A_{S_\Co}$ and $A_{T_\Co}$ have exponent $2$, because $S_\Co\cong\latI_{1,10}(2)$ and $T_\Co$ is $2$-elementary (@prop:coinvariant_involution_2elementary), so $-1 = 1$ on both and the pair $(\phi|_{S_\Co}, -\id_{T_\Co})$ acts trivially on $A_{S_\Co}\oplus A_{T_\Co}$.
The gluing subgroup of $S_\Co\perp T_\Co$ is the graph of the anti-isometry $\gamma_\Co$ of @prop:coble-invariant-lattice, and an automorphism of $A_{S_\Co}\oplus A_{T_\Co}$ acting trivially on each factor preserves that graph; by @thm:automorphism-lifting-criterion the pair therefore extends, uniquely, to an isometry of $\lkt$.
That extension preserves $S_\Co$ and $T_\Co$, hence commutes (@def:commutative-diagram) with $I_\Co$, and it fixes $H$ because $H\in\langle f^*F_1,f^*F_2\rangle$.
Finally $\alpha\cdot f^*F_1 = 18-18 = 0$ and $\alpha\cdot f^*F_2 = 18-18 = 0$, so $\alpha\in N$ and $\phi(\alpha) = -\alpha$.
:::

::: {.lemma #lem:alpha-is-ramification-class title="The root $\alpha$ is the class of the ramification curve"}

In @prop:coble-cover-marking let $R\definedas f^{-1}(\tilde C)\subset X$ be the ramification curve.
Then $\alpha = [R]$; so $\alpha$ is effective and $-\alpha$ is the class of no effective divisor.
:::

::: {.proof}

The strict transform (@def:strict-transform) $\tilde C$ is smooth and $f$ is ramified along $R$ with index $2$, so $f^*[\tilde C] = 2[R]$.
With $[\tilde C] = 6H-2\Sum_iE_i = -2K_S$ this gives $2[R] = f^*(-2K_S) = 2\alpha$, and $H^2(X,\ZZ)$ is torsion-free, so $[R] = \alpha$.
If $D$ were effective with $[D] = -\alpha$, then $R+D$ would be a nonzero effective divisor of class $0$, whose intersection with an ample class is $0$, which is impossible.
:::

::: {.corollary #cor:coble-polarization-nef-big title="The degree-$4$ class is nef and big exactly when $h_\Co$ is nef"}

In @prop:coble-cover-marking let $h_\Co = 6H-2\Sum_{i\le8}E_i-E_9-E_{10} = F_1+F_2\in\Pic(S)$ (@def:coble-polarization-classes), so that $\tilde h_\Co = f^*h_\Co$.
Then $f^*h_\Co$ is nef and big if and only if $h_\Co$ is nef.
:::

::: {.proof}

By @prop:nef-big-finite-cover, $f^*h_\Co$ is nef if and only if $h_\Co$ is nef, and a nef class (@def:nef-cone) with $(f^*h_\Co)^2 = 2h_\Co^2 = 4>0$ is big.
:::

::: {.example #ex:coble-polarization-window title="$h_\Co$ against the exceptional curves, the branch curve and a window of $(-2)$-classes"}

Let $h_\Co$ be as in @cor:coble-polarization-nef-big.

1. On the ten exceptional curves $E_i$ of the blowup [@DK13, §3], $h_\Co\cdot E_i = 2$ for $i\le8$ and $h_\Co\cdot E_i = 1$ for $i = 9,10$.
2. On the branch curve $\tilde C = -2K_S = 6H-2\Sum_iE_i$, of self-intersection $-4$, $h_\Co\cdot\tilde C = 36-(8\cdot4+2+2) = 0$.
3. Let $W$ be the set of classes $x = aH-\Sum_ib_iE_i$ with $x^2 = -2$ and $0\le a\le3$. For each $a$ the classes with $x\cdot H = a$ form a coset of the negative definite lattice $H^{\perp} = \langle E_1,\dots,E_{10}\rangle$, so $W$ is finite. Enumeration of these cosets gives $\abs W = 193\,140$, of which $192\,929$ classes have $h_\Co\cdot x>0$, $150$ have $h_\Co\cdot x = 0$ and $61$ have $h_\Co\cdot x<0$.

The $61$ classes of the last kind are the $45$ classes $-E_i-E_j$ with $i<j$, on which $h_\Co$ takes the values $-4$, $-3$ and $-2$, and the $16$ classes $E_i-E_j$ with $i\in\set{9,10}$ and $j\le8$, on which $h_\Co$ takes the value $-1$: these lie in $W$ with $a = 0$ and there are $45+16 = 61$ of them.
None of them is effective.
The class $-E_i-E_j$ is the negative of a nonzero effective class.
An effective divisor $D$ with $H\cdot D = 0$ has only components contracted by the blowdown, because $H$ is nef, so it is a nonnegative combination of the $E_k$; the class $E_i-E_j$ is not.
So no effective class of $W$ pairs negatively with $h_\Co$.
:::

::: {.proposition #prop:coble-enriques-polarized-match title="The polarized Coble and Enriques embeddings are conjugate"}

Let $S_\Co$, $T_\Co = S_\Co^{\perp\lkt}$ and $H = \tilde h_\Co$ be as in @prop:coble-cover-marking, and let $M\definedas S_\En\oplus\ZZ\delta$, with $h = e+f\in S_\En$ the polarization (@def:numerical-polarization) of @prop:gamma-en-two-gluing and $\delta$ the Heegner vector of @lem:coble-heegner-vector.
Then $M = (\delta^{\perp\ten})^{\perp\lkt}$, and there is an isometry $\Phi\in\Orth(\lkt)$ with
$$
\Phi(S_\Co) = M,
\qquad
\Phi(T_\Co) = \delta^{\perp\ten},
\qquad
\Phi(H) = h
.$$
The vectors of square $-2$ in $H^{\perp S_\Co}$ are $\pm\alpha$, and $\Phi(\alpha) = -\delta$.
:::

::: {.proof}

*The complement.*
$S_\En$ is orthogonal to $\ten\supset\delta^{\perp\ten}$ and $\delta\perp\delta^{\perp\ten}$, so $M\subseteq(\delta^{\perp\ten})^{\perp\lkt}$.
The lattice $\delta^{\perp\ten}$ is primitive in $\ten$, which is primitive in $\lkt$, and $\lkt$ is unimodular, so $\abs{\det(\delta^{\perp\ten})^{\perp\lkt}} = \abs{\det\delta^{\perp\ten}} = \abs{\det T_\Co} = 2^{11}$.
Also $\abs{\det M} = \abs{\det S_\En}\cdot\abs{\delta^2} = 2^{10}\cdot 2 = 2^{11}$, and both lattices have rank $11$, so $M = (\delta^{\perp\ten})^{\perp\lkt}$.

*An isometry $\psi\colon S_\Co\to M$ with $\psi(H) = h$.*
$\Pic(S)\cong\latI_{1,10}$ is unimodular, and $K_S^2 = -1$, so $\Pic(S) = \ZZ K_S\perp K_S^{\perp}$ with $K_S^{\perp}\cong U\oplus E_8$ even unimodular (@prop:canonical-perp-is-e10).
The classes $F_1 = 3H_{\PP^2}-\Sum_{i\le9}E_i$ and $F_2 = 3H_{\PP^2}-\Sum_{i\le8}E_i-E_{10}$ of the plane model satisfy $\Sum_i b_i = 9 = 3a$, so they lie in $K_S^{\perp}$, and $F_i^2 = 0$, $F_1\cdot F_2 = 1$; so $\langle F_1,F_2\rangle\cong U$ is unimodular and $K_S^{\perp} = \langle F_1,F_2\rangle\perp E'$ with $E'$ even, unimodular and negative definite (@def:definiteness) of rank $8$, hence $E'\cong E_8$.
Pullback along $f$ multiplies the form by $2$ and $S_\Co = f^*\Pic(S)$ (@prop:coble-cover-marking), so
$$
S_\Co = \langle f^*F_1, f^*F_2\rangle\perp\ZZ f^*K_S\perp f^*E'
\cong U(2)\oplus\generators{-2}\oplus E_8(2)
.$$
Define $\psi$ by $f^*F_1\mapsto e$, $f^*F_2\mapsto f$, $f^*K_S\mapsto\delta$, and an isometry $f^*E'\iso E_8(2)$ onto the $E_8(2)$ summand of $S_\En$.
It is an isometry $S_\Co\iso M$, $\psi(H) = \psi(f^*F_1+f^*F_2) = e+f = h$, and $\psi(\alpha) = \psi(-f^*K_S) = -\delta$.

*The roots of $H^{\perp}$.*
Inside $U(2)$ the complement of $h = e+f$ is $\ZZ(e-f)$, of square $-4$, so $\psi(H^{\perp S_\Co}) = h^{\perp M} = \ZZ(e-f)\oplus E_8(2)\oplus\ZZ\delta$.
A vector $x = c(e-f)+v+d\delta$ there has $x^2 = -4c^2+v^2-2d^2$ with $v^2\in 4\ZZ_{\le0}$, so $x^2 = -2$ forces $c = 0$, $v = 0$ and $d = \pm1$.
So the vectors of square $-2$ in $h^{\perp M}$ are $\pm\delta = \mp\psi(\alpha)$.

*Extension to $\lkt$.*
Let $\gamma_\Co\colon A_{S_\Co}\iso A_{T_\Co}$ and $\gamma_M\colon A_M\iso A_{\delta^{\perp\ten}}$ be the gluing anti-isometries of the two primitive embeddings into $\lkt$, and choose any isometry $\varphi_0\colon T_\Co\iso\delta^{\perp\ten}$, which exists because $\delta^{\perp\ten}\cong T_\Co$ (@lem:coble-heegner-vector).
The map $\bar\varphi_0^{-1}\gamma_M\bar\psi\gamma_\Co^{-1}$ is an isometry of $q_{T_\Co}$, so by @thm:two-elementary-surjectivity it is $\bar\chi$ for some $\chi\in\Orth(T_\Co)$.
Then $\varphi\definedas\varphi_0\chi$ satisfies $\bar\varphi\gamma_\Co = \gamma_M\bar\psi$, so $\psi\oplus\varphi$ maps the graph of $\gamma_\Co$ to the graph of $\gamma_M$, and by Nikulin's gluing theorem (@thm:nikulin-gluing) it extends to an isometry $\Phi$ of the common overlattice $\lkt$, which restricts to $\psi$ on $S_\Co$.
:::

::: {.proposition #prop:coble-enriques-ambient-isometry title="The isometry of the comparison, built"}
The isometry $\Phi$ of @prop:coble-enriques-polarized-match exists as an integral isometry of $\lkt$.
In the model $\lkt = U^3\oplus 2E_8(-1)$ with standard basis $e_0,\dots,e_{21}$ and blocks $U_1 = \langle e_0,e_1\rangle$, $U_2 = \langle e_2,e_3\rangle$, $U_3 = \langle e_4,e_5\rangle$, $E_{8,1} = \langle e_6,\dots,e_{13}\rangle$, $E_{8,2} = \langle e_{14},\dots,e_{21}\rangle$, let $I_{\mathrm{dP}}, I_\En$ be the two involutions of [@AEGS25, Def. 2.3], $w$ the reflection in $\alpha = e_0-e_1$, and $J_\Co = wI_\En$, $J_{\mathrm{dP}} = wI_{\mathrm{dP}}$; write $\Delta$, $\Delta^-$ for the diagonal and antidiagonal copies of a summand in a split sum, and put
$$
S_\Co = \ker(J_\Co-\id),\qquad T_\Co = S_\Co^{\perp\lkt},\qquad \delta = e_0-e_1,
$$
$$
M = \Delta(U_2,U_3)\oplus\Delta(E_{8,1},E_{8,2})\oplus\ZZ\delta,\qquad H = h = e_2+e_3+e_4+e_5.
$$
Then:

1. $S_\Co\cong U(2)\oplus\generators{-2}\oplus E_8(2)$, $T_\Co = S_\Co^{\perp\lkt}\cong\generators{2}\oplus U(2)\oplus E_8(2)$, and $H\in S_\Co$ has $H^2 = 4$, $H\cdot\alpha = 0$, with $H$ and $\alpha$ primitive of divisibility (@def:lattice-divisibility) $2$ in $S_\Co$; $H$ is the corner of the primitive $U(2) = \Delta(U_2,U_3)\subseteq S_\Co$, which is $\sdp$;
2. $\Delta(U_2,U_3)\oplus\Delta(E_{8,1},E_{8,2}) = S_\En$, and $M = S_\En\oplus\ZZ\delta$ with $\delta^2 = -2$, $\delta\in S_\En^{\perp\lkt}$, $h^2 = 4$, $h\cdot\delta = 0$, $M\cong S_\Co$ and $M^{\perp\lkt} = \delta^{\perp T_\En}\cong T_\Co$;
3. $S_\Co = M$ and $H = h$, as sublattices and as classes of $\lkt$: the Coble invariant lattice is the Enriques one plus the line $\ZZ\alpha$;
4. the map $g$ exchanging $e_0$ and $e_1$ and fixing $e_2,\dots,e_{21}$ is an integral involution of $\lkt$ with
$$
g(S_\Co) = M,\qquad g(T_\Co) = M^{\perp\lkt},\qquad g(H) = h,\qquad g(\alpha) = -\delta,
$$
fixing the slot $U(2) = \Delta(U_2,U_3)$ pointwise and commuting with $I_{\mathrm{dP}}$, $I_\En$, $J_\Co$ and $J_{\mathrm{dP}}$.
:::

::: {.proof}

Every assertion is a check at the owner on the objects, in `computations/reports/coble_a21-ambient-extension.py`, transcript `-run.txt`, sage-extensions at provider main `1488acf`, Sage 11.0.beta5; the run takes about ninety seconds and prints each line below.

*The two embeddings.* $S_\Co$, $S_\En$, $T_\Co$, $T_\En$, $M$ and $M^{\perp\lkt}$ are built as primitive sublattices by `primitive_sublattice_from` and `orthogonal_complement`, and their types are decided by `is_isometric_to` against the model lattices: the ranks $11, 10, 11, 12, 11, 11$, the determinants $2^{11}$, $-2^{10}$, $-2^{11}$, $2^{10}$, $2^{11}$, $-2^{11}$ and the signatures $(1,10)$, $(1,9)$, $(2,9)$, $(2,10)$, $(1,10)$, $(2,9)$ of parts 1 and 2 are the owner's, and $M\cong S_\Co$ is the owner's `is_isometric_to` (`True`). The classes $H$, $h$, $\alpha$, $\delta$ are entered as integral vectors and their squares, their pairing, their primitivity in $S_\Co$ and in $M$ (as the coordinate test $H\notin 2S_\Co$, $\alpha\notin 2S_\Co$, $\delta\notin 2M$) are computed. Part 3 is two containment tests in both directions, `S_Co contained in M` and `M contained in S_Co`, together with the vector equality $H = h$.

*The isometry.* $g$ is entered by its images on the standard basis and accepted by `L.O()`, so the isometry property is the constructor's; the pairing is separately checked on all $22\cdot22$ pairs, $g^2 = \id$ on the basis, and the matrix of $g$ on the standard basis is the permutation matrix of $e_0\leftrightarrow e_1$, of determinant $-1$. The four labelled images of part 4 are equalities of lattice elements, and $g(S_\Co) = M$, $g(T_\Co) = M^{\perp\lkt}$ are equality of sublattices, tested by exact coordinates in each other's bases (@def:based-module). Commutation with the four involutions is checked on the basis.

*The criterion.* The two gluing anti-isometries $\gamma_\Co$ and $\gamma_M$ are built by `gluing_anti_isometry` from the two finite-index inclusions $S_\Co\oplus T_\Co\injects\lkt$ and $M\oplus M^{\perp\lkt}\injects\lkt$, each of index $2^{11}$ with glue subgroup of order $2048$ in $A_{S_\Co\oplus T_\Co}$; the restriction $g|_{S_\Co}\oplus g|_{T_\Co}$ is an isometry of $S_\Co\oplus T_\Co$ and `isometry_extends` returns `True`, which is @thm:automorphism-lifting-criterion applied to it, that is exactly the equation $\bar\varphi\gamma_\Co = \gamma_M\bar\psi$. Since the pair is the restriction of an isometry of $\lkt$ that the owner has already accepted, the criterion is satisfied by the construction of $g$ and not searched for after it.

*The surjectivity input.* $\rho_{S_\Co}\colon\Orth(S_\Co)\to\Orth(A_{S_\Co})$ and $\rho_{T_\Co}\colon\Orth(T_\Co)\to\Orth(A_{T_\Co})$ are both decided surjective at this provider (`discriminant_representation_is_surjective` returns `True` for each), which is @thm:two-elementary-surjectivity instantiated; the pinned-provider `TypeError` at `recursive.py:154` recorded for $T_\Co$ under A20 item 1 does not reproduce at this provider.
:::

::: {.remark title="What the object settles, and what it does not"}

What it settles is the last step of A20 item 2 as stated: the comparison of the labelled Coble and Enriques data is carried by an exhibited element of $\Orth(\lkt)$ rather than by an argument that one exists, and its action on every label is an equality of lattice elements. Part 3 sharpens @prop:coble-enriques-polarized-match: in this marking the two primitive embeddings coincide, the degree-$4$ class of the Coble tuple is the degree-$2$ class of the Enriques tuple, the del Pezzo slot $\sdp$ is the Enriques polarization, and the whole labelled difference between the two data is the sign of the root, which $g$ reverses.

What it does not settle. It does not settle the chamber clause, and by @thm:chamber-clause-fails that clause is false: a chamber is cut from the effective classes of a member, no isometry of $\lkt$ decides effectivity, and $g$ transports the lattice labels and not $\mcc$. It does not reach the multi-node locus either, and need not: $S_{\mathrm{dP}}$ has rank $k+2$ (@prop:tuple-of-the-construction, part 5), so the tuple of a one-node member and that of a two-node member are never conjugate (@prop:node-count-invariant), and @prob:coble-rigidity fails there before the chamber is reached; the one question left on that locus, the saturation identity of @qst:del-pezzo-saturation-higher-k for $k\ge2$, is a lattice question on which no reading of @prob:coble-rigidity depends. The block-compatibility of $\gamma$ and $\gamma_\Co$ of @def:congruence-group is decided separately, on the two gluings as objects: @prop:coble-block-compatibility answers it affirmatively for both.

The Coble-to-Coble content of @prob:coble-rigidity is @thm:a21-labels on the one-node locus, by parallel transport, and that is all of it that survives: the chamber clause fails (@thm:chamber-clause-fails) and the node count separates the strata of the construction (@prop:node-count-invariant). The object here is the Coble-to-Enriques comparison that A20 item 2 needs, and it does not extend @thm:a21-labels beyond that locus.
:::

::: {.theorem #thm:theta-co-coordinates title="The sign involution of the Coble embedding in coordinates"}

In the model $\lkt = U^3\oplus E_8^2$ of @prop:coble-enriques-ambient-isometry, with standard basis (@def:based-module) $e_0,\dots,e_{21}$ and blocks
$$
U_1 = \generators{e_0,e_1},\quad U_2 = \generators{e_2,e_3},\quad U_3 = \generators{e_4,e_5},\quad
E_{8,1} = \generators{e_6,\dots,e_{13}},\quad E_{8,2} = \generators{e_{14},\dots,e_{21}},
$$
let $I_\En$ be the Enriques involution of [@AEGS25, Def. 2.3], let $\alpha = e_0-e_1$, and let $w = s_\alpha$ be the reflection in $\alpha$, so that $J_\Co \definedas w\,I_\En$ is the involution of @prop:coble-enriques-ambient-isometry with invariant lattice $S_\Co = \ker(J_\Co-\id)$.
Then the sign involution $\theta_\Co$ of @prop:theta-co-exists is, in this marking,
$$
\theta_\Co = -J_\Co = -w\,I_\En .
$$
On the standard basis it is the signed permutation
$$
\theta_\Co(e_0) = e_1,\quad \theta_\Co(e_1) = e_0,\quad
\theta_\Co(e_2) = -e_4,\quad \theta_\Co(e_4) = -e_2,\quad
\theta_\Co(e_3) = -e_5,\quad \theta_\Co(e_5) = -e_3,
$$
$$
\theta_\Co(e_{6+k}) = -e_{14+k},\qquad \theta_\Co(e_{14+k}) = -e_{6+k},
\qquad k = 0,\dots,7,
$$
that is, the $22\times22$ matrix whose blocks are indexed by $(U_1,U_2,U_3,E_{8,1},E_{8,2})$,
$$
\Theta =
\begin{pmatrix}
P & 0 & 0 & 0 & 0\\
0 & 0 & -I_2 & 0 & 0\\
0 & -I_2 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & -I_8\\
0 & 0 & 0 & -I_8 & 0
\end{pmatrix},
\qquad
P = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix},
$$
with $\Theta\in M_{22}(\bZ)$, $\Theta^2 = \id$, $\Theta^{\mathsf T}G\Theta = G$ for the Gram matrix $G$ of $\lkt$, $\trace\Theta = 0$ and $\det\Theta = -1$.

Its eigenspaces have the following bases (@def:based-module) in the same coordinates:
$$
\lkt^{\theta_\Co} = T_\Co = \generators{e_0+e_1,\; e_2-e_4,\; e_3-e_5,\; e_{6+k}-e_{14+k}\ (k = 0,\dots,7)},
$$
$$
\lkt^{-\theta_\Co} = S_\Co = \generators{e_0-e_1,\; e_2+e_4,\; e_3+e_5,\; e_{6+k}+e_{14+k}\ (k = 0,\dots,7)},
$$
with Gram matrices $\generators{2}\perp U(2)\perp E_8(2)$ and $\generators{-2}\perp U(2)\perp E_8(2)$, the three blocks being pairwise orthogonal in each, the $E_8(2)$ block being negative definite of determinant $2^8 = 256$, its Gram matrix in the basis $e_{6+k}-e_{14+k}$ being $-2\,\mathrm{Cartan}(E_8)$, of diagonal entries $-4$ and off-diagonal entries $0$ or $2$: that is $E_8(2) = 2E_8$ in the convention of @def:enriques-lattice, and not the diagonal lattice $\generators{-4}^{8}$, whose determinant is $4^8$. Both lattices have rank $11$, discriminant group $(\bZ/2\bZ)^{11}$ and coparity $\delta = 1$, so by Nikulin's classification [@Nik80, Thm. 3.6.2] each is determined by its signature: $T_\Co\cong\generators{2}\oplus U(2)\oplus E_8(2)$ of @prop:theta-co-exists, of determinant $-2^{11}$ and signature $(2,9)$, and $S_\Co\cong\generators{2}\oplus\generators{-2}^{10} = \latI_{1,10}(2)$ of @prop:coble-invariant-lattice, of determinant $2^{11}$ and signature $(1,10)$. The two are orthogonal and of index
$$
[\lkt : S_\Co\oplus T_\Co] = 2^{11}.
$$

The degree-$4$ Coble class is $H = \tilde h_\Co = e_2+e_3+e_4+e_5$ in this marking, with $H^2 = 4$ and $H\cdot\alpha = 0$, and
$$
\theta_\Co(H) = -H,
\qquad
\theta_\Co(\alpha) = -\alpha .
$$

The matrix is a representative and not an invariant of $\lkt$ alone: if $\theta'$ is any involution of $\lkt$ whose $(+1)$- and $(-1)$-eigenspaces are isometric to $T_\Co$ and $S_\Co$, then $\theta'$ is $\Orth(\lkt)$-conjugate to $\theta_\Co$. Hence every marking of the Coble pair presents $\theta_\Co$ by a matrix conjugate to $\Theta$, and $\Theta$ exhibits the coordinates of $\theta_\Co$ up to that conjugacy.
:::

::: {.proof}

**The matrix.** The block $P$ exchanges the two isotropic generators of the unimodular plane $U_1$: its Gram matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ is $P$-invariant and $P^2 = \id$. The block on $U_2\oplus U_3$ sends $(u,u')$ to $(-u',-u)$, so it multiplies $\langle (u,u'),(v,v')\rangle = u\cdot v + u'\cdot v'$ by $(-1)(-1) = 1$, and its square is the identity; the same computation applies to $E_{8,1}\oplus E_{8,2}$, whose form is likewise the orthogonal sum (@def:orthogonal-sum) of two isometric summands. Hence $\Theta^{\mathsf T}G\Theta = G$ and $\Theta^2 = \id$, and $\Theta$ is integral. Its trace is $0$ because every diagonal entry is $0$, and its determinant is $(-1)^{11}$: $\Theta$ moves the basis only through the eleven transpositions $(e_0\,e_1)$, $(e_2\,e_4)$, $(e_3\,e_5)$ and $(e_{6+k}\ e_{14+k})$, and the $2\times2$ block carrying each of them is $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ in the first case and $\begin{pmatrix}0&-1\\-1&0\end{pmatrix}$ in the other ten, of determinant $-1$ in every case.

**The eigenspaces.** Each vector of the first display is fixed and each vector of the second is negated: $\theta_\Co(e_0+e_1) = e_1+e_0$, $\theta_\Co(e_2-e_4) = -e_4+e_2$, $\theta_\Co(e_{6+k}-e_{14+k}) = -e_{14+k}+e_{6+k}$, and the same three computations with the signs reversed give $\theta_\Co(e_0-e_1) = -e_0+e_1$, $\theta_\Co(e_2+e_4) = -e_2-e_4$ and $\theta_\Co(e_{6+k}+e_{14+k}) = -e_{6+k}-e_{14+k}$. The eleven vectors of each display are linearly independent. Both eigenspaces therefore have rank $11$: $\trace\Theta = 0$ gives $\dim\lkt^{\theta_\Co} = \dim\lkt^{-\theta_\Co}$, and the two dimensions sum to $22$. Each display is thus a basis of its eigenspace. Both eigenspaces are primitive, as the eigenspaces of an integral involution always are: $kx\in\ker(\theta_\Co-\id)$ implies $\theta_\Co(x) = x$.

**The Gram matrices and the types.** In the first display $e_0+e_1$ has square $2$ and is orthogonal to the other ten vectors; $e_2-e_4$ and $e_3-e_5$ are isotropic and pair to $e_2\cdot e_3+e_4\cdot e_5 = 2$, so they span $U(2)$; and $e_{6+k}-e_{14+k}$ has square $-4$ and pairs with $e_{6+j}-e_{14+j}$ to $e_{6+k}\cdot e_{6+j} + e_{14+k}\cdot e_{14+j}$ --- the two cross terms vanish because $E_{8,1}$ and $E_{8,2}$ are orthogonal --- so these eight span $E_8(2)$, whose determinant is $2^8$. In the second display the same computation with the signs reversed gives the same three Gram matrices, with $\generators{-2}$ in place of $\generators{2}$. The ranks, determinants, signatures, Smith normal forms $(\bZ/2\bZ)^{11}$ and coparities $\delta = 1$ of the two Gram matrices, and the identity $[\lkt:S_\Co\oplus T_\Co] = 2^{11}$, are recorded in `computations/reports/coble_a13-theta-coordinates-run.txt`. Nikulin's classification [@Nik80, Thm. 3.6.2] then identifies the two isometry classes from the signature, the number $a = \dim_{\F_2}A_L = 11$ of generators of the discriminant group and the coparity $\delta = 1$, both lattices being indefinite.

**The identification with $\theta_\Co$.** By @prop:theta-co-exists the sign involution $\theta_\Co$ is the isometry of $\lkt$ that is $-\id$ on $S_\Co$ and $\id$ on $T_\Co$, and $J_\Co$ is $+\id$ on $S_\Co$ and $-\id$ on $T_\Co$ by the definition of $S_\Co$ in @prop:coble-enriques-ambient-isometry and the primitivity of the eigenspaces; so $-J_\Co$ has exactly the two restrictions that define $\theta_\Co$. Two isometries of $\lkt$ agreeing on $S_\Co$ and on $T_\Co$ agree on $\lkt$, since $S_\Co\oplus T_\Co$ has finite index in $\lkt$. The two labelled images are values of the displayed matrix: $\theta_\Co(e_2+e_3+e_4+e_5) = -e_4-e_5-e_2-e_3$ and $\theta_\Co(e_0-e_1) = e_1-e_0$.

::: {.remark title="Which record decides what, and which one is the construction #81 asks for"}

research#81 requires the matrix to be a derived presentation of the morphism: the lattice built from named summands, the involution defined on those summands, the eigenspaces taken as the invariant lattices $\ker(\theta_\Co\pm\id)$, each a primitive sublattice with its inclusion retained, and only then the matrix — "hard-coding the matrix, expected eigenspace bases or target invariants does not complete this issue".
That construction is `computations/reports/coble_a13-library-construction.py`, its transcript `-run.txt`: $\lkt$ from $\mathrm{block\_diagonal}(U,U,U,E_8,E_8)$, $I_\En$ and $I_{\mathrm{dP}}$ defined by their action on those summands and built through the library's isometry constructor, $w$ as `L.reflection` in $\alpha$, $J_\Co = wI_\En$ and $\theta_\Co = -J_\Co$ built by the isometry constructor, the order-two equation decided inside $\Orth(\lkt)$ and again on the standard basis, then the invariant lattices $S_\Co = \ker(\theta_\Co+\id)$ and $T_\Co = \ker(\theta_\Co-\id)$, each taken as a primitive sublattice with its inclusion through `primitive_sublattice_from`, $T_\Co$ cross-checked against `orthogonal_complement`, the types decided by an exhibited isometry onto $\langle2\rangle\oplus\langle-2\rangle^{10}$ and onto $\langle2\rangle\oplus U(2)\oplus E_8(2)$, printed as a matrix, verified entry by entry as $M^{\mathsf T}GM = G$ and onto an embedded sublattice equal to the eigenspace, the index and the gluing from the finite-index inclusion through `gluing_anti_isometry`, the chain $T_\Co\to\ten\to\tdp\to\lkt$ as four more saturated kernels, and the nineteen diagram roots as lattice elements whose Gram entries are the library's pairings. Every number it prints agrees with the theorem above.

The six records `coble_a13-theta-coordinates`, `-gluing-anti-isometry`, `-heegner-comparison`, `-diagram-roots`, `-chain-matrices` and `coble_explicit-sextic` are exact and provider-free, and serve as the independent cross-check: they re-derive every displayed value with integer and rational arithmetic alone, and each of them reproduces its committed transcript. They are not the construction, and this remark exists so that no reader takes them for it.
:::

**The conjugacy class.** Let $\theta'$ be an involution of $\lkt$ with eigenspaces $T' = \lkt^{\theta'}$ and $S' = \lkt^{-\theta'}$ isometric to $T_\Co$ and $S_\Co$, and choose isometries $\psi\colon S'\iso S_\Co$ and $\varphi\colon T'\iso T_\Co$. Let $\gamma$, $\gamma'$ be the gluing anti-isometries of the two primitive embeddings $S_\Co\oplus T_\Co\injects\lkt$ and $S'\oplus T'\injects\lkt$, which exist by @thm:nikulin-gluing and are isomorphisms $A_{S_\Co}\iso A_{T_\Co}(-1)$ and $A_{S'}\iso A_{T'}(-1)$. By the lifting criterion (@thm:automorphism-lifting-criterion), $\psi\oplus\varphi$ extends to an isometry of $\lkt$ exactly when its discriminant action carries the graph of $\gamma'$ to the graph of $\gamma$, that is when
$$
\bar\varphi\,\gamma' = \gamma\,\bar\psi
,
$$
where $\bar\psi\colon A_{S'}\iso A_{S_\Co}$ and $\bar\varphi\colon A_{T'}\iso A_{T_\Co}$ are the induced maps. The composite $\eta_0\definedas\bar\varphi^{-1}\gamma\bar\psi\gamma'^{-1}$ is read from right to left as $\gamma'^{-1}\colon A_{T'}(-1)\iso A_{S'}$, then $\bar\psi$, then $\gamma\colon A_{S_\Co}\iso A_{T_\Co}(-1)$, so it is an isometry $A_{T'}(-1)\iso A_{T'}(-1)$, that is an element of $\Orth(q_{T'})$; and $\rho_{T'}$ is onto for the even indefinite $2$-elementary lattice $T'$ [@thm:two-elementary-surjectivity, which is @Nik80, Thm. 3.6.3], so $\eta_0 = \bar\eta$ for some $\eta\in\Orth(T')$. With $\varphi_1\definedas\varphi\circ\eta$ one has $\bar\varphi_1\gamma' = \bar\varphi\,\bar\varphi^{-1}\gamma\bar\psi = \gamma\bar\psi$, so the pair $(\psi,\varphi_1)$ is compatible with the two gluings and $\psi\oplus\varphi_1$ extends over the common overlattice $\lkt$ to an isometry $\Phi$ with $\Phi|_{S'} = \psi$ and $\Phi|_{T'} = \varphi_1$. Then $\Phi\theta'\Phi^{-1}$ is the involution that is $-\id$ on $\Phi(S') = S_\Co$ and $+\id$ on $\Phi(T') = T_\Co$, that is $\theta_\Co$, an involution being determined by its eigenspaces.
:::

::: {.theorem #thm:gamma-co-coordinates title="The Coble gluing anti-isometry in coordinates"}

In the marking of @thm:theta-co-coordinates put $\alpha = e_0-e_1$ and $\beta = e_0+e_1$, and let $\iota$ be the identification of $U_2 = \generators{e_2,e_3}$ with $U_3 = \generators{e_4,e_5}$ given by $e_2\mapsto e_4$ and $e_3\mapsto e_5$, and of $E_{8,1} = \generators{e_6,\dots,e_{13}}$ with $E_{8,2} = \generators{e_{14},\dots,e_{21}}$ given by $e_{6+k}\mapsto e_{14+k}$. Write $\Delta(V_1,V_2)$ and $\Delta^-(V_1,V_2)$ for the diagonal (@def:polarization-functors) and antidiagonal copies of $V_1\oplus V_2$ in a doubled sum, and put $\Delta(V) := \Delta(V,\iota V)$ and $\Delta^-(V) := \Delta^-(V,\iota V)$ for $V = U_2$ and for $V = E_{8,1}$, so that there
$$
S_\Co = \generators{\alpha}\oplus\Delta(U_2,U_3)\oplus\Delta(E_{8,1},E_{8,2}),
\qquad
T_\Co = \generators{\beta}\oplus\Delta^-(U_2,U_3)\oplus\Delta^-(E_{8,1},E_{8,2}).
$$
Then the gluing anti-isometry $\gamma_\Co\colon A_{S_\Co}\iso A_{T_\Co}$ of @prop:theta-co-exists is
$$
\gamma_\Co\bigl([\alpha/2]\bigr) = [\beta/2],
\qquad
\gamma_\Co\bigl([(w,w)/2]\bigr) = [(w,-w)/2]
$$
for every $w$ in $U_2$ and every $w$ in $E_{8,1}$, with $(w,\pm w) := w\pm\iota(w)$; equivalently $\gamma_\Co$ is the identity map $A_{\Delta(V)}\iso A_{\Delta^-(V)}$ read through $w\mapsto (w,w)/2$ and $w\mapsto(w,-w)/2$. In particular:

1. the formula is well defined on classes and bijective, because $(w,w)/2\in\Delta(V)$ forces $w\in 2V$, so $w\mapsto(w,w)/2$ is injective (@def:injective-map) on $V/2V$, whose order is that of $A_{\Delta(V)}$;
2. the eleven gluing vectors of the inclusion $S_\Co\oplus T_\Co\injects\lkt$ are the standard basis vectors
$$
\alpha/2+\beta/2 = e_0,\qquad (e_2+e_4)/2+(e_2-e_4)/2 = e_2,\qquad e_3,\qquad e_{6+k}\ (k = 0,\dots,7),
$$
and $\det[s_1,\dots,s_{11},\,e_0,e_2,e_3,e_6,\dots,e_{13}] = 1$, so that $\lkt = \generators{S_\Co, e_0, e_2, e_3, e_6,e_7,\dots,e_{13}}$: the eleven values determine $\gamma_\Co$ on the whole of $A_{S_\Co}$ and not only up to a coset;
3. $q_{T_\Co}\circ\gamma_\Co = -q_{S_\Co}$ on all $2048$ classes of $A_{S_\Co}$, and $b_{T_\Co}(\gamma_\Co x,\gamma_\Co x') = -b_{S_\Co}(x,x')$, so the displayed map is an anti-isometry;
4. it is block-compatible in the sense of @def:congruence-group, with the two blocks and the remaining class explicit: $\gamma_\Co(A_{\Delta(U_2,U_3)}) = A_{\Delta^-(U_2,U_3)}$, $\gamma_\Co(A_{\Delta(E_{8,1},E_{8,2})}) = A_{\Delta^-(E_{8,1},E_{8,2})}$ and $\gamma_\Co([\alpha/2]) = [\zeta/2]$ for $\zeta = \beta$; this is the marked instance of @prop:coble-block-compatibility;
5. the class of the degree-$4$ polarization (@def:numerical-polarization) goes to
$$
\gamma_\Co\bigl([H/2]\bigr) = [(e_2+e_3-e_4-e_5)/2],
$$
of value $-q_{S_\Co}(\overline{H/2}) = -H^2/4 \equiv -1 \pmod{2\ZZ}$, and the vector that @prop:rank-one-slot(3) asks for is
$$
t = \tfrac12\bigl(-3e_2-e_3+3e_4+e_5\bigr) - e_6 + e_{14},
\qquad
t^2 = -1,
$$
whose class in $T_\Co^{\#} = \tfrac12T_\Co$ is $\gamma_\Co([H/2])$; with $b\definedas H/2+t = -e_2+2e_4+e_5-e_6+e_{14}$ one has $b\in\lkt$, $b^2 = 0$, $b\cdot H = 2$ and $b\perp H^{\perp S_\Co}$, the lattice $\langle H,b\rangle$ has Gram matrix $\begin{pmatrix}4&2\\2&0\end{pmatrix}$ and is $U(2)$, and the involution $J$ with $(+1)$-eigenspace $\langle H,b\rangle$ is integral, fixes $H$ and $b$, preserves the form and commutes (@def:commutative-diagram) with $\theta_\Co$.
:::

::: {.proof}

Every value below is printed in `computations/reports/coble_a13-gluing-anti-isometry-run.txt`, sections 1--8: the two Gram matrices and the index, the eleven classes and their images, the determinant, the $2048$ values of $q$ and the $121$ bilinear pairs, the block images, the marked class, the vector $t$ and the involution $J$. The text gives the reasons; the transcript gives the decisions.

**How a class is read off.** By Nikulin's gluing theorem (@thm:nikulin-gluing) the gluing subgroup of $A_{S_\Co}\oplus A_{T_\Co}$ is the graph of $\gamma_\Co$: for $x\in S_\Co^{\#}$ and $y\in T_\Co^{\#}$ the class $(x,y)$ lies in it if and only if $x+y\in\lkt$, and then $y$ represents $\gamma_\Co(x)$. The graph meets each fibre over $A_{S_\Co}$ in exactly one class, so an exhibited $y$ is a decision and not a choice.

**The classes are a basis.** Each of $[\alpha/2]$, $[(e_2+e_4)/2]$, $[(e_3+e_5)/2]$ and $[(e_{6+k}+e_{14+k})/2]$ is represented by a vector whose pairings with the $S_\Co$-basis $(\alpha,\,e_2+e_4,\,e_3+e_5,\,e_{6+k}+e_{14+k})$ are integers, so it is a class of $A_{S_\Co}$; and the $2^{11} = 2048$ sums of these eleven are distinct, which is the order of $A_{S_\Co}$, so they are a $\Z/2$-basis.

**The images.** The announced sums are integral vectors of $\lkt$: $\alpha/2+\beta/2 = e_0$, $(e_2+e_4)/2+(e_2-e_4)/2 = e_2$, $(e_3+e_5)/2+(e_3-e_5)/2 = e_3$ and $(e_{6+k}+e_{14+k})/2+(e_{6+k}-e_{14+k})/2 = e_{6+k}$. For each of the eleven classes, the classes of $A_{T_\Co}$ whose representative $y$ makes $x+y$ integral were enumerated — the $2048$ classes $\tfrac12\sum\epsilon_jt_j$ of $T_\Co^{\#} = \tfrac12T_\Co$ — and exactly one does, the announced one. Hence the display is $\gamma_\Co$ on a basis of $A_{S_\Co}$, and by linearity on all of $A_{S_\Co}$.

**Why the basis values are the whole map.** The $22\times22$ determinant $\det[s_1,\dots,s_{11},e_0,e_2,e_3,e_6,\dots,e_{13}]$ is $1$, so $\lkt$ is generated over $\Z$ by $S_\Co$ and those eleven vectors; an element of $A_{S_\Co}$ is therefore the class of a vector of $S_\Co^{\#}$ whose sum with the corresponding half of those vectors lies in $\lkt$, and no coset ambiguity is left.

**The anti-isometry.** For each of the $2048$ classes $x = \sum\epsilon_ix_i$ with its image $y = \sum\epsilon_iy_i$ one has $x+y\in\lkt$ and hence $q_{S_\Co}(x)+q_{T_\Co}(y)\equiv0$ modulo $2\Z$, that is $q_{T_\Co}(\gamma_\Co x) = -q_{S_\Co}(x)$; the bilinear relation $b_{T_\Co}(\gamma_\Co x,\gamma_\Co x')\equiv -b_{S_\Co}(x,x')$ modulo $\Z$ holds on the $121$ pairs of basis classes and hence everywhere. Both signs are the ones of @prop:theta-co-exists, in the convention $q_L(\bar x) = x^2$ modulo $2\Z$ of @def:discriminant that @prop:rank-one-slot(2) uses.

**The blocks.** For $V$ one of $U_2$ and $E_{8,1}$, the map $w\mapsto[(w,w)/2]$ is a group homomorphism $V/2V\to A_{\Delta(V)}$, injective because $(w,w)/2\in\Delta(V)$ forces $w\in2V$, and $|V/2V| = |A_{\Delta(V)}|$: $|U_2/2U_2| = 4 = |A_{\Delta(U_2,U_3)}|$, because $\Delta(U_2,U_3)\cong U(2)$ has determinant $-4$, and $|E_{8,1}/2E_{8,1}| = 2^8 = |A_{E_8(2)}|$, because $\det E_8(2) = 2^8$; so it is an isomorphism. The gluing is the graph of an anti-isometry [@Nik80, Prop. 1.5.1 and Cor. 1.5.2], and the display says that $\gamma_\Co$ carries $A_{\Delta(V)}$ onto $A_{\Delta^-(V)}$ and $[\alpha/2]$ to $[\beta/2]$. That is @prop:coble-block-compatibility for $\gamma_\Co$ in this marking, obtained here as a consequence of the formula rather than by a search over the two blocks.

**The marked class and $t$.** $H$ has divisibility $2$ in $S_\Co$ — $H\cdot\alpha = 0$, $H\cdot(e_2+e_4) = H\cdot(e_3+e_5) = 2$ and $H\cdot(e_{6+k}+e_{14+k}) = 0$ — so $\overline{H/2}$ is a class, and $H/2 = (u,u)/2$ with $u = e_2+e_3$, whence $\gamma_\Co(\overline{H/2}) = [(u,-u)/2] = [(e_2+e_3-e_4-e_5)/2]$ and its square is $((e_2+e_3-e_4-e_5)/2)^2 = 1 \equiv -1 = -q_{S_\Co}(\overline{H/2}) \pmod{2\ZZ}$. The displayed $t$ satisfies $2t\in T_\Co$, $t\cdot T_\Co\subseteq\Z$ and $t^2 = -1$, so it is the vector of @prop:rank-one-slot(3) with that class; then $b = H/2+t$ is an integral vector because the two summands' classes are the two halves of a gluing vector, $b^2 = \tfrac14H^2+t^2 = 1-1 = 0$, $b\cdot H = \tfrac12H^2 = 2$, and $b$ is orthogonal to $H^{\perp S_\Co}$ because both summands are. The Gram matrix of $H,b$ is $\begin{pmatrix}4&2\\2&0\end{pmatrix}$, of determinant $-4$ and even, so $\langle H,b\rangle\cong U(2)$; $J = 2\operatorname{proj}_{\langle H,b\rangle}-\id$, the projection being along the orthogonal complement, is $+1$ on $\langle H,b\rangle$ and $-1$ on its complement, hence $J^2 = \id$ and $J$ preserves the form; it is integral, which the record checks column by column, and it fixes $H$ and $b$ by construction. Commutation with $\theta_\Co$: $\theta_\Co$ is $-\id$ on $S_\Co\ni H$ and $\id$ on $T_\Co\tensor_\ZZ\QQ\ni t$, so $\theta_\Co(b) = -H/2+t = b-H$; hence $\theta_\Co$ preserves $\langle H,b\rangle$ and its orthogonal complement, and $J$ is $+\id$ on the first and $-\id$ on the second, so $J$ commutes with $\theta_\Co$, which is also what the record checks on the $22$ basis vectors.
:::

::: {.corollary #cor:no-del-pezzo-involution-coble-cover title="The isometry fixing $\langle f^*F_1,f^*F_2\rangle$ is not geometric"}

In the marking of @prop:coble-cover-marking, the isometry $\phi$ is a Hodge isometry (@not:k3-automorphism-data) of $H^2(X,\ZZ)$, and it is not the action of an automorphism of $X$.
:::

::: {.proof}

The transcendental lattice of $X$ lies in $\Pic(X)^{\perp}\subseteq S_\Co^{\perp} = T_\Co$, on which $\phi$ is $-\id$, so $\phi$ acts on $H^{2,0}(X)$ by $-1$ and preserves the Hodge decomposition.
By @prop:coble-cover-marking, $\phi(\alpha) = -\alpha$.
By @lem:alpha-is-ramification-class, $\alpha$ is effective and $-\alpha$ is not.
An automorphism of $X$ carries effective classes to effective classes, so no $\iota\in\Aut(X)$ has $\iota^* = \phi$.
:::

::: {.proposition #prop:del-pezzo-placement title="What the abstract conditions determine about the del Pezzo slot"}

Let $\psi$ be an involution of $\lkt$ whose invariant lattice is $\sdp\cong U(2)$, let $H\in\sdp$ with $H^2 = 4$, and suppose that $\psi$ commutes (@def:commutative-diagram) with $I_\Co$ — equivalently, that it preserves $S_\Co$.
Then $H = a+b$ for a hyperbolic (@def:definiteness) basis (@def:based-module) $a,b$ of $\sdp$, and the isotropic classes (@def:descent-class) $a'\in\sdp$ with $a'\cdot H = 2$ are exactly $a$ and $b$.
Put $A \definedas S_\Co\cap\sdp$ and $B \definedas S_\Co\cap\sdp^{\perp\lkt}$. Then $S_\Co\otimes\QQ = A_\QQ\oplus B_\QQ$ and $2S_\Co\subseteq A\oplus B\subseteq S_\Co$, so $A\oplus B$ has index a power of $2$ in $S_\Co$.
$A$ is primitive in $S_\Co$ and contains $H$, so $\rank_\ZZ A\in\{1,2\}$; rank $1$ forces $A = \ZZ H$, and rank $2$ occurs exactly when $\sdp\subseteq S_\Co$, in which case $[S_\Co:\sdp\oplus B]$ is a power of $2$ and equals $1$ for the candidate of @prop:coble-cover-marking.
:::

::: {.proof}

In a hyperbolic basis $a,b$ of $U(2)$ write $H = pa+qb$; since $H^2 = 4$ forces $4pq = 4$, one has $(p,q) = (1,1)$ or $(-1,-1)$ and $H = \pm(a+b)$, and replacing $(a,b)$ by $(-a,-b)$ gives $H = a+b$.
For an isotropic $a' = \lambda a+\mu b$ one has $(a')^2 = 4\lambda\mu = 0$ and $a'\cdot H = 2(\lambda+\mu)$, so $a'\cdot H = 2$ forces $\lambda\mu = 0$ and $\lambda+\mu = 1$, that is $(\lambda,\mu) = (1,0)$ or $(0,1)$: exactly two solutions, $a$ and $b$, with sum $H$.
Two involutions commute exactly when each preserves the other's eigenspaces, so $\psi(S_\Co) = S_\Co$. For $x\in S_\Co$ both $x+\psi x$ and $x-\psi x$ then lie in $S_\Co$, the first fixed by $\psi$ and the second negated by it, so they lie in $A$ and in $B$; hence $2S_\Co\subseteq A\oplus B$, and the index divides $2^{11}$.
Over $\QQ$ the $(\pm1)$-eigenspaces of $\psi$ meet $S_\Co\otimes\QQ$ in $A_\QQ$ and $B_\QQ$, which therefore span it.
$A$ is primitive in $S_\Co$: if $nx\in A$ with $x\in S_\Co$ and $n\neq0$, then $x\in\sdp$ because $\sdp$ is primitive in $\lkt$, and so $x\in A$. It contains $H$, which is primitive in $S_\Co$ since $H/2\notin S_\Co$; a primitive rank-one sublattice of $S_\Co$ containing a primitive vector is its span, so rank $1$ gives $A = \ZZ H$. If $\sdp\subseteq S_\Co$ then $B = \sdp^{\perp S_\Co}$, and $\det\sdp\cdot\det B = [S_\Co:\sdp\oplus B]^2\det S_\Co$; for the candidate the three values are $-4$, $-512$ and $2048$, giving index $1$.
:::

::: {.lemma #lem:rank-two-slot-unique title="The rank-two del Pezzo slot is unique"}

In @prop:coble-cover-marking let $N'\subseteq S_\Co$ be a sublattice isometric to $U(2)$ that contains $H$.
Then $N' = \langle f^*F_1, f^*F_2\rangle$.
Hence an involution $\psi$ as in @prop:del-pezzo-placement with $\sdp\subseteq S_\Co$ is the isometry $\phi$ of @prop:coble-cover-marking.
:::

::: {.proof}

By @prop:del-pezzo-placement, $N'$ has a hyperbolic (@def:definiteness) basis (@def:based-module) $a,b$ with $a+b = H$, so $a$ and $b$ are isotropic classes (@def:descent-class) of $S_\Co$ with $a\cdot H = b\cdot H = 2$.
The map $a\mapsto y\definedas 2a-H$ is a bijection from the isotropic $a\in S_\Co$ with $a\cdot H = 2$ onto the $y\in H^{\perp S_\Co}$ with $y^2 = -4$ and $y\equiv H\pmod{2S_\Co}$.
Indeed $(2a-H)^2 = 4a^2-4a\cdot H+H^2 = -4$ and $(2a-H)\cdot H = 0$; conversely, for such a $y$ the class $a = (y+H)/2$ lies in $S_\Co$ by the congruence, $(y+H)^2 = y^2+H^2 = 0$ and $(y+H)\cdot H = H^2 = 4$.

Transport the count along the isometry $\psi\colon S_\Co\iso M$ of the proof of @prop:coble-enriques-polarized-match, which sends $H$ to $h = e+f$ and $H^{\perp S_\Co}$ to $\ZZ(e-f)\oplus E_8(2)\oplus\ZZ\delta$.
A vector $c(e-f)+v+d\delta$ there has square $-4c^2+v^2-2d^2$ with $v^2\in 4\ZZ_{\le0}$, so the vectors of square $-4$ are the $2$ vectors $\pm(e-f)$ and the $240$ vectors $v\in E_8(2)$ with $v^2 = -4$, which are the roots of $E_8$; there are $242$ in all.
Of these, $\pm(e-f)-(e+f)\in\set{-2f,-2e}$ lies in $2M$, and $v-(e+f)$ does not, because its coefficient of $e$ is odd (@def:two-elementary-isotropic-types).
So the solutions are $a = (\pm(e-f)+h)/2\in\set{e,f}$, whose preimages under $\psi$ are $f^*F_1$ and $f^*F_2$.
Therefore $\set{a,b} = \set{f^*F_1,f^*F_2}$ and $N' = \langle a,b\rangle = \langle f^*F_1,f^*F_2\rangle$.

An involution of $\lkt$ is $-\id$ on the orthogonal complement of its invariant lattice, so it is determined by that lattice; with invariant lattice $\langle f^*F_1,f^*F_2\rangle$ it is $\phi$.
:::

::: {.proposition #prop:rank-one-slot title="The rank-one del Pezzo slot, at the level of lattices"}

Let $S_\Co\injects\lkt$ be the primitive embedding of @prop:coble-invariant-lattice, with complement $T_\Co = S_\Co^{\perp\lkt}$ and gluing anti-isometry $\gamma_\Co\colon A_{S_\Co}\iso A_{T_\Co}(-1)$ (@prop:theta-co-exists), and let $H\in S_\Co$ be the degree-$4$ class of @prop:coble-cover-marking — the generator of $S_\Co\cap\sdp$ when that intersection has rank $1$ (@prop:del-pezzo-placement).
Then:
1. the values $x\cdot H$ for $x\in S_\Co$ generate $2\bZ$, and $\varphi(x)\definedas -x+\tfrac12(x\cdot H)H$ is an integral isometry of $S_\Co$ with $\varphi^2 = \id$, $\varphi(H) = H$, $\varphi = -\id$ on $H^{\perp S_\Co}$ and fixed lattice exactly $\ZZ H$; the eigenspaces $\ZZ H$ and $H^{\perp S_\Co}$ nevertheless span only an index-$2$ sublattice of $S_\Co$;
2. $q_{T_\Co}\bigl(\gamma_\Co(\overline{H/2})\bigr) = -1$, and every class of $A_{T_\Co,q}$ of odd value contains a vector of $T_\Co^{\#}$ of square $-1$; there are $496$ such classes among the $2048$;
3. hence there is $t\in T_\Co^{\#}$ with $t^2 = -1$ and class $\gamma_\Co(\overline{H/2})$, and $b\definedas\tfrac12H+t$ lies in $\lkt$, is isotropic, satisfies $b\cdot H = 2$, and is orthogonal to $H^{\perp S_\Co}$;
4. the involution $J$ of $\lkt$ with $(+1)$-eigenspace $\langle H,b\rangle$ is integral, fixes $H$, commutes (@def:commutative-diagram) with $I_\Co$, has invariant lattice $\langle H,b\rangle\cong U(2) = \sdp$ meeting $S_\Co$ in $\ZZ H$, is conjugate to $I_{\mathrm{dP}}$ of [@AEGS25, Def. 2.3] in $\Orth(\lkt)$, and is nonsymplectic for every action of it on a K3 surface — so the product $I_\Co J$ is symplectic, both factors acting by $-1$ on the holomorphic $2$-form.
:::

::: {.proof}

Write $\overline{x}$ for the class in $A_{L,q}$ of $x\in L^{\#}$; by @def:discriminant $q_L(\overline{x}) = x^2$ modulo $2\bZ$.
(1) In the basis $e_0 = f^*H$, $e_i = f^*E_i$ of @prop:coble-invariant-lattice one has $H\cdot e_0 = 12$, $H\cdot e_i = 4$ for $1\le i\le 8$ and $H\cdot e_9 = H\cdot e_{10} = 2$, so those values generate $2\bZ$; and $H/2\notin S_\Co$ because $(H/2)^2 = 1$ is odd while $S_\Co$ is even. Hence $\varphi$ is integral, and it is $(-\id)\circ s_H$ with $s_H$ the reflection in $H$, an integral isometry because $2(x\cdot H)/H^2 = (x\cdot H)/2\in\bZ$ for $x\in S_\Co$; the scalar $-\id$ commutes with $s_H$, so $\varphi^2 = s_H^2 = \id$. Moreover $\varphi(H) = -H+2H = H$, and $\varphi(x) = -x$ for $x\in H^{\perp S_\Co}$; conversely $\varphi(x) = x$ forces $2x = \tfrac12(x\cdot H)H$, that is $x\in\bQ H$, and then $x\in\ZZ H$ because $H$ is primitive in $S_\Co$. Finally $H^2\det(H^{\perp S_\Co}) = 4\cdot 2^{11} = 4\det S_\Co$, so $\ZZ H+(H^{\perp S_\Co})$ has index $2$ in $S_\Co$, and $2S_\Co$ lies in it by the argument with $x\pm\varphi x$ of @prop:del-pezzo-placement, so the index is exactly $2$.
(2) By @prop:tco-split-maximal $T_\Co = B(2)$ with $B = U\oplus U\oplus\latI_{0,7}$, so $T_\Co\cong U(2)\perp U(2)\perp\generators{-2}^{\oplus7}$ and every vector of $T_\Co$ has even square. Hence $\tfrac12T_\Co\subseteq T_\Co^{\#}$, and $\cardinality{A_{T_\Co}} = 2^{11} = [T_\Co:\tfrac12T_\Co]$ by @prop:twisted-unimodular-discriminant, so $T_\Co^{\#} = \tfrac12T_\Co$ and every class of $A_{T_\Co}$ is the class of some $\tfrac12\tau$ with $\tau\in T_\Co$. Replacing $\tau$ by $\tau+2\lambda$ adds $\lambda\in T_\Co$ to $\tfrac12\tau$ and leaves the class alone, while $\bigl(\tfrac12\tau+\lambda\bigr)^2 = \tfrac14\tau^2+\tau\cdot\lambda+\lambda^2$.
Take $\tau = \sum_ic_ie_i$ with $c_i\in\set{0,1}$, in the basis $e_0,e_1$ of the first $U(2)$, $e_2,e_3$ of the second, and $e_4,\ldots,e_{10}$ the orthogonal basis vectors of square $-2$. Two cases cover every class of odd value. If $c_i = 1$ for some $i\le3$, say $c_0 = 1$, then $\tfrac12\tau\cdot e_1 = c_0 = 1$, so $\tfrac12\tau+p e_1$ has square $\tfrac14\tau^2+2p$, which is $-1$ for $p = -\tfrac12\bigl(1+\tfrac14\tau^2\bigr)\in\bZ$ because $\tfrac14\tau^2$ is odd; and $(c_1,e_0)$, $(c_2,e_3)$, $(c_3,e_2)$ do the same for the other three coordinates. If $c_0 = c_1 = c_2 = c_3 = 0$ then $\tfrac14\tau^2 = -\tfrac12k$, where $k$ is the number of $j$ with $c_{4+j} = 1$, and that is odd exactly for $k = 2$ and $k = 6$: for $k = 2$ the square is already $-1$, and for $k = 6$ one has $\tfrac12\tau\cdot(e_0+e_1+e_j) = 0$ and $(e_0+e_1+e_j)^2 = 2$ for any $j$ with $c_{4+j} = 0$, so $\tfrac12\tau+e_0+e_1+e_j$ has square $-3+2 = -1$. So every class of odd value contains a vector of square $-1$. Since $\gamma_\Co$ is an anti-isometry, $q_{T_\Co}\bigl(\gamma_\Co(\overline{H/2})\bigr) = -q_{S_\Co}(\overline{H/2}) = -\tfrac14H^2 = -1$, which is odd, so for every gluing anti-isometry $\gamma_\Co$ the class $\gamma_\Co(\overline{H/2})$ is one of the $496$ classes with $q = 1$ (@prop:coble-q-fibers).
(3) $t\perp S_\Co$ because $t\in T_\Co\otimes\bQ = (S_\Co\otimes\bQ)^{\perp}$, so $b\in(S_\Co\perp T_\Co)^{\#}$, with class $(\overline{H/2},\bar t)$ in the gluing subgroup; that subgroup is the graph of $\gamma_\Co$, so $b$ lies in the overlattice it cuts out, which is $\lkt$ (@cor:lifting-unimodular). There $b^2 = \tfrac14H^2+t^2 = 1-1 = 0$, $b\cdot H = \tfrac12H^2 = 2$, and $b\perp H^{\perp S_\Co}$ because both summands are.
(4) Put $J(x)\definedas (x\cdot H)b+(x\cdot b)H-2(x\cdot b)b-x$; the Gram matrix of $H,b$ in that basis is $\begin{pmatrix}4&2\\2&0\end{pmatrix}$ with inverse $\begin{pmatrix}0&\tfrac12\\\tfrac12&-1\end{pmatrix}$, so $J$ is twice the projection onto $\langle H,b\rangle_{\bQ}$ minus the identity, and it is an integral combination of $H$, $b$ and $x$ for $x\in\lkt$. Hence $J$ is an isometry of $\lkt$ with $J^2 = \id$; it fixes $H$ and $b$ and negates the orthogonal complement of $\langle H,b\rangle$, so its $(+1)$-eigenspace is $\langle H,b\rangle_{\bQ}\cap\lkt$, which is $\langle H,b\rangle$: if $mH+nb = 2y$ with $y\in\lkt$ then $2m+n = (mH+nb)\cdot e_9$ is even, so $n$ is even, and then $mH = 2y-nb$ forces $m$ even because $H$ is primitive in $\lkt$. The Gram matrix has determinant $-4$ and is even, so $\langle H,b\rangle\cong U(2) = \sdp$; and $S_\Co\cap\langle H,b\rangle = \ZZ H$, since $(b+mH)\cdot H = 2+4m\neq0$ for every $m$. For commutation, $I_\Co$ is $+\id$ on $S_\Co$ and $-\id$ on $T_\Co$, so $I_\Co(t) = -t$ and $I_\Co(b) = \tfrac12H-t = H-b$, which preserves $\langle H,b\rangle$, and an involution is determined by its $(+1)$-eigenspace. The coinvariant lattice $\langle H,b\rangle^{\perp\lkt}$ is even of rank $20$ and signature $(2,18)$, and its discriminant form is that of $U(2)$ up to sign — of order $4$, with integral values — so it is $2$-elementary with $a = 2$ and $\delta = 0$; $T_{\mathrm{dP}} = \Delta^-(U)\perp U\perp E_8^2\cong U(2)\perp U\perp E_8^2$ has the same invariants, so the two are isometric by @thm:two-elementary-classification. An isometry $\sdp\iso\langle H,b\rangle$ then extends to an isometry of $\lkt$: after fixing any isometry of the two complements, the remaining mismatch is an element of $\Orth\bigl(A_{\langle H,b\rangle^{\perp}}\bigr)$, which @thm:two-elementary-surjectivity realises by an isometry of $\langle H,b\rangle^{\perp}$, and the compatible pair extends by @cor:lifting-unimodular. So $J$ is conjugate to $I_{\mathrm{dP}}$ in $\Orth(\lkt)$, and its orbit (@def:group-orbit) is that of the involution of [@AEGS25, Lem. 3.11]. Finally, a symplectic involution fixes the holomorphic $2$-form, whose real and imaginary parts span a positive definite (@def:definiteness) $2$-plane inside the $(+1)$-eigenspace, and $U(2)$ has signature $(1,1)$, which contains no positive definite $2$-plane.
:::

::: {.proposition #prop:no-rank-one-automorphism title="A rank-one del Pezzo slot is induced by no automorphism"}

Let $\widetilde X$ be a projective K3 surface over $\CC$, let $\iota$ be a nonsymplectic involution of it with invariant lattice (@def:invariant_coinvariant_lattices) $S \definedas H^2(\widetilde X,\bZ)^{\iota}$, and let $\iota'$ be an involution commuting with $\iota$ whose invariant lattice $S'$ is isometric to $U(2)$.
Let $H\in S\cap S'$ with $H^2 = 4$, suppose $\rank(S\cap S') = 1$, and let $\alpha\in S$ be effective with $\alpha^2 = -2$ and $H\cdot\alpha = 0$.
Then $\iota'(\alpha) = -\alpha$, and no automorphism of $\widetilde X$ induces $\iota'$.
:::

::: {.proof}

$S$ is even (@def:form-axioms) because $H^2(\widetilde X,\bZ)$ is, and it has signature (@def:signature) $(1,\cdot)$: $\iota$ is nonsymplectic, so it acts as $-\id$ on $H^{2,0}\oplus H^{0,2}$, and a Kähler class can be averaged over $\set{\id,\iota}$ to an invariant one.
Hence $H$, of positive square, spans a maximal (@def:maximal-lattice) positive definite (@def:definiteness) subspace, and $H^{\perp S}$ is negative definite (@def:definiteness), the orthogonal complement of a non-isotropic vector being nondegenerate (@def:polarization).
$\iota'$ commutes (@def:commutative-diagram) with $\iota$, so it preserves $S$, and $A \definedas S\cap S'$ is the fixed lattice of $\iota'$ in $S$; it is saturated (@def:saturation) in $S$ because both factors are saturated in $H^2(\widetilde X,\bZ)$.
By hypothesis $\rank A = 1$ and $H\in A$, so $A = \ZZ H$: $H$ is primitive (@def:primitive-embedding) in $S$, since $H/2\in S$ would give $(H/2)^2 = 1$, odd (@def:two-elementary-isotropic-types) in an even lattice (@def:even-lattice).
Therefore $\iota'$ is $+\id$ on $\ZZ H$ and $-\id$ on $H^{\perp S}$, which is its $(-1)$-eigenspace in $S$.
The class $\alpha$ lies in $S$ and $\alpha\cdot H = 0$, so $\alpha\in H^{\perp S}$ and $\iota'(\alpha) = -\alpha$.
If $g\in\Aut(\widetilde X)$ had $g^* = \iota'$, then $g_*\alpha = (g^*)^{-1}\alpha = -\alpha$ would be the class of the effective divisor $g(D)$, for any effective divisor $D$ of class $\alpha$.
But $\alpha\cdot A_0>0$ for an ample class $A_0$, since $\alpha\neq0$ is effective and $\widetilde X$ is projective, whereas $(-\alpha)\cdot A_0<0$. Contradiction.
:::

::: {.proposition #prop:local-operators title="The two involutions of the nodal cover, their fixed loci and their symplectic characters"}

Let $X^\sharp = \set{z^2 = f(x,y)}$ over the $\tau$-fixed point $p$ of $Y$, with $f$ having a nondegenerate (@def:polarization) quadratic part there, and let
$$\iota_{\mathrm{dP}}(x,y,z) = (x,y,-z),\qquad \iota_\Co(x,y,z) = (-x,-y,-z).$$
Then:
1. the two commute, and $\iota_\Co\iota_{\mathrm{dP}}(x,y,z) = (-x,-y,z)$;
2. all three act on the holomorphic $2$-form $\omega = \frac{dx\wedge dy}{2z}$ by $\iota_{\mathrm{dP}}^*\omega = -\omega$, $\iota_\Co^*\omega = -\omega$ and $(\iota_\Co\iota_{\mathrm{dP}})^*\omega = +\omega$: both involutions are nonsymplectic and their product is symplectic;
3. $\mathrm{Fix}(\iota_{\mathrm{dP}}) = \set{z = 0}\cap X^\sharp$, the branch curve, nodal (@def:nodal-enriques-surface) at $p$;
4. $\mathrm{Fix}(\iota_\Co)$ is contained in the singular points of $X^\sharp$: if $\iota_\Co(x,y,z) = (x,y,z)$ then $x = y = 0$ and $z = -z$, so $z = 0$ and $f(0,0) = 0$; and $f$ is $\tau$-invariant, so its terms of odd (@def:two-elementary-isotropic-types) order at the $\tau$-fixed point $p$ vanish and the vanishing order there is even (@def:form-axioms) — the point is singular, of type $A_1$ when the quadratic part is nondegenerate. So $\iota_\Co$ has no isolated fixed point, which is what its nonsymplecticity requires: at an isolated fixed point the differential would be $-\id$ on the tangent space and $\omega$ would be preserved.
:::

::: {.proof}

(1) is substitution. (2) is the residue form: on $X^\sharp$ away from $z = 0$ one has $\omega = \frac{dx\wedge dy}{2z}$, and $\iota_{\mathrm{dP}}^*(dx\wedge dy) = dx\wedge dy$ with $\iota_{\mathrm{dP}}^*(2z) = -2z$, while $\iota_\Co^*(dx\wedge dy) = (-dx)\wedge(-dy) = dx\wedge dy$ with $\iota_\Co^*(2z) = -2z$; the product fixes $z$ and acts by $(-dx)\wedge(-dy)$ on the $x,y$-form, so it scales $\omega$ by $+1$.
(3) $z = -z$ gives $z = 0$, and then $f(x,y) = z^2 = 0$.
(4) $x = -x$ and $y = -y$ give $x = y = 0$; then $z = -z$ gives $z = 0$ and $f(0,0) = 0$. Since $f(-x,-y) = f(x,y)$, every monomial of odd total degree (@def:graded-object) has coefficient $0$, so the lowest-order part at the origin is even and $f$ vanishes there to order at least $2$; with nondegenerate quadratic part that is an $A_1$ point. For the last sentence: at an isolated fixed point $d\iota$ has no eigenvalue $1$, so being an involution it equals $-\id$ and $\iota^*\omega = \det(d\iota)\,\omega = +\omega$ there, against $\iota^*\omega = -\omega$.
:::

::: {.example #ex:product-eight-points title="The fixed points of the product involution"}

The product $\rho = \iota_\Co\iota_{\mathrm{dP}}$ of @prop:local-operators is $\rho(x,y,z) = (-x,-y,z)$, so its fixed points are the points over the four $\tau$-fixed points of $Y$, where $z^2 = f$.
Over a fixed point at which $f\ne0$ there are two, $z = \pm\sqrt f$.
Over one at which $f = 0$ the single point is the node, which the resolution replaces by the two points $[1:\pm i:0]$ of @prop:del-pezzo-type-on-the-resolution(2).
So $\rho$ has $2\cdot4 = 8$ fixed points when $I_\Co$ has no fixed point, and $2\cdot3+2 = 8$ with one node.
By the formula of @prop:tuple-of-the-construction, $\rank S_\rho = \tfrac12(8+20) = 14$, and $S_\Co\cap S_{\mathrm{dP}}\subseteq S_\rho$ because a class fixed by both involutions is fixed by their product.
:::

::: {.proposition #prop:del-pezzo-type-on-the-resolution title="The invariant type of the lifted del Pezzo involution on the resolution"}

Let $\widehat X\to X^\sharp$ be the minimal resolution (@def:minimal-resolution-of-surface-singularity) of the node at $p$, $D$ the exceptional $(-2)$-curve, and $\widehat\iota_{\mathrm{dP}}$, $\widehat\iota_\Co$ the lifts. Then:
1. $\widehat\iota_\Co$ acts trivially on the exceptional $\PP^2$ and hence fixes $D$ pointwise;
2. $\widehat\iota_{\mathrm{dP}}$ acts on that $\PP^2$ by $[X:Y:Z]\mapsto[X:Y:-Z]$, so it preserves the conic $D = \set{Z^2 = X^2+Y^2}$ and fixes on it exactly the two points $[1:\pm i:0]$, which are also where the proper transform (@def:strict-transform) of the branch curve meets $D$;
3. consequently $\mathrm{Fix}(\widehat\iota_{\mathrm{dP}})$ is the normalization of the branch curve: for $f$ with exactly $k$ nodes and otherwise smooth, the branch curve has arithmetic genus $9$ and geometric genus $9-k$, so $\chi(\mathrm{Fix}) = 2-2(9-k) = 2k-16$, and Lefschetz gives $\rank S_{\mathrm{dP}} = \tfrac12(22+(2k-16)-2) = 2+k$;
4. $S_{\mathrm{dP}}$ contains $\pi^*\Pic(Y)\perp\ZZ D_1\perp\cdots\perp\ZZ D_k$, of rank $2+k$: the pullbacks (@def:pullback-square) of $\Pic(Y) = \ZZ^2$ have Gram matrix $U(2)$, each $D_g$ is a $(-2)$-class because it is preserved by $\widehat\iota_{\mathrm{dP}}$, and $D_g\perp\pi^*\Pic(Y)$ and $D_g\perp D_{g'}$ for $g\ne g'$ because the resolution contracts them.
So $S_{\mathrm{dP}}$ contains $U(2)\perp\langle-2\rangle^{\oplus k}$ with finite index (@def:index), and $S_{\mathrm{dP}}\not\cong U(2)$ whenever $k\neq0$.
:::

::: {.proof}

(1) and (2) are the substitution $(-x,-y,-z)$ and $(x,y,-z)$ in homogeneous coordinates on the exceptional $\PP^2$, whose point set is the conic $\set{Z^2 = X^2+Y^2}$; the fixed points of $[X:Y:Z]\mapsto[X:Y:-Z]$ on it satisfy $Z = 0$, that is $X^2+Y^2 = 0$, and the two branches of the nodal (@def:nodal-enriques-surface) curve $\set{z = 0, f = 0}$ have exactly those tangent directions.
(3) the proper transform of the branch curve under the resolution of its node is its normalization, of geometric genus $9-k$; the two fixed points on $D$ are its two points over the node, so they are part of it and contribute nothing further.
(4) as stated, with the projection formula giving $(\pi^*F)\cdot(\pi^*G) = \deg\pi\,(F\cdot G) = 2(F\cdot G)$, which is $U(2)$ on the basis (@def:based-module) of $\Pic(\PP^1\times\PP^1)$.
:::

::: {.proposition #prop:tuple-of-the-construction title="The construction's own tuple satisfies the five conditions of the tuple"}

Let $\pi\colon X^\sharp = \set{z^2 = f(x,y)}\to Y = \PP^1\times\PP^1$ be the double cover branched along $B = \set{f = 0}\in\abs{\OO_Y(4,4)}$, so that $K_{X^\sharp} = \pi^*(K_Y+\OO_Y(2,2)) = 0$, and let $\widehat X\to X^\sharp$ be the resolution of the $k$ nodes of $B$, all of them at $\tau$-fixed points. Put $H\definedas\pi^*\OO_Y(1,1)$, and let $\alpha\definedas[D_g]$ be the class of the exceptional curve over one of them. Then
1. $H^2 = 4$, and $H$ is fixed by both $I_\Co$ and $I_{\mathrm{dP}}$;
2. $\alpha^2 = -2$, $H\cdot\alpha = 0$, and $\alpha$ is fixed by $I_\Co$ and by $I_{\mathrm{dP}}$;
3. $H$ is nef and big, $h^0(\widehat X,H) = 4$, and $\alpha$ is the class of an effective curve;
4. both involutions are nonsymplectic and their product is symplectic;
5. $\rank S_{\mathrm{dP}} = k+2$ and $\rank S_\Co = k+10$;
6. $\pi^*\Pic(Y)\perp\ZZ D_1\perp\cdots\perp\ZZ D_k\subseteq S_\Co\cap S_{\mathrm{dP}}$, and $S_{\mathrm{dP}}\subseteq S_\Co$.
So for $k\ge1$ the five bullets of @sec-labeled-lattice-data hold on $\widehat X$: the tuple of the direct-projective construction exists, and its quotient by $I_\Co$ is not Enriques.
:::

::: {.proof}

(1) $(\pi^*\OO(1,1))^2 = \deg\pi\,(\OO(1,1))^2 = 2\cdot2 = 4$. Both involutions satisfy $\pi\circ\iota = \iota'\circ\pi$, with $\iota' = \id_Y$ for $\iota_{\mathrm{dP}}$ and $\iota' = \tau$ for $\iota_\Co$; and $\tau$ acts by $[-1]$ on each factor, with $[-1]^*\OO(1) = \OO(1)$, so $\iota'^*\OO(1,1) = \OO(1,1)$ in both cases and $\widehat\iota^*H = \pi^*\iota'^*\OO(1,1) = H$, the resolution being equivariant.
(2) $D_g$ is a $(-2)$-curve, fixed pointwise by $\widehat\iota_\Co$ and preserved by $\widehat\iota_{\mathrm{dP}}$ (@prop:del-pezzo-type-on-the-resolution, parts 1 and 2); and $H\cdot D_g = \OO(1,1)\cdot\pi_*D_g = 0$ because $\pi_*D_g = 0$, the curve lying in a fibre of the resolution.
(3) $\OO_Y(1,1)$ is very ample, the Segre embedding, hence nef; for a curve $C$ one has $H\cdot C = \OO(1,1)\cdot\pi_*C\ge0$, so $H$ is nef, and $H^2 = 4>0$ with $H$ nef makes $H$ big on a surface. The surface $X^\sharp$ is normal, so the resolution $\nu\colon\widehat X\to X^\sharp$ has $\nu_*\OO_{\widehat X} = \OO_{X^\sharp}$, and $\pi_*\OO_{X^\sharp} = \OO_Y\oplus\OO_Y(-2,-2)$; by the projection formula $h^0(\widehat X,H) = h^0(\OO_Y(1,1))+h^0(\OO_Y(-1,-1)) = 4+0$. $\alpha$ is the class of the curve $D_g$.
(4) @prop:local-operators, part 2, computes the two characters on $X^\sharp$; away from the nodes the resolution is an isomorphism (@def:isomorphism-of-objects) and both involutions act on the exceptional curves, so the characters are unchanged.
(5) For a nonsymplectic involution of a K3 with fixed locus $F$, Lefschetz gives $\chi(F) = 2+\tr$. Decompose over $\QQ$, where the eigensplitting is available: $H^2(\widehat X,\QQ) = S_\QQ\oplus T_\QQ$ with $\id$ on $S$ and $-\id$ on $T$, so $\tr = \rank S-\rank T$ and, with $\rank S+\rank T = 22$, $\tr = 2\rank S-22$ and $\rank S = \tfrac12(\chi(F)+20)$. For $\widehat\iota_{\mathrm{dP}}$ the fixed locus is the normalization of $B$, of $\chi = 2k-16$ (@prop:del-pezzo-type-on-the-resolution, part 3), so $\rank S_{\mathrm{dP}} = k+2$. For $\widehat\iota_\Co$ it is the disjoint union of the $k$ exceptional curves: @prop:local-operators, part 4, puts every fixed point of $\iota_\Co$ at a singular point, and @prop:del-pezzo-type-on-the-resolution, part 1, makes the curve over each of them fixed pointwise. So $\chi(F) = 2k$ and $\rank S_\Co = k+10$. At $k = 0$ this last value is $10$, the rank of the invariant lattice (@def:invariant_coinvariant_lattices) of an Enriques involution (@def:enriques-surface) of a K3, which is what $I_\Co$ is when its fixed locus is empty.
(6) The involution $\iota_{\mathrm{dP}}$ is the deck transformation of $\pi$, so it fixes every class $\pi^*c$; the involution $\iota_\Co$ covers $\tau$, and $\tau^*\OO_Y(a,b) = \OO_Y(a,b)$, so it fixes every $\pi^*c$ too. Each $D_g$ is fixed by both involutions by (2), and $D_g\cdot\pi^*c = c\cdot\pi_*D_g = 0$, while $D_g\cdot D_{g'} = 0$ for $g\ne g'$. This gives the first containment. That sublattice has rank $k+2 = \rank S_{\mathrm{dP}}$ by (5) and @prop:del-pezzo-type-on-the-resolution, part 4. The invariant lattice $S_\Co$ of an isometry is primitive (@def:primitive-embedding) in $H^2(\widehat X,\ZZ)$, so $S_\Co\cap S_{\mathrm{dP}}$ is primitive in $S_{\mathrm{dP}}$; it has full rank, so it is $S_{\mathrm{dP}}$.
:::

::: {.proposition #prop:one-node-family title="The one-node construction is a smooth proper equivariant family with a relative polarization and an exceptional divisor"}

Let $B\subset\abs{\OO_Y(4,4)}^\tau$ be the set of $\tau$-invariant sections whose branch curve has exactly one node, at the $\tau$-fixed point $p$, and is otherwise smooth with nondegenerate (@def:polarization) quadratic part at $p$; it is open in the invariant linear system of @sec-invariant-system, and it is nonempty by @ex:one-node-branch-curve. Put $\mathcal L\definedas\OO_Y(2,2)$, a square root of $\OO_Y(4,4)$, and $\mathcal Y\definedas Y\times B$. Then:
1. $\mathcal X^\sharp = \Spec_{\mathcal Y}(\OO_{\mathcal Y}\oplus\mathcal L^{-1})$, with algebra structure $z^2 = f_b$ for $z$ the coordinate on the $\mathcal L$-summand, is a flat family of surfaces, finite and hence proper and projective over $\mathcal Y$ and over $B$, smooth away from the section $\sigma$ over $p$; the blow-up $\beta\colon\widehat{\mathcal X}\to\mathcal X^\sharp$ of $\sigma(B)$ is smooth and proper over $B$ with K3 fibres;
2. $\iota_\Co$ and $\iota_{\mathrm{dP}}$ act fibrewise, commute, and fix $\sigma$, hence lift to $\widehat{\mathcal X}$ commuting with $\beta$;
3. $\mathcal H\definedas\pi^*\OO_Y(1,1)$ is a line bundle on $\widehat{\mathcal X}$ whose restriction to every fibre is nef of degree (@def:graded-object) (@def:numerical-polarization) $4$, hence big, and not ample, its degree on the exceptional curves being $0$; its class is $H_b$;
4. the exceptional divisor $\mathcal D$ of $\beta$ is a $\PP^1$-bundle over $B$ with $\mathcal D_b^2 = -2$ and $\mathcal H_b\cdot\mathcal D_b = 0$, and $c_1(\mathcal H)$ and $[\mathcal D]$ are sections of $R^2\widehat\pi_*\ZZ$ flat for the Gauss–Manin connection (@def:calculus-connection).
:::

::: {.proof}

$B$ is open because the node condition is the vanishing of the coefficient of $x_0^4y_0^4$ at $p$ together with nondegeneracy of the quadratic part, an open condition (@lem:node-condition, @sec-invariant-system), and smoothness elsewhere is open.
(1) Since $\mathcal L^2 = \OO_Y(4,4)$, the sheaf of algebras $\OO\oplus\mathcal L^{-1}$ with $z^2 = f_b$ is a coherent sheaf of $\OO_{\mathcal Y}$-algebras, flat over $B$ because $f_b$ varies linearly, so $\mathcal X^\sharp\to B$ is finite and flat and the fibres are surfaces; the linear system is base-point free, so no fibre contains a component of a $\PP^1$-fibre and $B$ parametrizes a bounded family; projectivity comes from finiteness over the projective $\mathcal Y\to B$. The branch curve of the double cover is $B$, and $K_{\mathcal X^\sharp} = \pi^*(K_Y+\mathcal L) = \pi^*(\OO(-2,-2)+\OO(2,2)) = \OO_{\mathcal X^\sharp}$, with $\pi_*\OO_{\mathcal X^\sharp} = \OO_Y\oplus\mathcal L^{-1} = \OO_Y\oplus K_Y$; the fibres are K3 surfaces. The singular points of the fibres are the nodes, one per fibre by construction, at $p$; locally the family is $z^2 = q_b(x,y) + (\text{terms of order }\ge3)$ with $q_b$ nondegenerate for every $b\in B$, so the singular locus is exactly $\sigma(B)$ and is a family of ordinary (@def:two-elementary-isotropic-types) double points, which the blow-up of $\sigma(B)$ resolves simultaneously in a smooth family; on each fibre the blow-up replaces the node by a $(-2)$-curve.
(2) $\iota_{\mathrm{dP}}$ acts by $z\mapsto-z$ and $\iota_\Co$ by $(z,x,y)\mapsto(-z,-x,-y)$ on the $\mathcal L$-coordinate and on $Y$; both preserve each equation, commute, and fix the point over $p$, where $z = 0$; an automorphism fixing the centre of a blow-up lifts to it.
(3) $H_b\cdot C = \OO(1,1)\cdot\pi_b(C)\ge0$ for every curve $C$ on a fibre, since $\OO(1,1)$ is ample, so $H_b$ is nef; $H_b^2 = \deg\pi_b\cdot(\OO(1,1))^2 = 4>0$, so $H_b$ is big; and $H_b\cdot D_b = 0$ against the curve $D_b$, so $H_b$ is not ample.
(4) The exceptional divisor of the blow-up of a smooth subscheme is the projectivized normal bundle, so a $\PP^1$-bundle over $B$ when the centre is a smooth section; its fibre is $D_b$, of square $-2$, and $\pi$ contracts it, so $\mathcal H_b\cdot\mathcal D_b = 0$. The classes of a flat family of divisors are flat sections of $R^2\widehat\pi_*\ZZ$.
:::

::: {.proposition #prop:one-node-connected title="The one-node locus is path-connected: any two members lie on a pencil meeting the bad strata in finitely many points"}

Let $H = \set{f(p) = 0}\subset\abs{\OO_Y(4,4)}^\tau$, of dimension $11$ since evaluation at $p$ is a nonzero functional, and let $B\subset H$ be the members whose branch curve is smooth away from $p$ and has a nondegenerate (@def:polarization) node at $p$, exactly the locus of @prop:one-node-family. Then $B$ is nonempty, and for any $f_0,f_1\in B$ the pencil through them meets the complement of $B$ in at most finitely many points, so $f_0$ and $f_1$ lie in one path-connected (@def:path-connectedness) subfamily of $B$.
:::

::: {.proof}

Write $\ell\subset\abs{\OO_Y(4,4)}$ for the projective line through $f_0$ and $f_1$; it lies in $H$ because vanishing at $p$ is linear. Its base locus contains $p$, and it meets $C_{f_0}\cap C_{f_1}$. The conditions a member can fail to meet $B$ are, one by one, closed conditions on $\ell$ that are not identically satisfied:
- a shared base point (@def:complete-linear-system) $q\ne p$: "singular at $q$" is a closed linear evaluation condition, and it cannot hold for every member of the pencil, since $f_0$ is not singular at $q$;
- degeneracy of the quadratic part at $p$: this is the vanishing of a determinant of five coefficients, closed on $\ell$, and $f_0$ does not satisfy it;
- a singularity away from the base locus: by Bertini's theorem for pencils on a smooth variety, a general member of $\ell$ has no singularity outside the base locus, so the set of such $t$ is a closed proper subset.

Each of those closed loci is therefore a finite subset of $\ell$, as is their union.
The curve of @ex:one-node-branch-curve lies in $B$, so $B\ne\varnothing$.
A projective line with finitely many points removed is path-connected, so $f_0$ and $f_1$ are joined by a path (@def:path-connectedness) in $\ell\cap B$.
:::

::: {.theorem #thm:a21-labels title="The labels of any two tuples of the one-node direct-projective construction are conjugate"}

Let $\mathfrak L$, $\mathfrak L'$ be tuples of the direct projective construction arising from one-node members, in the sense of @prob:coble-rigidity. Then there is $\gamma\in\Orth(\lkt)$ mapping the involutions to the involutions, the degree-$4$ class to the degree-$4$ class, and the effective root to the effective root:
$$\gamma S_{\Co} = S'_{\Co},\qquad \gamma S_{\mathrm{dP}} = S'_{\mathrm{dP}},\qquad \gamma H = H',\qquad \gamma\alpha = \alpha'.$$
:::

::: {.proof}

By @prop:one-node-connected both parameter points lie in one connected $B$, so they are joined by a path (@def:path-connectedness); the family of @prop:one-node-family is smooth and proper over $B$ with $\mathcal H$ and $\mathcal D$ flat; @thm:one-node-transport applied to the path gives the conclusion.
:::

::: {.theorem #thm:one-node-transport title="Parallel transport preserves the lattice labels"}

In the situation of @prop:one-node-family let $\theta$ be a path (@def:path-connectedness) in $B$ from $b$ to $b'$, and let $\psi_\theta\colon H^2(\widehat X_b,\ZZ)\iso H^2(\widehat X_{b'},\ZZ)$ be the Gauss–Manin parallel transport (@cons:calculus-transport). Then $\psi_\theta H_b = H_{b'}$, $\psi_\theta\alpha_b = \alpha_{b'}$, and $\psi_\theta$ intertwines $\widehat\iota_{\Co,b},\widehat\iota_{\mathrm{dP},b}$ with $\widehat\iota_{\Co,b'},\widehat\iota_{\mathrm{dP},b'}$; hence, after markings, there is $\gamma\in\Orth(\lkt)$ with
$$\gamma S_{\Co,b} = S_{\Co,b'},\qquad \gamma S_{\mathrm{dP},b} = S_{\mathrm{dP},b'},\qquad \gamma H_b = H_{b'},\qquad \gamma\alpha_b = \alpha_{b'}.$$
:::

::: {.proof}

Parallel transport is an isometry of the fibres of $R^2\widehat\pi_*\ZZ$ and is compatible with flat sections, which $c_1(\mathcal H)$ and $[\mathcal D]$ are (@prop:one-node-family, part 4); that gives the first two. The involutions act on the total space, so transport intertwines them; a $(+1)$-eigenspace is determined by its involution, so the fixed lattices go to fixed lattices. Choosing markings and composing the transports gives $\gamma$.
:::

::: {.lemma #lem:face-at-H title="The curves contracted by $\pi$ are the ray in the cone of curves, and its annihilator is the smallest face of the nef cone through $H$"}

In the situation of @prop:one-node-family, on every fibre, with $\Delta_b$ and the chamber $\mathfrak c_b$ as in @def:coble-polarization-classes, part 3:
1. $\alpha_b = \pi_b^*e$, where $e\subset\widehat Y = \Bl_pY$ is the exceptional curve;
2. $\overline{\mathrm{NE}}(\widehat X_b)\cap H_b^\perp = \RR_{\ge0}\alpha_b$, and the classes of the irreducible curves contracted by $\pi_b$ are exactly the positive multiples of $\alpha_b$;
3. the nef cone (@def:nef-cone) $\mathcal N_b = \overline{\mathrm{NE}}(\widehat X_b)^\vee$ has a unique face $F_b$ whose relative interior contains $H_b$, namely
$$F_b = \set{v\in\mathcal N_b : v\cdot\alpha_b = 0},$$
and $H_b\cdot\gamma>0$ for every curve class $\gamma$ outside the ray $\RR_{\ge0}\alpha_b$;
4. no wall (@not:coxeter-polytope-faces) $\delta^\perp$ with $\delta\in\Delta_b\setminus\set{\alpha_b}$ passes through $H_b$, and the chamber $\mathfrak c_b$ has $H_b$ in its closure and lies on the side $x\cdot\alpha_b>0$.
:::

::: {.proof}

(1) $\pi^{-1}(p)$ is the single node $\hat p$ of $X^\sharp_b$, the cover being ramified there, so the pullback of the maximal (@def:maximal-lattice) ideal of $p$ is invertible on $\widehat X_b$ and $\pi_b$ factors through $\widehat X_b\to\widehat Y = \Bl_pY$, the double cover branched along the proper transform (@def:strict-transform) $\widetilde B$. The preimage of $e$ is therefore $D_b$, and $D_b\to e$ is the double cover branched at $e\cap\widetilde B$, of degree (@def:graded-object) (@def:numerical-polarization) $e\cdot\widetilde B = -2e^2 = 2$; being branched, $\pi_b^*e = D_b$, that is $\alpha_b = \pi_b^*e$, and $(\pi_b^*e)^2 = 2e^2 = -2$.
(2) $H_b\cdot C = \OO(1,1)\cdot\pi_b(C)$ with $\OO(1,1)$ ample, so it vanishes exactly when $\pi_b(C)$ is a point, that is when $C$ is contracted by $\pi_b$. Since $\pi_b$ factors through the finite map $X^\sharp_b\to Y$, which contracts no curve, $C$ is contracted by the resolution $\widehat X_b\to X^\sharp_b$, whose only exceptional curve is $D_b$; so $[C]\in\QQ_{\ge0}\alpha_b$. Passing to the closure of the cone (@def:closed-cone) spanned by curve classes gives the same ray.
(3) For a closed convex cone $K$ and $y\in K^\vee$, the set $F = \set{z\in K^\vee : \langle z,x\rangle = 0 \ \text{for all } x\in K \text{ with } \langle y,x\rangle = 0}$ is the smallest face of $K^\vee$ containing $y$, and $y$ lies in its relative interior. Taking $K = \overline{\mathrm{NE}}(\widehat X_b)$, whose dual cone is the nef cone, and using (2), the defining set is $\RR_{\ge0}\alpha_b$ and $F = F_b$ as displayed. For the last clause: $H_b$ is nef, so $H_b\cdot\gamma\ge0$ for every curve class, and it vanishes only on the ray by (2).
(4) Let $\delta\in\Delta_b$ have $H_b\cdot\delta = 0$. Writing $\delta = \sum a_iC_i$ over irreducible curves with $a_i>0$ gives $0 = \sum a_i(C_i\cdot H_b)$ with every term non-negative, so each $C_i$ is orthogonal to $H_b$ and hence, by (2), equal to $D_b$; then $\delta = m\alpha_b$ and $-2 = -2m^2$ forces $m = 1$. So $\delta = \alpha_b$.
$H_b$ is nef, so it lies in the closure of $\Amp(\widehat X_b)$, and every ample class is positive on $\alpha_b$, the class of an effective curve. So the chamber $\mathfrak c_b$, which contains $\Amp(\widehat X_b)$, has $H_b$ in its closure and lies on the side $x\cdot\alpha_b>0$.
:::

::: {.proposition #prop:chamber-pinned title="When the walls do not accumulate at $H$, the labels determine the chamber"}

In the situation of @lem:face-at-H, suppose that there is a convex open neighbourhood $U$ of $H_b$ in the cone (@def:closed-cone) $\mathcal C_b\definedas\mathcal C_{\widehat X_b}$ of @def:coble-polarization-classes, part 3, that meets no wall (@not:coxeter-polytope-faces) $\delta^\perp$ with $\delta\in\Delta_b\setminus\set{\alpha_b}$. Then $\mathfrak c_b$ is the only component of $\mathcal C_b\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp$ whose closure contains $H_b$ and which lies on the side $x\cdot\alpha_b>0$.
:::

::: {.proof}

On $U$ the only wall is $\alpha_b^\perp$, so $U\setminus\alpha_b^\perp$ is the disjoint union of the convex sets $U_+ = U\cap\set{x\cdot\alpha_b>0}$ and $U_- = U\cap\set{x\cdot\alpha_b<0}$. Each is connected and meets no wall, so each lies in a single component of the complement of the walls.
Let $\mathfrak c$ be a component whose closure contains $H_b$ and which lies on the side $x\cdot\alpha_b>0$. Then $\mathfrak c$ meets $U$, and $\mathfrak c\cap U\subseteq U_+$. So $\mathfrak c$ meets $U_+$, and it is the component that contains $U_+$.
By @lem:face-at-H, part 4, $\mathfrak c_b$ is such a component, so $\mathfrak c = \mathfrak c_b$.
:::

::: {.theorem #thm:chamber-pinned-by-labels title="At a member whose Picard lattice is the invariant lattice the chamber is a function of the labels"}

Let $b$ be a one-node member of @prop:one-node-family with $\Pic(\widehat X_b) = S_{\Co,b}$, let $\Delta_b$ and $\mcc_b$ be as in @def:coble-polarization-classes, part 3, and put $\mathcal C_b\definedas\mathcal C_{\widehat X_b}$ as in @prop:chamber-pinned. Then

1. $\Delta_b = \set{\delta\in S_{\Co,b} : \delta^2 = -2,\ H_b\cdot\delta>0}\cup\set{\alpha_b}$, and $\alpha_b$ is the only class of $\Delta_b$ orthogonal to $H_b$;
2. $\mcc_b = \set{x\in\mathcal C_b : x\cdot\delta>0 \ \text{for every}\ \delta\in\Delta_b}$;
3. every $\psi\in\Orth(S_{\Co,b})$ with $\psi H_b = H_b$ and $\psi\alpha_b = \alpha_b$ satisfies $\psi(\Delta_b) = \Delta_b$ and $\psi(\mcc_b) = \mcc_b$;

and consequently every $g\in Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}$ preserves $\Delta_b$ and $\mcc_b$, so that the chamber carried by @def:direct-group costs nothing at such a member:
$$Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha,\mcc} = Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}.$$
:::

::: {.proof}

*The classes of square $-2$.*
Let $\delta\in S_{\Co,b}$ have $\delta^2 = -2$ and $H_b\cdot\delta>0$.
On a $K3$ surface Riemann–Roch gives $\chi(\delta) = 2+\tfrac12\delta^2 = 1$, and Serre duality gives $h^2(\delta) = h^0(-\delta)$, so $h^0(\delta)+h^0(-\delta) = 1+h^1(\delta)\ge1$; both cannot be positive, since effective divisors of classes $\delta$ and $-\delta$ would sum to an effective divisor linearly equivalent to $0$.
Exactly one of $\pm\delta$ is therefore effective, and it is $\delta$: were $-\delta$ effective, then $H_b\cdot(-\delta)\ge0$ because $H_b$ is nef (@prop:tuple-of-the-construction, part 3), against $H_b\cdot\delta>0$.
So $\delta\in\Delta_b$, and conversely a class of $\Delta_b$ has square $-2$ and pairs nonnegatively with the nef class (@def:nef-cone) $H_b$.
If now $\delta\in\Delta_b$ has $H_b\cdot\delta = 0$, write $\delta = \sum_ia_iC_i$ over irreducible curves with $a_i>0$: then $0 = \sum_ia_i(H_b\cdot C_i)$ with every term nonnegative, so $H_b\cdot C_i = 0$ for every $i$ and $C_i\in\RR_{\ge0}\alpha_b$ by @lem:face-at-H, part 2, that is $C_i = k_i\alpha_b$ with $k_i$ a positive integer. An irreducible curve of negative square satisfies $C_i^2 = 2p_a-2\ge-2$ by adjunction, while $(k_i\alpha_b)^2 = -2k_i^2$, so $k_i = 1$ and $C_i = \alpha_b$; hence $\delta = m\alpha_b$ with $m$ a positive integer, and $-2 = \delta^2 = -2m^2$ forces $m = 1$, while $\alpha_b\in\Delta_b$ by @prop:tuple-of-the-construction, part 3.
This proves (1).

*The chamber.*
By @def:coble-polarization-classes, part 3, $\mcc_b$ is the component of $\mathcal C_b\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp$ that contains $\Amp(\widehat X_b)$; a class of it pairs with a fixed $\delta\in\Delta_b$ with a sign that is constant on the connected set $\mcc_b$, and that sign is positive because $\Amp(\widehat X_b)\subseteq\mcc_b$ and an ample class is positive on an effective class.
The set displayed in (2) is convex, contains an ample class and meets no wall (@not:coxeter-polytope-faces), so it lies in a single component, which is then $\mcc_b$.
This proves (2).

*The action.*
The walls are the hyperplanes $\delta^\perp$ for $\delta$ of square $-2$, a set that every isometry of $S_{\Co,b}$ permutes, so $\psi$ carries components of the complement to components; and it preserves $\mathcal C_b$, the component of the positive cone containing $H_b$, because $\psi H_b = H_b$.
For $\delta$ in the first piece of (1) one has $(\psi\delta)^2 = -2$ and $H_b\cdot\psi\delta = \psi^{-1}H_b\cdot\delta = H_b\cdot\delta>0$, so $\psi\delta$ lies in that piece; and $\psi\alpha_b = \alpha_b$.
Hence $\psi(\Delta_b)\subseteq\Delta_b$, and applying the same to $\psi^{-1}$ turns this into equality.
Then, by (2),
$$\psi(\mcc_b) = \set{x\in\mathcal C_b : (\psi^{-1}x)\cdot\delta>0 \ \text{for all}\ \delta\in\Delta_b} = \set{x\in\mathcal C_b : x\cdot\psi\delta>0 \ \text{for all}\ \delta\in\Delta_b} = \mcc_b.$$
This proves (3).

For the last assertion: an isometry of $\lkt$ commuting with $I_\Co$ preserves the $(+1)$-eigenspace of $I_\Co$, which is $S_{\Co,b}$, and hence also its orthogonal complement $T_\Co$; fixing $H$ and $\alpha$ it induces $\psi\in\Orth(S_{\Co,b})$ with $\psi H_b = H_b$ and $\psi\alpha_b = \alpha_b$, so (3) applies, and the two centralizers agree because the second condition is then redundant.
:::

::: {.remark #rmk:chamber-pinned-scope title="What the hypothesis $\Pic(\widehat X_b) = S_{\Co,b}$ buys, and where it fails"}

The hypothesis is used in (1) and nowhere else: with it $\Delta_b$ is a set of classes of $S_{\Co,b}$, and (1) then says that it is the set of classes of square $-2$ pairing positively with $H_b$, together with $\alpha_b$ — a set determined by the two labels and the lattice, not by the member.

The hypothesis is not redundant in the direction that matters, but the witness that would show it has to exist at a member of the construction, and there it does not. At a member whose Picard lattice is larger than $S_{\Co,b}$ the extra classes are not functions of the labels, and they cut the chamber. For $\delta\in\Pic(\widehat X_b)\cap T_\Co$ effective of square $-2$ the reflection $s_\delta$ fixes $H_b$ and $\alpha_b$ and commutes with both involutions, since $I_\Co$ and $I_{\mathrm{dP}}$ both act on $\delta\in T_\Co$ by $-1$; it acts trivially on $A_{T_\Co}$, so the pair $(\id_{S_\Co},s_\delta)$ is an element of $Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}$ (@thm:automorphism-lifting-criterion); and it negates the effective class $\delta$, whose sign is constant and positive on $\mcc_b$, so it preserves neither $\Delta_b$ nor $\mcc_b$. But no such $\delta$ exists at a member of the construction: by @prob:B24, no period of the construction lies on a wall $\delta^\perp$ of a class of square $-2$ in $T_\Co$, that is $\Pic(\widehat X_b)\cap T_\Co$ contains no class of square $-2$ at any member. The extra classes of the members with larger Picard lattice are therefore not of that shape — at the member of @thm:chamber-clause-fails they are the two $H_b$-degree-one components $C_\pm$ of a ruling fibre, of square $-2$ but with $C_++C_-$ the fibre class in $S_{\Co,b}$, and $C_+-C_-$ of square $-8$ — and whether a label centralizer element moves the chamber there is answered, in the affirmative, by @thm:chamber-subscript-is-a-condition: the witness is a reflection in a class of $T_\Co$ that is *not* algebraic at the member, applied to a class of the member's own Picard lattice.
The equality of centralizers in @thm:chamber-pinned-by-labels is therefore a statement about the members whose Picard lattice is exactly the invariant lattice, which exist by @prop:one-node-period-image, part 3; at a member with a larger one the chamber subscript is a genuine condition, and @thm:chamber-subscript-is-a-condition is the element that witnesses it.
So the two readings of the fourth bullet of @sec-labeled-lattice-data — a chamber cut by the classes the labels themselves generate, and a chamber cut by the member's own effective classes — part company at a member with more classes: the $(-2)$-witness above is excluded by @prob:B24, and the witness of @thm:chamber-subscript-is-a-condition is of another shape.
:::

::: {.theorem #thm:effective-roots-are-the-h-positive-ones title="At every member the effective classes of square $-2$ are the member's $H$-positive ones, with $\alpha_b$"}

In the situation of @prop:one-node-family, at every member $b$ of the construction,
$$\Delta_b = \set{\gamma\in\Pic(\widehat X_b) : \gamma^2 = -2,\ H_b\cdot\gamma>0}\cup\set{\alpha_b},$$
and $\alpha_b$ is the only class of $\Delta_b$ orthogonal to $H_b$.

So @thm:chamber-pinned-by-labels, part 1, holds at every member once $S_{\Co,b}$ is replaced by the member's own Picard lattice, and the member's arrangement is a function of $H_b$ and $\Pic(\widehat X_b)$ alone — not of the labels, and not of anything else about the member.
:::

::: {.proof}

Let $\gamma\in\Pic(\widehat X_b)$ have $\gamma^2 = -2$. If the effective sign of $\pm\gamma$ is $\gamma$ then $H_b\cdot\gamma\ge0$ because $H_b$ is nef (@prop:tuple-of-the-construction, part 3) and $\gamma$ is a nonnegative combination of effective curves; and if $H_b\cdot\gamma = 0$ then $\gamma = \alpha_b$ by @lem:face-at-H, part 4.

Conversely, let $h\definedas H_b\cdot\gamma>0$. Riemann--Roch gives $h^0(\gamma)+h^0(-\gamma) = 1+h^1(\gamma)\ge1$, and $H_b\cdot(-\gamma) = -h<0$ with $H_b$ nef excludes $h^0(-\gamma)>0$; so $h^0(\gamma)>0$ and $\gamma$ is effective. This is the argument @thm:chamber-clause-fails runs on its $H$-degree-one classes, and it does not use the degree (@def:graded-object) beyond its sign.
:::

::: {.theorem #thm:chamber-subscript-is-a-condition title="The chamber in the datum of the direct group is a genuine condition, and the element that moves it"}

Let $b$ be the member of @thm:chamber-clause-fails, with the two $H_b$-degree-one components $C_+,C_-$ of its ruling fibre, of square $-2$, of sum $C_++C_-\in S_{\Co,b}$, and let $v\definedas C_+-\widehat\iota_{\Co,b}C_+$ be the class of square $-4$ in $T_{\Co,b}\intersect\Pic(\widehat X_b)$ of @thm:direct-period-meets-minus-four (@rmk:chamber-pinned-scope). Then there is a class $\delta\in T_\Co$ of square $-2$ with $v\cdot\delta\neq0$, and for such a class
$$g\definedas s_\delta\;\in\;Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha},\qquad
g\;\notin\;Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha,\mcc}.$$
The element is the identity modulo $2$, so it lies in $\ker\rho_{T_\Co}$: the subscript cuts into the kernel, and nothing here is asserted about the image of the centralizer in $P$, which is @qst:chamber-subscript-image.
So the chamber subscript of @def:direct-group is a genuine condition at a member of the construction, and the implication (INV) of research#720 — every $g\in Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}$ preserves the tuple's model-effective arrangement — is false.
:::

::: {.proof}

*The class $\delta$ exists.* The classes of square $-2$ of $T_\Co$ span $T_\Co\tensor\QQ$, so a nonzero vector of $T_\Co$ pairs nontrivially with one of them, and $v^2 = -4$ makes $v$ nonzero. For the span: write $B\cong\latI_{2,9}$ with $T_\Co = B(2)$ and $B = \langle u_1,u_2\rangle\perp\langle c_1,\dots,c_9\rangle$ (@prop:tco-as-twist); the vectors $c_j$ and $u_i + c_1 + c_2$ have square $-1$ in $B$, hence $-2$ in $T_\Co$, and a vector orthogonal to all of them is orthogonal to the $c_j$, hence lies in $\langle u_1,u_2\rangle\otimes\QQ$, and orthogonal to $u_1+c_1+c_2$ and to $u_2+c_1+c_2$, hence orthogonal to $u_1$ and $u_2$, hence zero.

*$g$ fixes the labels.* The class $\delta$ lies in $T_\Co$, so $s_\delta$ is the identity on $S_\Co$ and, $H$ and $\alpha$ lying in $S_\Co$, fixes both; and $I_\Co$ and $I_{\mathrm{dP}}$ act on $T_\Co$ by $-\id$ (@prop:coble-transcendental, and the action of $I_{\mathrm{dP}}$ computed in @prop:direct-eq-heegner), so both commute with $s_\delta$ and both leave $S_\Co$ invariant, so $g$ commutes (@def:commutative-diagram) with both.

*$g$ is discriminant-trivial.* Every pairing in $\lkt$ is even, so $s_\delta(x)-x = (x\cdot\delta)\delta$ lies in $2\lkt$ and $s_\delta\equiv\id\pmod 2$; under the convention of @prop:gamma-co-reflective-set, part (3), that is $\rho_{T_\Co}(g) = \id$.

*The class $v$.* $\widehat\iota_{\Co,b}$ covers $\tau$, which carries the ruling fibre over $x=1$ to the one over $x=-1$ (@thm:direct-period-meets-minus-four, proof), so $C_+$ and $\widehat\iota_{\Co,b}C_+$ lie in disjoint fibres; $v$ is anti-invariant, hence in $T_\Co$, and $C_++\widehat\iota_{\Co,b}C_+$ is invariant, hence in $S_{\Co,b}$. The class $C_+-C_-$ is not anti-invariant, since $\widehat\iota_{\Co,b}$ does not carry the fibre over $x=1$ to itself, and it does not lie in $T_\Co$.

*$g$ moves the arrangement.* Write $m\definedas C_+\cdot\delta = \tfrac12 v\cdot\delta$, which is nonzero because $C_++\widehat\iota_{\Co,b}C_+$ lies in $S_{\Co,b}$ and $\delta\perp S_\Co$. Then
$$g(C_+) = C_+ + (C_+\cdot\delta)\,\delta = C_+ + m\delta,$$
again of square $-2$; and it is not a class of $\widehat X_b$: if $C_+ + m\delta$ were integral for the member, then $m\delta\in\Pic(\widehat X_b)$ with $m\neq0$, and $\Pic(\widehat X_b)$ being primitive in $\lkt$ this would put $\delta$ in it, whereas no period of the construction lies on a wall (@not:coxeter-polytope-faces) of a class of square $-2$ in $T_\Co$ (@prob:B24, part 1, @thm:direct-period-misses-root-walls). So $g(C_+)$ is not algebraic at $b$, hence not effective, and $g\Delta_b\neq\Delta_b$.

*$g$ moves the chamber.* Both $\mathfrak c_b$ and $g\mathfrak c_b$ contain $A_b$, since $A = 2H-\alpha$ lies in $S_\Co$, is fixed by $g$ and is ample. If the two chambers were equal, $g$ would carry each facet (@def:facet-maximal-face) of $\mathfrak c_b$ to a facet, and the facets lie in the walls $\gamma^\perp$ for $\gamma\in\Delta_b$ with the sign fixed by $A$-positivity (@def:coble-polarization-classes, part 3); so $g$ would permute the classes of $\Delta_b$, contradicting the previous paragraph. Hence $g\mathfrak c_b\neq\mathfrak c_b$, that is $g\notin Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha,\mcc}$.
:::

::: {.lemma #lem:known-part-of-the-picard-lattice-at-the-test-member title="The part of $\Pic(\widehat X_{b_\star})$ the record determines"}

At the member $b_\star$ of @thm:direct-period-meets-minus-four, let $D_{1,\pm}$ be the two components of the ruling fibre over $x=1$, $D_{-1,\pm}\definedas\widehat\iota_{\Co,b_\star}D_{1,\pm}$ those over $x=-1$, $f\definedas\widehat\pi^*h_1$ the fibre class, and $v\definedas D_{1,+}-D_{-1,+}$. Then

1. $D_{1,+}+D_{1,-} = D_{-1,+}+D_{-1,-} = f$, $D_{\pm1,\pm}^2=-2$, and $s_0\definedas D_{1,+}+D_{-1,+}\in S_{\Co,b}$;
2. $v\in T_\Co$ has $v^2=-4$, is primitive, and has divisibility $2$ in $T_\Co$;
3. the lattice $M\definedas S_{\Co,b}+\ZZ D_{1,+}$ spanned by $S_{\Co,b}$ and the four components is the index-two overlattice of $S_{\Co,b}\perp\langle v\rangle$ glued by $D_{1,+}=\tfrac12(s_0+v)$, of rank $12$, signature $(1,11)$ and $\abs{\det M}=2^{11}$;
4. $M\subseteq\Pic(\widehat X_{b_\star})$ and $T_{\Co,b_\star}\subseteq v^{\perp T_\Co}$, a lattice of rank $10$, signature $(2,8)$ and $\abs{\det}=2^{11}$; so $\rho(\widehat X_{b_\star})\ge12$.

The difference $C_+-C_-$ of the two components over one fibre is not in $T_\Co$: it is $2D_{1,+}-f$, and its image $2D_{-1,+}-f$ is a different class.
:::

::: {.proof}

(1) @thm:direct-period-meets-minus-four and its proof give the components, their squares and $D_{1,+}\cdot D_{1,-}=2$. $\widehat\iota_{\Co,b_\star}$ covers $\tau$, which preserves the ruling $h_1$, so $f$ is invariant; $s_0$ is invariant because $\widehat\iota_{\Co,b_\star}$ is an involution exchanging $D_{1,+}$ and $D_{-1,+}$, and $S_{\Co,b}$ is the invariant lattice.

(2) $v$ is anti-invariant, so $v\in T_\Co$; $v^2=-4$ and primitivity are @thm:direct-period-meets-minus-four. $T_\Co = B(2)$ with $B$ unimodular (@prop:tco-as-twist), so $v\cdot T_\Co = 2(v'\cdot B)$ for $v=v'$ read in $B$, and $v'$ is primitive in $B$, so $v'\cdot B=\ZZ$ and the divisibility is $2$.

(3) $D_{1,-}=f-D_{1,+}$ and $D_{-1,\pm}$ lie in $S_{\Co,b}+\ZZ D_{1,+}$, and $2D_{1,+}=s_0+v$. $D_{1,+}\notin S_{\Co,b}\perp\langle v\rangle$, since $v\cdot D_{1,+} = -2$ and $\tfrac{v\cdot D_{1,+}}{v^2}=\tfrac12$. So the index is $2$ and $\abs{\det M}=2^{11}\cdot4/4=2^{11}$, with $\abs{\det S_{\Co,b}}=2^{11}$ (@prop:coble-invariant-lattice).

(4) The components are curves, so $M\subseteq\Pic$; the transcendental lattice is orthogonal to $v$ and lies in $T_\Co$. $\abs{\det v^{\perp T_\Co}} = \abs{\det T_\Co}\cdot\abs{v^2}/\div(v)^2 = 2^{11}\cdot4/4$.
:::

::: {.lemma #lem:chamber-condition-is-period-condition title="The chamber condition is a linear condition on the period, not a count of chambers"}

In the situation of @thm:chamber-subscript-is-a-condition, let $g\in Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}$ and let $\omega_b$ be a holomorphic $2$-form on $\widehat X_b$, with $\langle\Delta_b\rangle$ the span of the effective classes of square $-2$ in $H^2(\widehat X_b,\ZZ)$. Then

1. for $\gamma\in\Delta_b$ the class $g\gamma$ has square $-2$ and $H_b$-degree $H_b\cdot\gamma$, and $g\gamma\in\Delta_b$ if and only if $g^{-1}\omega_b\perp\gamma$;
2. consequently $g\mathfrak c_b = \mathfrak c_b$ if and only if $g^{-1}\omega_b\perp\langle\Delta_b\rangle$.

So the chamber subscript of @def:direct-group is a linear condition on the transport of the period, and not a condition to be read off from the arrangement of chambers.
:::

::: {.proof}

(1) $g$ is an isometry, so $(g\gamma)^2 = -2$, and it fixes $H$, so $H_b\cdot g\gamma = H_b\cdot\gamma$; write $h\definedas H_b\cdot\gamma\ge0$, the class being effective. If $h>0$ then Riemann--Roch gives $h^0(g\gamma)+h^0(-g\gamma)\ge1$ on the member whose Picard lattice contains $g\gamma$, and $H_b\cdot(-g\gamma) = -h<0$ with $H_b$ nef excludes the second summand, so $h^0(g\gamma)>0$; this is the argument @thm:chamber-clause-fails runs on its $H$-degree-one classes. Such a class is effective if and only if it is algebraic, that is if and only if $\omega_b\perp g\gamma$, which is $g^{-1}\omega_b\perp\gamma$. If $h = 0$ then $\gamma = \alpha_b$ by @lem:face-at-H, part 4, and $g\alpha_b = \alpha_b$ because $\alpha\in S_\Co$ and $g$ fixes $S_\Co$.

(2) $g\mathfrak c_b = \mathfrak c_b$ exactly when $g$ permutes the walls (@not:coxeter-polytope-faces) of $\mathfrak c_b$, that is when $g\Delta_b = \Delta_b$; by (1) and the injectivity of $g$ that is the stated orthogonality.
:::

::: {.corollary #cor:chamber-preserved-by-picard-stabilizer title="Preserving the Picard lattice preserves the chamber"}

In the situation of @lem:chamber-condition-is-period-condition, let $g\in Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}$ satisfy $g\Pic(\widehat X_b) = \Pic(\widehat X_b)$ as sublattices of $\lkt$. Then $g\mathfrak c_b = \mathfrak c_b$. Conversely, if the effective classes of square $-2$ span $\Pic(\widehat X_b)\tensor\QQ$, the two conditions are equivalent.

Hence the question of @qst:chamber-subscript-image is the question whether the stabilizer (@def:group-orbit) of the member's Picard lattice surjects onto $P$, and a surjection there is sufficient, with no hypothesis on the effective classes, for the image of the centralizer to be all of $\Gamma^{\mathrm{dir}}_{\Co,2}$.
:::

::: {.proof}

Write $\Pic_b\definedas\Pic(\widehat X_b)$, so that $\Pic_b = \omega_b^\perp\intersect\lkt$. Suppose $g\Pic_b = \Pic_b$, and let $x\in\Pic_b$: then $g^{-1}x\in\Pic_b$, so $\omega_b\perp g^{-1}x$, so $g^{-1}\omega_b\perp x$ because $(g^{-1}\omega_b, x) = (\omega_b, g^{-1}x)$. Since $\langle\Delta_b\rangle\subseteq\Pic_b\tensor\QQ$ (the effective classes are classes of the member), @lem:chamber-condition-is-period-condition gives $g\mathfrak c_b = \mathfrak c_b$.

Conversely, suppose the effective classes span $\Pic_b\tensor\QQ$. Orthogonality to $\langle\Delta_b\rangle$ is then orthogonality to $\Pic_b$, which says $g^{-1}\omega_b\perp\Pic_b$; then $\omega_b\perp g\Pic_b$ by the same identity, that is $g\Pic_b\subseteq\omega_b^\perp\intersect\lkt = \Pic_b$, and the two lattices have equal rank, so the inclusion is an equality.
:::

::: {.corollary #cor:construction-monodromy title="The monodromy of the one-node construction lies in the stabilizer of its lattice labels"}

In the situation of @prop:one-node-family the monodromy representation (@def:transport-and-monodromy) of $R^2\widehat\pi_*\ZZ$ on $H^2(\widehat X_b,\ZZ)$ lands, after a marking, in the stabilizer (@def:group-orbit) in $\Orth(\lkt)$ of the quadruple $(S_\Co,S_{\mathrm{dP}},H,\alpha)$, that is in the group (@def:group) of isometries that commute with both involutions and fix $H$ and $\alpha$.
:::

::: {.proof}

Monodromy is parallel transport (@cons:calculus-transport) along loops (@def:loops-suspension), which by @thm:one-node-transport preserves each of the four pieces.
:::

::: {.corollary #cor:d1-minus-two-half title="(D1) for the walls of square $-2$, from the period image alone"}

In the situation of @prop:one-node-family, every Heegner divisor $\delta^\perp$ with $\delta\in T_\Co$ of square $-2$ is contained in the complement of the period image. Hence the family's discriminant meets every orbit (@def:group-orbit) of the walls (@not:coxeter-polytope-faces) of square $-2$ under $\Gamma^{\mathrm{dir}}_{\Co,2}$, and it meets each such wall: the $(-2)$-half of (D1) of research#720 holds, and no local monodromy (@cons:pf-from-jacobian) input enters it.
:::

::: {.proof}

That the image meets no such wall is @prob:B24, part 1, whose statement is exactly that no period of the construction lies on $\delta^\perp$ for $\delta$ of square $-2$.
A wall disjoint from the image is a subset of the complement, which is the discriminant; and since this holds for every class of square $-2$, for every orbit of walls at least one member — in fact every member — lies in the discriminant.
:::

::: {.proposition #prop:monodromy-contains-root-reflections title="The monodromy contains the reflection in every $(-2)$-class, given the meridian statement"}

With $\Gamma^{\mathrm{geom}}$ the image of the monodromy representation of @cor:construction-monodromy in $\Orth(T_\Co)$, suppose that for every class $\delta\in T_\Co$ of square $-2$ the meridian of the Heegner divisor $\delta^\perp$ acts on $T_\Co$ by the reflection $s_\delta$ — the local statement the record computes at the two wall (@not:coxeter-polytope-faces) types of the construction (`computations/reports/smwo_direct-period.md`:833-838). Then $s_\delta\in\Gamma^{\mathrm{geom}}$ for every such $\delta$, and
$$W(T_\Co)\subseteq\Gamma^{\mathrm{geom}}.$$
:::

::: {.proof}

Fix $\delta$ of square $-2$. By @cor:d1-minus-two-half the wall $\delta^\perp$ lies in the complement of the image, so a point of it is not a realized period and a small circle in the ambient domain around that point avoids the wall and lies in the image.
That circle is a loop of the construction, and the monodromy of a loop is an element of $\Gamma^{\mathrm{geom}}$; by the hypothesis its monodromy is $s_\delta$.
Since $\delta$ was arbitrary and $W(T_\Co)$ is by definition the group generated by the reflections in the classes of square $-2$ (@prop:gamma-co-reflective-set), the inclusion follows.
:::

::: {.theorem #thm:d1-minus-four-half title="The $(-4)$ half of (D1) fails, and (D1) with it"}

Let $L\definedas\set{c\in A_{T_\Co} : q_{T_\Co}(c) = 1}$, the level set of @rmk:coble-discriminant-levels, which has $496$ classes, and let $B\subseteq L$ be the $121$ classes that @prob:B24, part 2 carries there and whose walls (@not:coxeter-polytope-faces) the image misses.
Then $B\neq L$ and $B$ is stable under $\Gamma^{\mathrm{dir}}_{\Co,2}$; consequently $L\setminus B$ is a nonempty stable set, it is a union of orbits (@def:group-orbit), and for every class of such an orbit the wall is met by the image. So the family's discriminant meets every orbit of walls if and only if $B = L$, which it is not: the $(-4)$ half of (D1) of research#720 fails, and with it (D1) as the register states it.
:::

::: {.proof}

*The size.* $|L| = 496$ is the level count of @rmk:coble-discriminant-levels, reproduced from the Gram matrix of $T_\Co = \langle 2\rangle\perp U(2)\perp E_8(2)$ by the record `computations/reports/coble_663-d1-level-orbits.py` and its transcript.
$|B| = 121$ is @prob:B24, part 2.

*The stability.* $\mathrm{BAD}_S\subseteq A_{S_\Co}$ is the level set of $q_{S_\Co}$ whose classes carry a vector of square $-4$, so every isometry of $(A_{S_\Co}, q_{S_\Co})$ preserves it; $B = \gamma_\Co(\mathrm{BAD}_S)$, and $\Gamma^{\mathrm{dir}}_{\Co,2}$ acts on $A_{T_\Co}$ through $\rho_{T_\Co}$, whose image is $P = \gamma_\Co P_{S_\En}\gamma_\Co^{-1}$ (@prop:direct-eq-heegner). Hence $P\cdot B = \gamma_\Co(P_{S_\En}\cdot\mathrm{BAD}_S) = B$.

*The consequence.* $121 < 496$ makes $L\setminus B$ a nonempty $P$-stable subset of a finite set, hence a union of $P$-orbits; pick one. By part 2 of @prob:B24 the walls the image misses are exactly those of the classes of $B$ — that is the excluded set the register states — so every class of this orbit has its wall met by the image, and the discriminant misses the orbit.
:::

::: {.corollary #cor:d1-concrete-witness title="An exhibited class of the level set whose wall the image meets"}

Let $v$ be the class of @thm:direct-period-meets-minus-four — a primitive class of square $-4$ in $T_{\Co,b_\star}\intersect\Pic(\widehat X_{b_\star})$, whose period lies on $v^\perp$ — and let $L$ and $B$ be as in @thm:d1-minus-four-half. Then

1. the class $[v/2]$ lies in $L$;
2. $[v/2]\notin B$, and its orbit (@def:group-orbit) under $P = \gamma_\Co P_{S_\En}\gamma_\Co^{-1}$ lies in $L\setminus B$;
3. every class of that orbit has its wall (@not:coxeter-polytope-faces) met by the image.

So the failure of the $(-4)$ half is exhibited by a class and not only by a count, and $L\setminus B$ contains the whole $P$-orbit of $[v/2]$.
:::

::: {.proof}

(1) $v^2 = -4$ gives $q_{T_\Co}([v/2]) = v^2/4 = -1\equiv1\pmod 2$, so $[v/2]$ lies at the level $1$ (@prop:coble-transcendental for the normalization of $q$).

(2) The period of $b_\star$ lies on $v^\perp$ (@thm:direct-period-meets-minus-four), so $v^\perp$ is met by the image; but the walls the image misses are exactly the walls of the classes of $B$ (@prob:B24, part 2, as @thm:d1-minus-four-half uses it). So $[v/2]\notin B$, and $B$ being stable under $P$ (@thm:d1-minus-four-half), the orbit of $[v/2]$ misses $B$ too.

(3) is the argument of @thm:d1-minus-four-half: a class of $L\setminus B$ has a wall the image meets.
:::

A remark on what the statement is sensitive to. The failure is also exhibited by a class and not only counted: @cor:d1-concrete-witness takes the primitive class $v$ of square $-4$ that @thm:direct-period-meets-minus-four produces at $b_\star$ and shows that $[v/2]$ lies in $L\setminus B$ with its whole $P$-orbit. The argument uses only that the excluded set is $B$; it does not use the orbit decomposition, which the same record computes for the group generated by the swap of the isotropic generators of $U(2)$ and the orthogonal transvections of $E_8(2)$: four orbits, of sizes $240$, $135$, $120$ and $1$, among which $121 = 120 + 1$ is the only subset sum equal to $|B|$. That is consistent with $B$ being the two smallest orbits and is corroboration, not the proof. Were the excluded set a union of orbits containing one of the other two, the statement would change; no reading on record gives that.

::: {.proposition #prop:det-saturation-del-pezzo title="The del Pezzo invariant lattice is the flat lattice, index one"}

Let the branch curve $B$ have at most one node, at a $\tau$-fixed point $p$ and with nondegenerate (@def:polarization) quadratic part there, and be otherwise smooth.

1. If $B$ has one node, let $\widehat X_b$ be the resolved K3 surface of @prop:del-pezzo-type-on-the-resolution, the double cover of $\widehat Y = \Bl_p(\PP^1\times\PP^1)$ branched along the smooth proper transform (@def:strict-transform) $\widetilde B$, with $e_b = \widehat\pi^*h_1$, $f_b = \widehat\pi^*h_2$ the ruling pullbacks (@def:pullback-square) and $D_b = \widehat\pi^*e$ the exceptional $(-2)$-curve. Then
$$S_{\mathrm{dP},b}=H^2(\widehat X_b,\ZZ)^{\widehat\iota_{\mathrm{dP}}=+1}
=\Lambda\definedas\langle e_b,f_b,[D_b]\rangle\cong U(2)\perp\langle-2\rangle,\qquad \det S_{\mathrm{dP},b} = 8,$$
and the index-$2$ overlattice (@def:overlattice) $U\perp\langle-2\rangle$ (determinant $2$) does not occur. In particular every $I_{\mathrm{dP}}$-invariant class pairs evenly with each ruling class.
2. If $B$ is smooth, then $S_{\mathrm{dP}} = \pi^*H^2(Y,\ZZ)\cong U(2)$.
:::

::: {.proof}

Write $L\definedas H^2(\widehat X_b,\ZZ)$ and $S\definedas S_{\mathrm{dP},b}$, and prove (1); the proof of (2) is the same with $\widehat Y$ replaced by $Y$ and $D_b$ omitted.

*Step 1 (index (@def:index) bound).* $S$ is even (@def:form-axioms) and primitive (@def:primitive-embedding) in $L$. Since $\widehat\pi$ is finite flat of degree (@def:graded-object) $2$, the transfer formula $\widehat\pi^*\widehat\pi_* = 1+\widehat\iota_{\mathrm{dP}}^*$ sends $x\in S$ to $2x = \widehat\pi^*\widehat\pi_*x\in\widehat\pi^*H^2(\widehat Y,\ZZ) = \Lambda$. So $2S\subseteq\Lambda\subseteq S$, the two lattices have equal rank, and $[S:\Lambda]^2$ divides $\det\Lambda = 8$; hence $[S:\Lambda]\in\set{1,2}$.

*Step 2 (what index $2$ would impose).* Suppose $[S:\Lambda]=2$. Pick $z\in S\setminus\Lambda$ and write $2z=ae_b+bf_b+cD_b$ with $a,b,c\in\ZZ$. Then $z^2=ab-\tfrac{c^2}2$. Integrality of $z^2$ forces $c$ even, and evenness of $S$ forces $ab$ even. If $a$ and $b$ are both even then $z\in\Lambda$, contrary to the choice. Hence exactly one of $a,b$ is odd (@def:two-elementary-isotropic-types), and exactly one of $e_b/2,f_b/2$ lies in $S$; in particular $e_b\in2L$ or $f_b\in2L$.

*Step 3 (no ruling line lies in $B$).* Let $M$ be a line of either ruling of $Y$, and suppose $B = M+B'$. Then $M\cdot B' = 4$, and every point of $M\cap B'$ is a singular point of $B$. The point $p$ is an ordinary (@def:two-elementary-isotropic-types) node, so if $p\in M$ then $M$ and $B'$ are the two branches of $B$ at $p$ and meet there with intersection multiplicity $1$. So $M\cap B'$ contains a point other than $p$, and $B$ has a second singular point, a contradiction.

*Step 4 (each fibre is a reduced divisor).* The linear system $|e_b|$ is base-point free, because $e_b=\widehat\pi^*h_1$ and $|\OO_Y(1,0)|$ is base-point free; let $\varphi\colon\widehat X_b\to\PP^1$ be the fibration it defines. Its fibres are $\widehat\pi^*M'$ for the members $M'$ of $|h_1|$ on $\widehat Y$. These are reduced divisors: the proper transforms of the lines of the first ruling not through $p$ and, for the line $M_p$ through $p$, the divisor $\widetilde M_p+e$. No component of them lies in $\widetilde B$: a proper transform of a line does not by Step 3, and $e$ does not because $e\cdot\widetilde B = 2$. So $\widehat\pi$ is étale over the generic point of each component, and $\widehat\pi^*M'$ is reduced. So every component of every fibre of $\varphi$ has multiplicity $1$.

*Step 5 (the ruling classes are primitive in $L$).* Suppose $e_b = 2\eta$ with $\eta\in L$; then $\eta\in\mathrm{NS}(\widehat X_b)$, since $e_b$ is of type $(1,1)$. Then $\eta^2=0$, $\eta\cdot e_b=0$ and $\eta\cdot f_b=1$. Since $(-\eta)\cdot f_b=-1<0$ and $f_b$ is nef, $h^0(-\eta)=0$; Riemann–Roch on the K3 surface then gives $h^0(\eta)\ge2$, so let $E\in|\eta|$. Each component of $E$ lies in a fibre of $\varphi$, because $\eta\cdot e_b=0$ and $e_b$ is nef. Group (@def:group) the components by fibre, $E=\sum_v E_v$ with disjoint supports. Then $\sum_vE_v^2 = E^2 = 0$ and each $E_v^2\le0$ by Zariski's lemma, so each $E_v^2 = 0$, and Zariski's lemma gives $E_v=q_vF_v$ with $q_v\in\QQ_{\ge0}$. By Step 4 every coefficient of $F_v$ is $1$, so $q_v\in\ZZ_{\ge0}$. But then
$$1=\eta\cdot f_b=\sum_v q_v\,(e_b\cdot f_b)=2\sum_v q_v,$$
which is impossible. Hence $e_b$ is primitive in $L$, and the same argument with the rulings exchanged shows that $f_b$ is primitive.

*Conclusion.* By Step 5 neither $e_b/2$ nor $f_b/2$ lies in $L$, so by Step 2 the index is not $2$, and $[S:\Lambda]=1$ by Step 1.
:::

::: {.proposition #prop:node-count-invariant title="The number of $\tau$-fixed nodes is an invariant of the tuple"}

Let $f,f'$ be $\tau$-invariant sections of $\OO_Y(4,4)$ whose branch curves have exactly $k$, respectively $k'$, ordinary (@def:two-elementary-isotropic-types) nodes at $\tau$-fixed points and are otherwise smooth with nondegenerate (@def:polarization) quadratic part at those points, and let $\mathfrak L,\mathfrak L'$ be the tuples @prop:tuple-of-the-construction attaches to them. Then $\mathfrak L$ and $\mathfrak L'$ are conjugate in $\Orth(\lkt)$ only if $k = k'$. Both $k = 1$ and $k = 2$ occur.
:::

::: {.proof}

A conjugation preserving the labels carries $I_{\mathrm{dP}}$ to $I'_{\mathrm{dP}}$, and conjugate involutions have isometric invariant lattices (@def:invariant_coinvariant_lattices), of ranks $k+2$ and $k'+2$ by @prop:tuple-of-the-construction; hence $k = k'$.

For the occurrence: the value of a $\tau$-invariant section at the $\tau$-fixed point $([1:0],[1:0])$ is the coefficient of $x_0^4y_0^4$, and correspondingly $x_0^4y_1^4$, $x_1^4y_0^4$, $x_1^4y_1^4$ at the other three fixed points. These four monomials are independent, and every other invariant monomial vanishes at all four points, so the conditions $f(p) = 0$ at chosen fixed points and $f\neq0$ at the others are independent hyperplane conditions in the $\bP^{12}$ of @sec-invariant-system. By @lem:node-condition the general member of each stratum has an ordinary node at each chosen fixed point; degeneracy of the quadratic part there and nodes elsewhere are proper closed conditions, so the general member has neither. Taking one, respectively two, chosen points gives $k = 1$ and $k = 2$.
:::

::: {.proposition #prop:rank-two-slot-boundary title="The rank-two del Pezzo slot"}

In the notation of @prop:no-rank-one-automorphism let $\rank(S\cap S') = 2$.
Then $S\cap S' = S'$, so $S'\subseteq S$; taking isotropic classes (@def:descent-class) $a_1,a_2$ of $S'\cong U(2)$ with $a_1\cdot a_2 = 2$, one has $H = \pm(a_1+a_2)$, and $\alpha = p(a_1-a_2)+\beta$ with $\beta\perp S'$ and $p\in\bQ$ satisfies:
1. $\beta\in S\otimes\bQ\cap H^{\perp}$, which is negative definite (@def:definiteness), so $\beta^2\le0$; and $\beta^2 = -2+4p^2$, so $p^2\le\tfrac12$; since $\alpha\cdot a_1 = -2p\in\bZ$, this leaves $\alpha\cdot a_1\in\set{-1,0,1}$.
2. $\iota'(\alpha) = -\alpha$ exactly when $\alpha\cdot a_1 = 0$, and in that case no automorphism of $\widetilde X$ induces $\iota'$.
3. In the marking of @prop:coble-cover-marking, $S' = \langle f^*F_1,f^*F_2\rangle$ and $\alpha\cdot f^*F_1 = \alpha\cdot f^*F_2 = 0$, so no automorphism of $X$ induces the rank-two slot.
:::

::: {.proof}

$\rank(S\cap S') = 2 = \rank S'$ and $S\cap S'$ is saturated in $S'$, so the two coincide and $S' = \langle a_1,a_2\rangle$ with $a_i$ isotropic and $a_1\cdot a_2 = 2$. Writing $H = ma_1+na_2$ gives $H^2 = 4mn = 4$, so $(m,n) = \pm(1,1)$.
Decompose $\alpha$ over $\bQ$ as $\alpha = (pa_1+qa_2)+\beta$ with $\beta\perp S'$; then $\alpha\cdot H = 2(p+q) = 0$, so $q = -p$ and the $S'$-component of $\alpha$ is $p(a_1-a_2)$, of square $-4p^2$; the cross terms with $\beta$ vanish, so $\beta^2 = \alpha^2+4p^2 = -2+4p^2$.
$\beta$ lies in $S\otimes\bQ$ and is orthogonal to $H$, so $\beta^2\le0$ by the proof of @prop:no-rank-one-automorphism, giving $p^2\le\tfrac12$; and $\alpha\cdot a_1 = -2p$ is an integer because both classes lie in the lattice, leaving $\alpha\cdot a_1\in\set{-1,0,1}$.
Since $\iota'$ is $\id$ on $S'$ and $-\id$ on $S'^{\perp}$, $\iota'(\alpha) = p(a_1-a_2)-\beta$, which equals $-\alpha$ exactly when $p = 0$, that is exactly when $\alpha\cdot a_1 = 0$. The effectivity argument of @prop:no-rank-one-automorphism then shows that no automorphism induces $\iota'$.
(3) By @lem:rank-two-slot-unique, $S' = \langle f^*F_1,f^*F_2\rangle$. In the basis (@def:based-module) of @prop:coble-cover-marking, $\alpha\cdot f^*F_1 = (3e_0-\Sum_{i\le10}e_i)\cdot(3e_0-\Sum_{i\le9}e_i) = 18-18 = 0$, and the same computation gives $\alpha\cdot f^*F_2 = 0$. So part 2 applies, as @cor:no-del-pezzo-involution-coble-cover also shows.
:::

::: {.proposition #prop:rank-one-slot-hodge-locus title="The periods at which the rank-one slot is a Hodge isometry"}

Let $t$, $b$ and $J$ be as in @prop:rank-one-slot. Let $X$ be a K3 surface with a marking $H^2(X,\ZZ)\iso\lkt$ under which $S_\Co\subseteq\Pic(X)$, and let $\omega$ span $H^{2,0}(X)$.
Then $2t\in T_\Co$ and $(2t)^2 = -4$, and $J$ is a Hodge isometry (@not:k3-automorphism-data) of $H^2(X,\ZZ)$ if and only if $\omega\cdot 2t = 0$, that is, if and only if $2t\in\Pic(X)$.
The orthogonal complement $(2t)^{\perp T_\Co}$ has rank $10$ and signature $(2,8)$.
:::

::: {.proof}

By @prop:rank-one-slot, part 2, and its proof, $t\in T_\Co^{\#} = \tfrac12T_\Co$ and $t^2 = -1$; so $2t\in T_\Co$ and $(2t)^2 = -4$.
$J$ is a Hodge isometry exactly when $J\omega\in\CC\omega$. Since $J$ is an involution, the scalar is $\pm1$.
The scalar $+1$ is impossible: then $\omega$ and $\bar\omega$ lie in the $(+1)$-eigenspace $\langle H,b\rangle\otimes\CC$, so the positive definite (@def:definiteness) real $2$-plane spanned by $\operatorname{Re}\omega$ and $\operatorname{Im}\omega$ lies in $\langle H,b\rangle\otimes\RR$, which has signature $(1,1)$.
The scalar $-1$ holds exactly when $\omega\perp\langle H,b\rangle$. Since $H\in S_\Co\subseteq\Pic(X)$, $\omega\cdot H = 0$, and so $\omega\cdot b = \omega\cdot(\tfrac12H+t) = \omega\cdot t$. Hence $J$ is a Hodge isometry exactly when $\omega\cdot 2t = 0$, and by the Lefschetz theorem on $(1,1)$-classes an integral class orthogonal to $\omega$ lies in $\Pic(X)$.
$T_\Co$ has signature $(2,9)$ and $2t$ has negative square, so its orthogonal complement in $T_\Co$ is nondegenerate of rank $10$ and signature $(2,8)$.
:::


## Which of the arithmetic groups is $\widetilde\Orth^+(T_\Co)$ {#sec-gamma-co-comparison}

The **stable group** is
$$
\widetilde\Orth^+(T_\Co) \definedas \Orth^+(T_\Co)^* = \Orth^+(T_\Co)\intersect\discriminantkernel{T_\Co}.
$$

::: {.proposition #prop:gamma-co-in-heegner-group title="The stable group inside the Heegner group"}

Let $\delta\in\ten$ be the $(-2)$ vector of @lem:coble-heegner-vector, so that $\delta^{\perp\ten} = T_\Co$, the sublattice $\ZZ\delta\oplus T_\Co$ has index $2$ in $\ten$, and the gluing class is $\tfrac12\zeta\in A_{T_\Co}$; let $\gent$ be the degree-$2$ Enriques group of @prop:gamma-en-two-gluing.
Put
$$
\Gamma^{\mathrm{Hdg}}_\Co
\definedas
\theset{\;
\varphi\in\Orth^+(T_\Co)
\;\middle|\;
\exists\, g\in\Stab_{\gent}(\ZZ\delta)\ \text{with}\ \restrictionof{g}{T_\Co} = \varphi
\;}
,
$$
the part of the image of @def:gamma-co-en that lies in $\Orth^+(T_\Co)$.
Then

1. $\widetilde\Orth^+(T_\Co)\iscontainedin\Gamma^{\mathrm{Hdg}}_\Co$, by $\varphi\mapsto\varphi\oplus\id_{\ZZ\delta}$;
2. $\widetilde\Orth^+(T_\Co) = \ker\bigl(\Gamma^{\mathrm{Hdg}}_\Co\too\Orth(A_{T_\Co}, q_{T_\Co})\bigr)$, so $\widetilde\Orth^+(T_\Co)$ is normal in $\Gamma^{\mathrm{Hdg}}_\Co$ and
   $$
   [\Gamma^{\mathrm{Hdg}}_\Co : \widetilde\Orth^+(T_\Co)]
   = \abs{\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr)}
   \leq \abs{W(E_8)} = 696\,729\,600
   ;
   $$
3. $\Gamma^{\mathrm{Hdg}}_\Co = \widetilde\Orth^+(T_\Co)$ if and only if every element of $\gent$ that preserves the Heegner line acts trivially on the discriminant form of $T_\Co$.
:::

::: {.proof}

(1) Let $\varphi\in\widetilde\Orth^+(T_\Co)$.
The isometry $g_T \definedas \varphi\oplus\id_{\ZZ\delta}$ of $\ZZ\delta\oplus T_\Co$ acts as the identity on $A_{\ZZ\delta}\oplus A_{T_\Co}$: on the second summand because $\varphi\in\ker\rho_{T_\Co}$, and on the first because $A_{\ZZ\delta}\cong\ZZ/2\ZZ$ has trivial automorphism group.
It therefore preserves the gluing subgroup $\generators{(\tfrac12\delta, \tfrac12\zeta)}$ of @lem:coble-heegner-vector, and by @cor:liftable-automorphisms it extends over the overlattice $\ten$ while fixing $\ZZ\delta$ pointwise.
The extension acts trivially on $A_{\ten} = H^{\perp}/H$, since that is a subquotient of the discriminant group on which $g_T$ is the identity.
In the description of @prop:gamma-en-two-gluing take $g_S = \id_{S_\En}$: it fixes $h$, and $\bar g_T\circ\gamma = \gamma = \gamma\circ\bar g_S$ because $\bar g_T = \id$.
Hence $g_T\in\gent$ by that proposition, and $g_T(\delta) = \delta$, so $g_T\in\Stab_{\gent}(\ZZ\delta)$ and its restriction to $T_\Co$ is $\varphi$.

(2) An element of $\Gamma^{\mathrm{Hdg}}_\Co$ is an isometry of $T_\Co$, so its image under $\rho_{T_\Co}$ is defined without a choice of lift, and by (1) the kernel is $\Orth^+(T_\Co)\intersect\ker\rho_{T_\Co} = \widetilde\Orth^+(T_\Co)$.
The index equals the order of the image by the first isomorphism theorem.

For the bound, the image of $\Stab_{\gent}(\ZZ\delta)$ is a subgroup of that of $\gent$.
Restricting $g\in\gent$ to $T_\Co$ gives an isometry with the same discriminant action on the common factor: by @prop:coble-discriminant-group every isometry of $q_{T_\Co}$ fixes the class $\tfrac12\zeta$ and respects the orthogonal decomposition $A_{T_\Co} = \ZZ\tfrac12\zeta\perp A^0$ with $A^0\cong A_{E_{10}(2)}$, so the discriminant representation (@def:discriminant-rep) factors through the isomorphism $\Orth(A_{T_\Co},q_{T_\Co})\iso\Orth(A^0, q_{T_\Co}|_{A^0})$; under it $A^0 = A_{U(2)}\oplus A_{E_8(2)} = A_{\ten}$ with the same form, which is the identification of $A_{\ten}$ with $H^{\perp}/H$ used in @thm:normalization. On $A_{\ten}$ the image of $\gent$ is the $\gamma$-transport of the image of $\Stab_{\Orth(S_\En)}(h)$ described in @prop:gamma-en-two-gluing.
That image is a quotient of $\Stab_{\Orth(S_\En)}(h)$, which by @prop:polarization-stabilizer-enriques is isomorphic to $\theset{\pm1}\times W(E_8)$ of order $2\abs{W(E_8)}$ and whose reduction to the discriminant group has $\id_U\oplus(-\id_{E_8})$ in its kernel by the last claim of that proposition; so the image has order at most $\abs{W(E_8)}$, and the same bound holds for $\rho_{T_\Co}(\Gamma^{\mathrm{Hdg}}_\Co)$.

(3) By (2), the index is one exactly when the image is trivial.
:::

::: {.proposition #prop:gamma-co-in-theta-centralizer title="The stable group inside the Coble centralizer"}

Let $S_\Co\injects\lkt$ be the primitive embedding of @prop:coble-invariant-lattice, with complement $T_\Co$ and gluing anti-isometry $\gamma_\Co\colon A_{S_\Co}\iso A_{T_\Co}$, and let $\theta_\Co\in\Orth(\lkt)$ be the sign involution of @prop:theta-co-exists, whose eigenspaces are $T_\Co$ and $S_\Co$.
Let $\tilde h_\Co\in S_\Co$ be the pullback of the degree-$2$ Coble polarization (@def:numerical-polarization) (@def:coble-polarization-classes), of square $4$, and put
$$
\Gamma^\theta_\Co
\definedas
\theset{\;
\varphi\in\Orth^+(T_\Co)
\;\middle|\;
\exists\, g\in Z_{\Orth(\lkt)}(\theta_\Co)\intersect\Stab_{\Orth(\lkt)}(\tilde h_\Co)
\ \text{with}\ \restrictionof{g}{T_\Co} = \varphi
\;}
,
$$
the part of the image of that intersection that lies in $\Orth^+(T_\Co)$.
Then $\widetilde\Orth^+(T_\Co)\iscontainedin\Gamma^\theta_\Co$, $\widetilde\Orth^+(T_\Co) = \ker\bigl(\Gamma^\theta_\Co\too\Orth(A_{T_\Co},q_{T_\Co})\bigr)$, and $[\Gamma^\theta_\Co : \widetilde\Orth^+(T_\Co)] = \abs{\rho_{T_\Co}(\Gamma^\theta_\Co)}$.
:::

::: {.proof}

By @prop:theta-co-exists an isometry of $\lkt$ commutes (@def:commutative-diagram) with $\theta_\Co$ exactly when it preserves both eigenspaces, and by @thm:automorphism-lifting-criterion a pair $(g_S, g_T)\in\Orth(S_\Co)\times\Orth(T_\Co)$ that preserves both extends over the overlattice $\lkt$ of $S_\Co\oplus T_\Co$ exactly when $\bar g_T\circ\gamma_\Co = \gamma_\Co\circ\bar g_S$.
So $Z_{\Orth(\lkt)}(\theta_\Co)$ is the set of such pairs.

For $\varphi\in\widetilde\Orth^+(T_\Co)$ the pair $(\id_{S_\Co}, \varphi)$ satisfies the condition, since $\bar\varphi = \id$; and $\id_{S_\Co}$ fixes $\tilde h_\Co$.
So $\varphi$ lies in $\Gamma^\theta_\Co$, which is the inclusion.
An element of $\Gamma^\theta_\Co$ is an isometry of $T_\Co$, so its discriminant image is defined without a choice of lift, and the kernel is $\Orth^+(T_\Co)\intersect\ker\rho_{T_\Co} = \widetilde\Orth^+(T_\Co)$; the index is the order of the image.
:::

::: {.lemma #lem:gamma-co-is-tilde-o-plus title="The stable group is $\widetilde\Orth^+(T_\Co)$, definitionally"}

With $\Orth^+(L)\definedas\Theta_\bR(L)$ of @def:lattice-spinor-kernels and $\widetilde\Orth^+(L)$ the pullback (@def:pullback-square) of $\widetilde\Orth(L)=\ker\rho_L$ along the inclusion $\Orth^+(L)\injects\Orth(L)$,
$$
\widetilde\Orth^+(T_\Co)
.$$
:::

::: {.proof}

The left side is $\Orth^+(T_\Co)\intersect\ker\rho_{T_\Co}$ by the definition of $\widetilde\Orth^+(T_\Co)$ above, and the right side is the same intersection by the definition of a pullback along an inclusion: the pullback of $\ker\rho_L$ along $\Orth^+(L)\injects\Orth(L)$ is the set of those $g\in\Orth^+(L)$ whose image lies in $\ker\rho_L$.
:::

::: {.proposition #prop:gamma-co-two-definitions title="The two further descriptions of $\widetilde\Orth^+(T_\Co)$ are decided by their finite images"}

Let $\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma^\theta_\Co$ be the groups of @prop:gamma-co-in-heegner-group and @prop:gamma-co-in-theta-centralizer.
Then:

1. $\Gamma^{\mathrm{Hdg}}_\Co = \widetilde\Orth^+(T_\Co)$ if and only if $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr) = 1$, and $\Gamma^\theta_\Co = \widetilde\Orth^+(T_\Co)$ if and only if $\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr) = 1$;
2. both $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr)$ and $\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr)$ are subgroups of the finite group $\Orth(A_{T_\Co}, q_{T_\Co})$, of order $46\,998\,591\,897\,600$ by @prop:coble-discriminant-group;
3. $\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr)\neq1$ exactly when some $g\in Z_{\Orth(\lkt)}(\theta_\Co)\intersect\Stab_{\Orth(\lkt)}(\tilde h_\Co)$ has $\restrictionof{g}{T_\Co}$ acting nontrivially on $A_{T_\Co}$, whether or not $\restrictionof{g}{T_\Co}$ lies in $\Orth^+(T_\Co)$.
:::

::: {.proof}

(1) is the second claim of each of the two propositions, which identifies $\widetilde\Orth^+(T_\Co)$ with the kernel of the respective finite image, together with the first isomorphism theorem; a kernel is everything exactly when the image is trivial.
(2) an isometry of $T_\Co$ has a discriminant image, so each image is a subgroup of the finite group acting on $A_{T_\Co}$, and the order of that group is the one @prop:coble-discriminant-group computes.
(3) unwinds the definition of $\Gamma^\theta_\Co$ as the set of restrictions of the elements of that intersection, so a nontrivial image is a restriction acting nontrivially on $A_{T_\Co}$, and conversely.
The definition of $\Gamma^\theta_\Co$ also requires $\restrictionof{g}{T_\Co}\in\Orth^+(T_\Co)$, and this can be arranged. Let $w\in T_\Co$ have $w^2 = 2$ — $\zeta$ of the $\generators{2}$ summand, for instance — so that $s_w\in\ker\rho_{T_\Co}$ and $\spinornorm_\bR(s_w) = [-1]$ by @prop:gamma-co-reflective-set(2) and its proof.
The pair $(\id_{S_\Co}, s_w)$ satisfies the compatibility of @thm:automorphism-lifting-criterion because $\bar s_w = \id$, so it extends to an isometry $\hat h$ of $\lkt$ with $\hat h|_{S_\Co} = \id_{S_\Co}$ and $\hat h|_{T_\Co} = s_w$; then $g\hat h$ commutes (@def:commutative-diagram) with $\theta_\Co$, fixes $\tilde h_\Co$, has restriction $\restrictionof{g}{T_\Co}s_w$ with the same discriminant action as $\restrictionof{g}{T_\Co}$, and spinor norm multiplied by $-1$.
So one of $\restrictionof{g}{T_\Co}$ and $\restrictionof{g}{T_\Co}s_w$ is in $\Orth^+(T_\Co)$, and it lies in $\Gamma^\theta_\Co$ with nontrivial image.
:::

::: {.lemma #lem:polarization-stabilizer-discriminant-nontrivial title="The finite image of the polarization stabilizer is not trivial"}

Let $C = U\oplus E_8$ and $S_\En = C(2) = U(2)\oplus E_8(2)$ be the lattices of @def:enriques-lattice, where $E_8$ is negative definite in that definition's convention, and let $h = u_0+w_0$ be the degree-$2$ polarization (@def:numerical-polarization) class of $S_\En$; put $v \definedas u_0-w_0$.
Then the reflection $s_v$ is an isometry of $S_\En$ fixing $h$, and it acts nontrivially on $A_{S_\En}$; consequently the subgroup $\rho_{S_\En}\bigl(\Stab_{\Orth(S_\En)}(h)\bigr)$ whose order bounds the index in @prop:gamma-co-in-heegner-group is not trivial.
:::

::: {.proof}

In $S_\En$ one has $u_0^2 = w_0^2 = 0$ and $b(u_0,w_0) = 2$, so $v^2 = -4$ and $\div_{S_\En}(v) = 2$; the reflection is therefore the integral isometry $s_v(x) = x + \tfrac12 b(x,v)v$ of @def:spinor-norm.
It fixes $h$: $b(h,v) = b(u_0+w_0,\,u_0-w_0) = 0-2+2-0 = 0$, hence $s_v(h) = h$.

For the discriminant, the class of $u_0/2$ lies in $S_\En^*$, because $b_{S_\En} = 2\,b_C$ and $u_0, y\in C$ give $b_{S_\En}(u_0/2, y) = b_C(u_0,y)\in\ZZ$ for every $y\in S_\En$.
Then $b(u_0/2, v) = \tfrac12\bigl(b(u_0,u_0) - b(u_0,w_0)\bigr) = -1$, so
$$
s_v\bigl(\tfrac12 u_0\bigr) = \tfrac12 u_0 - \tfrac12 v = \tfrac12 w_0
,$$
and $\tfrac12 w_0 - \tfrac12 u_0 = \tfrac12(w_0-u_0)$ has coordinates $(-\tfrac12, \tfrac12, 0,\dots,0)$ in the basis $u_0, w_0$ together with a basis of $E_8(2)$, so it is not in $S_\En$.
Hence $\rho_{S_\En}(s_v)\neq\id$ while $s_v(h) = h$, which is the claim.
:::

::: {.proposition #prop:gamma-co-heegner-strict title="The Heegner description is strictly larger, by exactly $\abs{W(E_8)}$"}

The inclusion $\widetilde\Orth^+(T_\Co)\iscontainedin\Gamma^{\mathrm{Hdg}}_\Co$ of @prop:gamma-co-in-heegner-group is strict, and
$$
\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr) \;=\; G_\Co \definedas \rho_{S_\En}\bigl(\Stab_{\Orth(S_\En)}(h)\bigr),
\qquad
[\Gamma^{\mathrm{Hdg}}_\Co:\widetilde\Orth^+(T_\Co)] \;=\; \abs{G_\Co} \;=\; \abs{W(E_8)} \;=\; 696\,729\,600
,$$
the two finite images being identified through the gluing anti-isometry $\gamma$.
:::

::: {.proof}

Let $s_v$ be the reflection of @lem:polarization-stabilizer-discriminant-nontrivial, so $v = u_0-w_0\in S_\En$, $s_v(h) = h$ and $\rho_{S_\En}(s_v)\neq\id$; put $c \definedas \gamma\,\rho_{S_\En}(s_v)\,\gamma^{-1}\in\Orth(q_{\ten})$, which is nontrivial.

*Surjectivity.*
$T_\Co$ is even, indefinite and $2$-elementary, so $\rho_{T_\Co}\colon\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is onto (@thm:two-elementary-surjectivity).
By @prop:coble-discriminant-group every isometry of $q_{T_\Co}$ fixes the class $\zeta/2$ and respects the decomposition $A_{T_\Co} = \ZZ(\zeta/2)\perp A^0$, so the representation (@def:discriminant-rep) factors through $\Orth(q_{T_\Co})\iso\Orth(q_{T_\Co}|_{A^0})$, and $A^0$ is identified with $A_{\ten}$ as in the proof of @prop:gamma-co-in-heegner-group.
Choose $\varphi\in\Orth(T_\Co)$ whose class is the one matching $c$ under that identification.

*Extension.*
$\varphi$ fixes $\zeta/2$, so $\varphi\oplus\id_{\ZZ\delta}$ preserves the gluing subgroup $\generators{(\delta/2,\,\zeta/2)}$ of @lem:coble-heegner-vector and by @cor:liftable-automorphisms extends over the index-two overlattice $\ten$ to an isometry $g$ with $g(\delta) = \delta$ and $\restrictionof{g}{T_\Co} = \varphi$.

*Membership in $\gent$.*
By that extension the class of $g$ in $\Orth(q_{\ten})$ is the class of $\varphi$ on $A^0$, that is $c = \gamma\rho_{S_\En}(s_v)\gamma^{-1}$; so $\bar g_T\circ\gamma = \gamma\circ\bar g_S$ with $g_S = s_v$, and $s_v(h) = h$.
By @prop:gamma-en-two-gluing this is exactly the condition for $g\in\gent$, and $g(\delta) = \delta$, so $g\in\Stab_{\gent}(\ZZ\delta)$ with nontrivial $\rho_{T_\Co}(\restrictionof{g}{T_\Co})$.

*The component condition.*
If $\varphi\notin\Orth^+(T_\Co)$, use the proof of @prop:gamma-co-two-definitions(3): $s_\zeta\in\ker\rho_{T_\Co}$ has $\spinornorm_\bR(s_\zeta) = [-1]$, so $(\id_{S_\En}, s_\zeta)$ glues and extends to an isometry $h'$ of $\ten$ with $h'(\delta) = \delta$, $\restrictionof{h'}{T_\Co} = s_\zeta$ and trivial class; hence $h'\in\gent$ with partner $\id_{S_\En}$, and $gh'\in\Stab_{\gent}(\ZZ\delta)$ has restriction $\varphi s_\zeta\in\Orth^+(T_\Co)$ with the same nontrivial class.

So $\Gamma^{\mathrm{Hdg}}_\Co$ contains an element of $\Orth^+(T_\Co)$ acting nontrivially on $A_{T_\Co}$, which by @prop:gamma-co-two-definitions(1) makes the inclusion strict.

*The other inclusion, hence equality.*
Nothing above used anything about $s_v$ except that it lies in $\Stab_{\Orth(S_\En)}(h)$, so the construction applies to every element of that stabilizer (@def:group-orbit) and gives $\gamma\,G_\Co\,\gamma^{-1}\subseteq\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr)$.
Conversely $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr)\subseteq\gamma\,G_\Co\,\gamma^{-1}$: that is the containment in the proof of @prop:gamma-co-in-heegner-group(2), where the image of $\gent$ in $\Orth(q_{\ten})$ is identified with the $\gamma$-transport of the image of $\Stab_{\Orth(S_\En)}(h)$ (@prop:gamma-en-two-gluing) and $\Gamma^{\mathrm{Hdg}}_\Co$ is the image of $\Stab_{\gent}(\ZZ\delta)\iscontainedin\gent$ under restriction.
So the two images are equal, and by @prop:gamma-co-in-heegner-group(2) the index is their common order.

*The order of $G_\Co$.*
By @prop:polarization-stabilizer-enriques, $\Stab_{\Orth(S_\En)}(h)\iso\Orth(h^{\perp C}) = \Orth\bigl(\generators{-2}\oplus E_8\bigr) = \theset{\pm1}\times W(E_8)$, of order $2\abs{W(E_8)}$; the first factor is the reflection $s_{u_0-w_0}$ in the $\generators{-2}$ direction $u_0-w_0$ of $h^{\perp C}$, and the second is $W(E_8)$ acting on $E_8$.
In the coordinates of $C$ — the module of $S_\En = C(2)$ — an isometry acts on $A_{S_\En} = C/2C$ by its reduction modulo $2$ (@prop:twisted-unimodular-discriminant), each factor acting trivially on the other's summand.
The two factors behave differently there: $s_{u_0-w_0}$ acts nontrivially, since it moves the class of $u_0/2$ (@lem:polarization-stabilizer-discriminant-nontrivial), whereas the element $\id_U\oplus(-\id_{E_8})$, which is the image of $-\id_{E_8} = w_0\in W(E_8)$ and not of $s_{u_0-w_0}$, is trivial modulo $2$.
The $W(E_8)$ factor meets the kernel in $\theset{\pm\id_{E_8}}$, the kernel of the reduction $W(E_8)\to\Orth(E_8/2E_8)$ (@lem:weyl-E8-mod-two).
Hence the kernel of $\Stab_{\Orth(S_\En)}(h)\to\Orth(A_{S_\En})$ is $\theset{1,\ \id_U\oplus(-\id_{E_8})}$, of order $2$, and
$$
\abs{G_\Co} = \frac{2\abs{W(E_8)}}{2} = \abs{W(E_8)} = 696\,729\,600
.$$
:::

## The $\theta$-description: the Coble-side gluing statement {#sec-theta-gluing}

::: {.proposition #prop:theta-co-gluing title="The image of the $\theta$-description is the transported $S_\Co$-stabilizer"}

Let $S_\Co\injects\lkt$ be the primitive embedding of @prop:coble-invariant-lattice with complement $T_\Co$ and gluing anti-isometry $\gamma_\Co\colon A_{S_\Co}\iso A_{T_\Co}$, and let $\Gamma^\theta_\Co$ be the group of @prop:gamma-co-in-theta-centralizer.
Then
$$
\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr)
=
\gamma_\Co\,\rho_{S_\Co}\bigl(\Stab_{\Orth(S_\Co)}(\tilde h_\Co)\bigr)\,\gamma_\Co^{-1}
\qquad\text{in}\qquad \Orth(A_{T_\Co}, q_{T_\Co}),
$$
and consequently
$$
\Gamma^\theta_\Co = \widetilde\Orth^+(T_\Co) \iff \rho_{S_\Co}\bigl(\Stab_{\Orth(S_\Co)}(\tilde h_\Co)\bigr) = 1,
\qquad
[\Gamma^\theta_\Co : \widetilde\Orth^+(T_\Co)] = \abs{\rho_{S_\Co}\bigl(\Stab_{\Orth(S_\Co)}(\tilde h_\Co)\bigr)}.
$$
:::

::: {.proof}

*One inclusion.*
Let $\varphi\in\Gamma^\theta_\Co$, so $\varphi = \restrictionof{g}{T_\Co}$ for some $g\in Z_{\Orth(\lkt)}(\theta_\Co)\intersect\Stab_{\Orth(\lkt)}(\tilde h_\Co)$.
By @prop:theta-co-exists $g$ preserves both eigenspaces, so $g = \psi\oplus\varphi$ with $\psi = \restrictionof{g}{S_\Co}\in\Orth(S_\Co)$; it fixes $\tilde h_\Co\in S_\Co$, so $\psi\in\Stab_{\Orth(S_\Co)}(\tilde h_\Co)$.
By @thm:automorphism-lifting-criterion the pair $(\psi,\varphi)$ glues, that is $\bar\varphi\circ\gamma_\Co = \gamma_\Co\circ\bar\psi$, which is the statement $\rho_{T_\Co}(\varphi) = \gamma_\Co\rho_{S_\Co}(\psi)\gamma_\Co^{-1}$.

*The other inclusion.*
Let $\psi\in\Stab_{\Orth(S_\Co)}(\tilde h_\Co)$ and put $c \definedas \gamma_\Co\bar\psi\gamma_\Co^{-1}\in\Orth(q_{T_\Co})$.
$T_\Co$ is even, indefinite and $2$-elementary, so $\rho_{T_\Co}$ is onto (@thm:two-elementary-surjectivity) and there is $\varphi_0\in\Orth(T_\Co)$ with $\rho_{T_\Co}(\varphi_0) = c$; then the pair $(\psi,\varphi_0)$ satisfies the compatibility of @thm:automorphism-lifting-criterion, so it extends to an isometry $g\in\Orth(\lkt)$ preserving both eigenspaces, that is commuting with $\theta_\Co$ (@prop:theta-co-exists), and fixing $\tilde h_\Co$ because $\psi$ does.
If $\varphi_0\in\Orth^+(T_\Co)$ then $\varphi_0\in\Gamma^\theta_\Co$ and $c$ is its image.
If not, let $\hat h\in\Orth(\lkt)$ be the extension of $(\id_{S_\Co}, s_\zeta)$ given by @prop:gamma-co-two-definitions(3); it also commutes (@def:commutative-diagram) with $\theta_\Co$ and fixes $\tilde h_\Co$, and $g\hat h$ has restriction $\varphi_0 s_\zeta\in\Orth^+(T_\Co)$ with the same discriminant class, because $\rho_{T_\Co}(s_\zeta) = \id$.
So $c\in\rho_{T_\Co}(\Gamma^\theta_\Co)$ either way, and the two images are equal.
The two corollaries are @prop:gamma-co-two-definitions(1) and the first isomorphism theorem.
:::

::: {.lemma #lem:coble-stabilizer-discriminant-nontrivial title="The $\tilde h_\Co$-stabilizer of $S_\Co$ has nontrivial discriminant image"}

Let $C = \Pic(S)\cong\latI_{1,10}$, and let $h_\Co = F_1+F_2\in C$, with $F_i^2 = 0$ and $F_1\cdot F_2 = 1$, be the degree-$2$ numerical polarization (@def:numerical-polarization) of @def:coble-polarization-classes. Write
$$
C \;\iso\; \generators{K}\oplus U\oplus E_8,
\qquad K^2 = -1,
$$
with $K = K_S$, $U = \generators{F_1,F_2}$ the hyperbolic plane (@def:hyperbolic-plane) and $E_8$ the negative-definite lattice of @thm:E8-characterization.
This decomposition holds: $\generators{K_S}$ splits (@def:hyperbolic-plane) $C$ with complement $K_S^\perp$, even and unimodular of signature $(1,9)$ (@prop:canonical-perp-is-e10); $U\iscontainedin K_S^\perp$ because $F_1,F_2\in K_S^\perp$, and $U$ is unimodular, so it splits $K_S^\perp$ (@prop:unimodular-splits); the complement of $U$ in $K_S^\perp$ is even, unimodular and negative definite (@def:definiteness) of rank $8$, hence isometric to $E_8$ (@thm:E8-characterization).
The pullback $f^*$ identifies $C(2)$ with $S_\Co = f^*\Pic(S)$, and $\tilde h_\Co = f^*h_\Co$ has $\tilde h_\Co^2 = 2\cdot2 = 4$.
Put $u\definedas f^*F_1$ and $w\definedas f^*F_2$, so that $u^2 = w^2 = 0$, $u\cdot w = 2$ and $u+w = \tilde h_\Co$, and put $v \definedas u-w = f^*(F_1-F_2)$.
Then $v^2 = -4$, $v$ is primitive, $b(\tilde h_\Co, v) = 0$, and the reflection $s_v$ is an isometry of $S_\Co$ fixing $\tilde h_\Co$ with $\rho_{S_\Co}(s_v)\neq\id$.
Consequently $\rho_{S_\Co}\bigl(\Stab_{\Orth(S_\Co)}(\tilde h_\Co)\bigr)\neq1$.
:::

::: {.proof}

$v^2 = u^2 - 2\,u\cdot w + w^2 = 0-4+0 = -4$, and $b(\tilde h_\Co, v) = u^2 - u\cdot w + w\cdot u - w^2 = 0$, so $s_v(\tilde h_\Co) = \tilde h_\Co$ as soon as $s_v$ is an isometry.

*Primitivity.*
Suppose $v = kx$ with $k\geq2$ and $x$ integral. Then $-4 = v^2 = k^2x^2$, so $k^2\mid 4$ and $x^2 = -4/k^2$; the only integer value left is $k = 2$, giving $x^2 = -1$, and an even lattice has no vector of square $-1$.
So $v$ is primitive.

*Integrality.*
$S_\Co = C(2)$ with $C$ unimodular, so $b_{S_\Co} = 2\,b_C$ and $b_{S_\Co}(v,S_\Co) = 2\ZZ$: every primitive vector of a twist $C(2)$ has divisibility (@def:lattice-divisibility) $2$.
Hence $s_v(x) = x + \tfrac12 b(x,v)v = x + b_C(x,v)v$ is an isometry of $S_\Co$.

*Nontrivial discriminant class (@def:lattice-discriminant-class).*
$C$ is unimodular and $v$ primitive, so the functional $b_C(\cdot,v)$ is unimodular and some $x\in S_\Co$ has $b_C(x,v) = 1$; for that $x$,
$$
s_v(x) - x = v \notin 2S_\Co
,$$
since $v$ is primitive.
Under $A_{S_\Co} = S_\Co/2S_\Co$ — the identification of @prop:twisted-unimodular-discriminant — reduction modulo $2$ is the discriminant action, so $\rho_{S_\Co}(s_v)\neq\id$.
:::

::: {.corollary #cor:theta-co-strict title="The $\theta$-description is strictly larger"}

$\widetilde\Orth^+(T_\Co)\subsetneq\Gamma^\theta_\Co$, with $[\Gamma^\theta_\Co:\widetilde\Orth^+(T_\Co)] = \abs{\rho_{S_\Co}(\Stab_{\Orth(S_\Co)}(\tilde h_\Co))}$, which @prop:theta-co-index evaluates as $\abs{W(E_8)} = 696\,729\,600$.
:::

::: {.proof}

Immediate from @prop:theta-co-gluing and @lem:coble-stabilizer-discriminant-nontrivial: the image there is nontrivial, and it is a subgroup of $\Orth(A_{T_\Co},q_{T_\Co})$ of @prop:coble-discriminant-group.
:::

::: {.proposition #prop:theta-co-index title="The index of the $\theta$-description"}

$[\Gamma^\theta_\Co:\widetilde\Orth^+(T_\Co)] = \abs{W(E_8)} = 696\,729\,600$, the same number as the Heegner index of @prop:gamma-co-heegner-strict.
:::

::: {.proof}

By @prop:theta-co-gluing the index is $\abs{\rho_{S_\Co}(\Stab_{\Orth(S_\Co)}(\tilde h_\Co))}$. Write $C = \generators{K}\oplus U\oplus E_8$ with $K^2 = -1$ and $h = h_\Co = F_1+F_2$, as in @lem:coble-stabilizer-discriminant-nontrivial. Through $f^*\colon C(2)\iso S_\Co$ one has $\Orth(S_\Co) = \Orth(C)$, and the stabilizer (@def:group-orbit) of $\tilde h_\Co = f^*h$ corresponds to the stabilizer of $h$; below, $v = F_1-F_2\in C$.

*The shape of $h^{\perp C}$.*
$h^{\perp C} = \generators{K}\oplus\generators{v}\oplus E_8$ with $K^2 = -1$, $v = F_1-F_2$ of square $-2$ and the $E_8$ form; it is negative definite and has determinant
$$
\det(h^{\perp C}) = \det(C)\cdot\frac{[C:\ZZ h\oplus h^{\perp C}]^2}{\det(\ZZ h)} = 1\cdot\frac{4}{2} = 2,
$$
since $\det(\ZZ h) = 2$ and the index is $2$.
Its root system (@def:root-system-base) — the vectors of square $-2$ — is exactly $\theset{\pm v}$ together with the $240$ roots of $E_8$: a vector $x = aK + bv + e$ has
$$
x^2 = -a^2 - 2b^2 + e^2 = -2,
$$
which solves as $e^2 = a^2 + 2b^2 - 2$; since $e^2 \in 2\ZZ_{\leq0}$ we need $a^2 + 2b^2 \leq 2$, and the cases are $a = 0$, $b = 0$ giving $e^2 = -2$ with $e$ a root of $E_8$; $a = 0$, $b = \pm1$ giving $e = 0$; $a = \pm1$, $b = 0$ giving the odd value $e^2 = -1$; and $a = \pm1$, $b = \pm1$ giving the positive value $e^2 = 1$. The last two do not occur.

*The stabilizer.*
The restriction $\Stab_{\Orth(C)}(h)\to\Orth(h^{\perp C})$ is an isomorphism: an isometry of $h^{\perp C}$ acts trivially on $A_{h^{\perp C}} = \ZZ/2\ZZ$, whose automorphism group is trivial, so the pair $(\id_h,\varphi)$ preserves the glue subgroup of $\ZZ h\oplus h^{\perp C}$ in $C$ and extends by @thm:automorphism-lifting-criterion with $u = \id$.
On $h^{\perp C}$, an isometry permutes roots, and by the count above the roots are the disjoint union of $\theset{\pm v}$ and the root system of $E_8$; the two components have different ranks, so an isometry preserves each, hence preserves $\generators{v}$ and also its orthogonal complement $\generators{K}\oplus E_8$, in which the roots span $E_8$. It therefore preserves $E_8$ and fixes $\generators{K}$, which is the orthogonal complement of $\generators{v}\oplus E_8$.
Hence
$$
\Stab_{\Orth(S_\Co)}(\tilde h_\Co) \;\iso\; \theset{\pm1}_K\times\langle s_v\rangle\times \Orth(E_8), \qquad \abs{\cdot} = 2\cdot2\cdot\abs{W(E_8)} = 4\abs{W(E_8)},
$$
using $\Orth(E_8) = W(E_8)$, since $-\id = w_0$ lies in $W(E_8)$.

*The image.*
By @prop:twisted-unimodular-discriminant, $\rho_{S_\Co}(g) = \id$ exactly for $g\equiv\id\bmod 2$ on $C/2C$.
Of the three factors: $1$ and $s_K$ are trivial there, because $s_K(x) = x + 2b(x,K)K$ when $K^2 = -1$; $-\id_{E_8}$ is trivial because $-1\equiv1\bmod2$; $s_v$ is not, because $s_v(F_1) = F_1 + b(F_1,v)v = F_1 - v = F_2$ and $F_2 - F_1 = -v$ is not in $2C$, $v$ being primitive; and $W(E_8)$ meets the kernel in $\theset{\pm1}$, that being the kernel of $W(E_8)\to\Orth(E_8/2E_8)$ ([@CCN+85], as in @prop:gamma-co-heegner-strict).
So the kernel has order $2\cdot2 = 4$ and
$$
\abs{\rho_{S_\Co}(\Stab_{\Orth(S_\Co)}(\tilde h_\Co))} = \frac{4\abs{W(E_8)}}{4} = \abs{W(E_8)} = 696\,729\,600
.$$
:::

## The congruence comparison {#sec-congruence-comparison}

::: {.definition #def:congruence-group title="The congruence group and block-compatibility" defines="$P$; congruence group; $\Gamma^{\mathrm{cong}}_{\Co,2}$; block-compatible"}

Let
$$
P \definedas \Orth(q_{U(2)})\times\Orth(q_{E_8(2)}) \leq \Orth(A_{T_\Co}, q_{T_\Co}),
$$
made a subgroup of $\Orth(A_{T_\Co},q_{T_\Co})$ by the identity on $\ZZ\tfrac12\zeta$, which every isometry of $q_{T_\Co}$ fixes (@prop:coble-discriminant-group).
The *congruence group* is $\Gamma^{\mathrm{cong}}_{\Co,2}\definedas\rho_{T_\Co}^{-1}(P)\leq\Orth(T_\Co)$.
The gluing $\gamma$ of @prop:gamma-en-two-gluing, respectively $\gamma_\Co$ of @prop:theta-co-exists, is *block-compatible* if it maps the $U(2)$ block $A_{U(2)}$ of its source (@def:globular-boundary) onto the $U(2)$ block $A_{U(2)}$ of $A_{T_\Co}$.
:::

::: {.lemma #lem:coble-discriminant-blocks title="The $U(2)$ block of the Coble discriminant forms"}

Let $A^0 = A_{U(2)}\perp A_{E_8(2)}$, of order $1024$, with the discriminant quadratic form (@def:discquad) $q$ of $U(2)\oplus E_8(2)$ or of its negative.
Let $A$ be either $A^0$ or a nondegenerate (@def:polarization) finite quadratic form $\ZZ k\perp A^0$ with $k$ of order $2$; these are the shapes of $A_{S_\En}$, and of $A_{S_\Co}$ with $k = [K/2]$ and $A_{T_\Co}$ with $k = [\zeta/2]$.
Then:

1. the only $\Orth(q_{E_8(2)})$-invariant subgroups of $A_{E_8(2)}$ are $0$ and $A_{E_8(2)}$, and $A_{U(2)}$ is the only subgroup of $A^0$ of order $4$ invariant under $\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$;
2. the orbits (@def:group-orbit) of $\Orth(q_{A^0})$ on $A^0$ are $\set{0}$, the $527$ nonzero classes with $q = 0$, and the $496$ classes with $q = 1$;
3. if $A = \ZZ k\perp A^0$, every isometry of $q_A$ fixes $k$, restriction to $A^0$ is an isomorphism (@def:isomorphism-of-objects) $\Orth(q_A)\iso\Orth(q_{A^0})$, and the orbits of $\Orth(q_A)$ on $A$ are the orbits of (2) and their translates by $k$, of sizes $1, 1, 527, 527, 496, 496$;
4. $\Stab_{\Orth(q_A)}\bigl(A_{U(2)}\bigr) = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$, and some $g\in\Orth(q_A)$ has $g(A_{U(2)})\neq A_{U(2)}$; so if an anti-isometry $\gamma$ with source (@def:globular-boundary) $A$ is block-compatible (@def:congruence-group), then $\gamma\circ g$ is not;
5. if $A'$ is a second form of the shapes above with the same two summands $A_{U(2)}$, $A_{E_8(2)}$ — as $A_{S_\En}$ and $A_{T_\En}$ are — then there is an anti-isometry $A\too A'$ with $\gamma(A_{U(2)}) = A_{U(2)}$, and one without that property.
:::

::: {.proof}

Write $H = A_{U(2)}$ and $E = A_{E_8(2)} = E_8/2E_8$.
On $A^0$ the form $q$ takes values in $\ZZ/2\ZZ$, so $(A^0,q)$ is a quadratic space over $\mathbb{F}_2$; its bilinear form is nondegenerate because $A^0$ is an orthogonal summand of a nondegenerate discriminant form, so Witt's extension theorem applies to it and to $E$.
On $H$ the three nonzero classes $[e'/2]$, $[f'/2]$ and $[(e'+f')/2]$, for a standard isotropic basis (@def:isotropic-basis-hyperbolic-plane) (@def:based-module) $e',f'$ of $U(2)$ with $e'\cdot f' = 2$, have the values $q = \tfrac14(e')^2 = 0$, $\tfrac14(f')^2 = 0$ and $\tfrac14(e'+f')^2 = 1$; on $E$ the $120$ classes of value $1$ are the images of the $240$ roots of $E_8$, and the other $135$ nonzero classes have value $0$.

(1) Let $W\leq E$ be a nonzero $\Orth(q_E)$-invariant subgroup and $x\in W$ nonzero. By Witt's extension theorem $\Orth(q_E)$ is transitive on the nonzero classes of each value of $q$, so $W$ contains every nonzero class of value $q(x)$. If $q(x) = 1$, these are the images of the roots, which span $E$. If $q(x) = 0$, then $W$ has at least $136 > 128 = \tfrac12\abs{E}$ elements. In both cases $W = E$.
Let $W\leq A^0$ be a subgroup of order $4$ invariant under $\Orth(q_H)\times\Orth(q_E)$. Its projection to $E$ along $H$ is $\Orth(q_E)$-invariant of order at most $4 < 256$, hence $0$. So $W\leq H$, and $W = H$.

(2) For $h\in H$ and $e\in E$ one has $q(h+e) = q(h)+q(e)$. So $3\cdot136+1\cdot120 = 528$ classes of $A^0$ have value $0$, the zero class included, and $3\cdot120+1\cdot136 = 496$ have value $1$. By Witt's extension theorem the nonzero classes of one value form one orbit.

(3) Since $k\perp A^0$ and $b_A$ is nondegenerate, $b(k,k) = \tfrac12$. For $x = \epsilon k+a$ with $a\in A^0$ one has $b(a,a)\equiv q(a)\equiv0\pmod 1$, so $b(x,x) = \tfrac\epsilon2 = b(x,k)$. If $c\in A$ also satisfies $b(x,x) = b(x,c)$ for every $x$, then $c-k$ is orthogonal to $A$, so $c = k$. An isometry preserves $b$, so it fixes $k$ and preserves $k^\perp = A^0$; conversely every isometry of $q_{A^0}$ extends by $k\mapsto k$. The orbits follow from (2), because $q(k+a) = q(k)+q(a)$.

(4) An isometry that preserves $H$ fixes $k$ by (3) when $A = \ZZ k\perp A^0$, so it preserves $A^0$ and hence $H^\perp\intersect A^0 = E$; this gives the stabilizer (@def:group-orbit). The class of value $1$ in $H$ and the image $r\in E$ of a root lie in one orbit by (2) and (3), so some $g$ maps the first to $r\notin H$, and $g(H)\neq H$. If $\gamma(H) = H$, then $\gamma(g(H))\neq\gamma(H) = H$.

(5) The map that is the identity on each of the two summands is an isometry $A\too A'$ carrying $H$ to $H$, and both $q_A$ and $q_{A'}$ take values in $\tfrac12\ZZ/\ZZ$, where $q = -q$; so that map is an anti-isometry, and composing it with the $g$ of (4) gives one that moves the block.
:::

::: {.lemma #lem:overgroups-of-gamma-co title="Overgroups of the stable group in $\Orth^+(T_\Co)$"}

Let $G$ be a group (@def:group) with $\widetilde\Orth^+(T_\Co)\leq G\leq\Orth^+(T_\Co)$. Then
$$
G = \rho_{T_\Co}^{-1}\bigl(\rho_{T_\Co}(G)\bigr)\intersect\Orth^+(T_\Co)
\qquad\text{and}\qquad
[G:\widetilde\Orth^+(T_\Co)] = \abs{\rho_{T_\Co}(G)}.
$$
:::

::: {.proof}

$\widetilde\Orth^+(T_\Co) = \Orth^+(T_\Co)\intersect\ker\rho_{T_\Co}$ (@sec-gamma-co-comparison), so the kernel (@def:kernel-cokernel) of $\rho_{T_\Co}$ on $G$ is $\widetilde\Orth^+(T_\Co)$, which gives the index (@def:index).
The left side is contained in the right side. Let $x$ be in the right side, and choose $y\in G$ with $\rho_{T_\Co}(y) = \rho_{T_\Co}(x)$. Then $y^{-1}x\in\Orth^+(T_\Co)\intersect\ker\rho_{T_\Co} = \widetilde\Orth^+(T_\Co)\leq G$, so $x\in G$.
:::

::: {.proposition #prop:gamma-cong-eq-heegner title="The Heegner description and the congruence description"}

Let $\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma^\theta_\Co$ be the groups of @prop:gamma-co-in-heegner-group and @prop:gamma-co-in-theta-centralizer, and put $P_{S_\En}\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})\leq\Orth(A_{S_\En},q_{S_\En})$ and $P_{S_\Co}\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})\leq\Orth(A_{S_\Co},q_{S_\Co})$.
Then

1. $\abs{\Orth(q_{U(2)})} = 2$ and $\abs{\Orth(q_{E_8(2)})} = \tfrac12\abs{W(E_8)} = 348\,364\,800$, so
   $$
   \abs{P} = 2\cdot 348\,364\,800 = 696\,729\,600 = \abs{W(E_8)}
   ;$$
2. $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr) = \gamma P_{S_\En}\gamma^{-1} = \Stab_{\Orth(q_{T_\Co})}\bigl(\gamma(A_{U(2)})\bigr)$, of order $\abs{W(E_8)}$, and it equals $P$ if and only if $\gamma$ is block-compatible;
3. $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)\bigr) = P$, so $[\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co):\widetilde\Orth^+(T_\Co)] = \abs{W(E_8)}$ and $[\Gamma^{\mathrm{cong}}_{\Co,2}:\widetilde\Orth^+(T_\Co)] = 2\abs{W(E_8)} = 1\,393\,459\,200$; and $\Gamma^{\mathrm{Hdg}}_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ if and only if $\gamma$ is block-compatible;
4. $\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr) = \gamma_\Co P_{S_\Co}\gamma_\Co^{-1} = \Stab_{\Orth(q_{T_\Co})}\bigl(\gamma_\Co(A_{U(2)})\bigr)$, of order $\abs{W(E_8)}$, and $\Gamma^\theta_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ if and only if $\gamma_\Co$ is block-compatible.
:::

::: {.proof}

(1) $q_{U(2)}$ takes the values $0,0,0,1$ on the four classes of $A_{U(2)}$: the three nonzero classes are $[e'/2]$, $[f'/2]$ and $[(e'+f')/2]$, with squares $0$, $0$ and $1$, and every pair of distinct nonzero classes has $b = \tfrac12$ in $\QQ/\ZZ$.
An isometry must therefore fix the class of value $1$ and may or may not swap the other two, and both maps preserve $b$; so $\abs{\Orth(q_{U(2)})} = 2$.
For $A_{E_8(2)} = E_8/2E_8$, the isometry group is $\operatorname{GO}^+_8(2)$, the image of the reduction of $W(E_8)$, of order $\tfrac12\abs{W(E_8)} = 348\,364\,800$ (@lem:weyl-E8-mod-two).
Hence $\abs{P} = 2\cdot 348\,364\,800 = 696\,729\,600 = \abs{W(E_8)}$.

(2) $S_\En = U(2)\oplus E_8(2)$, so $A_{S_\En} = A_{U(2)}\perp A_{E_8(2)}$.
The reflection $s_{u_0-w_0}$ and the eight reflections in simple roots of $E_8(2)$, which by @prop:gamma-co-heegner-strict generate $\Stab_{\Orth(S_\En)}(h)$, preserve that splitting: $s_{u_0-w_0}$ acts on the $U(2)$ summand and fixes $E_8(2)$ pointwise, and the eight root reflections fix $U(2)$ pointwise.
So $\rho_{S_\En}\bigl(\Stab_{\Orth(S_\En)}(h)\bigr)\leq P_{S_\En}$; both have order $\abs{W(E_8)}$, by @prop:gamma-co-heegner-strict and by (1), so they are equal, and by @prop:gamma-co-heegner-strict
$$
\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr) = \gamma\,\rho_{S_\En}\bigl(\Stab_{\Orth(S_\En)}(h)\bigr)\,\gamma^{-1} = \gamma P_{S_\En}\gamma^{-1}.
$$
By @lem:coble-discriminant-blocks(4), $P_{S_\En}$ is the stabilizer (@def:group-orbit) of $A_{U(2)}$ in $\Orth(q_{S_\En})$ and $P$ is the stabilizer of $A_{U(2)}$ in $\Orth(q_{T_\Co})$, so $\gamma P_{S_\En}\gamma^{-1}$ is the stabilizer of $\gamma(A_{U(2)})$.
If $\gamma$ is block-compatible, this is $P$. Conversely, if $\gamma P_{S_\En}\gamma^{-1} = P$, then $\gamma(A_{U(2)})$ is a $P$-invariant subgroup of $A^0$ of order $4$, so it is $A_{U(2)}$ by @lem:coble-discriminant-blocks(1).

(3) $T_\Co$ is even, indefinite and $2$-elementary, so $\rho_{T_\Co}$ is onto (@thm:two-elementary-surjectivity), and $\rho_{T_\Co}(\Gamma^{\mathrm{cong}}_{\Co,2}) = P$.
The reflection $s_\zeta$ has $\zeta^2 = 2$, so $\rho_{T_\Co}(s_\zeta) = \id$ — $s_\zeta(x^*) - x^* = -\beta(x^*,\zeta)\zeta$ with $\beta(x^*,\zeta)\in\ZZ$ — while $\spinornorm_\bR(s_\zeta) = [-1]$ (the component step of @prop:gamma-co-heegner-strict).
$\Orth^+(T_\Co)$ is the kernel of $\spinornorm_\bR$, so for $x\in\Gamma^{\mathrm{cong}}_{\Co,2}$ one of $x$ and $xs_\zeta$ lies in $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$, with the same image under $\rho_{T_\Co}$.
Hence $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)\bigr) = P$, and the first index is $\abs{P}$ by @lem:overgroups-of-gamma-co. The same element gives $[\ker\rho_{T_\Co}:\widetilde\Orth^+(T_\Co)] = 2$, so
$$
\bigl[\Gamma^{\mathrm{cong}}_{\Co,2}:\widetilde\Orth^+(T_\Co)\bigr] = 2\abs{P} = 1\,393\,459\,200
.$$
$\Gamma^{\mathrm{Hdg}}_\Co$ lies in $\Orth^+(T_\Co)$ and contains $\widetilde\Orth^+(T_\Co)$ (@prop:gamma-co-in-heegner-group). By @lem:overgroups-of-gamma-co, $\Gamma^{\mathrm{Hdg}}_\Co = \rho_{T_\Co}^{-1}\bigl(\rho_{T_\Co}(\Gamma^{\mathrm{Hdg}}_\Co)\bigr)\intersect\Orth^+(T_\Co)$, while $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co) = \rho_{T_\Co}^{-1}(P)\intersect\Orth^+(T_\Co)$ has image $P$. So the two groups are equal if and only if $\rho_{T_\Co}(\Gamma^{\mathrm{Hdg}}_\Co) = P$, that is, by (2), if and only if $\gamma$ is block-compatible.

(4) The first equality is @prop:theta-co-gluing. That $\rho_{S_\Co}(\Stab_{\Orth(S_\Co)}(\tilde h_\Co)) = P_{S_\Co}$ is the computation of @prop:theta-co-index: the stabilizer is $\theset{\pm1}_K\times\langle s_v\rangle\times\Orth(E_8)$, its factors act in $K$, in $U$ and in $E_8$ respectively, its image preserves the three blocks of $A_{S_\Co} = C/2C$ and has order $\abs{W(E_8)} = \abs{P_{S_\Co}}$ by (1), so it is $P_{S_\Co}$.
The anti-isometry $\gamma_\Co$ maps $[K/2]$ to $[\zeta/2]$, because these are the classes characterized in @lem:coble-discriminant-blocks(3), so it maps the summand $A^0$ of $A_{S_\Co}$ onto that of $A_{T_\Co}$.
By @lem:coble-discriminant-blocks(4), $\gamma_\Co P_{S_\Co}\gamma_\Co^{-1}$ is the stabilizer of $\gamma_\Co(A_{U(2)})$, and it is $P$ if and only if $\gamma_\Co$ is block-compatible, by the argument of (2).
$\Gamma^\theta_\Co$ lies in $\Orth^+(T_\Co)$ and contains $\widetilde\Orth^+(T_\Co)$ (@prop:gamma-co-in-theta-centralizer), so by @lem:overgroups-of-gamma-co and (3), $\Gamma^\theta_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ if and only if $\rho_{T_\Co}(\Gamma^\theta_\Co) = P$.
:::

::: {.remark title="The block condition is satisfiable and not automatic, computed"}

By @lem:coble-discriminant-blocks(5) a block-compatible anti-isometry $A_{S_\En}\too A_{T_\En}$ exists, and by (4) one that moves the block exists as well; so the hypothesis of @prop:gamma-cong-eq-heegner(2) is a condition on the chosen gluing, neither vacuous nor automatic.
Both are on record at the owner, on $A_{S_\En}$ of order $1024$: `computations/reports/coble_a20-enriques-gluing-block.py`, transcript `-run.txt`, finds the three orbits of $\Orth(q_{S_\En})$ on its classes, of sizes $1$, $496$ and $527$, meeting the $U(2)$ block in $1$, $1$ and $2$ classes, with the witness pair $[0]+[1]$ inside and $[2]+[4]+[7]+[9]$ outside, both in the orbit of size $496$ and both of value $1$.
The same record applies the block test to the anti-isometry that the owner's torsion-form isometry constructor returns for $A_{S_\En}\too A_{T_\En}(-1)$: it satisfies $q_{T_\En}\circ\gamma = -q_{S_\En}$ on all $259$ classes of the two blocks and carries the $U(2)$ block to a four-element subgroup contained in neither block, so that map is not block-compatible.
The record decides nothing about the gluing of the marked embedding $S_\En\injects\lkt$, and by the orbit computation it cannot: no property of the pair of forms selects a block-compatible anti-isometry, and which one a marking induces is the labelled-embedding datum of @prob:coble-rigidity.
What the pair of forms cannot supply, the marked embedding does: @prop:coble-enriques-ambient-isometry builds both primitive embeddings with their marked classes, and the gluing anti-isometry of each inclusion, as objects; on those objects the block test is a decision, and @prop:coble-block-compatibility runs it and answers it affirmatively for both gluings.
:::

::: {.proposition #prop:coble-block-compatibility title="Both marked gluings are block-compatible"}

The gluing anti-isometries $\gamma$ of @prop:gamma-en-two-gluing and $\gamma_\Co$ of @prop:theta-co-exists are block-compatible in the sense of @def:congruence-group.
Precisely, in the model of @prop:coble-enriques-ambient-isometry with
$$
S_\En = \Delta(U_2,U_3)\oplus\Delta(E_{8,1},E_{8,2}),\quad S_\Co = S_\En\oplus\ZZ\alpha,
$$
$$
T_\En = U_1\oplus\Delta^-(U_2,U_3)\oplus\Delta^-(E_{8,1},E_{8,2}),\quad T_\Co = \langle\zeta\rangle\oplus\Delta^-(U_2,U_3)\oplus\Delta^-(E_{8,1},E_{8,2}),
$$
where $\zeta = e_0+e_1$ has $\zeta^2 = 2$:

1. each of $\gamma\colon A_{S_\En}\iso A_{T_\En}$ and $\gamma_\Co\colon A_{S_\Co}\iso A_{T_\Co}$ carries the $U(2)$ block of its source (@def:globular-boundary) onto the $U(2)$ block $\Delta^-(U_2,U_3)$ of its target (@def:globular-boundary), and the $E_8(2)$ block onto the $E_8(2)$ block $\Delta^-(E_{8,1},E_{8,2})$ of its target;
2. the restriction to the two blocks is a bijection there: every one of the $1024$ classes of the two blocks has exactly one image, and the eight generators of the $E_8(2)$ block are carried to eight distinct classes of the target block;
3. $\gamma_\Co$ carries the remaining square-$2$ direction $[\alpha/2]$ to $[\zeta/2]$, which is $[\overline{K_S/2}]\mapsto[\bar\zeta/2]$ of @lem:coble-discriminant-blocks(3) under $\alpha = -f^*K_S$.
:::

::: {.proof}

The test is `computations/reports/coble_a21-ambient-extension.py` part 6, transcript `-run.txt`, provider main `1488acf`, Sage 11.0.beta5.

*How a class is read off.* Let $x\in S^*$ represent a class of $A_S$ and $y\in T^*$ a class of $A_T$, with $S,T$ one of the two complementary pairs. By Nikulin's gluing theorem (@thm:nikulin-gluing) the class $\gamma(x)$ is the unique class of $A_T$ represented by a $y$ with $x+y\in\lkt$; in the standard basis of $\lkt$ used by @prop:coble-enriques-ambient-isometry that membership is the integrality of the coordinate vector $x+y$. So the search over the target block — four classes for $U(2)$, $256$ for $E_8(2)$, built as the classes of $u/2$ for $u$ running over the block vectors — is exhaustive, and each answer is a decision rather than a search bound. That each representative $u/2$ is a dual vector (@def:lattice-discriminant-class) is checked by the pairing test $u\cdot S\subseteq 2\ZZ$; the classes are the ones of @lem:coble-discriminant-blocks, the $U(2)$ block being the del Pezzo slot and the $E_8(2)$ block being $\Delta(E_{8,1},E_{8,2})$.

*The Coble side.* The three nonzero classes of the $U(2)$ block of $A_{S_\Co}$ land on the three nonzero classes of the $U(2)$ block of $A_{T_\Co}$; the eight generators of the $E_8(2)$ block land on the classes of the eight target block generators, one each; all $255$ nonzero classes of the block have exactly one image inside it; and $[\alpha/2]$ lands on $[\zeta/2]$. Hence $\gamma_\Co(A_{U(2)}) = A_{U(2)}$ and $\gamma_\Co$ preserves the $E_8(2)$ block, which is block-compatibility and more.

*The Enriques side.* The same three statements hold with $A_{S_\En}$ and $A_{T_\En}$ in place of $A_{S_\Co}$ and $A_{T_\Co}$, so $\gamma(A_{U(2)}) = A_{U(2)}$ as well.
:::

::: {.corollary #cor:gamma-hdg-is-congruence title="The Heegner and $\theta$ descriptions coincide with the congruence one"}

By @prop:coble-block-compatibility the hypotheses of the three equivalences in @prop:gamma-cong-eq-heegner hold, so
$$
\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr) = P = \rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr),
\qquad
\Gamma^{\mathrm{Hdg}}_\Co = \Gamma^\theta_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co).
$$
:::

::: {.proof}

Items (2), (3) and (4) of @prop:gamma-cong-eq-heegner each state the corresponding assertion as an equivalence with block-compatibility of $\gamma$, respectively of $\gamma_\Co$; @prop:coble-block-compatibility supplies both hypotheses, so each conclusion holds.
Nothing else enters: the indices computed there ($\abs{P} = \abs{W(E_8)}$, $[\Gamma^{\mathrm{cong}}_{\Co,2}:\widetilde\Orth^+(T_\Co)] = 2\abs{W(E_8)}$) are unchanged.
:::

::: {.theorem #thm:gamma-co-2-comparison title="The comparison with the Enriques group at the Heegner vector"}

Let $\delta$ and $\zeta$ be the vectors of @lem:coble-heegner-vector, $\gent$ the degree-$2$ Enriques group of @prop:gamma-en-two-gluing, $R_{\gent}$ the image of $\Stab_{\gent}(\ZZ\delta)$ in $\Orth(\delta^{\perp\ten}) = \Orth(T_\Co)$ (@def:gamma-co-groups, @def:gamma-co-en), and $\Gamma^{\mathrm{cong}}_{\Co,2} = \rho_{T_\Co}^{-1}(P)$ the congruence group of @def:congruence-group. Then:

1. $R_{\gent} = \Gamma^{\En}_\Co(\delta) = \Gamma^{\mathrm{cong}}_{\Co,2}$: the Enriques description at $\delta$ and the congruence description give the same subgroup of $\Orth(T_\Co)$. The image of the $\theta$-centralizer $Z_{\Orth(\lkt)}(\theta_\Co)\intersect\Stab_{\Orth(\lkt)}(\tilde h_\Co)$ in $\Orth(T_\Co)$ is the same group again, so the $\theta$-description and the Enriques description differ in nothing but the condition $\varphi\in\Orth^+(T_\Co)$ with which @prop:gamma-co-in-theta-centralizer states the $\theta$ one; with that condition the three descriptions give $\Gamma^{\mathrm{Hdg}}_\Co = \Gamma^\theta_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ (@cor:gamma-hdg-is-congruence).

2. The two descriptions differ by one coset: $[R_{\gent}:\Gamma^\theta_\Co] = 2$, that is $R_{\gent} = \Gamma^\theta_\Co\sqcup s_\zeta\Gamma^\theta_\Co$, and the nontrivial class is that of the reflection $s_\zeta$, whose $\zeta^2 = 2$ gives it trivial discriminant action and spinor norm $-1$ (@prop:gamma-cong-eq-heegner(3), @prop:gamma-co-reflective-set(2)). So the $\theta$-description of @prop:gamma-co-in-theta-centralizer and the Enriques description agree up to that single isometry and no further.

3. The indices are
$$
\widetilde\Orth^+(T_\Co)\subseteq\Gamma^\theta_\Co\subseteq R_{\gent} = \Gamma^{\mathrm{cong}}_{\Co,2},
\qquad
[\Gamma^\theta_\Co:\widetilde\Orth^+(T_\Co)] = \abs{W(E_8)},
\qquad
[R_{\gent}:\widetilde\Orth^+(T_\Co)] = 2\abs{W(E_8)} = 1\,393\,459\,200,
$$
and the index in the whole orthogonal group, which @prop:gamma-co-images(3) states as the index of the subgroup $P$ of $\Orth(q_{T_\Co})$, is
$$
[\Orth(T_\Co):R_{\gent}] = [\Orth(q_{T_\Co}):P] = 67\,456
,
$$
it is the number of decompositions of $A^0 = [\overline{\zeta/2}]^{\perp}$ into a two-dimensional summand isometric to $A_{U(2)}$ and an eight-dimensional one isometric to $A_{E_8(2)}$.

4. Under @conj:gamma-co-stable, $\Gamma_\Co$ of @def:coble-family-unpolarized $= \widetilde\Orth^+(T_\Co)\subseteq R_{\gent}\intersect\Orth^+(T_\Co)$, and then $\fco = \bD(T_\Co)/\Gamma_\Co\to\bD(T_\Co)/(R_{\gent}\intersect\Orth^+(T_\Co))$ is finite of degree (@def:graded-object) $\abs{W(E_8)} = 696\,729\,600$; the inclusion $\widetilde\Orth^+(T_\Co)\subseteq R_{\gent}\intersect\Orth^+(T_\Co)$ and that index hold unconditionally.

5. In the marking of @thm:theta-co-coordinates, $\delta = e_0-e_1$ and $\zeta = e_0+e_1$; the span $\generators{\delta,\zeta}$ has index $2$ in $U_1$, and $\delta^{\perp\ten} = T_\Co$; $s_\zeta$ is the reflection in $e_0+e_1$, an integral isometry of $\lkt$ fixing $S_\Co$ pointwise, hence lying in $Z_{\Orth(\lkt)}(\theta_\Co)\intersect\Stab(\tilde h_\Co)$, and it acts trivially on $A_{T_\Co}$ and on $A_{T_\En}$, so it lies in $\ker\rho_{T_\En}\subseteq\gent$ and fixes the line $\ZZ\delta$.
:::

::: {.proof}

**The congruence group and the vector stabilizer (@def:group-orbit).** @prop:gamma-co-images(3) computes the image of the stabilizer of the *vector* $\delta$, whose elements are the $\varphi\oplus\id$ with $\varphi\oplus\id\in\gent$: it is $\bar\rho^{-1}(P)$, for the stabilizer $P$ of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$, which @lem:coble-discriminant-blocks(4) identifies with $\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$, the $P$ of @def:congruence-group. So $\rho_{T_\Co}^{-1}(P) = \Gamma^{\mathrm{cong}}_{\Co,2}$ is contained in $R_{\gent}$ as @def:gamma-co-en defines it, over the line.

**The line stabilizer adds nothing.** Let $g\in\Stab_{\gent}(\ZZ\delta)$ and $\varphi = g|_{T_\Co}$. The discriminant action of $\varphi$ is the action of $g$ read on $A^0\subset A_{T_\Co}$ through the identification $A^0 = A_{\ten}$ of @thm:normalization — the computation of the proof of @prop:gamma-cong-eq-heegner(2), and nothing in it uses whether $g$ fixes $\delta$ or negates it — and that action lies in $M = \rho_{\ten}(\gent)$, which is $P$ under the identification. So $\bar\rho(\varphi)\in P$, that is $\varphi\in\Gamma^{\mathrm{cong}}_{\Co,2}$, and the two groups coincide.

**The $\theta$-side gives the same group.** Let $g\in Z_{\Orth(\lkt)}(\theta_\Co)\intersect\Stab(\tilde h_\Co)$. By @prop:theta-co-exists $g$ preserves the two eigenspaces $S_\Co$ and $T_\Co$, so it is a pair $(g_S,g_T)$ with $g_T\in\Orth(T_\Co)$, and by @thm:automorphism-lifting-criterion the compatibility of the pair with the gluing is $\bar g_T\gamma_\Co = \gamma_\Co\bar g_S$; hence $\bar g_T\in\gamma_\Co P_{S_\Co}\gamma_\Co^{-1}$. Conversely let $\varphi\in\Orth(T_\Co)$ have $\bar\rho(\varphi)\in P$. Then $\bar\gamma_\Co^{-1}\bar\rho(\varphi)\bar\gamma_\Co$ lies in $P_{S_\Co}$, so by @prop:theta-co-index it is $\bar\varphi_S$ for some $\varphi_S\in\Stab_{\Orth(S_\Co)}(\tilde h_\Co)$; the pair $(\varphi_S,\varphi)$ satisfies the compatibility, and @thm:automorphism-lifting-criterion extends it to an isometry $g$ of $\lkt$ with $g|_{S_\Co} = \varphi_S$ and $g|_{T_\Co} = \varphi$, which commutes (@def:commutative-diagram) with $\theta_\Co$ and fixes $\tilde h_\Co$. So the image is $\{\varphi : \bar\rho(\varphi)\in\gamma_\Co P_{S_\Co}\gamma_\Co^{-1}\}$, and by @prop:coble-block-compatibility with @prop:gamma-cong-eq-heegner(4) that is $\rho_{T_\Co}^{-1}(P)$.

**One coset.** By @prop:gamma-cong-eq-heegner(3), for $x\in\Gamma^{\mathrm{cong}}_{\Co,2}$ one of $x$ and $xs_\zeta$ lies in $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$, and the two have the same image under $\rho_{T_\Co}$; and $s_\zeta$ does not lie in $\Orth^+(T_\Co)$, because a reflection in a vector of square $2$ has spinor norm $-1$ (@prop:gamma-co-reflective-set(2)). So the quotient has two elements, and one of them is the class of $s_\zeta$.

**The indices.** $\widetilde\Orth^+(T_\Co)\subseteq\Gamma^\theta_\Co$ is @prop:gamma-co-in-heegner-group(1); $[\Gamma^\theta_\Co:\widetilde\Orth^+(T_\Co)] = \abs{W(E_8)}$ and $[R_{\gent}:\widetilde\Orth^+(T_\Co)] = 2\abs{W(E_8)}$ are @prop:gamma-cong-eq-heegner(3), and the second is the product of the first with the index $2$ of the previous paragraph. For $[\Orth(T_\Co):R_{\gent}]$: $\rho_{T_\Co}$ is onto (@thm:two-elementary-surjectivity), so the index is $[\Orth(q_{T_\Co}):P]$, and a coset decomposition of $\Orth(q_{T_\Co})$ by the stabilizer of the decomposition matches the decompositions $A^0 = W\perp W^{\perp}$ with $W\cong A_{U(2)}$ and $W^{\perp}\cong A_{E_8(2)}$ (Witt's extension theorem, applied as in the proof of @prop:gamma-cong-eq-heegner(1)). The number of those decompositions is counted in `computations/reports/coble_a13-heegner-comparison-run.txt`: $67\,456$ for the $2^{10}$ elements of $A^0$, and the same file checks it against $\abs{\Orth(q_{T_\Co})}/\abs{P} = 46\,998\,591\,897\,600/696\,729\,600$.

**The quotient map.** For subgroups $\Gamma\subseteq\Gamma'$ of $\Orth(T_\Co)$ of finite index acting properly discontinuously on $\bD(T_\Co)$, the natural map $\bD/\Gamma\to\bD/\Gamma'$ has degree $[\Gamma':\Gamma]$ at a generic point, since a generic $\Gamma'$-orbit is the union of $[\Gamma':\Gamma]$ $\Gamma$-orbits. With $\Gamma = \Gamma_\Co$ and $\Gamma' = R_{\gent}$ the degree is therefore $[R_{\gent}:\Gamma_\Co] = 2\abs{W(E_8)}$ under @conj:gamma-co-stable, and the unconditional part is the inclusion $\widetilde\Orth^+(T_\Co)\subseteq R_{\gent}$ with that index.

**The coordinates.** Everything in part 5 is a computation in the marking of @thm:theta-co-coordinates, recorded in the same transcript: the Gram matrix $\begin{pmatrix}-2&0\\0&2\end{pmatrix}$ of $\delta,\zeta$ and its determinant $-4$, the identity $\delta^{\perp\ten} = T_\Co$, the integrality of $s_\zeta$ and its being an involution preserving the form, its fixing the eleven $S_\Co$-basis vectors and its commutation with $\theta_\Co$, the triviality of its action on $A_{T_\Co}$ and on $A_{T_\En}$ tested against the dual bases of those two discriminant groups, and its fixing $\delta$. Membership in $\gent$ follows from $\bar\rho_{T_\En}(s_\zeta) = 1$ and $\gent = \rho_{T_\En}^{-1}(M)$ (@prop:sterk-group-identification(2)).
:::

::: {.theorem #thm:diagram-roots-coordinates title="The polarization classes and the $(18,0,0)_1$ diagram in the standard basis"}

In the marking of @thm:theta-co-coordinates:

1. The two polarization (@def:numerical-polarization) classes are one vector: $\tilde h_\Co = h_\En = H = e_2+e_3+e_4+e_5$, of square $4$, and $\theta_\Co(H) = -H$ while $I_\Co(H) = H$; $\tilde h_\Co = h_\En$ holds in every marking, both being the class $H$ of @prop:coble-cover-marking and @prop:coble-enriques-ambient-isometry(3).
2. The lattice $\bar T_{\mathrm{dP}} = U\oplus E_8^2 = (18,0,0)_1$ of the $0$-cusp to which the Coble $0$-cusp maps (@lem:cusp_map_dP) has two copies in this marking, $$W = U_2\oplus E_{8,1}\oplus E_{8,2}\quad\text{and}\quad W' = U_3\oplus E_{8,1}\oplus E_{8,2},$$ each spanned by eighteen standard basis vectors, even of rank $18$, determinant $-1$ and signature $(1,17)$, that is $U\oplus E_8^2 = (18,0,0)_1$, the unique even unimodular lattice of that signature; $\theta_\Co$ carries $W$ to $W'$, and $H$ lies in neither.
3. The nineteen roots of the Coxeter diagram of $(18,0,0)_1$ in $W$, in the standard basis, are $$w_1,\dots,w_7 = \alpha_1,\alpha_3,\alpha_4,\alpha_5,\alpha_6,\alpha_7,\alpha_8,\qquad w_8 = \omega_8+e_2,\qquad w_9 = e_3-e_2,\qquad w_{10} = \tilde\omega_8+e_2,$$ $$w_{11},\dots,w_{17} = \tilde\alpha_8,\tilde\alpha_7,\tilde\alpha_6,\tilde\alpha_5,\tilde\alpha_4,\tilde\alpha_3,\tilde\alpha_1,\qquad w_{18} = \alpha_2,\qquad w_{19} = \tilde\alpha_2,$$ where $\alpha_i = e_{5+i}$ are the Bourbaki simple roots of $E_{8,1}$, $\tilde\alpha_i = e_{13+i}$ those of $E_{8,2}$, and $\omega_8$, $\tilde\omega_8$ the fundamental weights (@def:coroot-weight) dual to $\alpha_8$, $\tilde\alpha_8$. Every one has square $-2$, and their Gram matrix is the diagram's: a tree on nineteen nodes all of whose bonds --- in Bourbaki's word for the edges of a Coxeter graph (@def:coxeter-form) [@Bou08, Ch. VI §4] --- are of label $3$, its two $E_8$ branches being the $\alpha$-chains with $\alpha_2$ hanging off $\alpha_4$, joined through the path (@def:path-connectedness) $w_8-w_9-w_{10}$.
4. $I_\Co = -\theta_\Co$ carries these nineteen roots to the nineteen roots of the same diagram in $W'$, node $k$ to node $18-k$ for $k\le 8$, $w_{18}$ to $w'_{19}$ and $w_{19}$ to $w'_{18}$, and fixes $w_9$: an involution of the diagram exchanging its two $E_8$ branches, which is the reflection $J\colon\alpha_k\mapsto\alpha_{20-k}$ of [@AEGS25, Lemma 3.9] read across the two copies. The folded roots (@def:folded-root) $w_k+w_{18-k}$ for $k\le 8$, $w_9$ and $w_{18}+w_{19}$ have norms $(-4^{\times 8},-2,-4)$, the entries of the folded diagram of cusp $2$ in [@AEGS25, Fig. 7].
5. The polarization meets exactly two of the nineteen roots: $H\cdot w = 0$ for the sixteen $E_8$-roots and $H\cdot w_8 = H\cdot w_{10} = 1$, and the same holds for the copy in $W'$; the Heegner vector $\delta = e_0-e_1$ is orthogonal to all nineteen roots of both copies.
:::

::: {.proof}

Every value below is in `computations/reports/coble_a13-diagram-roots-run.txt`.

**The two polarization classes.** $\tilde h_\Co = H$ is @prop:coble-cover-marking, $H = h$ is @prop:coble-enriques-ambient-isometry(3), and $\theta_\Co(H) = -H$ because $H\in S_\Co$ is the $(-1)$-eigenspace of $\theta_\Co$ (@prop:theta-co-exists); $I_\Co = -\theta_\Co$ is $+\id$ there, so $I_\Co(H) = H$. Both classes belong to the tuple $(S_\Co,T_\Co,H)$, which @thm:theta-co-coordinates determines up to $\Orth(\lkt)$, so their equality is a statement about the tuple and not about this marking.

**The two copies.** The spans are direct sums of standard basis blocks, so their invariants are read off: rank $2+8+8 = 18$, Gram with diagonal (@def:polarization-functors) $0,0,-2^{\times 16}$, determinant $-1$, and signature $(1,17)$, which is $(18,0,0)_1$ (@def:gamma-co-groups names the lattice; the invariants $(18,0,0)_1$ determine it, its signature being indefinite). The action of $\theta_\Co$ on the standard basis of @thm:theta-co-coordinates sends $e_2\mapsto-e_4$, $e_3\mapsto-e_5$ and $e_{6+k}\leftrightarrow -e_{14+k}$, so it carries $W$ to $W'$; and $H$ has the component $e_3$ outside $W$ and $e_2$ outside $W'$, so it lies in neither.

**The roots.** The table is the transcription of the root table of @sec-root-vectors-and-folded-sterk-diagrams into this marking: $U_2 = \generators{e_2,e_3}$ with $e = e_2$, $f = e_3$, and the two $E_8$ summands with $\alpha_i = e_{5+i}$, $\tilde\alpha_i = e_{13+i}$. The record checks that all nineteen squares are $-2$, that the off-diagonal entries of the Gram matrix lie in $\{0,1\}$, that they give a connected tree on nineteen nodes with eighteen bonds, that the nineteen roots have rank $18$ and so generate $W$, and that the two eight-node blocks are $-\mathrm{Cartan}(E_8)$ in the orders $\alpha_1,\alpha_3,\alpha_4,\alpha_5,\alpha_6,\alpha_7,\alpha_8,\alpha_2$ and $\tilde\alpha_8,\dots,\tilde\alpha_1,\tilde\alpha_2$.

**The folding (@def:folding-bc).** The record computes $I_\Co(w_k)$ for the nineteen roots and finds the node pairing displayed in part 4, verifies that it is a bijection of order two preserving the Gram matrix, that its only fixed node is $w_9$ and that it exchanges the two $E_8$ branches; that is the reflection of [@AEGS25, Lemma 3.9], whose fixed sublattice is $U\oplus E_8(2)$ and whose folded diagram is the cusp-$2$ diagram of their Fig. 7, and the norms of the folded roots printed in the record, $(-4^{\times8},-2,-4)$, are the entries of that diagram's nodes.

**The pairings.** $H\cdot\alpha_i = H\cdot\tilde\alpha_i = 0$ because $H$ has no component in either $E_8$; $H\cdot(\omega_8+e_2) = H\cdot e_2 = 1$ because $\omega_8$ lies in $E_{8,1}$, which is orthogonal to $H$, and $H\cdot e_2 = 1$; likewise for $\tilde\omega_8+e_2$; and $H\cdot(e_3-e_2) = 1-1 = 0$. The Heegner vector lies in $U_1$, which is orthogonal to $W$ and to $W'$.
:::

::: {.theorem #thm:chain-matrices title="The chain $T_\Co\injects\ten\injects\tdp\injects\lkt$ in the standard basis"}

In the marking of @thm:theta-co-coordinates, write $\Delta^\pm$ for the diagonal (@def:polarization-functors) and antidiagonal copies of a summand of a doubled sum and put
$$
T_\Co = \generators{e_0+e_1}\oplus\Delta^-(U_2,U_3)\oplus\Delta^-(E_{8,1},E_{8,2}),
\qquad
T_\En = U_1\oplus\Delta^-(U_2,U_3)\oplus\Delta^-(E_{8,1},E_{8,2}),
$$
$$
T_{\mathrm{dP}} = U_1\oplus\Delta^-(U_2,U_3)\oplus E_{8,1}\oplus E_{8,2},
\qquad
\lkt = U_1\oplus U_2\oplus U_3\oplus E_{8,1}\oplus E_{8,2}.
$$
Then:

1. $T_\Co = \ker(\theta_\Co-\id)$, the $(+1)$-eigenspace of @thm:theta-co-coordinates; $T_\En = \ker(I_\En+\id)$ and $T_{\mathrm{dP}} = \ker(I_{\mathrm{dP}}+\id)$, while $S_{\mathrm{dP}}\definedas\ker(I_{\mathrm{dP}}-\id)$ is $\Delta(U_2,U_3)\cong U(2)$, with $I_\En$ and $I_{\mathrm{dP}}$ the involutions of [@AEGS25, Def. 2.3].
2. The three inclusions of @lem:sequence_of_embeddings are primitive, and in the bases displayed above they are the block matrices
$$
M_{\Co\En} = \begin{pmatrix}1&0\\ 1&0\\ 0&I_{10}\end{pmatrix},
\qquad
M_{\En\mathrm{dP}} = \begin{pmatrix}I_2&0&0\\ 0&I_2&0\\ 0&0&I_8\\ 0&0&-I_8\end{pmatrix},
\qquad
M_{\mathrm{dP}\lkt} =
\begin{pmatrix}
I_2&0&0&0\\
0&I_2&0&0\\
0&-I_2&0&0\\
0&0&I_8&0\\
0&0&0&I_8
\end{pmatrix},
$$
of shapes $12\times11$, $20\times12$ and $22\times20$. The blocks are those of the summands $(U_1,\ \Delta^-(U_2,U_3),\ E_{8,1},\ E_{8,2})$: in $M_{\Co\En}$ the row blocks have sizes $1,1,10$ and the column blocks $1,10$; in $M_{\En\mathrm{dP}}$ they are $2,2,8,8$ and $2,2,8$; in $M_{\mathrm{dP}\lkt}$ they are $2,2,2,8,8$ and $2,2,8,8$.
3. $M_{\mathrm{dP}\lkt}\,M_{\En\mathrm{dP}}\,M_{\Co\En}$ is the coordinate matrix of $T_\Co$ in the standard basis. The first factor is the map $\eta$ of @lem:primitive_embedding_eta, $h\mapsto\tilde e+\tilde f = e_0+e_1$ and the identity on $E_{10}(2) = \Delta^-(U_2,U_3)\oplus\Delta^-(E_{8,1},E_{8,2})$; and the composite equals the map $(h,x,y)\mapsto(\tilde e+\tilde f,\,x,\,(y,y))$ of @lem:sequence_of_embeddings after the isometry $\sigma$ of $\lkt$ that is the identity on $U_1,U_2,U_3$ and $-\id$ on $E_{8,2}$.
4. The four members have the invariants

| member | rank | determinant | signature | Smith normal form |
|:---|:---|:---|:---|:---|
| $T_\Co$ | $11$ | $-2048$ | $(2,9)$ | $2^{11}$ |
| $T_\En$ | $12$ | $1024$ | $(2,10)$ | $1^2,\,2^{10}$ |
| $T_{\mathrm{dP}}$ | $20$ | $4$ | $(2,18)$ | $1^{18},\,2^{2}$ |
| $\lkt$ | $22$ | $-1$ | $(3,19)$ | $1^{22}$ |

and their types are read off the displays, not classified: $T_\Co\cong\generators{2}\oplus U(2)\oplus E_8(2)$, $T_\En\cong U\oplus U(2)\oplus E_8(2)$, $T_{\mathrm{dP}}\cong U\oplus U(2)\oplus E_8^2$.

5. The Smith normal form of each inclusion matrix is trivial, which is the primitivity the two lemmas invoke, and the cokernels $\ten/T_\Co$, $\tdp/\ten$, $\lkt/\tdp$ have ranks $1$, $8$, $2$.

What this does not give is the equations of the sextic $C$ and of its double plane in these bases; that is @thm:coble-explicit-sextic, which works in the plane model rather than in a lattice basis, no basis of $H^2$ determining an equation.
:::

::: {.proof}

Every value and every entry below is in `computations/reports/coble_a13-chain-matrices-run.txt`.

**The eigenspaces.** $\theta_\Co$ is $-\id$ on $S_\Co$ and $+\id$ on $T_\Co$ (@thm:theta-co-coordinates), and $T_\Co$ as displayed has $\beta = e_0+e_1$ with $\beta^2 = 2$ and the nine antidiagonal vectors, each an eigenvector of $\theta_\Co$ with eigenvalue $+1$; since both spaces have rank $11$, the displayed basis is the eigenspace. $I_\En$ acts on $U_1$ as $-\id$, on $\Delta^\pm(U_2,U_3)$ and $\Delta^\pm(E_8)$ by the sign of the diagonal, hence $\ker(I_\En+\id) = U_1\oplus\Delta^-(U_2,U_3)\oplus\Delta^-(E_{8,1},E_{8,2})$ of rank $12$, which is $T_\En$; and $I_{\mathrm{dP}}$ negates $U_1$, swaps $U_2$ and $U_3$, and negates both $E_8$ summands, so its $(-1)$-eigenspace is $U_1\oplus\Delta^-(U_2,U_3)\oplus E_8^2$ and its $(+1)$-eigenspace is $\Delta(U_2,U_3)$, of ranks $20$ and $2$.

**The containments and the matrices.** Each displayed basis is a set of standard basis vectors or of differences of two, so containments are read off term by term, and in the displayed bases the coordinate matrices are the block matrices of part 2: the first column of $M_{\Co\En}$ is $\beta = e_0+e_1$ in the basis $(e_0,e_1)$ of $U_1$ and the remaining ten columns are the identity, since the two lattices share the $E_{10}(2)$ summand; $M_{\En\mathrm{dP}}$ is the identity on $U_1\oplus\Delta^-(U_2,U_3)$ and sends the antidiagonal vector $e_{6+k}-e_{14+k}$ to $e_{6+k}-e_{14+k}$, that is to minus the $k$-th vector of the $E_{8,2}$ block of $T_{\mathrm{dP}}$; and $M_{\mathrm{dP}\lkt}$ writes each of the twenty basis vectors in the standard basis, the two antidiagonal ones as $e_2-e_4$, $e_3-e_5$.

**The composite.** Multiplying the three block matrices gives the coordinate matrix of $T_\Co$ in the standard basis, which the record checks against the direct construction. The first factor being $\eta$ is immediate from its block form. For the last statement: $\sigma$ is an isometry of $\lkt$ (it negates a whole $E_8$ summand and fixes the rest), it preserves $T_{\mathrm{dP}}$, and it carries the composite's images to $\beta$, to $e_2-e_4$ and $e_3-e_5$, and to $e_{6+k}+e_{14+k}$ for $k = 0,\dots,7$ — that is to $\tilde e+\tilde f = e_0+e_1$, to $x$, and to $(y,y)$.

**Primitivity.** The Smith normal form of each inclusion matrix is trivial (all invariant factors $1$), which says the cokernel is torsion-free; that is the criterion of @lem:primitive_embedding_eta and of the proof of @lem:sequence_of_embeddings, so each step is primitive. The ranks of the cokernels are the rank differences $12-11$, $20-12$, $22-20$.

**The invariants.** The Gram matrices of the four displayed bases are computed in the record; the determinants and signatures are those of the orthogonal sums the displays name, and the decompositions $\generators{2}\oplus U(2)\oplus E_8(2)$, $U\oplus U(2)\oplus E_8(2)$, $U\oplus U(2)\oplus E_8^2$ are the displays themselves, so no classification theorem is used for them. The Smith normal forms are those of the Gram matrices: $2^{11}$ for $T_\Co$, $1^2,2^{10}$ for $T_\En$, $1^{18},2^2$ for $T_{\mathrm{dP}}$, and $1^{22}$ for the unimodular $\lkt$.
:::

::: {.proposition #prop:direct-eq-heegner title="The direct labelled group equals the Heegner one"}

Let $\Gamma^{\mathrm{dir}}_{\Co,2}$ and $\Gamma^{\mathrm{Hdg}}_{\Co,2}$ be the groups of @def:direct-group and @def:hodge-group, the first taken with the centralizer $Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}$ of its four labels, which at a member with $\Pic(\widehat X_b) = S_{\Co,b}$ is the centralizer of @def:direct-group with the chamber in its datum as well, by @thm:chamber-pinned-by-labels.
Then
$$
\Gamma^{\mathrm{dir}}_{\Co,2} = \Gamma^{\mathrm{Hdg}}_{\Co,2} = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co).
$$
:::

::: {.proof}

*The $S$-side of the centralizer.*
Two facts, computed on the objects of @prop:coble-enriques-ambient-isometry in part 7 of `computations/reports/coble_a21-ambient-extension.py`, transcript `-run.txt`, provider main `1488acf`:

1. $\alpha^{\perp}\cap S_\Co = S_\En$: the orthogonal complement of the root line inside $S_\Co$ is the Enriques invariant lattice, checked there as mutual containment of two primitive rank-$10$ sublattices of determinant $2^{10}$ — the content, in coordinates, of the orthogonal decomposition $S_\Co = S_\En\oplus\ZZ\alpha$ of @prop:coble-enriques-ambient-isometry(3);
2. $I_{\mathrm{dP}}$ acts on $S_\Co$ by $+1$ on the slot $\Delta(U_2,U_3)$, by $-1$ on $\Delta(E_{8,1},E_{8,2})$ and by $-1$ on $\ZZ\alpha$, and by $-\id$ on $T_\Co$, checked on the bases of those pieces.

So an isometry of $\lkt$ commuting with $I_\Co$ and $I_{\mathrm{dP}}$ is a pair preserving $S_\Co$ and $T_\Co$ and, inside $S_\Co$, the three pieces; if it fixes $\alpha$ it preserves $\alpha^{\perp}\cap S_\Co = S_\En$, and restriction to $S_\En$ is injective (@def:injective-map) because an isometry acting trivially on $S_\En$ and on $\alpha$ is the identity.
Conversely every $\psi\in\Stab_{\Orth(S_\En)}(h)$ extends by $\id$ on $\ZZ\alpha$, fixes the three pieces, and hence commutes (@def:commutative-diagram) with $I_{\mathrm{dP}}$ and fixes $H = h$ and $\alpha$.
Therefore
$$
\{\,\psi \mid (\psi,\varphi)\in Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}\,\} = \Stab_{\Orth(S_\En)}(h),
$$
whose discriminant image is $P_{S_\En}$ of order $\abs{W(E_8)}$ (@prop:gamma-co-heegner-strict).

*The image in $\Orth(A_{T_\Co})$.*
The glue condition is $\bar\varphi\gamma_\Co = \gamma_\Co\bar\psi$ (@thm:automorphism-lifting-criterion), so
$$
\rho_{T_\Co}\bigl(\Gamma^{\mathrm{dir}}_{\Co,2}\bigr)
= \gamma_\Co P_{S_\En}\gamma_\Co^{-1}
= \Stab_{\Orth(q_{T_\Co})}\bigl(\gamma_\Co(A_{U(2)})\bigr)
= P,
$$
the second equality by @lem:coble-discriminant-blocks(4) and the third by @prop:coble-block-compatibility.

*The kernel and the sign.*
For $\varphi\in\widetilde\Orth^+(T_\Co)$ the pair $(\id_{S_\Co},\varphi)$ acts trivially on both discriminant forms, so it glues; it fixes $H$ and $\alpha$ and commutes with both involutions, since $I_{\mathrm{dP}}$ is $-\id$ on $T_\Co$ by fact 2.
Hence $\widetilde\Orth^+(T_\Co)\subseteq\Gamma^{\mathrm{dir}}_{\Co,2}$, and the same inclusion holds for $\Gamma^{\mathrm{Hdg}}_\Co$ (@prop:gamma-co-in-heegner-group).
An element of $\Orth^+(T_\Co)$ whose discriminant action lies in $P$ therefore differs from one of $\Gamma^{\mathrm{dir}}_{\Co,2}$ by an element of $\widetilde\Orth^+(T_\Co)$, so
$$
\Gamma^{\mathrm{dir}}_{\Co,2} = \rho_{T_\Co}^{-1}(P)\intersect\Orth^+(T_\Co) = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co),
$$
and by @cor:gamma-hdg-is-congruence that is $\Gamma^{\mathrm{Hdg}}_\Co$.

*The chamber.*
@def:direct-group carries the subscript $\mcc$, and nothing above uses it: every step is a statement about the centralizer of the four labels $I_\Co,I_{\mathrm{dP}},H,\alpha$.
The subscript is nevertheless no restriction on that centralizer where the group is defined, since at a one-node member with $\Pic(\widehat X_b) = S_{\Co,b}$ the chamber is a function of $H_b$ and $\alpha_b$ (@thm:chamber-pinned-by-labels): every element of the centralizer preserves it, and
$$Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha,\mcc} = Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}.$$
The equality proved is therefore the one for the group that @def:direct-group defines, with $\mcc$ in its datum, and not for a subscript-free variant of it: the chamber clause of the labelled rigidity theorem is not an input here, the chamber being read off from the other labels; and at a member whose Picard lattice is larger it is no restriction on the part of the centralizer that preserves the member's period either, which preserves the chamber there as well (@lem:chamber-preserved-on-period).
:::

::: {.remark #rmk:root-arrangement-answered title="The root arrangement"}

Every $g\in Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}$ preserves the $(-2)$-root arrangement $\Delta_b$ of the tuple and its chamber, at a member whose Picard lattice is the invariant lattice: there $\Delta_b$ is the set of classes of square $-2$ pairing positively with $H_b$, together with $\alpha_b$, and the chamber is the set of classes of $\mathcal C_b$ positive on all of $\Delta_b$, so both are functions of the two labels (@thm:chamber-pinned-by-labels).

The two grounds on which this was earlier expected to need an effective-Torelli input do not hold, and are recorded here because they are what the question rested on. Effectivity is not an extra input: on a $K3$ exactly one of $\pm\delta$ is effective for a class of square $-2$, and the nef class $H_b$ decides which one. And the centralizer being infinite does not put the question beyond a lattice argument: an element of it acts on $\mathcal C_b$ through its restriction to $S_{\Co,b}$, and the pairs with trivial first component act trivially there.

What the argument does not reach is the member with a larger Picard lattice, where $\Delta_b$ is not a function of the labels and the chamber is cut finer, so that the subscript is a condition on the centralizer (@rmk:chamber-pinned-scope). It is not a condition on the whole of it: every element that preserves the member's period preserves the member's chamber, at every member of the construction and by Torelli, which is @lem:chamber-preserved-on-period. Nor is it an open question on the rest of the centralizer: @thm:chamber-subscript-is-a-condition exhibits an element of the centralizer at a member with a larger Picard lattice that moves the chamber, so the subscript is a genuine condition, and what is left open is only its effect on the group, which @qst:chamber-subscript-image states.
:::

::: {.lemma #lem:chamber-preserved-on-period title="The chamber is preserved by the part of the centralizer that preserves the member's period"}

In the situation of @prop:one-node-family, let $b$ be a member, let $\psi\colon H^2(\widehat X_b,\ZZ)\iso\lkt$ be a marking, and let $g\in Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}$ satisfy $g\psi(\omega_b)\in\CC\psi(\omega_b)$ for a holomorphic $2$-form $\omega_b$ on $\widehat X_b$.
Then $\psi^{-1}g\psi$ preserves the chamber $\mathfrak c_b$ and the arrangement $\Delta_b$ of @def:coble-polarization-classes, part 3.

Consequently the chamber in the datum of @def:direct-group costs nothing on that part of the centralizer at every member of the construction, the members whose Picard lattice is larger than $S_{\Co,b}$ included, where @thm:chamber-pinned-by-labels does not apply.
:::

::: {.proof}

Put $\gamma\definedas\psi^{-1}g\psi$, an isometry of $H^2(\widehat X_b,\ZZ)$; the hypothesis says it carries $\omega_b$ to a multiple of itself, so it is a Hodge isometry.
It fixes $H_b$ and $\alpha_b$ because $g$ fixes $H$ and $\alpha$, hence it fixes $A_b = 2H_b-\alpha_b$, and $A_b$ is ample on every member of the construction (@lem:chamber-from-marked-period).
A Hodge isometry carrying an ample class to an ample class is the pullback of an automorphism: that is the form of the strong Torelli theorem [@BHPV04, Ch. VIII, Thm. 11.1] used in @lem:chamber-from-marked-period, applied here with the two ample classes equal.
So $\gamma = \varphi^*$ for some $\varphi\in\Aut(\widehat X_b)$, and an automorphism preserves the effective classes: $\gamma\Delta_b = \Delta_b$, and $\gamma$ permutes the walls (@not:coxeter-polytope-faces) $\delta^\perp$, $\delta\in\Delta_b$, of $\mathfrak c_b$.
Since $\gamma A_b = A_b$ and $A_b$ is ample, $\mathfrak c_b$ and $\gamma\mathfrak c_b$ are both components of $\mathcal C_b\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp$ containing the ample class $A_b$; components are disjoint, so they are equal.
:::

::: {.theorem #rmk:divisibility-of-the-difference-class title="If the Picard rank is twelve, the known part is the whole Picard lattice"}

In the notation of @lem:known-part-of-the-picard-lattice-at-the-test-member, if $\rho(\widehat X_{b_\star})=12$ then $\Pic(\widehat X_{b_\star})=M$ and $T_{\Co,b_\star}=v^{\perp T_\Co}$.
:::

::: {.proof}
With $\rho=12$ both inclusions of @lem:known-part-of-the-picard-lattice-at-the-test-member, part 4, are of finite index, say $j=[\Pic:M]$ and $k=[v^{\perp T_\Co}:T_{\Co,b_\star}]$. $\Pic$ and $T_{\Co,b_\star}$ are mutual orthogonal complements in the unimodular $\lkt$, so $\abs{\det\Pic}=\abs{\det T_{\Co,b_\star}}$, that is $2^{11}/j^2 = 2^{11}k^2$, and $j=k=1$.
:::

::: {.remark #rmk:dichotomy-not-decided-by-the-root-exclusion title="What is left of A20 2 at this member"}

An earlier version of @lem:known-part-of-the-picard-lattice-at-the-test-member took $u=C_+-C_-$, of square $-8$, to lie in $T_\Co$, on the reading that $\widehat\iota_{\Co,b_\star}$ exchanges the two components of one fibre. It does not: it carries the fibre over $x=1$ to the fibre over $x=-1$ (@thm:direct-period-meets-minus-four, proof). So the dichotomy that was stated for $u$, and the question whether $u^{\perp T_\Co}\subseteq\Pic(\widehat X_{b_\star})$, have no object. The algebraic part of $T_\Co$ that the record fixes is $\ZZ v$, and @rmk:divisibility-of-the-difference-class leaves no second case. The rank count gives only $\rho\ge12$. It does not give $\rho=12$. What remains is the Picard number of this one explicit member. A reduction modulo a prime $p$ of good reduction at which the Frobenius has no eigenvalue $p\zeta$ on the $10$-dimensional complement of $M$ decides it, by point counts of $z^2=f_\star(x,y)$ over $\FF_{p^n}$.

Those counts were run at $p=11,13,17,19,23$, $n\le5$ (`computations/reports/coble_766_a20_picard_number.py`, with `coble_766_a20_counts.gp`; transcript `coble_766_a20_picard_number-run.txt`). They give $\rho\le13$, not $\rho=12$. All four primes are of good reduction (the branch curve is smooth on $\PP^1\times\PP^1$ over $\overline{\FF}_p$ away from an ordinary node at $(0,0)$). The traces of $F^n$ and of $F^n\circ\widehat\iota_{\Co,b_\star}$ on $H^2$ come from the counts of the member and of its twist by $\widehat\iota_{\Co,b_\star}$, the lift $z\mapsto-z$ over $\tau$ being the one whose invariant part has every trace in $p^n\ZZ$, as $S_{\Co,b}$ requires; on the anti-invariant $11$-dimensional part, $v$ is defined over $\QQ$ and contributes the eigenvalue $p$. On the complement $v^\perp$ the normalized characteristic polynomial $Q$ of $F/p$ has degree $10$ and satisfies $Q(t)=\pm t^{10}Q(1/t)$; Newton's identities [@vL07, Lemma 2.4, arXiv v2 p. 4] give its coefficients up to $t^5$.

- At $p=17$ and $p=23$ the coefficient of $t^5$ is nonzero, so the sign is $+1$, and $Q=(t-1)^2(t+1)^2Q_6$: the bound there is $16$.
- At $p=11,13,19$ the coefficient of $t^5$ is $0$. With the sign $+1$, $Q$ has no cyclotomic factor and $\rho\le12$ [@vL07, Prop. 2.2 and Cor. 2.3, arXiv v2 p. 3]. With the sign $-1$, $Q=(t-1)(t+1)Q_8$, the bound is $14$, and by the Artin--Tate formula over $\FF_{p^2}$ the class of $\disc\NS(\widehat X_{b_\star,\overline{\FF}_p})$ in $\QQ^*/\QQ^{*2}$ is that of $R(p)R(-p)$, $R(t)=p^8Q_8(t/p)$, the Brauer group of an elliptic surface having square order: $7$ at $p=11$, $6$ at $p=13$, $870$ at $p=19$.

So $\rho\le13$: if the sign is $+1$ at $11$ or at $19$, $\rho=12$; if it is $-1$ at both, the two bounds are $14$ and the discriminants differ by a non-square, so $\rho\le13$ [@vL07, Remark 2, arXiv v2 p. 6, with Artin--Tate for ordinary reductions in characteristic $p\ge5$ as cited there; $11$ and $19$ are ordinary, the traces $52$ and $110$ of $F$ on $H^2$ being prime to $p$]. What is open is $\rho=12$ against $\rho=13$. No tested prime gives the bound $12$, which is what an odd geometric Picard number forces at every prime. The curves $x=A(y)/B(y)$, $\deg A,\deg B\le2$, whose preimage splits (`computations/reports/coble_766_a20_curve_search.py`) exist over $\FF_{11}$ (one $\tau$-pair) and $\FF_{17}$ (two), and none over $\FF_{13}$; no curve $y=A(x)/B(x)$ of that degree and no $(1,1)$-curve splits over $\FF_{11}$. Of these, only one $\tau$-pair at $17$ lifts to $\ZZ_{17}$ (`coble_766_a20_curve_lift.py`), so it comes from a curve $C$ over $\overline\QQ$; its class $w=C_+-\widehat\iota_{\Co,b_\star}C_+$ has $w^2=-4$ and $w\cdot v=4$ (`coble_766_a20_curve_class.py`), so $w+v$ is anti-invariant, algebraic and of square $0$, hence $0$, the anti-invariant part of $\NS$ being negative definite. So $w=-v$, and this curve adds no class.
:::

::: {.question #qst:chamber-subscript-image title="What the chamber subscript does to the group"}

@lem:chamber-preserved-on-period settles the chamber on the elements of $Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}$ that preserve the member's period, and @thm:chamber-subscript-is-a-condition settles the other direction at a member with a larger Picard lattice: an element that moves no label can move the chamber, so the subscript of @def:direct-group is a genuine condition and the group it defines is the group of a member and not of the labels.

What is left is what that condition does to the group: is
$$\rho_{T_\Co}\bigl(Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha,\mcc}\bigr)\;=\;\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$$
at a member whose Picard lattice is larger than $S_{\Co,b}$, as @prop:direct-eq-heegner proves it at a member whose Picard lattice is $S_{\Co,b}$ itself? By @lem:chamber-condition-is-period-condition the condition is linear: a lift $g$ preserves the chamber exactly when the transported period $g^{-1}\omega_b$ is orthogonal to the span of $\Delta_{b_\star}$. So the question is which cosets of $\ker\rho_{T_\Co}$ in the centralizer contain an element with that property, and it is decided by a lattice computation once the span of $\Delta_{b_\star}$ is known, that is once $\Pic(\widehat X_{b_\star})$ is: @cor:chamber-preserved-by-picard-stabilizer reduces it further to whether the stabilizer of the member's Picard lattice surjects onto $P$, which is the form the computation should take. What the record fixes at $b_\star$ is @lem:known-part-of-the-picard-lattice-at-the-test-member: the branch curve, the two reducible fibres over $x=\pm1$ with their four components, the node's fibre, and the count $\nu(b_\star) = 4$ (@thm:chamber-clause-fails and its proof). It does not fix $\Pic(\widehat X_{b_\star})$, which by @thm:effective-roots-are-the-h-positive-ones determines the whole arrangement; by @rmk:divisibility-of-the-difference-class the part that is fixed, $M$, is the whole of it exactly when $\rho(\widehat X_{b_\star})=12$ (@rmk:dichotomy-not-decided-by-the-root-exclusion); and by @lem:chamber-condition-is-period-condition the classes of $H$-degree greater than one are walls of the chamber too: $2C_+ + C_-$ is one, of square $-2$ and $H$-degree $3$. The witness of @thm:chamber-subscript-is-a-condition is not such a check, being discriminant-trivial and moving no element of $P$; what that theorem decides is that the subscript cuts into the kernel of $\rho_{T_\Co}$, not that it changes the image.
:::

## Integral cusp lifting {#sec-cusp-lifting}

In this section $T_\Co = B(2)$ with $B\cong\latI_{2,9}$ (@prop:tco-as-twist), so that $\Orth(T_\Co) = \Orth(B)$, $T_\Co^\# = \tfrac12T_\Co$ and $A_{T_\Co} = B/2B$; write $\rho = \rho_{T_\Co}$ and $q = q_{T_\Co}$.

::: {.lemma #lem:isotropic-classes-lift title="The classes of primitive isotropic vectors"}

1. For a primitive isotropic $v\in T_\Co$ the class $[v/2]\in A_{T_\Co}$ is nonzero and isotropic, and $\rho(g)[v/2] = [gv/2]$ for $g\in\Orth(T_\Co)$.
2. The classes $[v/2]$ of the primitive isotropic $v\in T_\Co$ are exactly the $527$ nonzero isotropic classes (@def:descent-class) of $A_{T_\Co}$, and these form one $\Orth(q)$-orbit.
:::

::: {.proof}

(1) $q([v/2]) = v^2/4 = 0$, and $[v/2]\neq0$ because a primitive vector of $B$ does not lie in $2B$. The equivariance is the definition of $\rho$.

(2) An isotropic class lies in the subgroup $A^0$ of @prop:coble-discriminant-group: $A_{T_\Co}=\ZZ k\perp A^0$ with $q(k)=\tfrac12$, so a class outside $A^0$ is $k+a$ with $q(k+a)=\tfrac12+q(a)\in\tfrac12+\ZZ/2\ZZ$, never $0$. Also $A^0\cong A_{E_{10}(2)} = A_{U(2)}\perp A_{E_8(2)}$, with $\Orth(q)\iso\Orth(q_{A^0})$ by restriction. So by @lem:coble-discriminant-blocks(2) the nonzero isotropic classes number $527$ and form one $\Orth(q)$-orbit.

*The full discriminant surjectivity.* The representation $\rho_{T_\Co}\colon\Orth(T_\Co)\too\Orth(q_{T_\Co})$ is **onto**. This is Nikulin's theorem for an even indefinite $2$-elementary lattice, applied to $T_\Co=B(2)$: [@Nik80, Theorem 3.6.3] (@thm:two-elementary-surjectivity). It is the surjectivity onto the orthogonal group of the full discriminant group $A_{T_\Co}=B/2B$; the surjectivity for the complement $K(2)$ is a separate instance.

*Every class occurs.* Let $S\definedas\theset{[v/2] : v\in T_\Co\ \text{primitive isotropic}}$. The set $S$ is nonempty: in the diagonal (@def:polarization-functors) model $B=\latI_{2,9}$ the vector $e_0+e_2$ has $e_0^2=1$, $e_2^2=-1$ and primitive coordinates, so it is a primitive isotropic vector (@def:isotropic-subspace) of $B=T_\Co$. By (1) each element of $S$ is a nonzero isotropic class. For $g\in\Orth(T_\Co)$ and $v$ primitive isotropic, $gv$ is primitive isotropic and $[gv/2]=\rho_{T_\Co}(g)[v/2]$ by (1); since $\rho_{T_\Co}$ is onto, $S$ is stable under all of $\Orth(q)$. A nonempty $\Orth(q)$-stable subset of the single orbit (@def:group-orbit) of @lem:coble-discriminant-blocks(2) is that orbit. Therefore $S$ is exactly the $527$ nonzero isotropic classes, and these form one $\Orth(q)$-orbit.
:::

::: {.lemma #lem:cusp-vector-stabilizer-image title="The stabilizer of a primitive isotropic vector"}

Let $v\in T_\Co$ be primitive isotropic and $c = [v/2]$. Then

1. $\rho\bigl(\Stab_{\Orth(B)}(v)\bigr) = \Stab_{\Orth(q)}(c)$;
2. $\Stab_{\Orth(B)}(v)\intersect\ker\rho$ contains an element outside $\Orth^+(B)$.
:::

::: {.proof}

By @lem:odd-unimodular-isotropic-splitting(1), $B = P\perp K$ with $v\in P\cong\latI_{1,1}$ and $K\cong\latI_{1,8}$, and $v^{\perp} = \ZZ v\perp K$, so $v^\perp/v\cong K$. Write $P=\ZZ v\oplus\ZZ w$ with $(v,w)=1$.

*The parabolic decomposition.* Let $P_v=\Stab_{\Orth(B)}(v)$ and $K_{\mathrm{ev}}\definedas\theset{k\in K : k^2\in2\ZZ}$, a sublattice of index $2$ in $K$. For $k\in K_{\mathrm{ev}}$ define, after [@Eic74, eq. (3.2)],
$$
E(v,k)(x)\definedas x-(x,k)v+(x,v)k-\tfrac12(k,k)(x,v)v .
$$
This is the Eichler transvection $t(v,k)$ of [@GHS08, §3.1, equation (4)], written for the integral form of $B$; GHS08 state it for an even lattice, and here the coefficient $\tfrac12(k,k)$ is an integer exactly because $k\in K_{\mathrm{ev}}$. Since $(x,k),(x,v)\in\ZZ$ as well, $E(v,k)$ is integral, and $E(v,k)(v)=v$, so $E(v,k)\in P_v$. Thus $P_v$ contains $\Orth(K)$, acting trivially on $P$, and the transvections $E(v,k)$ for $k\in K_{\mathrm{ev}}$.

*The unipotent radical.* Every $g\in P_v$ acting trivially on $v^\perp/v$ is $E(v,k)$ for a unique $k\in K_{\mathrm{ev}}$. Indeed, $g(v)=v$ and $g(y)=y+\lambda(y)v$ for $y\in K$, with $\lambda$ an additive map $K\to\ZZ$; and $g(w)=w+\alpha v+k$ with $k\in K$ and $\alpha\in\ZZ$, the coefficient of $w$ being $(g(w),v)=(w,v)=1$. Preservation of the form gives $(g(w),g(y))=(w,y)+(k,y)+\lambda(y)$, hence $\lambda(y)=-(y,k)$, and $(g(w),g(w))=k^2+2\alpha$, hence $\alpha=-\tfrac12(k,k)$ and $k\in K_{\mathrm{ev}}$. Then $g=E(v,k)$, and $E(v,k)(w)=w-\tfrac12(k,k)v+k$ shows that $k$ is determined by $g$. By [@GHS08, equation (5)], $E(v,k)E(v,k')=E(v,k+k')$ and $E(v,xv)=\id$, so $k\mapsto E(v,k)$ is an isomorphism from $K_{\mathrm{ev}}$ onto the unipotent radical $U$ of $P_v$. Every $g\in P_v$ differs from the lift $\id_P\oplus\bar g\in\Orth(K)$ of its induced isometry $\bar g\in\Orth(v^\perp/v)$ by an element of $U$, so $P_v=\Orth(K)\,U$ with $\Orth(K)\cap U=1$.

*The image of $U$.* For $y\in K$, $E(v,k)(y)=y-(y,k)v\equiv y\pmod{\ZZ v}$; hence $\rho(E(v,k))$ acts trivially on $c^\perp/c\cong K/2K$ and lies in the kernel $N$ of $\Stab_{\Orth(q)}(c)\to\Orth(c^\perp/c)$. Moreover $E(v,k)\equiv\id\pmod{2B}$ if and only if $k\in2K$: the $K$-component of $E(v,k)(w)-w$ is $k$, and $k\in2K$ makes $(y,k)$ and $\tfrac12(k,k)$ even for every $y\in K$. So $\rho$ induces an isomorphism $K_{\mathrm{ev}}/2K\iso\rho(U)$. The quotient $K_{\mathrm{ev}}/2K$ has order $2^8$: $K/2K$ is $9$-dimensional and $k\mapsto k^2\bmod2$ is a nonzero linear form on it, because $K$ is odd and represents $1$.

*The Levi image.* The inclusion $\Orth(K)\subset P_v$ is the identity on $v^\perp/v=K$, and the composite $\Orth(K)\subset P_v\xrightarrow{\rho}\Orth(q)$ is the discriminant representation of $K(2)$ on $c^\perp/c=K/2K$. The lattice $K(2)$ is even, indefinite and $2$-elementary of rank $9$, so this representation is onto by [@Nik80, Theorem 3.6.3] (@thm:two-elementary-surjectivity). Moreover $q_{K(2)}\iso q|_{c^\perp/c}$: the class of $y\in K$ in $c^\perp/c$ corresponds to $y/2\in A_{K(2)}$, and both forms take there the value $\tfrac12(y,y)_B$, the form of $T_\Co$ being twice that of $B$. Therefore $\rho(P_v)$ maps onto $\Stab_{\Orth(q)}(c)/N$.

*The kernel.* By @lem:isotropic-classes-lift(2) and @prop:coble-discriminant-group, $\abs{\Stab_{\Orth(q)}(c)}=\abs{\Orth(q)}/527$, and $\abs{\Orth(c^\perp/c)}=348\,364\,800$. For the identification, $q_{K(2)}$ takes values in $\ZZ/2\ZZ$ exactly on the hyperplane $H=K_{\mathrm{ev}}/2K$, of dimension $8$, and on $H$ it is an $\F_2$-valued form with nondegenerate polar form: $H^\perp$ is spanned by the characteristic class $n$, with $b(n,h)\equiv h^2\pmod2$ equal to $0$ for $h\in H$, and $n\notin H$. To identify the form on $H$, use that $K$ is odd unimodular of signature $(1,8)$, hence isometric to $\generators{1}\oplus E_8(-1)$ by @thm:indefinite-unimodular-classification: a vector $ae+y$ with $e^2=1$ and $y\in E_8(-1)$ has square $a^2+y^2$, even exactly when $a$ is even, so $K_{\mathrm{ev}}=2\ZZ e\oplus E_8(-1)$ and $2K=2\ZZ e\oplus 2E_8(-1)$, and
$$
H=K_{\mathrm{ev}}/2K\cong E_8(-1)/2E_8(-1),\qquad q_H(y)=\tfrac12 y^2_{E_8(-1)}=-\tfrac12 y^2_{E_8}=\bar q_{E_8}(y)\ \text{in }\ZZ/2\ZZ .
$$
By @lem:even-unimodular-mod-two-form this form is of plus type with $136=2^7+2^3$ zeros, so $\Orth(q|_H)=\operatorname{GO}^+_8(2)$. Restriction $\Orth(q_{K(2)})\to\Orth(q|_H)$ is an isomorphism: an isometry fixing $H$ pointwise is the identity, since $g(n)=n+h$ forces $b(h,H)=0$; and an isometry of $H$ extends by fixing $n$, because $b(n,H)=0$. Hence $\abs{\Orth(c^\perp/c)}=\abs{\operatorname{GO}^+_8(2)}=348\,364\,800$ by @lem:weyl-E8-mod-two, whose order $348\,364\,800$ is the full group construction in `computations/reports/coble_orthogonal_group_orders.g`. Hence
$$
\abs{N} = \frac{\abs{\Stab_{\Orth(q)}(c)}}{\abs{\Orth(c^{\perp}/c)}} = \frac{\abs{\Orth(q)}/527}{\abs{\operatorname{GO}^+_8(2)}} = \frac{89\,181\,388\,800}{348\,364\,800} = 2^8 = \abs{\rho(U)} .
$$
Since $\rho(U)\subseteq N$, this gives $\rho(U)=N$, and $\rho(P_v)=\rho(\Orth(K))\,\rho(U)$ is all of $\Stab_{\Orth(q)}(c)$.

*The exact certificate.* The equality is also certified directly at the base vector $u=e_0+e_2$ of the one $\Orth(T_\Co)$-orbit, without the order count. Every one of the $240$ nonsingular classes $x\in A^0\cap c^\perp$ has an integral norm-$\pm2$ lift $r_x\in u^\perp$ in its parity class, and the reflection $s_{r_x}$ fixes $u$ exactly and reduces to the nonsingular symmetry determined by $x$. The source-hashed Sage certificate `computations/reports/coble_full_discriminant_root_lifts.py` constructs all $240$ roots, verifies each norm, parity and orthogonality to $u$, and computes by Schreier--Sims the permutation group they generate on the $527$ nonzero singular classes. Its executed transcript, `computations/reports/coble_full_discriminant_root_lifts-run.txt`, records the order $89\,181\,388\,800=\abs{\Orth(q)}/527=\abs{\Stab_{\Orth(q)}(c)}$; the ten roots with parity masks $(1919,215,58,359,311,335,591,538,2016,594)$ already generate it, and their exact standard-basis matrices are stored with the order in `computations/reports/coble_singular_integral_representatives.json` (`vector_stabilizer_ten_roots_standard`, `vector_stabilizer_finite_order`). A subgroup of $\Stab_{\Orth(q)}(c)$ of order $\abs{\Stab_{\Orth(q)}(c)}$ is $\Stab_{\Orth(q)}(c)$, so this is an independent exact verification of the same equality at $u$; transitivity of $\Orth(T_\Co)$ on the primitive isotropic vectors (@def:isotropic-subspace) (@lem:I29-plus-line-transitivity) and conjugacy carry it to every $v$.

(2) Let $g = \id_P\oplus(-\id_K)$. It fixes $v$, and it is the identity modulo $2B$, so $g\in\ker\rho$. By @lem:split-isometry-spinor-norm and @lem:minus-identity-spinor-norm, $\spinornorm_\bR(g) = \spinornorm_\bR(-\id_K) = -1$, because the positive index (@def:maximal-positive-definite-subspace) of $K$ is $1$. So $g\notin\Orth^+(B)$.
:::

::: {.theorem #thm:coble-zero-cusp-count title="The $527$ orbits of primitive isotropic lines of $T_\Co$"}

Let $B=\latI_{2,9}$, $T_\Co=B(2)$, $q=q_{T_\Co}$ and $\rho=\rho_{T_\Co}\colon\Orth(T_\Co)\too\Orth(q)$, and put
$$
K \definedas \discriminantkernel{T_\Co}=\ker\rho,
\qquad
\widetilde\Orth^+(T_\Co)\definedas K\intersect\Orth^+(T_\Co),
$$
the discriminant kernel and its real-spinor-positive part (@conv:spinor-positive-subgroup).

1. If $v,v'\in T_\Co$ are primitive isotropic with $[v'/2]=[v/2]$, then $v'=kv$ for some $k\in K$. So $v\mapsto[v/2]$ is a bijection from the $K$-orbits of primitive isotropic vectors (@def:isotropic-subspace) onto the $527$ nonzero isotropic classes of $A_{T_\Co}$, and it is a bijection from the $K$-orbits of primitive isotropic lines onto the same classes.
2. Consequently $K$ has exactly $527$ orbits (@def:group-orbit) of primitive isotropic vectors and exactly $527$ orbits of primitive isotropic lines, one for each nonzero isotropic class of $A_{T_\Co}$, and so does $\widetilde\Orth^+(T_\Co)$. The index is
$$
\abs{\Orth(q)}/\abs{\rho\left(\Stab_{\Orth(B)}(v)\right)} = \frac{46\,998\,591\,897\,600}{89\,181\,388\,800} = 527 .
$$
3. This is the count for these two groups, and a count of $0$-cusps names its group (@def:gamma-co-groups). For $\Gamma=\Orth(T_\Co)$ it is $1$ (@thm:unpolarized-cusps): that is the single $0$-cusp of $F^{\mathrm{un}}_\Co=\bD(T_\Co)/\Orth(T_\Co)$, a statement about $F^{\mathrm{un}}_\Co$ and not about $\fco$. For $\ker\rho\subseteq\Gamma\subseteq\Orth(T_\Co)$ it is the number of $\rho(\Gamma)$-orbits on the $527$ nonzero isotropic classes, which depends on the subgroup. Under @conj:gamma-co-stable, $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$ and $\fco=\bD(T_\Co)/\Gamma_\Co$ has $527$ $0$-cusps, which is the only sense in which $527$ is asserted for $\fco$.
4. Both counts stand in the public computation record of @rmk:coble-zero-cusp-reproduction, sage-extensions#357 closed at `4533f0fdbe`, whose two calls return $527$ representatives each. The count is proved here rather than read off that record, and the eight line-orbit constants are now separately certified on the $T_\Co$ lattice card in lattice-database#7. The two arithmetic-group generator fields are also independently certified on that card: 56 ordinary generators of $\widetilde O(T_\Co)$ and 95 ordinary generators of $\widetilde O^+(T_\Co)$, at lattice-database commit `a784518254`.
:::

::: {.proof}

$B$ is odd unimodular, so $\Orth(B)$ is transitive on its primitive isotropic vectors (@lem:I29-plus-line-transitivity).

*The fibre over a class.* Let $v$ be primitive isotropic and $c\definedas[v/2]$, a nonzero isotropic class (@lem:isotropic-classes-lift(1)). By @lem:cusp-vector-stabilizer-image(1), $\rho\left(\Stab_{\Orth(B)}(v)\right)=\Stab_{\Orth(q)}(c)$. So for $v'$ primitive isotropic with $[v'/2]=c$ and $v'=gv$ one has $\rho(g)\in\Stab_{\Orth(q)}(c)$, that is $\rho(g)=\rho(h)$ for some $h\in\Stab_{\Orth(B)}(v)$, and then $v'=kv$ with $k=gh^{-1}\in\ker\rho$. The fibre over $c$ is therefore a single $K$-orbit.

*The classes that occur.* By @lem:isotropic-classes-lift(2) the classes $[v/2]$ of the primitive isotropic $v$ are exactly the $527$ nonzero isotropic classes of $A_{T_\Co}$. With the previous paragraph, $v\mapsto[v/2]$ is a bijection from the $K$-orbits of primitive isotropic vectors onto them.

*Lines.* $A_{T_\Co}=B/2B$ is $2$-torsion, so $-\id\in K$ and $[-v/2]=[v/2]$ for every $v\in T_\Co$: the map is constant on the two vectors spanning a line, and those two vectors lie in one $K$-orbit, so the orbits of primitive isotropic vectors and of primitive isotropic lines are the same partition and the bijection above is one of line orbits.

*Intermediate groups.* A subgroup $\Gamma$ with $K\subseteq\Gamma$ acts on the primitive isotropic vectors through $\rho(\Gamma)$, and each fibre above is a single orbit of $K\subseteq\Gamma$, so the $\Gamma$-orbits correspond to the $\rho(\Gamma)$-orbits on the classes that occur; this is the reduction of the double cosets through the normal subgroup $K$ to the finite group $\Orth(q)$ [@DH23, Lemma 3.6].

*The two stable groups.* By @prop:discriminant-kernel-orbits(2), $K$ and $\widetilde\Orth^+(T_\Co)=K\intersect\Orth^+(T_\Co)$ have the same orbits on the primitive isotropic vectors and on the primitive isotropic lines, so the count belongs to both. In the index of item 2, $\abs{\Orth(q)}$ is that of @prop:coble-discriminant-group, computed by the full group construction in `computations/reports/coble_orthogonal_group_orders.g`, and $\abs{\rho\left(\Stab_{\Orth(B)}(v)\right)}=\abs{\Orth(q)}/527$ is @lem:cusp-vector-stabilizer-image(1) together with the class count of @lem:isotropic-classes-lift(2), namely $89\,181\,388\,800$.

*The groups of item 3.* The group $\Orth(T_\Co)$ is transitive on the primitive isotropic vectors (@thm:unpolarized-cusps), so its count is $1$; that is the group of $F^{\mathrm{un}}_\Co=\bD(T_\Co)/\Orth(T_\Co)$, the quotient in which the moduli space $\mcm_\Co$ of Coble surfaces sits as an open subset [@DK13, (3.6), Prop. 3.2, p. 513]. The group $\Gamma_\Co$ is the monodromy group of the VHS on the universal family over the moduli stack of Coble surfaces, and on the labelled presentation $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$ (@def:gamma-co-groups(1), @thm:gamma-co-is-stable); the count for $\fco=\bD(T_\Co)/\Gamma_\Co$ is this one once $\Gamma_\Co=\Gamma_\Co(B)$, which is research#797, item 6. The group $R_{\gent} = \bar\rho^{-1}(P)$ is the image of the stabilizer (@def:group-orbit) $\Stab_{\gent}(\delta)$ in $\Orth(T_\Co)$ (@prop:gamma-co-images(3)), and it is neither of the two groups counted here; the monodromy group $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5) lies in $R_{\gent}\intersect\Orth^+(T_\Co)$ (@thm:coble-monodromy-versus-enriques(4)) and is not known to equal it (@qst:coble-monodromy-equality), so the count above says nothing about its orbits either.
:::

::: {.remark #rmk:coble-zero-cusp-count-subgroups title="The $0$-cusp count for $R_{\gent}$ and $\Gamma_{\Co,2}$"}

In @thm:coble-zero-cusp-count(3), for $R_{\gent} = \rho_{T_\Co}^{-1}(P)$ the count is $4$ by @thm:cusp-lifting(1) and @prop:coble-cong-point-stabilizer(1), (2), independently checked by the public row of @rmk:coble-plane-incidence-rows, and the monodromy group $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5) has this count exactly when @qst:coble-monodromy-equality holds, what is unconditional being $\Gamma_{\Co,2}\subseteq R_{\gent}\intersect\Orth^+(T_\Co)$ (@thm:coble-monodromy-versus-enriques(4)).
:::

::: {.corollary #cor:coble-eight-standard-line-counts title="Line, plane and flag orbits for all eight standard orthogonal subgroups"}

Let $T=T_\Co=B(2)$, $O=\Orth(T)$, $K=\ker\rho_T$, and let $O^+=\ker\spinornorm_\bR$, $SO=\ker\det$, and $SO^+=SO\intersect O^+$. Then the numbers of orbits (@def:group-orbit) of primitive isotropic lines, primitive isotropic planes and incident line-plane flags are

| Arithmetic subgroup of $\Orth(T)$ | Line orbits | Plane orbits | Flag orbits | Incidence edges |
| --- | ---: | ---: | ---: | ---: |
| $O$, $SO$, $O^+$, $SO^+$ | $1$ each | $1$ each | $1$ each | $1$ each |
| $K$, $K\intersect SO$, $K\intersect O^+$, $K\intersect SO^+$ | $527$ each | $189\,720$ each | $569\,160$ each | $569\,160$ each |

The line counts also hold for primitive isotropic **vectors**. These are theorem-derived comparison values for the eight standard subgroup operations. The independent lattice-database card `lattices/6JRR.md` now records the eight certified primitive isotropic **line** constants under field certificate `4282656a7d42a5489e900ad120e0f39897cca2d71dabca91e1874feee4fca7b9`, and its two arithmetic-group index certificates are `682c595c52447cd1add71138601fe9259fd3e5e868e05a646a95e0b27c3225f1` and `326145ccf46247778eb506416cb6c6985eedf61029060ff4497597e2c3f8a3b0`. The card still lacks full affected-card verification and a plane or incidence field (lattice-database#7); the public integral kernel-incidence operation, for its part, has since returned both kernel rows (job 44392429173, @rmk:coble-plane-incidence-rows). What the card does carry, read at lattice-database main `d5e96acf`: the eight line constants under `integral.primitive_orbits` (`:21`, block `:69-101`, its own prose at `:3493` saying that the key is the line count), both index certificates (`:22-23`), both integral generator certificates (`:24-25`), and the generators themselves as the card's `morphisms` entries from `:133` on, each an isometry of $T_\Co$ of scale $1$, with the card's prose at `:3502` naming the two proved families — so the certified integral generators this page once recorded as absent are present. A field that no certificate names is not a field that card admits (`tests/test_catalogue_schemas.py:170`, `:195`), so a plane or an incidence value is a computation before it is a card entry. The card also names $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$ at `:3488` while calling that identification a conjecture at `:3501`; only the eight subgroup-specific numerical certificates are cited here, and the family-group identification remains conditional on @conj:gamma-co-stable.

:::

::: {.proof}

Fix a primitive isotropic vector (@def:isotropic-subspace) $v\in B$. By @lem:odd-unimodular-isotropic-splitting(1), there is an integral orthogonal decomposition $B=U\perp M$ with $v\in U$ and $M\cong\latI_{1,8}$. Choose a vector $d$ of square $-1$ in the standard diagonal (@def:polarization-functors) basis of $M$. Its integral reflection $r_d$ fixes $U$ pointwise, so fixes $v$, and satisfies $r_d(x)=x+2(x,d)_B d\equiv x\pmod{2B}$ for every $x\in B$. Thus $r_d\in K\intersect\Stab_O(v)$, with $\det(r_d)=-1$ and normalized real spinor norm $+1$ (the reflection is in a negative vector; see @def:spinor-norm).

The isometry $h=\id_U\oplus(-\id_M)$ also fixes $v$ and belongs to $K$, since it is the identity modulo $2B$. It has $\det(h)=(-1)^9=-1$ and $\spinornorm_\bR(h)=-1$ by @lem:minus-identity-spinor-norm, since $M$ has positive index (@def:maximal-positive-definite-subspace) one. Hence the pairs $(\det,\spinornorm_\bR)$ of $r_d$ and $h$ are $(-1,+1)$ and $(-1,-1)$, which generate $\{\pm1\}^2$. Therefore the stabilizer (@def:group-orbit) of **every** primitive isotropic vector inside $K$ maps onto both determinant and normalized-spinor characters simultaneously: transport these two witnesses by an isometry of $B$, using transitivity from @lem:I29-plus-line-transitivity and normality of $K$.

If $G$ is any of $O,SO,O^+,SO^+$, every $O$-orbit of primitive isotropic vectors is one $G$-orbit: for $g\in O$ sending $v$ to $v'$, multiply $g$ on the right by a suitable element of $\Stab_K(v)$ to make both required characters equal to $+1$, without changing $gv=v'$. Since $O$ is transitive, each of the four groups has one orbit. Likewise, every $K$-orbit is one orbit for each of $K$, $K\intersect SO$, $K\intersect O^+$ and $K\intersect SO^+$, because the same adjustment can be made inside $K$. There are $527$ such $K$-orbits by @thm:coble-zero-cusp-count(1), (2). Finally, the vector-to-line map is a bijection on orbit sets for each of the eight groups: $O$ is transitive on primitive vectors, and for each $v$ the vectors $v$ and $-v$ are already in one $K\intersect SO^+$-orbit by the same character-adjustment argument applied to $-\id_B\in K$. Thus no further identification occurs upon passing to unoriented lines.

For planes and flags, take the standard primitive isotropic plane $P=\generators{e_1,e_2}$ of the Witt decomposition $B=U_1\perp U_2\perp\generators{-1}^{7}$, and the line $\ell=\ZZ e_2\subset P$. Reflection in one of the seven negative norm-one basis vectors of $\generators{-1}^{7}$ fixes $P$ and $\ell$ pointwise, lies in $K$ and has $(\det,\spinornorm_\bR)=(-1,+1)$ by the same reflection formula as above. The isometry $\tau=-\id_{U_1}\oplus\id_{U_2\perp\generators{-1}^{7}}$ preserves $P$, fixes $\ell$ pointwise, lies in $K$ and has $(\det,\spinornorm_\bR)=(+1,-1)$ by @thm:coble-plane-stabilizer-image(5). These two elements generate all four determinant/spinor character pairs inside the stabilizer of the **flag**. By @thm:plane-transitivity-tco and the integral $GL_2(\ZZ)$ Levi action of @thm:coble-plane-stabilizer-image(1), $O$ is transitive on primitive isotropic flags; conjugating the two witnesses gives full character image in every flag stabilizer, hence also every plane stabilizer. The same character-adjustment argument shows that none of the three character restrictions splits an $O$-orbit or a $K$-orbit of planes or flags. The full group therefore has one plane orbit and one flag orbit; the kernel has $189\,720$ plane orbits and $569\,160$ flag orbits by @thm:coble-plane-stabilizer-image(5) and @thm:cusp-lifting(3), respectively. This proves the remaining columns.

For $K$, a line orbit is specified by its nonzero discriminant class $c$, and a plane orbit by its pair $(J,s)$, by @thm:cusp-lifting(1), (2). A flag orbit is specified by $(J,s,c)$ with $0\ne c\in J$, by @thm:cusp-lifting(3). Consequently two distinct $K$-flag orbits have distinct pairs of line and plane orbit endpoints: the forgetful map from flag orbits to incidence edges is injective (@def:injective-map), hence bijective. The three determinant/spinor restrictions of $K$ have exactly the same line, plane and flag orbits, so the same edge count $569\,160$ applies to them. Each full-group character restriction has just one line and one plane orbit and a flag between them, so its incidence relation consists of one edge. This proves the final column. It is a theorem-derived count, and the public kernel-incidence computation has since returned both kernel rows with exactly it (job 44392429173, @rmk:coble-plane-incidence-rows).

More precisely, the incidence graph of each of the four kernel character subgroups is $(1080,3)$-biregular: each of its $527$ line vertices $c$ belongs to $135$ isotropic subgroups $J$ (@cor:coble-zero-one-cusp-incidence), and each $J$ has eight stars (@def:plane-star) (@lem:plane-stars), so $c$ has $135\cdot8=1080$ neighboring plane vertices $(J,s)$. Each of its $189\,720$ plane vertices has exactly the three nonzero elements of $J$ as neighbors. Both degree (@def:graded-object) sums give $527\cdot1080=189\,720\cdot3=569\,160$ edges. This determines the complete finite combinatorial incidence relation from the proved integral orbit fibres. The exact enumeration in `computations/reports/coble_gco_plane-orbits.py` independently checks all $527$ individual line degrees from the $23\,715$ enumerated finite planes, the $189\,720$ decorated-plane count, and both degree sums; its executed result is recorded in `computations/reports/coble_gco_plane-orbits-run.txt`. This finite verification does not by itself return the public operation's integral witnesses; the endpoint row has since returned (job 44392429173, @rmk:coble-plane-incidence-rows), and the per-edge integral transporter clause remains the certificate route's.

:::

::: {.remark #rmk:coble-zero-cusp-reproduction title="The public record behind the two line rows"}

The record is sage-extensions#357, closed at `4533f0fdbe`; its commit body is the run's evidence, and it is a computation record rather than a lattice-database card. Its two calls are `Tco.stable_orthogonal_group().isotropic_orbit_representatives(1)` and `Tco.stable_orthogonal_group().intersection(Tco.O_plus()).isotropic_orbit_representatives(1)`, and they returned $527$ representatives each, in $1934.1$ s and $294.0$ s, every representative a primitive isotropic vector of divisor $2$ with a nonzero divided class.

On the same lattice the record checks the hypotheses that @lem:isotropic-classes-lift and @lem:cusp-vector-stabilizer-image prove, at the representative of the one $\Orth(T_\Co)$-orbit of primitive isotropic vectors: the split-signature witness held ($46.9$ s), the complement's discriminant surjectivity held ($29.3$ s), the divided class of that vector was nonzero, and the two line-stabilizer images returned $([f_2],\text{False})$ and $([f_2],\text{True})$, in $1092.7$ s and $224.2$ s.

The revisions the rows ran at are not in the body of `4533f0fdbe`, which names the port `991b88b0` and no revision: the run report retained at `61394dad3de18255fc1b2488eadc72fc67f9c6b4` --- `results/issue357-tco-kernel-rows.md`, the evidence file whose content that commit moved into its own body --- records that all rows were run on the #357 worktree at `a5fa20dc63` with the port bound at `991b88b0`.

The test is recorded in a separate commit, `1ae9568197894256e7fd45e294c12ecdb7c142f8`, whose body states that the test records both counts and compares each with the page-proof value of `sec-cusp-lifting` in its docstring, its assertions being the recorded computed counts and never the page. `4533f0fdbe` then removed the two `cardinal(527)` assertions, so what the test asserts now is the construction's guarantee for every output --- that each representative is a primitive isotropic line of $T_\Co$, and that the second row has at least as many orbits as the first, the second group being the smaller --- and not the count; subsequently lattice-database#7 certified all eight line-orbit constants on the $T_\Co$ card.
:::

::: {.proposition #prop:coble-planecusp-finite title="The isotropic subgroups of order $4$ of $A_{T_\Co}$"}
Let $B$, $T_\Co = B(2)$, $\rho$, $q$ and $A = A_{T_\Co}$ be as in this section, and let $P\subset B$ be a primitive isotropic plane.

1. Every primitive vector $p\in P$ has $\operatorname{div}_{T_\Co}(p) = 2$ and a nonzero class $[p/2]\in A$. The subgroup $J(P)\definedas\im(P/2)\leq A$ is isotropic of order $4$, its three nonzero elements are the classes of the primitive vectors of $P$, and $\rho(g)(J(P)) = J(g(P))$ for $g\in\Orth(B)$.
2. $\Orth(q)$ acts transitively on the isotropic subgroups of order $4$ of $A$, and each of them is $J(P')$ for a primitive isotropic plane $P'\subset B$.
3. There are $23715 = 527\cdot 270/6$ isotropic subgroups of order $4$ of $A$, and $23715 = 1575+270+9450+3780+8640$ is the sum of the five orbit (@def:group-orbit) sizes of @tbl-finite-plane-orbits.
4. For each such subgroup $J$, $\abs{\Stab_{\Orth(q)}(J)} = 1\,981\,808\,640 = 2^{21}\cdot 3^3\cdot 5\cdot 7$.
:::

::: {.proof}

(1) The pairing $B\to P^*$, $b\mapsto(p\mapsto(p,b))$, is onto because $B$ is unimodular and $P$ is primitive. So $\operatorname{div}_B(p) = 1$ and $\operatorname{div}_{T_\Co}(p) = 2$. Primitivity gives $P\intersect 2B = 2P$, so $P/2P$ injects into $A = B/2B$ and $[p/2]\neq 0$. Thus $J(P)\cong P/2P$ has order $4$, and its nonzero elements are the classes of the primitive vectors of $P$. For $p\in P$, $q([p/2]) = (p,p)_B/2 = 0$, so $J(P)$ is isotropic. The equivariance is the definition of $\rho$.

(2) Let $\bar w_0$ be the characteristic class of $q$, the class with $b(x,x) = b(x,\bar w_0)$ for all $x\in A$. For $x$ in an isotropic subgroup $J$, $b(x,\bar w_0) = b(x,x) \equiv q(x) = 0 \pmod\ZZ$, so $J\iscontainedin\bar w_0^{\perp}$. So the isotropic subgroups of order $4$ are the totally isotropic $2$-planes of the plus-type quadratic space $\bar w_0^{\perp}$, and $2$ is less than its Witt index $5$. So $\Orth(q)$ is transitive on them by Witt's theorem over $\F_2$. The map $\rho$ is onto $\Orth(q)$ (@thm:two-elementary-surjectivity), so every such $J$ is $\rho(g)(J(P)) = J(g(P))$ for some $g\in\Orth(B)$.

(3) For each nonzero isotropic $u\in A$, the isotropic $v\in u^{\perp}\sm\generators{u}$ number $270$: $u^{\perp}/\generators{u}$ is of plus type and dimension $8$ with $135$ nonzero singular vectors, and each of them lifts to the two vectors $au+w$, $a\in\F_2$. There are $527$ nonzero isotropic $u$ (@lem:isotropic-classes-lift(2)), and each subgroup of order $4$ contains $\abs{GL_2(\F_2)} = 6$ ordered pairs $(u,v)$ of distinct nonzero elements. So there are $527\cdot 270/6 = 23715$ subgroups.

(4) By (2) and (3), $\abs{\Stab_{\Orth(q)}(J)} = \abs{\Orth(q)}/23715$. By @lem:isotropic-classes-lift(2) and @lem:cusp-vector-stabilizer-image(1), $\abs{\Orth(q)}/527 = 89\,181\,388\,800$. So $\abs{\Stab_{\Orth(q)}(J)} = 89\,181\,388\,800\cdot 527/23715 = 1\,981\,808\,640$.
:::

::: {.theorem #thm:coble-plane-stabilizer-image title="The integral plane stabilizer and its discriminant image"}
Let $B = U\perp U\perp\generators{-1}^{7}$, with isotropic bases $e_1,f_1$ and $e_2,f_2$ of the two hyperbolic planes and the basis $d_1,\dots,d_7$ of $D = \generators{-1}^{7}$. Let $P = \generators{e_1,e_2}$, so that $D\cong P^{\perp B}/P$, and let $J = \im(P/2)$. Normalize the discriminant forms on $A = A_{T_\Co} = B/2B$ by
$$ b\bigl([x/2],[y/2]\bigr) = \tfrac{(x,y)_B}{2}\ \mathrm{mod}\ \ZZ, \qquad q\bigl([x/2]\bigr) = \tfrac{(x,x)_B}{2}\ \mathrm{mod}\ 2\ZZ , $$
and put $\beta = 2b\bmod 2$, so that $\beta([x/2],[y/2]) = (x,y)_B\bmod 2$. Write $j_i = [e_i/2]$, $\bar d_i = [d_i/2]$ and $\bar w = [w/2]$ for $w\in B$, and let $\bar w_0 = [w_0/2]$ with $w_0 = \sum_i d_i$.

1. (Parabolic factorization.) $\Stab_{\Orth(B)}(P) = L\ltimes U$. Here $L\cong GL_2(\ZZ)\times\Orth(D)$ is the group of the isometries $\gamma\oplus(\gamma^{-1})^{T}\oplus\delta$ of the Witt decomposition $B = P\oplus\generators{f_1,f_2}\oplus D$, in the block order $P$, $P^*\cong\generators{f_1,f_2}$, $D$. The group $U$ is the kernel of the action of $\Stab_{\Orth(B)}(P)$ on $P$ and on $P^{\perp B}/P$.
2. (Discriminant images.) The transposition of the two hyperbolic planes and the shears of $GL_2(\ZZ)$ map onto $GL(J)\cong S_3$. The signed permutations of $D$ map onto the group $S_7$ of the coordinate permutations of the $\bar d_i$. For $w\in D^{\mathrm{ev}}$, the sublattice of the $w\in D$ with $w^2$ even, the Eichler transvection $E_{e_i,w}$ maps to
$$ \bar x\mapsto\bar x + \beta(\bar x,j_i)\bar w + \bigl(\beta(\bar x,\bar w) + \tfrac{w^2}{2}\beta(\bar x,j_i)\bigr)j_i , $$
and $\sigma = E_{e_1,e_2}$ maps to the transvection $\bar x\mapsto\bar x + \beta(\bar x,j_1)j_2 + \beta(\bar x,j_2)j_1$.
3. (The image.) $\abs{\rho\bigl(\Stab_{\Orth(B)}(P)\bigr)} = 30240\cdot 2^{13} = 247\,726\,080 = 2^{18}\cdot 3^3\cdot 5\cdot 7$.
4. (The index.) $\left[\Stab_{\Orth(q)}(J) : \rho(\Stab_{\Orth(B)}(P))\right] = 8 = \left[\Orth^+(6,2) : S_7\right] = \left[S_8 : S_7\right]$.
5. (The orbit (@def:group-orbit) fibres.) Let $\ker\rho\iscontainedin\Gamma\iscontainedin\Orth(B)$, and put $Q = \Orth(q)$, $H = \rho(\Gamma)$, $F = \Stab_Q(J)$ and $S = \rho\bigl(\Stab_{\Orth(B)}(P)\bigr)$. For $k\in Q$, put $\Gamma_{kJ}=\Gamma\intersect\rho^{-1}(\Stab_Q(kJ))$. The $\Gamma_{kJ}$-orbits of the primitive isotropic planes $P'\subset B$ with $J(P') = kJ$ are in bijection with the double cosets
$$ \bigl(k^{-1}Hk\intersect F\bigr)\bigl\backslash F \big/ S . $$
In particular:
   a. for $\Gamma = \ker\rho$ there are $\abs{F/S} = 8$ orbits over each $J'$;
   b. for $\Gamma = \Orth(B)$ there is one orbit;
   c. for $\widetilde\Orth^+(T_\Co) = \Orth^+(B)\intersect\ker\rho$ there are $8$ orbits over each of the $23715$ subgroups of @prop:coble-planecusp-finite, so $8\times 23715 = 189\,720$ orbits of primitive isotropic planes in all.
:::

::: {.proof}

(1) The group $\Stab_{\Orth(B)}(P)$ acts on $P$ and on $P^{\perp B}/P\cong D$, and $U$ is the kernel of the resulting map $\Stab_{\Orth(B)}(P)\to GL(P)\times\Orth(D)$. In the Witt decomposition, $P$ and $D$ are orthogonal, $\generators{f_1,f_2}$ is orthogonal to $D$ and in hyperbolic duality with $P$, and $GL(P)$ acts on $\generators{f_1,f_2}\cong P^*$ by the contragredient action. So each $\gamma\oplus(\gamma^{-1})^{T}\oplus\delta$ is an isometry of $B$ that stabilizes $P$ and induces $(\gamma,\delta)$. These elements form a subgroup $L$ that maps isomorphically onto $GL_2(\ZZ)\times\Orth(D)$. So the map is onto, $L$ splits it, and $\Stab_{\Orth(B)}(P) = L\ltimes U$.

For completeness of the **integral** generating family (@def:generating-frame), let $u\in U$. Since $u$ fixes $P$ and $P^\perp/P$, its action on $f_i$ is $f_i+w_i+p_i$ for $w_i\in D$ and $p_i\in P$. The isotropy of $u(f_i)$ forces $(w_i,w_i)_D$ to be even (the remaining diagonal (@def:polarization-functors) term is twice an integer), so $w_i\in D^{\mathrm{ev}}$. Composing with the inverses of the integral Eichler transvections $E_{e_i,w_i}$ removes both $D$-components. What remains fixes $P$ and $D$ pointwise and maps $f_i\mapsto f_i+\sum_j c_{ji}e_j$; preservation of the bilinear form forces $C=(c_{ji})$ skew-symmetric with zero diagonal. For $\rank P=2$ this is an integral power of the central shear $E_{e_1,e_2}$. Hence $U$ is generated by the two families $E_{e_i,w}$, $w\in D^{\mathrm{ev}}$, and the central shear. The vectors $d_j+d_7$ for $1\leq j\leq6$ together with their conjugates $d_j-d_7$ under the sign reflection of $d_7$ generate $D^{\mathrm{ev}}$: the first six sums and $2d_7$ form an integral basis of determinant $2$. The six adjacent swaps and the seven sign reflections generate $\Orth(D)=(\ZZ/2)^7\rtimes S_7$, while the displayed swap and shear generate $GL_2(\ZZ)$. This proves that the $28$ integral matrices in `computations/reports/coble_complete_plane_parabolic_generators.json` generate the entire $L\ltimes U$. Their Gram preservation, integral plane action, and finite reduction are checked by the independent source-hashed Sage certificate, and the additional seven sign reflections are all trivial modulo $2$.

(2) $GL_2(\ZZ)\to GL_2(\F_2)\cong S_3$ is onto, and $GL(P)$ acts on $J = P/2P$ by its reduction. $\Orth(D)$ is the group of signed permutations of the $d_i$, and the signs act trivially modulo $2$. So $\rho(\Orth(D))\cong S_7$, of order $5040$, inside $\Orth(\generators{-\tfrac12}^{7})$. For $w\in D^{\mathrm{ev}}$, @def:eichler-siegel gives $E_{e_i,w}(x) = x + (e_i,x)w - \bigl((w,x) + \tfrac{w^2}{2}(e_i,x)\bigr)e_i$ with $\tfrac{w^2}{2}\in\ZZ$; its reduction modulo $2B$ is the displayed map. The vector $e_2$ is isotropic and orthogonal to $e_1$, so $E_{e_1,e_2}(x) = x + (e_1,x)e_2 - (e_2,x)e_1$, whose reduction is the displayed transvection. The elements $E_{e_i,w}$ and $\sigma$ fix $P$ and $P^{\perp B}/P$ pointwise, so they lie in $U$.

(3) $U$ fixes $P$ and $P^{\perp B}/P$ pointwise, so $\rho(U)$ fixes $J$ and $J^{\perp}/J$ pointwise and lies in the unipotent radical of $\Stab_{\Orth(q)}(J)$. By (2), the image of $L$ is $S_3\times S_7$, of order $30240$. The unipotent radical has order $2^{13}$. In the Witt block order $J\oplus J^*\oplus V_6$ of the plus-type ten-space $\bar w_0^{\perp}$, which matches $P\oplus P^*\oplus D$, its elements are the block matrices with identity diagonal blocks. Their free parameters are the blocks of linear maps $J\to V_6$, of size $2\times 6$ over $\F_2$, which give $2^{12}$ elements, and the $J$-valued block. A $J$-valued block map
$$ \bar x\mapsto\bar x + a_1\beta_1 j_1 + a_2\beta_1 j_2 + a_3\beta_2 j_1 + a_4\beta_2 j_2, \qquad \beta_i = \beta(\bar x,j_i),\ a_i\in\F_2, $$
preserves $q$ if and only if $a_1\beta_1 + (a_2+a_3)\beta_1\beta_2 + a_4\beta_2 \equiv 0$ identically, because $q(\bar x+\delta) = q(\bar x)+\beta(\bar x,\delta)$ and $q(\delta) = 0$ for $\delta\in J$. This forces $a_1 = a_4 = 0$ and $a_2 = a_3$. So the block has the two elements: the identity and the transvection $\bar x\mapsto\bar x+\beta(\bar x,j_1)j_2+\beta(\bar x,j_2)j_1$. This gives $2^{12}\cdot 2 = 2^{13}$.
The elements of (2) attain each block. The classes $[w/2]$ of $w\in D^{\mathrm{ev}}$ are the even-weight classes, that is all of $V_6$, so the $E_{e_i,w}$ realize all linear maps $\generators{j_i}\to V_6$ for each $i$. The element $\sigma$ realizes the $J$-valued block. Hence $\abs{\rho(\Stab_{\Orth(B)}(P))} = 30240\cdot 2^{13} = 247\,726\,080$.

(4) The space $J^{\perp}/J$ is seven-dimensional over $\F_2$ and spanned by the $\bar d_i$. It has the descended quadratic form, because $J$ is totally isotropic and $b(J,J^{\perp}) = 0$, so $q(x+j) = q(x)$. Since $(w_0,w_0)_B = -7$, $q(\bar w_0) = -\tfrac72 \equiv \tfrac12$ and $b(\bar w_0,\bar w_0) = -\tfrac72 \equiv \tfrac12 \neq 0$. So $\bar w_0$ is not in the radical of $b$, and
$$ V_6 \definedas \bar w_0^{\perp} \cap J^{\perp}/J = \theset{\textstyle\sum c_i \bar d_i : \sum c_i \equiv 0 \pmod 2} $$
is six-dimensional, with $J^{\perp}/J = \generators{\bar w_0} \perp V_6$. On $V_6$ the form is $q(\sum c_i \bar d_i) = -\tfrac{\mathrm{wt}}{2} \bmod 2$, where $\mathrm{wt} = \sum c_i$ is even, so $q$ is $\F_2$-valued on $V_6$. It is nondegenerate of plus type. The classes with $q = 0$ are those of weight $\equiv 0 \pmod 4$, and they number $\binom70 + \binom74 = 36 = 2^5 + 2^2$, the plus-type count $2^{2m-1}+2^{m-1}$ at $m = 3$.
The Levi factor of $\Stab_{\Orth(q)}(J)$ is $S_3\times\Orth^+(6,2)$, and $\Orth^+(6,2)\cong S_8$ acts on $V_6$ and fixes the characteristic class $\bar w_0$. The Levi factor $L$ acts on $P^{\perp B}/P\cong D$ through $\Orth(D)$, the signed permutation group of order $2^7\cdot 7!$, whose image modulo $2$ is the $S_7$ of (2). By (3), $\rho(\Stab_{\Orth(B)}(P))$ contains the unipotent radical of $\Stab_{\Orth(q)}(J)$, and its Levi image is $S_3\times S_7$. So the index is $\left[S_3\times S_8 : S_3\times S_7\right] = \left[S_8 : S_7\right] = 8$, and indeed $1\,981\,808\,640/247\,726\,080 = 8$ by (3) and @prop:coble-planecusp-finite(4).

(5) By @thm:plane-transitivity-tco, every primitive isotropic plane of $B$ is $g(P)$ for some $g\in\Orth(B)$. By @prop:coble-planecusp-finite(1), $J(g(P)) = \rho(g)J$. So the planes $P'$ with $J(P') = J$ form the orbit of $P$ under $\rho^{-1}(F)$, and the $\Gamma$-orbits on it are the double cosets
$$ \bigl(\Gamma\intersect\rho^{-1}(F)\bigr)\bigl\backslash \rho^{-1}(F) \big/ \Stab_{\rho^{-1}(F)}(P) . $$
Since $\ker\rho\iscontainedin\Gamma$, they reduce modulo $\ker\rho$ to $(H\intersect F)\backslash F/S$. For $k\in Q$ with a lift $\tilde k\in\Orth(B)$, the planes $P'$ with $J(P') = kJ$ form the orbit of $\tilde k(P)$ under $\rho^{-1}(kFk^{-1})$. The full group $\Gamma$ need not preserve this fibre; its subgroup $\Gamma_{kJ}$ does. Conjugation by $\tilde k$ identifies the $\Gamma_{kJ}$-orbits in that fibre with the double cosets $(k^{-1}Hk\intersect F)\backslash F/S$. The full $\Gamma$-orbit classification is obtained by taking one $kJ$ from each $H$-orbit on isotropic order-$4$ subgroups and then taking these fibre orbit sets: any element of $\Gamma$ relating two planes over the same $kJ$ necessarily belongs to $\Gamma_{kJ}$.
For $H = 1$ this is $F/S$, of order $8$ by (4). For $H = Q$ there is one double coset over each $J'$, and $Q$ is transitive on the $J'$ (@prop:coble-planecusp-finite(2)), so there is one orbit.
For (c), $\widetilde\Orth^+(T_\Co)\iscontainedin\ker\rho$ has index at most $2$, and a $\ker\rho$-orbit of planes is one $\widetilde\Orth^+(T_\Co)$-orbit if the stabilizer (@def:group-orbit) in $\ker\rho$ of one of its planes contains an element outside $\Orth^+(B)$. Let $\tau = -\id_{U_1}\oplus\id_{U_2\perp D}$. Then $\tau(e_1) = -e_1$ and $\tau(e_2) = e_2$, so $\tau$ stabilizes $P$. It is the identity modulo $2B$, so $\tau\in\ker\rho$. Its normalized real spinor norm (@sec-lattice-spinor-norm) is $\spinornorm_\bR(-\id_{U_1}) = [(-1)^1] = -1$ by @lem:minus-identity-spinor-norm, since $U_1$ has positive index (@def:maximal-positive-definite-subspace) one. For $k\in\Orth(B)$, $k\tau k^{-1}$ lies in $\ker\rho$, stabilizes $k(P)$ and has spinor norm $-1$. So no $\ker\rho$-orbit splits, and (a) together with @prop:coble-planecusp-finite(3) gives $8\times 23715 = 189\,720$ orbits.
:::

::: {.proposition #prop:coble-even-neighbor-kneser title="The canonical even sublattice satisfies Kneser's reflection hypotheses"}

Let $B=I_{2,9}\cong U^{\oplus2}\perp\generators{-1}^{7}$, and put $M=\{x\in B:x^2\in2\ZZ\}$. Then
$$
M\cong U^{\oplus2}\perp D_7(-1),\qquad [B:M]=2,
\qquad A_M\cong\ZZ/4.
$$
Restriction induces an **isomorphism** $\Orth(B)\xrightarrow{\sim}\Orth(M)$. Moreover $M$ satisfies the Kneser hypotheses of [@GHS08, Theorem 1.1]: it is even, has real Witt index (@def:witt-index) $2$, represents $-2$, and has $2$-adic unimodular rank $10$ and $3$-adic unimodular rank $11$. Consequently the subgroup $\Orth'(M)$ of that theorem is generated by products of reflections in norm-$-2$ vectors of $M$.

This supplies a reflection-generation theorem for a canonical even model of the *ambient* integral orthogonal group (@def:group). It does **not** assert that a finite list of those reflections generates the principal level-two kernel (@def:kernel-cokernel) $\Gamma(2)\leq\Orth(B)$, nor that the Kneser subgroup equals $\Gamma(2)$.
:::

::: {.proof}
In the odd (@def:two-elementary-isotropic-types) diagonal (@def:polarization-functors) coordinates, parity of $x^2$ is parity of the sum of its seven negative coordinates: the two $U$ summands are even. Hence $M=U^{\oplus2}\perp D_7(-1)$, where $D_7=\{(x_i)\in\ZZ^7:\sum x_i\equiv0\pmod2\}$; its index (@def:index) in $B$ is $2$. The determinant of $D_7$ is $4$. The class of $\omega=(\tfrac12,\ldots,\tfrac12)$ in $D_7^*/D_7$ has order $4$: $4\omega\in D_7$, while $2\omega=(1,\ldots,1)\notin D_7$ because seven is odd. Thus $A_M\cong\ZZ/4$, and $B$ is exactly the integral overlattice (@def:overlattice) corresponding to its **unique** order-two subgroup $\generators{2\omega+M}$ under the discriminant-bilinear overlattice correspondence. Every isometry of $M$ preserves this subgroup and therefore extends uniquely to an integral isometry of $B$. Conversely $M$ is intrinsic to $B$ as its even-norm sublattice, so every isometry of $B$ restricts to one of $M$. These maps are inverse.

The roots $e_i-e_{i+1}$ ($1\le i\le6$) and $e_6+e_7$ give the standard $D_7$ Gram matrix of determinant $4$; the first six form an $A_6$ Gram minor of determinant $7$, a $2$-adic unit. Thus $D_7$ has a $2$-adically unimodular summand of rank $6$, and its remaining rank-one constituent has determinant valuation $2$. Together with $U^{\oplus2}$ this gives unimodular rank $10$ at $2$. Since $\det M=4$ is a $3$-adic unit, the unimodular rank at $3$ is $11$. The displayed $U^{\oplus2}$ gives real Witt index $2$, and every $D_7$ root has norm (@def:lattice-basic-invariants) $-2$ in $M$. All the hypotheses of [@GHS08, Theorem 1.1] hold, so its stated reflection-generation conclusion applies.
:::

::: {.theorem #thm:coble-ambient-21-generators title="Twenty-one explicit generators of the full integral Coble orthogonal group"}

In the standard integral coordinates $B=U_1\perp U_2\perp\generators{-1}^{7}$, write $U_1=\generators{e,f}$ and $U_2=\generators{e',f'}$. Let $a_1,\ldots,a_9$ be the basis of $U_2\perp D_7(-1)$ consisting of $e',f'$ and the seven simple roots $d_i-d_{i+1}$ ($1\le i\le6$), $d_6+d_7$. Then **the full group $\Orth(B)$ is generated by 21 explicit integral isometries**:

$$
\big\{t(e,a_i),t(f,a_i):1\le i\le9\big\}
\ \cup\ \big\{r_{e'-f'},r_{d_1},-\id_{U_1}\perp\id_{U_2\perp\generators{-1}^{7}}\big\}.
$$

Here $t$ denotes the integral Eichler transvection, and $r_v$ is reflection in $v$. The first 18 generators generate precisely the subgroup $\widetilde{\mathrm{SO}}^+(M)$, where $M=U_1\perp U_2\perp D_7(-1)$ is the canonical even sublattice of $B$. The remaining three have independent images under the discriminant character $\Orth(M)\to\Orth(A_M)\cong\{\pm1\}$, determinant and normalized real spinor norm. In particular the subgroup generated by the first 18 has index exactly $8$ in $\Orth(B)$.

This is a **complete finite generating family (@def:generating-frame) for the ambient infinite arithmetic group (@def:arithmetic-group)**. A distinct, **minimal 56-element ordinary generating family** for the principal congruence subgroup $\Gamma(2)=\ker(\Orth(B)\to\Orth(B/2B))$ is established later in this section. The independent exact Sage regression `test_coble_ambient_twenty_one_integral_generators` constructs all 21 integral matrices, checks their Gram identities and discriminant characters, then constructs their permutations of the 527 nonzero isotropic discriminant classes of $B(2)$. Schreier--Sims gives image order **$46\,998\,591\,897\,600$**, the full $\Orth(q_{T_\Co})$ order. Thus this finite generating family also surjects onto the entire discriminant orthogonal group; the kernel has precisely that index in the proved ambient group. The reproducible `computations/reports/coble_ambient_twenty_one_generators.py` transports the 21 matrices by an explicit integral basis change from $U^{\oplus2}\perp\generators{-1}^7$ into the maintained standard $\generators1\perp U\perp E_8(-1)$ basis. Its source-hashed `coble_ambient_twenty_one_generators.json` contains every exact standard-basis matrix; the separate regression `test_coble_ambient_standard_generator_certificate` verifies all 21 Gram identities in that basis. The public-API regression `test_coble_ambient_generators_are_public_integral_isometry_morphisms` additionally constructs **all 21 as actual morphisms of `NamedLattices.Tco.O()`** and verifies their ownership and group membership; the certificate is therefore directly usable by the maintained arithmetic library, not only by an external matrix computation.
:::

::: {.proof}
By @prop:coble-even-neighbor-kneser, $M$ satisfies Kneser's conditions. The stronger exact result [@GHS08, Proposition 3.4, equation (15)] identifies $\widetilde{\mathrm{SO}}^+(M)=E_{U_1}(U_2\perp D_7(-1))$, generated by $t(e,a)$ and $t(f,a)$ for every $a\in U_2\perp D_7(-1)$. The Eichler composition identity $t(e,a+b)=t(e,a)t(e,b)$ (and similarly for $f$) reduces this to the displayed 18 transvections. Each extends integrally from $M$ to $B$ by the canonical even-sublattice isomorphism, and the displayed formula has integral coefficients directly in $B$.

The discriminant group of $M$ is cyclic of order $4$, so its orthogonal group has at most two elements. The sign change $r_{d_1}$ acts by $-1$ on it: it sends the half-sum class $\omega$ to $\omega-d_1\equiv-\omega\pmod{D_7}$. Both $r_{e'-f'}$ and $-\id_{U_1}$ act trivially on $A_M$. The first two reflections have determinant $-1$ and normalized real spinor norm $+1$, while $-\id_{U_1}$ has determinant $+1$ and normalized real spinor norm $-1$. Thus the three character vectors $(\rho,\det,\spinornorm_\bR)$ are independent. Their images generate the entire target (@def:globular-boundary) $\{\pm1\}^3$, whose kernel is $\widetilde{\mathrm{SO}}^+(M)$ by definition. Hence these 21 matrices generate $\Orth(M)\cong\Orth(B)$, and the asserted index is $8$.
:::

::: {.corollary #cor:coble-level-two-kernel-split-extension title="A split finite-character reduction of the full level-two kernel"}

With $E=\widetilde{\mathrm{SO}}^+(M)$ generated by the 18 Eichler transvections of @thm:coble-ambient-21-generators, let $r=r_{d_1}$ and $h=-\id_{U_1}\perp\id_{U_2\perp\generators{-1}^7}$. Then
$$
\Orth(B)\cong E\rtimes(\ZZ/2)^3,
\qquad
\Gamma(2)\cong E(2)\rtimes(\ZZ/2)^2,
\quad E(2):=\ker\big(E\longrightarrow\Orth(q_{T_\Co})\big),
$$
where the latter order-four complement is generated by $r$ and $h$. The image of $E$ on the 527 nonzero isotropic discriminant classes has order **$23\,499\,295\,948\,800$**, precisely half of $\abs{\Orth(q_{T_\Co})}$. This reduces the full kernel-generation problem to the level-two kernel of the explicitly given **18-generator Eichler group** $E$. The split-extension identity alone does not generate that kernel; its exact normal generation and its minimal ordinary generation are proved later in this section.
:::

::: {.proof}
The three extra generators of @thm:coble-ambient-21-generators act on disjoint orthogonal blocks and therefore are commuting involutions. Their three independent character vectors identify the subgroup they generate with $(\ZZ/2)^3$ and show that it meets the normal subgroup $E=\ker(\rho_{A_M},\det,\spinornorm_\bR)$ trivially. As those subgroups generate $\Orth(B)$, the first split extension follows. The exact Schreier--Sims computation in `test_coble_ambient_twenty_one_integral_generators` gives $\abs{\rho_{T_\Co}(E)}=23\,499\,295\,948\,800$, while the full image has twice that order. The two involutions $r,h$ are the identity modulo $2B$, whereas the third involution $r_{e'-f'}$ has image outside $\rho_{T_\Co}(E)$ by the index-two computation. Therefore an element $e\,r^a h^b r_{e'-f'}^c$ lies in $\Gamma(2)$ if and only if $c=0$ and $e\in E(2)$. This gives the second split extension and the index assertion.
:::

::: {.proposition #prop:coble-eichler-squares-obstruction title="Squares of the 18 Eichler generators do not normally generate the level-two kernel"}

Let $g_1,\ldots,g_{18}$ be the exact Eichler generators of $E$ in @thm:coble-ambient-21-generators, and let $N_2\lhd E$ be the normal closure of their squares. Then
$$
N_2\subsetneq E(2).
$$
More precisely, the image of $N_2$ in the binary congruence quotient $\Gamma(2)/\Gamma(4)$ has dimension **44**, whereas the image of $E(2)$ has dimension **at least 54**. In fact, the quotient of their level-four images has order $2^{54-44}=1024$, so $[E(2):N_2]\ge1024$. Thus simply squaring the 18 ambient Eichler generators and closing under conjugation is provably insufficient, already at level four. There is an explicit additional relation: the last two simple $D_7$ roots are $d_6-d_7$ and $d_6+d_7$, whose sum is $2d_6$. Therefore $g_8g_9=t(e,2d_6)$ is in $E(2)$ (indices $7,8$ in the zero-based certificate). Adjoining this **one** element to the 18 squares and closing under $E$-conjugation increases the exact level-four rank from **44 to 54**. The two independent character involutions complement this 54-dimensional subspace to the full 56-dimensional congruence image, so this **does** certify equality with the complete image of $E(2)$ modulo four. It does not prove generation of the infinite $E(2)$.

Furthermore, adjoining the two explicit character involutions $r_{d_1}$ and $-\id_{U_1}$ raises the rank from **54 to 56**, exactly the independently proved dimension of $\Gamma(2)/\Gamma(4)$. Thus the 18 squares, the single relation $t(e,2d_6)$, their conjugates under the 18 Eichler generators, and these two involutions **generate the entire finite congruence quotient $\Gamma(2)/\Gamma(4)$**. This is a complete finite-level generating theorem; it does not identify their generated infinite subgroup with $\Gamma(2)$. The source-hashed `coble_ambient_twenty_one_generators.json` records all 21 exact positive relation words (18 squares, one root-pair product, and two character involutions); `test_coble_level_two_relation_words_are_public_kernel_morphisms` independently reconstructs all 21 as actual elements of the maintained public `Tco.stable_orthogonal_group()` API.
:::

::: {.proof}
Each $g_i^2$ reduces to the identity modulo $2B$ because the 18 Eichler generators act as characteristic-two unipotent transvections on $B/2B$. The map $\Gamma(2)\to\operatorname{Mat}_{11}(\F_2)$, $g\mapsto(g-I)/2\bmod2$, has kernel $\Gamma(4)$ and is a homomorphism. Conjugation by $g_i$ acts on its image by $A\mapsto\bar g_i A\bar g_i^{-1}$. The exact regression `test_coble_level_two_eichler_squares_fail_normal_generation` starts with the 18 matrices $(g_i^2-I)/2\bmod2$, row-reduces their span (rank 16), and closes that span under conjugation by all 18 reductions $\bar g_i$. The closure stabilizes at rank **44**. This is precisely the image of $N_2$ in $\Gamma(2)/\Gamma(4)$, because the $g_i$ generate $E$.

On the other hand, @cor:coble-level-two-kernel-split-extension gives $[\Gamma(2):E(2)]=4$, and @cor:coble-level-four-normal-span proves that $\Gamma(2)/\Gamma(4)$ is a 56-dimensional binary vector space. The image $E(2)\Gamma(4)/\Gamma(4)$ therefore has index at most four in that vector space, hence dimension at least 54. As $44<54$, the normal closure of the 18 squares is strictly smaller than $E(2)$. The same regression then inserts the exact matrix $(g_8g_9-I)/2\bmod2$ and closes the enlarged span under the 18 conjugations, obtaining rank 54. Since $g_8g_9=t(e,2d_6)$ is congruent to the identity modulo two, this enlarged span consists entirely of images of actual elements of $E(2)$.

Finally, the regression inserts the two exact matrices $(r_{d_1}-I)/2\bmod2$ and $(-\id_{U_1}-I)/2\bmod2$. Their two classes are independent modulo the preceding 54-dimensional subspace, giving rank 56. Each matrix comes from an actual integral isometry in $\Gamma(2)$; hence the resulting subgroup image is all of $\Gamma(2)/\Gamma(4)$, by its independently certified dimension.
:::

::: {.proposition #prop:coble-eichler-level-eight-derived-image title="Exact rank 54 of the Eichler congruence layer modulo eight"}

Let $E(2^k)=E\cap\Gamma(2^k)$, and let $H\lhd E$ be the normal closure of the 19 integral Eichler relations of @prop:coble-eichler-squares-obstruction. Then
$$
E(4)/E(8)\cong(\ZZ/2)^{54},\qquad H\,E(8)=E(2).
$$
Thus the **19 explicit relations normally generate the entire finite quotient $E(2)/E(8)$**, not merely its quotient modulo four. This remains distinct from generation of the infinite group $E(2)$.
:::

::: {.proof}
The exact regression `test_coble_eichler_normal_relations_have_rank_54_at_level_eight` reconstructs 54 integral lifts $h_i\in H\cap E(2)$ independent modulo four. Their squares and pairwise commutators lie in $H\cap E(4)$ and span a **54-dimensional** binary image in $E(4)/E(8)$. It remains to prove that this is an upper bound for *all* of $E(4)/E(8)$.

Work in the odd unimodular diagonal (@def:polarization-functors) basis $B\cong\generators1^2\perp\generators{-1}^9$, with diagonal Gram matrix $D=\operatorname{diag}(\varepsilon_1,\ldots,\varepsilon_{11})$, $\varepsilon_i\in\{\pm1\}$. For any $g\in E(4)$ write $g=I+4A$, $A\in\operatorname{Mat}_{11}(\ZZ)$. Orthogonality gives
$$
A^tD+DA+4A^tDA=0.
$$
Modulo two, $A$ is symmetric. The diagonal equations give $A_{ii}=-2\varepsilon_i\sum_j\varepsilon_j A_{ji}^2$, so every $A_{ii}$ is even. Summing these equations and pairing $(i,j)$ with $(j,i)$ shows $\operatorname{tr}A\equiv0\pmod4$, since $A_{ij}\equiv A_{ji}\pmod2$. Therefore $\bar A=A\bmod2$ is alternating, and the space of all such matrices has dimension $\binom{11}{2}=55$.

Because $g\in E=\widetilde{\mathrm{SO}}^+(M)=O'(M)$, its **rational spinor norm is trivial** by @thm:coble-ambient-21-generators. The [Zassenhaus determinant formula (Conrad, *Reductive Group Schemes (@def:scheme-as-lrs)*, Theorem C.5.7)](https://math.stanford.edu/~conrad/papers/luminysga3smf.pdf) applies because $I+g$ is invertible over $\QQ_2$ and gives
$$
\operatorname{sn}_{\QQ_2}(g)=\det((I+g)/2)=\det(I+2A)
\quad\text{in }\QQ_2^\times/(\QQ_2^\times)^2.
$$
Expanding the determinant modulo eight and using $A_{ii}\equiv0\pmod2$ and $\operatorname{tr}A\equiv0\pmod4$ gives
$$
\det(I+2A)\equiv1+4\sum_{i<j}A_{ij}\pmod8.
$$
This determinant is an odd $2$-adic square, so it is $1$ modulo eight. Hence the single nonzero linear equation $\sum_{i<j}\bar A_{ij}=0$ cuts the 55-dimensional alternating-matrix space to dimension **54**. The 54 independent exact classes computed above therefore exhaust $E(4)/E(8)$. The regression independently transports their leading matrices to this diagonal basis and checks symmetry, zero diagonal and the Zassenhaus parity equation.

Finally, @prop:coble-eichler-squares-obstruction already proves $H\,E(4)=E(2)$. The rank computation gives $E(4)\subseteq H\,E(8)$; combining this with $H\,E(4)=E(2)$ yields $H\,E(8)=E(2)$, as claimed.
:::

::: {.corollary #cor:coble-eichler-all-higher-congruence-lower-bound title="Uniform rank 54 at every higher power of two"}

Let $H\lhd E$ be the normal closure of the 19 integral Eichler relations of @prop:coble-eichler-squares-obstruction. For **every** integer $k\ge2$, the image of $H\cap\Gamma(2^k)$ in $\Gamma(2^k)/\Gamma(2^{k+1})$ contains an elementary abelian subgroup of rank **54**. Thus the 19 explicit relations give a uniform, infinite tower of independent higher-congruence classes, not merely the level-four computation. This remains a *lower bound* and does not assert equality with the full congruence subgroup at any level.
:::

::: {.proof}
By @prop:coble-eichler-level-eight-derived-image, there are 54 elements $h_i\in H\cap\Gamma(4)$ with linearly independent images $(h_i-I)/4\pmod2$. For any $m\ge2$ and $g=I+2^m A$ with integral $A$, direct multiplication gives
$$
g^2=I+2^{m+1}(A+2^{m-1}A^2),
$$
so $(g^2-I)/2^{m+1}\equiv A\pmod2$. Iterating, $h_i^{2^{k-2}}\in H\cap\Gamma(2^k)$ and their leading matrices modulo two are the same independent 54 matrices for every $k\ge2$. The regression verifies this lifting explicitly at $k=3,4$ using exact arithmetic modulo 32; the formula proves it for all $k$.
:::

::: {.theorem #thm:coble-eichler-exact-deep-congruence-ranks title="Exact rank 55 at every congruence level at least eight"}

For $E=\widetilde{\mathrm{SO}}^+(U^{\oplus2}\perp D_7(-1))$, **every** integer $k\ge3$ satisfies
$$
E(2^k)/E(2^{k+1})\cong(\ZZ/2)^{55}.
$$
This differs from the rank **54** at $k=2$ proved in @prop:coble-eichler-level-eight-derived-image. The extra direction at level eight has a short, explicit integral witness: if $g_0,\ldots,g_{17}$ are the zero-based Eichler generators in `coble_ambient_twenty_one_generators.json`, then
$$
w=\big(g_{17}g_{14}^{-1}g_{11}^{-1}g_3\big)^{10}\in E(8)
$$
has leading matrix $(w-I)/8\pmod2$ independent of the 54 classes supplied by the squares of the preceding level-four witnesses. Its successive powers $w^{2^{k-3}}$ supply the extra direction for all $k\ge3$.

Consequently the 19-relation normal closure is proved to supply at least 54 of the 55 dimensions at every deeper level; **whether it also supplies the last dimension is not established**. In particular, a rank-54 lower bound cannot be promoted to full higher-congruence generation.
:::

::: {.proof}
For any $k\ge2$, write $g=I+2^kA$ with $g\in E(2^k)$. Orthogonality in the odd diagonal (@def:polarization-functors) basis gives $A^tD+DA+2^kA^tDA=0$. Modulo two this makes $A$ symmetric; its diagonal equations imply $A_{ii}$ is divisible by $2^{k-1}$, hence even. Thus the leading matrix $A\bmod2$ is alternating, a space of dimension $\binom{11}{2}=55$. This proves the upper bound $55$ for every congruence layer.

The exact regression `test_coble_eichler_normal_relations_have_rank_54_at_level_eight` constructs 54 independent elements of $E(4)/E(8)$ as squares and commutators of the 19-relation lifts. Squaring these 54 elements gives 54 independent classes in $E(8)/E(16)$. The same regression constructs the displayed four-letter word and verifies that its tenth power is the identity modulo eight, while its leading matrix modulo sixteen is **independent** of those 54 classes. Therefore $E(8)/E(16)$ has dimension at least 55, and the upper bound proves equality. For $k\ge3$, the identity $(I+2^kA)^2\equiv I+2^{k+1}A\pmod{2^{k+2}}$ preserves the leading matrix under squaring, so the 55 independent witnesses propagate to every deeper layer. This proves the formula for all $k\ge3$.
:::

::: {.theorem #thm:coble-eichler-normal-closure-two-adic-density title="The 19 explicit Eichler relations are dense at every power of two"}

Let $H\lhd E$ be the normal closure of the 19 exact integral Eichler relations of @prop:coble-eichler-squares-obstruction. Then for **every integer $k\ge1$**,
$$
H\,E(2^k)=E(2).
$$
Equivalently, the 19 relations normally generate the **entire image of $E(2)$ modulo $2^k$ for every $k$**. This is an infinite family of exact finite-quotient equalities, not a bounded computational extrapolation. It proves that $H$ is dense in the $2$-adic congruence topology on $E(2)$; it does **not**, by itself, prove the abstract group equality $H=E(2)$.
:::

::: {.proof}
The exact test `test_coble_nineteen_relations_generate_the_full_kernel_modulo_sixteen` works with the 18 Eichler generators from the source-hashed 21-matrix certificate, reduced modulo sixteen. Starting from the 19 certified level-two words, it repeatedly forms squares, commutators and conjugates by all 18 Eichler generators, retaining an exact matrix lift whenever a new independent leading vector appears at levels two, four or eight. Every retained lift is therefore a product of conjugates of the 19 relations, hence belongs to $H$. The calculation terminates with independent ranks **$(54,54,55)$** in the successive quotients $E(2)/E(4)$, $E(4)/E(8)$, and $E(8)/E(16)$. These are their *exact full dimensions*, by @prop:coble-eichler-squares-obstruction, @prop:coble-eichler-level-eight-derived-image and @thm:coble-eichler-exact-deep-congruence-ranks. In particular $H\,E(16)=E(2)$, and the four-letter witness $w=(g_{17}g_{14}^{-1}g_{11}^{-1}g_3)^{10}$ from @thm:coble-eichler-exact-deep-congruence-ranks reduces to the identity against the retained $H$-basis modulo sixteen.

The same computation supplies 55 actual elements $h_1,\ldots,h_{55}\in H\cap E(8)$ whose leading matrices $(h_i-I)/8\pmod2$ are independent. For every $m\ge3$, the squaring identity $(I+2^mA)^2\equiv I+2^{m+1}A\pmod{2^{m+2}}$ shows that $h_i^{2^{m-3}}\in H\cap E(2^m)$ have the **same 55 independent leading matrices**. By @thm:coble-eichler-exact-deep-congruence-ranks, this is the entire quotient $E(2^m)/E(2^{m+1})$. Inductively, from $H\,E(16)=E(2)$ we obtain $H\,E(2^k)=E(2)$ for every $k\ge4$; the lower powers follow immediately. No assertion about noncongruence finite quotients is used.
:::

::: {.corollary #cor:coble-eichler-odd-congruence-surjectivity title="The Eichler-square normal closure surjects at every odd modulus"}

Let $E=\generators{g_1,\ldots,g_{18}}$ be the explicit Eichler group of @thm:coble-ambient-21-generators, and let $N_2\lhd E$ be the normal closure of the squares $g_i^2$. For **every odd positive integer** $m$, the reductions of $N_2$ and $E$ in $\GL(B/mB)$ are equal:
$$
\rho_m(N_2)=\rho_m(E).
$$
The same is therefore true for the larger normal closure of all 19 level-two Eichler relations. In particular, **no odd-modulus finite congruence quotient distinguishes that normal closure from $E$**. This is an exact theorem for every odd modulus, independent of the remaining higher-power-of-two problem.
:::

::: {.proof}
Each $g_i$ is an Eichler transvection $t(e,a)$ or $t(f,a)$, so the composition identity of @thm:coble-ambient-21-generators gives $g_i^n=t(e,na)$ (or $t(f,na)$) for every integer $n$. For odd $m$, the matrix formula for $t(e,ma)$ has all nonconstant terms divisible by $m$, hence $g_i^m\equiv I\pmod m$. Consequently
$$
(g_i^2)^{(m+1)/2}=g_i^{m+1}\equiv g_i\pmod m.
$$
Since $g_i^2\in N_2$, the reduction of $N_2$ contains every $\rho_m(g_i)$, which generate $\rho_m(E)$. The reverse inclusion follows from $N_2\subseteq E$. The exact regression `test_coble_eichler_squares_generate_every_odd_modulus_image` independently checks the displayed matrix identities for all 18 generators at moduli $3,5,7,9,15$; the transvection identity proves them uniformly.
:::

::: {.theorem #thm:coble-eichler-full-congruence-density title="The 19 explicit relations are dense in every integral congruence quotient"}

Let $E=\widetilde{\mathrm{SO}}^+(U^{\oplus2}\perp D_7(-1))$, $E(2)=\ker(E\to\Orth(B/2B))$, and let $H\lhd E$ be the normal closure of the 19 exact Eichler relations. Then for **every positive integer $n$**,
$$
\rho_n(H)=\rho_n(E(2)),\qquad\text{equivalently }H\,(E(2)\cap\Gamma(n))=E(2).
$$
Thus the 19 relations generate the entire image of the infinite level-two kernel in **every** congruence quotient, including arbitrary mixed moduli, not only powers of two. The normal closure is congruence-dense in $E(2)$. This theorem does **not** identify $H$ with $E(2)$ as abstract groups: equality also requires ruling out proper finite-index subgroups invisible to congruence reduction.
:::

::: {.proof}
The even lattice $M=U^{\oplus2}\perp D_7(-1)$ satisfies the hypotheses of [@GHS08, Theorem 1.7], which proves that $E=\widetilde{\mathrm{SO}}^+(M)$ has **trivial abelianization**, i.e. $E$ is perfect. By @cor:coble-eichler-odd-congruence-surjectivity, the normal closure of the 18 squares, which lies in $H\subseteq E(2)$, surjects onto $\rho_m(E)$ for every odd integer $m$. Therefore $\rho_m(E(2))=\rho_m(E)$, a perfect finite group, and $\rho_m(H)$ equals it. By @thm:coble-eichler-normal-closure-two-adic-density, $\rho_{2^k}(H)=\rho_{2^k}(E(2))$ for every $k\ge0$.

Write $n=2^km$ with $m$ odd, and put $A=\rho_{2^k}(E(2))$, $B=\rho_m(E(2))$. The group $A$ is a finite $2$-group: it consists of matrices congruent to the identity modulo two, with a filtration whose successive quotients are elementary abelian $2$-groups. The group $B$ is perfect, as just proved. By the Chinese remainder theorem, the images of $H$ and of $E(2)$ modulo $n$ are subgroups of $A\times B$, and each projects surjectively to **both** factors. By Goursat's lemma, any such subdirect subgroup determines a common quotient of $A$ and $B$. Every quotient of a finite $2$-group is a $2$-group, while every quotient of a perfect group is perfect; the only finite perfect $2$-group is trivial. Hence every such subdirect subgroup is the full direct product $A\times B$. In particular both $H$ and $E(2)$ have the same image modulo $n$, proving the theorem.
:::

::: {.theorem #thm:coble-eichler-normal-closure-finite-index title="The explicit Eichler-square normal closure has finite index"}

Let $E=\widetilde{\mathrm{SO}}^+(U^{\oplus2}\perp D_7(-1))$ and let $N_2\lhd E$ be the normal closure of the squares of the 18 explicit Eichler generators of @thm:coble-ambient-21-generators. Then **$N_2$ has finite index in $E$**, hence also in $E(2)$. More precisely,
$$
1024\ \le\ [E(2):N_2]\ <\ \infty.
$$
The normal closure $N_{19}$ of the 19 relations obtained by adjoining $g_8g_9=t(e,2d_6)$ likewise has finite index in $E(2)$. This is a theorem about the *infinite* integral arithmetic group (@def:arithmetic-group), not a finite congruence calculation. It does **not** establish $N_{19}=E(2)$, nor does the normal subgroup theorem alone identify a principal congruence subgroup contained in $N_{19}$.
:::

::: {.proof}
The integral group $E$ has index eight in $\Orth(I_{2,9})$ by @thm:coble-ambient-21-generators and lies in the identity component $\mathrm{SO}_0(2,9)$. By the Borel--Harish-Chandra lattice theorem, it is an arithmetic lattice in that connected simple real Lie group (@def:real-lie-group). The group $\mathrm{SO}_0(2,9)$ has real rank two and finite center, so $E$ is an irreducible higher-rank lattice. The first Eichler generator $g_1=t(e,e')$ has infinite order: $g_1^n=t(e,ne')$ and its action on $f$ distinguishes all integers $n$. Therefore $N_2$ contains the infinite cyclic subgroup $\generators{g_1^2}$ and is an infinite normal subgroup of $E$. The [Margulis normal subgroup theorem (Witte Morris, *Introduction to Arithmetic Groups*, Theorem 13.1)](https://www.mathi.uni-heidelberg.de/~wienhard/retreat10/references/morris_book.pdf) implies that $E/N_2$ is finite. Since $N_2\subseteq E(2)$, its index in $E(2)$ is finite. The exact level-four ranks 44 and 54 of @prop:coble-eichler-squares-obstruction give $[E(2):N_2]\ge2^{54-44}=1024$. Finally $N_2\subseteq N_{19}\subseteq E(2)$, so $N_{19}$ also has finite index.
:::

::: {.theorem #thm:coble-eichler-full-normal-generation title="The 19 Eichler relations normally generate the full infinite level-two kernel"}

Let $B=I_{2,9}$, $M=U^{\oplus2}\perp D_7(-1)$, $E=\widetilde{\mathrm{SO}}^+(M)$, and $E(2)=E\cap\Gamma(2)$. Then the normal closure $H\lhd E$ of the **19 explicit integral relations**
$$
g_i^2\ (0\le i<18),\qquad g_7g_8
$$
from the exact source-hashed `coble_ambient_twenty_one_generators.json` satisfies
$$
\boxed{H=E(2).}
$$
Consequently the full infinite principal level-two orthogonal kernel has the exact **finite normal-generation description**
$$
\Gamma(2)=\generators{E(2),r_{d_1},-\id_{U_1}}
=E(2)\rtimes(\ZZ/2)^2,
$$
where $E(2)$ is the normal closure in the explicitly 18-generated Eichler group $E$ of the 19 displayed relations. This is an equality of **abstract integral groups**, not merely of finite congruence images.

The 19 relations are **normal generators relative to $E$**, not asserted to be an ordinary 19-element generating set of $E(2)$. The compact **minimal 56-element ordinary generating family (@def:generating-frame)** is proved later in this section, independently of the infeasible full-index Schreier enumeration.
:::

::: {.proof}
We combine the exact congruence-density theorem @thm:coble-eichler-full-congruence-density with the arithmetic normal-subgroup theorem @thm:coble-eichler-normal-closure-finite-index, and eliminate the possible noncongruence finite quotient by the **central congruence kernel** and the **trivial Schur multiplier** of the finite simple discriminant image.

**Centrality of the congruence kernel.** Let $G=\operatorname{Spin}(B_\QQ)$, an absolutely simple simply connected $\QQ$-group of type $B_5$ and $\QQ$-rank $2$. Its real Lie group (@def:real-lie-group) $G(\RR)=\operatorname{Spin}(2,9)(\RR)$ is *not* topologically simply connected: a maximal (@def:maximal-lattice) compact subgroup has a circle factor from $\operatorname{Spin}(2)$, so its fundamental group is infinite. The congruence kernel of $G$ is central by the Kneser--Raghunathan centrality theorem for isotropic simply connected groups; see [Prasad--Rapinchuk, *Developments on the congruence subgroup problem*, §5.1](https://www.mathi.uni-heidelberg.de/~wienhard/retreat10/references/prasad_rapinchuk_CSP.pdf). Their Theorem 3 says the metaplectic kernel is trivial when $S=\{\infty\}$ contains a real place at which $G(\RR)$ is not topologically simply connected; their Theorem 2 identifies the central congruence kernel with its Pontryagin dual. Hence the congruence kernel of $G$ is **trivial**.

Let $\pi:G\to\mathrm{SO}(B_\QQ)$ be the central isogeny, and let $\widetilde E=\pi^{-1}(E)\subset G(\QQ)$. Since $E$ is an arithmetic subgroup (@def:hsd-arithmetic-subgroup) of the rational spinor kernel, $\widetilde E$ is arithmetic, and the trivial congruence kernel property passes to this finite-index arithmetic subgroup. Thus the profinite completion $\widehat{\widetilde E}$ identifies with its closure in $G(\mathbb A_f)$. The exact central quotient $\widetilde E/\{\pm1\}=E$ gives $\widehat E\cong\widehat{\widetilde E}/\{\pm1\}$. On the other hand, the congruence completion $\overline E$ is the image of the compact closure $\overline{\widetilde E}\subset G(\mathbb A_f)$ under $\pi$. The kernel of $\pi$ on this closure is contained in the product of the local central kernels $\prod_p\{\pm1\}$, hence is central. Therefore the kernel $C_E$ of $\widehat E\to\overline E$ is **central**, whether or not it is trivial. This argument does not assume that arbitrary congruence subgroups have congruence images under $\pi$.

**The finite central extension.** By @thm:coble-eichler-normal-closure-finite-index, $H\lhd E$ has finite index. Put $Q=E/H$ and $K=E(2)/H$. Since $H$ has the *same image as $E(2)$ in every congruence quotient* by @thm:coble-eichler-full-congruence-density, the compact image of $\widehat H$ in $\overline E$ equals the image of $\widehat{E(2)}$. Thus every element of $K$ is represented in $Q$ by an element of the central congruence kernel $C_E$: for a lift of $x\in E(2)$, choose a lift from $\widehat H$ with the same congruence image; their quotient lies in $C_E$. Consequently $K\subseteq Z(Q)$.

By [@GHS08, Theorem 1.7], $E$ is **perfect**, so its finite quotient $Q$ is perfect. The exact 527-point Schreier--Sims computation in `test_coble_ambient_twenty_one_integral_generators` identifies the quotient $F=E/E(2)$ as the finite simple orthogonal group $P\Omega_{10}^+(2)$ of order $23\,499\,295\,948\,800$: it is the derived index-two subgroup of the full plus-type discriminant orthogonal group. Its Schur multiplier is **trivial**, by the standard $D_n(q)$ multiplier formula for odd $n$ (order $\gcd(4,q-1)$), here $n=5$, $q=2$; the [ATLAS entry for $O_{10}^+(2)$](https://brauer.maths.qmul.ac.uk/Atlas/v3/clas/O10p2/) records its exact order $23\,499\,295\,948\,800$, multiplier $1$, and a faithful $527$-point permutation representation (@def:permutation-representation), matching the certified finite action; see also [GLS, Theorem 2.5.12(i)](https://ri.conicet.gov.ar/server/api/core/bitstreams/cfea7e45-79d3-4836-838f-98aaa5dc0b90/content). Hence
$$
1\longrightarrow K\longrightarrow Q\longrightarrow F\longrightarrow1
$$
is a **perfect central extension** of a perfect group with trivial Schur multiplier. Such an extension has trivial kernel by the universal-central-extension characterization of the Schur multiplier. Therefore $K=1$, i.e. $H=E(2)$. The final split decomposition follows from @cor:coble-level-two-kernel-split-extension.
:::

::: {.proposition #prop:coble-ordinary-fifty-six-congruence-generators title="Fifty-six ordinary integral generators of every level-sixteen quotient"}

There is a **56-element ordinary generating family (@def:generating-frame)** $S\subset\Gamma(2)$, given by the exact integral matrices in `computations/reports/coble_kernel_fifty_six_congruence_generators.json`, such that
$$
\generators{S}\,\Gamma(16)=\Gamma(2).
$$
In fact $S$ consists of the 26 proved generators of the integral level-two plane stabilizer (@def:group-orbit) $K_P$ from @prop:coble-level-two-plane-parabolic, together with 30 explicitly selected conjugates $g_i k_j g_i^{-1}$ for $10\le i\le15$ and $k_j\in K_P$, where $g_i$ are the published ambient Eichler generators. The 56 matrices first generate the full finite congruence quotient; their **ordinary generation of the entire infinite group** is established separately, so the lattice-database `generator_morphisms` field may use this certified family. Moreover, **56 is a sharp lower bound for the number of ordinary generators of $\Gamma(2)$**: its quotient $\Gamma(2)/\Gamma(4)\cong(\ZZ/2)^{56}$ requires at least 56 generators. Thus this family attains the minimum (@def:definite-minimum-shell) possible cardinality for an ordinary generating family of the full infinite group.
:::

::: {.proof}
Each selected matrix is an integral isometry congruent to the identity modulo two: this is true for $K_P$, and is preserved under conjugation by integral isometries. The reproducible source-hashed Sage script `coble_kernel_fifty_six_congruence_generators.py` performs exact binary elimination on their leading matrices $(g-I)/2\pmod2$, selecting 26 original parabolic generators and 30 conjugates that give rank **56**, equal to $\dim_{\F_2}\Gamma(2)/\Gamma(4)$ by @cor:coble-level-four-normal-span.

The regression `test_coble_fifty_six_ordinary_elements_span_kernel_modulo_sixteen` then computes the **subgroup generated by these 56 matrices**, not its normal closure in the ambient group. It retains exact matrix lifts whenever a new class appears at levels two, four or eight, and repeatedly takes their squares and pairwise commutators. Exact elimination terminates with graded ranks **$(56,54,55)$**. These equal the full graded ranks of $\Gamma(2)/\Gamma(4)$, $\Gamma(4)/\Gamma(8)$, and $\Gamma(8)/\Gamma(16)$, by @cor:coble-level-four-normal-span, @prop:coble-eichler-level-eight-derived-image and @thm:coble-eichler-exact-deep-congruence-ranks. Consequently the generated subgroup has the full image of $\Gamma(2)$ modulo sixteen.
:::

::: {.theorem #thm:coble-fifty-six-ordinary-generators-finite-index title="The 56 ordinary integral kernel elements generate a finite-index subgroup"}

Let $S\subset\Gamma(2)$ be the 56 exact integral isometries of @prop:coble-ordinary-fifty-six-congruence-generators, and put $K=\generators{S}$. Then
$$
\boxed{[\Gamma(2):K]<\infty.}
$$
Moreover $K$ has full image in $\Gamma(2)/\Gamma(2^k)$ for **every** $k\ge1$. Thus $K$ is a **finite-index ordinary finitely generated, 2-adically dense subgroup** of the full integral kernel. An independent exact GAP matrix-group computation also shows that its reduction modulo **three** is the full $\Orth(11,\F_3)$, of order
$$
2\cdot3^{25}\prod_{i=1}^{5}(3^{2i}-1)=305\,831\,171\,736\,479\,457\,253\,785\,600.
$$
The source-hashed result is `computations/reports/coble_kernel_fifty_six_mod_three_image.json`, regenerated by `coble_kernel_fifty_six_odd_image_audit.py`; its integrity is checked by `test_coble_fifty_six_mod_three_full_orthogonal_image_certificate`. The finite-index and congruence calculations alone do not establish $K=\Gamma(2)$; the missing noncongruence obstruction is eliminated by the spin-cover CSP argument that follows.
:::

::: {.proof}
The source-hashed exact computation of @prop:coble-ordinary-fifty-six-congruence-generators proves that $K$ has full images in the successive congruence layers of ranks $(56,54,55)$ through modulus sixteen. The exact rank of each layer $\Gamma(2^k)/\Gamma(2^{k+1})$ for $k\ge3$ is $55$ by @thm:coble-eichler-exact-deep-congruence-ranks, since every element sufficiently close to the identity has trivial determinant and rational spinor character. Choose 55 elements of $K\cap\Gamma(8)$ whose leading matrices form a basis. Repeated squaring preserves those 55 leading matrices at all deeper levels. By induction and compactness, the closure of $K$ in $\Orth(B\otimes\ZZ_2)$ contains the entire principal congruence subgroup of level eight. In particular the $2$-adic closure of $K\cap E$ contains an open neighborhood of the identity in $\mathrm{SO}(B\otimes\QQ_2)$; therefore $K\cap E$ is Zariski dense in the rational algebraic group $\mathrm{SO}(B_\QQ)$.

The 56-element family contains **all 26 generators of $K_P=\Stab_{\Orth(B)}(P)\cap\Gamma(2)$**, not just a selection from them. By @prop:coble-level-two-plane-parabolic, its intersection with the integral unipotent radical $U_P(\ZZ)$ of the rational maximal (@def:maximal-lattice) parabolic stabilizing $P$ is a subgroup of finite index (indeed the full level-two unipotent subgroup). Thus $K\cap E$ is Zariski dense and contains a finite-index subgroup of $U_P(\ZZ)$. The [Raghunathan--Venkataramana arithmeticity criterion](https://helper.ipam.ucla.edu/publications/zds2015/zds2015_12461.pdf) for higher-rank rational simple groups states that such a subgroup has finite index in the integral arithmetic group (@def:arithmetic-group). Apply it to the inverse image of $K\cap E$ in the simply connected rational spin group $\operatorname{Spin}(B_\QQ)$: the spin covering is a finite central isogeny, it is an isomorphism on each rational unipotent radical, and Zariski density lifts. The spin group has real rank $2$ and rational rank $2$, so the criterion gives finite index in its integral arithmetic subgroup (@def:hsd-arithmetic-subgroup). Projecting through the finite central isogeny proves $[E:K\cap E]<\infty$, hence $[\Gamma(2):K]<\infty$.

No claim about arbitrary odd or mixed moduli is made for $K$: the normal-generation theorem for the separate subgroup $H$ does not automatically imply ordinary generation or congruence-density for $K$.
:::

::: {.proposition #prop:coble-fifty-six-full-odd-lie-span title="The 56 ordinary candidates generate the full orthogonal Lie algebra away from two"}

Among the 56 exact integral kernel matrices of @prop:coble-ordinary-fifty-six-congruence-generators, **46** are nonidentity unipotent isometries $g$ with $(g-I)^3=0$. Their integral logarithms
$$
\log g=(g-I)-\tfrac12(g-I)^2
$$
lie in $\mathfrak{so}(B;\ZZ)$. The **integral Lie subring** generated by these 46 logarithms has full rank $55$ and index exactly
$$
[\mathfrak{so}(B;\ZZ):\operatorname{Lie}_{\ZZ}\generators{\log g}]=2^{64}.
$$
In particular their reductions generate the **entire orthogonal Lie algebra over $\F_p$ for every odd prime $p$**, and the connected algebraic subgroup of $\mathrm{SO}(B_\QQ)$ generated by their unipotent one-parameter groups is all of $\mathrm{SO}(B_\QQ)$. This does **not** by itself prove that the 56 matrices generate the finite group $\mathrm{SO}(B/ pB)$ for every odd prime: Lie-algebra generation and generation of rational points are different assertions.
:::

::: {.proof}
In the fixed odd diagonal (@def:polarization-functors) basis, $\mathfrak{so}(B;\ZZ)$ has the explicit 55-dimensional basis of matrices $E_{ij}-\varepsilon_i\varepsilon_j E_{ji}$, $i<j$. The reproducible source-hashed Sage script `coble_kernel_fifty_six_lie_span.py` takes the 46 integral logarithms, expresses them in this basis, and repeatedly adds every bracket $[a,b]$ with $a$ in the current Hermite-normal-form basis and $b$ one of the original 46 logarithms. The first span has rank 46; after one bracket enlargement it has rank 55, and the next iteration verifies closure. The final 55-by-55 integer Hermite basis has determinant $2^{64}$. This is an exact integer computation, reproduced byte-identically and checked by `test_coble_fifty_six_unipotent_lie_lattice_is_full_away_from_two`. The determinant is a unit after inverting two, proving the uniform odd-characteristic assertion. In characteristic zero, a connected algebraic subgroup containing the one-parameter groups also contains their logarithms and the Lie algebra they generate, so it has the same Lie algebra as the connected group $\mathrm{SO}(B_\QQ)$ and therefore equals it.
:::

::: {.theorem #thm:coble-fifty-six-all-odd-prime-powers title="The 56 ordinary candidates have the full kernel image at every odd prime power"}

Let $K$ be the subgroup generated by the 56 exact integral matrices of @prop:coble-ordinary-fifty-six-congruence-generators. Then for **every odd prime $p$ and every $k\ge1$**,
$$
\boxed{\rho_{p^k}(K)=\rho_{p^k}(\Gamma(2)).}
$$
This is a theorem for **all odd prime powers**, not just sufficiently large primes. Together with @thm:coble-fifty-six-ordinary-generators-finite-index it proves that $K$ is finite-index, has full images in all $2$-power congruence quotients, and has full images in all odd-prime-power congruence quotients. Equality of the abstract integral groups $K$ and $\Gamma(2)$ remains a separate assertion.
:::

::: {.proof}
**Small primes.** The exact source-hashed Sage/GAP audit `coble_kernel_fifty_six_small_odd_local.py` verifies for $p=3,5,7,11,13$ that the finite matrix group generated by the 56 reductions contains $\Omega_{11}(\F_p)$, using the `RecogniseClassical` algorithm. Independently, it computes the leading matrices $(g^p-I)/p\pmod p$ for the 46 integral unipotents $g$ of @prop:coble-fifty-six-full-odd-lie-span, closes their span under conjugation by the 56 finite generators, and obtains the **full rank 55** of $\mathfrak{so}_{11}(\F_p)$ at every one of these primes. The complete audit and its source (@def:globular-boundary) hash are checked byte-for-byte by `test_coble_fifty_six_small_odd_local_images_are_full`. At $p=3$, the stronger independent exact GAP group-order calculation of @thm:coble-fifty-six-ordinary-generators-finite-index gives the entire $\Orth_{11}(\F_3)$.

**Primes $p\ge17$.** Let $H_p$ be the finite subgroup generated by the reductions of the 46 unipotents. They have order $p$ for $p>3$. Their logarithms generate the full orthogonal Lie algebra over $\F_p$ by @prop:coble-fifty-six-full-odd-lie-span. Thus the natural 11-dimensional $H_p$-module is absolutely irreducible: any invariant subspace is stable under the logarithms (polynomials in the unipotents), hence under all of $\mathfrak{so}_{11}(\F_p)$, whose natural module is irreducible in odd characteristic. A normal $p$-subgroup of $H_p$ would have a nonzero fixed subspace, which by irreducibility would be the whole module, so it is trivial. The hypotheses of [@Gur99, Theorem D] therefore hold for $p\ge11+3$; the exceptional $J_1$ case has dimension 7 or 8 and cannot occur here. The theorem identifies the group generated by $p$-elements with the finite Chevalley group associated with its exponential envelope. The envelope has Lie algebra $\mathfrak{so}_{11}$, hence is $\mathrm{SO}_{11}$; its $p$-generated finite subgroup is $\Omega_{11}(\F_p)$. Therefore $H_p$ contains $\Omega_{11}(\F_p)$ for every $p\ge17$.

For these same primes, the span of the 46 leading matrices $(g^p-I)/p\pmod p$ under $\operatorname{Ad}(H_p)$ is a nonzero $\Omega_{11}(\F_p)$-stable subspace of $\mathfrak{so}_{11}(\F_p)$. The adjoint module is irreducible for $p\ge17$: stability under all root-group elements $\exp(tX_\alpha)$, $t\in\F_p$, implies stability under $\operatorname{ad}(X_\alpha)$ by polynomial interpolation (the adjoint root-group action has degree (@def:graded-object) less than $p$), so such a subspace is an ideal in the simple Lie algebra. Hence the span is all 55 dimensions, as at the small primes.

**Lifting to all powers.** For every odd prime $p$, we have proved that the image of $K\cap\Gamma(p)$ in $\Gamma(p)/\Gamma(p^2)$ contains all 55 orthogonal Lie-algebra directions. If $h=I+p^mA$, $m\ge1$, then the binomial theorem gives $h^p\equiv I+p^{m+1}A\pmod{p^{m+2}}$. Thus the same 55 independent directions lift to every successive congruence layer, and induction shows that the closure of $K$ contains the entire principal $p$-adic congruence subgroup.

Finally, @thm:coble-eichler-full-normal-generation gives $\Gamma(2)=E(2)\rtimes\generators{r_{d_1},-\id_{U_1}}$. The reduction of $E(2)$ modulo an odd prime lies in $\Omega_{11}(\F_p)$ because $E$ has trivial determinant and rational spinor norm. The two explicit character involutions are already among the 26 integral plane-parabolic generators contained in $K$. Therefore the mod-$p$ image of $K$ contains the mod-$p$ image of $\Gamma(2)$, and the reverse inclusion is automatic. Combining this equality at level $p$ with the full principal $p$-adic congruence layers proves the asserted equality for every $p^k$.
:::

::: {.theorem #thm:coble-fifty-six-full-congruence-density title="The 56 ordinary candidates have the full image in every congruence quotient"}

Let $K=\generators{S}\subset\Gamma(2)$ be the ordinary subgroup generated by the 56 exact integral matrices of @prop:coble-ordinary-fifty-six-congruence-generators. Then for **every positive integer $n$**,
$$
\boxed{\rho_n(K)=\rho_n(\Gamma(2)).}
$$
Thus $K$ is a **finite-index, congruence-dense, 56-generated ordinary subgroup** of the full infinite level-two kernel. Its 56 generators attain the sharp lower bound of @prop:coble-ordinary-fifty-six-congruence-generators. This theorem is about *all* finite congruence quotients, including mixed moduli; the further spin-cover argument later in this section establishes the equality of **abstract integral groups**.
:::

::: {.proof}
Write $E_2=E(2)$ and $K_0=K\cap E_2$. We first prove that $K_0$ has the full image of $E_2$ at **every prime power**. For odd $p$, the 46 unipotent elements of $K$ belong to $E_2$ and, by @thm:coble-fifty-six-all-odd-prime-powers, their reductions generate $\Omega_{11}(\F_p)$ and their $p$-th powers and conjugates generate the entire 55-dimensional first principal $p$-adic layer. Iterated $p$-th powers fill every higher layer, so $\rho_{p^k}(K_0)=\rho_{p^k}(E_2)$ for all $k$. For $p=2$, @prop:coble-ordinary-fifty-six-congruence-generators and its proof give full $\Gamma(2)$ images modulo every $2^k$, while the two character involutions $r_{d_1}$ and $-\id_{U_1}$ lie in $K$. Their images modulo four are independent modulo the image of $E_2$, so the two characters of $\Gamma(2)/E_2$ are detected by reduction modulo four. Any $K$-element congruent to an $E_2$-element modulo $2^k$ for $k\ge2$ therefore already lies in $K_0$. Hence $\rho_{2^k}(K_0)=\rho_{2^k}(E_2)$ for every $k$.

To combine primes, put $L_{p,k}=\rho_{p^k}(E_2)$. For odd $p$, $L_{p,1}=\Omega_{11}(\F_p)$, a nonabelian simple perfect group. For $k>1$, the reduction map $L_{p,k}\to L_{p,k-1}$ has an elementary abelian kernel $V\cong\mathfrak{so}_{11}(\F_p)$, with conjugation action factoring through $\Omega_{11}(\F_p)$. The exact audit `coble_kernel_fifty_six_small_odd_local.py` checks for $p=3,5,7,11,13$ that the span of all differences $\operatorname{Ad}(g)A-A$, for the 46 unipotents and the full orthogonal Lie algebra, has rank **55**. For $p\ge17$, the same assertion follows from the simplicity of $\mathfrak{so}_{11}(\F_p)$ and the root-group interpolation argument in @thm:coble-fifty-six-all-odd-prime-powers. Thus $[\Omega_{11}(\F_p),V]=V$ for every odd prime. Induction on $k$ shows that **every $L_{p,k}$ is perfect**: its derived subgroup surjects onto the perfect group $L_{p,k-1}$ and contains the whole kernel $V$ by the displayed commutator equality.

The composition factors of $L_{p,k}$ consist of the unique nonabelian simple group $\Omega_{11}(\F_p)$ and cyclic groups of order $p$. Consequently for distinct odd primes $p\ne q$, the perfect groups $L_{p,k}$ and $L_{q,\ell}$ have **no common nontrivial quotient**, since their nonabelian simple composition factors have different orders. The group $L_{2,k}$ is a finite $2$-group, so it likewise has no common nontrivial quotient with any perfect odd-prime $L_{p,\ell}$. By Goursat's lemma, any subgroup of the product of these local groups projecting surjectively to each factor is the **entire product**; induction extends this to any finite set of distinct primes. Applying this to the image of $K_0$ and using the prime-power surjectivity proved above yields
$$
\rho_n(K_0)=\rho_n(E_2)=\prod_{p^k\parallel n}L_{p,k}
$$
under the Chinese remainder identification. Finally, @cor:coble-level-two-kernel-split-extension gives $\Gamma(2)=E_2\rtimes\generators{r_{d_1},-\id_{U_1}}$, and both displayed character involutions belong to $K$ by @prop:coble-level-two-plane-parabolic. Thus the equality for $K_0$ implies $\rho_n(K)=\rho_n(\Gamma(2))$ for every $n$, as claimed.
:::

::: {.proposition #prop:coble-fifty-six-contains-all-normal-relations title="All 19 exact infinite-kernel normal generators are short words in the 56 ordinary candidates"}

Let $K=\generators{S}$ be the ordinary subgroup generated by the 56 integral matrices of @prop:coble-ordinary-fifty-six-congruence-generators. Then **every one of the 19 normal generators of the full infinite Eichler kernel $E(2)$** from @thm:coble-eichler-full-normal-generation belongs to $K$, with an explicit ordinary word in $S^{\pm1}$ of length **at most four**. Consequently
$$
\langle\!\langle K\cap E(2)\rangle\!\rangle_E=E(2),
\qquad
\langle\!\langle K\rangle\!\rangle_{\Orth(B)}=\Gamma(2).
$$
Here double brackets denote **normal closure** in the indicated ambient group. This proposition proves the normal-closure equality; the **ordinary subgroup equality** is established separately in @thm:coble-fifty-six-ordinary-full-kernel-generation by the spin-cover congruence subgroup property.
:::

::: {.proof}
The reproducible exact certificate `coble_kernel_fifty_six_normal_relation_words.json` gives, for each of the 18 Eichler squares $g_i^2$ and the root-pair relation $g_7g_8$, a word of length at most four in the 56 ordinary matrices and their inverses. Its generator script `coble_kernel_fifty_six_normal_relation_words.py` multiplies both sides as **exact integral 11-by-11 matrices** and checks equality for all 19 relations. The certificate is source-hashed against both the ambient 21-generator artifact and the 56-generator artifact, and byte-identical regeneration is independently checked by `test_coble_fifty_six_contains_all_nineteen_eichler_normal_relations`.

Thus $K\cap E(2)$ contains the 19 normal generators. Their normal closure in $E$ is exactly $E(2)$ by @thm:coble-eichler-full-normal-generation, proving the first equality. The full $\Gamma(2)$ is generated by $E(2)$ and the two character involutions $r_{d_1}$ and $-\id_{U_1}$ by @cor:coble-level-two-kernel-split-extension; both involutions lie in $K_P\subset K$. Since $\Gamma(2)$ is normal in $\Orth(B)$ and contains $K$, the second equality follows.
:::

::: {.theorem #thm:coble-fifty-six-ordinary-full-kernel-generation title="Fifty-six explicit ordinary integral generators of the full Coble level-two kernel"}

Let $B=I_{2,9}$, $T_\Co=B(2)$, and let $S$ be the **56 exact integral matrices** in the source-hashed certificate `computations/reports/coble_kernel_fifty_six_congruence_generators.json`. Then
$$
\boxed{\Gamma(2)=\ker\bigl(\Orth(T_\Co)\longrightarrow\Orth(A_{T_\Co})\bigr)
=\generators{S}.}
$$
The equality is one of **abstract infinite integral arithmetic groups (@def:arithmetic-group)**. Every matrix in $S$ is an actual integral isometry acting trivially on the discriminant group, as verified by `test_coble_fifty_six_ordinary_elements_are_public_kernel_morphisms`. Moreover **56 is the minimal possible number of ordinary generators**, since $\Gamma(2)/\Gamma(4)\cong(\ZZ/2)^{56}$. This is the complete ordinary generator family required by the public Sage stable-orthogonal-group API and the lattice-database `arithmetic-group.otilde-t-co.generator_morphisms` field.
:::

::: {.proof}
Put $E_2=E(2)$ and $K=\generators{S}\subset\Gamma(2)$. By @thm:coble-fifty-six-ordinary-generators-finite-index, $K$ has finite index in $\Gamma(2)$. By @thm:coble-fifty-six-full-congruence-density, $K$ has **exactly the same image as $\Gamma(2)$ modulo every positive integer**. We prove that a finite-index subgroup with these properties is the entire group in this case, using the simply connected spin cover and the congruence subgroup property; no assumption that $K$ is already normal is made.

Let $G=\operatorname{Spin}(B_\QQ)$, with its rational central isogeny $\pi:G\to\mathrm{SO}(B_\QQ)$ of kernel $\{\pm1\}$. Write $\widetilde E_2=\pi^{-1}(E_2)$ and $\widetilde K_0=\pi^{-1}(K\cap E_2)$ as arithmetic subgroups (@def:hsd-arithmetic-subgroup) of $G(\QQ)$. The group $G$ is absolutely simple and simply connected of type $B_5$, with rational rank $2$. **Strong approximation** for simply connected rationally isotropic groups implies that the congruence closure of $\widetilde E_2$ in $G(\mathbb A_f)$ is a product $\prod_p G_p$ of compact open local groups. For every odd prime $p$, $G_p$ is the hyperspecial integral group $\operatorname{Spin}(B\otimes\ZZ_p)$; at $p=2$, $G_2$ is the inverse image of the principal level-two orthogonal subgroup under $\pi$. The latter is a **pro-$2$ group**, because its orthogonal image consists of matrices congruent to the identity modulo two and its central kernel has order two.

The congruence-density theorem @thm:coble-fifty-six-full-congruence-density also gives $\rho_n(K\cap E_2)=\rho_n(E_2)$ for **every** $n$, as established in its proof. Therefore the projections of the congruence closure of $\widetilde K_0$ to the local orthogonal groups $\pi(G_p)$ are surjective. Since $\widetilde K_0$ contains the global central kernel $\{\pm1\}$, its projection to **each** $G_p$ is surjective: two local spin lifts of the same orthogonal element differ only by $\pm1$. Thus $\overline{\widetilde K_0}$ is a closed subdirect subgroup of $\prod_p G_p$.

For odd $p$, $G_p$ is **topologically perfect**. Indeed, its reduction modulo $p$ is the perfect finite simply connected Chevalley group $\operatorname{Spin}_{11}(\F_p)$. Each successive principal $p$-adic congruence quotient is the additive Lie algebra $\mathfrak{so}_{11}(\F_p)$, on which the finite Chevalley group has no nonzero coinvariants. For $p=3,5,7,11,13$, the exact source-hashed audit `coble_kernel_fifty_six_small_odd_local.py` verifies the rank-55 commutator condition directly; for $p\ge17$ it follows from the irreducibility of the adjoint module proved in @thm:coble-fifty-six-all-odd-prime-powers. Induction on the congruence level shows every finite quotient $G_p/\ker(G_p\to G(\ZZ/p^k))$ is perfect, hence $G_p$ is topologically perfect.

Moreover, any nontrivial finite quotient of $G_p$ for odd $p$ has the nonabelian simple group $\Omega_{11}(\F_p)$ as a composition factor: all remaining composition factors come from the pro-$p$ congruence kernel. For distinct odd primes $p\ne q$, these simple groups have different orders, so $G_p$ and $G_q$ have **no common nontrivial finite quotient**. The pro-$2$ group $G_2$ has no common nontrivial finite quotient with any perfect $G_p$. By the profinite form of **Goursat's lemma**, a closed subdirect subgroup of a finite product of these groups must be the full product; applying this to every finite set of primes and using compactness gives
$$
\overline{\widetilde K_0}=\prod_p G_p=\overline{\widetilde E_2}.
$$
Thus $\widetilde K_0$ is **congruence-dense in the simply connected spin arithmetic group** $\widetilde E_2$.

Finally, the **congruence subgroup property with trivial congruence kernel** holds for $G=\operatorname{Spin}(2,9)$ over $\QQ$ with $S=\{\infty\}$. The Kneser--Raghunathan centrality theorem applies to this rationally isotropic spin group of dimension eleven. The **Margulis--Platonov hypothesis** in [Prasad--Rapinchuk, *Developments on the congruence subgroup problem*, Theorem 2(1)](https://www.mathi.uni-heidelberg.de/~wienhard/retreat10/references/prasad_rapinchuk_CSP.pdf) is also satisfied: $G$ has positive rational rank, and the Kneser--Tits theorem over global fields (proved by Gille, as recalled in the same source (@def:globular-boundary), §3.5) implies the Margulis--Platonov property for rationally isotropic simply connected groups. With **both** centrality and Margulis--Platonov established, their Theorem 2 identifies the congruence kernel with the Pontryagin dual of the metaplectic kernel. Their Theorem 3 makes the latter trivial when $S$ contains a real place where $G(\RR)$ is not topologically simply connected. This condition holds here: the maximal (@def:maximal-lattice) compact subgroup of $\operatorname{Spin}(2,9)(\RR)$ has a circle factor from $\operatorname{Spin}(2)$, so its fundamental group is infinite. Consequently **every finite-index subgroup of $\widetilde E_2$ is congruence-open**. Since $\widetilde K_0$ has finite index but is congruence-dense, it must equal $\widetilde E_2$. Projecting through $\pi$ yields $K\cap E_2=E_2$.

By @cor:coble-level-two-kernel-split-extension, $\Gamma(2)=E_2\rtimes\generators{r_{d_1},-\id_{U_1}}$. Both character involutions occur among the 26 plane-parabolic generators contained in $S$. Hence $K$ contains $E_2$ and the two complementary generators, proving $K=\Gamma(2)$. The minimality assertion follows from the exact 56-dimensional level-four quotient.
:::

::: {.theorem #thm:coble-positive-kernel-ninety-five-generators title="Ninety-five explicit ordinary generators of the positive Coble discriminant kernel"}

The subgroup $\widetilde O^+(T_\Co)=\Gamma(2)\cap\ker(\operatorname{sn}_{\mathbb R})$ is generated **as an ordinary infinite integral group** by the **95 exact integral matrices** in the source-hashed certificate `computations/reports/coble_kernel_positive_schreier_generators.json`. They are obtained by an index-two Reidemeister--Schreier construction from the 56 ordinary generators of @thm:coble-fifty-six-ordinary-full-kernel-generation; no cosets of the enormous discriminant image are enumerated.
:::

::: {.proof}
Work in the diagonal (@def:polarization-functors) realization $B\cong\generators1^2\perp\generators{-1}^9$, and let $A_g$ be the upper-left $2\times2$ block of $g$. Since $g$ preserves the form of signature $(2,9)$, the positive-plane projection $A_g$ is invertible. The sign $\chi(g)=\operatorname{sgn}\det A_g$ is the orientation (@def:free-module-orientation) character of the maximal (@def:maximal-lattice) positive two-plane. By Cartan--Dieudonné it suffices to compare $\chi$ and the real spinor character on reflections. Reflection in a positive-norm vector reverses this orientation and has real spinor norm $-1$ for the Gritsenko--Hulek--Sankaran multiplier $-\tfrac12$; reflection in a negative-norm vector preserves it and has real spinor norm $+1$. Thus $\chi=\operatorname{sn}_{\mathbb R}$ on $O(B)$.

Let $S=\generators{s_1,\ldots,s_{56}}$ be the certified ordinary generating family (@def:generating-frame) of $\Gamma(2)$, and choose one $t\in S$ with $\chi(t)=-1$. The two right cosets of $\ker\chi$ have representatives $1,t$. The Reidemeister--Schreier theorem gives an ordinary generating family consisting of the elements $r s_i\,\overline{r s_i}^{-1}$, for $r\in\{1,t\}$, where the bar denotes the chosen right-coset representative. The reproducible Sage script `computations/reports/coble_kernel_positive_schreier_generators.py` constructs all 112 candidates as exact integral matrices, checks their Gram identities, reduction modulo two and positive-plane character, and removes identities and repeated matrices, leaving **95**. The source (@def:globular-boundary) SHA-256 and exact matrix list are retained in the accompanying JSON. The public regression `test_coble_positive_schreier_generators_are_public_positive_kernel_morphisms` verifies that every matrix is an actual member of the maintained $\widetilde O^+(T_\Co)$ predicate. Since $S$ generates $\Gamma(2)$ by @thm:coble-fifty-six-ordinary-full-kernel-generation, Reidemeister--Schreier proves that the 95 matrices generate its positive real-spinor kernel, as claimed.
:::

::: {.proposition #prop:coble-positive-fifty-five-congruence-basis title="A sharp 55-element positive-kernel congruence basis"}

The first **55** matrices in the certified 95-element positive Schreier family of @thm:coble-positive-kernel-ninety-five-generators are linearly independent modulo four. Their ordinary subgroup has the **full image of $\widetilde O^+(T_\Co)$ modulo sixteen**, with exact successive congruence ranks $(55,54,55)$ at levels two, four, and eight. They are recorded, with source (@def:globular-boundary) SHA-256, in `computations/reports/coble_positive_kernel_fifty_five_generators.json`.

The number 55 is the **sharp lower bound** on the number of ordinary generators of the infinite positive kernel, since its quotient modulo four is $(\ZZ/2)^{55}$. This proposition establishes finite congruence generation; the separate arithmeticity and congruence-subgroup proof of **full infinite ordinary generation** is given later in this section.
:::

::: {.proof}
The source-hashed generator script selects independent leading matrices $(g-I)/2\pmod2$ from the 95 exact Schreier matrices; exact binary elimination selects precisely indices $0,\ldots,54$ and gives rank 55. The regression `test_coble_fifty_five_positive_elements_span_kernel_modulo_sixteen` constructs their ordinary subgroup using exact matrix products, squares and commutators modulo sixteen (without taking ambient normal closures). Its successive subgroup-collection ranks are $(55,54,55)$. The corresponding full positive-kernel ranks are 55 at level two (the real-spinor character removes one of the 56 full-kernel directions), 54 at level four by @prop:coble-eichler-level-eight-derived-image, and 55 at level eight by @thm:coble-eichler-exact-deep-congruence-ranks. Equality of all three ranks proves the stated finite congruence generation. The quotient of rank 55 proves the generator lower bound.
:::

::: {.theorem #thm:coble-positive-fifty-five-finite-index title="The 55-element positive kernel family has finite index"}

Let $S_{55}$ be the first 55 exact matrices in the positive Schreier certificate, as in @prop:coble-positive-fifty-five-congruence-basis. Then their **ordinary subgroup**
$$
K_{55}=\generators{S_{55}}\le\widetilde O^+(T_\Co)
$$
has **finite index** in the infinite positive kernel, and has full image in the positive kernel modulo $2^k$ for every $k\ge1$. In particular, the smallest possible number of ordinary generators already suffices to generate a finite-index, $2$-adically dense subgroup. Equality with the entire positive kernel is not asserted here.
:::

::: {.proof}
By @prop:coble-positive-fifty-five-congruence-basis, the 55 ordinary generators fill the successive graded congruence layers of ranks $(55,54,55)$ through modulus sixteen. The 55 independent level-eight lifts obtained by subgroup collection remain independent at every higher $2$-power level under repeated squaring, by the formula of @thm:coble-eichler-exact-deep-congruence-ranks. This proves full $2$-adic congruence images. Consequently $K_{55}$ is Zariski dense in the connected rational orthogonal group, since its $2$-adic closure contains an open subgroup.

The source-hashed Schreier construction `coble_kernel_positive_schreier_generators.py` orders the first 55 matrices as the positive members of the original 56-element family. Its unique omitted original generator is index 3, the determinant-negative Levi matrix $\operatorname{diag}(-1,1)$ on the fixed integral isotropic plane. All the other 25 generators of the integral level-two plane stabilizer (@def:group-orbit) are retained. In particular, the **14 Eichler transvections and central unipotent generator** at original indices 11 through 25 are all in $K_{55}$; these generate a finite-index subgroup of the integral unipotent radical of the maximal (@def:maximal-lattice) rational parabolic (@def:hsd-parabolic-subgroup) stabilizing the plane, by @prop:coble-level-two-plane-parabolic. The Raghunathan--Venkataramana arithmeticity criterion quoted and applied through the simply connected spin cover in @thm:coble-fifty-six-ordinary-generators-finite-index therefore applies equally to $K_{55}$ and proves it has finite index in the positive arithmetic group (@def:arithmetic-group).
:::

::: {.theorem #thm:coble-positive-fifty-five-full-generation title="Exactly 55 ordinary generators of the full positive Coble kernel"}

Let $S_{55}$ be the **55 exact integral matrices** in the source-hashed certificate `computations/reports/coble_positive_kernel_fifty_five_generators.json`. Then
$$
\boxed{\widetilde O^+(T_\Co)=\generators{S_{55}}.}
$$
This is equality of **infinite integral arithmetic groups (@def:arithmetic-group)**, not merely of finite congruence images. The number **55 is minimal**, since $\widetilde O^+(T_\Co)$ has an elementary abelian quotient of rank 55 modulo four. Consequently the 95-element Reidemeister--Schreier family of @thm:coble-positive-kernel-ninety-five-generators can be replaced by this provably minimal ordinary generating family (@def:generating-frame) in the public arithmetic-group API and the lattice-database card.
:::

::: {.proof}
Write $K=\generators{S_{55}}$, $E_2=E(2)$ and $\Gamma^+=\widetilde O^+(T_\Co)=E_2\rtimes\generators{r}$, where $r$ is a negative-root reflection with determinant $-1$ and real-spinor sign $+1$. The first 55 Schreier generators include the negative-root reflection from the original plane-parabolic generator at index 4, so $K$ contains such an $r$. Put $K_0=K\cap E_2$.

**The exact odd-prime calculation.** The 55 matrices contain **47 unipotent isometries** of nilpotency degree (@def:graded-object) at most three. Their integral logarithms, transported to the odd diagonal (@def:polarization-functors) basis, generate under Lie brackets a full-rank sublattice of $\mathfrak{so}_{11}(\ZZ)$ of **index $2^{63}$**, by the exact source-hashed audit `coble_positive_fifty_five_odd_local.py`. In particular the logarithms generate the entire Lie algebra modulo every odd prime. For $p=3,5,7,11,13$, the same audit independently applies GAP's `RecogniseClassical` to the 55 reductions, certifies that the generated finite group contains $\Omega_{11}(\F_p)$, and proves that the $p$-th powers of the 47 unipotents and their conjugates span the full 55-dimensional first $p$-adic congruence layer. For $p\ge17$, the full integral Lie span and the finite-characteristic recognition argument of @thm:coble-fifty-six-all-odd-prime-powers apply verbatim: the 47 unipotents have order $p$, their logarithms generate $\mathfrak{so}_{11}(\F_p)$, the natural module is absolutely irreducible, and Guralnick's theorem identifies the finite group generated by these $p$-elements with $\Omega_{11}(\F_p)$. Its adjoint action generates the full first congruence layer; iterated $p$-th powers generate all higher layers. All 47 unipotents lie in $E_2$ (unipotents have determinant and rational spinor norm one), so
$$
\rho_{p^k}(K_0)=\rho_{p^k}(E_2)
\qquad(p\text{ odd},\ k\ge1).
$$

**The two-adic calculation.** The exact ordinary subgroup-collection test `test_coble_fifty_five_positive_elements_span_kernel_modulo_sixteen` proves that $K$ has full graded ranks $(55,54,55)$ through modulus sixteen. By @thm:coble-eichler-exact-deep-congruence-ranks, repeated squaring of the 55 level-eight witnesses gives full image at every deeper $2$-power. Since $K$ contains $r$ and the character $\Gamma^+/E_2\cong\ZZ/2$ is already detected modulo four, $K_0$ has the full image of $E_2$ modulo every $2^k$.

**Mixed moduli and equality.** The odd-prime local groups $\rho_{p^k}(E_2)$ are perfect, as proved in @thm:coble-fifty-six-full-congruence-density. The $2$-adic congruence image of $E_2$ is a finite $2$-group. These groups have no common nontrivial quotient, so Goursat's lemma and the Chinese remainder theorem combine the prime-power equalities into
$$
\rho_n(K_0)=\rho_n(E_2)\quad\text{for every }n\ge1.
$$
By @thm:coble-positive-fifty-five-finite-index, $K_0$ has finite index in $E_2$. The simply connected spin-cover argument and the **trivial congruence kernel** proved in @thm:coble-fifty-six-ordinary-full-kernel-generation now apply without alteration: the lift of $K_0$ is finite-index and congruence-dense in the arithmetic spin cover, so it equals the lift of $E_2$. Hence $K_0=E_2$. Since $r\in K$, we conclude $K=\Gamma^+$.

The rank-55 quotient of @prop:coble-positive-fifty-five-congruence-basis proves that no smaller ordinary generating family exists.
:::

::: {.proposition #prop:coble-level-two-plane-parabolic title="Generators of the level-two kernel in the integral plane stabilizer"}

In the notation of @thm:coble-plane-stabilizer-image, let $K_P=\Stab_{\Orth(B)}(P)\cap\ker\rho$. The following $26$ integral isometries generate $K_P$:

1. the Levi extensions of $-I_2$, $\begin{psmallmatrix}1&2\\0&1\end{psmallmatrix}$, $\begin{psmallmatrix}1&0\\2&1\end{psmallmatrix}$ and $\operatorname{diag}(-1,1)$ in $GL(P)$;
2. the seven sign reflections $r_{d_j}$ in the norm-$-1$ vectors $d_j$;
3. the fourteen Eichler transvections $E_{e_i,2d_j}$, for $i=1,2$ and $j=1,\dots,7$;
4. the square $E_{e_1,e_2}^{,2}$ of the central shear.

The exact matrices in the standard basis, their Gram preservation, plane preservation and triviality modulo $2$ are recorded in `computations/reports/coble_plane_parabolic_level_two_generators.json`, regenerated by the adjacent Sage script. The $26$ matrices are **a minimal generating family (@def:generating-frame)** for $K_P$. This is a generating family for the *plane stabilizer (@def:group-orbit) inside* $\ker\rho$, not a generating family for the full discriminant kernel (@def:mm-integral-spinor-data) $\ker\rho$.
:::

::: {.proof}
The splitting $\Stab_{\Orth(B)}(P)= (GL_2(\ZZ)\times\Orth(D))\ltimes U$ of @thm:coble-plane-stabilizer-image(1) is integral. The reductions of the three factors form the Levi image $GL_2(\F_2)\times S_7$ and the unipotent image of order $2^{13}$, with trivial intersection of the Levi and unipotent images, by parts (2) and (3) of that theorem. Thus an element is trivial modulo $2$ precisely when its Levi components and its unipotent component are each trivial modulo $2$.

The kernel of $GL_2(\ZZ)\to GL_2(\F_2)$ is generated by the four matrices in (1): the kernel in $SL_2(\ZZ)$ is generated by $-I_2$ and the two elementary matrices with off-diagonal entry $2$ (the Reidemeister–Schreier calculation for $PSL_2(\ZZ)=C_2*C_3\to PSL_2(\F_2)\cong S_3$), and adjoining $\operatorname{diag}(-1,1)$ gives the determinant-$-1$ component. Since $\Orth(D)=(\ZZ/2)^7\rtimes S_7$ and reduction forgets exactly the signs, its kernel is generated by the seven reflections in (2).

Finally, $U$ is generated by $E_{e_i,w_i}$ for $w_i\in D^{\mathrm{ev}}$ and the central shear, as proved in @thm:coble-plane-stabilizer-image(1). Its finite image records the two classes $w_i\bmod 2D$ in $D^{\mathrm{ev}}/2D\cong\F_2^6$ and the central shear parameter modulo $2$; this follows from the explicit reduction formulas in part (2), whose independent $V_6$ blocks and central block have orders $2^{12}$ and $2$, respectively. Consequently its kernel consists of the elements with $w_i\in2D$ and even central parameter. The fourteen transvections in (3) generate the two copies of $2D$, and (4) generates the remaining central subgroup. The semidirect factorization then proves generation of all of $K_P$.

For minimality, the map $g\mapsto(g-I)/2\bmod2$ is a homomorphism from $K_P$ to the additive group of $11\times11$ matrices over $\F_2$, since $(I+2A)(I+2B)\equiv I+2(A+B)\pmod4$. The $26$ displayed matrices have linearly independent images under this map: the exact binary rank is $26$, checked independently by the certificate producer and the regression's bitwise elimination. Thus every generating family of $K_P$ contains at least $26$ elements, and the family above attains this bound.
:::

::: {.corollary #cor:coble-level-four-normal-span title="The plane kernel normally generates the full level-two image modulo four"}

Let $\Gamma(2)=\ker(\Orth(B)\to GL(B/2B))$, let $\Gamma(4)=\ker(\Orth(B)\to GL(B/4B))$, and let $N$ be the normal closure of $K_P$ in $\Orth(B)$. Then
$$
\Gamma(2)/\Gamma(4)\cong(\ZZ/2)^{56},\qquad N\Gamma(4)=\Gamma(2).
$$
This is a statement about the reduction modulo $4$, **not** an assertion that $N=\Gamma(2)$.
:::

::: {.proof}
Use the integral diagonal (@def:polarization-functors) model $B\cong\generators{1}^{2}\perp\generators{-1}^{9}$, with Gram matrix $G=\operatorname{diag}(\varepsilon_i)$, $\varepsilon_i=\pm1$. For $g=I+2A\in\Gamma(2)$, the identity $g^tGg=G$ modulo $4$ implies that $\bar A=A\bmod2$ is symmetric. The diagonal identities modulo $8$, divided by $4$ and reduced modulo $2$, give
$$
\sum_{j\ne i}\bar A_{ji}=0\qquad(1\le i\le11).
$$
Indeed, the diagonal contribution is $A_{ii}+A_{ii}^2\equiv0\pmod2$ and every sign $\varepsilon_j$ reduces to $1$. These are the vertex-incidence equations of the complete graph on eleven vertices for the off-diagonal entries of a symmetric matrix. They have rank ten over $\F_2$: the sum of the eleven equations vanishes, and deleting any one equation leaves ten independent equations (use the ten edges incident to the deleted vertex). The space of possible $\bar A$ therefore has dimension at most $11\cdot12/2-10=56$.

The $26$ matrices of @prop:coble-level-two-plane-parabolic are in $\Gamma(2)$. Conjugating their images $\bar A$ by the reductions of the ten integral root reflections in `coble_singular_integral_representatives.json` and taking their binary linear span gives rank **56**. The source-hashed exact calculation in `coble_plane_parabolic_level_two_generators.py` starts from the 26 matrices, closes their span under each of the ten conjugations, and terminates with this rank; the regression independently checks the rank. In fact **one conjugation suffices**: the certificate explicitly lists 56 independent integral matrices, each one of the original 26 or its conjugate by a single one of the ten root reflections. Their exact standard-basis entries, source generator indices and conjugating reflection words are retained in `coble_plane_parabolic_level_two_generators.json` and reconstructed independently by the regression. These 56 images form a *minimal generating family (@def:generating-frame) of the finite quotient* $\Gamma(2)/\Gamma(4)$. Every vector obtained is an image of an actual element of $N$, since $g\mapsto(g-I)/2\bmod2$ is a homomorphism on $\Gamma(2)$. Thus $N$ already has the maximum possible image of dimension 56, and the same is true of $\Gamma(2)$. Its kernel is exactly $\Gamma(4)$, proving both assertions.
:::

::: {.proposition #prop:stabilizers-conjugate title="The stabilizers of the polarized $0$-cusps are conjugate"}

Let $T_\Co = B(2)$ and let $\widetilde\Orth^+(T_\Co) = \Orth^+(T_\Co)\intersect\ker\rho_{T_\Co}$ be the stable subgroup (@conv:stable-subgroup), and let $v, v'\in T_\Co$ be primitive isotropic vectors (@def:isotropic-subspace) with $v' = gv$ for some $g\in\Orth(T_\Co)$, which exists by @thm:unpolarized-cusps.
Then

1. $\widetilde\Orth^+(T_\Co)$ is normal in $\Orth(T_\Co)$, and $\Stab_{\widetilde\Orth^+(T_\Co)}(v') = g\,\Stab_{\widetilde\Orth^+(T_\Co)}(v)\,g^{-1}$;

2. the subgroups of $\Orth(v^{\perp T_\Co}/\generators{v})$ and of $\Orth((v')^{\perp T_\Co}/\generators{v'})$ induced by those stabilizers (@def:group-orbit) are mapped onto one another by the isometry $\bar g$ that $g$ induces on the quotients;

3. consequently the subgroups $G\leq\Orth(\latI_{1,8}(2))$ induced by those stabilizers at the polarized $0$-cusps are conjugate, and they have equal index.
:::

::: {#rmk:normality-fails-enriques-side .remark title="The normality this uses fails on the Enriques side"}

Step 3 uses that $\widetilde\Orth^+(T_\Co)$ is normal in $\Orth(T_\Co)$, so that the stabilizers at two cusps are conjugate in $\Orth(T_\Co)$ and the induced subgroups are carried onto one another. Nothing of the kind holds for $\gent\subset\Orth(T_\En)$, which is a level-two subgroup and not normal: the four divisibility-two Enriques cusps lie in four different $\gent$-orbits, and the class stabilizers inside $M$ have orders $348\,364\,800$, $5\,806\,080$, $2\,580\,480$ and $5\,160\,960$ at cusps $2,3,4,5$ respectively (@thm:sterk-reflection-subgroups). The unit of that theorem is the $\gent$-orbit of a $0$-cusp, not the isometry class of the quotient, which is why the four published Enriques diagrams can differ while their quotient lattices coincide.
:::

::: {.proof}

(1) By @conv:spinor-positive-subgroup and @def:discriminant-rep, $\widetilde\Orth^+(T_\Co) = \ker\rho_{T_\Co}\cap\ker\spinornorm_\bR$ inside $\Orth(T_\Co)$, so it is the intersection of two kernels and therefore normal.
For $h\in\Stab_{\widetilde\Orth^+(T_\Co)}(v)$ and $g$ as in the statement, $ghg^{-1}(v') = ghv = gv = v'$, and $ghg^{-1}\in\widetilde\Orth^+(T_\Co)$ by normality; so $g\Stab_{\widetilde\Orth^+(T_\Co)}(v)g^{-1}\subseteq\Stab_{\widetilde\Orth^+(T_\Co)}(v')$, and the reverse inclusion follows by applying the same argument to $g^{-1}$, or by counting cosets of the same index.

(2) An isometry fixing $v$ preserves $v^{\perp}$ and $\generators{v}$, hence descends to the quotient, and the resulting map $g\mapsto\bar g$ is a homomorphism of stabilizers; conjugating on $T_\Co$ becomes conjugating by $\bar g$ on the quotient.
So the image of $\Stab_{\widetilde\Orth^+(T_\Co)}(v')$ is $\bar g\,\rho_v(\Stab_{\widetilde\Orth^+(T_\Co)}(v))\,\bar g^{-1}$, and $\bar g$ is an isometry of the two cusp lattices.

(3) By @prop:zero-cusp-lattices the quotient is $\latI_{1,8}(2)$ for every such $v$, so (2) exhibits the images as conjugate inside one isometry group, and conjugate subgroups have equal index.
:::

::: {.theorem #thm:plane-half-index title="The subgroup $G^+$ of the cusp lattice, and $c = 1$"}

Let $v$ be a primitive isotropic vector (@def:isotropic-subspace) of $T_\Co$, $S = \Stab_{\Orth(T_\Co)}(v)$, $K = v^{\perp T_\Co}/\generators{v}\cong\I_{1,8}(2)$, $\pi: S\to\Orth(K)$, $W\leq S$ generated by the nine wall reflections of the $K$-chamber, and
$$
G \definedas \pi(\ker\rho_{T_\Co}\cap S),\qquad G^+ \definedas \pi\left(\ker\rho_{T_\Co}\cap S\cap\Orth^+(T_\Co)\right) = G\cap\Orth^+(K),\qquad c \definedas \abs{\rho(W)\cap\rho(\ker\pi)} .
$$
Then

1. $\ker\pi = \set{E_B(e_1,w) : w\in\I_{1,8}^{\mathrm{ev}}}$, the transvections in the even sublattice, and $\rho(\ker\pi)\cong\I_{1,8}^{\mathrm{ev}}/2\I_{1,8}$ has order $256$;

2. $\abs{\rho(W)} = 348\,364\,800$, $\abs{\rho(S)} = \abs{\langle\rho(W),\rho(\ker\pi)\rangle} = 89\,181\,388\,800 = \abs{\Stab_{\Orth(q_{T_\Co})}([e_1/2])}$, hence $c = 1$;

3. $-\id_K$ lies in $G$ and not in $\Orth^+(K)$, so
$$
\left[\Orth^+(K) : G^+\right] = \left[\Orth(K) : G\right] = \frac{\abs{\rho(W)}}{c} = 348\,364\,800,
\qquad
\left[\Orth(K) : G^+\right] = 696\,729\,600 ;
$$

4. the element $\id_{U_1}\oplus(-\id_K)$ lies in $\ker\rho_{T_\Co}$ and outside $\Orth^+(T_\Co)$, so the $\widetilde\Orth(T_\Co)$-orbit of $e_1$ is a single $\widetilde\Orth^+(T_\Co)$-orbit, and the index
$$
\frac{\abs{\Orth(q)}}{\abs{\rho(S)}} = \frac{46\,998\,591\,897\,600}{89\,181\,388\,800} = 527 = 527\,c
$$
is the count of @thm:coble-zero-cusp-count(2): the orbit (@def:group-orbit) of $e_1$ is the one over $[e_1/2]$, and $c = 1$ is the index-one fibre of that theorem read from the cusp lattice.
:::

::: {.proof}

Coordinates as above: $B = U_1\oplus U_2\oplus\generators{-1}^{7}$, $v = e_1$, $K = U_2\oplus\generators{-1}^{7}$ with the $\I_{1,8}$-adapted basis $v_0 = e+f+g_1$, $v_1 = e+g_1$, $v_2 = f+g_1$, $v_3,\dots,v_8 = g_2,\dots,g_7$; the nine walls of @thm:zero-cusp-chambers substituted through that dictionary have exactly the printed chamber Gram matrix.

(1) An element of $\Orth(B)$ fixing $e_1$ and acting trivially on $K$ sends $f_1\mapsto f_1+\alpha e_1+w$ with $w\in\I_{1,8}$, and integrality of its norm forces $\alpha = -w^2/2$; such elements exist exactly for $w^2$ even and are the transvections
$$
E_B(e_1,w)(x) = x - \beta_B(w,x)e_1 + x_1w - \tfrac{w^2}{2}x_1e_1 ,
$$
where $x_1 = \beta_B(x,e_1)$.
Modulo $2$ this is $x\mapsto x + \overline{\beta_B(w,x)}\,\overline{e_1} + x_1\overline{w} + \overline{\tfrac{w^2}{2}}\,x_1\overline{e_1}$: the $\tfrac{w^2}{2}$ term sits on $\overline{e_1}$ and not on $\overline{w}$, and the parity condition on $w$ is what keeps $\alpha$ integral; for odd $w^2$ the formula does not preserve $q$.
The map $w\mapsto\rho(E_B(e_1,w))$ is a homomorphism on $\I_{1,8}^{\mathrm{ev}}$, and by the proof of @lem:cusp-vector-stabilizer-image(1) its kernel is $\I_{1,8}^{\mathrm{ev}}\cap(\ZZ e_1+2B) = 2\I_{1,8}$. Since $\I_{1,8}^{\mathrm{ev}}$ has index $2$ in $\I_{1,8}$, the image has order $2^9/2 = 256$.

(2) Every isometry of $K$ extends by $\id_{U_1}$ to an element of $S$, so $\pi$ is split and $S = \Orth(K)\cdot\ker\pi$.
By [@Vin72, Table 5], $\Orth^+(\I_{1,8})$ is the reflection group (@def:reflection-group) of the chamber, whose diagram has no symmetry; so $\Orth(K) = \set{\pm1}\times W$ and $S = \langle W,\ \id_{U_1}\oplus(-\id_K),\ \ker\pi\rangle$.
The element $\id_{U_1}\oplus(-\id_K)$ is the identity modulo $2B$, so $\rho$ kills it, and $\rho(S) = \rho(W)\cdot\rho(\ker\pi)$, with $\rho(\ker\pi)$ normal because $\ker\pi$ is normal in $S$.
By @lem:cusp-vector-stabilizer-image(1), @lem:isotropic-classes-lift(2) and @prop:coble-discriminant-group, $\abs{\rho(S)} = \abs{\Stab_{\Orth(q)}([e_1/2])} = \abs{\Orth(q)}/527 = 89\,181\,388\,800$.
The group $\rho(W) = \rho(\Orth(K))$ acts trivially on $U_1/2U_1$, and on $K/2K$ it is the image of $\Orth(K)\to\Orth(q_{K(2)})$, which is onto by @thm:two-elementary-surjectivity; so $\abs{\rho(W)} = \abs{\Orth(q_{K(2)})} = \abs{\operatorname{GO}^+_8(2)} = 348\,364\,800$, as in the proof of @lem:cusp-vector-stabilizer-image(1).
Hence $c = \abs{\rho(W)}\cdot\abs{\rho(\ker\pi)}/\abs{\rho(S)} = 348\,364\,800\cdot256/89\,181\,388\,800 = 1$.

(3) The element $g = \id_{U_1}\oplus(-\id_K)$ fixes $e_1$, acts as $-1$ on $K$, is trivial on $A_{T_\Co}$ and so lies in $\ker\rho_{T_\Co}\cap S$; its image in $\Orth(K)$ is $-\id_K$, which is not in $\Orth^+(K)$ because $\I_{1,8}$ has positive index (@def:maximal-positive-definite-subspace) $1$ and $\spinornorm_\bR(-\id) = [(-1)^1] = -1$ (@lem:minus-identity-spinor-norm).
So $G = \set{\pm1}\cdot G^+$ as subgroups of $\Orth(K) = \set{\pm1}\times\Orth^+(K)$, and the two indices in (3) follow from (2).

(4) The element $g$ lies outside $\Orth^+(T_\Co)$, since it reverses the plane spanned by the positive directions of $U_1$ and of $K$, while it does lie in the discriminant kernel; hence the stabilizer (@def:group-orbit) in $\widetilde\Orth(T_\Co)$ of $e_1$ is not contained in $\widetilde\Orth^+(T_\Co)$ and the two groups have the same orbit on $e_1$.
The index $\abs{\Orth(q)}/\abs{\rho(S)}$ is the count of @thm:coble-zero-cusp-count(2), the $\ker\rho$-orbits inside the orbit of $e_1$ being in bijection with $\Orth(q)/\rho(S)$ by $\rho$ onto $\Orth(q)$ (@thm:two-elementary-surjectivity); so $c = 1$ says that the fibre over $[e_1/2]$ is one orbit, which is @lem:cusp-vector-stabilizer-image(1) again.
:::

::: {.theorem #thm:plane-fibre title="The plane fibre, the plane classes and the $1$-cusp count of the stable quotient"}

Let $P\subset B = U\perp U\perp \I_{0,7}$ be a primitive isotropic plane, $K_P = P^{\perp B}/P\iso\I_{0,7}$, $J = [P/2]\leq A_{T_\Co}$ the order-$4$ isotropic subgroup it spans, and $\widetilde\Orth^+(T_\Co)$ the stable subgroup, whose discriminant image is trivial.
Then

1. $\abs{\Stab_{\Orth(q_{T_\Co})}(J)} = 1\,981\,808\,640$ and $\abs{\rho(\Stab_{\Orth(B)}(P))} = 247\,726\,080$, so the plane fibre has index
$$
\bigl[\Stab_{\Orth(q_{T_\Co})}(J) : \rho(\Stab_{\Orth(B)}(P))\bigr] = 8 ;
$$

2. the isotropic subgroups of order $4$ of $A_{T_\Co}$ form the $\Orth(q_{T_\Co})$-orbit of $J$, of size $23\,715$, which the five $G_\Co$-orbits of @tbl-finite-plane-orbits, of sizes $1575, 270, 9450, 3780, 8640$, partition;

3. hence the stable quotient $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ has $23\,715\cdot 8 = 189\,720$ $1$-cusps, one fibre of eight over each liftable $J$: a page proof, and both of its rows are public computation records, returned for $\ker\rho$ and for $\widetilde\Orth^+(T_\Co)$ in run 43798731423 (@rmk:coble-plane-incidence-rows). The quotient $F^{\mathrm{un}}_\Co = \bD(T_\Co)/\Orth(T_\Co)$ has one $1$-cusp (@thm:plane-transitivity-tco), and its row is the $\Orth(T_\Co)$ row of the same operation, returned in run 43556671111. $R_{\gent}\intersect\Orth^+(T_\Co)$ has seven $1$-cusps: the seven plane orbits (@def:group-orbit) of @thm:coble-integral-lifting-fibre(4)(b), the same seven that the integral decorated-plane lifting and finite $G_\Co$-orbit calculation of @cor:coble-heegner-integral-plane-descent gives, independently reproduced by that run's public row (@rmk:coble-plane-incidence-rows); $F_{\Co,2}$ has the same seven exactly when @qst:coble-monodromy-equality holds (@prop:coble-cong-point-stabilizer(3) is the analogous $0$-cusp statement). The count for $\fco$ is that of the stable quotient if @conj:gamma-co-stable holds.
:::

::: {.proof}

$T_\Co = B(2)$ with $B$ unimodular, so $A_{T_\Co} = B/2B\cong\F_2^{11}$ with $q([x/2]) = B(x,x)/2\pmod{2\ZZ}$, and the discriminant action of $g\in\Orth(B)$ is $g\bmod 2$.

(1) By @prop:coble-planecusp-finite(3) and (4), $\abs{\Stab_{\Orth(q)}(J)} = \abs{\Orth(q)}/23\,715 = 1\,981\,808\,640$, and by @thm:coble-plane-stabilizer-image(3), $\abs{\rho(\Stab_{\Orth(B)}(P))} = 247\,726\,080$.
An integral isometry preserving $P$ maps the classes of $\tfrac12 e_1$ and $\tfrac12 e_2$ into $J$, so its reduction modulo $2$ stabilises $J$. Hence $\rho(\Stab_{\Orth(B)}(P))\subseteq\Stab_{\Orth(q)}(J)$, and the index is $1\,981\,808\,640/247\,726\,080 = 8$, which is $[S_8:S_7]$ by @thm:coble-plane-stabilizer-image(4).

(2) By @prop:coble-planecusp-finite(2), $\Orth(q)$ is transitive on the isotropic subgroups of order $4$, and by @prop:coble-planecusp-finite(3) they number $23\,715$. Their $G_\Co$-orbits are the five orbits of @ex:gco-finite-orbits, of the sizes listed in @tbl-finite-plane-orbits.

(3) By @thm:coble-plane-stabilizer-image(5), the $\widetilde\Orth^+(T_\Co)$-orbits of primitive isotropic planes over each of the $23\,715$ subgroups $J$ are eight in number.
:::

::: {.corollary #cor:coble-zero-one-cusp-incidence title="Incidence of the $0$-cusps and the plane classes"}
Let $\widetilde\Orth^+(T_\Co) = \widetilde\Orth^+(T_\Co)$. Each isotropic subgroup $J$ of order $4$ of $A_{T_\Co}$ contains exactly three of the $527$ nonzero isotropic classes, each of which is one $0$-cusp of $\widetilde\Orth^+(T_\Co)$, and each nonzero isotropic class lies in exactly $135$ of the $23\,715$ subgroups $J$.
:::

::: {.proof}
Write $J = [P/2]$ with $P = \langle e_1,e_2\rangle$ a primitive isotropic plane of $B$. By @prop:coble-planecusp-finite(1), the three nonzero elements of $J$ are the classes of $\tfrac12 e_1$, $\tfrac12 e_2$ and $\tfrac12(e_1+e_2)$, the classes of the primitive isotropic vectors (@def:isotropic-subspace) $e_1$, $e_2$, $e_1+e_2$ of $T_\Co$, each of divisibility $2$.
By @thm:coble-zero-cusp-count, parts 1 and 2, the primitive isotropic vectors of $T_\Co$ in one nonzero isotropic class form one $\widetilde\Orth^+(T_\Co)$-orbit, so each of the three classes is one $0$-cusp.
For a nonzero isotropic class $u$, the subgroups $J$ that contain $u$ are the subgroups $\langle u,v\rangle$ with $v$ isotropic in $u^\perp\setminus\langle u\rangle$. By @prop:coble-planecusp-finite(3) there are $270$ such $v$, and each subgroup contains two of them, so $u$ lies in $135$ subgroups. This agrees with the double count $23\,715\cdot3/527 = 135$.
:::


::: {.proposition #prop:coble-arithmetic-flag-incidence title="Line-in-plane flags over one isotropic subgroup of order $4$"}
Let $P=\langle e_1,e_2\rangle$ be the standard primitive isotropic plane of $B=U_1\perp U_2\perp D$, let $J=[P/2]$, and let $\widetilde\Orth^+(T_\Co)=\ker\rho\intersect\Orth^+(B)$.

1. The image of $\Stab_{\widetilde\Orth^+(T_\Co)}(P)$ in $GL(P)$ is
$$ \Gamma(P)\definedas\theset{A\in SL(P): A\equiv I_2\pmod2}. $$
2. Let $\mathcal P$ be one of the eight $\widetilde\Orth^+(T_\Co)$-orbits of primitive isotropic planes $P'$ with $J(P') = J$ (@thm:coble-plane-stabilizer-image(5)), and let $c\in J$ be nonzero. Then the flags $(P',L)$ with $P'\in\mathcal P$, $L\subset P'$ a primitive line and $[L/2]=c$ form one $\widetilde\Orth^+(T_\Co)$-orbit.

So the $\widetilde\Orth^+(T_\Co)$-orbits of flags $(P',L)$ with $J(P') = J$ are the $3\times8 = 24$ orbits (@def:group-orbit) of item 2, one for each pair of an orbit $\mathcal P$ and a nonzero class $c\in J$.
:::

::: {.proof}
(1) By @thm:coble-plane-stabilizer-image(1), $\Stab_{\Orth(B)}(P) = L\ltimes U$, and the Levi factor acts by $A$ on $P$, by $(A^{-1})^{T}$ on $P^*$ and by an arbitrary $\delta\in\Orth(D)$ on $D$. An element of $\ker\rho$ acts trivially on $J = P/2P$, so its image $A$ satisfies $A\equiv I_2\pmod2$.
The normalized real spinor norm of such an element is $\det A$. The unipotent group $U$ has connected real points, so it is spinor-positive. $D$ is negative definite, so $\Orth(D)$ is generated by reflections in negative vectors, which are spinor-positive. For $\det A = 1$, the element $A\oplus(A^{-1})^{T}$ lies in the image of the connected group $SL_2(\bR)$, so it is spinor-positive. For $\det A = -1$, write $A = A'\diag(-1,1)$ with $\det A' = 1$; the element $\diag(-1,1)\oplus\diag(-1,1)$ is $-\id_{U_1}\oplus\id_{U_2}$, of spinor norm $-1$ by @lem:minus-identity-spinor-norm.
So the image of $\Stab_{\widetilde\Orth^+(T_\Co)}(P)$ lies in $\Gamma(P)$. Conversely, for $A\in\Gamma(P)$ the element $A\oplus(A^{-1})^{T}\oplus\id_D$ is the identity modulo $2B$ and spinor-positive, so it lies in $\Stab_{\widetilde\Orth^+(T_\Co)}(P)$.

(2) First, $\Gamma(P)$ is transitive on the primitive lines of $P$ in each nonzero class of $J$. A primitive line of $P$ is $L_{(a,b)}=\ZZ(ae_1+be_2)$ with $\gcd(a,b)=1$, and its class is $(\bar a,\bar b)\in J\sm\{0\}$. By Bezout's identity, each primitive vector $v=(a,b)^T$ is the first column of a matrix $M_v=[v,z_v]\in SL_2(\ZZ)$. Let $w$ be another primitive vector with $w\equiv v\pmod 2$, and let $M_w=[w,z_w]\in SL_2(\ZZ)$. Write $c$ for the common reduction of $v$ and $w$. Then
$$ \det(c,z_w-z_v)=\det M_w+\det M_v=1+1=0\quad\text{in }\F_2. $$
The functional $x\mapsto\det(c,x)$ on $\F_2^2$ is nonzero with kernel $\langle c\rangle$, so $z_w-z_v\equiv t c\pmod 2$ for some $t\in\F_2$. Lift $t$ to an integer and replace the second column of $M_w$ by $z_w-t w$. The new $M_w$ has determinant one and $M_w\equiv M_v\pmod2$. So $A=M_wM_v^{-1}$ satisfies $A\equiv I_2\pmod2$ and $Av=w$, that is $A\in\Gamma(P)$ and $A(L_v) = L_w$.

Now fix $P_0\in\mathcal P$. By @thm:plane-transitivity-tco, $P_0 = k(P)$ for some $k\in\Orth(B)$. The group $\widetilde\Orth^+(T_\Co)$ is normal in $\Orth(B)$, so $\Stab_{\widetilde\Orth^+(T_\Co)}(P_0) = k\Stab_{\widetilde\Orth^+(T_\Co)}(P)k^{-1}$, and by (1) and the preceding paragraph it is transitive on the primitive lines $L\subset P_0$ with $[L/2]=c$. Let $(P_1,L_1)$ and $(P_2,L_2)$ be two flags with $P_i\in\mathcal P$ and $[L_i/2] = c$. An element of $\widetilde\Orth^+(T_\Co)$ moves $P_2$ to $P_1$; it lies in $\ker\rho$, so it preserves the class $c$, and it moves $L_2$ to a line of class $c$ in $P_1$. An element of $\Stab_{\widetilde\Orth^+(T_\Co)}(P_1)$ then moves that line to $L_1$.
:::

::: {.theorem #thm:coble-integral-lifting-fibre title="Integral cusps of a subgroup, and the fibre over one finite datum"}
Let $B=\latI_{2,9}$ and $T_\Co=B(2)$ [@DK13, (3.6)], so that $\Orth(T_\Co)=\Orth(B)$ and $A_{T_\Co}=B/2B$. Write $\rho=\rho_{T_\Co}\colon\Orth(T_\Co)\too\Orth(q)$ with $q=q_{T_\Co}$, $Q=\Orth(q)$, $K=\discriminantkernel{T_\Co}$ and $\widetilde\Orth^+(T_\Co)=K\intersect\Orth^+(T_\Co)$ (@thm:coble-zero-cusp-count). Let $\Gamma\leq\Orth(T_\Co)$ be a subgroup with $\widetilde\Orth^+(T_\Co)\iscontainedin\Gamma$, and
$$
H\definedas\rho(\Gamma)\leq Q
$$
its **discriminant image**.

An *object* is a primitive isotropic line $\ell\subset T_\Co$, a primitive isotropic plane $P\subset T_\Co$, or a flag $L\subset P$ of a primitive isotropic line in a primitive isotropic plane. Its *finite datum* is, respectively, the nonzero isotropic class $[\ell/2]\in A_{T_\Co}$ of @lem:isotropic-classes-lift, the pair $(J(P),s(P))$ of the order-$4$ isotropic subgroup of @prop:coble-planecusp-finite(1) and the star (@def:plane-star) of @lem:plane-stars, and the triple $(J(P),s(P),[L/2])$.

1. (Lifting.) $x\mapsto D(x)$ induces a bijection from the $\Gamma$-orbits of objects of each of the three types onto the $H$-orbits of the finite data of that type, the data being all $527$ nonzero isotropic classes, all $8\cdot 23\,715=189\,720$ pairs and all $3\cdot 189\,720=569\,160$ triples. So the number of $\Gamma$-orbits of a type is the number of $H$-orbits of its finite data.

2. (The fibre over one datum.) For a datum $D$ of one of the three types and an object $x$ with $D(x)=D$, put $F_D=\Stab_Q(D)$ and $S_x=\rho\left(\Stab_{\Orth(T_\Co)}(x)\right)$. Then
$$
S_x=F_D .
$$
the integral stabilizer (@def:group-orbit) of an object realizes the whole finite stabilizer of its datum. Consequently the double quotient of the fibre of @thm:descent-double-coset is
$$
\left(H\intersect F_D\right)\backslash F_D\big/ S_x
 =\left(H\intersect F_D\right)\backslash F_D\big/ F_D ,
$$
a single point, and the fibre $\theset{y : D(y)=D}$ is a single orbit (@def:group-orbit) of $\widetilde\Orth^+(T_\Co)$, hence a single orbit of $\Gamma$.

3. (The hypotheses, and which one does what.) Two hypotheses are in play and they are not the same one. Item 1 requires $\widetilde\Orth^+(T_\Co)\iscontainedin\Gamma$: for $\ker\rho$ every fibre of item 2 is already a single orbit, and the spinor-negative stabilizer witnesses of @thm:cusp-lifting(4) keep it one on passing to $\Orth^+(T_\Co)$ and hence to any group between. The reduction of a fibre's double quotient to the finite quotient displayed in item 2 requires $\ker\rho\iscontainedin\Gamma$ (@thm:descent-double-coset). Kernel containment implies the first, since $\widetilde\Orth^+(T_\Co)\iscontainedin\ker\rho$, and not conversely: $\Gamma=\widetilde\Orth^+(T_\Co)$ satisfies the first and not the second. By item 2, however, $S_x=F_D$, so the finite double quotient is a single point for **every** subgroup and every datum; what makes the number of lattice orbits equal the number of finite orbits is the first hypothesis alone, and the second is what lets the fibre's orbits be *read off* the finite quotient. This is the precise sense in which a finite double quotient counts the lattice orbits here: one orbit per finite datum, and no datum contributes a second.

4. (The three subgroups, and the counts.) With $P\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})\leq Q$ the stabilizer of the $U(2)$ block (@prop:coble-cong-point-stabilizer(1)):
   a. for $\Gamma=\widetilde\Orth^+(T_\Co)$ one has $H=1$, and the three counts are $527$, $189\,720$ and $569\,160$;
   b. for $\Gamma=R_{\gent}=\rho^{-1}(P)$ one has $H=P$, of order $696\,729\,600=\abs{W(E_8)}$ (@prop:gamma-cong-eq-heegner(1)), with $[\Orth(T_\Co):R_{\gent}]=67\,456$, and the three counts are $4$, $7$ and $13$;
   c. for $\Gamma=\Orth(T_\Co)$ one has $H=Q$ and the three counts are $1$, $1$ and $1$.
:::

::: {.proof}
*The datum map.* For $g\in\Orth(T_\Co)$ and a primitive isotropic $v$ one has $[gv/2]=\rho(g)[v/2]$ (@lem:isotropic-classes-lift(1)); for a primitive isotropic plane $J(gP)=\rho(g)J(P)$ (@prop:coble-planecusp-finite(1)) and $s(gP)=\rho(g)s(P)$, the star being defined intrinsically from the quotient $P^{\perp B}/P$ (@lem:plane-stars); and for a flag both components. So $D(gx)=\rho(g)D(x)$, and $x\mapsto D(x)$ carries $\Gamma$-orbits to $H$-orbits. Vector and line orbits coincide because $-\id_{T_\Co}\in\widetilde\Orth^+(T_\Co)$ (@thm:cusp-lifting(4)). Every datum of each of the three types is attained: @lem:isotropic-classes-lift(2) for the classes; @prop:coble-planecusp-finite(2) for the subgroups $J$, with the eight stars of @thm:coble-plane-stabilizer-image(5) over each; and @prop:coble-planecusp-finite(1), the three nonzero elements of $J(P)$ being the classes of the primitive vectors of $P$, for the triples. Hence the induced map on orbits is onto, and it is injective (@def:injective-map) exactly when every fibre is a single $\Gamma$-orbit.

*The fibres.* For $\Gamma=K$ each fibre is one $K$-orbit: @thm:coble-zero-cusp-count(1) for the lines, @lem:plane-stars(3) for the planes and @thm:cusp-lifting(3) for the flags, that is, the bijections of @thm:cusp-lifting(1)--(3) at $\Gamma=\ker\rho$. By @thm:cusp-lifting(4) each of these fibres carries a spinor-negative element of $K$ in the stabilizer of each of its points, so no $K$-orbit splits on intersection with $\Orth^+(T_\Co)$: every fibre is one $\widetilde\Orth^+(T_\Co)$-orbit. For $\Gamma\supseteq\widetilde\Orth^+(T_\Co)$ the group $\Gamma\intersect K$ contains $\widetilde\Orth^+(T_\Co)$ and is therefore transitive on each fibre too, so the $\Gamma$-orbit of a point of the fibre is that fibre. This proves item 1, and the last clause of item 2.

*The stabilizer equality.* For lines it is @lem:cusp-vector-stabilizer-image(1); the stabilizer of a nonzero class and of the subgroup it generates agree, $A_{T_\Co}$ being $2$-torsion. For planes it is @lem:plane-stars(2): for a primitive isotropic plane $P$ with $J(P)=J$, the group $S=\rho\left(\Stab_{\Orth(B)}(P)\right)$ is the stabilizer in $F=\Stab_Q(J)$ of exactly one star, namely $s(P)$, so that
$$
S=\Stab_F\left(s(P)\right)=\Stab_Q(J)\intersect\Stab_Q(s(P))=F_{(J,s)} .
$$
The index of @thm:coble-plane-stabilizer-image(4) is the same statement numerically: $F$ permutes the eight stars transitively (@lem:plane-stars(1)), so the stabilizer of one of them has order $\abs{F}/8=1\,981\,808\,640/8=247\,726\,080=\abs{S}$ (@prop:coble-planecusp-finite(4), @thm:coble-plane-stabilizer-image(3)), and $8$ is the number of stars. The middle order is that of $\rho$ of the complete integral plane stabilizer, whose generating family (@def:generating-frame) of $28$ matrices is `computations/reports/coble_complete_plane_parabolic_generators.json`; the executable `computations/reports/coble_proper_plane_stabilizer_image.py` recomputes the three numbers from it and prints them at `computations/reports/coble_proper_plane_stabilizer_image-run.txt:2`, `:3`, `:4` and `:5`.
For flags, put $S_2=F_{(J,s)}=S_{(J,s)}$ by the plane case. Both $\Stab_Q(J,s,c)=\Stab_{S_2}(c)$ and $\rho\left(\Stab_{\Orth(B)}(L\subset P)\right)$ lie in $S_2$, and the second is contained in the first because it fixes the line $L$ and hence the class $c=[L/2]$. By @thm:coble-plane-stabilizer-image(3) the image of $\Stab_{\Orth(B)}(P)=L\ltimes U$ is $S_2=\rho(L)\rho(U)$ with $\rho(L)=S_3\times S_7$ and $\rho(U)$ the unipotent radical of order $2^{13}$. An element $\gamma\oplus(\gamma^{-1})^{T}\oplus\delta$ of $L$ (@thm:coble-plane-stabilizer-image(1)) preserves the line $L=\ZZ e_2$ exactly when $\gamma$ preserves $\ZZ e_2$ in $P=\generators{e_1,e_2}$, that is, when $\gamma$ lies in the upper triangular subgroup $\operatorname{B}(\ZZ)\subset GL_2(\ZZ)$, and $U$ fixes $P$ pointwise; so
$$
\rho\left(\Stab_{\Orth(B)}(L\subset P)\right)=\rho\left(\operatorname{B}(\ZZ)\times\Orth(D)\right)\,\rho(U)
$$
is the stabilizer in $S_2$ of the class $c=[L/2]$, because upper triangular matrices reduce onto the stabilizer of the class $\bar e_2$ in $S_3=GL(J)$ and the factors $\Orth(D)$ and $U$ act trivially on $J$. The $S_2$-orbit of $c$ is its $S_3$-orbit, of length $3$, so that stabilizer has order $247\,726\,080/3=82\,575\,360=\abs{\Stab_{S_2}(c)}$, and the two groups coincide. Item 2 follows in all three cases, and with it the value of the double quotient, because $(H\intersect F)F=F$ for every subgroup $H\leq F$.
The star is what carries the vanishing multiplicity, and it is also why @thm:coble-plane-stabilizer-image(5) and item 2 do not contradict one another: that item states the fibre over the **undecorated** datum $J$, whose finite stabilizer is $F=\Stab_Q(J)$ of order $1\,981\,808\,640$, so its quotient over one $J$ has the $8$ cosets of the eight stars as its multiplicity (@thm:plane-fibre(1)), while the decorated datum $(J,s)$ of item 2 has $F_{(J,s)}=S_x$ and multiplicity one. In the same way the line datum is the class and not the pair of opposite lines, $A_{T_\Co}$ being $2$-torsion so that the two stabilizers agree.

*The counts.* For (a), $H=\rho\left(\widetilde\Orth^+(T_\Co)\right)=1$, so the counts are the cardinalities of the three data sets: $527$ (@thm:coble-zero-cusp-count(2)), $189\,720$ (@thm:plane-fibre(3)) and $569\,160=24\cdot 23\,715$ (@prop:coble-arithmetic-flag-incidence, the $24$ orbits over each of the $23\,715$ subgroups of @prop:coble-planecusp-finite(3)). The last is also the edge count and the two vertex degrees (@def:graded-object) of the kernel incidence relation of the integral flag archive, printed at `computations/reports/coble_integral_public_edge_multiplicities-run.txt:35`, and the total edge count of its provenance ledger `computations/reports/coble_integral_flag_certificate_manifest.json:10`, whose $32$ shards are the records of `:11` and whose producing run and artifact are `:3` and `:6`.
For (b), @prop:coble-cong-point-stabilizer(1) gives $R_{\gent}=\rho^{-1}(P)$, so the discriminant image of $R_{\gent}$ is $P$; @prop:coble-cong-point-stabilizer(2) gives its four orbits $2,135,270,120$ on the $527$ classes. The enumerated group $G_\Co$ of @thm:coble-heegner-finite-orbits(2) is $P$: it is the transport $\gamma G\gamma^{-1}$ of the group $G=P_{S_\En}$ of @thm:coble-heegner-finite-orbits(1), it has order $\abs{W(E_8)}=\abs{P}$ (@prop:gamma-cong-eq-heegner(1)), and $\gamma P_{S_\En}\gamma^{-1}=P$ because the marked gluing is block-compatible (@prop:gamma-cong-eq-heegner(2), @prop:coble-block-compatibility). So the decomposition of `computations/reports/coble_gco_plane-orbits-run.txt:3` is a decomposition of $P$. The index is $\abs{Q}/\abs{P}=46\,998\,591\,897\,600/696\,729\,600=67\,456$, the value the record `computations/reports/coble_a13-heegner-comparison-run.txt:41` computes as $\abs{\Orth(q)}/\abs{P}$ and `:42` prints as $[\Orth(T_\Co):\Gamma_{\Co,2}]$. The seven $P$-orbits on the pairs and the thirteen on the triples are the enumerations of `computations/reports/coble_gco_plane-orbits-run.txt:9` and `:10`, whose orbit sizes sum to $189\,720$ and to $569\,160$; the thirteen are carried to the thirteen public $\Gamma_{\Co,2}$ edge multiplicities at `computations/reports/coble_integral_public_edge_multiplicities-run.txt:47`. The flag count agrees with the independent decomposition of @prop:coble-flag-orbits-and-edges(1) over the seven plane orbits, whose seven summands are the $3,1,2,1,2,2,2$ flag orbits printed at `computations/reports/coble_gco_plane-orbits-run.txt:19`--`:25`.
For (c), $H=Q$ is transitive on the $527$ nonzero classes (@lem:isotropic-classes-lift(2)), on the $23\,715$ subgroups of order $4$ (@prop:coble-planecusp-finite(2)) and, with $F$, on the eight stars; so each of the three data sets is one orbit, which is @thm:unpolarized-cusps, @thm:plane-transitivity-tco and @cor:coble-flag-counts-per-group(2) respectively.
:::

::: {.remark #rmk:coble-integral-lifting-records title="The records the three counts name, at their lines"}
The three subgroups of @thm:coble-integral-lifting-fibre(4) and the line of their record:
$\widetilde\Orth^+(T_\Co)$ with $527,189\,720,569\,160$, proved on this page and archived as the complete $569\,160$-edge integral certificate whose total is `computations/reports/coble_integral_flag_certificate_manifest.json:10` and whose incidence degrees are `computations/reports/coble_integral_public_edge_multiplicities-run.txt:35`;
$R_{\gent}$ with $4,7,13$ (@thm:coble-integral-lifting-fibre(4)(b)), the last two also from `computations/reports/coble_gco_plane-orbits-run.txt:9` and `:10`, with the public edge weights at `computations/reports/coble_integral_public_edge_multiplicities-run.txt:47`; the record's row is labelled `Gamma_{Co,2}` and builds this arithmetic group, not the monodromy group $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5) (@prop:coble-cong-point-stabilizer(1));
and $\Orth(T_\Co)$ with $1,1,1$, proved on this page. The plane count of each row is also the corresponding column of @thm:coble-plane-orbit-counts, which carries that count against the public call and record of the group; the line and flag counts above are the two rows that theorem does not carry. The parabolic image that item 2 of that theorem uses is the family of $28$ matrices in `computations/reports/coble_complete_plane_parabolic_generators.json`, with the image order, the index $8$ and the eight stars at `computations/reports/coble_proper_plane_stabilizer_image-run.txt:2`--`:5`. No line above is a returned public subgroup-incidence row: the counts are proved here, the records are the executions that were run against the integral flag family, and the public operation of sage-extensions#286 and sage-extensions#381 and the lattice-database card of #7 remain separate obligations (see @rmk:coble-plane-incidence-row-provenance).
:::

### The plane fibre and the flag incidence against the public rows {#sec-plane-flag-rows}

The counts proved above are counts of orbits of groups acting on $T_\Co$, and a computation that certifies one of them has to build the same group. This section fixes which group each public entry point builds, and then reads the plane rows, the cusp rows and the incidence row against @thm:plane-fibre and @prop:coble-arithmetic-flag-incidence. The flags enter it because an incidence row returns a relation between orbit vertices, which is not the set of flag orbits; @prop:coble-flag-orbits-and-edges states the difference exactly.

::: {.proposition #prop:coble-flag-orbits-and-edges title="The flag orbits over a group containing the stable group, and the endpoint relation they refine"}
Let $B = \latI_{2,9}$, $T_\Co = B(2)$, $J(P)\leq A_{T_\Co}$ the order-$4$ subgroup of a primitive isotropic plane $P\subset B$ (@prop:coble-planecusp-finite(1)), $\rho$ the discriminant representation (@def:discriminant-rep) and $\widetilde\Orth^+(T_\Co)\subseteq\Gamma\subseteq\Orth(B)$, and put $H\definedas\rho(\Gamma)$. For a $\Gamma$-orbit $\mathcal P$ of primitive isotropic planes of $B$ choose $P_0\in\mathcal P$, put $J_0\definedas J(P_0)$ and $H_0\definedas\rho\left(\Stab_\Gamma(P_0)\right)\leq H$, and put
$$
C(\mathcal P)\definedas\bigcup_{P'\in\mathcal P}\bigl(J(P')\sm\generators{0}\bigr) = H\cdot\bigl(J_0\sm\generators{0}\bigr)\subseteq A_{T_\Co}\sm\generators{0}
,$$
the nonzero isotropic classes that the primitive lines of the planes of $\mathcal P$ represent.

1. (Flag orbits.) The primitive lines of $P_0$ fall into the three nonzero classes of $J_0$, and $\Stab_\Gamma(P_0)$ is transitive on the primitive lines of each of them, because $\widetilde\Orth^+(T_\Co)\subseteq\Gamma$ and @prop:coble-arithmetic-flag-incidence(1), (2) gives that transitivity for $\widetilde\Orth^+(T_\Co)$. So the $\Gamma$-orbits of flags $(P',L)$ over $\mathcal P$ are the $H_0$-orbits on $J_0\sm\generators{0}$, and $\Gamma$ has exactly
$$
\sum_{\mathcal P}\abs{\left(J_0\sm\generators{0}\right)/H_0}
$$
orbits of flags of a primitive isotropic line in a primitive isotropic plane.

2. (The endpoint relation.) A $\Gamma$-orbit of primitive isotropic lines is determined by the $H$-orbit of the class of its lines: the $\widetilde\Orth^+(T_\Co)$-orbits already equal the $\ker\rho$-orbits (@thm:cusp-lifting(1), (4)), and $\widetilde\Orth^+(T_\Co)\subseteq\Gamma$. So the line orbits meeting the planes of $\mathcal P$ are the $H$-orbits of $C(\mathcal P)$, and the endpoint relation --- the pairs of a line orbit and a plane orbit realized by a flag --- has exactly
$$
\sum_{\mathcal P}\abs{C(\mathcal P)/H}
$$
edges. Each summand is the number of classes of the relation on $J_0\sm\generators{0}$ that puts $c$ and $c'$ together when $c' = hc$ for some $h\in H$, so it lies between $1$ and $3$.

3. (Which of the two is larger.) $H_0\leq H$, and two elements of $J_0\sm\generators{0}$ in one $H_0$-orbit lie in one $H$-orbit of $C(\mathcal P)$, so the number of edges is at most the number of flag orbits, with equality exactly when for every $\mathcal P$ the $H_0$-orbits on $J_0\sm\generators{0}$ are the classes of that relation. Each plane orbit contributes at most $\abs{J_0\sm\generators{0}} = 3$ to either sum.
:::

::: {.proof}
(1) A flag with plane in $\mathcal P$ is carried to one with plane $P_0$ by an element of $\Gamma$, so the $\Gamma$-orbits of flags over $\mathcal P$ are the orbits (@def:group-orbit) of $\Stab_\Gamma(P_0)$ on the primitive lines of $P_0$. By @prop:coble-planecusp-finite(1) the nonzero classes of $J_0$ are the classes $[L/2]$ of the primitive lines of $P_0$, and by $[gv/2] = \rho(g)[v/2]$ the class map is $\Stab_\Gamma(P_0)$-equivariant onto $J_0\sm\generators{0}$. Its fibres are single $\Stab_\Gamma(P_0)$-orbits --- that is the transitivity stated --- so the orbits on the lines correspond bijectively to the orbits of $H_0$ on the classes, and summing over the plane orbits gives the total.

(2) For $g\in\Orth(B)$ and a primitive isotropic $v$ one has $[gv/2] = \rho(g)[v/2]$, and $\rho(g)$ preserves isotropy and the nonzero classes. By @thm:cusp-lifting(1), (4), the fibres of this class map are single $\widetilde\Orth^+(T_\Co)$-orbits. Since that group is contained in $\Gamma$, the $\Gamma$-orbits of primitive isotropic lines are therefore the $H$-orbits of classes. More explicitly, for an integral basis $p,q$ of any primitive isotropic plane $P$, the three primitive isotropic vectors (@def:isotropic-subspace) $p,q,p+q$ represent exactly the three nonzero classes of $J(P)$; their primitiveness follows from the coefficient pairs $(1,0)$, $(0,1)$, $(1,1)$ in the saturated plane. For any $\Gamma$-line cusp whose $H$-orbit of classes contains $c\in J(P)\sm\generators{0}$, choose a representative of that cusp with class $c$. Let $u$ be a primitive vector spanning the chosen line representative and $v\in\{p,q,p+q\}$ the vector of class $c$. By @lem:I29-plus-line-transitivity there is $g\in\Orth(B)$ with $gu=v$. Then $\rho(g)$ fixes $c$, so @lem:cusp-vector-stabilizer-image(1) supplies $h\in\Stab_{\Orth(B)}(u)$ with $\rho(h)=\rho(g)$. Consequently $k=gh^{-1}\in\ker\rho$ sends $u$ to $v$. If $k$ has negative real spinor norm, choose a spinor-negative $t\in\ker\rho\intersect\Stab_{\Orth(B)}(v)$ by @lem:cusp-vector-stabilizer-image(2); then $tk\in\widetilde\Orth^+(T_\Co)$ still sends $u$ to $v$. Thus the finite endpoint datum constructs an integral incident flag and proves the existence of its subgroup transporter, without claiming that the public class-only row has returned the matrices $g,h,t$. This constructs an integral incident flag from the finite endpoint classes, although the lifting theorem does not itself output a transporter matrix for the particular public representatives. A line orbit contains a line of a plane of $\mathcal P$ exactly when its class lies in $C(\mathcal P)$, and $C(\mathcal P)$ is $H$-invariant by construction; every $H$-orbit inside it is the orbit of an element of $J_0\sm\generators{0}$, and two elements of $J_0\sm\generators{0}$ lie in one $H$-orbit of $C(\mathcal P)$ exactly when they are $H$-equivalent. So the $H$-orbits of $C(\mathcal P)$ correspond to the classes of that relation on $J_0\sm\generators{0}$, and the edge count is their sum over the plane orbits.

(3) The partition of $J_0\sm\generators{0}$ into $H_0$-orbits refines its partition into the traces of the $H$-orbits of $C(\mathcal P)$, since equivalence under $H_0$ implies equivalence under $H$. Equality of the two counts for every $\mathcal P$ is therefore exactly the stated condition, and $\abs{J_0\sm\generators{0}} = 3$ bounds each summand.
:::

::: {.corollary #cor:coble-flag-counts-per-group title="Three flag counts: the stable group, the full orthogonal group, and the arithmetic group $R_{\gent}$"}
1. For $\Gamma = \widetilde\Orth^+(T_\Co)$ one has $H = H_0 = 1$, so the edges and the flag orbits (@def:group-orbit) both number $3\cdot 23\,715\cdot 8 = 569\,160$: this is the $24$ per $J$ of @prop:coble-arithmetic-flag-incidence read over the $23\,715$ subgroups of @prop:coble-planecusp-finite(3), and for the stable group it is both the flag count and the edge count.
2. For $\Gamma = \Orth(B)$ there is one plane orbit (@thm:plane-transitivity-tco) and one line orbit (@thm:unpolarized-cusps), so the endpoint relation is a single edge; and $\rho\left(\Stab_{\Orth(B)}(P)\right)= H_0$ acts on $J_0\sm\generators{0}$ through a group containing $GL(J_0)\cong S_3$ (@thm:coble-plane-stabilizer-image(2)), so it is transitive there and there is one flag orbit as well.
3. For $\Gamma = R_{\gent}$ there are $4$ line orbits, $7$ plane orbits, $13$ flag orbits and $13$ edges: the three orbit counts are @thm:coble-integral-lifting-fibre(4)(b), and the $13$ edges are @prop:coble-flag-orbits-and-edges(3). For the monodromy group $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5) the same four numbers hold exactly when @qst:coble-monodromy-equality does, since then $\Gamma_{\Co,2} = R_{\gent}\intersect\Orth^+(T_\Co)$, whose discriminant image is $\rho(R_{\gent}\intersect\Orth^+(T_\Co)) = P$ (@prop:gamma-cong-eq-heegner(3)) and to which the bijections of @thm:cusp-lifting(1)--(3) apply by @thm:cusp-lifting(4); unconditionally @thm:coble-monodromy-versus-enriques(4) gives only $\Gamma_{\Co,2}\subseteq R_{\gent}\intersect\Orth^+(T_\Co)$, and $\rho(\Gamma_{\Co,2})\subseteq P$. The public row of @rmk:coble-plane-incidence-rows computes the endpoint relation and its $13$ edges, not the flag-orbit count; the latter is established independently by @cor:coble-heegner-integral-plane-descent and its finite triple-orbit enumeration.
:::

::: {.proof}
(1) $\widetilde\Orth^+(T_\Co)\subseteq\ker\rho$ gives $H = 1$, hence $H_0 = 1$, so both sums are $\sum_{\mathcal P}3$ over the $189\,720$ plane orbits of @thm:coble-plane-stabilizer-image(5)(c). (2) A group acting on $J_0$ through a group containing $GL(J_0)$ is transitive on $J_0\sm\generators{0}$, so the flag sum has the single term $1$; and $\Orth(q)$ is transitive on the $527$ nonzero isotropic classes (@lem:coble-discriminant-blocks(2)), so $C(\mathcal P)$ is a single $H$-orbit and the edge sum has the single term $1$. (3) The group identity is @prop:coble-cong-point-stabilizer(1), so the thirteen flag orbits are @cor:coble-heegner-integral-plane-descent; the thirteen edges are the distinct endpoint pairs in the public row of @rmk:coble-plane-incidence-rows. These are separate arguments, not an inference of the flag count from the endpoint row.
:::

::: {.proposition #prop:coble-cong-point-stabilizer title="The group the public plane stabilizer builds, and the $0$-cusps of $F_{\Co,2}$"}
1. $\Stab_{\Orth(q_{T_\Co})}\bigl(A_{U(2)}\bigr) = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)}) = P$ of @def:congruence-group, and consequently
$$
\rho_{T_\Co}^{-1}\left(\Stab_{\Orth(q_{T_\Co})}\bigl(A_{U(2)}\bigr)\right) = \rho_{T_\Co}^{-1}(P) = \Gamma^{\mathrm{cong}}_{\Co,2} = R_{\gent}
,$$
the three equalities after $\rho_{T_\Co}^{-1}(P)$ being @def:congruence-group and @prop:gamma-co-images(3); this is the arithmetic group $R_{\gent}$, not the monodromy group $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5), which is compared with it in @thm:coble-monodromy-versus-enriques.
2. The orbits of $P$ on the $527$ nonzero isotropic classes of $A_{T_\Co}$ are four, of sizes $2$, $135$, $270$ and $120$.
3. Hence $\bD(T_\Co)/(R_{\gent}\intersect\Orth^+(T_\Co))$ has exactly four $0$-cusps, and $F_{\Co,2} = \bD(T_\Co)/\Gamma_{\Co,2}$ does not: that would need @qst:coble-monodromy-equality, which is false (@prop:coble-monodromy-equality-false, @rmk:coble-monodromy-counts).
:::

::: {.proof}
(1) The inclusion $\supseteq$ is clear, and $\subseteq$ is @lem:coble-discriminant-blocks(4). For the chain, @prop:gamma-co-images(3) describes $P$ as the stabilizer (@def:group-orbit) of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$ of $A_{E_{10}(2)}$: an isometry carrying $A_{U(2)}$ onto $A_{E_8(2)}$ would be an isometry of quadratic forms of orders $4$ and $256$, which does not exist, so the stabilizer of the decomposition is the setwise stabilizer of $A_{U(2)}$.

(2) Write $A = A_{T_\Co} = \generators{k}\perp A^0$ with $k = [\zeta/2]$ and $A^0 = A_{U(2)}\perp A_{E_8(2)}$, as in @lem:coble-discriminant-blocks. By (3) of that lemma every isometry of $q_A$ fixes $k$ and acts on $A^0$, and $q_A(k+a) = \tfrac12 + q_{A^0}(a)$, so the isotropic classes of $A$ are the isotropic classes of $A^0$: $0$ together with $527$ nonzero ones, $3\cdot 136 + 1\cdot 120 = 528$ in all (@lem:coble-discriminant-blocks(2), @lem:gco-orbit-transfer).
On $A_{U(2)}$ the three nonzero classes $u_1,u_2,u_3$ have $q$-values $0,0,1$, and $\Orth(q_{U(2)})$ fixes $u_3$ and swaps $u_1,u_2$ (@prop:gamma-cong-eq-heegner(1)); on $A_{E_8(2)}$ the $135$ nonzero classes of value $0$ form one orbit (@def:group-orbit) of $\Orth(q_{E_8(2)})$ and the $120$ of value $1$ form one (@lem:coble-discriminant-blocks(2), by Witt's theorem). Write $E_0$ and $E_1$ for those two sets. The isotropic classes of $A^0$ are then $0$, $u_1$, $u_2$, the classes $(0,e)$, $(u_1,e)$, $(u_2,e)$ with $e\in E_0$, and the classes $(u_3,e')$ with $e'\in E_1$, and by @lem:coble-discriminant-blocks(4) the group $P$ acts on the first coordinate through $\Orth(q_{U(2)})$ and on the second through $\Orth(q_{E_8(2)})$. Its orbits are therefore
$$
\generators{0},\qquad
\theset{u_1,u_2},\qquad
\theset{(0,e) : e\in E_0},\qquad
\theset{(u_1,e),(u_2,e) : e\in E_0},\qquad
\theset{(u_3,e') : e'\in E_1},
$$
of sizes $1$, $2$, $135$, $270$ and $120$; the four nonzero orbits total $527$.

(3) The $0$-cusps of $\bD(T_\Co)/(R_{\gent}\intersect\Orth^+(T_\Co))$ are its orbits on the primitive isotropic vectors (@def:isotropic-subspace) of $T_\Co$. Every primitive vector of $T_\Co$ has divisibility $2$ (@lem:divisibilityAlwaysTwoTco), and $\rho(R_{\gent}\intersect\Orth^+(T_\Co)) = P$ (@prop:gamma-cong-eq-heegner(3)), so by @thm:cusp-lifting(1), (4) these orbits correspond to the orbits of $P$ on the $527$ nonzero isotropic classes, which by (2) number four; this is @prop:coble-cong-point-stabilizer(3), and $F_{\Co,2} = \bD(T_\Co)/\Gamma_{\Co,2}$ has exactly four $0$-cusps when @qst:coble-monodromy-equality holds, not otherwise asserted. This count is independently returned by the public row of @rmk:coble-plane-incidence-rows.

:::

::: {.remark #rmk:coble-plane-descent-group title="The group of the integral plane descent"}

*The group that @cor:coble-heegner-integral-plane-descent counts is $R_{\gent}$.* That corollary counts the orbits of $\rho_{T_\Co}^{-1}(G_\Co)$, so what is needed is $G_\Co = P$, and this is the computation of the proof of @thm:coble-integral-lifting-fibre(4)(b): $G_\Co$ is the transport $\gamma G\gamma^{-1}$ of the group $G = P_{S_\En}$ of @thm:coble-heegner-finite-orbits(1), of order $\abs{W(E_8)} = \abs{P}$ (@prop:gamma-cong-eq-heegner(1)), and $\gamma P_{S_\En}\gamma^{-1} = P$ because the marked gluing is block-compatible (@prop:gamma-cong-eq-heegner(2), @prop:coble-block-compatibility). Hence $\rho_{T_\Co}^{-1}(G_\Co) = \rho_{T_\Co}^{-1}(P) = R_{\gent}$ (@prop:coble-cong-point-stabilizer(1)).
:::

::: {.remark #rmk:coble-cong-point-cusps-over-sterk title="Where the four $0$-cusps of $R_{\gent}$ lie"}

In @prop:coble-cong-point-stabilizer(3): the four lie one over each of Sterk's cusps $2,3,4,5$ and none over cusp $1$ (@thm:four-r-orbits, @thm:orbit-per-cusp, @thm:cusp-fibres-four), and the same group has $7$ orbits on the primitive isotropic planes, as the plane count of this page gives, none over the four $1$-cusp types containing $1$ and distributed over the five others as @thm:one-cusp-multiplicities gives: one over $\{2,4,5\}$, one over $\{4,5\}$, two over $\{3,5\}$, one over $\{3,4\}$ and two over $\{5,5\}$; the incidence is $0_k\rightsquigarrow T$ exactly when $k\in T$, with degrees $1,3,3,6$ and $13$ edges (@thm:cusp-diagram-tco).
:::

::: {.theorem #thm:coble-plane-orbit-counts title="The primitive isotropic plane orbits of the four group rows, each against its call and its record"}
Let $B = \latI_{2,9}$, $T_\Co = B(2)$, $K = \ker\rho_{T_\Co}$, and in the notation of @cor:coble-eight-standard-line-counts let $O = \Orth(T_\Co)$, $O^+ = \ker\spinornorm_\bR$, $SO = \ker\det$ and $SO^+ = SO\intersect O^+$. Then the primitive isotropic planes of $T_\Co$ fall into

1. one orbit (@def:group-orbit) under each of $O$, $SO$, $O^+$ and $SO^+$;
2. $189\,720$ orbits under $K$ and under each of $K\intersect SO$, $K\intersect O^+$ and $K\intersect SO^+$;
3. seven orbits under $R_{\gent}\intersect\Orth^+(T_\Co)$, and not under $\Gamma_{\Co,2}$, which would need @qst:coble-monodromy-equality (@prop:coble-monodromy-equality-false);

and the count for $\Gamma_\Co$ is $189\,720$, since $\Gamma_\Co$ is the stable group on the labelled base (@thm:gamma-co-is-stable). Each count is proved on the page, and each is also the integer a public row returns: the proof lists the call that builds each group and the record that prints its number.
:::

::: {.proof}
Items 1 and 2 are the plane column of @cor:coble-eight-standard-line-counts, and item 3 is @cor:coble-heegner-integral-plane-descent; the last sentence is @thm:plane-fibre(3) with @thm:plane-transitivity-tco for $F^{\mathrm{un}}_\Co$. So no count here rests on a row. What the rows are is a reproduction of each, through the group the entry point builds, and each is named by the record that prints it, by path (@def:path-connectedness) and line on sage-extensions `main`. The four rows are `tests/coble_gamma_co_2_incidence_rows.py:620`'s labels `O`, `Gamma_{Co,2}`, `Otilde` and `Otilde+`:

| group | orbits | the public call, and where it is made | the record that prints the count |
| --- | ---: | --- | --- |
| $O$, $SO$, $O^+$, $SO^+$ | $1$ | `Tco.Aut().isotropic_orbit_representatives(2)` | `results/issue286-the-stage-1-call.md:99`, one orbit in $4.4$ s; the single plane cusp and the single edge of the $O$ row are @rmk:coble-plane-incidence-rows's |
| $K$, $\widetilde\Orth^+(T_\Co) = K\intersect O^+$ | $189\,720$ | `Tco.stable_orthogonal_group().isotropic_orbit_representatives(2)` for $K$, and the same call on its intersection with `Tco.O_plus()` for $K\intersect O^+$ (`tests/coble_kernel_plane_rows.py:133`, `:272`, `:276`) | run 43798731423 at `897e7f7fd4` (@rmk:coble-plane-incidence-rows); and the same row on the cusp instrument `cusps(2)` at sage-extensions `7753092`, `results/issue286-the-stage-1-call.md:271-273` and `:281-283`, which prints $189\,720$ cusps in $2171.0$ s at a $3476.4$ MiB peak and $189\,720$ in $1812.8$ s at $3554.3$ MiB |
| $R_{\gent}$ (the row's label `Gamma_{Co,2}`) | $7$ | `Tco.Aut().discriminant_point_stabilizer(A_{U(2)}).isotropic_orbit_representatives(2)`, the point being the span of the two $U(2)$ generator classes, whose preimage is $R_{\gent}$ by @prop:coble-cong-point-stabilizer(1) (`tests/lattices/test_the_coble_gamma_co_2_plane_row_and_the_building_incidence.sage:89`, `:91`) | `.tmp/qc-evidence/issue390-tco-rows.log:16`, seven planes in $127.7$ s; and the seven plane cusps of run 43556671111, `.tmp/qc-evidence/issue391-incidence-rows.log:5`, also at `results/issue381-kernel-incidence-rows.md:56` |

The two intermediate character subgroups $K\intersect SO$ and $K\intersect SO^+$ have the orbits of $K$ by the character-adjustment argument of @cor:coble-eight-standard-line-counts, and no separate row is run for them; the rows above are the two kernel groups the driver builds, which are the two its job dispatches. The seven are the planes of the arithmetic quotient $\bD(T_\Co)/(R_{\gent}\intersect\Orth^+(T_\Co))$, and of $F_{\Co,2}$ exactly when @qst:coble-monodromy-equality holds: no inclusion between $\Gamma_{\Co,2}$ and $\Gamma_\Co$ is asserted.
:::

::: {.remark #rmk:coble-plane-incidence-rows title="The public rows behind the plane fibre, the cusps of $F_{\Co,2}$ and the incidence"}
These plane and incidence rows are computation records in sage-extensions, not lattice-database card fields. The $T_\Co$ lattice card now separately holds certified primitive isotropic **line** counts for all eight standard subgroups, and its two arithmetic-group cards hold certified indices (lattice-database#7). The integral generator morphisms, which this remark recorded as absent, are on both cards at lattice-database main `d5e96acf` (`lattices/6JRR.md:24-25`, with the matrices themselves as the card's `morphisms` entries from `:133` on); what that card does not carry is a plane count or an incidence value, and it admits no field that no certificate names (`tests/test_catalogue_schemas.py:170`, `:195`). Affected-card `latticedb verify` is not checked here, being that repository's own tool; #7 therefore remains open against its original acceptance, and what it still owes is the plane and incidence fields.

*The row labels.* Throughout this remark a record's row label `Gamma_{Co,2}` names the arithmetic group $R_{\gent} = \rho_{T_\Co}^{-1}(P)$ of @prop:coble-cong-point-stabilizer(1), not the monodromy group $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5); the two are compared in @thm:coble-monodromy-versus-enriques, and no count in this remark is asserted for the monodromy group.

*The two plane rows.* The driver is `tests/coble_kernel_plane_rows.py` at `897e7f7fd45e4d4f4cfcb29b266672e9232d25ab`, and the call is `isotropic_orbit_representatives(2)` on `Tco.stable_orthogonal_group()` and on its intersection with `Tco.O_plus()`, that is on $K = \ker\rho$ and on $\widetilde\Orth^+(T_\Co) = K\intersect\Theta_\bR(T_\Co)$, the real-spinor kernel of @conv:spinor-positive-subgroup that the driver names `sn_RR`: the two groups whose line counts are @thm:coble-zero-cusp-count(2) and whose plane and flag counts are @cor:coble-eight-standard-line-counts. Every returned representative is checked to have rank two, to be primitive in $T_\Co$, and to carry the zero Gram tensor, and the count is compared with the double cosets over the single $\Orth(T_\Co)$-class of primitive isotropic planes, computed as a quotient of two group orders. Run 43798731423 reports $189\,720$ planes for $\ker\rho$ in $4013.4$ s and $189\,720$ for $\widetilde\Orth^+(T_\Co)$ in $1821.2$ s, each against an expected $189\,720$ over one class of $\Orth(T_\Co)$; the run's own record, sage-extensions#390's closing comment of 2026-11-16, gives the same two counts and durations and states that the driver checks each count against the double-coset count of Dutour Sikiric--Hulek, arXiv:2302.01679v2, Lemma 3.6, and it is archived verbatim at `computations/reports/coble_kernel_plane_rows-issue390-run-record.txt` because the run's log archive is not downloadable without admin rights on that repository.

The page's count and the row's are the same integer seen from two sides. The page counts eight orbits over each of the $23\,715$ subgroups (@thm:coble-plane-stabilizer-image(5)(c)); the row counts one quotient over the one $\Orth(T_\Co)$-class of planes, namely
$$
\frac{\abs{\rho(\Orth(T_\Co))}}{\abs{\rho\left(\Stab_{\Orth(B)}(P)\right)}} = \frac{46\,998\,591\,897\,600}{247\,726\,080} = 189\,720 = 8\cdot 23\,715
,$$
and the two agree because $\abs{\Orth(q)}/\abs{S} = \left(\abs{\Orth(q)}/\abs{F}\right)\left(\abs{F}/\abs{S}\right) = 23\,715\cdot 8$ with $F = \Stab_{\Orth(q)}(J)$ and $S = \rho\left(\Stab_{\Orth(B)}(P)\right)$ of @thm:plane-fibre(1). The driver's own note records that its order formula was validated against those two Coble orders.

*The cusp rows and the incidence row.* The driver is `tests/coble_gamma_co_2_incidence_rows.py` at `3147ea330f1f91bef3ae20006210dcbdc4456323`, and the two rows run `cusps(1)`, `cusps(2)` and `tits_building_incidence()` on `Tco.Aut()` and on `Tco.Aut().discriminant_point_stabilizer(point)`, the point being the span of the classes of the two $U(2)$ module generators; that last call is $\rho_{T_\Co}^{-1}$ of the setwise stabilizer of the point, which by @prop:coble-cong-point-stabilizer(1) is $R_{\gent}$; the row's label `Gamma_{Co,2}` names this arithmetic group, not the monodromy group $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5). The incidence returned is the endpoint relation of @prop:coble-flag-orbits-and-edges(2), the driver retaining one flag certificate per pair of endpoints and asserting of each certificate that its line lies in its plane, that one element of the group carries the line cusp representative into the plane cusp representative, that no two edges share both endpoints, and that every line cusp and every plane cusp carries an edge. Run 43556671111 reports, for $\Orth(T_\Co)$, one line cusp, one plane cusp and one edge in $188.5$ s --- @thm:unpolarized-cusps and @thm:plane-transitivity-tco certified at one plane --- and, for the row it labels `Gamma_{Co,2}`, that is for $R_{\gent}$, four line cusps, seven plane cusps and thirteen edges in $2195.2$ s. The four is @prop:coble-cong-point-stabilizer(3), proved on the page independently of the run. The seven is @cor:coble-heegner-integral-plane-descent, proved on the page as well, and the run reproduces it rather than supplying it. The thirteen is the run's, and what the run counts is its *edge* count: the thirteen flag orbits are the corollary's and are a different object, by @prop:coble-flag-orbits-and-edges(3). No count in this remark is read off a card. The seven and the thirteen are also recomputed from the discriminant module alone, without the provider, in `computations/reports/coble_a2-plane-flag-orbit-reproduction.py`, whose transcript records the same seven decorated-plane orbits and the same thirteen flag orbits with the sizes listed above.

*What the rows do not establish.* The public endpoint row does not itself establish the $13$ flag orbits of $R_{\gent}$: that independent count is @cor:coble-heegner-integral-plane-descent, from the exact finite triple-orbit computation. The distinction is not academic: the row's earlier run 43540655128 printed $15$, counting flag-cover candidates, and that number depends on the double-coset representatives the row picks, so it is neither the $13$ flag orbits nor the $13$ edges that the accepted run 43556671111 returns (@prop:coble-flag-orbits-and-edges(3)). The incidence rows of the two kernel subgroups, owned by sage-extensions#381: [run 44012568639](https://github.com/dzackgarza/sage-extensions/actions/runs/44012568639) at `921dcf6ed7b921ff78479cd4eb067008e2eff42a` completed unsuccessfully on 2026-11-17. The process running `tests/coble_gamma_co_2_incidence_rows.py --rows Otilde,Otilde+ --lattice Tco` was killed with exit code $137$ after approximately two hours and twenty-four minutes, without printing either incidence row. Thus that run did not return either public kernel incidence row; neither row can be inferred merely from the public plane counts. Independently, @cor:coble-eight-standard-line-counts proves the kernel incidence graph has $569\,160$ edges and is $(1080,3)$-biregular, using the integral lifting theorem and its injective flag-to-endpoint map. The checker `computations/reports/coble_kernel_public_incidence_audit.py` reads the two actual public row logs and tests these numbers, all edge endpoint classes, and the integral Gram, primitivity and inclusion conditions of every printed edge witness. It accepts neither an incomplete row nor a synthetic count in place of public witnesses. The alternative `tits_building_incidence_by_divided_classes()` route introduced on sage-extensions main at `8fc0f49ef178d448fbfcab90655ac893fcb4d6b5` computes endpoint pairs without retaining an integral flag or subgroup transporters per edge; its output alone therefore cannot be read as a successful run of this integral-witness checker. The independent [public divided-class run 44098720620](https://github.com/dzackgarza/sage-extensions/actions/runs/44098720620), on `6b8f2822869633f55ad8692f0225b344b6b75991` with Sage 11.0.beta5, also failed: the process was killed with exit code $137$ on 2026-11-17 after approximately 106 minutes, before printing either kernel row. Thus that run of the class-only implementation did not return the required public endpoint relation either; its lower retention of flag/transport objects did not suffice for that execution. The checker's explicit `--class-only` mode verifies that divided-class endpoint relation against the integral cusp representatives and the finite incidence criterion, while leaving the missing integral transporter certificates unasserted. The theorem-derived values are not read off a returned edge list: the endpoint relation has since returned both kernel rows with exactly these counts (job 44392429173, below), while the integral transporter certificate of each edge is the certificate route's clause and is not asserted for them. And the count for $\fco$ itself: $\Gamma_\Co$ is the monodromy group of the VHS on the universal family over the moduli stack of Coble surfaces, and $\Gamma_\Co(B) = \widetilde\Orth^+(T_\Co)$ on the labelled presentation (@def:gamma-co-groups(1), @thm:gamma-co-is-stable), so $189\,720$ is the number of $1$-cusps of $\fco$ once $\Gamma_\Co=\Gamma_\Co(B)$ (research#797, item 6); $R_{\gent} = \bar\rho^{-1}(P)$ is the restricted stabilizer (@prop:gamma-co-images(3)); of the monodromy group $\Gamma_{\Co,2}$ only the containment $\Gamma_{\Co,2}\subseteq R_{\gent}\intersect\Orth^+(T_\Co)$ is asserted (@thm:coble-monodromy-versus-enriques(4)), and no inclusion between it and $\Gamma_\Co$ is asserted. The counts above are $R_{\gent}$'s, and the cusps of $F_{\Co,2} = \bD(T_\Co)/\Gamma_{\Co,2}$ are $\Gamma_{\Co,2}$'s own, equal to these only under @qst:coble-monodromy-equality (@prop:coble-cong-point-stabilizer(3) for the $0$-cusps).

The later [public run 44135163725](https://github.com/dzackgarza/sage-extensions/actions/runs/44135163725), at source `34c9be895206eb7756de3411eb4d8b0d1c53b059`, likewise returned no kernel incidence row: the divided-class $\widetilde\Orth(T_\Co)$ call exceeded its $10\,800$-second cap on 2026-11-17, and the workflow exited with code $1$. Its timing artifact records $3199.79$ seconds for the rank-two coset splitting and transport, and an additional uninstrumented interval of approximately $1$ hour $54$ minutes between completion of the rank-one coset stage and commencement of the rank-two stage. This is a time-cap failure, not evidence of memory exhaustion. Neither the newer run nor the earlier ones returned a public integral incidence row.

**The relation has returned, and both kernel rows are decided.** Image job [44392429173](https://github.com/dzackgarza/sage-extensions/actions/runs/44392429173) --- workflow `.github/workflows/coble-kernel-incidence-rows.yml` #37 at sage-extensions main `0bbf022b6bf72e5a1d1f3267f3b7481fc19ba49f`, dispatched 2026-11-18 20:34 --- completed successfully in $2$ h $20$ m $26$ s, both of its matrix jobs completed, their names `Public incidence row Otilde` and `Public incidence row Otilde+`. A job of that matrix runs one row under `fail-fast: false`, and a row ends non-zero on every status but `decided` (`tests/coble_row_status.py`: undecided $1$, contract violation $2$, count mismatch $3$, error $4$), so a green job is a decided row. On $T_\Co$ the driver refuses a kernel row unless every one of the $527$ line cusps carries degree $1080$, every one of the $189\,720$ plane cusps carries degree $3$, every cusp of both rows carries an edge, no two edges share both endpoints, and the row's counts are exactly $(569\,160,\,527,\,189\,720)$ (`tests/coble_gamma_co_2_incidence_rows.py:530-548`, `:842-849` at that commit). So both kernel incidence rows returned decided, with $569\,160$ edges each over $527$ line cusps and $189\,720$ plane cusps --- the count, the degrees and the two vertex rows that @cor:coble-eight-standard-line-counts and @cor:coble-zero-one-cusp-incidence prove. The three runs of the paragraph above are the history of this item and are superseded by this one.

*What the green does not put on this page.* The rows' per-edge records, the route each row took, and the numbers as printed are in the run's log, which needs signing in to that repository, and in its two retained artifacts, which are the timing records; no comment and no file under `results/` on sage-extensions main prints them. A row on the divided-class route states the endpoint relation and keeps no integral transporter per edge, so the transporter clause that `computations/reports/coble_kernel_public_incidence_audit.py` requires is not asserted for these rows unless the run took the certificate route --- which its log would say, and which this page therefore does not claim. And the card application is not made by any of it: lattice-database#7 carries no `T_Co` incidence value, its arithmetic-group cards still lack the integral generator morphisms, and it remains open against its own acceptance.

The [independent integral certificate workflow 44170494099](https://github.com/dzackgarza/research/actions/runs/44170494099), on research commit `c08aeb6baa98cfcd2a39c46141432f4ce9c92661`, completed successfully on 2026-11-17. Its $32$ disjoint shard jobs generated all $569\,160$ explicit integral flag transporters, each with an exact $11\times11$ kernel matrix, a spinor-reversing flag stabilizer, a spinor-positive matrix and the parabolic correction word. Every shard passed the independent exact-integer verifier. The final job downloaded all $32$ artifacts, checked their SHA-256 digests, replayed every transporter in four verifier processes, checked that the indices partition the $23\,715$ finite planes and that all $569\,160$ flags occur, and printed `independently certified complete integral kernel incidence: 569160 edges`. The full compressed certificate is retained as the run artifact `coble-complete-integral-flag-certificate` (artifact ID `14371631974`, $542\,141\,291$ bytes). This is a complete research-side integral witness computation and is not the public row itself: the separate public `tits_building_incidence()` operation has since returned both kernel incidence rows (job 44392429173, above), and what these certificates add is the exact integral transporter of every one of the $569\,160$ edges, which the returned row's route need not keep. The lattice-database group-card generator fields are separately certified at commit `a784518254`.

The [full integral-to-$\Gamma_{\Co,2}$ quotient audit 44187809226](https://github.com/dzackgarza/research/actions/runs/44187809226), on research commit `5edb967bc6cc06f0488d267303b0daea1bb82859`, independently downloaded and rehashed the $32$ original archives, inverted the integral diagonal-to-standard basis change, reconstructed each of the eight integral plane stars, and classified **all $569\,160$ archived integral flag witnesses** under the nine-generator finite $G_\Co$ action. The resulting $13$ orbit cardinalities are
$$
2160,\ 2160,\ 2160,\ 7560,\ 9450,\ 15120,\ 22680,\ 28350,\ 45360,\ 69120,\ 75600,\ 138240,\ 151200.
$$
They equal the independent finite Schreier orbit sizes, and the $13$ flag orbits have $13$ distinct pairs of line and plane orbit endpoints. The CI job succeeded at 2026-11-17 22:19:41 UTC, retaining artifact `coble-integral-flag-quotient-proof` (ID `14375827131`); its verbatim $38$-line transcript is committed as `computations/reports/coble_integral_flag_quotient-run.txt`. This checks the actual complete integral witness family against the $\Gamma_{\Co,2}$ quotient, rather than comparing independently computed total counts. It remains a research-side certificate, not a returned public Sage-extensions subgroup-incidence row.

The eight seed stars used by these complete-family computations are also checked directly in `computations/reports/coble_plane_integral_star_section.py` (research commit `e27bf36b4c`): for each of the seven nontrivial seed reflections, the seven norm-$-1$ vectors of the primitive perpendicular quotient are reflected integrally, and their seven six-fold sum classes modulo the common isotropic plane are required to equal the corresponding finite star. The identity seed is constructed from the same negative quotient basis. Thus the eight star labels are tied to actual integral quotient bases, not just permuted finite labels; transport by the verified integral root words propagates this identity to every finite plane.

The stronger [public-edge-weighted audit 44189878302](https://github.com/dzackgarza/research/actions/runs/44189878302), on commit `712e5be4409d6c9790d04a5ed3810fc2524a494d`, also completed successfully on 2026-11-17 at 22:31:57 UTC. It identified each of the $569\,160$ archived integral flags with an **actual public** $\Gamma_{\Co,2}$ line/plane incidence edge, using the unique graph isomorphism determined by the published integral plane-star invariants. The multiplicities, in the public cusp indices of sage-extensions run 43556671111, are

| Public edge | Integral flags | Public edge | Integral flags |
| --- | ---: | --- | ---: |
| $L_0<P_0$ | $2160$ | $L_1<P_1$ | $69120$ |
| $L_1<P_3$ | $45360$ | $L_1<P_5$ | $15120$ |
| $L_2<P_0$ | $2160$ | $L_2<P_2$ | $75600$ |
| $L_2<P_3$ | $22680$ | $L_2<P_4$ | $28350$ |
| $L_2<P_5$ | $7560$ | $L_2<P_6$ | $9450$ |
| $L_3<P_0$ | $2160$ | $L_3<P_1$ | $138240$ |
| $L_3<P_2$ | $151200$ | | |

The $13$ distinct edge labels agree exactly with the public incidence graph, and the weights sum to $569\,160$. The independently produced CI transcript is committed as `computations/reports/coble_integral_public_edge_multiplicities-run.txt` and retained as artifact `coble-integral-flag-quotient-proof` (ID `14377530380`). This establishes the direct numerical correspondence of the complete integral kernel flag family with the public $\Gamma_{\Co,2}$ graph; it does not certify the public $\widetilde\Orth(T_\Co)$ or $\widetilde\Orth^+(T_\Co)$ incidence rows, which have since returned as an endpoint relation (job 44392429173, above), and it is not their certificate.

**Integral parabolic generators versus their finite image.** The $21$ matrices stored in `coble_plane_integral_star_section.json` generate the full *finite discriminant image* of the standard plane stabilizer, but do not themselves generate the entire integral stabilizer: they omit the seven sign changes $d_i\mapsto-d_i$ in $\Orth(\generators{-1}^{7})$. The independent Sage certificate `computations/reports/coble_complete_plane_parabolic_generators.py` adjoins precisely these seven norm-$-1$ reflections, checks all $28$ matrices preserve the integral Gram form and the plane, and verifies that the seven new reflections are congruent to the identity modulo $2$. Their addition therefore leaves the proven finite image order $247\,726\,080$ unchanged. Conjugating the twelve existing Eichler transvections with these sign changes produces the coefficient vectors $d_i-d_7$ alongside $d_i+d_7$ for $1\leq i\leq6$; these span $D^{\mathrm{ev}}$ (a determinant-$2$ sublattice of $D$), supplying the full integral unipotent coefficient lattice. Together with the central shear and $GL_2(\ZZ)$ generators, the enlarged family generates the entire split parabolic described in @thm:coble-plane-stabilizer-image(1), not just its finite reduction. The separate script deliberately does not alter the archived $569\,160$ transporter witnesses or their source SHA-256 values.

The exact proper-image index is independently verified in `computations/reports/coble_proper_plane_stabilizer_image.py`, with immutable transcript `computations/reports/coble_proper_plane_stabilizer_image-run.txt`. This calculation constructs $Q=\rho(\Orth(T_\Co))$ as a permutation group on all $527$ singular classes from the ambient root reflections, computes $F=\Stab_Q(J)$ for the standard finite plane $J$, and separately computes $S$ from the complete $28$ **integral** parabolic generators. It verifies $S\subset F$ by generator membership and obtains the exact orders $\abs Q=46\,998\,591\,897\,600$, $\abs F=1\,981\,808\,640$, $\abs S=247\,726\,080$. Consequently $[F:S]=8$ and $[Q:S]=189\,720$. This verifies the *proper* integral image directly in the same finite group, rather than assuming that the integral stabilizer maps onto the entire finite-plane stabilizer. Moreover, the same computation recovers the $10$-dimensional characteristic-perpendicular action from ten independent singular classes, applies the finite-plane stabilizer $F$ to the $28$ nonsingular representatives of the standard characteristic star, and verifies that its orbit is **exactly the eight** integral stars of the canonical certificate. Every generator of $S$ fixes the standard star. Thus the eight stars are precisely the $F/S$ cosets, not merely eight labels with the correct cardinality. More precisely, $S\subseteq\Stab_F(\mathcal S_0)$ by its exact integral generator action, while the orbit of $\mathcal S_0$ has eight elements and $[F:S]=8$; orbit–stabilizer forces the equality $S=\Stab_F(\mathcal S_0)$. The verifier also outputs and replays eight explicit short words in the ordered finite $F$ generators representing the $F/S$ cosets, in the same order as the eight integral stars. In the pinned Sage realization the words are $(),(9,6),(9),(9,12,4,5),(9,12,4),(9,7),(9,12),(0)$, with zero-based generator indices; each is checked to send the standard star to its assigned integral star. The complete ordered finite generators (as explicit permutations of all $527$ singular classes), the eight characteristic stars, their eight explicit integral primitive plane bases in the standard $B$-basis, and these coset words are retained together with all $23\,715$ finite-plane representatives and their integral reflection words in the source-hashed artifact `computations/reports/coble_proper_plane_stabilizer_image.json` (about $1.7$ MB). Thus the data give, for every finite plane class $J\prime$, an explicit integral transporter from the standard plane and the eight integral lifts indexed by $F/S$, without reconstructing GAP's choice of generator ordering. The stored flag coefficients $(1,0),(0,1),(1,1)$ then give all three primitive line representatives in each of the $189\,720$ planes, and hence all $569\,160$ integral incidence flags. The same artifact also retains the ten integral reflection roots and the standard Gram matrix needed to replay all $23\,715$ transport words, together with the independently source-hashed public $\Gamma_{\Co,2}$ representatives from workflow $43556671111$: its $4$ line representatives, $7$ plane bases, and $13$ incidence edges. The exact original $53$ KB public workflow log is archived as `computations/reports/coble_gco_public_incidence_source-run.log`, and its SHA-256 is checked against the extracted representative JSON. Each of the $13$ edge records also retains its actual integral line/plane witness pair (which need not be the chosen standalone orbit representatives); the generator checks their isotropy, primitivity, and integral line-in-plane coordinates directly. The artifact labels the two kernel subgroups $\widetilde{O}$ and $\widetilde{O}^{+}$ as having the same plane/flag orbit sets (the no-splitting proof in (5)), with counts $(527,189\,720,569\,160)$, and records the public $\Gamma_{\Co,2}$ counts $(4,7,13)$. Thus the finite-to-integral transport data and all three requested subgroup rows have their exact integral representative data in one self-contained package. The Sage regression also regenerates this artifact byte-for-byte. The independently dispatched [GitHub Actions run 44199540950](https://github.com/dzackgarza/research/actions/runs/44199540950) on source commit `ab8535091d925614b21e683660f99d51e2914b64` passed both exact Sage regressions in $17.93$ seconds on the pinned Sage image, verifying byte-for-byte regeneration of the complete $28$-matrix parabolic and the full finite $F/S$ coset artifact. The workflow completed successfully on 2026-11-17 at 23:32:20 UTC. It supplies the precise proper-image input required for the public plane-orbit double quotient.

**Permanent complete-witness archive.** The full $32$ compressed witness shards ($541\,965\,486$ bytes, exactly $569\,160$ records) are now published as [release `coble-integral-flags-v1`](https://github.com/dzackgarza/research/releases/tag/coble-integral-flags-v1), not merely retained as expiring GitHub Actions artifacts. Before publication, each archive was independently rehashed against the source manifest; after publication, `shard-0.jsonl.gz` was independently downloaded and its SHA-256 verified again. The complete set of $32$ release asset identifiers, canonical download URLs, sizes and source SHA-256 values is retained in `computations/reports/coble_integral_flag_permanent_release.json`, with a regression checking the full manifest-to-release correspondence. The archive is a reproducible mathematical witness record, not a substitute for the maintained public Sage operation.

The permanent provenance ledger `computations/reports/coble_integral_flag_certificate_manifest.json` retains the SHA-256 of each of the $32$ compressed shards and its uncompressed record stream, the exact per-shard edge counts, the source certificate digests, the producing commit, the archived artifact ID and the Sage image digest. The hashes were independently recomputed from all $32$ downloaded workflow artifacts; the image digest `sha256:12e5716067b5cf2fd34c00e9ba97e9c09d51a70664de817f4ae29743b64c5f61` was independently read from all $32$ shard job logs and was identical in each. The manifest is also checked against the committed source certificates by `test_complete_integral_flag_certificate_manifest`. To verify a downloaded archive, run the independent checker with `--shards shard-*.jsonl.gz --manifest computations/reports/coble_integral_flag_certificate_manifest.json`; this checks both byte identity with the archived certificate and the mathematical content of every transporter.

As an additional cross-revision reproducibility check, the later deterministic-gzip producer on research main regenerated the **entire** shard $4/32$ (all $17\,784$ integral flags). Its uncompressed JSONL record-stream SHA-256 was `bae2df20435b33c8f8c0fb71237965367290e9025c8a8599bca878dfebc4ee4b`, identical to the original archived shard's manifest entry. The compressed-file SHA-256 differs because the later producer intentionally removes the gzip timestamp and embedded filename; this does not change any transporter record.

The independent strict public-row audit `computations/reports/coble_kernel_public_incidence_audit.py` now requires, for **every** kernel incidence edge, an exact $11\times11$ integral transporter from its indexed line representative to its displayed flag vector. It checks the full integral Gram identity, reduction to the identity on $A_{T_\Co}$, exact line-to-flag action, and for $\widetilde\Orth^+$ the positive orientation of the real positive two-plane. A row containing only an integral line inside an integral plane is not an accepted kernel-transporter certificate. The parameterized constructive section of @prop:coble-explicit-kernel-flag-transport supplies the mathematical method for producing these matrices; the maintained public operation returns the endpoint relation (job 44392429173, above), and it certifies these matrices only on the certificate route, which the run's log would name and which this page does not claim.

:::

::: {.remark #rmk:coble-plane-incidence-row-provenance title="The revisions the two runs bound, and the ones they do not"}
Both workflows run in the container `ghcr.io/dzackgarza/sage:develop` and install nothing: the step puts `src` on `PYTHONPATH` and runs the driver from the checkout, so the `sage_extensions` code a row imports is the dispatched commit's, and the workflow head is the revision of that code. It is not the revision of the runtime underneath. The tag `develop` is a moving tag, each log records the manifest digest it pulled, and the two runs pulled different ones: `sha256:84037cf751ae0762b0734d65e9df2b5bcfc1cfec964eb464bcb91d79fb4a1fed` for run 43798731423 and `sha256:40697f55c8a03ce5bc913afdd0acb89f879c4b168ab076ff0a9a4fc348fa7874` for run 43556671111. Each number therefore belongs to the pair of its commit and its image digest, and to no other pair; the Sage version both logs print, `11.0.beta5`, identifies the build no more tightly than that.

The durations are the runs' own. The body of `3147ea330f1f91bef3ae20006210dcbdc4456323` also records `95.1` s for the $\Orth(T_\Co)$ row, `1449.3` s for the $\Gamma_{\Co,2}$ row and a pinned baseline of thirteen pairs in `1599.3` s; those are other runs, and the durations of run 43556671111 are the `188.5` s and `2195.2` s its own log prints.
:::

### The reflective set of the stable group {#sec-gamma-co-reflective-set}

::: {#not:discriminants-of-twists-by-2 .notation title="Discriminants of twists by $2$" defines="$T_\Co^*$; $S_\En^*$"}
$T_\Co = B(2)$ and $S_\En = C(2)$ are twists (@def:form-twist) by $2$ of unimodular lattices (@def:unimodular), so their duals are half of them,
$$
T_\Co^* = \tfrac12 T_\Co \subset T_\Co\tensor\bQ,
\qquad
S_\En^* = \tfrac12 S_\En
,
$$
and $A_L = L^*/L = (\tfrac12 L)/L\cong L/2L$.
Under that identification the discriminant action of $g\in\Orth(L)$ is reduction modulo $2$, so
$$
\rho_L(g) = \id \quad\Longleftrightarrow\quad g\equiv\id \pmod 2
.
$$
The pairing of two vectors of $L^*$ lies in $\tfrac12\ZZ$.
By @def:2elementary-roots, the roots of the $2$-elementary lattice $T_\Co$ are the short roots, of square $-2$, and the long roots, of square $-4$ and divisibility (@def:lattice-divisibility) $2$.
:::

::: {.definition #def:reflective-set title="The reflective set of an arithmetic group" defines="reflective set"}

Let $T$ be an even lattice (@def:even-lattice) and $\Gamma\leq\Orth(T)$. The *reflective set* of $\Gamma$ is the set of primitive vectors $v\in T$ with $v^2\neq0$ whose reflection $s_v\colon x\mapsto x-2\frac{(x,v)}{v^2}v$ is an element of $\Gamma$.
:::

::: {.proposition #prop:gamma-co-reflective-set title="The reflective set of the stable Coble group"}

Let $T_\Co = B(2)$ be the Coble lattice of @prop:tco-as-twist, even of signature $(2,9)$ and determinant $-2048$, so that every primitive vector of $T_\Co$ has divisibility $2$ (@lem:divisibilityAlwaysTwoTco), and let $\widetilde\Orth^+(T_\Co) = \Orth^+(T_\Co)\intersect\ker\rho_{T_\Co}$, with $\Orth^+(T_\Co) = \Theta_\bR(T_\Co)$ of @def:lattice-spinor-kernels and $\spinornorm_\bR$ the real spinor norm of @def:spinor-norm.
Write $s_v$ for the reflection of @def:spinor-norm in a nonisotropic vector $v$.
Then, for a primitive $v$, $s_v$ is an isometry of $T_\Co$ exactly for $v^2\in\{2,-2,4,-4\}$, and among those:

1. if $v^2 = -2$ then $s_v\in\widetilde\Orth^+(T_\Co)$; hence the short roots generate a subgroup
   $$
   W(T_\Co) \definedas \generators{\,s_v \;:\; v \in T_\Co,\ v^2 = -2\,}
   \iscontainedin \widetilde\Orth^+(T_\Co)
   ,$$
   which is infinite;
2. if $v^2 = 2$ or $v^2 = 4$ then $s_v\notin\Orth^+(T_\Co)$, hence $s_v\notin\widetilde\Orth^+(T_\Co)$; for $v^2 = 2$ one has in addition $s_v\in\ker\rho_{T_\Co}$, and for $v^2 = 4$ never;
3. if $v^2 = -4$ then $s_v\in\Orth^+(T_\Co)$ and $s_v\notin\ker\rho_{T_\Co}$.

Consequently the reflective set (@def:reflective-set) of $\widetilde\Orth^+(T_\Co)$ is exactly the set of primitive short roots, which is every vector of square $-2$, and no long root (@def:2elementary-roots) lies in it.
:::

::: {.proof}

*Integrality.*
A primitive $v$ has $\div_{T_\Co}(v) = 2$ (@lem:divisibilityAlwaysTwoTco), so $\beta(v,T_\Co) = 2\ZZ$; then $2\beta(x,v)/\beta(v,v)$ is an integer for every $x\in T_\Co$ exactly when $\beta(v,v)$ divides $4$, because $2\beta(x,v)$ runs over $4\ZZ$ while $\beta(v,v)$ need not divide it.
So for primitive $v$ the reflection is integral exactly for $v^2\in\{2,-2,4,-4\}$.
Primitivity cannot be dropped from that clause: $s_v$ depends only on the line $\ZZ v$, so $v = 2w$ with $w^2 = -2$ has $v^2 = -8$ and $s_v = s_w$, which is integral.
The real spinor norm of @def:spinor-norm is $\spinornorm_\bR(s_w) = [-\tfrac12\beta(w,w)]$ for any nonisotropic $w$, so $\spinornorm_\bR(s_v)$ is $[-1]$ for $v^2 = 2$, $[1]$ for $v^2 = -2$, $[-2] = [-1]$ for $v^2 = 4$, and $[2] = [1]$ for $v^2 = -4$.

(1) For $v^2 = -2$ the reflection is $s_v(x) = x + \beta(x,v)v$.
The spinor norm is $[1]$, so $s_v\in\Theta_\bR(T_\Co)$.
For $x^*\in T_\Co^*$ the pairing $\beta(x^*,v)$ is an integer, because $x^*$ pairs integrally with every element of $T_\Co$ and $v$ lies in $T_\Co$; hence $s_v(x^*)-x^* = \beta(x^*,v)v\in T_\Co$ and $\rho_{T_\Co}(s_v) = \id$.
So $s_v\in\widetilde\Orth^+(T_\Co)$.
The group (@def:group) $W(T_\Co)$ is infinite, because distinct lines $\ZZ v$ give distinct reflections and there are infinitely many such lines: for odd $a\in\ZZ$,
$$
x_a \definedas a\zeta + e' - \tfrac{a^2+1}{2}f'
\qquad\text{has}\qquad
x_a^2 = 2a^2 + 4\cdot\Bigl(-\tfrac{a^2+1}{2}\Bigr) = -2
,$$
since $\zeta$ is orthogonal to the $U(2)$ summand and $\beta(e',f') = 2$ there.

(2) Both squares give $\spinornorm_\bR(s_v) = [-1]$, which is not the identity of $\bR^\times/(\bR^\times)^2$, so $s_v\notin\Theta_\bR(T_\Co)$ and hence $s_v\notin\widetilde\Orth^+(T_\Co)$.
For $v^2 = 2$ the reflection is $s_v(x) = x - \beta(x,v)v$, and $\beta(x^*,v)\in\ZZ$ for $x^*\in T_\Co^*$, so $s_v(x^*)-x^*\in T_\Co$ and $s_v\in\ker\rho_{T_\Co}$: such a reflection is discriminant-trivial and fails only the component condition.
For $v^2 = 4$ it never is.
In the coordinates of $B$ one has $b_B(v,v) = 2$ and $s_v(x) = x - b_B(x,v)v$; $B$ is unimodular and $v$ primitive, so $b_B(\cdot,v)$ is unimodular and some $x$ has $b_B(x,v) = 1$, whence
$$
s_v(x) - x = -v \notin 2B
,$$
so $s_v\not\equiv\id\bmod 2$ and $\rho_{T_\Co}(s_v)\neq\id$ — the argument of (3), with the sign of the coefficient reversed.

(3) Let $v^2 = -4$, and write the same reflection in the coordinates of $B$, where $b_B = \tfrac12\beta_{T_\Co}$ and $b_B(v,v) = -2$; then
$$
s_v(x) = x + b_B(x,v)\,v
\qquad (x\in B = T_\Co).
$$
$B$ is unimodular and $v$ is primitive, so the functional $b_B(\cdot,v)$ is unimodular and some $x\in B$ has $b_B(x,v) = 1$; for that $x$,
$$
s_v(x) - x = v \notin 2B
,$$
because $v$ is primitive.
Under the convention above, $A_{T_\Co} = B/2B$ and $\rho_{T_\Co}(g) = \id$ means $g\equiv\id\bmod 2$; so $\rho_{T_\Co}(s_v)\neq\id$ and $s_v\notin\widetilde\Orth^+(T_\Co)$.
With (2) this excludes the two positive squares and the long roots, leaving exactly (1), and the reflective set is the short roots.
:::

::: {.lemma #lem:minus-two-vectors-use-the-two-summand title="Every $(-2)$-vector of $T_\Co$ has odd coefficient on the $\langle2\rangle$ summand"}

Write $T_\Co = \langle\zeta\rangle\perp U(2)\perp E_8(2)$ with $\zeta^2 = 2$ (@prop:coble-transcendental), and let $v = a\zeta + u + w$ with $u\in U(2)$ and $w\in E_8(2)$. Then
$$v^2 \equiv 2a \pmod 4,$$
and consequently every vector of $T_\Co$ of square $-2$ has $a$ odd and in particular $a\neq0$. So

1. no vector of the sublattice $U(2)\perp E_8(2)$ has square $-2$, and no reflection in such a vector lies in $W(T_\Co)$;
2. the reflection in an $E_8(2)$-vector of square $-4$, in particular the reflection used to write $-\id_{E_8(2)}$ as a product of eight of them, is not in $W(T_\Co)$ — it is not even in $\ker\rho_{T_\Co}$ (@prop:gamma-co-reflective-set, part 3).
:::

::: {.proof}

$u^2 = 2ab\cdot2\equiv0\pmod4$ for $u = ae' + bf'$ in $U(2)$ with $e'\cdot f' = 2$, and $w^2\in4\ZZ$ because $w = 2w'$ for $w'\in E_8(-1)$; $a^2\equiv a\pmod 2$, so $v^2 = 2a^2 + u^2 + w^2\equiv2a\pmod4$. For $v^2 = -2\equiv2\pmod4$ this gives $2a\equiv2$, that is $a$ odd.

(1) A vector of $U(2)\perp E_8(2)$ has $a = 0$, so its square is divisible by $4$ and is not $-2$; $W(T_\Co)$ is generated by the reflections in the classes of square $-2$ (@prop:gamma-co-reflective-set, part 1).

(2) is that part of the same proposition: for $v^2 = -4$ the reflection lies in $\Orth^+(T_\Co)$ and outside $\ker\rho_{T_\Co}$, while the reflections in the classes of square $-2$ lie in the kernel, so it is not a word in them.

The mod-2 count agrees: of the $1024$ classes of $A_{T_\Co}$ whose $\beta$-square is $-2$ modulo $4$, none has $\zeta$-coefficient zero (`computations/reports/coble_663-rel-level2-shadow-run.txt` computes the same class set (@def:genus)).
:::

::: {.remark #rmk:longest-element-route-closed title="Why the longest element of $W(E_8)$ does not put the block sign in $W(T_\Co)$"}

The natural attempt on the membership query of research#720 (REL) is this, and what it refutes is the transport, not the membership: $\delta_{E_8}\in W(T_\Co)$ is now @thm:coble-block-sign-in-w, by an argument that uses no word in $W(E_8)$. The block sign $\delta_{E_8} = -\id_{E_8(2)}$, extended by the identity, is the image of the longest element of $W(E_8)$, which is $-\id$ — its exponents $1,7,11,13,17,19,23,29$ are all odd and $w_0 = -1$ [@Bou08, Ch. VI, §4, no. 10]. One would like to read that as $\delta_{E_8}\in W(T_\Co)$ by transporting the word through the isomorphism $E_8(2)\cong 2E_8(-1)$.

That transport is invalid, and @lem:minus-two-vectors-use-the-two-summand is why: the reflections generating $W(T_\Co)$ are those in vectors of square $-2$, and every such vector has odd coefficient on $\langle\zeta\rangle$; the reflections in $E_8(2)$'s own vectors have square $-4$ and lie outside $\ker\rho_{T_\Co}$. So the $E_8(2)$ summand carries no generator of $W(T_\Co)$ at all, and the query cannot be answered inside it. What the lemma does give in the other direction is a constraint on any positive answer: a word for $\delta_{E_8}$ has to use vectors with nonzero $U(2)$ and $\langle\zeta\rangle$ parts, and those act nontrivially on the other summands in general.
:::

::: {.lemma #lem:block-sign-reduces-to-gamma-four title="The block sign is a word in the reflections times an explicit element of $\Gamma(4)$"}

Let $T_\Co = \langle2\rangle\perp U(2)\perp E_8(2)$, let $h(g) = (g-\id)/2$ be the level-two shadow of @prop:level-two-shadow-consistent-with-both-answers, and let $\delta_{E_8}=\id_{\langle2\rangle\perp U(2)}\oplus(-\id_{E_8(2)})$ be the block sign of @warn:block-signs-not-both-in-w. Then the $\F_2$-span of the $h(s_v)$ over the classes of $T_\Co$ that carry a vector of square $-2$ has dimension $55$, it contains $h(\delta_{E_8})$, and consequently there are

1. a product $w$ of $14$ reflections in classes of square $-2$ — hence $w\in W(T_\Co)$, verified as an exact isometry of $T_\Co$ — with $w\equiv\delta_{E_8}\pmod 4$, listed in `computations/reports/coble_663-rel-gamma4-reduction-run.txt`;
2. an element $k\definedas w^{-1}\delta_{E_8}$ with $k\equiv\id\pmod 4$, so $k\in\Gamma(4)$, integral and an exact isometry, and $k\neq\id$.

Hence $\delta_{E_8} = wk$ and
$$\delta_{E_8}\in W(T_\Co)\iff k\in W(T_\Co),$$
so the membership query of research#720 (REL) is a question about one explicit element of $\Gamma(4)$ and not about the arrangement of the root system. (The query is now answered, by a different route: @thm:coble-block-sign-in-w.)
:::

::: {.proof}

$h(s_v)$ depends only on $v\bmod 2$: it is $x\mapsto b_B(x,v)v$ with $T_\Co = B(2)$. So the span is computed over the finitely many classes that carry a vector of square $-2$; the enumeration of `computations/reports/coble_663-rel-gamma4-reduction.py` collects $50\,732$ such vectors realising $494$ classes, and elimination over $\F_2$ gives dimension $55$ and a certificate of $14$ classes for $h(\delta_{E_8})$.

The corresponding product $w = \prod s_{v_i}$ satisfies $h(w)\equiv\sum h(s_{v_i})\equiv h(\delta_{E_8})\pmod 2$, because $h(g_1g_2)\equiv h(g_1)+h(g_2)$ on the congruence subgroup (@prop:level-two-shadow-consistent-with-both-answers, part 1); hence $w\equiv\id+2h(\delta_{E_8}) = \delta_{E_8}\pmod 4$. The script verifies both steps exactly, on integer matrices: every factor satisfies $R^{\mathsf T}GR = G$, the product satisfies $(w-\delta_{E_8})\equiv0\pmod 4$, and $k = w^{-1}\delta_{E_8}$ is integral, is an isometry, satisfies $k\equiv\id\pmod4$, and is not the identity.
:::

::: {.proposition #prop:level-two-shadow-consistent-with-both-answers title="The level-two shadow is consistent with both answers to the block-sign query"}

Let $T_\Co = B(2)$ and let $h(g)\in\End_{\F_2}(B/2B)$ be defined by $g = \id + 2h$ for $g\in\Orth(T_\Co)$ congruent to the identity modulo $2$. Then

1. $W(T_\Co)$ lies in that congruence subgroup, and $h(s_v)\neq0$ for every $v$ of square $-2$;
2. $h(\delta_{E_8})$ is the projection onto the eight $E_8(2)$-coordinates, so it is nonzero, and it lies in the $\F_2$-span of the $h(s_v)$, which has dimension $56$;
3. hence no linear functional $\lambda$ of $h$ takes the value $0$ on $W(T_\Co)$ and a nonzero value at $\delta_{E_8}$: the shadow separates neither $\delta_{E_8}$ from $W(T_\Co)$ nor its negation. That limitation is now immaterial: $\delta_{E_8}\in W(T_\Co)$ and so do $\iota$ and $\epsilon$ (@thm:coble-block-sign-in-w), and the span of the $h(s_v)$, which contains all three, was never going to distinguish them.

So the level-two information was consistent with both answers to (REL)'s query and could decide neither; the query is now decided by an arithmetic argument of a different kind (@thm:coble-block-sign-in-w). That rules out the level-two family of arguments; the other natural attempt, through the longest element of $W(E_8)$, is closed in @rmk:longest-element-route-closed, and a level-four reduction is no longer needed for the answer. The orientation (@def:free-module-orientation) test is exhausted as well: on the positive definite plane $\langle\zeta, e'+f'\rangle$ the quantity $\det(\pi_W g|_W)$ of @prop:spinor-norm-orientation-classes(4) is positive for the word $w$, for $\delta_{E_8}$ and for the residual $k$ alike ($1\,485\,620\,920\,945$, $1$ and $1\,485\,620\,920\,945$), so $\Orth^+$ separates none of them.
:::

::: {.proof}

(1) Every pairing in $T_\Co$ is even, so $(x\cdot v)\in2\ZZ$ and $s_v(x)-x = (x\cdot v)v\in2T_\Co$; hence $s_v\equiv\id\pmod2$ and $h(s_v)$ is defined. It is nonzero: in the coordinates of $B$, $h(s_v)(\bar x) = \overline{(x\cdot v)/2}\cdot\bar v$, and $x$ with $(x\cdot v)/2$ odd exists because $v$ is primitive in the unimodular $B$, giving $\bar v\neq0$.

(2) $\delta_{E_8}$ acts by $-1$ on $E_8(2)$ and by $+1$ elsewhere, so $\delta_{E_8} = \id + 2h$ with $h = -1$ on the eight $E_8(2)$-coordinates and $0$ elsewhere, that is the projection onto those coordinates after reduction modulo $2$; it is nonzero. That it lies in the span is computed: over the $1024$ classes whose $\beta$-square is $-2$ modulo $4$ the span of the $h(s_v)$ has dimension $56$ and contains the projection onto every block, this one included (`computations/reports/coble_663-rel-level2-shadow-run.txt`, whose controls are the two elements quoted in (3)).

(3) If $\lambda\circ h$ vanishes on $W$ then it annihilates the span of the $h(s_v)$, so by (2) it vanishes at $h(\delta_{E_8})$: no such functional separates $\delta_{E_8}$ from $W$. For the other direction, $h(\iota)$ and $h(\epsilon)$ are in the span, and $\iota,\epsilon\in W$ (@thm:coble-block-sign-in-w), so membership in the span is a statement about the abelian shadow and not about $W$.
:::

::: {.proposition #prop:kernel-exceeds-short-roots title="The congruence kernel is strictly larger than the short-root reflection group"}

Let $g\in T_\Co$ span the $\langle 2\rangle$ summand of $T_\Co = \langle 2\rangle\oplus U(2)\oplus E_8(2)$, and let $s_g(x) = x-(x\cdot g)g$ be the reflection in it. Then

1. $s_g$ is an integral isometry of $T_\Co$, and $s_g\in\ker\rho_{T_\Co}$;
2. $s_g\notin\Orth^+(T_\Co)$, while $W(T_\Co)\subseteq\Orth^+(T_\Co)$;
3. hence $\ker\rho_{T_\Co}\neq W(T_\Co)$, and the reflection index (@def:index) that remains is the one inside $\widetilde\Orth^+(T_\Co) = \ker\rho_{T_\Co}\intersect\Orth^+(T_\Co)$.
:::

::: {.proof}

(1) $g^2 = 2$, and $x\cdot g\in 2\Z$ for every $x\in T_\Co$: the three summands of the decomposition are mutually orthogonal and each has all its pairings even, so every pairing in $T_\Co$ is even. Hence $s_g(x) = x-(x\cdot g)g$ is integral, and being a reflection it is an isometry with $s_g^2 = \id$. For $x\in T_\Co$ the difference $s_g(x)-x = -(x\cdot g)g$ lies in $2T_\Co$, so $s_g\equiv\id\bmod 2$ and $\rho_{T_\Co}(s_g) = \id$, under the convention that $\rho_{T_\Co}(h) = \id$ means $h\equiv\id\bmod 2$ (proof of @prop:gamma-co-reflective-set, part (3)).

(2) The class of a reflection in $\pi_0\Orth(T_\Co\tensor\RR) = \pi_0\Orth(2)\times\pi_0\Orth(9)$ is read off from the sign of its square. If $v^2<0$ then the mirror (@not:hyperbolic-polytope-setting) $v^\perp$ contains a maximal (@def:maximal-lattice) positive definite (@def:definiteness) $2$-plane on which $s_v$ is the identity, so $s_v$ preserves the orientation (@def:free-module-orientation) of the positive part; if $v^2>0$ then a maximal positive definite $2$-plane containing $v$ is preserved by $s_v$, which acts on it with determinant $-1$. So every reflection in a vector of square $-2$ lies in $\Orth^+(T_\Co)$, hence $W(T_\Co)\subseteq\Orth^+(T_\Co)$, while $s_g$ has $g^2 = 2$ and does not.

(3) By (1) $s_g\in\ker\rho_{T_\Co}$ and by (2) $s_g\notin\Orth^+(T_\Co)$, so $\ker\rho_{T_\Co}$ is not contained in $\Orth^+(T_\Co)$; since $W(T_\Co)$ is contained there, the two groups (@def:group) differ.
:::

::: {.lemma #lem:coble-2adic-closure-short-roots title="The $2$-adic closure of the short-root reflections contains $\Gamma(8)$"}

Let $B=\latI_{2,9}$ and let $W_0\subseteq W(T_\Co)$ be the subgroup generated by the reflections $s_v$ in the norm $-1$ vectors $v\in B$ whose coordinates in the diagonal (@def:polarization-functors) basis lie in $\{-1,0,1\}$. There are $3\,282$ such vectors and, since $s_v=s_{-v}$, $1\,641$ distinct reflections. Write $\Gamma(2^k)=\ker(\Orth(B)\to\Orth(B/2^kB))$. Then the $2$-adic closure of $W_0$ contains $\Gamma(8)$, and
$$
\delta_{E_8},\qquad -\id_{T_\Co},\qquad \epsilon'=\delta_{E_8}(-\id_{T_\Co})
\;\in\; W_0\cdot\Gamma(16).
$$
:::

::: {.proof}

The record is `computations/reports/coble_663-rel-lemma-c.py`, whose output is `computations/reports/coble_663-rel-lemma-c-run.txt` and whose assertions are also stored in `coble_663-rel-lemma-c.json`. It builds $B$ as `Lattices(ZZ).IPQ(2,9)` and $T_\Co$ as `NamedLattices.Tco`, verifies $T_\Co=B(2)$ through a library isometry of the halved Gram matrix to $B$, transports the block sign $\id_{\langle2\rangle\perp U(2)}\oplus(-\id_{E_8(2)})$ to the diagonal model of $B$, and checks that its $(-1)$-eigenspace is $E_8(-1)$. The image of $W_0$ in $\Gamma(2)/\Gamma(2^k)$ is computed by subgroup collection, the algorithm of `test_coble_fifty_five_positive_elements_span_kernel_modulo_sixteen`: generators are admitted through a pivot set recording the leading matrix at each level, and the admitted set is closed under squares and commutators. As a control, the same code reproduces the ranks $(55,54,55)$ that @prop:coble-positive-fifty-five-congruence-basis records for the certified $55$-element family; a second control shows that $\epsilon$ of @lem:sign-reduces-to-positive-plane lies in the subgroup modulo $16$ while the reflection in the norm $+1$ basis vector $e_0$ does not, so the test is not vacuous.

The layers are $(55,54)$ modulo $8$ and $(55,54,55)$ modulo $16$, against $\dim\mathfrak{so}_{11}(\F_2)=55$. The second layer is the trace hyperplane: $\det(g)=1$ and $g=\id+4A$ give $1\equiv\det(g)\equiv1+4\operatorname{tr}A\pmod{16}$, so $\operatorname{tr}A\equiv0\pmod2$. $\delta_{E_8}$, $\epsilon'$ and $-\id$ all reduce to the identity against the pivot set of the level-sixteen image.

For the closure, the third layer being full is enough. For $j\ge2$ the squaring map
$$
\Gamma(2^j)/\Gamma(2^{j+1})\longrightarrow\Gamma(2^{j+1})/\Gamma(2^{j+2}),\qquad [g]\longmapsto[g^2],
$$
is a bijection, because $g=\id+2^jA$ gives $g^2\equiv\id+2^{j+1}A\pmod{2^{j+2}}$. Squares of elements of $W_0\cap\Gamma(2^j)$ lie in $W_0\cap\Gamma(2^{j+1})$, so a full $j$-th layer gives a full $(j+1)$-st. Since the third layer is full, induction makes every layer $j\ge3$ of the closure full, and the image of a closed subgroup of $\Gamma(2)$ that is full at every level contains $\Gamma(8)$. (This is the elementary pro-$2$ form of the exponential-logarithm picture: on $\Gamma(4)$ the logarithm is a bijection onto $4\mathfrak{so}(B;\Z_2)$, and squaring is the doubling map level by level.) Since $\Gamma(16)\subseteq\Gamma(8)$, the three named elements lie in the closure.
:::

::: {.theorem #thm:coble-block-sign-in-w title="The block sign and $-\id$ lie in the short-root reflection group"}

Let $T_\Co=\langle2\rangle\perp U(2)\perp E_8(2)=B(2)$ with $B=\latI_{2,9}$, and let $W(T_\Co)$ be the group generated by the reflections in the $(-2)$-vectors of $T_\Co$, that is, by $s_v(x)=x+2b_B(x,v)v$ for $v\in B$ with $v^2=-1$. Then
$$
\delta_{E_8}\definedas\id_{\langle2\rangle\perp U(2)}\oplus(-\id_{E_8(2)})\in W(T_\Co),
\qquad
-\id_{T_\Co}\in W(T_\Co).
$$
Consequently $\epsilon'=\delta_{E_8}(-\id_{T_\Co})$ and $\epsilon=-\id_{\langle u_1,u_2\rangle}\oplus\id_{\langle c_1,\dots,c_9\rangle}$ of @lem:sign-reduces-to-positive-plane lie in $W(T_\Co)$, and $W(T_\Co)$ has finite index in $\Orth(B)$.
:::

::: {.proof}

**Step 0, where the two elements sit.** For $v\in B$ with $v^2=-1$, $s_v(x)-x=2b_B(x,v)v\in2B$, so $W(T_\Co)\subseteq\Gamma(2)$, and $gs_vg^{-1}=s_{gv}$ makes $W(T_\Co)$ normal in $\Orth(B)$. The rational spinor norm $\Theta_\QQ$ below satisfies $\Theta_\QQ(s_v)=[b_B(v,v)]=[-1]=\det s_v$, so $\Theta_\QQ=\det$ on $W(T_\Co)$.

On $B$ the block sign is $\id_{\langle1\rangle\perp U}\oplus(-\id_{E_8(-1)})$, with determinant $(+1)^3(-1)^8=1$; it acts as the identity on the rank-three summand $\langle1\rangle\perp U$, of signature $(2,1)$, so it fixes a positive definite plane pointwise and lies in $\SO(B)\cap\SO(2,9)^0$.

The conventions for spin lifts are those of @sec-clifford-lifting. In the Clifford algebra $C(B_\QQ)$, with $u^2=b_B(u,u)$ for $u\in B_\QQ$, an element $c$ acts by the twisted adjoint formula $c\cdot b=cb(c')^{-1}$, and $N(c)=c\bar c$. For a vector $u$ of nonzero square, $u'=-u$, so $u\cdot b=-ubu^{-1}=s_u(b)$; for an even element, $c'=c$ and the action is conjugation. $\pi\colon\Spin(B_\QQ)\to\SO(B_\QQ)$ is this action on the even elements with $N(c)=1$. Its kernel is $\{\pm1\}$: an even element that commutes (@def:commutative-diagram) with every vector is a scalar (O'Meara, *Introduction to Quadratic Forms*, 54:4), and $N(\alpha)=\alpha^2=1$. The spinor norm is O'Meara's $\theta$ (§55): $\theta(s_{u_1}\cdots s_{u_r})=[u_1^2\cdots u_r^2]\in\QQ^\times/(\QQ^\times)^2$, well defined and multiplicative, with kernel $\mathrm{O}'(V)$ on the rotations; it is the $\Theta_\QQ$ used above. Every $\sigma\in\mathrm{O}'(B_\QQ)$ lifts: write $\sigma=s_{u_1}\cdots s_{u_{2k}}$ (a rotation is a product of an even number of reflections, O'Meara 43:3), choose $\alpha\in\QQ^\times$ with $\alpha^2=\prod_iu_i^2$, and put $x=u_1\cdots u_{2k}/\alpha$. Then $N(x)=\prod_iu_i^2/\alpha^2=1$ (the identity $(u_1\cdots u_r)(u_r\cdots u_1)=\prod_iu_i^2$ of O'Meara p. 137), and $\pi(x)=\sigma$ because the signs of the $2k$ factors $-ubu^{-1}$ cancel. Write
$$
\Spin_B\definedas\{x\in\Spin(B_\QQ):xBx^{-1}=B\},\qquad \mathrm{O}'(B)\definedas\SO(B)\cap\ker\theta .
$$
Then $\pi(\Spin_B)=\mathrm{O}'(B)$, with kernel $\pm1$, because a lift of an element of $\SO(B)$ stabilizes $B$ by definition. Over $\RR$ the elements of $\mathrm{O}'(B)$ have positive spinor norm, so $\mathrm{O}'(B)\subseteq\SO(2,9)^0$. The real spinor norm is not the criterion for a lift: for orthogonal roots $r,s$ of $E_8(-1)$ and $v=r+s$, of square $-4$, the isometry $s_rs_v$ lies in $\SO(B)\cap\SO(2,9)^0$, while $\theta(s_rs_v)=[-2][-4]=[2]\neq1$, so it has no lift.

Both elements lie in $\mathrm{O}'(B)$, by their reflection decompositions. For $\delta_{E_8}$, take pairwise orthogonal roots $r_1,\dots,r_8$ of $E_8(-1)$, each of square $-2$: $\delta_{E_8}=s_{r_1}\cdots s_{r_8}$ and $\theta(\delta_{E_8})=[-2]^8=[1]$. For $-\id_{T_\Co}s_v$, take an orthogonal integral basis $e_1,\dots,e_{11}$ of $B$: $-\id_{T_\Co}=s_{e_1}\cdots s_{e_{11}}$, so $\theta(-\id_{T_\Co})=\prod_i[e_i^2]=[\det B]=[-1]$, while $\theta(s_v)=[-1]$; the product is $[1]$.

The lifts can be written down. $x_\delta\definedas r_1\cdots r_8/16$ satisfies $N(x_\delta)=\prod_ir_i^2/256=1$ and $x_\delta bx_\delta^{-1}=\delta_{E_8}(b)$, so $x_\delta\in\Spin_B$ lifts $\delta_{E_8}$. It is moreover a unit of the integral Clifford algebra $C(B)$: in the model $B=\langle1\rangle\perp U\perp E_8(-1)$ with $E_8=D_8^+\subset\QQ^8$ and the roots $f_1\pm f_2,\dots,f_7\pm f_8$, one has $(f_{2i-1}+f_{2i})(f_{2i-1}-f_{2i})=-2f_{2i-1}f_{2i}$, so $x_\delta=f_1\cdots f_8$, which is $\pm$ the volume element of the unimodular lattice $E_8(-1)$. So $x_\delta$ also lies in the group $\Spin(B)(\Z)$ of @sec-clifford-lifting. $x_v\definedas e_1\cdots e_{11}v$, an even product of twelve vectors of $B$, satisfies $N(x_v)=\prod_ie_i^2\cdot v^2=(\det B)(-1)=1$ and $x_vbx_v^{-1}=s_{e_1}\cdots s_{e_{11}}s_v(b)=-s_v(b)$, so it lies in $\Spin(B)(\Z)\subseteq\Spin_B$ and lifts $-\id_{T_\Co}s_v$. These four identities, the integrality of $x_\delta$ in $C(B)$, and the sign $ubu^{-1}=-s_u(b)$ are checked by exact arithmetic in `computations/reports/coble_663-rel-spin-lifts.py` (output `coble_663-rel-spin-lifts-run.txt`).

**Step 1, finite index.** $\Gamma=\Orth(B)\cap\SO(2,9)^0$ is an irreducible arithmetic lattice in the simple group $\SO(2,9)^0$ of real rank $2$ and finite centre (Borel--Harish-Chandra, in the form of Witte Morris, *Introduction to Arithmetic Groups (@def:arithmetic-group)*, arXiv:math/0106063v6, Theorem 1.3.9: for $G\subseteq\mathrm{SL}(\ell,\RR)$ a product of simple Lie groups with $G\cap\mathrm{SL}(\ell,\QQ)$ dense in $G$, $G\cap\mathrm{SL}(\ell,\Z)$ is a lattice; here $G=\SO(2,9)^0$ in the basis of $B$, the identity component of the $\QQ$-group $\SO(B_\QQ)$, whose rational points are dense, and $G\cap\mathrm{SL}(11,\Z)=\Gamma$ because $B$ is unimodular). $W(T_\Co)\cap\Gamma$ is normal in $\Gamma$. It is infinite: in the model $B=\langle a\rangle\perp U\perp E_8(-1)$ (an odd unimodular lattice of signature $(2,9)$, hence isometric to $B$), with $a^2=1$, hyperbolic pair (@def:isotropic-basis-hyperbolic-plane) $e,f$, and roots $r,r'$ of $E_8(-1)$ with $r\cdot r'=1$, the vectors $v=a+r$ and $w=a+f+r'$ have $v^2=w^2=-1$ and $v\cdot w=2$, so $s_vs_w$ acts on the Lorentzian (@def:hyperbolic-coxeter) plane $\langle v,w\rangle$ as a hyperbolic element; $(s_vs_w)^2\in\Gamma$ has infinite order. It is not central, the centre of $\Gamma$ being finite. By the Margulis normal subgroup theorem (Witte Morris, *Introduction to Arithmetic Groups*, arXiv:math/0106063v6, Theorem 17.1.1, where it is attributed to Margulis, *Discrete Subgroups of Semisimple Lie Groups*, Theorem VIII.2.6) $W(T_\Co)\cap\Gamma$ has finite index in $\Gamma$. Since $\Gamma$ has index two in $\SO(B)$ and $\det$ is onto on both $W$ and $\Orth(B)$, $W(T_\Co)$ has finite index in $\Orth(B)$; so $W(T_\Co)\cap\SO(B)$ has finite index in $\SO(B)$, and $\widetilde W\definedas\pi^{-1}(W(T_\Co)\cap\SO(B))\subseteq\Spin_B$ has finite index in $\Spin_B$, because $\pi(\Spin_B)=\mathrm{O}'(B)\supseteq W(T_\Co)\cap\SO(B)$ with kernel $\pm1$ (Step 0); it contains $\pm1$.

**Step 2, congruence.** Let $G=\Spin(B_\QQ)$, absolutely simple and simply connected of type $B_5$; it is $\QQ$-isotropic, of $\QQ$-rank $2$, the Witt index of $B_\QQ$, and $S=\{\infty\}$ with $\rank_\RR G=2$. Prasad--Rapinchuk, *Computation of the metaplectic kernel*, Publ. Math. IH\'ES 84 (1996) 91--187, state at: the $S$-congruence kernel $C(S,G)$ is the kernel of the map from the completion of $G(\QQ)$ in the $S$-arithmetic topology to its completion in the $S$-congruence topology; if $C(S,G)$ is central and $G(K)$ is perfect, then $C(S,G)$ is the dual of the metaplectic kernel $M(S,G)$; $G(K)$ is perfect when $G$ is $K$-isotropic and not an outer form of type $E_6$ of $K$-rank one; and $C(S,G)$ is known to be central when $\sum_{v\in S}K_v\text{-rank}\,G\ge2$. Their Main Theorem, gives $M(S,G)=1$ when $S$ contains a real place $v_0$ at which $G(K_{v_0})$ is not topologically simply connected. Here $\sum_{v\in S}\rank_{\QQ_v}G=\rank_\RR\Spin(2,9)=2$; for $\Spin(f)$ with $f$ in $n\ge5$ variables the centrality is Kneser's theorem (*Normalteiler ganzzahliger Spingruppen*, J. reine angew. Math. 311/312 (1979) 191--214, as stated in Prasad--Rapinchuk, *Developments on the congruence subgroup problem after the work of Bass, Milnor and Serre*, in *Collected Papers of John Milnor* V, AMS 2010, §5.3). $G(\QQ)$ is perfect because $G$ is $\QQ$-isotropic of type $B_5$. $\Spin(2,9)$ is not topologically simply connected: its maximal compact subgroup is $(\Spin(2)\times\Spin(9))/\{\pm1\}$, with fundamental group $\Z$. Hence $C(S,G)=1$: the $S$-arithmetic and $S$-congruence topologies on $G(\QQ)$ agree.

$\Spin_B$ is an arithmetic subgroup (@def:hsd-arithmetic-subgroup) of this kind. For each prime $p$ put $G_p\definedas\pi_p^{-1}(\mathrm{O}'(B_p))\subseteq\Spin(B_{\QQ_p})$, the stabilizer (@def:group-orbit) of $B_p=B\otimes\Z_p$; it is open, as the preimage of the open subgroup $\mathrm{O}'(B_p)$, and compact, because $\pi_p$ is a continuous surjection of $\Spin(B_{\QQ_p})$ onto the closed subgroup $\mathrm{O}'(B_{\QQ_p})$ with finite kernel, hence open (open mapping theorem) and proper. Then $\Spin_B=G(\QQ)\cap\prod_pG_p$. The finite-index subgroup $\widetilde W$ of Step 1 is open in the $S$-arithmetic topology, hence in the congruence topology: there is an open subgroup $U=\prod_{p\mid N}U_p\times\prod_{p\nmid N}G_p$ of $\prod_pG_p$, for some $N=2^am$ with $m$ odd, such that $\widetilde W\supseteq G(\QQ)\cap U$.

**Step 3, odd local images.** Write $W'\definedas W(T_\Co)\cap\SO(B)$; it lies in $\mathrm{O}'(B)$ because $\theta=\det$ on $W(T_\Co)$, and $\widetilde W=\pi^{-1}(W')$. Fix an odd prime $\ell$. $B_\ell$ is unimodular, $r\colon\SO(B_\ell)\to\SO_{11}(\F_\ell)$ is reduction, $\Omega_{11}(\F_\ell)\definedas\mathrm{O}'_{11}(\F_\ell)$, and $K'_\ell$ is the closure of $W'$ in $\SO(B_\ell)$.

(a) *Density.* O'Meara's strong approximation theorem for rotations (104:4) applies to $V=B_\QQ$ (regular, $\dim V\ge3$) with $S$ the set of finite primes, which is indefinite for $V$ because $V_\infty$ has signature $(2,9)$. For a finite set $T$ of primes and $\varphi_p\in\mathrm{O}'(B_p)$, $p\in T$, it gives $\sigma\in\mathrm{O}'(V)$ arbitrarily close to $\varphi_p$ at $p\in T$ and with $\|\sigma\|_p=1$ at the other primes, in the norm of a basis of $B$. Then $\sigma$ and $\sigma^{-1}=G_B^{-1}\sigma^{t}G_B$ are integral, so $\sigma\in\mathrm{O}'(B)$. Hence $\mathrm{O}'(B)$ is dense in $\prod_{p\in T}\mathrm{O}'(B_p)$. Since $W(T_\Co)$ is normal in $\Orth(B)$, $K'_\ell$ is normal in $\mathrm{O}'(B_\ell)$.

(b) *The bottom.* For $u\in B_\ell$ with $u^2\in\Z_\ell^\times$ the reflection $s_u$ preserves $B_\ell$. Every element of $\Omega_{11}(\F_\ell)$ is a product $s_{\bar u_1}\cdots s_{\bar u_{2k}}$ (O'Meara 43:3) with $\prod_i\bar u_i^2$ a square. Lift each $\bar u_i$ to $u_i\in B_\ell$: $\prod_iu_i^2$ is a unit whose residue is a square, hence a square in $\Z_\ell$ (O'Meara's Local Square Theorem 63:1: in a non-dyadic field $1+4\pi\alpha$ is a square for every integer $\alpha$, so a unit $\varepsilon$ with $\varepsilon\equiv c^2\pmod\ell$ has $\varepsilon/c^2\equiv1\pmod\ell$ a square), and $s_{u_1}\cdots s_{u_{2k}}\in\mathrm{O}'(B_\ell)$ reduces to the given element. So $r(\mathrm{O}'(B_\ell))\supseteq\Omega_{11}(\F_\ell)$; the same lifting without the square condition shows that $r$ is onto $\SO_{11}(\F_\ell)$. Let $H=r(W')$. An element of $W'$ is a word of even length in reflections $s_v$ with $v^2=-1$, so its reduction has spinor norm $[(-1)^{2k}]=1$: $H\subseteq\Omega_{11}(\F_\ell)$. $H$ is normalized by $r(\mathrm{O}'(B))$, which equals $r(\mathrm{O}'(B_\ell))$ by (a) and so contains $\Omega_{11}(\F_\ell)$; thus $H\trianglelefteq\Omega_{11}(\F_\ell)$. $H\neq1$: it contains $s_vs_w\neq\id$ for $v=e_2$ and $w=e_2+e_3+e_0$, whose inner product is $-1$. $\Omega_{11}(\F_\ell)$ is simple. Hahn--O'Meara, *The Classical Groups and K-Theory*, Theorem 6.4.27, gives $\mathrm{EO}_{11}(V)=\mathrm{O}'_{11}(V)$ for isotropic $V$; Theorem 6.3.16, says that every proper normal subgroup of $\mathrm{EO}_n(V)$ lies in its centre, for $V$ isotropic and not in the listed exceptions ($\mathrm{O}_4$ of Witt index two, $\mathrm{O}_3(\F_3)$ and groups that are not orthogonal); every $11$-dimensional quadratic space over $\F_\ell$ is isotropic; and the centre is trivial, the only scalars of $\Orth_{11}$ being $\pm1$ and $-1$ having determinant $-1$. Hence $H=\Omega_{11}(\F_\ell)$.

(c) *The layers.* Let $\Gamma_\ell(\ell^j)=\ker(\SO(B_\ell)\to\SO(B/\ell^jB))$. For $j\ge1$ the map $\id+\ell^jA\mapsto\bar A$ identifies $\Gamma_\ell(\ell^j)/\Gamma_\ell(\ell^{j+1})$ with $\mathfrak{so}(B/\ell B)=\{A:A^tG_B+G_BA=0\}$, of dimension $55$; it is onto, by the Cayley transform $(\id-\ell^jA/2)^{-1}(\id+\ell^jA/2)\equiv\id+\ell^jA\pmod{\ell^{2j}}$. $\Gamma_\ell(\ell)$ is a pro-$\ell$ group and $\theta$ takes values in a group of exponent two, so $\Gamma_\ell(\ell)\subseteq\mathrm{O}'(B_\ell)$. For $k\in K'_\ell$ and $\gamma=\id+\ell^jA$ the commutator $k\gamma k^{-1}\gamma^{-1}$ lies in $K'_\ell$, by (a), and is $\equiv\id+\ell^j(\bar k\bar A\bar k^{-1}-\bar A)\pmod{\ell^{j+1}}$. As $\bar k$ runs over $H=\Omega_{11}(\F_\ell)$ these differences span $\mathfrak{so}_{11}(\F_\ell)$ exactly when its $\Omega_{11}(\F_\ell)$-coinvariants vanish. They do: $\mathfrak{so}_{11}(\F_\ell)\cong\Lambda^2V$ is self-dual, so the coinvariants are dual to the invariants, and an invariant vector is an invariant alternating bilinear form on the absolutely irreducible module $V$, whose invariant bilinear form is unique up to a scalar and symmetric. For $\ell=3,5,7,11,13$ the span is also computed directly, of rank $55$, over $46$ unipotent elements of $\Orth(B)$ in `computations/reports/coble_663-rel-odd-local-perfection.py` (output `coble_663-rel-odd-local-perfection-run.txt`); their reductions lie in $\Omega_{11}(\F_\ell)$, which contains every unipotent element (Hahn--O'Meara 6.4.21, with 6.4.27). So $K'_\ell\cap\Gamma_\ell(\ell^j)$ maps onto every layer, and $K'_\ell$, being closed, contains $\Gamma_\ell(\ell)$. With (b), $K'_\ell=r^{-1}(\Omega_{11}(\F_\ell))$.

(d) *$K'_\ell=\mathrm{O}'(B_\ell)$, and it is topologically perfect.* $K'_\ell\subseteq\mathrm{O}'(B_\ell)\subsetneq\SO(B_\ell)$. The last inclusion is strict: take from the diagonal basis $u$ of square $1$ and $f_1,f_2$ of square $-1$, choose $a,b\in\Z_\ell$ with $a^2+b^2\equiv c$ for a nonsquare $c$ (every residue is a sum of two squares) and put $w=af_1+bf_2$; then $\theta(s_us_w)=[-(a^2+b^2)]$ differs from $\theta(s_us_{f_1})=[-1] by the nonsquare class $[c]$, so one of the two rotations is not in $\mathrm{O}'(B_\ell)$. Since $r$ is onto, $[\SO(B_\ell):r^{-1}(\Omega_{11}(\F_\ell))]=[\SO_{11}(\F_\ell):\Omega_{11}(\F_\ell)]=2$ (Hahn--O'Meara 6.4.28: $\Orth_n/\mathrm{EO}_n\cong\F_\ell^\times/\F_\ell^{\times2}\times\Z/2$), so $K'_\ell=\mathrm{O}'(B_\ell)$. Its closed commutator subgroup maps onto the perfect group $\Omega_{11}(\F_\ell)$ and, by the commutators of (c), contains $\Gamma_\ell(\ell)$; so it is $K'_\ell$.

(e) *The spin level.* Let $K_\ell$ be the closure of $\widetilde W$ in $G_\ell=\pi_\ell^{-1}(\mathrm{O}'(B_\ell))$. It contains $\pm1$, and $\pi_\ell(K_\ell)=K'_\ell=\mathrm{O}'(B_\ell)$ by compactness, so $K_\ell=G_\ell$. $G_\ell$ is topologically perfect: its closed commutator subgroup $D_\ell$ maps onto the closed commutator subgroup of $\mathrm{O}'(B_\ell)$, which is all of it by (d), so $D_\ell\{\pm1\}=G_\ell$; and $-1\in D_\ell$, because for pairwise orthogonal $f_1,f_2,f_3\in B$ of square $-1$ the elements $a=f_1f_2$ and $b=f_2f_3$ of $\Spin_B$ satisfy $ab=-ba$, so $aba^{-1}b^{-1}=-1$ (checked in `coble_663-rel-spin-lifts-run.txt`, item 4).

**Step 4, the $2$-adic input.** By @lem:coble-2adic-closure-short-roots the closure of $W(T_\Co)\cap\SO(B)$ in $\SO(B\otimes\Z_2)$ contains $\Gamma(8)$, and $\delta_{E_8}\in W_0\Gamma(16)$; since $\Gamma(16)\subseteq\Gamma(8)$, $\delta_{E_8}$ lies in that closure. So does $-\id_{T_\Co}s_v$, which is $-\id_{T_\Co}$ times the reflection $s_v\in W(T_\Co)$. Because $\Gamma(8)$ lies in the closure, for every $k$ the image of $W(T_\Co)\cap\SO(B)$ in $\SO(B/2^kB)$ is the image of the closure in that finite quotient and contains $\delta_{E_8}$ and $-\id s_v$. An approximant $w\in W_0$ with $w\equiv\delta_{E_8}\pmod{2^k}$, $k\ge2$, has $\det w\equiv\det\delta_{E_8}=1\pmod 4$, hence $\det w=1$ and $w\in W'$; so $\delta_{E_8}$, and likewise $-\id_{T_\Co}s_v$, lies in the closure of $W'$ in $\SO(B\otimes\Z_2)$.

**Step 5, conclusion.** Let $T$ be the set of primes dividing $N$, $\mathcal G=\prod_{p\in T}G_p$, and $K$ the closure of the diagonal image of $\widetilde W$ in $\mathcal G$.

First, an element $y\in\Spin_B$ whose image lies in $K$ lies in $\widetilde W$. Choose $w\in\widetilde W$ with $w^{-1}y\in\prod_{p\in T}U_p$; since $w$ and $y$ stabilize $B$, $w^{-1}y\in G_p$ for $p\notin T$, so $w^{-1}y\in G(\QQ)\cap U\subseteq\widetilde W$ by Step 2.

Second, $K$ contains every element of $\mathcal G$ supported at a single odd $\ell\in T$. Let $C$ be the closure of $\Spin_B$ in $\mathcal G$. By Step 3(a), $\pi(C)\supseteq\prod_{p\in T}\mathrm{O}'(B_p)$, so $\mathcal G=C\cdot Z$ with $Z=\prod_{p\in T}\{\pm1\}$ central. $\widetilde W$ is normal in $\Spin_B$, because $W(T_\Co)$ is normal in $\Orth(B)$, so $K$ is normal in $C$, and $[k,g]\in K$ for all $k\in K$ and $g\in\mathcal G$. The projection of $K$ to $G_\ell$ is $K_\ell=G_\ell$ (Step 3(e)). For $g$ supported at $\ell$ and $k\in K$ with prescribed $k_\ell$, $[k,g]$ is supported at $\ell$ with entry $[k_\ell,g_\ell]$. So $K$ contains the subgroup supported at $\ell$ that these commutators generate, and its closure $D_\ell=G_\ell$.

Third, the projection of $K$ to $G_2$ (when $2\in T$) contains both lifts of $\delta_{E_8}$. It is the closure $K_2$ of $\widetilde W$ in $G_2$; it contains $\pm1$, and $\pi(K_2)$ is the closure of $W'$ in $\SO(B_2)$, which contains $\delta_{E_8}$ by Step 4.

Now take $x=x_\delta\in\Spin_B$. Choose $k\in K$ whose $2$-component is that of $x$; for each odd $\ell\in T$ the element $x_\ell k_\ell^{-1}\in G_\ell$, supported at $\ell$, lies in $K$; their product with $k$ is the image of $x$. So the image of $x$ lies in $K$, and $x\in\widetilde W$ by the first point. Projecting to $\SO(B)$ gives $\delta_{E_8}\in W(T_\Co)$. The same argument with $x_v$ in place of $x_\delta$, using Step 4 for $-\id_{T_\Co}s_v$, gives $-\id_{T_\Co}s_v\in W(T_\Co)$, and multiplying by $s_v$ gives $-\id_{T_\Co}\in W(T_\Co)$; then $\epsilon'=\delta_{E_8}(-\id)\in W$, and $\epsilon=\iota\,(s_{c_1}\cdots s_{c_9})^{-1}$ with $\iota=-\id_{T_\Co}$ and $s_{c_j}\in W$ (@lem:sign-reduces-to-positive-plane) lies in $W$ too.
:::

::: {.corollary #cor:coble-rel-section title="The block-diagonal section of $\rho_{T_\Co}$ exists, so $(REL)$ holds"}

Let $H_0=\langle\tau\rangle\times W(E_8)\subseteq\Orth(T_\Co)$, with $\tau$ the transposition of the two isotropic generators of $U(2)$ and $W(E_8)$ acting on $E_8(2)$. Then $\rho_{T_\Co}(H_0)=P$ and $H_0\cap\ker\rho_{T_\Co}=\langle\delta_{E_8}\rangle\subseteq W(T_\Co)$. Consequently $H_0\subseteq\Gamma^{\mathrm{cong}}_{\Co,2}$, and any section $\sigma\colon P\to H_0$ of $\rho_{T_\Co}|_{H_0}$ satisfies $\sigma(p)w\sigma(p)^{-1}\in W(T_\Co)$ and $\sigma(p)\sigma(q)\sigma(pq)^{-1}\in H_0\cap\ker\rho_{T_\Co}\subseteq W(T_\Co)$; that is, $(REL)$ of research\#720, item 3 of @qst:gamma-co-generators, holds.
:::

::: {.proof}

$H_0\subseteq\rho_{T_\Co}^{-1}(P)=\Gamma^{\mathrm{cong}}_{\Co,2}$ because $\rho_{T_\Co}(H_0)=P$: the mod-$2$ image of $W(E_8)$ on $E_8/2E_8$ has order $\abs{\Orth(q_{E_8(2)})}=348\,364\,800=|W(E_8)|/2$ and kernel $\{\pm1\}$, and $\rho_{T_\Co}(\tau)\neq\id$, so $\abs{\rho_{T_\Co}(H_0)}=2\cdot348\,364\,800=\abs P$ (`computations/reports/coble_rel_block_diagonal_section-run.txt`). An element of $H_0$ in $\ker\rho_{T_\Co}$ lies in $\langle\tau\rangle\cap\ker\rho=\{\id\}$ or in $W(E_8)\cap\ker\rho=\{\pm1\}=\langle\delta_{E_8}\rangle$, so $H_0\cap\ker\rho_{T_\Co}=\langle\delta_{E_8}\rangle$, which lies in $W(T_\Co)$ by @thm:coble-block-sign-in-w. The normalization clause is automatic because $W(T_\Co)$ is normal in $\Orth(T_\Co)$, and the cocycle defect lies in $H_0\cap\ker\rho_{T_\Co}$.
:::

::: {.question #qst:gamma-co-reflection-index title="The index of the short-root reflection group"}
**The index is finite**, and its value is what remains open. Finiteness is @thm:coble-block-sign-in-w: $W(T_\Co)$ has finite index in $\Orth(B)$, hence in the finite-index subgroup $\widetilde\Orth^+(T_\Co)$.
The unrestricted form, $\ker\rho_{T_\Co} = W(T_\Co)$, is false: @prop:kernel-exceeds-short-roots exhibits an element of $\ker\rho_{T_\Co}$ outside $\Orth^+(T_\Co)$, so the question is the index inside $\widetilde\Orth^+(T_\Co)$, where both groups lie.
What would settle it is a finite set of reflections generating $W(T_\Co)$ together with the chamber they cut in the space of positive definite $2$-planes of $T_\Co\tensor_\ZZ\RR$, namely $\Orth(T_\Co\tensor_\ZZ\RR)/\Orth(2)\times\Orth(9)$ — equivalently a Coxeter presentation of $W(T_\Co)$.
The reflective set is known as a set (@prop:gamma-co-reflective-set), but not as a finite presentation, and no operation used on this page produces one.
The group $\widetilde\Orth^+(T_\Co)$ has finite covolume, so the finite index is the ratio of the two covolumes once the chamber is known; that ratio, and not the finiteness, is what the chamber would supply.
:::
