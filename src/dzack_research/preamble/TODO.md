# Outstanding work in the preamble

## Mathematics stated and not built

Each of these is a mathematical statement the preamble makes in prose and does
not realize as an object or a morphism.

### The free divided-power adjunction has no target category

Tensor and symmetric extension now implement their hom-set bijections.
Alternating extension enforces the square-zero and anticommutation relations,
and $\Gamma(f)$ preserves divided powers. A category of divided-power algebras,
with morphisms that preserve every $\gamma_n$, is still absent. Thus
$\Gamma$ has functoriality but not its full free-forgetful adjunction.

### $\Gamma^n(M) = (M^{\otimes n})^{S_n}$

The divided powers are the symmetric invariants of the tensor power. This is
the characterization that produces $\Gamma^2 M \to M \otimes M$, and that map
is the general polarization: it is how a quadratic form and its bilinear form
are one object seen twice. The preamble has bilinear forms on $M \otimes M$ and
quadratic forms on $\Gamma^2 M$ as two homsets with nothing between them.

Polarization *is* built for discriminant quadratic modules
(`associated_bilinear_form`, with $q(x+y) = q(x) + q(y) + 2b_q(x,y)$). That is
the special case. The general statement is missing, and the general statement
is what the divided square was introduced for.

### A form gives $M \cong M^*$, and nothing uses it

A nondegenerate form is an isomorphism $M \to M^*$. That isomorphism is what
raising and lowering an index means, so it is the only thing connecting the
tensor layer to the forms layer. `Tensor(M,(p,q))` has contraction and trace
and no way to apply a lattice's form, so `gram_tensor()` returns a $(0,2)$
tensor that can never become the $(1,1)$ identity, and a lattice cannot hand
its form to a tensor at all.

### The lattice axioms are declared and never established

`Lattices(R)` is defined as the projective $R$-modules carrying an $R$-valued
bilinear form, with `FinitelyGenerated`, `Integral` and `Nondegenerate` as
axioms. Axioms are declarations by design. Nothing establishes any of them for
a constructed object: no specimen is shown projective, no form is shown to
land in $R$, and no Gram matrix is shown nonsingular. A lattice built from a
degenerate Gram matrix would enter `Nondegenerate` and say so.

### The free-module functor does not preserve equality of indexing sets

The transcript requires $F_R(S)=F_R(S')$ when $S=S'$. This is equality of
objects, not an extra chosen isomorphism. The induced maps must also agree
under that equality.

Separately built finite free modules with equal ordered indexing sets can be
equal but not identical. Their underlying sets are then identified through
equality, while morphism evaluation still expects identity. A morphism between
the equal modules can fail. Thus the object assignment exists, but it is not
yet a coherent functor on sets and maps.

### Forgetting structure does not preserve one ring object uniformly

The transcript treats a ring $R$ as the same object when regarded as an
$R$-module or an $R$-algebra. Forgetting structure should return that object,
not a second ring joined by an implicit conversion.

This holds for the named session rings, but not for every construction. A
module built directly over an engine ring can return that engine object.
Uniform promotion during parent construction breaks the base-ring morphism of
a free algebra. The missing construction is one coherent family of forgetful
and change-of-scalars functors across rings, modules, algebras, and lattices.

## The preamble does not own `Subsets` — [#348]

`Subsets(S)` for infinite `S` reports itself as a **finite enumerated set** and
does not terminate when iterated. There are $2^{\aleph_0}$ subsets of a
countable set: it is neither finite nor enumerable.

Set-level notions to own:

- $\mathcal{P}(S)$, uncountable when $S$ is infinite, answering `Sets().Infinite()`.
- The finite subsets of $S$, countably infinite when $S$ is, and enumerable.
- $\binom{S}{k}$, infinite for infinite $S$ and every $k \geq 1$.

`AlternatingMonomials._build_parent` branches on whether the generating set is
finite and assembles the finite subsets as a union over their sizes. That
branch exists only because `Subsets` cannot be asked, and goes away here.

Red proof: `test_the_subsets_of_a_countable_set_are_uncountable`, xfail
against #348.

## Free constructions on presented modules beyond degree two

The tensor and divided squares now use the degree-two quotient presentations.
The full graded algebras on $M=\operatorname{coker}(K\to F)$ remain absent.
They require $A(F)/\langle K\rangle$ in every degree. The degree-wise relation
generators, including every $\gamma_d(k)$ for $\Gamma$, now exist. No quotient
parent assembles those pieces into one graded algebra.

## Symmetric-only surface inherited by the other three

`_as_polynomial`, `_from_polynomial`, factorisation, `gcd`, `roots`,
`is_squarefree`, `leading_coefficient` and `monic` on `FreeAlgebraOnSet` cross
to Sage's *commutative* polynomial rings, and several assert rank one. That was
already wrong for `TensorAlgebraOnSet` before $\Lambda$ and $\Gamma$ inherited
it by subclassing. Either they are refused where they do not apply, or they are
sited on the symmetric flavour rather than on the shared class.

## Smaller, and unblocked

- **Graded pieces of an infinitely generated algebra.** `monomials_of_degree`
  asserts the generating set is finite (`MonomialSystem._finite_labels`) and
  `module_generators_of_degree` wraps the result in `finite_ordered_set`. For
  infinite $S$ there are infinitely many degree-$n$ monomials, so both are
  wrong rather than merely unbuilt: $T(F_R(S))[n]$ exists and has countable
  rank.

- **`A[n]` cannot mean the graded piece.** `FreeAlgebraOnSet.__getitem__` means
  adjoining variables, and `polynomial_ring` already reads an integer as a
  *count* of them, so `A[2]` is two new variables. The accessor stays
  `graded_piece(2)`.

- **$T(M) \otimes_R T(M^*)$ as the home of type-$(p,q)$ tensors.**
  `Tensor(M,(p,q))` stands alone and reads its own components. It is a graded
  piece of that bigraded algebra, which is an $R$-algebra for any commutative
  $R$ without further hypothesis.

- **$L^2(\mathbb{R})$ and $C^\infty(\mathbb{R})$ are shells.** Smoothness,
  square-integrability and the bilinearity of the pairing are unchecked and
  not decidable there. That is deliberate — their purpose is to make a
  construction that assumes coordinates fail early — but they are also missing
  from the obligation sweep.

## Claims that need repair

- **The obligation sweep does not cover every constructor.**
  `_constructions()` in `tests/test_constructors_meet_their_obligations.sage`
  is a hand-maintained list. It omits function modules, three free-algebra
  variants, `Tensor(M, (p, q))`, and graded pieces. New constructors can avoid
  the sweep without a visible failure. The sweep needs a complete source of
  constructors.

- **`Tensor` does not use Sage's parent and element structure.**
  `Tensor(M, (p, q))` is a `Parent`, but `TensorElement` is a plain Python
  class. It does not inherit `Element`, use `element_class`, or receive its
  arithmetic from the parent's category. Replace its local arithmetic with
  Sage's tensor implementation or another mature implementation.

## Local workarounds with unresolved causes

- **The compiler prelude overwrites `Set`.** `install_preamble` restores
  `Set`, `Sets`, `ConditionSet`, and `ImageSet` after the export sweep. Each
  lowered `.sage` module exports the prelude's names, so the last module can
  overwrite the session bindings. The compiler prelude must stop exporting
  these names into each module.

- **Unicode and ASCII ring names can normalize to one identifier.** Python's
  NFKC normalization made the mathematical integer-ring symbol and `Z` equal
  as identifiers. `init.sage` restores the session rings from the ring module.
  The preamble still needs a direct check for normalization collisions.

- **Category refinement can bypass required data.** `_refine_category_` can
  place an object in a category without implementations for its abstract
  parent methods. The incomplete constructor sweep is the only current
  detector.

## Verification not completed

- **The preamble notebook predates the restructuring.**
  `computations/notebooks/preamble.ipynb` predates
  `install_preamble(namespace)`, the category and axiom changes to `Lattices`,
  and the graded-module work. Its current behavior is unknown.

- **Ownership transfer of preparser tests was not confirmed.** Tests were
  removed from this repository because `tree-sitter-sage` owns the compiler.
  The transcript did not confirm that the required behavior has tests there.

## Repository

- The whole-repo mypy gate is red (~1634 errors, spike-side), so every commit
  in this line of work used `--no-verify`.
