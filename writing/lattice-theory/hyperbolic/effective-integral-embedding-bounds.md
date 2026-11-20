# Effective bounds for integral embeddings {#sec-effective-integral-embedding-bounds}

Let $A\in\operatorname{Sym}_m(\bZ)$ and $G\in\operatorname{Sym}_n(\bZ)$ be nondegenerate Gram matrices in *selected* bases. An embedding has column matrix $X$ with $X^TGX=A$. Write $\|C\|_\infty=\max_{ij}|C_{ij}|$. A bound containing one representative in every target-isometry orbit suffices for the unconstrained existence problem. A bound containing **every** embedding also permits arbitrary decidable conditions on its coordinates.

## Definite targets {#sec-definite-embedding-bound}

::: {.proposition #prop:definite-coordinate-bound title="Definite square-fibre bound"}

Let $G$ be definite (@def:definiteness) of positive rank, choose $\sigma\in\{\pm1\}$ such that $P=\sigma G$ is positive definite (@def:definiteness), and put $t=\sigma a$. If $t<0$, the square-$a$ fibre is empty. If $t\ge0$, every $x\in\bZ^n$ with $x^TGx=a$ satisfies
$$
|x_i|\le\left\lfloor\sqrt{t(P^{-1})_{ii}}\right\rfloor
\le b_G(a):=\left\lfloor\sqrt{t\max_i(P^{-1})_{ii}}\right\rfloor.
$$
For rank zero put $b_G(a)=0$.
:::

::: {.proof}

In the positive inner product $\langle u,v\rangle_P=u^TPv$, one has $x_i=\langle P^{-1}e_i,x\rangle_P$. Cauchy–Schwarz gives
$$x_i^2\le\langle P^{-1}e_i,P^{-1}e_i\rangle_P\langle x,x\rangle_P
=t(P^{-1})_{ii}.$$
Take square roots and use the integrality of $x_i$.
:::

This dual-norm estimate sharpens the bounded-region argument for definite forms in [@Cas78, Chapter 9, §1].

For $m>0$ put $B=\max_j b_G(A_{jj})$. Every column of every embedding lies in $[-B,B]^n$, so the finite matrix box contains every embedding. Exact rational inversion and integer square root evaluate this bound. In the sheared form
$$G=\begin{pmatrix}1&N\\N&N^2+1\end{pmatrix},\quad N>0,$$
the vector $(-N,1)$ has square one and $b_G(1)=N$: a small bound after changing basis does not bound coordinates in the selected basis. For the zero source, the empty column family is the only candidate.

The same inequality proves finiteness of a definite norm shell. A maintained exact short-vector enumeration may replace the box, provided its returned signs and original coordinates are restored. In particular a count returned by floating-point short-vector code is not an exclusion proof. The nonzero minimum of a positive definite integral form lies between one and the least diagonal Gram entry; the finite bound therefore allows exact minimization. The negative definite convention can report the negative of the corresponding positive minimum, the square closest to zero.

For $G=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)$, the square-two shell is $\{\pm e_1,\pm e_2,\pm(e_1-e_2)\}$. Thus $\operatorname{Emb}_{\bZ}(\langle2\rangle,L)$ has six elements. Requiring a positive first target coordinate keeps $e_1$ and $e_1-e_2$, exactly two. This condition depends on the selected basis, so the example uses a box containing every embedding. For
$$G=2^{34}\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad a=2^{35},$$
the shell is $\{\pm e_1,\pm e_2,\pm(e_1+e_2)\}$, the shell at $a=1$ is empty, and the positive minimum is $2^{35}$. Negating $G$ gives closest-to-zero nonzero square $-2^{35}$.

## Rank at least three {#sec-higher-rank-embedding-bound}

Li–Margulis [@LM16b, Theorem 4] prove that, if $A=X_0^TGX_0$ for nondegenerate integral forms and $n\ge3$, some integral solution satisfies
$$
\|X\|_\infty<C_n|\det A|^{n^4}|\det G|^{n^3}
\|A\|_\infty^{n^3}\|G\|_\infty^{n^3}. \tag{1}
$$
For $A=H^{\oplus r}$ the first and third factors are one. Their displayed theorem leaves $C_n$ dimension-dependent. The proof makes it effective, but a numerical search requires an evaluated value or another explicit bound. The following construction obtains one from Calderón [@Cal23, Theorem 5.1 and Appendices A, B, F].

### Representative and completion bounds {#sec-integral-representative-bound}

For $n\ge3$ set
$$
\begin{aligned}
E_n&=(4n^3 6^n)^{n^2}(n^3+n),&
L_n&=2n^nE_n^{n-1},\\
R_n&=L_n^{n^2+1}+1,&
I(n,D)&=nR_n^2D,\\
F(n,D)&=2^{n(n-1)/2}D.
\end{aligned}
$$
Set $B(1,D)=D$, $B(2,D)=F(2,D)$ and
$$B(n,D)=\max\{F(n,D),I(n,D)\}\quad(n\ge3),\qquad K(n)=B(n,1).$$

::: {.proposition #prop:integral-representative-bound title="Bounded equivalent Gram matrix"}

If $G$ is nonsingular integral of rank $n\ge1$ and $D=|\det G|$, some $P\in\mathrm{GL}_n(\bZ)$ satisfies $\|P^TGP\|_\infty\le B(n,D)$.
:::

::: {.proof}

For a definite (@def:definiteness) form, negate if necessary and choose an LLL-reduced basis (@def:based-module) with parameter $3/4$. The reduced-basis inequalities [@LLL82, §1, conditions (1.4)–(1.5) and Proposition 1.6] give
$$\prod_i\|b_i\|^2\le2^{n(n-1)/2}D.$$
Every squared length is a positive integer, hence at least one; each is at most the product. Cauchy–Schwarz bounds every Gram entry by $F(n,D)$.

For an indefinite (@def:definiteness) form of rank at least three, Li–Margulis [@LM16b, §2.3, Lemma 13 and Appendix] give an explicit compact subset of unimodular Euclidean lattice space with minimum (@def:definite-minimum-shell) at least $E_n^{-1}$ meeting the relevant closed orthogonal orbit (@def:group-orbit). Minkowski's second theorem gives independent vectors of lengths less than $L_n$ [@Hen02, Theorem 1.3]. To see the bound, if the successive minima are $\lambda_i$, the unit-ball volume estimate gives $\prod\lambda_i\le n^{n/2}$, while every $\lambda_i\ge E_n^{-1}$.

The independent vectors generate a sublattice of index (@def:index) $d\le L_n^n$ by Hadamard. If $d>1$, reduce a vector from a nonzero quotient coset to $w=\sum c_iv_i$ with $|c_i|\le1/2$. Replace a $v_j$ for which $c_j\ne0$ by $w$. The new index is $|c_j|d\le d/2$, and the largest length grows by at most a factor $n$. After at most $\log_2d$ replacements these vectors form a basis. Since $n\le2^n$, their lengths are at most $L_nn^{\log_2d}\le L_nd^n\le L_n^{n^2+1}<R_n$. A column sign adjusts the determinant. In the normalized expression $G=D^{1/n}g^TJg$, each Gram coefficient at that orbit point is bounded by $nR_n^2D^{1/n}\le I(n,D)$.

For an indefinite binary isotropic (@def:orthogonal-complement) form, complete a primitive (@def:primitive-embedding) zero to a basis and reduce the other diagonal coefficient modulo twice the cross coefficient; its determinant is minus the cross coefficient squared, giving bound $D$. For an anisotropic binary form, choose a primitive $v$ minimizing $|q(v)|=|a|>0$, complete it to a basis and shift the other vector until $|b|\le|a|/2$. Minimality gives $|c|\ge|a|$. Since $ac=b^2-D$, the inequalities force $ac<0$, $a^2\le D-b^2$ and $|c|\le D$. Rank one has coefficient of absolute value $D$.
:::

The compact-subset step is a source-dependent estimate, not a bound on the change-of-basis matrix. In particular @prop:integral-representative-bound alone does not bound an embedding.

The sharper Li–Margulis representation constant in (1) remains a separate computation. Their §8.5 reduces Theorem 4 to Theorem 1 and Lemma 20; @prop:integral-completion-bound evaluates the latter's completion step. Their §6 reduces Theorem 1 to Theorems 5 and 6 and Lemma 1. Numerical values for Theorem 5 still require its injectivity-radius and bump-function estimates and Lemma 3(2)'s matrix-coefficient estimate, for which the paper points to Shalom, Theorem 2.1, and Kontorovich–Oh, Proposition 3.2 [@LM16b]. The evaluated Calderón route below avoids claiming a numerical value for that sharper chain.

::: {.proposition #prop:integral-completion-bound title="Completion preserving prescribed columns"}

Suppose $0<m<n$, $\tau^TG\tau=A$, and $a=|\det A|$, $D=|\det G|$, $k=n-m$. Let $d$ be the gcd of the maximal minors of $\tau$. There is an integral completion $\gamma=(\tau\mid\tau_1)$ with
$$
|\det\gamma|=d,\qquad
\|\gamma^TG\gamma\|_\infty
\le C:=K(k)a^kD+(m+1)^2\|A\|_\infty.
\tag{2}
$$
It is unimodular exactly when $\tau(\bZ^m)$ is primitive (@def:primitive-embedding).
:::

::: {.proof}

Hermite normal form completes $\tau$ to $\gamma_0$ with determinant of absolute value $d$. Cauchy–Binet shows $d\mid\det A$, so $d\le a$. Write
$$\gamma_0^TG\gamma_0=
\begin{pmatrix}A&c^T\\c&C_0\end{pmatrix},\qquad
E=C_0-cA^{-1}c^T,\qquad \lambda=\det A.$$
The matrix $\lambda E$ is integral and nonsingular, with
$$|\det(\lambda E)|=a^{k-1}d^2D\le a^{k+1}D.$$
Apply @prop:integral-representative-bound to $\lambda E$. The resulting $T\in\mathrm{GL}_k(\bZ)$ has $\|T^TET\|_\infty\le K(k)a^kD$. Choose $r\in\bZ^{k\times m}$ so that every entry of $s=r+T^TcA^{-1}$ has absolute value at most $1/2$. Then
$$\gamma=\gamma_0\begin{pmatrix}I_m&r^T\\0&T\end{pmatrix},\qquad
\gamma^TG\gamma=
\begin{pmatrix}A&As^T\\sA&T^TET+sAs^T\end{pmatrix}.$$
The cross entries are at most $m\|A\|_\infty/2$ and the last correction at most $m^2\|A\|_\infty/4$, both bounded by the second term in (2).
:::

For $m=0<n$, use $B(n,D)$ and a unimodular completion. The example $\tau=(2,0)^T$, $A=(4)$, $G=I_2$ has $d=2$ and a completion of Gram height at most $20$; no unimodular matrix can retain that first column.

### An evaluated equivalence bound {#sec-calderon-equivalence-bound}

Calderón's equivalence estimate [@Cal23, Theorem 5.1 and Appendix F] contains a spherical-function constant and a quotient-volume factor. The following explicit majorants use his Haar normalization:
$$\mathcal D_1\le9,\qquad \mathcal D\le15,\qquad
\operatorname{vol}X^1_{n,\infty}\le2^{2n^3+1}\quad(n\ge3). \tag{3}$$
For the first, his Appendix A integral becomes
$$\Xi_\infty(a_t)=\frac2\pi\int_0^{\pi/2}
(e^t\sin^2\theta+e^{-t}\cos^2\theta)^{-1/2}\,d\theta.$$
Split it at $e^{-t}$. On the first interval $\cos\theta\ge1/2$; on the second, $\sin\theta\ge2\theta/\pi$. Integration gives
$$\Xi_\infty(a_t)\le(t+3)e^{-t/2}\le9e^{-t/3},$$
and Appendix F permits $\mathcal D=5\sqrt{\mathcal D_1}=15$.
For the volume, use the Siegel set with $a_i/a_{i+1}\le2/\sqrt3$ and $|u_{ij}|\le1/2$ [@Cal23, Proposition 6.6]. In the tangent bases $E_{ij}-E_{ji}$, $E_{ii}-E_{nn}$ and $E_{ij}$ for the compact, diagonal and unipotent factors, the combined change of Lie basis has determinant of absolute value one. The Iwasawa density is $\prod_{i<j}a_i/a_j$. Set $b_i=a_i/a_{i+1}$. The diagonal Jacobian is $1/n$, and its integral is
$$\frac1n\prod_{i=1}^{n-1}\frac{(2/\sqrt3)^{i(n-i)}}{i(n-i)}\le2^{n^3}.$$
The unipotent box has volume one. Successive Riemannian submersions $SO(j)\to S^{j-1}$ give the orthogonal-group volume in the tangent normalization:
$$2\prod_{j=2}^n\operatorname{vol}S^{j-1}\le2^{n(n+1)+1}.$$
Here $\operatorname{vol}S^{j-1}=2\pi^{j/2}/\Gamma(j/2)\le4^j$. The covering set gives the last inequality of (3), since $n(n+1)\le n^3$.

For $n\ge3$ define the integers
$$
\begin{aligned}
r_n&=n(n+1)/2-1,\\
\overline M_n&=10^{n^2}n^{\lceil(n+2)^2/4\rceil},\\
\overline N_n&=3(3n^2n!)^{\lceil n(n-1)/4+1\rceil}\overline M_n,\\
\overline C_n&=12\,2^{3n^2(n-1)}n^2\,15^6\overline N_n^{12},\\
\overline V_n&=2^{2n^3+1},\\
\overline W_n&=2^{2n^6}
 (2^{2n^3+5}3^{4n^4}n^{6n^3+1})^{r_n}\overline V_n,\\
K_n&=2^{6n^3}n^{4n^3}(n!)^{2n^2+1}
      \overline C_n\overline W_n^6,\\
F_n(h,k)&=K_n(4hk)^{2n^3}.
\end{aligned}
\tag{4}
$$

::: {.proposition #prop:calderon-equivalence-bound title="Evaluated integral equivalence bound"}

If $G,J$ are integrally isometric nondegenerate (@def:polarization) integral matrices of rank $n\ge3$ with heights at most $h,k$, some $U\in\mathrm{GL}_n(\bZ)$ satisfies
$$U^TGU=J,\qquad \|U\|_\infty\le F_n(h,k).$$
:::

::: {.proof}

For indefinite (@def:definiteness) forms substitute (3) into Calderón's Appendix F constants and Theorem 5.1 with $S=\{\infty\}$ [@Cal23, Theorem 5.1 and Appendix F]. The factor $2^{2n^6}$ in (4) retains the closed-orbit volume factor without absorbing it into another constant. Replacing positive fractional exponents by their ceilings enlarges every bound, and polynomial coefficient height is at most twice matrix height. For definite (@def:definiteness) forms, negate both forms if needed. Each isometry column has square at most $k$; the inverse-Gram estimate bounds its coordinate square by $k(n-1)!h^{n-1}$, which is below $F_n(h,k)^2$.
:::

::: {.proposition #prop:integral-embedding-orbit-bound title="Bound in every embedding orbit"}

Let $0<m\le n$, $n\ge3$, $a=|\det A|$, $h=\|G\|_\infty$, and let $C$ be (2) when $m<n$, or $\|A\|_\infty$ when $m=n$. For each integral solution $X^TGX=A$, some $g\in O(G,\bZ)$ satisfies
$$
\|gX\|_\infty\le n a(n-1)!F_n(h,n^2C). \tag{5}
$$
The image of $X$ need not be primitive (@def:primitive-embedding).
:::

::: {.proof}

Complete $X$ to $\gamma$ as in @prop:integral-completion-bound; for $m=n$ take $\gamma=X$. Put $H=\gamma^TG\gamma$, $d=|\det\gamma|\le a$, and $P=\gamma^{-1}\bZ^n$. The lattice $dP$ has a column Hermite basis (@def:based-module) $B$ with entries at most $d$; $\beta=B/d$ is a basis of $P$ with $\|\beta\|_\infty\le1$ and $\beta^{-1}$ integral with entries bounded by $d(n-1)!$. Since $V=\gamma\beta$ is unimodular,
$$J=\beta^TH\beta=V^TGV,\qquad \|J\|_\infty\le n^2C.$$
Choose $U$ from @prop:calderon-equivalence-bound with $U^TGU=J$. If $E$ selects the first $m$ columns, $X'=U\beta^{-1}E$ is integral, has Gram matrix $A$, and obeys (5). Moreover $g=UV^{-1}\in O(G,\bZ)$ and $gX=X'$. This last identity proves the orbit (@def:group-orbit) assertion, not only existence of some bounded embedding.
:::

The bound (5) is vast but finite and fully evaluated. It does not make the box polynomial in input *bit length*. For $A=H^{\oplus r}$ it gives a complete integral hyperbolic-summand decision when combined with @prop:hyperbolic-summand-splits.

## Binary indefinite targets {#sec-binary-indefinite-embedding-bounds}

::: {.proposition #prop:split-binary-all-embedding-bound title="All embeddings in a split binary target"}

Let $G=\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)$ be integral, indefinite (@def:definiteness) and nondegenerate (@def:polarization), with $b^2-ac=s^2$ for an integer $s>0$. Let $A$ be a nondegenerate integral source (@def:globular-boundary) of rank one or two and $H_A=\max_{ij}|A_{ij}|$. Every integral $X$ with $X^TGX=A$ has entries bounded by $H_A$ when $a=c=0$, and by $2H_A\max(|a|,|b|,s)$ when $a\ne0$. If $a=0\ne c$, interchange target (@def:globular-boundary) coordinates first.
:::

::: {.proof}

For a column $(x_i,y_i)$ and $a\ne0$ put $u_i=ax_i+(b+s)y_i$, $v_i=ax_i+(b-s)y_i$. Then
$$u_iv_i=aA_{ii},\qquad u_iv_j+v_iu_j=2aA_{ij}.$$
A nonzero diagonal square bounds both nonzero integer factors by $|a|H_A$. If a diagonal square is zero, nondegeneracy of $A$ forces rank two and a nonzero off-diagonal pairing. Exactly one factor is nonzero, and the pairing bounds it by $2|a|H_A$. Invert:
$$y_i=(u_i-v_i)/(2s),\qquad
x_i=((b+s)v_i-(b-s)u_i)/(2as).$$
These give the stated bound. If $a=c=0$, use $2bx_iy_i=A_{ii}$ and $b(x_iy_j+y_ix_j)=A_{ij}$ in the same way.
:::

The source must be nondegenerate: multiples of an isotropic vector in $U$ make its zero-norm fibre unbounded. This binary bound contains every embedding, so a finite box also settles arbitrary decidable filters.

For $U(4)\to U$, the images $e\mapsto4e$, $f\mapsto f$ give a nonprimitive embedding inside the box. The same factor equations apply after a shear of the target basis, even when its displayed diagonal entries become large; the bound uses those displayed entries.

::: {.proposition #prop:nonsplit-binary-orbit-bound title="A norm-orbit bound in an anisotropic binary target"}

Let $G$ be indefinite (@def:definiteness) binary with nonsquare discriminant and let $A$ be nondegenerate (@def:polarization) integral of rank $m=1$ or $2$. Put $\alpha=A_{11}$ and $h=\|G\|_\infty$. If $\alpha=0$, no embedding exists. Otherwise let $v_1,\ldots,v_s$ be a finite transversal for vectors of square $\alpha$ modulo $O(G,\bZ)$, and put $V=\max_{k,i}|(v_k)_i|$, with $V=0$ for an empty transversal. Every embedding orbit (@def:group-orbit) meets the box of radius
$$B=V\quad(m=1),\qquad B=(|A_{12}|+2h|\det A|)V\quad(m=2).$$
:::

::: {.proof}

Move the first column of an embedding to a transversal vector $v$. In rank two write $\beta=A_{12}$, $\gamma=A_{22}$, $p=Gv$, $z=(-p_2,p_1)^T$. Then $v^TGz=0$, $z^TGz=(\det G)\alpha$, and the second column is $w=(\beta/\alpha)v+tz$. Its square imposes
$$t^2=\det A/((\det G)\alpha^2).$$
Since the determinants and $\alpha$ are nonzero integers, $|t|\le|\det A|$ and $\|z\|_\infty\le2hV$. These give the bound. An empty transversal excludes embeddings.
:::

The finite norm-orbit transversal can be computed by binary quadratic-form methods such as PARI's [qfbsolve](https://pari.math.u-bordeaux.fr/dochtml/html/Quadratic_number_fields_and_binary_quadratic_forms.html#qfbsolve), including imprimitive solutions. The theorem concerns orbit representatives, so a coordinate filter changed by an isometry needs another argument.

In $\langle1,-2\rangle$, the vectors $(1,0)$, $(0,1)$ and $(2,0)$ have squares $1,-2,4$. Square $3$ is impossible: modulo $8$, an even second coordinate would require $x^2\equiv3$, and an odd one would require $x^2\equiv5$. The identity is a rank-two embedding, while $U$ cannot embed because this target is anisotropic over $\bQ$.

## Conditions on embeddings {#sec-constrained-embedding-bounds}

::: {.proposition #prop:invariant-embedding-filter title="Finite search with an invariant condition"}

Let $P$ be a decidable predicate on $\operatorname{Emb}_{\bZ}(T,L)$ such that $P(g\circ j)=P(j)$ for all $g\in O(L,\bZ)$. In each nondegenerate (@def:polarization) regime above, the $P$-locus is empty if and only if its intersection with the corresponding finite orbit (@def:group-orbit) box is empty.
:::

::: {.proof}

An embedding satisfying $P$ moves into the box by a target (@def:globular-boundary) isometry. Invariance preserves $P$. The reverse implication is immediate. All entries in the box are integers, and the Gram equation and $P$ can be tested finitely.
:::

Primitivity is invariant: postcomposition by $g$ identifies the quotient modules $L/j(T)$ and $L/(g\circ j)(T)$. For $U(2)\to U$, the map $e\mapsto2e$, $f\mapsto f$ is an embedding of index two. Every embedding has index two because $(\det j)^2=\det U(2)/\det U=4$; hence the embedding space is nonempty but its primitive subspace is empty. A fixed-coordinate sign condition need not be invariant under $O(L,\bZ)$. Its emptiness does not follow from an orbit box.

An alternative finite procedure enumerates bounded Gram matrices for complements of ranks $n-2r$, determinant $(-1)^r\det G$, and signature $(p-r,q-r)$, then tests integral equivalence to $H^{\oplus r}\oplus K$. It needs an isometry witness, not merely an affirmative genus or equivalence label. Rank-one complements are fixed by their determinant and rank zero is empty. The direct embedding bounds avoid this intermediate enumeration.
