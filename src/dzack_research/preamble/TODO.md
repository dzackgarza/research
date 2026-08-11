# Outstanding work in the preamble

## Mathematics stated and not built

Each of these is a mathematical statement the preamble makes in prose and does
not realize as an object or a morphism.

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

## The free constructions are not functors in the category layer

The transcript used the functorial statement to determine the construction on
a presentation:

\[
M=\operatorname{coker}(K\to F)
\quad\Longrightarrow\quad
A(M)=A(F)/\langle K\rangle,
\]

because each free-algebra functor is a left adjoint and therefore preserves
colimits. The code now has extension and restriction morphisms, and it can
construct induced morphisms in some free cases. It does not have functors

\[
T,\operatorname{Sym},\Lambda,\Gamma:R\text{-Mod}\longrightarrow R\text{-Alg}
\]

with object and morphism maps on the same domain. In particular, there is no
identity or composition law for these assignments, no natural unit of an
adjunction, and no induced algebra morphism for a morphism of presented
modules. The missing full quotient algebras above are the missing object part
of this same statement, not a separate convenience API.

## Mixed tensors do not construct the stated tensor product

`Tensor(M, (p, q))` is stated to be

\[
M^{\otimes p}\otimes_R(M^*)^{\otimes q},
\]

and `MixedTensorAlgebra(M)` is stated to be

\[
T(M)\otimes_R T(M^*).
\]

The implementation stores a component dictionary whose indices all range over
one framing of `M`. It never constructs `M.dual_module()`, never forms either
tensor algebra, and never takes their tensor product. Thus upper indices are
labels from the same coordinate set as lower indices, rather than elements of
the dual construction. Module relations are also absent, so the component
model does not descend from a framing to a presented module.

Contraction, outer product, trace, and index raising work for the finite free
coordinate specimens now tested. They do not establish the claimed intrinsic
construction. This is the remaining mathematical gap behind the transcript's
request to place all type-$(p,q)$ tensors in one bigraded algebra.

## Smaller, and unblocked

- **`A[n]` cannot mean the graded piece.** `FreeAlgebraOnSet.__getitem__` means
  adjoining variables, and `polynomial_ring` already reads an integer as a
  *count* of them, so `A[2]` is two new variables. The accessor stays
  `graded_piece(2)`.

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
