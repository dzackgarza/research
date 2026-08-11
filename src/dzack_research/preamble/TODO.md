# Outstanding work in the preamble

## Claims the code makes and does not keep

These are not unstarted work. Each is a statement in the repository that is
false as written, so each is misleading until fixed.

- **The obligation sweep says it covers everything and does not.**
  `_constructions()` in `tests/test_constructors_meet_their_obligations.sage`
  is documented as "every way the preamble makes an object" and is a
  hand-maintained dict of nineteen entries. Function modules, the tensor
  algebra, the alternating algebra, the divided power algebra, `Tensor(M,(p,q))`
  and graded pieces are all absent — every constructor added since the sweep
  was written is unswept, silently. A constructor list that does not enumerate
  itself will keep drifting; the sweep should discover constructors rather than
  be told about them.

- **`ideal_generators_in_degree` says "Γ adds its divided powers".**
  No `DividedPowerAlgebras` override exists, so the method is wrong for Γ: its
  ideal must be a divided power ideal, closed under the $\gamma_d$, so
  $\gamma_d(k)$ for $k \in K$ and $d \geq 2$ must join the generators. Nothing
  calls it yet, so nothing downstream is broken.

- **The four constructions are called left adjoints with nothing behind the
  word.** That claim appears in several docstrings and is what justifies
  $A(\operatorname{coker}) = A(F)/\langle K\rangle$. There are no `Functor`
  objects and no `Adjunction` instances for `T`, `Sym`, `Λ` or `Γ` — only the
  existing $F_R \dashv U$ pair between `Set` and `R-Mod` in
  `categories/functors/free_forgetful_adjunction.sage`, which does have real
  functors, a real unit and counit, and the hom-set bijection. Each of the four
  needs its functor, its forgetful partner out of the matching algebra
  category, and the pair.

- **`Tensor` is a parent whose elements do not belong to it.**
  `Tensor(M,(p,q))` is a `Parent` in `Modules(R)`, and `TensorElement`
  (`categories/modules/tensors.sage:109`) is a plain Python class with
  hand-rolled `__eq__`, `__hash__`, `__add__` and `__mul__`. It is not an
  `Element`, it is never built through `element_class`, and there is no
  coercion — so the parent's category supplies it nothing. The arithmetic was
  also written out rather than delegated: Sage's own tensor machinery was
  named as the reference implementation and is not being leaned on.

## The chain that blocks the forms layer

One line of work, in order. Each is blocked on the one above it.

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

Red proof: `test_a_graded_piece_is_a_submodule_carrying_its_inclusion`, xfail
against #351.

### 2. Graded pieces become real submodules

`GradedModules.ParentMethods.graded_piece` is written and correct — it asks for
the submodule the degree-$n$ generators span — and fails today only because of
(1). Nothing to write; it starts working when (1) lands.

### 3. `TensorSquare` and `DividedSquare` stop being placeholders

Both are formal `Parent`s in `categories/forms/forms.sage` and say so: "what
the preamble needs of it is that a form has an honest domain, not that its
elements are constructed." They should be $T(M)[2]$ and $\Gamma(M)[2]$, which
is the point of building $T$ and $\Gamma$ at all — there is no separate
$M^{\otimes 2}$.

The discriminant group carries a quadratic form and is a *presented* torsion
module, so this also needs (4).
`tests/test_constructors_meet_their_obligations.sage:126-127` cases on
`isinstance` against both and will need to follow.

### 4. The free constructions applied to presented modules

$A(M)$ for $M = \operatorname{coker}(K \to F)$. Each of $T$, `Sym`, $\Lambda$,
$\Gamma$ is a free object functor into its own category of algebras, hence a
left adjoint, hence preserves the presentation colimit:
$A(M) = A(F)/\langle K\rangle$.

`ideal_generators_in_degree` states the degree-$n$ part of that ideal and has
no callers. Missing: the Γ override (above), and whatever object $A(M)$ returns
for presented $M$. It needs `graded_piece(n)`; it does not obviously need a
normal form, which for $T$ would mean noncommutative Gröbner bases.

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

## Papercuts worked around rather than fixed

Each of these is a local accommodation for a defect that lives somewhere else.
The accommodation works; the defect is still there and will produce the next
one.

- **The compiler prelude overwrites `Set` in every lowered module.**
  `install_preamble` re-binds `Set`, `Sets`, `ConditionSet` and `ImageSet` from
  their owning module after the export sweep, because every lowered `.sage`
  module carries the prelude's `Set` and the last module swept wins. The cause
  is in the prelude that `tree-sitter-sage` emits, not here.

- **`ℤ` and `Z` are one Python identifier.** NFKC normalization makes them the
  same name, which collided with `Lattices.Z`; `init.sage` works around it by
  reading the session rings off the ring module. Any future unicode/ASCII pair
  collides identically, silently, and the preamble has no check that would say
  so.

- **`_refine_category_` is an open backdoor.** An object can enter a category
  without carrying its data, and neither `abstract_method` nor anything else
  gates it — `__init_extra__` would, and is not used for this. The constructor
  sweep is the only detector, and per the first section it does not cover
  everything.

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

## Unverified

- **The preamble notebook has not been run since the restructuring.**
  `computations/notebooks/preamble.ipynb` predates `install.sage` becoming
  `install_preamble(namespace)`, the `Lattices` rework into a category with
  axioms, and the graded node. Whether it still runs is unknown.

- **Whether the preparser tests landed in the repository that owns the
  compiler.** They were removed from here on the grounds that
  `tree-sitter-sage` owns them; that they arrived there has not been checked.

## Repository

- The whole-repo mypy gate is red (~1634 errors, spike-side), so every commit
  in this line of work used `--no-verify`.
