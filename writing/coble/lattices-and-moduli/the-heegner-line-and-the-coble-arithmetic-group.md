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
Identifying that group with $\Gamma_\Co^\En(\delta)$ of @def:gamma-co-en requires an isometry between the Coble primitive embedding and the Enriques Heegner complement carrying $\tilde h_\Co$ to the class $h=e+f$ of @prop:gamma-en-two-gluing.
By @prop:gamma-co-in-theta-centralizer and @prop:gamma-co-in-heegner-group the two groups are extensions of the same $\Gamma_\Co$ by subgroups of $\Orth(A_{T_\Co}, q_{T_\Co})$, so what the missing isometry would identify is a pair of finite subgroups of that finite group; agreement of finite images is weaker than an isomorphism of the lattice subgroups, and agreement of the lattice subgroups is weaker still than the isometry itself, which is the labeled rigidity of @prob:coble-rigidity.
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
What the argument needs of $\sigma$ is that it lies in $\Orth^+(T_\Co) = \Theta_\bR(T_\Co)$ by @def:spinor-norm, that it moves the discriminant, and that its discriminant action fixes the $\langle2\rangle$- and $E_8(2)$-blocks and transposes the two isotropic classes of the $U(2)$-block; these are verified through the owner's operations in `computations/reports/coble_congruence_witness.py`, where $\sigma$ is built by `Lattices.reflection`, its membership in `O_plus` and in `stable_orthogonal_group` is decided by those groups, the classes are the owner's `discriminant_class` of `primitive_dual`, and the action is `discriminant_morphism`, with $q([\tfrac12 e']) = q([\tfrac12 f']) = 0$, $q([\tfrac12\zeta]) = \tfrac12$, $b([\tfrac12 e'], [\tfrac12 f']) = \tfrac12$ and $\abs{A_{T_\Co}} = \abs{\det T_\Co} = 2048$ read off the same objects.
So $\rho(\sigma)\in P$ is nontrivial, $\sigma\notin\Gamma_\Co$, and $\Gamma^{\mathrm{cong}}_{\Co,2}$ strictly contains $\Gamma_\Co$.
What this does and does not settle: the four-group identification of @prob:group-identification cannot be an equality with the stable group $\Gamma_\Co$, only an equality among overgroups of it, and for the congruence group the overgroup is strictly larger while for the Heegner and $\theta$-groups no witness is proposed and strictness stays open.

*Torelli, monodromy and labeled embeddings.* Two of the four are not of that kind.
The direct and geometric groups are images of centralizers in $\Orth(\lkt)$ of the labeled Coble datum, so comparing either with a Heegner group requires an isometry of $\lkt$ carrying the Enriques-labeled structure $(S_\En, T_\En, \ZZ\delta, h)$ of @prop:gamma-en-two-gluing to the Coble-labeled one $(S_\Co, T_\Co, \tilde h_\Co)$ of @prop:gamma-co-in-theta-centralizer; that is the labeled rigidity of @prob:coble-rigidity, not a computation in $T_\Co$.
And the geometric group is the monodromy of a moduli stack, so it agrees with an arithmetic group only through the direct period theorem and the direct monodromy theorem, @prob:B24 and @prob:B25.
Nothing in the two propositions above bears on either, and replacing $\Gamma_\Co$ by $\Gamma^{\mathrm{Hdg}}_\Co$ in an orbit count is exactly the change of group that the comparison forbids.
:::
