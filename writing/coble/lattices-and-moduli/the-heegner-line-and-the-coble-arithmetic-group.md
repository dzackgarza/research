# The Heegner line and the stable orthogonal group {#sec-heegner-line}

::: {.remark}

The Coble locus is the $(-2)$ Heegner divisor $\mch_{-2}$ inside the Enriques period domain, and the Coble period lattice is the orthogonal complement of a $(-2)$ vector of $\ten$.
Both statements are used throughout, and both are statements about a *choice* of vector.
This section fixes that choice explicitly, shows it is unique up to the degree-$2$ Enriques arithmetic group, and describes the subgroup of $\Orth(T_\Co)$ that the choice produces.
The lattices are those of @sec-lattices, and the arithmetic groups those of @sec-moduli-construction.
:::

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

::: {.remark}

By @lem:primitive_embedding_eta, the primitive embedding $T_\Co\injects\ten$ sends the generator $h$ of $\generators{2}$ to $\tilde e+\tilde f$, which in the notation above is $\zeta=u+w$; @lem:coble-heegner-vector identifies this embedding with the inclusion of $\delta^{\perp\ten}$ for $\delta=u-w$ and supplies the gluing datum left implicit by @lem:primitive_embedding_eta.
This is the explicit form of the statement, recorded in the Period Domains section, that $T_\Co\cong v^{\perp \ten}$ for a vector $v$ with $v^2 = -2$ [@DK13].
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

::: {.remark}

The $(-2)$ divisor $\mch_{-2}$ is the discriminant divisor of the Enriques period space, whose points parameterize quotients of nodal K3 surfaces by an involution fixing a node, that is Coble surfaces with a $\tfrac14(1,1)$ singularity [@AEGS25 §2].
By @thm:coble-heegner-line-unique, this divisor stays irreducible after passing from $\Gamma_\En = \Orth(\ten)$ to the degree-$2$ group $\gent$.
It is a statement about the negative vector $\delta$, and is independent of the count of $\gent$-orbits of primitive *isotropic* lines in $\ten$, of which there are five, one for each $0$-cusp of $\fentwo$ [@AEGS25 Cor. 3.12].
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
The condition is on the line, since a component of the Heegner divisor is determined by $\ZZ\delta$ and not by a choice of sign for $\delta$.
The group $\gent$ here is the degree-$2$ group whose discriminant description is @prop:gamma-en-two-gluing, and the image is taken in $\Orth(T_\Co)$ and not in the stable subgroup $\Gamma_\Co$; how the two are related, and by how much they differ, is @prop:gamma-co-in-heegner-group (see @sec-gamma-co-comparison).
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

::: {.theorem #thm:coble-heegner-finite-orbits title="The finite image and its isotropic orbits"}

With the notation of @prop:polarization-stabilizer-enriques and @lem:coble-heegner-vector:

1. the image of the integral stabilizer in the discriminant group,
   $$
   G \definedas \im\bigl(\Stab_{\Orth(\sen)}(h)\to\Orth(A_{\sen}, q_{\sen})\bigr)
   ,
   $$
   has order $\abs{W(E_8)} = 696\,729\,600$, and is generated by the swap of the two isotropic generators of the $U$ summand of $C$, which fixes $h$, together with the reflections in the simple roots of the $E_8$ summand;

2. the corresponding group $G_\Co\leq\Orth(A_{T_\Co}, q_{T_\Co})$, obtained by transporting $G$ along $\gamma$ and restricting to the Coble Heegner complement $\delta^{\perp\ten} = T_\Co$, has order $\abs{W(E_8)}$ and acts on the $528$ isotropic classes of $A_{T_\Co}$ with orbit lengths
   $$
   [\,1,\ 2,\ 120,\ 135,\ 270\,]
   ;
   $$

3. the finite stabilizer $\Stab_{\Orth(q_{T_\Co})}\bigl(\tfrac12\tilde h_\Co\bigr)$ of the class of the transported polarization has order $94\,755\,225\,600$, contains $G_\Co$ with index $136$, and acts on the same $528$ isotropic classes with orbit lengths $[\,1,\ 255,\ 272\,]$.
:::

::: {.proof}

Finiteness of the orbits is finiteness of the class set in a fixed genus, which is `def:genus` together with the finiteness of the class number for a definite lattice of the relevant rank; the Coble-specific content is the identification of the relevant lattice as definite on the Heegner line.
:::

::: {.remark title="How the three orders are obtained"}

The generators named in (1) are the two evident families of isometries of $C$ fixing $h = u_0 + w_0$: the involution $u_0\leftrightarrow w_0$, and $W(E_8)$ acting on the second summand.
By @prop:polarization-stabilizer-enriques these generate a group of order $2\abs{W(E_8)}$ whose reduction has $\id_U\oplus(-\id_{E_8})$ in its kernel, so the image has order at most $\abs{W(E_8)}$.
The equality in (1), and the fact that finitely many integral isometries realise it, is verified through the owner's operations in `computations/reports/coble_stabilizer_generators.py`: the reflections in $u_0-w_0$ and in the eight simple roots of $E_8(-1)$ generate $\Orth(h^{\perp C})$ — the owner's own subgroup comparison, the generated subgroup having the order $2\abs{W(E_8)}$ of the whole group — and their discriminant images generate a subgroup of $\Orth(A_{S_\En}, q_{S_\En})$ of order $\abs{W(E_8)}$.
What that verification does *not* cover is (2) and (3): the two orbit decompositions are computations in the finite quadratic space $A_{T_\Co}\cong B/2B$ defined in @def:coble-mod-four-form, carried out by stabilizing the four fibers of $Q$ inside $\GL(B/2B)$ and then computing orbits of the resulting finite group on the fiber $\inverseof{Q}(0)$, and they are recorded here as computations whose verification is not part of this book.
The index $136 = 94\,755\,225\,600 / 696\,729\,600$ in (3), and the relation $46\,998\,591\,897\,600 = 496\cdot 94\,755\,225\,600$ between the order in @prop:coble-discriminant-group and that of the finite stabilizer, are consistency checks: $\tfrac12\tilde h_\Co$ is a class with $q_{T_\Co} = 1$, and by @prop:coble-q-fibers there are $496$ such classes.
:::

::: {.remark title="Reading the two orbit decompositions"}

The two decompositions of @thm:coble-heegner-finite-orbits answer different questions.
The coarser one, $[1, 255, 272]$, is the decomposition under the *whole* finite stabilizer of the polarization class, the largest group the discriminant form alone can distinguish.
The finer one, $[1, 2, 120, 135, 270]$, is the decomposition under the group that actually arises from integral isometries of $\sen$ fixing $h$, namely $G_\Co$.
Since the latter has index $136$ in the former, a calculation carried out purely in $\Orth(q_{T_\Co})$ overestimates how much of $A_{T_\Co}$ a degree-$2$ Coble period point can see.
By @prop:coble-q-fibers there are $527$ nonzero isotropic classes, and by @thm:coble-isotropic-class-orbits they form a single orbit. Since $2+120+135+270=527$, both decompositions refine that orbit.
They also refine one another, in exactly one way, which is a check available whenever either is recomputed: among the subset sums of $2,120,135,270$ the value $255$ occurs only as $120+135$, so a coarse orbit of size $255$ must consist of exactly those two fine orbits and a coarse orbit of size $272$ of the other two, $2+270$. A recomputation that produced any other refinement would contradict one of the two lists.
The index $136$ then fixes the four stabilizer indices, which is a second and independent check. If the fine orbit of a class has size $n$ and its coarse orbit has size $m$, then $[S_x:(G_\Co)_x]=136n/m$ for $S_x$ the stabilizer of the class in the finite stabilizer and $(G_\Co)_x$ its stabilizer in $G_\Co$; the four values are $136\cdot2/272=1$, $136\cdot270/272=135$, $136\cdot120/255=64$ and $136\cdot135/255=72$. All are integers, as they must be, and all are at most $136$, as $[S_x:(G_\Co)_x]\leq[S:G_\Co]$ forces; a recomputation producing a non-integral ratio would contradict the two lists together with the index.

Both are statements in the finite quadratic space $A_{T_\Co}$.
By @prop:coble-primitive-isotropic-classes, an integral parabolic stabilizer may have proper image in the finite one, so a finite orbit can split; hence neither decomposition yet classifies $\Gamma_\Co^\En(\delta)$-orbits of primitive isotropic *vectors* of $T_\Co$.
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

::: {.remark}

By @prop:theta-co-exists, the sign involution $\theta_\Co$ is determined as a lattice isometry by the primitive embedding and the gluing anti-isometry.
What a matrix realization additionally supplies is a basis in which $\theta_\Co$, the polarization class, and the roots of the Coxeter diagram can be compared with one another.

Combining @prop:theta-co-exists with @prop:gamma-en-two-gluing gives the Coble-side analogue: the restriction to $T_\Co$ of the centralizer of $\theta_\Co$ inside the stabilizer of a chosen polarization class $\tilde h_\Co\in S_\Co$ consists of those $g_T\in\Orth(T_\Co)$ for which some $g_S\in\Orth(S_\Co)$ satisfies $g_S(\tilde h_\Co) = \tilde h_\Co$ and $\bar g_T\circ\gamma_\Co = \gamma_\Co\circ\bar g_S$.
Identifying that group with $\Gamma_\Co^\En(\delta)$ of @def:gamma-co-en would require an isometry of $\lkt$ carrying $T_\Co^{\mathrm{Coble}} = S_\Co^{\perp\lkt}$ to $T_\Co = \delta^{\perp\ten}$ and $\tilde h_\Co$ to $h = e+f$ of @prop:gamma-en-two-gluing, and such an isometry would carry the orthogonal complement of $\tilde h_\Co$ in $S_\Co$ to that of $h$ in $\langle S_\En,\delta\rangle$.
That necessary condition is tested on an *admissible* polarization, one inside $K_S^\perp$ as @def:coble-polarization-classes requires: with $K_S = -3H + \sum_i E_i$ fixed by @prop:canonical-perp-is-e10, whose criterion is $\sum_i b_i = 3a$ for $D = aH - \sum_i b_i E_i$, the classes $F_1 = 3H - (E_1+\dots+E_9)$ and $F_2 = 3H - (E_1+\dots+E_8+E_{10})$ are isotropic, orthogonal to $K_S$, and satisfy $F_1\cdot F_2 = 1$, so $h_\Co = F_1+F_2$ has $a = 6$, $\sum_i b_i = 18$ and $h_\Co^2 = 2$.
For its pullback the two complements agree: both have rank $10$, determinant $2048$, signature $(0,10)$ and $2$ vectors of square $-2$, and the owner returns `True` for `is_isometric_to` (`computations/reports/coble_labeled_embedding.py`).
So the necessary condition holds for an admissible marking and does not obstruct the identification.
What an earlier version of this comparison reported as an obstruction used classes such as $H+E_1$, which satisfies $D\cdot K_S = -4$ and is therefore not admissible at all; that negative is withdrawn, and it is why admissibility has to be checked against @prop:canonical-perp-is-e10 rather than against squares and pairings.
Two further steps remain before anything can be identified. The comparison of A21 is between *labeled* tuples — commuting nonsymplectic involutions $I_\Co$, $I_{\mathrm{dP}}$, the degree-$4$ class $H$ fixed by both, a root $\alpha$ with $\alpha^2 = -2$, $H\cdot\alpha = 0$, fixed by $I_\Co$, and a chamber in which $\alpha$ is effective and $H$ nef and big (the research report's @sec-labeled-lattice-data) — Of those labels, the root is identified only at coordinate level. The two vectors of $\tilde h_\Co^{\perp}$ are $\pm\bigl(3f^*H-\sum_if^*E_i\bigr)$, and by @prop:coble-invariant-lattice's dictionary — a class of $S_\Co$ has the same coordinates as its preimage in $\Pic(S)$ and half the square — their preimages are $\pm\bigl(3H-\sum_iE_i\bigr) = \mp K_S$, a $(-1)$-class (`computations/reports/coble_root_effectivity.py`).
Its effectivity is decided by the cover, and two divisors have to be kept apart. The *branch* divisor is the plane sextic $C\subset S$, of class $[C] = 6H-2\sum_iE_i = -2K_S$ — DK13's model, $S$ being the blowup at the ten nodes of $C$, so the strict transform carries those multiplicities. The *ramification* divisor is $R = f^{-1}(C)$ inside $X$, and it is $R$, not $C$, that lives upstairs. For a double cover branched along $C$ the pullback relation is
$$
f^*[C] = 2[R],
$$
the coefficient $2$ being the ramification index along $R$, which is reduced because the strict transform of $C$ is smooth. With $[C] = -2K_S$ this gives
$$
[R] = \tfrac12 f^*[C] = f^*(-K_S) = \alpha,
$$
so $\alpha$ is the class of the *ramification curve* — an effective divisor exhibited geometrically, not a cohomological count. The sign is thereby fixed: $-R'$ with $R'$ effective would make $\alpha + [R'] = 0$, i.e. $R+R'$ principal with both terms effective and nonnegative, forcing both to vanish; so $+\alpha = 3f^*H-\sum_if^*E_i$ is the retained effective root, and $2\alpha = f^*[C] = 2[R]$ is effective as twice $R$, consistently.
What remains of the chamber is separate, and it is a question about a class: nefness is numerical and pulls back through the finite cover $f$, so $H = \tilde h_\Co$ is nef exactly when $h_\Co$ is (@prop:nef-big-finite-cover), and once $H$ is nef it is big because $H^2 = \deg(f)\,h_\Co^2 = 4 > 0$ on a surface; hence $H$ is nef and big exactly when $h_\Co$ is nef. What the sources do not assert is the nefness of $h_\Co$: @def:coble-polarization-classes gives $h_\Co = F_1+F_2$ with $F_i^2 = 0$, $F_1\cdot F_2 = 1$ in the non-degenerate case, which is the numerical pattern of an Enriques degree-$2$ polarization and not a nefness statement, and nefness would follow if the two isotropic classes $F_i$ were nef, for instance fibres of fibrations, which the definition does not require — the nefness assertion for a degree-$2$ polarization in [@DK13] is made for the Enriques surface's $h$, and the corresponding statement for the Coble surface is made in [@DK13, §8] only under the hypothesis that $S$ is *unnodal* — see the remark below, which records what that source does and does not supply. That is the missing premise of this half of the chamber, not a defect of the class formulation.

::: {.remark title="The degree-$2$ polarization on the Coble side, from the primary construction"}

The primary source behind [@DK13, §8] is [@CD12] — Cantat and Dolgachev, *Rational surfaces with a large group of automorphisms*, DK13's reference [3] — and its §3 was read directly. On an **unnodal** Coble surface $S$ — one with no $(-2)$-curves — take half-fibres $F_1\in\abs{f_1}$, $F_2\in\abs{f_2}$ of the Halphen fibrations of index $2$ and put $h = F_1+F_2$, so $h^2 = 2$ with $F_i^2 = 0$, $F_1\cdot F_2 = 1$. Then $\abs{2h}$ has no base points and defines a morphism $\phi_h: S\to\PP^4$ ([@CD12], Lemma 3.7, whose proof uses only the intersection properties of $f_1,f_2,K_S$ and $\abs{f_i} = \set{F_i}$, not the effectivity of $-2K_S$ — Remark 3.8); its image is a surface of degree $4$ and $\phi_h$ is $2$-to-$1$ onto it (Lemma 3.9), and that image is a Del Pezzo surface of degree $4$ with four ordinary double points (Lemma 3.10). Hence $2h$, and so $h$, is nef, and $h^2 = 2>0$ makes it big: **in the unnodal case the chamber's nefness premise is a theorem of the primary source**. The earlier sentence of this section, which said that [@DK13] asserts nefness only for the Enriques surface's $h$, was wrong about the Coble side.

That does **not** transfer to the construction used in this section, and what is missing is a map rather than a citation: no source gives a morphism from the one-node family of @prop:quasipolarization into [@CD12]'s model, so the comparison has not been made. [@CD12], Remark 3.3, states that unnodal Coble sets form a Zariski **open** subset of the set of all Coble sets and concludes that an unnodal Coble surface is a general one; openness, with the classical nonemptiness of the conditions (i)–(v) of Theorem 3.2, makes the unnodal locus dense in the Coble locus *if* that locus is irreducible, which the passage does not state and which is not claimed here. What the *one-node* members of @prop:quasipolarization form is not compared with the cited model here: no map from that family into [@CD12]'s construction is available in either source, so nothing is asserted about how it meets the unnodal open set, and the passage gives no nonemptiness, no density and no degeneration argument for such an intersection. So the chamber obligation of the direct-projective construction is **not** discharged by the citation; only the unnodal, and possibly general, smooth case is.

The maps and the automorphisms have to be kept apart, with each automorphism acting on its own surface, and the curves on the three surfaces are differently named:

$$
\begin{array}{ccc}
\widetilde X & \xrightarrow{\ \pi\ } & S \\[2pt]
{\scriptstyle I_\Co}\circlearrowleft & & {\scriptstyle \tau}\circlearrowleft \\[2pt]
\widetilde X & \xrightarrow{\ \pi\ } & S
\end{array}
\qquad
\begin{array}{ccc}
S & \xrightarrow{\ \phi_h\ } & \mathsf D\subset\PP^4 \\[2pt]
& & {\scriptstyle \mathrm{bl}_q}\uparrow \\[2pt]
S & \xrightarrow{\ \phi'\ } & \mathsf D'
\end{array}
$$

$\pi:\widetilde X\to S$ is the K3 double cover branched along the anticanonical curve $\mathfrak C\subset S$ (the unique curve in $\abs{-2K_S}$, of self-intersection $-4$, [@CD12], §3.2), with $I_\Co$ the deck involution *of $\widetilde X$*, whose fixed curve is $R_\pi \definedas \pi^{-1}(\mathfrak C)$; $\phi_h$ contracts $\mathfrak C$ to the node $q$ of $\mathsf D$ (as $h\cdot\mathfrak C = h\cdot(-2K_S) = 0$), $\mathrm{bl}_q$ blows up $q$ with exceptional curve $E_q\subset\mathsf D'$, and $\phi'$ is the resulting finite separable double cover, whose deck involution $\tau$ acts *on $S$* and whose fixed locus is the genus-$4$ curve $\overline W\subset S$ together with three isolated points — $\overline W$ being a curve on $S$, not on $\widetilde X$. With that separation, the fixed-locus figure that [@DK13, §8] attributes to "the deck transformation $\sigma$ of $S$" contradicts nothing about the genus-$0$ curve $R_\pi$: an earlier version of this remark compared the two and flagged a discrepancy, which was a conflation of domains and is withdrawn.

Whether $\tau$ lifts to $\widetilde X$ is decided by the double-cover criterion, and its two conditions hold here rather than being assumed: for $\pi$ branched along $B$ with $\OO_S(B) = \mathcal L^{\otimes 2}$, an automorphism $\tau$ of $S$ lifts to $\widetilde X$ if and only if $\tau(B) = B$ and $\tau^*\mathcal L\cong\mathcal L$. Here $B = \mathfrak C$ and $\mathcal L = \OO_S(-K_S)$, since $\OO_S(\mathfrak C) = \OO_S(-2K_S)$; the first condition holds because $\mathfrak C = \phi'^{-1}(E_q)$ and $\tau$ acts fibrewise over $\mathsf D'$, and the second because [@CD12] records that $K_S$ is $\tau$-invariant (proof of Theorem 3.5, where $f_1,f_2,K_S$ are used as $\tau$-invariant classes), so $\tau^*\OO_S(-K_S)\cong\OO_S(-K_S)$. A lift $\tilde\tau$ exists and commutes with $I_\Co$.
Existence is not the requirement, and the two data the tuple needs are not supplied by the sources. What the lift is, whether it is an involution and what it does to the lattice are settled below, from the cover algebra and from [@CD12]'s own action: @prop:involution-lifting-double-cover and the remark after this one.
Finally, no identification is made between the data of this section and those of [@CD12]. The classes $H = \pi_{\mathrm{dP}}^*\OO(1,1)$ and $L$ with $\psi^*L = H$ are classes of the direct-projective construction, with $H^2 = 4$ and $L^2 = 2$; $h$ and $\mathfrak C$ are classes of the cited model, with $h^2 = 2$ and $\mathfrak C^2 = -4$, and $h\cdot\mathfrak C = 0$ as $L\cdot C = 0$. The numerical coincidences are consistent with an identification and do not demonstrate one; what would demonstrate it is a marking carrying one set of classes to the other, and none is produced here.
:::

::: {.proposition #prop:involution-lifting-double-cover title="Lifting an involution through a branched double cover, and when the lift is an involution"}

Let $S$ be a smooth projective surface over $\CC$, let $\mcl$ be a line bundle, let $s\in H^0(\mcl^{\otimes2})$ be a section cutting out a **smooth** curve $B$, and let $\pi\colon\widetilde X\to S$ be the double cover with $\pi_*\OO_{\widetilde X} = \OO_S\oplus\mcl^{-1}$ and multiplication given by $s$; let $\iota$ be the deck involution, $+1$ on $\OO_S$ and $-1$ on $\mcl^{-1}$.
Let $\tau\in\Aut(S)$ be an **involution** with $\tau(B) = B$, and let $\lambda\colon\tau^*\mcl\to\mcl$ be an isomorphism satisfying $\lambda(\tau^*s) = c\,s$ for some $c\in\CC^\times$ — the compatibility of the branch section with the chosen isomorphism; rescaling $\lambda$ by a square root of $c$ normalizes $c = 1$ over $\CC$, and the freedom left is $\pm\lambda$, which is what part (1) records as the choice of lift. Then:
1. $\tau$ lifts to an automorphism $\tilde\tau$ of $\widetilde X$ with $\pi\tilde\tau = \tau\pi$, and the lifts of $\tau$ are exactly $\tilde\tau$ and $\tilde\tau\iota$;
2. $\tilde\tau^2\in\set{\id,\iota}$, and $(\tilde\tau\iota)^2 = \tilde\tau^2$: both lifts have the same square, so replacing one lift by the other does **not** change the order;
3. let $p\in B$ be a fixed point of $\tau$ and let $\sigma\in\set{\pm1}$ be the sign by which $\tau$ acts on the normal line $N_{B/S,p}$. Then $\tilde\tau^2 = \id$ if $\sigma = +1$, and $\tilde\tau^2 = \iota$ if $\sigma = -1$; in particular, if a fixed curve of $\tau$ passes through $p$ transversally to $B$, then $\tilde\tau^2 = \id$ and the lift is an involution.
:::

::: {.proof}

(1) The $\ZZ/2$-graded algebra $\mca = \OO_S\oplus\mcl^{-1}$ has $\Spec_S\mca = \widetilde X$. The action of $\tau$ on it is the identity in degree $0$ and $\mcl^{-1}\to\tau_*\mcl^{-1} = \tau_*(\tau^*\mcl)^{-1}\xrightarrow{\lambda^{-1}}\tau_*\mcl^{-1}$ in degree $1$; it is multiplicative because $\lambda(\tau^*s) = cs$ makes the structure section go to a scalar multiple of itself. Any two such actions agree on $\OO_S$, so their quotient is an automorphism over $\OO_S$, i.e. an element of the deck group $\set{\id,\iota}$ ($\widetilde X$ being connected as $B\neq\emptyset$).
(2) $\tilde\tau^2$ satisfies $\pi\tilde\tau^2 = \pi$, so it is a deck transformation. Since $\iota$ is central in $\Aut(\widetilde X/S)$, $(\tilde\tau\iota)^2 = \tilde\tau\iota\tilde\tau\iota = \tilde\tau^2\iota^2 = \tilde\tau^2$; the two lifts therefore share their square, and neither choice changes the order.
(3) Take coordinates $(u,v)$ at $p$ with $B = \set{u = 0}$ and $\mcl$ trivialized so that $s = u$; then $\widetilde X$ is $\set{w^2 = u}$ over that neighbourhood and $\tau^*(u) = \sigma u + O(u^2)$ because $\tau$ fixes $p$ and preserves $B$. A lift acts by $\tau^*(w) = \epsilon w$ with $\epsilon^2 w^2 = \tau^*(u)$, i.e. $\epsilon^2 = \sigma$. Then $\tilde\tau^2$ acts on $w$ by $\epsilon^2 = \sigma$, whereas $\iota$ acts by $-1$; so $\tilde\tau^2 = \id$ exactly when $\sigma = +1$, and when $\sigma = -1$ one has $\epsilon = \pm i$ over $\CC$ and $\tilde\tau^2 = \iota$. If a fixed curve $C'$ of $\tau$ passes through $p$ transversally to $B$, then $T_pC' = N_{B/S,p}$ and $\tau$ fixes $C'$ pointwise, so $\sigma = +1$.
:::

::: {.corollary #cor:lift-in-cd12-model title="The lift of CD12's deck transformation is an involution"}
Let $B = \mathfrak C\in\abs{-2K_S}$, $\mcl = \OO_S(-K_S)$, and let $\tau$ be [@CD12]'s deck transformation of $\phi'\colon S\to\mathsf D'$. The hypotheses hold: $\tau$ is an involution by construction, $\mathfrak C$ is smooth and rational, $\tau(\mathfrak C) = \mathfrak C$, and the linearization exists because $K_S$ is $\tau$-invariant; and the compatibility of the branch section is automatic once $\tau(\mathfrak C) = \mathfrak C$, since $s$ and $\tau^*s$ cut out the same divisor $\mathfrak C\in\abs{2\mcl}$ and so differ by a nonzero constant.
[@DK13, §8] states that the fixed locus of the deck transformation of $S$ consists of a smooth curve $\overline W$ of genus $4$ together with three isolated points, and that $\overline W$ meets $\mathfrak C$ in two points. Let $p$ be one of them. Since $\overline W$ is fixed pointwise, $\tau$ acts by $+1$ on $T_p\overline W$; and it acts on $\mathfrak C\cong\PP^1$ as a nontrivial involution — were it trivial, $\mathfrak C$ would lie in the fixed locus, hence in $\overline W$ or equal to one of the three isolated points, and neither is possible: $\mathfrak C\cong\PP^1$ has genus $0$ against the genus $4$ of $\overline W$, and it is a curve — so it acts by $-1$ on $T_p\mathfrak C$. The two eigenvalues therefore differ, the tangent lines differ, and $T_p\overline W$ is the normal line $N_{\mathfrak C,p}$: the intersection is transverse as a *consequence* of the fixed-locus data, not of the count of two points. At such a $p$ one has $\sigma = +1$, so $\tilde\tau^2 = \id$ by part (3) of the proposition and the lift is an involution commuting with $I_\Co$.
The three isolated fixed points of $\tau$ cannot lie on $\mathfrak C$: at such a point both eigenvalues of $\tau$ on $T_pS$ would be $-1$, giving $\sigma = -1$ and hence $\tilde\tau^2 = \iota$, which part (2) excludes. This is consistent with [@DK13, §8], where those points map to the three nodes of $\mathsf D$ other than $q = \phi_h(\mathfrak C)$.
:::

::: {.remark title="What the lift does to the lattice, in CD12's own notation"}
Take $B = \mathfrak C\in\abs{-2K_S}$ and $\mcl = \OO_S(-K_S)$, so $\OO_S(\mathfrak C)\cong\mcl^{\otimes2}$, and take for $\tau$ [@CD12]'s deck transformation of $\phi'\colon S\to\mathsf D'$: it preserves $\mathfrak C$ because $\mathfrak C = \phi'^{-1}(E_q)$ and $\tau$ is fibrewise over $\mathsf D'$, and $\tau^*\OO_S(-K_S)\cong\OO_S(-K_S)$ because [@CD12] uses $f_1,f_2,K_S$ as $\tau$-invariant in the proof of its Theorem 3.5. The hypotheses of @prop:involution-lifting-double-cover hold — $\tau$ is an involution by construction, $\mathfrak C$ is a smooth rational curve, $\tau(\mathfrak C) = \mathfrak C$, and the linearization exists because $K_S$ is $\tau$-invariant — and the lift is an involution by @cor:lift-in-cd12-model, not by a choice of lift: the fixed curve $\overline W$ supplies the normal action that part (3) asks for.
On classes pulled back from $S$ the action is forced and independent of that choice, since $\tilde\tau(\pi^*D) = \pi^*(\tau D)$ for a divisor class $D$. [@CD12] gives $\tau^* = \id_{\mathsf H}\oplus(-\id_{E_8})$ on $\Pic(S)\otimes\QQ$, where $\mathsf H$ is CD12's hyperbolic plane $\langle f_1,f_2\rangle$ and $E_8$ its orthogonal complement; $\mathsf H$ here is *not* the degree-$4$ class $H$ of this section, which is why it is written with a different face. The dimensions account for the whole space: $\rk\Pic(S) = 2 + 8 + 1 = 11$, the Picard rank of a Coble surface, the last summand being $\ZZ K_S$, on which $\tau$ acts trivially.
So $\tilde\tau$ fixes $\pi^*\mathsf H$ and $\pi^*K_S$ and negates $\pi^*E_8$, and its invariant lattice contains $\pi^*\mathsf H\oplus\ZZ\pi^*K_S$, of rank $3$. The first summand is $\cong U(2)$, since $f_i^2 = 0$ and $f_1\cdot f_2 = 1$ give $(\pi^*f_i)^2 = 0$ and $\pi^*f_1\cdot\pi^*f_2 = 2$; so the invariant lattice does contain the lattice $\sdp$ of [@AEGS25]. But $\pi^*K_S$ has square $2K_S^2 = -2$ in the model of [@CD12, §3] and [@DK13, §3], where $K_S^2 = 9-10 = -1$, and $U(2)$ has no class of square $-2$; the rank-$3$ lattice $\pi^*\mathsf H\oplus\ZZ\pi^*K_S$ is therefore not contained in $\sdp$, so the lift's invariant lattice is not $\sdp$ and the lift is not an involution of [@AEGS25]'s $\mathrm{dP}$ type. Whether it is a Del Pezzo involution in a wider sense, with quotient a Del Pezzo surface of lower degree, is a separate question this computation does not touch.
What the source does *not* determine, and what is not assumed here: the action on the part of $H^2(\widetilde X,\QQ)$ not pulled back from $S$ — the classes carried by the ramification curve and its geometry. There the two lifts $\tilde\tau$ and $\tilde\tau I_\Co$ differ, so no single sign acts on "the whole anti-invariant lattice"; deciding it needs the linearization, equivalently the induced action on the normal bundle of $\mathfrak C$ at a fixed point, which [@CD12] does not record.

Two further things the same algebra does decide, and they matter for the tuple. First, $I_\Co$ is nonsymplectic. The canonical bundle of the double cover is $K_{\widetilde X} = \pi^*(K_S+\mcl)$ (@rmk:k3-double-cover-construction), which with $\mcl = \OO_S(-K_S)$ is $\OO_{\widetilde X}$ — the reason $\widetilde X$ is a K3 — so that $H^0(\widetilde X,K_{\widetilde X}) = H^0(S,K_S+\mcl)\oplus H^0(S,K_S)$, the twist by $\mcl$ sitting in the $\OO_S$-summand of $\pi_*\OO_{\widetilde X}$: the first summand is $H^0(S,\OO)\cong\CC$ and the second vanishes because $S$ is rational. Since $K_{\widetilde X}$ is trivial the sign can be read off locally: at a point of $B$, in coordinates with $B = \set{u = 0}$ and $\widetilde X = \set{w^2 = u}$, a generator is $dw\wedge dv$ and $I_\Co^*(dw\wedge dv) = -dw\wedge dv$; so $I_\Co$ acts by $-1$ on $H^{2,0}(\widetilde X)$. The two lifts differ by $I_\Co$, so exactly one of $\tilde\tau,\tilde\tau I_\Co$ is nonsymplectic; both are involutions by @cor:lift-in-cd12-model, and imposing the tuple's requirement selects that one.
Second, the lift fixes every class in $\pi^*\mathsf H$, so it fixes every degree-$4$ class of the form $\pi^*h$ with $h\in\mathsf H$ — in particular $\pi^*h$ for CD12's polarization $h = F_1+F_2$. Whether the degree-$4$ class $H$ of this section *is* such a pullback is the identification that is *not* made in the remark above, and it is not assumed. What is decided is the shape: the primary construction yields a geometric involution commuting with $I_\Co$, nonsymplectic after the choice of lift, fixing the pulled-back polarization, with invariant lattice strictly larger than $\sdp$ — hence not an involution of [@AEGS25]'s $\mathrm{dP}$ type.

::: {.remark title="The del Pezzo slot: what is established, and the answer"}
Established, and kept separate from anything proposed. (i) $M_X = S_\Co$ and the coordinates of $H$ and $\alpha$ (@prop:coble-cover-marking). (ii) If the slot lies in $S_\Co$ it is forced to be $\langle f^*F_1,f^*F_2\rangle$ — the enumeration over the definite fibre is complete — and that isometry is the action of no automorphism in the marking of the construction (@prop:del-pezzo-placement, @cor:no-del-pezzo-involution-coble-cover). (iii) The discriminant forms are anti-isometric, so the gluing of $S_\Co$ with $T_\Co$ is unobstructed. (iv) [@CD12]'s deck transformation lifts to an involution commuting with $I_\Co$, nonsymplectic after the choice of lift, fixing every class of $\pi^*\mathsf H$, and its invariant lattice is strictly larger than $\sdp$.
The residue is a two-case statement, and the cases are exhaustive because commutation with $I_\Co$ forces the slot to be nested with $S_\Co$ (@prop:del-pezzo-placement), so $\rk(S_\Co\cap\sdp)\in\set{1,2}$. For $\rk = 2$ the answer is negative by (ii). For $\rk = 1$ the lattice question is settled in the affirmative, and the settlement is @prop:rank-one-slot's, not the one an earlier version of this remark gave: the operator on $S_\Co$ with $(+1)$-eigenspace $\ZZ H$ is integral because the values of $x\cdot H$ on $S_\Co$ generate $2\bZ$, and its eigenspaces do *not* split $S_\Co$; the second generator of the slot is not a vector of $S_\Co\oplus T_\Co$ at all, but the sum $\tfrac12H+t$ of half the class $H$ and a vector $t\in T_\Co^{\#}$ of square $-1$, whose existence in the class the gluing presents is what makes the slot exist. What is withdrawn with that earlier version is the whole of its last chain: the orthogonal sum $S'\perp T$ of two lattices of nontrivial discriminant is not unimodular and is not $\lkt$, Nikulin's existence theorem for a complement of the required genus is a predicate and not a construction, and it supplies neither the gluing nor a primitive embedding nor any operator.
So the two ranks stand differently, and the difference is where the unfinished premise sits. Rank one is settled for the authored tuple: it needs only the bullets, the rank of the del Pezzo invariant lattice, and the effectivity of $\alpha$ (@prop:no-rank-one-automorphism), with no identification and no smoothness. Rank two needs, beyond the lattice reduction that leaves one integer, the parity $\alpha\cdot S_\Co\subseteq2\bZ$, which is proved when the quotient is a smooth Coble surface and the root is the fixed curve (@prop:root-pairs-evenly) and is a hypothesis otherwise (@rmk:parity-scope): for it one needs $S_\Co = \psi^*\Pic(\wV)$, hence @prop:coble-invariant-lattice's hypotheses, which the classical ten-nodal model satisfies and a resolved nodal member does not. The lattice computations of @prop:rank-one-slot, @prop:del-pezzo-placement and @cor:no-del-pezzo-involution-coble-cover remain what they were, statements in the marking of @prop:coble-cover-marking.
:::
:::
Of the involutions, $I_\Co = -\theta_\Co$ exists without gluing data: @prop:theta-co-exists gives $\theta_\Co$ as $+1$ on $T_\Co$ and $-1$ on $S_\Co$, and the pair $(\id_{S_\Co}, -\id)$ used to define $-\theta_\Co$ preserves every isotropic gluing subgroup because both discriminant forms are $2$-elementary; its action on $H$ is that of $+\id_{S_\Co}$, an isometry of $S_\Co\perp T_\Co$ which the owner verifies fixes $H$. The del Pezzo involution *is* lattice data, contrary to what an earlier version of this paragraph said: [@AEGS25, def:involutions] gives $I_{\mathrm{dP}}(v,u,u',e,e') = (-v,u',u,-e,-e')$ on $U^3\oplus E_8^2$, with eigenspaces $S_{\mathrm{dP}} = \Delta(U) = U(2)$ and $T_{\mathrm{dP}} = U\oplus\Delta^-(U)\oplus E_8^2$, and the owner confirms that the four stated eigenspaces act by $+1$ and $-1$ as stated and that AEGS's Enriques pair is exactly the $S_\En$, $T_\En$ used here, with $[\lkt:S_\En\oplus T_\En] = \abs{A_{S_\En}} = 2^{10}$ (`computations/reports/coble_aegs_involutions.py`). What the *labeling* asks — that this $I_{\mathrm{dP}}$ is the del Pezzo involution of the Coble K3 cover, commuting with $I_\Co$ and fixing $H$ — is not left open by a missing marking: the marking is forced by the source construction itself, and with it the candidate whose invariant lattice is the span of the two isotropic summands is excluded as an automorphism (@cor:no-del-pezzo-involution-coble-cover). That was one case of two; the other, the rank-one slot, is excluded as well (@prop:no-rank-one-automorphism), so no admissible invariant lattice has a realizability question left: every one of them reverses the authored root. An earlier version of this paragraph located the difficulty in placing $M_X$ inside $U^3\oplus E_8^2$; [@DK13] names the classes $e_0 = f^*H$ and $e_i = f^*E_i$ explicitly, and those are classes in the basis this book already uses, so no placement had to be invented. The chamber's remaining condition is the nefness of $h_\Co$ set out above, nef-cone geometry rather than a lattice computation. Nothing above promotes the modelled lattice data to the retained geometric labels.
The morphism check recorded for $I_\Co$ is on the abstract orthogonal sum: it is an isometry of $S_\Co\perp T_\Co$ — rank $22$, determinant $-2^{22}$, signature $(3,19)$ — and not of $\lkt$, which is not built here; the sum is the free part of $\lkt$ before the gluing, so the check verifies the component behaviour that the labels need and not the ambient isometry.

Matching complements is necessary rather than sufficient, and the further step is now taken: by Nikulin an isometry carrying $\tilde h_\Co$ to $h$ exists exactly when some isometry $\tilde h_\Co^{\perp}\to h^{\perp}$ carries the glue class of one to that of the other, and that is decided in the affirmative at the owner (`computations/reports/coble_labeled_embedding.py`). One fixed isometry $\phi_0$ carries the whole set of isometries to $\phi_0\circ\Orth(\tilde h_\Co^{\perp})$; $\Orth(\tilde h_\Co^{\perp})$ has order $2\,786\,918\,400$ with $22$ generators, its image in $\Orth(A)$ has order $696\,729\,600$, and through the represented action of that image on the finite form — restricted along the subgroup inclusion — the glue class of $S_\Co$ and the transport of that of $M$ lie in one orbit. So the two polarized lattices are matched by an isometry carrying $\tilde h_\Co$ to $h$.
The ambient step is an argument from five stated inputs, each sourced, and it is abstract in a way that has to be said plainly.
(i) $S_\Co^{\perp\lkt} = T_\Co$: this is the primitive embedding and gluing of @prop:coble-invariant-lattice together with @prop:theta-co-exists, whose eigenspaces are $S_\Co$ and $T_\Co$.
(ii) $M \definedas T_\Co^{\perp\lkt}$, identified with $S_\En\oplus\ZZ\delta$ by determinants rather than by a saturation step: $\lkt$ is the overlattice of $S_\En\oplus T_\En$ glued along the graph of the *full* anti-isometry $\gamma$ of @prop:gamma-en-two-gluing, so $[\lkt : S_\En\oplus T_\En] = \abs{A_{S_\En}} = 2^{10}$ — not $2$, which is what an earlier version of this paragraph asserted without a source; and with $\det T_\Co = 2^{11}$ one has $\det(T_\Co^{\perp\lkt}) = \det T_\Co = 2^{11}$ while $\det(S_\En\oplus\ZZ\delta) = \det S_\En\cdot\delta^2 = 2^{10}\cdot 2 = 2^{11}$, and $S_\En\oplus\ZZ\delta\subseteq T_\Co^{\perp\lkt}$, so the containment is an equality.
(iii) $\gamma_\Co\colon A_{S_\Co}\iso A_{T_\Co}$ and $\gamma\colon A_{S_\En}\iso A_{T_\En}$ are the anti-isometries of those two propositions; their existence and the sign $q\circ\gamma = -q$ are part of them.
(iv) $\Orth(T_\Co)\to\Orth(A_{T_\Co})$ is surjective for the $2$-elementary lattice $T_\Co$: @thm:two-elementary-surjectivity. This is the theorem, and it is where the owner's generator route stands aside: at the pinned provider that route raises, with the traceback in the repository's defect list, while on the later provider recorded there the same specimen returns `True` — a later-provider non-reproduction, with the provenance caveat that the executed tree, not the header's hash, is the one that ran, and with the historical failure preserved. Neither outcome bears on the theorem, and the step above uses the theorem.
(v) $\lkt$ is the unique even unimodular lattice of signature $(3,19)$, by the classification of indefinite even unimodular lattices.
On those, the composite $\gamma_\En\bar\psi\gamma_\Co^{-1}$ is an isometry of $A_{T_\Co}$, realised by an integral $\phi\in\Orth(T_\Co)$ by (iv); the pair $(\psi,\phi)$ then preserves the gluing subgroup by (iii) and extends over $\lkt$ by @thm:nikulin-gluing, carrying the Coble embedding to the Enriques one and $\tilde h_\Co$ to $h$.
What this does *not* establish: that either decomposition comes from an actual Coble, respectively Enriques, surface, that the chamber is the one in which $h_\Co$ is nef, or that the embeddings are the retained geometric ones — those are the labels, and they are exactly what @prob:coble-rigidity carries. Of the three lattices involved, $\Orth(S_\Co)\to\Orth(A_{S_\Co})$ and $\Orth(M)\to\Orth(A_M)$ are owner-verified; for $T_\Co$ that route failed at the pinned provider and returns `True` on the later provider recorded in the repository's defect list, so what stands there is a pinned-provider failure that a later provider does not reproduce — a statement about the maintained implementation and not a mathematical question, with the traceback, minimal construction and provenance kept beside it. The step for $T_\Co$ is therefore @thm:two-elementary-surjectivity, cited as a theorem, and the failure of a computation to reproduce it is no evidence either way. The labels are as stated above: the root is $+\alpha = 3f^*H-\sum_if^*E_i$, the class of the ramification curve $R$ since $f^*[C] = 2[R]$ and $[C] = -2K_S$; what remains of the chamber is the nefness of $h_\Co$, the degree-$4$ class $H = f^*h_\Co$ being nef and big exactly when $h_\Co$ is nef and not otherwise; $I_\Co = -\theta_\Co$ exists without gluing data and fixes $H$ through its $+\id_{S_\Co}$ component; $I_{\mathrm{dP}}$ is lattice data of [@AEGS25, def:involutions], and the candidate whose invariant lattice is the span of the two isotropic summands is a lattice isometry that no automorphism realizes (@cor:no-del-pezzo-involution-coble-cover): there the lattice pair exists and commutes and the automorphism does not, while for any other admissible invariant lattice the question is open.
The finite comparison is untouched by all of this: by @prop:gamma-co-in-theta-centralizer and @prop:gamma-co-in-heegner-group both groups are extensions of the same $\Gamma_\Co$ by subgroups of $\Orth(A_{T_\Co}, q_{T_\Co})$.
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

::: {.remark title="Why no assertion about bigness of $f^*L$ is made here"}
What the chamber below needs is only that $f^*h_\Co$ be nef and big when $h_\Co$ is nef, and that follows from the two halves above together with $h_\Co^2 = 2$; no equality of Iitaka dimensions, and no statement that bigness of $L$ and of $f^*L$ agree in general, is used anywhere, so none is asserted.
:::

::: {.proposition #prop:coble-cover-marking title="The marking of the Coble cover and the del Pezzo slot"}

In the model of [@DK13, §3] let $S$ be the blowup of $\PP^2$ at the ten nodes of an irreducible plane sextic $C$ and let $f\colon X\to S$ be the double cover branched along the proper transform $\tilde C\in\abs{-2K_S}$, so that $X$ is a K3 surface.
Then the invariant lattice of the covering involution is $f^*\Pic(S)$, spanned by $e_0 = f^*H$ and $e_i = f^*E_i$ for $i = 1,\dots,10$, with $e_0^2 = 2$ and $e_i^2 = -2$; this lattice is $M_X$, it equals $S_\Co$, and $N_X = T_\Co$.
In that basis
$$
H = \tilde h_\Co = 6e_0 - 2\Sum_{i\le 8}e_i - e_9 - e_{10},
\qquad
\alpha = 3e_0 - \Sum_{i=1}^{10}e_i,
$$
and the two isotropic classes $f^*F_1 = 3e_0-\Sum_{i\le9}e_i$ and $f^*F_2 = 3e_0-\Sum_{i\le8}e_i-e_{10}$ span a primitive $U(2)$ inside $S_\Co$ with $H = f^*F_1+f^*F_2$.
Taking $+1$ on that $U(2)$, $-1$ on its orthogonal complement $N\definedas\langle f^*F_1,f^*F_2\rangle^{\perp S_\Co}$ inside $S_\Co$, and $-\id$ on $T_\Co$ defines an integral isometry $\phi$ of $\lkt$: its $(+1)$-eigenspace is $\langle f^*F_1,f^*F_2\rangle\cong U(2)$, its $(-1)$-eigenspace is the negative definite rank-$9$ lattice $N$ together with $T_\Co$, it fixes $H$, and it reverses $\alpha$.
This is a statement about the lattice: nothing here asserts that $\phi$ is the action of an automorphism of $X$, nor that it preserves a chamber.
:::

::: {.proof}

$\tilde C\cdot E_i = (6H - 2\Sum_j E_j)\cdot E_i = 2$, so $f^{-1}(E_i)\to E_i\cong\PP^1$ is a double cover branched at two points, hence a connected smooth rational curve; $E_i$ lies outside the branch locus, so $f^*E_i = [f^{-1}(E_i)]$ and $(f^*E_i)^2 = \deg(f)\,E_i^2 = -2$.
The span of the $e_i$ is $f^*\Pic(S)$, contained in $H^2(X,\ZZ)^{I_\Co}$; that group has rank $b_2(S) = 11$ by $\pi^*\pi_* = \id+\iota^*$ over $\QQ$, and $f^*\Pic(S)$ has rank $11$ and determinant $2^{11}\det\Pic(S) = 2^{11}$, which is also $\det S_\Co$ — since $\det T_\Co = 2^{11}$ and $[S_\Co\oplus T_\Co:\lkt] = 2^{11}$ — so the containment is an equality, and the coordinates of $H$ and $\alpha$ are those of $f^*(F_1+F_2)$ and $f^*(3H-\Sum_iE_i)$.
The classes $f^*F_1, f^*F_2$ are isotropic with $f^*F_1\cdot f^*F_2 = 2$: in the display, $(f^*F_1)^2 = 18-18 = 0$, $(f^*F_2)^2 = 18-18 = 0$ and $f^*F_1\cdot f^*F_2 = 18-16 = 2$, and the pair is primitive in $S_\Co$ because $kv = ma+nb$ forces $k\mid m,n$ and then $v\in\langle a,b\rangle$.
Integrality is the extension datum, and it sits in the pair $(\phi|_{S_\Co}, -\id_{T_\Co})$. The decomposition $S_\Co = \langle f^*F_1,f^*F_2\rangle\perp N$ is an orthogonal direct sum with $\det\langle f^*F_1,f^*F_2\rangle = -4$ and $\det N = -512$, whose product $2048 = 2^{11} = \det S_\Co$ is the determinant of $S_\Co$, so the index is $1$: every element of $S_\Co$ is a sum of one element of each summand. On the two summands $\phi$ acts by $+1$ and by $-1$; the discriminant group $A_{S_\Co}$ has exponent $2$ — $S_\Co$ is $2$-elementary — so $-1 = 1$ there and $\phi$ acts trivially on $A_{S_\Co}$.
For $T_\Co$ the reason is not the same: that $q_{T_\Co}(-x) = q_{T_\Co}(x)$ shows only that $-\id$ *preserves* the discriminant form, not that it acts as the identity on discriminant classes, and the identity requires the exponent. It is the stated $2$-elementarity of $T_\Co$ (@prop:coinvariant_involution_2elementary) that supplies it, $A_{T_\Co}$ then having exponent $2$, on which $-\id = \id$.
The gluing subgroup of $S_\Co\perp T_\Co$ is the graph of the anti-isometry $\gamma_\Co$ of @prop:coble-invariant-lattice, and an automorphism of $A_{S_\Co}\oplus A_{T_\Co}$ acting trivially on each factor preserves that graph; by @thm:automorphism-lifting-criterion the pair therefore extends, uniquely, to an isometry of $\lkt$.
The operator and the two discriminant facts are certified by the owner's operations in `computations/reports/coble_del_pezzo_slot_operator.py`: $\phi$ is built from its images through the isometry constructor, which accepts it only as an isometry of $S_\Co$; the pairing preservation, the involution, $\phi(H) = H$, $\phi(\alpha) = -\alpha$ and the two eigenspaces are checked as equalities of lattice elements; $\rho(\phi)$ and $\rho(-\id_{T_\Co})$ are checked to fix every discriminant generator; and the exponent $2$ of both discriminant groups is checked. What that run does *not* do is build $\lkt$ or the gluing: the extension is the criterion applied to those verified hypotheses, and $\lkt$ itself is not constructed here.
That extension preserves $S_\Co$ and $T_\Co$, hence commutes with $I_\Co$, and it fixes $H$ because $H\in\langle f^*F_1,f^*F_2\rangle$.
The source hypotheses used are [@DK13, §3] for the model and the ten classes, @prop:coble-invariant-lattice for the primitive embedding with complement $T_\Co$ and its gluing, @prop:coinvariant_involution_2elementary for the $2$-elementarity that makes $-\id$ an identity on $A_{T_\Co}$, and the effectivity of $\alpha = [R]$ established above.
:::

::: {.corollary #cor:no-del-pezzo-involution-coble-cover title="The isometry carried by the two isotropic summands is not geometric"}

In the marking of @prop:coble-cover-marking — the one that names the classes $e_0,\dots,e_{10}$ on $X$ — the isometry $\phi$ is not the action of an automorphism of $X$ on $H^2(X,\ZZ)$.
Indeed $\alpha$ is orthogonal to $f^*F_1$ and $f^*F_2$ — both pairings are zero, computed at the owner in `computations/reports/coble_del_pezzo_placement.py` — so $\phi(\alpha) = -\alpha$; in this marking $\alpha = [R]$ is the class of the ramification curve and is effective, while $-\alpha$ is the class of no effective divisor, and an automorphism carries effective classes to effective classes, so no $\iota\in\Aut(X)$ has $\iota^* = \phi$ under this identification.
The scope is this marking: the argument uses the effectivity of the class named $\alpha$, which is a fact about the construction and not about an arbitrary isometry of $H^2(X,\ZZ)$ with $\lkt$.
This excludes $\phi$, and only $\phi$; what it does not exclude is the subject of the next remark.
:::

::: {.remark title="What the corollary settles, and what it does not"}

Three levels have to be kept apart, and all three are now settled. $\phi$ exists as an integral isometry of $L_{K3}$, commutes with $I_\Co$ and fixes $H$ — that is @prop:coble-cover-marking. It is not the action of an automorphism of $X$ — that is the corollary. And no other admissible slot is either: every one of them reverses $\alpha$, in rank one by @prop:no-rank-one-automorphism and in rank two by @prop:rank-two-slot-boundary together with the parity of @prop:root-pairs-evenly.
The corollary is about $\phi$, and not about every candidate: the tuple requires an involution whose invariant lattice is $\sdp$ and contains $H$, and $\phi$ is one such, distinguished by being $+1$ on the span of the two isotropic summands of the degree-$2$ polarization. That last step is where this corollary stopped: it excludes $\phi$ and said nothing about a slot defined by a different primitive $U(2)\subset S_\Co$ containing $H$. The rank-two case is nevertheless exhaustive, because such a slot is forced to be $\phi$ (@prop:del-pezzo-placement and the uniqueness remark after it), and the rank-one case is the other branch.
For $\phi$ the geometric question is one of cones rather than of lattices: the action is $-\id$ on the whole of $U(2)^{\perp\lkt}$, which contains the transcendental lattice of every member of the family, so $\phi$ is a Hodge isometry for every member, and it would be realised exactly when it preserved the Kähler cone. That is not what fails: the reversal of $\alpha$ fails, and it fails before any cone is consulted. The rank-one slot is not even a Hodge isometry on a general member, which is what @rmk:rank-one-geometry locates.
Nor is the obstruction of the cruder kind that the ten curves $f^{-1}(E_i)$ might suggest: an involution whose invariant lattice is $\sdp$ fixes no smooth rational curve, since $\sdp$ contains no class of square $-2$ (@prop:del-pezzo-invariant-has-no-roots), and it may simply move them. What obstructs $\phi$ is narrower: its anti-invariant part is the rank-$9$ lattice $N$, which contains the effective class $\alpha$ of square $-2$, and $\phi$ reverses that class.
:::

::: {.proposition #prop:del-pezzo-placement title="What the abstract conditions determine about the del Pezzo slot"}

Let $\psi$ be an involution of $\lkt$ whose invariant lattice is $\sdp\cong U(2)$, let $H\in\sdp$ with $H^2 = 4$, and suppose that $\psi$ commutes with $I_\Co$ — equivalently, that it preserves $S_\Co$.
Then $H = a+b$ for a hyperbolic basis $a,b$ of $\sdp$, and the isotropic classes $a'\in\sdp$ with $a'\cdot H = 2$ are exactly $a$ and $b$.
Put $A \definedas S_\Co\cap\sdp$ and $B \definedas S_\Co\cap\sdp^{\perp\lkt}$. Then $S_\Co\otimes\QQ = A_\QQ\oplus B_\QQ$ and $2S_\Co\subseteq A\oplus B\subseteq S_\Co$; the sum therefore has finite index in $S_\Co$, a power of $2$, and is *not* in general all of $S_\Co$ — the halves $(x\pm\psi x)/2$ of an element $x\in S_\Co$ need not lie in $S_\Co$, which is why the direct sum is asserted over $\QQ$ and only with an index integrally.
$A$ is primitive in $S_\Co$ and contains $H$, so $\rank_\ZZ A\in\{1,2\}$; rank $1$ forces $A = \ZZ H$, and rank $2$ occurs exactly when $\sdp\subseteq S_\Co$, in which case $[S_\Co:\sdp\oplus B]$ is a power of $2$ and equals $1$ for the candidate of @prop:coble-cover-marking.
:::

::: {.proof}

In a hyperbolic basis $a,b$ of $U(2)$ write $H = pa+qb$; since $H^2 = 4$ forces $4pq = 4$, one has $(p,q) = (1,1)$ or $(-1,-1)$ and $H = \pm(a+b)$, and replacing $(a,b)$ by $(-a,-b)$ gives $H = a+b$.
For an isotropic $a' = \lambda a+\mu b$ one has $(a')^2 = 4\lambda\mu = 0$ and $a'\cdot H = 2(\lambda+\mu)$, so $a'\cdot H = 2$ forces $\lambda\mu = 0$ and $\lambda+\mu = 1$, that is $(\lambda,\mu) = (1,0)$ or $(0,1)$: exactly two solutions, $a$ and $b$, with sum $H$.
Two involutions commute exactly when each preserves the other's eigenspaces, so $\psi(S_\Co) = S_\Co$. For $x\in S_\Co$ both $x+\psi x$ and $x-\psi x$ then lie in $S_\Co$, the first fixed by $\psi$ and the second negated by it, so they lie in $A$ and in $B$; hence $2S_\Co\subseteq A\oplus B$, and the index divides $2^{11}$.
Over $\QQ$ the $(\pm1)$-eigenspaces of $\psi$ meet $S_\Co\otimes\QQ$ in $A_\QQ$ and $B_\QQ$, which therefore span it; no integral splitting is claimed, and none follows — the same argument applied to $I_\Co$ on $\lkt$ would give $\lkt = S_\Co\oplus T_\Co$, which is false, the index there being $2^{11}$.
$A$ is primitive in $S_\Co$: if $nx\in A$ with $x\in S_\Co$ and $n\neq0$, then $x\in\sdp$ because $\sdp$ is primitive in $\lkt$, and so $x\in A$. It contains $H$, which is primitive in $S_\Co$ since $H/2\notin S_\Co$; a primitive rank-one sublattice of $S_\Co$ containing a primitive vector is its span, so rank $1$ gives $A = \ZZ H$. If $\sdp\subseteq S_\Co$ then $B = \sdp^{\perp S_\Co}$, and $\det\sdp\cdot\det B = [S_\Co:\sdp\oplus B]^2\det S_\Co$; for the candidate the three values are $-4$, $-512$ and $2048$, giving index $1$.
:::

::: {.remark title="The authored tuple is geometric; this is the abstract reading"}
The conditions of the tuple are conditions on a surface: $I_{\mathrm{dP}}$ is an involution of the K3 cover, not merely an isometry of $\lkt$ (@prop:coble-cover-marking is where the lattice candidate is built, and it says so). The proposition above is about the *abstract* reading — lattice data only — which is strictly weaker: a lattice involution need not be the action of any automorphism, and for the candidate of @prop:coble-cover-marking it is not (@cor:no-del-pezzo-involution-coble-cover). The two readings are kept apart here on purpose; nothing below replaces the geometric condition by the lattice one.
:::

::: {.remark title="What the abstract conditions do and do not determine"}
Read as a list of *lattice* conditions — a reading strictly weaker than the authored geometric one, as the remark above records — the five bullets paraphrase to: the invariant lattice is a primitive $\sdp\cong U(2)$ in $L_{K3}$, it contains $H$, and $\psi$ commutes with $I_\Co$. The fifth bullet's condition on the product is commutation again (@prop:product-of-involutions), and the fourth constrains the chamber rather than $\psi$. That is a paraphrase for the abstract reading and not a replacement for the authored five, which remain the obligation.
No authored condition relates $\sdp$ to $\alpha$: of the five bullets, three mention $I_{\mathrm{dP}}$ and two mention $\alpha$, and none mentions both (the authored list is quoted in @sec-labeled-lattice-data).
So the abstract conditions leave the placement open: they do not fix the rank of $A = S_\Co\cap\sdp$, which the proposition leaves at $1$ or $2$, nor the index of $A\oplus B$ in $S_\Co$, which is a power of $2$ in general.
Once the rank is $2$, however, the placement is forced — the next remark shows that inside $S_\Co$ there is exactly one primitive $U(2)$ containing $H$ — so the whole of the freedom left by the abstract conditions lies in the case $A = \ZZ H$, or in a slot that is not nested inside $S_\Co$ at all; and for the forced rank-two placement the index of $A\oplus B$ is $1$.
The case $A = \ZZ H$ is not excluded by the abstract conditions, and it is realised as lattice data: @prop:rank-one-slot exhibits a vector $b\in\lkt$ with $b^2 = 0$ and $b\cdot H = 2$, orthogonal to $H^{\perp S_\Co}$, whose involution commutes with $I_\Co$ and fixes $H$. What it does not supply is the automorphism, and @prop:no-rank-one-automorphism shows that none exists: the involution reverses the authored root.
What a decision would require is the del Pezzo involution itself on the Coble cover, that is, a marking in which $I_\Co$ and an involution with invariant lattice $\sdp$ are realized on one surface. [@AEGS25, def:involutions] defines $I_{\mathrm{dP}}$ on $L_{K3}$ together with the Enriques and Nikulin involutions, so its $\sdp = \Delta(U)$ is described relative to the Enriques structure; [@DK13, §3] supplies the Coble side, $M_X = S_\Co$ with its ten classes and $N_X = T_\Co$, and carries no del Pezzo involution. Neither source relates $\sdp$ to $S_\Co$ on one surface, and the tuple conjoins data from the two: the missing datum is exactly that relation.
The embedding problem this remark used to leave open is now answered in both of its cases rather than posed: the primitive $U(2)$-sublattices of $L_{K3}$ containing $H$ and nested with $S_\Co$ are classified by @prop:del-pezzo-placement for the one case and by @prop:rank-one-slot for the other, and neither carries an automorphism — the rank-two candidate by @cor:no-del-pezzo-involution-coble-cover, the rank-one slot by @prop:no-rank-one-automorphism, which reverses the authored root. The chamber condition — $h_\Co$ nef, $H$ nef and big in $\mcc$ — and the effectivity of $\alpha$ are properties of a realization, and there is no realization for them to be imposed on.
:::

::: {.remark title="The rank-two placement is unique"}
For a candidate with $\sdp\subseteq S_\Co$ the classes to list are the isotropic $a\in S_\Co$ with $a\cdot H = 2$, and inside $S_\Co$ there are exactly two, $f^*F_1$ and $f^*F_2$.
That suffices because every primitive $U(2)$ inside $S_\Co$ containing $H$ contains one of them: by @prop:del-pezzo-placement its hyperbolic basis sums to $H$, so both generators lie in $S_\Co$ and pair $2$ against $H$; the enumerated set is $\{f^*F_1,f^*F_2\}$; these are the two members of one pair, $H - f^*F_1 = f^*F_2$, so containing one gives both, hence $\langle f^*F_1,f^*F_2\rangle\subseteq N'$.
Equal rank alone does not conclude: $\langle f^*F_1,f^*F_2\rangle$ is primitive in $S_\Co$ — its complement $N$ has determinant $-512$ against the determinants $-4$ and $2^{11}$ of the summand and of $S_\Co$, so the decomposition $S_\Co = \langle f^*F_1,f^*F_2\rangle\perp N$ has index $1$ by @prop:coble-cover-marking — so $S_\Co/\langle f^*F_1,f^*F_2\rangle$ is torsion-free, $N'/\langle f^*F_1,f^*F_2\rangle$ is a torsion-free subgroup of it, and being finite of equal rank it is trivial.
Hence a del Pezzo slot lying in $S_\Co$ is forced to be $\langle f^*F_1,f^*F_2\rangle$, and @cor:no-del-pezzo-involution-coble-cover covers the rank-two case entirely.
The argument is a bijection onto a *definite* fibre, which is what makes the enumeration exhaustive rather than bounded. The map $a\mapsto y\definedas 2a-H$ carries the solutions onto the $y\in H^{\perp}\cap S_\Co$ with $y^2 = -4$ and $y\equiv H \pmod{2S_\Co}$: indeed $(2a-H)^2 = 4a^2-4a\cdot H+H^2 = -4$ when $a^2 = 0$ and $a\cdot H = 2$, and conversely for such a $y$ one has $(y+H)^2 = y^2+H^2 = 0$ and $(y+H)\cdot H = H^2 = 4$, so $a = (y+H)/2$ is isotropic and pairs $2$ against $H$. The complement $H^{\perp}\cap S_\Co$ is negative definite because $H^2 = 4>0$, so its norm-$(-4)$ fibre is finite and the owner's fibre operation returns all of it: $242$ elements, of which exactly the two congruent to $H$ modulo $2S_\Co$ give solutions (`computations/reports/coble_del_pezzo_placement.py`).
What this does not decide is the case $A = \ZZ H$, where the slot meets $S_\Co$ only in $\langle H\rangle$; that case is @prop:rank-one-slot, which constructs the slot as lattice data, and @prop:no-rank-one-automorphism, which shows that no automorphism of a Coble cover induces it.
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
Take $\tau = \sum_ic_ie_i$ with $c_i\in\set{0,1}$, in the basis $e_0,e_1$ of the first $U(2)$, $e_2,e_3$ of the second, and $e_4,\ldots,e_{10}$ the $(-2)$-generators. Two cases cover every class of odd value. If $c_i = 1$ for some $i\le3$, say $c_0 = 1$, then $\tfrac12\tau\cdot e_1 = c_0 = 1$, so $\tfrac12\tau+p e_1$ has square $\tfrac14\tau^2+2p$, which is $-1$ for $p = -\tfrac12\bigl(1+\tfrac14\tau^2\bigr)\in\bZ$ because $\tfrac14\tau^2$ is odd; and $(c_1,e_0)$, $(c_2,e_3)$, $(c_3,e_2)$ do the same for the other three coordinates. If $c_0 = c_1 = c_2 = c_3 = 0$ then $\tfrac14\tau^2 = -\tfrac12k$, where $k$ is the number of $j$ with $c_{4+j} = 1$, and that is odd exactly for $k = 2$ and $k = 6$: for $k = 2$ the square is already $-1$, and for $k = 6$ one has $\tfrac12\tau\cdot(e_0+e_1+e_j) = 0$ and $(e_0+e_1+e_j)^2 = 2$ for any $j$ with $c_{4+j} = 0$, so $\tfrac12\tau+e_0+e_1+e_j$ has square $-3+2 = -1$. So every class of odd value contains a vector of square $-1$. Since $\gamma_\Co$ is an anti-isometry, $q_{T_\Co}\bigl(\gamma_\Co(\overline{H/2})\bigr) = -q_{S_\Co}(\overline{H/2}) = -\tfrac14H^2 = -1$, which is odd, so the class the gluing presents is one of the $496$ — and this holds for every anti-isometry, which is what the argument needs, since $\gamma_\Co$ is not determined by anything this book constructs. Both the census and a witness in each class are at the owner, with the case each witness falls under (`computations/reports/coble_rank_one_placement.py`).
(3) $t\perp S_\Co$ because $t\in T_\Co\otimes\bQ = (S_\Co\otimes\bQ)^{\perp}$, so $b\in(S_\Co\perp T_\Co)^{\#}$, with class $(\overline{H/2},\bar t)$ in the gluing subgroup; that subgroup is the graph of $\gamma_\Co$, so $b$ lies in the overlattice it cuts out, which is $\lkt$ (@cor:lifting-unimodular). There $b^2 = \tfrac14H^2+t^2 = 1-1 = 0$, $b\cdot H = \tfrac12H^2 = 2$, and $b\perp H^{\perp S_\Co}$ because both summands are.
(4) Put $J(x)\definedas (x\cdot H)b+(x\cdot b)H-2(x\cdot b)b-x$; the Gram matrix of $H,b$ in that basis is $\begin{pmatrix}4&2\\2&0\end{pmatrix}$ with inverse $\begin{pmatrix}0&\tfrac12\\\tfrac12&-1\end{pmatrix}$, so $J$ is twice the projection onto $\langle H,b\rangle_{\bQ}$ minus the identity, and it is an integral combination of $H$, $b$ and $x$ for $x\in\lkt$. Hence $J$ is an isometry of $\lkt$ with $J^2 = \id$; it fixes $H$ and $b$ and negates the orthogonal complement of $\langle H,b\rangle$, so its $(+1)$-eigenspace is $\langle H,b\rangle_{\bQ}\cap\lkt$, which is $\langle H,b\rangle$: if $mH+nb = 2y$ with $y\in\lkt$ then $2m+n = (mH+nb)\cdot e_9$ is even, so $n$ is even, and then $mH = 2y-nb$ forces $m$ even because $H$ is primitive in $\lkt$. The Gram matrix has determinant $-4$ and is even, so $\langle H,b\rangle\cong U(2) = \sdp$; and $S_\Co\cap\langle H,b\rangle = \ZZ H$, since $(b+mH)\cdot H = 2+4m\neq0$ for every $m$. For commutation, $I_\Co$ is $+\id$ on $S_\Co$ and $-\id$ on $T_\Co$, so $I_\Co(t) = -t$ and $I_\Co(b) = \tfrac12H-t = H-b$, which preserves $\langle H,b\rangle$, and an involution is determined by its $(+1)$-eigenspace. The coinvariant lattice $\langle H,b\rangle^{\perp\lkt}$ is even of rank $20$ and signature $(2,18)$, and its discriminant form is that of $U(2)$ up to sign — of order $4$, with integral values — so it is $2$-elementary with $a = 2$ and $\delta = 0$; $T_{\mathrm{dP}} = \Delta^-(U)\perp U\perp E_8^2\cong U(2)\perp U\perp E_8^2$ has the same invariants, so the two are isometric by @thm:two-elementary-classification. An isometry $\sdp\iso\langle H,b\rangle$ then extends to an isometry of $\lkt$: after fixing any isometry of the two complements, the remaining mismatch is an element of $\Orth\bigl(A_{\langle H,b\rangle^{\perp}}\bigr)$, which @thm:two-elementary-surjectivity realises by an isometry of $\langle H,b\rangle^{\perp}$, and the compatible pair extends by @cor:lifting-unimodular. So $J$ is conjugate to $I_{\mathrm{dP}}$ in $\Orth(\lkt)$, and its orbit is that of [@AEGS25]'s involution. Finally, a symplectic involution fixes the holomorphic $2$-form, whose real and imaginary parts span a positive definite $2$-plane inside the $(+1)$-eigenspace, and $U(2)$ has signature $(1,1)$, which contains no positive definite $2$-plane.
:::

::: {.proposition #prop:no-rank-one-automorphism title="A rank-one del Pezzo slot is induced by no automorphism"}

Let $\widetilde X$ be a projective K3 surface over $\CC$, let $\iota$ be a nonsymplectic involution of it with invariant lattice $S \definedas H^2(\widetilde X,\bZ)^{\iota}$, and let $\iota'$ be an involution commuting with $\iota$ whose invariant lattice $S'$ is isometric to $U(2)$.
Let $H\in S\cap S'$ with $H^2 = 4$, suppose $\rk(S\cap S') = 1$, and let $\alpha\in S$ be effective with $\alpha^2 = -2$ and $H\cdot\alpha = 0$.
Then $\iota'(\alpha) = -\alpha$, and no automorphism of $\widetilde X$ induces $\iota'$.
Of the del Pezzo involution only $S'\cong U(2)$ is used, and of $H$ only $H^2 = 4$ and $H\cdot\alpha = 0$: no marking, no coordinate expression of $H$, and no identification between the direct-projective construction and any model.
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

::: {.proposition #prop:root-pairs-evenly title="The root of the double cover pairs evenly with the invariant lattice"}

Let $\psi\colon\wX\to\wV$ be a double cover with $\wX$ a smooth K3 and $\wV$ a terminal Coble surface of K3 type with $n = 1$, branched along $C\in\abs{-2K_{\wV}}$; let $\iota_\Co$ be the deck involution, $E\subset\wX$ the fixed curve, and suppose $\psi^*C = 2E$ and $S_\Co = \psi^*\Pic(\wV)$ as in @prop:coble-invariant-lattice.
Then:
1. $\deg\psi = 2$ and $\psi_*[E] = [C]$ give $C^2 = C\cdot\psi_*E = \psi^*C\cdot E = 2E^2$, so $E^2 = \tfrac12C^2 = 2K_{\wV}^2$, which is $-2$ when $K_{\wV}^2 = -1$;
2. the class of the fixed curve is $\alpha\definedas[E] = \tfrac12\psi^*C = -\psi^*K_{\wV}$: half of the lattice class $\psi^*C$, a lattice class itself because $\OO_{\wV}(C) = \OO_{\wV}(-2K_{\wV})$ is even in $\Pic(\wV)$;
3. for $F\in\Pic(\wV)$ one has $\alpha\cdot\psi^*F = C\cdot F = -2(K_{\wV}\cdot F)$, hence $\alpha\cdot S_\Co\subseteq2\bZ$;
4. the divisibility of $\alpha$ in $S_\Co$ is $2$ for $\wV = \Bl_{10}\PP^2$, while separately $\alpha/2\notin S_\Co$. These are different statements and neither implies the other: primitivity follows from $(\alpha/2)^2 = \tfrac14\alpha^2 = -\tfrac12\notin\bZ$ with $S_\Co$ even, divisibility from the values $2(K_{\wV}\cdot F)$ whose generating ideal is $2\bZ$ because $K_{\wV}\cdot E_i = 1$; and the generator of $\generators{2}$ is primitive with divisibility $2$, which is the book's own warning (@lem:divisibilityAlwaysTwoTco).
:::

::: {.proof}

(1) is the projection formula for $E\to C$, which is an isomorphism because $C$ is the branch divisor.
(2) $K_{\wX} = \psi^*(K_{\wV}+\mcl)$ for $\OO_{\wV}(C) = \mcl^{\otimes2}$ (@rmk:k3-double-cover-construction), and $\psi_*K_{\wX} = (K_{\wV}+\mcl)\oplus K_{\wV}$, so $h^0(K_{\wV}+\mcl) = h^0(K_{\wX})-h^0(K_{\wV}) = 1-0$; a line bundle with a nonzero section whose pullback is trivial is trivial, so $\mcl = \OO(-K_{\wV})$ and $C = -2K_{\wV}$, whence $\alpha = \tfrac12\psi^*C = -\psi^*K_{\wV}$.
(3) $\alpha\cdot\psi^*F = \tfrac12\psi^*C\cdot\psi^*F = \tfrac12\cdot2(C\cdot F)$, by $\deg\psi = 2$.
(4) $\alpha/2\notin S_\Co$ because $S_\Co$ is even and $(\alpha/2)^2 = -\tfrac12$; and the pairings in (3) are $2(K_{\wV}\cdot F)$, whose gcd is $2$ on $\Bl_{10}\PP^2$ since $K_{\wV}\cdot E_i = 1$.
:::

::: {.remark #rmk:parity-scope title="Which hypotheses of the parity are verified, and what a resolution changes"}

@prop:coble-invariant-lattice asks for $n = 1$, terminality of $\wV$, and a fixed locus that is a single smooth rational curve — the last is what makes $\chi(\mathrm{Fix}) = 2$ in its Lefschetz count, and it is not implied by the other two.
For the classical model of the construction, $\wV = \Bl_{10}\PP^2$ at the ten nodes of an irreducible sextic and $C$ its proper transform, all three hold: terminality is smoothness of that blowup, rationality of $C$ is @lem:rational_sextic_ten_nodes (ten $A_1$ points exactly), and the transform is smooth there while $\mathrm{Fix} = E$ is the curve itself. So in that case the equality $S_\Co = \psi^*\Pic(\wV)$, and with it the parity, is proved and not assumed.
A *resolved* nodal member is different and the equality can fail. If $\wX$ has a node $q$ and $\widehat X\to\wX$ is its minimal resolution with exceptional curve $D$, then $D^2 = -2$ and $D\cdot\psi^*\Pic(\wV) = 0$ because $D$ is contracted, and $D$ is $\iota_\Co$-invariant whenever $\iota_\Co$ preserves the two branches at $q$; then the invariant lattice of $\widehat X$ contains $\psi^*\Pic(\wV)\perp\ZZ D$, of rank $12$, so it is strictly larger than $\psi^*\Pic(\wV)$ and @prop:coble-invariant-lattice's equality says nothing about it.
The parity survives for the two classes a nodal cover naturally carries, and the computation is immediate in each case: for $\alpha = [D]$ the pairings are $0$ against $\psi^*\Pic(\wV)$ and $-2$ against $D$; for $\alpha$ the proper transform $\tfrac12\psi^*C-\mu D$ of the fixed curve, with $\mu$ the multiplicity of $E$ at $q$, they are $C\cdot F$ against $\psi^*F$ and $2\mu$ against $D$. Both are even. What is *not* established is the parity for an arbitrary effective $\iota_\Co$-invariant class of square $-2$ and degree $0$ against $H$: the tuple names such a class and does not identify it with either of these, and on a resolved surface the identification is an extra step.
:::

::: {.proposition #prop:rank-two-slot-boundary title="The rank-two slot: the lattice reduction, and the vanishing in both constructions"}

In the notation of @prop:no-rank-one-automorphism let $\rk(S\cap S') = 2$.
Then $S\cap S' = S'$, so $S'\subseteq S$; taking isotropic generators $a_1,a_2$ of $S'\cong U(2)$ with $a_1\cdot a_2 = 2$, one has $H = \pm(a_1+a_2)$, and $\alpha = p(a_1-a_2)+\beta$ with $\beta\perp S'$ and $p\in\bQ$ satisfies:
1. $\beta\in S\otimes\bQ\cap H^{\perp}$, which is negative definite, so $\beta^2\le0$; and $\beta^2 = -2+4p^2$, so $p^2\le\tfrac12$; since $\alpha\cdot a_1 = -2p\in\bZ$, this leaves $\alpha\cdot a_1\in\set{-1,0,1}$.
2. $\iota'(\alpha) = -\alpha$ exactly when $\alpha\cdot a_1 = 0$, and in that case no automorphism of $\widetilde X$ induces $\iota'$, by the effectivity argument of @prop:no-rank-one-automorphism.
3. That vanishing holds in the marking of @prop:coble-cover-marking, where $S' = \langle f^*F_1,f^*F_2\rangle$ by the uniqueness proved for @prop:del-pezzo-placement and $\alpha\cdot f^*F_1 = \alpha\cdot f^*F_2 = 0$ is computed at the owner (`computations/reports/coble_del_pezzo_placement.py`); there the rank-two slot is induced by no automorphism either.
4. For the direct-projective construction the vanishing follows from the parity $\alpha\cdot S_\Co\subseteq2\bZ$, which turns $\alpha\cdot a_1 = -2p$ into $p\in\bZ$ and then, with $p^2\le\tfrac12$, into $p = 0$: so $\alpha\perp S'$ and the slot is induced by no automorphism. That parity is proved when the quotient is a smooth Coble surface with $\alpha$ the fixed curve (@prop:root-pairs-evenly) and, for a resolved nodal member, for the two classes such a cover carries; it is a *hypothesis* for an arbitrary effective invariant $(-2)$-class of degree $0$ against $H$, and the tuple names the class without identifying it (@rmk:parity-scope).
:::

::: {.proof}

$\rk(S\cap S') = 2 = \rk S'$ and $S\cap S'$ is saturated in $S'$, so the two coincide and $S' = \langle a_1,a_2\rangle$ with $a_i$ isotropic and $a_1\cdot a_2 = 2$. Writing $H = ma_1+na_2$ gives $H^2 = 4mn = 4$, so $(m,n) = \pm(1,1)$.
Decompose $\alpha$ over $\bQ$ as $\alpha = (pa_1+qa_2)+\beta$ with $\beta\perp S'$; then $\alpha\cdot H = 2(p+q) = 0$, so $q = -p$ and $\alpha_A = p(a_1-a_2)$, whose square is $-4p^2$; the cross terms with $\beta$ vanish, so $\beta^2 = \alpha^2+4p^2 = -2+4p^2$.
$\beta$ lies in $S\otimes\bQ$ and is orthogonal to $H$, so $\beta^2\le0$ by (the proof of) @prop:no-rank-one-automorphism, giving $p^2\le\tfrac12$; and $\alpha\cdot a_1 = -2p$ is an integer because both classes lie in the lattice, leaving $\alpha\cdot a_1\in\set{-1,0,1}$.
Since $\iota'$ is $\id$ on $S'$ and $-\id$ on $S'^{\perp}$, $\iota'(\alpha) = p(a_1-a_2)-\beta$, which equals $-\alpha$ exactly when $p = 0$, that is exactly when $\alpha\cdot a_1 = 0$; the effectivity argument then applies verbatim.
Parts 3 and 4 are the two ways the vanishing is known: part 3 in the marking of @prop:coble-cover-marking by the complete enumeration there, part 4 in the direct-projective construction by the parity of @prop:root-pairs-evenly, under the hypotheses that proposition and @rmk:parity-scope record. Where either applies the slot reverses $\alpha$ and no automorphism induces it.
The signature $(1,1)$ of $S'$ does *not* shorten this, although it looks as if it should: one might expect the invariant Kähler class to force $H$ to be ample. It does not, because the positive cone of a $(1,1)$ form is $2$-dimensional and an invariant nef class can lie on the edge of $\mathcal K_X\cap(S'\otimes\bR)$; in $U(2)$ itself, $H+e_0$ and $H+2e_0$ are independent classes of positive square while $H-e_0$ is isotropic, so the invariant positive classes are not a single ray. The vanishing $\alpha\cdot a_1 = 0$ is therefore a genuine geometric obstruction and not a consequence of the signature.
:::

::: {.remark #rmk:a21-premises title="What the negative answer uses, premise by premise, and which of it is marking-free"}

The tuple is the authored one of @sec-labeled-lattice-data, unchanged: $I_\Co$ and $I_{\mathrm{dP}}$ commuting nonsymplectic involutions of the K3 cover, $H^2 = 4$ fixed by both, $\alpha$ of square $-2$ with $H\cdot\alpha = 0$ fixed by $I_\Co$, and a chamber in which $\alpha$ is effective and $H$ is nef and big.
In the direct-projective construction those classes are $H = \pi_{\mathrm{dP}}^*\OO(1,1)$ and the effective root, with $H^2 = 4$ and $H\cdot\alpha = 0$; the identification of $H$ with the class of @prop:coble-cover-marking is *not* made in this section and is not used below.
What the rank-one result needs, with its source:
(i) $X$ is a projective K3 and $I_\Co$ is nonsymplectic: the authored setting. Nonsymplecticity is used once, to give $S = H^2(X,\bZ)^{I_\Co}$ signature $(1,\cdot)$, hence $H^{\perp S}$ negative definite — no Coble model is needed for that.
(ii) $I_{\mathrm{dP}}$ commutes with $I_\Co$ — the first bullet — hence preserves $S$, and $S_\Co\cap\sdp$ is the fixed lattice of $\iota' = I_{\mathrm{dP}}^*$ in $S$, saturated in $S$.
(iii) $S_{\mathrm{dP}}\cong U(2)$: the del Pezzo label, [@AEGS25, def:involutions] with the eigenspaces checked at the owner. It is a statement about the *label*, not a computation from the bullets or from the direct-cover datum: the tuple names $I_{\mathrm{dP}}$, AEGS's involution has that invariant lattice, and no source here computes the invariant lattice of an involution of a concrete Coble cover. If a construction produced one of del Pezzo type with a larger invariant lattice — as the resolution of a nodal cover does, the exceptional class being invariant — the tuple would not be of AEGS's type, and the rank split below, which uses $\rk S' = 2$, would not apply.
(iv) $H^2 = 4$ and $H\in S_{\mathrm{dP}}$ — the second bullet — so $H$ is a positive vector of $S$; and $H$ is primitive in $S$ because $S$ is even.
(v) $\alpha\in S$ with $\alpha\cdot H = 0$: the third bullet, which makes $\alpha$ $I_\Co$-invariant with $H\cdot\alpha = 0$.
(vi) $\alpha$ is effective: the fourth bullet. Hence $\alpha\cdot A_0>0$ against an ample class, and an automorphism would carry it to an effective class of degree $-\alpha\cdot A_0<0$.
(vii) For the rank-two half, the dictionary of the construction: $\psi\colon\wX\to\wV$ is the double cover branched along $C = \psi(E)$ with $\psi^*C = 2E$, $\wX$ a smooth K3, so $C = -2K_{\wV}$ and $\alpha = [E] = -\psi^*K_{\wV}$; and $S_\Co = \psi^*\Pic(\wV)$, which is @prop:coble-invariant-lattice and needs its hypotheses — $n = 1$, terminality of $\wV$, and a fixed locus that is one smooth rational curve. They hold for the classical model, $\wV = \Bl_{10}\PP^2$ with $C$ the proper transform of the ten-nodal sextic, rational by @lem:rational_sextic_ten_nodes; they do not hold automatically for a resolved nodal member, where the invariant lattice gains the exceptional class.
(viii) The parity $\alpha\cdot S_\Co\subseteq2\bZ$ itself, in rank two: proved for the smooth quotient with $\alpha$ the fixed curve (@prop:root-pairs-evenly) and for the two classes a resolved nodal cover carries (@rmk:parity-scope); for an arbitrary effective $\iota_\Co$-invariant class of square $-2$ and degree $0$ against $H$ it is a hypothesis, because the tuple names the class without identifying it.
So in the rank-one case — $\rk(S_\Co\cap\sdp) = 1$ — the conclusion holds for the authored tuple as it stands, with no correspondence: @prop:no-rank-one-automorphism, whose proof uses (i), (ii), (iv), (v) and (vi) and neither (iii)'s sharp form beyond $\rk S' = 2$, nor (vii), nor (viii).
In the rank-two case the lattice alone gives only $\alpha\cdot a_1\in\set{-1,0,1}$ (@prop:rank-two-slot-boundary, part 1). The vanishing then needs (vii) and (viii): with $\alpha$ pairing evenly with $S_\Co$, the equality $\alpha\cdot a_1 = -2p$ becomes $p\in\bZ$ and $p^2\le\tfrac12$ gives $p = 0$. That is proved where (vii) holds and $\alpha$ is the fixed curve, and it is what a resolved nodal member or a differently named root leaves open; the marking computes the same vanishing and is a cross-check, not a substitute for (vii).
Where the coordinate class $H = 6e_0-2\sum_{i\le8}e_i-e_9-e_{10}$ *is* used, it is used in that marking and says so: @prop:coble-cover-marking, @prop:rank-one-slot, @prop:del-pezzo-placement and the owner computation of the rank-two pairings. None of those is a premise of the rank-one conclusion, which never names a coordinate of $H$.
What a correspondence would have to be, and is not produced here: a marking of the direct-projective surface carrying $\pi_{\mathrm{dP}}^*\OO(1,1)$ and the effective root to the classes of @prop:coble-cover-marking, together with the involutions. The numerical coincidences — $H^2 = 4$ on both sides, $L^2 = 2 = h^2$, $\mathfrak C^2 = -4$, $h\cdot\mathfrak C = 0$ — are recorded as consistent with it and do not supply it.
The two formal steps are checked in Lean 4 with Mathlib in `formalization/coble-enriques/EffectiveReversal.lean`: `slot_reverses_root` (the eigenvalue argument of the rank-one proof), `not_preserves_effectivity_of_reversal` (the positivity argument) and their composite `no_automorphism_reverses_root`, together with `rank_two_narrowing`, the arithmetic of the rank-two reduction. No `sorry`; axioms `propext`, `Classical.choice`, `Quot.sound` only. The geometric premises above enter as explicit hypotheses, since the surface theory that supplies them is not part of the file.
:::

::: {.remark #rmk:rank-one-geometry title="Where the Hodge condition sits, why the ample strengthening is empty, and the answer to A21"}
*The Hodge condition, located.* $J$ is a Hodge isometry of a member exactly when $J\omega$ spans $\omega$; as $J$ is an involution the scalar is $\pm1$, and $+1$ is impossible because the real and imaginary parts of $\omega$ span a positive definite $2$-plane while the $(+1)$-eigenspace $U(2)$ has signature $(1,1)$. So the condition is $\omega\perp t$, equivalently $\omega\perp 2t$, which is the statement that the $(-4)$-class $2t$ is algebraic. In the notation of [@DK13, (3.2)] the periods orthogonal to a vector $\delta\in N_{-2d}$ form the Heegner divisor $H_{-2d}$ of the period domain $\bD(N)$, and here $N = \langle2\rangle\oplus E(2) = T_\Co$ and $2d = 4$: so the members whose cover admits $J$ as a Hodge isometry are the Coble covers whose period lies on $H_{-4}$. That divisor is nonempty, since $(2t)^{\perp T_\Co}$ has rank $10$ and signature $(2,8)$ (`computations/reports/coble_rank_one_placement.py`) so its own period domain is nonempty, and it is proper, since a generic period is not orthogonal to $2t$. It is a divisor of the family and not merely of the period domain by [@DK13, Prop. 3.2], which identifies $\mathcal M_{Co}$ with an open subset of $\bD(N)/O(N)$ through the Torelli theorem of Piatetskii-Shapiro and Shafarevich, together with @prop:coble-invariant-lattice for the lattice $N = T_\Co$; the two inputs are exactly those two, and neither is replaced by the signature computation.
*Why this does not decide the tuple, and what does.* The Torelli criterion of @sec-k3-automorphisms asks for a Hodge isometry preserving the ample cone, so on the Heegner divisor the realization question would be a chamber question. @prop:no-rank-one-automorphism answers it before either condition is reached: $\iota'$ reverses the effective class $\alpha$, so no chamber can be preserved, on the divisor or off it, for every member at once. In the rank-two case the same reversal is what the marking records (@cor:no-del-pezzo-involution-coble-cover), while there it needs the vanishing $\alpha\cdot a_1 = 0$ that @prop:rank-two-slot-boundary isolates; so the rank-one answer is unconditional and the rank-two answer is the marking's.
*The ample strengthening is empty, and is kept apart from the tuple.* Replacing the fourth bullet's nef and big $H$ by an ample one does not produce a smaller hypothesis under which the tuple holds: with $H$ ample and $\alpha$ effective, nonzero and of degree $0$ against $H$, the third and fourth bullets are already contradictory, by the same positivity that the proposition uses. The hypothesis stays nef and big throughout, and no ample subcase is claimed as, or substituted for, the conclusion.
:::

::: {.remark title="The rank-one case: the formulation, and the one input the gluing carries"}
When $\sdp$ is not contained in $S_\Co$, @prop:del-pezzo-placement gives $A = S_\Co\cap\sdp = \ZZ H$, and the same bijection formulates the question in $L_{K3}$ instead of $S_\Co$: an isotropic $b\in L_{K3}$ with $b\cdot H = 2$ corresponds to $y = 2b-H\in H^{\perp}\cap L_{K3}$ of square $-4$ with $y\equiv H \pmod{2L_{K3}}$, and the slot meets $S_\Co$ only in $\langle H\rangle$ exactly when $y\notin S_\Co\otimes\QQ$.
@prop:rank-one-slot answers it in the affirmative, and the two arithmetic conditions on $b$ suffice for that: the involution with $(+1)$-eigenspace $\langle H,b\rangle$ is integral on $\lkt$ by the projection formula, and its restriction to $S_\Co$ is integral because the values of $x\cdot H$ on $S_\Co$ generate $2\bZ$. What those conditions do not give is an eigensplitting of $S_\Co$ — that sum has index $2$ — and an earlier version of this remark read the failure of the splitting as a failure of integrality, which it is not. The datum that is genuinely missing is a different one, and it is the gluing: $b$ is not a vector of $S_\Co\oplus T_\Co$ at all, so what has to be exhibited is a vector of $T_\Co^{\#}$ of square $-1$ in the class $\gamma_\Co(\overline{H/2})$, and @prop:rank-one-slot shows that every class the gluing can present contains one.
What is in hand at the level of the gluing: the two discriminant forms are anti-isometric, $A_{S_\Co}\cong A_{T_\Co}(-1)$, verified at the pin by `A_{S_\Co}.is_anti_isometric(A_{T_\Co})` returning `True` (`computations/reports/coble_gluing_discriminants.py`), so by @thm:nikulin-gluing the pair does admit a unimodular overlattice with the full graph gluing and the stated index $2^{11}$ is consistent with it. The explicit arrow was recorded here as blocked at an earlier pin, and that block is now resolved: maintained `sage-extensions` at main `6ad7a5ea396da6e758ee28f3dea10a35baee0266` supplies `A_{S_\Co}.isometry_to(A_{T_\Co}(-1))`, and its published test `tests/forms/test_the_coble_anti_isometry.sage` runs on these inputs — the Coble lattices $S_\Co = \latI_{1,10}(2)$ and $T_\Co = B(2)$ — and checks the exact source and target types, the quadratic values on generators and on pair sums, all pairwise bilinear values, the sign of the twist, and the inverse and composition laws. The refusals recorded earlier were made at pin `c546077d`, where `then` is guarded by object identity, `normal_form` is recomputed per call so that the two normal forms are distinct objects, and `isometry_to` exists at the lattice level only; they are superseded, not explained away.
The arrow is still not needed for what is proved here, and the two reasons differ. @prop:rank-one-slot quantifies over $\gamma_\Co$: it shows that every class of $A_{T_\Co}$ of odd value contains a vector of square $-1$, which is why the slot exists whatever the anti-isometry is. @prop:no-rank-one-automorphism uses no gluing at all, since $\alpha\in S_\Co$ and $2t = 2b-H\in T_\Co$, so what it reverses it reverses for every admissible $b$. An explicit $\gamma_\Co$ would therefore serve the writing down of the overlattice, which is a construction this book does not need for either conclusion; it is not a step in an argument still owing something.
The formulation is also not one the provider's fibre machinery reaches directly: $H^{\perp}\cap\lkt$ has signature $(2,19)$, since $\lkt$ has signature $(3,19)$ and $H^2 = 4>0$, so it is indefinite, and the exhaustive enumeration that made the rank-two computation a certificate does not apply to it; and testing $y\notin S_\Co\otimes\QQ$ needs $S_\Co$ placed inside $\lkt$, that is the gluing in machine-readable form, which the book does not carry. Neither point bears on @prop:rank-one-slot, which decides the question on the discriminant form of $T_\Co$ — finite of order $2^{11}$ — and never enters the indefinite fibre.
On top of the embedding question the authored tuple asks for automorphisms. In rank one the obligation is answered: @prop:no-rank-one-automorphism shows that no automorphism of the surface induces the rank-one slot, because the slot reverses the authored root $\alpha$, and that argument uses no class of the marking. In rank two it is answered under the parity on which @prop:rank-two-slot-boundary's part 4 depends, which @prop:root-pairs-evenly proves for the smooth quotient with the fixed-curve root. Where either applies, the chamber condition and the effectivity of $\alpha$ are not conditions still to be met — the effectivity of $\alpha$ is what forbids the tuple.
:::


## Which of the arithmetic groups is $\Gamma_\Co$ {#sec-gamma-co-comparison}

Several different groups have been called $\Gamma_\Co$ in this book, and a further family of them appears in the arithmetic-group problem of the research report (@prob:group-identification).
The name is fixed here once: $\Gamma_\Co$ is the stable subgroup displayed below, and the other candidates receive their own symbols, $\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma^\theta_\Co$, and are compared with it in @prop:gamma-co-in-heegner-group and @prop:gamma-co-in-theta-centralizer.
The reason to fix it first is that an orbit count made for one of these groups is not a count for another.
The group of the moduli problem is the stable one,
$$
\Gamma_\Co \definedas \Orth^+(T_\Co)^* = \Orth^+(T_\Co)\intersect\discriminantkernel{T_\Co},
$$
and it is the same object as the simultaneous discriminant-and-spinor kernel of @def:lattice-spinor-kernels: $\Orth^+(L)\definedas\Theta_\bR(L)$ there, and $\widetilde\Orth^+(L)$ is defined as the pullback of $\widetilde\Orth(L) = \ker\rho_L$ along the inclusion $\Orth^+(L)\injects\Orth(L)$, so that
$$
\widetilde\Orth^+(T_\Co) = \Orth^+(T_\Co)\intersect\ker\rho_{T_\Co} = \Gamma_\Co
.
$$
That is a substitution and carries no arithmetic content.
What is not definitional is how the two further descriptions of the group stand to this one.

The Heegner side describes $\Gamma_\Co$ from the line $\ZZ\delta$: @def:gamma-co-en takes the image in $\Orth(T_\Co)$ of those elements of $\gent$ that preserve the line, where $\gent$ is the degree-$2$ group whose discriminant description @prop:gamma-en-two-gluing gives.
The Coble side describes it from the sign involution: by @prop:theta-co-exists the eigenlattices of $\theta_\Co$ are $T_\Co$ and $S_\Co$, so an isometry of $\lkt$ commuting with $\theta_\Co$ is a compatible pair of isometries of the two eigenspaces, and cutting by a polarization class cuts one factor.
In both cases the resulting group contains $\Gamma_\Co$ and exceeds it by a subgroup of the finite group $\Orth(A_{T_\Co}, q_{T_\Co})$, which by @prop:coble-discriminant-group is $\Orth(A_{E_{10}(2)}, q_{E_{10}(2)})$ and has order $46\,998\,591\,897\,600$.
The two propositions below compute that subgroup and the index in each case.

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
That the order is *equal* to $\abs{W(E_8)}$ is the sharper assertion of @thm:coble-heegner-finite-orbits (1), which asserts an exact order rather than an inequality; the bound proved here does not need it, and no orbit length enters this proposition.

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
The component condition has to be imposed and not assumed: the intersection can contain isometries of $\lkt$ acting on either positive or negative definite part of its restriction to $T_\Co$, and only those acting in $\Orth^+(T_\Co)$ are wanted, exactly as in @prop:gamma-co-in-heegner-group.
Then $\Gamma_\Co\iscontainedin\Gamma^\theta_\Co$, $\Gamma_\Co = \ker\bigl(\Gamma^\theta_\Co\too\Orth(A_{T_\Co},q_{T_\Co})\bigr)$, and $[\Gamma^\theta_\Co : \Gamma_\Co] = \abs{\rho_{T_\Co}(\Gamma^\theta_\Co)}$.
:::

::: {.proof}

By @prop:theta-co-exists an isometry of $\lkt$ commutes with $\theta_\Co$ exactly when it preserves both eigenspaces, and by @thm:automorphism-lifting-criterion a pair $(g_S, g_T)\in\Orth(S_\Co)\times\Orth(T_\Co)$ that preserves both extends over the overlattice $\lkt$ of $S_\Co\oplus T_\Co$ exactly when $\bar g_T\circ\gamma_\Co = \gamma_\Co\circ\bar g_S$.
So $Z_{\Orth(\lkt)}(\theta_\Co)$ is the set of such pairs.

For $\varphi\in\Gamma_\Co$ the pair $(\id_{S_\Co}, \varphi)$ satisfies the condition, since $\bar\varphi = \id$; and $\id_{S_\Co}$ fixes $\tilde h_\Co$.
So $\varphi$ lies in $\Gamma^\theta_\Co$, which is the inclusion.
An element of $\Gamma^\theta_\Co$ is an isometry of $T_\Co$, so its discriminant image is defined without a choice of lift, and the kernel is $\Orth^+(T_\Co)\intersect\ker\rho_{T_\Co} = \Gamma_\Co$; the index is the order of the image.
:::

::: {.remark title="Definitions, gluing, and what is still geometry"}

Three kinds of statement are in play, and only the last two carry arithmetic content.

*Definitions.* $\Gamma_\Co = \Orth^+(T_\Co)^* = \widetilde\Orth^+(T_\Co)$ above, $\Gamma^{\mathrm{Hdg}}_\Co$ of @prop:gamma-co-in-heegner-group, $\Gamma^\theta_\Co$ of @prop:gamma-co-in-theta-centralizer, and the four groups of @prob:group-identification are defined.
No equality among them is a definition, and the identity $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$ is the only one settled by unpacking notation.

*Discriminant gluing.* The two propositions above are of this kind: they express each of $\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma^\theta_\Co$ as an extension of $\Gamma_\Co$ by an explicit subgroup of the finite group $\Orth(A_{T_\Co},q_{T_\Co})$, so each equals $\Gamma_\Co$ exactly when its finite subgroup is trivial.
Strictness of either inclusion is therefore a question about that subgroup and not about the lattices, and neither is asserted here.
The consequence for an orbit count is quantitative: a $\Gamma^{\mathrm{Hdg}}_\Co$-orbit of primitive isotropic vectors splits into at most $[\Gamma^{\mathrm{Hdg}}_\Co : \Gamma_\Co]$ orbits under $\Gamma_\Co$, so a count made for one of the two groups is not a count for the other, and the factor relating them is finite.
In the same way the congruence group of @prob:group-identification is $\rho_{T_\Co}^{-1}(P)$ with $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)}) \leq \Orth(A_{T_\En}, q_{T_\En}) \iso \Orth(A^0, q_{T_\Co}|_{A^0})$, made into a subgroup of $\Orth(A_{T_\Co},q_{T_\Co})$ by the identity on $\ZZ\tfrac12\zeta$.
Nontriviality of $P$ alone does not separate that preimage from $\Gamma_\Co$: a preimage of a subgroup is larger than the kernel only if some element of the subgroup is realised by an integral isometry.
Here one is, and it is proposed as an explicit witness whose required properties are then verified rather than asserted.
Let $(e', f')$ be the basis of the $U(2)$ summand of $T_\Co$, with $e'^2 = f'^2 = 0$ and $e'\cdot f' = 2$, and let $\sigma$ be the transposition of $e'$ and $f'$ fixing $\ZZ\zeta$ and $E_8(2)$, which is the reflection $s_{e'-f'}$ in a vector of square $-4$.
What the argument needs of $\sigma$ is that it lies in $\Orth^+(T_\Co) = \Theta_\bR(T_\Co)$ by @def:spinor-norm, that it moves the discriminant, and that its discriminant action preserves the three blocks of $A_{T_\Co} = \ZZ\tfrac12\zeta\perp A_{U(2)}\perp A_{E_8(2)}$ and acts on the $U(2)$ block by the transposition; these are verified through the owner's operations, where $\sigma$ is built by `Lattices.reflection`, its membership in `O_plus` and in `stable_orthogonal_group` is decided by those groups, the classes are the owner's `discriminant_class` of `primitive_dual`, and the action is `discriminant_morphism`, with $q([\tfrac12 e']) = q([\tfrac12 f']) = 0$, $q([\tfrac12\zeta]) = \tfrac12$, $b([\tfrac12 e'], [\tfrac12 f']) = \tfrac12$ and $\abs{A_{T_\Co}} = \abs{\det T_\Co} = 2048$ read off the same objects (`computations/reports/coble_congruence_witness.py`).
Since a transposition of the two isotropic classes of $A_{U(2)}$ is an isometry of that block, $\rho(\sigma)\in\Orth(q_{U(2)})\subseteq P$; that inclusion is the block argument just stated and is not a computation of $P$ itself, and what the owner builds on the congruence side is the preimage of the cyclic subgroup $\generators{\rho(\sigma)}$, not of $P$ (`computations/reports/coble_stabilizer_generators.py`).
So $\rho(\sigma)\in P$ is nontrivial, $\sigma\notin\Gamma_\Co$, and $\Gamma^{\mathrm{cong}}_{\Co,2}$ strictly contains $\Gamma_\Co$.
What this does and does not settle: the four-group identification of @prob:group-identification cannot be an equality with the stable group $\Gamma_\Co$, only an equality among overgroups of it, and for the congruence group the overgroup is strictly larger while for the Heegner and $\theta$-groups no witness is proposed and strictness stays open.

*Torelli, monodromy and labeled embeddings.* Two of the four are not of that kind.
The direct and geometric groups are images of centralizers in $\Orth(\lkt)$ of the labeled Coble datum, so comparing either with a Heegner group requires an isometry of $\lkt$ carrying the Enriques-labeled structure $(S_\En, T_\En, \ZZ\delta, h)$ of @prop:gamma-en-two-gluing to the Coble-labeled one $(S_\Co, T_\Co, \tilde h_\Co)$ of @prop:gamma-co-in-theta-centralizer; that is the labeled rigidity of @prob:coble-rigidity, not a computation in $T_\Co$.
And the geometric group is the monodromy of a moduli stack, so it agrees with an arithmetic group only through the direct period theorem and the direct monodromy theorem, @prob:B24 and @prob:B25.
Nothing in the two propositions above bears on either, and replacing $\Gamma_\Co$ by $\Gamma^{\mathrm{Hdg}}_\Co$ in an orbit count is exactly the change of group that the comparison forbids.
:::
