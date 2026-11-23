# Integral line and plane lifting for the Coble lattice {#sec-o2-lifting}

This section proves the general integral orbit theorem of research#667 for the lattice of Dolgachev--Kondo, for both primitive isotropic lines and primitive isotropic planes, under each of the four groups whose orbits the public operation of sage-extensions#286 builds; it constructs the complete integral generating families of the stabilizers that can be constructed, and it names the two that cannot be, with their exact statements, instead of substituting a count. It is the input of obligations O3 (research#834, the orbit fibres), O4 (research#835, the incidence) and O5 (research#836, the public operation and the cards) of that chain, and @sec-o2-consumers records which statement each of them consumes.

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
the last by @prop:gamma-co-images(3). The groups $\widetilde O$ and $\widetilde O^+$ do **not** have finite index in $O$, so no count for one of them is a count for another; and $R_\Gamma\neq\widetilde O$ and $R_\Gamma\neq\widetilde O^+$, because $[O:R_\Gamma]$ is finite while $[O:\widetilde O]$ and $[O:\widetilde O^+]$ are not.
:::

::: {.remark #rmk:o2-congruence title="How $R_\Gamma$ is identified with the congruence group, and how it is not"}
The group $\Gamma^{\mathrm{cong}}_{\Co,2}$ is defined by $\Gamma^{\mathrm{cong}}_{\Co,2}\definedas\rho_{T_\Co}^{-1}(P)$. The equality $R_\Gamma=\Gamma^{\mathrm{cong}}_{\Co,2}$ is therefore the conjunction of two already established propositions and not a definitional rewriting: @prop:gamma-co-images(3), which identifies $R_\Gamma$ with $\bar\rho^{-1}(P)$, and @prop:coble-cong-point-stabilizer(1), which identifies $\rho_{T_\Co}^{-1}\bigl(\Stab_{\Orth(q)}(A_{U(2)})\bigr)$ with $\rho_{T_\Co}^{-1}(P)$ and with $\Gamma^{\mathrm{cong}}_{\Co,2}$, the stabilizer of the decomposition being the setwise stabilizer of $A_{U(2)}$ because an isometry of quadratic forms of orders $4$ and $256$ carrying one summand onto the other does not exist. The arithmetic content of the identification — that the same group is the image of the Enriques stabilizer and the congruence condition of the degree-two datum — is @prop:gamma-cong-eq-heegner and @prop:direct-eq-heegner with @cor:four-groups-decided. Nothing in this section writes $\Gamma^{\mathrm{cong}}_{\Co,2}$ for any other lattice group, and nothing writes $\Gamma_\Co$ or $\Gamma_{\Co,2}$ for any of them: those are the monodromy groups of @def:gamma-co-groups(1) and (5), their identification with lattice groups is @conj:gamma-co-stable (@thm:gamma-co-is-stable(2)) and research#797 item 6, and the second is not even the intersection of $R_\Gamma$ with $\Orth^+$ (@prop:coble-monodromy-equality-false).
:::

::: {.remark #rmk:o2-group-list title="Why these four groups are exactly the groups of the public operation"}
The operation of sage-extensions#286 builds its subgroups from the Coble divisor and the three Enriques groups: it takes $O(T_\Co)$ itself, the discriminant kernel $\ker\rho=\widetilde O(T_\Co)$, its spinor-positive part $\widetilde O^+(T_\Co)$, and the images in $\Orth(\delta^{\perp})$ of $\Stab_\Gamma(\delta)$ for $\Gamma=\Gamma_\En=\widetilde\Orth^+(T_\En)$, for $\Gamma=\Gamma^K_\En=\Orth(T_\En)$ and for $\Gamma=\Gamma_{\En,2}$ (@def:gamma-co-groups). The first two restricted stabilizers are not new groups: by @prop:gamma-co-images(1), $R_{\Gamma_\En}=\widetilde\Orth^+(T_\Co)$ with no computation, and by @prop:gamma-co-images(2), $R_{\Gamma^K_\En}=\Orth(T_\Co)$ because every isometry of $q_{T_\Co}$ fixes the characteristic class $[h/2]$. The third is $R_\Gamma$ of @def:o2-groups. Hence the list of that operation is $O$, $\widetilde O$, $\widetilde O^+$, $R_\Gamma$ — four groups and no more — and a theorem stated for these four is a theorem for every group the operation builds. The two monodromy groups are not on that list and are not covered here (@conj:gamma-co-stable, @prop:coble-monodromy-equality-false).
:::

## The required statements, with their proof status {#sec-o2-ledger}

The orbit theorems of @sec-o2-lines and @sec-o2-planes are assembled from statements of three kinds: the lifting statements that carry a finite discriminant datum to integral objects, the stabilizer-image statements that compute the discriminant image of an integral stabilizer, and the completeness statements for integral generating families. Several of the first two were used inside @sec-cusp-lifting without being stated as theorems of their own, and the completeness statements were not separated from the finite-image computations that witness them. @tbl-o2-ledger lists all of them, with the status each has in this book after this section.

| | Statement | Status |
| --- | --- | --- |
| (L1) | $\ell\mapsto[\ell/2]$, well defined on primitive isotropic lines, $\Gamma$-equivariant for $\widetilde O^+\leq\Gamma\leq O$, image $\mathcal C$ | proved: @lem:o2-line-classmap |
| (L2) | the fibres of (L1) are single $\widetilde O^+$-orbits | proved: @lem:o2-line-classmap(3) |
| (L3) | hence $\Gamma$-orbits of lines $\leftrightarrow$ $\rho(\Gamma)$-orbits on $\mathcal C$, bijectively | proved: @thm:o2-lines(1) |
| (L4) | the decorated pair $(J(P),s(P))$ classifies primitive isotropic planes equivariantly, and is attained | proved: @thm:coble-integral-plane-lifting(1) |
| (L5) | the fibres of (L4) are single $\widetilde O^+$-orbits | proved: @thm:coble-integral-plane-lifting(2) |
| (L6) | the double-coset reduction through the normal subgroup $\widetilde O$ | [@SH23, Lemma 3.6]: a general group lemma, hypotheses verified in @thm:o2-lines(2) |
| (S1) | $\rho\bigl(\Stab_\Gamma(\ell)\bigr)=\rho(\Gamma)\intersect\Stab_{\Orth(q)}([\ell/2])$ for lines | proved: @lem:o2-line-stabilizer-image |
| (S2) | $\rho\bigl(\Stab_\Gamma(P)\bigr)=\rho(\Gamma)\intersect S_{(J(P),s(P))}$ for planes | proved: @lem:coble-plane-stabilizer-descends |
| (C1) | a complete integral family for $\Stab_O(P_0)$ | proved: @thm:o2-plane-family |
| (C2) | a complete integral family for $\Stab_{\widetilde O}(P_0)$ and $\Stab_{\widetilde O^+}(P_0)$ | proved: @thm:o2-plane-family-kernel |
| (C3) | a complete integral family for $\Stab_O(\ell)$ | **not proved**; by @lem:o2-line-reduction it is equivalent to (U1), which is therefore its exact statement |
| (C4) | a complete integral family for $\Stab_{R_\Gamma}(P)$ | **not proved**; its exact statement is (U2) of @qst:o2-congruence-family |
| (U1) | a finite family of integral isometries generating $\Orth(\latI_{1,8})$ | **open**, @qst:o2-line-family |
| (U2) | the congruence condition of $R_\Gamma$ inside the plane parabolic, generated | **open**, @qst:o2-congruence-family |

: The statements obligation O2 requires, and their status. {#tbl-o2-ledger}

Two entries of the table need saying explicitly, because they are what a count would hide. First, (C3) is not a formality: no step of the plane argument transfers to lines, because the plane parabolic has a two-dimensional Levi factor containing an integral $GL_2(\bZ)$, while the line parabolic's Levi factor is $\Orth(\latI_{1,8})$, an infinite group with trivial discriminant group (@lem:o2-line-reduction). Second, (U1) and (U2) are **not used** by any orbit theorem of this section: the orbit theorems use (L1)--(L6) and (S1)--(S2), and (S1), (S2) are proved structurally, by the parabolic decomposition of the stabilizer, not by enumerating a family. What is missing is the family-completeness clause that the acceptance of sage-extensions#286 attaches to the phrase "each $\rho(\Stab(x))$ computed from a family proved to generate $\Stab(x)$"; the *value* of each $\rho(\Stab(x))$ is a theorem here for all four groups and both object types.

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
the double-coset decomposition of the finite group $\Orth(q)$ by $(\rho(\Gamma),\rho(\Stab_{\Orth(T_\Co)}(\ell_0)))$, and this is the reduction of the integral double cosets $\Gamma\backslash\Orth(T_\Co)/\Stab_{\Orth(T_\Co)}(\ell_0)$ through the normal subgroup $\widetilde O$ of [@SH23, Lemma 3.6], whose hypotheses $U\subseteq K$ are $U=\widetilde O$ normal in $G=\Orth(T_\Co)$, $K=\Gamma\supseteq\widetilde O$, $H=\Stab_{\Orth(T_\Co)}(\ell_0)$.
3. (The four groups.) The number of orbits of primitive isotropic lines is
   a. $1$ for $\Gamma=O$;
   b. $527$ for $\Gamma=\widetilde O$ and for $\Gamma=\widetilde O^+$;
   c. $4$ for $\Gamma=R_\Gamma$, the orbits being those of $P$ on $\mathcal C$, of sizes $2$, $135$, $270$ and $120$.
4. (The character subgroups.) The same numbers hold with $O$ replaced by $SO=\ker\det$, $O^+=\Orth^+(T_\Co)$ or $SO^+=SO\intersect O^+$, and with $\widetilde O$ replaced by $\widetilde O\intersect SO$, $\widetilde O\intersect O^+$ or $\widetilde O\intersect SO^+$.
5. (What is not covered.) No clause is asserted for the monodromy group $\Gamma_\Co$ of @def:gamma-co-groups(1) or for $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5). For the labelled base only $\Gamma_\Co(B)\subseteq\widetilde O^+$ is proved (@thm:gamma-co-is-stable(1)), so $527$ is a *lower bound* for the number of $\Gamma_\Co(B)$-orbits and not the count.
:::

::: {.proof}

(1) The map of @lem:o2-line-classmap is $\Gamma$-equivariant and onto $\mathcal C$; it is constant on $\Gamma$-orbits, so it induces a surjection $\mathcal L_\Gamma\to\rho(\Gamma)\backslash\mathcal C$, and it is injective on orbits because the fibre over each class is a single $\widetilde O^+$-orbit (@lem:o2-line-classmap(3)) and $\widetilde O^+\iscontainedin\Gamma$.

(2) By (1), $\abs{\mathcal L_\Gamma}$ is the number of $\rho(\Gamma)$-orbits on $\mathcal C=\rho(\Orth(T_\Co))\cdot c_0$, which by orbit--stabilizer is the number of double cosets $\rho(\Gamma)\backslash\rho(\Orth(T_\Co))/\rho(\Stab_{\Orth(T_\Co)}(\ell_0))$, the stabilizer being computed by @lem:o2-line-stabilizer-image with $\Gamma=\Orth(T_\Co)$. For the cited lemma: the double-coset decomposition of $\Orth(T_\Co)$ by $(\Stab_{\Orth(T_\Co)}(\ell_0),\Gamma)$ has one element for each $\Gamma$-orbit in the $\Orth(T_\Co)$-orbit of $\ell_0$, which is all of $\mathcal L$; $\widetilde O$ is normal in $\Orth(T_\Co)$ and is contained in $\Gamma$, so the lemma applies verbatim and says the quotient map to $\Orth(T_\Co)/\widetilde O\iso\Orth(q)$ carries that decomposition to the decomposition of $\Orth(q)$ by the images, with the same index set.

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
4. (Why (3c) has two groups.) The seven is the number of $P$-orbits on $\mathcal D$ (@cor:coble-heegner-integral-plane-descent), and it is the count for $R_\Gamma$ as well as for $R_\Gamma\intersect\Orth^+$ because a fibre is a single $\widetilde O^+$-orbit and $\widetilde O^+\subseteq R_\Gamma\intersect\Orth^+$: both groups have the same orbits, although $R_\Gamma\supsetneq R_\Gamma\intersect\Orth^+$ and although $\Stab_{\Orth(T_\Co)}(P_0)$ is *not* contained in $R_\Gamma$, its discriminant image $S_3\times S_7$ being of order $247\,726\,080$ inside a group $P$ of order $696\,729\,600$ (@thm:coble-plane-stabilizer-image(3), @prop:gamma-co-images(3)).
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

The orbit theorems of @sec-o2-lines and @sec-o2-planes do not need a generating family: their stabilizer images are proved from the parabolic decomposition of the stabilizer and the surjectivity of $\rho$. What a family is needed for is the finer statement the acceptance of sage-extensions#286 attaches to it, "each $\rho(\Stab(x))$ computed from a family proved to generate $\Stab(x)$", and the corresponding statements of O5 (research#836). This section constructs those families where they can be constructed and names them where they cannot.

::: {.lemma #lem:o2-even-part title="The family of the kernel of a character"}
Let $G=\generators{F}$ with $F$ finite and let $\chi\colon G\too\generators{\pm1}$ be a surjective homomorphism. Then
$$\ker\chi=\bigl\langle\, \theset{f\in F : \chi(f)=1}\ \cup\ \theset{f f' : f,f'\in F,\ \chi(f)=\chi(f')=-1}\ \cup\ \theset{[f,f'] : f,f'\in F}\,\bigr\rangle .$$
:::

::: {.proof}

Let $H$ be the subgroup on the right. Every listed element lies in $\ker\chi$, so $H\subseteq\ker\chi$. The commutators $[f,f']$ of a generating set generate the derived subgroup $[G,G]$, which is normal, so $[G,G]\subseteq H$; hence $G/H$ is abelian. In $G/H$ every $f$ with $\chi(f)=1$ is trivial and any two $f,f'$ with $\chi(f)=\chi(f')=-1$ are equal, because $ff'\in H$ and an abelian group has $f=f'^{-1}=f'$. So $G/H$ is generated by the class of one odd element and has order at most $2$; since $\chi$ is onto it has $G/H\cong\bZ/2$ and $\ker\chi=H$.
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
In the notation of @thm:o2-plane-family, put $\Gamma(2)\definedas\ker\bigl(GL_2(\bZ)\to GL_2(\bF_2)\bigr)$ and let $D[\pm1]\cong(\bZ/2)^7$ be the sign changes of $D$. Then

1. $\Stab_{\widetilde O}(P_0)=\bigl(\Gamma(2)\times D[\pm1]\bigr)\ltimes U_{\mathrm{ev}}$, where $U_{\mathrm{ev}}=U\intersect\widetilde O$ is generated by the fourteen transvections $E_{e_i,2d_j}$ ($i=1,2$, $j=1,\dots,7$) together with the square $\sigma^2$ of the central shear;
2. $\Stab_{\widetilde O^+}(P_0)=\Stab_{\widetilde O}(P_0)\intersect\Orth^+(T_\Co)$ is generated by the family of (1) together with the element $\tau=-\id_{U_1}\oplus\id_{U_2\perp D}$, through @lem:o2-even-part with $\chi=\spinornorm_\bR$;
3. the discriminant images of both stabilizers are trivial.
:::

::: {.proof}

(1) An element of $L$ is $\gamma\oplus(\gamma^{-1})^T\oplus\delta$ with $\delta\in\Orth(D)$ a signed permutation. It is the identity modulo $2B$ exactly when $\gamma\equiv I_2\pmod 2$ and the underlying permutation of $\delta$ is trivial, signs acting by $\pm1\equiv1\pmod2$; that is $L\intersect\widetilde O=\Gamma(2)\times D[\pm1]$. An element $E_{e_i,w}$ is congruent to the identity modulo $2B$ exactly when $w\in2D$: $w$ is the $D$-component of $E_{e_i,w}(f_i)-f_i$, and $(d,w)$ is even for all $d\in D$ exactly when $w\in2D$, since $D$ is unimodular. The central shear $\sigma$ is not the identity modulo $2B$, so $\sigma\notin\widetilde O$. An element of $U$ is a product of the $E_{e_i,w}$ with the power $\sigma^c$, and it is the identity modulo $2B$ exactly when $w_1,w_2\in2D$ and $c$ is even: $\sigma$ acts by $f_1\mapsto f_1+e_2$, $f_2\mapsto f_2-e_1$, so $\sigma^2$ is the first even power and is the identity modulo $2B$, while $\sigma$ is not. Hence $U\intersect\widetilde O=\theset{E_{e_i,w}: w\in2D}\cdot\generators{\sigma^2}$, generated by the fourteen $E_{e_i,2d_j}$ by additivity and by $\sigma^2$, and $\Stab_{\widetilde O}(P_0)=\Stab_{\Orth(B)}(P_0)\intersect\widetilde O=(L\intersect\widetilde O)\ltimes(U\intersect\widetilde O)$ because $\widetilde O$ is normal and the decomposition is a semidirect product.

(2) $\tau$ fixes $P_0$ pointwise in the sense that it fixes $e_1,e_2,D$ and negates $f_1$; it is the identity modulo $2B$, so it lies in $\Stab_{\widetilde O}(P_0)$; and $\spinornorm_\bR(\tau)=\spinornorm_\bR(-\id_{U_1})=[-1]\neq1$ by @lem:split-isometry-spinor-norm and @lem:minus-identity-spinor-norm, $U_1$ having positive index one. So $\tau$ is an odd element of the stabilizer and @lem:o2-even-part applies.

(3) $\widetilde O=\ker\rho$ by definition, and $\widetilde O^+\subseteq\widetilde O$.
:::

::: {.lemma #lem:o2-line-reduction title="A line family is a family for $\Orth(\latI_{1,8})$"}
Let $v$ be primitive isotropic in $B=\latI_{2,9}$, split $B=P\perp K$ with $v\in P\cong\latI_{1,1}$ and $K\cong\latI_{1,8}$ (@lem:odd-unimodular-isotropic-splitting(1)), and put $U_v\definedas\ker\bigl(\Stab_{\Orth(B)}(v)\too\Orth(K)\bigr)$, so that $\Stab_{\Orth(B)}(v)=\Orth(K)\ltimes U_v$ with $U_v=\theset{E(v,k) : k\in K_{\mathrm{ev}}}$ (@lem:cusp-vector-stabilizer-image' proof).

1. For every generating set $F$ of $\Stab_{\Orth(B)}(v)$, the image of $F$ in $\Orth(K)=\Orth(v^{\perp B}/v)$ generates $\Orth(K)$.
2. Conversely, if $F_K$ generates $\Orth(K)$ and $\theset{k_1,\dots,k_8}$ is a $\bZ$-basis of $K_{\mathrm{ev}}$, then $F_K\cup\theset{E(v,k_i)}$ generates $\Stab_{\Orth(B)}(v)$.

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

::: {.question #qst:o2-line-family title="The missing line family: a generating set for $\Orth(\latI_{1,8})$"}
Does $\Orth(\latI_{1,8})$ admit an explicit finite family of integral isometries that generates it — in particular the family consisting of the integral transvections $t_K(e_2,d)$, $t_K(f_2,d)$ for $d$ in the $\bZ$-basis $d_1+d_7,\dots,d_6+d_7,2d_7$ of $D^{\mathrm{ev}}$, the six transpositions and seven sign changes of $D$, and the reflections $r_w$ of $K$ in the vectors $w$ with $w^2\in\theset{\pm1,\pm2}$?

*Status.* Open in this book. What is available is the semidirect decomposition $\Orth(K)=A(K)\cdot W(K)$ of [@Nik79b, §1.2°], where $W(K)$ is generated by the reflections of a fundamental chamber and $A(K)$ is the finite group preserving a chamber; that decomposition is stated there for negative definite even $K$, and the numbered theorems of that paper (Propositions 1.3.1 and 1.5.2 and their corollaries) are stated for even lattices and their $(-2)$-reflections, so none of them names the odd unimodular $K=\latI_{1,8}$. [@Nik79b, §0.1°] records that the description of hyperbolic unimodular lattices whose automorphism group is generated by reflections up to finite index is due to Vinberg's series, and states no numbered theorem of that description; a citation of it here would be a citation of a survey sentence, so it is not used. The reflection framework of this book (@thm:vinberg-algorithm, @cor:vinberg-terminates-reflective) is stated for even $2$-elementary lattices. Hence the statement above is the exact input obligation O2 does not close: at the level of the integral stabilizer of a primitive isotropic line, and nowhere else, the orbit theorem is proved and the family is not.
:::

::: {.question #qst:o2-congruence-family title="The missing congruence family: a generating set for $\Stab_{R_\Gamma}(P_0)$"}
Let $Q\definedas\rho\bigl(\Stab_{\Orth(T_\Co)}(P_0)\bigr)\intersect P$, a subgroup of $P\iso\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ whose order divides $\gcd(247\,726\,080,\,696\,729\,600)=15\,482\,880$, so that $Q$ has index at least $16$ in $\rho(\Stab_{\Orth(T_\Co)}(P_0))$. Is there an explicit finite family of integral isometries generating
$$\Stab_{R_\Gamma}(P_0)=\Stab_{\Orth(T_\Co)}(P_0)\intersect\rho^{-1}(P)?$$

*Status.* Open in this book, and it is a finite but non-trivial computation: $\Stab_{R_\Gamma}(P_0)$ contains $\Stab_{\widetilde O}(P_0)$ with finite index, and the quotient is the image of the family of @thm:o2-plane-family in the finite group $\rho(\Stab_{\Orth(T_\Co)}(P_0))/Q$; a family is obtained from a Schreier transversal of that quotient once the transversal's lifts are exhibited as integral isometries. Note that $\Stab_{\Orth(T_\Co)}(P_0)\not\subseteq R_\Gamma$ (@thm:o2-planes(4)), so the plane family of @thm:o2-plane-family is *not* a family of $\Stab_{R_\Gamma}(P_0)$: its generators lie outside the group. The orbit count of @thm:o2-planes(3c) does not use this statement.
:::

## What the later obligations consume {#sec-o2-consumers}

The chain of research#667 divides the question into five obligations; this section is O2, and @tbl-o2-consumers states, for each later obligation, which statement of this section it may cite and which statement it must still supply. A statement of this section is available to the others at the strength stated, and at no other strength.

| Obligation | Consumes from this section | Must supply itself |
| --- | --- | --- |
| O3, research#834 (orbit fibres over every discriminant class) | @lem:o2-line-classmap with @lem:o2-line-stabilizer-image for lines, @thm:coble-integral-plane-lifting with @lem:coble-plane-stabilizer-descends for planes: the fibre over a class is a single $\widetilde O^+$-orbit, and the stabilizer image is the finite stabilizer of the datum | nothing for the four groups: every fibre statement is a theorem here. For a group $\Gamma$ *not* containing $\widetilde O$, the double-coset formula of [@SH23, Lemma 3.6] is not available, and O3 must name the theorem it uses instead |
| O4, research#835 (complete integral line-plane incidence) | the plane classification by decorated pairs and the line classification by classes, hence the two vertex sets of the incidence graph, and @thm:coble-integral-flag-lifting for the flags | the condition ($\ast$) of @thm:coble-integral-incidence, that every permutation of $J\sm\generators{0}$ realized by $H$ is realized in the stabilizer of the decorated plane; @cor:coble-integral-incidence-rows(3) records it as unproved for $R_\Gamma$, and @prop:coble-incidence-not-automatic shows it is not a consequence of the containment $\widetilde O^+\iscontainedin\Gamma$ |
| O5, research#836 (public operation and certified cards) | the four counts of @thm:o2-lines(3) and @thm:o2-planes(3) as the values the operation must return, and @thm:o2-plane-family with @thm:o2-plane-family-kernel for the plane rows' "computed from a proved complete family" clause | the public operation itself, the card entries, and, for the line rows, the family of @qst:o2-line-family, which this section does not supply |

: What each later obligation of the chain consumes. {#tbl-o2-consumers}

Two of the entries deserve the emphasis they get there. First, the clause of sage-extensions#286's acceptance that asks for "a theorem the call uses instead" is *not* vacuous for O3: of the four groups, $O$, $\widetilde O$ and $R_\Gamma$ contain $\widetilde O$, so for them the double-coset formula of [@SH23, Lemma 3.6] applies, but $\Gamma=\widetilde O^+$ does not contain $\widetilde O$. For $\widetilde O^+$ the count is not a double-coset count at all: $\rho(\widetilde O^+)=1$, and @thm:o2-lines(1) and @thm:o2-planes(1) give the bijection with $\mathcal C$ and with $\mathcal D$ directly. That is the theorem used instead, and it is not the same argument. Second, the incidence of O4 is *not* determined by the two orbit sets: @prop:coble-incidence-not-automatic exhibits a subgroup containing $\widetilde O^+$ over which eight flag orbits fall onto four edges, so the edge count and the flag count can agree while the forgetful map is not injective.

## What is not covered, and the two exact open statements {#sec-o2-not-covered}

1. **The monodromy groups.** No statement of this section is a statement about $\Gamma_\Co$ of @def:gamma-co-groups(1) or about $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5). The identification of $\Gamma_\Co$ with a lattice group is @conj:gamma-co-stable and is not a theorem (@thm:gamma-co-is-stable(2)); on the labelled base only $\Gamma_\Co(B)\subseteq\widetilde O^+$ is proved, so @thm:o2-lines(3b) gives $527$ as a lower bound for $\Gamma_\Co(B)$ and nothing for $\Gamma_\Co$. For $\Gamma_{\Co,2}$ the containment $\Gamma_{\Co,2}\subseteq R_\Gamma\intersect\Orth^+(T_\Co)$ is @lem:d2-degree-two-base(3) and the reverse inclusion fails (@prop:coble-monodromy-equality-false), so no count of $R_\Gamma$ transfers.
2. **Eichler's criterion is not used.** No step of this section needs it, and none could: it requires a summand $U\oplus U$ in the lattice acted on, and $T_\Co$ has none. What replaces it is the parabolic decomposition of each stabilizer with the surjectivity of $\rho$ onto $\Orth(q_{T_\Co})$ ([@Nik80, Theorem 3.6.3], hypotheses verified in @prop:coble-discriminant-group) and the spinor-norm adjustment of @lem:o2-line-classmap(3).
3. **The published inputs, with their hypotheses on these objects.** [@DK13, (3.6)] is the lattice and [@DK13, Proposition 3.2] the period quotient, hypotheses checked in @sec-o2-groups. [@Nik80, Theorem 3.6.3] is the surjectivity of $\rho$ for an even, indefinite, $2$-elementary lattice, and $T_\Co$ is one, of signature $(2,9)$ and with $\abs{A_{T_\Co}}=2^{11}$. [@GHS08, §3.1, equations (4) and (5)] are the transvection formula and its additivity, used as formulas for the integral form of $B$ with the parity condition $k\in K_{\mathrm{ev}}$ that makes them integral. [@SH23, Lemma 3.6] is the reduction of a double-coset decomposition through a normal subgroup, a statement about groups with no lattice in it. [@Nik79b, §1.2°] and [@Nik79b, §0.1°] are cited only in @qst:o2-line-family, for what they do *not* give.
4. **The two statements this section does not close**, stated exactly so that no count stands in their place: (U1) of @qst:o2-line-family, a finite family generating $\Orth(\latI_{1,8})$, which by @lem:o2-line-reduction is equivalent to the completeness of the line-stabilizer family and cannot be decided by any finite discriminant computation (@lem:o2-line-kernel-infinite); and (U2) of @qst:o2-congruence-family, a finite family generating $\Stab_{R_\Gamma}(P_0)=\Stab_{\Orth(T_\Co)}(P_0)\intersect\rho^{-1}(P)$, a subgroup of finite index of the plane parabolic that does not contain it (@thm:o2-planes(4)). Everything else in @tbl-o2-ledger is proved, and no orbit theorem of this section uses either.
