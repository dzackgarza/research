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

::: {.lemma #lem:gco-orbit-transfer title="The $G_\Co$ orbit decomposition lives on the $S_\En$ summand"}

By @prop:tco-as-twist $T_\Co = B(2) = \generators{2}\oplus U(2)\oplus E_8(2)$, so $T_\Co = \generators{\zeta}\perp S_\En$ with $\zeta^2 = 2$ and $S_\En = U(2)\oplus E_8(2)$, and discriminant forms add over orthogonal sums:
$$
A_{T_\Co} = A_{\generators{2}}\perp A_{S_\En},
\qquad
q_{T_\Co} = q_{\generators{2}} + q_{S_\En},
$$
with $q_{\generators{2}}$ taking the value $\tfrac12$ on the nonzero class and $q_{S_\En}$ taking values in $\ZZ/2\ZZ$.
Then the isotropic classes of $A_{T_\Co}$ are exactly the classes whose $A_{\generators{2}}$-coordinate vanishes, and they number $528$, the same as the isotropic classes of $A_{S_\En}$.
Each of the nine generators of $G_\Co$ is the reflection in a vector of $S_\En$, hence fixes $\zeta$, preserves the splitting, and acts on $A_{T_\Co}$ as $\id\oplus\rho_{S_\En}(g_i)$.
Consequently the orbits of $G_\Co$ on the isotropic classes of $A_{T_\Co}$ are its orbits on the isotropic classes of $A_{S_\En}$, with the same sizes.
:::

::: {.proof}

The splitting is the one displayed; $q_{\generators{2}}(\tfrac12\zeta) = \tfrac14\zeta^2 = \tfrac12$, and the values of $q_{S_\En}$ are integers.
A class $(a, y)$ with $a\in\{0,1\}$ has $q_{T_\Co}(a,y) = \tfrac{a}{2} + q_{S_\En}(y)$, which vanishes in $\QQ/2\ZZ$ only if $a = 0$ and $q_{S_\En}(y) = 0$: for $a = 1$ it would require $q_{S_\En}(y) = -\tfrac12$, and no class of $A_{S_\En}$ has that value.
So the isotropic classes of $A_{T_\Co}$ are the isotropic classes of $A_{S_\En}$ with first coordinate $0$, and their number is the one recorded for $A_{S_\En}$.
The nine vectors generating $G_\Co$ are $u_0 - w_0$ and the eight simple roots of $E_8(2)$ (@prop:polarization-stabilizer-enriques), all of them in the $S_\En$ summand, hence orthogonal to $\zeta$; so each reflection fixes $\zeta$ and acts as $\id\oplus\rho_{S_\En}(g_i)$ on the discriminant module.
An orbit of $G_\Co$ on $A_{T_\Co}$ therefore stays in its first coordinate, and on the first coordinate $0$ it is an orbit on $A_{S_\En}$.

The numerical inputs are computed in `computations/reports/coble_gco_orbit-transfer.py`, whose run reports $\abs{A_{T_\Co}} = 2048$ and $\abs{A_{S_\En}} = 1024$ with $528$ isotropic classes each, the values $0, \tfrac12, 1, \tfrac32$ of $q_{T_\Co}$ against $0, 1$ for $q_{S_\En}$, all $528$ isotropic classes of $A_{T_\Co}$ with vanishing first coordinate and none with nonzero first coordinate, and each of the nine reflections fixing $\zeta$ and preserving that coordinate.
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
   ,$$
   computed on $A_{S_\En}$ in `computations/reports/coble_gco_orbit-decomposition.py` and carried to $A_{T_\Co}$ by @lem:gco-orbit-transfer, whose numerical inputs are `computations/reports/coble_gco_orbit-transfer.py` and its run;

3. the finite stabilizer $\Stab_{\Orth(q_{T_\Co})}\bigl(\tfrac12\tilde h_\Co\bigr)$ of the class of the transported polarization has order $94\,755\,225\,600$, contains $G_\Co$ with index $136$, and acts on the same $528$ isotropic classes with orbit lengths $[\,1,\ 255,\ 272\,]$.
:::

::: {.proof}

Finiteness of the orbits is finiteness of the class set in a fixed genus, which is `def:genus` together with the finiteness of the class number for a definite lattice of the relevant rank; the Coble-specific content is the identification of the relevant lattice as definite on the Heegner line.
:::

::: {.remark title="How the three orders are obtained"}

The generators named in (1) are the two evident families of isometries of $C$ fixing $h = u_0 + w_0$: the involution $u_0\leftrightarrow w_0$, and $W(E_8)$ acting on the second summand.
By @prop:polarization-stabilizer-enriques these generate a group of order $2\abs{W(E_8)}$ whose reduction has $\id_U\oplus(-\id_{E_8})$ in its kernel, so the image has order at most $\abs{W(E_8)}$.
The equality in (1), and the fact that finitely many integral isometries realise it, is verified through the owner's operations in `computations/reports/coble_stabilizer_generators.py`: the reflections in $u_0-w_0$ and in the eight simple roots of $E_8(-1)$ generate $\Orth(h^{\perp C})$ — the owner's own subgroup comparison, the generated subgroup having the order $2\abs{W(E_8)}$ of the whole group — and their discriminant images generate a subgroup of $\Orth(A_{S_\En}, q_{S_\En})$ of order $\abs{W(E_8)}$.
Those generators are the Heegner-side input to the finite stabilizer whose orbits (2) and (3) record, so the two properties they are used for are checked generator by generator rather than assumed: `computations/reports/coble_heegner-generator-checks-run.txt` fixes the class $\tfrac12\tilde h_\Co$ under each of the $1984$ generators of that stabilizer in $\Orth(A_{T_\Co},q_{T_\Co})$, restores $q$-preservation through `validate_form_preservation()` — which tests $q$ on the eleven module generators and all their pairwise sums, hence on the whole module, instead of on the $528$ isotropic classes — and validates point closure of the restricted action on those classes; the run is at provider pin `15db925b` and its numbers are $\abs{G} = 46\,998\,591\,897\,600$ and $\abs{H} = 94\,755\,225\,600 = \abs{G}/496$.
What that verification does *not* cover is (2) and (3), the two orbit decompositions, which are computations in the finite quadratic space $A_{T_\Co}\cong B/2B$ of @def:coble-mod-four-form.
The finer one, (2), is computed on $A_{S_\En}$: `computations/reports/coble_gco_orbit-decomposition.py` builds $G_\Co$ from its nine generators — the discriminant images of the reflections in $u_0-w_0$ and in the eight simple roots of $E_8(2)$ — as a subgroup of $\Orth(A_{S_\En}, q_{S_\En})$, where $A_{S_\En}$ has $528$ isotropic classes, and its orbits there are of sizes $1,\,2,\,120,\,135,\,270$, summing to $528$; the run also returns $\abs{G_\Co} = 696\,729\,600$, which @prop:gamma-co-heegner-strict now proves independently.
The passage of those sizes to $A_{T_\Co}$, which is what (2) states, is @lem:gco-orbit-transfer: $A_{T_\Co} = A_{\generators{2}}\perp A_{S_\En}$ with $q_{\generators{2}} = \tfrac12$ on the nonzero class, the isotropic classes of $A_{T_\Co}$ are exactly those with vanishing first coordinate, and the nine generators act as $\id\oplus\rho_{S_\En}(g_i)$ because each is a reflection in a vector of the $S_\En$ summand. The run behind those three inputs is `computations/reports/coble_gco_orbit-transfer-run.txt`.
The coarser one, (3), is now computed too, by `computations/reports/coble_isotropic-stabilizer-orbits.py`: the stabilizer $H$ of the class of $\tfrac12\tilde h_\Co$ in $\Orth(A_{T_\Co},q_{T_\Co})$ has order $94\,755\,225\,600 = 46\,998\,591\,897\,600/496$ — the arithmetic check the run performs — and its orbits on the $528$ isotropic classes are of sizes $1,\,255,\,272$, summing to $528$, covering them, with the zero class as the only singleton. The orbits are computed through the action restricted to those $528$ classes after verifying $H' = H$ from $H' = G.\mathrm{subgroup\_on}(H.\mathrm{group\_generators}())$ and the equality of orders; asking the module for the orbits of $H$ on the whole $2048$-class module instead enumerates four times the set that is asked about and did not finish within $5400$ s, which `computations/reports/coble_isotropic-stabilizer-orbits-run-cut.txt` records. The operation by which the stabilizer is presented on generators alone, without building $\Orth(A_{T_\Co},q_{T_\Co})$ first, is still absent (sage-extensions#273) and is no longer on this page's critical path.
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
The block-compatibility conditions of @prop:gamma-cong-eq-heegner are instances of exactly this: that a gluing anti-isometry carries the $U(2)$ summand to the $U(2)$ summand is a statement about the labeled primitive embedding, not about the abstract pair of discriminant forms, so it falls under @prob:coble-rigidity in the sense used here.
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

What is *computed* about it, and how far it reaches: `computations/reports/coble_nefness-one-node.py`, transcript `-run.txt`, tests $h_\Co = 6H-2(E_1+\dots+E_8)-E_9-E_{10}$ against every class whose effectivity has a named source and against the $(-2)$-classes that Riemann--Roch makes effective in a window. The sourced classes: the ten exceptional curves $E_i$ of the blowup at the nodes of the sextic ([@DK13, §3]), on which $h_\Co\cdot E_i = 2$ for $i\le8$ and $1$ for $i = 9,10$; and the branch sextic $\mathfrak c = -2K_S = 6H-2\sum_iE_i$, of self-intersection $-4$, on which $h_\Co\cdot\mathfrak c = 0$ — the null curve of the one-node member of @prop:quasipolarization has that same class, so the zero there is a **wall** and not a failure of nefness. The window: writing $\delta = aH-\sum b_iE_i$ with $\delta^2 = -2$, the slice $\delta\cdot H = a$ is a coset of the negative definite $H^{\perp} = \langle E_1,\dots,E_{10}\rangle$, so the owner's fibre operation on that definite lattice enumerates the slice completely; over $a\le3$ there are $193\,140$ such classes, of which $192\,929$ have $h_\Co\cdot\delta>0$, $150$ have $h_\Co\cdot\delta = 0$, **none** has $h_\Co\cdot\delta<0$ together with $(-K_S)\cdot\delta\ge2$ — the Riemann--Roch condition that makes a $(-2)$-class effective — and $61$ have $h_\Co\cdot\delta<0$ with effectivity undecided by Riemann--Roch, the class $-E_9-E_{10}$ among them ($h_\Co\cdot\delta = -2$, $(-K_S)\cdot\delta = -2$), which the record reports as of unknown effectivity and not as a counterexample. So nefness of $h_\Co$ is confirmed on every sourced class and throughout that window, and is not proved over all curves.

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

*What the labels do pin, and what they do not.* By @lem:face-at-H the only wall through $H_b$ is $\alpha_b^\perp$, and the component containing the Kähler cone has $H_b$ in its closure and is positive on $\alpha_b$; that component is a chamber of the arrangement cut by the effective roots of that member, and it is the chamber of the tuple — this is the reading of the chamber clause of @def:coble-polarization-classes, which defines $\mathfrak c$ by the member's own $\Delta_X$: @lem:face-at-H(4) and @prop:chamber-pinned are statements about those walls and use the effectivity of each tested class, so a reading that named the chamber from the labels alone would not support them, and two members with equal labels but different effective-root sets would be given one chamber where the walls give two. If the walls do not accumulate at $H_b$ it is moreover the only such component (@prop:chamber-pinned), so that in that case $(H_b,\alpha_b)$ pin it; where they may accumulate, they do not, and the pinning is a hypothesis rather than a theorem. What they do not fix is the arrangement itself: if $\Delta_{\widehat X_{b'}}$ is larger than the transported $\Delta_{\widehat X_b}$, the transported chamber is a union of chambers of $b'$ and not a chamber, and the conjugacy then fails on the chamber even though it holds on the labels. So the chamber clause of A21 turns on whether the effective roots agree, which is the next statement; the Gauss–Manin connection does not preserve $H^{2,0}$, and that agreement is not something parallel transport supplies.
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


::: {.remark title="The labeled conjugacy: what is to be computed, and what a computation cannot decide"}

The isometry carrying $\tilde h_\Co$ to $h$ is on record: Nikulin's criterion was discharged by `in_same_orbit` returning `True` for the two glue classes through the represented action of $\Orth(\tilde h_\Co^{\perp})$ — order $2\,786\,918\,400$, $22$ generators, image of order $696\,729\,600$ in $\Orth(A)$ — so such an isometry exists and the open question is its *labels*.
What is to be computed is a joint orbit question and not three separate ones: the isometries $\tilde h_\Co^{\perp}\to h^{\perp}$ carrying one glue class to the other form a torsor under the finite group $\Orth(\tilde h_\Co^{\perp}) = \Orth(h^{\perp})$ (definite, rank $10$, order $2\,786\,918\,400$), so the labels hold exactly when the root $\alpha = 3e_0-\sum_{i\le10}e_i$ and the shadow of the $U(2)$-direction of $f^*F_1, f^*F_2$ land in the orbit of their counterparts under that group; the two data are not independent, since $f^*F_1-f^*F_2$ has square $-4$ and the only roots of the complement are $\pm\alpha$, so the $U(2)$ enters as a discriminant class, and the sign of $\alpha$ alone is free because $-\id$ on a $2$-elementary complement has $\rho(-\id) = \id$.
Owner operations: `primitive_sublattice_from` and `orthogonal_complement` to build the two complements, `Aut()` for the finite group and its generator count, `discriminant_representation` for the action on $A$, and `in_same_orbit` on the total quotient — with the one thing to check before running being whether that action is available on *pairs* and not on classes alone.
Premises and their sources: [@DK13, §3] for $e_0, e_i$, for the classes $\alpha$ and $-2K_S$, and for the effectivity asymmetry that makes $+\alpha$ the retained root; @prop:quasipolarization and @prop:polarization-stabilizer-enriques for the $U(2)$ on each side, its uniqueness inside $S_\Co$ being the enumeration in `computations/reports/coble_del_pezzo_placement.py`; AEGS `def:involutions` for the del Pezzo slot; and Nikulin's criterion with the glue-class orbit for the existence of the underlying isometry.
What such a computation could not decide: it lives in the rank-$10$ complements, while $\lkt$ and the two primitive embeddings are not built by any owner object on record, so the passage from matching complements to an isometry of $\lkt$ remains the extension by @thm:automorphism-lifting-criterion applied to verified hypotheses; and nothing geometric follows from it — not the Kähler cone, not the chamber of the item above, not the effectivity of any transported class.
:::

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
3. $\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr)\neq1$ exactly when some $g\in Z_{\Orth(\lkt)}(\theta_\Co)\intersect\Stab_{\Orth(\lkt)}(\tilde h_\Co)$ has $\restrictionof{g}{T_\Co}$ acting nontrivially on $A_{T_\Co}$; the component condition on that restriction is not an extra hypothesis, because it can always be arranged (see the proof).

So each of the two questions is a question about a finite group, and a *witness* for strictness of either inclusion is a single explicit isometry, of $\lkt$ in case (3) and of the Heegner lattice in the other.
:::

::: {.proof}

(1) is the second claim of each of the two propositions, which identifies $\Gamma_\Co$ with the kernel of the respective finite image, together with the first isomorphism theorem; a kernel is everything exactly when the image is trivial.
(2) an isometry of $T_\Co$ has a discriminant image, so each image is a subgroup of the finite group acting on $A_{T_\Co}$, and the order of that group is the one @prop:coble-discriminant-group computes.
(3) unwinds the definition of $\Gamma^\theta_\Co$ as the set of restrictions of the elements of that intersection, so a nontrivial image is a restriction acting nontrivially on $A_{T_\Co}$, and conversely.
The one place the definition is not unwound by itself is the requirement $\restrictionof{g}{T_\Co}\in\Orth^+(T_\Co)$, which is part of the definition of $\Gamma^\theta_\Co$ and is not implied by acting nontrivially on the discriminant.
It is nevertheless free: let $w\in T_\Co$ have $w^2 = 2$ — $\zeta$ of the $\generators{2}$ summand, for instance — so that $s_w\in\ker\rho_{T_\Co}$ and $\spinornorm_\bR(s_w) = [-1]$ by @prop:gamma-co-reflective-set(2) and its proof.
The pair $(\id_{S_\Co}, s_w)$ satisfies the compatibility of @thm:automorphism-lifting-criterion because $\bar s_w = \id$, so it extends to an isometry $\hat h$ of $\lkt$ with $\hat h|_{S_\Co} = \id_{S_\Co}$ and $\hat h|_{T_\Co} = s_w$; then $g\hat h$ commutes with $\theta_\Co$, fixes $\tilde h_\Co$, has restriction $\restrictionof{g}{T_\Co}s_w$ with the same discriminant action as $\restrictionof{g}{T_\Co}$, and spinor norm multiplied by $-1$.
So one of $\restrictionof{g}{T_\Co}$ and $\restrictionof{g}{T_\Co}s_w$ is in $\Orth^+(T_\Co)$, and it lies in $\Gamma^\theta_\Co$ with nontrivial image.
:::

This proposition reduces the two questions but does not by itself decide whether either image is trivial, and by contrast the congruence group is *proved* strictly larger, in the remark below.
The Heegner one is decided in the next two statements: the finite image of the polarization stabilizer is not trivial (@lem:polarization-stabilizer-discriminant-nontrivial), and the surjectivity of the discriminant representation for a $2$-elementary lattice transports that nontriviality into $\Gamma^{\mathrm{Hdg}}_\Co$ itself (@prop:gamma-co-heegner-strict).
The theta one is decided below, in the section on the Coble-side gluing statement: there the analogue of the "equivalently" clause of @prop:gamma-en-two-gluing is not an extra theorem, because the discriminant representation of $T_\Co$ is surjective, and the transported class of a nontrivial $S_\Co$-side isometry is realised by an integral isometry of $T_\Co$ (@prop:theta-co-gluing, @lem:coble-stabilizer-discriminant-nontrivial, @prop:theta-co-index).

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
The order $\abs{G_\Co} = \abs{W(E_8)}$ is proved here and uses no computation.
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
If $\varphi\notin\Orth^+(T_\Co)$, use the repair of @prop:gamma-co-two-definitions(3): $s_\zeta\in\ker\rho_{T_\Co}$ has $\spinornorm_\bR(s_\zeta) = [-1]$, so $(\id_{S_\En}, s_\zeta)$ glues and extends to an isometry $h'$ of $\ten$ with $h'(\delta) = \delta$, $\restrictionof{h'}{T_\Co} = s_\zeta$ and trivial class; hence $h'\in\gent$ with partner $\id_{S_\En}$, and $gh'\in\Stab_{\gent}(\ZZ\delta)$ has restriction $\varphi s_\zeta\in\Orth^+(T_\Co)$ with the same nontrivial class.

So $\Gamma^{\mathrm{Hdg}}_\Co$ contains an element of $\Orth^+(T_\Co)$ acting nontrivially on $A_{T_\Co}$, which by @prop:gamma-co-two-definitions(1) makes the inclusion strict.

*The other inclusion, hence equality.*
Nothing above used anything about $s_v$ except that it lies in $\Stab_{\Orth(S_\En)}(h)$, so the construction applies to every element of that stabilizer and gives $\gamma\,\abs{G_\Co}\,\gamma^{-1}\subseteq\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr)$.
Conversely $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr)\subseteq\gamma\,\abs{G_\Co}\,\gamma^{-1}$: that is the containment in the proof of @prop:gamma-co-in-heegner-group(2), where the image of $\gent$ in $\Orth(q_{\TEn})$ is identified with the $\gamma$-transport of the image of $\Stab_{\Orth(S_\En)}(h)$ (@prop:gamma-en-two-gluing) and $\Gamma^{\mathrm{Hdg}}_\Co$ is the image of $\Stab_{\gent}(\ZZ\delta)\iscontainedin\gent$ under restriction.
So the two images are equal, and by @prop:gamma-co-in-heegner-group(2) the index is their common order.

*The order of $G_\Co$.*
By @prop:polarization-stabilizer-enriques, $\Stab_{\Orth(S_\En)}(h)\iso\Orth(h^{\perp C}) = \Orth\bigl(\generators{-2}\oplus E_8\bigr) = \theset{\pm1}\times W(E_8)$, of order $2\abs{W(E_8)}$; the first factor is the reflection $s_{u_0-w_0}$ in the $\generators{-2}$ direction $u_0-w_0$ of $h^{\perp C}$, and the second is $W(E_8)$ acting on $E_8$.
In the coordinates of $C$ — the module of $S_\En = C(2)$ — an isometry acts on $A_{S_\En} = C/2C$ by its reduction modulo $2$ (@prop:twisted-unimodular-discriminant), each factor acting trivially on the other's summand.
The two factors behave differently there: $s_{u_0-w_0}$ acts nontrivially, since it moves the class of $u_0/2$ (@lem:polarization-stabilizer-discriminant-nontrivial), whereas the element $\id_U\oplus(-\id_{E_8})$, which is the image of $-\id_{E_8} = w_0\in W(E_8)$ and not of $s_{u_0-w_0}$, is trivial modulo $2$.
The $W(E_8)$ factor meets the kernel in $\theset{\pm1}$, because the reduction $W(E_8)\to\Orth(E_8/2E_8)$ has kernel $\theset{\pm1}$ (the identification $W(E_8)\cong 2\Orth^+_8(2)\cdot 2$ of [@CCN+85], under which that reduction is onto $\Orth^+_8(2)\cdot 2$ of order $\abs{W(E_8)}/2$), and $\pm\id_{E_8}$ are the two elements of that kernel.
Hence the kernel of $\Stab_{\Orth(S_\En)}(h)\to\Orth(A_{S_\En})$ is $\theset{1,\ \id_U\oplus(-\id_{E_8})}$, of order $2$, and
$$
\abs{G_\Co} = \frac{2\abs{W(E_8)}}{2} = \abs{W(E_8)} = 696\,729\,600
.$$
:::

::: {.remark title="What the two statements settle"}

@lem:polarization-stabilizer-discriminant-nontrivial and @prop:gamma-co-heegner-strict settle the Heegner half of the comparison: the Heegner description and the stable group are *different* groups, with index exactly $\abs{W(E_8)}$.
The objection that an isometry of $S_\En$ with nontrivial discriminant image "need not have a partner in $T_\Co$" is answered, not waved away: every class of $\Orth(q_{T_\Co})$ is realised by an integral isometry of $T_\Co$ (@thm:two-elementary-surjectivity), every such isometry fixes the gluing class $\zeta/2$ (@prop:coble-discriminant-group), so it glues to the identity on $\ZZ\delta$ (@cor:liftable-automorphisms), and @prop:gamma-en-two-gluing puts the pair in $\gent$.
:::

## The $\theta$-description: the Coble-side gluing statement {#sec-theta-gluing}

The $\theta$-description of $\Gamma_\Co$ is @prop:gamma-co-in-theta-centralizer: the restrictions to $T_\Co$ of the isometries of $\lkt$ that commute with $\theta_\Co$ and fix $\tilde h_\Co$.
Comparing it with $\Gamma_\Co$ needs the Coble analogue of the sentence of @prop:gamma-en-two-gluing that identifies the image of $\gent$ in $\Orth(q_{\TEn})$ with the $\gamma$-transport of the image of an integral stabilizer.
On the Coble side that sentence is not an extra theorem: the discriminant representation of $T_\Co$ is *surjective*, so a class on the $S_\Co$ side can always be lifted on the $T_\Co$ side to an integral isometry, and the pair then glues.

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

The remaining question is therefore about $\rho_{S_\Co}\bigl(\Stab_{\Orth(S_\Co)}(\tilde h_\Co)\bigr)$, and it is answered affirmatively by the same device that settled the Enriques side.
The difference is where the witness comes from: there the nontrivial class was produced by a reflection in $u_0-w_0$, here it comes from the two isotropic classes that make up the degree-$2$ polarization.

::: {.lemma #lem:coble-stabilizer-discriminant-nontrivial title="The $\tilde h_\Co$-stabilizer of $S_\Co$ has nontrivial discriminant image"}

Let $C = \latI_{1,10}$ be the odd unimodular lattice of signature $(1,10)$, so that
$$
C \;\iso\; \generators{K}\oplus U\oplus E_8(-1),
\qquad K^2 = -1,
$$
with $U = \generators{F_1,F_2}$ the hyperbolic plane and $E_8(-1)$ negative definite (@thm:indefinite-unimodular-classification); the sign of $K$ is forced by the signature, $(0,1)+(1,1)+(0,8) = (1,10)$, and $C$ has determinant $+1$ because $\operatorname{sign}C = (-1)^{10}$.
Note that this is *not* the odd unimodular lattice $B = \generators{1}\oplus U\oplus E_8(-1)$ of @prop:tco-as-twist, which has signature $(2,9)$; $S_\Co$ lives in signature $(1,10)$.
Let $S_\Co = C(2)$ with $\tilde h_\Co = F_1+F_2\in S_\Co$ the degree-$2$ Coble polarization of @def:coble-polarization-classes, which is the Enriques-type presentation $h_\Co = F_1+F_2$ with $F_i^2 = 0$ and $F_1\cdot F_2 = 1$ pulled back along the double cover; in $S_\Co = C(2)$ one has $\tilde h_\Co^2 = 2\cdot 2 = 4$, while $u \definedas F_1$ and $w \definedas F_2$ have $u^2 = w^2 = 0$ and $u\cdot w = 2$, with $u+w = \tilde h_\Co$.
Put $v \definedas u-w = F_1-F_2$.
Then $v^2 = -4$, $v$ is primitive, $b(\tilde h_\Co, v) = 0$, and the reflection $s_v$ is an isometry of $S_\Co$ fixing $\tilde h_\Co$ with $\rho_{S_\Co}(s_v)\neq\id$.
Consequently $\rho_{S_\Co}\bigl(\Stab_{\Orth(S_\Co)}(\tilde h_\Co)\bigr)\neq1$.
:::

::: {.proof}

$v^2 = u^2 - 2\,u\cdot w + w^2 = 0-4+0 = -4$, and $b(\tilde h_\Co, v) = u^2 - u\cdot w + w\cdot u - w^2 = 0$, so $s_v(\tilde h_\Co) = \tilde h_\Co$ as soon as $s_v$ is an isometry.

*Primitivity.*
Suppose $v = kx$ with $k\geq2$ and $x$ integral. Then $-4 = v^2 = k^2x^2$, so $k^2\mid 4$ and $x^2 = -4/k^2$; the only integer value left is $k = 2$, giving $x^2 = -1$, and an even lattice has no vector of square $-1$.
(The two halves combine: $b(u,v) = u^2 - u\cdot w = -2 = k\,b(u,x)$ shows $k \mid 2$, so $k$ is $1$ or $2$, and $k = 2$ is excluded as just shown.)
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

By @prop:theta-co-gluing the index is $\abs{\rho_{S_\Co}(\Stab_{\Orth(S_\Co)}(\tilde h_\Co))}$. Write $C = \generators{K}\oplus U\oplus E_8(-1)$ with $K^2 = -1$ and $h = \tilde h_\Co = F_1+F_2$, as in @lem:coble-stabilizer-discriminant-nontrivial, so that $u = F_1$ and $w = F_2$; recall $\Orth(S_\Co) = \Orth(C)$ because $S_\Co = C(2)$.

*The shape of $h^{\perp C}$.*
$h^{\perp C} = \generators{K}\oplus\generators{v}\oplus E_8(-1)$ with $K^2 = -1$, $v = F_1-F_2$ of square $-2$ and the $E_8(-1)$ form; it is negative definite and has determinant
$$
\det(h^{\perp C}) = \det(C)\cdot\frac{[C:\ZZ h\oplus h^{\perp C}]^2}{\det(\ZZ h)} = 1\cdot\frac{4}{2} = 2,
$$
since $\det(\ZZ h) = 2$ and the index is $2$.
Its root system — the vectors of square $-2$ — is exactly $\theset{\pm v}$ together with the $240$ roots of $E_8(-1)$: a vector $x = aK + bv + e$ has
$$
x^2 = -a^2 - 2b^2 + e^2 = -2,
$$
which solves as $e^2 = a^2 + 2b^2 - 2$; since $e^2 \in 2\ZZ_{\leq0}$ we need $a^2 + 2b^2 \leq 2$, and the cases are $a = 0$, $b = 0$ giving $e^2 = -2$ with $e$ a root of $E_8(-1)$; $a = 0$, $b = \pm1$ giving $e = 0$; $a = \pm1$, $b = 0$ giving the odd value $e^2 = -1$; and $a = \pm1$, $b = \pm1$ giving the positive value $e^2 = 1$. The last two do not occur.

*The stabilizer.*
The restriction $\Stab_{\Orth(C)}(h)\to\Orth(h^{\perp C})$ is an isomorphism: an isometry of $h^{\perp C}$ acts trivially on $A_{h^{\perp C}} = \ZZ/2\ZZ$, whose automorphism group is trivial, so the pair $(\id_h,\varphi)$ preserves the glue subgroup of $\ZZ h\oplus h^{\perp C}$ in $C$ and extends by @thm:automorphism-lifting-criterion with $u = \id$.
On $h^{\perp C}$, an isometry permutes roots, and by the count above the roots are the disjoint union of $\theset{\pm v}$ and the root system of $E_8(-1)$; the two components have different ranks, so an isometry preserves each, hence preserves $\generators{v}$ and also its orthogonal complement $\generators{K}\oplus E_8(-1)$, in which the roots span $E_8(-1)$. It therefore preserves $E_8(-1)$ and fixes $\generators{K}$, which is the orthogonal complement of $\generators{v}\oplus E_8(-1)$.
Hence
$$
\Stab_{\Orth(S_\Co)}(\tilde h_\Co) \;\iso\; \theset{\pm1}_K\times\langle s_v\rangle\times \Orth(E_8(-1)), \qquad \abs{\cdot} = 2\cdot2\cdot\abs{W(E_8)} = 4\abs{W(E_8)},
$$
using $\Orth(E_8(-1)) = W(E_8)$, since $-\id = w_0$ lies in $W(E_8)$.

*The image.*
By @prop:twisted-unimodular-discriminant, $\rho_{S_\Co}(g) = \id$ exactly for $g\equiv\id\bmod 2$ on $C/2C$.
Of the three factors: $1$ and $s_K$ are trivial there, because $s_K(x) = x + 2b(x,K)K$ when $K^2 = -1$; $-\id_{E_8}$ is trivial because $-1\equiv1\bmod2$; $s_v$ is not, because $s_v(F_1) = F_1 + b(F_1,v)v = F_1 - v = F_2$ and $F_2 - F_1 = -v$ is not in $2C$, $v$ being primitive; and $W(E_8)$ meets the kernel in $\theset{\pm1}$, that being the kernel of $W(E_8)\to\Orth(E_8/2E_8)$ ([@CCN+85], as in @prop:gamma-co-heegner-strict).
So the kernel has order $2\cdot2 = 4$ and
$$
\abs{\rho_{S_\Co}(\Stab_{\Orth(S_\Co)}(\tilde h_\Co))} = \frac{4\abs{W(E_8)}}{4} = \abs{W(E_8)} = 696\,729\,600
.$$
:::

With @prop:gamma-co-heegner-strict, both candidate overgroups of $\Gamma_\Co$ are strictly larger by the *same* factor $\abs{W(E_8)}$; what remains of @prob:group-identification is the direct and geometric comparison (@prob:coble-rigidity, @prob:B24, @prob:B25), and not the $\theta$ one.

## The congruence comparison {#sec-congruence-comparison}

The congruence group of @prob:group-identification is $\Gamma^{\mathrm{cong}}_{\Co,2} = \rho_{T_\Co}^{-1}(P)$ with
$$
P \definedas \Orth(q_{U(2)})\times\Orth(q_{E_8(2)}) \leq \Orth(A_{T_\Co}, q_{T_\Co}),
$$
made a subgroup of $\Orth(A_{T_\Co},q_{T_\Co})$ by the identity on $\ZZ\tfrac12\zeta$, which is legitimate because every isometry of $q_{T_\Co}$ fixes that class (@prop:coble-discriminant-group).
The two other descriptions are preimages of finite subgroups as well, so the comparison of A20 item 1 is a comparison of three subgroups of one finite group, once the orders and the block structure are known.

::: {.proposition #prop:gamma-cong-eq-heegner title="The Heegner description and the congruence description"}

Let $P$ be as above and let $\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma^\theta_\Co$ be the groups of @prop:gamma-co-in-heegner-group and @prop:gamma-co-in-theta-centralizer.
Then

1. $\abs{\Orth(q_{U(2)})} = 2$ and $\abs{\Orth(q_{E_8(2)})} = \tfrac12\abs{W(E_8)} = 348\,364\,800$, so
   $$
   \abs{P} = 2\cdot 348\,364\,800 = 696\,729\,600 = \abs{W(E_8)}
   ;$$
2. $\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr)$ is a subgroup of $\Orth(q_{T_\Co})$ of order $\abs{W(E_8)}$, contained in the block-preserving part of the *transported* blocks, namely in $\Orth\bigl(\gamma(A_{U(2)})\bigr)\times\Orth\bigl(\gamma(A_{E_8(2)})\bigr)$; consequently
   $$
   \rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr) = P \iff \gamma\bigl(A_{U(2)}\bigr) = A_{U(2)},
   $$
   the condition called **block-compatibility of $\gamma$** below;
3. unconditionally in $\gamma$, $[\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co):\Gamma_\Co] = \abs{W(E_8)}$ and $[\Gamma^{\mathrm{cong}}_{\Co,2}:\Gamma_\Co] = 2\abs{W(E_8)} = 1\,393\,459\,200$, the factor $2$ being $\ker\rho_{T_\Co}\not\subseteq\Orth^+(T_\Co)$; and *under* block-compatibility of $\gamma$ one has $\Gamma^{\mathrm{Hdg}}_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$;
4. $\rho_{T_\Co}\bigl(\Gamma^\theta_\Co\bigr) = \gamma_\Co\,P_{S_\Co}\,\gamma_\Co^{-1}$ where $P_{S_\Co}\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})\leq\Orth(A_{S_\Co},q_{S_\Co})$, so $\rho_{T_\Co}(\Gamma^\theta_\Co)$ has order $\abs{W(E_8)} = \abs{P}$, and the $\theta$-description equals the congruence one exactly when that transport is $P$ itself.

So A20 item 1 is *not* settled unconditionally: it reduces to the single condition that the gluing be block-compatible — for $\gamma$ in the Heegner description, for $\gamma_\Co$ in the $\theta$ one — and only the orders and the indices above are unconditional.
Block-compatibility is a statement about a labeled primitive embedding, and as such it is an instance of @prob:coble-rigidity rather than a free-standing computation.
:::

::: {.proof}

(1) $q_{U(2)}$ takes the values $0,0,0,1$ on the four classes of $A_{U(2)}$: the three nonzero classes are $[e'/2]$, $[f'/2]$ and $[(e'+f')/2]$, with squares $0$, $0$ and $1$, and every pair of distinct nonzero classes has $b = \tfrac12$ in $\QQ/\ZZ$.
An isometry must therefore fix the class of value $1$ and may or may not swap the other two, and both maps preserve $b$; so $\abs{\Orth(q_{U(2)})} = 2$.
For $A_{E_8(2)} = E_8/2E_8$ use the page's own count: the reduction $W(E_8)\to\Orth(E_8/2E_8)$ is onto with kernel $\theset{\pm1}$ ([@CCN+85], as in @prop:gamma-co-heegner-strict), so the image has order $\tfrac12\abs{W(E_8)} = 348\,364\,800$, and that is all of the isometry group, since $\abs{\Orth^+_8(2)} = 2q^{m(m-1)}(q^m-1)\prod_{i=1}^{m-1}(q^{2i}-1)$ at $q = 2$, $m = 4$ is $2\cdot 2^{12}\cdot 15\cdot 3\cdot 15\cdot 63 = 348\,364\,800$; the two computations agree.
Hence $\abs{P} = 2\cdot 348\,364\,800 = 696\,729\,600 = \abs{W(E_8)}$.

(2) $S_\En = U(2)\oplus E_8(2)$, so $A_{S_\En} = A_{U(2)}\perp A_{E_8(2)}$.
Each of the nine generators named in the remark after @prop:polarization-stabilizer-enriques — the reflection $s_{u_0-w_0}$ and the eight reflections in simple roots of $E_8(2)$, which by @prop:gamma-co-heegner-strict generate $\Stab_{\Orth(S_\En)}(h)$ — preserves that splitting: $s_{u_0-w_0}$ acts on the $U(2)$ summand and fixes $E_8(2)$ pointwise, and the eight root reflections fix $U(2)$ pointwise.
So $\rho_{S_\En}\bigl(\Stab_{\Orth(S_\En)}(h)\bigr)\subseteq\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$, and by @prop:gamma-co-heegner-strict
$$
\rho_{T_\Co}\bigl(\Gamma^{\mathrm{Hdg}}_\Co\bigr) = \gamma\,\rho_{S_\En}\bigl(\Stab_{\Orth(S_\En)}(h)\bigr)\,\gamma^{-1}
\subseteq \Orth\bigl(\gamma(A_{U(2)})\bigr)\times\Orth\bigl(\gamma(A_{E_8(2)})\bigr),
$$
a subgroup of $\Orth(q_{T_\Co})$ of order $\abs{W(E_8)}$.
What is *not* on the page is that the gluing $\gamma$ of @prop:gamma-en-two-gluing keeps the $U(2)$ summand on the $U(2)$ summand: the identification $A^0\cong A_{T_\En}$ used in the proof of @prop:gamma-co-in-heegner-group is canonical and block-preserving, but $\gamma$ itself is supplied by @cons:embedding-gluing-data for a primitive embedding and nothing here shows $\gamma(A_{U(2)}) = A_{U(2)}$.
If it does — block-compatibility of $\gamma$ — the image is a subgroup of $P$ of order $\abs{P}$ by (1), hence equal to $P$; if it does not, the image is a subgroup of the same order preserving the transported blocks instead.

(3) Suppose block-compatibility of $\gamma$, so the image is $P$ by (2).
$\Gamma^{\mathrm{Hdg}}_\Co$ is then the preimage of $P$ inside $\Orth^+(T_\Co)$ by @prop:gamma-co-heegner-strict, whose construction produces for each class an element with that class *and* in $\Orth^+(T_\Co)$; hence $\Gamma^{\mathrm{Hdg}}_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ and
$$
\bigl[\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co):\Gamma_\Co\bigr] = \abs{P} = \abs{W(E_8)}.
$$
The full preimage is twice as large, and this needs no hypothesis: $s_\zeta$ has $\zeta^2 = 2$, so $\rho_{T_\Co}(s_\zeta) = \id$ — $s_\zeta(x^*) - x^* = -\beta(x^*,\zeta)\zeta$ with $\beta(x^*,\zeta)\in\ZZ$ — while $\spinornorm_\bR(s_\zeta) = [-1]$ (the component step of @prop:gamma-co-heegner-strict); so $\ker\rho_{T_\Co}\not\subseteq\Orth^+(T_\Co)$ and
$$
\bigl[\ker\rho_{T_\Co}:\Gamma_\Co\bigr] = 2,
\qquad
\bigl[\Gamma^{\mathrm{cong}}_{\Co,2}:\Gamma_\Co\bigr] = 2\abs{P} = 1\,393\,459\,200
.$$

(4) The first equality is @prop:theta-co-gluing. That $\rho_{S_\Co}(\Stab_{\Orth(S_\Co)}(\tilde h_\Co)) = P_{S_\Co}$ is the computation of @prop:theta-co-index: the stabilizer is $\theset{\pm1}_K\times\langle s_v\rangle\times\Orth(E_8(-1))$, its factors act in $K$, in $U$ and in $E_8(-1)$ respectively, its image preserves the three blocks of $A_{S_\Co} = C/2C$ and has order $\abs{W(E_8)} = \abs{P_{S_\Co}}$ by (1), so it is $P_{S_\Co}$.
An isometry conjugates the block decomposition of one side to *a* block decomposition of the other, and $\gamma_\Co$ is an anti-isometry, so the transported group has order $\abs{W(E_8)}$; it equals $P$ if and only if $\gamma_\Co$ carries the $U(2)$ block of $A_{S_\Co}$ to that of $A_{T_\Co}$.
Both directions of that "if and only if" are now argued: if $\gamma_\Co P_{S_\Co}\gamma_\Co^{-1} = P$ then $\gamma_\Co(A_{U(2)})$ is a $P$-invariant two-dimensional subspace of $A^0$, and $A_{U(2)}$ is the only one — a two-dimensional invariant subspace projects to a subspace of the $E_8$ block invariant under $\Orth^+(q_{E_8(2)})$, which acts irreducibly on $E_8/2E_8$, so that projection has dimension $0$ or $8$ and, being of dimension at most $2$, it is $0$; hence the subspace lies in $A_{U(2)}$ and equals it.
Irreducibility is by Witt's extension theorem, not by simplicity: $\Orth(q_{E_8(2)})$ is transitive on the nonzero classes of each value of $q$, so an invariant subspace containing one of the $120$ classes with $q = 1$ — the images of the $240$ roots of $E_8$ — contains all of them, and they span $E_8/2E_8$; and likewise an invariant subspace containing one of the $135$ nonzero isotropic classes contains all of them, and those span as well. So the only invariant subspaces are $0$ and $E_8/2E_8$.

*Why the $\zeta$-block is fixed.*
It is not the value of $q$ that singles out the class $[\zeta/2]\in A_{T_\Co}$, and nor $[K/2]\in A_{S_\Co}$: $528$ classes of $A_{T_\Co}$ have $q = 3/2$, namely $[\zeta/2]$ together with every isotropic class of $A^0$, so a value of $q$ distinguishes nothing. What singles it out is that it is the **characteristic element**: for $C$ odd unimodular, $b_C(x,x)\equiv b_C(x,K) \pmod 2$ for every $x\in C$, so the class $[K/2]$ is the unique class of $A_{S_\Co}$ with $b(x,x) = b(x,[K/2])$ for all $x$; and the same holds for $[\zeta/2]$ in $A_{T_\Co}$ with $B$ in place of $C$.
An isometry preserves $b(x,x)$ and $b$, so it fixes that class, and $\gamma_\Co$ must carry one characteristic element to the other.
:::

::: {.remark title="What part (4) leaves, and what it does not"}

Part (4) is not a gap in the argument but a statement that the page does not fix $\gamma_\Co$ finely enough: the two candidate blocks are distinguished neither by their order — both are four-element subgroups of an elementary abelian group — nor by the values of $q$ on them, and $\gamma_\Co$ is only determined up to the automorphisms of the pair of forms.
What decides it is the gluing isometry as constructed for the embedding $S_\Co\oplus T_\Co\into\lkt$, block by block; the corpus's own `computations/reports/coble_gluing_discriminants.py` checks that construction block by block, and the statement needed here is that its $U(2)$-block matches.
This is the same block-compatibility of @prop:gamma-cong-eq-heegner(2), for $\gamma_\Co$ instead of $\gamma$: with it, $\Gamma^\theta_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ as well; without it, $\Gamma^\theta_\Co$ is a subgroup of index $\abs{W(E_8)}$ over $\Gamma_\Co$ which need not be that one, and the page's data do not decide which.
:::

::: {.remark title="The block decomposition is not $O(q)$-invariant, computed"}

The summand decomposition $A_{S_\Co} = \ZZ(K/2)\perp A_{U(2)}\perp A_{E_8(2)}$ is not invariant under $\Orth(q_{S_\Co})$: that group's orbits on the $2048$ classes are six, of sizes $1,1,496,496,527,527$, and two of them meet the $U(2)$ block without being contained in it, so some isometry of $q_{S_\Co}$ carries a class of that block outside the block. Consequently two anti-isometries $A_{S_\Co}\to A_{T_\Co}(-1)$ that are block-compatible elsewhere differ by an isometry of $q_{S_\Co}$ which moves the block, and block-compatibility is a property of a chosen anti-isometry — never of the pair of forms — which is exactly the condition @prop:gamma-cong-eq-heegner(2) places on the gluing and the reason it is an instance of @prob:coble-rigidity rather than a computation on the discriminant forms. The computation is `computations/reports/coble_gluing_discriminants.py`, transcript `-run.txt`, on the adopted runtime (Sage checkout `281da26ffd`, Sage 11.0.beta5, GAP 4.16.1) with `sage-extensions` at pin `15db925b`. The same test on the side that the Heegner condition of @prop:gamma-cong-eq-heegner(2) actually lives on — $A_{S_\En}$, of order $1024$ — gives the same answer, and that is what makes the condition real there: `computations/reports/coble_a20-block-invariance.py` finds three orbits of $\Orth(q_{S_\En})$ on its $1024$ classes, of sizes $1$, $496$, $527$, and the orbit of size $496$ meets the $U(2)$ block in one class and carries others out of it (witness $[0]+[1]$ inside and $[0]+[1]+[3]+[4]+[5]+[6]+[8]$ outside, both of value $1$), so block-compatibility in the Enriques gluing $\gamma$ is a property of $\gamma$ and not of the pair of forms either.
:::

::: {.remark title="What this does to A20"}
Item 1 of A20 — the comparison of the Heegner group with the congruence group — was recorded as blocked on two owner capabilities: explicit generators of $\gent$, and an explicit isometry of torsion forms.
The first of the two is not needed: generators of the *image* suffice, and they are the nine reflections whose discriminant images @prop:gamma-co-heegner-strict transports, while the congruence subgroup is given by its two factors, whose orders are computed in (1).
The second is exactly what is missing: block-compatibility of $\gamma$ is a statement about an explicit isometry of torsion forms — that the gluing carries the $U(2)$ summand to the $U(2)$ summand — so the explicit torsion-form isometry that A20 recorded as unavailable is what item 1 still needs, and it is not replaced by anything above.
`computations/reports/coble_gluing_discriminants.py` builds the two discriminant forms and their anti-isometry; the check wanted is that its $U(2)$ block is carried to the $U(2)$ block.
That the condition is substantive rather than a formality of the construction is itself computed, on both sides: `computations/reports/coble_gluing_discriminants.py` on $A_{S_\Co}$ (orbits of $\Orth(q_{S_\Co})$ of sizes $1,1,496,496,527,527$, two of them crossing the $U(2)$ block) and `computations/reports/coble_a20-block-invariance.py` on $A_{S_\En}$ (three orbits of sizes $1,496,527$, the $496$ crossing it), so on neither side is the summand decomposition determined by the form.
What remains of A20 beyond that is item 2, item 3, and the four items of the absorbed swarm (#720), none of which is a comparison of two subgroups of $\Orth(A_{T_\Co},q_{T_\Co})$.
:::

::: {.remark title="A20 item 2: the direct and geometric entries are not subgroup comparisons"}

Item 2 of A20 — $\Gamma^{\mathrm{dir}}_{\Co,2}$ against the other two — is not a question of the kind the rest of this section answers, and no finite computation decides it.
$\Gamma^{\mathrm{dir}}_{\Co,2}$ is the image of $Z_{\Orth(\lkt)}(I_\Co, I_{\mathrm{dP}})_{H,\alpha,\mathcal C}$ under restriction to $T_\Co$ (@def:direct-group), so comparing it with $\Gamma^{\mathrm{Hdg}}_\Co$ asks for an isometry of $\lkt$ carrying the Coble-labeled datum to the Enriques-labeled one — the labeled rigidity of @prob:coble-rigidity, and nothing about $\Orth(A_{T_\Co},q_{T_\Co})$ enters it.
$\Gamma^{\mathrm{geom}}_{\Co,2}$ is the monodromy of the direct moduli stack (@def:geometric-monodromy), so it agrees with an arithmetic group only through the direct period and direct monodromy theorems, @prob:B24 and @prob:B25.
What *is* recorded and stands: the pair $(I_\Co,I_{\mathrm{dP}})$ defines a lattice datum whose slot is a $U(2)$ or a $\ZZ H$ inside $S_\Co$, the rank-two case is unique inside $S_\Co$ (`computations/reports/coble_del_pezzo_placement.py`) and the rank-one case exists for every anti-isometry (`computations/reports/coble_rank_one_placement.py`), and no automorphism of the Coble cover realises the slot's involution (@cor:no-del-pezzo-involution-coble-cover); that is why the entry is a *lattice* label and not a geometric group.
So item 2 is handed to @prob:coble-rigidity — where the labeled-conjugacy computation of the A21 discussion lives (@rmk:chamber-not-transported and the scope remark after it) — and item 3 to @prob:B24 and @prob:B25; neither is claimed here.
:::

::: {.remark title="A20 item 3, and the six items absorbed from the swarm"}

Item 3 is the agreement of $\Gamma^{\mathrm{geom}}_{\Co,2}$ with an arithmetic group, and it is a theorem about a moduli stack — the direct global Torelli and the direct monodromy theorem, @prob:B24 and @prob:B25 — with no lattice statement in it; nothing on this page bears on it and none is offered.

The six items absorbed from #720, one line each on what would settle it, so that the issue can be split:
(D1) *monodromy maximality* — an identification of the arithmetic monodromy with $\Gamma^{\mathrm{dir}}_{\Co,2}$, that is the labeled period theorem for the direct stack, not a lattice computation.
(RI) *$\ker\rho_{T_\Co} = W$* — generators of $\ker\rho_{T_\Co}$ and a comparison with the group generated by the $(-2)$-reflections; the reflection group is not finitely presented in any object here and no owner operation returns generators of $\ker\rho_{T_\Co}$, so the index $[\ker\rho_{T_\Co} : W(T_\Co)]$ is the decidable form and it is open.
(REL) *the section relations* — for a section $\sigma\colon P\to G_5$ of $\rho_T$, that $\sigma(p)w\sigma(p)^{-1}\in W$ and $\sigma(p)\sigma(q)\sigma(pq)^{-1}\in W$; it needs the same generators as (RI) plus a section, so it is downstream of (RI).
(INV) *the model-effective arrangement* — that every $g\in Z_{\Orth(\lkt)}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}$ preserves the tuple's $(-2)$-root arrangement; it would follow from an effective-Torelli or lift-to-automorphism input, which is not available for arbitrary lattice isometries and is not a lattice statement.
$G_3$, $G_4$ — untouched, with no formulation on the page to state a requirement against.
None of the six is decided here.
:::

::: {.remark title="A20, closed out: what this section decides and what it hands on"}

What is decided by this section, each with its own record: the stable group is the discriminant-and-spinor kernel and is contained in both candidate overgroups with index $\abs{W(E_8)}$ (@prop:gamma-co-heegner-strict, @prop:theta-co-index); the congruence group is larger by the factor $2$ coming from $\ker\rho_{T_\Co}\not\subseteq\Orth^+$ (@prop:gamma-cong-eq-heegner(3)); and the Heegner description equals the congruence one exactly when the Enriques gluing is block-compatible (@prop:gamma-cong-eq-heegner(2)) — a *real* condition, since neither summand decomposition is $\Orth(q)$-invariant (`computations/reports/coble_gluing_discriminants.py`, `computations/reports/coble_a20-block-invariance.py`).
What is handed on, and to where: item 1's remaining statement and item 2 both become the labeled-embedding question of @prob:coble-rigidity — whether the gluing $\gamma$ of the marked embedding carries the $U(2)$ summand to the $U(2)$ summand — which is a computation on the embedding and not on the abstract pair of forms; item 3 becomes @prob:B24 and @prob:B25; and the six absorbed items are split in the remark above with what each would need.
No further record on this page changes any of that: the issue's remaining content is that one block check, and it lives with the A21 work.
:::

::: {.remark title="What the block-compatibility test decides, once the gluing of the embedding is in hand"}

The test is not a question about the abstract pair of forms, and the two orbit computations below say why: neither the decomposition of $A_{S_\Co}$ nor that of $A_{S_\En}$ is preserved by the full orthogonal group, so *which* anti-isometry $\gamma$ is being tested is part of the data. The test is therefore stated for one $\gamma$ only — the one **induced by the marked embedding**, that is by the overlattice $\lkt$ of $S_\Co\oplus T_\Co$ of index $2048$, respectively of $S_\En\oplus T_\En$ of index $1024$ — and never for an anti-isometry chosen from the forms.
Under that hypothesis the criterion is: $\gamma$ is block-compatible when $\gamma\bigl(A_{U(2)}\bigr) = A_{U(2)}$, the four-element subgroup of the target that the $U(2)$ summand cuts out, and the criterion has exactly two outcomes for @prop:gamma-cong-eq-heegner(2):
if it holds, then $\rho_{T_\Co}(\Gamma^{\mathrm{Hdg}}_\Co) = P$ and $\Gamma^{\mathrm{Hdg}}_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$, while $\rho_{T_\Co}(\Gamma^\theta_\Co) = \gamma_\Co P_{S_\Co}\gamma_\Co^{-1} = P$ gives $\Gamma^\theta_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ as well — so the Heegner and $\theta$ descriptions of $\Gamma_\Co$ are the congruence one and A20 item 1 and the $\theta$ entry of @prob:group-identification are settled affirmatively;
if it fails, then $\rho_{T_\Co}(\Gamma^{\mathrm{Hdg}}_\Co)$ is a subgroup of order $\abs{W(E_8)}$ preserving the *transported* blocks $\gamma(A_{U(2)})\perp\gamma(A_{E_8(2)})$ and not equal to $P$, so $\Gamma^{\mathrm{Hdg}}_\Co$ is a proper subgroup of $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ of the same index $\abs{W(E_8)}$ over $\Gamma_\Co$, and the two descriptions are *different* groups — the negative answer, which is an answer.
What the computation needs, and what the two records above do not supply: the anti-isometry $\gamma$ as a morphism induced by the overlattice, which is `sage-extensions#276` (`gluing_anti_isometry`), and the root $\delta\in T_\En$ with $\delta^{\perp T_\En} = T_\Co$ on the Enriques side, which is `sage-extensions#279`.
What is built already, and verified without them: $\lkt = 3U\oplus 2E_8(-1)$ and the summands $S_\Co = C_S(2)$, $T_\Co = B(2)$, $S_\En = C(2)$ with the ranks $22, 11, 11, 10$, the signatures $(3,19), (1,10), (2,9), (1,9)$, the determinants $-1, 2048, -2048, -1024$ and evenness, and the two orthogonal sums with $\det = -2^{22}$ and $\det = -2^{20}$, into which the recorded indices $2^{11}$ and $2^{10}$ divide correctly (`computations/reports/coble_a21-embedding-build.py`).
:::

## Integral cusp lifting: the map from lattice orbits to discriminant orbits {#sec-cusp-lifting}

@prob:cusp-lifting asks for the $\Gamma_{\Co,2}$-classification of the primitive isotropic *lines* and *planes* of $T_\Co$. It is answered here: the lifting theorem holds (every nonzero isotropic class lifts, the zero class does not), the fibre of the map over a class has *one* $\Gamma_\Co$-orbit because $\rho(\Stab_{\Orth(B)}(v)) = \Stab_{\Orth(q)}(c)$, and the $\Gamma_\Co$-orbits of primitive isotropic vectors, hence the $0$-cusps of $\fco$, number $527$ — one per nonzero isotropic class, a count **proved in prose only** here: no computation record decides it, and the library call that would is sage-extensions#286. For an intermediate group $\Gamma$ they are the $\rho(\Gamma)$-orbits on those $527$ classes; the four finite orbits $135, 2, 270, 120$ are the count for $\Gamma = \rho^{-1}(G_\Co)$ and not for $\Gamma_\Co$.

*The map, and why it is a map of orbits at all.* Let $T_\Co = B(2)$ with $B$ unimodular, so $T_\Co^* = \tfrac12 T_\Co$ and $A_{T_\Co} = B/2B$. A primitive isotropic $v\in T_\Co$ gives the class $[v/2]\in A_{T_\Co}$, of value $q([v/2]) = v^2/4 = 0$, so isotropic; and $\Gamma_\Co = \Orth^+(T_\Co)\intersect\ker\rho_{T_\Co}$ acts **trivially** on $A_{T_\Co}$, since $\ker\rho_{T_\Co}$ is by definition the isometries congruent to the identity modulo $2$.
So $[v/2]$ is a $\Gamma_\Co$-invariant of $v$ — the statement $\rho(g) = \id \iff g\equiv\id\bmod 2$ of §@sec-gamma-co-reflective-set — and there is a well defined map
$$
\bigl\{\Gamma_\Co\text{-orbits of primitive isotropic }v\bigr\}\longrightarrow \bigl\{\text{isotropic classes of }A_{T_\Co}\bigr\},
\qquad
\Gamma_\Co\cdot v\longmapsto [v/2],
$$
and likewise for primitive isotropic planes $P\subset T_\Co$, whose image is the subgroup $(P\cap \tfrac12T_\Co)/T_\Co$ … more precisely the isotropic subgroup $[P/2]$ of $A_{T_\Co}$, of order $4$, spanned by the classes of a basis.

*Step 1: $\Orth(B)$ is transitive.* $B = \generators{1}\perp U\perp E_8(-1)$ is odd, unimodular, indefinite, of rank $11$. Wall classifies the orbits of $\Orth(B)$ on primitive vectors of an indefinite unimodular lattice of rank $\ge3$ by norm and type, characteristic or ordinary ([@Wal62], Theorem 1.2 and §1.3). A primitive isotropic $v$ has $v^2 = 0$, and it is *not* characteristic: a characteristic vector $w$ of a unimodular lattice satisfies $w^2\equiv \sigma(B) \pmod 8$ (van der Blij; [@Nik80], §1.9), and here $\sigma(B) = 2-9 = -7\equiv 1\pmod 8$, so $w^2$ is odd, while $v^2 = 0$ is even. So all primitive isotropic vectors of $B$ have norm $0$ and ordinary type, and there is exactly **one** $\Orth(B)$-orbit of them.
Consequently the class $[v/2]\in B/2B$ is *not* an $\Orth(B)$-invariant — an isometry moves it by $\bar g$ — while it *is* a $\Gamma_\Co$-invariant, since $\Gamma_\Co$ is the congruence subgroup $\bar g = \id$. So $\Gamma_\Co$ does not act transitively, and the finite lists cannot be its orbits.

*Step 2: the fibres are cosets of the stabilizer image.* $\rho_{T_\Co}\colon\Orth(B)\to\Orth(q_{T_\Co})$ is onto for a $2$-elementary lattice ([@Nik80], 1.14.2 and Theorem 3.6.3 — @thm:two-elementary-surjectivity). Write $K_\rho=\ker\rho$, which is normal, and $\Gamma_\Co=K_\rho\intersect\Orth^+(B)$. For a primitive isotropic $v$ with class $c = [v/2]$ the orbit $K_\rho\cdot v$ depends only on the coset of $\Orth(B)$ modulo $K_\rho$, so
$$
\theset{K_\rho\text{-orbits inside } \Orth(B)\cdot v \text{ with class } c}
\;\iso\;
\Stab_{\Orth(q)}(c)\,\big/\,\rho\bigl(\Stab_{\Orth(B)}(v)\bigr),
$$
and the number of $K_\rho$-orbits of primitive isotropic vectors is
$$
\sum_{c}\;\bigl[\Stab_{\Orth(q)}(c) : \rho(\Stab_{\Orth(B)}(v_c))\bigr],
$$
the sum over the isotropic classes $c\in A_{T_\Co}$, which are the $528$ classes of @prop:coble-q-fibers, with $v_c$ any primitive isotropic lift.

*The classes that lift, and the lifting theorem.* The $528$ classes of @prop:coble-q-fibers include the zero class, since $A_{T_\Co} = B/2B = \F_2^{11}$ and $1+135+2+270+120 = 528$ counts the solutions of $x^2\equiv0 \pmod 4$ with $x = 0$ included. The zero class is $[v/2]$ only for $v\in 2B$, which is not primitive, so it contributes no term. Which classes do lift is decided as follows.
Let $\bar w$ be the class of a characteristic vector $w$ of $B$: it is the unique class with $b(\bar w,\bar x)=q(\bar x)$ for all $\bar x$ in the common $\F_2$ reduction, hence $\Orth(q)$-invariant. Since $b(\bar w,\bar w)=w^2/2$ is nonzero modulo $\ZZ$, $A_{T_\Co}=\generators{\bar w}\perp\bar w^\perp$, and $w^2\equiv1\pmod8$ gives $q(\bar w)=w^2/2\equiv1/2\pmod{2\ZZ}$ (taking $w^2=1$). On $\bar w^{\perp}$, of dimension $10$, the form $q$ is $\F_2$-valued, nondegenerate and of **plus** type: its nonzero singular vectors number $(2^5-1)(2^4+1) = 527$, and $\abs{\Orth(q)} = \abs{\Orth^+_{10}(2)} = 46\,998\,591\,897\,600$ is the order @prop:coble-discriminant-group records. By Witt's theorem for quadratic forms over $\F_2$ that group is transitive on those $527$ vectors.
Now combine the three: Step 1 gives one $\Orth(B)$-orbit of primitive isotropic vectors; $\rho$ is onto; and $\rho$ carries $\Orth(B)$-orbits to $\Orth(q)$-orbits. So the classes $[v/2]$ of primitive isotropic vectors form a single $\Orth(q)$-orbit of isotropic classes, which by the count above is the set of all $527$ nonzero isotropic classes. That is the lifting theorem:
$$
\theset{[v/2] : v\in T_\Co \text{ primitive isotropic}} = \theset{\text{the } 527 \text{ nonzero isotropic classes}},
$$
every nonzero isotropic class has a primitive isotropic lift and the zero class does not.

*The index is $1$: $\rho(\Stab_{\Orth(B)}(v)) = \Stab_{\Orth(q)}(c)$.* Write $B = U\perp K$ with $v$ spanning one isotropic line of $U$, so that $K \definedas v^{\perp}/v \iso \I_{1,8}$, odd unimodular of signature $(1,8)$; then $\Orth(K)\iscontainedin\Stab_{\Orth(B)}(v)$ as the isometries fixing $U$ pointwise, and the stabilizer also contains the Eichler transvections $E(v,k)$ for $k\in v^{\perp}$ with $k^2$ even ([@Eic74]; [@GHS08], §3).
Under $\rho$, $\Orth(K)\to\Orth(q_{K(2)})$ is onto, since $K(2)$ is even, indefinite and $2$-elementary of rank $9$ ([@Nik80], 3.6.3), and $q_{K(2)}\iso q|_{c^{\perp}/c}$ with $c = [v/2]$; so $\rho(\Stab(v))$ maps onto the Levi quotient $\Stab_{\Orth(q)}(c)/N$, where $N$ is the kernel of $\Stab(c)\to\Orth(c^{\perp}/c)$. That kernel has order
$$
\abs{N} = \frac{\abs{\Stab_{\Orth(q)}(c)}}{\abs{\Orth(c^{\perp}/c)}} = \frac{\abs{\Orth(q)}/527}{\abs{\Orth^+_8(2)}} = \frac{89\,181\,388\,800}{348\,364\,800} = 2^8 .
$$
The images $\rho(E(v,k))$ lie in $N$, and $\rho(E(v,k)) = \id\iff k\in \ZZ v + 2B$, so they form a group isomorphic to $K_{\mathrm{ev}}/2K$ of order $2^8 = \abs{N}$. Hence $\rho(\Stab_{\Orth(B)}(v)) = \Stab_{\Orth(q)}(c)$ — the index is $1$, not larger — and the number of $\Gamma_\Co$-orbits of primitive isotropic vectors is
$$
\abs{\Orth(q)}/\abs{\Stab_{\Orth(q)}(c)} = 527,
$$
one per nonzero isotropic class. Since $-\id\in\ker\rho_{T_\Co}\intersect\Orth^+(B)$ (signature $(2,9)$), vectors and lines give the same count.

*The spinor restriction does not split a fibre.* The preceding computation is for $K_\rho=\ker\rho$, whereas $\Gamma_\Co=K_\rho\intersect\Orth^+(B)$. Write $B=U_1\perp K_v$ with $v=e_1$ in the first hyperbolic plane and $K_v\cong\I_{1,8}$. The isometry $g=\id_{U_1}\oplus(-\id_{K_v})$ fixes $e_1$, is the identity modulo $2$ on both blocks, and is spinor-negative: $\spinornorm_\bR(-\id_{K_v})=-1$ by @lem:minus-identity-spinor-norm at positive index one. Hence $g\in K_\rho\intersect\Stab_{\Orth(B)}(e_1)\setminus\Orth^+(B)$. Since $[K_\rho:\Gamma_\Co]=2$ and the stabilizer of $e_1$ in $K_\rho$ likewise meets both spinor classes, the $K_\rho$-orbit and the $\Gamma_\Co$-orbit of $e_1$ have the same cardinality; in fact they coincide, because every vector of the former is reached by an element which can be corrected by $g$ or by the identity. At any other liftable class $c=[v_c/2]$, choose $h\in\Orth(B)$ with $h(e_1)=v_c$; then $hgh^{-1}$ fixes $v_c$, lies in $K_\rho$ by normality, and is again spinor-negative. The same conclusion therefore holds at every liftable class: no $\Gamma_\Co$-class loses an orbit when $\Gamma_\Co$ replaces $K_\rho$. The $527$ fibres therefore remain singletons under the actual stable group, not merely under the full discriminant kernel. The exact line and plane witnesses, together with the integral block maps used below, are checked in `computations/reports/coble_integral-lifting-structure.py` and its run.

*Consequences, and where the finite lists sit.* For any group $\Gamma$ with $\ker\rho\iscontainedin\Gamma\iscontainedin\Orth(B)$, the $\Gamma$-orbits of primitive isotropic vectors are in bijection with the $\rho(\Gamma)$-orbits on the $527$ nonzero isotropic classes, the $527$ being **proved in prose only**, with sage-extensions#286 the computation owed. The four finite orbits $135,\,2,\,270,\,120$ are therefore exactly the orbits for $\Gamma = \rho^{-1}(G_\Co)$, where $G_\Co$ is the image of the degree-$2$ parabolic stabilizer of order $\abs{W(E_8)}$ (@prop:polarization-stabilizer-enriques, @prop:gamma-co-heegner-strict), and the computation `computations/reports/coble_gco_orbit-decomposition.py` gives them. The page's stable group is $\Gamma_\Co = \Orth^+(B)\intersect\ker\rho$, whose image is trivial, so its $0$-cusp count is $527$; for $O(B)$ itself it is $1$, the transitivity of @thm:unpolarized-cusps. The four numbers are the count for the *intermediate* group $\rho^{-1}(G_\Co)$, not for $\Gamma_\Co$.

*Planes: the same two steps, with the complement proved.*
Let $P\subset B$ be a primitive isotropic plane and $K_P \definedas P^{\perp B}/P$.
$P$ is primitive of rank $2$ and isotropic, so $P^{\perp B}$ has rank $9$ and $K_P$ rank $7$, and $K_P$ is unimodular: the index of $\ZZ$-sublattices $P\oplus P^{\perp}$ in $P^{\perp}$ has square $\det(P^{\perp})/\det(P)$ … equivalently $B$ unimodular forces $K_P$ unimodular. Its signature is $(0,7)$, so $K_P$ is a definite unimodular lattice of odd determinant sign, hence odd; an even definite unimodular lattice has rank divisible by $8$, so there is none of rank $7$; and there is exactly one odd definite unimodular lattice in each rank below $9$, namely $\I_{0,7} = \generators{-1}^{7}$ (the classification of odd unimodular forms, [@Nik80], §1.8; the rank-$8$ exception $E_8$ is even and does not occur here).
So $K_P \iso \I_{0,7}$ for every such $P$, and $B\iso U\perp U\perp\I_{0,7}$ with $P$ the isotropic plane of the $U\perp U$ summand — whence any two primitive isotropic planes of $B$ are carried to each other by an isometry of $B$: **one $\Orth(B)$-orbit**, the plane analogue of Step 1 and proved without invoking Wall.
For the fibre, let $J \definedas [P/2]\leq A_{T_\Co}$ be the order-$4$ isotropic subgroup the plane spans, and compare $\Stab_{\Orth(q)}(J)$ with $\rho\bigl(\Stab_{\Orth(B)}(P)\bigr)$ exactly as in the vector case: the $\Gamma_\Co$-orbits over $J$ are $\Stab_{\Orth(q)}(J)/\rho(\Stab_{\Orth(B)}(P))$, and the $1$-cusp count for $\Gamma$ is the number of $\rho(\Gamma)$-orbits of liftable order-$4$ isotropic subgroups, each fibre being that index.
The Levi part of $\Stab_{\Orth(B)}(P)$ is $\Orth(\I_{0,7})$, of order $2^7\cdot 7! = 645\,120$, and its image lies in $\Orth(q_{\I_{0,7}(2)}) = \Orth(\generators{-\tfrac12}^{7})$ on the seven coordinates of $K_P/2K_P$; that image is *not* covered by Nikulin's surjectivity, which needs an indefinite lattice, $K_P(2) = \generators{-2}^{7}$ being definite. The exact index and the count of liftable order-$4$ subgroups are exactly the computation the library does not yet expose: it needs the $\Gamma$-orbits of primitive isotropic planes of $T_\Co$ with their stabilizers, that is the public call `sage-extensions#286` (the $\Gamma$-orbits of primitive isotropic vectors and planes of $T_\Co$ with incidence, as one call), whose owner is sage-extensions. **No pure-Python orbit computation is run here for it**: the research pages rest on library calls, and this is the missing one.

::: {.proposition #prop:coble-planecusp-finite title="The finite images of the plane cusp map: liftable means all, and the count is 23715"}
With $B$, $T_\Co = B(2)$, $\rho$ and $A = A_{T_\Co}$ as in this section:

1. Every primitive vector $p$ of a primitive isotropic plane $P\subset B$ has $T_\Co$-divisibility $2$ and nonzero class: the pairing $B\to P^*$, $b\mapsto(p\mapsto(p,b))$ is onto because $B$ is unimodular and $P$ primitive, so $\operatorname{div}_B(p) = 1$ and $\operatorname{div}_{T_\Co}(p) = 2$; and $P\intersect 2B = 2P$ by primitivity, so $[p/2]\neq 0$. The subgroup $J(P)\definedas\im(P/2)\leq A$ is isotropic of order $4$, the classes of $P$'s primitive vectors are exactly the three nonzero elements of $J(P)$, and $\rho(g)(J(P)) = J(g(P))$.

2. **Every order-$4$ isotropic subgroup is liftable.** $\Orth(q)$ is transitive on them: they are the totally isotropic $2$-planes of the plus-type $\bar w^{\perp}$, below its Witt index $5$, so Witt transitivity over $\F_2$ applies; with $\rho$ onto, every such $J$ is $J(gP)$ for some $g\in\Orth(B)$.

3. **They number $23715 = 527\cdot 270/6$.** For each nonzero isotropic $u$, the isotropic $v\in u^{\perp}\sm\generators{u}$ number $270$: $u^{\perp}/\generators{u}$ is plus-type of dimension $8$ with $135$ nonzero singular vectors, and each lifts to the two partners $au+w$. Division by $\abs{GL_2(\F_2)} = 6$ gives the count of subgroups. Computed exactly, by the pair count and by direct enumeration of the totally isotropic $2$-planes: `computations/reports/coble_planecusp-finite-images.py`, transcript `coble_planecusp-finite-images-run.txt` — $528$ isotropic classes, $527$ nonzero, the partner count uniformly $270$, $23715$ subgroups. This is the number GAPS.md records and the sum $1575+270+9450+3780+8640$ of the five published plane sizes.

4. $\abs{\Stab_{\Orth(q)}(J)} = \abs{\Orth(q)}/23715 = 1\,981\,808\,640 = 2^{21}\cdot 3^3\cdot 5\cdot 7$, while the on-record image $H$ of the $119$ setwise-stabilizer generators of a plane has order $247\,726\,080 = 2^{18}\cdot 3^3\cdot 5\cdot 7$: the index is $8$.
:::

::: {.theorem #thm:coble-plane-stabilizer-image title="The integral plane stabilizer, its discriminant image, and the failure of plane lifting"}
Let $B = U\perp U\perp\generators{-1}^{7}$ with isotropic generators $e_1,f_1$ and $e_2,f_2$ of the two hyperbolic planes, $P = \generators{e_1,e_2}$ the standard primitive isotropic plane, $D = \generators{-1}^{7} = P^{\perp B}/P$, and $J = \im(P/2)$. Then:

1. **(Parabolic factorization.)** $\Stab_{\Orth(B)}(P) = L\ltimes U$ where the Levi $L\cong GL_2(\ZZ)\times\Orth(D)$ consists of the isometries preserving the *Witt decomposition* $B = P\oplus\generators{f_1,f_2}\oplus D$ — $P$ and $D$ orthogonal, $\generators{f_1,f_2} = B/P^{\perp B}\cong P^*$ orthogonal to $D$ and in hyperbolic duality with $P$, carrying the contragredient $GL_2$-action — and $U$ is the unipotent radical, the kernel of the action on $P$ and on $P^{\perp B}/P$. The exact hypothesis of the factorization is the surjectivity of $\Stab_{\Orth(B)}(P)\to GL(P)\times\Orth(P^{\perp B}/P)$, exhibited by the elements $\gamma\oplus(\gamma^{-1})^{T}\oplus\delta$ of the Witt decomposition, the diagonal action in the block order $P$, $P^*$, $D$.

2. **(Discriminant actions on generators.)** Coefficients of $\F_2$-vectors are taken with $\beta \definedas 2b \bmod 2$, i.e. $\beta([x/2],[y/2]) = (x,y)_B \bmod 2$, the same normalization as item 3 governing both. With $j_i = [e_i/2]$ and $\bar w = [w/2]$: the transposition of the two $U$-summands and the shear of $GL_2(\ZZ)$ reduce mod $2$ to the $S_3$ on $J$; the signed permutations of $D$ reduce to the coordinate permutations $S_7$ on the seven classes $\bar d_i$ (signs act trivially mod $2$, so $\rho(\Orth(D))\cong S_7$ of order $5040$ inside $\Orth(\generators{-\tfrac12}^{7})$); the Siegel–Eichler elements of $U$ — $\sigma = E_{e_1,e_2}$, which fixes $P$ and $P^{\perp B}$ pointwise, and $E_{e_i,w}$ for $w\in D^{\mathrm{ev}}$ (the even sublattice, $w^2$ even) — map to $\bar x\mapsto\bar x + \beta(\bar x,j_i)\bar w + \bigl(\beta(\bar x,\bar w) + \tfrac{w^2}{2}\beta(\bar x,j_i)\bigr)j_i$ and to the transvection $\bar x\mapsto\bar x + \beta(\bar x,j_1)j_2 + \beta(\bar x,j_2)j_1$, the integral Eichler formula reducing with this same $\beta$.

3. **(The image, and the generators attain it block by block.)** The discriminant forms are normalized throughout by
$$ b\bigl([x/2],[y/2]\bigr) = \tfrac{(x,y)_B}{2}\ \mathrm{mod}\ \ZZ, \qquad q\bigl([x/2]\bigr) = \tfrac{(x,x)_B}{2}\ \mathrm{mod}\ 2\ZZ . $$
$U$ fixes $P$ and $P^{\perp B}/P$ pointwise, so $\rho(U)$ fixes $J$ and $J^{\perp}/J$ pointwise and lies in the unipotent radical of $\Stab_{\Orth(q)}(J)$; the Levi image is $S_3\times S_7$ of order $30240$. The unipotent radical's order $2^{13}$ is read off the block parameters: in the Witt block order $J\oplus J^*\oplus V_6$ of the plus-type ten-space $\bar w^{\perp}$ (matching $P\oplus P^*\oplus D$ on the integral side), its elements are the block matrices with identity diagonal blocks, the free parameters being the $\Hom(J,V_6)$-blocks — $2\times 6$ over $\F_2$, hence $2^{12}$ — and the $J$-valued block, whose two surviving elements are derived from its quadratic equations: a $J$-block map $\bar x\mapsto\bar x + a_1\beta_1 j_1 + a_2\beta_1 j_2 + a_3\beta_2 j_1 + a_4\beta_2 j_2$ (with $\beta_i = \beta(\bar x,j_i)$, $a_i\in\F_2$) preserves $q$ iff $a_1\beta_1 + (a_2+a_3)\beta_1\beta_2 + a_4\beta_2 \equiv 0$ identically — since $q(\bar x+\delta) = q(\bar x)+\beta(\bar x,\delta)$ and $q(\delta) = 0$ on $J$ — which forces $a_1 = a_4 = 0$ and $a_2 = a_3$, leaving exactly the identity and the transvection $\bar x\mapsto\bar x+\beta(\bar x,j_1)j_2+\beta(\bar x,j_2)j_1$. So $2^{12}\cdot 2 = 2^{13}$. The integral generators attain each block: the classes $[w/2]$ of the even sublattice $D^{\mathrm{ev}}$ are exactly the even-weight classes, i.e. all of $V_6$, so the $E_{e_i,w}$ realize the full $\Hom(\generators{j_i},V_6)$ for each $i$, and $\sigma = E_{e_1,e_2}$ realizes the central block. Hence
$$ \abs{\rho\bigl(\Stab_{\Orth(B)}(P)\bigr)} \;=\; 30240\cdot 2^{13} \;=\; 247\,726\,080 , $$
and the $119$ verified setwise-stabilizer generators recorded in `computations/reports/coble_plane-half-f2.py` have image of exactly this order, confirming the blockwise attainment: the generators are exhaustive and the computed order $|H|$ is a *consequence* of the structure, not an assumption. Independently of that order computation, `computations/reports/coble_integral-lifting-structure-run.txt` checks the Witt Levi blocks, every integral Eichler block, the characteristic-line and $V_6$ forms, and both spinor witnesses used in the fibre argument.

4. **(The index is structural.)** $\bqty{\Stab_{\Orth(q)}(J) : \rho(\Stab_{\Orth(B)}(P))} = 8 = \bqty{\Orth^+(6,2) : S_7} = \bqty{S_8 : S_7}$. Here $J^{\perp}/J$ is seven-dimensional over $\F_2$, spanned by the classes $\bar d_i = [d_i/2]$, and carries the descended quadratic form ($J$ is totally isotropic and $b(J,J^{\perp}) = 0$, so $q(x+j) = q(x)$). The characteristic class is $\bar w' = [w/2]$ with $w = \sum_i d_i$: $B(w,w) = -7$, so $q(\bar w') = -\tfrac72 \equiv \tfrac12$ and — the point the bilinear normalization settles — $b(\bar w',\bar w') = -\tfrac72 \equiv \tfrac12 \neq 0$: the characteristic line is **not** in the bilinear radical. Its canonical orthogonal complement is
$$ V_6 \definedas (\bar w')^{\perp} \cap J^{\perp}/J = \theset{\text{even-weight classes } \textstyle\sum c_i \bar d_i : \sum c_i \equiv 0 \pmod 2} , $$
six-dimensional, and $J^{\perp}/J = \ZZ\bar w' \perp V_6$ with the orthogonal direct sum canonical. On $V_6$ the form is $q(\sum c_i \bar d_i) = -\tfrac{\mathrm{wt}}{2} \bmod 2$ with $\mathrm{wt} = \sum c_i$ even, hence $\F_2$-valued; it is nondegenerate of **plus** type, proved by the zero count: the even-weight classes with $q = 0$ are those of weight $\equiv 0 \pmod 4$, and they number $\binom70 + \binom74 = 1 + 35 = 36 = 2^5 + 2^2$, the plus-type count $2^{2m-1}+2^{m-1}$ at $m = 3$ (equivalently, the generating identity $\sum_{c \in \F_2^7} \mathrm{i}^{\mathrm{wt}(c)} = (1+\mathrm{i})^7$ splits the $64$ even-weight classes $36/28$ by weight $\equiv 0$ vs $\equiv 2 \bmod 4$). The finite stabilizer's Levi is $S_3\times\Orth^+(6,2)$, with $\Orth^+(6,2)\cong S_8$ acting on $V_6$ and fixing $\bar w'$, which is characteristic. The integral Levi is the isometry group of the *definite* lattice $D\cong\generators{-1}^{7}$, the signed permutation group of order $2^7\cdot 7!$, whose mod-$2$ image is only the $S_7$ permuting the $\bar d_i$. The missing eight cosets are exactly the non-permutation part of $\Orth^+(6,2)$, and **no integral isometry of $B$ stabilizing $P$ realizes them**: any such isometry induces an isometry of $P^{\perp B}/P\cong\generators{-1}^{7}$, a finite group with mod-$2$ image $S_7$. This is the definite-quotient obstruction: it is not a gap in the generator list but a property of the lattice.

5. **(Consequence: the orbit-fibre count.)** *Assume $\ker\rho\iscontainedin\Gamma\iscontainedin\Orth(B)$.* Write $Q = \rho(\Orth(B)) = \Orth(q)$, $H = \rho(\Gamma)\leq Q$, $F = \Stab_Q(J)$ and $S = \rho\bigl(\Stab_{\Orth(B)}(P)\bigr)$. The fibre over $J$ is the orbit of $P$ under $\rho^{-1}(F)$, and the $\Gamma$-orbits on it are the double cosets
$$ \bigl(\Gamma\intersect\rho^{-1}(F)\bigr)\bigl\backslash \rho^{-1}(F) \big/ \Stab_{\rho^{-1}(F)}(P) , $$
which, since $\ker\rho\iscontainedin\Gamma$, reduce modulo $\ker\rho$ to $F$-double cosets. Over a translate $qJ$ with $q\in Q$ and any lift $\tilde q\in\Orth(B)$, conjugate: the fibre is the orbit of $\tilde q(P)$ under $\rho^{-1}(qFq^{-1})$ and the $\Gamma$-orbits on it are the double cosets of $\Gamma\intersect\tilde q\rho^{-1}(F)\tilde q^{-1}$ inside $\rho^{-1}(qFq^{-1})$, reducing to
$$ \bigl(q^{-1}Hq\intersect F\bigr)\bigl\backslash F \big/ S $$ The two anchor cases: $H = 1$, that is $\Gamma = \ker\rho$, gives $\abs{F/S} = 8$ orbits per subgroup — the plane lifting theorem *fails* for the Coble family — while $H = Q$, that is $\Gamma = \Orth(B)$, gives a single double coset over the whole $23715$, the one $\Orth(B)$-orbit of planes of this section. For the page's stable group $\Gamma_\Co = \Orth^+(B)\intersect\ker\rho$, whose image is also trivial, the fibres are the same eight $\ker\rho$-orbits *provided* none of them splits under the spinor restriction — and none does. The witness is the Levi isometry $\tau = -\id_{U_1}\oplus\id$ acting as minus the identity on the first hyperbolic plane and the identity on $U_2\perp D$: it stabilizes $P$ setwise ($\tau(e_1) = -e_1$, $\tau(e_2) = e_2$), it is the identity modulo $2$ (so $\tau\in\ker\rho$), and it is spinor-negative under the normalized real spinor norm of @sec-lattice-spinor-norm: on $U_1$ it factors as $\tau = s_{e_1-f_1}s_{e_1+f_1}$, a reflection in the negative vector $e_1-f_1$ of square $-2$ — positive sign — composed with a reflection in the positive vector $e_1+f_1$ of square $2$ — negative sign — so $\tau$ reverses one positive direction and has negative sign, equivalently $\spinornorm_\bR(-\id_{U_1}) = [(-1)^1] = -1$ by @lem:minus-identity-spinor-norm at positive index one. (A reflection in a negative vector has *positive* sign under the normalized convention, which is why the sign change $-\id_D$ of the definite summand, a product of seven negative-vector reflections, is spinor-positive and is *not* the witness.) The spinor class is conjugation-invariant, so every conjugate stabilizer $k\Stab(P)k^{-1}$ contains the spinor-negative $k\tau k^{-1}$, and no $\ker\rho$-orbit in any fibre splits. Hence the $1$-cusp count for $\Gamma_\Co$ is $8\times 23715 = 189\,720$, and for a general $\Gamma$ it is the sum of the double-coset counts over the $H$-orbits of the $23715$ subgroups of @prop:coble-planecusp-finite — a count that remains subject to the known-family and card dependencies, as everything on this page does.
:::

::: {.remark #rmk:coble-planecusp-boundary title="Why the Enriques kernel-transitivity does not transport"}
The fibre statement just computed is *not* the Enriques lemma of the degree-two family transported. The two full discriminant forms are not isometric — $A_{T_\En}$ has order $1024$ and $A_{T_\Co}$ order $2048$ — and the actual relationship is that $A_{T_\En}$, a plus-type ten-dimensional $\F_2$-form, is isometric to the characteristic complement $\bar w^{\perp}$ inside $A_{T_\Co}$. The reason the Enriques fibre argument does not transport is not that finite relationship but the *integral* one: that argument runs [@Ste91, Cor. 3.3], whose engine is the Siegel–Eichler transformation along an isotropic vector of an $H(2)$-summand, and those transformations lie in the level-$2$ kernel only because $H(2)$'s isotropic vectors pair *evenly* with the whole lattice — the $U + U(2)$ hypothesis. $B$ is unimodular: its isotropic vectors pair by units, the transvections along them are not level-$2$, and the parabolic and level-two structure that replaces them is @thm:coble-plane-stabilizer-image. The Coble replacement is @thm:coble-plane-stabilizer-image: the parabolic arithmetic with its definite Levi quotient, which decides the fibre exactly — by the index $8 = [S_8 : S_7]$ — rather than by a transitivity that does not hold here.
:::

::: {.proposition #prop:stabilizers-conjugate title="The stabilizers of the polarized $0$-cusps are conjugate"}

Let $T_\Co = B(2)$ and $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$, and let $v, v'\in T_\Co$ be primitive isotropic vectors with $v' = gv$ for some $g\in\Orth(T_\Co)$, which exists by @thm:unpolarized-cusps.
Then

1. $\Gamma_\Co$ is normal in $\Orth(T_\Co)$, and $\Stab_{\Gamma_\Co}(v') = g\,\Stab_{\Gamma_\Co}(v)\,g^{-1}$;

2. the subgroups of $\Orth(v^{\perp T_\Co}/\generators{v})$ and of $\Orth((v')^{\perp T_\Co}/\generators{v'})$ induced by those stabilizers are carried onto one another by the isometry $\bar g$ that $g$ induces on the quotients;

3. consequently the datum of @qst:sterk-reflection-subgroup is **one** subgroup $G\leq\Orth(\latI_{1,8}(2))$, up to isometry, at every polarized $0$-cusp, and its index is one number and not $527$ of them.
:::

::: {.remark title="The normality this uses fails on the Enriques side"}

Step 3 uses that $\Gamma_\Co$ is normal in $\Orth(T_\Co)$, so that the stabilizers at two cusps are conjugate in $\Orth(T_\Co)$ and the induced subgroups are carried onto one another. Nothing of the kind holds for $\gent\subset\Orth(T_\En)$, which is a level-two subgroup and not normal: the four divisibility-two Enriques cusps lie in four different $\gent$-orbits, and the class stabilizers inside $M$ have orders $348\,364\,800$, $5\,806\,080$, $2\,580\,480$ and $5\,160\,960$ at cusps $2,3,4,5$ respectively (@thm:sterk-reflection-subgroups). The unit of that theorem is the $\gent$-orbit of a $0$-cusp, not the isometry class of the quotient, which is why the four published Enriques diagrams can differ while their quotient lattices coincide.
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
$\Gamma_\Co$ has $527$ orbits of primitive isotropic vectors, one per nonzero isotropic class --- a page proof, with the public lattice-orbit computation remaining sage-extensions#286.
:::

::: {.proof}

Coordinates as above: $B = U_1\oplus U_2\oplus\generators{-1}^{7}$, $v = e_1$, $K = U_2\oplus\generators{-1}^{7}$ with the $\I_{1,8}$-adapted basis $v_0 = e+f+g_1$, $v_1 = e+g_1$, $v_2 = f+g_1$, $v_3,\dots,v_8 = g_2,\dots,g_7$; the nine walls of @thm:zero-cusp-chambers substituted through that dictionary have exactly the printed chamber Gram matrix.

(1) An element of $\Orth(B)$ fixing $e_1$ and acting trivially on $K$ sends $f_1\mapsto f_1+\alpha e_1+w$ with $w\in\I_{1,8}$, and integrality of its norm forces $\alpha = -w^2/2$; such elements exist exactly for $w^2$ even and are the transvections
$$
E_B(e_1,w)(x) = x - \beta_B(w,x)e_1 + x_1w - \tfrac{w^2}{2}x_1e_1 ,
$$
where $x_1 = \beta_B(x,e_1)$.
Modulo $2$ this is $x\mapsto x + \overline{\beta_B(w,x)}\,\overline{e_1} + x_1\overline{w} + \overline{\tfrac{w^2}{2}}\,x_1\overline{e_1}$: the $\tfrac{w^2}{2}$ term sits on $\overline{e_1}$ and not on $\overline{w}$, and the parity condition on $w$ is what keeps $\alpha$ integral --- admitting odd-square $w$ gives maps that fail $q$-preservation, which is how the check caught the earlier version of this statement.
The record builds the maps for $w$ running over $2v_0, v_0+v_1,\dots,v_0+v_8$, each of square divisible by $4$, verifies $q$-preservation on the coordinate classes and further test classes, and $\GAP$ returns order $256$.

(2) $\rho(S) = \langle\rho(W),\rho(\ker\pi)\rangle$: both $\rho(W)$ and $\rho(\ker\pi)$ lie in $\Stab_{\Orth(q)}([e_1/2])$, since an isometry fixing $v$ preserves the class $[v/2]$ and $\Gamma_\Co$ acts trivially on $A_{T_\Co}$; that stabilizer has order $\abs{\Orth(q)}/527 = 89\,181\,388\,800$, the orbit length $527$ being the recorded $\Orth(q)$-orbit of the nonzero isotropic classes (`computations/reports/coble_isotropic_orbits.py`); and the subgroup computed from the two families already has that order, so the inclusion is an equality.
Equivalently, $\Orth(K) = \set{\pm1}\times\Orth^+(K)$ with $\Orth^+(\I_{1,8})$ the reflection group of the chamber, whose diagram has no symmetry ([@Vin72, Table 5]), so $S = \langle \text{lifts of } W,\ \id_{U_1}\oplus(-\id_K),\ \ker\pi\rangle$, and $\rho(\id_{U_1}\oplus(-\id_K)) = \id$ because $A_{T_\Co}$ is $2$-elementary and its $K$-block is the discriminant of $2\I_{1,8}$.

(3) The element $g = \id_{U_1}\oplus(-\id_K)$ fixes $e_1$, acts as $-1$ on $K$, is trivial on $A_{T_\Co}$ and so lies in $\ker\rho_{T_\Co}\cap S$; its image in $\Orth(K)$ is $-\id_K$, which is not in $\Orth^+(K)$ because $\I_{1,8}$ has positive index $1$ and $\spinornorm_\bR(-\id) = [(-1)^1] = -1$ (@lem:minus-identity-spinor-norm).
So $G = \set{\pm1}\cdot G^+$ as subgroups of $\Orth(K) = \set{\pm1}\times\Orth^+(K)$, and the two indices in (3) follow from (2).

(4) The same $g$ shows the other half: it lies outside $\Orth^+(T_\Co)$, since it reverses the plane spanned by the positive directions of $U_1$ and of $K$, while it does lie in the discriminant kernel; hence the stabilizer in $\widetilde\Orth(T_\Co)$ of $e_1$ is not contained in $\widetilde\Orth^+(T_\Co)$ and the two groups have the same orbit on $e_1$.
The orbit count then follows from $\rho$ onto $\Orth(q)$ (@thm:two-elementary-surjectivity): the $\ker\rho$-orbits inside the orbit of $e_1$ are in bijection with $\Orth(q)/\rho(S)$, of order $527$.
:::

::: {.remark title="What the index does not need"}

The proposition reduces the $527$ polarized $0$-cusps to one datum, but does not compute it: what is needed is which $g\in\Orth(\latI_{1,8}(2))$ lift into $\Gamma_\Co$, a condition on the action on $A_{T_\Co} = A_{\langle2\rangle}\perp A_{K}$, and then the index $[\Orth^+(\latI_{1,8}(2)) : G]$ in the finite image of that action.
Both need the wall reflections of Vinberg's $I_{1,8}$ chamber as generators of $\Orth(\latI_{1,8})$, which is the transcription of [@Vin72] that @sec-zero-cusp-lattices records as outstanding, and the index itself is computed in $\GAP$ on the finite image.
No chamber of $G$ is needed for the index; the chamber is sage-extensions#285 and sage-extensions#297.
:::

::: {.theorem #thm:plane-fibre title="The plane fibre, the plane classes and the $1$-cusp count of $\fco$"}

Let $P\subset B = U\perp U\perp \I_{0,7}$ be a primitive isotropic plane, $K_P = P^{\perp B}/P\iso\I_{0,7}$, $J = [P/2]\leq A_{T_\Co}$ the order-$4$ isotropic subgroup it spans, and $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$, whose discriminant image is trivial.
Then

1. $\abs{\Stab_{\Orth(q_{T_\Co})}(J)} = 1\,981\,808\,640$ and $\abs{\rho(\Stab_{\Orth(B)}(P))} = 247\,726\,080$, so the plane fibre has index
$$
\bigl[\Stab_{\Orth(q_{T_\Co})}(J) : \rho(\Stab_{\Orth(B)}(P))\bigr] = 8 ;
$$

2. the liftable order-$4$ isotropic subgroups are the $\Orth(q_{T_\Co})$-orbit of $J$, of size $23\,715$, which is the total the five sizes $1575, 270, 9450, 3780, 8640$ of @sec-open-problems sum to;

3. hence $\fco$ has $23\,715\cdot 8 = 189\,720$ $1$-cusps for $\Gamma_\Co$, one fibre of eight over each liftable $J$: a page proof, with the public lattice-orbit computation remaining sage-extensions#286.
:::

::: {.proof}

Everything is finite linear algebra over $\F_2$: $T_\Co = B(2)$ with $B$ unimodular, so $A_{T_\Co} = B/2B\cong\F_2^{11}$. Since the coordinates are in the unscaled $B$, the norm-valued discriminant form is $q([x/2])=B(x,x)/2\pmod{2\ZZ}$; on the exponent-two complement it takes the $\F_2$ values used by the matrix computation. The discriminant action of $g\in\Orth(B)$ is $g\bmod 2$.

The record is `computations/reports/coble_plane-half-f2.py` and its run.
It realises $A_{T_\Co}\cong B/2B$ by masks, builds $G = \Orth(q)$ as a matrix group over $\GF(2)$ from the orthogonal group's four generators and verifies $\abs{G} = 46\,998\,591\,897\,600 = \abs{\Orth(q)}$; it reduces the $119$ lattice generators of $\Stab_{\Orth(B)}(P)$, each of which the companion record `computations/reports/coble_plane-half.py` verifies to be an isometry of $B$ preserving $P$, to matrices over $\GF(2)$ and forms $H$, with $\abs{H} = 247\,726\,080$; it presents $J$ to $\Stab(G,J,\mathrm{OnSubspacesByCanonicalBasis})$ as its canonical-basis matrix, obtaining $\abs{\Stab} = 1\,981\,808\,640$, and to $\mathrm{Orbit}(G,J,\cdot)$, obtaining $23\,715$ with
$$\abs{\Stab_{\Orth(q)}(J)}\cdot\abs{\Orth(q)\cdot J} = \abs{\Orth(q)} .$$
That identity is orbit--stabilizer and is the record's first check; the second, $H\subseteq \Stab_{\Orth(q)}(J)$, also holds, which is what makes the index a fibre index and not a ratio of two unrelated orders: an integral isometry preserving $P$ carries the classes of $\tfrac12 e_1$ and $\tfrac12 e_2$ into $J$, so its reduction mod $2$ stabilises $J$.
The reduction enters transposed, because a $\GAP$ matrix group acts on row vectors by right multiplication while the matrix of a module automorphism is written in columns; with that one convention fixed both orders are unchanged and the containment holds.
The index is also the index of $S_7$ in $\Orth(q_{\I_{0,7}(2)})$, the Levi computation of `computations/reports/coble_plane-half-levi.py`, which is an independent agreement.
The five sizes $1575, 270, 9450, 3780, 8640$ sum to $23\,715$, the size of the $\Orth(q)$-orbit, so they are a refinement of one orbit and not a partition of it: their five-way split is a statement about the orbits of a *smaller* group, which this record does not compute.
Nothing on this page asserts the split; @tbl-finite-plane-orbits carries the marking, and sage-extensions#286 is the computation that would identify the group and decide the five numbers.

*The finite discriminant incidence, before any arithmetic flag partition.* A liftable $J$ is a two-dimensional $\F_2$-subspace of $A_{T_\Co}$ spanned by the classes of $\tfrac12 e_1$ and $\tfrac12 e_2$, so its three nonzero elements are the classes of $\tfrac12 e_1$, $\tfrac12 e_2$ and $\tfrac12(e_1+e_2)$.
Each is attained, and attained by a primitive isotropic vector of $B$: $e_1$, $e_2$ and $e_1+e_2$ are primitive isotropic vectors, and each has divisibility $2$ in $T_\Co = B(2)$ because $\beta_{T_\Co}(v,f_i) = 2\delta_{ij}$ for the dual basis vector $f_i$, so the class of $v/\div(v)$ is exactly the class of $\tfrac12 v$ listed.
By the index $1$ of @sec-cusp-lifting, two primitive isotropic vectors of $T_\Co$ with the same class are $\Gamma_\Co$-equivalent, so each of the three classes is a single $\Gamma_\Co$-orbit of primitive isotropic vectors, that is one $0$-cusp.
The incidence matrix of $0$-cusps with plane classes therefore has one row for each of the $527$ nonzero isotropic classes and one column for each of the $23\,715$ plane classes, its entry being $1$ exactly when the class is one of the three in $J$; each column has three entries, and the row sums are the number of plane classes through a given $0$-cusp.
:::

The public lattice computation remains sage-extensions#286. It is additional owner evidence for the page's $527$ and $189\,720$ page proofs and must also supply the five-way refinement of the $23\,715$ under the smaller group: the orbit decomposition of the $528$ isotropic classes' order-$4$ isotropic subgroups under the acting group, with a representative stabilizer of each orbit. The five published sizes are not inferred from the integral fibre theorem.

::: {.proposition #prop:coble-arithmetic-flag-incidence title="The arithmetic plane--line--flag graph over one discriminant plane"}
Fix the standard primitive isotropic plane $P=\langle e_1,e_2\rangle$ in $B=U_1\perp U_2\perp D$, and put $\Gamma_\Co=\ker\rho\intersect\Orth^+(B)$. Over $J=[P/2]$, the arithmetic graph has:

1. the eight $\Gamma_\Co$-orbits of planes in the fibre already proved above;
2. for each arithmetic plane orbit $\mathcal P$ and each of the three nonzero classes $c\in J$, exactly **one** $\Gamma_\Co$-orbit of line-in-plane flags $(P,L)$ with $P\in\mathcal P$ and $[L/2]=c$.

Consequently each arithmetic plane node is incident to all three arithmetic line classes in $J$, with no repeated flag orbit between those nodes. Each arithmetic line node has eight incident plane nodes over $J$; each of those $3\times8$ incidences is one arithmetic flag orbit, not merely a containment of discriminant classes. Under the projection to discriminant data, all eight plane nodes map to the same $J$, and every finite containment of $c$ in $J$ has exactly eight flag preimages, one for each arithmetic plane orbit. No further hidden splitting or merging occurs at the flag level.
:::

::: {.proof}
**The integral plane action.** By the parabolic factorization of @thm:coble-plane-stabilizer-image, the full integral Levi induces $GL_2(\ZZ)$ on $P$: $A$ acts on $P$, $A^{-T}$ on $P^*$, and the definite $D$ block is arbitrary. Modulo $2$, the level condition forces $A\equiv I\pmod2$. On this real Witt block the normalized real spinor character is $\det A$: the $SL_2(\bR)$ factor is connected, hence spinor-positive, while after reducing to that factor the only remaining model is $\diag(\det A,1)$, which is spinor-negative exactly when $\det A=-1$ (the hyperbolic-plane witness already used above). The definite and unipotent factors are spinor-positive. Thus the image of $\Stab_{\Gamma_\Co}(P)$ on $P$ is exactly
$$ \Gamma(P)\definedas\theset{A\in SL(P): A\equiv I_2\pmod2}. $$

**Transitivity of that action on a parity class.** A primitive line in $P$ is $L_{(a,b)}=\ZZ(ae_1+be_2)$ with $\gcd(a,b)=1$, and its class is $(\bar a,\bar b)\in J\setminus\{0\}$. Complete each primitive vector $v=(a,b)^T$ to a determinant-one matrix $M_v=[v,z_v]\in SL_2(\ZZ)$ with first column $v$; this is the elementary divisibility-one completion supplied by Bezout's identity. If $w$ is another primitive vector in the same parity class, complete it similarly to $M_w=[w,z_w]$. Write $c$ for the common nonzero first column modulo $2$. Then
$$ \det(c,z_w-z_v)=\det M_w+\det M_v=1+1=0\quad\text{in }\F_2. $$
The functional $x\mapsto\det(c,x)$ is nonzero and alternating, so its one-dimensional kernel is exactly $\langle c\rangle$ (indeed $\det(c,c)=0$). Hence $z_w-z_v=t c$ for some $t\in\F_2$. Lift $t$ to an integer and replace the second column of $M_w$ by $z_w-t w$: this subtracts the first column $w$ $t$ times, preserves determinant one, and makes $M_w\equiv M_v\pmod2$. *Only now* form
$$ A=M_wM_v^{-1}. $$
This adjusted quotient satisfies $A\equiv I_2\pmod2$ and $Av=w$, so $A\in\Gamma(P)$ carries one primitive line to the other. The construction is uniform in all three parity classes, with the composition direction fixed: it is the adjusted $M_wM_v^{-1}$, not its inverse. Hence $\Gamma(P)$ is transitive on primitive lines within each fixed class in $J$; it cannot permute the three classes, because its action modulo $2$ is the identity.

Now let $\mathcal P$ be one of the eight arithmetic plane orbits in the fibre and fix $P_0\in\mathcal P$. Conjugating the standard plane transfers both the exact image $\Gamma(P)$ and the preceding transitivity to $\Stab_{\Gamma_\Co}(P_0)$. For every nonzero $c\in J$ pick any $L_c\subset P_0$ with class $c$. If $(P_0,L')$ is another flag with the same $c$, the level-two line action moves $L_c$ to $L'$ while fixing $P_0$ setwise. Hence there is exactly one arithmetic flag orbit for this pair $(\mathcal P,c)$. It remains one, not eight: the plane stabilizer supplies precisely the alignment that the global line-lifting theorem alone cannot guarantee while keeping the plane fixed. Since every $\Gamma_\Co$-orbit of planes has this normal form, this proves item 2; item 1 is the spinor-restricted fibre assertion of @thm:coble-plane-stabilizer-image. Each conclusion is therefore local to an actual arithmetic fibre, with the public lattice-orbit computation remaining sage-extensions#286 as the separate owner comparison and the known-family card retaining its own dependency.
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
Two consequences are used below and are worth separating from the arguments that use them: a pairing of two vectors that both lie in $L^*$ lies in $\tfrac12\ZZ$ and need not be integral, and the reduction modulo $2$ is the only place where the integral lattice enters the discriminant representation.

By @def:2elementary-roots the roots of a $2$-elementary lattice are the short roots of square $-2$ and the long roots of square $-4$ with divisibility $2$; that definition carries no signature hypothesis, so it applies to $T_\Co$ as it stands.

::: {.proposition #prop:gamma-co-reflective-set title="The reflective set of the stable Coble group"}

Let $T_\Co = B(2)$ be the Coble lattice of @prop:tco-as-twist, even of signature $(2,9)$ and determinant $-2048$, so that every primitive vector of $T_\Co$ has divisibility $2$ (@lem:divisibilityAlwaysTwoTco), and let $\Gamma_\Co = \Orth^+(T_\Co)\intersect\ker\rho_{T_\Co}$, with $\Orth^+(T_\Co) = \Theta_\bR(T_\Co)$ of @def:lattice-spinor-kernels and $\spinornorm_\bR$ the real spinor norm of @def:spinor-norm.
Write $s_v$ for the reflection of @def:spinor-norm in a nonisotropic vector $v$.
Then, for a primitive $v$, $s_v$ is an isometry of $T_\Co$ exactly for $v^2\in\{2,-2,4,-4\}$, and among those:

1. if $v^2 = -2$ then $s_v\in\Gamma_\Co$; hence the short roots generate a subgroup
   $$
   W(T_\Co) \definedas \generators{\,s_v \;:\; v \in T_\Co,\ v^2 = -2\,}
   \iscontainedin \Gamma_\Co
   ,$$
   which is infinite, the proof exhibiting a family;
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
The set of such $v$ is infinite and the family is explicit: for odd $a\in\ZZ$,
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

::: {.remark title="What the reflective set settles, and what it does not"}

Parts (1)–(3) decide the reflective set: it is the short roots, determined and not chosen, with nothing left to add and nothing to remove.

They do not decide how large $W(T_\Co)$ is in $\Gamma_\Co$.
The question is *not* whether "a reflective set together with finitely many further isometries generates $\Gamma_\Co$": $\Gamma_\Co$ is an arithmetic subgroup of $\Orth(T_\Co\tensor\bR)\iso\Orth(2,9)$, and arithmetic subgroups of semisimple real groups are finitely generated (Borel--Harish-Chandra), so any subset of $\Gamma_\Co$ together with a finite generating set generates $\Gamma_\Co$, and that formulation carries no content.
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
Strictness is therefore a question about that subgroup and not about the lattices, and it is decided above for both: $\rho_{T_\Co}(\Gamma^{\mathrm{Hdg}}_\Co)\neq1$ (@prop:gamma-co-heegner-strict) and $\rho_{T_\Co}(\Gamma^\theta_\Co)\neq1$ (@cor:theta-co-strict).
The consequence for an orbit count is quantitative: a $\Gamma^{\mathrm{Hdg}}_\Co$-orbit of primitive isotropic vectors splits into at most $[\Gamma^{\mathrm{Hdg}}_\Co : \Gamma_\Co]$ orbits under $\Gamma_\Co$, so a count made for one of the two groups is not a count for the other, and the factor relating them is finite.
In the same way the congruence group of @prob:group-identification is $\rho_{T_\Co}^{-1}(P)$ with $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)}) \leq \Orth(A_{T_\En}, q_{T_\En}) \iso \Orth(A^0, q_{T_\Co}|_{A^0})$, made into a subgroup of $\Orth(A_{T_\Co},q_{T_\Co})$ by the identity on $\ZZ\tfrac12\zeta$.
Nontriviality of $P$ alone does not separate that preimage from $\Gamma_\Co$: a preimage of a subgroup is larger than the kernel only if some element of the subgroup is realised by an integral isometry.
Here one is, and it is proposed as an explicit witness whose required properties are then verified rather than asserted.
Let $(e', f')$ be the basis of the $U(2)$ summand of $T_\Co$, with $e'^2 = f'^2 = 0$ and $e'\cdot f' = 2$, and let $\sigma$ be the transposition of $e'$ and $f'$ fixing $\ZZ\zeta$ and $E_8(2)$, which is the reflection $s_{e'-f'}$ in a vector of square $-4$.
What the argument needs of $\sigma$ is that it lies in $\Orth^+(T_\Co) = \Theta_\bR(T_\Co)$ by @def:spinor-norm, that it moves the discriminant, and that its discriminant action preserves the three blocks of $A_{T_\Co} = \ZZ\tfrac12\zeta\perp A_{U(2)}\perp A_{E_8(2)}$ and acts on the $U(2)$ block by the transposition; these are verified through the owner's operations, where $\sigma$ is built by `Lattices.reflection`, its membership in `O_plus` and in `stable_orthogonal_group` is decided by those groups, the classes are the owner's `discriminant_class` of `primitive_dual`, and the action is `discriminant_morphism`, with $q([\tfrac12 e']) = q([\tfrac12 f']) = 0$, $q([\tfrac12\zeta]) = \tfrac12$, $b([\tfrac12 e'], [\tfrac12 f']) = \tfrac12$ and $\abs{A_{T_\Co}} = \abs{\det T_\Co} = 2048$ read off the same objects (`computations/reports/coble_congruence_witness.py`).
Since a transposition of the two isotropic classes of $A_{U(2)}$ is an isometry of that block, $\rho(\sigma)\in\Orth(q_{U(2)})\subseteq P$; that inclusion is the block argument just stated and is not a computation of $P$ itself, and what the owner builds on the congruence side is the preimage of the cyclic subgroup $\generators{\rho(\sigma)}$, not of $P$ (`computations/reports/coble_stabilizer_generators.py`).
So $\rho(\sigma)\in P$ is nontrivial, $\sigma\notin\Gamma_\Co$, and $\Gamma^{\mathrm{cong}}_{\Co,2}$ strictly contains $\Gamma_\Co$.
What this does and does not settle: the four-group identification of @prob:group-identification cannot be an equality with the stable group $\Gamma_\Co$, only an equality among overgroups of it, and of the four, two are now known to be strictly larger than $\Gamma_\Co$ — the congruence group by the witness $\sigma$ just described, and the Heegner group by @prop:gamma-co-heegner-strict, whose index is $\abs{W(E_8)}$ — while the direct and geometric entries are not comparisons of subgroups of $\Orth(A_{T_\Co})$ at all (§@sec-four-groups) and their open content is @prob:coble-rigidity, @prob:B24 and @prob:B25.
$\Gamma^\theta_\Co$ of @prop:gamma-co-in-theta-centralizer is a fifth group, outside that list, and it too is strictly larger, with the same index (@prop:theta-co-index).

*Torelli, monodromy and labeled embeddings.* Two of the four are not of that kind.
The direct and geometric groups are images of centralizers in $\Orth(\lkt)$ of the labeled Coble datum, so comparing either with a Heegner group requires an isometry of $\lkt$ carrying the Enriques-labeled structure $(S_\En, T_\En, \ZZ\delta, h)$ of @prop:gamma-en-two-gluing to the Coble-labeled one $(S_\Co, T_\Co, \tilde h_\Co)$ of @prop:gamma-co-in-theta-centralizer; that is the labeled rigidity of @prob:coble-rigidity, not a computation in $T_\Co$.
And the geometric group is the monodromy of a moduli stack, so it agrees with an arithmetic group only through the direct period theorem and the direct monodromy theorem, @prob:B24 and @prob:B25.
Nothing in the two propositions above bears on either, and replacing $\Gamma_\Co$ by $\Gamma^{\mathrm{Hdg}}_\Co$ in an orbit count is exactly the change of group that the comparison forbids.
:::
