# Verbatim statements and proofs checked

## Gluing and G4, lattices.md

::: {.lemma #lem:gluing-discriminant-identification title="The gluing identification $\kappa\colon A_{E_{10}(2)}\isoto A_{T_\En}$"}

With $T_\Co = \generators{h}\perp E_{10}(2)$, $T_\En = U\perp E_{10}(2)$, $\delta$ and $H = \generators{(h/2,\delta/2)}$ as in @def:gamma-co-groups, put $S\definedas T_\Co\perp\ZZ\delta$, so that $T_\En = S_H$ and $A_{T_\En} = H^{\perp}/H$ carries the quadratic form induced by $q_S$ (@thm:nikulin-gluing); the map $\kappa$ below is the quotient $A_{E_{10}(2)}\isoto H^{\perp}/H$ and is not the inclusion $\kappa_h$ of that theorem.
Write $A_S = A_{T_\Co}\oplus A_{\ZZ\delta} = \generators{[h/2]}\perp A_{E_{10}(2)}\perp\generators{[\delta/2]}$. Then:

1. $H^{\perp} = \theset{a[h/2] + y + a[\delta/2]\ \mid\ a\in\{0,1\},\ y\in A_{E_{10}(2)}}$ and $[(a,y,a)] = [(0,y,0)]$ for these elements, so that
$$
\kappa\colon A_{E_{10}(2)}\too H^{\perp}/H = A_{T_\En},\qquad y\longmapsto[(0,y,0)],
$$
is a bijection.
2. $\kappa$ is an isometry of quadratic forms: $q_{T_\En}(\kappa(y)) = q_{E_{10}(2)}(y)$ for every $y\in A_{E_{10}(2)}$.
3. $\kappa$ carries the summands $A_{U(2)}$ and $A_{E_8(2)}$ of $A_{E_{10}(2)}$ onto the summands of the same names in $A_{T_\En} = A_{U(2)}\perp A_{E_8(2)}$; hence it conjugates the summand-preserving group $M\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})\leq\Orth(A_{T_\En},q)$ to the same product in $\Orth(q_{E_{10}(2)})$, which is the group $P$ of @def:congruence-group under the restriction isomorphism $\Orth(q_{T_\Co})\iso\Orth(q_{E_{10}(2)})$ of @lem:coble-discriminant-blocks(3).
4. Let $\varphi\in\Orth(T_\Co)$ fix $[h/2]$, so that $\varphi\oplus\id_{\ZZ\delta}$ preserves $H$ and extends to an isometry $g$ of $T_\En$ with $\restrictionof{g}{T_\Co} = \varphi$ (@thm:automorphism-lifting-criterion). Then
$$
\kappa^{-1}\,\bar\rho_{T_\En}(g)\,\kappa = \restrictionof{\bar\rho_{T_\Co}(\varphi)}{A_{E_{10}(2)}} ;
$$
in particular $g\in\discriminantkernel{T_\En}$ exactly when $\bar\rho_{T_\Co}(\varphi)$ acts trivially on $A_{E_{10}(2)}$, and, since $\bar\rho_{T_\Co}(\varphi)$ fixes $[h/2]$ and $A_{T_\Co} = \generators{[h/2]}\perp A_{E_{10}(2)}$, exactly when $\bar\rho_{T_\Co}(\varphi) = \id$.
:::

::: {.proof}

*The gluing data.* $S$ is even, and $H$ has order $2$ and is isotropic: the element $(h/2,\delta/2)$ has
$$
q_S = q_{T_\Co}(h/2) + q_{\ZZ\delta}(\delta/2) = \tfrac12 - \tfrac12 = 0 \pmod{2\ZZ},
$$
and its pairing with itself is $0$ in $\QQ/\ZZ$ for the same reason. So $A_{T_\En} = H^{\perp}/H$ with $q_{T_\En}$ induced by $\restrictionof{q_S}{H^{\perp}}$ (@thm:nikulin-gluing). On the two generators $q(h/2) = h^2/4 = \tfrac12$ and $q(\delta/2) = \delta^2/4 = -\tfrac12$, so $b(h/2,h/2) = h^2/4 = \tfrac12$ and $b(\delta/2,\delta/2) = \delta^2/4 = -\tfrac12$ in $\QQ/\ZZ$.

*(1)* An element $z = a[h/2] + y + c[\delta/2]$, with $a,c\in\{0,1\}$ and $y\in A_{E_{10}(2)}$, lies in $H^{\perp}$ exactly when
$$
b\bigl(z,(h/2,\delta/2)\bigr) = a\,b(h/2,h/2) + b(y,h/2) + c\,b(\delta/2,\delta/2) = \tfrac{a-c}{2}
$$
vanishes in $\QQ/\ZZ$, that is exactly when $a = c$; the middle term vanishes because $b(A_{E_{10}(2)},[h/2]) = 0$, $T_\Co = \generators{h}\perp E_{10}(2)$ being an orthogonal sum. This is the set displayed in (1). For such a $z$ one has $z - a(h/2,\delta/2) = (0,y,0)$ with $a(h/2,\delta/2)\in H$, so $[z] = [(0,y,0)]$, and every class of $H^{\perp}/H$ is of this form. The map is injective (@def:injective-map) on these representatives: if $(0,y,0)\in H$, then $y$ is the $A_{E_{10}(2)}$-coordinate of $0$ or of $(h/2,\delta/2)$, and in both cases $y = 0$. Hence $\kappa$ is a bijection.

*(2)* $q_{T_\En}(\kappa(y)) = q_S(0,y,0) = q_{T_\Co}(y) = q_{E_{10}(2)}(y)$, the middle term because $q_{T_\En}$ is induced by $q_S$ on $H^{\perp}$ and $(0,y,0)\in H^{\perp}$, the last because $T_\Co = \generators{h}\perp E_{10}(2)$ is an orthogonal sum.

*(3)* Since $U$ is unimodular, $T_\En^* = U\oplus U(2)^*\oplus E_8(2)^*$, so the classes modulo $T_\En$ of $U(2)^*$ and of $E_8(2)^*$ are the two summands of $A_{T_\En} = A_{U(2)}\perp A_{E_8(2)}$. For $y\in A_{U(2)}$ or $y\in A_{E_8(2)}$ one has $y\in E_{10}(2)^* = U(2)^*\oplus E_8(2)^*\subseteq T_\Co^*\cap T_\En^*$, the $U(2)^*\oplus E_8(2)^*$ summand being common to $T_\Co^* = \generators{h/2}\oplus E_{10}(2)^*$ and to $T_\En^* = U\oplus E_{10}(2)^*$, and the class of $y$ modulo $T_\En$ is $\kappa(y) = [(0,y,0)]$; so $\kappa$ maps the two summands of $A_{E_{10}(2)}$ onto those of $A_{T_\En}$ and conjugates $\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ to the same product. For the last clause, $A_{T_\Co} = \generators{[h/2]}\perp A^0$ with $A^0 = A_{E_{10}(2)}$, so restriction is an isomorphism $\Orth(q_{T_\Co})\iso\Orth(q_{A^0})$, and it carries the stabilizer (@def:group-orbit) $P$ of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$ to $\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ (@lem:coble-discriminant-blocks(3), (4)).

*(4)* Let $y\in A_{E_{10}(2)}$, represented by the functional that is $y$ on $E_{10}(2)$ and vanishes on $\generators{h}$ and on $\delta$. That representative lies in $E_{10}(2)^* = U(2)^*\oplus E_8(2)^*$, which is a summand of $T_\Co^* = \generators{h/2}\oplus E_{10}(2)^*$ and of $T_\En^* = U\oplus E_{10}(2)^*$; so $y$ may be read indifferently as a class of $A_{T_\Co}$ or of $A_{T_\En}$. The discriminant action of $g$ is $[x]\mapsto[g(x)]$ on $T_\En^*$. Choose a representative $z\in E_{10}(2)^*$ of $y$. Since $g$ restricts to $\varphi$ on $T_\Co$, its rational extension sends $z$ to $\varphi(z)\in T_\Co^*$. The class of $\varphi(z)$ modulo $T_\Co$ is $\bar\rho_{T_\Co}(\varphi)(y)$. Moreover $T_\Co\subseteq T_\En$, so replacing $\varphi(z)$ by an equivalent representative changes its class modulo $T_\En$ by zero. Note also that $\bar\rho_{T_\Co}(\varphi)$ preserves $A_{E_{10}(2)} = [h/2]^{\perp}$, because it fixes $[h/2]$. So
$$
\bar\rho_{T_\En}(g)(\kappa(y)) = [g(y)] = [\bar\rho_{T_\Co}(\varphi)(y)] = \kappa\bigl(\bar\rho_{T_\Co}(\varphi)(y)\bigr),
$$
which is the displayed identity. Its last clause is then immediate, and $\bar\rho_{T_\Co}(\varphi)$ acts on the direct sum $A_{T_\Co} = \generators{[h/2]}\perp A_{E_{10}(2)}$ as the identity on the first summand by hypothesis.
:::

::: {.proposition #prop:gamma-co-images title="The three restricted stabilizers"}
With $\delta$, $H$ and $R_\Gamma$ as in @def:gamma-co-groups, and $\bar\rho$ the discriminant representation (@def:discriminant-rep) of $T_\Co$:

1. $R_{\Gamma_\En} = \widetilde\Orth^+(T_\Co)$.
2. $R_{\Gamma^K_\En}$ is the stabilizer (@def:group-orbit) in $\Orth(T_\Co)$ of the class $[h/2]$ of $A_{T_\Co}$, and that stabilizer is all of $\Orth(T_\Co)$, because $[h/2]$ is the characteristic class of $q_{T_\Co}$:
$$
R_{\Gamma^K_\En} = \theset{\varphi\in\Orth(T_\Co)\ \mid\ \bar\rho(\varphi)(h/2) = h/2} = \Orth(T_\Co).
$$
3. $R_{\gent} = \bar\rho^{-1}(P)$, where $P\leq\Orth(q_{T_\Co})$ is the stabilizer of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$ of the proof. It is a subgroup of $\Orth(T_\Co)$ of index $[\Orth(q_{T_\Co}) : P] = 2^7\cdot17\cdot31 = 67\,456$ (Step 6 of the proof), and it contains $\ker\bar\rho$.
:::

::: {.proof}

*Step 0: the two lattices and the gluing.* $T_\Co = \generators{h}\perp U(2)\perp E_8(2)$ and $T_\En = U\perp U(2)\perp E_8(2)$, and $\delta = \tilde e-\tilde f$ has $\delta^2 = -2$ and $\delta^{\perp T_\En} = \eta(T_\Co)$ (@lem:primitive_embedding_eta). By Nikulin's gluing theorem (@thm:nikulin-gluing, which is [@Nik80, Prop. 1.5.1]) an even overlattice of $T_\Co\perp\generators{\delta}$ is the same thing as an isotropic subgroup $H\subseteq A_{T_\Co}\oplus A_{\generators{\delta}}$, and $A_{(T_\Co\perp\generators{\delta})_H} = H^{\perp}/H$ as quadratic forms, the form on the quotient being the one induced by $q_{T_\Co}\oplus q_{\generators{\delta}}$ on $H^{\perp}$; here $H = \generators{(h/2,\delta/2)}$. Isotropy of this $H$ is the single congruence
$$
q_{T_\Co}(h/2)+q_{\generators{\delta}}(\delta/2) = \tfrac12-\tfrac12\equiv 0 \pmod{2\bZ},
$$
and it is what makes $T_\En$ an *even* lattice rather than merely an overlattice glued along a subgroup of order $2$. Since $\abs{H} = 2$,
$$
\abs{A_{T_\En}} = \abs{A_{T_\Co}}\cdot\abs{A_{\generators{\delta}}}/\abs{H}^2 = 2^{11}\cdot 2/4 = 2^{10},
$$
as the invariant $a = 10$ of $T_\En = (12,10,0)_2$ requires.

*Step 1: the discriminant form of $T_\Co$, and its characteristic class.* On the orthogonal decomposition $A_{T_\Co} = \generators{h/2}\perp A_{U(2)}\perp A_{E_8(2)}$, which is orthogonal because $T_\Co = \generators{h}\perp E_{10}(2)$ is, the values of $q$ are these:

- $q(h/2) = h^2/4 = 1/2$, and $b(h/2,h/2) = 1/2$;
- on $A_{U(2)}$, with the classes of $e'/2$ and $f'/2$ for the isotropic basis (@def:isotropic-basis-hyperbolic-plane) $e',f'$ of $U(2)$, $(e',f') = 2$: $q(e'/2) = q(f'/2) = 0$ and $q((e'+f')/2) = (e'+f')^2/4 = 1$, so the three nonzero classes have $q$-values $0,0,1$, all integers, and $q\bmod1$ vanishes on this block;
- on $A_{E_8(2)}$, with the classes of $\alpha_i/2$ for a basis $\alpha_i$ of $E_8$: $q(y/2) = y^2/2\in\bZ$ for every $y\in E_8$, so $q\bmod1$ vanishes here too, and $q$ on this block is the quadratic form $y\mapsto y^2/2\bmod 2\bZ$ of $E_8/2E_8$.

The form $b$ is nondegenerate on each block: on $\generators{h/2}$ it has $b(h/2,h/2)=1/2$; on $A_{U(2)}$ it has $b(e'/2,e'/2)=b(f'/2,f'/2)=0$ and $b(e'/2,f'/2)=1/2$; and on $A_{E_8(2)}$ the associated $\bF_2$-polar form is the $E_8$ Cartan matrix modulo $2$, of determinant $1$. Hence $b$ is nondegenerate on their orthogonal sum $A_{T_\Co}$.

The argument needs $2$-elementarity for $q$ to take values in $\tfrac12\bZ/2\bZ$ and for $q\bmod1$ to be linear: if $L$ is even and $2$-elementary then $2x\in L$ for $x\in L^*$, hence $q(x) = x^2$ lies in $\tfrac12\bZ/2\bZ$ and $2b(x,y)$ is integral for all $x,y\in A_L$, so $q(x+y)-q(x)-q(y) = 2b(x,y)$ vanishes modulo $1$. Since $b$ is nondegenerate there is therefore a *unique* $w$ with $b(w,x)\equiv q(x)\pmod1$ for all $x$, the characteristic element of $q$; additivity over orthogonal sums follows from uniqueness, and $w=0$ exactly when $q$ is $\bZ$-valued. Applied to $q_{T_\Co} = q_{\generators{h/2}}\oplus q_{E_{10}(2)}$ this gives $w = [h/2]$ in one line: $q(h/2) = h^2/4 = 1/2 = b(h/2,h/2)$ makes $[h/2]$ the characteristic element of the first summand, and $q_{E_{10}(2)}$ is $\bZ$-valued, $q(y/2) = y^2/2\in\bZ$ for $y\in E_{10}$, so its characteristic element is $0$. Hence for every isometry $\sigma$ of $(A_{T_\Co},q)$ and every $x$,
$$
b(\sigma(h/2),x) = b(h/2,\sigma^{-1}x)\equiv q(\sigma^{-1}x) = q(x)\equiv b(h/2,x)\pmod1,
$$
and nondegeneracy of $b$ gives $\sigma(h/2) = h/2$: every isometry of $q_{T_\Co}$ fixes $[h/2]$. This is the case $k = [h/2]$ of @lem:coble-discriminant-blocks(3), which proves the same thing for every form of the shape $\bZ k\perp A^0$; the argument is repeated here because (1) and (3) both use it, and because the vanishing of $q\bmod1$ has to be checked on the two blocks separately, with a different reason in each.

*Step 2: which isometries of $T_\Co$ lift over $\delta$.* Let $g\in\Orth(T_\En)$ fix $\delta$. Then $g$ preserves $\delta^{\perp T_\En} = \eta(T_\Co)$, so after scalar extension $g = \varphi\oplus\id_{\generators{\delta}}$ with $\varphi = \restrictionof{g}{T_\Co}$; in particular the restriction map $\Stab_{\Orth(T_\En)}(\delta)\to\Orth(T_\Co)$ is injective (@def:injective-map). And $\varphi\oplus\id$ preserves the overlattice $T_\En$ exactly when $(\bar\rho(\varphi)\oplus\id)(H) = H$ (@thm:automorphism-lifting-criterion, which is [@Nik80, Cor. 1.5.2] applied to the gluing datum of @def:gluing-datum-of-a-pair). The elements of $H$ are $0$ and $(h/2,\delta/2)$, and the second coordinate of $(\bar\rho(\varphi)\oplus\id)(h/2,\delta/2)$ is $\delta/2\neq0$, so the condition is $\bar\rho(\varphi)(h/2) = h/2$. Conversely that condition makes $\varphi\oplus\id$ preserve $H$, hence extend to an isometry of $T_\En$, which fixes $\delta$. So $\varphi$ extends to an isometry of $T_\En$ fixing $\delta$, uniquely, exactly when it fixes $[h/2]$; on discriminant groups, $\varphi\oplus\id$ acts by $\bar\rho(\varphi)$ on $A_{E_{10}(2)}$, which $\kappa$ identifies with the whole of $A_{T_\En}$ (@lem:gluing-discriminant-identification(4)).

*Step 3: part (2).* By Step 1 every isometry of $q_{T_\Co}$ fixes $[h/2]$, and by @thm:two-elementary-surjectivity ([@Nik80, Thm. 3.6.3]) the map $\bar\rho\colon\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is onto, its hypotheses being exactly that $T_\Co$ is even, indefinite and $2$-elementary, which the table gives; $T_\Co$ is moreover the case $a = t_{(+)}+t_{(-)}$ of the proof of the theorem, $11 = 2+9$, where Nikulin reduces to the orthogonal summand $u_+^{(2)}(2)$ or $\upsilon_+^{(2)}(2)$ that $q_{T_\Co}$ has in its $U(2)$ block [@Nik80, Thm. 3.6.3]. So every $\varphi\in\Orth(T_\Co)$ satisfies the condition of Step 2, and
$$
\Stab_{\Orth(T_\En)}(\delta) = \theset{\varphi\oplus\id_{\generators{\delta}}\mid\varphi\in\Orth(T_\Co)}\;\cong\;\Orth(T_\Co),
$$
the restriction map being the inverse. That is (2), and with it: every isometry of $T_\Co$ extends to an isometry of $T_\En$ fixing $\delta$.

*Step 4: part (1).* Let $g = \varphi\oplus\id$ fix $\delta$. By @lem:gluing-discriminant-identification(4), $g\in\discriminantkernel{T_\En}$ exactly when $\bar\rho(\varphi)$ acts trivially on $A_{E_{10}(2)}$; since $\bar\rho(\varphi)$ fixes $[h/2]$ (Step 1) and $A_{T_\Co} = \generators{h/2}\oplus A_{E_{10}(2)}$, that holds exactly when $\bar\rho(\varphi) = \id$. For the sign, recall that $\Orth^+(L) = \Theta_\bR(L) = \ker\spinornorm_\bR$ is the kernel of the real spinor norm [@def:lattice-spinor-kernels], and that $g = \varphi\perp\id_{\generators{\delta}}$ is an orthogonal sum. The spinor norm is multiplicative on an orthogonal sum,
$$
\spinornorm_\bR(\varphi\perp\psi) = \spinornorm_\bR(\varphi)\,\spinornorm_\bR(\psi),
$$
because a reflection $s_w$ with $w\in T_\Co\tensor\bR$ acts on $T_\En\tensor\bR$ as the reflection in the same vector, with the same value $\spinornorm_\bR(s_w) = [-\tfrac12w^2]$ [@def:spinor-norm], and $\varphi\perp\psi = (\varphi\perp\id)(\id\perp\psi)$. So $\spinornorm_\bR(g) = \spinornorm_\bR(\varphi)\cdot\spinornorm_\bR(\id) = \spinornorm_\bR(\varphi)$, and $g\in\Orth^+(T_\En)$ exactly when $\varphi\in\Orth^+(T_\Co)$.

The sign is not read off positive definite subspaces, and the tempting argument that it is, is false: $\delta^2<0$ does not place every maximal positive definite subspace (@def:maximal-positive-definite-subspace) of $T_\En\tensor_\bR$ inside $\delta^{\perp}$, since $\eta(h)$ and $e'+f'+\delta$ span a positive definite plane --- of the maximal dimension $2$ --- with $(\eta(h),e'+f'+\delta) = 0$ and $(e'+f'+\delta,\delta) = -2$. What is true is the spinor statement above, and it is what the proof uses. So restriction carries $\Stab_{\Gamma_\En}(\delta)$ into $\widetilde\Orth^+(T_\Co)$; conversely, for $\varphi\in\widetilde\Orth^+(T_\Co)$ the element $\varphi\oplus\id$ lies in $\Stab_{\Gamma_\En}(\delta)$ by the two characterizations just proved. That is (1).

*Step 5: part (3).* By @prop:sterk-group-identification(2), $\gent = \rho^{-1}(M)$ with $M = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ the subgroup of $\Orth(A_{T_\En},q)$ preserving the decomposition, the identification of $\gent$ with the group of [@AEGS25, Def. 2.6] being @prop:sterk-group-identification(1) and the description by the two summands being [@Ste91, Prop. 2.7]. So $g = \varphi\oplus\id$ fixing $\delta$ lies in $\gent$ exactly when $\bar\rho(\varphi)$ preserves $A_{U(2)}$ and $A_{E_8(2)}$, the summands of $A_{T_\En}$ being $\kappa$ of the summands of $A_{E_{10}(2)}$ (@lem:gluing-discriminant-identification(3)). Every $\sigma\in\Orth(q_{T_\Co})$ fixes $w = [h/2]$ (Step 1), hence preserves $w^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$, of dimension $10$; so restriction $\Orth(q_{T_\Co})\to\Orth(w^{\perp},q|_{w^{\perp}})$ is defined, and it is injective because an isometry fixing $w^{\perp}$ pointwise fixes $w$ too, $A_{T_\Co} = \generators{w}\oplus w^{\perp}$. The condition is therefore $\bar\rho(\varphi)\in P$, where $P$ is the stabilizer in $\Orth(q_{T_\Co})$ of the decomposition $w^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$, and $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ by @lem:coble-discriminant-blocks(4). So $R_{\gent} = \bar\rho^{-1}(P)$, and it contains $\ker\bar\rho$.

*Step 6: the index.* Because $\bar\rho$ is onto (Step 3), $[\Orth(T_\Co):R_{\gent}] = [\Orth(q_{T_\Co}):P]$, and by orbit--stabilizer the latter is the number of elements in the orbit (@def:group-orbit) of the decomposition $D\colon w^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$. Let $N$ be the number of decompositions of $w^{\perp}$ into a $2$-dimensional summand isometric to $A_{U(2)}$ and an $8$-dimensional one isometric to $A_{E_8(2)}$; the orbit lies in that set, so $[\Orth(q_{T_\Co}):P]\leq N$. The two are computed separately, and they agree.

*(i) $N = 67\,456$.* On $w^{\perp}$ the form $q$ is $\bZ$-valued (Step 1), so $(w^{\perp},q)$ is a quadratic space over $\bF_2$, and it is of plus type: $528$ of its classes have $q = 0$, the zero class included, and $496$ have $q = 1$ (@lem:coble-discriminant-blocks(2), whose count $3\cdot136+1\cdot120 = 528$ is this one). A $2$-dimensional subspace of $w^{\perp}$ is isometric to $A_{U(2)}$ exactly when it is spanned by classes $a,b$ with $q(a) = q(b) = 0$ and $b(a,b) = 1/2$, for then $q(a+b) = 1$ and $b$ is nondegenerate on the span. There are $527$ choices for $a$; for fixed $a$ the classes with $b(a,b) = 1/2$ form an affine hyperplane of order $2^9 = 512$, and the translation $b\mapsto b+a$ preserves it and sends $q(b)$ to $q(b)+q(a)+2b(a,b) = q(b)+1$, so exactly $256$ of them have $q(b) = 0$; each subspace is counted twice, through its two classes of value $0$. Hence
$$
N = \frac{527\cdot 256}{2} = 527\cdot 128 = 2^7\cdot17\cdot31 = 67\,456 .
$$
The orthogonal complement of such a subspace is a plus space of dimension $8$, that is $A_{E_8(2)}$ up to isometry, so every such subspace is one of the decompositions counted by $N$.

*(ii) $\abs{\Orth(q_{T_\Co})}/\abs{P} = 2^7\cdot17\cdot31$.* Here $\Orth(q_{T_\Co})\cong\Orth(w^{\perp},q)$ is the orthogonal group of a hyperbolic space of dimension $10$, and $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$. The restriction is an isomorphism, not only an injection: an isometry of $w^{\perp}$ extends by $w\mapsto w$, and that is an isometry because $\generators{w}\perp w^{\perp} = A_{T_\Co}$. Both orders are counts of ordered hyperbolic bases, an isometry of a hyperbolic space being determined by, and determining, the image of one fixed hyperbolic basis, and in dimension $2m$ the first hyperbolic pair (@def:isotropic-basis-hyperbolic-plane) can be chosen in $(2^{2m-1}+2^{m-1}-1)\cdot2^{2m-2}$ ways. This gives $\abs{\Orth(q_{U(2)})} = 2$, then $\abs{\Orth(q_{E_8(2)})} = 2\cdot(9\cdot4)\cdot(35\cdot16)\cdot(135\cdot64) = 348\,364\,800$, then $\abs{P} = 2\cdot 348\,364\,800 = 696\,729\,600 = \abs{W(E_8)}$ and $\abs{\Orth(q_{T_\Co})} = 527\cdot256\cdot 348\,364\,800 = 46\,998\,591\,897\,600 = 2^{21}3^55^27\cdot17\cdot31$, so that
$$
\frac{\abs{\Orth(q_{T_\Co})}}{\abs{P}} = 2^7\cdot17\cdot31 = 67\,456 .
$$
Both computations are in `computations/reports/coble_788-gamma-co-images-index-run.txt`, which also verifies the quadratic-form relation on all $2^{22}$ pairs, the characteristic class on all $2048$ classes, the plus type of $w^{\perp}$ and the type of the $67\,456$ complements. Since the orbit has $67\,456$ elements and the set it lies in has $67\,456$ elements, the orbit is that whole set and
$$
[\Orth(T_\Co):R_{\gent}] = [\Orth(q_{T_\Co}):P] = 2^7\cdot17\cdot31 = 67\,456 .
$$
The number is published, and the two orders are the two in the source: [@Ste91, Rem. 2.12] computes $[\Orth(L_-):\Gamma] = (2^{21}3^55^27\cdot17\cdot31)/(2\cdot2^{13}3^55^27) = 2^7\cdot17\cdot31$, and $[\Orth(L_-):\Gamma] = [\Orth(q_{T_\Co}):P]$ because $\kappa$ identifies $A_{T_\En}$ with $A_{E_{10}(2)}$ and carries $M$ to $P$ (@lem:gluing-discriminant-identification(2), (3), with the restriction $\Orth(q_{T_\Co})\iso\Orth(q_{E_{10}(2)})$ of @lem:coble-discriminant-blocks(3)), the lattice $L_-$ of the source being $T_\En$ summand by summand (@prop:sterk-group-identification(1)), and $\Gamma$ is $\gent$, whose discriminant image is $M = P$. The same number is the index in $\Orth^+$: the vector $\zeta\definedas h$ is primitive of square $2$, so $s_\zeta\in\ker\bar\rho\subseteq R_{\gent}$ and $s_\zeta\notin\Orth^+(T_\Co)$ (@prop:gamma-co-reflective-set(2), which proves both halves for a primitive vector of square $2$). The first holds because $s_\zeta(x^*) - x^* = -b(x^*,\zeta)\zeta$ lies in $T_\Co$ for every $x^*\in T_\Co^*$, a reflection in a vector of square $2$ being discriminant-trivial; the second because $\spinornorm_\bR(s_\zeta) = [-\tfrac12\zeta^2] = [-1]$ is not the identity (@prop:gamma-co-reflective-set(2), @def:spinor-norm). Hence $R_{\gent}\cdot\Orth^+(T_\Co) = \Orth(T_\Co)$, and
$$
[\Orth^+(T_\Co):R_{\gent}\intersect\Orth^+(T_\Co)] = [\Orth(T_\Co):R_{\gent}] = 67\,456 .
$$
:::

::: {.remark #rmk:gamma-co-images-inputs title="What each step of @prop:gamma-co-images needs, and where it stands"}

Each step of the proof above rests on a statement that the step itself does not prove. The eleven such statements are listed below with the step that uses each and with its status; *proved* means proved on this page, and the numbered source is the numbered statement that supplies the mathematical content, with its section. The list is the check that no step carries more than it says.

1. *$T_\Co$ is even, of signature $(2,9)$ and $2$-elementary with $a = 11$.* Needed in Step 1 (for $q$ to take values in $\tfrac12\bZ/2\bZ$), Step 0 ($\abs{A_{T_\Co}} = 2^{11}$) and Step 3 (the three hypotheses of Nikulin's theorem). Status: proved --- @prop:theta-co-exists with the table of the notation block at the head of this chapter; the isometry class is [@DK13, (3.6)] and [@Nik80, Thm. 3.6.2].
2. *$H = \generators{(h/2,\delta/2)}$ is isotropic.* Needed in Step 0: otherwise $(T_\Co\perp\generators{\delta})_H$ is not even and Nikulin's gluing theorem does not apply to it. Status: proved --- the one congruence displayed in Step 0.
3. *$[h/2]$ is the characteristic class of $q_{T_\Co}$, i.e. $b(h/2,x)\equiv q(x)\pmod1$ for all $x$.* Needed in Step 2, where the lifting condition becomes automatic, and hence in (2). Status: proved --- Step 1 checks the characteristic equation on the two summands, and nondegeneracy (item 4) gives uniqueness and invariance under every discriminant isometry; @lem:coble-discriminant-blocks(3) independently proves the same thing in the shape $k\perp A^0$.
4. *$b$ is nondegenerate on $A_{T_\Co}$.* Needed in Step 1 for the uniqueness of the characteristic class, and so for the passage from (2) to (3). Status: proved directly on the three orthogonal blocks in Step 1 --- the $U(2)$ pairing has determinant $-1/4$, and the $E_8$ Cartan matrix modulo $2$ has determinant $1$.
5. *$\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is onto.* Needed in Step 3 and in Step 6, and it is what turns "every isometry of the discriminant form" into "every isometry of the lattice". Status: published --- [@Nik80, Thm. 3.6.3] = @thm:two-elementary-surjectivity, the hypotheses being verified in Step 3.
6. *$\gent$ is the group of [@AEGS25, Def. 2.6], and that group is the set of isometries of $T_\En$ whose discriminant action preserves the two summands $A_{U(2)}$, $A_{E_8(2)}$.* Needed in Step 5: without it $R_{\gent}$ is the image of a group that has not been identified with the group of the published degree-two family. Status: page proof --- @prop:sterk-group-identification(1), (2), resting on [@AEGS25, Defs. 2.6--2.7] and [@Ste91, Prop. 2.7]. This is the step that identifies the group of the published degree-two Enriques family; it is a statement about an arithmetic group, and the monodromy group $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5) is a different group, no inclusion between it and $R_{\gent}$ being asserted here.
7. *$\Orth^+$ is the kernel of the real spinor norm, and the spinor norm is multiplicative on an orthogonal sum, so $\spinornorm_\bR(\varphi\perp\id) = \spinornorm_\bR(\varphi)$.* Needed in Step 4 for the sign. It cannot be replaced by an argument about positive definite subspaces: $\delta^2<0$ does not put every maximal positive definite subspace of $T_\En\tensor\bR$ inside $\delta^{\perp}$, since $\eta(h)$ and $e'+f'+\delta$ span one with $(e'+f'+\delta,\delta) = -2$. Status: definition plus the reflection formula of @def:spinor-norm, and multiplicativity is what the exact sequence of @def:lattice-spinor-kernels asserts.
8. *The restriction $\Stab_{\Orth(T_\En)}(\delta)\to\Orth(T_\Co)$ is injective.* Needed for an equality, not only an inclusion, in (2) and (3): an isometry fixing $\delta$ and acting trivially on $\delta^{\perp T_\En}$ is the identity. Status: proved --- Step 2, where the scalar extension of $g$ is $\varphi\oplus\id$.
9. *The line stabilizer $\Stab_{\gent}(\ZZ\delta)$ and the vector stabilizer $\Stab_{\gent}(\delta)$ have the same image in $\Orth(T_\Co)$.* Needed only if the statement is read with the root fixed up to sign, which is how the stabilizer of a root class is usually written; with $\delta$ fixed as a vector, as in (2) and (3), it is not needed. Status: page proof --- the proof of @lem:coble-monodromy-in-stabilizer: if $\rho(\gamma)\delta = -\delta$ then $s_\delta\rho(\gamma)$ fixes $\delta$, and $s_\delta$ acts as the identity on $\delta^{\perp T_\En}$.
10. *$w^{\perp} = [h/2]^{\perp}$ is of plus type, and $[h/2]$ generates a direct summand of $A_{T_\Co}$.* Needed in Step 6, both for the count of the $527$ classes and for reading $\Orth(q_{T_\Co})\to\Orth(w^{\perp},q)$ as an isomorphism. Status: proved --- Step 1 and @lem:coble-discriminant-blocks(2), (3).
11. *The gluing identification $\kappa\colon A_{E_{10}(2)}\isoto A_{T_\En}$ is defined and is an isometry, it carries the two summands of $A_{E_{10}(2)}$ to those of $A_{T_\En}$, and $\varphi\oplus\id$ acts on $A_{T_\En}$ by $\bar\rho(\varphi)$.* Needed in Steps 2, 4, 5 and 6: it is what makes "$A_{E_{10}(2)}$" and "$A_{T_\En}$" the same object, hence what turns the vanishing of the discriminant action of $g$ into a condition on $\bar\rho(\varphi)$, and what transfers Sterk's group $M$ and its index to $P$. Status: proved --- @lem:gluing-discriminant-identification(1)--(4), which proves the bijectivity, the isometry, the two summands and the action formula from the gluing datum of @def:gamma-co-groups.

*The statements that the issue names.* The issue names four of Nikulin's; the proof uses three of them, and the fourth is read and recorded below as not needed. A fifth, Proposition 1.5.1, is the gluing theorem that Step 0 rests on. Proposition 1.5.1 is on the page as @thm:nikulin-gluing; Corollary 1.5.2 is the automorphism-lifting criterion used in Steps 2 and 5 and in @lem:gluing-discriminant-identification(4), on the page as @thm:automorphism-lifting-criterion; Theorem 3.6.2 is item 1 (the isometry class of an even $2$-elementary lattice by its invariants); Theorem 3.6.3 is item 5. The fourth of the issue's, **Theorem 1.14.4** [@Nik80, Thm. 1.14.4], is **not used** by the proof, and it is recorded here so that its absence is a statement and not an omission. It is the analogue of Witt's theorem: for an even lattice $M$ of signature $(t_{(+)},t_{(-)})$ and an even unimodular lattice $L$ of signature $(l_{(+)},l_{(-)})$, there is a *unique* primitive embedding $M\into L$ provided (1) $l_{(+)}-t_{(+)}>0$ and $l_{(-)}-t_{(-)}>0$, (2) $l_{(+)}-t_{(+)} + l_{(-)}-t_{(-)}\geq 2 + \ell(A_{M_p})$ for every $p\neq2$, and (3) if that difference equals $\ell(A_{M_2})$ then $q_M\cong u_+^{(2)}(2)\oplus q'$ or $q_M\cong v_+^{(2)}(2)\oplus q'$. [@AEGS25, Lemma 2.4], on the page as @lem:enriques-embedding-chain, invokes it for the uniqueness of the embedding $U(2)\oplus E_8(2)\into L$ of the Enriques theory, into the even unimodular lattice $(3,19)$: the three conditions hold there, $(1)$ as $3-1 = 2>0$ and $19-9 = 10>0$, $(2)$ as $12\geq 2+0$ for odd $p$, and $(3)$ is vacuous because $12\neq\ell(A_{M_2}) = 10$. The uniqueness that @prop:gamma-co-images(2) asserts is *not* an instance of it and does not need it: there the embedding $\eta$ is given, and uniqueness is injectivity of the restriction $\Stab_{\Orth(T_\En)}(\delta)\to\Orth(T_\Co)$ (item 8), while existence is Corollary 1.5.2. An embedding-uniqueness theorem about $M\into L$ with $L$ unimodular says nothing about which isometries of a fixed $\delta^{\perp}$ lift, which is what the proposition is about.


## Sterk identification, lattices.md

:::

::: {.proposition #prop:sterk-group-identification title="The discriminant image of $\gent$"}

Let $\rho\colon\Orth(\ten)\to\Orth(A_{\ten}, q_{\ten})$ be the discriminant representation (@def:discriminant-rep) and $K = \ker\rho$.
Identify $\ten = U\oplus U(2)\oplus E_8(2)$ with the lattice $L_- = \mathbf H\oplus\mathbf H(2)\oplus E_8(-2)$ of [@Ste91, 1.3] summand by summand, and let $e', f'$ be the isotropic (@def:orthogonal-complement) basis (@def:based-module) of $U(2)$, with $(e', f') = 2$.

1. $\gent$ is the group (@def:group) $\Gamma$ of [@Ste91, §2, Prop. 2.7], and $\gent = \theset{g\in\Orth(\ten) \st \rho(g)\text{ preserves the summands } A_{U(2)} \text{ and } A_{E_8(2)} \text{ of } A_{\ten}}$.
2. $\rho(\gent) = M\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$, and $\gent = \rho^{-1}(M)$; in particular $K\subseteq\gent$.
3. $\gent$ is a proper subgroup of $\Stab_{\Orth(\ten)}\bigl([(e'+f')/2]\bigr)$.
:::

::: {.proof}

(1) The group $\Gamma$ of [@Ste91, Prop. 2.7] is the image in $\Orth(L_-)$ of the isometries of the K3 lattice that commute with the Enriques involution (@def:enriques-surface) and fix the polarization vector (@def:polarization-vector), and $\gent$ is the image in $\Orth(\ten)$ of the same group [@AEGS25 Def. 2.6].
The description by the two summands is [@Ste91, Prop. 2.7].

(2) Because $U$ is unimodular, $A_{\ten} = A_{U(2)}\perp A_{E_8(2)}$, and an isometry of $q_{\ten}$ preserves both summands exactly when it is a pair of isometries of the summands.
So (1) says $\gent = \rho^{-1}(M)$.
The lattice $\ten$ is even (@def:form-axioms), indefinite (@def:definiteness) and $2$-elementary, so $\rho$ is surjective (@thm:two-elementary-surjectivity), and $\rho(\gent) = M$.

(3) The three nonzero classes of $A_{U(2)}$ are $[e'/2]$, $[f'/2]$ and $[(e'+f')/2]$, with $q$-values $0$, $0$ and $(e'+f')^2/4 = 1$.
So every element of $\Orth(q_{U(2)})$ fixes $[(e'+f')/2]$, and $\gent$ stabilizes it by (2).
Since $f'\in\ten$, the classes $[(e'+f')/2]$ and $[(e'-f')/2]$ are equal.
The isometry $\psi\in\Orth(L_-)$ of [@Ste91, Rem. 2.8] stabilizes $\tfrac12(e'-f')+L_-$ and is not in $\Gamma$.
:::

::: {.proposition #prop:gamma-en-two-index title="The index of $\gent$"}

With $\rho$, $K$ and $M$ as in @prop:sterk-group-identification,
$$
[\Orth(\ten) : \gent] \;=\; [\Orth(A_{\ten},q_{\ten}) : M] \;=\; 2^7\cdot 17\cdot 31 \;=\; 67\,456 .
$$
:::

::: {.proof}

By @prop:sterk-group-identification, $\gent = \rho^{-1}(M)$ and $\rho$ is surjective, so $\rho$ induces a bijection $\Orth(\ten)/\gent\to\Orth(A_{\ten},q_{\ten})/M$.
Because $U$ is unimodular, $A_{\ten} = A_{E_{10}(2)}$, so $\abs{\Orth(A_{\ten},q_{\ten})} = 2^{21}\cdot3^5\cdot5^2\cdot7\cdot17\cdot31$ by @prop:coble-discriminant-group.
By @prop:gamma-en-two-gluing, $M = \rho(\gent)$ is the $\gamma$-transport of the image of $\Stab_{\Orth(\sen)}(h)$ in $\Orth(q_{\sen})$, which has order $\abs{W(E_8)} = 2^{14}\cdot3^5\cdot5^2\cdot7$ by @thm:coble-heegner-finite-orbits(1).

## G5 reverse-reduction citation, lattices.md

:::

::: {.lemma #lem:coble-monodromy-reverse-reduction title="The reverse inclusion splits into a discriminant surjectivity and the stable group"}

Let $\Gamma_{\Co,2}$ be the monodromy group of @def:gamma-co-groups(5), so that $\Gamma_{\Co,2}\subseteq\Orth^+(T_\Co)$ (@thm:coble-monodromy-versus-enriques(1)), and let $R_{\gent} = \bar\rho^{-1}(P)$ (@prop:gamma-co-images(3)). Then
$$\Gamma_{\Co,2} = R_{\gent}\intersect\Orth^+(T_\Co)$$
if and only if both

1. $\bar\rho(\Gamma_{\Co,2}) = P$, and
2. $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$.
:::

::: {.proof}
Since $R_{\gent} = \bar\rho^{-1}(P)$ and $\widetilde\Orth^+(T_\Co) = \ker\bar\rho\intersect\Orth^+(T_\Co)$, the group $R_{\gent}\intersect\Orth^+(T_\Co)$ is the preimage in $\Orth^+(T_\Co)$ of $P$.

If (1) and (2) hold and $g\in R_{\gent}\intersect\Orth^+(T_\Co)$, choose $\gamma\in\Gamma_{\Co,2}$ with $\bar\rho(\gamma) = \bar\rho(g)$, which (1) permits; then $g\gamma^{-1}\in\Orth^+(T_\Co)$ and $\bar\rho(g\gamma^{-1}) = \id$, so $g\gamma^{-1}\in\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$ by (2), and $g\in\Gamma_{\Co,2}$.


## B2 setting and zero-cusp proof

Let
$$
\gent = \Gamma_{\En,2}\leq\Orth(\ten)
$$
be the image of $\{g\in\Orth(L) : g\Ien = \Ien g,\ g(h) = h\}$, $h$ the degree-$2$ polarization [@AEGS25, Def. 2.6]; this is the group $\Gamma$ of [@Ste91, Prop. 2.7], characterised there as the set of isometries of $\ten$ whose induced map on $A_{\ten} = A_{U(2)}\oplus A_{E_8(2)}$ respects the two summands. Let
$$
R \definedas R_{\gent} = \text{the image of } \Stab_{\gent}(\delta) \text{ in } \Orth(\delta^{\perp\ten}) = \Orth(T_\Co)
$$
[@def:gamma-co-groups(4)]; equivalently $R = \bar\rho^{-1}(P)$, where $\bar\rho\colon\Orth(T_\Co)\to\Orth(q_{T_\Co})$ is the discriminant representation and $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$ the stabilizer of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$, so that
$$
[\Orth(T_\Co):R] = \abs{\Orth(q_{T_\Co})}/\abs{P} = 2^7\cdot17\cdot31 = 67\,456
$$
[@prop:gamma-co-images(3), @thm:gamma-co-2-comparison(3)].

The boundary components of a type IV quotient $D(\Lambda)/\Gamma$ are described as follows: a $0$-cusp is a $\Gamma$-orbit of primitive isotropic lines of $\Lambda$, a $1$-cusp a $\Gamma$-orbit of primitive isotropic planes [@AEGS25, Def. 2.9]. Sterk's five $0$-cusps of $F_{\En,2} = D(\ten)/\gent$ are represented by
$$
e,\qquad e',\qquad e'+f'+y_3,\qquad 2e'+f'+y_4,\qquad 2e+2f+y_4,
$$
with $y_3 = -(2\alpha_1+3\alpha_2+4\alpha_3+6\alpha_4+5\alpha_5+4\alpha_6+3\alpha_7+2\alpha_8)$ of square $-4$ and $y_4 = -(4\alpha_1+5\alpha_2+7\alpha_3+10\alpha_4+8\alpha_5+6\alpha_6+4\alpha_7+2\alpha_8)$ of square $-8$ [@Ste91, (4.2.3)], and are numbered $1,\dots,5$ in that order; the numbering and the vectors are those of @ex:sterk-isotropic-divisibilities. Throughout, $\Stab_{\gent}(e_k)$ denotes the stabilizer in $\gent$ of the line $\ZZ e_k$.

## Primitivity

::: {.lemma #lem:primitivity-tco-in-ten title="A vector primitive in $T_\Co$ is primitive in $\ten$"}
If $v\in T_\Co$ is primitive (@def:primitive-embedding) in $T_\Co$, it is primitive in $\ten$.
:::

::: {.proof}
Suppose $v = mw$ with $w\in\ten$ and $m>1$. Since $v\in T_\Co = \delta^{\perp\ten}$, $0 = v\cdot\delta = m\,(w\cdot\delta)$, hence $w\cdot\delta = 0$ and $w\in\delta^{\perp\ten} = T_\Co$. So $v$ is not primitive in $T_\Co$.
:::

Consequently a primitive isotropic line or plane of $T_\Co$ is a primitive isotropic line or plane of $\ten$. Together with the fact that every $r\in R$ is the restriction of an element of $\Stab_{\gent}(\delta)$ (@prop:gamma-co-images(3)), this makes the forgetful map on cusps below well defined; a $\gent$-orbit of lines or planes of $\ten$ need not however preserve $\delta^{\perp}=T_\Co$, and none of the arguments below uses such a statement.

## The correspondence

::: {.theorem #thm:b2-zero-cusps title="B2 for $0$-cusps: the $0$-cusps of $D(T_\Co)/R$ are the $\gent$-orbits of pairs $(\ell,\alpha)$"}
Let $\mathcal P_0$ be the set of pairs $(\ell,\alpha)$ in which $\ell\subset\ten$ is a primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) line and $\alpha\in\ten$ is a $(-2)$-vector with $\alpha\perp\ell$, and let $\gent$ act on $\mathcal P_0$ by $g(\ell,\alpha) = (g\ell,g\alpha)$. Then:

1. The forgetful map $\ell\mapsto\ell$ induces a well defined map of cusp sets
$$
\Phi_0\colon\{0\text{-cusps of }D(T_\Co)/R\}\longrightarrow\{0\text{-cusps of }F_{\En,2}\},
$$
sending the $R$-orbit of a primitive isotropic line $\ell\subset T_\Co$ to the $\gent$-orbit of $\ell$.
2. For Sterk's representative $e_k$ of the $k$-th $0$-cusp, the fibre $\Phi_0^{-1}([e_k])$ is canonically in bijection with the set of $\Stab_{\gent}(e_k)$-orbits of $(-2)$-vectors $\alpha\in\ten$ perpendicular to $e_k$.
3. Consequently there is a bijection
$$
\{0\text{-cusps of }D(T_\Co)/R\}\ \longleftrightarrow\ \gent\backslash\mathcal P_0,
$$
and, choosing one representative $e_k$ per Sterk cusp, a bijection onto the disjoint union
$$
\coprod_{k=1}^{5}\ \Stab_{\gent}(e_k)\backslash\{\alpha\in\ten : \alpha^2 = -2,\ \alpha\perp e_k\}.
$$
:::

::: {.proof}
$(1)$ A primitive isotropic line of $T_\Co$ is a primitive isotropic line of $\ten$ (@lem:primitivity-tco-in-ten), and restriction sends $\Stab_{\gent}(\delta)$ onto $R$ (@prop:gamma-co-images(3)), so the $\gent$-orbit of $\ell$ depends only on the $R$-orbit of $\ell$.

$(2)$ Let $\mathcal Y_k$ be the set of primitive isotropic lines $\ell\subset T_\Co$ with $[\ell]_{\gent} = [e_k]_{\gent}$, so that the fibre is the set $R\backslash\mathcal Y_k$ of $R$-orbits; and let $\tilde Y_k = \{\gamma\in\gent : \gamma e_k\perp\delta\}$, so that $\gamma\mapsto\gamma e_k$ is a surjection $\tilde Y_k\to\mathcal Y_k$ whose fibres are the cosets of $\Stab_{\gent}(e_k)$. Define
$$
\Psi_k\colon\tilde Y_k\longrightarrow L_k\definedas\{\alpha\in\ten : \alpha^2 = -2,\ \alpha\perp e_k\},\qquad \gamma\longmapsto \gamma^{-1}\delta .
$$
The target (@def:globular-boundary) is right: $(\gamma^{-1}\delta)\cdot e_k = \delta\cdot(\gamma e_k) = 0$ because $\gamma e_k\in T_\Co = \delta^{\perp}$, and $\delta^2 = -2$. The map is invariant under left multiplication by $\Stab_{\gent}(\delta)$, because $(r\gamma)^{-1}\delta = \gamma^{-1}r^{-1}\delta = \gamma^{-1}\delta$; and it is equivariant for right multiplication by $s\in\Stab_{\gent}(e_k)$, with $s e_k = \pm e_k$, acting on $L_k$ by $\alpha\mapsto s^{-1}\alpha$, which preserves $L_k$ because $(s^{-1}\alpha)\cdot e_k = \alpha\cdot(s e_k) = \pm\alpha\cdot e_k = 0$. It is surjective: for $\alpha\in L_k$, transitivity of $\gent$ on the $(-2)$-vectors of $\ten$ [@Ste91, 2.10] gives $\gamma\in\gent$ with $\gamma\alpha = \delta$, and then $\gamma e_k\perp\delta$ and $\Psi_k(\gamma) = \gamma^{-1}\delta = \alpha$. It is injective (@def:injective-map) on $\Stab_{\gent}(\delta)$-orbits: if $\gamma^{-1}\delta = \gamma'^{-1}\delta$ then $\gamma'\gamma^{-1}\delta = \delta$, so $\gamma'\gamma^{-1}\in\Stab_{\gent}(\delta)$ and $\gamma'$ lies in that stabilizer's orbit of $\gamma$. Hence $\Psi_k$ induces a bijection
$$
\Stab_{\gent}(\delta)\backslash\tilde Y_k/\Stab_{\gent}(e_k)\ \cong\ \Stab_{\gent}(e_k)\backslash L_k,
$$
and restriction identifies the left-hand side with $R\backslash\mathcal Y_k$, the fibre, because $R$ is the image of $\Stab_{\gent}(\delta)$ (@prop:gamma-co-images(3)).

$(3)$ The $0$-cusps of $F_{\En,2}$ are the $\gent$-orbits of primitive isotropic lines, and Sterk's five representatives exhaust them [@Ste91, (4.2.3)], so the cusp set of $F_{\En,2}$ is the disjoint union of the five orbits (@def:group-orbit) and (2) applies over each. For the second bijection, send the $R$-orbit of $\ell$ to the $\gent$-orbit of $(\ell,\delta)$, and the $\gent$-orbit of $(\ell,\alpha)$ to the $R$-orbit of $\gamma\ell$, where $\gamma\in\gent$ is any element with $\gamma\alpha = \delta$; that $\gamma\ell\subset T_\Co$ and that its $R$-orbit does not depend on $\gamma$ are the computations of (2), and the two assignments are inverse by construction.

## Finite discriminant-block lemma

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

## Spinor reflection input

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
