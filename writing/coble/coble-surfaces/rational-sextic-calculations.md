# Rational Sextic Calculations

::: {.lemma #lem:rational_sextic_ten_nodes}

Let $C \subset \PP^2$ be an irreducible sextic curve with at worst $A_1$ singularities.
Then $C$ is a rational curve if and only if it has exactly ten $A_1$ singularities.
:::

::: {.proof}

Let $\nu\colon\widetilde C\to C$ be the normalization. For an integral plane curve of degree $d$, the plane genus formula gives $p_a(C)=(d-1)(d-2)/2$. The cokernel of $\OO_C\to\nu_*\OO_{\widetilde C}$ has length $\delta_p$ at each singular point $p$. Taking Euler characteristics gives
$$
g(\widetilde C)=p_a(C)-\sum_{p\in C^{\rm sing}}\delta_p.
$$
A node contributes one. Thus a sextic with $n$ nodes and no other singularities has arithmetic genus $10$ and normalization of genus $10-n$. Over $\CC$ the normalization is rational exactly when this genus is zero [@stacks-0CE0].
:::

::: {.example #ex:explicit-ten-nodal-sextic title="An explicit ten-nodal sextic and its K3 cover"}

Over $\CC$, consider the image of $\PP^1$ under the degree-six forms
$$
\begin{aligned}
f_0&=s^6+s^5t+2s^4t^2+3s^3t^3+2s^2t^4+st^5+t^6,\\
f_1&=2s^6+3s^5t+s^4t^2+2s^3t^3+3s^2t^4+st^5+2t^6,\\
f_2&=3s^6+2s^5t+3s^4t^2+s^3t^3+2s^2t^4+3st^5+t^6.
\end{aligned}
$$
Its reduced image $W$ is an irreducible rational sextic with exactly ten ordinary nodes. Its equation is $F=\sum_{i+j+k=6}a_{ijk}x^iy^jz^k$, where for $k=0,\ldots,6$ the following rows give $a_{6-k-j,j,k}$ in increasing order of $j$:
$$
\begin{array}{c|rrrrrrr}
k&\multicolumn{7}{c}{a_{6-k-j,j,k}}\\\hline
0&19783&-277523&1236290&-1155576&608968&-195808&26447\\
1&205052&-1702068&1686557&-1099558&366024&-45478\\
2&584140&-622975&609573&-130204&8334\\
3&3528&-73520&-118908&15408\\
4&-16747&89450&2144\\
5&-14520&-9276\\
6&2732
\end{array}
$$
The minimal resolution $X$ of the double plane $w^2=F(x,y,z)$ is a K3 surface. The pullbacks of a line and the ten exceptional curves on the blowup of the nodes span a primitive lattice in $\Pic(X)$ isometric to
$S_\Co\cong\generators{-2}\oplus E_{10}(2)$, whose orthogonal complement in $H^2(X,\bZ)$ is $T_\Co\cong\generators{2}\oplus E_{10}(2)$.

The parametrization and equation are recovered from the original lattice-research Task 1.1 example; the verification below is independent of the old singular-point transcript.

:::

::: {.proof}

First work over $\bZ_{(101)}$. The following exact computations, reproduced by [the arithmetic verification script](../scripts/certificates/rational_sextic_example.py), use only polynomial substitution, polynomial gcd, linear algebra and Gröbner bases.

1. Substitution gives $F(f_0,f_1,f_2)=0$ in $\bZ[s,t]$.
2. Over $\bF_{101}$, the gcd of $f_i(u,1)$ is $1$, and the forms do not vanish simultaneously at $[1:0]$. Thus the common-zero subscheme in the projective line has empty special fibre. By properness over $\bZ_{(101)}$, its generic fibre is empty as well: the closed image of a nonempty generic fibre would contain the closed point. The characteristic-zero forms are base-point free.
3. Over $\bF_{101}$ the $31\times21$ matrix whose columns are the coefficients of $f_0(u,1)^if_1(u,1)^jf_2(u,1)^l$, for $i+j+l=5$, has rank $21$. A nonzero maximal minor therefore also gives rank $21$ in characteristic zero. There is no nonzero homogeneous relation of degree five, hence none of smaller degree (multiply by a monomial to get degree five).
4. In each of the three affine coordinate charts of $\PP^2_{\bF_{101}}$, write $h(a,b)$ for the dehomogenization of $F$. In all three charts the ideal
$$
 (h,h_a,h_b,h_{aa}h_{bb}-h_{ab}^2)
$$
has reduced Gröbner basis $[1]$. Thus the special fibre has no singular point with degenerate quadratic part.

The image in characteristic zero is integral, since it is the reduced image of the integral projective line. The parametrization is nonconstant by the absence of degree-one relations. Let $d$ be its degree onto its image and let $e$ be the degree of that image. A general line pulls back to a divisor of degree six because the forms have degree six and no common zero. Hence $de=6$. By (3), $e\geq6$, so $e=6$ and $d=1$. The image is consequently rational, and the nonzero degree-six relation in (1) is its defining equation up to scalar.

For nodality, the bad singular-point scheme is closed in $\PP^2_{\bZ_{(101)}}$: it is given by $F$, its first partials and all the $2\times2$ minors of its homogeneous Hessian. At a singular point with representative $p$, the Hessian annihilates $p$ by the differentiated homogeneous Euler identity. On a chart with one coordinate of $p$ normalized to $1$, the two other coordinate directions and $p$ form a basis, and the Hessian has the chart Hessian as its upper $2\times2$ block and a zero last row and column. Thus the rank-at-most-one condition is precisely the vanishing in (4). The bad scheme has empty special fibre by (4), so its generic fibre is empty by properness. Since the characteristic is zero, a singular plane-curve point with nondegenerate quadratic part is an ordinary node. Now @lem:rational_sextic_ten_nodes gives exactly ten nodes.

Let $S$ be the blowup at these nodes and $B$ the strict transform of $W$. The local ordinary-node calculation shows that $B$ is smooth, and the blowup formula gives $B\sim-2K_S$ and $B^2=-4$ by @prop:coble-canonical-class and @prop:antibicanonical-curve. If another effective divisor is linearly equivalent to $B$, its intersection with $B$ is $-4$, so it must contain $B$; the effective difference is linearly equivalent to zero and hence zero on the projective surface. Thus $\abs{-2K_S}=\{B\}$ and $\abs{-K_S}=\varnothing$ (otherwise twice an effective anticanonical divisor would equal the reduced irreducible $B$). This is the terminal Coble surface with a single branch component.

The double cover $f:X\to S$ branched along $B$ is smooth and is a K3 surface by @prop:double-cover-is-k3. It resolves the double plane: the pullback of $W$ to $S$ is $B+2\sum_i E_i$, so normalization of the pulled-back double plane is the double cover branched along $B$, defined by the line bundle $\OO_S(3H-\sum_i E_i)=\OO_S(-K_S)$. This gives a proper birational morphism to the double plane that is an isomorphism off the ten nodes. Smoothness of $X$ gives a resolution, and adjunction with $K_X=0$ excludes exceptional $(-1)$-curves, so the resolution is minimal.

Finally @prop:coble-invariant-lattice applies to this particular one-component cover, identifying the lattice generated by $f^*H,f^*E_1,\ldots,f^*E_{10}$ with the primitive invariant lattice $S_\Co$, with Gram matrix $\operatorname{diag}(2,-2,\ldots,-2)$. The complement in the unimodular K3 lattice is the anti-invariant lattice of signature $(2,9)$, with discriminant form the negative of that of $S_\Co$. Its invariants are therefore $(11,11,1)_2$, which identify it with $\generators{2}\oplus E_{10}(2)$ by [@Nik80, Thm. 3.6.2], as in @prop:coble-period-domain. This is a construction on an actual explicitly specified double plane, not just an abstract pair of glued lattices.

:::

::: {.example #ex:two-more-explicit-ten-nodal-sextics title="Two further explicit ten-nodal sextics"}

The two other parametrizations recovered from the same computation history have the following coefficient rows in the ordered monomials $(s^6,s^5t,\ldots,t^6)$:
$$
\begin{pmatrix}
1&2&-1&3&1&-2&1\\
2&-1&3&2&-1&3&2\\
3&1&2&-1&3&1&1
\end{pmatrix},
\qquad
\begin{pmatrix}
1&3&2&-1&1&2&1\\
2&1&3&2&-1&1&3\\
1&-1&1&3&2&-1&2
\end{pmatrix}.
$$
Each image is an irreducible rational plane sextic with ten ordinary nodes, and hence each supplies a Coble surface and K3 cover with the lattices of @ex:explicit-ten-nodal-sextic.

:::

::: {.proof}
The equation for each was recovered independently by finding the one-dimensional kernel of degree-six substitution over $\bQ$ and clearing denominators; both exact equations are recorded in [the arithmetic script](../scripts/certificates/rational_sextic_example.py). For each, direct substitution gives zero over $\bZ$; at the same prime $101$ the base-point gcd is $1$, at least one leading coefficient is nonzero, the degree-five substitution matrix has rank $21$, and the bad singularity ideals have Gröbner basis $[1]$ in all three affine charts. The proof of @ex:explicit-ten-nodal-sextic applies without change. This verifies all three original parametrizations, but does not assert that their moduli points are pairwise distinct.
:::


::: {.example #ex:thas-desargues-sextic title="A ten-nodal sextic with a Desargues configuration"}

Specialize Charles Thas's parametrization in [*A rational sextic associated with a Desargues configuration*, Geom. Dedicata **51** (1994), 163–180, §3, pp. 167–170](https://doi.org/10.1007/BF01265327) to $(a,b,c)=(2,2,3)$. Homogenize the three affine polynomials
$$
\begin{aligned}
X(t)&=6t^6+8t^4-10t^2-4,\\
Y(t)&=-16t^5+116t^4-40t^3-8t,\\
Z(t)&=12t^5+32t^3-116t^2+20t
\end{aligned}
$$
to common degree six. Their reduced plane image is an irreducible rational sextic with ten rational nodes, indexed by $0,\ldots,9$:
$$
\begin{array}{c|rrr@{\qquad}c|rrr}
0&1&0&0&5&-1&-8&4\\
1&2&1&1&6&2&-4&12\\
2&14&4&-2&7&0&1&-1\\
3&14&-1&3&8&0&2&1\\
4&2&28&28&9&0&1&3
\end{array}
$$
Its implicit equation has coefficient rows in the monomials $x^{6-j-h}y^jz^h$ for $h=0,\ldots,6$, $j=0,\ldots,6-h$:
$$
\begin{array}{c|rrrrrrr}
0&0&0&240&-696&96&0&9\\
1&0&416&-928&8&348&-24\\
2&128&-1160&3268&-464&-14\\
3&-464&136&-580&52\\
4&80&232&9\\
5&0&-20\\
6&4
\end{array}
$$
The configuration lines are indexed by
$$
\mathcal T=\{014,025,036,129,138,237,459,468,567,789\},
$$
where $014$ denotes the line through points $0,1,4$.

Let $S$ be the blowup of these points and $B$ the strict transform of the sextic. Then $S$ is a Coble surface. The strict transforms of the ten configuration lines are smooth rational $(-2)$-curves disjoint from $B$, whose classes generate a sublattice of index $16$ in $K_S^\perp$.

:::

::: {.proof}

The [exact arithmetic script](../scripts/certificates/desargues_sextic.py) verifies that the parametrization is base-point free: the three affine polynomials have gcd one and the leading coefficient of $X$ is nonzero. Substitution into the displayed sextic gives zero, and the degree-five substitution matrix has rank $21$. Thus there is no relation of degree five or lower. As in @ex:explicit-ten-nodal-sextic, the image degree times the generic mapping degree is six, forcing the image degree to be six and the map to be birational.

The script verifies pairwise projective distinctness of the ten points, vanishing of the equation and all first derivatives, and homogeneous Hessian rank two at every point. The Hessian argument of @ex:explicit-ten-nodal-sextic identifies each as an ordinary node; the genus formula excludes any further singularities. Checking all $\binom{10}{3}=120$ determinants gives exactly the ten triples displayed above. No four points are collinear, and every point belongs to three lines.

The configuration conic $x^2-yz=0$ satisfies
$$
X(t)^2-Y(t)Z(t)=4(3t^6+12t^4-58t^3+15t^2+2)^2.
$$
None of the ten nodes lies on this conic.

Write $H$ for the pullback of a line and $E_i$ for the exceptional divisors. The argument of @ex:explicit-ten-nodal-sextic gives the Coble surface and its K3 cover. The strict transform of the line indexed by $I$ has class $C_I=H-\sum_{i\in I}E_i$. By @prop:blowup-geometric-basis, $C_I^2=-2$, $K_S\cdot C_I=0$ and $B\cdot C_I=0$. The latter vanishing gives disjointness since the effective curves have no common component. The Gram matrix in the displayed order is $G_{IJ}=1-|I\cap J|$. Its determinant is $-256$, with characteristic polynomial $(\lambda-1)(\lambda+1)^5(\lambda+4)^4$. These ten classes therefore span a rank-ten sublattice of $K_S^\perp$. Since $K_S^2=-1$ and the blowup lattice is unimodular, it splits integrally as $\bZ K_S\perp K_S^\perp$ and $K_S^\perp$ is unimodular. The sublattice index is $\sqrt{256}=16$. This calculation does not assert that the curves exhaust the effective roots.

:::

The different affine coordinate degrees of Thas's parametrization and the three examples in @ex:explicit-ten-nodal-sextic and @ex:two-more-explicit-ten-nodal-sextics do not prove projective inequivalence. Such a comparison requires a projective invariant, for instance the incidence of the nodes.

::: {.proposition #prop:rational-sextic-severi title="The Severi variety of rational sextics"}

1. Let $S_{6,0}\iscontainedin\PP^{27}$ be the Severi variety of rational plane sextics. It is irreducible of dimension $17$ and degree (@def:graded-object) (@def:numerical-polarization) $26312976$. Its general member has exactly $10$ nodes, and the set of these $10$ nodes determines the curve [@BHO+12, §4, proof of Thm. 2].
2. There is a rational cuspidal plane sextic over $\CC$ whose only singular point is a cusp with multiplicity sequence $[5]$ [@GK20, Thm. 1.1, Thm. 3.1]. It does not have ten $A_1$ singularities.

:::

::: {.question #qst:sextic-moduli-maps title="Can one recover a nodal plane sextic from its abstract curve or its pointed normalization?"}

Fix an irreducible plane sextic with $n$ ordinary nodes and no other singularities, and put $g=10-n$. Forgetting the plane gives a stable curve in $\overline{\mathcal M}_{10}$. Normalizing gives a smooth curve of genus $g$ with $n$ unordered pairs of distinct branch points. On the equinodal locus, label the nodes and order their branches étale locally. Changing these choices gives the action of $G_n=(\mathfrak S_2)^n\rtimes\mathfrak S_n$ on the markings. The two constructions fit into
$$
[\text{equinodal sextics}/\mathrm{PGL}_3]\longrightarrow
[\mathcal M_{g,2n}/G_n]\xrightarrow{\ \mathrm{glue\ the\ pairs}\ }
\overline{\mathcal M}_{10}.
$$
Gluing recovers the original abstract nodal curve. What are the fibres of these maps from the plane-curve stack? For a given pointed normalization, which base-point-free plane linear series of degree six identify just the prescribed pairs and give ordinary nodes? On which locus, if any, can the plane series be recovered up to projectivity from the abstract curve? This recovery is the issue in asking for an embedding into curve moduli.
:::

::: {.proposition #prop:sextic-plane-recovery title="Recovery of the plane of a nodal sextic from its canonical curve"}

Over $\CC$, every isomorphism of abstract integral plane sextics extends uniquely to an isomorphism of their ambient projective planes. More generally, for families of integral nodal plane sextics (allowing the ambient planes to be forms of $\PP^2$ over the base), the forgetful morphism from the plane-sextic quotient stack to $\overline{\mathcal M}_{10}$ is a monomorphism. In particular the same holds on each equinodal substack. The geometric fibre over an abstract curve or a paired pointed normalization in @qst:sextic-moduli-maps is empty or consists of a single plane model with no relative automorphisms.

:::

::: {.proof}

For a plane sextic $C=V(F)$, adjunction for the Cartier divisor gives $\omega_C=\OO_C(3)$: this follows by applying the dualizing-sheaf Ext construction to $0\to\OO_{\PP^2}(-6)\to\OO_{\PP^2}\to\OO_C\to0$ with $\omega_{\PP^2}=\OO_{\PP^2}(-3)$. The argument applies also at nodes. Restriction identifies $H^0(\PP^2,\OO(3))$ with $H^0(C,\omega_C)$ since $H^0(\OO(-3))=H^1(\OO(-3))=0$. Thus the complete canonical embedding of $C$ in $\PP^9$ is its inclusion in the cubic Veronese surface $V=v_3(\PP^2)$.

Write $A=\operatorname{Sym} H^0(C,\omega_C)$ for the polynomial coordinate ring of that canonical ambient space, and $I_C,I_V\subset A$ for the homogeneous ideals. The quadratic restriction $A_2\to H^0(\PP^2,\OO(6))$ is surjective by factoring monomials. Hence
$
(I_C)_2=(I_V)_2\oplus\CC Q,
$
where $Q$ is any quadratic lift of the sextic equation $F$. Consider the intrinsic vector space of linear syzygies
$
K_C=\ker\bigl(A_1\otimes (I_C)_2\longrightarrow A_3\bigr).
$
Reducing any such syzygy modulo $I_V$ gives $L F=0$ in the polynomial ring on the plane, with $L$ a cubic. Since $F\ne0$, $L=0$; the restriction on linear forms is an isomorphism. Therefore $K_C=K_V$ inside $A_1\otimes(I_C)_2$.

Let $W_C$ be the image of $A_1^\vee\otimes K_C\to(I_C)_2$ by contraction. Then $W_C=(I_V)_2$. Indeed the cubic Veronese of the smooth projective plane in characteristic zero satisfies property $N_2$ by Ottaviani--Paoletti, [*Syzygies of Veronese embeddings*, Compos. Math. **125** (2001), Theorem 3.1 and Proposition 3.2, p. 36; Definition 1.3, p. 33](https://doi.org/10.1023/A:1002662809474) (take $d=3$, $p=2$). This says exactly that its homogeneous ideal is generated by quadrics and the module of relations among these quadrics is generated by linear syzygies. If their coefficient span were proper, choose a basis of $(I_V)_2$ extending a basis of that span and let $q$ be an omitted basis element. All relations generated by the linear ones would then have zero $q$-coordinate. For any other basis element $q'$, the Koszul relation $q'e_q-qe_{q'}$ has nonzero $q$-coordinate, a contradiction. (There are $55-28=27$ independent quadrics.) Thus the ideal generated by $W_C$ is precisely $I_V$.

It follows that the canonical curve determines its surrounding Veronese surface scheme-theoretically. An isomorphism of curves induces an isomorphism of their canonical ambient spaces carrying this intrinsic ideal to itself and hence carrying their Veronese surfaces to one another. Inverting the Veronese embeddings gives the desired plane isomorphism. It is unique: a plane isomorphism restricting to the identity on $C$ induces the identity on the canonical projective space, because the restriction of cubics is an isomorphism (the scalar in the adjunction identification is projectively immaterial).

For the family assertion this same construction works fppf locally on any base $T$ over $\CC$, including nonreduced bases. Trivialize the ambient plane and the base line of the sextic equation, and work over an affine base ring $R$. Relative adjunction and the same cohomology of twists on the relative projective plane give the canonical space and relative cubic Veronese as above; the equation is $F\in R[x_0,x_1,x_2]_6$ nonzero on every residue-field fibre. The quadratic multiplication onto $R[x_0,x_1,x_2]_6$ is split surjective; the equations of the canonical curve in degree two are the inverse image of $RF$, so the decomposition with a lift $Q$ still holds. Multiplication by $F$ from $R[x_0,x_1,x_2]_3$ to $R[x_0,x_1,x_2]_9$ is injective: at every residue field it has full column rank, and locally a maximal minor is a unit. The syzygy argument therefore identifies $K_C$ with the linear syzygies of the relative Veronese, which are obtained by scalar extension from $\CC$ (the defining linear maps are between finite-dimensional $\CC$-vector spaces). Contraction likewise recovers the base extension of the Veronese quadratic ideal, with no reducedness assumption on $R$. These intrinsic constructions commute with the local identifications of the canonical spaces. Any isomorphism of abstract families consequently extends uniquely fppf locally to the plane families and the extensions agree on overlaps by uniqueness, hence descend. This proves full faithfulness on every base and thus a monomorphism of stacks [Stacks Project, Lemma 100.8.4, Tag 04ZZ](https://stacks.math.columbia.edu/tag/04ZZ).

Finally a paired smooth normalization determines the abstract nodal curve by gluing the marked pairs, so the geometric fibre over it also has the asserted uniqueness, including for the degree-six series on a rational normalization. Existence in either fibre is equivalent to admitting the specified plane model; for a geometric pointed curve the recovered plane's line bundle of lines pulls back along its normalization to the unique plane series up to change of plane coordinates.

:::

::: {.proposition #prop:sextic-plane-locus-immersion title="The integral nodal plane-sextic locus is locally closed in stable curve moduli"}

Over $\CC$, the morphism in @prop:sextic-plane-recovery from the stack of integral plane sextics with at worst nodes (including smooth sextics) to $\overline{\mathcal M}_{10}$ is a locally closed immersion. Its image has a scheme-theoretic description by canonical multiplication maps and the orbit of the cubic Veronese quadratic ideal.

:::

::: {.proof}

Work on the open substack of $\overline{\mathcal M}_{10}$ where the geometric fibres are integral and the dualizing sheaf is very ample. For the universal curve $\pi$, write $E=\pi_*\omega_\pi$ and $A_j=\operatorname{Sym}^j E$. Relative duality and cohomology and base change give vector bundles $E$ and $\pi_*\omega_\pi^j$ compatible with base change, of ranks $10$ and $9(2j-1)$ for $j\geq2$ (on a geometric fibre, $H^1(\omega^j)=H^0(\omega^{1-j})^\vee=0$ and Riemann--Roch applies). On the open locus where $A_2\to\pi_*\omega_\pi^2$ is surjective, let $I_2$ denote its rank-$28$ kernel. Take the scheme-theoretic rank-$175$ stratum of
$
E\otimes I_2\longrightarrow A_3.
$
On it the kernel $K$ is a vector bundle of rank $280-175=105$. Take in turn the scheme-theoretic rank-$27$ stratum of the contraction $E^\vee\otimes K\to I_2$. On this stratum its image $W$ is a rank-$27$ subbundle of $A_2$. Here exact rank $r$ means the closed condition of vanishing $(r+1)$-minors intersected with the open locus where the $r$-minors generate the unit ideal; it implies local split image and kernel, not just constant rank on geometric points.

Trivialize $E$ locally. Then $W$ defines a map to $\operatorname{Gr}(27,\operatorname{Sym}^2\CC^{10})$. Require this map to factor through the reduced $\operatorname{GL}_{10}$-orbit $\mathcal O$ of the quadratic ideal space of the cubic Veronese surface. This is a locally closed condition: the orbit is locally closed and its orbit map from $\operatorname{GL}_{10}$ is faithfully flat and of finite presentation by [Milne, *Algebraic Groups* (2017), Propositions 1.65 and 7.4, §7c](https://www.jmilne.org/math/Books/iAG2017.pdf). In particular the condition descends under changes of frame and is imposed as a subscheme, not merely on geometric points. The successive open and locally closed conditions thus define a locally closed substack.

Every integral nodal plane sextic family factors through it. Indeed in the notation of @prop:sextic-plane-recovery, the canonical ring in degrees two and three is obtained by taking plane polynomials of degrees six and nine modulo the multiples of $F$. Both multiplication maps onto $\pi_*\omega_\pi^j$, $j=2,3$, are surjective by monomial factorization and restriction. Their kernels have ranks $55-27=28$ and $220-45=175$. Moreover the whole canonical ideal is generated by the Veronese quadrics and the lift $Q$ of $F$: in degree $j$ the additional equations modulo the Veronese ideal are exactly $F$ times plane forms of degree $3j-6$, and those forms are images of $A_{j-2}$. Consequently $E\otimes I_2$ surjects onto the degree-three ideal bundle. This verifies the first rank condition as a bundle map, also over nonreduced bases. The contraction has split image equal to the base extension of the Veronese quadratic ideal by @prop:sextic-plane-recovery, so the second rank condition and the orbit condition hold scheme-theoretically as well.

Conversely, for any family in the specified locally closed substack, the faithfully flat orbit map permits an fppf-local change of frame carrying $W$ to the constant Veronese quadratic ideal space. Its common zero scheme $V$ in the canonical projective bundle is therefore fppf locally the cubic Veronese plane, and $C\subset V$ scheme-theoretically since $W\subset I_2$. On every geometric fibre the integral curve in this plane has degree six: its degree in the canonical embedding is $2\cdot10-2=18$, and the Veronese hyperplane bundle is the cube of the plane line bundle. The fibre inclusion is an effective Cartier divisor in the smooth plane. Since the curve and plane families are flat and locally of finite presentation over the base, the inclusion is a relative effective Cartier divisor by [Stacks Project, Lemma 31.19.9, Tag 062Y](https://stacks.math.columbia.edu/tag/062Y). Hence this is a family of degree-six plane divisors, with integral nodal geometric fibres, giving the required plane presentation locally. The intrinsic zero scheme of $W$ supplies the ambient plane form globally; the curve and the extensions of its isomorphisms descend by @prop:sextic-plane-recovery. The two constructions are inverse on arbitrary base schemes, proving the locally closed immersion.

:::

For comparison, [Landesman, *The locus of plane curves in the moduli stack of curves*, arXiv:2509.25432 (2025), Theorems 1.1 and 4.3](https://arxiv.org/html/2509.25432v1) proves the locally closed embedding for smooth plane curves of every degree at least four. His smoothness hypothesis does not directly cover integral nodal sextics; the preceding argument gives the nodal degree-six statement using the canonical syzygies rather than a uniqueness theorem for linear series on smooth curves. The nodal image is smooth of dimension $19$, since the integral at-worst-nodal locus is open in the projective space $\PP^{27}$ of sextic equations and the smooth group $\mathrm{PGL}_3$ has dimension eight. For a fixed number of nodes one can restrict to the corresponding scheme-theoretic equisingular stratum; over nonreduced bases the number of geometric nodes alone is not a simultaneous-normalization condition (the local family $xy=\epsilon$ over $\CC[\epsilon]/(\epsilon^2)$ has a nodal geometric fibre but a nonzero smoothing parameter).

The proposition concerns the moduli of **plane presentations**. It does not identify distinct blowdown presentations of an abstract Coble surface, or assert that the plane-sextic locus is closed in the stable-curve stack. It gives a canonical recovery procedure on the entire integral nodal sextic locus, not merely a generic injectivity statement.

::: {.proposition #prop:coble-canonical-class title="Canonical class of the blowup of the ten nodes"}

Let $W\subset \PP^2$ be an irreducible sextic whose singular points are exactly ten $A_1$ singularities $p_1, \ldots, p_{10}$.
Let $\pi\colon S\to\PP^2$ be the blowup of $p_1, \ldots, p_{10}$, with geometric basis (@def:based-module) $e_0, \ldots, e_{10}$ as in @prop:blowup-geometric-basis, and let $C$ be the proper transform (@def:strict-transform) of $W$.
Then
$$
K_S = -3e_0 + \Sum_{k=1}^{10} e_k,
\qquad
K_S^2 = -1,
\qquad
C \sim 6e_0 - 2\Sum_{k=1}^{10} e_k = -2K_S
.
$$
The surface $S$ is a Coble surface (@def:coble-surface) [@DK13, §3].
Coble studied the sets of ten nodes of rational sextics in [@Cob19].

:::

::: {.proof}

The formula for $K_S$ is @prop:blowup-geometric-basis (2).
By @prop:blowup-geometric-basis (1),
$$
K_S^2 = 9e_0^2 + \Sum_{k=1}^{10} e_k^2 = 9 - 10 = -1
.
$$
An $A_1$ singularity of a plane curve is a double point, so $W$ has multiplicity $2$ at each $p_k$.
The points $p_k$ are distinct points of $\PP^2$, so each blowup is an isomorphism (@def:isomorphism-of-objects) near the other points, and the proper transform of $W$ still has multiplicity $2$ at each point blown up later.
By [@Har77, V.3.6], the pullback (@def:pullback-square) of a curve under the blowup of a point of multiplicity $r$ on it is its proper transform plus $r$ times the exceptional curve.
Applied ten times, with $W\sim 6h$ for the class $h$ of a line [@Har77, II.6.4], this gives $6e_0 = C + 2\Sum_{k=1}^{10} e_k$ in $\Pic(S)$, so $C \sim 6e_0 - 2\Sum_k e_k = -2K_S$.

:::

::: {.proposition #prop:antibicanonical-curve title="Invariants of an antibicanonical curve"}

Let $S$ be a Coble surface (@def:coble-surface) of K3 type with $K_S^2 = -1$, and let $C\in\abs{-2K_S}$ be an integral curve.
Then $C$ is a smooth rational curve and $C^2 = -4$.

:::

::: {.proof}

By [@Har77, V Ex. 1.3(a)], $2p_a(C) - 2 = C\cdot(C + K_S)$.
With $C \sim -2K_S$ this gives
$$
p_{a}(C)=1+\frac{1}{2}\qty{ C^{2}+C \cdot K_{S} } = 1 + \frac12\qty{4K_S^2 - 2K_S^2} = 1+K_{S}^{2}=0
.
$$
An integral projective curve with $p_a = 0$ is nonsingular and isomorphic to $\PP^1$ [@Har77, IV Ex. 1.8(b)].
Finally $C^2 = 4K_S^2 = -4$.

:::

## The configuration constraint on the ten nodes

::: {.proposition #prop:sextic-node-conditions title="Ten nodes impose more conditions than the linear system has"}

The space of plane sextics is
$$
\dim_\CC H^0\bigl(\PP^2, \OO_{\PP^2}(6)\bigr) = \binom{8}{2} = 28
,
$$
so sextic curves form a $\PP^{27}$.
Requiring a singular point at a prescribed $p\in\PP^2$ imposes at most three linear conditions on this space.
A sextic singular at all of $p_1, \ldots, p_{10}$ exists if and only if the resulting thirty conditions have rank at most $27$.
There is a nonempty Zariski-open subset $\mathcal U\iscontainedin(\PP^2)^{10}$ such that for $(p_1, \ldots, p_{10})\in\mathcal U$ the thirty conditions have rank $28$, and no sextic is singular at all ten points.
:::

::: {.proof}

The monomials $x^iy^jz^k$ with $i+j+k=6$ number $\binom{6+2}{2} = 28$, giving the stated dimension.
For a fixed $p$, singularity of $\theset{F = 0}$ at $p$ is the vanishing of the three partial derivatives $\del_x F(p)$, $\del_y F(p)$, $\del_z F(p)$; each is a linear condition on the coefficients of $F$, and $F(p) = 0$ follows from Euler's identity $\Sum_i x_i\,\del_i F = 6F$.
Choose representatives $\tilde p_i\in\CC^3\setminus\theset{0}$ of the points $p_i$.
The thirty conditions form the linear map $M(\tilde p_1, \ldots, \tilde p_{10})\colon H^0\bigl(\PP^2, \OO_{\PP^2}(6)\bigr)\cong\CC^{28}\to\CC^{30}$ that sends $F$ to the values of $\del_x F$, $\del_y F$, $\del_z F$ at the $\tilde p_i$.
A sextic singular at all ten points is a nonzero vector of its kernel (@def:kernel-cokernel), and the kernel is nonzero if and only if the rank is at most $27$.

The partial derivatives are homogeneous of degree (@def:graded-object) (@def:numerical-polarization) $5$, so replacing $\tilde p_i$ by $\lambda\tilde p_i$ multiplies three rows by $\lambda^5$ and does not change the rank.
The locus where the rank is $28$ is the complement of the common zero set of the $28\times 28$ minors, which are polynomials in the coordinates of the $\tilde p_i$; it therefore descends to a Zariski-open subset $\mathcal U\iscontainedin(\PP^2)^{10}$.
The subset $\mathcal U$ is nonempty by @ex:sextic-node-conditions-rank.
:::

::: {.example #ex:sextic-node-conditions-rank title="Ten points at which the node conditions have full rank"}

For the ten points
$$
(1:0:0),\ (0:1:0),\ (0:0:1),\ (1:1:1),\ (1:2:3),\ (1:-1:2),\ (2:1:-1),\ (1:3:-2),\ (3:-2:1),\ (1:4:5)
$$
the $30\times 28$ matrix over $\QQ$ of the map $M$ of @prop:sextic-node-conditions, in the monomial basis $x^iy^jz^{6-i-j}$, has rank $28$.
This is a computation in SageMath with exact rational arithmetic.
:::

::: {.proposition #prop:sextic-equisingular-dimension title="Dimension of the space of sextics of a fixed singular type"}

Let $Z$ be a reduced plane sextic with only simple singularities, with root lattices $R_1, \ldots, R_m$, and let $T$ be its singular type.
Then $\PP\mcv_T$ (@not:sextic-singular-type) is a smooth irreducible quasi-projective variety (@def:projective-variety) of the expected dimension
$$
\binom{6+2}{2} - 1 - \Sum_{i=1}^m \rank(R_i) = 27 - \Sum_{i=1}^m \rank(R_i)
,
$$
and its points are stable for the action of $\SL_3$ on $\bigl(\PP H^0(\PP^2, \OO_{\PP^2}(6)), \OO(1)\bigr)$ [@YZZ25, §2.1].

:::

::: {.corollary #cor:ten-nodal-sextic-dimension title="Dimension of the space of ten-nodal sextics"}

For a singular type $T$ with root lattice $A_1^{\oplus 10}$, $\dim\PP\mcv_T = 17$.
This is the dimension of the Severi variety $S_{6,0}$ of @prop:rational-sextic-severi.

:::

::: {.proof}

Each $A_1$ has rank $1$, so $\Sum_i\rank(R_i) = 10$, and @prop:sextic-equisingular-dimension gives $27 - 10 = 17$.
The second statement is @prop:rational-sextic-severi (1).

:::

## A criterion for a node of a plane curve

::: {.proposition #prop:hessian-rank-at-singular-point title="Hessian rank at a singular point"}

Let $k$ be a field, let $F\in k[x_0, x_1, x_2]$ be homogeneous of degree (@def:graded-object) (@def:numerical-polarization) $n$, and let $p\in k^3$ be nonzero with
$$
\del_j F(p) = 0
\qquad\text{for } j = 0, 1, 2
.
$$
Then the Hessian matrix $H(F)(p) = \bigl(\del_i\del_j F(p)\bigr)_{ij}$ satisfies $H(F)(p)\cdot p = 0$, and hence
$$
\rank H(F)(p) \leq 2
.
$$
:::

::: {.proof}

Euler's identity for a homogeneous polynomial of degree $n$ reads $\Sum_i x_i\,\del_i F = n F$.
Differentiating it by $\del_j$ gives the polynomial identity
$$
\Sum_i x_i\,\del_j\del_i F \;+\; \del_j F \;=\; n\,\del_j F
,
$$
that is $\Sum_i x_i\,\del_i\del_j F = (n-1)\,\del_j F$.
Evaluating at $p$, where every first partial vanishes, gives $H(F)(p)\cdot p = 0$.
Since $p\neq 0$ the kernel (@def:kernel-cokernel) of $H(F)(p)$ is nonzero, so by rank-nullity in dimension $3$ the rank is at most $2$.
:::

