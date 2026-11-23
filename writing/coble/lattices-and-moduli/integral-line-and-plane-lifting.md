# Integral line and plane lifting for the Coble lattice {#sec-o2-lifting}

This section proves the general integral orbit theorem of research#667 for the lattice of Dolgachev--Kondo, for both primitive isotropic lines and primitive isotropic planes, under each of the four groups whose orbits the public operation of sage-extensions#286 builds; it constructs the complete integral generating families of all four groups' stabilizers, the $R_\Gamma$ ones by an enumerated Schreier transversal (@lem:o2-explicit-transversal, @thm:o2-congruence-family), instead of substituting a count or a finite discriminant image. It is the input of obligations O3 (research#834, the orbit fibres), O4 (research#835, the incidence) and O5 (research#836, the public operation and the cards) of that chain; @sec-o2-orbit-fibres states the orbit-fibre theorem of O3 group by group, and @sec-o2-consumers records which statement each of the three obligations consumes.

## The lattice, the two object types, and the four groups {#sec-o2-groups}

Throughout, $B\definedas\latI_{2,9}$ and $T_\Co\definedas B(2)$, so that $T_\Co=\generators{2}\oplus E_{10}(2)$ with $E_{10}=U\oplus E_8$ and $E_8$ negative definite (@prop:tco-as-twist). This is the lattice $N=\generators{2}\oplus E(2)$ of [@DK13, (3.6)], and the moduli space of Coble surfaces is an open subset of $\bD(N)/\Orth(N)$ for it by [@DK13, Proposition 3.2]. The object that proposition applies to is identified in that paper by two facts, both of which are statements about $T_\Co$ proved here: $N$ is the orthogonal complement of a $(-2)$-vector in $U\oplus E(2)$, and $N$ is even, of signature $(2,9)$ and $2$-elementary with $A_N\cong(\bZ/2)^{11}$ — which is @prop:coble-discriminant-group, $B(2)$ being even because $B$ is integral. Write $\rho\definedas\rho_{T_\Co}\colon\Orth(T_\Co)\too\Orth(q_{T_\Co})$ for the discriminant representation (@def:discriminant-rep), $q\definedas q_{T_\Co}$, $A\definedas A_{T_\Co}=B/2B$, and
$$\mathcal C\definedas\theset{c\in A : q(c)=0,\ c\neq0},$$
the set of $527$ nonzero isotropic classes (@lem:isotropic-classes-lift(2)). The two object types are the set $\mathcal L$ of primitive isotropic lines of $T_\Co$ and the set $\mathcal P$ of primitive isotropic planes (@def:isotropic-subspace); a primitive isotropic line is a $0$-cusp of a quotient of $\bD(T_\Co)$ and a primitive isotropic plane a $1$-cusp, so the orbit counts below are cusp counts, and each names its group (@def:gamma-co-groups); a plane contains primitive lines of each of the three nonzero classes of its order-four subgroup $J(P)\leq A$ (@prop:coble-planecusp-finite(1)), and flags are @sec-cusp-lifting's business, not this section's.

::: {.definition #def:o2-groups title="The four groups, kept distinct"}
Let $\bar\rho$ be the discriminant representation of $T_\Co$ and $P\leq\Orth(q_{T_\Co})$ the stabilizer of the decomposition $[h/2]^{\perp}=A_{U(2)}\oplus A_{E_8(2)}$ (@prop:gamma-co-images(3)). Put
$$
O\definedas\Orth(T_\Co),\qquad
\widetilde O\definedas\ker\rho,\qquad
\widetilde O^+\definedas\widetilde O\intersect\Orth^+(T_\Co),
$$
where $\widetilde O$ is the discriminant kernel and $\widetilde O^+$ its spinor-positive part, $\Orth^+$ being the kernel of the normalized real spinor norm (@conv:spinor-positive-subgroup);
and let $R_\Gamma\definedas\bar\rho^{-1}(P)$ be the restricted stabilizer of @def:gamma-co-groups(4), that is the image of $\Stab_{\gent}(\delta)$ in $\Orth(\delta^{\perp T_\En})=\Orth(T_\Co)$ (@prop:gamma-co-images(3)). The four groups of this section are $O$, $\widetilde O$, $\widetilde O^+$ and $R_\Gamma$. They are related, and not identified, as follows:
$$
\widetilde O^+\leq\widetilde O\leq O,\qquad
\widetilde O^+\leq R_\Gamma\leq O,\qquad
[\widetilde O:\widetilde O^+]=2,\qquad
[O:R_\Gamma]=2^7\cdot17\cdot31=67\,456,
$$
the last by @prop:gamma-co-images(3). The groups $\widetilde O$ and $\widetilde O^+$ **do** have finite index in $O$: $A=B/2B$ is finite, so $\rho$ has finite image and
$$
[O:\widetilde O]=\abs{\im\rho}<\infty,\qquad [O:\widetilde O^+]=2\abs{\im\rho}<\infty .
$$
This finiteness does not identify their orbit counts. Indeed $\rho(R_\Gamma)=P\neq1$ by @prop:gamma-co-images(3), whereas $\rho(\widetilde O)=\rho(\widetilde O^+)=1$, so $R_\Gamma$ is distinct from both stable groups. In addition $R_\Gamma$ is not contained in $\Orth^+(T_\Co)$ (@thm:coble-monodromy-versus-enriques(2)); the character condition, like the discriminant condition, therefore has to be retained rather than replaced by an index comparison.
:::

::: {.remark #rmk:o2-congruence title="How $R_\Gamma$ is identified with the congruence group, and how it is not"}
The group $\Gamma^{\mathrm{cong}}_{\Co,2}$ is defined by $\Gamma^{\mathrm{cong}}_{\Co,2}\definedas\rho_{T_\Co}^{-1}(P)$. The equality $R_\Gamma=\Gamma^{\mathrm{cong}}_{\Co,2}$ is therefore the conjunction of two already established propositions and not a definitional rewriting: @prop:gamma-co-images(3), which identifies $R_\Gamma$ with $\bar\rho^{-1}(P)$, and @prop:coble-cong-point-stabilizer(1), which identifies $\rho_{T_\Co}^{-1}\bigl(\Stab_{\Orth(q)}(A_{U(2)})\bigr)$ with $\rho_{T_\Co}^{-1}(P)$ and with $\Gamma^{\mathrm{cong}}_{\Co,2}$, the stabilizer of the decomposition being the setwise stabilizer of $A_{U(2)}$ because an isometry of quadratic forms of orders $4$ and $256$ carrying one summand onto the other does not exist. The arithmetic content of the identification — that the same group is the image of the Enriques stabilizer and the congruence condition of the degree-two datum — is @prop:gamma-cong-eq-heegner and @prop:direct-eq-heegner with @cor:four-groups-decided. Nothing in this section writes $\Gamma^{\mathrm{cong}}_{\Co,2}$ for any other lattice group, and nothing writes $\Gamma_\Co$ or $\Gamma_{\Co,2}$ for any of them: those are the monodromy groups of @def:gamma-co-groups(1) and (5), their identification with lattice groups is @conj:gamma-co-stable (@thm:gamma-co-is-stable(2)) and research#797 item 6, and the second is not even the intersection of $R_\Gamma$ with $\Orth^+$ (@prop:coble-monodromy-equality-false).
:::

::: {.remark #rmk:o2-group-list title="Why these four groups are exactly the groups of the public operation"}
The operation of sage-extensions#286 builds its subgroups from the Coble divisor and the three Enriques groups: it takes $O(T_\Co)$ itself, the discriminant kernel $\ker\rho=\widetilde O(T_\Co)$, its spinor-positive part $\widetilde O^+(T_\Co)$, and the images in $\Orth(\delta^{\perp})$ of $\Stab_\Gamma(\delta)$ for $\Gamma=\Gamma_\En=\widetilde\Orth^+(T_\En)$, for $\Gamma=\Gamma^K_\En=\Orth(T_\En)$ and for $\Gamma=\Gamma_{\En,2}$ (@def:gamma-co-groups). The first two restricted stabilizers are not new groups: by @prop:gamma-co-images(1), $R_{\Gamma_\En}=\widetilde\Orth^+(T_\Co)$ with no computation, and by @prop:gamma-co-images(2), $R_{\Gamma^K_\En}=\Orth(T_\Co)$ because every isometry of $q_{T_\Co}$ fixes the characteristic class $[h/2]$. The third is $R_\Gamma$ of @def:o2-groups. Hence the list of that operation is $O$, $\widetilde O$, $\widetilde O^+$, $R_\Gamma$ — four groups and no more — and a theorem stated for these four is a theorem for every group the operation builds. The two monodromy groups are not on that list and are not covered here (@conj:gamma-co-stable, @prop:coble-monodromy-equality-false).
:::

## The required statements, with their proof status {#sec-o2-ledger}

The orbit theorems of @sec-o2-lines and @sec-o2-planes are assembled from statements of three kinds: the lifting statements that carry a finite discriminant datum to integral objects, the stabilizer-image statements that compute the discriminant image of an integral stabilizer, and the completeness statements for integral generating families. Several of the first two were used inside @sec-cusp-lifting without being stated as theorems of their own, and the completeness statements were not separated from the finite-image computations that witness them. @tbl-o2-ledger lists all of them, with the status each has in this book after this section; the last of them, (U2), is the statement @thm:o2-congruence-family, which is why the `(C4)` and `(C5)` rows now read `proved`.

| | Statement | Status |
| --- | --- | --- |
| (L1) | $\ell\mapsto[\ell/2]$, well defined on primitive isotropic lines, $\Gamma$-equivariant for $\widetilde O^+\leq\Gamma\leq O$, image $\mathcal C$ | proved: @lem:o2-line-classmap |
| (L2) | the fibres of (L1) are single $\widetilde O^+$-orbits | proved: @lem:o2-line-classmap(3) |
| (L3) | hence $\Gamma$-orbits of lines $\leftrightarrow$ $\rho(\Gamma)$-orbits on $\mathcal C$, bijectively | proved: @thm:o2-lines(1) |
| (L4) | the decorated pair $(J(P),s(P))$ classifies primitive isotropic planes equivariantly, and is attained | proved: @thm:coble-integral-plane-lifting(1) |
| (L5) | the fibres of (L4) are single $\widetilde O^+$-orbits | proved: @thm:coble-integral-plane-lifting(2) |
| (L6) | the double-coset reduction through the normal subgroup $\widetilde O$ | [@SH23, Lemma 3.6] for $\Gamma\supseteq\widetilde O$, hypotheses verified in @thm:o2-lines(2); for $\widetilde O^+$ the same formula follows directly from (L3), not from that lemma |
| (S1) | $\rho\bigl(\Stab_\Gamma(\ell)\bigr)=\rho(\Gamma)\intersect\Stab_{\Orth(q)}([\ell/2])$ for lines | proved: @lem:o2-line-stabilizer-image |
| (S2) | $\rho\bigl(\Stab_\Gamma(P)\bigr)=\rho(\Gamma)\intersect S_{(J(P),s(P))}$ for planes | proved: @lem:coble-plane-stabilizer-descends |
| (C1) | a complete integral family for $\Stab_O(P_0)$ | proved: @thm:o2-plane-family |
| (C2) | a complete integral family for $\Stab_{\widetilde O}(P_0)$ and $\Stab_{\widetilde O^+}(P_0)$ | proved: @thm:o2-plane-family-kernel |
| (C3) | a complete integral family for $\Stab_O(\ell)$ | proved: @thm:o2-line-family and @lem:o2-line-stabilizer-image(2) |
| (C3') | a complete integral family for $\Stab_{\widetilde O}(\ell)$ and for its three character subgroups | proved: @thm:o2-stable-line and @thm:o2-stable-level-two-generation |
| (C4) | a complete integral family for $\Stab_{R_\Gamma}(P)$ | proved: @thm:o2-congruence-family(2), with the transversal of @lem:o2-explicit-transversal |
| (C5) | a complete integral family for $\Stab_{R_\Gamma}(\ell)$ | proved: @thm:o2-congruence-family(1) |
| (U1) | a finite family of integral isometries generating $\Orth(\latI_{1,8})$ | proved: @thm:o2-line-family |
| (U2) | the congruence condition of $R_\Gamma$ inside the line and plane parabolics, generated | proved: @thm:o2-congruence-family |

: The statements obligation O2 requires, and their status. {#tbl-o2-ledger}

Four distinctions matter here. First, no step of the plane argument proves a line family: the plane parabolic has a two-dimensional Levi factor containing $GL_2(\bZ)$, whereas the line parabolic's Levi factor is $O(\latI_{1,8})$ (@lem:o2-line-reduction). The full line family instead comes from @thm:o2-line-family, and the stable line family from its level-two companion @thm:o2-stable-level-two-generation. Second, the $21/45$ level-four span is only a necessary condition and proves no generation assertion (@rmk:o2-stable-line-level-four). Third, (U2) is proved for both lines and planes of $R_\Gamma$ by @thm:o2-congruence-family, and *not* by intersecting a family for $O$ with $\rho^{-1}(P)$: the members of the $O$-families are not in $R_\Gamma$ (for the plane, $\Stab_{\Orth(T_\Co)}(P_0)\not\subseteq R_\Gamma$ by @thm:o2-planes(4)), and what the construction supplies is a transversal together with the Schreier matrices $t_Vft_{V'}^{-1}$ of @lem:o2-explicit-transversal. Fourth, none of the generation statements is used to prove an orbit classification: those classifications use (L1)--(L6) and (S1)--(S2), whose stabilizer images are proved structurally. Conversely, no finite discriminant-image computation was used as a substitute for an integral generation proof.

::: {.remark #rmk:o2-bibliography title="A citation key"}
The reduction through the normal subgroup is [@SH23, Lemma 3.6]; the entry is the Dutour Sikiri\'c--Hulek paper *Moduli of polarized Enriques surfaces --- computational aspects* (arXiv:2302.01679). An earlier page of this book cites the same lemma under the key `DH23`, which is not in the bibliography; that is a defect of that page and not repaired here. The lemma is a statement about a group, a normal subgroup and two subgroups, with no lattice in it, so its hypotheses are checked where it is applied (@thm:o2-lines(2)) and its tables and its numerical rows are not used anywhere in this section: those rows concern $U+U(2)+E_8(-2)$, the Enriques lattice, and not $T_\Co$.
:::

## Primitive isotropic lines: the lifting theorem {#sec-o2-lines}

::: {.lemma #lem:o2-line-classmap title="The divided class of a primitive isotropic line"}
Let $v\in T_\Co$ be primitive and isotropic (@def:isotropic-subspace) and $\ell=\bZ v$.

1. The class $[\ell/2]\definedas[v/2]\in A$ is well defined by $\ell$ alone, nonzero, and isotropic; and $\rho(g)[\ell/2]=[g\ell/2]$ for every $g\in\Orth(T_\Co)$.
2. The image of $\ell\mapsto[\ell/2]$ is $\mathcal C$, the $527$ nonzero isotropic classes.
3. If $v,v'\in T_\Co$ are primitive isotropic with $[v'/2]=[v/2]$, then $kv=v'$ for some $k\in\widetilde O^+$. In particular two primitive isotropic lines have the same class if and only if some element of $\widetilde O^+$ carries one to the other, and the fibres of $\ell\mapsto[\ell/2]$ are single $\widetilde O^+$-orbits.
:::

::: {.proof}

(1) A primitive vector of $T_\Co$ has divisibility $2$ (@lem:divisibilityAlwaysTwoTco), so $v/2\notin B$ and $[v/2]\neq0$; $q([v/2])=v^2/4=0$; the other primitive vector of $\ell$ is $-v$ and $[-v/2]=[v/2]$ because $-v-v=-2v\in2B$; and $\rho(g)[v/2]=[gv/2]$ is the definition of $\rho$. All of this is @lem:isotropic-classes-lift(1).

(2) is @lem:isotropic-classes-lift(2).

(3) Let $v,v'$ be primitive isotropic with $[v'/2]=[v/2]$. The full group $\Orth(T_\Co)$ is transitive on primitive isotropic lines (@lem:I29-plus-line-transitivity, whose $\Orth^+(B)$ is $\Orth^+(T_\Co)$ by @prop:tco-as-twist), so $v'=\pm gv$ for some $g$; replacing $g$ by $-g$, which changes neither the line nor the class, take $v'=gv$. Then $\rho(g)\in\Stab_{\Orth(q)}([v/2])=\rho\bigl(\Stab_{\Orth(B)}(v)\bigr)$ (@lem:cusp-vector-stabilizer-image(1)), so $\rho(g)=\rho(h)$ for some $h$ fixing $v$; hence $k\definedas gh^{-1}\in\widetilde O$ also carries $v$ to $v'$. Choose $\varepsilon\in\Stab_{\widetilde O}(v)$ with $\spinornorm_\bR(\varepsilon)=\spinornorm_\bR(k)$; this is possible because that stabilizer contains an element of normalized real spinor norm $-1$ (@lem:cusp-vector-stabilizer-image(2)) together with the identity. Then $k\varepsilon^{-1}\in\widetilde O\intersect\Orth^+(T_\Co)=\widetilde O^+$ and $(k\varepsilon^{-1})v=v'$ because $\varepsilon v=v$. So the fibre is a single $\widetilde O^+$-orbit, and it is a single $\widetilde O$-orbit a fortiori.
:::

::: {.lemma #lem:o2-line-stabilizer-image title="The discriminant image of the stabilizer of a primitive isotropic line"}
Let $v$ be primitive isotropic, $\ell=\bZ v$, $c=[\ell/2]$, and let $\Gamma$ be a subgroup with $\widetilde O^+\iscontainedin\Gamma\iscontainedin\Orth(T_\Co)$. Then

1. $\rho\bigl(\Stab_\Gamma(v)\bigr)=\rho(\Gamma)\intersect\Stab_{\Orth(q)}(c)$;
2. $-\id\in\widetilde O\intersect\Orth^+(T_\Co)=\widetilde O^+\iscontainedin\Gamma$, so $\Stab_\Gamma(\ell)=\Stab_\Gamma(v)\cdot\generators{\pm1}$ and therefore $\rho\bigl(\Stab_\Gamma(\ell)\bigr)$ is the same subgroup.

In particular the stabilizer of a line has the same discriminant image as the stabilizer of either of its two vectors, and for $\Gamma=O$ that image is all of $\Stab_{\Orth(q)}(c)$, of order $\abs{\Orth(q)}/527=89\,181\,388\,800$.
:::

::: {.proof}

(1) The class of $gv$ is $\rho(g)c$ by @lem:o2-line-classmap(1), so an element of $\Stab_\Gamma(v)$ has its image in the stabilizer of $c$: the inclusion $\subseteq$. Conversely let $h\in\rho(\Gamma)\intersect\Stab_{\Orth(q)}(c)$ and $\gamma\in\Gamma$ with $\rho(\gamma)=h$. Then $[\gamma v/2]=\rho(\gamma)c=c=[v/2]$, so by @lem:o2-line-classmap(3) there is $k\in\widetilde O^+$ with $k\gamma v=v$. Now $k\gamma\in\Gamma$ because $\widetilde O^+\iscontainedin\Gamma$, it fixes $v$, and $\rho(k\gamma)=\rho(\gamma)=h$.

(2) $-\id$ acts trivially on $A=B/2B$, which is $2$-torsion, so $-\id\in\ker\rho$; and $-\id\in\Orth^+(T_\Co)$ because the positive index of $T_\Co$ is $2$ (@lem:minus-identity-spinor-norm), so $-\id\in\widetilde O^+$, and $\widetilde O^+\iscontainedin\Gamma$ puts it in $\Gamma$; and $\Stab_\Gamma(\ell)$ is the union of $\Stab_\Gamma(v)$ and $-\Stab_\Gamma(v)$, since $g\ell=\ell$ means $gv=\pm v$. The order is $\abs{\Stab_{\Orth(q)}(c)}=\abs{\Orth(q)}/527$ by @lem:cusp-vector-stabilizer-image(1) and the transitivity of @lem:isotropic-classes-lift(2).
:::

::: {.theorem #thm:o2-lines title="Integral line orbits for the four groups"}
Let $\Gamma$ be a subgroup with $\widetilde O^+\iscontainedin\Gamma\iscontainedin\Orth(T_\Co)$; fix a primitive isotropic line $\ell_0$ and put $\mathcal L_\Gamma\definedas\Gamma\backslash\mathcal L$.

1. (The lifting theorem.) The map $\ell\mapsto[\ell/2]$ induces a bijection $\mathcal L_\Gamma\isoto\rho(\Gamma)\backslash\mathcal C$ between the $\Gamma$-orbits of primitive isotropic lines and the orbits of $\rho(\Gamma)$ on the $527$ nonzero isotropic classes.
2. (The double-coset form.) Equivalently,
$$\abs{\mathcal L_\Gamma}=\abs{\rho(\Gamma)\backslash\rho(\Orth(T_\Co))\big/\rho\bigl(\Stab_{\Orth(T_\Co)}(\ell_0)\bigr)},$$
the double-coset decomposition of the finite group $\Orth(q)$ by $(\rho(\Gamma),\rho(\Stab_{\Orth(T_\Co)}(\ell_0)))$. The formula follows directly from (1) for every $\Gamma$ in the theorem. When $\Gamma\supseteq\widetilde O$, it is also the reduction of the integral double cosets $\Gamma\backslash\Orth(T_\Co)/\Stab_{\Orth(T_\Co)}(\ell_0)$ through the normal subgroup $\widetilde O$ of [@SH23, Lemma 3.6], with $U=\widetilde O$, $K=\Gamma$ and $H=\Stab_{\Orth(T_\Co)}(\ell_0)$; in particular that citation is **not** applied to $\Gamma=\widetilde O^+$, which does not contain $\widetilde O$.
3. (The four groups.) The number of orbits of primitive isotropic lines is
   a. $1$ for $\Gamma=O$;
   b. $527$ for $\Gamma=\widetilde O$ and for $\Gamma=\widetilde O^+$;
   c. $4$ for $\Gamma=R_\Gamma$, the orbits being those of $P$ on $\mathcal C$, of sizes $2$, $135$, $270$ and $120$.
4. (The character subgroups.) The same numbers hold with $O$ replaced by $SO=\ker\det$, $O^+=\Orth^+(T_\Co)$ or $SO^+=SO\intersect O^+$, and with $\widetilde O$ replaced by $\widetilde O\intersect SO$, $\widetilde O\intersect O^+$ or $\widetilde O\intersect SO^+$.
5. (What is not covered.) No clause is asserted for the monodromy group $\Gamma_\Co$ of @def:gamma-co-groups(1) or for $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5). For the labelled base only $\Gamma_\Co(B)\subseteq\widetilde O^+$ is proved (@thm:gamma-co-is-stable(1)), so $527$ is a *lower bound* for the number of $\Gamma_\Co(B)$-orbits and not the count.
:::

::: {.proof}

(1) The map of @lem:o2-line-classmap is $\Gamma$-equivariant and onto $\mathcal C$; it is constant on $\Gamma$-orbits, so it induces a surjection $\mathcal L_\Gamma\to\rho(\Gamma)\backslash\mathcal C$, and it is injective on orbits because the fibre over each class is a single $\widetilde O^+$-orbit (@lem:o2-line-classmap(3)) and $\widetilde O^+\iscontainedin\Gamma$.

(2) By (1), $\abs{\mathcal L_\Gamma}$ is the number of $\rho(\Gamma)$-orbits on $\mathcal C=\rho(\Orth(T_\Co))\cdot c_0$, which by orbit--stabilizer is the stated number of double cosets, with the stabilizer computed by @lem:o2-line-stabilizer-image. This proves the formula for every $\Gamma$ in the theorem without a further group lemma. If $\widetilde O\subseteq\Gamma$, then the $\Gamma$-orbits in the single $\Orth(T_\Co)$-orbit $\mathcal L$ are also the integral double cosets $\Gamma\backslash\Orth(T_\Co)/\Stab_{\Orth(T_\Co)}(\ell_0)$. Here $U=\widetilde O$ is normal and is contained in $K=\Gamma$, so [@SH23, Lemma 3.6] applies and carries this decomposition to the displayed finite double-coset decomposition. When $\widetilde O\not\subseteq\Gamma$, and in particular for $\widetilde O^+$, no such application is made: the first sentence of this proof, through (1), is the argument.

(3a) $\Orth^+(T_\Co)=\Orth^+(B)$ acts transitively on the primitive isotropic lines of $B$ (@lem:I29-plus-line-transitivity), and $\Orth^+(T_\Co)\subseteq O$, so $O$ does too.

(3b) $\rho(\widetilde O)=1$, so by (1) the orbits are the elements of $\mathcal C$, of which there are $527$ by @lem:isotropic-classes-lift(2); and $\rho(\widetilde O^+)=1$ as well, so the fibres are still single orbits.

(3c) $\rho(R_\Gamma)=P$ by @prop:gamma-co-images(3), so by (1) the $R_\Gamma$-orbits correspond to the $P$-orbits on $\mathcal C$, which are four, of sizes $2$, $135$, $270$, $120$, by @prop:coble-cong-point-stabilizer(2). In particular no count of $R_\Gamma$ is a count of $\widetilde O$ or of $\widetilde O^+$, although $[R_\Gamma:\widetilde O^+]$ is finite: the groups have different orbits on the same finite set.

(4) It suffices to show that passing from $O$ to $SO$, $O^+$ or $SO^+$ does not split an $O$-orbit, and that passing from $\widetilde O$ to one of its intersections with $SO$ or $O^+$ does not split a $\widetilde O$-orbit. Fix the standard $v=e_1$ with $B=U_1\perp K$, $K=U_2\perp D$, $D=\generators{-1}^7$. Two elements of $\Stab_{\widetilde O}(v)$ with the four character values are available: the reflection $r_d$ in a vector $d\in K$ of square $-1$ (which fixes $U_1$ pointwise, hence $v$) has $r_d(x)=x+2(x,d)d\equiv x\pmod{2B}$, so $r_d\in\Stab_{\widetilde O}(v)$, and its characters are $(\det,\spinornorm_\bR)=(-1,+1)$ because a reflection in a negative vector has trivial normalized real spinor norm (@def:spinor-norm); while $h=\id_{U_1}\oplus(-\id_K)$ fixes $v$, is the identity modulo $2B$, and has $(\det,\spinornorm_\bR)=(-1,-1)$, since $\det(-\id_K)=(-1)^9$ and $\spinornorm_\bR(-\id_K)=-1$ by @lem:minus-identity-spinor-norm, $K$ having positive index one (@lem:split-isometry-spinor-norm). Given $g\in\widetilde O$ with $gv=v'$, multiply it on the right by the one of $\id,\ r_d,\ h,\ r_dh$ whose characters equal those of $g$: the product has trivial $\det$ and trivial spinor norm, lies in $\widetilde O\intersect SO^+$, and still carries $v$ to $v'$. The same adjustment applied to $g\in O$ carrying $\ell_0$ to $\ell$, with the witnesses transported along $g$ ($\widetilde O$ being normal in $\Orth(T_\Co)$), puts the transporter in $SO^+$; this is the argument of @cor:coble-eight-standard-line-counts. So the four counts of the full groups agree and the four counts of the kernel subgroups agree.

(5) is the statement's own restriction, and the bound is @thm:gamma-co-is-stable(1) with the fibre theorem (1): an orbit of $\Gamma_\Co(B)\subseteq\widetilde O^+$ is contained in a $\widetilde O^+$-orbit, so the number of them is at least $527$.
:::

## Primitive isotropic planes: the lifting theorem {#sec-o2-planes}

For a primitive isotropic plane $P$ let $J(P)\definedas\im(P/2)\leq A$, an isotropic subgroup of order $4$ whose three nonzero elements are the classes of the primitive vectors of $P$, and let $s(P)$ be the star of $J(P)$ (@prop:coble-planecusp-finite(1), @def:plane-star). Let
$$\mathcal D\definedas\theset{(J,s) : J\leq A\ \text{isotropic of order }4,\ s\ \text{a star of } J}$$
be the set of decorated planes; $\abs{\mathcal D}=8\cdot23\,715=189\,720$ (@lem:plane-stars(1), @prop:coble-planecusp-finite(3)). For $(J,s)\in\mathcal D$ let $S_{(J,s)}\definedas\Stab_{\Stab_{\Orth(q)}(J)}(s)$.

::: {.theorem #thm:o2-planes title="Integral plane orbits for the four groups"}
Let $\Gamma$ be a subgroup with $\widetilde O^+\iscontainedin\Gamma\iscontainedin\Orth(T_\Co)$ and put $H\definedas\rho(\Gamma)$.

1. (The lifting theorem.) The map $P\mapsto(J(P),s(P))$ is $\rho$-equivariant and onto $\mathcal D$, and it induces a bijection $\Gamma\backslash\mathcal P\isoto H\backslash\mathcal D$; every fibre of the induced map is a single $\widetilde O^+$-orbit.
2. (The stabilizer image.) $\rho\bigl(\Stab_\Gamma(P)\bigr)=H\intersect S_{(J(P),s(P))}$.
3. (The four groups.) The number of orbits of primitive isotropic planes is
   a. $1$ for $\Gamma=O$, and the same for $SO$, $O^+$, $SO^+$;
   b. $189\,720=8\cdot23\,715$ for $\Gamma=\widetilde O$, and the same for $\widetilde O\intersect SO$, $\widetilde O\intersect O^+$, $\widetilde O\intersect SO^+$;
   c. $7$ for $\Gamma=R_\Gamma$, and the same for $R_\Gamma\intersect\Orth^+(T_\Co)$.
4. (Why (3c) has two groups.) The seven is the number of $P$-orbits on $\mathcal D$ (@cor:coble-heegner-integral-plane-descent), and it is the count for $R_\Gamma$ as well as for $R_\Gamma\intersect\Orth^+$ because a fibre is a single $\widetilde O^+$-orbit and $\widetilde O^+\subseteq R_\Gamma\intersect\Orth^+$: both groups have the same orbits, although $R_\Gamma\supsetneq R_\Gamma\intersect\Orth^+$ and although $\Stab_{\Orth(T_\Co)}(P_0)$ is *not* contained in $R_\Gamma$: its discriminant image $S_3\times S_7$ has order $247\,726\,080=2^{18}\cdot3^3\cdot5\cdot7$, which cannot divide the order $696\,729\,600=2^{14}\cdot3^5\cdot5^2\cdot7$ of $P$, so that image is not a subgroup of $P$ (@thm:coble-plane-stabilizer-image(3), @prop:gamma-co-images(3)).
5. (What is not covered.) No clause is asserted for $\Gamma_\Co$ or $\Gamma_{\Co,2}$; see @thm:o2-lines(5), and note that the seven-orbit count for $F_{\Co,2}$ is @prop:coble-monodromy-equality-false's counterexample, not a consequence of this theorem.
:::

::: {.proof}

(1) Equivariance, attainment and the fibre statement are @thm:coble-integral-plane-lifting(1) and (2), whose hypothesis is exactly $\widetilde O^+\iscontainedin\Gamma\iscontainedin\Orth(T_\Co)$ and whose proof uses the parabolic decomposition of the plane stabilizer, the surjectivity of $\rho$ onto $\Orth(q)$ ([@Nik80, Theorem 3.6.3], whose hypotheses are that $T_\Co$ is even, indefinite and $2$-elementary, all verified in @prop:coble-discriminant-group), and the spinor-negative witness $\tau=-\id_{U_1}\oplus\id_{U_2\perp D}$.

(2) is @lem:coble-plane-stabilizer-descends.

(3a) $\Orth^+(T_\Co)$ is transitive on the primitive isotropic planes of $T_\Co$ (@thm:plane-transitivity-tco), so $O$ is; and as in @thm:o2-lines(4), the stabilizer of every plane contains witnesses of both characters, so $SO$, $O^+$ and $SO^+$ have the same single orbit.

(3b) $H=1$, so by (1) the orbits are the elements of $\mathcal D$, and $\abs{\mathcal D}=8\cdot23\,715$ by @lem:plane-stars(1) and @prop:coble-planecusp-finite(3); the four kernel subgroups have the same orbits by the character adjustment of @thm:o2-lines(4), applied to the plane stabilizer, which contains $\tau$ of spinor norm $-1$ and the reflection in a vector of square $-1$ orthogonal to $P$.

(3c) is @thm:coble-integral-plane-lifting(3)(c) with @cor:coble-heegner-integral-plane-descent.

(4) The image of $\Stab_{\Orth(T_\Co)}(P_0)$ is of order $30240\cdot2^{13}=247\,726\,080=2^{18}\cdot3^3\cdot5\cdot7$ by @thm:coble-plane-stabilizer-image(3), while $\abs P=2\cdot348\,364\,800=696\,729\,600=2^{14}\cdot3^5\cdot5^2\cdot7$ by @prop:gamma-co-images(3)'s Step 6. The first order does not divide the second, $2^{18}\nmid2^{14}$, so $\rho\bigl(\Stab_{\Orth(T_\Co)}(P_0)\bigr)$ is not a subgroup of $P$ and $\Stab_{\Orth(T_\Co)}(P_0)\not\subseteq R_\Gamma$. So $R_\Gamma$ does not contain the plane parabolic, and the fact that both it and its spinor-positive half have seven plane orbits is a statement about the orbits on $\mathcal D$, not about containment of stabilizers: a fibre is a single $\widetilde O^+$-orbit, and $\widetilde O^+$ lies in both groups.
:::

::: {.remark #rmk:o2-plane-row-check title="The two rows this theorem carries, and what they do not carry"}
The four counts of (3) are the plane column of @cor:coble-eight-standard-line-counts and @thm:coble-plane-orbit-counts, and their agreement with the public rows is recorded there; the seven is also the count of @cor:coble-heegner-integral-plane-descent. None of these is used in the proof: the proof is (1)--(2) with the finite sets $\mathcal C$ and $\mathcal D$ of @prop:coble-discriminant-group and @prop:coble-planecusp-finite. A public row returning $189\,720$ or $7$ reproduces the theorem; it does not replace it, and it cannot, since the row is an enumeration and the theorem is what makes the enumeration complete (@thm:o2-lines(1), (2)).
:::

## Complete integral stabilizer families {#sec-o2-families}

The orbit theorems of @sec-o2-lines and @sec-o2-planes do not need a generating family: their stabilizer images are proved from the parabolic decomposition of the stabilizer and the surjectivity of $\rho$. What a family is needed for is the finer statement the acceptance of sage-extensions#286 attaches to it, "each $\rho(\Stab(x))$ computed from a family proved to generate $\Stab(x)$", and the corresponding statements of O5 (research#836). This section constructs those families: for $O$, $\widetilde O$ and $\widetilde O^+$ from the parabolic decompositions, and for $R_\Gamma$ by the enumerated transversal of @lem:o2-explicit-transversal.

::: {.lemma #lem:o2-even-part title="The Schreier family of an index-two kernel"}
Let $G=\generators{F}$ with $F$ finite, let $\chi\colon G\too\generators{\pm1}$ be onto, and choose $t\in F$ with $\chi(t)=-1$. Then $\ker\chi$ is generated by
$$
\theset{f,\ tf t^{-1}:f\in F,\ \chi(f)=1}
\cup\theset{ft^{-1},\ tf:f\in F,\ \chi(f)=-1}.
$$
For a character $\chi\colon G\too Q$ onto a finite group $Q$, the analogous finite family is supplied by the same Schreier construction with a right transversal of $\ker\chi$ in $G$; it is not a collection of pairwise generator commutators.
:::

::: {.proof}

Write $\bar x=1$ if $\chi(x)=1$ and $\bar x=t$ if $\chi(x)=-1$. Every element $s$ of the displayed set is $r f\,\overline{rf}^{\,-1}$ with $r\in\{1,t\}$ and $f\in F$, hence lies in $\ker\chi$. Conversely, write $g=f_1\cdots f_n\in\ker\chi$, put $r_0=1$ and $r_i=\overline{r_{i-1}f_i}$. Since $r_n=1$,
$$g=\prod_{i=1}^n\bigl(r_{i-1}f_i r_i^{-1}\bigr),$$
and each factor or its inverse belongs to the displayed set. This is the Schreier argument for the transversal $\{1,t\}$; the same calculation with any finite transversal proves the final assertion. No assertion that pairwise commutators of generators generate $[G,G]$ is used.
:::

::: {.theorem #thm:o2-plane-family title="A complete integral family for the plane stabilizer of $\Orth(T_\Co)$"}
In the standard model $B=U_1\perp U_2\perp D$ with $U_1=\generators{e_1,f_1}$, $U_2=\generators{e_2,f_2}$, $D=\generators{-1}^7$ with basis $d_1,\dots,d_7$, and $P_0=\generators{e_1,e_2}$, the stabilizer $\Stab_{\Orth(B)}(P_0)$ is generated by the following integral isometries of $B$:

1. $W\colon e_1\leftrightarrow e_2$, $f_1\leftrightarrow f_2$, $d_i\mapsto d_i$ (the transposition of the two hyperbolic planes);
2. $A=\gamma\oplus(\gamma^{-1})^{T}\oplus\id_D$ with $\gamma=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, that is $e_1\mapsto e_1$, $e_2\mapsto e_1+e_2$, $f_1\mapsto f_1-f_2$, $f_2\mapsto f_2$;
3. the six transpositions $d_j\leftrightarrow d_{j+1}$ and the seven sign changes $d_j\mapsto-d_j$;
4. the fourteen Eichler transvections $E_{e_i,d_j+d_7}$ ($i=1,2$, $1\leq j\leq 6$) and $E_{e_i,2d_7}$ ($i=1,2$);
5. the central shear $\sigma=E_{e_1,e_2}$, $x\mapsto x+(e_1,x)e_2-(e_2,x)e_1$.

In particular the discriminant image is generated by the images of these thirty elements and equals $\rho\bigl(\Stab_{\Orth(B)}(P_0)\bigr)$ of order $30\,240\cdot2^{13}=247\,726\,080$.
:::

::: {.proof}

$\Stab_{\Orth(B)}(P_0)=L\ltimes U$ with $L\cong GL_2(\bZ)\times\Orth(D)$ and $U$ the kernel of the action on $P_0$ and on $P_0^{\perp B}/P_0$ (@thm:coble-plane-stabilizer-image(1)). The elements of (1)--(5) lie in $\Stab_{\Orth(B)}(P_0)$: those of (1)--(3) in $L$, those of (4)--(5) in $U$ by @thm:coble-plane-stabilizer-image(2), where the transvection formula is displayed and its integrality is the condition $k\in D^{\mathrm{ev}}$ (@def:eichler-siegel).

*$L$.* The elements of (1) and (2) act as $\gamma\oplus(\gamma^{-1})^{T}$ with $\gamma$ the transposition $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and the shear $\begin{pmatrix}1&1\\0&1\end{pmatrix}$; these two generate $GL_2(\bZ)$, the standard generators $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ and $-\id$ being words in them (a word search in $W$, $A$, $A^{-1}$ of length at most ten finds both; `computations/reports/coble_833-line-parabolic-checks.py`, part 2). The elements of (3) generate the group of signed permutation matrices of $D$, which is $\Orth(D)$ because the vectors of square $-1$ in $D$ are the $\pm d_i$ (@thm:definite-unimodular-class-numbers). So (1)--(3) generate $L$.

*$U$.* Let $u\in U$ and write $u(f_i)=f_i+w_i+p_i$ with $w_i\in D$, $p_i\in P_0$. Isotropy of $u(f_i)$ forces $w_i\in D^{\mathrm{ev}}$; composing with the inverses of $E_{e_1,w_1}$ and $E_{e_2,w_2}$, which lie in the group generated by (4) because $E_{e_i,w+w'}=E_{e_i,w}E_{e_i,w'}$ ([@GHS08, §3.1, equation (5)]) and because $d_1+d_7,\dots,d_6+d_7,2d_7$ is a $\bZ$-basis of $D^{\mathrm{ev}}$ of determinant $2$ (checked exactly, `computations/reports/coble_833-line-parabolic-checks.py`, part 1), we reduce to an element $u'$ with $w_1=w_2=0$. The rest of the argument is @thm:coble-plane-stabilizer-image(1)'s: the $D$-component of $u'(d)$ must vanish, and the remaining datum is a skew matrix $C=(c_{ji})$ with $u'(f_i)=f_i+\sum_jc_{ji}e_j$, whose entries are arbitrary integers; and the map with a given skew $C$ is exactly $\sigma^{c}$ for $C=c\cdot\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, since $\sigma$ acts by $f_1\mapsto f_1+e_2$, $f_2\mapsto f_2-e_1$ and fixes $e_1,e_2,D$. Hence $U$ is generated by (4) and (5), and $\Stab_{\Orth(B)}(P_0)$ by (1)--(5).

*The image.* The images of (1)--(3) generate $GL(P_0/2P_0)\cong S_3$ and the coordinate permutations of the $\bar d_i$, that is $S_3\times S_7$, of order $30\,240$, and those of (4)--(5) generate the unipotent radical of $\Stab_{\Orth(q)}(J_0)$, of order $2^{13}$ (@thm:coble-plane-stabilizer-image(2), (3)). Hence the images of the family generate $\rho(\Stab_{\Orth(B)}(P_0))$, of the stated order.
:::

::: {.remark #rmk:o2-family-versus-record title="What the certificate of the record establishes"}
The record `computations/reports/coble_complete_plane_parabolic_generators.json` holds $28$ exact integral matrices of the shapes (1)--(5), and the source-hashed Sage certificate of research#667 verifies that each is Gram preserving, fixes $P_0$ and reduces as displayed. That is an integral *witness* for the shapes, and it is what a certificate can be: it does not prove that any family generates, and the completeness above is proved from the parabolic decomposition and the two generation lemmas, not from the certificate. The earlier $21$-matrix version of the record is corrected there by the seven sign reflections of (3), which is exactly the $L$-part the reduction needs.
:::

::: {.theorem #thm:o2-plane-family-kernel title="Complete integral families for the plane stabilizers of $\widetilde O$ and $\widetilde O^+$"}
In the notation of @thm:o2-plane-family, put $\Gamma_{GL}(2)\definedas\ker\bigl(GL_2(\bZ)\to GL_2(\bF_2)\bigr)$, $\Gamma_{SL}(2)\definedas\Gamma_{GL}(2)\intersect SL_2(\bZ)$, and
$$
X=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
Y=\begin{pmatrix}1&0\\2&1\end{pmatrix},\qquad
J=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
$$
Let $D[\pm1]\cong(\bZ/2)^7$ be the sign changes of $D$. Then

1. $\Stab_{\widetilde O}(P_0)=\bigl(\Gamma_{GL}(2)\times D[\pm1]\bigr)\ltimes U_{\mathrm{ev}}$ has the following complete family: the Levi lifts of $-I_2,X,Y,J$, the seven sign changes $r_{d_j}$, the fourteen transvections $E_{e_i,2d_j}$ ($i=1,2$, $j=1,\dots,7$), and $\sigma^2$;
2. $\Stab_{\widetilde O^+}(P_0)=\bigl(\Gamma_{SL}(2)\times D[\pm1]\bigr)\ltimes U_{\mathrm{ev}}$ has the complete family obtained from (1) by omitting $J$;
3. the discriminant images of both stabilizers are trivial.

Here $U_{\mathrm{ev}}=U\intersect\widetilde O$. The group identities use the standard generations $\Gamma_{GL}(2)=\generators{-I_2,X,Y,J}$ and $\Gamma_{SL}(2)=\generators{-I_2,X,Y}$, proved below; they do not use commutators of generators.
:::

::: {.proof}

First generate the two level-two matrix groups. In $SL_2(\bZ)$, left and right multiplication by $X^{\pm1}$ and $Y^{\pm1}$ are the even-step Euclidean operations on the first column. A matrix in $\Gamma_{SL}(2)$ has odd diagonal entries and even off-diagonal entries, so these operations reduce it to $\pm I_2$ followed by an even power of $X$; the factor $-I_2$ clears the sign. This proves the $SL_2$ generation. Multiplication by $J$ makes determinant $+1$ in the other $GL_2$ coset, proving the $GL_2$ generation.

(1) An element of $L$ is $\gamma\oplus(\gamma^{-1})^T\oplus\delta$ with $\delta\in\Orth(D)$ a signed permutation. It is the identity modulo $2B$ exactly when $\gamma\equiv I_2\pmod 2$ and the underlying permutation of $\delta$ is trivial, signs acting by $\pm1\equiv1\pmod2$; that is $L\intersect\widetilde O=\Gamma_{GL}(2)\times D[\pm1]$. An element $E_{e_i,w}$ is congruent to the identity modulo $2B$ exactly when $w\in2D$: $w$ is the $D$-component of $E_{e_i,w}(f_i)-f_i$, and $(d,w)$ is even for all $d\in D$ exactly when $w\in2D$, since $D$ is unimodular. The central shear $\sigma$ is not the identity modulo $2B$, so $\sigma\notin\widetilde O$. An element of $U$ is a product of the $E_{e_i,w}$ with the power $\sigma^c$, and it is the identity modulo $2B$ exactly when $w_1,w_2\in2D$ and $c$ is even: $\sigma$ acts by $f_1\mapsto f_1+e_2$, $f_2\mapsto f_2-e_1$, so $\sigma^2$ is the first even power and is the identity modulo $2B$, while $\sigma$ is not. Hence $U\intersect\widetilde O=\theset{E_{e_i,w}: w\in2D}\cdot\generators{\sigma^2}$, generated by the fourteen $E_{e_i,2d_j}$ by additivity and by $\sigma^2$. If $g=\ell u$ is the decomposition of an element of $\Stab_{\widetilde O}(P_0)$, its induced actions on $P_0/2P_0$ and $D/2D$ are trivial. Those induced actions are precisely the $\gamma$ and $\delta$ components of $\ell$, so $\ell\in L\intersect\widetilde O$ by the preceding computation; consequently $u=\ell^{-1}g\in U\intersect\widetilde O$. Intersecting with $\widetilde O$ respects the displayed semidirect splitting, by these graded actions and not merely by normality, and the stated complete family follows.

(2) The sign changes of the negative definite summand $D$ are spinor-positive, and $U$ is spinor-positive because its real points form a connected unipotent group. On the Levi factor the normalized real spinor norm is $\det\gamma$: determinant $+1$ follows from the connected $SL_2(\bR)$ action, and determinant $-1$ from the lift of $J$, namely $\tau=-\id_{U_1}\oplus\id_{U_2\perp D}$, whose spinor norm is $-1$ by @lem:split-isometry-spinor-norm and @lem:minus-identity-spinor-norm. Thus $\Stab_{\widetilde O^+}(P_0)$ is exactly the $\det\gamma=+1$ part of (1), and the complete family is obtained by omitting $J$.

(3) $\widetilde O=\ker\rho$ by definition, and $\widetilde O^+\subseteq\widetilde O$.
:::

::: {.lemma #lem:o2-line-reduction title="A line family is a family for $\Orth(\latI_{1,8})$"}
Let $v$ be primitive isotropic in $B=\latI_{2,9}$, split $B=P\perp K$ with $v\in P\cong\latI_{1,1}$ and $K\cong\latI_{1,8}$ (@lem:odd-unimodular-isotropic-splitting(1)), and put $U_v\definedas\ker\bigl(\Stab_{\Orth(B)}(v)\too\Orth(K)\bigr)$, so that $\Stab_{\Orth(B)}(v)=\Orth(K)\ltimes U_v$ with $U_v=\theset{E(v,k) : k\in K_{\mathrm{ev}}}$ (@lem:cusp-vector-stabilizer-image' proof).

1. For every generating set $F$ of $\Stab_{\Orth(B)}(v)$, the image of $F$ in $\Orth(K)=\Orth(v^{\perp B}/v)$ generates $\Orth(K)$.
2. Conversely, if $F_K$ generates $\Orth(K)$ and $\theset{k_1,\dots,k_9}$ is a $\bZ$-basis of $K_{\mathrm{ev}}$ (of rank $2+7=9$), then $F_K\cup\theset{E(v,k_i)}$ generates $\Stab_{\Orth(B)}(v)$.

So a complete integral family for the stabilizer of a primitive isotropic line exists if and only if $\Orth(\latI_{1,8})$ admits one.
:::

::: {.proof}

(1) The quotient map $\pi\colon\Stab_{\Orth(B)}(v)\too\Orth(K)$ is onto, so $\pi(\generators{F})=\generators{\pi(F)}=\Orth(K)$.

(2) $\Stab_{\Orth(B)}(v)=\Orth(K)\ltimes U_v$; $\generators{F_K}=\Orth(K)$ by hypothesis, and $\generators{E(v,k_i)}=U_v$ because $k\mapsto E(v,k)$ is an isomorphism of groups from $K_{\mathrm{ev}}$ onto $U_v$ ([@GHS08, §3.1, equation (5)], @lem:cusp-vector-stabilizer-image' proof). A generating set of each factor of a semidirect product generates the product.
:::

::: {.lemma #lem:o2-line-kernel-infinite title="The finite image cannot decide a line family"}
Let $B=U_1\perp K$, $K=U_2\perp D$, $D=\generators{-1}^7$, $v=e_1$.

1. $\Stab_{\Orth(B)}(v)\intersect\ker\rho_{T_\Co}$ contains an element of infinite order:
$$s\definedas\id_{U_1}\perp t_K(e_2,2d_1),\qquad
t_K(e_2,2d_1)(x)=x-(x,2d_1)e_2+(x,e_2)\,2d_1+2(x,e_2)e_2 .$$
2. $K$ is unimodular, and for $\varphi\in\Orth(K)$ the image $\rho(\id_{U_1}\perp\varphi)$ depends on $\varphi$ only modulo $2$, so the restriction of $\rho$ to $\Orth(K)$ factors through the finite group $\GL(K/2K)$; its kernel is therefore infinite, containing $s$ of (1). Consequently the equality $\rho(\generators{F})=\rho(\Stab_{\Orth(B)}(v))$, for a finite $F\subset\Stab_{\Orth(B)}(v)$, is a necessary and not a sufficient condition for $\generators{F}=\Stab_{\Orth(B)}(v)$, and no computation of that finite image can supply the missing condition.
:::

::: {.proof}

(1) $2d_1\in K_{\mathrm{ev}}$ because $(2d_1)^2=-4$, so $t_K(e_2,2d_1)$ is an integral isometry of $K$; it is the identity modulo $2K$ because its displacements are multiples of $2$; and $2K\subseteq2B$, so $s\in\ker\rho_{T_\Co}$. It fixes $e_1$, so $s\in\Stab_{\Orth(B)}(v)$. It is unipotent with nonzero logarithmic part ($f_2\mapsto f_2+2e_2+2d_1$), hence of infinite order: exact integer arithmetic gives $s^m\neq\id$ for $m=1,2,3,4$ and the displacement grows linearly (`computations/reports/coble_833-line-parabolic-checks.py`, part 4).

(2) $K=\latI_{1,8}$ is unimodular, so $A_K=K^*/K=0$. An isometry of $B$ fixing $v$ acts on $v^{\perp B}/v\cong K$, and on $A=B/2B$; the classes of $K$ generate $B/2B$ modulo those of $U_1$, so $\ker\rho$ meets $\Orth(K)$ in the isometries of $K$ that are trivial modulo $2K$. A finite family $F$ and the group it generates have the same image under $\rho$ whenever $F$ has full image; by (1) that image says nothing about the infinite part.
:::

::: {.remark #rmk:o2-record-line title="What the two line certificates establish, and what they do not"}
The certificate `computations/reports/coble_vector_parabolic_generators.py` builds the nine transvections $E(v,k_i)$ for a $\bZ$-basis of $K_{\mathrm{ev}}$ together with the reflections of $K$ in vectors of square $\pm2$, verifies that each is an integral Gram-preserving isometry fixing $v$, and computes by Schreier--Sims the order $89\,181\,388\,800=\abs{\Stab_{\Orth(q)}(c)}$ of their image in $\Orth(q_{T_\Co})$; the certificate `computations/reports/coble_full_discriminant_root_lifts.py` does the same at $u=e_0+e_2$ with $240$ root reflections. Both are integral *witnesses for the finite image*, and the second also an independent check of the order in @lem:cusp-vector-stabilizer-image(1). By @lem:o2-line-kernel-infinite they cannot be a completeness proof for the integral family, and by @lem:o2-line-reduction the family is complete only if its $K$-part generates $\Orth(\latI_{1,8})$, which no computation of a finite image can show.
:::

::: {.lemma #lem:o2-ert-hr-transport title="The integral transport to Heckman--Rieken and Everitt--Ratcliffe--Tschantz"}
Write $K=U_2\perp D$, with $U_2=\generators{e_2,f_2}$ and $D=\generators{d_1,\dots,d_7}$ as above. Put
$$
a=-2e_2-2f_2+\sum_{j=1}^7d_j,\qquad z=d_7-f_2,
$$
and define
$$
\beta_0=f_2-d_1-d_2,\qquad
\beta_1=-e_2-2f_2+\sum_{j=2}^7d_j,\qquad
\beta_i=d_{i-1}-d_i\quad(2\le i\le7).
$$
In the HR lattice $\bZ^{8,1}$, with basis $\varepsilon_0,\dots,\varepsilon_8$, form $(\varepsilon_0)^2=-1$ and $(\varepsilon_i)^2=1$ for $i>0$, put $v_8=3\varepsilon_0-\sum_{i=1}^8\varepsilon_i$, and let $\alpha_0=\varepsilon_0-\varepsilon_1-\varepsilon_2-\varepsilon_3$, $\alpha_i=\varepsilon_i-\varepsilon_{i+1}$ for $1\le i\le7$. Then

1. The linear map $\Phi\colon-K\isoto\bZ^{8,1}$ determined by $a\mapsto v_8$, $\beta_i\mapsto\alpha_i$ ($0\le i\le7$) is an integral isometry with integral inverse, and $\Phi(z)=\varepsilon_8$.
2. If $M_8$ is the $9\times9$ matrix displayed in [@ERT10, Theorem 2.1], then, after moving its time coordinate to the front and reversing the signs of its eight spatial coordinates, $\Phi m\Phi^{-1}=M_8$, where $m=-r_a$ is the identity on $\bZ a$ and minus the identity on $a^{\perp K}$.
3. The projective groups in [@ERT10, Theorem 2.1] lift to integral time-oriented orthogonal groups without losing elements: a scalar real matrix $\lambda I$ is orthogonal only for $\lambda=\pm1$, and the time-oriented projective class has a unique integral representative.
:::

::: {.proof}
(1) Both $(a,\beta_0,\dots,\beta_7)$ and $(v_8,\alpha_0,\dots,\alpha_7)$ are integral bases: their basis matrices relative to the coordinates above have determinants $-1$ and $+1$, respectively. Direct evaluation gives $a^2=1$, $\beta_i^2=-2$, $(\beta_0,\beta_3)=(\beta_1,\beta_2)=1$, $(\beta_i,\beta_{i+1})=1$ for $2\le i\le6$, and all the other off-diagonal pairings zero. The HR Gram matrix is exactly the negative of this one. Thus $\Phi^*b_{\bZ^{8,1}}=-b_K$, and integrality of the two basis matrices proves that it is an isometry of **integral** lattices, not merely an identification of their rational forms. Substituting the same matrices gives $\Phi(z)=\varepsilon_8$. `computations/reports/coble_833-ert-hr-transport.py` records these exact checks.

(2) One checks directly that $a^2=1$ and $m=-r_a$; its matrix and $M_8$ are compared by the stated permutation in that script. ERT's matrix is Gram preserving in its own last-time-coordinate convention, and the permutation is the coordinate change to HR's first-time-coordinate convention. This check is an identity of integral matrices, not a geometric assertion inferred from the word “longest”.

(3) Two matrices in one projective orthogonal class differ by a scalar, hence by $\pm I$. The element $-I$ interchanges the two components of the negative light cone, so each projective class acting on the chosen component has exactly one time-oriented representative. That representative is integral by ERT's construction of the Lorentzian matrices. This is the lift used everywhere below; no statement about the GHS normalized real spinor kernel is being smuggled into ERT's $O^+$.
:::

::: {.theorem #thm:o2-line-family title="Complete generating families for the full integral group and its line stabilizer"}
Retain @lem:o2-ert-hr-transport, and let $O^+_{\mathrm{time}}(K)$ be the time-oriented integral group pulled back through $\Phi$ from $\Orth^+(\bZ^{8,1})$ in [@HR14, Theorem 2.1]. Then

1. $O^+_{\mathrm{time}}(K)=\generators{r_{\beta_0},\dots,r_{\beta_7},r_z}$.
2. $\Orth(K)=O^+_{\mathrm{time}}(K)\times\generators{-\id_K}$, so the nine reflections of (1) together with $-\id_K$ generate $\Orth(K)$.
3. For a primitive isotropic vector $v\in B$ and $L=\bZ v$, the group $\Stab_{\Orth(B)}(v)$ is generated by these ten isometries, extended by $\id_P$, together with the nine transvections $E(v,k)$ for $k$ in the $\bZ$-basis $e_2,f_2,d_1+d_7,\dots,d_6+d_7,2d_7$ of $K_{\mathrm{ev}}$. For the line stabilizer,
$$\Stab_{\Orth(B)}(L)=\Stab_{\Orth(B)}(v)\times\generators{-\id_B},$$
and adjoining $-\id_B$ therefore gives a complete integral family.
:::

::: {.proof}

(1) [@HR14, Theorem 2.1] states that $\Orth^+(\bZ^{8,1})$, the forward Lorentz group preserving a component of the negative light cone, is generated by reflections in its roots of norms $1$ and $2$, and displays the simple roots $\alpha_0,\dots,\alpha_8$ with $\alpha_8=\varepsilon_8$. A fundamental chamber's simple reflections generate the Coxeter group, so the nine corresponding reflections generate the group. Transport them by @lem:o2-ert-hr-transport: $\alpha_0,\dots,\alpha_7$ give $\beta_0,\dots,\beta_7$, and $\alpha_8$ gives $z$. These are integral reflections in vectors of primitive squares $-2,-2$ and $-1$ on $K$. The superscript $+$ here is **time orientation**, not the normalized real spinor kernel of @conv:spinor-positive-subgroup.

(2) In the HR model, $-I$ interchanges the two components of the negative light cone, commutes with every isometry, and is not time-oriented. Every isometry either preserves or interchanges those components, so multiplication by $-I$ as necessary gives the direct product. Transporting back proves the full integral generation. This is the $-I$ step needed to pass from the published $O^+$ statement to $O(K)$.

(3) Apply @lem:o2-line-reduction with the generating family from (2); its nine transvections use exactly the displayed $\bZ$-basis of $K_{\mathrm{ev}}$. Finally, any isometry stabilizing $L$ sends $v$ to $\pm v$, and $-\id_B$ is central, belongs to no vector-fixing group with $v\neq0$, and is already in $\Orth(B)$. This proves the direct product and completes the line family. No finite-order calculation of a discriminant image is used as a completeness argument.
:::

::: {.lemma #lem:o2-explicit-transversal title="A generating family from an enumerated transversal"}
Let $S$ be a group, $F$ a finite symmetric generating set of $S$, $\rho\colon S\too H$ a homomorphism into a finite group acting on a set $\Omega$, $W\in\Omega$, $P\definedas\Stab_H(W)$ the stabilizer of $W$, $K\definedas S\intersect\rho^{-1}(P)$, and
$$\mathcal W\definedas\theset{\rho(s)^{-1}W : s\in S},$$
the orbit of $W$, a finite subset of $\Omega$. For $V\in\mathcal W$ choose $t_V\in S$ with $\rho(t_V)^{-1}W=V$, and put $t_W\definedas1$.

1. The map $Ks\mapsto\rho(s)^{-1}W$ is a bijection $K\backslash S\isto\mathcal W$; in particular the $t_V$ form a left transversal of $K$ in $S$.
2. For $V\in\mathcal W$ and $f\in F$ put $V'\definedas\rho(f)^{-1}V$. Then $t_Vft_{V'}^{-1}\in K$.
3. $K$ is generated by the finite set $\theset{t_Vft_{V'}^{-1} : V\in\mathcal W,\ f\in F}$.
:::

::: {.proof}

(1) *Well defined.* For $k\in K$ one has $\rho(ks)^{-1}W=\rho(s)^{-1}\rho(k)^{-1}W=\rho(s)^{-1}W$, because $\rho(k)\in P$ stabilizes $W$. *Injective.* If $\rho(s)^{-1}W=\rho(s')^{-1}W$, then $\rho(s's^{-1})W=\rho(s')\rho(s)^{-1}W=\rho(s'){\rho(s')}^{-1}W=W$, so $\rho(s's^{-1})\in P$ and $s's^{-1}\in K$, that is $Ks=Ks'$. *Surjective.* Given $V=\rho(s)^{-1}W\in\mathcal W$, the element $t_V$ has the same property, so $Ks$ maps onto $V$ and every $V$ is attained.

(2) Put $g\definedas\rho(t_Vft_{V'}^{-1})=\rho(t_V)\rho(f)\rho(t_{V'})^{-1}$. Then
$$gW=\rho(t_V)\rho(f)\rho(t_{V'})^{-1}W=\rho(t_V)\rho(f)V'=\rho(t_V)\rho(f)\rho(f)^{-1}V=\rho(t_V)V=\rho(t_V)\rho(t_V)^{-1}W=W,$$
using $\rho(t_{V'})^{-1}W=V'$ and $\rho(t_V)^{-1}W=V$; so $g\in P$ and $t_Vft_{V'}^{-1}\in\rho^{-1}(P)\intersect S=K$.

(3) Let $k\in K$ and write $k=f_1\cdots f_m$ with $f_i\in F$, possible because $F$ generates $S$ and is symmetric. Put $V_i\definedas\rho(f_1\cdots f_i)^{-1}W$; then $V_0=V_m=W$, since $\rho(k)\in P$, and $V_i=\rho(f_i)^{-1}V_{i-1}$, so each pair $(V_{i-1},f_i)$ is one of the pairs of (2) with $V_i$ in the role of $V'$. Every factor of the product $\prod_{i=1}^{m}t_{V_{i-1}}f_it_{V_i}^{-1}$ therefore lies in $K$ by (2), and the product telescopes:
$$\prod_{i=1}^{m}t_{V_{i-1}}f_it_{V_i}^{-1}=t_{V_0}\,f_1\cdots f_m\,t_{V_m}^{-1}=t_W\,k\,t_W^{-1}=k.$$
So $K=\generators{\theset{t_Vft_{V'}^{-1}}}$.
:::

This is the Schreier argument of @lem:o2-even-part with the finite transversal *constructed* instead of assumed; the only finiteness used is that of the orbit $\mathcal W$, and no element of $H$ is ever lifted other than through an actual element of $S$. Applied with $S=\Stab_{\Orth(T_\Co)}(x)$, the group $K$ is the $R_\Gamma$-stabilizer, so an exact enumeration of $\mathcal W$ *is* an explicit finite integral family for it.

::: {.theorem #thm:o2-congruence-family title="Complete integral families for the two $R_\Gamma$ stabilizers"}
Keep the notation of @sec-o2-groups, with $B=\latI_{2,9}=U_1\perp U_2\perp D$, $T_\Co=B(2)$ and $\rho\definedas\rho_{T_\Co}$, so that $A=A_{T_\Co}=B/2B$. The two-dimensional subspace
$$W\definedas A_{U(2)}=\generators{[e_1/2],[f_1/2]}=\generators{e_1,f_1}\ \text{in}\ B/2B$$
is the image of the $U(2)$ summand: $T_\Co=B(2)=U_1(2)\perp K(2)$ and $K(2)=\latI_{1,8}(2)$ is isometric to $\generators{2}\oplus E_8(2)$, so $U(2)=2U_1$ and its discriminant classes are those of $e_1,f_1$. Let $P=\Stab_{\Orth(q)}(W)$.

1. *(The line.)* Take $S=\Stab_{\Orth(T_\Co)}(e_1)$ and $F$ the symmetrization of the complete family of @thm:o2-line-family — the same family with the inverse of each of its $19$ members adjoined, so a list of $38$ entries. Then $\mathcal W$ has exactly $256$ elements, and the family of @lem:o2-explicit-transversal has $256\cdot38=9728$ entries, of which $1306$ are the identity and $948$ are pairwise distinct integral matrices. It generates $\Stab_{R_\Gamma}(e_1)$, and together with $-\id_B$ it generates
$$\Stab_{R_\Gamma}(\bZ e_1)=\Stab_{R_\Gamma}(e_1)\times\generators{-\id_B}.$$
2. *(The plane.)* Take $S=\Stab_{\Orth(T_\Co)}(P_0)$ with $P_0=\generators{e_1,e_2}$ and $F$ the symmetrization of the complete family of @thm:o2-plane-family, a list of $60$ entries. Then $\mathcal W$ has exactly $768$ elements, and the family has $768\cdot60=46\,080$ entries, of which $4130$ are the identity and $2957$ are pairwise distinct integral matrices. It generates $\Stab_{R_\Gamma}(P_0)$.
3. *(Every other primitive isotropic object.)* Nothing in @lem:o2-explicit-transversal uses more than a finite symmetric generating set of $\Stab_{\Orth(T_\Co)}(x)$, the subspace $W$ and the homomorphism $\rho$; so for any primitive isotropic line or plane $x$, any proven complete integral family of $\Stab_{\Orth(T_\Co)}(x)$ runs through the same construction, with its own orbit $\mathcal W_x$, and yields a complete integral family of $\Stab_{R_\Gamma}(x)$.
4. *(What these families are not.)* They are families in the arithmetic group $R_\Gamma=\rho^{-1}(P)$ and in no monodromy group (@rmk:o2-congruence); the orbit counts of @thm:o2-lines(3c) and @thm:o2-planes(3c) are neither used nor reproved here, and no step replaces the completeness of $F$ by a computation in the finite group $\rho(S)$.
:::

::: {.proof}

Statements (1)--(2) are @lem:o2-explicit-transversal applied to the two standard objects, with the exact orbit enumeration of the certificate below. Its hypotheses are met: $F$ is finite and symmetric, $\rho(S)$ is finite because $A$ is finite, and the completeness of $F$, that is $S=\generators F$, is @thm:o2-line-family for the line and @thm:o2-plane-family for the plane. The orbit $\mathcal W$ is computed by breadth-first search from $W$ along the edges $V\mapsto\rho(f)^{-1}V$ for the finite symmetric list $F$, storing on the first visit of a state $V$ the integral matrix $t_V$ of the word reaching it; the search terminates because the set of two-dimensional subspaces of $A$ is finite — and in these two cases after $256$ and $768$ states. For each visited $V$ and each $f\in F$ the certificate forms the exact product $t_Vft_{\rho(f)^{-1}V}^{-1}$ and checks that it is an integral Gram isometry of $B$, that it fixes the object ($e_1$ pointwise for the line, $P_0$ as a lattice for the plane), and that its reduction modulo $2B$ stabilizes $W$ — the last being the element-wise assertion of @lem:o2-explicit-transversal(2), which the telescoping identity of part (3) upgrades to generation. The three counts distinguish the entries of the list, the identities $t_Vft_{V'}^{-1}=1$ (which occur exactly when the pair $(V,f)$ is a tree edge), and the remaining matrices, which are the family proper; distinctness is exact matrix equality. Clause (1)'s direct product is @lem:o2-level-two-membership(3), and $-\id_B$ lies in $\rho^{-1}(P)$ because $\rho(-\id_B)=\id$. Clause (3) restates (1)--(2) for an arbitrary complete family, which the construction consumes as an input and does not supply.

The two orbit sizes are consistent with the finite geometry of $A$ and with the published orders, which is a check on the identification of $W$: $[O:R_\Gamma]=[\Orth(q):P]=67\,456$ (@prop:gamma-co-images(3)), so for the line $|\mathcal W|=[\Stab_{\Orth(q)}(c):P\intersect\Stab_{\Orth(q)}(c)]=67\,456\cdot\lvert P\cdot c\rvert/527=67\,456\cdot2/527=256$ with $\lvert P\cdot c\rvert=2$ (@prop:coble-cong-point-stabilizer(2), $c=[e_1/2]$ lying in the two-element orbit inside $W$), and for the plane $|\mathcal W|=67\,456\cdot2160/189\,720=768$. Equivalently, the stabilizer in $P$ of the class of the standard line has order $89\,181\,388\,800/256=348\,364\,800$, and the stabilizer in $P$ of the standard decorated plane has order $247\,726\,080/768=322\,560$. All of this is finite-group arithmetic about $P$; the integral generation statements are (1)--(3).
:::

::: {.remark #rmk:o2-congruence-run title="The certificate, and the four checks it does and does not make"}
`computations/reports/coble_833-congruence-schreier.py` writes `computations/reports/coble_833-congruence-schreier.json`, which holds the two transversals — the $256$ and $768$ exact integral matrices $t_V$, indexed by the three nonzero vectors of $V$ — and the index of every member of each family as a pair (state, generator), from which the matrix $t_Vft_{V'}^{-1}$ is recomputed exactly. It also records, and the run transcript `...-schreier-run.txt` prints, these exact checks: the $527$ nonzero isotropic classes and the $67\,456$ plus-type two-dimensional subspaces of $A$ (so the index $[\Orth(q):P]$ of @prop:gamma-co-images(3) is reproduced); the orbits of $P$ on those classes, of sizes $2$, $120$, $270$, $135$, which are exactly the four numbers of @prop:coble-cong-point-stabilizer(2) and are what pins $W$ to $A_{U(2)}$; the Gram preservation and the fixed object of every member of the two input families; the two determinants $2$ of the bases of $D^{\mathrm{ev}}$ and $K_{\mathrm{ev}}$ used in the proofs of @thm:o2-plane-family and @thm:o2-line-family; the words in $W,A$ for the standard generators of $GL_2(\bZ)$; the $9728$ and $46\,080$ members with their Gram, isotropy and $W$-stability checks; and the telescoping identity of @lem:o2-explicit-transversal(3) on random elements of $K$, reproduced exactly. It does **not** prove the completeness of $F$ — that is @thm:o2-line-family and @thm:o2-plane-family — and it does not identify $R_\Gamma$ with any monodromy group.
:::

::: {.remark #rmk:o2-which-summand title="Which hyperbolic summand carries $A_{U(2)}$, and why the answer does not enter the proof"}
The model $B=\latI_{2,9}=U_1\perp U_2\perp D$, $T_\Co=B(2)$, carries two hyperbolic summands $2U_1$ and $2U_2$, each isometric to $U(2)$, and the page's decomposition $T_\Co=\generators{h}\oplus E_{10}(2)$ does not by itself say which of them is the $U(2)$ block: since $2K=I_{1,8}(2)=U(2)\perp\generators{-2}^7$ is isometric to $\generators{2}\oplus E_8(2)$, either hyperbolic plane can be paired with a $\generators{2}$-direction inside the other to produce the stated decomposition. @thm:o2-congruence-family fixes the choice by taking $W=\generators{[e_1/2],[f_1/2]}$, the discriminant block of $2U_1$, and the certificate confirms it in the only way available inside this model: $P$ then has orbits $2$, $120$, $270$, $135$ on the $527$ isotropic classes, and the class $[e_1/2]$ of the standard line lies in the two-element orbit, which is $W\intersect\mathcal C$ and is the orbit @prop:coble-cong-point-stabilizer(2) attaches to the two isotropic classes $u_1,u_2$ of $A_{U(2)}$.

The construction of @lem:o2-explicit-transversal is insensitive to that choice — it needs a finite symmetric generating set of $S_x$, the subspace $W$ and $\rho$ — but the *group it outputs* is not: the other choice $W'=\generators{[e_2/2],[f_2/2]}$ gives the conjugate stabilizer of a different plus-type two-dimensional subspace, and the same script then returns $|\mathcal W|=17\,280$ for the line $\bZ e_1$ (whose class then lies in the orbit of size $135$) and $|\mathcal W|=768$ for $P_0$, with its own families. Both computations are certified by the same certificate, which prints the orbit of $[e_1/2]$ under $P$ together with the four orbit sizes; what the theorem states, and what the acceptance of sage-extensions\#286 needs, is the family for the subgroup attached to the summand named there, and the corpus's $P$ is the one for which the primitive isotropic classes with vanishing $E_8(2)$-component lie in the two-element orbit.
:::

## The orbit-fibre theorem, group by group {#sec-o2-orbit-fibres}

@sec-o2-lines and @sec-o2-planes prove the two fibre statements and the two stabilizer-image statements, and @sec-o2-families the complete integral families. This section assembles them into the statement obligation O3 (research#834) asks for: for each group, the fibre over each orbit of discriminant data and the number of lattice orbits, with the published double-coset reduction applied where its hypothesis holds and named as the theorem used where it does not, every stabilizer image computed from an integral stabilizer proved complete, and every count derived from an image rather than copied from a table. It closes with what does, and what does not, change when the marked $U(2)$ block is replaced by an isometric block (@lem:o2-marking-immaterial): that is the only place in the two orbit theorems where a coordinate choice enters.

::: {.theorem #thm:o2-orbit-fibres title="The orbit fibres, the double-coset formula, and the eight stabilizer images"}
Keep the notation of @sec-o2-groups: $B=\latI_{2,9}$, $T_\Co=B(2)$, $q=q_{T_\Co}$, $\rho=\rho_{T_\Co}\colon O\definedas\Orth(T_\Co)\too Q\definedas\Orth(q)$, $\widetilde O\definedas\ker\rho$, $\widetilde O^+\definedas\widetilde O\intersect\Orth^+(T_\Co)$, $P\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ and $R_\Gamma\definedas\rho^{-1}(P)$ (@def:o2-groups, @prop:coble-cong-point-stabilizer(1)). Let $\mathcal X$ be the set of primitive isotropic lines $\mathcal L$ or of primitive isotropic planes $\mathcal P$ of $T_\Co$, let $\mathcal Y$ be the corresponding set of finite data — the $527$ nonzero isotropic classes $\mathcal C$ (@lem:isotropic-classes-lift(2)) or the $189\,720=8\cdot23\,715$ decorated planes $\mathcal D$ (@lem:plane-stars(1), @prop:coble-planecusp-finite(3)) — and let $\Gamma$ be a subgroup with $\widetilde O^+\iscontainedin\Gamma\iscontainedin O$, $H\definedas\rho(\Gamma)$. For $x\in\mathcal X$ write $H_x\definedas\Stab_O(x)$, the **full** integral stabilizer of $x$ in $O$, as opposed to a subgroup of it that generates the same discriminant image.

1. (Fibres, for every group between $\widetilde O^+$ and $O$.) The datum map $D\colon\mathcal X\too\mathcal Y$ — $\ell\mapsto[\ell/2]$ for lines (@lem:o2-line-classmap(1)) and $P\mapsto(J(P),s(P))$ for planes (@thm:coble-integral-plane-lifting(1)) — is $\rho$-equivariant, attains every element of $\mathcal Y$, and its fibres are single $\widetilde O^+$-orbits (@lem:o2-line-classmap(3), @thm:coble-integral-plane-lifting(2)). Hence $D$ induces a bijection
$$\Gamma\backslash\mathcal X\ \isoto\ H\backslash\mathcal Y,\qquad
\text{so}\qquad \abs{\Gamma\backslash\mathcal X}=\abs{\rho(\Gamma)\backslash\mathcal Y},$$
and for each $D_0\in\mathcal Y$ the discriminant image of the stabilizer of an object of that datum is the whole finite stabilizer of the datum, not a proper subgroup of it:
$$\rho\bigl(\Stab_\Gamma(x)\bigr)=H\intersect\Stab_Q(D_0)\qquad\text{for every }x\in\mathcal X\ \text{with}\ D(x)=D_0,$$
so that the fibre of the orbit map is a single point per datum and no datum contributes a second orbit.
2. (The double-coset formula, where its hypothesis holds.) Suppose in addition that $\widetilde O\iscontainedin\Gamma$; among the four groups this holds for $\Gamma=O$, for $\Gamma=\widetilde O$ and for $\Gamma=R_\Gamma$. Then $O$ is transitive on $\mathcal X$ (@lem:I29-plus-line-transitivity for lines, @thm:plane-transitivity-tco for planes), so $\mathcal X=O/H_x$ as a set and $\Gamma\backslash\mathcal X$ is the set of double cosets $\Gamma\backslash O/H_x$, and the reduction of [@SH23, Lemma 3.6] with $G=O$, $U=\widetilde O$, $K=\Gamma$, $H=H_x$ gives the equality of cardinalities
$$\abs{\Gamma\backslash\mathcal X}=\#\bigl(\Gamma\backslash O/H_x\bigr)=\#\bigl(\rho(\Gamma)\backslash Q/\rho(H_x)\bigr).$$
The hypothesis of that lemma is exactly $\widetilde O\subseteq\Gamma$; see the proof for why its disjointness step needs it, and for the reading of its statement as an equality of counts.
3. (Where the hypothesis fails, and what is used instead.) $\widetilde O\not\subseteq\Gamma$ for $\Gamma=\widetilde O^+$, for $SO=\ker\det$, for $O^+=\ker\spinornorm_\bR$ and for $SO^+=SO\intersect O^+$: for $\widetilde O^+$ because $\widetilde O^+=\widetilde O\intersect O^+$ with $O^+\neq O$ and $\widetilde O$ containing the spinor-negative element $\id_P\oplus(-\id_K)$ of @lem:cusp-vector-stabilizer-image(2); for $SO$ and $SO^+$ because $-\id_B\in\widetilde O$ has determinant $(-1)^{11}=-1$; for $O^+$ by the same element. For these four groups no application of [@SH23, Lemma 3.6] is made and no double-coset formula is asserted: the theorem used in its place is clause (1), whose fibre statement is proved for **every** subgroup containing $\widetilde O^+$ and not merely for those containing $\widetilde O$. Its proof, for both types, is the spinor-norm adjustment: an element of $\widetilde O$ carrying one primitive object to another of the same datum is multiplied by an explicit integral element of the $\widetilde O$-stabilizer of that object whose normalized real spinor norm is $-1$ — $\id_P\oplus(-\id_K)$ for a line (@lem:cusp-vector-stabilizer-image(2)), the conjugate of $\tau=-\id_{U_1}\oplus\id_{U_2\perp D}$ for a plane (@thm:coble-integral-plane-lifting(2), proof) — so that the product lies in $\widetilde O\intersect\Orth^+(T_\Co)$ and moves nothing.
4. (The eight stabilizer images, from integral stabilizers proved complete.) The table below gives, for each group and each of the two types, the discriminant image $\rho\bigl(\Stab_\Gamma(x)\bigr)$, its order, and the complete integral family of O2 that generates $\Stab_\Gamma(x)$ and from whose images the entry is computed. The column $\rho(\Gamma)\intersect\ldots$ is clause (1) with (S1) @lem:o2-line-stabilizer-image for lines and (S2) @lem:coble-plane-stabilizer-descends for planes; the point of the last column is that no entry rests on a finite-image computation alone.

| $\Gamma$ | $\rho(\Gamma)$, order | lines: $\rho(\Stab_\Gamma(\ell))=\rho(\Gamma)\intersect\Stab_Q([\ell/2])$ | order | planes: $\rho(\Stab_\Gamma(P))=\rho(\Gamma)\intersect S_{(J(P),s(P))}$ | order | the integral family proved to generate $\Stab_\Gamma(x)$ |
| --- | ---: | --- | ---: | --- | ---: | --- |
| $O$ | $Q=2^{21}3^55^27\cdot17\cdot31=46\,998\,591\,897\,600$ | $\Stab_Q([\ell/2])$ | $2^{21}3^55^27=89\,181\,388\,800$ | $S_{(J,s)}$ | $2^{18}3^35\cdot7=247\,726\,080$ | line: @thm:o2-line-family(3); plane: @thm:o2-plane-family (1)--(5) |
| $\widetilde O$ | $1$ | $1$ | $1$ | $1$ | $1$ | line: @thm:o2-stable-line(5); plane: @thm:o2-plane-family-kernel(1) |
| $\widetilde O^+$ | $1$ | $1$ | $1$ | $1$ | $1$ | line: @thm:o2-stable-line(5); plane: @thm:o2-plane-family-kernel(2) |
| $R_\Gamma$ | $P=2\cdot\abs{\Orth(q_{E_8(2)})}=696\,729\,600=\abs{W(E_8)}$ | $P\intersect\Stab_Q([\ell/2])$ | $2^{13}3^55^27=348\,364\,800$ | $P\intersect S_{(J,s)}$ | $2^{10}3^25\cdot7=322\,560$ | line: @thm:o2-congruence-family(1); plane: @thm:o2-congruence-family(2) |

The two $R_\Gamma$ orders are the index computations of @thm:o2-congruence-family's proof: $89\,181\,388\,800/2^8=348\,364\,800$ with $|\mathcal W|=2^8=256$ for the class $[\ell/2]$, and $247\,726\,080/768=322\,560$ with $|\mathcal W|=768$ for the decorated plane. The $O$ line entry is @lem:cusp-vector-stabilizer-image(1) and its order $\abs{Q}/527$; the $O$ plane entry is @thm:coble-plane-stabilizer-image(3) with @lem:plane-stars(2), and the factorisation $\abs{Q}/\abs{S_{(J,s)}}=2^3\cdot3^2\cdot5\cdot17\cdot31$ below is the check that the two are consistent.

5. (The eight counts, each derived from its two images.) The number of $\Gamma$-orbits of primitive isotropic lines and of primitive isotropic planes is

| $\Gamma$ | lines $\abs{\Gamma\backslash\mathcal L}$ | planes $\abs{\Gamma\backslash\mathcal P}$ | derivation |
| --- | ---: | ---: | --- |
| $O$ | $1$ | $1$ | transitivity of clause (2) with $H=Q$ |
| $\widetilde O$ | $527=17\cdot31$ | $189\,720=2^33^25\cdot17\cdot31$ | $\abs{Q}/\abs{\rho(H_x)}$ |
| $\widetilde O^+$ | $527$ | $189\,720$ | clause (1), the double-coset formula being inapplicable (3) |
| $R_\Gamma$ | $4=2+135+270+120$ | $7$ | $P$-orbits on $\mathcal C$ and on $\mathcal D$ |

with the derivations spelled out: $527=\abs{Q}/\abs{\Stab_Q([\ell/2])}=2^{21}3^55^27\cdot17\cdot31/(2^{21}3^55^27)=17\cdot31$; $189\,720=\abs{Q}/\abs{S_{(J,s)}}=2^{21}3^55^27\cdot17\cdot31/(2^{18}3^35\cdot7)=2^3\cdot3^2\cdot5\cdot17\cdot31=8\cdot23\,715$, so that the factor $8$ of stars and the $23\,715=45\cdot527$ undecorated planes both come out of the two orders rather than being inserted; and $2+135+270+120=527$, the four $P$-orbits of @prop:coble-cong-point-stabilizer(2) partitioning $\mathcal C$, while the seven $P$-orbits on $\mathcal D$ are those of @cor:coble-heegner-integral-plane-descent, of sizes $2160$, $3150$, $9450$, $7560$, $22\,680$, $69\,120$, $75\,600$, whose sum is $189\,720$. Each of these is an orbit count of an arithmetic group acting on $T_\Co$; none is a count of a monodromy group (clause (6)).
6. (What is not covered.) No clause is asserted for $\Gamma_\Co$ of @def:gamma-co-groups(1) or for $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5), and none of the four groups above is identified with either: the first identification is @conj:gamma-co-stable, open in the direction needed (@thm:gamma-co-is-stable(2)), and the second is false for the lattice group of the same index (@prop:coble-monodromy-equality-false). For the labelled base @thm:gamma-co-is-stable(1) gives only $\Gamma_\Co(B)\subseteq\widetilde O^+$, so $527$ and $189\,720$ are lower bounds for its counts by clause (1) and not the counts.
:::

::: {.proof}

*(1) The fibres and the stabilizer images.* Both datum maps are $\rho$-equivariant and onto by the statements cited in the clause: for lines @lem:o2-line-classmap(1), (2); for planes @thm:coble-integral-plane-lifting(1), whose attainment step uses @prop:coble-planecusp-finite(2) for the subgroup $J$ and the transitivity of $\Stab_Q(J)$ on the eight stars (@lem:plane-stars(1)) together with the surjectivity of $\rho$ onto $Q$ (@thm:two-elementary-surjectivity, [@Nik80, Theorem 3.6.3], its hypotheses verified in @prop:coble-discriminant-group). An equivariant map carries $\Gamma$-orbits into $H$-orbits, so $D$ induces a map of orbit sets, surjective because $D$ is onto. It is injective because each fibre is a single $\widetilde O^+$-orbit and $\widetilde O^+\subseteq\Gamma$: two objects with the same datum are $\widetilde O^+$-equivalent, hence $\Gamma$-equivalent. That is the bijection. For the stabilizer image, the inclusion $\subseteq$ is equivariance, and for the converse let $h\in H\intersect\Stab_Q(D_0)$ and $\gamma\in\Gamma$ with $\rho(\gamma)=h$; then $D(\gamma x)=hD_0=D_0$, so $\gamma x$ lies in the fibre of $x$, which is a single $\widetilde O^+$-orbit, so some $k\in\widetilde O^+$ has $k\gamma x=x$; then $k\gamma\in\Stab_\Gamma(x)$ and $\rho(k\gamma)=h$. This is @lem:o2-line-stabilizer-image(1) for lines and @lem:coble-plane-stabilizer-descends for planes, and it is the statement that the integral stabilizer is *full* over its finite image: $\rho\bigl(\Stab_\Gamma(x)\bigr)=H\intersect\Stab_Q(D_0)=F_{D_0}\intersect H$, with $F_{D_0}=\Stab_Q(D_0)$ of order $89\,181\,388\,800$ for a class and $247\,726\,080$ for a decorated plane, by @lem:cusp-vector-stabilizer-image(1) with $\abs{Q}/527$, and by @lem:plane-stars(2) with @thm:coble-plane-stabilizer-image(3).

*(2) The source's lemma, its hypothesis, and why it gives an equality.* [@SH23, Lemma 3.6] reads: let $G$ be a group, $U$ a normal subgroup and $K$, $H$ two subgroups such that $U\subset K$; then the quotient map $G\too G/U$ establishes a many-to-one correspondence between the double-coset decompositions of $G$ by $(K,H)$ and those of $G/U$ by $(K/U,\overline H)$, $\overline H$ the image of $H$. The quotient map is, of course, many-to-one on *elements*; what the proof gives on double cosets is stronger than a surjection, and it is what makes the formula a count. From a decomposition $G=\bigcup_i Kg_iH$ it obtains $G/U=\bigcup_i(K/U)\overline{g_i}\,\overline H$, and it concludes that these are *pairwise disjoint* — "since $U\subset K$, the double coset $Kg_iH$ is actually a union of left $U$-cosets" — so the displayed union is a double-coset decomposition of $G/U$ with one term per $i$, and the two double-coset sets are in bijection. The hypothesis enters exactly in that disjointness step: it is what makes the image of $Kg_iH$ equal to the single coset $(K/U)\overline{g_i}\,\overline H$. Two consequences are used above and neither is available without the hypothesis: distinct integral double cosets cannot merge on reduction, and no finite double coset is the image of two integral ones. With $G=O$, $U=\widetilde O$ (normal as a kernel), $K=\Gamma$ and $H=H_x$ one has $K/U=\rho(\Gamma)$ and $\overline H=\rho(H_x)$, so
$$\#\bigl(\Gamma\backslash O/H_x\bigr)=\#\bigl(\rho(\Gamma)\backslash Q/\rho(H_x)\bigr).$$
That is clause (2), the hypothesis $U\subseteq K$ being $\widetilde O\subseteq\Gamma$.

*(3) The four groups outside that hypothesis.* The witness $\id_P\oplus(-\id_K)$ of @lem:cusp-vector-stabilizer-image(2) lies in $\widetilde O$, fixes the primitive isotropic vector $v$ generating a line $L$, and has $\spinornorm_\bR=-1$ because the positive index of $K=\latI_{1,8}$ is $1$ (@lem:minus-identity-spinor-norm, @lem:split-isometry-spinor-norm); so it lies in $\widetilde O\sm\Orth^+(T_\Co)$. And $-\id_B$ lies in $\widetilde O$ with $\det=(-1)^{11}=-1$, so in $\widetilde O\sm SO$; it lies in $\Orth^+(T_\Co)$ because the positive index of $T_\Co$ is $2$, so the single element $-\id_B$ separates $\widetilde O$ from $SO$ and $\id_P\oplus(-\id_K)$ separates it from $O^+$ and from $SO^+$. Hence $\widetilde O$ is contained in none of $\widetilde O^+$, $SO$, $O^+$, $SO^+$, and [@SH23, Lemma 3.6] says nothing about any of them. What clause (1) uses instead is the fibre statement, and its two inputs are the two spinor-negative witnesses already displayed: for lines, if $k\in\widetilde O$ carries $v$ to $v'$ with $[v'/2]=[v/2]$, choose $\varepsilon\in\{\id,\id_P\oplus(-\id_K)\}\subseteq\Stab_{\widetilde O}(v)$ with $\spinornorm_\bR(\varepsilon)=\spinornorm_\bR(k)$ — possible because $\spinornorm_\bR$ is a homomorphism onto $\{\pm1\}$ and the set has one element of each value — and then $k\varepsilon^{-1}\in\widetilde O\cap\Orth^+$ still carries $v$ to $v'$; that is @lem:o2-line-classmap(3). For planes the same with $\tau$ and its conjugates, that is @thm:coble-integral-plane-lifting(2). Neither argument is the reduction through a normal subgroup, and neither could be replaced by one.

*(4) The table.* The $\rho(\Gamma)$ column is @def:o2-groups with @prop:coble-cong-point-stabilizer(1) for $P$; the $\widetilde O$ and $\widetilde O^+$ rows have trivial image by definition of $\widetilde O=\ker\rho$. The two $O$ entries are the statements in (1) with $\Gamma=O$, $H=Q$. For $R_\Gamma$, $\rho(R_\Gamma)=P$ by @prop:gamma-co-images(3), and (S1), (S2) with $\Gamma=R_\Gamma$ give the two intersections with $P$; their orders are computed from the transversals rather than asserted: $\abs{P\intersect\Stab_Q([\ell/2])}=\abs{P}/\abs{P\cdot[\ell/2]}=\abs P/2=348\,364\,800$, the class $[e_1/2]$ lying in the two-element $P$-orbit of @prop:coble-cong-point-stabilizer(2) (@rmk:o2-which-summand); and $\abs{P\intersect S_{(J,s)}}=\abs{S_{(J,s)}}/768=322\,560$, because the transversal of @lem:o2-explicit-transversal for the plane has $768$ elements, that is $[S_{(J,s)}:P\intersect S_{(J,s)}]=768$ (@thm:o2-congruence-family(2) and its proof). The integral families named in the last column are the O2 families; that each generates its stabilizer is @thm:o2-line-family(3), @thm:o2-plane-family, @thm:o2-plane-family-kernel, @thm:o2-stable-line(5) and @thm:o2-congruence-family(1), (2), so each image in the table is the image of a family proved to generate the group and not the image of a finite set of guesses: that is the sense in which no finite-image computation is substituted for an integral statement. The four orders on the $O$ and $R_\Gamma$ lines are the four that (5) divides by, so the table and the count table are two readings of the same two stabilizer-image computations.

*(5) The counts.* For $\Gamma=O$ both sets are single orbits: transitivity on lines is @lem:I29-plus-line-transitivity and on planes @thm:plane-transitivity-tco. For $\widetilde O$ and $\widetilde O^+$ the image is trivial, so clause (1) gives exactly the number of data: $527$ and $8\cdot23\,715$. The two factorisations are the displayed divisions, in which $\abs{Q}=2^{21}3^55^27\cdot17\cdot31$ is the order of the full discriminant orthogonal group (@lem:coble-full-finite-image-root-lifts, whose $496$ integral root reflections generate it and whose exact Schreier--Sims computation returns this order), $\abs{\Stab_Q([\ell/2])}=\abs{Q}/527$ is @lem:cusp-vector-stabilizer-image(1), and $\abs{S_{(J,s)}}=2^{18}3^35\cdot7$ is @thm:coble-plane-stabilizer-image(3). Both divisions are exact, which is a check on the two stabilizer images and on the identification of the data: $527=17\cdot31$ and $189\,720/(8)=23\,715=45\cdot527$. For $R_\Gamma$ the image is $P$ and the counts are the $P$-orbit decompositions of $\mathcal C$ and $\mathcal D$: the four orbits of @prop:coble-cong-point-stabilizer(2), of sizes $2,135,270,120$, summing to $527$; and the seven of @cor:coble-heegner-integral-plane-descent, of sizes $2160,3150,9450,7560,22680,69120,75600$, summing to $189\,720$, the sum of that corollary's column of decorated-plane orbit sizes. That these two enumerations are enumerations of the group $P$ and not of another group of the same order is @prop:coble-cong-point-stabilizer(1) with @prop:gamma-cong-eq-heegner. No count in this clause is read off a public row: each is the cardinality of a set of data divided by the order of an integral stabilizer's image, or an enumerated orbit decomposition of that image.

*(6)* is the restriction stated in the clause: the only inclusions between a monodromy group and one of these four are @thm:gamma-co-is-stable(1) ($\Gamma_\Co(B)\subseteq\widetilde O^+$) and @lem:d2-degree-two-base(3) ($\Gamma_{\Co,2}\subseteq R_\Gamma\intersect\Orth^+$), and in both directions from these to a count the step is @conj:gamma-co-stable or @prop:coble-monodromy-equality-false.
:::

::: {.lemma #lem:o2-marking-immaterial title="Which $U(2)$ block is marked, and what does not depend on it"}
Let $A\definedas A_{T_\Co}=B/2B$ with the discriminant form $q$, and let $k\definedas[h/2]$ be the characteristic class, so that $A=\generators{k}\perp A^0$ with $A^0=A_{U(2)}\perp A_{E_8(2)}$ and **every** isometry of $q$ fixes $k$ (@lem:coble-discriminant-blocks(3), @prop:gamma-co-images proof Step 1). Call a two-dimensional subspace $W\leq A^0$ a **block** when it is spanned by classes $x,y$ with $q(x)=q(y)=0$ and $b(x,y)=\tfrac12$ — that is $W\iso q_{U(2)}$ — and when $V_W\definedas W^{\perp}\intersect A^0$ is isometric to $q_{E_8(2)}$. Put $P_W\definedas\Stab_Q(W)$ and $R_W\definedas\rho^{-1}(P_W)$. Then

1. $P_W=\Stab_Q(W)\intersect\Stab_Q(V_W)$ is the stabilizer of the decomposition $A^0=W\perp V_W$, and
$$P_W=\Orth(q|_W)\times\Orth(q|_{V_W}),\qquad
\abs{P_W}=2\cdot\abs{\Orth(q_{E_8(2)})}=2\cdot348\,364\,800=696\,729\,600=\abs{P},$$
where $\abs{\Orth(q|_W)}=2$ because among the three nonzero classes of $W$ exactly one has nonzero value, namely $x+y$, and every isometry of $W$ fixes it. So "the stabilizer of the decomposition $[h/2]^{\perp}=A_{U(2)}\oplus A_{E_8(2)}$" of @prop:gamma-co-images(3) and "the stabilizer of the block $A_{U(2)}$" are the same group, and that group is $P_{A_{U(2)}}$ of the statement: the decomposition contributes no datum beyond the block plus $k$, and $k$ is fixed by all of $Q$.
2. (The two blocks of the model are exchanged by an explicit integral isometry.) In $B=U_1\perp U_2\perp D$ put $W_1\definedas\generators{[e_1/2],[f_1/2]}=A_{2U_1}$ and $W_2\definedas\generators{[e_2/2],[f_2/2]}=A_{2U_2}$. Both are blocks, and the transposition $T$ of @thm:o2-plane-family(1) — $e_1\mapsto e_2$, $f_1\mapsto f_2$, $e_2\mapsto e_1$, $f_2\mapsto f_1$, $d_i\mapsto d_i$ — is a Gram-preserving integral automorphism of $B$, hence an element of $O=\Orth(T_\Co)$ because $T_\Co=B(2)$, with
$$\rho(T)W_1=W_2,\qquad \rho(T)k=k,\qquad\text{hence}\qquad T\,R_{W_1}\,T^{-1}=R_{W_2}.$$
$\rho(T)k=k$ is not an extra hypothesis: every isometry of $q$ fixes $k$ by (1).
3. (Every statement of @thm:o2-orbit-fibres is invariant under the marking.) Let $\sigma\in Q$ with $\sigma W=W'$ for two blocks, and $g\in O$ with $\rho(g)=\sigma$, which exists by @thm:two-elementary-surjectivity. Then $g\,R_W\,g^{-1}=R_{W'}$, and $x\mapsto gx$ is a bijection $\mathcal L\too\mathcal L$, $\mathcal P\too\mathcal P$ carrying $R_W$-orbits onto $R_{W'}$-orbits, fibres onto fibres, and $\Stab_{R_W}(x)$ onto $\Stab_{R_{W'}}(gx)$. Consequently the bijections of @thm:o2-orbit-fibres(1), the stabilizer images of (4) and the counts of (5) are the same for $R_W$ and for $R_{W'}$: in particular the $R_\Gamma$ rows $4$ and $7$ hold for every block, and a coordinate identification that picks the *other* block of the same model cannot change them.
4. (What does depend on the marking, and where it is recorded.) The left transversal of @lem:o2-explicit-transversal does depend on $W$, hence so does the family of @thm:o2-congruence-family: for $W_1$ and the class $[e_1/2]$ the orbit $\mathcal W$ has $256$ elements, for $W_2$ it has $17\,280$. This is consistent with (3) and no contradiction: the orbit *count* of $P$ on $\mathcal C$ is four for both blocks (@prop:coble-cong-point-stabilizer(2) for the one and (3) of this lemma for the other), while the class $[e_1/2]$ lies in a $P_{W_1}$-orbit of size $2$ and in a $P_{W_2}$-orbit of size $135$, the two indices being $\abs{\Stab_Q([e_1/2])}/\abs{P\cap\Stab_Q([e_1/2])}=89\,181\,388\,800/348\,364\,800=256$ for $W_1$ and $89\,181\,388\,800/(696\,729\,600/135)=17\,280$ for $W_2$. The family, unlike the orbit count, is a statement about a subgroup of $O$ and not about its conjugacy class, and it is stated per marking: @thm:o2-congruence-family(3) for an arbitrary complete input family, and @rmk:o2-which-summand for the two marks of the model.
:::

::: {.proof}

*(1)* Since $k$ is fixed by every isometry of $q$ (@lem:coble-discriminant-blocks(3)), an isometry stabilizing $W$ preserves $W^{\perp}=\generators{k}\perp V_W$ and hence $V_W$; conversely an element of $\Orth(q|_W)\times\Orth(q|_{V_W})$, extended by $k\mapsto k$, stabilizes $W$. So $P_W=\Orth(q|_W)\times\Orth(q|_{V_W})$. On $W$ the form has $q(x)=q(y)=0$ and $q(x+y)=q(x)+q(y)+b(x,y)=1$, so $x+y$ is the only class of $W\sm\generators{0}$ of value $1$ and every isometry of $W$ fixes it and permutes $\{x,y\}$: $\abs{\Orth(q|_W)}=2$. On $V_W$ the form is $q_{E_8(2)}$, of plus type, with $136$ classes of value $0$ and $120$ of value $1$ in the $\bZ/2$ normalisation of @lem:coble-discriminant-blocks(2), so $\Orth(q|_{V_W})\iso\operatorname{GO}^+_8(2)$ of order $348\,364\,800$ (@lem:weyl-E8-mod-two). The product is $2\cdot348\,364\,800=696\,729\,600$, which is the order @prop:coble-cong-point-stabilizer(1) gives $P$: the two computations agree, one from the splitting of the form and one from the identification $P=\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$.

*(2)* $T$ permutes the two hyperbolic summands of $B$ and fixes $D$ pointwise, so it preserves the Gram matrix of $B$ and is integral; $\Orth(B(2))=\Orth(B)$ as subgroups of $\GL_{11}(\bZ)$, so $T\in O$. For a primitive vector $v$ of $T_\Co$ one has $\rho(T)[v/2]=[Tv/2]$ (@lem:o2-line-classmap(1)), and $Te_1=e_2$, $Tf_1=f_2$, so $\rho(T)[e_1/2]=[e_2/2]$ and $\rho(T)[f_1/2]=[f_2/2]$, that is $\rho(T)W_1=W_2$. Conjugation by $T$ carries $\rho^{-1}(\Stab_Q(W_1))$ to $\rho^{-1}(\rho(T)\Stab_Q(W_1)\rho(T)^{-1})=\rho^{-1}(\Stab_Q(W_2))$. $T$ is one of the thirty generators of @thm:o2-plane-family, so the conjugating element is not produced by an existence argument: it is a displayed integral matrix in the family this book already uses. For admissibility of $W_2$: $T_\Co=2U_1\perp I_{1,8}(2)$ with $I_{1,8}(2)\iso\generators{2}\oplus E_8(2)$ (@thm:indefinite-unimodular-classification applied to $I_{1,8}\iso\generators{1}\oplus E_8(-1)$ and scaled by $2$), so taking $U(2)\definedas 2U_2$ inside $I_{1,8}(2)=2U_2\perp\generators{-2}^{7}$ exhibits $W_2$ as the $U(2)$ block of a second decomposition of the same lattice — this is @rmk:o2-which-summand's sentence that either hyperbolic summand can be the $U(2)$ block. Whether that second decomposition is the geometrically marked one is a question about the degree-two datum and not about $T_\Co$; (3) is the statement that no answer to it changes the orbit theorems.

*(3)* $\rho(gR_Wg^{-1})=\rho(g)\Stab_Q(W)\rho(g)^{-1}=\Stab_Q(W')$, so $gR_Wg^{-1}=R_{W'}$. The map $x\mapsto gx$ is a bijection of $\mathcal X$ because $g\in O$ is invertible, it carries $\Gamma$-orbits to $g\Gamma g^{-1}$-orbits and $\Stab_\Gamma(x)$ to $\Stab_{g\Gamma g^{-1}}(gx)$; applied to $\Gamma=R_W$ this gives the four statements. For the fibre statement: if $D(x)=D(y)$ and $y=kx$ with $k\in\widetilde O^+$, then $g(y)=(gkg^{-1})(gx)$ with $gkg^{-1}\in\widetilde O^+$, $\widetilde O^+$ being normal in $O$ — so the fibres are single orbits for $R_{W'}$ as well, which is clause (1) again and therefore not an extra assumption.

*(4)* The two transversal sizes are @thm:o2-congruence-family(1) and @rmk:o2-which-summand. The two indices: $\mathcal W$ of @lem:o2-explicit-transversal is the left transversal of $K=S\intersect\rho^{-1}(P)$ in $S=\Stab_O(x)$, so $\abs{\mathcal W}=\abs{\rho(S)}/\abs{\rho(S)\intersect P}$; for the line $\rho(S)=\Stab_Q([e_1/2])$ of order $89\,181\,388\,800$ and for the plane $\rho(S)=S_{(J,s)}$ of order $247\,726\,080$, so $\abs{\mathcal W}=256$ and $768$ are exactly the indices displayed in @thm:o2-orbit-fibres(4), and they are consistent with $\abs{P\cap\Stab_Q([e_1/2])}=\abs P/2$ and $\abs{P\cap S_{(J,s)}}=\abs{S_{(J,s)}}/768$. For the other block the class $[e_1/2]$ lies in a $P_{W_2}$-orbit of size $135$, so $\abs{P_{W_2}\cap\Stab_Q([e_1/2])}=\abs P/135$ and the transversal of $\Stab_O(\bZ e_1)$ acquires $89\,181\,388\,800\cdot135/696\,729\,600=17\,280$ elements, as recorded there; the orbit count of $P_{W_2}$ on $\mathcal C$ is still four, by (3).
:::

## What the later obligations consume {#sec-o2-consumers}

The chain of research#667 divides the question into five obligations; this section is O2, and @tbl-o2-consumers states, for each later obligation, which statement of this section it may cite and which statement it must still supply. A statement of this section is available to the others at the strength stated, and at no other strength.

| Obligation | Consumes from this section | Must supply itself |
| --- | --- | --- |
| O3, research#834 (orbit fibres over every discriminant class) | the statement itself, in @thm:o2-orbit-fibres: the two fibre bijections for every $\Gamma$ with $\widetilde O^+\iscontainedin\Gamma\iscontainedin\Orth(T_\Co)$ (1), the double-coset formula $\abs{\Gamma\backslash\mathcal X}=\#\bigl(\rho(\Gamma)\backslash Q/\rho(H_x)\bigr)$ where $\widetilde O\subseteq\Gamma$ (2) with the source's hypothesis checked line by line, the theorem used in its place for the four groups that do not contain $\widetilde O$ (3), the eight stabilizer images with the integral families that generate each (4), and the eight counts derived from those images (5); @lem:o2-marking-immaterial decides which part of that argument depends on the choice of $U(2)$ block | nothing for the four groups. What O3 still owns: any identification of one of the four with a monodromy group, which is @conj:gamma-co-stable and @prop:coble-monodromy-equality-false and not a theorem; and the fibre statement for any fifth group the public operation may build, since (2) needs $\widetilde O\subseteq\Gamma$ and (1) alone gives the bijection but not a double-coset formula |
| O4, research#835 (complete integral line-plane incidence) | the plane classification by decorated pairs and the line classification by classes, hence the two vertex sets of the incidence graph — $\widetilde O^+$: $527$ lines and $189\,720$ planes, $R_\Gamma$: $4$ and $7$ (@thm:o2-orbit-fibres(1), (5)) — @thm:coble-integral-flag-lifting for the flags, and the plane stabilizer image $\rho(\Stab_{R_\Gamma}(P))=P\intersect S_{(J,s)}$ of @thm:o2-orbit-fibres(4), the group that condition ($\ast$) is a statement about | the condition ($\ast$) of @thm:coble-integral-incidence, that every permutation of $J\sm\generators{0}$ realized by $H$ is realized in the stabilizer of the decorated plane; @cor:coble-integral-incidence-rows(3) records it as unproved for $R_\Gamma$, and @prop:coble-incidence-not-automatic shows it is not a consequence of the containment $\widetilde O^+\iscontainedin\Gamma$ |
| O5, research#836 (public operation and certified cards) | the four counts of @thm:o2-lines(3) and @thm:o2-planes(3) with their derivations in @thm:o2-orbit-fibres(5), the eight stabilizer images and orders of @thm:o2-orbit-fibres(4) with the integral family generating each, @thm:o2-plane-family with @thm:o2-plane-family-kernel for the full and stable plane families, and @thm:o2-line-family with @thm:o2-stable-line for the full and stable line families; @thm:o2-stable-line(4) supplies the trivial stable discriminant images | the public operation itself and the card entries. For both line and plane rows of $R_\Gamma$: nothing, @thm:o2-congruence-family supplies the families, and the record `computations/reports/coble_833-congruence-schreier.json` their transversals |

: What each later obligation of the chain consumes. {#tbl-o2-consumers}

Three points in those rows deserve the emphasis they get there. First, the clause of sage-extensions#286's acceptance that asks for "a theorem the call uses instead" is answered by @thm:o2-orbit-fibres(3), and the answer is not vacuous for either type: of the four groups only $O$, $\widetilde O$ and $R_\Gamma$ contain $\widetilde O$, so the double-coset formula of [@SH23, Lemma 3.6] applies to six of the eight rows and to none of the $\widetilde O^+$, $SO$, $O^+$, $SO^+$ rows. For those the argument is the fibre statement with the spinor-negative witness, which is what @thm:o2-orbit-fibres(1), (3) state, and it is the same argument that proves the line double-coset *formula* of @thm:o2-lines(2) without ever pretending that the hypothesis $U\subseteq K$ of the source's lemma holds. Second, the incidence of O4 is *not* determined by the two orbit sets: @prop:coble-incidence-not-automatic exhibits a subgroup containing $\widetilde O^+$ over which eight flag orbits fall onto four edges, so the edge count and the flag count can agree while the forgetful map is not injective. Third, a card entry of O5 that reproduces a number of @thm:o2-orbit-fibres(5) reproduces a count of an arithmetic group: it does not become a count of $\Gamma_\Co$ or of $\Gamma_{\Co,2}$, and @lem:o2-marking-immaterial(3) is the sense in which even the choice of $U(2)$ block in the coordinates cannot change it — while the recorded transversal of @thm:o2-congruence-family does depend on that choice and is recorded per marking.

## What is not covered {#sec-o2-not-covered}

1. **The monodromy groups.** No statement of this section is a statement about $\Gamma_\Co$ of @def:gamma-co-groups(1) or about $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5). The identification of $\Gamma_\Co$ with a lattice group is @conj:gamma-co-stable and is not a theorem (@thm:gamma-co-is-stable(2)); on the labelled base only $\Gamma_\Co(B)\subseteq\widetilde O^+$ is proved, so @thm:o2-lines(3b) gives $527$ as a lower bound for $\Gamma_\Co(B)$ and nothing for $\Gamma_\Co$. For $\Gamma_{\Co,2}$ the containment $\Gamma_{\Co,2}\subseteq R_\Gamma\intersect\Orth^+(T_\Co)$ is @lem:d2-degree-two-base(3) and the reverse inclusion fails (@prop:coble-monodromy-equality-false), so no count of $R_\Gamma$ transfers.
2. **Eichler's criterion is not used.** No step of this section needs it, and none could: it requires a summand $U\oplus U$ in the lattice acted on, and $T_\Co$ has none. What replaces it is the parabolic decomposition of each stabilizer with the surjectivity of $\rho$ onto $\Orth(q_{T_\Co})$ ([@Nik80, Theorem 3.6.3], hypotheses verified in @prop:coble-discriminant-group) and the spinor-norm adjustment of @lem:o2-line-classmap(3).
3. **The published inputs, with their hypotheses on these objects.** [@DK13, (3.6)] is the lattice and [@DK13, Proposition 3.2] the period quotient, hypotheses checked in @sec-o2-groups. [@Nik80, Theorem 3.6.3] is the surjectivity of $\rho$ for an even, indefinite, $2$-elementary lattice, and $T_\Co$ is one, of signature $(2,9)$ and with $\abs{A_{T_\Co}}=2^{11}$. [@GHS08, §3.1, equations (4) and (5)] supply only the transvection formula and additivity on the integral form, with the parity condition $k\in K_{\mathrm{ev}}$. [@SH23, Lemma 3.6] is used only for $\Gamma\supseteq\widetilde O$, where its inclusion hypothesis holds (@thm:o2-lines(2)). [@HR14, Theorem 2.1] applies in rank $9$ to the time-oriented integral group of the odd unimodular lattice; [@HR14, Theorem 2.2] and [@ERT10, Theorem 2.1] apply at $n=8$, with the norm-one reflection subgroup of index $2$ and the displayed longest element. @lem:o2-ert-hr-transport verifies the integral basis, the projective/integral lift, the sign and time-coordinate conventions, and the transported matrix before these inputs are used. No Kneser or GHS generation theorem requiring Witt index at least $2$ is invoked: $K$ has Witt index $1$, and $T_\Co$ does not contain $U\oplus U$.
4. **(U2) is now proved, and what is still not.** @thm:o2-congruence-family gives explicit finite integral families generating $\Stab_{R_\Gamma}(P_0)$ and $\Stab_{R_\Gamma}(\bZ e_1)$ inside $\rho^{-1}(P)$, so (C4) and (C5) are proved and every entry of @tbl-o2-ledger is. Three things this section still does not assert: nothing about the monodromy groups $\Gamma_\Co$ and $\Gamma_{\Co,2}$ (@rmk:o2-congruence); no count of the $R_\Gamma$ orbits is rederived, those remain @thm:o2-lines(3c) and @thm:o2-planes(3c); and the completeness of the two input families is @thm:o2-line-family and @thm:o2-plane-family, whose published inputs are item 3 above, not the certificate of @rmk:o2-congruence-run.

## The stable-group line stabilizer {#sec-o2-stable-line}

The stable level is $\widetilde O=\ker\rho=\Gamma_B(2)=\theset{g\in\Orth(T_\Co):g\equiv\id\bmod2B}$. This section gives the level-two membership laws, proves the vector and line parabolic decompositions from the induced $K$-action, and then supplies the complete integral families through @thm:o2-stable-level-two-generation. It also computes the three character-kernel indices as $2,2,4$. The refuted $35$-element proposal and the inconclusive $21/45$ level-four span are retained only to record exactly what those data do and do not say.

Keep the notation of @lem:cusp-vector-stabilizer-image: $v$ is primitive isotropic, $L=\bZ v$, $B=P\perp K$ with $P=\bZ v\oplus\bZ w\cong\latI_{1,1}$ and $K=v^{\perp B}/v\cong\latI_{1,8}$, $K_{\mathrm{ev}}=\theset{k\in K : k^2\in2\bZ}$, and
$$\Stab_{\Orth(B)}(v)=\Orth(K)\ltimes U_v,\qquad U_v=\theset{E(v,k) : k\in K_{\mathrm{ev}}},$$
the $\Orth(K)$ being the lift acting trivially on $P$. Write $\Gamma_K(2)\definedas\ker\bigl(\Orth(K)\too\Orth(K/2K)\bigr)=\theset{\varphi : \varphi\equiv\id\pmod{2K}}$.

::: {.lemma #lem:o2-level-two-membership title="The level-two membership laws of the line parabolic"}
1. For $k\in K_{\mathrm{ev}}$ the transvection $E(v,k)$ lies in $\widetilde O$ if and only if $k\in2K$; hence $U_v\intersect\widetilde O=\theset{E(v,2k) : k\in K}$, a free abelian group of rank $9$, and $E(v,k)E(v,k')=E(v,k+k')$ makes $k\mapsto E(v,2k)$ an isomorphism onto it from $(K,+)$.
2. For $\varphi\in\Orth(K)$ the lift $\id_P\perp\varphi$ lies in $\widetilde O$ if and only if $\varphi\in\Gamma_K(2)$.
3. Consequently
$$\Stab_{\widetilde O}(v)=\bigl(\id_P\perp\Gamma_K(2)\bigr)\ltimes\theset{E(v,2k) : k\in K},\qquad
\Stab_{\widetilde O}(L)=\Stab_{\widetilde O}(v)\times\generators{-\id_B}.$$
:::

::: {.proof}

(1) Recall $E(v,k)(x)=x-(x,k)v+(x,v)k-\tfrac12(k,k)(x,v)v$ and $E(v,k)(w)=w-\tfrac12(k,k)v+k$ (@lem:cusp-vector-stabilizer-image' proof). Modulo $2B$ the displacement of $w$ has $K$-component $k$, so $E(v,k)\equiv\id\pmod{2B}$ forces $k\in2K$; and $k\in2K$ forces $(x,k)\in2\bZ$ for all $x\in B$ ($K$ being unimodular, so $k=2k'$ gives $(x,k)=2(x,k')$), $\tfrac12(k,k)=2(k',k')\in2\bZ$, and $k\in2B$, so every displacement lies in $2B$. Since $\widetilde O=\theset{g\equiv\id\bmod2B}$ this is the stated membership law. The rank is $\rank K=9$, and additivity in the second argument is [@GHS08, §3.1, equation (5)], checked exactly together with the two boundary cases $k=d_1+d_2\notin2K$ and $k=2d_1\in2K$ in `computations/reports/coble_833-stable-line-level2.py`, part 1 and 3. The second case is also the warning that the parameter is a basis of $K$, not of $K_{\mathrm{ev}}$: $2d_1\notin2K_{\mathrm{ev}}$, because $d_1\notin K_{\mathrm{ev}}$, while $E(v,2d_1)\in\widetilde O$.

(2) $\id_P\perp\varphi$ is congruent to the identity modulo $2B$ if and only if $\varphi$ is congruent to the identity modulo $2K$, $P$ being unimodular and $B=P\perp K$.

(3) Let $g\in\Stab_{\Orth(B)}(v)$ and write $g=(\id_P\perp\varphi)u$ with $\varphi\in\Orth(K)$ and $u\in U_v$. Its induced isometry on $v^{\perp B}/v\cong K$ is $\varphi$. If $g\in\widetilde O$, that induced action is trivial on $K/2K$, so $\varphi\in\Gamma_K(2)$. By (2), $\id_P\perp\varphi\in\widetilde O$; consequently $u=(\id_P\perp\varphi)^{-1}g\in\widetilde O$ too, and (1) gives $u=E(v,2k)$ for some $k\in K$. The other inclusion is immediate from (1) and (2). This proves the vector-stabilizer decomposition directly from the induced $K$-action, without invoking normality. Now let $g\in\Stab_{\widetilde O}(L)$. Either $gv=v$ and $g\in\Stab_{\widetilde O}(v)$, or $gv=-v$ and $-g\in\Stab_{\widetilde O}(v)$. Since $-\id_B$ is central, lies in $\widetilde O$ because $(-I)-I=-2I$, and is not in the vector stabilizer, the second stated direct product follows.
:::

::: {.theorem #thm:o2-stable-level-two-generation title="The complete integral level-two family for $\Orth(\latI_{1,8})$"}
In @lem:o2-ert-hr-transport, define the $240$ reflections
$$
\mathcal S\definedas\theset{r_{a+\zeta}:\zeta\in a^{\perp K},\ \zeta^2=-2},
\qquad m\definedas-r_a,
$$
and let $\Gamma_{K,\mathrm{time}}(2)\definedas\Gamma_K(2)\intersect O^+_{\mathrm{time}}(K)$. Then

1. $\Gamma_1\definedas\generators{\mathcal S}$ is the norm-one reflection subgroup in the HR convention, and $[\Gamma_{K,\mathrm{time}}(2):\Gamma_1]=2$;
2. $\Gamma_{K,\mathrm{time}}(2)=\generators{\Gamma_1,m}$ and
$$\Gamma_K(2)=\Gamma_{K,\mathrm{time}}(2)\times\generators{-\id_K},$$
so $\mathcal S\cup\theset{m,-\id_K}$ is a complete integral generating family for $\Gamma_K(2)$;
3. the old $35$-element family of @rmk:o2-stable-line-level-four does **not** generate $\Gamma_K(2)$.
:::

::: {.proof}

(1) In the HR model, [@HR14, Theorem 2.2]'s proof identifies $Q_0=v_8^{\perp}\intersect\bZ^{8,1}$ with the $E_8$ root lattice. For each $E_8$ root $\eta$, the vector $\eta+v_8$ has norm $1$ and is integral. There are $240$ such roots $\eta$; the long-simple-root Weyl group $\Sigma^8=W(E_8)$ is transitive on them, and $\varepsilon_8=(\varepsilon_8-v_8)+v_8$ is one of these vectors. Hence these $240$ vectors are exactly the $\Sigma^8$-conjugates of ERT's extra simple side and define the $240$ side reflections of $P^8$ in [@ERT10, Theorem 2.1]. Transporting by @lem:o2-ert-hr-transport turns them into $\mathcal S$. The cited HR Theorem 2.2 says that the norm-one reflection subgroup $\Gamma_1$ has index $2$ in the time-oriented principal congruence subgroup at $n=8$. This is an application at rank $9$ and time orientation, not a Witt-index or spinor-kernel statement.

(2) ERT's second displayed split sequence in Theorem 2.1 says that $\Gamma_2^8/\Gamma(P^8)$ is generated by the congruence-two member of $\Sigma^8$, namely its longest element. By @lem:o2-ert-hr-transport(2), that element is $m=-r_a$. It is integral and $m\equiv\id\pmod{2K}$, since $r_a$ has displacement $2(x,a)a$ and $-I\equiv I\pmod2$. Since $m\notin\Gamma_1$, it supplies the second coset. Finally, $-\id_K$ is congruent to the identity modulo $2K$ and interchanges the two time components; multiplication by it exactly as in @thm:o2-line-family gives the stated direct product and completes the full integral level-two family.

(3) Every reflection $r_{d_j},r_{e_2+d_j},r_{f_2+d_j}$ in the old list has primitive norm $-1$, so lies in $\Gamma_1$. Exact evaluation gives
$$
t_K(e_2,2d_j)=r_{e_2+d_j}r_{d_j},\qquad
t_K(f_2,2d_j)=r_{f_2+d_j}r_{d_j}.
$$
All $35$ elements therefore lie in $\Gamma_1$ (the transvections add no new reflection subgroup), whereas $m\notin\Gamma_1$ by (2). The old family cannot generate $\Gamma_K(2)$.

There is also a completely explicit counterexample. Put $w=e_2+f_2+d_1$, so $w^2=1$ and $r_w\in\Gamma_K(2)$. For a level-two isometry $g$, reduction of $(g-I)/2$ modulo $2$ gives an additive class. The $e_2$-coefficient of $(g(e_2)-e_2)/2$ is zero for all $35$ old generators, but $r_w(e_2)=e_2-2w$, so that coefficient for $r_w$ is $-1\equiv1\pmod2$. Hence the class of $r_w$ is not in the subgroup generated by their classes, and $r_w$ is not in the group generated by the $35$ elements. This verifies the failure by a one-coordinate certificate, independently of the dimension count. The bare $21/45$ comparison is still not assigned any generation conclusion.
:::

::: {.theorem #thm:o2-stable-line title="The structure and complete families of the four stable-group line stabilizers"}
Let $L$ be a primitive isotropic line of $T_\Co$, with $v$ a primitive generator and $K=L^{\perp T_\Co}/L\cong\latI_{1,8}$.

1. (Structure.) $\Stab_{\widetilde O}(v)=(\id_P\perp\Gamma_K(2))\ltimes\{E(v,2k):k\in K\}$ and $\Stab_{\widetilde O}(L)=\Stab_{\widetilde O}(v)\times\langle-\id_B\rangle$. Relative to the full vector parabolic, the substitutions are precisely $U_v=\{E(v,k):k\in K_{\mathrm{ev}}\}\mapsto\{E(v,2k):k\in K\}$ and $\Orth(K)\mapsto\Gamma_K(2)$; the line has the further central $C_2$.
2. (The unipotent factor is generated.) The transvection factor is generated by the nine $E(v,2k_i)$ for any $\bZ$-basis $k_1,\dots,k_9$ of $K$, by @lem:o2-level-two-membership(1).
3. (The character subgroups.) $\Stab_{\widetilde O\intersect SO}(L)$ and $\Stab_{\widetilde O\intersect\Orth^+}(L)$ have index exactly $2$ in $\Stab_{\widetilde O}(L)$, while $\Stab_{\widetilde O\intersect SO^+}(L)$, the joint kernel of $(\det,\spinornorm_\bR)$, has index exactly $4$. Indeed all four character pairs are realized inside the vector stabilizer: $\id_P\perp r_{d_1}$, $\id_P\perp(-\id_K)$ and their product have pairs $(-1,1)$, $(-1,-1)$ and $(1,-1)$, respectively, and the identity has $(1,1)$. These witnesses already fix $v$, so passing from $v$ to $L$ does not change the character image.
4. (The discriminant images are trivial, and that closes the image side of O2 at the stable level.) $\rho\bigl(\Stab_\Gamma(L)\bigr)=1$ for each of $\Gamma=\widetilde O$, $\widetilde O\intersect SO$, $\widetilde O\intersect\Orth^+$, $\widetilde O\intersect SO^+$; so for these four groups the stabilizer's discriminant image needs no generating family at all, and the count $527$ of @thm:o2-lines(3b) is exactly $\abs{\mathcal C}$ with the fibres of @lem:o2-line-classmap being single orbits.
5. (Complete integral families.) A complete family for $\Stab_{\widetilde O}(v)$ consists of $\id_P\perp\mathcal S$, $\id_P\perp m$, $\id_P\perp(-\id_K)$ and the nine transvections $E(v,2k_i)$ from (2); adjoining $-\id_B$ gives $\Stab_{\widetilde O}(L)$. The three character stabilizers have complete families obtained from this line family by @lem:o2-even-part, after adjoining the odd witness needed in each case to the displayed generating set: use $t:=r=\id_P\perp r_{d_1}$ for determinant, $t:=rh$ for spinor, and the transversal $\{1,r,h,rh\}$ for the joint quotient. No unresolved congruence generation remains in these four groups.
:::

::: {.proof}

(1), (2) are @lem:o2-level-two-membership(3) and (1).

(3) An element of $\Stab_{\widetilde O}(L)$ lies in $SO$ and $\Orth^+$ exactly when the corresponding characters are $+1$. The witnesses realize the full map $(\det,\spinornorm_\bR)$ onto $\{\pm1\}^2$: first, $\id_P\perp r_{d_1}$ with $r_{d_1}$ the reflection of $K$ in the vector $d_1$ of square $-1$: it is an integral isometry congruent to the identity modulo $2K$, and its characters are $(\det,\spinornorm_\bR)=(-1,+1)$ (@def:spinor-norm: a reflection in a negative vector has trivial normalized real spinor norm); $\id_P\perp(-\id_K)$ is congruent to the identity modulo $2K$ and has characters $(-1,-1)$ because $\det(-\id_K)=(-1)^9$ and $\spinornorm_\bR(-\id_K)=-1$ by @lem:minus-identity-spinor-norm with $K$ of positive index one; their product has $(+1,-1)$. All three lie in $\id_P\perp\Gamma_K(2)$ by @lem:o2-level-two-membership(2), hence already in $\Stab_{\widetilde O}(v)$. Surjectivity of $(\det,\spinornorm_\bR)$ gives indices $2$, $2$ and $4$ for its two coordinate kernels and its joint kernel, respectively.

(4) Every element of $\widetilde O$ is $\equiv\id\bmod2B$, hence acts trivially on $A=B/2B$; that is $\rho=1$ on all of $\widetilde O$, and the three other stable groups are subgroups of it.

(5) The Levi factor is generated by @thm:o2-stable-level-two-generation(2), the unipotent factor by (2), and the central line factor by $-\id_B$. Adjoin $r$ and $rh$ to the displayed finite family if necessary. Then @lem:o2-even-part applies to the determinant character with $t=r$, to the spinor character with $t=r h$, and, by its final sentence, to the joint character with the transversal $\{1,r,h,rh\}$. The character values in (3) prove that these are transversals.
:::

::: {.remark #rmk:o2-primitive-reflections title="Which primitive reflections have level two"}
For a **primitive** $w\in K$, unimodularity gives an $x$ with $(x,w)=1$. Integrality of $s_w(x)=x-2(x,w)w/w^2$ forces $w^2\mid2$, so primitive square $\pm1,\pm2$ are the only possibilities. If $w^2=\pm2$, then $s_w(x)-x=\pm(x,w)w\notin2K$ for $x$ with odd $(x,w)$, so $s_w\notin\Gamma_K(2)$; if $w^2=\pm1$, then $s_w(x)-x=\mp2(x,w)w\in2K$, so it does belong. This is stated only for primitive vectors: divisibility changes the reflection formula but not the underlying involution, and for example $s_{2d_1}=s_{d_1}$ although $(2d_1)^2=-4$.
:::

::: {.remark #rmk:o2-stable-line-level-four title="The finite datum: the level-four classes"}
Any complete family for $\Gamma_K(2)$ must have its classes in $\Gamma_K(2)/\Gamma_K(4)$ spanning the image of $\Gamma_K(2)$ there. That image lies in the space of $A\in\Mat_9(\bF_2)$ with $A^{t}\bar G+\bar GA=0$, $\bar G$ the reduction of the Gram matrix of $K$, of $\bF_2$-dimension $45$; and the $35$ elements $r_{d_j}$, $t_K(e,2d_j)$, $t_K(f,2d_j)$, $r_{e+d_j}$, $r_{f+d_j}$ ($1\le j\le7$) — all of them integral isometries congruent to the identity modulo $2K$, $21$ of them fixing the line $\bZ e$ — span $21$ dimensions there. The further element $r_{e+d_1+d_2}\,r_{e+d_1-d_2}$ of $\Gamma_K(2)$ has its class inside that $21$-dimensional span. So the level-four datum is a necessary condition only and proves no generation conclusion: neither the number $21/45$ nor the containment of the further element decides completeness. The complete family and the failure of the old $35$-element family are instead established by @thm:o2-stable-level-two-generation. The numerical check is retained only as the recorded necessary condition, not as evidence (`computations/reports/coble_833-stable-line-level2.py`, part 5).
:::

::: {.remark #rmk:o2-old-stable-family title="The status of the old $35$-element proposal"}
The question whether the $35$ elements generate $\Gamma_K(2)$ is answered **no** by @thm:o2-stable-level-two-generation(3): they lie in the norm-one reflection subgroup $\Gamma_1$, while $m$ lies outside it. This does not assert the separate, unused question whether those $35$ elements generate all of $\Gamma_1$. The displayed complete family in @thm:o2-stable-level-two-generation(2) is the one used here. No count of $\mathcal C$, $\mathcal D$, or cusps enters either assertion.
:::
