# Outstanding work in the preamble

## Mathematics stated and not built

Each of these is a mathematical statement the preamble makes in prose and does
not realize as an object or a morphism.

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

## Smaller, and unblocked

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
