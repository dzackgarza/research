# Norm fibres and spaces of embeddings {#sec-norm-fibres-embedding-loci}

The splitting of @sec-integral-hyperbolic-index selects points of norm fibres and embedding spaces. Their definitions do not require that a solver exist. A point, an exhaustive enumeration and a decision that the space is empty are different data.

## The loci and their maps {#sec-hyperbolic-loci}

For a formed module $(L,b)$ and $a\in R$, the *norm fibre* is the equalizer
$$
q^{-1}(a)\longrightarrow L
\underset{a}{\overset{q}{\rightrightarrows}} R.
$$
It contains zero when $a=0$. The nonzero isotropic locus is $q^{-1}(0)\setminus\{0\}$. An undecided scalar equation does not destroy either locus or its inclusion. For a supplied $v$, the predicates $q(v)=0$, $b(v,w)=0$, and $q(v)=a$ are equations; the existential question whether some nonzero $v$ has a specified square is different. In particular a solver that returns a nonzero norm-zero vector has solved an isotropy problem, while the canonical zero proves the full zero fibre nonempty without solving it.

For nondegenerate finite free formed modules $T,L$ over the same ring,
$$
\operatorname{Emb}_R(T,L)=
\{j:T\to L\mid j\text{ linear and injective},\ b_L(jx,jy)=b_T(x,y)\}.
$$
In selected bases the equation is $X^TG_LX=G_T$. It implies injectivity under the nondegeneracy hypothesis: $Xx=0$ implies $G_Tx=0$ after scalar extension to the fraction field. An integral embedding need not be primitive; @prop:hyperbolic-summand-splits covers the special source $U^{\perp r}$. An element of $\operatorname{Emb}_R(T,L)$ is the map with its source, target and evaluation, rather than an image sublattice or an orbit class.

A fixed image condition is a fibre of an evaluation map. Other conditions, such as orthogonality to a specified submodule, integral image after rational extension, or primitive image, define intersections or predicate subspaces. The finite boxes of @sec-effective-integral-embedding-bounds are subspaces of this embedding space, with their inclusions into the original Hom-object. A quotient by the target orthogonal group is another construction.

For a specified $S\hookrightarrow L$, the perpendicular is the kernel of
$$
L\longrightarrow S^\vee,\qquad x\longmapsto(s\longmapsto b_L(x,s)).
$$
The kernel retains its inclusion into $L$. It exists even when $S$ is degenerate; an orthogonal direct sum requires a further hypothesis. Over $\bZ$, primitivity means torsion-free cokernel of the selected inclusion. For a vector $v$, test the arrow $R\to L$, $1\mapsto v$: testing only its image would incorrectly call the zero vector primitive, since the zero *submodule* is primitive.

## Field and integral existence {#sec-embedding-existence}

::: {.proposition #prop:field-embedding-witt-test title="Embedding criterion over a field"}

For nondegenerate (@def:polarization) finite-dimensional spaces $T,L$ over a field of characteristic (@def:two-elementary-isotropic-types) different from two,
$$
\operatorname{Emb}(T,L)\ne\varnothing
\quad\Longleftrightarrow\quad
i_W(L\perp(-T))\ge\dim T.
$$
:::

::: {.proof}

If $T$ embeds, split (@def:hyperbolic-plane) its nondegenerate image to write $L\cong T\perp M$. Then $T\perp(-T)$ is hyperbolic (@def:definiteness) of rank $2\dim T$, giving the inequality. Conversely Witt decomposition with at least $\dim T$ planes yields $L\perp(-T)\cong M\perp T\perp(-T)$. Witt cancellation of $-T$ gives $L\cong M\perp T$ [@OM00, §42E, 42:16].
:::

When source and target have equal dimension, an embedding is an isometry. The inverse map must be returned with the original endpoints. Over $\bQ$, an affirmative criterion followed by a complete rational enumeration yields a witness; over a real closed exact field, matching diagonal signs and square-root scalings gives one directly. For example $\langle1/4\rangle\cong\langle1\rangle$ over $\bQ$ by $v\mapsto e/2$, with inverse $e\mapsto2v$. The forms $\langle3\rangle$ and $\langle1\rangle$ become isometric over a real algebraic closure by $\sqrt3$, but not over $\bQ$. The rational form $\langle1,1\rangle$ represents $2$ but not $3$, whereas both are represented over a real algebraic closure.

For a concrete higher-dimensional algebraic-real embedding, $T$ with Gram matrix $\left(\begin{smallmatrix}3&1\\1&-2\end{smallmatrix}\right)$ has signature $(1,1)$ and embeds in $L=\langle1,2,-1\rangle$ of signature $(2,1)$. Diagonalize both forms, match one positive and one negative basis vector, scale by positive square roots of the ratios of their squares, and transport through the retained diagonalization maps. This specifies a map in the original source and target without enumerating algebraic-real vectors.

::: {.proposition #prop:integral-embedding-saturation title="Saturation reduction"}

For nondegenerate (@def:polarization) finite-rank integral lattices $T,L$,
$$
\operatorname{Emb}_{\bZ}(T,L)\ne\varnothing
\quad\Longleftrightarrow\quad
\text{some integral overlattice }T\subseteq T'\subseteq T^\vee
\text{ embeds primitively in }L.
$$
The family of such $T'$ is finite.
:::

::: {.proof}

For $j:T\to L$, put $P=j_{\bQ}(T_{\bQ})\cap L$. If a nonzero multiple of $x\in L$ lies in the rational image, then $x$ lies there, so $P$ is primitive (@def:primitive-embedding). Pull $P$ back through $j_{\bQ}$ to $T'$. Its form is integral because $P\subseteq L$, and $b(T',T)\subseteq\bZ$ gives $T'\subseteq T^\vee$. Conversely compose an overlattice (@def:overlattice) inclusion with a primitive embedding (@def:primitive-embedding) of $T'$. Since $T^\vee/T$ is finite, its subgroups give a finite list. Integrality is the vanishing of the discriminant bilinear pairing on the subgroup; evenness is a stronger condition and is not required here.
:::

For $U(4)\to U(2)$, $e\mapsto2e$ and $f\mapsto f$ gives an index-two embedding. It is neither primitive nor an isometry in equal rank, but its saturation is an integral overlattice. An odd $\langle1\rangle$ cannot embed in the even lattice $U(2)$. Classification by primitive embeddings of these finite overlattices supplies an unconstrained existence decision when its primitive-embedding decision applies. An extra condition on the original map may not survive passage to a class representative.

For nonzero $a\in\bZ$, an embedding $\langle a\rangle\to L$ is precisely a nonzero integral vector of square $a$. A positive decision can be evaluated on the source generator to obtain the vector. Local solvability alone does not provide it.

::: {.example #ex:borovoi-ternary-obstruction title="A ternary integral obstruction"}

Borovoi [@Bor00a, §2 and Example 0.1.1] studies
$$
G=\begin{pmatrix}-9&1&0\\1&7&0\\0&0&2\end{pmatrix},
\qquad q(x,y,z)=-9x^2+2xy+7y^2+2z^2.
$$
It represents $1$ over every completion but not over $\bZ$; $(0,0,1)$ has square $2$. The vector $(-1/2,1/2,1)$ is a $1$-representation at every odd prime. At $2$, $q(4,1,1)-1=-128$ and the derivative with respect to $z$ is $4$, so the strong Hensel inequality gives a $2$-adic solution.

For integral exclusion, suppose $q(x,y,z)=1$ and set $u=x-y$, $v=x+y$. Then
$$2z^2-1=u(u+8v).$$
Reduction of the original equation modulo two makes $x,y$ have opposite parity, hence $u,v$ are odd. Modulo eight the displayed equation forces $z$ odd. Modulo sixteen it gives $u^2\equiv9$, so $u\equiv\pm3\pmod8$. Some odd prime divisor $p$ of $u$ must then be $\pm3\pmod8$. But $2z^2\equiv1\pmod p$ makes $2$ a quadratic residue, which requires $p\equiv\pm1\pmod8$, a contradiction. Thus the integral norm-one fibre is empty.

Borovoi's example pairs this form with $\operatorname{diag}(-1,64,2)$ in the same genus; the latter represents one at $(1,0,1)$. The forms are inequivalent, and Eichler's theorem gives more than one spinor genus in this genus [@CS10, Ch. 15, Thm. 14 and eq. (51)]. The local tests therefore cannot decide the first integral embedding problem.
:::

## Enumeration, choice and emptiness {#sec-hyperbolic-enumeration}

A complete enumeration of a countable set reaches each member after finitely many steps; countability alone does not give such an enumeration. Exhausting finite integer boxes or rational-height sets gives a complete candidate enumeration for vectors and maps. A decidable filter preserves eventual discovery of each satisfying candidate, but an empty infinite filtered search need not terminate. If a predicate is only semidecidable, fair interleaving is needed to avoid waiting forever at one candidate.

There is no sequential enumeration of the entire real norm-zero locus in $U_{\bR}$: it contains the uncountable line $\bR e$. The equalizer and its inclusion still exist. A solver for a fibre may produce a point without enumerating the ambient space; its failure to produce a point is not an emptiness certificate. A known point immediately proves nonemptiness and can be retained for subsequent selection. The zero vector gives such a point for $q^{-1}(0)$. Over a definite integral lattice @prop:definite-coordinate-bound makes a norm fibre finite, and then exact exhaustion can decide it.

An infinite countable discrete set has no uniform probability measure assigning equal positive mass to every point. Continuous sampling from a real box likewise misses the norm-zero axes of $U_{\bR}$ with probability one. A finite embedding box does admit a uniform distribution, but unsuccessful samples never prove absence. Exact emptiness requires a theorem supplying a bound or a separate decision procedure.

For a split integral binary plane $U$, a nonzero square equation is $2xy=a$ and has finitely many integral solutions, indexed by divisors of $a/2$ when $a$ is even. Its zero fibre contains both isotropic axes and is infinite. A rank-zero norm fibre contains its sole zero point exactly at square zero. These are finite-fibre statements, not an enumeration of the whole real locus.

::: {.proposition #prop:arbitrary-embedding-filter-undecidable title="Undecidability of unrestricted filtered emptiness"}

There is no total emptiness algorithm for arbitrary decidable predicate subsets of $\operatorname{Emb}_{\bZ}(U,U\perp\langle2\rangle)$.
:::

::: {.proof}

Choose a basis (@def:based-module) $e,f,a$ of $L=U\perp\langle2\rangle$ with $b(e,f)=1$ and $q(a)=2$. For every $n\ge0$ define
$$j_n(e)=e,\qquad j_n(f)=f+na-n^2e.$$
The Gram equation makes each $j_n$ an embedding. Conversely, an embedding $j$ with $j(e)=e$ has $j(f)=xe+f+na$; its zero square forces $x=-n^2$. Restricting to nonnegative $a$-coordinate therefore selects precisely the $j_n$.

For any fixed program $C$, let $P_C(j_n)$ mean that $C$ halts within $n$ steps, and set $P_C$ false outside that coordinate locus. This predicate is decidable on each input map by a finite simulation. Its locus is nonempty if and only if $C$ halts. A uniform emptiness algorithm would decide the halting problem [@Tur37].
:::

This does not obstruct constructing the predicate subset, its inclusion, membership tests, or its complete countable enumeration. @prop:invariant-embedding-filter applies when the filter is invariant under target isometries. The predicates in this proof need not be invariant.

## Scalar extension and retained morphisms {#sec-hyperbolic-base-change-maps}

For a unital ring map $\varphi:R\to S$, extend a finite free formed module and its Gram matrix by applying $\varphi$ to the coefficients. Then
$$\det G_S=\varphi(\det G).$$
A unit determinant remains a unit under every such map. If $R,S$ are domains and $\varphi$ is injective, a nonzero determinant remains nonzero. Without injectivity, nondegeneracy may fail: $\langle2\rangle$ reduces to the zero form over $\bF_2$, while $U$ remains unimodular.

A formed morphism is a pair $(f,h)$ with $f:M\to N$, $h:R\to R$ linear, satisfying
$$h(b_M(x,y))=b_N(fx,fy).$$
Its scalar extension is $(f_S,h_S)$, where $f_S=1_S\otimes f$ and $h_S=1_S\otimes h$ under $S\otimes_RR\cong S$. The form equation holds on pure tensors, hence everywhere by bilinearity. Since $h(r)=rh(1)$, the extended value map is multiplication by $\varphi(h(1))$. On $\langle1\rangle$, $(x\mapsto2x,r\mapsto4r)$ extends with both components. It is not an isometry: a lattice isometry has value map the identity.

Scalar extension of a formed morphism does not always preserve injectivity. The embedding $\langle4\rangle\to\langle1\rangle$, $v\mapsto2e$, becomes zero over $\bF_2$. Flatness is a sufficient condition for preserving an embedding. By contrast an inverse pair extends to an inverse pair under every unital base change, so isometries retain their inverse maps.

For an exact-field linear map $f:V\to W$ with matrix $A$, a target $b$ has a preimage precisely when $\operatorname{rank}[A\mid b]=\operatorname{rank}A$. In the consistent case the solver must return a point of the *original* $V$. It need not decide whether each solved coefficient is zero before storing the coordinate vector. For the row $(1,t)$, $(-t,1)$ generates the kernel for every $t$, including a real scalar whose zero status is undecided. A full kernel with its inclusion, rather than a rationalized basis or its dimension alone, is what the perpendicular and splitting constructions use.

For the triangular map with columns $(1,0)$ and $(1,1)$, the target $(1+t,1)$ has preimage $(t,1)$. This remains a valid returned point when $t$ is represented by the regular Cauchy sequence $2^{-n}\to0$ and its zero status is undecided. The coordinate belongs to the original domain even if its storage cannot discard it as zero.

The orthogonal sum of nondegenerate forms is nondegenerate: a vector in its radical pairs to zero with each summand injection and hence has zero component in every summand. This includes the empty sum. Scaling a form by $s$ is always defined; symmetry persists. If multiplication by $s$ is injective on values, the radical stays zero. If $s$ is a unit, unimodularity also persists. Unknown zero or unit status withholds these conclusions but does not prevent constructing the scaled form.

## The output map {#sec-hyperbolic-output-map}

A maximal splitting returns an isometry
$$\phi:U_R^{\perp h_R(L)}\perp M\xrightarrow{\sim}L.$$
Its composites with the two summand inclusions are the selected embeddings in $L$; the projections from $L$ are the summand projections composed with $\phi^{-1}$. A Gram matrix or a complement's isometry class alone does not determine these maps. Over a field the complement is anisotropic by Witt decomposition. Over $\bZ$ a maximal complement can remain rationally isotropic, as $2U$ and $\langle1,-1\rangle$ show.

The mathematical operations in these chapters are the norm fibre, embedding space, scalar extension, kernel and orthogonal complement at their general owners. A computation may decide a particular emptiness question, find a point, or return an isometry only under its stated hypotheses. The existence of the locus does not confer any of those algorithms.

## Partner loci and affine equations {#sec-hyperbolic-partner-locus}

For a supplied isotropic vector $e$, the affine pairing fibre is
$$F_e=\{v\in L:b(e,v)=1\}.$$
Its *hyperbolic-partner locus* is the norm-zero fibre inside $F_e$,
$$\{f\in F_e:q(f)=0\}\longrightarrow F_e\longrightarrow L.$$
The locus exists before either fibre is decided nonempty. Over an exact field of characteristic different from two, a known nonzero isotropic $e$ in a nondegenerate space has a point: solve $b(e,v)=1$, then take $f=v-q(v)e/2$. Over $\bZ$ the Bézout and parity criterion of @sec-integral-hyperbolic-pairs states exactly when the same construction is integral. A solver may be retained with this locus and invoked only when a point is requested. An unavailable solver does not change the defining subset or its emptiness proposition.

The affine fibre of a linear map $f:V\to W$ over an exact field is nonempty exactly when its target lies in $\operatorname{im}(f)$. Once a base point $v_0$ is found, its full point set is $v_0+\ker f$, with the kernel inclusion retained in $V$. Over $\bZ$, a rational preimage is insufficient: multiplication by two on $\bZ$ has a rational preimage of one but no integral preimage.
