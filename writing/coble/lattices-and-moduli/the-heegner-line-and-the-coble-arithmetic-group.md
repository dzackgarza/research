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
So the position is this. The two ranks of @prop:del-pezzo-placement are settled for slots whose invariant lattice is $\sdp\cong U(2)$: rank one by @prop:no-rank-one-automorphism, rank two by @prop:rank-two-slot-boundary with the vanishing computed in the marking of @prop:coble-cover-marking. That is not the slot the direct-projective construction produces. There the operators are the ones of @prop:local-operators, the lifted $I_{\mathrm{dP}}$ has invariant rank $2+k\ge3$ for a Coble member (@prop:del-pezzo-type-on-the-resolution), and it fixes the authored root rather than reversing it, so no effectivity obstruction arises (@rmk:a21-open). The authored tuple is therefore **open** for that construction, and what is settled about it is its local shape: the two involutions, their symplectic characters, their fixed loci after the resolution, and the rank of the del Pezzo invariant lattice. The lattice computations of @prop:rank-one-slot, @prop:del-pezzo-placement and @cor:no-del-pezzo-involution-coble-cover remain statements in the marking of @prop:coble-cover-marking.
:::
:::
Of the involutions, $I_\Co = -\theta_\Co$ exists without gluing data: @prop:theta-co-exists gives $\theta_\Co$ as $+1$ on $T_\Co$ and $-1$ on $S_\Co$, and the pair $(\id_{S_\Co}, -\id)$ used to define $-\theta_\Co$ preserves every isotropic gluing subgroup because both discriminant forms are $2$-elementary; its action on $H$ is that of $+\id_{S_\Co}$, an isometry of $S_\Co\perp T_\Co$ which the owner verifies fixes $H$. The del Pezzo involution *is* lattice data, contrary to what an earlier version of this paragraph said: [@AEGS25, def:involutions] gives $I_{\mathrm{dP}}(v,u,u',e,e') = (-v,u',u,-e,-e')$ on $U^3\oplus E_8^2$, with eigenspaces $S_{\mathrm{dP}} = \Delta(U) = U(2)$ and $T_{\mathrm{dP}} = U\oplus\Delta^-(U)\oplus E_8^2$, and the owner confirms that the four stated eigenspaces act by $+1$ and $-1$ as stated and that AEGS's Enriques pair is exactly the $S_\En$, $T_\En$ used here, with $[\lkt:S_\En\oplus T_\En] = \abs{A_{S_\En}} = 2^{10}$ (`computations/reports/coble_aegs_involutions.py`). What the *labeling* asks — that this $I_{\mathrm{dP}}$ is the del Pezzo involution of the Coble K3 cover, commuting with $I_\Co$ and fixing $H$ — is not left open by a missing marking: the marking is forced by the source construction itself, and with it the candidate whose invariant lattice is the span of the two isotropic summands is excluded as an automorphism (@cor:no-del-pezzo-involution-coble-cover). That was one case of two; the other, the rank-one slot, is excluded as well (@prop:no-rank-one-automorphism), so for slots with $S_{\mathrm{dP}}\cong\sdp$ — that is, for the del Pezzo label — both cases are excluded, and each of them reverses the authored root. The slot the direct-projective construction itself produces is not of that type: its invariant lattice has rank $k+2\ge3$ and it fixes the root, which puts it outside both cases (@prop:tuple-of-the-construction, @rmk:a21-open). An earlier version of this paragraph located the difficulty in placing $M_X$ inside $U^3\oplus E_8^2$; [@DK13] names the classes $e_0 = f^*H$ and $e_i = f^*E_i$ explicitly, and those are classes in the basis this book already uses, so no placement had to be invented. The chamber's remaining condition is the nefness of $h_\Co$ set out above, nef-cone geometry rather than a lattice computation. Nothing above promotes the modelled lattice data to the retained geometric labels.
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

Three levels have to be kept apart. $\phi$ exists as an integral isometry of $L_{K3}$, commutes with $I_\Co$ and fixes $H$ — that is @prop:coble-cover-marking — and it is not the action of an automorphism of $X$ — that is the corollary. Whether *any* admissible slot is geometric is a further question: for slots with invariant lattice $\sdp$ it is answered negatively (@prop:no-rank-one-automorphism, @prop:rank-two-slot-boundary), and for the slot the direct-projective construction actually produces the invariant lattice is larger and the question is open (@rmk:a21-open).
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
The embedding problem this remark used to leave open is now answered in both of its cases rather than posed: the primitive $U(2)$-sublattices of $L_{K3}$ containing $H$ and nested with $S_\Co$ are classified by @prop:del-pezzo-placement for the one case and by @prop:rank-one-slot for the other, and neither carries an automorphism — the rank-two candidate by @cor:no-del-pezzo-involution-coble-cover, the rank-one slot by @prop:no-rank-one-automorphism, which reverses the authored root. The chamber condition — $h_\Co$ nef, $H$ nef and big in $\mcc$ — and the effectivity of $\alpha$ are properties of a realization, and of the two cases above none supplies one. The tuple the direct-projective construction produces does supply one — $H = \pi^*\OO(1,1)$ is nef and big and $\alpha$ is the class of an exceptional curve (@prop:tuple-of-the-construction) — and there the open question is the one of @rmk:a21-open, not the chamber.
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

::: {.proposition #prop:local-operators title="The two involutions of the nodal cover, their fixed loci and their symplectic characters"}

Let $X^\sharp = \set{z^2 = f(x,y)}$ over the $\tau$-fixed point $p$ of $Y$, with $f$ having a nondegenerate quadratic part there, and let
$$\iota_{\mathrm{dP}}(x,y,z) = (x,y,-z),\qquad \iota_\Co(x,y,z) = (-x,-y,-z).$$
Then:
1. the two commute, and $\iota_\Co\iota_{\mathrm{dP}}(x,y,z) = (-x,-y,z)$;
2. all three act on the holomorphic $2$-form $\omega = \frac{dx\wedge dy}{2z}$ by $\iota_{\mathrm{dP}}^*\omega = -\omega$, $\iota_\Co^*\omega = -\omega$ and $(\iota_\Co\iota_{\mathrm{dP}})^*\omega = +\omega$: both involutions are nonsymplectic and their product is symplectic, as the authored bullets require;
3. $\mathrm{Fix}(\iota_{\mathrm{dP}}) = \set{z = 0}\cap X^\sharp$, the branch curve, nodal at $p$;
4. $\mathrm{Fix}(\iota_\Co)$ is contained in the singular points of $X^\sharp$: if $\iota_\Co(x,y,z) = (x,y,z)$ then $x = y = 0$ and $z = -z$, so $z = 0$ and $f(0,0) = 0$; and $f$ is $\tau$-invariant, so its terms of odd order at the $\tau$-fixed point $p$ vanish and the vanishing order there is even — the point is singular, of type $A_1$ when the quadratic part is nondegenerate. So $\iota_\Co$ has no isolated fixed point, which is what its nonsymplecticity requires: at an isolated fixed point the differential would be $-\id$ on the tangent space and $\omega$ would be preserved.
:::

::: {.proof}

(1) is substitution. (2) is the residue form: on $X^\sharp$ away from $z = 0$ one has $\omega = \frac{dx\wedge dy}{2z}$, and $\iota_{\mathrm{dP}}^*(dx\wedge dy) = dx\wedge dy$ with $\iota_{\mathrm{dP}}^*(2z) = -2z$, while $\iota_\Co^*(dx\wedge dy) = (-dx)\wedge(-dy) = dx\wedge dy$ with $\iota_\Co^*(2z) = -2z$; the product fixes $z$ and acts by $(-dx)\wedge(-dy)$ on the $x,y$-form, so it scales $\omega$ by $+1$.
(3) $z = -z$ gives $z = 0$, and then $f(x,y) = z^2 = 0$.
(4) $x = -x$ and $y = -y$ give $x = y = 0$; then $z = -z$ gives $z = 0$ and $f(0,0) = 0$. Since $f(-x,-y) = f(x,y)$, every monomial of odd total degree has coefficient $0$, so the lowest-order part at the origin is even and $f$ vanishes there to order at least $2$; with nondegenerate quadratic part that is an $A_1$ point. For the last sentence: at an isolated fixed point $d\iota$ has no eigenvalue $1$, so being an involution it equals $-\id$ and $\iota^*\omega = \det(d\iota)\,\omega = +\omega$ there, against $\iota^*\omega = -\omega$.
:::

::: {.remark #rmk:product-eight-points title="The product involution, and what it checks about the local model"}

The product $\rho = \iota_\Co\iota_{\mathrm{dP}}$ is symplectic (part 2 of @prop:local-operators), so a symplectic involution of a K3 and hence fixed at isolated points only, and at exactly eight of them: $\rho(x,y,z) = (-x,-y,z)$, so its fixed points are the points over the four $\tau$-fixed points of $Y$, where $z^2 = f$. Over a fixed point at which $f\ne0$ there are two, $z = \pm\sqrt f$; over one at which $f = 0$ the single point is the node, which the resolution replaces by the two points $[1:\pm i:0]$ of @prop:del-pezzo-type-on-the-resolution, part 2. So the count is $2\cdot4 = 8$ in the fixed-point-free case of $I_\Co$ and $2\cdot3+2 = 8$ with one node, and by the formula of @prop:tuple-of-the-construction $\rk S_\rho = \tfrac12(8+20) = 14$. The local model therefore reproduces the global number, which is what a local computation of a global invariant should do; and $S_\Co\cap S_{\mathrm{dP}}\subseteq S_\rho$ because a class fixed by both involutions is fixed by their product, so the rank $3$ of the intersection sits inside a rank $14$ lattice as it must.
:::

::: {.proposition #prop:del-pezzo-type-on-the-resolution title="The invariant type of the lifted del Pezzo involution on the resolution"}

Let $\widehat X\to X^\sharp$ be the minimal resolution of the node at $p$, $D$ the exceptional $(-2)$-curve, and $\widehat\iota_{\mathrm{dP}}$, $\widehat\iota_\Co$ the lifts. Then:
1. $\widehat\iota_\Co$ acts trivially on the exceptional $\PP^2$ and hence fixes $D$ pointwise;
2. $\widehat\iota_{\mathrm{dP}}$ acts on that $\PP^2$ by $[X:Y:Z]\mapsto[X:Y:-Z]$, so it preserves the conic $D = \set{Z^2 = X^2+Y^2}$ and fixes on it exactly the two points $[1:\pm i:0]$, which are also where the proper transform of the branch curve meets $D$;
3. consequently $\mathrm{Fix}(\widehat\iota_{\mathrm{dP}})$ is the normalization of the branch curve: for $f$ with exactly $k$ nodes and otherwise smooth, the branch curve has arithmetic genus $9$ and geometric genus $9-k$, so $\chi(\mathrm{Fix}) = 2-2(9-k) = 2k-16$, and Lefschetz gives $\rk S_{\mathrm{dP}} = \tfrac12(22+(2k-16)-2) = 2+k$;
4. $S_{\mathrm{dP}}$ contains $\pi^*\Pic(Y)\perp\ZZ D_1\perp\cdots\perp\ZZ D_k$, of rank $2+k$: the pullbacks of $\Pic(Y) = \ZZ^2$ have Gram matrix $U(2)$, each $D_g$ is a $(-2)$-class because it is preserved by $\widehat\iota_{\mathrm{dP}}$, and $D_g\perp\pi^*\Pic(Y)$ and $D_g\perp D_{g'}$ for $g\ne g'$ because the resolution contracts them.
So the invariant type of the lifted $I_{\mathrm{dP}}$ is $U(2)\perp\langle-2\rangle^{\oplus k}$ up to a finite index, and *not* $U(2)$ whenever $k\neq0$. The finite index is settled at the one-node scope — $k=1$ with an ordinary node at a $\tau$-fixed point and the branch curve irreducible — by @prop:det-saturation-del-pezzo below (index $1$, i.e. equality of lattices there); it is properly not settled here for $k\ge2$.
:::

::: {.proof}

(1) and (2) are the substitution $(-x,-y,-z)$ and $(x,y,-z)$ in homogeneous coordinates on the exceptional $\PP^2$, whose point set is the conic $\set{Z^2 = X^2+Y^2}$; the fixed points of $[X:Y:Z]\mapsto[X:Y:-Z]$ on it satisfy $Z = 0$, that is $X^2+Y^2 = 0$, and the two branches of the nodal curve $\set{z = 0, f = 0}$ have exactly those tangent directions.
(3) the proper transform of the branch curve under the resolution of its node is its normalization, of geometric genus $9-k$; the two fixed points on $D$ are its two points over the node, so they are part of it and contribute nothing further.
(4) as stated, with the projection formula giving $(\pi^*F)\cdot(\pi^*G) = \deg\pi\,(F\cdot G) = 2(F\cdot G)$, which is $U(2)$ on the basis of $\Pic(\PP^1\times\PP^1)$.
:::

::: {.proposition #prop:tuple-of-the-construction title="The construction's own tuple satisfies the five authored bullets"}

Let $\pi\colon X^\sharp = \set{z^2 = f(x,y)}\to Y = \PP^1\times\PP^1$ be the double cover branched along $B = \set{f = 0}\in\abs{\OO_Y(4,4)}$, so that $K_{X^\sharp} = \pi^*(K_Y+\OO_Y(2,2)) = 0$, and let $\widehat X\to X^\sharp$ be the resolution of the $k$ nodes of $B$, all of them at $\tau$-fixed points. Put $H\definedas\pi^*\OO_Y(1,1)$, and let $\alpha\definedas[D_g]$ be the class of the exceptional curve over one of them. Then
1. $H^2 = 4$, and $H$ is fixed by both $I_\Co$ and $I_{\mathrm{dP}}$;
2. $\alpha^2 = -2$, $H\cdot\alpha = 0$, and $\alpha$ is fixed by $I_\Co$;
3. $H$ is nef and big, and $\alpha$ is the class of an effective curve;
4. both involutions are nonsymplectic and their product is symplectic;
5. $\rk S_{\mathrm{dP}} = k+2$ and $\rk S_\Co = k+10$.
So for $k\ge1$ the five bullets of @sec-labeled-lattice-data hold on $\widehat X$: the tuple of the direct-projective construction exists, and its quotient by $I_\Co$ is not Enriques.
:::

::: {.proof}

(1) $(\pi^*\OO(1,1))^2 = \deg\pi\,(\OO(1,1))^2 = 2\cdot2 = 4$. Both involutions satisfy $\pi\circ\iota = \iota'\circ\pi$, with $\iota' = \id_Y$ for $\iota_{\mathrm{dP}}$ and $\iota' = \tau$ for $\iota_\Co$; and $\tau$ acts by $[-1]$ on each factor, with $[-1]^*\OO(1) = \OO(1)$, so $\iota'^*\OO(1,1) = \OO(1,1)$ in both cases and $\widehat\iota^*H = \pi^*\iota'^*\OO(1,1) = H$, the resolution being equivariant.
(2) $D_g$ is a $(-2)$-curve and is fixed pointwise by $\widehat\iota_\Co$ (@prop:del-pezzo-type-on-the-resolution, part 1); and $H\cdot D_g = \OO(1,1)\cdot\pi_*D_g = 0$ because $\pi_*D_g = 0$, the curve lying in a fibre of the resolution.
(3) $\OO_Y(1,1)$ is very ample, the Segre embedding, hence nef; for a curve $C$ one has $H\cdot C = \OO(1,1)\cdot\pi_*C\ge0$, so $H$ is nef, and $H^2 = 4>0$ with $H$ nef makes $H$ big on a surface. $\alpha$ is the class of the curve $D_g$.
(4) @prop:local-operators, part 2, computes the two characters on $X^\sharp$; away from the nodes the resolution is an isomorphism and both involutions act on the exceptional curves, so the characters are unchanged.
(5) For a nonsymplectic involution of a K3 with fixed locus $F$, Lefschetz gives $\chi(F) = 2+\tr$. Decompose over $\QQ$, where the eigensplitting is available: $H^2(\widehat X,\QQ) = S_\QQ\oplus T_\QQ$ with $\id$ on $S$ and $-\id$ on $T$, so $\tr = \rk S-\rk T$ and, with $\rk S+\rk T = 22$, $\tr = 2\rk S-22$ and $\rk S = \tfrac12(\chi(F)+20)$. Only ranks enter here. The integral refinement $H^2(\widehat X,\ZZ) = S\oplus T$ is *not* asserted and is not used: $S\oplus T$ is a sublattice of finite index, which can be $2$ (@prop:rank-one-slot records the analogous index $2^{11}$ for $S_\Co\oplus T_\Co$ inside $\lkt$), and an index statement would have to be proved before it could be divided by. For $\widehat\iota_{\mathrm{dP}}$ the fixed locus is the normalization of $B$, of $\chi = 2k-16$ (@prop:del-pezzo-type-on-the-resolution, part 3), so $\rk S_{\mathrm{dP}} = k+2$. For $\widehat\iota_\Co$ it is the disjoint union of the $k$ exceptional curves: @prop:local-operators, part 4, puts every fixed point of $\iota_\Co$ at a singular point, and @prop:del-pezzo-type-on-the-resolution, part 1, makes the curve over each of them fixed pointwise. So $\chi(F) = 2k$ and $\rk S_\Co = k+10$. At $k = 0$ this last value is $10$, the rank of the invariant lattice of an Enriques involution of a K3, which is what $I_\Co$ is when its fixed locus is empty.
:::

::: {.proposition #prop:one-node-family title="The one-node construction is a smooth proper equivariant family carrying a relative polarization and an exceptional divisor"}

Let $B\subset\abs{\OO_Y(4,4)}^\tau$ be the set of $\tau$-invariant sections whose branch curve has exactly one node, at the $\tau$-fixed point $p$, and is otherwise smooth with nondegenerate quadratic part at $p$; it is open in the invariant linear system of @sec-invariant-system and nonempty, one nodal example being recorded at @sec-computational-record. Put $\mathcal L\definedas\OO_Y(2,2)$, a square root of $\OO_Y(4,4)$, and $\mathcal Y\definedas Y\times B$. Then:
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
The example of @sec-explicit-curve, with $x^2+xy+2y^2$ of discriminant $-7$ at $p$ and, as the Gröbner-basis verification at @sec-computational-record records, no other singular point, supplies $B\ne\varnothing$, and a line with its bad points finite is what makes any two members of $B$ reachable inside $B$, since a punctured projective line is connected. The smooth proper family of @prop:one-node-family then runs over any connected smooth curve of $B$, and @thm:one-node-transport applies to any two members of $B$, not only to pairs from a subfamily.
:::

::: {.theorem #thm:a21-labels title="The labels of any two tuples of the one-node direct-projective construction are conjugate"}

Let $\mathfrak L$, $\mathfrak L'$ be tuples of the direct projective construction arising from one-node members, in the sense of @prob:coble-rigidity. Then there is $\gamma\in\Orth(\lkt)$ carrying the involutions to the involutions, the degree-$4$ class to the degree-$4$ class, and the effective root to the effective root:
$$\gamma S_{\Co} = S'_{\Co},\qquad \gamma S_{\mathrm{dP}} = S'_{\mathrm{dP}},\qquad \gamma H = H',\qquad \gamma\alpha = \alpha'.$$
:::

::: {.proof}

By @prop:one-node-connected both parameter points lie in one connected $B$, so they are joined by a path; the family of @prop:one-node-family is smooth and proper over $B$ with $\mathcal H$ and $\mathcal D$ flat; @thm:one-node-transport applied to the path gives the conclusion.
:::

::: {.problem #prob:effective-cone-agreement title="Required theorem (chamber clause of labeled Coble rigidity)"}

For any two tuples of the direct projective construction arising from one-node members, with $\gamma$ the conjugating isometry of @thm:a21-labels, there are no effective classes of square $-2$ of the second member outside $\gamma\Delta$ that cut the transported chamber; equivalently, by @lem:face-at-H and @prop:chamber-conditional, the effective cones of the two members agree under $\gamma$.
:::

The condition is used exactly in @prop:chamber-conditional's form: outside it, @thm:a21-labels closes the labels, so this is the only ingredient kept out of the conclusion by hypothesis.
The tuple's chamber is the chamber containing the Kähler cone (@rmk:chamber-not-transported), so this is a statement about the effective cones of the members — a comparison of Picard lattices — and not one the family's cohomological transport can shortcut.

::: {.problem #prob:twist-identification title="Required theorem (the construction's involution pair is the reflection twist)"}

For one tuple of the direct projective construction arising from a one-node member, with the data of @prop:tuple-of-the-construction, the pair $(I_\Co, I_{\mathrm{dP}})$ is conjugate in $\Orth(\lkt)$ to the twist pair of @cons:reflection-twist, with $H$ mapping to a class of the same type and $\alpha$ to $\pm$(the twist's root).
:::

By @thm:a21-labels the tuple has a single conjugacy class, so one identification of one tuple with the twist suffices for all members. The twist's invariant lattice is computed integrally at @prop:coble-eigenspaces; the construction's involution's invariant lattice has rank $k+10$ (@prop:tuple-of-the-construction) with the containment and saturation cautions of @rmk:a21-open. No equality of lattice types is asserted anywhere here, and neither this problem nor @prob:effective-cone-agreement is a hypothesis used elsewhere.

::: {.remark #rmk:a21-resolution title="What remains of A21 after the labels"}

By @thm:a21-labels the three label clauses of A21 hold for the whole one-node locus of the construction — for every pair, not only for pairs of a subfamily. The fourth clause, the chamber, is a separate condition and is not implied: by @prop:chamber-conditional it holds exactly when no effective root of the second member outside the transported set cuts the transported chamber, and in particular whenever the two effective cones agree. So the full conclusion of @prob:coble-rigidity is settled within any connected subfamily over which the effective $(-2)$-classes agree, and the content that does not follow from the construction and its family is precisely that agreement — a statement about periods, not about the local system (@prob:effective-cone-agreement). Separately, and on the lattice side: the labels' type is the twist datum of @cons:reflection-twist (which @prop:coble-eigenspaces now computes integrally), and identifying the tuple's involution pair with that twist is the labelled-lattice identification recorded at @rmk:a21-open — also open, and also not a local-system statement (@prob:twist-identification). These are the two conditions of the original problem that remain, each named with its hypothesis.
:::

::: {.theorem #thm:one-node-transport title="What parallel transport gives: the lattice labels, not the chamber"}

The hypotheses are those of @prop:one-node-family and nothing else: $B$ smooth, $\widehat\pi\colon\widehat{\mathcal X}\to B$ smooth and proper with K3 fibres, $\mathcal H$ and $\mathcal D$ divisors flat over $B$ — no ampleness of $\mathcal H$, no projectivity of the total space beyond properness, and no hypothesis on cones is used. Let $\theta$ be a path in $B$ from $b$ to $b'$ — so the statement applies to any two points in one connected component — and $\psi_\theta\colon H^2(\widehat X_b,\ZZ)\iso H^2(\widehat X_{b'},\ZZ)$ the Gauss–Manin parallel transport. Then $\psi_\theta H_b = H_{b'}$, $\psi_\theta\alpha_b = \alpha_{b'}$, and $\psi_\theta$ carries $\widehat\iota_{\Co,b},\widehat\iota_{\mathrm{dP},b}$ to $\widehat\iota_{\Co,b'},\widehat\iota_{\mathrm{dP},b'}$; hence, after markings, an element $\gamma\in\Orth(\lkt)$ with
$$\gamma S_{\Co,b} = S_{\Co,b'},\qquad \gamma S_{\mathrm{dP},b} = S_{\mathrm{dP},b'},\qquad \gamma H_b = H_{b'},\qquad \gamma\alpha_b = \alpha_{b'}.$$
No statement about chambers is part of this conclusion. What the labels do determine, and where the chamber enters, is @lem:face-at-H and @rmk:chamber-not-transported.
:::

::: {.proof}

Parallel transport is an isometry of the fibres of $R^2\widehat\pi_*\ZZ$ and is compatible with flat sections, which $c_1(\mathcal H)$ and $[\mathcal D]$ are (@prop:one-node-family, part 4); that gives the first two. The involutions act on the total space, so transport intertwines them; a $(+1)$-eigenspace is characterized by its involution, so the fixed lattices are carried to fixed lattices. Choosing markings and composing gives $\gamma$ as in the proof of the earlier version of this statement.
:::

::: {.lemma #lem:face-at-H title="The curves contracted by $\pi$ are the ray in the cone of curves, and its annihilator is the smallest face of the nef cone through $H$"}

In the situation of @prop:one-node-family, on every fibre:
1. $\alpha_b = \pi_b^*e$, where $e\subset\widehat Y = \Bl_pY$ is the exceptional curve;
2. the *curve* statement: $\overline{\mathrm{NE}}(\widehat X_b)\cap H_b^\perp = \RR_{\ge0}\alpha_b$, and the classes of the irreducible curves contracted by $\pi_b$ are exactly the positive multiples of $\alpha_b$;
3. the *dual* statement: the nef cone $\mathcal N_b = \overline{\mathrm{NE}}(\widehat X_b)^\vee$ has a unique face $F_b$ whose relative interior contains $H_b$, namely
$$F_b = \set{v\in\mathcal N_b : v\cdot\alpha_b = 0},$$
and $H_b\cdot\gamma>0$ for every curve class $\gamma$ outside the ray $\RR_{\ge0}\alpha_b$;
4. the *local chamber implication*: no wall other than $\alpha_b^\perp$ passes through $H_b$, and the component $\mathfrak c_b$ of $\mathcal C_b\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp$ that contains the Kähler cone has $H_b$ in its closure and lies on the side $x\cdot\alpha_b>0$. Whether the pair $(H_b,\alpha_b)$ pins $\mathfrak c_b$ among all components is a further question, answered below only under a hypothesis on the walls.
:::

::: {.proof}

(1) $\pi^{-1}(p)$ is the single node $\hat p$ of $X^\sharp_b$, the cover being ramified there, so the pullback of the maximal ideal of $p$ is invertible on $\widehat X_b$ and $\pi_b$ factors through $\widehat X_b\to\widehat Y = \Bl_pY$, the double cover branched along the proper transform $\widetilde B$. The preimage of $e$ is therefore $D_b$, and $D_b\to e$ is the double cover branched at $e\cap\widetilde B$, of degree $e\cdot\widetilde B = -2e^2 = 2$; being branched, $\pi_b^*e = D_b$, that is $\alpha_b = \pi_b^*e$. Consistently $(\pi_b^*e)^2 = 2e^2 = -2$, and $\alpha_b$ is primitive in $M$ with divisibility $2$, as the marking of @prop:coble-cover-marking records for its own $\alpha$.
(2) $H_b\cdot C = \OO(1,1)\cdot\pi_b(C)$ with $\OO(1,1)$ ample, so it vanishes exactly when $\pi_b(C)$ is a point, that is when $C$ is contracted by $\pi_b$. Since $\pi_b$ factors through the finite map $X^\sharp_b\to Y$, which contracts no curve, $C$ is contracted by the resolution $\widehat X_b\to X^\sharp_b$, whose only exceptional curve is $D_b$; so $[C]\in\QQ_{\ge0}\alpha_b$. Passing to the closure of the cone spanned by curve classes gives the same ray.
(3) Elementary convex duality: for a closed convex cone $K$ and $y\in K^\vee$, the set $F = \set{z\in K^\vee : \langle z,x\rangle = 0 \ \text{for all } x\in K \text{ with } \langle y,x\rangle = 0}$ is the smallest face of $K^\vee$ containing $y$, and $y$ lies in its relative interior. Taking $K = \overline{\mathrm{NE}}(\widehat X_b)$, whose dual is the nef cone, and using (2), the defining set is $\RR_{\ge0}\alpha_b$ and $F = F_b$ as displayed. For the last clause: $H_b$ is nef, so $H_b\cdot\gamma\ge0$ for every curve class, and it vanishes only on the ray by (2).
(4) Let $\delta\in\Delta_b$ be an effective class of square $-2$ with $H_b\cdot\delta = 0$. Writing $\delta = \sum a_iC_i$ over irreducible curves with $a_i>0$ gives $0 = \sum a_i(C_i\cdot H_b)$ with every term non-negative, so each $C_i$ is orthogonal to $H_b$ and hence, by (2), equal to $D_b$; then $\delta = m\alpha_b$ and $-2 = -2m^2$ forces $m = 1$. So $\delta = \alpha_b$ and no wall other than $\alpha_b^\perp$ passes through $H_b$.
For the rest, only what the comparison needs is asserted. $H_b$ is nef, so it lies in the closure of the Kähler cone, which is contained in $\mathcal C_b$ because a Kähler class has positive square; and every Kähler class is positive on $\alpha_b$, that being the class of an effective curve. So the component $\mathfrak c_b$ containing the Kähler cone has $H_b$ in its closure and is α-positive. What is *not* asserted is that no other component does: a $(-2)$-class $\delta$ with $H_b\cdot\delta\ne0$ still has its wall crossing every neighbourhood of $H_b$ if the walls accumulate there, which they can when the Picard lattice is indefinite of rank $\ge3$. Pinning $\mathfrak c_b$ by $(H_b,\alpha_b)$ therefore needs a hypothesis excluding such accumulation, and @prop:chamber-pinned states it rather than assuming it away.
:::

::: {.proposition #prop:chamber-pinned title="When the labels do pin the chamber, and what that costs"}

In the situation of @lem:face-at-H, suppose in addition that for every effective class $\delta\in\Delta_b$ with $\delta\ne\pm\alpha_b$ the walls do not accumulate at $H_b$: that is, there is a neighbourhood $U$ of $H_b$ in $\mathcal C_b$ meeting no $\delta^\perp$ for those $\delta$. Then $\mathfrak c_b$ is the only component of $\mathcal C_b\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp$ whose closure contains $H_b$ and which is positive on $\alpha_b$.
:::

::: {.proof}

On $U$ the only wall is $\alpha_b^\perp$, so $U\setminus\alpha_b^\perp$ has exactly two components, one on each side; a component whose closure contains $H_b$ meets $U$, and if it meets only one side it is the corresponding one, and if its wall set includes only $\alpha^\perp$ on $U$ it is that side. Being positive on $\alpha_b$ selects the α-positive side, which is $\mathfrak c_b$ by @lem:face-at-H, part 4.
:::

::: {.remark #rmk:chamber-not-transported title="Which roots cut the chamber, and what the labels do and do not determine"}

*What a chamber is here, and which roots cut it.* For a K3 surface $X$ let $\mathcal C_X\subset H^2(X,\RR)$ be a component of $\{x^2>0\}$, and let $\Delta_X\subset\Pic(X)$ be the set of classes of square $-2$ that are effective. The Kähler cone is
$$\mathcal K_X = \set{x\in\mathcal C_X : x\cdot\delta>0\ \text{for every }\delta\in\Delta_X},$$
which is the standard description [@BHPV04]: it is a chamber of the decomposition of $\mathcal C_X$ by the hyperplanes $\delta^\perp$ with $\delta\in\Delta_X$, and its walls are the *effective algebraic* roots.

*The lattice alone does not give $\Delta_X$.* The arrangement of all classes of square $-2$ in $H^2(X,\ZZ)$ is determined by the lattice, but the algebraic ones — and the sign of each — are read off the period. In particular, orthogonality to an ample class does not by itself make an integral class of type $(1,1)$: if $\delta^2 = -2$ and $\delta\perp\omega$ for an ample $\omega$, then $\delta^{1,1}\perp\omega$ lies in the primitive $(1,1)$ part, where the intersection form is negative definite, while $\delta^{2,0}+\delta^{0,2}$ has positive square, and the identity $-2 = (\delta^{1,1})^2+(\delta^{2,0}+\delta^{0,2})^2$ forces neither summand to vanish. So the walls are not the walls of the full lattice arrangement, and which of them bound $\mathcal K_X$ depends on the member. The fourth bullet's $\mathfrak c$ is this chamber, the one containing the Kähler cone — the reading taken here, and the one under which $H$ nef and big and $\alpha$ effective are conditions on the member rather than on $\mathfrak c$.

*What the labels do pin, and what they do not.* By @lem:face-at-H the only wall through $H_b$ is $\alpha_b^\perp$, and the component containing the Kähler cone has $H_b$ in its closure and is positive on $\alpha_b$; that component is a chamber of the arrangement cut by the effective roots of that member, and it is the chamber of the tuple. If the walls do not accumulate at $H_b$ it is moreover the only such component (@prop:chamber-pinned), so that in that case $(H_b,\alpha_b)$ pin it; where they may accumulate, they do not, and the pinning is a hypothesis rather than a theorem. What they do not fix is the arrangement itself: if $\Delta_{\widehat X_{b'}}$ is larger than the transported $\Delta_{\widehat X_b}$, the transported chamber is a union of chambers of $b'$ and not a chamber, and the conjugacy then fails on the chamber even though it holds on the labels. So the chamber clause of A21 turns on whether the effective roots agree, which is the next statement; the Gauss–Manin connection does not preserve $H^{2,0}$, and that agreement is not something parallel transport supplies.
:::

::: {.proposition #prop:chamber-conditional title="The chamber clause holds exactly when the effective roots agree, which is what has to be checked"}

In the situation of @prop:one-node-family let $b,b'\in B$, let $\gamma$ be the isometry of @thm:one-node-transport, and let $\mathfrak c_b$ be the chamber of the tuple at $b$, that is the component of $\mathcal C_b\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp$ containing the Kähler cone. Then $\gamma\mathfrak c_b = \mathfrak c_{b'}$ if and only if no effective class $\delta$ of square $-2$ on $\widehat X_{b'}$ outside the transported set $\gamma\Delta_b$ cuts $\gamma\mathfrak c_b$; in particular the chamber clause holds whenever the transported effective roots agree with those of $b'$, and then the tuples are conjugate with $H$, $\alpha$, both involutions and the chamber.
:::

::: {.proof}

If no such $\delta$ cuts $\gamma\mathfrak c_b$, then $\gamma\mathfrak c_b$ is a component of $\mathcal C_{b'}\setminus\bigcup_{\delta\in\Delta_{b'}}\delta^\perp$; it contains $\gamma\mathcal K_b$, and the Kähler cone of $b'$ lies in it whenever — as is the case when no extra wall cuts — the two are not separated, whence $\gamma\mathfrak c_b$ is the component containing $\mathcal K_{b'}$, that is $\mathfrak c_{b'}$. Conversely if some $\delta\in\Delta_{b'}\setminus\gamma\Delta_b$ cuts $\gamma\mathfrak c_b$, then $\gamma\mathfrak c_b$ is not a component of the $b'$ arrangement and so is not $\mathfrak c_{b'}$.
The "in particular" is the case $\gamma\Delta_b = \Delta_{b'}$: the tuple comparison is then @thm:one-node-transport for the labels together with $\gamma\mathfrak c_b = \mathfrak c_{b'}$.
:::


::: {.corollary #cor:construction-monodromy title="The monodromy of the one-node construction lies in the stabilizer of its lattice labels"}

In the situation of @prop:one-node-family the monodromy representation of $R^2\widehat\pi_*\ZZ$ on $H^2(\widehat X_b,\ZZ)$ lands, after a marking, in the stabilizer in $\Orth(\lkt)$ of the quadruple $(S_\Co,S_{\mathrm{dP}},H,\alpha)$ — the isometries commuting with both involutions and fixing $H$ and $\alpha$. Nothing is claimed about chambers, by @rmk:chamber-not-transported.
:::

::: {.proof}

Monodromy is parallel transport along loops, which by @thm:one-node-transport preserves each of the four pieces.
:::

::: {.proposition #prop:det-saturation-del-pezzo title="The del Pezzo invariant lattice is the flat lattice, index one"}

For a one-node member as in @prop:del-pezzo-type-on-the-resolution — the resolved K3 $\widehat X_b$ of the double cover of $\widehat Y = \Bl_p(\PP^1\times\PP^1)$ branched along the smooth proper transform $\widetilde B$, with $e_b = \widehat\pi^*h_1$, $f_b = \widehat\pi^*h_2$ the ruling pullbacks and $D_b = \widehat\pi^*e$ the exceptional $(-2)$-curve —
$$S_{\mathrm{dP},b}=H^2(\widehat X_b,\ZZ)^{\widehat\iota_{\mathrm{dP}}=+1}
=\Lambda=\langle e_b,f_b,[D_b]\rangle\cong U(2)\perp\langle-2\rangle,\qquad \det S_{\mathrm{dP},b} = 8,$$
and the index-$2$ candidate $U\perp\langle-2\rangle$ (det $2$) of the corpus's earlier candidates does not occur. In particular every $I_{\mathrm{dP}}$-invariant class pairs evenly with each ruling class.
:::

::: {.proof}

*Context and hypotheses on which this depends: one node at a $\tau$-fixed point whose proper transform is smooth, so that $\widehat\pi$ is a double cover of a smooth rational surface branched along a smooth curve — the node condition of @lem:node-condition and the resolution of @prop:del-pezzo-type-on-the-resolution; a second one is the irreducibility of a one-nodal $\tau$-invariant curve of bidegree $(4,4)$ (recorded and proved as reported in `computations/reports/sm57_audit-one-node-m2.md`, `lem:irred`), which is what keeps every fibre-divisor of each ruling's pullback reduced.*

*Step 1 (index bound).* $S_{\mathrm{dP},b}$ is even and primitive in $L\definedas H^2(\widehat X_b,\ZZ)$. Since $\widehat\pi$ is finite flat of degree $2$, the transfer formula $\widehat\pi^*\widehat\pi_* = 1+\widehat\iota_{\mathrm{dP}}^*$ on $H^2(\widehat X_b,\ZZ)$ sends $x\in S_{\mathrm{dP},b}$ to $2x = \widehat\pi^*\widehat\pi_*x\in\Lambda$; hence $\Lambda\subseteq S_{\mathrm{dP},b}\subseteq\widehat\pi^*H^2(\widehat Y,\ZZ)=\Lambda\otimes\QQ$ rationally, equal ranks, and $[S_{\mathrm{dP},b}:\Lambda]\in\set{1,2}$ by $\det\Lambda=8$.

*Step 2 (what index $2$ would impose).* Suppose $[S_{\mathrm{dP},b}:\Lambda]=2$ with $S/S_0 = \mathbb Z/2$. Pick $z\notin\Lambda$, write $2z=ae+bf+cD$; integrality of $z^2=ab-\tfrac{c^2}2$ forces $c$ even; evenness forces $ab$ even. If both $a,b$ even then $z\in\Lambda$, contrary to choice. Hence exactly one of $e_b/2,f_b/2$ is integral in $S$, and in particular $e_b\in2L$ or $f_b\in2L$. (This enumeration is exactly the two even half-classes the maintained provider's census returns, `computations/reports/sdp_discriminant_referee.py` and its log at pin `c546077d`, with the index-4 case removed by the same arithmetic.)

*Step 3 (hypotheses: each fibre preimage is a reduced divisor).* For the fibration $\varphi=\phi_{|e_b|}\colon\widehat X_b\to\PP^1$ defined by $|e_b|$ (base-point free because $e_b=\widehat\pi^*h_1$ and $|\OO_Y(1,0)|$ is base-point free; each fibre class $[F_v]=e_b$), every fibre $F_v = \widehat\pi^{-1}(M)$ of a ruling line $M$ has all multiplicities $n_j=1$ in its component decomposition: $\widehat\pi$ is étale over the generic point of $M$ (branch points of the cover over $M$ sit in the finite set $\widetilde B\cap M$, and $M$ is not contained in $\widetilde B$ — with $B$ irreducible by the premise quoted above), so each component enters with multiplicity $1$.

*Lemma (the ruling classes are primitive in $L$).* Suppose $e_b = 2\eta$ with $\eta\in L$ (hence $\eta\in\mathrm{NS}$, since $e_b$ is type $(1,1)$). Then $\eta^2=0$, $\eta\cdot e_b=0$, $\eta\cdot f_b=1$. Since $(-\eta)\cdot f_b=-1<0$ and $f_b$ is nef, $h^0(-\eta)=0$; Riemann–Roch on the K3 then gives $h^0(\eta)\ge2$, so let $E\in|\eta|$ be effective. Each component of $E$ lies in a fibre of $\varphi$ (from $\eta\cdot e_b=0$ and $e_b$ nef), and grouping by fibre, $E=\sum_v E_v$ with disjoint supports; the component span of one fibre is negative semidefinite (Hodge index on $e_b^\perp/\mathbb R e_b$), so $[E_v]=q_v[F_v]$ in that span with $q_v\in\mathbb Q_{\ge0}$ (sign by effectivity). Comparing coefficients with Step 3's $n_j=1$, every $q_v\in\mathbb Z_{\ge0}$. But then
$$1=\eta\cdot f_b=\sum_v q_v\cdot(e_b\cdot f_b)=2\sum_v q_v,$$
an integer on the right but $1$ on the left: impossible. Hence $e_b$ is primitive in $L$, and the same argument with the rulings exchanged shows $f_b$ primitive.

*Conclusion.* By the steps, neither $e_b/2$ nor $f_b/2$ is integral in $L$, so Step 2's alternative is empty and $[S_{\mathrm{dP},b}:\Lambda]=1$. At $k=0$, $\Lambda=U(2)=\widehat\pi^*H^2(Y,\ZZ)$ retains its two summands and the same primitivity argument excludes the unimodular overlattice $U$ of step 2's family, deciding the earlier "$U(2)$ or $U$" binary in favour of $U(2)$.
:::

::: {.remark #rmk:a21-open title="What the original operators do to the A21 slot, and why it is open"}

*The root of the construction is an exceptional curve, and the slot fixes it.* By @prop:local-operators the fixed locus of $I_\Co$ on the cover is carried by the singular $\tau$-fixed points, and by @prop:del-pezzo-type-on-the-resolution each of them contributes an exceptional curve $D_g$ fixed pointwise after the resolution; there are no isolated fixed points, for the reason given there. The root of the construction is one of them: the exceptional curve over a singular $\tau$-fixed point, which is effective, of square $-2$ and of degree $0$ against $H$ because $\pi$ contracts it. Each $D_g$ is preserved by $\widehat\iota_{\mathrm{dP}}$ as well. Hence
$$\iota'(\alpha) = +\alpha,$$
and the effectivity argument that forbids $-\alpha$ says nothing here: it excludes a slot that reverses the root, and this slot fixes it.

*The del Pezzo label does not apply in the Coble case.* By @prop:del-pezzo-type-on-the-resolution the lifted invariant lattice has rank $2+k$ for $k$ nodes of the branch curve, containing $\pi^*\Pic(Y)\perp\ZZ D_1\perp\cdots\perp\ZZ D_k\cong U(2)\perp\langle-2\rangle^{\oplus k}$. The value $k = 0$ is the only one in which the invariant lattice is $U(2)$, and there $\mathrm{Fix}(I_\Co)$ is empty, so the quotient is an Enriques surface and not a Coble one. A parity argument does *not* close the case $k = 0$, and the reason is worth recording because it is the obvious way to try: a rank-$2$ even lattice containing $U(2)$ with finite index $i$ has determinant $-4/i^2$, which is integral for $i\in\set{1,2}$, and $i = 2$ gives $U$ itself — even, of determinant $-1$, an overlattice generated by $e/2$ and $f$. So at $k = 0$ the invariant lattice is $U(2)$ or $U$ and which of the two is not decided here. The same argument does settle the double plane, where $\pi^*\OO(1)$ generates $\langle2\rangle$ and an index-$2$ overlattice would have determinant $1/2$; it does not settle $U(2)$, and a determinant computation is not an identification. Every Coble member of the construction therefore has $k\ge1$ and $I_{\mathrm{dP}}$ of invariant rank at least $3$.

*What that does to the rank analysis.* The two invariant lattices meet in full rank. The lattice $\pi^*\Pic(Y)\perp\ZZ D_1\perp\cdots\perp\ZZ D_k$ lies in both: $\iota_{\mathrm{dP}}$ is the deck transformation, so it acts trivially on every pullback, and $\iota_\Co$ covers $\tau$ with $\tau^*\OO(a,b) = \OO(a,b)$ because $[-1]$ has degree $1$, so the pullbacks are invariant under it too; each $D_g$ is fixed pointwise by $\widehat\iota_\Co$ and preserved by $\widehat\iota_{\mathrm{dP}}$ (@prop:del-pezzo-type-on-the-resolution); and $D_g\cdot\pi^*c = c\cdot\pi_*D_g = 0$. That lattice has rank $k+2 = \rk S_{\mathrm{dP}}$ (@prop:tuple-of-the-construction), so
$$\rk(S_\Co\cap S_{\mathrm{dP}}) = k+2 = \rk S_{\mathrm{dP}}.$$
So the slot meets $S_\Co$ in full rank rather than in the rank $1$ or $2$ that @prop:no-rank-one-automorphism and @prop:rank-two-slot-boundary assume — those hypotheses fail for every Coble member, $k\ge1$ — and the two propositions do not describe this tuple at all. The intersection may still be a proper sublattice of $S_{\mathrm{dP}}$, since the containment above has finite index in it, and that index is the saturation question again.

*What is missing even for the type.* Containment with equal rank is not equality: $U(2)\perp\langle-2\rangle^{\oplus k}\subseteq S_{\mathrm{dP}}$ has the rank computed in @prop:del-pezzo-type-on-the-resolution, but the index may exceed $1$, and the saturation of that sublattice is not established here. The rank of $S_\Co$ is computed there — $k+10$ — but the containment of the pullback of the quotient's Picard group together with the exceptional classes is not shown to be saturated either, so neither invariant lattice is described exactly, at any $k$.
*The nefness, and the sections of $H$.* $H = \pi^*\OO_Y(1,1)$ with $\OO_Y(1,1)$ very ample is nef, and by $\pi_*\OO_{X^\sharp} = \OO_Y\oplus K_Y$ its space of sections is $H^0(\OO_Y(1,1))\oplus H^0(\OO_Y(1,1)\otimes K_Y) = 4\oplus0$, so $H$ is effective too. Effectivity of $H$ together with $H\cdot\alpha = 0$ and $\alpha$ effective is not a contradiction, and that is the precise sense in which the fourth bullet is satisfiable here while its ample strengthening is not: a nef class is orthogonal to the effective curves it contracts, and $\pi$ contracts $D_g$. Reading $H^0\ne0$ as a failure of nefness would be reading it backwards.

So the tuple of the construction exists (@prop:tuple-of-the-construction) and the A21 question — whether two such tuples are conjugate by an element of $\Orth(\lkt)$ preserving the labels, $H$, $\alpha$ and the chamber — is **open**. What obstructs the earlier routes is the slot, not the tuple: its lattice involution fixes the authored root rather than reversing it, its invariant type is not the one the earlier propositions analyse, and no marking of this surface by the classes of @prop:coble-cover-marking is produced. So an empty labelled set is not what A21's answer can be here, and the effectivity argument of @prop:no-rank-one-automorphism cannot be the instrument.
:::

::: {.proposition #prop:node-count-invariant title="The number of $\tau$-fixed nodes is an invariant of the tuple"}

Let $f,f'$ be $\tau$-invariant sections of $\OO_Y(4,4)$ whose branch curves have exactly $k$, respectively $k'$, ordinary nodes at $\tau$-fixed points and are otherwise smooth with nondegenerate quadratic part at those points, and let $\mathfrak L,\mathfrak L'$ be the tuples @prop:tuple-of-the-construction attaches to them. Then $\mathfrak L$ and $\mathfrak L'$ are conjugate in $\Orth(\lkt)$ only if $k = k'$. Both $k = 1$ and $k = 2$ occur.
:::

::: {.proof}

A conjugation preserving the labels carries $I_{\mathrm{dP}}$ to $I'_{\mathrm{dP}}$, and conjugate involutions have isometric invariant lattices, of ranks $k+2$ and $k'+2$ by @prop:tuple-of-the-construction; hence $k = k'$.

For the occurrence: the value of a $\tau$-invariant section at the $\tau$-fixed point $([1:0],[1:0])$ is the coefficient of $x_0^4y_0^4$, and correspondingly $x_0^4y_1^4$, $x_1^4y_0^4$, $x_1^4y_1^4$ at the other three fixed points. These four monomials are independent, and every other invariant monomial vanishes at all four points, so the conditions $f(p) = 0$ at chosen fixed points and $f\neq0$ at the others are independent hyperplane conditions in the $\bP^{12}$ of @sec-invariant-system. By @lem:node-condition the general member of each stratum has an ordinary node at each chosen fixed point; degeneracy of the quadratic part there and nodes elsewhere are proper closed conditions, so the general member has neither. Taking one, respectively two, chosen points gives $k = 1$ and $k = 2$.
:::

::: {.remark #rmk:a21-scope title="What that does to A21, and what the one-node locus leaves"}

The one-node locus is the problem's own case — it is where @prop:quasipolarization and the coverage count of @sec-projective-coverage are made — and A21 there is settled in its label clauses and open in its chamber clause, with the following precise accounting, current after @prop:one-node-connected and @thm:a21-labels. The family exists as a smooth proper equivariant family carrying a relative polarization and an exceptional divisor (@prop:one-node-family); along any path its parallel transport carries $S_\Co$, $S_{\mathrm{dP}}$, $H$ and $\alpha$ to those of the other endpoint (@thm:one-node-transport), and therefore the monodromy of a connected such family lands in the stabilizer of those four labels (@cor:construction-monodromy). The settled part is the labels (@thm:a21-labels), and it was the connectedness that closed them: by @prop:one-node-connected the locus is a nonempty Zariski-open of the hyperplane $\{f(p) = 0\}$, hence connected — an elementary openness argument, not a Severi-variety theorem — so the label clauses hold for every pair of the locus. What is not established is, first, the chamber: the family alone does not transport it. The labels themselves do pin a chamber of the arrangement cut by the member's own effective roots, by @lem:face-at-H, since the root is the only effective class of square $-2$ orthogonal to $H$; what they do not fix is that arrangement, and by @prop:chamber-conditional the chamber is carried exactly when the effective roots of square $-2$ agree across the family. So A21's chamber clause is a check on the effective cones of the members — a comparison of periods — and not something the local system decides; and, second, the identification of the lattice labels with a named labelling, which is @rmk:a21-open's question.

*Where the type of $S_{\mathrm{dP}}$ will be decided.* For a member of Picard rank $3$ one has a sandwich, $M\subseteq S_{\mathrm{dP}}\subseteq\Pic(\widehat X_b)$: $S_{\mathrm{dP}}$ has rank $3$ and contains $M$, and $\Pic$ contains $M$ and has rank $3$, so the three span the same $\QQ$-space, and an element of $S_{\mathrm{dP}}$, being a rational combination of algebraic classes, is algebraic, hence a Picard class once integral. So $S_{\mathrm{dP}} = M$ whenever the Picard lattice of the member is $M$, and the index in general is the index of $M$ in that Picard lattice.  The index of $M = \pi^*\Pic(\widehat Y)\perp\ZZ D$ in $S_{\mathrm{dP}}$ is $1$ or $2$, those being the only possibilities for an even overlattice of $M$, whose discriminant group is $(\ZZ/2)^3$; the index-$2$ case is $U\perp\langle-2\rangle$, generated by $e/2$, $f$ and the exceptional class. In that case $S_{\mathrm{dP}}$ would contain a class pairing oddly with $e = \pi^*h_1$, whereas every element of $M$ pairs evenly with $e$, since $\pi^*c\cdot\pi^*h_1 = 2(c\cdot h_1)$. So the type is decided by a single question: whether an $I_{\mathrm{dP}}$-invariant class of odd degree against $\pi^*h_1$ exists. None is exhibited here. A member whose elliptic fibration by $|e|$ carries an $I_{\mathrm{dP}}$-invariant section would supply one, a section having degree $1$ against $e$. Splitting of the cover over a curve $D\subset\widehat Y$ with $D\cdot h_1 = 1$ needs $D\cdot\widetilde B = 0$, and with $\widetilde B = -2K_{\widehat Y} = 4h_1+4h_2-2e$ the classes $D = ah_1+h_2+ce$ satisfying that have $c = -2a-2$ and $D^2 = 2a-4(a+1)^2$, so the only one of square at least $-2$ is $h_2-h_1$, of bidegree $(-1,1)$, which is not effective. So this route to an odd invariant class is closed, and the question is genuinely open rather than settled by the lattice.

Away from it the node count separates. @prop:node-count-invariant is auxiliary to the above and says only what its hypotheses give: when the $k$ nodes are all at $\tau$-fixed points, a one-node and a two-node member both satisfy the five bullets and have del Pezzo invariant lattices of ranks $3$ and $4$, so no element of $\Orth(\lkt)$ conjugates those two tuples — that comparison being one of labels only, and therefore unaffected by the chamber question. Nothing here is a claim about members with nodes off the fixed points, where the invariant rank is $k+2$ for the del Pezzo lift and $j+10$ for the Coble one, $j$ being the number of fixed nodes, and neither is computed in this book.

:::

::: {.proposition #prop:rank-two-slot-boundary title="The rank-two slot: the lattice reduction, and the vanishing in both constructions"}

In the notation of @prop:no-rank-one-automorphism let $\rk(S\cap S') = 2$.
Then $S\cap S' = S'$, so $S'\subseteq S$; taking isotropic generators $a_1,a_2$ of $S'\cong U(2)$ with $a_1\cdot a_2 = 2$, one has $H = \pm(a_1+a_2)$, and $\alpha = p(a_1-a_2)+\beta$ with $\beta\perp S'$ and $p\in\bQ$ satisfies:
1. $\beta\in S\otimes\bQ\cap H^{\perp}$, which is negative definite, so $\beta^2\le0$; and $\beta^2 = -2+4p^2$, so $p^2\le\tfrac12$; since $\alpha\cdot a_1 = -2p\in\bZ$, this leaves $\alpha\cdot a_1\in\set{-1,0,1}$.
2. $\iota'(\alpha) = -\alpha$ exactly when $\alpha\cdot a_1 = 0$, and in that case no automorphism of $\widetilde X$ induces $\iota'$, by the effectivity argument of @prop:no-rank-one-automorphism.
3. That vanishing holds in the marking of @prop:coble-cover-marking, where $S' = \langle f^*F_1,f^*F_2\rangle$ by the uniqueness proved for @prop:del-pezzo-placement and $\alpha\cdot f^*F_1 = \alpha\cdot f^*F_2 = 0$ is computed at the owner (`computations/reports/coble_del_pezzo_placement.py`); there the rank-two slot is induced by no automorphism either.
4. This proposition is about a slot whose invariant lattice is $U(2)$ and whose fixed lattice in $S_\Co$ is $\ZZ H$ or all of $S_\Co$. It does not describe the del Pezzo involution of the direct-projective construction, whose lifted invariant lattice has rank $2+k\ge3$ for a Coble member and which fixes the authored root instead of reversing it (@prop:del-pezzo-type-on-the-resolution, @rmk:a21-open). The direct-projective tuple is therefore not covered by this proposition, and it is not covered by @prop:no-rank-one-automorphism either.
:::

::: {.proof}

$\rk(S\cap S') = 2 = \rk S'$ and $S\cap S'$ is saturated in $S'$, so the two coincide and $S' = \langle a_1,a_2\rangle$ with $a_i$ isotropic and $a_1\cdot a_2 = 2$. Writing $H = ma_1+na_2$ gives $H^2 = 4mn = 4$, so $(m,n) = \pm(1,1)$.
Decompose $\alpha$ over $\bQ$ as $\alpha = (pa_1+qa_2)+\beta$ with $\beta\perp S'$; then $\alpha\cdot H = 2(p+q) = 0$, so $q = -p$ and $\alpha_A = p(a_1-a_2)$, whose square is $-4p^2$; the cross terms with $\beta$ vanish, so $\beta^2 = \alpha^2+4p^2 = -2+4p^2$.
$\beta$ lies in $S\otimes\bQ$ and is orthogonal to $H$, so $\beta^2\le0$ by (the proof of) @prop:no-rank-one-automorphism, giving $p^2\le\tfrac12$; and $\alpha\cdot a_1 = -2p$ is an integer because both classes lie in the lattice, leaving $\alpha\cdot a_1\in\set{-1,0,1}$.
Since $\iota'$ is $\id$ on $S'$ and $-\id$ on $S'^{\perp}$, $\iota'(\alpha) = p(a_1-a_2)-\beta$, which equals $-\alpha$ exactly when $p = 0$, that is exactly when $\alpha\cdot a_1 = 0$; the effectivity argument then applies verbatim.
Part 3 is the vanishing in the marking of @prop:coble-cover-marking, by the complete enumeration there; part 4 records that the direct-projective construction is a different case, and @rmk:a21-open says what its slot does instead. Where the hypotheses of this proposition hold, the slot reverses $\alpha$ and no automorphism induces it.
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
(vii) For the direct-projective construction the invariant type of the lifted $I_{\mathrm{dP}}$ is computed and is *not* $U(2)$: by @prop:del-pezzo-type-on-the-resolution it has rank $2+k$ and contains $U(2)\perp\langle-2\rangle^{\oplus k}$ for $k$ nodes of the branch curve, with equality a saturation question that is not settled. Since $k = 0$ makes $I_\Co$ fixed-point-free, every Coble member has $k\ge1$ and rank at least $3$ — so the rank split used in (iii)–(vi) does not apply to it.
(viii) The root of that tuple is an exceptional curve $D_g$, and it is fixed by both involutions, so the reversal argument of (v)–(vi) does not apply (@rmk:a21-open).
(ix) The tuple is not empty: by @prop:tuple-of-the-construction the five bullets hold on the resolved cover with $H = \pi^*\OO_Y(1,1)$ and $\alpha = [D_g]$. So what A21 asks there is a conjugacy statement about tuples that exist.
So the two cases this remark settles are those of (iii), and neither is the authored tuple. Where $S_{\mathrm{dP}}\cong\sdp$ and $\rk(S_\Co\cap\sdp) = 1$, the negative answer is @prop:no-rank-one-automorphism's, whose proof uses (i), (ii), (iv), (v) and (vi) and neither (iii)'s sharp form beyond $\rk S' = 2$, nor (vii), nor (viii).
Where $S_{\mathrm{dP}}\cong\sdp$ and the slot meets $S_\Co$ in rank two, the lattice alone leaves $\alpha\cdot a_1\in\set{-1,0,1}$ (@prop:rank-two-slot-boundary, part 1), and the vanishing is known in the marking of @prop:coble-cover-marking by the enumeration there, not from the shape of $S_\Co$, which is exactly what (vii) withholds.
For the direct-projective construction (iii) fails by (vii) and the authored root is fixed rather than reversed by (viii), so neither case covers it: the authored tuple is open for that construction (@rmk:a21-open) and nonempty by (ix), and what is established about it is (vii)–(ix) and the local shape of @prop:local-operators.
Where the coordinate class $H = 6e_0-2\sum_{i\le8}e_i-e_9-e_{10}$ *is* used, it is used in that marking and says so: @prop:coble-cover-marking, @prop:rank-one-slot, @prop:del-pezzo-placement and the owner computation of the rank-two pairings. None of those is a premise of the rank-one conclusion, which never names a coordinate of $H$.
What a correspondence would have to be, and is not produced here: a marking of the direct-projective surface carrying $\pi_{\mathrm{dP}}^*\OO(1,1)$ and the effective root to the classes of @prop:coble-cover-marking, together with the involutions. The numerical coincidences — $H^2 = 4$ on both sides, $L^2 = 2 = h^2$, $\mathfrak C^2 = -4$, $h\cdot\mathfrak C = 0$ — are recorded as consistent with it and do not supply it.
The two formal steps are checked in Lean 4 with Mathlib in `formalization/coble-enriques/EffectiveReversal.lean`: `slot_reverses_root` (the eigenvalue argument of the rank-one proof), `not_preserves_effectivity_of_reversal` (the positivity argument) and their composite `no_automorphism_reverses_root`, together with `rank_two_narrowing`, the arithmetic of the rank-two reduction. No `sorry`; axioms `propext`, `Classical.choice`, `Quot.sound` only. The geometric premises above enter as explicit hypotheses, since the surface theory that supplies them is not part of the file.
:::

::: {.remark #rmk:rank-one-geometry title="Where the Hodge condition sits, why the ample strengthening is empty, and what answers the $U(2)$ slots"}
*The Hodge condition, located.* $J$ is a Hodge isometry of a member exactly when $J\omega$ spans $\omega$; as $J$ is an involution the scalar is $\pm1$, and $+1$ is impossible because the real and imaginary parts of $\omega$ span a positive definite $2$-plane while the $(+1)$-eigenspace $U(2)$ has signature $(1,1)$. So the condition is $\omega\perp t$, equivalently $\omega\perp 2t$, which is the statement that the $(-4)$-class $2t$ is algebraic. In the notation of [@DK13, (3.2)] the periods orthogonal to a vector $\delta\in N_{-2d}$ form the Heegner divisor $H_{-2d}$ of the period domain $\bD(N)$, and here $N = \langle2\rangle\oplus E(2) = T_\Co$ and $2d = 4$: so the members whose cover admits $J$ as a Hodge isometry are the Coble covers whose period lies on $H_{-4}$. That divisor is nonempty, since $(2t)^{\perp T_\Co}$ has rank $10$ and signature $(2,8)$ (`computations/reports/coble_rank_one_placement.py`) so its own period domain is nonempty, and it is proper, since a generic period is not orthogonal to $2t$. It is a divisor of the family and not merely of the period domain by [@DK13, Prop. 3.2], which identifies $\mathcal M_{Co}$ with an open subset of $\bD(N)/O(N)$ through the Torelli theorem of Piatetskii-Shapiro and Shafarevich, together with @prop:coble-invariant-lattice for the lattice $N = T_\Co$; the two inputs are exactly those two, and neither is replaced by the signature computation.
*Why this does not decide the tuple, and what does.* The Torelli criterion of @sec-k3-automorphisms asks for a Hodge isometry preserving the ample cone, so on the Heegner divisor the realization question would be a chamber question. For a slot with $S_{\mathrm{dP}}\cong\sdp$ and $\rk(S_\Co\cap\sdp) = 1$, @prop:no-rank-one-automorphism answers it before either condition is reached: $\iota'$ reverses the effective class $\alpha$, so no chamber can be preserved, on the divisor or off it, for every member at once. In the marking the same reversal is what @cor:no-del-pezzo-involution-coble-cover records, and there it needs the vanishing $\alpha\cdot a_1 = 0$ that @prop:rank-two-slot-boundary isolates; so the rank-one answer is unconditional within that scope and the rank-two answer is the marking's. The slot of the direct-projective construction lies outside both, its lifted invariant rank being $2+k\ge3$ and its action on the authored root being $+1$ (@prop:del-pezzo-type-on-the-resolution, @rmk:a21-open), so nothing in this remark decides that tuple.
*The ample strengthening is empty, and is kept apart from the tuple.* Replacing the fourth bullet's nef and big $H$ by an ample one does not produce a smaller hypothesis under which the tuple holds: with $H$ ample and $\alpha$ effective, nonzero and of degree $0$ against $H$, the third and fourth bullets are already contradictory, by the same positivity that the proposition uses. The hypothesis stays nef and big throughout, and no ample subcase is claimed as, or substituted for, the conclusion.
:::

::: {.remark title="The rank-one case: the formulation, and the one input the gluing carries"}
When $\sdp$ is not contained in $S_\Co$, @prop:del-pezzo-placement gives $A = S_\Co\cap\sdp = \ZZ H$, and the same bijection formulates the question in $L_{K3}$ instead of $S_\Co$: an isotropic $b\in L_{K3}$ with $b\cdot H = 2$ corresponds to $y = 2b-H\in H^{\perp}\cap L_{K3}$ of square $-4$ with $y\equiv H \pmod{2L_{K3}}$, and the slot meets $S_\Co$ only in $\langle H\rangle$ exactly when $y\notin S_\Co\otimes\QQ$.
@prop:rank-one-slot answers it in the affirmative, and the two arithmetic conditions on $b$ suffice for that: the involution with $(+1)$-eigenspace $\langle H,b\rangle$ is integral on $\lkt$ by the projection formula, and its restriction to $S_\Co$ is integral because the values of $x\cdot H$ on $S_\Co$ generate $2\bZ$. What those conditions do not give is an eigensplitting of $S_\Co$ — that sum has index $2$ — and an earlier version of this remark read the failure of the splitting as a failure of integrality, which it is not. The datum that is genuinely missing is a different one, and it is the gluing: $b$ is not a vector of $S_\Co\oplus T_\Co$ at all, so what has to be exhibited is a vector of $T_\Co^{\#}$ of square $-1$ in the class $\gamma_\Co(\overline{H/2})$, and @prop:rank-one-slot shows that every class the gluing can present contains one.
What is in hand at the level of the gluing: the two discriminant forms are anti-isometric, $A_{S_\Co}\cong A_{T_\Co}(-1)$, verified at the pin by `A_{S_\Co}.is_anti_isometric(A_{T_\Co})` returning `True` (`computations/reports/coble_gluing_discriminants.py`), so by @thm:nikulin-gluing the pair does admit a unimodular overlattice with the full graph gluing and the stated index $2^{11}$ is consistent with it. The explicit arrow was recorded here as blocked at an earlier pin, and that block is now resolved: maintained `sage-extensions` at main `6ad7a5ea396da6e758ee28f3dea10a35baee0266` supplies `A_{S_\Co}.isometry_to(A_{T_\Co}(-1))`, and its published test `tests/forms/test_the_coble_anti_isometry.sage` runs on these inputs — the Coble lattices $S_\Co = \latI_{1,10}(2)$ and $T_\Co = B(2)$ — and checks the exact source and target types, the quadratic values on generators and on pair sums, all pairwise bilinear values, the sign of the twist, and the inverse and composition laws. The refusals recorded earlier were made at pin `c546077d`, where `then` is guarded by object identity, `normal_form` is recomputed per call so that the two normal forms are distinct objects, and `isometry_to` exists at the lattice level only; they are superseded, not explained away.
The arrow is still not needed for what is proved here, and the two reasons differ. @prop:rank-one-slot quantifies over $\gamma_\Co$: it shows that every class of $A_{T_\Co}$ of odd value contains a vector of square $-1$, which is why the slot exists whatever the anti-isometry is. @prop:no-rank-one-automorphism uses no gluing at all, since $\alpha\in S_\Co$ and $2t = 2b-H\in T_\Co$, so what it reverses it reverses for every admissible $b$. An explicit $\gamma_\Co$ would therefore serve the writing down of the overlattice, which is a construction this book does not need for either conclusion; it is not a step in an argument still owing something.
The formulation is also not one the provider's fibre machinery reaches directly: $H^{\perp}\cap\lkt$ has signature $(2,19)$, since $\lkt$ has signature $(3,19)$ and $H^2 = 4>0$, so it is indefinite, and the exhaustive enumeration that made the rank-two computation a certificate does not apply to it; and testing $y\notin S_\Co\otimes\QQ$ needs $S_\Co$ placed inside $\lkt$, that is the gluing in machine-readable form, which the book does not carry. Neither point bears on @prop:rank-one-slot, which decides the question on the discriminant form of $T_\Co$ — finite of order $2^{11}$ — and never enters the indefinite fibre.
On top of the embedding question the authored tuple asks for automorphisms. For a slot whose invariant lattice is $\sdp\cong U(2)$ the rank-one case is answered negatively: @prop:no-rank-one-automorphism shows that the slot reverses the authored root $\alpha$ and that no automorphism does that. The direct-projective construction does not produce such a slot: its lifted $I_{\mathrm{dP}}$ has invariant rank $2+k\ge3$ and fixes the root, so there the question is open (@prop:del-pezzo-type-on-the-resolution, @rmk:a21-open).
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

::: {.lemma #lem:gamma-co-is-tilde-o-plus title="The stable group is $\widetilde\Orth^+(T_\Co)$, definitionally"}

With $\Orth^+(L)\definedas\Theta_\bR(L)$ of @def:lattice-spinor-kernels and $\widetilde\Orth^+(L)$ the pullback of $\widetilde\Orth(L)=\ker\rho_L$ along the inclusion $\Orth^+(L)\injects\Orth(L)$,
$$
\Gamma_\Co = \Orth^+(T_\Co)^* = \widetilde\Orth^+(T_\Co)
.$$
:::

::: {.proof}

The left side is $\Orth^+(T_\Co)\intersect\ker\rho_{T_\Co}$ by the definition of $\Gamma_\Co$ above, and the right side is the same intersection by the definition of a pullback along an inclusion: the pullback of $\ker\rho_L$ along $\Orth^+(L)\injects\Orth(L)$ is the set of those $g\in\Orth^+(L)$ whose image lies in $\ker\rho_L$.
So the identity asserts nothing beyond those two definitions, and no arithmetic property of $T_\Co$ enters it.
:::

::: {.proposition #prop:gamma-co-two-definitions title="What separates the two further definitions of $\Gamma_\Co$"}

Let $\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma^\theta_\Co$ be the groups of @prop:gamma-co-in-heegner-group and @prop:gamma-co-in-theta-centralizer.
Then:

1. $\Gamma^{\mathrm{Hdg}}_\Co = \Gamma_\Co$ if and only if $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr) = 1$, and $\Gamma^\theta_\Co = \Gamma_\Co$ if and only if $\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr) = 1$;
2. both $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr)$ and $\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr)$ are subgroups of the finite group $\Orth(A_{T_\Co}, q_{T_\Co})$, of order $46\,998\,591\,897\,600$ by @prop:coble-discriminant-group, and neither question involves $\fco$ or a period domain;
3. $\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr)\neq1$ exactly when some $g\in Z_{\Orth(\lkt)}(\theta_\Co)\intersect\Stab_{\Orth(\lkt)}(\tilde h_\Co)$ has $\restrictionof{g}{T_\Co}$ acting nontrivially on $A_{T_\Co}$.

So each of the two questions is a question about a finite group, and a *witness* for strictness of either inclusion is a single explicit isometry, of $\lkt$ in case (3) and of the Heegner lattice in the other.
:::

::: {.proof}

(1) is the second claim of each of the two propositions, which identifies $\Gamma_\Co$ with the kernel of the respective finite image, together with the first isomorphism theorem; a kernel is everything exactly when the image is trivial.
(2) an isometry of $T_\Co$ has a discriminant image, so each image is a subgroup of the finite group acting on $A_{T_\Co}$, and the order of that group is the one @prop:coble-discriminant-group computes.
(3) unwinds the definition of $\Gamma^\theta_\Co$ as the set of restrictions of the elements of that intersection: a nontrivial image is an element of it acting nontrivially on $A_{T_\Co}$, and conversely.
:::

Nothing in the two propositions above, or in this one, says whether either image is trivial: the containment $\Gamma_\Co\iscontainedin\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma_\Co\iscontainedin\Gamma^\theta_\Co$ is all that is proved, and by contrast the congruence group is *proved* strictly larger, in the remark below.
What can be said without the finite computation is that the finite group on the Enriques side is not trivial, so the index in @prop:gamma-co-in-heegner-group is bounded by a group that is genuinely bigger than the trivial one and the question is not vacuous.

::: {.lemma #lem:polarization-stabilizer-discriminant-nontrivial title="The finite image of the polarization stabilizer is not trivial"}

Let $C = U\oplus E_8$ and $S_\En = C(2) = U(2)\oplus E_8(2)$ be the lattices of @def:enriques-lattice, where $E_8$ is negative definite in that definition's convention, and let $h = u_0+w_0$ be the degree-$2$ polarization class of $S_\En$; put $v \definedas u_0-w_0$.
Then the reflection $s_v$ is an isometry of $S_\En$ fixing $h$, and it acts nontrivially on $A_{S_\En}$; consequently the subgroup $\rho_{S_\En}\bigl(\Stab_{\Orth(S_\En)}(h)\bigr)$ whose order bounds the index in @prop:gamma-co-in-heegner-group is not trivial.
:::

::: {.proof}

In $S_\En$ one has $u_0^2 = w_0^2 = 0$ and $b(u_0,w_0) = 2$, so $v^2 = -4$ and $\div_{S_\En}(v) = 2$; the reflection is therefore the integral isometry $s_v(x) = x + \tfrac12 b(x,v)v$ of @def:spinor-norm, and $\spinornorm_\bR(s_v) = [2] = [1]$, so $s_v\in\Orth^+(S_\En)$.
It fixes $h$: $b(h,v) = b(u_0+w_0,\,u_0-w_0) = 0-2+2-0 = 0$, hence $s_v(h) = h$.

For the discriminant, the class of $u_0/2$ lies in $S_\En^*$, because $b_{S_\En} = 2\,b_C$ and $u_0, y\in C$ give $b_{S_\En}(u_0/2, y) = b_C(u_0,y)\in\ZZ$ for every $y\in S_\En$.
Then $b(u_0/2, v) = \tfrac12\bigl(b(u_0,u_0) - b(u_0,w_0)\bigr) = -1$, so
$$
s_v\bigl(\tfrac12 u_0\bigr) = \tfrac12 u_0 - \tfrac12 v = \tfrac12 w_0
,$$
and $\tfrac12 w_0 - \tfrac12 u_0 = \tfrac12(w_0-u_0)$ has coordinates $(-\tfrac12, \tfrac12, 0,\dots,0)$ in the basis $u_0, w_0$ together with a basis of $E_8(2)$, so it is not in $S_\En$.
Hence $\rho_{S_\En}(s_v)\neq\id$ while $s_v(h) = h$, which is the claim.
:::

::: {.remark title="What the lemma does and does not settle"}

The lemma is about the group whose order *bounds* the index in @prop:gamma-co-in-heegner-group, and it does not make either inclusion strict.
An element of $\Gamma^{\mathrm{Hdg}}_\Co$ is the restriction of an element of $\Stab_{\gent}(\ZZ\delta)$, and an isometry of $S_\En$ with nontrivial discriminant image need not have a partner in $T_\Co$: by @thm:automorphism-lifting-criterion a pair $(g_S,g_T)$ extends over the overlattice exactly when $\bar g_T\circ\gamma = \gamma\circ\bar g_S$, and the lemma's element $s_v$ supplies only its $g_S$ half.
So the strictness of the two inclusions remains open, and what would decide it is one of the following: an explicit pair, in which case the inclusion is strict and the two definitions are different groups; or the triviality of the two finite images, in which case the definitions agree.
Both are decided in a finite group by @prop:gamma-co-two-definitions, and neither is decided here: reading the discriminant image of a named isometry is the call `s.discriminant_morphism()`, which at the adopted runtime raises `TypeError: TorsionFormOrthogonalGroup._element_constructor_() got an unexpected keyword argument 'check'` (dzackgarza/sage-extensions#272), on $S_\En$ as on $T_\Co$.
The record of what was checked and what stopped is `computations/reports/coble_gamma_co_two_definitions.py`.
:::

### The reflective set of the stable group {#sec-gamma-co-reflective-set}

The two propositions above compare $\Gamma_\Co$ with the larger groups by way of its finite image on $A_{T_\Co}$.
The opposite question is what lies *inside* $\Gamma_\Co$, and it begins with the reflections of $T_\Co$.

*Convention, used throughout this section.*
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
Two consequences are used below and are worth separating from the arguments that use them: a pairing of two vectors that both lie in $L^*$ is a half-integer and not an integer, and the reduction modulo $2$ is the only place where the integral lattice enters the discriminant representation.

By @def:2elementary-roots the roots of an even $2$-elementary lattice are the short roots of square $-2$ and the long roots of square $-4$; that vocabulary is set up there for a hyperbolic lattice and transfers to $T_\Co$ because it uses the square and the divisibility and neither uses the signature.

::: {.proposition #prop:gamma-co-reflective-set title="The reflective set of the stable Coble group"}

Let $T_\Co = B(2)$ be the Coble lattice of @prop:tco-as-twist, even of signature $(2,9)$ and determinant $-2048$, so that every primitive vector of $T_\Co$ has divisibility $2$ (@lem:divisibilityAlwaysTwoTco), and let $\Gamma_\Co = \Orth^+(T_\Co)\intersect\ker\rho_{T_\Co}$, with $\Orth^+(T_\Co) = \Theta_\bR(T_\Co)$ of @def:lattice-spinor-kernels and $\spinornorm_\bR$ the real spinor norm of @def:spinor-norm.
Write $s_v$ for the reflection of @def:spinor-norm in a nonisotropic vector $v$.
Then $s_v$ is an isometry of $T_\Co$ exactly for $v^2\in\{2,-2,4,-4\}$, and among those:

1. if $v^2 = -2$ then $s_v\in\Gamma_\Co$; hence the short roots generate a subgroup
   $$
   W(T_\Co) \definedas \generators{\,s_v \;:\; v \in T_\Co,\ v^2 = -2\,}
   \iscontainedin \Gamma_\Co
   ,$$
   which is infinite, the proof exhibiting a family;
2. if $v^2 = 2$ or $v^2 = 4$ then $s_v\notin\Orth^+(T_\Co)$, hence $s_v\notin\Gamma_\Co$;
3. if $v^2 = -4$ then $s_v\in\Orth^+(T_\Co)$ and $s_v\notin\ker\rho_{T_\Co}$.

Consequently the reflective set of $\Gamma_\Co$ — the vectors of $T_\Co$ whose reflection lies in $\Gamma_\Co$ — is exactly the set of short roots, and no long root lies in it.
:::

::: {.proof}

*Integrality.*
A primitive $v$ has $\div_{T_\Co}(v) = 2$ (@lem:divisibilityAlwaysTwoTco), so $\beta(v,T_\Co) = 2\ZZ$; and $v^2\in\{2,-2,4,-4\}$ forces $v$ primitive, since $v = dw$ with $d\ge2$ would give $v^2 = d^2w^2$ with $w^2$ even.
Then $2\beta(x,v)/\beta(v,v)$ is an integer for every $x$, because $2\beta(x,v)$ is a multiple of $4$ and $\beta(v,v)$ divides $4$; so $s_v$ is an isometry of $T_\Co$ in all four cases, and for any other square it is not, since $\beta(v,T_\Co)\subseteq (v^2/2)\ZZ$ would fail.
The real spinor norm of @def:spinor-norm is $\spinornorm_\bR(s_w) = [-\tfrac12\beta(w,w)]$ for any nonisotropic $w$, so $\spinornorm_\bR(s_v)$ is $[-1]$ for $v^2 = 2$, $[1]$ for $v^2 = -2$, $[-2] = [-1]$ for $v^2 = 4$, and $[2] = [1]$ for $v^2 = -4$.

(1) For $v^2 = -2$ the reflection is $s_v(x) = x + \beta(x,v)v$.
The spinor norm is $[1]$, so $s_v\in\Theta_\bR(T_\Co)$.
For $x^*\in T_\Co^*$ the pairing $\beta(x^*,v)$ is an integer, because $x^*$ pairs integrally with every element of $T_\Co$ and $v$ lies in $T_\Co$; hence $s_v(x^*)-x^* = \beta(x^*,v)v\in T_\Co$ and $\rho_{T_\Co}(s_v) = \id$.
So $s_v\in\Gamma_\Co$.
The set of such $v$ is infinite and the family is explicit: for odd $a\in\ZZ$,
$$
x_a \definedas a\zeta + e' - \tfrac{a^2+1}{2}f'
\qquad\text{has}\qquad
x_a^2 = 2a^2 + 4\cdot\Bigl(-\tfrac{a^2+1}{2}\Bigr) = -2
,$$
since $\zeta$ is orthogonal to the $U(2)$ summand and $\beta(e',f') = 2$ there.

(2) Both squares give $\spinornorm_\bR(s_v) = [-1]$, which is not the identity of $\bR^\times/(\bR^\times)^2$, so $s_v\notin\Theta_\bR(T_\Co)$ and hence $s_v\notin\Gamma_\Co$.
Nothing about $\ker\rho_{T_\Co}$ is needed, and for $v^2 = 4$ the corresponding assertion would be false: for $v = e'+f'$ in the $U(2)$ summand one has $\beta(e'/2, v) = 1$ and
$$
s_v\bigl(\tfrac12 e'\bigr) = \tfrac12 e' - \tfrac12\bigl(e'+f'\bigr) = -\tfrac12 f',
\qquad
s_v\bigl(\tfrac12 e'\bigr) - \tfrac12 e' = -\tfrac12\bigl(e'+f'\bigr)\notin T_\Co
,$$
so $\rho_{T_\Co}(s_v)\neq\id$ there.
The factor $\tfrac12$ is exactly the half-integrality of a pairing of two vectors of $T_\Co^*$.

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

::: {.remark title="What the reflective set settles, and what it does not"}

Parts (1)–(3) decide the reflective set: it is the short roots, determined and not chosen, with nothing left to add and nothing to remove.

They do not decide how large $W(T_\Co)$ is in $\Gamma_\Co$.
The question is *not* whether "a reflective set together with finitely many further isometries generates $\Gamma_\Co$": $\Gamma_\Co$ is an arithmetic subgroup of $\Orth(T_\Co\tensor\bR)\iso\Orth(2,9)$, and arithmetic subgroups of semisimple real groups are finitely generated (Borel--Harish-Chandra), so any generating set together with finitely many further elements generates it, and that formulation carries no content.
What carries content is the **index** $[\Gamma_\Co : W(T_\Co)]$: whether it is finite, and if finite which.

That index is what a Vinberg-type statement computes, and the route named for it in the research report — Vinberg's algorithm at each cusp (@prob:coxeter-completeness item 2, and the cusp-level items B32--B34 of the taxonomy) — is a statement about hyperbolic lattices and does not apply to $T_\Co$ itself, which has signature $(2,9)$; the owning library refuses it on exactly that ground, `HyperbolicLattices` accepting signature $(1,n)$ or $(n,1)$ only, and the hyperbolic statement belongs to the cusp lattices of @sec-open-problems and not to $T_\Co$.
For $T_\Co$ the index is undecided here, and no operation of the owning library decides it: `Lattices.roots()` is the definite-lattice root set and refuses an indefinite lattice by contract, which is not evidence about the $(-2)$-vectors; `root_module_generating_set()` is a semi-decision for $T_\Co = \ZZ\Phi(T_\Co)$, the module the roots generate, and not for the index of $W(T_\Co)$ in $\Orth^+(T_\Co)\intersect\ker\rho_{T_\Co}$; and there is no operation returning generators of, or a finite-index certificate for, that intersection.
The computed state is recorded in `computations/reports/coble_gamma_co_reflective_set.py`, and the state of the running Sage and its lattice library that keeps (1)–(3) as proofs here rather than as decisions of that library is recorded in `computations/reports/coble_owner_gap-blockers-20261105.md`.
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
