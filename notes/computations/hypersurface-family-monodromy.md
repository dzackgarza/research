# Hodge-theoretic monodromy of a one-parameter hypersurface family — the pipeline, and the surface it has no home on

Migrated 2026-08-20 from the lattice-research corpus
(`src.bak/backends/foliation_backend.py`, `tests.bak/test_foliation_backend.py`,
`tests/theory_spec/monodromy_foliation_backend.md`).

This is a **note beside a stated gap**, not a migration into the preamble. The
computation below is complete and was run green in the source corpus; what does
not exist here is anything for it to be a method *of*. See “The gap” below
before proposing a landing.

## What the computation takes and produces

Input: a family of hypersurfaces over a one-dimensional base, presented as a
polynomial $f \in k[x_0,\dots,x_{n-1},t]$ with $\operatorname{char} k = 0$, the
last variable being the parameter. The source corpus normalised the variable
names to $x_0,\dots,x_{n-1},t$ and carried the term order's weight vector
through, because the weights become the Singular ring order (`wp(...)`, or
`dp` when the order is unweighted).

Output: the Milnor number $\mu$, the Picard–Fuchs operator, and the local
monodromy at $t=0$ in its multiplicative Jordan decomposition.

## The pipeline

1. **Jacobian ideal and Milnor algebra.** $J = \operatorname{jacob}(f)$ in
   $k(t)[x_0,\dots,x_{n-1}]$; a monomial basis $B$ of the Milnor algebra
   $k(t)[x]/J$ is read off a standard basis (Singular's `okbase(std(J))`), and
   $\mu = |B|$. The base field is $k(t)$, so $\mu$ is the *generic* Milnor
   number of the family.

2. **Brieskorn lattice and the Gauss–Manin connection.** Movasati's
   `foliation.lib` implements the Gauss–Manin connection on the Brieskorn
   module of $f$. The corpus fed it the form
   $$
   P = (-1)^{n-1}\,\frac{\partial_t f}{t}\,\Bigl(\sum_{b \in B} b\Bigr),
   $$
   with the cycle vector $\mathbf e = [1]$, and asked `PFequ(f, P, e)` for the
   Picard–Fuchs equation.

3. **The Picard–Fuchs operator.** `PFequ` returns a row of $\mu+1$
   coefficients, each a polynomial in $t$ alone (the corpus asserted both:
   no $x$-degree, and denominator $1$). They are assembled into
   $$
   L \;=\; \sum_{i=0}^{\mu} c_i(t)\,D_t^{\,i}
   $$
   in the Ore algebra $k[t]\langle D_t\rangle$ (`ore_algebra`'s
   `OreAlgebra(k[t], "Dt")`). The order of $L$ is $\mu$.

4. **Indicial polynomial at $t=0$.** `ore_algebra`'s `indicial_polynomial`,
   evaluated at the base ring's generator. Its roots are the indicial
   exponents $\alpha_1,\dots,\alpha_\mu$ at $t=0$, and the corpus asserted
   $\deg = \mu$ — which *is* the regular-singularity hypothesis at $t=0$, so
   the assertion is the hypothesis being checked rather than assumed.

5. **Logarithm of the monodromy.** The Jordan form $N$ over $\overline{\mathbb Q}$
   of the companion matrix of the monic indicial polynomial. Its diagonal part
   $S$ is the semisimple half, $N - S$ the nilpotent half.

6. **The monodromy.** With $\mathcal N = N - S$ nilpotent:
   * unipotent factor $U = \exp(2\pi i\,\mathcal N)$, a finite sum;
   * semisimple factor $S' = \operatorname{diag}\bigl(e^{2\pi i \alpha}\bigr)$,
     one entry per exponent, repeated over its Jordan block;
   * monodromy $T = S' U$, and its Jordan form assembled block by block —
     eigenvalue $e^{2\pi i\alpha}$ on the diagonal, $1$ on the superdiagonal
     inside each block.

   The block structure is recovered by scanning the superdiagonal of the
   computed Jordan form. That read is presentation-dependent: it is correct
   for Sage's normal form and would silently mis-segment a differently
   normalised one. Any landing should take the block sizes from the Jordan
   *decomposition data* rather than from the matrix's entries.

## The specimen: the Legendre family

$y^2 = x(x-1)(x-u)$, in the weighted ring $k[x,y,u]$ with
`wdegrevlex` weights $(2,3,1)$. The corpus recorded:

* $\mu = 2$;
* a second-order Picard–Fuchs operator whose coefficient list begins
  $-3t+3,\; 12t^2+8t-4,\; 12t^3-8t^2-4t$;
* indicial polynomial $-4\alpha^2$, i.e. a double exponent $\alpha = 0$ at
  $t=0$;
* log-monodromy Jordan form $\begin{pmatrix}0&1\\0&0\end{pmatrix}$;
* unipotent monodromy $\begin{pmatrix}1&2\pi i\\0&1\end{pmatrix}$ — a single
  Jordan block, maximally unipotent.

## The recorded finding: these numbers are not yet assertions

The corpus's own theory spec records that its tests were **not**
literature-grounded, and the finding stands here unchanged:

* The Picard–Fuchs coefficient list was asserted against values the code
  itself produced. It depends on the choice of the form $P$ and of the Milnor
  basis, so it is a fact about *this* normalisation, not about the Legendre
  family.
* The indicial polynomial was asserted with its leading coefficient, which is
  fixed by `ore_algebra`'s own normalisation (gcd-reduced, denominators
  cleared). The mathematical content is the *roots*: a double exponent $0$.
* The monodromy matrices are in the **period-integral basis**, not an integral
  homology basis — the entry $2\pi i$ rather than an integer is the tell. The
  standard topological statement (Picard–Lefschetz: monodromy conjugate to
  $\begin{pmatrix}1&2\\0&1\end{pmatrix}$ around a node) does not validate this
  output, because the bases differ.

The spec names the sources that would ground each assertion — Movasati's Hodge
theory course for the explicit Picard–Fuchs matrix and the Gauss–Manin basis,
Griffiths' *periods of certain rational integrals* for the regular-singularity
statement, SGA 7 Exp. XV for the integral-basis monodromy. **None of them has
been consulted here**; they are recorded as the corpus identified them, and no
citation key is claimed against them. Grounding an assertion means opening one
of them first.

## The gap

The preamble has no surface this is a method of. Sited honestly, the operation
belongs to a *family of varieties over a base* — the source corpus had a
`FamilyOfVarieties` notion its test subclassed — and its output is variation of
Hodge structure data: a Gauss–Manin connection, a Picard–Fuchs $D$-module, a
limit mixed Hodge structure at $t=0$. The preamble's `categories/schemes/` tree
owns schemes, subschemes, varieties, ambient spaces, polytopes and ADE
surfaces; there is no family, no relative object over a base, no connection,
and no $D$-module anywhere in it.

Adding one is an architecture decision and not a local addition: it introduces
a fibred category over a base, a de Rham/Betti pairing, and a differential
category whose objects are not modules over the base ring in the preamble's
current sense. That decision is the user's, so this note is where the content
waits.

What a landing would need, in order:

1. An object for a family $X \to S$ over a one-dimensional base, with fibres
   and specialisation.
2. The Brieskorn/Gauss–Manin construction as a functor out of it, not as a
   method returning matrices.
3. The Picard–Fuchs operator as an object of a differential algebra (the
   `ore_algebra` package is the existing implementation and would sit behind
   an engine seam, exactly as `julia` and `polyhedral_common` do).
4. Local monodromy as the operator's own question at a point of $S$, with the
   multiplicative Jordan decomposition read off the connection data rather
   than off a matrix's superdiagonal.

## Where the third-party code lives

Movasati's `foliation.lib` (Singular library, v2.34, 2019) is external code and
never migrates into the preamble. It is already in tree, byte-identical to the
corpus's copy, at
`computations/scripts/components/hodge-periods/foliation.lib`, with the local
driver `computations/scripts/components/monodromy/compute_monodromy.sing`
beside it. What of it is worth reimplementing is analysed in
`notes/computations/extraction-specs/foliation_extraction_spec.md`, and the two
period-computation approaches are compared in
`notes/computations/comparisons/foliation_vs_lefschetz.md`.

The corpus's own driver — the Python that assembles the pipeline above — is
`computations/scripts/lattice-research/backends/foliation_backend.py`, with its
Legendre-family test at `.../specs/tests/test_foliation_backend.py`. It is
source material, not a maintained surface; it is kept because it is the
reference implementation for whatever eventually owns the computation.
