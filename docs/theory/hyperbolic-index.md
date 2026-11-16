# Hyperbolic index: implementation contracts

The mathematical definitions, proofs, bounds, examples and limits of this work are in the research book:

- [Integral hyperbolic index and splitting](../../writing/lattice-theory/hyperbolic/integral-hyperbolic-index.md): hyperbolic pairs, complements, radical reduction, maximality and base-ring examples.
- [Constructive real and rational splitting](../../writing/lattice-theory/hyperbolic/constructive-real-rational-splitting.md): certified real input, signature, diagonalization and inverse maps, rational local tests and Witt splitting.
- [Effective bounds for integral embeddings](../../writing/lattice-theory/hyperbolic/effective-integral-embedding-bounds.md): definite shells, all representative and completion constants, evaluated equivalence and orbit bounds, binary bounds and constrained search.
- [Norm fibres and embedding loci](../../writing/lattice-theory/hyperbolic/norm-fibres-and-embedding-loci.md): norm equalizers, embedding spaces, saturation, the ternary obstruction, enumeration, arbitrary-filter undecidability, scalar extension and affine/partner loci.

The equation numbers used in the implementation records below refer to those book owners: the splitting equation and projection are in the first chapter; the sharper Li–Margulis bound and evaluated embedding bound are in the third chapter. The remaining text records source routes, object and map ownership, API contracts, provider constraints and verification status. A source route is not a correctness proof.

## Constructor and field routes

`Lattices(R)("U")` constructs the hyperbolic plane over the selected ring. The index computation has source routes for `ZZ`, `QQ`, `AA` and applicable `RR`, not for every ring accepted by the constructor. `L.hyperbolic_index()` returns the integral summand index over `ZZ`; `L.maximal_hyperbolic_index_splitting()` returns the isometry with its original endpoints and complement. Over fields the corresponding `witt_index()` and `witt_decomposition()` routes retain both summand embeddings and inverse maps. A degenerate input first passes through its radical quotient and lifts the splitting back into the original form. Rank zero retains the empty inverse pair and the original coefficient ring.

The rational route uses Sage's [qfsolve interface](https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/qfsolve.html) to PARI's Simon implementation when applicable. A vector or isotropic subspace from that solver still needs a pairing-one partner and the full perpendicular inclusion. [Magma's IsotropicSubspace documentation](https://docs.magma-maths.org/LatticesQuadraticForms/QuadraticForms/isotropic.html) qualifies maximality of its returned subspace. The rational adapter raises [Hecke's decomposition rows](https://github.com/thofma/Hecke.jl/blob/master/src/QuadForm/Quad/Spaces.jl) without transposition; the lattice owner assembles the original summand embeddings. These are source-convention checks, not runtime acceptance.

## Exact real scalar and matrix routes

`RR.of_cauchy(a)` admits a regular rational Cauchy computation with its explicit error hypothesis into the existing owned real field. `x.cauchy_sequence()` retains the presentation. Arbitrary programs without a convergence/error hypothesis are not admitted as real presentations. The owned comparison protocol decides a sign from a separating enclosure and leaves a zero relation undecided when every enclosure contains zero. `ExactRealNumber._arb_` evaluates a retained expression or Cauchy computation at requested ball precision with outward error bounds; it does not enclose a rounded MPFR value. Lazy comparisons or hashes do not decide real equality. Division requires a decided nonzero denominator; logarithms, roots and nonintegral powers require their real-domain hypotheses. `_linear_algebra_ring` and `_linear_algebra_element` pass the owned exact field into generic Sage calculations. Symbolic serialization remains a separate `SR` route and requires an available closed expression. `ExactRealNumber` remains unhashable; its `_cache_key` identifies a presentation, not mathematical equality. Finite tensor presentations use Sage's recursive cache-key protocol, including an identity token for a Cauchy presentation.

The direct `RR` constructor normalizes through `_closed_exact_real_expression`; `RR.of_cauchy` is the separate admitted-presentation route. Mathlib's [`Real.mk` and `Real.ofCauchy`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Real/Basic.html) give the formal counterpart, without creating a second real field here. Sage's [`real_lazy`](https://github.com/sagemath/sage/blob/develop/src/sage/rings/real_lazy.pyx) has deferred `LazyBinop.eval(R)` arithmetic, while `LazyFieldElement._richcmp_` permits false negatives in endpoint comparison and `LazyWrapper` does not carry a regular Cauchy error contract. The owned `RR` constructor also supplies the `OwnedOrderedRings()` placement needed by the sign route. This is structure supplied at construction, not inferred from a later comparison.

The input to `RR.of_cauchy(a)` is the actual effective infinite map $a:\mathbb N\to\mathbb Q$ with $|a(m)-a(n)|\le 2^{-n}$ for $m\ge n$. Checking a finite prefix cannot establish this hypothesis. Construction retains the map and evaluates no term. For a primitive limit, `x.cauchy_sequence()` returns that same map. Other represented values obtain a regular rational map by refining convergent Arb enclosures until the rational endpoint difference is at most $2^{-(n+1)}$ and taking the midpoint. At requested precision $p$, the private primitive evaluates $a(p+4)$ and encloses it with radius $2^{-(p+4)}$, with outward rounding on conversion to the requested ball field. The scalar stores its sequence or lazy expression, not that center or a floating-point approximation. The relation evaluator has a finite per-call precision budget. Unsupported expression evaluation errors propagate; nonfinite intermediate enclosures are refined. Termination of the signature route requires convergent enclosures for the supplied computations, not merely their admission into `RR`.

For a supplied nonsingular Gram matrix with convergent entry enclosures, `_nonsingular_real_signature` uses rational midpoint matrices and exact inverse-norm separation. It has no fixed precision cutoff and does not infer singularity when the check fails to finish. `L.diagonalization()` has a source route that searches a finite family of basis vectors and pairwise sums for a certified nonzero pivot, retains forward column changes and inverse row updates, and returns an isometry from the diagonal form to the original space. Its private quotient uses denominators already certified nonzero. The returned field Witt basis uses sign refinement and positive roots, retains the forward and inverse maps, and leaves the anisotropic complement and summand maps in the original space. `_real_representation_witness` uses the same basis for a requested norm with decided zero status. An arbitrary Cauchy-presented requested norm with undecided zero status is outside that decision. Real embeddings match diagonal signs and scale by positive square roots; equal-dimensional isometries retain reciprocal scales and the inverse pair. The direct real embedding decision compares the two endpoint signatures without constructing a difference form. These routes do not enumerate real vectors.

For a selected nonzero diagonal entry, [Sage's real-ball comparison contract](https://raw.githubusercontent.com/sagemath/sage/develop/src/sage/rings/real_arb.pyx) gives its sign when its entire enclosure is strictly positive or negative. An interval containing zero does not prove equality. In the exact real Witt route, normalization, square roots and reciprocal scales consume only these established sign and nonzero hypotheses. The returned inverse applies the retained diagonalization inverse and coordinate changes; it does not invoke a generic inverse of a matrix with Cauchy-real coefficients.

`BilinearFormModules(RR).Symmetric().signature_pair` applies to finite forms already placed in `FormModules(RR).Nondegenerate()`. It converts the original upper-triangular entries to symmetric Arb enclosures, reads outward [`RealBall.endpoints`](https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/real_arb.html#sage.rings.real_arb.RealBall.endpoints), and obtains exact rational endpoint values with [`RealNumber.exact_rational`](https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/real_mpfr.html#sage.rings.real_mpfr.RealNumber.exact_rational). `_real_witt_bases` normalizes the returned positive and negative vectors. The finite orthogonal-sum constructor retains `FormModules(R).Nondegenerate()` when every actual summand has that placement, including the empty family; absent placements still use the predicate computation. The formal construction is in `LeanCategories/Lattices/Valued/Constructions.lean`.

The signature supplier reflects the same entry enclosure across the diagonal. Rational midpoints give a symmetric matrix $A$; the maximum row sum of the rational half-widths bounds $\|G-A\|_\infty$. It doubles precision until $A$ is nonsingular and $\|A^{-1}\|_\infty\|G-A\|_\infty<1$ is certified from that bound, then returns the rational inertia. This does not decide singularity of an unplaced or degenerate form. The orthogonal-sum placement uses zero left and right radicals, without a field hypothesis or surjectivity of the adjoint. The general preservation declaration remains an audit item in [sage-extensions#238](https://github.com/dzackgarza/sage-extensions/issues/238); integral perfection-preservation theorems have stronger hypotheses and do not replace it. The selected sum keeps its original family, injections and projections, and absence of a nondegenerate placement is not evidence of degeneracy.

Gram nondegeneracy and unimodularity retain the scalar nonzero and unit propositions when undecided; finite-rank evenness combines the actual diagonal ideal-membership propositions. The scaled form $B_s(x,y)=sB(x,y)$ exists even when $s=0$ or $s=1$ is undecided. The selected construction returns the original form only when $s=1$ is explicitly true and otherwise retains its module, unscaled form and scalar. It preserves symmetry without a scalar hypothesis, unimodularity when $s$ is known to be a unit, and nondegeneracy when multiplication by $s$ is known injective on the value module. Unknown unit or zero status withholds those placements but does not assert degeneracy or prevent construction. A Cauchy presentation of zero with undecided zero status is a source specimen for this route.

The existing generic congruence route remains available when its scalar zero tests and divisions decide. It calls Sage's [`rational_diagonal_form(return_matrix=True)`](https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/quadratic_form.html#sage.quadratic_forms.quadratic_form.QuadraticForm.rational_diagonal_form) with owned `RR` coefficients; [Sage's congruence source](https://github.com/sagemath/sage/blob/develop/src/sage/quadratic_forms/quadratic_form__local_field_invariants.py) tests diagonal and off-diagonal coefficients before division. An unresolved pivot or sign propagates `NotImplementedError` instead of being coerced through `SR` or Python truth. [FLINT's Arb LDL routine](https://flintlib.org/doc/arb_mat.html) has a positive-definiteness success contract, not a general indefinite-inertia contract. The nonsingular enclosure route above needs neither a spectral routine nor general real equality.

`_matrix_determinant` uses Sage's maintained division-free [`Matrix.charpoly(algorithm="df")`](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix2.html#sage.matrix.matrix2.Matrix.charpoly) and reads the signed constant coefficient. It selects symbolic coefficients when all entries supply closed expressions and Arb ball coefficients for general Cauchy data. A ball merely containing zero stays in polynomial support; only an exact zero ball may be removed. The finite input matrix is snapshotted, so later mutation cannot change the returned real determinant. Singular matrices still have determinant values; a ball containing zero is no zero decision.

The maintained division-free characteristic-polynomial routine normalizes an intermediate coefficient polynomial before adding its monic term. Over owned exact reals that normalization could demand an undecidable zero test: the trace coefficient of $\operatorname{diag}(x,-x,1,-1)$ separates the cases. In the private ball polynomial, [`RealBall.__bool__`](https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/real_arb.html#sage.rings.real_arb.RealBall.__bool__) is only a polynomial-support test: it removes an exact zero ball, not a ball whose interval contains zero. For fixed rank, convergent input balls make every polynomial coefficient enclosure converge. The determinant's returned regular Cauchy map uses rational midpoints after endpoint width is at most $2^{-(n+1)}$. This works for singular input without asserting nondegeneracy.

Source specimens for `_arb_` check `3<pi<22/7`, the enclosure of `sqrt(2)` squared containing two, and exact zero. The regular sequence `1+2^-n` checks arithmetic, division, positive roots and the mixed-sign signature. Separating matrix specimens include the off-diagonal pi plane, a positive matrix with determinant `2^-512`, the empty form, a singular diagonal form, a trace-zero rank-four Cauchy form and a singular Cauchy determinant. Witt specimens include the pi/negative-one form, its form equation and two inverse laws, isotropic and norm witnesses, sign vectors, embedding endpoints and exclusion by opposite sign. Their mathematical values are in the real chapter. These source specimens remain unexecuted under DEV-58 unless a later status below explicitly records execution.

The nonalgebraic specimen and its inverse/form assertions remain unexecuted under DEV-58:

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

## Integral bound and provider routes

`L.square_coordinate_bound(a)` evaluates the definite inverse-Gram coordinate formula in the selected frame with exact [rational matrix inversion](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_rational_dense.html) and [integer square root](https://doc.sagemath.org/html/en/reference/rings_standard/sage/rings/integer.html#sage.rings.integer.Integer.isqrt); no approximate square-root rounding enters. The optimized definite shell delegates to Hecke's inclusive [`short_vectors(L,a,a)`](https://github.com/thofma/Hecke.jl/blob/v0.39.22/src/QuadForm/ShortVectors.jl#L61), which returns nonzero vectors up to sign in the original coordinates; the adapter restores both signs. Hecke's [enumeration](https://github.com/thofma/Hecke.jl/blob/v0.39.22/src/QuadForm/Enumeration.jl#L769) uses rational pseudo-Cholesky arithmetic after Gram LLL reduction and transports vectors through the retained basis matrix. The old fixed-precision PARI `forqfvec` error is not an empty-shell decision. Reflective roots additionally satisfy the exact divisibility condition on each coordinate of twice the Gram product. Hecke's [`minimum`](https://github.com/thofma/Hecke.jl/blob/v0.39.22/src/QuadForm/ShortVectors.jl#L134) supplies the finite nonzero minimum route; the negative-definite public convention gives the square closest to zero, and rank zero raises `ValueError`. The large scaled definite-shell provider specimen remains unexecuted under DEV-58.

That pending specimen uses $G=2^{34}\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)$ and $a=2^{35}$. Its shell is $\pm e_1$, $\pm e_2$, and $\pm(e_1+e_2)$ in the original coordinates. It also checks an empty shell at $a=1$, minimum $2^{35}$, the negative-definite minimum $-2^{35}$, and the rank-zero exception. The recorded old PARI route raises a precision error on this input; this is a source specimen, not an executed provider result.

`Lattices(ZZ).integral_representative_coefficient_bound(n,D)` evaluates the fully numeric bound from rank and determinant; `L.integral_representative_coefficient_bound()` supplies those invariants from a lattice. Neither constructs a representative or bounds its change-of-basis matrix. `T.integral_completion_coefficient_bound(n,det_G)` bounds the Gram height of a completion preserving specified columns, including nonprimitive columns; it does not bound those columns. `Lattices(ZZ).integral_isometry_coefficient_bound(n,h,k)` evaluates Calderon's rank-at-least-three equivalence bound without deciding equivalence or returning a matrix. `T.integral_embedding_coefficient_bound(L)` returns a box radius meeting each target-isometry orbit of embeddings. The definite and rationally split binary branches bound every embedding; the nonsplit binary norm-orbit branch reuses `binary_fixed_norm_representatives` and PARI's [`qfbsolve`](https://pari.math.u-bordeaux.fr/dochtml/html/Quadratic_number_fields_and_binary_quadratic_forms.html#qfbsolve) with flag three, including imprimitive solutions. The higher-rank branch uses completion and evaluated isometry bounds. A finite box proves exclusion for arbitrary decidable filters only when it contains every embedding; an orbit box suffices for decidable target-isometry-invariant filters. The sharper Li-Margulis numerical constant remains unevaluated; the alternative bound is evaluated in the book.

The nonsplit binary provider is also exposed through [Sage's `BinaryQF.solve_integer` wrapper](https://doc.sagemath.org/html/en/reference/quadratic_forms/sage/quadratic_forms/binary_qf.html#sage.quadratic_forms.binary_qf.BinaryQF.solve_integer). Its finite transversal includes imprimitive norm solutions. Passing from special orthogonal to full orthogonal orbits may merge representatives but cannot omit an orbit. Coordinate filters changed by target isometries need a separate full-embedding bound.

`FramedFreeModules.FinitelyGenerated.ParentMethods.coordinate_subset` builds a finite Cartesian coordinate subset in the selected basis and retains its inclusion. `LatticeEmbeddingMor.with_generator_images_in` tests every upper-triangular Gram equation for each tuple and retains original embedding endpoints; unknown equations are refused, not counted false. The returned finite set accepts `condition_set`, and its inclusion remains available. The complete `ZZ`/`QQ` embedding iterator is a separate fair coordinate enumeration; no empty infinite filtered search is inferred from waiting. The definite six-embedding and constrained two-embedding source specimens, split and nonsplit binary specimens, completion and orbit-bound specimens keep their individual status under DEV-58 or terminal T below. Finite bounded nonprimitive and primitivity-exclusion specimens have executed as recorded below.

The definite six-embedding and positive-filter specimens remain unexecuted under DEV-58:

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

The bounded nonprimitive specimen uses the finite subset and predicate constructions:

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
| Anisotropy and nonzero isotropic witnesses | `form_modules.py`: `is_anisotropic`; `lattices.py`: `is_isotropic`, `isotropic_vector`; rational PARI decision and real congruence routes | Exact ZZ/QQ, AA and applicable RR cases have source routes; general real-oracle zero decisions are not supplied |
| Witt index and decomposition | `lattices.py`: `witt_index`, `witt_decomposition`; exact rational isotropy splitting and real congruence/sign/root computation | Regular Cauchy admission, nonsingular signature and returned congruence isometry have source routes; Witt-basis sign/root normalization has a source route; nonsingular norm-witness normalization has a source route with decided requested-norm zero status; real Witt decomposition retains explicit inverse coordinate maps and actual summand maps |
| Norm fibres, including zero | `form_modules.py`: `square_fibre`, `elements_of_norm`; `lattices.py`: `elements_of_norm`, `representation_vector`; subset-owner lazy choice | Original equalizer and inclusion; canonical zero; finite integral shells where proved finite; supplied finite nondegenerate ZZ/QQ/AA/RR fibres can select a fresh point through the existing solver without ambient enumeration. Unavailable scalar decisions and failed solvers propagate |
| Scalar extension of objects and arrows | `FormBaseChanges`, `FormedModuleMorphism.base_change`, `LatticeIsometryMethods.base_change`, module scalar-extension functor | Original source, actual ring map and unit retained; both formed-arrow components and isometry inverse pairs retained. Finite unimodularity survives all unital maps; over a target domain, a nonzero mapped Gram determinant establishes nondegeneracy. Scalar values over a quotient ring use its regular module for the internal Mor while public pairings and Grams remain ring-valued. Arbitrary value-module extensions remain outside the current computation |
| Embedding sets, decisions and witnesses | `lattice_morphisms.py`: embedding Mor, `_emptiness_decision`, `an_element`, integral-overlattice factorization, rational Witt criterion and real inertia matching | Original endpoints retained. Real witnesses refine known nonzero signs; real isometries retain reciprocal-scale inverse matching. Rational-denominator, finite-empty and AA witness specimens have executed; broader backend coverage remains under terminal T |
| Complete countable enumeration | Finite free-module and embedding `__iter__` over ZZ/QQ | Each candidate must occur finitely far into the enumeration; asking for a next satisfying element need not terminate; no real enumeration is claimed |
| Finite constrained search | `coordinate_subset`, `Emb.with_generator_images_in`, `condition_set` | Exact pairing equations and the additional predicate must be decidable; finite search alone excludes only its specified box |
| Effective integral bounds | Definite inverse-Gram bound, representative/completion/isometry/embedding coefficient bounds, split binary factors and nonsplit binary norm orbits | The embedding bound meets every target-isometry orbit, hence covers decidable invariant constraints; arbitrary noninvariant constraints require an applicable argument and have no uniform solver below |
| Sampling | `finite_ordered_sets.py`: `random_element` on the selected finite support | Uniform finite-support distribution; empty support is rejected; no infinite uniform distribution or completeness inference |
| Exact solving, kernels and arithmetic predicates | Module morphism `preimage`, `kernel`, `cokernel`, `is_primitive`; `AffineModuleFibres.base_point`; lattice `div`, `bezout_partner`, `hyperbolic_partner` and its locus | Original-ring image solving and full kernel inclusions retained; affine points lift the combined equation and project to the original parameter module. Partner loci use lazy solver-backed choice under known hypotheses. Selected integral and represented-real preimage/kernel specimens have executed; the rest remain under terminal T |
| Perpendiculars and supplied decompositions | `orthogonal_complement`, `orthogonal_splitting`, `orthogonal_decomposition` | Retain the supplied first embedding and full kernel inclusion; direct-sum hypotheses remain essential |
| Target hyperbolic index and maximal splitting | `lattices.py`: `hyperbolic_index`, `maximal_hyperbolic_index_splitting`; general `Emb` decision and witness; `orthogonal_splitting`; field `witt_decomposition` | The integral route tests actual embeddings of `U^r` in descending order and returns the isometry; field routes use the Witt decomposition. Degenerate forms first pass to a nondegenerate radical quotient, then lift the selected summand into the original lattice. Focused zero, split, mixed, scaled, odd and degenerate specimens have executed; the broader terminal suite remains open |

**The old genus test and the specified lattice.** The historical
`integral_hyperbolic_index` implementation compared the genus of `L`
with that of `U^r + M`. This is necessary for a splitting, but equality
of genera does not itself construct or identify an isometry of `L`.
The applicable uniqueness theorem has hypotheses: Peters, *Primitive
lattices*, [Theorem 2.3](https://www-fourier.ujf-grenoble.fr/~peters/Articles/PrimLats.pdf)
(citing Nikulin and Kneser), states that an indefinite even lattice of
rank `n` is alone in its genus if its discriminant group has at most
`n-2` generators; for an odd lattice the bound is `n-3`. Since `U^r`
is unimodular, `U^r + M` has discriminant length at most `rank(M)=n-2r`.
Thus this theorem converts a positive genus comparison into a splitting
for even lattices with `r>=1`, and odd lattices with `r>=2`. It does not
cover the general odd `r=1` case when the complementary discriminant
length is `n-2`. No assertion about that case follows from this theorem.

The legacy method now delegates to the constructive `hyperbolic_index`.
A primitive divisibility-one isotropic vector with an integral hyperbolic
partner splits off a visible `U`; repeating on the actual complement
supplies a lower bound and an isometry. In an even lattice the partner
correction is automatic; in an odd lattice the existing norm-congruence
computation decides it. Every splitting `L ≅ U^r ⊥ M` also gives
`A_L ≅ A_M`, hence `length(A_L) ≤ rank(M) = rank(L)-2r`; a full-rank
splitting requires `L` even. These necessary bounds exclude candidate
ranks before computation. If the constructed index reaches the resulting
upper bound, it is maximal. For every remaining larger candidate `r`,
`Emb(U^r,L).is_empty()` uses the finite integral-overlattice and
primitive-embedding decision, and the first affirmative Mor supplies
an actual embedding. As `U^r` is
unimodular, the hyperbolic-summand projection in the linked book makes that embedding a direct summand;
`orthogonal_splitting()` returns its complement and the isometry over
the original ring. The lower candidates are unnecessary after the first
success, and every larger candidate has been excluded in the specified
lattice. For index zero the isometry has domain `U^0 + L`.

### Source implementation reconciliation

The dependency-only source assignment is reconciled against the public
call paths listed above. The implemented surface includes anisotropy and
isotropic witnesses; scalar extension of objects and both formed-arrow
components; field Witt indices and decomposition isometries; norm fibres
with original inclusions and applicable fresh point selection; embedding
sets, complete decisions and witnesses in the stated regimes; constrained
finite subsets; fair ZZ/QQ enumeration; evaluated integral bounds; uniform
sampling on a selected finite support; exact linear solving, kernels,
perpendiculars and splitting maps for supplied summands. The preceding
proofs, source-convention checks and owner-local specimens state each
route's hypotheses, returned maps, zero-rank behavior and limits.

This reconciliation concerns implemented computations and their wiring.
It does not assert that source inspection proves their correctness.
The focused specimens for this hyperbolic plan have now executed:
definite and split norm fibres, fresh QQ/AA/RR norm witnesses and RR
norm exclusion, QQ/AA/closed-RR Witt isometries and inverse laws,
represented-RR coordinate solving and integral/real kernels, scalar
extension of formed arrows and isometries, finite constrained embeddings
including invariant primitivity exclusion, finite sampling, and actual
integral maximal splittings at indices zero, one and two, including odd
and mixed-parity complements. A regular-Cauchy RR specimen verifies decomposition
endpoints and summand ranks; its symbolic Gram equality remains undecided.
The rest of the dependency index remains with `terminal-session`, [sage-extensions#238](https://github.com/dzackgarza/sage-extensions/issues/238).
The general zero-radical preservation
theorem is now `isNondegenerate_of_indexedOrthogonalPairing` at the
`lean-categories` bilinear-module owner, including the empty sum; its
lattice corollary is `indexedOrthogonalSum_isNondegenerate`. The historical
genus-based integral index question is resolved by the cited uniqueness
theorem with its stated range and by using an actual embedding decision
in the remaining range.

The boundary is mathematical rather than an omitted promised solver:
there is no exhaustive sequential enumeration of an uncountable real
locus, no uniform arbitrary-real zero decision, and no uniform emptiness
solver for arbitrary programmable embedding filters. The source retains
these sets and propositions. Effective search and exclusion use precisely
the additional hypotheses proved in the book. Arbitrary value-module scalar
extension lies beyond the scalar-valued lattice computations required by
this index. `hyperbolic_index` and
`maximal_hyperbolic_index_splitting` now compose the listed constructions;
the focused execution above does not close terminal T.

### Invariants, predicates, and decomposition morphisms

In this subsection $T$ is a finite-rank symmetric bilinear module over
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

**Construct the locus before selecting an enumeration.** The general
norm fibre is the equalizer of $q:L\to R$ and the constant map with
value $a$. Its defining equation and inclusion require no decision of
the signature or radical of $L$. The `vectors_of_square` entrypoint now
returns this existing locus immediately over nonintegral bases, before
asking about definiteness. Its special finite shell computations remain
integral computations. In particular, a rank-one RR form with an
undecided Cauchy-zero Gram entry still has a norm-zero fibre, its original
inclusion, and the canonical zero point. Its fibre is the same object
returned by `elements_of_norm(0)`, without requiring a decision that the
form is singular or definite. This supplies a source specimen for locus
construction with undecided inertia; it does not claim enumeration of
all real points.

**Fresh norm-fibre point selection.** A predicate-subset realization can
now retain a private, possibly failing point computation. This is
computational data, not a mathematical map from a singleton into the
subset: such a map would assert nonemptiness, which is not known merely
because a solver is available. Retaining the computation evaluates no
point and makes no nonemptiness decision. Choice first returns an
admitted point, then invokes the computation if present, and otherwise
requests the existing ambient enumeration. Evaluation failures propagate;
they are not interpreted as emptiness or as successful admission.

For a supplied positive finite-rank nondegenerate lattice over ZZ, QQ, AA or represented
RR with scalar-valued form, the norm-fibre constructor retains a
computation invoking the existing `representation_vector(a)`. On success,
the subset owner admits that returned solution in the original equalizer,
without re-deciding the equation constructed by the solver. The original
fibre and inclusion remain unchanged; later choice requests reuse the
actual point. Canonical zero keeps its immediate route. Other forms
retain their prior search or unavailable computation. Arbitrary requested
real zero status can still be unavailable, and no solver is inferred
for arbitrary predicate subsets. The fresh positive real line specimen
requests norm three without manual admission; a negative norm exercises
failure without retaining a point or changing the emptiness proposition.
Their execution remains deferred with the other source specimens.

Rank-zero fibres retain their existing finite selection route. The
condition-set constructor may realize a subset of a finite enumerated
universe directly as an ordered finite set; that realization does not
need the predicate engine's private point computation. Accordingly the
norm solver hook is installed only in positive rank over the stated
infinite scalar rings. Partner-locus solver hooks likewise require an
infinite exact field (or the stated primitive integral case); finite
fields retain their original finite search. The zero-space nonzero-norm
specimen checks construction and exclusion of its sole ambient point
without requiring the private predicate-engine interface.

The integral route uses the existing `representation_vector` computations,
not exhaustion of an infinite norm fibre: finite definite shells, the
binary norm-equation computation, or the integral-overlattice/embedding
route in higher indefinite rank. For the nonsplit plane
$q(x,y)=x^2-2y^2$, the norm-four fibre has $(2,0)$ as a point, which the
lazy choice route can select without enumerating the whole fibre. The
norm-three fibre is empty: if $y$ is even, $2y^2\equiv0\pmod8$ would
force $x^2\equiv3\pmod8$; if $y$ is odd it would force
$x^2\equiv5\pmod8$. Neither is a square residue. The source specimens
request these two fibres afresh, retain the actual integral inclusion
and selected point in the affirmative case, and propagate the existing
solver's exclusion in the negative case. These are point-selection
computations on norm fibres, not computations of a maximal hyperbolic
summand.

**Element equations retain predicates.** For a supplied vector $v$,
`v.is_isotropic()` denotes $q(v)=0$, `v.is_orthogonal_to(w)` denotes
$b(v,w)=0$, and `v.represents(a)` denotes $q(v)=a$. These are scalar
equations, distinct from the existential representation predicate on a
whole module. Their shared formed-module implementation now returns
the scalar equations themselves: a decided equation gives a Boolean,
while an undecided equation remains the original predicate. It does not
coerce an undecided equation to a Python truth value. A rank-one real
form whose Gram entry is the regular Cauchy presentation $2^{-n}\to0$
supplies source specimens for all three undecided equations. When a
lattice's nondegeneracy is undecided, its existential isotropy method
now also uses the common nonzero norm-zero fibre proposition instead
of falling through to `None`. The corresponding anisotropy predicate
remains the logical negation at its shared owner.

The same rule applies to real scalar units. In a field, $a$ is a unit
exactly when $a\ne0$; the exact real scalar's `is_unit()` now returns
that predicate directly. Thus a Cauchy presentation with undecided zero
status has undecided unit status, rather than a Boolean coercion failure.
The finite framed form's unimodularity computation likewise returns the
unit predicate of its determinant without forcing a Boolean. The
rank-one Cauchy-zero Gram specimen retains an undecided unimodularity
proposition. This also lets the existing regular-scalar computation read
the unit predicate safely before its integral-domain nonzero criterion.
The free-form specialization also honors a supplied unimodular placement
before requesting its determinant. This matters even in rank one:
the regular sequence $2^{-8192}+2^{-n}$ presents the positive real
$2^{-8192}$, hence a unit, while the ordinary bounded zero decision may
not resolve that fact. A form supplied as unimodular already has the
required hypothesis; the predicate returns true without re-solving it.
This is separate from its private certifying predicate, which still
computes from the actual form when explicitly requested.

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
$T=U^{\perp r}$ makes primitivity and splitting automatic by the hyperbolic-summand splitting proposition in the linked book.

An element is the map $j$ itself, not its image alone or its equivalence
class under an orthogonal-group action. Thus constructing and filtering
$\operatorname{Emb}_R(T,L)$ retains source, target and evaluation. Conditions
may specify images of given vectors, orthogonality to a given submodule,
integral image after rational base change, or primitive image. Fixed images
are fibres of evaluation maps; simultaneous conditions are intersections
of subsets. A quotient by a group action is a separate construction and
is not needed by the bounded search in this note.


The field embedding criterion and proof are in [Norm fibres and embedding loci](../../writing/lattice-theory/hyperbolic/norm-fibres-and-embedding-loci.md#sec-embedding-existence).

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


The saturation proposition and proof are in [Norm fibres and embedding loci](../../writing/lattice-theory/hyperbolic/norm-fibres-and-embedding-loci.md#sec-embedding-existence).

The family of integral overlattices is finite and includes $T$ itself.
It is computed by `T.integral_overlattice_inclusions()`, through
bilinear-isotropic subgroups of the discriminant bilinear form. This
uses integrality, not evenness; an even source can have an odd integral
overlattice. The correspondence and its inclusions are the constructions
in `LeanCategories/Lattices/Valued/Gluing.lean`.

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


The ternary obstruction and its congruence proof are in [Norm fibres and embedding loci](../../writing/lattice-theory/hyperbolic/norm-fibres-and-embedding-loci.md#ex:borovoi-ternary-obstruction). The source specimen remains below.

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
enumeration of its universe. At the common formed-module owner,
`square_fibre(0)` now retains the canonical zero vector using $q(0)=0$.
Consequently a fresh `L.elements_of_norm(0)` supplies zero and decides
nonemptiness without manual admission or real-vector iteration. The
symmetric-bilinear category inherits this same norm-fibre construction;
it has no separate realization that loses the chosen zero.
For nonzero $a$, one can admit a computed `L.representation_vector(a)`
into `L.elements_of_norm(a)`. Subsequent point selection uses
that actual admitted vector and the fibre inclusion, including over RR.
This supplies no iterator, cardinality or sampling distribution. With no
retained member the complete countable search still has its stated
termination limits. Pending real positive-subset and norm-fibre specimens
exercise this distinction without enumerating real points. The zero-norm
specimen requests a point directly from the fresh fibre, checks its
inclusion and nonemptiness, and checks that `square_fibre(0)` retains the
same equalizer object. It remains unexecuted under DEV-58.

The real scalar's cache integration is a separate requirement of this
existing cached construction. `ExactRealNumber` remains unhashable because
its equality is partial. It now implements Sage's documented
[`_cache_key` protocol](https://doc.sagemath.org/html/en/reference/misc/sage/misc/cachefunc.html)
using its actual parent and stored exact expression. That key identifies
the presentation used for a cached computation; it does not decide real
equality, and two different expressions for the same real may use
different entries. No new cache or equality algorithm is introduced.

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


The halting reduction for unrestricted filtered emptiness is in [Norm fibres and embedding loci](../../writing/lattice-theory/hyperbolic/norm-fibres-and-embedding-loci.md#prop:arbitrary-embedding-filter-undecidable).

This is an obstruction to a uniform decision, not to the subset itself,
its inclusion, exact membership, or complete countable enumeration.
Finite boxes decide their own restrictions. The invariant-constraint
theorem applies when its invariance hypothesis holds; the predicates
$P_C$ need not satisfy it. A proposed solver for a particular noninvariant
condition still needs its own mathematical hypotheses and termination
argument. The dependency index does not require an impossible universal
extension of `is_empty()` to every programmable predicate.

### Linear algebra, arithmetic, and retained maps

**Fresh choice in the hyperbolic-partner locus.** The partner locus is
the norm-zero equalizer inside the affine pairing fibre. It now retains
the existing `hyperbolic_partner` computation lazily when isotropy is
explicitly known and the input is either over an exact field of
characteristic different from two, or primitive over ZZ in finite rank.
It evaluates no partner while constructing the locus. The field solver
uses a preimage of one under the pairing and the exact quadratic
correction; the integral solver uses the Bezout partner and, if needed,
its complete finite kernel-residue computation. A successful returned
point is retained by the subset owner with the original affine-fibre
inclusion. Solver failure propagates without admitting a point or
changing an emptiness proposition. Inputs without these known hypotheses
keep their defining locus and existing selection capabilities. The
solver does not call the locus's choice operation, so this composition
does not recurse through choice. Integral and rational fresh-locus
specimens request a point without manual admission; their execution
remains deferred. This is point construction for a supplied vector,
not a search for a maximal hyperbolic summand.

| General construction or computation | Output needed by the splitting algorithm |
| --- | --- |
| Symmetric bilinear forms, evaluation and restriction | The actual form on each module and submodule, with the associated norm map |
| Scalar extension along a specified ring map | Extended modules, forms and maps; the original integral lattice remains specified when testing integral image |
| Finite orthogonal sums and hyperbolic planes | The formed sum with its summand inclusions and projections; the rank-zero case is included |
| Linear maps and their composition, inversion and evaluation | Embeddings, isometries and composed changes of basis in the original module |
| Kernels, images, preimages and restrictions of linear maps | The submodule with its inclusion; its induced form, rather than just its dimension |
| Orthogonal complement of a specified embedding or submodule | The kernel of the pairing map to its module dual, with inclusion and restricted form |
| Orthogonal splitting of a supplied hyperbolic embedding | The isometry obtained from its inclusion and the complementary inclusion, whose inverse is $x\mapsto(x-\pi_M(x),\pi_M(x))$ with $\pi_M$ given by the linked hyperbolic-summand projection |
| Exact linear solving, including affine solution sets | A solution of $B(e,v)=1$, or all solutions $v_0+\ker B(e,-)$ with their inclusion in the module |
| Congruence diagonalization retaining its isometry | Diagonal form and transport maps, for the real and rational routes |
| Integer kernel and linear-equation solving | A full integral kernel basis and Bézout solutions; Smith or Hermite computations retain their transformations |
| Divisibility, primitivity and parity | The ideal $B(e,L)$; primitivity of a submodule via torsion-freeness of the quotient; norm modulo $2$ |
| Exact scalar arithmetic, equality, sign and positive square roots where applicable | Valid pivots, normalization and equation comparisons in the chosen exact presentation |
| Rank and determinant | Dimension bounds and the determinant input to the integral representation bound |
| Integer factorization, valuations and rational-square decision | Bad primes, local precision, and binary rational isotropy |
| Finite residue rings, finite products and modular arithmetic | Complete finite local isotropy tests with primitive residue vectors |
| Effective representation bounds | A usable integer bound for the relevant form representation problem, with its hypotheses; the evaluated higher-rank embedding bound, the definite inverse-Gram bound and the two binary bounds are evaluated integral instances; the sharper Li–Margulis expression retains its unevaluated constant |
| Constructive integral equivalence and bounded representatives | The alternative complement-enumeration route only; a successful comparison returns the isometry |

For clarity, the orthogonal-complement row uses the map
$L\to S^\vee$, $x\mapsto(s\mapsto B(x,s))$, where $S\hookrightarrow L$
is the specified submodule and $S^\vee$ its module dual. Its kernel is
$S^\perp$. This construction exists even when $S$ is degenerate; the
direct-sum conclusion needs the hypotheses of the linked hyperbolic-summand splitting proposition.
Over $\mathbb Z$, a primitive image means that the quotient module is
torsion-free, not just that one selected vector has coprime coordinates.
For a primitive vector, retain the map $R\to L$, $1\mapsto v$, and require
both injectivity and torsion-free cokernel. Testing only the inclusion of
its image loses injectivity: the zero submodule is primitive although the
zero vector over $\mathbb Z$ or a field is not primitive. The vector's
`is_primitive()` operation now delegates this map from the free module of
rank one to the general module-morphism operation.

#### Scalar extension of the maps, not only the forms

**Preserved finite-free form hypotheses.** In a selected finite basis,
scalar extension sends a Gram matrix $G$ to $\varphi(G)$ and sends its
determinant to $\varphi(\det G)$, by the determinant's polynomial formula.
If $\det G$ is a unit, its image is a unit under every unital ring map;
thus supplied unimodularity is retained without a flatness hypothesis.
For a finite scalar-valued form over an integral domain, nondegeneracy
is equivalent to a nonzero determinant. An injective ring map between
integral domains preserves that nonzero determinant, so the source's
supplied nondegeneracy is retained when injectivity is known. Unknown
injectivity supplies no such shortcut. These placements are now
transported at `_formed_module_base_change`, along with the existing
source and actual ring map. No claim is made for arbitrary infinite
duals. Reduction of $\langle2\rangle$ modulo two gives the zero form
and shows why nondegeneracy cannot be transported along every ring map;
the unimodular plane $U$ remains unimodular under the same reduction.
The rational extension and both reduction cases have source specimens.

For scalar-valued formed modules over a commutative ring $R$, a morphism
is a pair $(f,h)$ with $f:M\to N$ and $h:R\to R$ linear and
$h(B_M(x,y))=B_N(fx,fy)$. A lattice morphism has $h=1_R$.
For a ring map $\varphi:R\to S$, scalar extension sends both maps to
$f_S=1_S\otimes f$ and $h_S=1_S\otimes h$, using the canonical
identification $S\otimes_RR\simeq S$ for the values. The formal
operation is `baseChangeBilWForm` in
`LeanCategories/Lattices/Valued/BaseChange.lean`; its two defining
components are the scalar extensions of the module and value maps.

The scalar-extension proof is in [Norm fibres and embedding loci](../../writing/lattice-theory/hyperbolic/norm-fibres-and-embedding-loci.md#sec-hyperbolic-base-change-maps).

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

**Retain the returned coordinates without new decisions.** After a
linear solver has produced a coordinate vector, constructing its point
requires no further nonzero test on each coordinate. The module
preimage route now passes the entire labelled coordinate family to
`linear_combination`, whose scalar storage discards only coefficients
explicitly equal to zero. Previously a Python `if coefficient` could
refuse an undecided real coefficient after solving had succeeded.
For the invertible triangular map with columns $(1,0)$ and $(1,1)$,
the target $(1+t,1)$ has preimage $(t,1)$. A Cauchy presentation
$t=\lim 2^{-n}=0$ may have undecided zero status, which does not prevent
retaining it as the first coordinate of that returned preimage. The
source specimen checks this distinction and the original parent;
execution remains deferred. The solver's own pivot applicability
conditions remain unchanged.

The finite-span constructor now follows the same rule when it builds
its coordinate map and raises a solved lift: all coefficients are passed
to the existing module constructor. To check whether a candidate lies
outside its finite coordinate window, it reads the finite retained
coefficient family rather than enumerating the exact support. Known
nonzero outside coordinates exclude membership; unknown outside zero
equations report an unavailable decision. Membership in the zero span
likewise distinguishes true, false and undecided equations. For a finite
ambient framing the coordinate window is the whole framing, so no exact
support decision is needed. The cyclic span of $(1,t)$, for a
Cauchy-presented zero $t$, has an inclusion retaining that coefficient;
its source specimen checks construction and the original endpoint.
The lattice column-matrix transport similarly retains all forward and
inverse coefficients after inversion. These changes add no rank or
zero decision procedure and do not turn undecided span membership into
absence.

The kernel audit found the same filter at both stages of coordinate
transport: raising the maintained matrix kernel basis into the
coordinate module, and transporting it into the original domain.
Both now retain every labelled coefficient. For the row map
$B(x,y)=x+ty$, the kernel is generated by $(-t,1)$ for every real $t$:
the displayed vector maps to zero, its second coordinate makes it
nonzero, and every solution has $x=-ty$. Thus deciding whether $t=0$
is unnecessary for these transports. The Cauchy-zero source specimen
checks the rank-one kernel, its original-domain inclusion and the
retained undecided first coordinate. This does not alter the maintained
kernel solver or make general real rank decidable.

The remaining coordinate path was inspected from `_engine_matrix` through
the exact-field positional solver and the raising helper
`_morphism_from_engine_matrix`. Matrix serialization reads each full
column once and retains every entry over the selected exact coefficient
ring. The field solver returns all solution coordinates; inverse-matrix
raising passes all rows to the original matrix Mor with reversed
endpoints. Rank-zero matrices retain their explicit row and column
counts. No further coordinate truth filter occurs in these stages.
The other inspected sparse filters in the module file apply to integral
order coordinates or integer relation matrices, where equality is
decidable; they do not need a real-predicate change. This completes the
source reconciliation of coordinate transport in the selected kernel,
preimage, finite-span and matrix-inverse routes. It does not establish
the availability of their scalar rank/pivot decisions, prove the
computations correct, or execute their mathematical specimens.

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
This repairs a source obstruction for RR: the former route
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

The rational Witt adapter was also checked against the maintained
[Hecke decomposition source](https://github.com/thofma/Hecke.jl/blob/master/src/QuadForm/Quad/Spaces.jl):
its anisotropic and hyperbolic matrices use rows in the original space;
successive hyperbolic pairs have zero squares and mutual pairing one.
The adapter raises those rows without a transpose, and the lattice owner
assembles the actual summand embeddings. This is a source convention
check, not evidence of mathematical correctness from the engine.

The subsequent rational call path is `witt_decomposition` ->
`subobject_on` -> `_span_basis_elements` ->
`_lattice_subobject_on_basis` for the anisotropic factor. The span
normalization can replace the solver's anisotropic basis, but retains
the same subspace; the subobject constructor evaluates the original
pairing on the resulting basis and retains its actual ambient inclusion.
Hyperbolic vectors are raised directly, in the solver's successive pair
order. `orthogonal_decomposition` assembles that hyperbolic embedding
and the complementary inclusion into the original lattice. Its inverse
uses the module's coefficient ring and the actual original endpoints.
This supplies the required decomposition isometry, without requiring
the complement to retain a particular coordinate matrix from the solver.

For `j.orthogonal_splitting()`, the same assembly instead receives the
original supplied embedding as its first leg and the full perpendicular
inclusion as its second. Over ZZ, the perpendicular uses the full integer
kernel of the pairing matrix. The generic inverse cannot replace an
integral direct-sum hypothesis with rational invertibility: its matrix
coefficients must raise into the original scalar ring. Thus the existing
index-two example fails to give an integral splitting, whereas its QQ
extension does split. These are inspected construction paths; their
mathematical specimens keep their stated execution status.

Rank zero now has a shared direct construction: the Witt index is zero,
and the decomposition domain is the orthogonal sum of the empty
hyperbolic space and the original zero space. The two empty generator
maps are retained as an inverse pair at the module core. Both inverse
laws hold because each space has only its zero point; the zero form is
anisotropic vacuously. The construction preserves the scalar field and
both factor maps, without invoking a rational decomposition engine.

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
| Rational splitting | Exact isotropy decision and construction of one nonzero isotropic vector, rational affine solving and kernels | Local finite tests plus exhaustive witness search as proved in the linked book, or a maintained rational quadratic-equation solver |
| Integral bounded embedding search | A valid effective representation bound, finite candidate enumeration, exact pairing comparisons and full integer kernels | Rational Witt index for pruning; a maintained embedding solver with a complete existence decision can replace the box search |
| Integral splitting from a supplied isotropic vector | Divisibility and affine integral solving, parity on the kernel, hyperbolic-pair completion | Useful when such a vector is already known; does not on its own prove maximality |
| Integral complement enumeration | Bounded form representatives and constructive integral equivalence | An alternative to the direct embedding search, not an additional mandatory dependency |

Thus the reusable mathematical surface includes anisotropy, norm fibres,
embedding subsets and decomposition isometries, while each computation selects
the search or solver capabilities its hypotheses justify. No route requires
every set to be enumerable, and no predicate-defined set becomes decidable or
searchable solely because its defining mathematical expression exists.


## Using the reusable constructions

The dependency interfaces below retain mathematical objects and maps. Their
execution obligations remain open under the repository's source phase in
the [issue tree](https://github.com/dzackgarza/research/issues/46); these examples do not certify an implementation.
The target integral index and maximal-splitting computations consume these
reusable constructions and return the actual isometry and its maps.

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
square roots; the `RR` route uses the same construction when
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
overlattice classification route. The sharper Li–Margulis constant remains
needed for that particular sharper expression. The evaluated alternative
The evaluated alternative now gives a direct integer box bound in rank at least three, while the
classification route supplies a separate unconstrained existence decision.
The evaluated bound meets every target-isometry orbit, so decidable
invariant predicates also admit complete finite exclusion. Other predicates
require their own termination argument.

The interfaces are defined at the [lattice owner](../../sage_extensions/categories/lattices.py),
[embedding-space owner](../../sage_extensions/categories/lattice_morphisms.py),
[finite free-module owner](../../sage_extensions/categories/modules/framed/framed_free_modules.py)
and [finite enumerated-set owner](../../sage_extensions/categories/sets/finite_ordered_sets.py).
The [formed scalar-extension construction](../../sage_extensions/categories/modules/framed/formed/form_modules.py)
retains the original lattice and scalar map.
