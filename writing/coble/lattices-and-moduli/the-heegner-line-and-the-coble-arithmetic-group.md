# The Heegner line and the stable orthogonal group {#sec-heegner-line}

## The Heegner vector inside $\ten$

::: {.lemma #lem:coble-heegner-vector title="An explicit $(-2)$ vector with Coble complement"}

Write $\ten = U\oplus U(2)\oplus E_8(2)$ and let $U = \ZZ u\oplus\ZZ w$ be the unimodular hyperbolic summand, so $u^2 = w^2 = 0$ and $u\cdot w = 1$.
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

For the index, $\delta$ and $\zeta$ have coordinate matrix $\begin{bmatrix}1 & -1\\ 1 & 1\end{bmatrix}$ of determinant $2$ in the basis $(u, w)$, so $\ZZ\delta\oplus\ZZ\zeta$ has index $2$ in $U$ and hence $\ZZ\delta\oplus\delta^{\perp\ten}$ has index $2$ in $\ten$; the class of $u = \tfrac12(\delta+\zeta)$ generates the quotient.
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

There is a single $\Orth(\ten)$-orbit of $(-2)$ vectors in $\ten$ [@AEGS25 §2], so it suffices to show that this orbit does not split under the subgroup $\gent\leq\Orth(\ten)$.

Write $\mathcal A\definedas\im\bigl(\gent\to\Orth(A_{\ten}, q_{\ten})\bigr)$, so that $\gent\iscontainedin\Orth_{\mathcal A}(\ten)\definedas \theset{\, g\in\Orth(\ten) \mid \bar g\in\mathcal A \,}$.
Algorithm 2.2 of [@Daw22] decides $\Orth_{\mathcal A}(L)$-equivalence of non-isotropic vectors under three hypotheses: the vector is non-isotropic, its orthogonal complement is indefinite, and $\Orth(L)\to\Orth(q_L)$ is surjective.
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

::: {.definition #def:gamma-co-en title="The induced Coble subgroup"}

For the Heegner vector $\delta$ of @lem:coble-heegner-vector, define
$$
\Gamma_\Co^\En(\delta)
\definedas \im\Bigl(
\Stab_{\gent}(\ZZ\delta)
\too
\Orth\bigl(\delta^{\perp \ten}\bigr) = \Orth(T_\Co)
\Bigr)
,
$$
the group of restrictions to $\delta^{\perp\ten}$ of those elements of $\gent$ that preserve the line $\ZZ\delta$.
:::

::: {.proposition #prop:gamma-en-two-gluing title="Discriminant description of $\gent$"}

Let $\sen = U(2)\oplus E_8(2)$ and $\ten$ be the invariant and coinvariant lattices of the Enriques involution on $\lkt$, and let
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
where $h = e + f\in U(2) = \sdp\iscontainedin \sen$ is the degree-$2$ polarization vector, with $e^2 = f^2 = 0$ and $e\cdot f = 2$, so that $h^2 = 4$ [@AEGS25 Def. 2.5, Def. 2.6].
Equivalently, the image of $\gent$ in $\Orth(q_{\ten})$ is the $\gamma$-transport of the image of $\Stab_{\Orth(\sen)}(h)$ in $\Orth(q_{\sen})$.
:::

::: {.proof}

By definition $\gent$ is the image in $\Orth(\ten)$ of the isometries of $\lkt$ that commute with $\Ien$ and fix $h$ [@AEGS25 Def. 2.6].
An isometry of $\lkt$ commuting with $\Ien$ is the same as a pair $(g_S, g_T)\in\Orth(\sen)\times\Orth(\ten)$ preserving the two eigenlattices, and by Nikulin's gluing theorem (@thm:nikulin-gluing) such a pair extends over the overlattice $\lkt$ of $\sen\oplus \ten$ exactly when it preserves the graph of $\gamma$, that is when $\bar g_T\circ\gamma = \gamma\circ\bar g_S$.
The polarization $h$ lies in $\sen$, so the condition $g(h) = h$ on $\lkt$ is the condition $g_S(h) = h$.
:::

::: {.proposition #prop:polarization-stabilizer-enriques title="The integral stabilizer of the degree-$2$ polarization"}

Write $\sen = C(2)$ with $C = U\oplus E_8$ even unimodular of signature $(1,9)$, and let $h\in \sen$ be the polarization vector of the discriminant description of $\gent$ (@prop:gamma-en-two-gluing), so that $h = u_0 + w_0$ for a basis $u_0, w_0$ of the $U$ summand of $C$ with $u_0\cdot w_0 = 1$.
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

Twisting does not change the isometry group, so $\Orth(\sen) = \Orth(C)$ and $\Stab_{\Orth(\sen)}(h) = \Stab_{\Orth(C)}(h)$.
Computing in $C$, one has $h^2 = 2$ and $h^{\perp C} = \ZZ(u_0 - w_0)\oplus E_8$ with $(u_0-w_0)^2 = -2$, so $h^{\perp C}\cong\generators{-2}\oplus E_8$.
An isometry fixing $h$ preserves $h^{\perp C}$, giving the restriction homomorphism, which is injective because $C_\QQ = \QQ h\oplus (h^{\perp C})_\QQ$.
It is surjective: $A_{h^{\perp C}}\cong A_{\generators{-2}}\cong\ZZ/2\ZZ$ has trivial automorphism group, so every isometry of $h^{\perp C}$ preserves the gluing class of the index-two overlattice $C$ of $\ZZ h\oplus h^{\perp C}$ and extends over $C$ fixing $h$, by Nikulin's gluing theorem (@thm:nikulin-gluing).
The lattice $\generators{-2}\oplus E_8$ is negative definite and generated by its $(-2)$ vectors, whose root system is $A_1\oplus E_8$; no isometry mixes summands of different ranks, so its isometry group is $\Orth(\generators{-2})\times\Orth(E_8) = \theset{\pm1}\times W(E_8)$.

For the last claim, $\id_U\oplus(-\id_{E_8})$ fixes $h\in U$ and acts on $A_{\sen}\cong C/2C$ as in @prop:twisted-unimodular-discriminant, by the identity on $U/2U$ and by $x\mapsto -x\equiv x$ on $E_8/2E_8$.
:::

::: {.lemma #lem:gco-orbit-transfer title="The $G_\Co$ orbit decomposition lives on the $S_\En$ summand"}

By @prop:tco-as-twist $T_\Co = B(2) = \generators{2}\oplus U(2)\oplus E_8(2)$, so $T_\Co = \generators{\zeta}\perp S_\En$ with $\zeta^2 = 2$ and $S_\En = U(2)\oplus E_8(2)$, and discriminant forms add over orthogonal sums:
$$
A_{T_\Co} = A_{\generators{2}}\perp A_{S_\En},
\qquad
q_{T_\Co} = q_{\generators{2}} + q_{S_\En},
$$
with $q_{\generators{2}}$ taking the value $\tfrac12$ on the nonzero class and $q_{S_\En}$ taking values in $\ZZ/2\ZZ$.
Then the isotropic classes of $A_{T_\Co}$ are exactly the classes whose $A_{\generators{2}}$-coordinate vanishes, and they number $528$, the same as the isotropic classes of $A_{S_\En}$.
Each of the nine group generators of $G_\Co$ is the reflection in a vector of $S_\En$, hence fixes $\zeta$, preserves the splitting, and acts on $A_{T_\Co}$ as $\id\oplus\rho_{S_\En}(g_i)$.
Consequently the orbits of $G_\Co$ on the isotropic classes of $A_{T_\Co}$ are its orbits on the isotropic classes of $A_{S_\En}$, with the same sizes.
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

1. the image of the integral stabilizer in the discriminant group,
   $$
   G \definedas \im\bigl(\Stab_{\Orth(\sen)}(h)\to\Orth(A_{\sen}, q_{\sen})\bigr)
   ,
   $$
   has order $\abs{W(E_8)} = 696\,729\,600$, and is generated by the images of the swap of the two isotropic basis vectors $u_0, w_0$ of the $U$ summand of $C$, which fixes $h$, and of the reflections in the simple roots of the $E_8$ summand;

2. the corresponding group $G_\Co\leq\Orth(A_{T_\Co}, q_{T_\Co})$, obtained by transporting $G$ along $\gamma$ and restricting to the Coble Heegner complement $\delta^{\perp\ten} = T_\Co$, has order $\abs{W(E_8)}$ and acts on the $528$ isotropic classes of $A_{T_\Co}$ with orbit lengths
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
An isometry of $\lkt$ commutes with $\theta_\Co$ if and only if it preserves both eigenlattices.
:::

::: {.proof}

Both $A_{S_\Co}$ and $A_{T_\Co}$ are $2$-elementary, so $-\id$ and $\id$ agree on each of them; the pair therefore acts as the identity on the graph of $\gamma_\Co$ and by Nikulin's gluing theorem (@thm:nikulin-gluing) extends over the overlattice $\lkt$ of $S_\Co\oplus T_\Co$.
The eigenlattice description is the definition of the extension.
For the last claim, an isometry commuting with an involution preserves its eigenspaces, which by @prop:involution_eigenspaces are the rational spans of $T_\Co$ and $S_\Co$; conversely an isometry preserving both eigenlattices commutes with $\theta_\Co$ on each of them and hence on $\lkt$.
:::

::: {.proposition #prop:unnodal-coble-polarization-nef title="The degree-$2$ polarization of an unnodal Coble surface is nef and big"}

Let $S$ be an unnodal Coble surface, that is one with no $(-2)$-curves, let $F_1\in\abs{f_1}$ and $F_2\in\abs{f_2}$ be half-fibres of its two Halphen fibrations of index $2$, and put $h = F_1+F_2$, so that $F_i^2 = 0$, $F_1\cdot F_2 = 1$ and $h^2 = 2$.
Then $\abs{2h}$ has no base points, and $h$ is nef and big.
:::

::: {.proof}

By [@CD12, Lemma 3.7], $\abs{2h}$ has no base points; the proof there uses only the intersection numbers of $f_1, f_2, K_S$ and the equalities $\abs{f_i} = \set{F_i}$, and not the effectivity of $-2K_S$ [@CD12, Remark 3.8].
A base-point-free class is nef, so $2h$ and hence $h$ are nef, and $h^2 = 2>0$ makes $h$ big by @prop:nef-big-finite-cover.
:::

::: {.construction #cons:cd12-double-plane title="The double-plane model of an unnodal Coble surface [@CD12, §3]"}

Let $S$ and $h$ be as in @prop:unnodal-coble-polarization-nef.

1. $\mathfrak C\subset S$ is the unique curve in $\abs{-2K_S}$; it is a smooth rational curve with $\mathfrak C^2 = -4$ [@CD12, §3.2].
2. $\pi\colon\widetilde X\to S$ is the K3 double cover branched along $\mathfrak C$, with $\pi_*\OO_{\widetilde X} = \OO_S\oplus\OO_S(K_S)$; $I_\Co$ is its deck involution, and $R_\pi\definedas\pi^{-1}(\mathfrak C)$ is the fixed curve of $I_\Co$.
3. $\phi_h\colon S\to\mathsf D\subset\PP^4$ is the morphism defined by $\abs{2h}$. It is $2$-to-$1$ onto a del Pezzo surface $\mathsf D$ of degree $4$ with four ordinary double points [@CD12, Lemmas 3.9, 3.10], and it contracts $\mathfrak C$ to one of them, $q$, because $h\cdot\mathfrak C = h\cdot(-2K_S) = 0$.
4. $\mathrm{bl}_q\colon\mathsf D'\to\mathsf D$ is the blowup of $q$, with exceptional curve $E_q$, and $\phi'\colon S\to\mathsf D'$ is the induced finite double cover, so that $\mathfrak C = \phi'^{-1}(E_q)$; $\tau\in\Aut(S)$ is its deck involution.
5. The fixed locus of $\tau$ is a smooth curve $\overline W\subset S$ of genus $4$ together with three isolated points, and $\overline W$ meets $\mathfrak C$ in two points [@DK13, §8].
6. $\mathsf H\definedas\langle f_1, f_2\rangle\subset K_S^{\perp}$ and $E_8\definedas\mathsf H^{\perp K_S^{\perp}}$. The classes $f_1, f_2, K_S$ are $\tau$-invariant, and $\tau^* = \id_{\mathsf H}\oplus(-\id_{E_8})$ on $K_S^{\perp}\otimes\QQ$ [@CD12, proof of Theorem 3.5].

The automorphism $I_\Co$ acts on $\widetilde X$ and $\tau$ acts on $S$; the curve $\overline W$ lies on $S$, and the curve $R_\pi$ lies on $\widetilde X$.
:::

::: {.proposition #prop:involution-lifting-double-cover title="Lifting an involution through a branched double cover, and when the lift is an involution"}

Let $S$ be a smooth projective surface over $\CC$, let $\mcl$ be a line bundle, let $s\in H^0(\mcl^{\otimes2})$ be a section cutting out a smooth curve $B$, and let $\pi\colon\widetilde X\to S$ be the double cover with $\pi_*\OO_{\widetilde X} = \OO_S\oplus\mcl^{-1}$ and multiplication given by $s$; let $\iota$ be the deck involution, $+1$ on $\OO_S$ and $-1$ on $\mcl^{-1}$.
Let $\tau\in\Aut(S)$ be an involution with $\tau(B) = B$, and let $\lambda\colon\tau^*\mcl\to\mcl$ be an isomorphism with $\lambda(\tau^*s) = c\,s$ for some $c\in\CC^\times$; rescaling $\lambda$ by a square root of $c$ normalizes $c = 1$, and leaves the choice $\pm\lambda$. Then:

1. $\tau$ lifts to an automorphism $\tilde\tau$ of $\widetilde X$ with $\pi\tilde\tau = \tau\pi$, and the lifts of $\tau$ are exactly $\tilde\tau$ and $\tilde\tau\iota$;
2. $\tilde\tau^2\in\set{\id,\iota}$, and $(\tilde\tau\iota)^2 = \tilde\tau^2$;
3. let $p\in B$ be a fixed point of $\tau$ and let $\sigma\in\set{\pm1}$ be the sign by which $\tau$ acts on the normal line $N_{B/S,p}$. Then $\tilde\tau^2 = \id$ if $\sigma = +1$, and $\tilde\tau^2 = \iota$ if $\sigma = -1$; in particular, if a fixed curve of $\tau$ passes through $p$ transversally to $B$, then $\tilde\tau$ is an involution.
:::

::: {.proof}

(1) The $\ZZ/2$-graded algebra $\mca = \OO_S\oplus\mcl^{-1}$ has $\Spec_S\mca = \widetilde X$. The action of $\tau$ on it is the identity in degree $0$ and $\mcl^{-1}\to\tau_*\mcl^{-1} = \tau_*(\tau^*\mcl)^{-1}\xrightarrow{\lambda^{-1}}\tau_*\mcl^{-1}$ in degree $1$; it is multiplicative because $\lambda(\tau^*s) = cs$ sends the structure section to a scalar multiple of itself. Any two such actions agree on $\OO_S$, so their quotient is an automorphism over $\OO_S$, that is an element of the deck group $\set{\id,\iota}$ ($\widetilde X$ being connected as $B\neq\emptyset$).
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
Each lift $\tilde\tau$ commutes with $I_\Co$: $\pi\tilde\tau I_\Co\tilde\tau^{-1} = \tau\pi I_\Co\tilde\tau^{-1} = \tau\pi\tilde\tau^{-1} = \pi$, so $\tilde\tau I_\Co\tilde\tau^{-1}$ is a deck transformation different from $\id$, that is $I_\Co$.

Let $p$ be one of the two points of $\overline W\cap\mathfrak C$ (@cons:cd12-double-plane(5)).
Since $\overline W$ is fixed pointwise, $\tau$ acts by $+1$ on $T_p\overline W$.
On $\mathfrak C\cong\PP^1$ the involution $\tau$ is not the identity: otherwise $\mathfrak C$ would lie in the fixed locus, so it would be $\overline W$, of genus $4$, or one of three points.
So $\tau$ acts by $-1$ on $T_p\mathfrak C$, the two tangent lines at $p$ are different eigenlines, and $T_p\overline W$ is the normal line $N_{\mathfrak C/S,p}$.
Hence $\sigma = +1$ at $p$, and $\tilde\tau^2 = \id$ by @prop:involution-lifting-double-cover(3); by part (2) of that proposition the other lift has the same square.

At an isolated fixed point $p'$ of $\tau$ on $\mathfrak C$, both eigenvalues of $\tau$ on $T_{p'}S$ would be $-1$, so $\sigma = -1$ and $\tilde\tau^2 = \iota$ by @prop:involution-lifting-double-cover(3), which contradicts $\tilde\tau^2 = \id$.
:::

::: {.proposition #prop:cd12-lift-on-lattice title="The lift of $\tau$ on the pulled-back lattice"}

In @cons:cd12-double-plane let $\tilde\tau$ be a lift of $\tau$ (@cor:lift-in-cd12-model). Then:

1. $\tilde\tau$ and $\tilde\tau I_\Co$ agree on $\pi^*\Pic(S)$; they fix $\pi^*\mathsf H$ and $\pi^*K_S$ and negate $\pi^*E_8$;
2. $\pi^*\mathsf H\cong U(2)$ and $(\pi^*K_S)^2 = -2$, so the invariant lattice of $\tilde\tau$ contains $\pi^*\mathsf H\oplus\ZZ\pi^*K_S$, of rank $3$, and is not $\sdp\cong U(2)$;
3. $I_\Co$ acts by $-1$ on $H^{2,0}(\widetilde X)$, so exactly one of $\tilde\tau$ and $\tilde\tau I_\Co$ is nonsymplectic.
:::

::: {.proof}

(1) $I_\Co$ acts trivially on $\pi^*\Pic(S)$, and $\tilde\tau(\pi^*D) = \pi^*(\tau D)$ for every divisor class $D$ on $S$.
So the two lifts act on $\pi^*\Pic(S)$ through $\tau^*$, which by @cons:cd12-double-plane(6) fixes $\mathsf H$ and $K_S$ and negates $E_8$.

(2) Pullback along the double cover multiplies intersection numbers by $2$.
So $(\pi^*f_i)^2 = 0$ and $\pi^*f_1\cdot\pi^*f_2 = 2$, which is $U(2)$, and $(\pi^*K_S)^2 = 2K_S^2 = -2$, because $K_S^2 = 9 - 10 = -1$ on the blowup of $\PP^2$ at ten points [@DK13, §3].
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

In the model of [@DK13, §3] let $S$ be the blowup of $\PP^2$ at the ten nodes of an irreducible plane sextic $C$ and let $f\colon X\to S$ be the double cover branched along the proper transform $\tilde C\in\abs{-2K_S}$, so that $X$ is a K3 surface.
Then the invariant lattice of the covering involution is $f^*\Pic(S)$, spanned by $e_0 = f^*H$ and $e_i = f^*E_i$ for $i = 1,\dots,10$, with $e_0^2 = 2$ and $e_i^2 = -2$; this lattice is $M_X$, it equals $S_\Co$, $N_X = T_\Co$, and the covering involution acts on $H^2(X,\ZZ)\cong\lkt$ as $I_\Co^* = -\theta_\Co$ (@prop:theta-co-exists).
In that basis
$$
H = \tilde h_\Co = 6e_0 - 2\Sum_{i\le 8}e_i - e_9 - e_{10},
\qquad
\alpha = 3e_0 - \Sum_{i=1}^{10}e_i,
$$
and the two isotropic classes $f^*F_1 = 3e_0-\Sum_{i\le9}e_i$ and $f^*F_2 = 3e_0-\Sum_{i\le8}e_i-e_{10}$ span a primitive $U(2)$ inside $S_\Co$ with $H = f^*F_1+f^*F_2$.
Taking $+1$ on that $U(2)$, $-1$ on its orthogonal complement $N\definedas\langle f^*F_1,f^*F_2\rangle^{\perp S_\Co}$ inside $S_\Co$, and $-\id$ on $T_\Co$ defines an integral isometry $\phi$ of $\lkt$: its $(+1)$-eigenspace is $\langle f^*F_1,f^*F_2\rangle\cong U(2)$, its $(-1)$-eigenspace is the negative definite rank-$9$ lattice $N$ together with $T_\Co$, it fixes $H$, and it reverses $\alpha$.
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
That extension preserves $S_\Co$ and $T_\Co$, hence commutes with $I_\Co$, and it fixes $H$ because $H\in\langle f^*F_1,f^*F_2\rangle$.
Finally $\alpha\cdot f^*F_1 = 18-18 = 0$ and $\alpha\cdot f^*F_2 = 18-18 = 0$, so $\alpha\in N$ and $\phi(\alpha) = -\alpha$.
:::

::: {.lemma #lem:alpha-is-ramification-class title="The root $\alpha$ is the class of the ramification curve"}

In @prop:coble-cover-marking let $R\definedas f^{-1}(\tilde C)\subset X$ be the ramification curve.
Then $\alpha = [R]$; so $\alpha$ is effective and $-\alpha$ is the class of no effective divisor.
:::

::: {.proof}

The strict transform $\tilde C$ is smooth and $f$ is ramified along $R$ with index $2$, so $f^*[\tilde C] = 2[R]$.
With $[\tilde C] = 6H-2\Sum_iE_i = -2K_S$ this gives $2[R] = f^*(-2K_S) = 2\alpha$, and $H^2(X,\ZZ)$ is torsion-free, so $[R] = \alpha$.
If $D$ were effective with $[D] = -\alpha$, then $R+D$ would be a nonzero effective divisor of class $0$, whose intersection with an ample class is $0$, which is impossible.
:::

::: {.corollary #cor:coble-polarization-nef-big title="The degree-$4$ class is nef and big exactly when $h_\Co$ is nef"}

In @prop:coble-cover-marking let $h_\Co = 6H-2\Sum_{i\le8}E_i-E_9-E_{10} = F_1+F_2\in\Pic(S)$ (@def:coble-polarization-classes), so that $\tilde h_\Co = f^*h_\Co$.
Then $f^*h_\Co$ is nef and big if and only if $h_\Co$ is nef.
:::

::: {.proof}

By @prop:nef-big-finite-cover, $f^*h_\Co$ is nef if and only if $h_\Co$ is nef, and a nef class with $(f^*h_\Co)^2 = 2h_\Co^2 = 4>0$ is big.
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

Let $S_\Co$, $T_\Co = S_\Co^{\perp\lkt}$ and $H = \tilde h_\Co$ be as in @prop:coble-cover-marking, and let $M\definedas S_\En\oplus\ZZ\delta$, with $h = e+f\in S_\En$ the polarization of @prop:gamma-en-two-gluing and $\delta$ the Heegner vector of @lem:coble-heegner-vector.
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
The classes $F_1 = 3H_{\PP^2}-\Sum_{i\le9}E_i$ and $F_2 = 3H_{\PP^2}-\Sum_{i\le8}E_i-E_{10}$ of the plane model satisfy $\Sum_i b_i = 9 = 3a$, so they lie in $K_S^{\perp}$, and $F_i^2 = 0$, $F_1\cdot F_2 = 1$; so $\langle F_1,F_2\rangle\cong U$ is unimodular and $K_S^{\perp} = \langle F_1,F_2\rangle\perp E'$ with $E'$ even, unimodular and negative definite of rank $8$, hence $E'\cong E_8$.
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

::: {.corollary #cor:no-del-pezzo-involution-coble-cover title="The isometry fixing $\langle f^*F_1,f^*F_2\rangle$ is not geometric"}

In the marking of @prop:coble-cover-marking, the isometry $\phi$ is a Hodge isometry of $H^2(X,\ZZ)$, and it is not the action of an automorphism of $X$.
:::

::: {.proof}

The transcendental lattice of $X$ lies in $\Pic(X)^{\perp}\subseteq S_\Co^{\perp} = T_\Co$, on which $\phi$ is $-\id$, so $\phi$ acts on $H^{2,0}(X)$ by $-1$ and preserves the Hodge decomposition.
By @prop:coble-cover-marking, $\phi(\alpha) = -\alpha$.
By @lem:alpha-is-ramification-class, $\alpha$ is effective and $-\alpha$ is not.
An automorphism of $X$ carries effective classes to effective classes, so no $\iota\in\Aut(X)$ has $\iota^* = \phi$.
:::

::: {.proposition #prop:del-pezzo-placement title="What the abstract conditions determine about the del Pezzo slot"}

Let $\psi$ be an involution of $\lkt$ whose invariant lattice is $\sdp\cong U(2)$, let $H\in\sdp$ with $H^2 = 4$, and suppose that $\psi$ commutes with $I_\Co$ — equivalently, that it preserves $S_\Co$.
Then $H = a+b$ for a hyperbolic basis $a,b$ of $\sdp$, and the isotropic classes $a'\in\sdp$ with $a'\cdot H = 2$ are exactly $a$ and $b$.
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

By @prop:del-pezzo-placement, $N'$ has a hyperbolic basis $a,b$ with $a+b = H$, so $a$ and $b$ are isotropic classes of $S_\Co$ with $a\cdot H = b\cdot H = 2$.
The map $a\mapsto y\definedas 2a-H$ is a bijection from the isotropic $a\in S_\Co$ with $a\cdot H = 2$ onto the $y\in H^{\perp S_\Co}$ with $y^2 = -4$ and $y\equiv H\pmod{2S_\Co}$.
Indeed $(2a-H)^2 = 4a^2-4a\cdot H+H^2 = -4$ and $(2a-H)\cdot H = 0$; conversely, for such a $y$ the class $a = (y+H)/2$ lies in $S_\Co$ by the congruence, $(y+H)^2 = y^2+H^2 = 0$ and $(y+H)\cdot H = H^2 = 4$.

Transport the count along the isometry $\psi\colon S_\Co\iso M$ of the proof of @prop:coble-enriques-polarized-match, which sends $H$ to $h = e+f$ and $H^{\perp S_\Co}$ to $\ZZ(e-f)\oplus E_8(2)\oplus\ZZ\delta$.
A vector $c(e-f)+v+d\delta$ there has square $-4c^2+v^2-2d^2$ with $v^2\in 4\ZZ_{\le0}$, so the vectors of square $-4$ are the $2$ vectors $\pm(e-f)$ and the $240$ vectors $v\in E_8(2)$ with $v^2 = -4$, which are the roots of $E_8$; there are $242$ in all.
Of these, $\pm(e-f)-(e+f)\in\set{-2f,-2e}$ lies in $2M$, and $v-(e+f)$ does not, because its coefficient of $e$ is odd.
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
4. the involution $J$ of $\lkt$ with $(+1)$-eigenspace $\langle H,b\rangle$ is integral, fixes $H$, commutes with $I_\Co$, has invariant lattice $\langle H,b\rangle\cong U(2) = \sdp$ meeting $S_\Co$ in $\ZZ H$, is conjugate to $I_{\mathrm{dP}}$ of [@AEGS25, def:involutions] in $\Orth(\lkt)$, and is nonsymplectic for every action of it on a K3 surface — so the product $I_\Co J$ is symplectic, both factors acting by $-1$ on the holomorphic $2$-form.
:::

::: {.proof}

Write $\overline{x}$ for the class in $A_{L,q}$ of $x\in L^{\#}$; by @def:discriminant $q_L(\overline{x}) = x^2$ modulo $2\bZ$.
(1) In the basis $e_0 = f^*H$, $e_i = f^*E_i$ of @prop:coble-invariant-lattice one has $H\cdot e_0 = 12$, $H\cdot e_i = 4$ for $1\le i\le 8$ and $H\cdot e_9 = H\cdot e_{10} = 2$, so those values generate $2\bZ$; and $H/2\notin S_\Co$ because $(H/2)^2 = 1$ is odd while $S_\Co$ is even. Hence $\varphi$ is integral, and it is $(-\id)\circ s_H$ with $s_H$ the reflection in $H$, an integral isometry because $2(x\cdot H)/H^2 = (x\cdot H)/2\in\bZ$ for $x\in S_\Co$; the scalar $-\id$ commutes with $s_H$, so $\varphi^2 = s_H^2 = \id$. Moreover $\varphi(H) = -H+2H = H$, and $\varphi(x) = -x$ for $x\in H^{\perp S_\Co}$; conversely $\varphi(x) = x$ forces $2x = \tfrac12(x\cdot H)H$, that is $x\in\bQ H$, and then $x\in\ZZ H$ because $H$ is primitive in $S_\Co$. Finally $H^2\det(H^{\perp S_\Co}) = 4\cdot 2^{11} = 4\det S_\Co$, so $\ZZ H+(H^{\perp S_\Co})$ has index $2$ in $S_\Co$, and $2S_\Co$ lies in it by the argument with $x\pm\varphi x$ of @prop:del-pezzo-placement, so the index is exactly $2$.
(2) By @prop:tco-split-maximal $T_\Co = B(2)$ with $B = U\oplus U\oplus\latI_{0,7}$, so $T_\Co\cong U(2)\perp U(2)\perp\generators{-2}^{\oplus7}$ and every vector of $T_\Co$ has even square. Hence $\tfrac12T_\Co\subseteq T_\Co^{\#}$, and $\cardinality{A_{T_\Co}} = 2^{11} = [T_\Co:\tfrac12T_\Co]$ by @prop:twisted-unimodular-discriminant, so $T_\Co^{\#} = \tfrac12T_\Co$ and every class of $A_{T_\Co}$ is the class of some $\tfrac12\tau$ with $\tau\in T_\Co$. Replacing $\tau$ by $\tau+2\lambda$ adds $\lambda\in T_\Co$ to $\tfrac12\tau$ and leaves the class alone, while $\bigl(\tfrac12\tau+\lambda\bigr)^2 = \tfrac14\tau^2+\tau\cdot\lambda+\lambda^2$.
Take $\tau = \sum_ic_ie_i$ with $c_i\in\set{0,1}$, in the basis $e_0,e_1$ of the first $U(2)$, $e_2,e_3$ of the second, and $e_4,\ldots,e_{10}$ the orthogonal basis vectors of square $-2$. Two cases cover every class of odd value. If $c_i = 1$ for some $i\le3$, say $c_0 = 1$, then $\tfrac12\tau\cdot e_1 = c_0 = 1$, so $\tfrac12\tau+p e_1$ has square $\tfrac14\tau^2+2p$, which is $-1$ for $p = -\tfrac12\bigl(1+\tfrac14\tau^2\bigr)\in\bZ$ because $\tfrac14\tau^2$ is odd; and $(c_1,e_0)$, $(c_2,e_3)$, $(c_3,e_2)$ do the same for the other three coordinates. If $c_0 = c_1 = c_2 = c_3 = 0$ then $\tfrac14\tau^2 = -\tfrac12k$, where $k$ is the number of $j$ with $c_{4+j} = 1$, and that is odd exactly for $k = 2$ and $k = 6$: for $k = 2$ the square is already $-1$, and for $k = 6$ one has $\tfrac12\tau\cdot(e_0+e_1+e_j) = 0$ and $(e_0+e_1+e_j)^2 = 2$ for any $j$ with $c_{4+j} = 0$, so $\tfrac12\tau+e_0+e_1+e_j$ has square $-3+2 = -1$. So every class of odd value contains a vector of square $-1$. Since $\gamma_\Co$ is an anti-isometry, $q_{T_\Co}\bigl(\gamma_\Co(\overline{H/2})\bigr) = -q_{S_\Co}(\overline{H/2}) = -\tfrac14H^2 = -1$, which is odd, so for every gluing anti-isometry $\gamma_\Co$ the class $\gamma_\Co(\overline{H/2})$ is one of the $496$ classes with $q = 1$ (@prop:coble-q-fibers).
(3) $t\perp S_\Co$ because $t\in T_\Co\otimes\bQ = (S_\Co\otimes\bQ)^{\perp}$, so $b\in(S_\Co\perp T_\Co)^{\#}$, with class $(\overline{H/2},\bar t)$ in the gluing subgroup; that subgroup is the graph of $\gamma_\Co$, so $b$ lies in the overlattice it cuts out, which is $\lkt$ (@cor:lifting-unimodular). There $b^2 = \tfrac14H^2+t^2 = 1-1 = 0$, $b\cdot H = \tfrac12H^2 = 2$, and $b\perp H^{\perp S_\Co}$ because both summands are.
(4) Put $J(x)\definedas (x\cdot H)b+(x\cdot b)H-2(x\cdot b)b-x$; the Gram matrix of $H,b$ in that basis is $\begin{pmatrix}4&2\\2&0\end{pmatrix}$ with inverse $\begin{pmatrix}0&\tfrac12\\\tfrac12&-1\end{pmatrix}$, so $J$ is twice the projection onto $\langle H,b\rangle_{\bQ}$ minus the identity, and it is an integral combination of $H$, $b$ and $x$ for $x\in\lkt$. Hence $J$ is an isometry of $\lkt$ with $J^2 = \id$; it fixes $H$ and $b$ and negates the orthogonal complement of $\langle H,b\rangle$, so its $(+1)$-eigenspace is $\langle H,b\rangle_{\bQ}\cap\lkt$, which is $\langle H,b\rangle$: if $mH+nb = 2y$ with $y\in\lkt$ then $2m+n = (mH+nb)\cdot e_9$ is even, so $n$ is even, and then $mH = 2y-nb$ forces $m$ even because $H$ is primitive in $\lkt$. The Gram matrix has determinant $-4$ and is even, so $\langle H,b\rangle\cong U(2) = \sdp$; and $S_\Co\cap\langle H,b\rangle = \ZZ H$, since $(b+mH)\cdot H = 2+4m\neq0$ for every $m$. For commutation, $I_\Co$ is $+\id$ on $S_\Co$ and $-\id$ on $T_\Co$, so $I_\Co(t) = -t$ and $I_\Co(b) = \tfrac12H-t = H-b$, which preserves $\langle H,b\rangle$, and an involution is determined by its $(+1)$-eigenspace. The coinvariant lattice $\langle H,b\rangle^{\perp\lkt}$ is even of rank $20$ and signature $(2,18)$, and its discriminant form is that of $U(2)$ up to sign — of order $4$, with integral values — so it is $2$-elementary with $a = 2$ and $\delta = 0$; $T_{\mathrm{dP}} = \Delta^-(U)\perp U\perp E_8^2\cong U(2)\perp U\perp E_8^2$ has the same invariants, so the two are isometric by @thm:two-elementary-classification. An isometry $\sdp\iso\langle H,b\rangle$ then extends to an isometry of $\lkt$: after fixing any isometry of the two complements, the remaining mismatch is an element of $\Orth\bigl(A_{\langle H,b\rangle^{\perp}}\bigr)$, which @thm:two-elementary-surjectivity realises by an isometry of $\langle H,b\rangle^{\perp}$, and the compatible pair extends by @cor:lifting-unimodular. So $J$ is conjugate to $I_{\mathrm{dP}}$ in $\Orth(\lkt)$, and its orbit is that of [@AEGS25]'s involution. Finally, a symplectic involution fixes the holomorphic $2$-form, whose real and imaginary parts span a positive definite $2$-plane inside the $(+1)$-eigenspace, and $U(2)$ has signature $(1,1)$, which contains no positive definite $2$-plane.
:::

::: {.proposition #prop:no-rank-one-automorphism title="A rank-one del Pezzo slot is induced by no automorphism"}

Let $\widetilde X$ be a projective K3 surface over $\CC$, let $\iota$ be a nonsymplectic involution of it with invariant lattice $S \definedas H^2(\widetilde X,\bZ)^{\iota}$, and let $\iota'$ be an involution commuting with $\iota$ whose invariant lattice $S'$ is isometric to $U(2)$.
Let $H\in S\cap S'$ with $H^2 = 4$, suppose $\rk(S\cap S') = 1$, and let $\alpha\in S$ be effective with $\alpha^2 = -2$ and $H\cdot\alpha = 0$.
Then $\iota'(\alpha) = -\alpha$, and no automorphism of $\widetilde X$ induces $\iota'$.
:::

::: {.proof}

$S$ is even because $H^2(\widetilde X,\bZ)$ is, and it has signature $(1,\cdot)$: $\iota$ is nonsymplectic, so it acts as $-\id$ on $H^{2,0}\oplus H^{0,2}$, and a Kähler class can be averaged over $\set{\id,\iota}$ to an invariant one.
Hence $H$, of positive square, spans a maximal positive definite subspace, and $H^{\perp S}$ is negative definite, the orthogonal complement of a non-isotropic vector being nondegenerate.
$\iota'$ commutes with $\iota$, so it preserves $S$, and $A \definedas S\cap S'$ is the fixed lattice of $\iota'$ in $S$; it is saturated in $S$ because both factors are saturated in $H^2(\widetilde X,\bZ)$.
By hypothesis $\rk A = 1$ and $H\in A$, so $A = \ZZ H$: $H$ is primitive in $S$, since $H/2\in S$ would give $(H/2)^2 = 1$, odd in an even lattice.
Therefore $\iota'$ is $+\id$ on $\ZZ H$ and $-\id$ on $H^{\perp S}$, which is its $(-1)$-eigenspace in $S$.
The class $\alpha$ lies in $S$ and $\alpha\cdot H = 0$, so $\alpha\in H^{\perp S}$ and $\iota'(\alpha) = -\alpha$.
If $g\in\Aut(\widetilde X)$ had $g^* = \iota'$, then $g_*\alpha = (g^*)^{-1}\alpha = -\alpha$ would be the class of the effective divisor $g(D)$, for any effective divisor $D$ of class $\alpha$.
But $\alpha\cdot A_0>0$ for an ample class $A_0$, since $\alpha\neq0$ is effective and $\widetilde X$ is projective, whereas $(-\alpha)\cdot A_0<0$. Contradiction.
:::

::: {.proposition #prop:local-operators title="The two involutions of the nodal cover, their fixed loci and their symplectic characters"}

Let $X^\sharp = \set{z^2 = f(x,y)}$ over the $\tau$-fixed point $p$ of $Y$, with $f$ having a nondegenerate quadratic part there, and let
$$\iota_{\mathrm{dP}}(x,y,z) = (x,y,-z),\qquad \iota_\Co(x,y,z) = (-x,-y,-z).$$
Then:
1. the two commute, and $\iota_\Co\iota_{\mathrm{dP}}(x,y,z) = (-x,-y,z)$;
2. all three act on the holomorphic $2$-form $\omega = \frac{dx\wedge dy}{2z}$ by $\iota_{\mathrm{dP}}^*\omega = -\omega$, $\iota_\Co^*\omega = -\omega$ and $(\iota_\Co\iota_{\mathrm{dP}})^*\omega = +\omega$: both involutions are nonsymplectic and their product is symplectic;
3. $\mathrm{Fix}(\iota_{\mathrm{dP}}) = \set{z = 0}\cap X^\sharp$, the branch curve, nodal at $p$;
4. $\mathrm{Fix}(\iota_\Co)$ is contained in the singular points of $X^\sharp$: if $\iota_\Co(x,y,z) = (x,y,z)$ then $x = y = 0$ and $z = -z$, so $z = 0$ and $f(0,0) = 0$; and $f$ is $\tau$-invariant, so its terms of odd order at the $\tau$-fixed point $p$ vanish and the vanishing order there is even — the point is singular, of type $A_1$ when the quadratic part is nondegenerate. So $\iota_\Co$ has no isolated fixed point, which is what its nonsymplecticity requires: at an isolated fixed point the differential would be $-\id$ on the tangent space and $\omega$ would be preserved.
:::

::: {.proof}

(1) is substitution. (2) is the residue form: on $X^\sharp$ away from $z = 0$ one has $\omega = \frac{dx\wedge dy}{2z}$, and $\iota_{\mathrm{dP}}^*(dx\wedge dy) = dx\wedge dy$ with $\iota_{\mathrm{dP}}^*(2z) = -2z$, while $\iota_\Co^*(dx\wedge dy) = (-dx)\wedge(-dy) = dx\wedge dy$ with $\iota_\Co^*(2z) = -2z$; the product fixes $z$ and acts by $(-dx)\wedge(-dy)$ on the $x,y$-form, so it scales $\omega$ by $+1$.
(3) $z = -z$ gives $z = 0$, and then $f(x,y) = z^2 = 0$.
(4) $x = -x$ and $y = -y$ give $x = y = 0$; then $z = -z$ gives $z = 0$ and $f(0,0) = 0$. Since $f(-x,-y) = f(x,y)$, every monomial of odd total degree has coefficient $0$, so the lowest-order part at the origin is even and $f$ vanishes there to order at least $2$; with nondegenerate quadratic part that is an $A_1$ point. For the last sentence: at an isolated fixed point $d\iota$ has no eigenvalue $1$, so being an involution it equals $-\id$ and $\iota^*\omega = \det(d\iota)\,\omega = +\omega$ there, against $\iota^*\omega = -\omega$.
:::

::: {.example #ex:product-eight-points title="The fixed points of the product involution"}

The product $\rho = \iota_\Co\iota_{\mathrm{dP}}$ of @prop:local-operators is $\rho(x,y,z) = (-x,-y,z)$, so its fixed points are the points over the four $\tau$-fixed points of $Y$, where $z^2 = f$.
Over a fixed point at which $f\ne0$ there are two, $z = \pm\sqrt f$.
Over one at which $f = 0$ the single point is the node, which the resolution replaces by the two points $[1:\pm i:0]$ of @prop:del-pezzo-type-on-the-resolution(2).
So $\rho$ has $2\cdot4 = 8$ fixed points when $I_\Co$ has no fixed point, and $2\cdot3+2 = 8$ with one node.
By the formula of @prop:tuple-of-the-construction, $\rk S_\rho = \tfrac12(8+20) = 14$, and $S_\Co\cap S_{\mathrm{dP}}\subseteq S_\rho$ because a class fixed by both involutions is fixed by their product.
:::

::: {.proposition #prop:del-pezzo-type-on-the-resolution title="The invariant type of the lifted del Pezzo involution on the resolution"}

Let $\widehat X\to X^\sharp$ be the minimal resolution of the node at $p$, $D$ the exceptional $(-2)$-curve, and $\widehat\iota_{\mathrm{dP}}$, $\widehat\iota_\Co$ the lifts. Then:
1. $\widehat\iota_\Co$ acts trivially on the exceptional $\PP^2$ and hence fixes $D$ pointwise;
2. $\widehat\iota_{\mathrm{dP}}$ acts on that $\PP^2$ by $[X:Y:Z]\mapsto[X:Y:-Z]$, so it preserves the conic $D = \set{Z^2 = X^2+Y^2}$ and fixes on it exactly the two points $[1:\pm i:0]$, which are also where the proper transform of the branch curve meets $D$;
3. consequently $\mathrm{Fix}(\widehat\iota_{\mathrm{dP}})$ is the normalization of the branch curve: for $f$ with exactly $k$ nodes and otherwise smooth, the branch curve has arithmetic genus $9$ and geometric genus $9-k$, so $\chi(\mathrm{Fix}) = 2-2(9-k) = 2k-16$, and Lefschetz gives $\rk S_{\mathrm{dP}} = \tfrac12(22+(2k-16)-2) = 2+k$;
4. $S_{\mathrm{dP}}$ contains $\pi^*\Pic(Y)\perp\ZZ D_1\perp\cdots\perp\ZZ D_k$, of rank $2+k$: the pullbacks of $\Pic(Y) = \ZZ^2$ have Gram matrix $U(2)$, each $D_g$ is a $(-2)$-class because it is preserved by $\widehat\iota_{\mathrm{dP}}$, and $D_g\perp\pi^*\Pic(Y)$ and $D_g\perp D_{g'}$ for $g\ne g'$ because the resolution contracts them.
So $S_{\mathrm{dP}}$ contains $U(2)\perp\langle-2\rangle^{\oplus k}$ with finite index, and $S_{\mathrm{dP}}\not\cong U(2)$ whenever $k\neq0$.
:::

::: {.proof}

(1) and (2) are the substitution $(-x,-y,-z)$ and $(x,y,-z)$ in homogeneous coordinates on the exceptional $\PP^2$, whose point set is the conic $\set{Z^2 = X^2+Y^2}$; the fixed points of $[X:Y:Z]\mapsto[X:Y:-Z]$ on it satisfy $Z = 0$, that is $X^2+Y^2 = 0$, and the two branches of the nodal curve $\set{z = 0, f = 0}$ have exactly those tangent directions.
(3) the proper transform of the branch curve under the resolution of its node is its normalization, of geometric genus $9-k$; the two fixed points on $D$ are its two points over the node, so they are part of it and contribute nothing further.
(4) as stated, with the projection formula giving $(\pi^*F)\cdot(\pi^*G) = \deg\pi\,(F\cdot G) = 2(F\cdot G)$, which is $U(2)$ on the basis of $\Pic(\PP^1\times\PP^1)$.
:::

::: {.proposition #prop:tuple-of-the-construction title="The construction's own tuple satisfies the five conditions of the tuple"}

Let $\pi\colon X^\sharp = \set{z^2 = f(x,y)}\to Y = \PP^1\times\PP^1$ be the double cover branched along $B = \set{f = 0}\in\abs{\OO_Y(4,4)}$, so that $K_{X^\sharp} = \pi^*(K_Y+\OO_Y(2,2)) = 0$, and let $\widehat X\to X^\sharp$ be the resolution of the $k$ nodes of $B$, all of them at $\tau$-fixed points. Put $H\definedas\pi^*\OO_Y(1,1)$, and let $\alpha\definedas[D_g]$ be the class of the exceptional curve over one of them. Then
1. $H^2 = 4$, and $H$ is fixed by both $I_\Co$ and $I_{\mathrm{dP}}$;
2. $\alpha^2 = -2$, $H\cdot\alpha = 0$, and $\alpha$ is fixed by $I_\Co$ and by $I_{\mathrm{dP}}$;
3. $H$ is nef and big, $h^0(\widehat X,H) = 4$, and $\alpha$ is the class of an effective curve;
4. both involutions are nonsymplectic and their product is symplectic;
5. $\rk S_{\mathrm{dP}} = k+2$ and $\rk S_\Co = k+10$;
6. $\pi^*\Pic(Y)\perp\ZZ D_1\perp\cdots\perp\ZZ D_k\subseteq S_\Co\cap S_{\mathrm{dP}}$, and $S_{\mathrm{dP}}\subseteq S_\Co$.
So for $k\ge1$ the five bullets of @sec-labeled-lattice-data hold on $\widehat X$: the tuple of the direct-projective construction exists, and its quotient by $I_\Co$ is not Enriques.
:::

::: {.proof}

(1) $(\pi^*\OO(1,1))^2 = \deg\pi\,(\OO(1,1))^2 = 2\cdot2 = 4$. Both involutions satisfy $\pi\circ\iota = \iota'\circ\pi$, with $\iota' = \id_Y$ for $\iota_{\mathrm{dP}}$ and $\iota' = \tau$ for $\iota_\Co$; and $\tau$ acts by $[-1]$ on each factor, with $[-1]^*\OO(1) = \OO(1)$, so $\iota'^*\OO(1,1) = \OO(1,1)$ in both cases and $\widehat\iota^*H = \pi^*\iota'^*\OO(1,1) = H$, the resolution being equivariant.
(2) $D_g$ is a $(-2)$-curve, fixed pointwise by $\widehat\iota_\Co$ and preserved by $\widehat\iota_{\mathrm{dP}}$ (@prop:del-pezzo-type-on-the-resolution, parts 1 and 2); and $H\cdot D_g = \OO(1,1)\cdot\pi_*D_g = 0$ because $\pi_*D_g = 0$, the curve lying in a fibre of the resolution.
(3) $\OO_Y(1,1)$ is very ample, the Segre embedding, hence nef; for a curve $C$ one has $H\cdot C = \OO(1,1)\cdot\pi_*C\ge0$, so $H$ is nef, and $H^2 = 4>0$ with $H$ nef makes $H$ big on a surface. The surface $X^\sharp$ is normal, so the resolution $\nu\colon\widehat X\to X^\sharp$ has $\nu_*\OO_{\widehat X} = \OO_{X^\sharp}$, and $\pi_*\OO_{X^\sharp} = \OO_Y\oplus\OO_Y(-2,-2)$; by the projection formula $h^0(\widehat X,H) = h^0(\OO_Y(1,1))+h^0(\OO_Y(-1,-1)) = 4+0$. $\alpha$ is the class of the curve $D_g$.
(4) @prop:local-operators, part 2, computes the two characters on $X^\sharp$; away from the nodes the resolution is an isomorphism and both involutions act on the exceptional curves, so the characters are unchanged.
(5) For a nonsymplectic involution of a K3 with fixed locus $F$, Lefschetz gives $\chi(F) = 2+\tr$. Decompose over $\QQ$, where the eigensplitting is available: $H^2(\widehat X,\QQ) = S_\QQ\oplus T_\QQ$ with $\id$ on $S$ and $-\id$ on $T$, so $\tr = \rk S-\rk T$ and, with $\rk S+\rk T = 22$, $\tr = 2\rk S-22$ and $\rk S = \tfrac12(\chi(F)+20)$. For $\widehat\iota_{\mathrm{dP}}$ the fixed locus is the normalization of $B$, of $\chi = 2k-16$ (@prop:del-pezzo-type-on-the-resolution, part 3), so $\rk S_{\mathrm{dP}} = k+2$. For $\widehat\iota_\Co$ it is the disjoint union of the $k$ exceptional curves: @prop:local-operators, part 4, puts every fixed point of $\iota_\Co$ at a singular point, and @prop:del-pezzo-type-on-the-resolution, part 1, makes the curve over each of them fixed pointwise. So $\chi(F) = 2k$ and $\rk S_\Co = k+10$. At $k = 0$ this last value is $10$, the rank of the invariant lattice of an Enriques involution of a K3, which is what $I_\Co$ is when its fixed locus is empty.
(6) The involution $\iota_{\mathrm{dP}}$ is the deck transformation of $\pi$, so it fixes every class $\pi^*c$; the involution $\iota_\Co$ covers $\tau$, and $\tau^*\OO_Y(a,b) = \OO_Y(a,b)$, so it fixes every $\pi^*c$ too. Each $D_g$ is fixed by both involutions by (2), and $D_g\cdot\pi^*c = c\cdot\pi_*D_g = 0$, while $D_g\cdot D_{g'} = 0$ for $g\ne g'$. This gives the first containment. That sublattice has rank $k+2 = \rk S_{\mathrm{dP}}$ by (5) and @prop:del-pezzo-type-on-the-resolution, part 4. The invariant lattice $S_\Co$ of an isometry is primitive in $H^2(\widehat X,\ZZ)$, so $S_\Co\cap S_{\mathrm{dP}}$ is primitive in $S_{\mathrm{dP}}$; it has full rank, so it is $S_{\mathrm{dP}}$.
:::

::: {.proposition #prop:one-node-family title="The one-node construction is a smooth proper equivariant family with a relative polarization and an exceptional divisor"}

Let $B\subset\abs{\OO_Y(4,4)}^\tau$ be the set of $\tau$-invariant sections whose branch curve has exactly one node, at the $\tau$-fixed point $p$, and is otherwise smooth with nondegenerate quadratic part at $p$; it is open in the invariant linear system of @sec-invariant-system, and it is nonempty by @ex:one-node-branch-curve. Put $\mathcal L\definedas\OO_Y(2,2)$, a square root of $\OO_Y(4,4)$, and $\mathcal Y\definedas Y\times B$. Then:
1. $\mathcal X^\sharp = \Spec_{\mathcal Y}(\OO_{\mathcal Y}\oplus\mathcal L^{-1})$, with algebra structure $z^2 = f_b$ for $z$ the coordinate on the $\mathcal L$-summand, is a flat family of surfaces, finite and hence proper and projective over $\mathcal Y$ and over $B$, smooth away from the section $\sigma$ over $p$; the blow-up $\beta\colon\widehat{\mathcal X}\to\mathcal X^\sharp$ of $\sigma(B)$ is smooth and proper over $B$ with K3 fibres;
2. $\iota_\Co$ and $\iota_{\mathrm{dP}}$ act fibrewise, commute, and fix $\sigma$, hence lift to $\widehat{\mathcal X}$ commuting with $\beta$;
3. $\mathcal H\definedas\pi^*\OO_Y(1,1)$ is a line bundle on $\widehat{\mathcal X}$ whose restriction to every fibre is nef of degree $4$, hence big, and not ample, its degree on the exceptional curves being $0$; its class is $H_b$;
4. the exceptional divisor $\mathcal D$ of $\beta$ is a $\PP^1$-bundle over $B$ with $\mathcal D_b^2 = -2$ and $\mathcal H_b\cdot\mathcal D_b = 0$, and $c_1(\mathcal H)$ and $[\mathcal D]$ are sections of $R^2\widehat\pi_*\ZZ$ flat for the Gauss–Manin connection.
:::

::: {.proof}

$B$ is open because the node condition is the vanishing of the coefficient of $x_0^4y_0^4$ at $p$ together with nondegeneracy of the quadratic part, an open condition (@lem:node-condition, @sec-invariant-system), and smoothness elsewhere is open.
(1) Since $\mathcal L^2 = \OO_Y(4,4)$, the sheaf of algebras $\OO\oplus\mathcal L^{-1}$ with $z^2 = f_b$ is a coherent sheaf of $\OO_{\mathcal Y}$-algebras, flat over $B$ because $f_b$ varies linearly, so $\mathcal X^\sharp\to B$ is finite and flat and the fibres are surfaces; the linear system is base-point free, so no fibre contains a component of a $\PP^1$-fibre and $B$ parametrizes a bounded family; projectivity comes from finiteness over the projective $\mathcal Y\to B$. The branch curve of the double cover is $B$, and $K_{\mathcal X^\sharp} = \pi^*(K_Y+\mathcal L) = \pi^*(\OO(-2,-2)+\OO(2,2)) = \OO_{\mathcal X^\sharp}$, with $\pi_*\OO_{\mathcal X^\sharp} = \OO_Y\oplus\mathcal L^{-1} = \OO_Y\oplus K_Y$; the fibres are K3 surfaces. The singular points of the fibres are the nodes, one per fibre by construction, at $p$; locally the family is $z^2 = q_b(x,y) + (\text{terms of order }\ge3)$ with $q_b$ nondegenerate for every $b\in B$, so the singular locus is exactly $\sigma(B)$ and is a family of ordinary double points, which the blow-up of $\sigma(B)$ resolves simultaneously in a smooth family; on each fibre the blow-up replaces the node by a $(-2)$-curve.
(2) $\iota_{\mathrm{dP}}$ acts by $z\mapsto-z$ and $\iota_\Co$ by $(z,x,y)\mapsto(-z,-x,-y)$ on the $\mathcal L$-coordinate and on $Y$; both preserve each equation, commute, and fix the point over $p$, where $z = 0$; an automorphism fixing the centre of a blow-up lifts to it.
(3) $H_b\cdot C = \OO(1,1)\cdot\pi_b(C)\ge0$ for every curve $C$ on a fibre, since $\OO(1,1)$ is ample, so $H_b$ is nef; $H_b^2 = \deg\pi_b\cdot(\OO(1,1))^2 = 4>0$, so $H_b$ is big; and $H_b\cdot D_b = 0$ against the curve $D_b$, so $H_b$ is not ample.
(4) The exceptional divisor of the blow-up of a smooth subscheme is the projectivized normal bundle, so a $\PP^1$-bundle over $B$ when the centre is a smooth section; its fibre is $D_b$, of square $-2$, and $\pi$ contracts it, so $\mathcal H_b\cdot\mathcal D_b = 0$. The classes of a flat family of divisors are flat sections of $R^2\widehat\pi_*\ZZ$.
:::

::: {.proposition #prop:one-node-connected title="The one-node locus is path-connected: any two members lie on a pencil meeting the bad strata in finitely many points"}

Let $H = \set{f(p) = 0}\subset\abs{\OO_Y(4,4)}^\tau$, of dimension $11$ since evaluation at $p$ is a nonzero functional, and let $B\subset H$ be the members whose branch curve is smooth away from $p$ and has a nondegenerate node at $p$, exactly the locus of @prop:one-node-family. Then $B$ is nonempty, and for any $f_0,f_1\in B$ the pencil through them meets the complement of $B$ in at most finitely many points, so $f_0$ and $f_1$ lie in one path-connected subfamily of $B$.
:::

::: {.proof}

Write $\ell\subset\abs{\OO_Y(4,4)}$ for the projective line through $f_0$ and $f_1$; it lies in $H$ because vanishing at $p$ is linear. Its base locus contains $p$, and it meets $C_{f_0}\cap C_{f_1}$. The conditions a member can fail to meet $B$ are, one by one, closed conditions on $\ell$ that are not identically satisfied:
- a shared base point $q\ne p$: "singular at $q$" is a closed linear evaluation condition, and it cannot hold for every member of the pencil, since $f_0$ is not singular at $q$;
- degeneracy of the quadratic part at $p$: this is the vanishing of a determinant of five coefficients, closed on $\ell$, and $f_0$ does not satisfy it;
- a singularity away from the base locus: by Bertini's theorem for pencils on a smooth variety, a general member of $\ell$ has no singularity outside the base locus, so the set of such $t$ is a closed proper subset.

Each of those closed loci is therefore a finite subset of $\ell$, as is their union.
The curve of @ex:one-node-branch-curve lies in $B$, so $B\ne\varnothing$.
A projective line with finitely many points removed is path-connected, so $f_0$ and $f_1$ are joined by a path in $\ell\cap B$.
:::

::: {.theorem #thm:a21-labels title="The labels of any two tuples of the one-node direct-projective construction are conjugate"}

Let $\mathfrak L$, $\mathfrak L'$ be tuples of the direct projective construction arising from one-node members, in the sense of @prob:coble-rigidity. Then there is $\gamma\in\Orth(\lkt)$ mapping the involutions to the involutions, the degree-$4$ class to the degree-$4$ class, and the effective root to the effective root:
$$\gamma S_{\Co} = S'_{\Co},\qquad \gamma S_{\mathrm{dP}} = S'_{\mathrm{dP}},\qquad \gamma H = H',\qquad \gamma\alpha = \alpha'.$$
:::

::: {.proof}

By @prop:one-node-connected both parameter points lie in one connected $B$, so they are joined by a path; the family of @prop:one-node-family is smooth and proper over $B$ with $\mathcal H$ and $\mathcal D$ flat; @thm:one-node-transport applied to the path gives the conclusion.
:::

::: {.theorem #thm:one-node-transport title="Parallel transport preserves the lattice labels"}

In the situation of @prop:one-node-family let $\theta$ be a path in $B$ from $b$ to $b'$, and let $\psi_\theta\colon H^2(\widehat X_b,\ZZ)\iso H^2(\widehat X_{b'},\ZZ)$ be the Gauss–Manin parallel transport. Then $\psi_\theta H_b = H_{b'}$, $\psi_\theta\alpha_b = \alpha_{b'}$, and $\psi_\theta$ intertwines $\widehat\iota_{\Co,b},\widehat\iota_{\mathrm{dP},b}$ with $\widehat\iota_{\Co,b'},\widehat\iota_{\mathrm{dP},b'}$; hence, after markings, there is $\gamma\in\Orth(\lkt)$ with
$$\gamma S_{\Co,b} = S_{\Co,b'},\qquad \gamma S_{\mathrm{dP},b} = S_{\mathrm{dP},b'},\qquad \gamma H_b = H_{b'},\qquad \gamma\alpha_b = \alpha_{b'}.$$
:::

::: {.proof}

Parallel transport is an isometry of the fibres of $R^2\widehat\pi_*\ZZ$ and is compatible with flat sections, which $c_1(\mathcal H)$ and $[\mathcal D]$ are (@prop:one-node-family, part 4); that gives the first two. The involutions act on the total space, so transport intertwines them; a $(+1)$-eigenspace is determined by its involution, so the fixed lattices go to fixed lattices. Choosing markings and composing the transports gives $\gamma$.
:::

::: {.lemma #lem:face-at-H title="The curves contracted by $\pi$ are the ray in the cone of curves, and its annihilator is the smallest face of the nef cone through $H$"}

In the situation of @prop:one-node-family, on every fibre, with $\Delta_b$ and the chamber $\mathfrak c_b$ as in @def:coble-polarization-classes, part 3:
1. $\alpha_b = \pi_b^*e$, where $e\subset\widehat Y = \Bl_pY$ is the exceptional curve;
2. $\overline{\mathrm{NE}}(\widehat X_b)\cap H_b^\perp = \RR_{\ge0}\alpha_b$, and the classes of the irreducible curves contracted by $\pi_b$ are exactly the positive multiples of $\alpha_b$;
3. the nef cone $\mathcal N_b = \overline{\mathrm{NE}}(\widehat X_b)^\vee$ has a unique face $F_b$ whose relative interior contains $H_b$, namely
$$F_b = \set{v\in\mathcal N_b : v\cdot\alpha_b = 0},$$
and $H_b\cdot\gamma>0$ for every curve class $\gamma$ outside the ray $\RR_{\ge0}\alpha_b$;
4. no wall $\delta^\perp$ with $\delta\in\Delta_b\setminus\set{\alpha_b}$ passes through $H_b$, and the chamber $\mathfrak c_b$ has $H_b$ in its closure and lies on the side $x\cdot\alpha_b>0$.
:::

::: {.proof}

(1) $\pi^{-1}(p)$ is the single node $\hat p$ of $X^\sharp_b$, the cover being ramified there, so the pullback of the maximal ideal of $p$ is invertible on $\widehat X_b$ and $\pi_b$ factors through $\widehat X_b\to\widehat Y = \Bl_pY$, the double cover branched along the proper transform $\widetilde B$. The preimage of $e$ is therefore $D_b$, and $D_b\to e$ is the double cover branched at $e\cap\widetilde B$, of degree $e\cdot\widetilde B = -2e^2 = 2$; being branched, $\pi_b^*e = D_b$, that is $\alpha_b = \pi_b^*e$, and $(\pi_b^*e)^2 = 2e^2 = -2$.
(2) $H_b\cdot C = \OO(1,1)\cdot\pi_b(C)$ with $\OO(1,1)$ ample, so it vanishes exactly when $\pi_b(C)$ is a point, that is when $C$ is contracted by $\pi_b$. Since $\pi_b$ factors through the finite map $X^\sharp_b\to Y$, which contracts no curve, $C$ is contracted by the resolution $\widehat X_b\to X^\sharp_b$, whose only exceptional curve is $D_b$; so $[C]\in\QQ_{\ge0}\alpha_b$. Passing to the closure of the cone spanned by curve classes gives the same ray.
(3) For a closed convex cone $K$ and $y\in K^\vee$, the set $F = \set{z\in K^\vee : \langle z,x\rangle = 0 \ \text{for all } x\in K \text{ with } \langle y,x\rangle = 0}$ is the smallest face of $K^\vee$ containing $y$, and $y$ lies in its relative interior. Taking $K = \overline{\mathrm{NE}}(\widehat X_b)$, whose dual cone is the nef cone, and using (2), the defining set is $\RR_{\ge0}\alpha_b$ and $F = F_b$ as displayed. For the last clause: $H_b$ is nef, so $H_b\cdot\gamma\ge0$ for every curve class, and it vanishes only on the ray by (2).
(4) Let $\delta\in\Delta_b$ have $H_b\cdot\delta = 0$. Writing $\delta = \sum a_iC_i$ over irreducible curves with $a_i>0$ gives $0 = \sum a_i(C_i\cdot H_b)$ with every term non-negative, so each $C_i$ is orthogonal to $H_b$ and hence, by (2), equal to $D_b$; then $\delta = m\alpha_b$ and $-2 = -2m^2$ forces $m = 1$. So $\delta = \alpha_b$.
$H_b$ is nef, so it lies in the closure of $\Amp(\widehat X_b)$, and every ample class is positive on $\alpha_b$, the class of an effective curve. So the chamber $\mathfrak c_b$, which contains $\Amp(\widehat X_b)$, has $H_b$ in its closure and lies on the side $x\cdot\alpha_b>0$.
:::

::: {.proposition #prop:chamber-pinned title="When the walls do not accumulate at $H$, the labels determine the chamber"}

In the situation of @lem:face-at-H, suppose that there is a convex open neighbourhood $U$ of $H_b$ in the cone $\mathcal C_b\definedas\mathcal C_{\widehat X_b}$ of @def:coble-polarization-classes, part 3, that meets no wall $\delta^\perp$ with $\delta\in\Delta_b\setminus\set{\alpha_b}$. Then $\mathfrak c_b$ is the only component of $\mathcal C_b\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp$ whose closure contains $H_b$ and which lies on the side $x\cdot\alpha_b>0$.
:::

::: {.proof}

On $U$ the only wall is $\alpha_b^\perp$, so $U\setminus\alpha_b^\perp$ is the disjoint union of the convex sets $U_+ = U\cap\set{x\cdot\alpha_b>0}$ and $U_- = U\cap\set{x\cdot\alpha_b<0}$. Each is connected and meets no wall, so each lies in a single component of the complement of the walls.
Let $\mathfrak c$ be a component whose closure contains $H_b$ and which lies on the side $x\cdot\alpha_b>0$. Then $\mathfrak c$ meets $U$, and $\mathfrak c\cap U\subseteq U_+$. So $\mathfrak c$ meets $U_+$, and it is the component that contains $U_+$.
By @lem:face-at-H, part 4, $\mathfrak c_b$ is such a component, so $\mathfrak c = \mathfrak c_b$.
:::

::: {.corollary #cor:construction-monodromy title="The monodromy of the one-node construction lies in the stabilizer of its lattice labels"}

In the situation of @prop:one-node-family the monodromy representation of $R^2\widehat\pi_*\ZZ$ on $H^2(\widehat X_b,\ZZ)$ lands, after a marking, in the stabilizer in $\Orth(\lkt)$ of the quadruple $(S_\Co,S_{\mathrm{dP}},H,\alpha)$, that is in the group of isometries that commute with both involutions and fix $H$ and $\alpha$.
:::

::: {.proof}

Monodromy is parallel transport along loops, which by @thm:one-node-transport preserves each of the four pieces.
:::

::: {.proposition #prop:det-saturation-del-pezzo title="The del Pezzo invariant lattice is the flat lattice, index one"}

Let the branch curve $B$ have at most one node, at a $\tau$-fixed point $p$ and with nondegenerate quadratic part there, and be otherwise smooth.

1. If $B$ has one node, let $\widehat X_b$ be the resolved K3 surface of @prop:del-pezzo-type-on-the-resolution, the double cover of $\widehat Y = \Bl_p(\PP^1\times\PP^1)$ branched along the smooth proper transform $\widetilde B$, with $e_b = \widehat\pi^*h_1$, $f_b = \widehat\pi^*h_2$ the ruling pullbacks and $D_b = \widehat\pi^*e$ the exceptional $(-2)$-curve. Then
$$S_{\mathrm{dP},b}=H^2(\widehat X_b,\ZZ)^{\widehat\iota_{\mathrm{dP}}=+1}
=\Lambda\definedas\langle e_b,f_b,[D_b]\rangle\cong U(2)\perp\langle-2\rangle,\qquad \det S_{\mathrm{dP},b} = 8,$$
and the index-$2$ overlattice $U\perp\langle-2\rangle$ (determinant $2$) does not occur. In particular every $I_{\mathrm{dP}}$-invariant class pairs evenly with each ruling class.
2. If $B$ is smooth, then $S_{\mathrm{dP}} = \pi^*H^2(Y,\ZZ)\cong U(2)$.
:::

::: {.proof}

Write $L\definedas H^2(\widehat X_b,\ZZ)$ and $S\definedas S_{\mathrm{dP},b}$, and prove (1); the proof of (2) is the same with $\widehat Y$ replaced by $Y$ and $D_b$ omitted.

*Step 1 (index bound).* $S$ is even and primitive in $L$. Since $\widehat\pi$ is finite flat of degree $2$, the transfer formula $\widehat\pi^*\widehat\pi_* = 1+\widehat\iota_{\mathrm{dP}}^*$ sends $x\in S$ to $2x = \widehat\pi^*\widehat\pi_*x\in\widehat\pi^*H^2(\widehat Y,\ZZ) = \Lambda$. So $2S\subseteq\Lambda\subseteq S$, the two lattices have equal rank, and $[S:\Lambda]^2$ divides $\det\Lambda = 8$; hence $[S:\Lambda]\in\set{1,2}$.

*Step 2 (what index $2$ would impose).* Suppose $[S:\Lambda]=2$. Pick $z\in S\setminus\Lambda$ and write $2z=ae_b+bf_b+cD_b$ with $a,b,c\in\ZZ$. Then $z^2=ab-\tfrac{c^2}2$. Integrality of $z^2$ forces $c$ even, and evenness of $S$ forces $ab$ even. If $a$ and $b$ are both even then $z\in\Lambda$, contrary to the choice. Hence exactly one of $a,b$ is odd, and exactly one of $e_b/2,f_b/2$ lies in $S$; in particular $e_b\in2L$ or $f_b\in2L$.

*Step 3 (no ruling line lies in $B$).* Let $M$ be a line of either ruling of $Y$, and suppose $B = M+B'$. Then $M\cdot B' = 4$, and every point of $M\cap B'$ is a singular point of $B$. The point $p$ is an ordinary node, so if $p\in M$ then $M$ and $B'$ are the two branches of $B$ at $p$ and meet there with intersection multiplicity $1$. So $M\cap B'$ contains a point other than $p$, and $B$ has a second singular point, a contradiction.

*Step 4 (each fibre is a reduced divisor).* The linear system $|e_b|$ is base-point free, because $e_b=\widehat\pi^*h_1$ and $|\OO_Y(1,0)|$ is base-point free; let $\varphi\colon\widehat X_b\to\PP^1$ be the fibration it defines. Its fibres are $\widehat\pi^*M'$ for the members $M'$ of $|h_1|$ on $\widehat Y$. These are reduced divisors: the proper transforms of the lines of the first ruling not through $p$ and, for the line $M_p$ through $p$, the divisor $\widetilde M_p+e$. No component of them lies in $\widetilde B$: a proper transform of a line does not by Step 3, and $e$ does not because $e\cdot\widetilde B = 2$. So $\widehat\pi$ is étale over the generic point of each component, and $\widehat\pi^*M'$ is reduced. So every component of every fibre of $\varphi$ has multiplicity $1$.

*Step 5 (the ruling classes are primitive in $L$).* Suppose $e_b = 2\eta$ with $\eta\in L$; then $\eta\in\mathrm{NS}(\widehat X_b)$, since $e_b$ is of type $(1,1)$. Then $\eta^2=0$, $\eta\cdot e_b=0$ and $\eta\cdot f_b=1$. Since $(-\eta)\cdot f_b=-1<0$ and $f_b$ is nef, $h^0(-\eta)=0$; Riemann–Roch on the K3 surface then gives $h^0(\eta)\ge2$, so let $E\in|\eta|$. Each component of $E$ lies in a fibre of $\varphi$, because $\eta\cdot e_b=0$ and $e_b$ is nef. Group the components by fibre, $E=\sum_v E_v$ with disjoint supports. Then $\sum_vE_v^2 = E^2 = 0$ and each $E_v^2\le0$ by Zariski's lemma, so each $E_v^2 = 0$, and Zariski's lemma gives $E_v=q_vF_v$ with $q_v\in\QQ_{\ge0}$. By Step 4 every coefficient of $F_v$ is $1$, so $q_v\in\ZZ_{\ge0}$. But then
$$1=\eta\cdot f_b=\sum_v q_v\,(e_b\cdot f_b)=2\sum_v q_v,$$
which is impossible. Hence $e_b$ is primitive in $L$, and the same argument with the rulings exchanged shows that $f_b$ is primitive.

*Conclusion.* By Step 5 neither $e_b/2$ nor $f_b/2$ lies in $L$, so by Step 2 the index is not $2$, and $[S:\Lambda]=1$ by Step 1.
:::

::: {.proposition #prop:node-count-invariant title="The number of $\tau$-fixed nodes is an invariant of the tuple"}

Let $f,f'$ be $\tau$-invariant sections of $\OO_Y(4,4)$ whose branch curves have exactly $k$, respectively $k'$, ordinary nodes at $\tau$-fixed points and are otherwise smooth with nondegenerate quadratic part at those points, and let $\mathfrak L,\mathfrak L'$ be the tuples @prop:tuple-of-the-construction attaches to them. Then $\mathfrak L$ and $\mathfrak L'$ are conjugate in $\Orth(\lkt)$ only if $k = k'$. Both $k = 1$ and $k = 2$ occur.
:::

::: {.proof}

A conjugation preserving the labels carries $I_{\mathrm{dP}}$ to $I'_{\mathrm{dP}}$, and conjugate involutions have isometric invariant lattices, of ranks $k+2$ and $k'+2$ by @prop:tuple-of-the-construction; hence $k = k'$.

For the occurrence: the value of a $\tau$-invariant section at the $\tau$-fixed point $([1:0],[1:0])$ is the coefficient of $x_0^4y_0^4$, and correspondingly $x_0^4y_1^4$, $x_1^4y_0^4$, $x_1^4y_1^4$ at the other three fixed points. These four monomials are independent, and every other invariant monomial vanishes at all four points, so the conditions $f(p) = 0$ at chosen fixed points and $f\neq0$ at the others are independent hyperplane conditions in the $\bP^{12}$ of @sec-invariant-system. By @lem:node-condition the general member of each stratum has an ordinary node at each chosen fixed point; degeneracy of the quadratic part there and nodes elsewhere are proper closed conditions, so the general member has neither. Taking one, respectively two, chosen points gives $k = 1$ and $k = 2$.
:::

::: {.proposition #prop:rank-two-slot-boundary title="The rank-two del Pezzo slot"}

In the notation of @prop:no-rank-one-automorphism let $\rk(S\cap S') = 2$.
Then $S\cap S' = S'$, so $S'\subseteq S$; taking isotropic classes $a_1,a_2$ of $S'\cong U(2)$ with $a_1\cdot a_2 = 2$, one has $H = \pm(a_1+a_2)$, and $\alpha = p(a_1-a_2)+\beta$ with $\beta\perp S'$ and $p\in\bQ$ satisfies:
1. $\beta\in S\otimes\bQ\cap H^{\perp}$, which is negative definite, so $\beta^2\le0$; and $\beta^2 = -2+4p^2$, so $p^2\le\tfrac12$; since $\alpha\cdot a_1 = -2p\in\bZ$, this leaves $\alpha\cdot a_1\in\set{-1,0,1}$.
2. $\iota'(\alpha) = -\alpha$ exactly when $\alpha\cdot a_1 = 0$, and in that case no automorphism of $\widetilde X$ induces $\iota'$.
3. In the marking of @prop:coble-cover-marking, $S' = \langle f^*F_1,f^*F_2\rangle$ and $\alpha\cdot f^*F_1 = \alpha\cdot f^*F_2 = 0$, so no automorphism of $X$ induces the rank-two slot.
:::

::: {.proof}

$\rk(S\cap S') = 2 = \rk S'$ and $S\cap S'$ is saturated in $S'$, so the two coincide and $S' = \langle a_1,a_2\rangle$ with $a_i$ isotropic and $a_1\cdot a_2 = 2$. Writing $H = ma_1+na_2$ gives $H^2 = 4mn = 4$, so $(m,n) = \pm(1,1)$.
Decompose $\alpha$ over $\bQ$ as $\alpha = (pa_1+qa_2)+\beta$ with $\beta\perp S'$; then $\alpha\cdot H = 2(p+q) = 0$, so $q = -p$ and the $S'$-component of $\alpha$ is $p(a_1-a_2)$, of square $-4p^2$; the cross terms with $\beta$ vanish, so $\beta^2 = \alpha^2+4p^2 = -2+4p^2$.
$\beta$ lies in $S\otimes\bQ$ and is orthogonal to $H$, so $\beta^2\le0$ by the proof of @prop:no-rank-one-automorphism, giving $p^2\le\tfrac12$; and $\alpha\cdot a_1 = -2p$ is an integer because both classes lie in the lattice, leaving $\alpha\cdot a_1\in\set{-1,0,1}$.
Since $\iota'$ is $\id$ on $S'$ and $-\id$ on $S'^{\perp}$, $\iota'(\alpha) = p(a_1-a_2)-\beta$, which equals $-\alpha$ exactly when $p = 0$, that is exactly when $\alpha\cdot a_1 = 0$. The effectivity argument of @prop:no-rank-one-automorphism then shows that no automorphism induces $\iota'$.
(3) By @lem:rank-two-slot-unique, $S' = \langle f^*F_1,f^*F_2\rangle$. In the basis of @prop:coble-cover-marking, $\alpha\cdot f^*F_1 = (3e_0-\Sum_{i\le10}e_i)\cdot(3e_0-\Sum_{i\le9}e_i) = 18-18 = 0$, and the same computation gives $\alpha\cdot f^*F_2 = 0$. So part 2 applies, as @cor:no-del-pezzo-involution-coble-cover also shows.
:::

::: {.proposition #prop:rank-one-slot-hodge-locus title="The periods at which the rank-one slot is a Hodge isometry"}

Let $t$, $b$ and $J$ be as in @prop:rank-one-slot. Let $X$ be a K3 surface with a marking $H^2(X,\ZZ)\iso\lkt$ under which $S_\Co\subseteq\Pic(X)$, and let $\omega$ span $H^{2,0}(X)$.
Then $2t\in T_\Co$ and $(2t)^2 = -4$, and $J$ is a Hodge isometry of $H^2(X,\ZZ)$ if and only if $\omega\cdot 2t = 0$, that is, if and only if $2t\in\Pic(X)$.
The orthogonal complement $(2t)^{\perp T_\Co}$ has rank $10$ and signature $(2,8)$.
:::

::: {.proof}

By @prop:rank-one-slot, part 2, and its proof, $t\in T_\Co^{\#} = \tfrac12T_\Co$ and $t^2 = -1$; so $2t\in T_\Co$ and $(2t)^2 = -4$.
$J$ is a Hodge isometry exactly when $J\omega\in\CC\omega$. Since $J$ is an involution, the scalar is $\pm1$.
The scalar $+1$ is impossible: then $\omega$ and $\bar\omega$ lie in the $(+1)$-eigenspace $\langle H,b\rangle\otimes\CC$, so the positive definite real $2$-plane spanned by $\operatorname{Re}\omega$ and $\operatorname{Im}\omega$ lies in $\langle H,b\rangle\otimes\RR$, which has signature $(1,1)$.
The scalar $-1$ holds exactly when $\omega\perp\langle H,b\rangle$. Since $H\in S_\Co\subseteq\Pic(X)$, $\omega\cdot H = 0$, and so $\omega\cdot b = \omega\cdot(\tfrac12H+t) = \omega\cdot t$. Hence $J$ is a Hodge isometry exactly when $\omega\cdot 2t = 0$, and by the Lefschetz theorem on $(1,1)$-classes an integral class orthogonal to $\omega$ lies in $\Pic(X)$.
$T_\Co$ has signature $(2,9)$ and $2t$ has negative square, so its orthogonal complement in $T_\Co$ is nondegenerate of rank $10$ and signature $(2,8)$.
:::

## Which of the arithmetic groups is $\Gamma_\Co$ {#sec-gamma-co-comparison}

The **stable group** is
$$
\Gamma_\Co \definedas \Orth^+(T_\Co)^* = \Orth^+(T_\Co)\intersect\discriminantkernel{T_\Co}.
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

1. $\Gamma_\Co\iscontainedin\Gamma^{\mathrm{Hdg}}_\Co$, by $\varphi\mapsto\varphi\oplus\id_{\ZZ\delta}$;
2. $\Gamma_\Co = \ker\bigl(\Gamma^{\mathrm{Hdg}}_\Co\too\Orth(A_{T_\Co}, q_{T_\Co})\bigr)$, so $\Gamma_\Co$ is normal in $\Gamma^{\mathrm{Hdg}}_\Co$ and
   $$
   [\Gamma^{\mathrm{Hdg}}_\Co : \Gamma_\Co]
   = \abs{\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr)}
   \leq \abs{W(E_8)} = 696\,729\,600
   ;
   $$
3. $\Gamma^{\mathrm{Hdg}}_\Co = \Gamma_\Co$ if and only if every element of $\gent$ that preserves the Heegner line acts trivially on the discriminant form of $T_\Co$.
:::

::: {.proof}

(1) Let $\varphi\in\Gamma_\Co$.
The isometry $g_T \definedas \varphi\oplus\id_{\ZZ\delta}$ of $\ZZ\delta\oplus T_\Co$ acts as the identity on $A_{\ZZ\delta}\oplus A_{T_\Co}$: on the second summand because $\varphi\in\ker\rho_{T_\Co}$, and on the first because $A_{\ZZ\delta}\cong\ZZ/2\ZZ$ has trivial automorphism group.
It therefore preserves the gluing subgroup $\generators{(\tfrac12\delta, \tfrac12\zeta)}$ of @lem:coble-heegner-vector, and by @cor:liftable-automorphisms it extends over the overlattice $\ten$ while fixing $\ZZ\delta$ pointwise.
The extension acts trivially on $A_{\ten} = H^{\perp}/H$, since that is a subquotient of the discriminant group on which $g_T$ is the identity.
In the description of @prop:gamma-en-two-gluing take $g_S = \id_{S_\En}$: it fixes $h$, and $\bar g_T\circ\gamma = \gamma = \gamma\circ\bar g_S$ because $\bar g_T = \id$.
Hence $g_T\in\gent$ by that proposition, and $g_T(\delta) = \delta$, so $g_T\in\Stab_{\gent}(\ZZ\delta)$ and its restriction to $T_\Co$ is $\varphi$.

(2) An element of $\Gamma^{\mathrm{Hdg}}_\Co$ is an isometry of $T_\Co$, so its image under $\rho_{T_\Co}$ is defined without a choice of lift, and by (1) the kernel is $\Orth^+(T_\Co)\intersect\ker\rho_{T_\Co} = \Gamma_\Co$.
The index equals the order of the image by the first isomorphism theorem.

For the bound, the image of $\Stab_{\gent}(\ZZ\delta)$ is a subgroup of that of $\gent$.
Restricting $g\in\gent$ to $T_\Co$ gives an isometry with the same discriminant action on the common factor: by @prop:coble-discriminant-group every isometry of $q_{T_\Co}$ fixes the class $\tfrac12\zeta$ and respects the orthogonal decomposition $A_{T_\Co} = \ZZ\tfrac12\zeta\perp A^0$ with $A^0\cong A_{E_{10}(2)}$, so the discriminant representation factors through the isomorphism $\Orth(A_{T_\Co},q_{T_\Co})\iso\Orth(A^0, q_{T_\Co}|_{A^0})$; under it $A^0 = A_{U(2)}\oplus A_{E_8(2)} = A_{\ten}$ with the same form, which is the identification of $A_{\ten}$ with $H^{\perp}/H$ used in @thm:normalization. On $A_{\ten}$ the image of $\gent$ is the $\gamma$-transport of the image of $\Stab_{\Orth(S_\En)}(h)$ described in @prop:gamma-en-two-gluing.
That image is a quotient of $\Stab_{\Orth(S_\En)}(h)$, which by @prop:polarization-stabilizer-enriques is isomorphic to $\theset{\pm1}\times W(E_8)$ of order $2\abs{W(E_8)}$ and whose reduction to the discriminant group has $\id_U\oplus(-\id_{E_8})$ in its kernel by the last claim of that proposition; so the image has order at most $\abs{W(E_8)}$, and the same bound holds for $\rho_{T_\Co}(\Gamma^{\mathrm{Hdg}}_\Co)$.

(3) By (2), the index is one exactly when the image is trivial.
:::

::: {.proposition #prop:gamma-co-in-theta-centralizer title="The stable group inside the Coble centralizer"}

Let $S_\Co\injects\lkt$ be the primitive embedding of @prop:coble-invariant-lattice, with complement $T_\Co$ and gluing anti-isometry $\gamma_\Co\colon A_{S_\Co}\iso A_{T_\Co}$, and let $\theta_\Co\in\Orth(\lkt)$ be the sign involution of @prop:theta-co-exists, whose eigenspaces are $T_\Co$ and $S_\Co$.
Let $\tilde h_\Co\in S_\Co$ be the pullback of the degree-$2$ Coble polarization (@def:coble-polarization-classes), of square $4$, and put
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
Then $\Gamma_\Co\iscontainedin\Gamma^\theta_\Co$, $\Gamma_\Co = \ker\bigl(\Gamma^\theta_\Co\too\Orth(A_{T_\Co},q_{T_\Co})\bigr)$, and $[\Gamma^\theta_\Co : \Gamma_\Co] = \abs{\rho_{T_\Co}(\Gamma^\theta_\Co)}$.
:::

::: {.proof}

By @prop:theta-co-exists an isometry of $\lkt$ commutes with $\theta_\Co$ exactly when it preserves both eigenspaces, and by @thm:automorphism-lifting-criterion a pair $(g_S, g_T)\in\Orth(S_\Co)\times\Orth(T_\Co)$ that preserves both extends over the overlattice $\lkt$ of $S_\Co\oplus T_\Co$ exactly when $\bar g_T\circ\gamma_\Co = \gamma_\Co\circ\bar g_S$.
So $Z_{\Orth(\lkt)}(\theta_\Co)$ is the set of such pairs.

For $\varphi\in\Gamma_\Co$ the pair $(\id_{S_\Co}, \varphi)$ satisfies the condition, since $\bar\varphi = \id$; and $\id_{S_\Co}$ fixes $\tilde h_\Co$.
So $\varphi$ lies in $\Gamma^\theta_\Co$, which is the inclusion.
An element of $\Gamma^\theta_\Co$ is an isometry of $T_\Co$, so its discriminant image is defined without a choice of lift, and the kernel is $\Orth^+(T_\Co)\intersect\ker\rho_{T_\Co} = \Gamma_\Co$; the index is the order of the image.
:::

::: {.lemma #lem:gamma-co-is-tilde-o-plus title="The stable group is $\widetilde\Orth^+(T_\Co)$, definitionally"}

With $\Orth^+(L)\definedas\Theta_\bR(L)$ of @def:lattice-spinor-kernels and $\widetilde\Orth^+(L)$ the pullback of $\widetilde\Orth(L)=\ker\rho_L$ along the inclusion $\Orth^+(L)\injects\Orth(L)$,
$$
\Gamma_\Co = \Orth^+(T_\Co)^* = \widetilde\Orth^+(T_\Co)
.$$
:::

::: {.proof}

The left side is $\Orth^+(T_\Co)\intersect\ker\rho_{T_\Co}$ by the definition of $\Gamma_\Co$ above, and the right side is the same intersection by the definition of a pullback along an inclusion: the pullback of $\ker\rho_L$ along $\Orth^+(L)\injects\Orth(L)$ is the set of those $g\in\Orth^+(L)$ whose image lies in $\ker\rho_L$.
:::

::: {.proposition #prop:gamma-co-two-definitions title="The two further descriptions of $\Gamma_\Co$ are decided by their finite images"}

Let $\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma^\theta_\Co$ be the groups of @prop:gamma-co-in-heegner-group and @prop:gamma-co-in-theta-centralizer.
Then:

1. $\Gamma^{\mathrm{Hdg}}_\Co = \Gamma_\Co$ if and only if $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr) = 1$, and $\Gamma^\theta_\Co = \Gamma_\Co$ if and only if $\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr) = 1$;
2. both $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr)$ and $\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr)$ are subgroups of the finite group $\Orth(A_{T_\Co}, q_{T_\Co})$, of order $46\,998\,591\,897\,600$ by @prop:coble-discriminant-group;
3. $\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr)\neq1$ exactly when some $g\in Z_{\Orth(\lkt)}(\theta_\Co)\intersect\Stab_{\Orth(\lkt)}(\tilde h_\Co)$ has $\restrictionof{g}{T_\Co}$ acting nontrivially on $A_{T_\Co}$, whether or not $\restrictionof{g}{T_\Co}$ lies in $\Orth^+(T_\Co)$.
:::

::: {.proof}

(1) is the second claim of each of the two propositions, which identifies $\Gamma_\Co$ with the kernel of the respective finite image, together with the first isomorphism theorem; a kernel is everything exactly when the image is trivial.
(2) an isometry of $T_\Co$ has a discriminant image, so each image is a subgroup of the finite group acting on $A_{T_\Co}$, and the order of that group is the one @prop:coble-discriminant-group computes.
(3) unwinds the definition of $\Gamma^\theta_\Co$ as the set of restrictions of the elements of that intersection, so a nontrivial image is a restriction acting nontrivially on $A_{T_\Co}$, and conversely.
The definition of $\Gamma^\theta_\Co$ also requires $\restrictionof{g}{T_\Co}\in\Orth^+(T_\Co)$, and this can be arranged. Let $w\in T_\Co$ have $w^2 = 2$ — $\zeta$ of the $\generators{2}$ summand, for instance — so that $s_w\in\ker\rho_{T_\Co}$ and $\spinornorm_\bR(s_w) = [-1]$ by @prop:gamma-co-reflective-set(2) and its proof.
The pair $(\id_{S_\Co}, s_w)$ satisfies the compatibility of @thm:automorphism-lifting-criterion because $\bar s_w = \id$, so it extends to an isometry $\hat h$ of $\lkt$ with $\hat h|_{S_\Co} = \id_{S_\Co}$ and $\hat h|_{T_\Co} = s_w$; then $g\hat h$ commutes with $\theta_\Co$, fixes $\tilde h_\Co$, has restriction $\restrictionof{g}{T_\Co}s_w$ with the same discriminant action as $\restrictionof{g}{T_\Co}$, and spinor norm multiplied by $-1$.
So one of $\restrictionof{g}{T_\Co}$ and $\restrictionof{g}{T_\Co}s_w$ is in $\Orth^+(T_\Co)$, and it lies in $\Gamma^\theta_\Co$ with nontrivial image.
:::

::: {.lemma #lem:polarization-stabilizer-discriminant-nontrivial title="The finite image of the polarization stabilizer is not trivial"}

Let $C = U\oplus E_8$ and $S_\En = C(2) = U(2)\oplus E_8(2)$ be the lattices of @def:enriques-lattice, where $E_8$ is negative definite in that definition's convention, and let $h = u_0+w_0$ be the degree-$2$ polarization class of $S_\En$; put $v \definedas u_0-w_0$.
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

The inclusion $\Gamma_\Co\iscontainedin\Gamma^{\mathrm{Hdg}}_\Co$ of @prop:gamma-co-in-heegner-group is strict, and
$$
\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr) \;=\; G_\Co \definedas \rho_{S_\En}\bigl(\Stab_{\Orth(S_\En)}(h)\bigr),
\qquad
[\Gamma^{\mathrm{Hdg}}_\Co:\Gamma_\Co] \;=\; \abs{G_\Co} \;=\; \abs{W(E_8)} \;=\; 696\,729\,600
,$$
the two finite images being identified through the gluing anti-isometry $\gamma$.
:::

::: {.proof}

Let $s_v$ be the reflection of @lem:polarization-stabilizer-discriminant-nontrivial, so $v = u_0-w_0\in S_\En$, $s_v(h) = h$ and $\rho_{S_\En}(s_v)\neq\id$; put $c \definedas \gamma\,\rho_{S_\En}(s_v)\,\gamma^{-1}\in\Orth(q_{\TEn})$, which is nontrivial.

*Surjectivity.*
$T_\Co$ is even, indefinite and $2$-elementary, so $\rho_{T_\Co}\colon\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is onto (@thm:two-elementary-surjectivity).
By @prop:coble-discriminant-group every isometry of $q_{T_\Co}$ fixes the class $\zeta/2$ and respects the decomposition $A_{T_\Co} = \ZZ(\zeta/2)\perp A^0$, so the representation factors through $\Orth(q_{T_\Co})\iso\Orth(q_{T_\Co}|_{A^0})$, and $A^0$ is identified with $A_{\TEn}$ as in the proof of @prop:gamma-co-in-heegner-group.
Choose $\varphi\in\Orth(T_\Co)$ whose class is the one matching $c$ under that identification.

*Extension.*
$\varphi$ fixes $\zeta/2$, so $\varphi\oplus\id_{\ZZ\delta}$ preserves the gluing subgroup $\generators{(\delta/2,\,\zeta/2)}$ of @lem:coble-heegner-vector and by @cor:liftable-automorphisms extends over the index-two overlattice $\ten$ to an isometry $g$ with $g(\delta) = \delta$ and $\restrictionof{g}{T_\Co} = \varphi$.

*Membership in $\gent$.*
By that extension the class of $g$ in $\Orth(q_{\TEn})$ is the class of $\varphi$ on $A^0$, that is $c = \gamma\rho_{S_\En}(s_v)\gamma^{-1}$; so $\bar g_T\circ\gamma = \gamma\circ\bar g_S$ with $g_S = s_v$, and $s_v(h) = h$.
By @prop:gamma-en-two-gluing this is exactly the condition for $g\in\gent$, and $g(\delta) = \delta$, so $g\in\Stab_{\gent}(\ZZ\delta)$ with nontrivial $\rho_{T_\Co}(\restrictionof{g}{T_\Co})$.

*The component condition.*
If $\varphi\notin\Orth^+(T_\Co)$, use the proof of @prop:gamma-co-two-definitions(3): $s_\zeta\in\ker\rho_{T_\Co}$ has $\spinornorm_\bR(s_\zeta) = [-1]$, so $(\id_{S_\En}, s_\zeta)$ glues and extends to an isometry $h'$ of $\ten$ with $h'(\delta) = \delta$, $\restrictionof{h'}{T_\Co} = s_\zeta$ and trivial class; hence $h'\in\gent$ with partner $\id_{S_\En}$, and $gh'\in\Stab_{\gent}(\ZZ\delta)$ has restriction $\varphi s_\zeta\in\Orth^+(T_\Co)$ with the same nontrivial class.

So $\Gamma^{\mathrm{Hdg}}_\Co$ contains an element of $\Orth^+(T_\Co)$ acting nontrivially on $A_{T_\Co}$, which by @prop:gamma-co-two-definitions(1) makes the inclusion strict.

*The other inclusion, hence equality.*
Nothing above used anything about $s_v$ except that it lies in $\Stab_{\Orth(S_\En)}(h)$, so the construction applies to every element of that stabilizer and gives $\gamma\,G_\Co\,\gamma^{-1}\subseteq\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr)$.
Conversely $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr)\subseteq\gamma\,G_\Co\,\gamma^{-1}$: that is the containment in the proof of @prop:gamma-co-in-heegner-group(2), where the image of $\gent$ in $\Orth(q_{\TEn})$ is identified with the $\gamma$-transport of the image of $\Stab_{\Orth(S_\En)}(h)$ (@prop:gamma-en-two-gluing) and $\Gamma^{\mathrm{Hdg}}_\Co$ is the image of $\Stab_{\gent}(\ZZ\delta)\iscontainedin\gent$ under restriction.
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
\Gamma^\theta_\Co = \Gamma_\Co \iff \rho_{S_\Co}\bigl(\Stab_{\Orth(S_\Co)}(\tilde h_\Co)\bigr) = 1,
\qquad
[\Gamma^\theta_\Co : \Gamma_\Co] = \abs{\rho_{S_\Co}\bigl(\Stab_{\Orth(S_\Co)}(\tilde h_\Co)\bigr)}.
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
If not, let $\hat h\in\Orth(\lkt)$ be the extension of $(\id_{S_\Co}, s_\zeta)$ given by @prop:gamma-co-two-definitions(3); it also commutes with $\theta_\Co$ and fixes $\tilde h_\Co$, and $g\hat h$ has restriction $\varphi_0 s_\zeta\in\Orth^+(T_\Co)$ with the same discriminant class, because $\rho_{T_\Co}(s_\zeta) = \id$.
So $c\in\rho_{T_\Co}(\Gamma^\theta_\Co)$ either way, and the two images are equal.
The two corollaries are @prop:gamma-co-two-definitions(1) and the first isomorphism theorem.
:::

::: {.lemma #lem:coble-stabilizer-discriminant-nontrivial title="The $\tilde h_\Co$-stabilizer of $S_\Co$ has nontrivial discriminant image"}

Let $C = \Pic(S)\cong\latI_{1,10}$, and let $h_\Co = F_1+F_2\in C$, with $F_i^2 = 0$ and $F_1\cdot F_2 = 1$, be the degree-$2$ numerical polarization of @def:coble-polarization-classes. Write
$$
C \;\iso\; \generators{K}\oplus U\oplus E_8,
\qquad K^2 = -1,
$$
with $K = K_S$, $U = \generators{F_1,F_2}$ the hyperbolic plane and $E_8$ the negative-definite lattice of @thm:E8-characterization.
This decomposition holds: $\generators{K_S}$ splits $C$ with complement $K_S^\perp$, even and unimodular of signature $(1,9)$ (@prop:canonical-perp-is-e10); $U\iscontainedin K_S^\perp$ because $F_1,F_2\in K_S^\perp$, and $U$ is unimodular, so it splits $K_S^\perp$ (@prop:unimodular-splits); the complement of $U$ in $K_S^\perp$ is even, unimodular and negative definite of rank $8$, hence isometric to $E_8$ (@thm:E8-characterization).
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
$S_\Co = C(2)$ with $C$ unimodular, so $b_{S_\Co} = 2\,b_C$ and $b_{S_\Co}(v,S_\Co) = 2\ZZ$: every primitive vector of a twist $C(2)$ has divisibility $2$.
Hence $s_v(x) = x + \tfrac12 b(x,v)v = x + b_C(x,v)v$ is an isometry of $S_\Co$.

*Nontrivial discriminant class.*
$C$ is unimodular and $v$ primitive, so the functional $b_C(\cdot,v)$ is unimodular and some $x\in S_\Co$ has $b_C(x,v) = 1$; for that $x$,
$$
s_v(x) - x = v \notin 2S_\Co
,$$
since $v$ is primitive.
Under $A_{S_\Co} = S_\Co/2S_\Co$ — the identification of @prop:twisted-unimodular-discriminant — reduction modulo $2$ is the discriminant action, so $\rho_{S_\Co}(s_v)\neq\id$.
:::

::: {.corollary #cor:theta-co-strict title="The $\theta$-description is strictly larger"}

$\Gamma_\Co\subsetneq\Gamma^\theta_\Co$, with $[\Gamma^\theta_\Co:\Gamma_\Co] = \abs{\rho_{S_\Co}(\Stab_{\Orth(S_\Co)}(\tilde h_\Co))}$, which @prop:theta-co-index evaluates as $\abs{W(E_8)} = 696\,729\,600$.
:::

::: {.proof}

Immediate from @prop:theta-co-gluing and @lem:coble-stabilizer-discriminant-nontrivial: the image there is nontrivial, and it is a subgroup of $\Orth(A_{T_\Co},q_{T_\Co})$ of @prop:coble-discriminant-group.
:::

::: {.proposition #prop:theta-co-index title="The index of the $\theta$-description"}

$[\Gamma^\theta_\Co:\Gamma_\Co] = \abs{W(E_8)} = 696\,729\,600$, the same number as the Heegner index of @prop:gamma-co-heegner-strict.
:::

::: {.proof}

By @prop:theta-co-gluing the index is $\abs{\rho_{S_\Co}(\Stab_{\Orth(S_\Co)}(\tilde h_\Co))}$. Write $C = \generators{K}\oplus U\oplus E_8$ with $K^2 = -1$ and $h = h_\Co = F_1+F_2$, as in @lem:coble-stabilizer-discriminant-nontrivial. Through $f^*\colon C(2)\iso S_\Co$ one has $\Orth(S_\Co) = \Orth(C)$, and the stabilizer of $\tilde h_\Co = f^*h$ corresponds to the stabilizer of $h$; below, $v = F_1-F_2\in C$.

*The shape of $h^{\perp C}$.*
$h^{\perp C} = \generators{K}\oplus\generators{v}\oplus E_8$ with $K^2 = -1$, $v = F_1-F_2$ of square $-2$ and the $E_8$ form; it is negative definite and has determinant
$$
\det(h^{\perp C}) = \det(C)\cdot\frac{[C:\ZZ h\oplus h^{\perp C}]^2}{\det(\ZZ h)} = 1\cdot\frac{4}{2} = 2,
$$
since $\det(\ZZ h) = 2$ and the index is $2$.
Its root system — the vectors of square $-2$ — is exactly $\theset{\pm v}$ together with the $240$ roots of $E_8$: a vector $x = aK + bv + e$ has
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

::: {.definition #def:congruence-group title="The congruence group and block-compatibility"}

Let
$$
P \definedas \Orth(q_{U(2)})\times\Orth(q_{E_8(2)}) \leq \Orth(A_{T_\Co}, q_{T_\Co}),
$$
made a subgroup of $\Orth(A_{T_\Co},q_{T_\Co})$ by the identity on $\ZZ\tfrac12\zeta$, which every isometry of $q_{T_\Co}$ fixes (@prop:coble-discriminant-group).
The *congruence group* is $\Gamma^{\mathrm{cong}}_{\Co,2}\definedas\rho_{T_\Co}^{-1}(P)\leq\Orth(T_\Co)$.
The gluing $\gamma$ of @prop:gamma-en-two-gluing, respectively $\gamma_\Co$ of @prop:theta-co-exists, is *block-compatible* if it maps the $U(2)$ block $A_{U(2)}$ of its source onto the $U(2)$ block $A_{U(2)}$ of $A_{T_\Co}$.
:::

::: {.lemma #lem:coble-discriminant-blocks title="The $U(2)$ block of the Coble discriminant forms"}

Let $A^0 = A_{U(2)}\perp A_{E_8(2)}$, of order $1024$, with the discriminant quadratic form $q$ of $U(2)\oplus E_8(2)$ or of its negative.
Let $A$ be either $A^0$ or a nondegenerate finite quadratic form $\ZZ k\perp A^0$ with $k$ of order $2$; these are the shapes of $A_{S_\En}$, and of $A_{S_\Co}$ with $k = [K/2]$ and $A_{T_\Co}$ with $k = [\zeta/2]$.
Then:

1. the only $\Orth(q_{E_8(2)})$-invariant subgroups of $A_{E_8(2)}$ are $0$ and $A_{E_8(2)}$, and $A_{U(2)}$ is the only subgroup of $A^0$ of order $4$ invariant under $\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$;
2. the orbits of $\Orth(q_{A^0})$ on $A^0$ are $\set{0}$, the $527$ nonzero classes with $q = 0$, and the $496$ classes with $q = 1$;
3. if $A = \ZZ k\perp A^0$, every isometry of $q_A$ fixes $k$, restriction to $A^0$ is an isomorphism $\Orth(q_A)\iso\Orth(q_{A^0})$, and the orbits of $\Orth(q_A)$ on $A$ are the orbits of (2) and their translates by $k$, of sizes $1, 1, 527, 527, 496, 496$;
4. $\Stab_{\Orth(q_A)}\bigl(A_{U(2)}\bigr) = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$, and some $g\in\Orth(q_A)$ has $g(A_{U(2)})\neq A_{U(2)}$; so if an anti-isometry $\gamma$ with source $A$ is block-compatible, then $\gamma\circ g$ is not.
:::

::: {.proof}

Write $H = A_{U(2)}$ and $E = A_{E_8(2)} = E_8/2E_8$.
On $A^0$ the form $q$ takes values in $\ZZ/2\ZZ$, so $(A^0,q)$ is a quadratic space over $\mathbb{F}_2$; its bilinear form is nondegenerate because $A^0$ is an orthogonal summand of a nondegenerate discriminant form, so Witt's extension theorem applies to it and to $E$.
On $H$ the three nonzero classes have the values $0$, $0$, $1$ (the proof of @prop:gamma-cong-eq-heegner(1)); on $E$ the $120$ classes of value $1$ are the images of the $240$ roots of $E_8$, and the other $135$ nonzero classes have value $0$.

(1) Let $W\leq E$ be a nonzero $\Orth(q_E)$-invariant subgroup and $x\in W$ nonzero. By Witt's extension theorem $\Orth(q_E)$ is transitive on the nonzero classes of each value of $q$, so $W$ contains every nonzero class of value $q(x)$. If $q(x) = 1$, these are the images of the roots, which span $E$. If $q(x) = 0$, then $W$ has at least $136 > 128 = \tfrac12\abs{E}$ elements. In both cases $W = E$.
Let $W\leq A^0$ be a subgroup of order $4$ invariant under $\Orth(q_H)\times\Orth(q_E)$. Its projection to $E$ along $H$ is $\Orth(q_E)$-invariant of order at most $4 < 256$, hence $0$. So $W\leq H$, and $W = H$.

(2) For $h\in H$ and $e\in E$ one has $q(h+e) = q(h)+q(e)$. So $3\cdot136+1\cdot120 = 528$ classes of $A^0$ have value $0$, the zero class included, and $3\cdot120+1\cdot136 = 496$ have value $1$. By Witt's extension theorem the nonzero classes of one value form one orbit.

(3) Since $k\perp A^0$ and $b_A$ is nondegenerate, $b(k,k) = \tfrac12$. For $x = \epsilon k+a$ with $a\in A^0$ one has $b(a,a)\equiv q(a)\equiv0\pmod 1$, so $b(x,x) = \tfrac\epsilon2 = b(x,k)$. If $c\in A$ also satisfies $b(x,x) = b(x,c)$ for every $x$, then $c-k$ is orthogonal to $A$, so $c = k$. An isometry preserves $b$, so it fixes $k$ and preserves $k^\perp = A^0$; conversely every isometry of $q_{A^0}$ extends by $k\mapsto k$. The orbits follow from (2), because $q(k+a) = q(k)+q(a)$.

(4) An isometry that preserves $H$ fixes $k$ by (3) when $A = \ZZ k\perp A^0$, so it preserves $A^0$ and hence $H^\perp\intersect A^0 = E$; this gives the stabilizer. The class of value $1$ in $H$ and the image $r\in E$ of a root lie in one orbit by (2) and (3), so some $g$ maps the first to $r\notin H$, and $g(H)\neq H$. If $\gamma(H) = H$, then $\gamma(g(H))\neq\gamma(H) = H$.
:::

::: {.lemma #lem:overgroups-of-gamma-co title="Overgroups of the stable group in $\Orth^+(T_\Co)$"}

Let $G$ be a group with $\Gamma_\Co\leq G\leq\Orth^+(T_\Co)$. Then
$$
G = \rho_{T_\Co}^{-1}\bigl(\rho_{T_\Co}(G)\bigr)\intersect\Orth^+(T_\Co)
\qquad\text{and}\qquad
[G:\Gamma_\Co] = \abs{\rho_{T_\Co}(G)}.
$$
:::

::: {.proof}

$\Gamma_\Co = \Orth^+(T_\Co)\intersect\ker\rho_{T_\Co}$ (@sec-gamma-co-comparison), so the kernel of $\rho_{T_\Co}$ on $G$ is $\Gamma_\Co$, which gives the index.
The left side is contained in the right side. Let $x$ be in the right side, and choose $y\in G$ with $\rho_{T_\Co}(y) = \rho_{T_\Co}(x)$. Then $y^{-1}x\in\Orth^+(T_\Co)\intersect\ker\rho_{T_\Co} = \Gamma_\Co\leq G$, so $x\in G$.
:::

::: {.proposition #prop:gamma-cong-eq-heegner title="The Heegner description and the congruence description"}

Let $\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma^\theta_\Co$ be the groups of @prop:gamma-co-in-heegner-group and @prop:gamma-co-in-theta-centralizer, and put $P_{S_\En}\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})\leq\Orth(A_{S_\En},q_{S_\En})$ and $P_{S_\Co}\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})\leq\Orth(A_{S_\Co},q_{S_\Co})$.
Then

1. $\abs{\Orth(q_{U(2)})} = 2$ and $\abs{\Orth(q_{E_8(2)})} = \tfrac12\abs{W(E_8)} = 348\,364\,800$, so
   $$
   \abs{P} = 2\cdot 348\,364\,800 = 696\,729\,600 = \abs{W(E_8)}
   ;$$
2. $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr) = \gamma P_{S_\En}\gamma^{-1} = \Stab_{\Orth(q_{T_\Co})}\bigl(\gamma(A_{U(2)})\bigr)$, of order $\abs{W(E_8)}$, and it equals $P$ if and only if $\gamma$ is block-compatible;
3. $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)\bigr) = P$, so $[\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co):\Gamma_\Co] = \abs{W(E_8)}$ and $[\Gamma^{\mathrm{cong}}_{\Co,2}:\Gamma_\Co] = 2\abs{W(E_8)} = 1\,393\,459\,200$; and $\Gamma^{\mathrm{Hdg}}_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ if and only if $\gamma$ is block-compatible;
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
By @lem:coble-discriminant-blocks(4), $P_{S_\En}$ is the stabilizer of $A_{U(2)}$ in $\Orth(q_{S_\En})$ and $P$ is the stabilizer of $A_{U(2)}$ in $\Orth(q_{T_\Co})$, so $\gamma P_{S_\En}\gamma^{-1}$ is the stabilizer of $\gamma(A_{U(2)})$.
If $\gamma$ is block-compatible, this is $P$. Conversely, if $\gamma P_{S_\En}\gamma^{-1} = P$, then $\gamma(A_{U(2)})$ is a $P$-invariant subgroup of $A^0$ of order $4$, so it is $A_{U(2)}$ by @lem:coble-discriminant-blocks(1).

(3) $T_\Co$ is even, indefinite and $2$-elementary, so $\rho_{T_\Co}$ is onto (@thm:two-elementary-surjectivity), and $\rho_{T_\Co}(\Gamma^{\mathrm{cong}}_{\Co,2}) = P$.
The reflection $s_\zeta$ has $\zeta^2 = 2$, so $\rho_{T_\Co}(s_\zeta) = \id$ — $s_\zeta(x^*) - x^* = -\beta(x^*,\zeta)\zeta$ with $\beta(x^*,\zeta)\in\ZZ$ — while $\spinornorm_\bR(s_\zeta) = [-1]$ (the component step of @prop:gamma-co-heegner-strict).
$\Orth^+(T_\Co)$ is the kernel of $\spinornorm_\bR$, so for $x\in\Gamma^{\mathrm{cong}}_{\Co,2}$ one of $x$ and $xs_\zeta$ lies in $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$, with the same image under $\rho_{T_\Co}$.
Hence $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)\bigr) = P$, and the first index is $\abs{P}$ by @lem:overgroups-of-gamma-co. The same element gives $[\ker\rho_{T_\Co}:\Gamma_\Co] = 2$, so
$$
\bigl[\Gamma^{\mathrm{cong}}_{\Co,2}:\Gamma_\Co\bigr] = 2\abs{P} = 1\,393\,459\,200
.$$
$\Gamma^{\mathrm{Hdg}}_\Co$ lies in $\Orth^+(T_\Co)$ and contains $\Gamma_\Co$ (@prop:gamma-co-in-heegner-group). By @lem:overgroups-of-gamma-co, $\Gamma^{\mathrm{Hdg}}_\Co = \rho_{T_\Co}^{-1}\bigl(\rho_{T_\Co}(\Gamma^{\mathrm{Hdg}}_\Co)\bigr)\intersect\Orth^+(T_\Co)$, while $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co) = \rho_{T_\Co}^{-1}(P)\intersect\Orth^+(T_\Co)$ has image $P$. So the two groups are equal if and only if $\rho_{T_\Co}(\Gamma^{\mathrm{Hdg}}_\Co) = P$, that is, by (2), if and only if $\gamma$ is block-compatible.

(4) The first equality is @prop:theta-co-gluing. That $\rho_{S_\Co}(\Stab_{\Orth(S_\Co)}(\tilde h_\Co)) = P_{S_\Co}$ is the computation of @prop:theta-co-index: the stabilizer is $\theset{\pm1}_K\times\langle s_v\rangle\times\Orth(E_8)$, its factors act in $K$, in $U$ and in $E_8$ respectively, its image preserves the three blocks of $A_{S_\Co} = C/2C$ and has order $\abs{W(E_8)} = \abs{P_{S_\Co}}$ by (1), so it is $P_{S_\Co}$.
The anti-isometry $\gamma_\Co$ maps $[K/2]$ to $[\zeta/2]$, because these are the classes characterized in @lem:coble-discriminant-blocks(3), so it maps the summand $A^0$ of $A_{S_\Co}$ onto that of $A_{T_\Co}$.
By @lem:coble-discriminant-blocks(4), $\gamma_\Co P_{S_\Co}\gamma_\Co^{-1}$ is the stabilizer of $\gamma_\Co(A_{U(2)})$, and it is $P$ if and only if $\gamma_\Co$ is block-compatible, by the argument of (2).
$\Gamma^\theta_\Co$ lies in $\Orth^+(T_\Co)$ and contains $\Gamma_\Co$ (@prop:gamma-co-in-theta-centralizer), so by @lem:overgroups-of-gamma-co and (3), $\Gamma^\theta_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ if and only if $\rho_{T_\Co}(\Gamma^\theta_\Co) = P$.
:::

::: {.question #qst:kernel-and-root-arrangement title="The root arrangement"}

Does every $g\in Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}$ preserve the $(-2)$-root arrangement of the tuple?
:::

## Integral cusp lifting {#sec-cusp-lifting}

In this section $T_\Co = B(2)$ with $B\cong\latI_{2,9}$ (@prop:tco-as-twist), so that $\Orth(T_\Co) = \Orth(B)$, $T_\Co^\# = \tfrac12T_\Co$ and $A_{T_\Co} = B/2B$; write $\rho = \rho_{T_\Co}$ and $q = q_{T_\Co}$.

::: {.lemma #lem:isotropic-classes-lift title="The classes of primitive isotropic vectors"}

1. For a primitive isotropic $v\in T_\Co$ the class $[v/2]\in A_{T_\Co}$ is nonzero and isotropic, and $\rho(g)[v/2] = [gv/2]$ for $g\in\Orth(T_\Co)$.
2. The classes $[v/2]$ of the primitive isotropic $v\in T_\Co$ are exactly the $527$ nonzero isotropic classes of $A_{T_\Co}$, and these form one $\Orth(q)$-orbit.
:::

::: {.proof}

(1) $q([v/2]) = v^2/4 = 0$, and $[v/2]\neq0$ because a primitive vector of $B$ does not lie in $2B$. The equivariance is the definition of $\rho$.

(2) An isotropic class lies in the subgroup $A^0$ of @prop:coble-discriminant-group, and $A^0\cong A_{E_{10}(2)} = A_{U(2)}\perp A_{E_8(2)}$, with $\Orth(q)\iso\Orth(q_{A^0})$ by restriction. So by @lem:coble-discriminant-blocks(2) the nonzero isotropic classes number $527$ and form one $\Orth(q)$-orbit.
By @lem:I29-plus-line-transitivity, $\Orth(B)$ is transitive on the primitive isotropic vectors, so by (1) their classes form one $\Orth(q)$-orbit of nonzero isotropic classes, namely all of them.
:::

::: {.lemma #lem:cusp-vector-stabilizer-image title="The stabilizer of a primitive isotropic vector"}

Let $v\in T_\Co$ be primitive isotropic and $c = [v/2]$. Then

1. $\rho\bigl(\Stab_{\Orth(B)}(v)\bigr) = \Stab_{\Orth(q)}(c)$;
2. $\Stab_{\Orth(B)}(v)\intersect\ker\rho$ contains an element outside $\Orth^+(B)$.
:::

::: {.proof}

By @lem:odd-unimodular-isotropic-splitting(1), $B = P\perp K$ with $v\in P\cong\latI_{1,1}$ and $K\cong\latI_{1,8}$, and $v^{\perp} = \ZZ v\perp K$, so $v^\perp/v\cong K$.

(1) $\Orth(K)\leq\Stab_{\Orth(B)}(v)$ as the isometries that fix $P$ pointwise, and the stabilizer also contains the Eichler transvections $E(v,k)$ for $k\in v^{\perp}$ with $k^2$ even ([@Eic74]; [@GHS08], §3).
$K(2)$ is even, indefinite and $2$-elementary of rank $9$, so $\Orth(K)\to\Orth(q_{K(2)})$ is onto (@thm:two-elementary-surjectivity), and $q_{K(2)}\iso q|_{c^{\perp}/c}$. So $\rho(\Stab_{\Orth(B)}(v))$ maps onto $\Stab_{\Orth(q)}(c)/N$, where $N$ is the kernel of $\Stab_{\Orth(q)}(c)\to\Orth(c^{\perp}/c)$.
By @lem:isotropic-classes-lift(2) and @prop:coble-discriminant-group, $\abs{\Stab_{\Orth(q)}(c)} = \abs{\Orth(q)}/527$, so
$$
\abs{N} = \frac{\abs{\Stab_{\Orth(q)}(c)}}{\abs{\Orth(c^{\perp}/c)}} = \frac{\abs{\Orth(q)}/527}{\abs{\operatorname{GO}^+_8(2)}} = \frac{89\,181\,388\,800}{348\,364\,800} = 2^8 .
$$
The images $\rho(E(v,k))$ lie in $N$, and $\rho(E(v,k)) = \id$ if and only if $k\in\ZZ v+2B$, so they form a group isomorphic to $K_{\mathrm{ev}}/2K$, of order $2^8 = \abs{N}$. Hence $\rho(\Stab_{\Orth(B)}(v)) = \Stab_{\Orth(q)}(c)$.

(2) Let $g = \id_P\oplus(-\id_K)$. It fixes $v$, and it is the identity modulo $2B$, so $g\in\ker\rho$. By @lem:split-isometry-spinor-norm and @lem:minus-identity-spinor-norm, $\spinornorm_\bR(g) = \spinornorm_\bR(-\id_K) = -1$, because the positive index of $K$ is $1$. So $g\notin\Orth^+(B)$.
:::

::: {.proposition #prop:coble-planecusp-finite title="The isotropic subgroups of order $4$ of $A_{T_\Co}$"}
Let $B$, $T_\Co = B(2)$, $\rho$, $q$ and $A = A_{T_\Co}$ be as in this section, and let $P\subset B$ be a primitive isotropic plane.

1. Every primitive vector $p\in P$ has $\operatorname{div}_{T_\Co}(p) = 2$ and a nonzero class $[p/2]\in A$. The subgroup $J(P)\definedas\im(P/2)\leq A$ is isotropic of order $4$, its three nonzero elements are the classes of the primitive vectors of $P$, and $\rho(g)(J(P)) = J(g(P))$ for $g\in\Orth(B)$.
2. $\Orth(q)$ acts transitively on the isotropic subgroups of order $4$ of $A$, and each of them is $J(P')$ for a primitive isotropic plane $P'\subset B$.
3. There are $23715 = 527\cdot 270/6$ isotropic subgroups of order $4$ of $A$, and $23715 = 1575+270+9450+3780+8640$ is the sum of the five orbit sizes of @tbl-finite-plane-orbits.
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
4. (The index.) $\bqty{\Stab_{\Orth(q)}(J) : \rho(\Stab_{\Orth(B)}(P))} = 8 = \bqty{\Orth^+(6,2) : S_7} = \bqty{S_8 : S_7}$.
5. (The orbit fibres.) Let $\ker\rho\iscontainedin\Gamma\iscontainedin\Orth(B)$, and put $Q = \Orth(q)$, $H = \rho(\Gamma)$, $F = \Stab_Q(J)$ and $S = \rho\bigl(\Stab_{\Orth(B)}(P)\bigr)$. For $k\in Q$, the $\Gamma$-orbits of the primitive isotropic planes $P'\subset B$ with $J(P') = kJ$ are in bijection with the double cosets
$$ \bigl(k^{-1}Hk\intersect F\bigr)\bigl\backslash F \big/ S . $$
In particular:
   a. for $\Gamma = \ker\rho$ there are $\abs{F/S} = 8$ orbits over each $J'$;
   b. for $\Gamma = \Orth(B)$ there is one orbit;
   c. for $\Gamma_\Co = \Orth^+(B)\intersect\ker\rho$ there are $8$ orbits over each of the $23715$ subgroups of @prop:coble-planecusp-finite, so $8\times 23715 = 189\,720$ orbits of primitive isotropic planes in all.
:::

::: {.proof}

(1) The group $\Stab_{\Orth(B)}(P)$ acts on $P$ and on $P^{\perp B}/P\cong D$, and $U$ is the kernel of the resulting map $\Stab_{\Orth(B)}(P)\to GL(P)\times\Orth(D)$. In the Witt decomposition, $P$ and $D$ are orthogonal, $\generators{f_1,f_2}$ is orthogonal to $D$ and in hyperbolic duality with $P$, and $GL(P)$ acts on $\generators{f_1,f_2}\cong P^*$ by the contragredient action. So each $\gamma\oplus(\gamma^{-1})^{T}\oplus\delta$ is an isometry of $B$ that stabilizes $P$ and induces $(\gamma,\delta)$. These elements form a subgroup $L$ that maps isomorphically onto $GL_2(\ZZ)\times\Orth(D)$. So the map is onto, $L$ splits it, and $\Stab_{\Orth(B)}(P) = L\ltimes U$.

(2) $GL_2(\ZZ)\to GL_2(\F_2)\cong S_3$ is onto, and $GL(P)$ acts on $J = P/2P$ by its reduction. $\Orth(D)$ is the group of signed permutations of the $d_i$, and the signs act trivially modulo $2$. So $\rho(\Orth(D))\cong S_7$, of order $5040$, inside $\Orth(\generators{-\tfrac12}^{7})$. For $w\in D^{\mathrm{ev}}$, @def:eichler-siegel gives $E_{e_i,w}(x) = x + (e_i,x)w - \bigl((w,x) + \tfrac{w^2}{2}(e_i,x)\bigr)e_i$ with $\tfrac{w^2}{2}\in\ZZ$; its reduction modulo $2B$ is the displayed map. The vector $e_2$ is isotropic and orthogonal to $e_1$, so $E_{e_1,e_2}(x) = x + (e_1,x)e_2 - (e_2,x)e_1$, whose reduction is the displayed transvection. The elements $E_{e_i,w}$ and $\sigma$ fix $P$ and $P^{\perp B}/P$ pointwise, so they lie in $U$.

(3) $U$ fixes $P$ and $P^{\perp B}/P$ pointwise, so $\rho(U)$ fixes $J$ and $J^{\perp}/J$ pointwise and lies in the unipotent radical of $\Stab_{\Orth(q)}(J)$. By (2), the image of $L$ is $S_3\times S_7$, of order $30240$. The unipotent radical has order $2^{13}$. In the Witt block order $J\oplus J^*\oplus V_6$ of the plus-type ten-space $\bar w_0^{\perp}$, which matches $P\oplus P^*\oplus D$, its elements are the block matrices with identity diagonal blocks. Their free parameters are the blocks of linear maps $J\to V_6$, of size $2\times 6$ over $\F_2$, which give $2^{12}$ elements, and the $J$-valued block. A $J$-valued block map
$$ \bar x\mapsto\bar x + a_1\beta_1 j_1 + a_2\beta_1 j_2 + a_3\beta_2 j_1 + a_4\beta_2 j_2, \qquad \beta_i = \beta(\bar x,j_i),\ a_i\in\F_2, $$
preserves $q$ if and only if $a_1\beta_1 + (a_2+a_3)\beta_1\beta_2 + a_4\beta_2 \equiv 0$ identically, because $q(\bar x+\delta) = q(\bar x)+\beta(\bar x,\delta)$ and $q(\delta) = 0$ for $\delta\in J$. This forces $a_1 = a_4 = 0$ and $a_2 = a_3$. So the block has the two elements: the identity and the transvection $\bar x\mapsto\bar x+\beta(\bar x,j_1)j_2+\beta(\bar x,j_2)j_1$. This gives $2^{12}\cdot 2 = 2^{13}$.
The elements of (2) attain each block. The classes $[w/2]$ of $w\in D^{\mathrm{ev}}$ are the even-weight classes, that is all of $V_6$, so the $E_{e_i,w}$ realize all linear maps $\generators{j_i}\to V_6$ for each $i$. The element $\sigma$ realizes the $J$-valued block. Hence $\abs{\rho(\Stab_{\Orth(B)}(P))} = 30240\cdot 2^{13} = 247\,726\,080$.

(4) The space $J^{\perp}/J$ is seven-dimensional over $\F_2$ and spanned by the $\bar d_i$. It has the descended quadratic form, because $J$ is totally isotropic and $b(J,J^{\perp}) = 0$, so $q(x+j) = q(x)$. Since $(w_0,w_0)_B = -7$, $q(\bar w_0) = -\tfrac72 \equiv \tfrac12$ and $b(\bar w_0,\bar w_0) = -\tfrac72 \equiv \tfrac12 \neq 0$. So $\bar w_0$ is not in the radical of $b$, and
$$ V_6 \definedas \bar w_0^{\perp} \cap J^{\perp}/J = \theset{\textstyle\sum c_i \bar d_i : \sum c_i \equiv 0 \pmod 2} $$
is six-dimensional, with $J^{\perp}/J = \generators{\bar w_0} \perp V_6$. On $V_6$ the form is $q(\sum c_i \bar d_i) = -\tfrac{\mathrm{wt}}{2} \bmod 2$, where $\mathrm{wt} = \sum c_i$ is even, so $q$ is $\F_2$-valued on $V_6$. It is nondegenerate of plus type. The classes with $q = 0$ are those of weight $\equiv 0 \pmod 4$, and they number $\binom70 + \binom74 = 36 = 2^5 + 2^2$, the plus-type count $2^{2m-1}+2^{m-1}$ at $m = 3$.
The Levi factor of $\Stab_{\Orth(q)}(J)$ is $S_3\times\Orth^+(6,2)$, and $\Orth^+(6,2)\cong S_8$ acts on $V_6$ and fixes the characteristic class $\bar w_0$. The Levi factor $L$ acts on $P^{\perp B}/P\cong D$ through $\Orth(D)$, the signed permutation group of order $2^7\cdot 7!$, whose image modulo $2$ is the $S_7$ of (2). By (3), $\rho(\Stab_{\Orth(B)}(P))$ contains the unipotent radical of $\Stab_{\Orth(q)}(J)$, and its Levi image is $S_3\times S_7$. So the index is $\bqty{S_3\times S_8 : S_3\times S_7} = \bqty{S_8 : S_7} = 8$, and indeed $1\,981\,808\,640/247\,726\,080 = 8$ by (3) and @prop:coble-planecusp-finite(4).

(5) By @thm:plane-transitivity-tco, every primitive isotropic plane of $B$ is $g(P)$ for some $g\in\Orth(B)$. By @prop:coble-planecusp-finite(1), $J(g(P)) = \rho(g)J$. So the planes $P'$ with $J(P') = J$ form the orbit of $P$ under $\rho^{-1}(F)$, and the $\Gamma$-orbits on it are the double cosets
$$ \bigl(\Gamma\intersect\rho^{-1}(F)\bigr)\bigl\backslash \rho^{-1}(F) \big/ \Stab_{\rho^{-1}(F)}(P) . $$
Since $\ker\rho\iscontainedin\Gamma$, they reduce modulo $\ker\rho$ to $(H\intersect F)\backslash F/S$. For $k\in Q$ with a lift $\tilde k\in\Orth(B)$, the planes $P'$ with $J(P') = kJ$ form the orbit of $\tilde k(P)$ under $\rho^{-1}(kFk^{-1})$. Conjugation by $\tilde k$ identifies their $\Gamma$-orbits with the double cosets $(k^{-1}Hk\intersect F)\backslash F/S$.
For $H = 1$ this is $F/S$, of order $8$ by (4). For $H = Q$ there is one double coset over each $J'$, and $Q$ is transitive on the $J'$ (@prop:coble-planecusp-finite(2)), so there is one orbit.
For (c), $\Gamma_\Co\iscontainedin\ker\rho$ has index at most $2$, and a $\ker\rho$-orbit of planes is one $\Gamma_\Co$-orbit if the stabilizer in $\ker\rho$ of one of its planes contains an element outside $\Orth^+(B)$. Let $\tau = -\id_{U_1}\oplus\id_{U_2\perp D}$. Then $\tau(e_1) = -e_1$ and $\tau(e_2) = e_2$, so $\tau$ stabilizes $P$. It is the identity modulo $2B$, so $\tau\in\ker\rho$. Its normalized real spinor norm (@sec-lattice-spinor-norm) is $\spinornorm_\bR(-\id_{U_1}) = [(-1)^1] = -1$ by @lem:minus-identity-spinor-norm, since $U_1$ has positive index one. For $k\in\Orth(B)$, $k\tau k^{-1}$ lies in $\ker\rho$, stabilizes $k(P)$ and has spinor norm $-1$. So no $\ker\rho$-orbit splits, and (a) together with @prop:coble-planecusp-finite(3) gives $8\times 23715 = 189\,720$ orbits.
:::

::: {.proposition #prop:stabilizers-conjugate title="The stabilizers of the polarized $0$-cusps are conjugate"}

Let $T_\Co = B(2)$ and $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$, and let $v, v'\in T_\Co$ be primitive isotropic vectors with $v' = gv$ for some $g\in\Orth(T_\Co)$, which exists by @thm:unpolarized-cusps.
Then

1. $\Gamma_\Co$ is normal in $\Orth(T_\Co)$, and $\Stab_{\Gamma_\Co}(v') = g\,\Stab_{\Gamma_\Co}(v)\,g^{-1}$;

2. the subgroups of $\Orth(v^{\perp T_\Co}/\generators{v})$ and of $\Orth((v')^{\perp T_\Co}/\generators{v'})$ induced by those stabilizers are mapped onto one another by the isometry $\bar g$ that $g$ induces on the quotients;

3. consequently the subgroups $G\leq\Orth(\latI_{1,8}(2))$ of @qst:sterk-reflection-subgroup at the polarized $0$-cusps are conjugate, and they have equal index.
:::

::: {.proof}

(1) $\Gamma_\Co = \ker\rho_{T_\Co}\cap\ker\varepsilon$ with $\varepsilon$ the orientation character of @prop:spinor-plus-cone-components, so it is the intersection of two kernels and therefore normal.
For $h\in\Stab_{\Gamma_\Co}(v)$ and $g$ as in the statement, $ghg^{-1}(v') = ghv = gv = v'$, and $ghg^{-1}\in\Gamma_\Co$ by normality; so $g\Stab_{\Gamma_\Co}(v)g^{-1}\subseteq\Stab_{\Gamma_\Co}(v')$, and the reverse inclusion follows by applying the same argument to $g^{-1}$, or by counting cosets of the same index.

(2) An isometry fixing $v$ preserves $v^{\perp}$ and $\generators{v}$, hence descends to the quotient, and the resulting map $g\mapsto\bar g$ is a homomorphism of stabilizers; conjugating on $T_\Co$ becomes conjugating by $\bar g$ on the quotient.
So the image of $\Stab_{\Gamma_\Co}(v')$ is $\bar g\,\rho_v(\Stab_{\Gamma_\Co}(v))\,\bar g^{-1}$, and $\bar g$ is an isometry of the two cusp lattices.

(3) By @prop:zero-cusp-lattices the quotient is $\latI_{1,8}(2)$ for every such $v$, so (2) exhibits the images as conjugate inside one isometry group, and conjugate subgroups have equal index.
:::

::: {.theorem #thm:plane-half-index title="The subgroup $G^+$ of the cusp lattice, and $c = 1$"}

Let $v$ be a primitive isotropic vector of $T_\Co$, $S = \Stab_{\Orth(T_\Co)}(v)$, $K = v^{\perp T_\Co}/\generators{v}\cong\I_{1,8}(2)$, $\pi: S\to\Orth(K)$, $W\leq S$ generated by the nine wall reflections of the $K$-chamber, and
$$
G \definedas \pi(\ker\rho_{T_\Co}\cap S),\qquad G^+ \definedas \pi\pqty{\ker\rho_{T_\Co}\cap S\cap\Orth^+(T_\Co)} = G\cap\Orth^+(K),\qquad c \definedas \abs{\rho(W)\cap\rho(\ker\pi)} .
$$
Then

1. $\ker\pi = \set{E_B(e_1,w) : w\in\I_{1,8}^{\mathrm{ev}}}$, the transvections in the even sublattice, and $\rho(\ker\pi)\cong\I_{1,8}^{\mathrm{ev}}/2\I_{1,8}$ has order $256$;

2. $\abs{\rho(W)} = 348\,364\,800$, $\abs{\rho(S)} = \abs{\langle\rho(W),\rho(\ker\pi)\rangle} = 89\,181\,388\,800 = \abs{\Stab_{\Orth(q_{T_\Co})}([e_1/2])}$, hence $c = 1$;

3. $-\id_K$ lies in $G$ and not in $\Orth^+(K)$, so
$$
\bqty{\Orth^+(K) : G^+} = \bqty{\Orth(K) : G} = \frac{\abs{\rho(W)}}{c} = 348\,364\,800,
\qquad
\bqty{\Orth(K) : G^+} = 696\,729\,600 ;
$$

4. the element $\id_{U_1}\oplus(-\id_K)$ lies in $\ker\rho_{T_\Co}$ and outside $\Orth^+(T_\Co)$, so the $\widetilde\Orth(T_\Co)$-orbit of $e_1$ is a single $\widetilde\Orth^+(T_\Co)$-orbit, and since
$$
\frac{\abs{\Orth(q)}}{\abs{\rho(S)}} = \frac{46\,998\,591\,897\,600}{89\,181\,388\,800} = 527 = 527\,c ,
$$
$\Gamma_\Co$ has $527$ orbits of primitive isotropic vectors, one per nonzero isotropic class.
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
By [@Vin72, Table 5], $\Orth^+(\I_{1,8})$ is the reflection group of the chamber, whose diagram has no symmetry; so $\Orth(K) = \set{\pm1}\times W$ and $S = \langle W,\ \id_{U_1}\oplus(-\id_K),\ \ker\pi\rangle$.
The element $\id_{U_1}\oplus(-\id_K)$ is the identity modulo $2B$, so $\rho$ kills it, and $\rho(S) = \rho(W)\cdot\rho(\ker\pi)$, with $\rho(\ker\pi)$ normal because $\ker\pi$ is normal in $S$.
By @lem:cusp-vector-stabilizer-image(1), @lem:isotropic-classes-lift(2) and @prop:coble-discriminant-group, $\abs{\rho(S)} = \abs{\Stab_{\Orth(q)}([e_1/2])} = \abs{\Orth(q)}/527 = 89\,181\,388\,800$.
The group $\rho(W) = \rho(\Orth(K))$ acts trivially on $U_1/2U_1$, and on $K/2K$ it is the image of $\Orth(K)\to\Orth(q_{K(2)})$, which is onto by @thm:two-elementary-surjectivity; so $\abs{\rho(W)} = \abs{\Orth(q_{K(2)})} = \abs{\operatorname{GO}^+_8(2)} = 348\,364\,800$, as in the proof of @lem:cusp-vector-stabilizer-image(1).
Hence $c = \abs{\rho(W)}\cdot\abs{\rho(\ker\pi)}/\abs{\rho(S)} = 348\,364\,800\cdot256/89\,181\,388\,800 = 1$.

(3) The element $g = \id_{U_1}\oplus(-\id_K)$ fixes $e_1$, acts as $-1$ on $K$, is trivial on $A_{T_\Co}$ and so lies in $\ker\rho_{T_\Co}\cap S$; its image in $\Orth(K)$ is $-\id_K$, which is not in $\Orth^+(K)$ because $\I_{1,8}$ has positive index $1$ and $\spinornorm_\bR(-\id) = [(-1)^1] = -1$ (@lem:minus-identity-spinor-norm).
So $G = \set{\pm1}\cdot G^+$ as subgroups of $\Orth(K) = \set{\pm1}\times\Orth^+(K)$, and the two indices in (3) follow from (2).

(4) The element $g$ lies outside $\Orth^+(T_\Co)$, since it reverses the plane spanned by the positive directions of $U_1$ and of $K$, while it does lie in the discriminant kernel; hence the stabilizer in $\widetilde\Orth(T_\Co)$ of $e_1$ is not contained in $\widetilde\Orth^+(T_\Co)$ and the two groups have the same orbit on $e_1$.
The orbit count then follows from $\rho$ onto $\Orth(q)$ (@thm:two-elementary-surjectivity): the $\ker\rho$-orbits inside the orbit of $e_1$ are in bijection with $\Orth(q)/\rho(S)$, of order $527$.
:::

::: {.theorem #thm:plane-fibre title="The plane fibre, the plane classes and the $1$-cusp count of $\fco$"}

Let $P\subset B = U\perp U\perp \I_{0,7}$ be a primitive isotropic plane, $K_P = P^{\perp B}/P\iso\I_{0,7}$, $J = [P/2]\leq A_{T_\Co}$ the order-$4$ isotropic subgroup it spans, and $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$, whose discriminant image is trivial.
Then

1. $\abs{\Stab_{\Orth(q_{T_\Co})}(J)} = 1\,981\,808\,640$ and $\abs{\rho(\Stab_{\Orth(B)}(P))} = 247\,726\,080$, so the plane fibre has index
$$
\bigl[\Stab_{\Orth(q_{T_\Co})}(J) : \rho(\Stab_{\Orth(B)}(P))\bigr] = 8 ;
$$

2. the isotropic subgroups of order $4$ of $A_{T_\Co}$ form the $\Orth(q_{T_\Co})$-orbit of $J$, of size $23\,715$, which the five $G_\Co$-orbits of @tbl-finite-plane-orbits, of sizes $1575, 270, 9450, 3780, 8640$, partition;

3. hence $\fco$ has $23\,715\cdot 8 = 189\,720$ $1$-cusps for $\Gamma_\Co$, eight over each of these subgroups.
:::

::: {.proof}

$T_\Co = B(2)$ with $B$ unimodular, so $A_{T_\Co} = B/2B\cong\F_2^{11}$ with $q([x/2]) = B(x,x)/2\pmod{2\ZZ}$, and the discriminant action of $g\in\Orth(B)$ is $g\bmod 2$.

(1) By @prop:coble-planecusp-finite(3) and (4), $\abs{\Stab_{\Orth(q)}(J)} = \abs{\Orth(q)}/23\,715 = 1\,981\,808\,640$, and by @thm:coble-plane-stabilizer-image(3), $\abs{\rho(\Stab_{\Orth(B)}(P))} = 247\,726\,080$.
An integral isometry preserving $P$ maps the classes of $\tfrac12 e_1$ and $\tfrac12 e_2$ into $J$, so its reduction modulo $2$ stabilises $J$. Hence $\rho(\Stab_{\Orth(B)}(P))\subseteq\Stab_{\Orth(q)}(J)$, and the index is $1\,981\,808\,640/247\,726\,080 = 8$, which is $[S_8:S_7]$ by @thm:coble-plane-stabilizer-image(4).

(2) By @prop:coble-planecusp-finite(2), $\Orth(q)$ is transitive on the isotropic subgroups of order $4$, and by @prop:coble-planecusp-finite(3) they number $23\,715$. Their $G_\Co$-orbits are the five orbits of @ex:gco-finite-orbits, of the sizes listed in @tbl-finite-plane-orbits.

(3) By @thm:coble-plane-stabilizer-image(5), the $\Gamma_\Co$-orbits of primitive isotropic planes over each of the $23\,715$ subgroups $J$ are eight in number.
:::

::: {.corollary #cor:coble-zero-one-cusp-incidence title="Incidence of the $0$-cusps and the plane classes"}
Let $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$. Each isotropic subgroup $J$ of order $4$ of $A_{T_\Co}$ contains exactly three of the $527$ nonzero isotropic classes, each of which is one $0$-cusp of $\Gamma_\Co$, and each nonzero isotropic class lies in exactly $135$ of the $23\,715$ subgroups $J$.
:::

::: {.proof}
Write $J = [P/2]$ with $P = \langle e_1,e_2\rangle$ a primitive isotropic plane of $B$. By @prop:coble-planecusp-finite(1), the three nonzero elements of $J$ are the classes of $\tfrac12 e_1$, $\tfrac12 e_2$ and $\tfrac12(e_1+e_2)$, the classes of the primitive isotropic vectors $e_1$, $e_2$, $e_1+e_2$ of $T_\Co$, each of divisibility $2$.
By @thm:plane-half-index(4), the primitive isotropic vectors of $T_\Co$ with one nonzero isotropic class form one $\Gamma_\Co$-orbit, so each of the three classes is one $0$-cusp.
For a nonzero isotropic class $u$, the subgroups $J$ that contain $u$ are the subgroups $\langle u,v\rangle$ with $v$ isotropic in $u^\perp\setminus\langle u\rangle$. By @prop:coble-planecusp-finite(3) there are $270$ such $v$, and each subgroup contains two of them, so $u$ lies in $135$ subgroups. This agrees with the double count $23\,715\cdot3/527 = 135$.
:::


::: {.proposition #prop:coble-arithmetic-flag-incidence title="Line-in-plane flags over one isotropic subgroup of order $4$"}
Let $P=\langle e_1,e_2\rangle$ be the standard primitive isotropic plane of $B=U_1\perp U_2\perp D$, let $J=[P/2]$, and let $\Gamma_\Co=\ker\rho\intersect\Orth^+(B)$.

1. The image of $\Stab_{\Gamma_\Co}(P)$ in $GL(P)$ is
$$ \Gamma(P)\definedas\theset{A\in SL(P): A\equiv I_2\pmod2}. $$
2. Let $\mathcal P$ be one of the eight $\Gamma_\Co$-orbits of primitive isotropic planes $P'$ with $J(P') = J$ (@thm:coble-plane-stabilizer-image(5)), and let $c\in J$ be nonzero. Then the flags $(P',L)$ with $P'\in\mathcal P$, $L\subset P'$ a primitive line and $[L/2]=c$ form one $\Gamma_\Co$-orbit.

So the $\Gamma_\Co$-orbits of flags $(P',L)$ with $J(P') = J$ are the $3\times8 = 24$ orbits of item 2, one for each pair of an orbit $\mathcal P$ and a nonzero class $c\in J$.
:::

::: {.proof}
(1) By @thm:coble-plane-stabilizer-image(1), $\Stab_{\Orth(B)}(P) = L\ltimes U$, and the Levi factor acts by $A$ on $P$, by $(A^{-1})^{T}$ on $P^*$ and by an arbitrary $\delta\in\Orth(D)$ on $D$. An element of $\ker\rho$ acts trivially on $J = P/2P$, so its image $A$ satisfies $A\equiv I_2\pmod2$.
The normalized real spinor norm of such an element is $\det A$. The unipotent group $U$ has connected real points, so it is spinor-positive. $D$ is negative definite, so $\Orth(D)$ is generated by reflections in negative vectors, which are spinor-positive. For $\det A = 1$, the element $A\oplus(A^{-1})^{T}$ lies in the image of the connected group $SL_2(\bR)$, so it is spinor-positive. For $\det A = -1$, write $A = A'\diag(-1,1)$ with $\det A' = 1$; the element $\diag(-1,1)\oplus\diag(-1,1)$ is $-\id_{U_1}\oplus\id_{U_2}$, of spinor norm $-1$ by @lem:minus-identity-spinor-norm.
So the image of $\Stab_{\Gamma_\Co}(P)$ lies in $\Gamma(P)$. Conversely, for $A\in\Gamma(P)$ the element $A\oplus(A^{-1})^{T}\oplus\id_D$ is the identity modulo $2B$ and spinor-positive, so it lies in $\Stab_{\Gamma_\Co}(P)$.

(2) First, $\Gamma(P)$ is transitive on the primitive lines of $P$ in each nonzero class of $J$. A primitive line of $P$ is $L_{(a,b)}=\ZZ(ae_1+be_2)$ with $\gcd(a,b)=1$, and its class is $(\bar a,\bar b)\in J\sm\{0\}$. By Bezout's identity, each primitive vector $v=(a,b)^T$ is the first column of a matrix $M_v=[v,z_v]\in SL_2(\ZZ)$. Let $w$ be another primitive vector with $w\equiv v\pmod 2$, and let $M_w=[w,z_w]\in SL_2(\ZZ)$. Write $c$ for the common reduction of $v$ and $w$. Then
$$ \det(c,z_w-z_v)=\det M_w+\det M_v=1+1=0\quad\text{in }\F_2. $$
The functional $x\mapsto\det(c,x)$ on $\F_2^2$ is nonzero with kernel $\langle c\rangle$, so $z_w-z_v\equiv t c\pmod 2$ for some $t\in\F_2$. Lift $t$ to an integer and replace the second column of $M_w$ by $z_w-t w$. The new $M_w$ has determinant one and $M_w\equiv M_v\pmod2$. So $A=M_wM_v^{-1}$ satisfies $A\equiv I_2\pmod2$ and $Av=w$, that is $A\in\Gamma(P)$ and $A(L_v) = L_w$.

Now fix $P_0\in\mathcal P$. By @thm:plane-transitivity-tco, $P_0 = k(P)$ for some $k\in\Orth(B)$. The group $\Gamma_\Co$ is normal in $\Orth(B)$, so $\Stab_{\Gamma_\Co}(P_0) = k\Stab_{\Gamma_\Co}(P)k^{-1}$, and by (1) and the preceding paragraph it is transitive on the primitive lines $L\subset P_0$ with $[L/2]=c$. Let $(P_1,L_1)$ and $(P_2,L_2)$ be two flags with $P_i\in\mathcal P$ and $[L_i/2] = c$. An element of $\Gamma_\Co$ moves $P_2$ to $P_1$; it lies in $\ker\rho$, so it preserves the class $c$, and it moves $L_2$ to a line of class $c$ in $P_1$. An element of $\Stab_{\Gamma_\Co}(P_1)$ then moves that line to $L_1$.
:::

### The reflective set of the stable group {#sec-gamma-co-reflective-set}

::: {.notation title="Discriminants of twists by $2$"}
$T_\Co = B(2)$ and $S_\En = C(2)$ are twists by $2$ of unimodular lattices, so their duals are half of them,
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
By @def:2elementary-roots, the roots of the $2$-elementary lattice $T_\Co$ are the short roots, of square $-2$, and the long roots, of square $-4$ and divisibility $2$.
:::

::: {.proposition #prop:gamma-co-reflective-set title="The reflective set of the stable Coble group"}

Let $T_\Co = B(2)$ be the Coble lattice of @prop:tco-as-twist, even of signature $(2,9)$ and determinant $-2048$, so that every primitive vector of $T_\Co$ has divisibility $2$ (@lem:divisibilityAlwaysTwoTco), and let $\Gamma_\Co = \Orth^+(T_\Co)\intersect\ker\rho_{T_\Co}$, with $\Orth^+(T_\Co) = \Theta_\bR(T_\Co)$ of @def:lattice-spinor-kernels and $\spinornorm_\bR$ the real spinor norm of @def:spinor-norm.
Write $s_v$ for the reflection of @def:spinor-norm in a nonisotropic vector $v$.
Then, for a primitive $v$, $s_v$ is an isometry of $T_\Co$ exactly for $v^2\in\{2,-2,4,-4\}$, and among those:

1. if $v^2 = -2$ then $s_v\in\Gamma_\Co$; hence the short roots generate a subgroup
   $$
   W(T_\Co) \definedas \generators{\,s_v \;:\; v \in T_\Co,\ v^2 = -2\,}
   \iscontainedin \Gamma_\Co
   ,$$
   which is infinite;
2. if $v^2 = 2$ or $v^2 = 4$ then $s_v\notin\Orth^+(T_\Co)$, hence $s_v\notin\Gamma_\Co$; for $v^2 = 2$ one has in addition $s_v\in\ker\rho_{T_\Co}$, and for $v^2 = 4$ never;
3. if $v^2 = -4$ then $s_v\in\Orth^+(T_\Co)$ and $s_v\notin\ker\rho_{T_\Co}$.

Consequently the reflective set of $\Gamma_\Co$ — the primitive vectors of $T_\Co$ whose reflection lies in $\Gamma_\Co$ — is exactly the set of primitive short roots, which is every vector of square $-2$, and no long root lies in it.
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
So $s_v\in\Gamma_\Co$.
The group $W(T_\Co)$ is infinite, because distinct lines $\ZZ v$ give distinct reflections and there are infinitely many such lines: for odd $a\in\ZZ$,
$$
x_a \definedas a\zeta + e' - \tfrac{a^2+1}{2}f'
\qquad\text{has}\qquad
x_a^2 = 2a^2 + 4\cdot\Bigl(-\tfrac{a^2+1}{2}\Bigr) = -2
,$$
since $\zeta$ is orthogonal to the $U(2)$ summand and $\beta(e',f') = 2$ there.

(2) Both squares give $\spinornorm_\bR(s_v) = [-1]$, which is not the identity of $\bR^\times/(\bR^\times)^2$, so $s_v\notin\Theta_\bR(T_\Co)$ and hence $s_v\notin\Gamma_\Co$.
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
Under the convention above, $A_{T_\Co} = B/2B$ and $\rho_{T_\Co}(g) = \id$ means $g\equiv\id\bmod 2$; so $\rho_{T_\Co}(s_v)\neq\id$ and $s_v\notin\Gamma_\Co$.
With (2) this excludes the two positive squares and the long roots, leaving exactly (1), and the reflective set is the short roots.
:::

::: {.question #qst:gamma-co-reflection-index title="The index of the short-root reflection group"}
Is the index $[\Gamma_\Co : W(T_\Co)]$ finite, and if so, what is it?
:::

