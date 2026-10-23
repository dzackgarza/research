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

**Current represented-real route.** This computation takes elements of
`RR` through their closed exact real expressions. The lattice operations
now reuse Sage's
[`rational_diagonal_form(return_matrix=True)`](https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/quadratic_form.html#sage.quadratic_forms.quadratic_form.QuadraticForm.rational_diagonal_form)
with `RR` coefficients in Sage's generic field arithmetic. Both retained
diagonalization and signature use the same private congruence supplier.
This is necessary already at pivot selection: Sage's generic algorithm
tests diagonal coefficients against zero and then off-diagonal coefficients
against zero before dividing by a pivot. These tests now call the `RR`
relation protocol instead of Python truth conversion of `SR` relations.
An undecided pivot comparison is refused by that protocol. No second
congruence algorithm is implemented; see
[Sage's computation](https://github.com/sagemath/sage/blob/develop/src/sage/quadratic_forms/quadratic_form__local_field_invariants.py).

Signature counts the resulting diagonal coefficients using that same
field's exact relation operation. An unresolved sign raises
`NotImplementedError`; it contributes
neither a positive, negative nor zero square. This avoids deriving an owned
real sign from Python truth conversion of a symbolic comparison.

The same existing diagonalization and positive-square-root constructions
now supply represented-real Witt index/decomposition, isotropic and
specified-norm witnesses, signed lattice vectors, and embeddings/isometries
with their original endpoints and inverses where applicable. This route
requires the represented arithmetic, congruence computation and comparisons
to succeed. It is not the certified-approximation algorithm of the preceding
paragraph, and it is not a total algorithm on all computable real oracles.
In particular, an unresolved equality needed by a pivot or a sign remains
a computation boundary. No exhaustive real iterator is introduced.

The pending off-diagonal specimen has Gram matrix
$\left(\begin{smallmatrix}0&\pi&0\\\pi&0&0\\0&0&0\end{smallmatrix}\right)$.
It forces the zero-diagonal pivot case and retains a radical line; its
inertia is $(1,1)$, and the returned diagonalization must satisfy its form
equation and both inverse composites in the original real space. This
complements the diagonal nonalgebraic specimen below. Both remain
unexecuted under DEV-58.

The nonalgebraic specimen below and its inverse/form assertions remain
unexecuted under DEV-58:

```python
p = RR.pi()
V = Lattices(RR)([[p, 0], [0, -1]])
assert V.witt_index() == ZZ(1) and V.is_anisotropic() is False
phi = V.witt_decomposition()
assert phi.codomain() is V
assert V.gram_tensor().pullback(phi) == phi.domain().gram_tensor()
assert all(phi(phi.inverse()(v)) == v for v in V.module_generators())
e = V.isotropic_vector()
assert e.parent() is V and V.q(e) == RR.zero()
f = e.hyperbolic_partner()
assert V.b(e, f) == RR.one() and V.q(f) == RR.zero()
assert V.q(V.representation_vector(p)) == p
assert V.q(V.positive_vector()) > RR.zero()
S = Lattices(RR)([[p]])
T = Lattices(RR)([[1]])
j = S.Emb(T).an_element()
assert j.domain() is S and j.codomain() is T
assert T.gram_tensor().pullback(j) == S.gram_tensor()
g = S.Isom(T).an_element()
assert all(g.inverse()(g(v)) == v for v in S.module_generators())
assert S.Emb(Lattices(RR)([[-1]])).is_empty() is True
```

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

#### Definite targets: a bound containing every embedding

**Proposition (coordinate bound for a definite square fibre).** Let
$G\in\operatorname{Sym}_n(\mathbb Z)$ be definite, $n>0$, and choose
$\sigma\in\{1,-1\}$ such that $P=\sigma G$ is positive definite.
For an integral square $a$, put $t=\sigma a$. If $t\ge0$, every
$x\in\mathbb Z^n$ with $x^TGx=a$ satisfies

$$
|x_i|\le\left\lfloor\sqrt{t(P^{-1})_{ii}}\right\rfloor
\le b_G(a):=
\left\lfloor\sqrt{t\max_i(P^{-1})_{ii}}\right\rfloor.
$$

If $t<0$ the fibre is empty; set $b_G(a)=0$. For the rank-zero
lattice set $b_G(a)=0$ for every $a$.

**Proof.** Assume $n>0$ and $x^TGx=a$; prove the coordinate bound.

1. **$t\ge0$.** Positive definiteness gives $x^TPx\ge0$, and
   $x^TPx=\sigma a=t$. Thus a negative $t$ admits no such $x$.
2. **$x_i=\langle P^{-1}e_i,x\rangle_P$.** Here
   $\langle u,v\rangle_P=u^TPv$, so this equality follows from
   symmetry of $P$ and $P^{-1}$.
3. **$x_i^2\le t(P^{-1})_{ii}$.** Cauchy–Schwarz for the positive
   inner product in step 2 gives
   $x_i^2\le\langle P^{-1}e_i,P^{-1}e_i\rangle_P
   \langle x,x\rangle_P=(P^{-1})_{ii}t$.
4. **Q.E.D.** Take square roots in step 3 and use the integrality of
   $x_i$. The maximum diagonal entry gives the uniform bound. In rank
   zero the only coordinate family is empty, so the assertion is vacuous.

`L.square_coordinate_bound(a)` evaluates this formula in the selected
framing. Exact rational matrix inversion and
$\operatorname{isqrt}(\lfloor t\max_i(P^{-1})_{ii}\rfloor)$ suffice;
there is no approximate square-root rounding. The maintained operations
are Sage's [rational matrix inverse](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_rational_dense.html)
and [integer square root](https://doc.sagemath.org/html/en/reference/rings_standard/sage/rings/integer.html#sage.rings.integer.Integer.isqrt).
This is the dual-norm Cauchy–Schwarz estimate for a definite form;
compare the bounded-region argument in Cassels, Chapter 9, §1.

The optimized definite square-shell computation delegates to Hecke's
[`short_vectors(L, a, a)`](https://github.com/thofma/Hecke.jl/blob/v0.39.22/src/QuadForm/ShortVectors.jl#L61).
Its bounds are inclusive and it returns nonzero vectors up to sign, in the
original lattice coordinates. The adapter restores both signs. The
[enumeration implementation](https://github.com/thofma/Hecke.jl/blob/v0.39.22/src/QuadForm/Enumeration.jl#L769)
uses rational pseudo-Cholesky arithmetic after Gram LLL reduction and
transports the resulting vectors back through the retained basis matrix.
This replaces the fixed-precision PARI `forqfvec` square-shell route;
it does not increase floating-point precision or infer completeness from
checking only the vectors returned. Zero and negative squares retain their
separate definite-form cases. Reflective roots are filtered by the exact
condition $a\mid 2(Gv)_i$ for every coordinate $i$.

The nonzero minimum uses the same maintained rational enumeration through
Hecke's [`minimum`](https://github.com/thofma/Hecke.jl/blob/v0.39.22/src/QuadForm/ShortVectors.jl#L134).
For a positive definite integral Gram matrix $P$ of positive rank,
$0<\mu\le\min_iP_{ii}$, since every basis vector is nonzero.
There are finitely many integral vectors below this upper bound, by the
coordinate estimate above, and the least nonzero square in this finite
set is the global minimum. Hecke applies this argument after Gram LLL
reduction; it does not decide the absence of vectors from floating-point
PARI `qfminim` counts. For a negative definite form the existing public
`minimum()` convention returns the negative of this positive minimum:
it is the square closest to zero, not a lower bound for all squares.
The zero lattice has no nonzero square and raises `ValueError`.

A distinguishing pending specimen is $G=2^{34}
\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)$,
$a=2^{35}$: the shell consists of $\pm e_1$, $\pm e_2$ and
$\pm(e_1+e_2)$. The original PARI route raises its recorded precision
error on this input. Verify both signs, the original coordinates, the
empty shell at $a=1$, minimum $2^{35}$, and the corresponding negative
definite form with returned square $-2^{35}$. Include the rank-zero
minimum exception.
These provider and shell specimens remain unexecuted under DEV-58.

For a source Gram matrix $A$ of rank $m>0$, let
$b=\max_j b_G(A_{jj})$. Every integral embedding $X$ with
$X^TGX=A$ has $|X_{ij}|\le b$, since each column has square $A_{jj}$.
Consequently the finite coordinate box contains **every** embedding,
including every embedding satisfying any extra predicate. A decidable
predicate can therefore be excluded by finite exhaustion in this case.
For a zero source the only embedding is the empty column family.

For example the following exhausts a constrained embedding set, retaining
the original source and target maps. These specimens remain unexecuted
under DEV-58.

```python
L = Lattices(ZZ)([[2, 1], [1, 2]])
T = Lattices(ZZ)([[2]])
b = L.square_coordinate_bound(2)
C = finite_ordered_set(ZZ(i) for i in range(-int(b), int(b) + 1))
box = L.coordinate_subset(C)
bounded = T.Emb(L).with_generator_images_in(box.domain())
all_embeddings = bounded.domain()
assert all_embeddings.cardinality() == cardinal(6)
v = T.module_generators()[0]
label = L.module_generating_set()[0]
positive = all_embeddings.condition_set(lambda j: j(v).to_vector()(label) > 0)
assert positive.cardinality() == cardinal(2)
assert all(j.domain() is T and j.codomain() is L for j in positive)
```

For a sheared Gram matrix $G=\left(\begin{smallmatrix}1&N\\N&N^2+1\end{smallmatrix}\right)$,
$b_G(1)=N$ for positive integral $N$: the vector $(-N,1)$ has square
one. This shows why a bound in the original framing must depend on that
framing. A small coefficient bound for an equivalent form cannot replace it.
The same coordinate inequality over $\mathbb Q$ or $\mathbb R$ does
not make the box finite; the finite search here uses integral coordinates.

#### General indefinite targets

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
The fully evaluated alternative (7) below now supplies such a bound, using
Calderón's later equivalence estimates and the completion construction.

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
nor supplies the constant needed to evaluate the direct matrix bound (5).

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

### An explicit coefficient bound for integral completions

The following evaluates the constant in Li–Margulis, Lemma 20. It fixes
the columns of a supplied embedding, including a nonprimitive embedding.
Write $\|C\|_\infty=\max_{i,j}|C_{ij}|$ and let $K(k)=B(k,1)$,
where $B$ is the representative bound proved in the preceding section.
Thus $B(k,D)=K(k)D$ for $k\ge1$ and positive integral $D$.

**Proposition (completion bound).** Let $A\in\operatorname{Sym}_m(\mathbb Z)$
and $G\in\operatorname{Sym}_n(\mathbb Z)$ be nonsingular, with $0<m<n$.
Put $k=n-m$, $a=|\det A|$ and $D=|\det G|$. For every
$\tau\in\mathbb Z^{n\times m}$ with $\tau^TG\tau=A$, there is
$\gamma=(\tau\mid\tau_1)\in\mathbb Z^{n\times n}$ such that

$$
|\det\gamma|=d,\qquad
\|\gamma^TG\gamma\|_\infty
\le K(k)a^kD+(m+1)^2\|A\|_\infty,
$$

where $d>0$ is the gcd of the maximal minors of $\tau$.
In particular $\gamma$ is unimodular exactly when the image of $\tau$
is primitive. For $m=0<n$, use $B(n,D)$ and a unimodular $\gamma$.

**Proof.** Assume the stated nonsingularity and representation equation;
prove the existence of the stated completion.

1. **Choose a completion $\gamma_0=(\tau\mid\tau')$ with
   $|\det\gamma_0|=d$ and $d\le a$.** The representation equation
   gives rank $m$ to $\tau$. Hermite normal form completes its image
   to a full-rank submodule of index $d$ (Li–Margulis, Lemma 19).
   Cauchy–Binet applied to $(\tau^TG)\tau$ shows that $d$ divides
   $\det A$, proving the inequality.

2. **The Schur complement has an integral multiple with controlled
   determinant.** Write
   $\gamma_0^TG\gamma_0=\left(\begin{smallmatrix}A&c^T\\c&C\end{smallmatrix}\right)$,
   $\lambda=\det A$, and $E=C-cA^{-1}c^T$.
   The adjugate formula shows $\lambda E$ is integral; it is symmetric
   and nonsingular. The block determinant identity gives
   $|\det E|=d^2D/a$, hence
   $|\det(\lambda E)|=a^{k-1}d^2D\le a^{k+1}D$.
   Integrality is asserted for $\lambda E$, not for $E$.

3. **Choose $T\in\operatorname{GL}_k(\mathbb Z)$ with
   $\|T^TET\|_\infty\le K(k)a^kD$.** Apply the preceding
   representative proposition to the integral form $\lambda E$ and
   divide its coefficient bound by $a$. This uses the linear dependence
   of $B(k,D)$ on $D$, together with step 2.

4. **Choose $r\in\mathbb Z^{k\times m}$ so that
   $s=r+T^TcA^{-1}$ has every entry of absolute value at most $1/2$.**
   Round each entry of $-T^TcA^{-1}$ to a nearest integer. Define
   $\gamma=\gamma_0\left(\begin{smallmatrix}I_m&r^T\\0&T\end{smallmatrix}\right)$.
   Its first $m$ columns are exactly $\tau$ and its determinant has
   absolute value $d$, because the second factor is unimodular.

5. **Bound the transformed Gram matrix.** Block multiplication gives

   $$
   \gamma^TG\gamma=
   \begin{pmatrix}A&As^T\\sA&T^TET+sAs^T\end{pmatrix}.
   $$

   Each cross coefficient is bounded by $m\|A\|_\infty/2$.
   Each coefficient of $sAs^T$ is bounded by
   $m^2\|A\|_\infty/4$. Step 3 bounds the remaining lower block.
   Since $(m+1)^2\ge\max(1,m/2,m^2/4)$, the proposed bound
   controls every block.

6. **Q.E.D.** Steps 1–5 give the required completion for $m>0$.
   For $m=0$, the preceding representative proposition gives a
   unimodular completion of the empty column family and bound $B(n,D)$.

The computation `T.integral_completion_coefficient_bound(n, det_G)`
uses the source's selected Gram matrix and only the target invariants.
It does not require constructing an embedding first. Neither this scalar
bound nor the proposition bounds the entries of $\tau$ or $\gamma$.
For example, the embedding $\tau=(2,0)^T$ from $A=(4)$ into $G=I_2$
has $d=2$; $\gamma=\operatorname{diag}(2,1)$ is a completion, but
no unimodular completion preserves that first column. The computed
coefficient bound is $1\cdot4\cdot1+4\cdot4=20$.

**Remaining embedding-bound computation.** Li–Margulis §1.7 explicitly
states that its multiplicative constants are computable. Their §8.5 reduces
Theorem 4 to Theorem 1 and Lemma 20; the latter now has the explicit
completion coefficient bound above. For indefinite forms their §6 reduces
Theorem 1 to Theorems 5 and 6 and Lemma 1. Theorem 5 still needs numerical
constants for its injectivity-radius and bump-function estimates and for
Lemma 3(2)'s matrix-coefficient estimate. The paper points to Shalom,
Theorem 2.1, and Kontorovich–Oh, Proposition 3.2, for that last evaluation.
The compactness constant above is therefore progress on this sharper
Li–Margulis chain. The alternative evaluated embedding bound follows below.

### A fully evaluated alternative integral embedding bound

The sharper Li–Margulis bound (6) is not the only possible finite bound.
[Irving Calderón, *S-integral quadratic forms and homogeneous dynamics*,
arXiv:2202.10257v2](https://arxiv.org/abs/2202.10257v2), Theorem 4.1 and
Appendix F, give an alternative equivalence bound. The following estimates
evaluate the two factors left implicit in that chain. Norms below are
maximum absolute matrix entries, in the supplied framings.

**Lemma (spherical-function factor).** Calderón's Appendix A constant
$\mathcal D_1$ may be replaced by $9$, and its mixing factor by $15$.

**Proof.** In the integral for $\Xi_\infty(a_t)$, symmetry gives

$$
\Xi_\infty(a_t)=\frac2\pi\int_0^{\pi/2}
(e^t\sin^2\theta+e^{-t}\cos^2\theta)^{-1/2}\,d\theta.
$$

1. On $[0,e^{-t}]$, $\cos\theta\ge1/2$, so the integrand is at most
   $2e^{t/2}$. On $[e^{-t},\pi/2]$, use
   $\sin\theta\ge2\theta/\pi$.
2. Integration gives
   $\Xi_\infty(a_t)\le e^{-t/2}(4/\pi+t+\log(\pi/2))
   \le(t+3)e^{-t/2}$, using $3<\pi<4$.
3. The function $(t+3)e^{-t/6}$ has maximum at $t=3$, with value
   $6e^{-1/2}<9$. Thus $\Xi_\infty(a_t)\le9e^{-t/3}$.
   Appendix F then permits $\mathcal D=5\sqrt9=15$.

**Lemma (volume factor).** In the Haar normalization of Calderón's
Appendix B, $\operatorname{vol}X^1_{n,\infty}\le2^{2n^3+1}$ for $n\ge3$.

**Proof.**

1. The Siegel set $KAN$ with $a_i/a_{i+1}\le2/\sqrt3$,
   $|u_{ij}|\le1/2$ and $\prod a_i=1$ covers the quotient
   (Calderón, Proposition 5.6).
2. Normalize the compact measure by the tangent basis $E_{ij}-E_{ji}$,
   the diagonal measure by $E_{ii}-E_{nn}$, and the unipotent measure by
   $E_{ij}$, $i<j$. Their combined determinant relative to Appendix B's
   Lie basis has absolute value one. The Iwasawa density is
   $\prod_{i<j}a_i/a_j$.
3. Put $b_i=a_i/a_{i+1}$. The diagonal Jacobian is $1/n$, and the
   integral over $A$ is
   $n^{-1}\prod_{i=1}^{n-1}(2/\sqrt3)^{i(n-i)}/[i(n-i)]
   \le2^{n^3}$. The unipotent box has volume one.
4. The orthogonal-group volume is
   $2\prod_{j=2}^n\operatorname{vol}S^{j-1}$. This follows successively
   from the Riemannian submersions $SO(j)\to S^{j-1}$ in the tangent
   normalization of step 2. Since
   $\operatorname{vol}S^{j-1}=2\pi^{j/2}/\Gamma(j/2)\le4^j$,
   its volume is at most $2^{n(n+1)+1}$. Here
   $\Gamma(j/2)\ge1/2$ follows directly from the integer and
   half-integer gamma values and their recurrence.
5. Multiply steps 3–4 and use $n(n+1)\le n^3$. A covering set bounds
   the quotient volume from above, proving the assertion.

For $n\ge3$, define the following **integers**:

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
$$

**Proposition (equivalence bound).** If two nondegenerate integral
symmetric $n$-ary matrices $G,J$ are integrally isometric and have heights
at most $h,k$, some unimodular $U$ satisfies
$U^TGU=J$ and $\|U\|_\infty\le F_n(h,k)$.

**Proof.** For indefinite forms, substitute the two lemmas into
Calderón's Appendix F constants and its Theorem 4.1 proof with
$S=\{\infty\}$. We retain the additional $2^{2n^6}$ factor in the
closed-orbit volume proposition in $\overline W_n$, without relying on
its absorption into the theorem's stated constant. Rounding the positive
fractional exponents upward enlarges the bounds. The polynomial coefficient
height is at most twice the matrix height, explaining $4hk$.
For definite forms, negate both if necessary. Each isometry column has
square at most $k$, and the inverse-Gram estimate gives coordinate square
at most $k(n-1)!h^{n-1}$. This is smaller than $F_n(h,k)^2$.

`Lattices(ZZ).integral_isometry_coefficient_bound(n,h,k)` evaluates
$F_n(h,k)$; it neither decides equivalence nor constructs an isometry.
The rank restriction $n\ge3$ is essential to the cited polynomial bound.

**Proposition (embedding bound, including nonprimitive images).** Let
$A,G$ be nondegenerate integral Gram matrices of ranks $0<m\le n$,
with $n\ge3$, and put $a=|\det A|$, $h=\|G\|_\infty$.
Let $C$ be the preceding completion Gram bound if $m<n$, and
$C=\|A\|_\infty$ if $m=n$. For every integral solution $X$ of
$X^TGX=A$, there is $g\in O(G,\mathbb Z)$ with

$$
\|gX\|_\infty\le n a(n-1)! F_n(h,n^2C).                 \tag{7}
$$

**Proof.**

1. Complete an existing solution to an integral matrix $\gamma$, preserving
   its first $m$ columns, with $H=\gamma^TG\gamma$ of height at most $C$.
   Its determinant $d=|\det\gamma|$ is the saturation index and
   $d\le a$. For $m=n$ take $\gamma=X$ and $H=A$.
2. The module $P=\gamma^{-1}\mathbb Z^n$ contains $\mathbb Z^n$ with
   index $d$, and $dP\subseteq\mathbb Z^n$. Choose a column Hermite basis
   $B$ of $dP$. Because $dP$ contains $d\mathbb Z^n$, its diagonal
   entries divide $d$ and its reduced off-diagonal entries have absolute
   value at most $d$. Thus $\beta=B/d$ is a basis of $P$ with
   $\|\beta\|_\infty\le1$ and $|\det\beta|=1/d$.
3. The matrix $\gamma\beta$ is integral unimodular, so
   $J=\beta^TH\beta$ is integrally isometric to $G$ and
   $\|J\|_\infty\le n^2C$. Moreover $\beta^{-1}$ is integral, because
   $\mathbb Z^n\subseteq P$, and its adjugate formula bounds its entries
   by $d(n-1)!$.
4. Choose $U$ with $U^TGU=J$ from the equivalence proposition. Let
   $E$ select the first $m$ standard columns and set $X'=U\beta^{-1}E$.
   This is integral and $X'^TGX'=E^THE=A$. Matrix multiplication bounds
   its entries by $nF_n(h,n^2C)d(n-1)!$.
5. **The bounded solution is in the original target orbit.** Put
   $V=\gamma\beta\in\operatorname{GL}_n(\mathbb Z)$. Step 3 gives
   $V^TGV=J=U^TGU$. Therefore $g=UV^{-1}$ is an integral target
   isometry, and
   $$gX=UV^{-1}\gamma E=U\beta^{-1}E=X'.$$
6. **Q.E.D.** Use $d\le a$. No primitivity assumption entered the proof.

`T.integral_embedding_coefficient_bound(L)` computes (7) for an indefinite
target of rank at least three. For a definite integral target of any rank,
it instead takes the maximum of the source-generator square-coordinate
bounds, containing **every** embedding. A zero source or a rank obstruction
receives zero. Rationally split indefinite binary targets have the
all-embedding bound proved below. Nonsplit indefinite binary targets use
their finite norm-orbit representatives and the second-column bound below.

The rank-at-least-three indefinite bound meets **every target-isometry
orbit** of embeddings. It therefore supplies a complete finite exclusion
search for any further decidable predicate invariant under target
isometries, as well as for the unconstrained problem. An arbitrary extra
predicate need not be invariant, so this is not a universal constrained solver.
Neither bound constructs an embedding or implements maximal splitting.
The nonprimitive, sheared-definite and zero-source specimens in its docstring
remain unexecuted under DEV-58. The original sharper formula (6) remains
unevaluated, but is no longer the only available direct bound in rank at
least three.

### Every embedding into a rationally split integral binary target

Let $G=\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)$
be integral, nondegenerate and indefinite, with $b^2-ac=s^2$ for an
integer $s>0$. Let $A$ be a nondegenerate integral source Gram matrix of
rank $1$ or $2$, and set $H=\max_{i,j}|A_{ij}|$. Then every integral
matrix $X$ satisfying $X^TGX=A$ has entries bounded by the following
explicit integer:

$$
B=\begin{cases}
H,&a=c=0,\\
2H\max(|a|,|b|,s),&a\ne0.
\end{cases}
$$

When $a=0\ne c$, interchange the two target basis vectors before applying
the second case; interchanging coordinates preserves their maximum
absolute value. This elementary factorization proof supplies the bound
without a reduction algorithm or an embedding as input.

**Proof.**

1. Suppose $a\ne0$. For each column $(x_i,y_i)$ of $X$, put
   $u_i=ax_i+(b+s)y_i$ and $v_i=ax_i+(b-s)y_i$. These are integers and
   satisfy
   $$u_iv_i=aA_{ii},\qquad
   u_iv_j+v_iu_j=2aA_{ij}.$$
2. If $A_{ii}\ne0$, both factors are nonzero integers, so
   $|u_i|,|v_i|\le |a|H$. If $A_{ii}=0$, nondegeneracy of $A$ implies
   rank two and $A_{ij}\ne0$ for the other column. Exactly one of
   $u_i,v_i$ is nonzero: both zero would make that row of $A$ zero.
   The pairing equation bounds its absolute value by $2|a|H$, since
   its partner in the other column is a nonzero integer. Thus every
   transformed coordinate is bounded by $K=2|a|H$.
3. Inverting these linear factors gives
   $$y_i=\frac{u_i-v_i}{2s},\qquad
   x_i=\frac{(b+s)v_i-(b-s)u_i}{2as}.$$
   Consequently $|y_i|\le 2|a|H/s$ and
   $|x_i|\le 2H\max(|b|,s)/s$, using
   $|b+s|+|b-s|=2\max(|b|,s)$. Since $s\ge1$, both are at most $B$.
4. If $a=c=0$, then $b\ne0$ and the equations are
   $2b x_i y_i=A_{ii}$ and
   $b(x_i y_j+y_i x_j)=A_{ij}$. A nonzero diagonal entry bounds both
   coordinates by $H/(2|b|)$. A zero diagonal entry has exactly one
   nonzero coordinate, bounded by $H/|b|$ through the nonzero pairing
   with the other column, as in step 2. Thus all coordinates are at most
   $H$, proving the assertion in every case.

Unlike (7), this bound contains **every** embedding. The finite box
constructed with `coordinate_subset` and `Emb.with_generator_images_in`
therefore gives complete exclusion for any further decidable predicate
in this split binary regime. It does not bound a zero-norm fibre by
itself: the nondegenerate source hypothesis is essential. For example,
the multiples of either isotropic basis vector of $U$ are unbounded.
Pending docstring specimens cover $U(4)\to U$, a target with nonzero
diagonal and square discriminant, and a sheared split target with large
coefficients. Runtime verification remains under DEV-58.

### A bound from nonsplit binary norm orbits

Let $G$ be a nondegenerate indefinite integral binary Gram matrix with
nonsquare discriminant. It is anisotropic over $\mathbb Q$. Let $A$ be a
nondegenerate integral source Gram matrix of rank $m\in\{1,2\}$. Write
$\alpha=A_{11}$, and let $h=\max_{i,j}|G_{ij}|$.

If $\alpha=0$, no embedding exists: its first basis vector would give a
nonzero rational isotropic vector of $G$. Otherwise take the existing
finite transversal $v_1,\ldots,v_r$ for the integral vectors of square
$\alpha$ modulo $O(G,\mathbb Z)$ and put
$V=\max_{k,i}|(v_k)_i|$, with $V=0$ for an empty transversal. Then the
following integer meets every target-isometry orbit of embeddings:

$$
B=\begin{cases}
V,&m=1,\\
(|A_{12}|+2h|\det A|)V,&m=2.
\end{cases}
$$

**Proof.**

1. Postcompose any embedding by an integral target isometry carrying its
   first column to one of the $v_k$. The new first column $v$ has
   coordinates bounded by $V$. For rank one this proves the assertion.
   An empty transversal excludes an embedding.
2. In rank two put $\beta=A_{12}$, $\gamma=A_{22}$, $p=Gv$, and
   $z=(-p_2,p_1)^T$. Direct multiplication gives
   $v^TGz=0$ and $z^TGz=(\det G)\alpha$. Since $\alpha\ne0$,
   every second column $w$ with $v^TGw=\beta$ has the form
   $$w=(\beta/\alpha)v+t z,\qquad t\in\mathbb Q.$$
3. The prescribed square of $w$ gives
   $$t^2=\frac{\alpha\gamma-\beta^2}{(\det G)\alpha^2}
       =\frac{\det A}{(\det G)\alpha^2}.$$
   Thus, whenever a second column exists,
   $|t|=\sqrt{|\det A|/|\det G|}/|\alpha|\le|\det A|$,
   using the nonzero integer determinants and $|\alpha|\ge1$.
   Also $\|z\|_\infty\le2hV$. These inequalities bound $w$ by $B$.
4. **Q.E.D.** The rank-two factor in $B$ is at least one, so it also
   bounds the first column. The argument makes no primitivity assumption.

The computation reuses `binary_fixed_norm_representatives`, its orbit
section and the selected target coordinates. Its private arithmetic
routine delegates to PARI's `qfbsolve` with flag 3, which returns all
solution classes modulo the special orthogonal group, including
imprimitive solutions; passing to orthogonal orbits can only merge them.
See the [PARI function contract](https://pari.math.u-bordeaux.fr/dochtml/html/Quadratic_number_fields_and_binary_quadratic_forms.html#qfbsolve)
and [Sage's wrapper](https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/binary_qf.html#sage.quadratic_forms.binary_qf.BinaryQF.solve_integer).
No new Pell equation solver or embedding construction is introduced.

This is an effective computation through finite norm-orbit representatives,
not a closed formula in the two Gram heights. It bounds a representative
of each embedding orbit, including nonprimitive images, and supports a
complete finite unconstrained search. Conditions invariant under target isometries are
also preserved by step 1. Arbitrary coordinate conditions need a separate
argument, because a target isometry may change them. Pending specimens
use $\langle1,-2\rangle$, represented squares $1,-2,4$, the excluded
square $3$, the identity embedding and the impossible embedding from $U$.
They remain unexecuted under DEV-58.

### Complete finite searches with invariant constraints

For every nondegenerate finite-rank integral pair $(T,L)$, the implemented
bound now meets every orbit of $O(L)$ on $\operatorname{Emb}(T,L)$.
For definite and split binary targets it even contains every embedding.
For nonsplit binary targets the proof normalizes the first column by a
target isometry and bounds the second column of that same transformed
embedding. For higher-rank indefinite targets, step 5 of the proof of
(7) identifies the target isometry explicitly.

**Proposition.** Let $P$ be a decidable predicate on embeddings with
$P(g\circ j)=P(j)$ for all $g\in O(L)$ and $j\in\operatorname{Emb}(T,L)$.
Then the subset of embeddings with $P$ is empty if and only if its
intersection with the box given by
`T.integral_embedding_coefficient_bound(L)` is empty.

**Proof.** One implication is inclusion of the bounded subset. For the
other, take an embedding satisfying $P$, move it into the box by the
target isometry guaranteed above, and apply the invariance of $P$.
The bounded subset is finite because its coordinates are integers.
Its exact pairing equations and the hypothesis on $P$ make finite
exhaustion a terminating decision.

Primitivity is such a predicate. Postcomposition by $g$ identifies
$L/j(T)$ with $L/(g\circ j)(T)$, so it preserves torsion-freeness of
the cokernel. More generally it preserves the isomorphism class of that
cokernel and the isometry class of the orthogonal complement. This
invariance does not by itself provide an effective decision for every
predicate defined from these objects; decidability remains a separate
hypothesis. A requirement that a selected coordinate be positive, or a
specified vector be fixed, need not be invariant under the full target
orthogonal group.

Use the existing finite subset and predicate constructions directly:

```python
T = Lattices(ZZ)("U").twist(ZZ(2))
L = Lattices(ZZ)("U")
B = T.integral_embedding_coefficient_bound(L)
coefficients = finite_ordered_set(tuple(ZZ(a) for a in range(-int(B), int(B) + 1)))
box = L.coordinate_subset(coefficients)
bounded = T.Emb(L).with_generator_images_in(box.domain())
primitive = bounded.domain().condition_set(lambda j: j.is_primitive())
assert bounded.domain().is_empty() is False
assert primitive.is_empty() is True
```

Here $B=2$. The map with images $2e,f$ embeds $U(2)$ into $U$ with
index two. Every such embedding has index two, since its determinant
satisfies $(\det j)^2=\det U(2)/\det U=4$, so none is primitive.
The finite search distinguishes these two existence questions while
retaining `box.inclusion()`, `bounded.inclusion()` and the original
embedding maps. The source specimens remain unexecuted under DEV-58.
Large bounds can make this finite method impractical; the separate
maintained classification computations remain available.

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

The implementation correspondence below records the current source routes.
It supplements the mathematical index; an inspected implementation is not
runtime acceptance, and none of these rows closes terminal verification.

| Indexed requirement | Current source owner and computation | Coverage still requiring evidence or further computation |
| --- | --- | --- |
| Anisotropy and nonzero isotropic witnesses | `form_modules.py`: `is_anisotropic`; `lattices.py`: `is_isotropic`, `isotropic_vector`; rational PARI decision and real congruence routes | Exact ZZ/QQ, AA and applicable represented RR cases have source routes; general real-oracle zero decisions are not supplied |
| Witt index and decomposition | `lattices.py`: `witt_index`, `witt_decomposition`; private Hecke rational computation and real congruence/sign/root computation | Returned forms and inverse maps need terminal execution; the separate certified-approximation route remains unimplemented |
| Norm fibres, including zero | `form_modules.py`: `square_fibre`, `elements_of_norm`; `lattices.py`: `elements_of_norm`, `representation_vector` | Set inclusion and membership are separate from finding a nonzero point; definite, rank-zero and nonzero split binary integral fibres have finite source routes |
| Scalar extension of objects and arrows | `FormBaseChanges`, `FormedModuleMorphism.base_change`, `LatticeIsometryMethods.base_change`, module scalar-extension functor | Scalar-valued forms have source routes with actual ring maps and both arrow components; arbitrary value-module extensions remain outside the current computation |
| Embedding sets, decisions and witnesses | `lattice_morphisms.py`: embedding Mor, `_emptiness_decision`, `an_element`, integral-overlattice factorization and field Witt criterion | Nondegenerate finite ZZ/QQ/AA and applicable RR endpoints have source routes; backend coverage and witness transport remain unexecuted |
| Complete countable enumeration | Finite free-module and embedding `__iter__` over ZZ/QQ | Each candidate must occur finitely far into the enumeration; asking for a next satisfying element need not terminate; no real enumeration is claimed |
| Finite constrained search | `coordinate_subset`, `Emb.with_generator_images_in`, `condition_set` | Exact pairing equations and the additional predicate must be decidable; finite search alone excludes only its specified box |
| Effective integral bounds | Definite inverse-Gram bound, representative/completion/isometry/embedding coefficient bounds, split binary factors and nonsplit binary norm orbits | The embedding bound meets every target-isometry orbit, hence covers decidable invariant constraints; arbitrary noninvariant constraints require an applicable argument and have no uniform solver below |
| Sampling | `finite_ordered_sets.py`: `random_element` on the selected finite support | Uniform finite-support distribution; empty support is rejected; no infinite uniform distribution or completeness inference |
| Exact solving, kernels and arithmetic predicates | Module morphism `preimage`, `kernel`, `cokernel`, `is_primitive`; lattice `div`, `bezout_partner`, `hyperbolic_partner` and its locus | PID/image-membership and finite integral congruence routes retain original-ring maps; terminal specimens remain unexecuted |
| Perpendiculars and supplied decompositions | `orthogonal_complement`, `orthogonal_splitting`, `orthogonal_decomposition` | Retain the supplied first embedding and full kernel inclusion; direct-sum hypotheses remain essential |
| Target hyperbolic index and maximal splitting | Mathematical contracts in this note | Their main computations remain explicitly deferred by the owner's dependency-only assignment |

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

For equal finite dimensions, an injective linear map over a field is
bijective. Thus the same decision also decides `T.Isom(L).is_empty()`
for finite nondegenerate endpoints over `QQ` and `AA`. Its witness
construction now retains the embedding's underlying module map and its
inverse as a module isomorphism, then returns the form-preserving
isomorphism with the original endpoints. Over `QQ` it takes a point of
the complete rational embedding iterator after deciding nonemptiness;
over `AA` it uses the diagonal-sign construction. In particular it
neither converts rational Gram coefficients to integers nor asks for an
enumeration of algebraic real points.

For example $\langle1/4\rangle\simeq\langle1\rangle$ over
$\mathbb Q$ by $v\mapsto e/2$, with inverse $e\mapsto2v$.
The forms $\langle3\rangle$ and $\langle1\rangle$ are isometric
over `AA`, by scaling by $\sqrt3$, but not over `QQ`.
These distinguish a field isometry from integral equivalence of the
chosen Gram presentations. This field route is also necessary for
`T.Emb(L).an_element()` in equal rank, which selects an isometry there.
The field decision and both inverse-composite specimens in
`LatticeIsometryMor.an_element` remain unexecuted under DEV-58.

The maintained primitive-embedding classifier is a separate, applicable
integral computation. Its target-specific calls now use
`primitive_embeddings(target, source; check=true)`. The
[OSCAR 1.8.2 lattice overload](https://github.com/oscar-system/Oscar.jl/blob/v1.8.2/src/NumberTheory/QuadFormAndIsom/embeddings.jl#L1632)
filters genus representatives by the isometry decision `is_isometric`.
The previous adapter instead asked for `is_isometric_with_isometry`
during filtering, although that
[Hecke 0.39.22 witness routine](https://github.com/thofma/Hecke.jl/blob/v0.39.22/src/QuadForm/Quad/ZLattices.jl#L595)
rejects indefinite lattices. A decision suffices to filter; when a map is
requested, the existing research `Isom` constructions transport the
returned inclusion to the original source and target. The classification
mode is preserved, and the finite representatives remain representatives
of classes, not all embeddings. For example $\langle2\rangle$ embeds
primitively into $U\perp\langle2\rangle$ by the displayed summand
inclusion. Its decision, retained endpoints and form/primitivity specimens
are recorded in the classifier docstring and remain unexecuted under
DEV-58. Failure of primitive embedding still does not exclude a
nonprimitive integral embedding.

#### General integral existence through integral overlattices

**Proposition (saturation reduction).** For nondegenerate integral
lattices $T,L$ of finite rank,

$$
\operatorname{Emb}_{\mathbb Z}(T,L)\ne\varnothing
\quad\Longleftrightarrow\quad
\text{some integral overlattice }T\subseteq T'\subseteq T^\vee
\text{ admits a primitive embedding into }L.
$$

The family of integral overlattices is finite and includes $T$ itself.
It is computed by `T.integral_overlattice_inclusions()`, through
bilinear-isotropic subgroups of the discriminant bilinear form. This
uses integrality, not evenness; an even source can have an odd integral
overlattice. The correspondence and its inclusions are the constructions
in `LeanCategories/Lattices/Valued/Gluing.lean`.

**Proof.** Assume the stated finite-rank nondegeneracy hypotheses;
prove the equivalence and finiteness.

1. **Given $j:T\hookrightarrow L$, form the saturation
   $P=j_{\mathbb Q}(T_{\mathbb Q})\cap L$.** This is a primitive
   sublattice of $L$: if a nonzero integer multiple of $x\in L$
   lies in the rational subspace, then $x$ lies there too.
2. **Pull $P$ back along $j_{\mathbb Q}$ to an integral overlattice
   $T'$ of $T$.** The form on $P$ is integral because $P\subseteq L$.
   For $x\in T'$ and $t\in T$, $B_T(x,t)=B_L(j_{\mathbb Q}x,jt)$
   is integral; hence $T'\subseteq T^\vee$. The restriction
   $T'\to L$ has image $P$ and is therefore primitive by step 1.
3. **Conversely, compose an overlattice inclusion with a primitive
   embedding $T'\hookrightarrow L$.** Both are injective and preserve
   the form, so their composite is an element of
   $\operatorname{Emb}_{\mathbb Z}(T,L)$.
4. **There are finitely many $T'$.** Nondegeneracy makes
   $T^\vee/T$ finite. Each overlattice corresponds to a subgroup of
   this finite group, with integrality equivalent to vanishing of the
   discriminant bilinear pairing on that subgroup.
5. **Q.E.D.** Steps 1–3 prove the equivalence and step 4 gives the
   required finite family.

The general integral embedding decision now composes these existing
computations. For an indefinite target, it exhausts the integral
overlattice inclusions, using the target-specific primitive decision
when the source rank is smaller. In equal rank, a primitive embedding
is an isometry, so it uses the integral `Isom` decision. The existence
decision retains a successful inclusion and its nonempty map set;
witness selection obtains the latter map and composes the actual
underlying module maps. Definite targets keep their finite-shell route.
Neither this reduction nor its implementation searches an unbounded
sequence of vector boxes. Runtime execution and engine coverage remain
unverified under DEV-58.

For example $U(4)\hookrightarrow U(2)$ has index two, by
$e\mapsto2e$, $f\mapsto f$. It is not an isometry and cannot be a
primitive embedding in equal rank, but the finite reduction finds the
intermediate overlattice. The odd lattice $\langle1\rangle$ does
not embed in the even lattice $U(2)$. Both cases are specimens of the
decision, and the first also checks witness endpoints, the form equation
and index. Extra predicates on embeddings are not preserved by passing
to a representative of an embedding class; their complete decision
still requires additional work.

For a nonzero integer $a$, $\langle a\rangle\hookrightarrow L$
is equivalent to a nonzero integral vector of square $a$. Thus the same
finite classification now supplies `L.representation_vector(a)` in
indefinite rank at least three, by evaluating the returned embedding on
the source generator. It also decides the remaining ternary
`L.represents(a)` cases after the existing local and single-spinor-genus
shortcuts. No local solvability assertion is used as a witness, and no
unbounded vector search replaces the missing construction. The
higher-rank norm and ternary distinguishing specimens remain pending
under their TODO owner.

For $T=U$, the same set is the subset of $L\times L$ defined by
$q(e)=q(f)=0$ and $B(e,f)=1$. For $U^{\perp r}$ it is the subset of the
finite product indexed by the specified hyperbolic basis satisfying all
pairing equations. This supplies the embedding-space interpretation of the
matrix search without making matrices the public mathematical result.

#### A ternary local–global obstruction

[Borovoi, *On representations of integers by indefinite ternary quadratic
forms*, §2 and Example 0.1.1](https://arxiv.org/abs/math/0006141)
gives

$$
G=\begin{pmatrix}-9&1&0\\1&7&0\\0&0&2\end{pmatrix},
\qquad q(x,y,z)=-9x^2+2xy+7y^2+2z^2.
$$

**Proposition.** This lattice represents $1$ over every completion but
not over $\mathbb Z$; it represents $2$ integrally.

**Proof.**

1. **Away from $2$.** The rational vector $(-1/2,1/2,1)$ has square
   one and is integral at every odd prime.
2. **At $2$.** For $F(Z)=q(4,1,Z)-1$, $F(1)=-128$ and
   $F'(1)=4$. Hensel's inequality $7>2\cdot2$ gives a root in
   $\mathbb Z_2$.
3. **Integral exclusion.** Suppose $q(x,y,z)=1$. Put $u=x-y$,
   $v=x+y$. Then $2z^2-1=u(u+8v)$. Both $u,v$ are odd;
   reduction modulo $8$ makes $z$ odd, and modulo $16$ gives
   $u^2\equiv9$, hence $u\equiv\pm3\pmod8$.
4. **Contradiction.** Some odd prime divisor $p$ of $u$ is
   $\pm3\pmod8$. But $2z^2\equiv1\pmod p$ makes $2$ a square,
   forcing $p\equiv\pm1\pmod8$.
5. **Q.E.D.** Finally $q(0,0,1)=2$.

Borovoi also places $G$ and $\operatorname{diag}(-1,64,2)$ in the same
genus. The latter represents $1$ at $(1,0,1)$. They are therefore
inequivalent; Eichler's theorem for indefinite lattices of rank at least
three implies that this genus has more than one spinor genus
(Conway–Sloane, Chapter 15). This supplies the missing distinguishing
specimen, without asserting an exact count from a backend.

```python
L = Lattices(ZZ)([[-9, 1, 0], [1, 7, 0], [0, 0, 2]])
assert L.spinor_genus_count() > ZZ(1)
assert L.represents(ZZ(1)) is False
assert Lattices(ZZ)([[1]]).Emb(L).is_empty() is True
assert L.represents(ZZ(2)) is True
v = L.representation_vector(ZZ(2))
assert v.parent() is L and L.q(v) == ZZ(2)
```

These assertions remain unexecuted under DEV-58. They distinguish the
integral exclusion from a local-solvability shortcut and exercise witness
construction in a genus with multiple spinor genera.

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

Successful membership or point selection does establish nonemptiness.
The predicate-subset owner retains its admitted points, and its
`is_empty()` computation now returns `False` when one is present, without
starting another search or asking for a cardinality. One failed membership
test supplies no empty-set decision, and an undecided membership test
supplies no member. The pending `NN` tail specimen checks this difference
at the general set owner, independently of lattices.

The same retained member now supplies `an_element()` before any iterator
is requested. Choosing an element of an inhabited subset needs no
enumeration of its universe. For example, admit zero into
`L.elements_of_norm(0)`, or a computed `L.representation_vector(a)` into
`L.elements_of_norm(a)` for nonzero $a$. Subsequent point selection uses
that actual admitted vector and the fibre inclusion, including over RR.
This supplies no iterator, cardinality or sampling distribution. With no
retained member the complete countable search still has its stated
termination limits. Pending real positive-subset and norm-fibre specimens
exercise this distinction without enumerating real points.

Searches in this note have explicit termination reasons: rational witness
search starts only after existence is decided. Integral exclusion uses either
a finite bound guaranteed to contain a solution or the finite integral-
overlattice and primitive-embedding reduction. A time
budget expiring yields an unfinished search, not an empty set. An arbitrary
extra predicate on embeddings need not preserve either termination guarantee.
The evaluated integral bound meets every target-isometry orbit, so it also
preserves existence under any further decidable invariant predicate, such
as primitivity. A noninvariant constrained search needs a bound valid for
those conditions or another complete solver.

Sampling must likewise state its distribution and its support. There is no
uniform probability distribution on a countably infinite discrete set giving
every point the same mass. Sampling vectors in a real box with a density
relative to area is also unsuitable for exact isotropy even in $U_{\mathbb R}$:
its zero locus is the union of two axes, each of area zero. Sampling on a
parametrization of the desired locus is a different operation. For software
over exact real presentations, the finitely describable outputs of a sampler
also need not exhaust the mathematical real locus. None of the exact
algorithms above requires a random sampler.

#### Why arbitrary decidable embedding filters have no uniform emptiness solver

The general subset operation accepts an arbitrary decidable predicate, not
only polynomial equations or predicates invariant under a group. No algorithm
can decide emptiness for every such subset, even with fixed nondegenerate
integral source and target.

**Proposition.** There is no total emptiness algorithm for arbitrary
decidable predicate subsets of $\operatorname{Emb}_{\mathbb Z}(U,U\perp\langle2\rangle)$.

**Proof.**

1. Give $L=U\perp\langle2\rangle$ basis $e,f,a$, with
   $B(e,f)=1$, $q(a)=2$ and other cross pairings zero. For each
   integer $n\ge0$, the map
   $$j_n(e)=e,\qquad j_n(f)=f+na-n^2e$$
   is an isometric embedding: its two squares are zero and its cross
   pairing is one. It is primitive, since its source is $U$ and (3)
   supplies a splitting.
2. Conversely, an embedding $j$ with $j(e)=e$ has
   $j(f)=xe+f+na$ for integers $x,n$. The cross pairing forces the
   coefficient of $f$ to be one; the zero square then gives $x=-n^2$.
   Thus the embeddings with $j(e)=e$ and nonnegative $a$-coordinate
   of $j(f)$ are exactly the distinct $j_n$.
3. For a program $C$ on a fixed input, define $P_C(j)$ to require
   those two coordinate conditions and that $C$ halt within $n$ steps.
   This predicate is decidable on every supplied embedding: after the
   coordinate tests, a simulation for a specified finite number of steps
   always terminates.
4. The subset defined by $P_C$ is nonempty exactly when $C$ eventually
   halts. A uniform emptiness algorithm would therefore decide the
   halting problem, contradicting Turing's undecidability theorem.
   See [Turing, *On Computable Numbers, with an Application to the
   Entscheidungsproblem*, §§8–9](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/plms/s2-42.1.230).

This is an obstruction to a uniform decision, not to the subset itself,
its inclusion, exact membership, or complete countable enumeration.
Finite boxes decide their own restrictions. The invariant-constraint
theorem applies when its invariance hypothesis holds; the predicates
$P_C$ need not satisfy it. A proposed solver for a particular noninvariant
condition still needs its own mathematical hypotheses and termination
argument. The dependency index does not require an impossible universal
extension of `is_empty()` to every programmable predicate.

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
| Effective representation bounds | A usable integer bound for the relevant form representation problem, with its hypotheses; (7), the definite inverse-Gram bound and the two binary bounds are evaluated integral instances; (6) retains its unevaluated sharper constant |
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

#### Scalar extension of the maps, not only the forms

For scalar-valued formed modules over a commutative ring $R$, a morphism
is a pair $(f,h)$ with $f:M\to N$ and $h:R\to R$ linear and
$h(B_M(x,y))=B_N(fx,fy)$. A lattice morphism has $h=1_R$.
For a ring map $\varphi:R\to S$, scalar extension sends both maps to
$f_S=1_S\otimes f$ and $h_S=1_S\otimes h$, using the canonical
identification $S\otimes_RR\simeq S$ for the values. The formal
operation is `baseChangeBilWForm` in
`LeanCategories/Lattices/Valued/BaseChange.lean`; its two defining
components are the scalar extensions of the module and value maps.

**Proposition.** This pair preserves the extended bilinear forms.

**Proof.** Assume the displayed form equation and $\varphi:R\to S$;
prove $h_S(B_{M,S}(u,v))=B_{N,S}(f_Su,f_Sv)$.

1. **$h(r)=r h(1)$ for every $r\in R$.** This is linearity on the
   regular module $R$. Hence $h_S$ is multiplication by $\varphi(h(1))$.
2. **The required equation holds on pure tensors.** For $s,t\in S$
   and $x,y\in M$, its two sides respectively equal
   $st\varphi(h(B_M(x,y)))$ and $st\varphi(B_N(fx,fy))$.
   These are equal by the assumed form equation.
3. **Q.E.D.** Pure tensors generate the scalar extension and both
   sides are bilinear, so step 2 proves the equation on all pairs.

`FormedModuleMorphism.base_change(phi)` now retains this pair. Its
underlying map uses the existing module scalar-extension functor; its
value map multiplies by the image of `map_value(R.one())`. For example,
on $\langle1\rangle$ the pair $(x\mapsto2x,r\mapsto4r)$ extends
with both components, rather than becoming only multiplication by two.
The current object computation supports scalar-valued forms; unsupported
value-module extensions remain a computation boundary.

This operation returns a formed morphism, not an unconditional embedding.
The embedding $\langle4\rangle\to\langle1\rangle$ defined by
$v\mapsto2e$ becomes zero after scalar extension to $\mathbb F_2$.
Its value map is still the identity, and its form equation still holds.
Flatness supplies the usual sufficient hypothesis for preserving
injectivity; an inverse pair is preserved along every scalar change.
The existing isometry specialization retains that pair separately.
The multiplier, composition and nonflat-injectivity specimens in the
formed-morphism docstring remain unexecuted under DEV-58.

#### Exact field preimages and affine solving

For a linear map $f:V\to W$ between finite-dimensional vector spaces over
an exact field, with coefficient matrix $A$ in the specified bases, a
target $b$ is in its image exactly
when $\operatorname{rank}[A\mid b]=\operatorname{rank}A$. Indeed the
augmented column adds no dimension precisely when it lies in the span of
the original columns. In the consistent case an exact linear solver
returns the coordinates of an actual preimage in the original $V$.

The finite-free module preimage computation now uses these maintained
rank and solving operations directly over exact fields; see
[Sage's linear-system interface](https://www.sagemath.org/doc/tutorial/tour_linalg.html).
This repairs a source obstruction for represented RR: the former route
required a PID Smith computation, whose presentation guard rejects SR
because `SR.is_exact()` is `False`. Sage documents this explicitly in its
[symbolic-ring reference](https://doc.sagemath.org/html/en/reference/calculus/sage/symbolic/ring.html#sage.symbolic.ring.SymbolicRing.is_exact).
The new field route computes over RR itself,
so elimination uses its exact scalar comparisons and divisions. It
returns absence only after the augmented-rank test proves inconsistency.
An unavailable scalar operation or solver error propagates, rather than
being caught and interpreted as an empty affine fibre.

The original module arrow supplies both bases and the returned point's
parent. Existing selected lifts retain precedence. The PID Smith route
continues to enforce divisibility for integral modules: multiplication by
two on $\mathbb Z$ has no preimage of one. Pending owner-local specimens
cover a rank-one map with coefficient $\pi$ over RR, a target outside its
image, zero source and the integral divisibility distinction. These serve
the affine pairing equations used by `hyperbolic_partner`; they remain
unexecuted under DEV-58.

The same scalar choice now governs generic kernel, inverse-matrix and
finite-span computations. `_linear_algebra_ring` uses the exact owned
field when its selected symbolic computation ring reports inexactness;
otherwise it uses the selected computation ring. This retains the field's
partial equality and exact division through all elimination stages,
including the normalization of the computed kernel's spanning family.
Private serialization into other engines keeps its existing selected-ring
contract.

The source kernel construction still returns its submodule and original
inclusion, and the inverse construction reverses the actual arrow's
endpoints. The pending rank-one map $\mathbb R^3\to\mathbb R$ with
matrix $(\pi,0,0)$ has kernel spanned by the last two basis vectors;
its two-dimensional kernel exercises finite-span normalization as well
as the nullspace computation. A triangular matrix with coefficient $\pi$
supplies both inverse-composite assertions, and the empty matrix checks
rank zero. These source specimens remain unexecuted under DEV-58.

#### Maps retained by the inspected constructions

This table records the source-level map checks for the index. It does
not replace the mathematical assertions or their pending execution.

| Construction | Inspected source | Retained datum and boundary |
| --- | --- | --- |
| Norm fibre | `form_modules.py`: `square_fibre`, `elements_of_norm`; `lattices.py`: finite integral `elements_of_norm`; `set_categories.py`: equalizer and finite-subset constructions | Inclusion into the original module; complete finite enumeration for definite integral, rank-zero integral and nonzero split binary integral fibres; zero remains in the zero fibre; general equalizers make no countability inference |
| Form scalar extension | `form_modules.py`: `_formed_module_base_change`, `FormBaseChanges` | Original formed module, actual ring map and source-to-restriction unit; current computation is scalar-valued |
| Formed morphism scalar extension | `form_modules.py`: `FormedModuleMorphism.base_change`; `scalar_change.py`: `_apply_morphism` | Both components of the form square; the module component retains its original morphism and extension functor; injectivity is not presumed |
| Isometry scalar extension | `lattice_morphisms.py`: `LatticeIsometryMethods.base_change` | Forward and inverse maps over the same extended endpoints, combined in the module core |
| Finite coordinate subset and embedding filter | `framed_free_modules.py`: `coordinate_subset`; `lattice_morphisms.py`: `with_generator_images_in` | Inclusion into the original module and inclusion into the original embedding set; members retain evaluation and both endpoints |
| Orthogonal complement | `lattice_morphisms.py`: `orthogonal_complement`; `form_modules.py`: general pairing-kernel route | Full integral kernel over ZZ, or the general module kernel, with inclusion and restricted form; no direct-sum conclusion is presumed |
| Splitting of a supplied summand | `lattice_morphisms.py`: `orthogonal_splitting`; `lattices.py`: `orthogonal_decomposition` | Original first summand and its specified embedding, complement inclusion, and isometry with inverse over the original ring |
| Field Witt decomposition and field isometry | `lattices.py`: `witt_decomposition`; `lattice_morphisms.py`: field `Isom` decision and witness | QQ/AA and applicable represented-RR endpoints, form equation and inverse maps; the Witt domain retains both summands and their module inclusions and projections |

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
square roots; the represented `RR` route uses the same construction when
its exact arithmetic and sign decisions succeed; `diagonalization()` itself returns an isometry from the diagonal
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

For finite-rank definite integral lattices, `elements_of_norm(a)` now
uses the complete finite `vectors_of_square(a)` computation. Thus the
zero fibre is a singleton whose enumeration terminates; a wrong-sign or
unrepresented square gives an empty finite set. Nonzero fibres of split
nondegenerate binary integral forms likewise retain their finite divisor
enumeration; the zero fibre of a hyperbolic plane remains infinite. The rank-zero integral
case is also finite: it contains zero exactly at square zero. The
finite-subset construction retains its original universe on the domain
set, so `F.inclusion(): F -> L` is available as well as the inclusion
on the subobject returned by `vectors_of_square`. This reuses the
ordered-subset construction; it does not create another norm-fibre type.
The definite, negative definite, empty and rank-zero examples in the
method docstring remain unexecuted under DEV-58.

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
conditions. The complete `T.Emb(L)` iterator remains available over `ZZ`
and `QQ`, but iteration alone is not an emptiness decision. For nondegenerate
rational endpoints, witness selection uses the Witt-index decision first.
For nondegenerate integral endpoints, it uses the finite-shell or integral-
overlattice classification route. The effective constant in (6) remains
needed for that particular sharper expression. The evaluated alternative
(7) now gives a direct integer box bound in rank at least three, while the
classification route supplies a separate unconstrained existence decision.
The evaluated bound meets every target-isometry orbit, so decidable
invariant predicates also admit complete finite exclusion. Other predicates
require their own termination argument.

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
- **Irving Calderón, *S-integral quadratic forms and homogeneous dynamics*,
  arXiv:2202.10257v2, 27 April 2023.**
  [Author's manuscript](https://arxiv.org/abs/2202.10257v2).
  Theorem 4.1, the closed-orbit volume proposition, and Appendices A, B
  and F give the equivalence estimate and its normalization. The spherical
  and quotient-volume majorants used here are proved above.
- **Mikhail Borovoi, *On representations of integers by indefinite ternary
  quadratic forms*, Journal of Number Theory 90 (2001), 281–293.**
  [Author's arXiv preprint](https://arxiv.org/abs/math/0006141),
  [published version](https://doi.org/10.1006/jnth.2001.2662).
  Section 2 proves the local–global obstruction for the displayed ternary
  form; Example 0.1.1 supplies the same-genus comparison.
- **J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups*,
  third edition, Springer, 1999, Chapter 15.**
  Sections 3.5 and 6 for indefinite spinor genera and the displayed genus.
- **SageMath reference manual, *Solving quadratic equations*.**
  [Official documentation](https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/qfsolve.html).
  The `qfsolve` interface to PARI's Simon implementation.
- **Magma handbook, *Isotropic subspaces*.**
  [Official documentation](https://docs.magma-maths.org/LatticesQuadraticForms/QuadraticForms/isotropic.html).
  Algorithm attribution and the qualifications on maximality of returned
  isotropic subspaces. Software documentation consulted 23 October 2026.
