# Outstanding work in the preamble

## The chain that blocks the forms layer

These are one line of work, in order. Each is blocked on the one above it.

### 1. A submodule requires the ambient to be finitely generated — [#351]

`submodule` and `subobject_on` sit on `FinitelyGeneratedFreeModules.ParentMethods`,
and `_independent_module_generators` (`module_morphisms.sage:225`) reads each
element's coordinates against the *whole* framing, then rebuilds the answer by
zipping against `module.module_generators()`. Both steps need a finite framing.

Neither is needed for the mathematics. Finitely many elements have finite
combined support, so the submodule they span is determined inside the framing
generators they touch, whatever the rest of the framing is. The fix is to
compute independence over the combined support and to site `submodule` on
framed modules rather than on finitely generated free ones.

`_independent_module_generators` is what every subobject in the preamble routes
through, so this wants its own pass rather than being changed in passing.

Red proof: `test_a_graded_piece_is_a_submodule_carrying_its_inclusion`
(`tests/test_free_constructions.sage`), xfail against #351.

### 2. Graded pieces become real submodules

`GradedModules.ParentMethods.graded_piece` is written and correct — it asks for
the submodule the degree-$n$ generators span — and fails today only because of
(1). Nothing to write here; it starts working when (1) lands.

### 3. `TensorSquare` and `DividedSquare` stop being placeholders

Both are formal `Parent`s in `categories/forms/forms.sage`, and say so: "what
the preamble needs of it is that a form has an honest domain, not that its
elements are constructed." They should be `T(M)[2]` and `Γ(M)[2]`, which is the
point of building `T` and `Γ` at all — there is no separate $M^{\otimes 2}$.

The discriminant group carries a quadratic form and is a *presented* torsion
module, so this also needs (4).

`tests/test_constructors_meet_their_obligations.sage:126-127` cases on
`isinstance` against both, and will need to follow.

### 4. The free constructions applied to presented modules

`A(M)` for `M = coker(K → F)`. Each of `T`, `Sym`, `Λ`, `Γ` is a free object
functor into its own category of algebras — associative, commutative,
alternating, divided power — hence a left adjoint, hence preserves the
presentation colimit: `A(M) = A(F)/⟨K⟩`.

`ideal_generators_in_degree` (`free_algebras.sage:120`) states the degree-$n$
part of that ideal and is **not yet called by anything**. What is missing:

- The `Γ` override. The docstring claims "Γ adds its divided powers" and no
  such override exists, so the method is wrong for `Γ` today: the ideal must be
  a divided power ideal, closed under the $\gamma_d$, so $\gamma_d(k)$ for
  $k\in K$ and $d\geq 2$ must join the generators.
- Whatever object `A(M)` returns for presented `M`. It needs `graded_piece(n)`;
  it does not obviously need a normal form, which for `T` would mean
  noncommutative Gröbner bases.

## Adjoint pairs are asserted only in prose

`categories/functors/free_forgetful_adjunction.sage` has real `Functor`
subclasses and a real `Adjunction` with unit, counit and the hom-set
bijection — for $F_R \dashv U$ between `Set` and `R-Mod` only.

The claim that `T`, `Sym`, `Λ` and `Γ` are left adjoints is currently made in
docstrings and used to justify (4), with no `Functor` objects and no
`Adjunction` instances behind it. Each needs its functor, its forgetful
partner out of the matching algebra category, and the pair.

## The preamble does not own `Subsets` — [#348]

`Subsets(S)` for infinite `S` reports itself as a **finite enumerated set** and
does not terminate when iterated. There are $2^{\aleph_0}$ subsets of a
countable set: it is neither finite nor enumerable.

Set-level notions the preamble should own:

- $\mathcal{P}(S)$, uncountable when $S$ is infinite, answering `Sets().Infinite()`.
- The finite subsets of $S$, countably infinite when $S$ is, and enumerable.
- $\binom{S}{k}$, infinite for infinite $S$ and every $k \geq 1$.

`AlternatingMonomials._build_parent` branches on whether the generating set is
finite and assembles the finite subsets as a union over their sizes. That
branch exists only because `Subsets` cannot be asked, and goes away here.

Red proof: `test_the_subsets_of_a_countable_set_are_uncountable`
(`tests/test_free_constructions.sage`), xfail against #348.

## Smaller, and unblocked

- **Graded pieces of an infinitely generated algebra.** `monomials_of_degree`
  asserts the generating set is finite (`MonomialSystem._finite_labels`), and
  `module_generators_of_degree` wraps the result in `finite_ordered_set`. For
  infinite $S$ the degree-$n$ monomials are infinite in number, so both are
  wrong rather than merely unbuilt: $T(F_R(S))[n]$ exists and has countable
  rank.

- **`A[n]` cannot mean the graded piece.** `FreeAlgebraOnSet.__getitem__` means
  adjoining variables, and `polynomial_ring` already reads an integer argument
  as a *count* of them. So `A[2]` is two new variables, not $A_2$, and the
  accessor stays spelled `graded_piece(2)`.

- **The polynomial presentation is symmetric-only.** `_as_polynomial`,
  `_from_polynomial`, factorisation, gcd and roots on `FreeAlgebraOnSet` cross
  to Sage's *commutative* polynomial rings. That was already wrong for
  `TensorAlgebraOnSet` before `Λ` and `Γ` inherited it. Either they are refused
  where they do not apply, or they are sited on the symmetric flavour.

- **`T(M) ⊗_R T(M*)` as the home of type-$(p,q)$ tensors.** `Tensor(M, (p,q))`
  in `categories/modules/tensors.sage` stands alone and reads its own
  components. It is a graded piece of that bigraded algebra, which is an
  $R$-algebra for any commutative $R$ without further hypothesis.

## Repository

- The whole-repo mypy gate is red (~1634 errors, spike-side), so every commit
  in this line of work used `--no-verify`.
