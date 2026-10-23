# Hyperbolic index and constructive hyperbolic splitting

This note gives exact algorithms for computing the largest orthogonal sum of
hyperbolic planes in a nondegenerate symmetric bilinear space over
$\mathbb R$ or $\mathbb Q$, or an integral lattice over $\mathbb Z$.
The output includes the complementary form and an explicit isometry.
The integral construction applies to both even and odd lattices.

## Conventions and the mathematical output

Let $R\in\{\mathbb R,\mathbb Q,\mathbb Z\}$, let $L$ be a finite free
$R$-module, and let $B:L\times L\to R$ be symmetric and nondegenerate.
For $R=\mathbb Z$, nondegenerate means that a Gram matrix has nonzero
determinant; unimodularity is not assumed. Write $q(x)=B(x,x)$, so that
$q(x+y)=q(x)+2B(x,y)+q(y)$.
These are the symmetric-bilinear-form conventions of [Conrad, §2 and §6](#references).

**Definition.** The hyperbolic plane $U_R$ has basis $e,f$ with
$B(e,e)=B(f,f)=0$ and $B(e,f)=1$. Its Gram matrix is
$H=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$.
Define

$$
h_R(L)=\max\{r\in\mathbb Z_{\ge0}: U_R^{\perp r}\perp M\simeq L
\text{ for some symmetric bilinear }R\text{-module }M\}.
$$

This fixes the meaning of **hyperbolic index** in this note. Over fields of
characteristic different from $2$, it is the Witt index
([Knebusch, §2, Theorem 1](#references)). Over $\mathbb Z$, the requirement
is an integral orthogonal direct summand isometric to $U_{\mathbb Z}$,
not merely a rational hyperbolic subspace or an isotropic sublattice.

Given a basis with Gram matrix $G$, the constructive problem is to return
$m=h_R(L)$, a symmetric matrix $G_M$, and $P\in\mathrm{GL}_n(R)$ with

$$
P^TGP=H_m\oplus G_M,\qquad H_m=H^{\oplus m}.                 \tag{1}
$$

The columns of $P$ define the isometry $U_R^{\perp m}\perp M\to L$.
Over $\mathbb Z$, $\det P=\pm1$ is essential: an invertible rational
matrix with integer columns would only specify a finite-index sublattice.
For a fixed integral $L$, base extension gives

$$
h_{\mathbb Z}(L)\le h_{\mathbb Q}(L\otimes\mathbb Q)
\le h_{\mathbb R}(L\otimes\mathbb R).                       \tag{2}
$$

Both inequalities follow by extending a splitting. The zero module has
index $0$, an empty change-of-basis matrix, and determinant $1$ by convention.
All remaining statements assume nondegeneracy. A degenerate form requires
a separate treatment of its radical.

## Splitting a given hyperbolic summand

The following calculation is valid over each of the three base rings.

**Proposition.** Suppose $e_1,f_1,\ldots,e_r,f_r\in L$ satisfy
$B(e_i,e_j)=B(f_i,f_j)=0$ and $B(e_i,f_j)=\delta_{ij}$.
Let $S$ be their span and $M=S^\perp$. Then the addition map
$S\perp M\to L$ is an isometry, with projection onto $M$ given by

$$
\pi_M(x)=x-\sum_{i=1}^r\bigl(B(x,f_i)e_i+B(x,e_i)f_i\bigr). \tag{3}
$$

**Proof.**

1. Pairing (3) with $e_j$ or $f_j$ gives zero, so $\pi_M(x)\in M$.
2. The difference $x-\pi_M(x)$ belongs to $S$, proving $L=S+M$.
3. If $s=\sum_i(a_i e_i+b_i f_i)\in M$, pairing with $f_j,e_j$
   gives $a_j=b_j=0$. Hence $S\cap M=0$.
4. The sum is orthogonal by the definition of $M$, proving the assertion.

In particular, every isometric embedding $U_{\mathbb Z}^{\perp r}\to L$
automatically has primitive image and splits. No independent primitivity
test is needed for this particular source lattice.

**Matrix construction.** Let $X$ have columns $e_1,f_1,\ldots,e_r,f_r$,
so $X^TGX=H_r$. Compute a basis matrix $Y$ for

$$
M=\ker_R(X^TG),\qquad P=(X\mid Y),\qquad G_M=Y^TGY.        \tag{4}
$$

Over a field, use exact linear algebra. Over $\mathbb Z$, use an integer
kernel computation, for example Smith normal form with transformations.
If $A=X^TG$ and $WAV=D$ is a Smith decomposition with unimodular $W,V$, the columns
of $V\in\mathrm{GL}_n(\mathbb Z)$ corresponding to zero columns of $D$
give a basis of the integer kernel. Arbitrarily clearing denominators in
a rational kernel basis need not give this full kernel. Proposition (3)
proves that the matrix $P$ in (4) is unimodular.

## Real forms: signature and an explicit basis

**Theorem.** If $L$ has signature $(p,q)$, with $p$ positive and $q$ negative
squares, then $h_{\mathbb R}(L)=\min(p,q)$.
This follows from Sylvester's law of inertia
([Conrad, Theorem 6.19 and Corollary 6.20](#references)).

**Construction and proof of maximality.**

1. Diagonalize by congruence, retaining the basis change:
   $S^TGS=\operatorname{diag}(d_1,\ldots,d_n)$ with every $d_i\ne0$.
   This is congruence, not similarity. A nonzero diagonal pivot eliminates
   its row and column. If all remaining diagonal entries vanish, a nonzero
   off-diagonal entry $B(u,v)$ gives $q(u+v)=2B(u,v)\ne0$ and hence a pivot.
2. Divide each diagonal basis vector by $\sqrt{|d_i|}$. This produces
   mutually orthogonal positive unit vectors $a_1,\ldots,a_p$ and
   negative unit vectors $b_1,\ldots,b_q$.
3. For $1\le i\le m=\min(p,q)$, set
   $e_i=(a_i+b_i)/\sqrt2$ and $f_i=(a_i-b_i)/\sqrt2$.
   Direct expansion gives $q(e_i)=q(f_i)=0$ and $B(e_i,f_i)=1$.
   Different pairs are orthogonal. Unpaired unit vectors form a basis of $M$.
4. Every hyperbolic plane contributes one positive and one negative square.
   Inertia therefore bounds the number by both $p$ and $q$. Step 3 attains
   this bound, proving maximality and (1).

**Exact real input.** Rational and real-algebraic coefficients support exact
arithmetic and sign decisions; positive square roots can be represented
algebraically. An exact ordered-field computation may similarly use sign
decisions and return the required real square-root extensions.

For computable real coefficients supplied with certified approximations and
the promise $\det G\ne0$, signature is also computable. To see this, refine
a rational symmetric approximation $A$ and an operator-norm error bound
$\|G-A\|\le\varepsilon$ until a certified lower bound for the absolute
values of all eigenvalues of $A$ exceeds $\varepsilon$. Such a stage exists
because $G$ is nonsingular. The straight path from $A$ to $G$ then remains
nonsingular, so its inertia is constant. This argument supplies a terminating
signature computation under the promise; it gives no uniform precision bound
near singularity. A diagonalizing basis can be computed with certified nonzero
pivots and represented by computable real expressions.

If singular computable inputs are allowed, a uniform index algorithm would
decide whether a computable $a\ge0$ is zero: the form
$\operatorname{diag}(a,-1)$ has index $0$ when $a=0$ and $1$ when $a>0$.
Such a zero decision is not generally computable. Fixed-precision `RR` data
also require an interpretation: stored binary numbers can be treated exactly
as dyadic rationals, but this does not establish the signature of unknown
real numbers they were intended to approximate.

## Rational forms: isotropy, construction, and maximality

**Theorem.** Rational isotropy decision and rational linear algebra compute
an explicit splitting (1) with $m=h_{\mathbb Q}(L)$.

**Algorithm.** Start with the whole space as the remaining complement.

1. Decide whether its form has a nonzero rational isotropic vector.
   If it is anisotropic, stop. Dimension zero or one is a stopping case.
2. Find such a vector $e$. Solve $B(e,v)=1$ by rational linear algebra;
   a solution exists by nondegeneracy. Set

   $$
   f=v-\frac{q(v)}2e.
   $$

   Then $B(e,f)=1$ and
   $q(f)=q(v)-q(v)B(v,e)+(q(v)^2/4)q(e)=0$.
3. Apply (4) to split off this plane. Repeat on its nondegenerate
   complement, composing the basis changes so the output remains expressed
   in the original basis of $L$.

**Proof of termination and maximality.**

1. Each successful iteration lowers dimension by two, so only finitely many
   iterations occur.
2. The final complement $M$ is anisotropic by the stopping decision.
3. The Witt decomposition theorem makes the dimension of the anisotropic
   part and the number of hyperbolic planes invariants of the original
   space. Thus the constructed number is maximal
   ([Knebusch, §2, Theorem 1](#references)).

### A terminating isotropy decision, including the local tests

Hasse–Minkowski states that a rational form is isotropic precisely when it is
isotropic over $\mathbb R$ and every $\mathbb Q_\ell$
([Conrad, *The local–global principle*, Theorem 3.3](#references)).
Here is a finite implementation in principle, independent of a particular CAS.

First diagonalize rationally. In dimension two, a diagonal form
$a x^2+b y^2$ is isotropic precisely when $-b/a$ is a rational square;
factor numerators and denominators to decide this. In dimension at least
three, clear a common denominator to obtain a nonsingular integral Gram
matrix $A$. The real test is indefiniteness. Only primes dividing
$2\det A$ need further examination: at every other prime, a nondegenerate
form in at least three variables has a nonzero zero over the residue field,
and this lifts by Hensel's lemma.

**Lemma (finite local test).** Fix a prime $\ell$, put
$c=v_\ell(\det A)+v_\ell(2)$ and $N=2c+1$.
The form $x^TAx$ is isotropic over $\mathbb Q_\ell$ if and only if there
exists $x\in(\mathbb Z/\ell^N\mathbb Z)^n$ with at least one coordinate
nonzero modulo $\ell$ and $x^TAx\equiv0\pmod{\ell^N}$.

**Proof.**

1. A nonzero $\ell$-adic isotropic vector can be scaled to a primitive
   vector in $\mathbb Z_\ell^n$. Its reduction gives the stated solution.
2. Conversely lift such a residue vector to an integer vector $x$.
   At least one entry of $Ax$ has valuation at most $v_\ell(\det A)$:
   otherwise $\operatorname{adj}(A)Ax=(\det A)x$ contradicts primitivity.
3. Choose an index $j$ at which the derivative
   $2(Ax)_j$ has valuation $s\le c$. Hold all other coordinates fixed
   and view $x^TAx$ as a polynomial in coordinate $j$. Its value has
   valuation at least $N>2s$.
4. The strong form of Hensel's lemma produces a zero differing in that
   coordinate by an element of valuation greater than $s$, hence divisible
   by $\ell$. The vector remains primitive and is therefore nonzero.
   This proves sufficiency. See [Conrad, *Hensel's lemma*, §4](#references).

The local searches are finite. If all tests succeed, Hasse–Minkowski
guarantees a rational isotropic vector. Enumerating nonzero integer vectors
by increasing maximum coordinate magnitude then finds one, since denominators
of a rational zero can be cleared. This is a terminating construction after
the affirmative decision, although it is not a competitive practical algorithm.

### Existing constructive software

[Sage's `qfsolve` documentation](https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/qfsolve.html)
describes its interface to PARI's implementation of Denis Simon's code for
rational quadratic equations. Its output distinguishes a solution from an
obstruction; a vector or a totally isotropic subspace still requires the
hyperbolic-pair completion and complement construction above.

[Magma's `IsotropicSubspace` documentation](https://docs.magma-maths.org/LatticesQuadraticForms/QuadraticForms/isotropic.html)
attributes its algorithm to Simon and states qualifications on maximality.
The dimension of an arbitrary returned isotropic subspace must therefore not
be substituted for an exact Witt-index computation without checking the
documented guarantee or proving the remaining complement anisotropic.
These are software references, not claims that this repository implements
either decomposition algorithm.

## Integral forms: a bounded constructive search

Integral splitting involves arithmetic beyond rational isotropy. There is,
nevertheless, a terminating exact algorithm returning both the maximal number
of planes and an integral basis. Effective representation bounds give a direct
construction without an integral cancellation assumption.

### Integral pairs and parity

For $e\in L$, its divisibility is the nonnegative generator of the ideal
$B(e,L)\subseteq\mathbb Z$; in coordinates it is the gcd of the entries
of $Ge$. If $q(e)=0$ and this divisibility is $1$, Bézout gives $v\in L$
with $B(e,v)=1$. The correction $f=v-q(v)e/2$ is integral whenever $q(v)$
is even. Thus, for an **even lattice**, finding an isotropic vector of
divisibility $1$ is equivalent to finding a copy of $U$ with that vector
as its first basis vector.

For a general integral lattice, the exact condition for a fixed isotropic
$e$ is the existence of an **even-norm** $v$ with $B(e,v)=1$.
This condition is necessary because a hyperbolic partner itself has norm zero,
and sufficient by the correction formula. Given one solution $v_0$, every
solution is $v_0+k$ with $k\in\ker B(e,-)$. Since
$q(v_0+k)\equiv q(v_0)+q(k)\pmod2$ and $q$ modulo $2$ is additive,
one can decide the condition using an integer kernel basis: either $q(v_0)$
is even, or some kernel basis vector has odd norm and can be added to it.

This constructs a pair for a supplied $e$. It does not bound a search for $e$
or establish that an arbitrarily chosen sequence of splittings is maximal.

### Effective search bounds for embeddings

Write $\|A\|_\infty=\max_{i,j}|A_{ij}|$.
Li–Margulis, **Theorem 4**, gives a representation bound for nonsingular
integral forms: if $A=T_0^TGT_0$, where $G$ has size $n\ge3$, then some
integral representation $A=T^TGT$ satisfies

$$
\|T\|_\infty<
C_n|\det A|^{n^4}|\det G|^{n^3}
\|A\|_\infty^{n^3}\|G\|_\infty^{n^3}.                    \tag{5}
$$

Here $C_n$ depends only on $n$; the theorem also treats primitive
representations. The paper's effective search bounds and their derivation,
not an unspecified numerical search limit, are the basis for termination.
For $A=H_r$, its determinant has absolute value $1$ and its maximum entry
magnitude is $1$, so (5) reduces to

$$
\|X\|_\infty< C_n|\det G|^{n^3}\|G\|_\infty^{n^3}.       \tag{6}
$$

The theorem leaves dimension-dependent constants in its displayed statement.
A numerical implementation of this bound must extract a valid effective
constant from the proof or use another explicit effective representation
bound. Choosing a convenient value for $C_n$ would not implement this algorithm.

**Algorithm for $n\ge3$.**

1. Compute $w=h_{\mathbb Q}(L\otimes\mathbb Q)$, an upper bound by (2).
   If $w=0$, return $m=0$, $M=L$, and $P=I_n$.
2. Obtain an effective integer bound $F(G)$ at least as large as the
   right-hand side of (6).
3. For $r=w,w-1,\ldots,1$, enumerate all
   $X\in\operatorname{Mat}_{n\times2r}(\mathbb Z)$ with
   $\|X\|_\infty\le F(G)$. Test the exact equation $X^TGX=H_r$.
4. At the first success, construct $Y$, $P$, and $G_M$ by (4), and return
   $m=r$ and the isometry (1). If every search fails, return the index-zero
   decomposition.

**Proof of termination, correctness, and maximality.**

1. Each matrix search has at most $(2F(G)+1)^{2rn}$ candidates, and there
   are at most $\lfloor n/2\rfloor$ searches. All comparisons are integer
   arithmetic. Thus the searches terminate.
2. A successful equation gives a hyperbolic embedding, which splits by
   Proposition (3). Formula (4) consequently returns a full integral basis.
3. Conversely, any splitting with $r$ planes supplies a representation
   of $H_r$. Bound (6) guarantees that the search finds a representation
   whenever one exists, even if the original embedding has large entries.
4. Every larger $r$ has been excluded before the first success, and $w$
   excludes all still larger values. Hence the returned $r$ is maximal.
   Complete failure proves $h_{\mathbb Z}(L)=0$.

The resulting $M$ need not be rationally anisotropic. Maximal integral
splitting says precisely that no larger integral splitting of the original
$L$ exists. The proof searches each $r$ in $L$ itself and does not appeal
to cancellation of integral summands.

**Ranks below three.** Rank zero or one has index zero. In rank two, the
index is one precisely when $G$ is even and $\det G=-1$.
Necessity follows from integral isometry to $H$.
For sufficiency, the negative determinant gives signature $(1,1)$, and
$-\det G=1$ makes the binary form rationally isotropic. Find a rational
zero, clear denominators, and divide by the coordinate gcd to get a primitive
integral isotropic $e$. Unimodularity makes $Ge$ primitive, hence gives
divisibility one. Evenness then gives an integral partner by the preceding
construction. The pair spans the whole rank-two lattice by Proposition (3).

### An alternative using possible complements

One may instead enumerate bounded representatives of possible complement
forms $K$ of rank $n-2r$, determinant $(-1)^r\det G$, and signature
$(p-r,q-r)$, and decide integral equivalence of $G$ with $H_r\oplus K$.
Li–Margulis **Corollary 1** gives a dimension-dependent bound on the entries
of an equivalent nonsingular integral form, and **§1.1** discusses effective
equivalence searches for all ranks at least two. Rank-one complements are
specified by their determinant; the rank-zero complement is the empty form.
The equivalence search must return the unimodular matrix, not just an
affirmative answer. The direct representation search avoids this intermediate
enumeration and its low-rank cases.

These exhaustive algorithms establish effective computability. Their bounds
do not establish a practical implementation or polynomial bit complexity:
even a bound polynomial in coefficient magnitude can entail an enormous
search in the binary input size.

### An explicit coefficient bound for integral form representatives

A coefficient bound for an equivalent form is different from the embedding
bound (5). The following bound is fully numeric and supplies the former.
It is deliberately large. It neither bounds the integral change of basis
nor supplies the still-required constant in (5).

Let $G$ be a nonsingular symmetric integral matrix of size $n\ge1$, and put
$D=|\det G|$. Define

$$
F(n,D)=2^{n(n-1)/2}D.
$$

For $n\ge3$ also define the integers

$$
\begin{aligned}
E_n&=(4n^3 6^n)^{n^2}(n^3+n),\\
L_n&=2n^nE_n^{n-1},\\
R_n&=L_n^{n^2+1}+1,\\
I(n,D)&=nR_n^2D.
\end{aligned}
$$

**Proposition.** Some $P\in\operatorname{GL}_n(\mathbb Z)$ satisfies
$\|P^TGP\|_\infty\le B(n,D)$, where

$$
B(n,D)=
\begin{cases}
D,&n=1,\\
F(2,D),&n=2,\\
\max\{F(n,D),I(n,D)\},&n\ge3.
\end{cases}
$$

For rank zero take the coefficient bound to be zero. The public computation
`Lattices(ZZ).integral_representative_coefficient_bound(n, D)` needs only
the invariants, so it can bound candidate complements before one has been
constructed. `L.integral_representative_coefficient_bound()` supplies the
invariants of an existing lattice. Both return an integer, not a
representative or an isometry. The bound is linear in $D$ for every fixed
rank. Its proof uses the upper inequality in Minkowski's second theorem
(Henk, Theorem 1.3, in the references) and
Li–Margulis's explicit compact subset in the Appendix, together with their
§2.3 and Lemma 13. No estimate from their matrix-coefficient or mixing
arguments is needed for this proposition.

**Basis estimate.** Suppose a Euclidean lattice $\Lambda$ of rank $n\ge1$
has covolume at least one and contains $n$ independent vectors of lengths
at most a real number $L\ge1$. Then it has a basis whose lengths are at
most $L^{n^2+1}$.

1. The given vectors generate a sublattice of index $d$. Hadamard's
   determinant inequality gives
   $d\le L^n/\operatorname{covol}(\Lambda)\le L^n$.
2. If their span is not all of $\Lambda$, choose a point in a nonzero coset
   of its quotient in $\Lambda$. Reducing its coefficients modulo integers
   gives a lattice vector $w=\sum c_iv_i$ with $|c_i|\le1/2$, not all zero.
3. Replace a $v_j$ with $c_j\ne0$ by $w$. The new vectors remain independent
   and their index is $|c_j|d\le d/2$. If their previous maximum length was
   $M$, their new maximum length is at most $nM$, by the triangle inequality.
4. The positive integer index can halve at most $k\le\log_2d$ times.
   Since $n\le2^n$, the final basis has lengths at most
   $Ln^k\le Ld^n\le L^{n^2+1}$.

To obtain independent vectors, write $v_n$ for the volume of the Euclidean
unit ball and $\lambda_i$ for the successive minima. Minkowski's second
theorem gives

$$
\prod_{i=1}^n\lambda_i\le
\frac{2^n}{v_n}\operatorname{covol}(\Lambda)
\le n^{n/2}\operatorname{covol}(\Lambda).
$$

The last inequality follows from the cube
$[-1/\sqrt n,1/\sqrt n]^n$ lying in the unit ball. If every nonzero lattice
vector has length at least $a>0$, then
$\lambda_n\le n^{n/2}\operatorname{covol}(\Lambda)a^{-(n-1)}$.
The successive minima are attained, so this bounds the lengths of $n$
independent lattice vectors.

**Definite forms.** Replace $G$ by $-G$ if necessary and choose an
LLL-reduced integral basis with parameter $3/4$. The reduced-basis
inequalities in Lenstra–Lenstra–Lovász, §1, imply

$$
\|b_i\|^2\le2^{i-1}\|b_i^*\|^2,\qquad
\prod_{i=1}^n\|b_i\|^2\le2^{n(n-1)/2}D.
$$

Here $b_i^*$ are the Gram–Schmidt vectors, whose squared lengths have
product $D$. Each $\|b_i\|^2$ is a positive integer, so it is at least one.
Every individual squared basis length is therefore at most the product
in the second inequality. Cauchy–Schwarz bounds every absolute Gram
coefficient by $F(n,D)$. This argument uses the standard reduced-basis
conditions (1.4)–(1.5) and Proposition 1.6 of that paper; no change-of-basis
bound is inferred from the length bound.

**Indefinite forms of rank at least three.** Li–Margulis's Appendix gives
$\epsilon_n=E_n^{-1}$ and a compact subset of the unimodular lattice space
consisting of lattices whose nonzero vectors have length at least
$\epsilon_n$. Lemma 13 ensures that it meets every closed orbit under the
relevant real orthogonal identity component. Their §2.3 associates such a
closed orbit to each integral indefinite form. A change of overall sign
allows the signature convention of their §2.2.

Normalize the form as $G=D^{1/n}g^TJg$, where $g\in\operatorname{SL}_n(\mathbb R)$
and $J$ is diagonal with entries $1$ and $-1$. At a point of the orbit in
the compact subset, the associated Euclidean lattice is unimodular and
has minimum length at least $E_n^{-1}$. The preceding minima inequality
supplies independent vectors of lengths at most
$n^{n/2}E_n^{n-1}<L_n$. The basis estimate, with a column sign reversed if
needed to give determinant one, supplies a representative matrix $g_1$
with $\|g_1\|_\infty<R_n$. Its lattice lies at the same orbit point, so
$D^{1/n}g_1^TJg_1$ is integrally equivalent to $G$. Each of its entries has
absolute value less than $nR_n^2D^{1/n}\le I(n,D)$, as required.

**Indefinite binary forms.** A sharper bound $D$ suffices. If the form is
isotropic, choose a primitive isotropic vector and complete it to a basis.
The Gram matrix is $\left(\begin{smallmatrix}0&b\\b&c\end{smallmatrix}\right)$.
Replacing the second basis vector by itself plus an integer multiple of
the first makes $|c|\le|b|$; since $D=b^2$, all entries have absolute value
at most $D$.

Otherwise choose a nonzero vector minimizing the positive integer $|q(v)|$.
It is primitive: dividing a nonprimitive vector by its content would
strictly lower that value. Complete it to a basis with Gram matrix
$\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)$ and shift the
second vector so that $|b|\le|a|/2$. Minimality gives $|c|\ge|a|>0$.
The equality $ac=b^2-D$ and the bound on $b$ force $ac<0$; otherwise
$b^2\ge a^2+D$ would contradict $b^2\le a^2/4$.
Consequently $a^2\le|ac|=D-b^2\le D$, and
$|c|=(D-b^2)/|a|\le D$. All entries are bounded by $D\le F(2,D)$.
Rank one has the original coefficient of absolute value $D$. This proves
the proposition in every stated rank.

**Remaining embedding-bound computation.** Li–Margulis §1.7 explicitly
states that its multiplicative constants are computable. Their §8.5 reduces
Theorem 4 to Theorem 1 and Lemma 20; the latter uses coefficient bounds for
an equivalent complement form. For indefinite forms their §6 reduces
Theorem 1 to Theorems 5 and 6 and Lemma 1. Theorem 5 still needs numerical
constants for its injectivity-radius and bump-function estimates and for
Lemma 3(2)'s matrix-coefficient estimate. The paper points to Shalom,
Theorem 2.1, and Kontorovich–Oh, Proposition 3.2, for that last evaluation.
The compactness constant above is therefore concrete progress on this
chain, not completion of the integral embedding bound.

## Examples separating the three base rings

**Example (a rational obstruction).** For
$G=\operatorname{diag}(1,-2)$, the real index is one. The equation
$x^2=2y^2$ has no nonzero rational solution, so both rational and integral
indices are zero.

**Example (divisibility).** For $G=2H$, the vectors
$e=(1,0)^T$ and $f=(0,1/2)^T$ form a rational hyperbolic pair. Thus the
rational and real indices are one. Every integral pairing is even, so
no integral pair has pairing one: the integral index is zero.

**Example (odd parity).** For $G=\operatorname{diag}(1,-1)$,
$e=(1,1)^T$ and $f=(1/2,-1/2)^T$ give a rational hyperbolic pair.
The primitive isotropic $e$ has divisibility one. But the lattice is odd,
whereas $U_{\mathbb Z}$ is even; their rank-two integral forms cannot be
isometric. The indices are again $(0,1,1)$ over
$(\mathbb Z,\mathbb Q,\mathbb R)$. In particular an integral complement
with index zero may still be rationally isotropic.

**Example (a maximal integral decomposition).** For
$G=H\oplus(2H)$, split off the displayed first plane. The integral index
is exactly one: if it were two, rank four would imply integral isometry
to $H_2$, but $\det G=4$ whereas $\det H_2=1$.
The rational and real indices are both two.

## Dependency index: mathematical operations and effective search

The algorithms use general operations on forms, modules, morphisms and sets.
The following index records their mathematical contracts and where they enter
the constructions. Method spellings are proposed notation for those contracts,
not assertions that methods with these names are implemented. This is a
dependency account, not an inventory of current code or formal declarations.

### Invariants, predicates, and decomposition morphisms

In this subsection $T$ is a nondegenerate symmetric bilinear module over
$R\in\{\mathbb Z,\mathbb Q,\mathbb R\}$; $V$ denotes a space over a field
$F\in\{\mathbb Q,\mathbb R\}$.

| Proposed operation | Mathematical result | Role in these algorithms |
| --- | --- | --- |
| `T.is_anisotropic()` | The truth value of $q(x)=0\Rightarrow x=0$ for every $x\in T$ | Exact stopping decision in rational Witt splitting; distinct from finding no zero in a partial search |
| `T.hyperbolic_index()` | $h_R(T)\in\mathbb Z_{\ge0}$ in the stated base ring | The requested invariant; integrally this is the $U$-summand index, with the special meaning fixed in this note |
| `T.maximal_hyperbolic_index_splitting()` | An isometry $\phi:U_R^{\perp m}\perp M\xrightarrow{\sim}T$, where $m=h_R(T)$ | The constructive result; its domain exposes $m$, $M$, and the two orthogonal summands |
| `V.witt_index()` | The maximal dimension of a totally isotropic subspace, equal to $h_F(V)$ | Field invariant; an upper bound for integral splitting after base change |
| `V.witt_decomposition()` | An isometry $\phi:U_F^{\perp w}\perp A\xrightarrow{\sim}V$ with $A$ anisotropic | Field construction; supplies the index and the complete basis change together |
| `T.base_change(S)` | The scalar extension $T_S=T\otimes_R S$ with its extended form, for a specified ring map $R\to S$ | Passes from integral to rational or real questions without identifying their answers |
| Real signature | $(p,q)$ for the chosen ordered real field | Computes the real index and the signs needed to construct the pairs |
| Nondegeneracy, evenness and unimodularity predicates | Respectively $\det G\ne0$, $q(T)\subseteq2\mathbb Z$, and $\det G\in\{1,-1\}$ in the applicable setting | Applicability, integral partner construction, and the binary case |

An isometry returned by either splitting operation must have its stated
source and target and support evaluation, inversion and composition. If
$\iota_U$ and $\iota_M$ are the inclusions into its domain, then
$\phi\iota_U$ and $\phi\iota_M$ are the actual embeddings into $T$.
The summand projections composed with $\phi^{-1}$ give the projections
from $T$. Thus the result includes the maps needed for subsequent mathematics;
a number, a Gram matrix, or an isomorphism class of $M$ alone is insufficient.

Over a field the two decomposition contracts above agree by Witt theory.
Over $\mathbb Z$ the complement of a maximal hyperbolic splitting can still
be isotropic. For integral forms, anisotropy of $T$ is equivalent to
anisotropy of $T\otimes\mathbb Q$: a rational zero can be multiplied by a
common denominator, and an integral zero remains a rational zero. It is
therefore strictly stronger than $h_{\mathbb Z}(T)=0$, as the examples
$2H$ and $\operatorname{diag}(1,-1)$ show.

The index and decomposition operations are outputs or reusable subcomputations,
not prerequisites that may call one another cyclically. A Witt decomposition
can supply its Witt index. The rational construction in this note instead
starts from isotropy decision and witness construction. The integral search
can use the rational index to prune candidates, but can also start at
$\lfloor\operatorname{rank}(T)/2\rfloor$; it does not require a rational
Witt decomposition merely to terminate.

### Norm fibres and spaces of embeddings

**Norm fibres.** For $a\in R$, `T.elements_of_norm(a)` denotes the set
$q^{-1}(a)$, with its inclusion into the set of elements of $T$. It includes
zero when $a=0$. The nonzero isotropic locus is
$q^{-1}(0)\setminus\{0\}$; selecting its elements must use this additional
condition. The norm fibre is meaningful over every stated base ring,
regardless of countability. Its set structure does not require a selected
enumeration or a decision procedure for every membership query.

**Isometric embeddings.** For a second nondegenerate formed module $L$ over
the same base ring, write

$$
\operatorname{Emb}_R(T,L)=
\{j:T\to L\text{ linear and injective}:
 B_L(jx,jy)=B_T(x,y)\text{ for all }x,y\in T\}.
$$

This is the subset of the set of linear maps defined by injectivity and
preservation of the form. With chosen bases, it is represented by
$X^TG_LX=G_T$. Under the present nondegeneracy hypotheses, this equation
already implies injectivity: $Xx=0$ implies $G_Tx=0$ over a field, or over
$\mathbb Q$ after extending an integral equation. A general integral
isometric embedding need not have primitive image. The special source
$T=U^{\perp r}$ makes primitivity and splitting automatic by (3).

An element is the map $j$ itself, not its image alone or its equivalence
class under an orthogonal-group action. Thus constructing and filtering
$\operatorname{Emb}_R(T,L)$ retains source, target and evaluation. Conditions
may specify images of given vectors, orthogonality to a given submodule,
integral image after rational base change, or primitive image. Fixed images
are fibres of evaluation maps; simultaneous conditions are intersections
of subsets. A quotient by a group action is a separate construction and
is not needed by the bounded search in this note.

For finite-dimensional nondegenerate spaces over a field of characteristic
different from two, there is also an emptiness criterion:

$$
\operatorname{Emb}_F(T,L)\ne\varnothing
\quad\Longleftrightarrow\quad
w(L\perp(-T))\ge\dim T.
$$

Here $-T$ means the same space with the negative form. To prove the forward
implication, split off the nondegenerate image of $T$. Then
$L\perp(-T)\simeq M\perp T\perp(-T)\simeq M\perp H^{\dim T}$.
Conversely write $L\perp(-T)\simeq A\perp H^w$ by Witt decomposition,
and put $r=\dim T$. If $w\ge r$, let $M=A\perp H^{w-r}$. Since
$T\perp(-T)\simeq H^r$, cancellation of $-T$ gives
$L\simeq M\perp T$, hence an embedding. These are consequences of
Witt decomposition and cancellation; see Knebusch, §2, in the references.
No assertion about integral embeddings follows from this field criterion.

The existing `Emb.is_empty()` computation now uses this criterion over
`QQ` and `AA`. For nondegenerate rational endpoints, an affirmative existence
decision followed by the complete rational iterator gives a terminating
witness construction. For example `diag(1,1)` represents `2` but does not
represent `3` over `QQ`, while it represents both over `AA`. The obstruction
at `3` for rational sums of two squares distinguishes the two fields despite
their identical real signatures.

For $T=U$, the same set is the subset of $L\times L$ defined by
$q(e)=q(f)=0$ and $B(e,f)=1$. For $U^{\perp r}$ it is the subset of the
finite product indexed by the specified hyperbolic basis satisfying all
pairing equations. This supplies the embedding-space interpretation of the
matrix search without making matrices the public mathematical result.

### Sets, enumeration, sampling, and search

These capabilities belong to general sets, maps and subsets, and can then be
used for norm fibres and embedding sets. Sage's distinction between
[sets](https://doc.sagemath.org/html/en/reference/categories/sage/categories/sets_cat.html),
[enumerated sets](https://doc.sagemath.org/html/en/reference/categories/sage/categories/enumerated_sets.html)
and [subsets defined by predicates](https://doc.sagemath.org/html/en/reference/sets/sage/sets/condition_set.html)
provides existing software terminology for this separation.

| General tool | Required mathematical or computational hypothesis | Use here |
| --- | --- | --- |
| Products, fibres, intersections and predicate-defined subsets | The input sets and defining maps or predicates | Norm fibres, affine solution sets and constrained embeddings |
| Exact membership or predicate decision | A terminating decision procedure on the supplied input presentation | Filters for norm, pairings, integrality, parity and bounded coordinates |
| Complete enumeration of a countable set | An effective enumeration that eventually reaches every element; abstract countability alone does not supply one | Searches over integer vectors, rational vectors or integral linear maps |
| Finite exhaustion by computable subsets | Finite enumerable subsets whose union is the whole set | Increasing coordinate boxes or rational-height bounds, each exhausted before advancing |
| Enumeration of a bounded finite subset | Specified bounds relative to a chosen basis or presentation | The finite integral embedding search, and the finite local congruence searches |
| A search for one satisfying element | A complete candidate procedure and decidable conditions, or a solver for the stated equations | Rational isotropic vectors and integral hyperbolic embeddings |
| Decision of emptiness | A terminating mathematical decision, not merely an element search | Rational anisotropy and rejection of each integral candidate rank |
| Sampling | A specified probability distribution and an effective sampling procedure | Optional acceleration for finding candidates, with no exclusion conclusion from failure |

Exhaustive sequential iteration cannot cover an uncountable set. For example,
the real norm-zero locus in $U_{\mathbb R}$ contains the whole line
$\mathbb R e$. Its norm fibre remains a set even though it has no exhaustive
iterator. A family parametrized by an uncountable set can describe all its
points; such a family is not an enumeration by successive natural-number
indices. Finite-dimensional real linear algebra supplies the pairs directly
and does not need to iterate over all real vectors.

For a countable candidate set with a decidable predicate, filtering a complete
enumeration eventually produces every satisfying element. However, asking for
the next element may never return when there are no further solutions.
If predicate evaluation is only a semidecision procedure, a sequential filter
can also remain forever on one candidate; fair interleaving of the individual
computations is then necessary to enumerate the affirmatively recognized
elements. Neither procedure decides emptiness in general.

Searches in this note have explicit termination reasons: rational witness
search starts only after existence is decided, and integral exclusion uses a
finite bound guaranteed to contain a solution whenever one exists. A time
budget expiring yields an unfinished search, not an empty set. An arbitrary
extra predicate on embeddings need not preserve either termination guarantee:
bound (6) guarantees a small representation of the form, not a small
representation satisfying additional conditions. A constrained finite search
needs a bound valid for those conditions or another complete solver.

Sampling must likewise state its distribution and its support. There is no
uniform probability distribution on a countably infinite discrete set giving
every point the same mass. Sampling vectors in a real box with a density
relative to area is also unsuitable for exact isotropy even in $U_{\mathbb R}$:
its zero locus is the union of two axes, each of area zero. Sampling on a
parametrization of the desired locus is a different operation. For software
over exact real presentations, the finitely describable outputs of a sampler
also need not exhaust the mathematical real locus. None of the exact
algorithms above requires a random sampler.

### Linear algebra, arithmetic, and retained maps

| General construction or computation | Output needed by the splitting algorithm |
| --- | --- |
| Symmetric bilinear forms, evaluation and restriction | The actual form on each module and submodule, with the associated norm map |
| Scalar extension along a specified ring map | Extended modules, forms and maps; the original integral lattice remains specified when testing integral image |
| Finite orthogonal sums and hyperbolic planes | The formed sum with its summand inclusions and projections; the rank-zero case is included |
| Linear maps and their composition, inversion and evaluation | Embeddings, isometries and composed changes of basis in the original module |
| Kernels, images, preimages and restrictions of linear maps | The submodule with its inclusion; its induced form, rather than just its dimension |
| Orthogonal complement of a specified embedding or submodule | The kernel of the pairing map to its module dual, with inclusion and restricted form |
| Orthogonal splitting of a supplied hyperbolic embedding | The isometry obtained from its inclusion and the complementary inclusion, whose inverse is $x\mapsto(x-\pi_M(x),\pi_M(x))$ with $\pi_M$ given by (3) |
| Exact linear solving, including affine solution sets | A solution of $B(e,v)=1$, or all solutions $v_0+\ker B(e,-)$ with their inclusion in the module |
| Congruence diagonalization retaining its isometry | Diagonal form and transport maps, for the real and rational routes |
| Integer kernel and linear-equation solving | A full integral kernel basis and Bézout solutions; Smith or Hermite computations retain their transformations |
| Divisibility, primitivity and parity | The ideal $B(e,L)$; primitivity of a submodule via torsion-freeness of the quotient; norm modulo $2$ |
| Exact scalar arithmetic, equality, sign and positive square roots where applicable | Valid pivots, normalization and equation comparisons in the chosen exact presentation |
| Rank and determinant | Dimension bounds and the determinant input to the integral representation bound |
| Integer factorization, valuations and rational-square decision | Bad primes, local precision, and binary rational isotropy |
| Finite residue rings, finite products and modular arithmetic | Complete finite local isotropy tests with primitive residue vectors |
| Effective representation bounds | A usable integer bound for the relevant form representation problem, with its hypotheses; (6) is the integral instance |
| Constructive integral equivalence and bounded representatives | The alternative complement-enumeration route only; a successful comparison returns the isometry |

For clarity, the orthogonal-complement row uses the map
$L\to S^\vee$, $x\mapsto(s\mapsto B(x,s))$, where $S\hookrightarrow L$
is the specified submodule and $S^\vee$ its module dual. Its kernel is
$S^\perp$. This construction exists even when $S$ is degenerate; the
direct-sum conclusion needs the additional hypotheses used in (3).
Over $\mathbb Z$, a primitive image means that the quotient module is
torsion-free, not just that one selected vector has coprime coordinates.
For a primitive vector, retain the map $R\to L$, $1\mapsto v$, and require
both injectivity and torsion-free cokernel. Testing only the inclusion of
its image loses injectivity: the zero submodule is primitive although the
zero vector over $\mathbb Z$ or a field is not primitive. The vector's
`is_primitive()` operation now delegates this map from the free module of
rank one to the general module-morphism operation.

### Which tools each construction actually needs

| Route | Required computation beyond the shared module, form and morphism constructions | Optional alternatives or accelerations |
| --- | --- | --- |
| Real splitting | Congruence diagonalization, sign and positive square-root operations, or certified real computations under the nonsingularity promise | Signature can be read from the diagonalization; no norm-fibre iterator is needed |
| Rational splitting | Exact isotropy decision and construction of one nonzero isotropic vector, rational affine solving and kernels | Local finite tests plus exhaustive witness search as proved here, or a maintained rational quadratic-equation solver |
| Integral bounded embedding search | A valid effective representation bound, finite candidate enumeration, exact pairing comparisons and full integer kernels | Rational Witt index for pruning; a maintained embedding solver with a complete existence decision can replace the box search |
| Integral splitting from a supplied isotropic vector | Divisibility and affine integral solving, parity on the kernel, hyperbolic-pair completion | Useful when such a vector is already known; does not on its own prove maximality |
| Integral complement enumeration | Bounded form representatives and constructive integral equivalence | An alternative to the direct embedding search, not an additional mandatory dependency |

Thus the reusable mathematical surface includes anisotropy, norm fibres,
embedding subsets and decomposition isometries, while each computation selects
the search or solver capabilities its hypotheses justify. No route requires
every set to be enumerable, and no predicate-defined set becomes decidable or
searchable solely because its defining mathematical expression exists.

## Mathematical identities and evidence boundaries

The constructive output obeys (1), with $\det P=\pm1$ integrally.
Its hyperbolic columns obey $X^TGX=H_m$, and its complementary columns
obey $X^TGY=0$. These identities establish a splitting, not its maximality.
Maximality follows from inertia over $\mathbb R$, anisotropy and Witt
decomposition over $\mathbb Q$, or the exhaustive effective exclusions
over $\mathbb Z$ proved here.

This note is mathematical exposition, not a declaration of a new runtime
API or a claim of completed formalization. In the architecture of
[INTENT.md](../../INTENT.md), definitions and theorems belong to
`lean-categories`; permanent mathematical acceptance assertions belong to
`lean-cas-dsl`. A computation's own assertions or account of its search
are not correctness evidence on the formal side.

## Using the reusable constructions

The dependency interfaces below retain mathematical objects and maps. Their
execution obligations remain open under the repository's source phase in
[TODO.md](../../TODO.md); these examples do not certify an implementation.
The target integral index and maximal-splitting computations are still separate
from these reusable constructions.

Scalar extension takes a specified ring morphism. For an integral lattice,
use its coefficient ring's fraction-field map:

```python
L = Lattices(ZZ)("U")
i = ZZ.fraction_field_map()
V = L.base_change(i)
phi = V.witt_decomposition()       # U_QQ^w orthogonal_sum A -> V
unit = V.base_change_unit()       # L -> restriction of V to ZZ
```

`V.base_change_source()` retains `L`, and `V.base_change_ring_map()` retains
`i`. The unit is a map of `ZZ`-modules into the restriction of scalars of
`V`; its values expose their original `V` elements by `underlying_element()`.
It must not be treated as an isometry between objects over one coefficient
ring. `phi` is an isometry over `QQ`, with evaluation and inverse. Over `AA`,
`witt_decomposition()` uses exact congruence diagonalization and positive
square roots; `diagonalization()` itself returns an isometry from the diagonal
space to the original space and also allows a degenerate form.

A finite orthogonal sum is constructed by
`Lattices(R).orthogonal_sum(factors)`. It carries the biproduct of the
underlying modules and the orthogonal form. Its injections and projections
retain that module decomposition; the projections need not preserve the form.
For example the first projection from `<1> orthogonal_sum <1>` kills the second
vector of square one. Consequently this construction does not supply
categorical lattice products or coproducts for form-preserving morphisms.

A supplied orthogonal summand embedding `j: T -> L` gives a splitting
without a search:

```python
phi = j.orthogonal_splitting()
```

The result is the isometry `T orthogonal_sum j.orthogonal_complement() -> L`.
It is assembled from `j` and the complement's inclusion, so its first factor
is the supplied source and its forward map on that factor is `j` itself.
The underlying module projections of `phi.domain()`, composed with
`phi.inverse()`, give the two projections from `L`. A nondegenerate source
suffices over a field; a unimodular source suffices over `ZZ`. A primitive
integral embedding alone does not suffice: the vector `(1,1)` in
`diag(1,1)` and its perpendicular `(1,-1)` span an index-two sublattice.
The inverse must exist over the original ring. Failure of integral
invertibility is not repaired by silently extending scalars.

For finite nondegenerate `AA` endpoints, embedding witnesses are constructed
directly:

```python
T = Lattices(AA)([[3, 1], [1, -2]])
V = Lattices(AA)([[1, 0, 0], [0, 2, 0], [0, 0, -1]])
j = T.Emb(V).an_element()
```

The existing diagonalization isometries give orthogonal bases of the two
spaces. Match each source basis vector of square $a$ with an unused target
basis vector of square $b$ of the same sign, and scale its image by
$\sqrt{a/b}$. This preserves each square and all cross pairings. Transport
back through the source diagonalization inverse to obtain the map on the
original source. There are enough target basis vectors exactly when its
positive and negative inertia dimensions dominate those of the source.
Otherwise the construction raises an empty-space error. This finite route
does not enumerate `AA` vectors and does not impose a coordinate bound.

Norm fibres are sets with their inclusions:

```python
null_vectors = L.elements_of_norm(ZZ(0))
nonzero_null_vectors = null_vectors.condition_set(lambda v: v != L.zero())
```

They include zero before the extra filter. In finite rank over `ZZ` or `QQ`,
the ambient coordinate iterator permits complete filtered searches. Over an
uncountable real base, the same fibre has membership and its inclusion
without acquiring an exhaustive sequential iterator. A next-element request
on an infinite filtered search may never return; it is not an emptiness test.

Exact real algebraic point construction also has direct operations:

```python
V = Lattices(AA)([[1, 0], [0, -2]])
e = V.isotropic_vector()
f = e.hyperbolic_partner()
v = V.representation_vector(AA(3))
p, n = V.positive_vector(), V.negative_vector()
```

These vectors belong to the original space. The partner satisfies
$B(e,f)=1$ and $B(f,f)=0$. For a scalar-valued symmetric bilinear form,
`representation_vector(a)` uses the square convention $B(v,v)=a$ and
requests a **nonzero** vector; at zero it is an isotropy request. In
contrast, `elements_of_norm(0)` includes the zero vector. Exact congruence
diagonalization gives a nonzero vector of square $a\ne0$ by choosing a
same-sign diagonal entry $d$ and multiplying its basis vector by
$\sqrt{a/d}$. A zero diagonal entry gives a radical isotropic vector;
a positive and a negative diagonal entry give an isotropic vector after
normalizing their squares to $1$ and $-1$. These square roots stay in `AA`.
The positive/negative-vector operations also apply to scalar-valued formed
modules with a finite framing, using the symmetric part for a bilinear
form's diagonal function. They return `None` when the requested sign is
excluded. This covers real algebraic coefficients, not arbitrary exact
real presentations.

For a terminating search within specified finite coordinates, retain the
coordinate subset and its inclusion, then construct the finite subset of
embedding maps:

```python
T = L.twist(ZZ(2))
coefficients = finite_ordered_set(tuple(ZZ(a) for a in range(-2, 3)))
box = L.coordinate_subset(coefficients)
bounded = T.Emb(L).with_generator_images_in(box.domain())
embeddings = bounded.domain()
j = embeddings.random_element()
```

Here the candidate box contains `2e,f`, so this particular finite embedding
set is nonempty. `box.inclusion()` maps its finite domain into `L`, while
`bounded.inclusion()` maps its finite domain into `T.Emb(L)`. Each member is
an actual form-preserving embedding, including a nonprimitive image such as
`U(2) -> U`. `embeddings.condition_set(predicate)` filters these maps; when
the predicate is decidable, the finite result can be exhausted. The selected
`random_element()` distribution is uniform on this finite set. An empty
support is rejected. This is neither uniform sampling on the whole lattice
nor sampling continuously in a real box.

A coordinate box alone supplies no global exclusion theorem. To conclude
that no embedding exists after exhausting it, its bound must be guaranteed
to contain a representative whenever one exists, including any additional
conditions. Without such a bound, `T.Emb(L)` iteration or `an_element()`
provides an exhaustive witness search over `ZZ` or `QQ` under the stated
finite-rank nondegeneracy hypotheses. For two nondegenerate rational
endpoints, the preceding Witt-index decision rejects the empty case before
`an_element()` starts its search. General integral exclusion still lacks
such a termination guarantee. The effective constant in (6) remains a required
computational dependency, not a caller-selected search limit.

The interfaces are defined at the [lattice owner](../../src/dzack_research/preamble/categories/lattices.py),
[embedding-space owner](../../src/dzack_research/preamble/categories/lattice_morphisms.py),
[finite free-module owner](../../src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py)
and [finite enumerated-set owner](../../src/dzack_research/preamble/categories/sets/finite_ordered_sets.py).
The [formed scalar-extension construction](../../src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py)
retains the original lattice and scalar map.

## References

- **Keith Conrad, *Bilinear forms*.**
  [Author's notes](https://kconrad.math.uconn.edu/blurbs/linmultialg/bilinearform.pdf).
  Sections 2 and 6 for symmetric bilinear forms and associated quadratic
  forms; Theorem 6.19 and Corollary 6.20 for real classification and inertia.
- **Manfred Knebusch, *Specialization of Quadratic and Symmetric Bilinear
  Forms*, translated by Thomas Unger, preliminary version, 22 November 2009.**
  [Author-hosted text](https://homepages.uni-regensburg.de/~knm22087/book.pdf).
  Section 2, Theorem 1: Witt decomposition and uniqueness of the anisotropic
  part; characteristic different from two identifies its plane blocks with $H$.
- **Keith Conrad, *The local–global principle*.**
  [Author's notes](https://kconrad.math.uconn.edu/blurbs/gradnumthy/localglobal.pdf).
  Theorem 3.3 and its discussion: Hasse–Minkowski and finite local reduction.
  The finite local precision bound in this note is derived explicitly above.
- **Keith Conrad, *Hensel's lemma*.**
  [Author's notes](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf).
  Section 4: the strong lifting criterion used for the finite local test.
- **Han Li and Gregory A. Margulis, *Effective estimates on integral
  quadratic forms: Masser's conjecture, generators of orthogonal groups,
  and bounds in reduction theory*.**
  [Author-hosted manuscript](https://li-han.weebly.com/uploads/5/1/3/3/51338781/equivalence.pdf).
  Theorem 4 for (5); Corollary 1 for bounded form representatives;
  §1.1 and Theorem 1 for constructive integral equivalence bounds.
  The integral decomposition algorithm here is a deduction from those
  bounds and Proposition (3), not a claim that the paper implements it.
- **A. K. Lenstra, H. W. Lenstra, Jr., and L. Lovász, *Factoring Polynomials
  with Rational Coefficients*, Math. Ann. 261 (1982), 515–534.**
  [Original paper, institutional copy](https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Lovasz/LovaszLenstraLenstrafactor.pdf).
  Section 1, conditions (1.4)–(1.5) and Proposition 1.6, for the reduced-basis
  inequalities used in the definite coefficient bound.
- **Martin Henk, *Successive Minima and Lattice Points*.**
  [Author's preprint on arXiv](https://arxiv.org/abs/math/0204158).
  Theorem 1.3 states the upper inequality of Minkowski's second theorem
  used in the explicit coefficient-bound derivation.
- **SageMath reference manual, *Solving quadratic equations*.**
  [Official documentation](https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/qfsolve.html).
  The `qfsolve` interface to PARI's Simon implementation.
- **Magma handbook, *Isotropic subspaces*.**
  [Official documentation](https://docs.magma-maths.org/LatticesQuadraticForms/QuadraticForms/isotropic.html).
  Algorithm attribution and the qualifications on maximality of returned
  isotropic subspaces. Software documentation consulted 23 October 2026.
