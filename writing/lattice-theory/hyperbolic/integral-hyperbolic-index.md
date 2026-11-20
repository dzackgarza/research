# Hyperbolic index and integral splitting {#sec-integral-hyperbolic-index}

Let $R$ be $\bZ$, $\bQ$, or $\bR$, and let $(L,b)$ be a finite free symmetric bilinear $R$-module. Write $q(x)=b(x,x)$. The hyperbolic plane $U_R$ has a basis $e,f$ with
$$
q(e)=q(f)=0,\qquad b(e,f)=1,\qquad
H=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$
The bilinear convention gives $q(x+y)=q(x)+2b(x,y)+q(y)$ [Conrad, *Bilinear Forms*, §§2, 6](https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf).

::: {.definition #def:integral-hyperbolic-index title="Integral hyperbolic index" defines="integral hyperbolic index"}

For an integral lattice $L$, its *integral hyperbolic index* is
$$
h_{\bZ}(L)=\max\{r\geq0:U_{\bZ}^{\perp r}\perp M\cong L\text{ for some }M\}.
$$
:::

Over $\bQ$ and $\bR$ the same formula defines $h_R(L)$; for a nondegenerate form it is the Witt index [Knebusch, *Specialization of Quadratic and Symmetric Bilinear Forms*, §2, Theorem 1](https://homepages.uni-regensburg.de/~knm22087/book.pdf). If $G$ is the Gram matrix in a selected basis, a constructive splitting is a Gram matrix $G_M$ and a matrix $P\in\mathrm{GL}_n(R)$ such that
$$
P^TGP=H^{\oplus h_R(L)}\oplus G_M. \tag{1}
$$
The columns of $P$ define the isometry $U_R^{\perp h_R(L)}\perp M\to L$. Over $\bZ$, $\det P=\pm1$ is essential.

::: {.proposition #prop:hyperbolic-index-base-change title="Indices under base change"}

For an integral lattice $L$,
$$
h_{\bZ}(L)\leq h_{\bQ}(L\otimes\bQ)\leq h_{\bR}(L\otimes\bR).
$$
If $L$ is nondegenerate of signature $(n_+,n_-)$, then
$$
h_{\bZ}(L)\leq i_W(L_{\bQ})\leq\min(n_+,n_-).
$$
:::

::: {.proof}

Tensor an orthogonal splitting with $\bQ$ and then $\bR$. The rational span of one isotropic vector in each integral hyperbolic plane is totally isotropic. A totally isotropic subspace of $L_{\bR}=V^+\perp V^-$ meets either definite summand trivially, so both projections from it are injective. Its dimension is at most $n_+$ and $n_-$. Nondegeneracy matters: a radical is totally isotropic but contributes no sign to the signature.
:::

## Radical reduction {#sec-hyperbolic-radical}

::: {.proposition #prop:hyperbolic-radical-reduction title="Radical reduction"}

Let $N=\operatorname{rad}(L)$. Over each of the three rings above, $N$ is saturated, $L/N$ is free and nondegenerate, and
$$L\cong N\perp(L/N),\qquad h_R(L)=h_R(L/N).$$
A splitting of $L/N$ lifts to a splitting of $L$ whose complement contains $N$.
:::

::: {.proof}

If $ax\in N$ for nonzero $a\in R$, then $ab(x,y)=0$ for every $y$, hence $x\in N$. The quotient is free because $R$ is a field or $\bZ$; choose a linear section. The radical is perpendicular to the section, proving the first decomposition. Its quotient form has zero radical. A hyperbolic summand of $L/N$ lifts along the section, and @prop:hyperbolic-summand-splits splits it in $L$. Conversely, the image of a hyperbolic summand in $L/N$ remains hyperbolic.
:::

The zero module has index zero; the empty basis change has determinant one.

## A specified summand and its complement {#sec-hyperbolic-summand}

::: {.proposition #prop:hyperbolic-summand-splits title="Splitting a hyperbolic summand"}

Suppose $e_1,f_1,\ldots,e_r,f_r\in L$ satisfy
$$b(e_i,e_j)=b(f_i,f_j)=0,\qquad b(e_i,f_j)=\delta_{ij}.$$
Let $S$ be their span. Then addition gives an isometry $S\perp S^\perp\xrightarrow{\sim}L$, with complementary projection
$$\pi_{S^\perp}(x)=x-\sum_{i=1}^r\bigl(b(x,f_i)e_i+b(x,e_i)f_i\bigr). \tag{2}$$
In particular an isometric integral embedding $U_{\bZ}^{\perp r}\to L$ has primitive image.
:::

::: {.proof}

Pairing (2) with any $e_j$ or $f_j$ gives zero. The difference $x-\pi_{S^\perp}(x)$ lies in $S$, and pairing an element of $S\cap S^\perp$ with $f_j$ and $e_j$ kills every coefficient. Thus $L=S\oplus S^\perp$, with vanishing cross pairing. The integral formula makes this a direct sum of integral modules, so the quotient by $S$ is free.
:::

In selected bases, let $X$ have the hyperbolic columns, $X^TGX=H^{\oplus r}$. A *full* basis $Y$ of $\ker_R(X^TG)$ gives
$$P=(X\mid Y),\qquad G_M=Y^TGY,\qquad P^TGP=H^{\oplus r}\oplus G_M. \tag{3}$$
Over $\bZ$, a Smith decomposition $W(X^TG)V=D$ provides the full integer kernel from the columns of unimodular $V$ corresponding to zero columns of $D$. Clearing denominators of a rational kernel basis may yield a proper sublattice. @prop:hyperbolic-summand-splits proves that $P$ is unimodular.

The specified inclusion $\iota_S:S\to L$ and complementary inclusion $\iota_M:M\to L$ induce the forward isometry. Its inverse is $x\mapsto(x-\pi_M(x),\pi_M(x))$. A chosen primitive integral embedding alone does not imply such a decomposition: $(1,1)$ in $\langle1,1\rangle$ is primitive, while it and its perpendicular $(1,-1)$ span index two.

## Integral hyperbolic pairs {#sec-integral-hyperbolic-pairs}

For $e\in L$, the *divisibility* $\operatorname{div}(e)$ is the positive generator of $b(e,L)$, equivalently the gcd of the entries of $Ge$. Suppose $q(e)=0$ and $\operatorname{div}(e)=1$. Bézout gives $v$ with $b(e,v)=1$; then
$$f=v-\frac{q(v)}2e,\qquad b(e,f)=1,\quad q(f)=0. \tag{4}$$
This is integral precisely when $q(v)$ is even. In an even lattice every such $e$ has a partner.

In an odd lattice, choose one Bézout solution $v_0$ and an integer basis $k_i$ of $\ker b(e,-)$. Every solution is $v_0+k$, and
$$q(v_0+k)\equiv q(v_0)+q(k)\pmod2.$$
The norm modulo two is additive, so an even-norm solution exists precisely when $q(v_0)$ is even or one of the $k_i$ has odd norm. The same calculation gives a partner of a supplied vector. It does not decide whether an unsupplied suitable $e$ exists.

## Maximality over the integers {#sec-integral-hyperbolic-algorithm}

The bounded searches of @sec-effective-integral-embedding-bounds give a finite existence decision for each $\operatorname{Emb}_{\bZ}(U^{\perp r},L)$ when the nondegenerate quotient has rank at least three. Search $r$ from the rational index down to one. At the first nonempty embedding space, take its map $j$, then form (3) from its images. If every space is empty, return the identity $L\to L$ as the index-zero splitting. Each search is finite, and @prop:hyperbolic-summand-splits turns a successful embedding into the required integral isometry. Searching in $L$ for every $r$ avoids an integral cancellation premise: a complement with no further $U$ need not certify that the first choice was maximal.

Rank zero and one have index zero. A nondegenerate rank-two integral form has index one exactly when it is even and has determinant $-1$. Necessity follows from $H$. Conversely, the determinant makes the binary form indefinite and rationally isotropic. Clear denominators of a rational zero and divide by its coordinate gcd to get a primitive integral isotropic $e$. Unimodularity makes $Ge$ primitive, and (4) supplies an integral partner.

For $L\cong U^{\perp r}\perp M$, the discriminant group of $L$ is that of $M$, so its minimum number of generators is at most $\operatorname{rank}(L)-2r$. If $2r=\operatorname{rank}(L)$, then $L$ is even. These are useful exclusions before an embedding decision; neither substitutes for a witness in the remaining cases.

Genus equality is not a general isometry decision. Peters's [*Primitive lattices*, Theorem 2.3](https://www-fourier.ujf-grenoble.fr/~peters/Articles/PrimLats.pdf) gives a uniqueness range for an indefinite lattice of rank $n$: discriminant length at most $n-2$ for even lattices and at most $n-3$ for odd lattices. Since $U^r$ is unimodular, a comparison with $U^r\perp M$ lies in that range when the lattice is even and $r\ge1$, or odd and $r\ge2$. The odd $r=1$ case requires an actual embedding or isometry decision.

::: {.example #ex:hyperbolic-indices title="Three base rings"}

For $\langle1,-2\rangle$, the indices over $(\bZ,\bQ,\bR)$ are $(0,0,1)$: $x^2=2y^2$ has no nonzero rational solution. For $2H$ they are $(0,1,1)$: $e=(1,0)^T$, $f=(0,1/2)^T$ form a rational hyperbolic pair, while every integral pairing is even. For $\langle1,-1\rangle$ they are also $(0,1,1)$: $e=(1,1)^T$, $f=(1/2,-1/2)^T$ form a rational pair, but the lattice is odd even though the integral $e$ has divisibility one. Finally $H\oplus2H$ has indices $(1,2,2)$; its displayed first plane splits integrally, and a second integral plane would force determinant one, whereas its determinant is four.
:::
