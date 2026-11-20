# Constructive splitting over the real and rational fields {#sec-constructive-real-rational-splitting}

The decomposition sought in @sec-integral-hyperbolic-index has different existence tests over $\bR$ and $\bQ$. Both return an isometry from the sum, rather than only its index or the Gram matrix of a complement.

## Real forms {#sec-real-hyperbolic-splitting}

::: {.theorem #thm:real-hyperbolic-index title="Real hyperbolic index"}

A real symmetric bilinear space of signature (@def:signature) $(p,q)$ has hyperbolic (@def:definiteness) index (@def:index) $\min(p,q)$. Its remaining nondegenerate (@def:polarization) summand is definite (@def:definiteness).
:::

::: {.proof}

Congruence diagonalization yields orthogonal vectors of nonzero square. Scale them to positive unit vectors $a_i$ and negative unit vectors $b_j$. For each opposite-sign pair put
$$e_i=(a_i+b_i)/\sqrt2,\qquad f_i=(a_i-b_i)/\sqrt2.$$
Then $q(e_i)=q(f_i)=0$ and $b(e_i,f_i)=1$. The unpaired unit vectors form a definite complement. Every hyperbolic plane (@def:hyperbolic-plane) contributes one positive and one negative square, so Sylvester's law of inertia excludes more planes [Conrad, *Bilinear Forms*, Theorem 6.19 and Corollary 6.20](https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf).
:::

A congruence is $S^TGS=D$, not a similarity. A nonzero diagonal pivot eliminates its row and column. If all remaining diagonal entries vanish but the matrix is nonzero, an off-diagonal entry $b(u,v)\ne0$ gives $q(u+v)=2b(u,v)\ne0$ and hence a pivot. Retaining every basis change gives the forward and inverse isometries. An alternative normalization uses $e=p+n$, $f=(p-n)/2$ for unit vectors $q(p)=1$, $q(n)=-1$. If $x=ap+bn$, then
$$x=\frac{a+b}{2}e+(a-b)f,$$
and the inverse coordinate change is $ue+vf=(u+v/2)p+(u-v/2)n$. These identities specify both maps even when the scalar presentation is lazy.

### Certified computable real input {#sec-certified-real-signature}

A computable real entry may be given by an effective rational sequence $a(n)$ with $|a(n)-x|\le2^{-n}$. A convenient stronger input hypothesis is
$$|a(m)-a(n)|\le2^{-n}\quad(m\ge n). \tag{1}$$
Completeness gives a limit $x$ satisfying $|x-a(n)|\le2^{-n}$. Conversely an approximation $c(n)$ with $|c(n)-x|\le2^{-n}$ yields such a regular sequence by $a(n)=c(n+1)$. A Cauchy sequence with a specified modulus can be resampled beyond that modulus. A finite prefix cannot certify (1). The sequence and its limit are a presentation of a real scalar; they do not create a new field or a decision of equality.

::: {.proposition #prop:certified-real-signature title="Signature from enclosures"}

Let $G$ be a symmetric real matrix with effective convergent rational enclosures for its entries, and suppose $\det G\ne0$. Then its signature (@def:signature) is computable without deciding equality of arbitrary real scalars.
:::

::: {.proof}

Choose symmetric rational midpoint matrices $A_n$ with entrywise error at most $2^{-n}$, and let $r$ be the size. Then $\|G-A_n\|_\infty\le e_n=r2^{-n}$. At a stage where $A_n$ is invertible, compute $K_n=\|A_n^{-1}\|_\infty$ exactly and stop when $K_ne_n<1$. For $0\le t\le1$,
$$A_n+t(G-A_n)=A_n\bigl(I+tA_n^{-1}(G-A_n)\bigr)$$
is invertible by the geometric series. Its inertia is constant along the path, so the rational inertia of $A_n$ is that of $G$. Since $G^{-1}$ exists, for large $n$ one has $\|A_n^{-1}\|_\infty\le2\|G^{-1}\|_\infty$, and $K_ne_n\to0$. Every stage uses rational decisions. Rank zero gives $(0,0)$.
:::

The same argument works with measured row-sum errors from outward-rounded ball endpoints. If midpoint and half-width are rational, take the maximum row sum of half-widths for $e$. The matrix and its inverse remain exact rational data. A fixed precision cutoff is not a singularity test.

For $x=\lim_n(1+2^{-n})=1$, the form $\operatorname{diag}(x,-1)$ has signature $(1,1)$. The positive matrix
$$\begin{pmatrix}1&\pi\\\pi&\pi^2+2^{-512}\end{pmatrix}$$
has determinant $2^{-512}$; its small positive eigenvalue calls for refinement, not a fixed precision rule. The off-diagonal plane $\left(\begin{smallmatrix}0&\pi\\\pi&0\end{smallmatrix}\right)$ has signature $(1,1)$ although both displayed diagonal entries vanish. Adding a zero radical line gives the singular form $\left(\begin{smallmatrix}0&\pi&0\\\pi&0&0\\0&0&0\end{smallmatrix}\right)$; the congruence construction still identifies its two nonzero signs when the scalar decisions are available.

::: {.proposition #prop:certified-real-diagonalization title="A diagonalizing isometry from a nonsingularity promise"}

Under the hypotheses of @prop:certified-real-signature, one can construct an orthogonal basis (@def:based-module) with nonzero squares, together with its inverse coordinate map, without a general real zero test.
:::

::: {.proof}

For a basis $u_1,\ldots,u_s$ of the remaining nonsingular space, inspect the finite family $u_i$ and $u_i+u_j$. At least one has nonzero square: otherwise polarization (@def:polarization-functors) makes every Gram entry zero. Refine the enclosures of all their squares until one excludes zero. Let that vector be $v$, put $d=q(v)\ne0$ and $s_j=b(v,u_j)$, and replace each remaining vector by
$$w_j=d u_j-s_jv.$$
These vectors lie in $v^\perp$. The column change has block matrix
$$E=\begin{pmatrix}1&-s^T\\0&dI\end{pmatrix},\qquad
E^{-1}=\begin{pmatrix}1&s^T/d\\0&d^{-1}I\end{pmatrix}.$$
Thus they form a basis, the perpendicular remains nonsingular, and the displayed inverse updates the coordinate map. Repeat in smaller dimension. Each selected denominator has already been proved nonzero by a separating enclosure. The resulting diagonalizing isometry and its inverse are expressed in the original endpoints; rank zero uses the empty inverse pair.
:::

For each nonzero diagonal square $d_i$, enclosure refinement eventually decides its sign. Put $r_i=\sqrt{|d_i|}$ and normalize $v_i/r_i$. Pair opposite signs as in the proof of @thm:real-hyperbolic-index. The inverse first applies the retained diagonalization inverse, then multiplies coordinates by $r_i$, then uses the displayed two-coordinate change. The forward map evaluates on the selected generators of the orthogonal sum. The coordinate identities prove both inverse composites.

For $\langle\pi,-1\rangle$, the vectors $p=\pi^{-1/2}e_1$ and $n=e_2$ have unit squares of opposite sign. Their hyperbolic combinations give a Witt isometry and inverse in the original real space. The positive square $\pi$ is represented by $e_1$; $\langle\pi\rangle$ embeds in $\langle1\rangle$ by multiplication by $\sqrt\pi$, and it cannot embed in $\langle-1\rangle$.

A prescribed nonzero norm $a$ is represented by $v_i\sqrt{a/d_i}$ when a diagonal square has its sign. If $a=0$, opposite signs give a nonzero isotropic vector. A definite form has no nonzero isotropic vector. The zero status of the requested $a$ is a separate hypothesis: a lazy presentation of zero need not have decidable equality. This distinction also applies to real embedding decisions. For nonsingular source and target, an embedding exists exactly when the source positive and negative indices do not exceed the target indices. Match diagonal basis vectors by sign and scale each by $\sqrt{a_i/b_{\sigma(i)}}$. For equal dimensions retain the reverse scaling and the two diagonalization maps to obtain the inverse isometry.

If singular computable forms were given a uniform index decision, it would decide whether a nonnegative computable real $a$ is zero: $\langle a,-1\rangle$ has index zero for $a=0$ and one for $a>0$. The nonsingularity promise is therefore a mathematical boundary of this computation. A stored fixed-precision number can be treated as an exact dyadic rational; it does not certify the signature of the unknown real it approximates.

## Rational forms {#sec-rational-hyperbolic-splitting}

::: {.theorem #thm:rational-hyperbolic-splitting title="Rational hyperbolic splitting"}

Exact (@def:exact-complex) isotropy decision and rational linear algebra construct an isometry
$$U_{\bQ}^{\perp w}\perp A\xrightarrow{\sim}L,$$
where $A$ is anisotropic and $w=h_{\bQ}(L)$.
:::

::: {.proof}

Work on the nondegenerate (@def:polarization) quotient if necessary. Decide whether the current complement has a nonzero isotropic (@def:orthogonal-complement) vector $e$. If so, solve $b(e,v)=1$ and put $f=v-q(v)e/2$. Then $q(f)=0$ and $b(e,f)=1$. Split (@def:hyperbolic-plane) the pair by @prop:hyperbolic-summand-splits and repeat on its nondegenerate complement. Each step removes two dimensions. The final complement is anisotropic by the exact stopping decision, and Witt decomposition makes the number of hyperbolic planes (@def:hyperbolic-plane) maximal (@def:maximal-lattice) [Knebusch, *Specialization of Quadratic and Symmetric Bilinear Forms*, §2, Theorem 1](https://homepages.uni-regensburg.de/~knm22087/book.pdf). Compose the retained basis (@def:based-module) maps to express the isometry in the original space.
:::

Hasse–Minkowski supplies a finite isotropy decision over $\bQ$ [Conrad, *The Local–Global Principle*, Theorem 3.3](https://kconrad.math.uconn.edu/blurbs/gradnumthy/localglobal.pdf). In dimension two, diagonalize and test whether $-b/a$ is a rational square. In dimension at least three, clear denominators to a nonsingular integral matrix $A$. The real test is indefiniteness. At primes not dividing $2\det A$, a nonzero zero modulo the prime exists in at least three variables and lifts. The remaining primes have the following finite test.

::: {.lemma #lem:rational-local-isotropy-test title="Finite local isotropy test"}

Let $\ell$ be prime, $c=v_\ell(\det A)+v_\ell(2)$ and $N=2c+1$. The form $x^TAx$ is isotropic (@def:orthogonal-complement) over $\bQ_\ell$ if and only if it has a zero modulo $\ell^N$ with at least one coordinate nonzero modulo $\ell$.
:::

::: {.proof}

A nonzero $\ell$-adic zero scales to a primitive (@def:primitive-embedding) integral one. Conversely let $x$ be a primitive residue solution. Some coordinate of $Ax$ has valuation at most $v_\ell(\det A)$: otherwise $\operatorname{adj}(A)Ax=(\det A)x$ contradicts primitivity. The corresponding derivative $2(Ax)_j$ has valuation $s\le c$. Since the value of the one-variable polynomial obtained by varying $x_j$ has valuation at least $N>2s$, the strong Hensel criterion gives a root congruent to $x_j$ modulo $\ell$. The vector stays primitive [Conrad, *Hensel's Lemma*, §4](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf).
:::

Each residue search is finite. After a positive decision, enumerate nonzero integral vectors by increasing maximum coordinate size; clearing denominators of a rational isotropic vector ensures this search eventually returns one. A solver such as Sage's [PARI-backed qfsolve](https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/qfsolve.html) can instead provide the vector. A returned isotropic subspace is not automatically maximal; the remaining complement must be proved anisotropic or a maximality guarantee must apply.

## Determinants of presented real matrices {#sec-cauchy-real-determinants}

The determinant polynomial can be evaluated on convergent enclosures even when zero status is undecided. At precision $p$, enclose each Gram entry by an outward-rounded ball. A division-free determinant calculation uses finitely many additions and multiplications, so induction on the expression shows that its output ball contains $\det G$. For fixed rank these polynomial operations are continuous; convergent input enclosures and vanishing rounding error give determinant enclosures of vanishing diameter. Taking rational midpoints at width at most $2^{-(n+1)}$ produces a regular Cauchy presentation of $\det G$, by the triangle-inequality argument after (1). This construction works for singular matrices. An enclosure containing zero is not an equality proof; only an exact zero enclosure may be dropped as a zero coefficient.

For example, let $z=\lim_n2^{-n}=0$ with its retained presentation. The determinant of $\operatorname{diag}(z,1,1,1)$ is the real number zero, although the chosen presentation may have no finite equality decision. If $x=\lim_n(1+2^{-n})=1$, the trace-zero form $\operatorname{diag}(x,-x,1,-1)$ has determinant $x^2=1$ and signature $(2,2)$. Its trace coefficient is zero even when direct comparison of the stored real presentations cannot decide that fact. Polynomial arithmetic on enclosing balls retains a coefficient whose ball merely contains zero; it discards only an exact zero ball. Neither determinant computation certifies a scalar zero relation unless the presentation supplies that separate decision.
