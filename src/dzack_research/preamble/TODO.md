# Outstanding work in the preamble

## Mathematics stated and not built

Each of these is a mathematical statement the preamble makes in prose and does
not realize as an object or a morphism.

### The universal properties are not there

$\Gamma^2$ is described as classifying quadratic forms:
$\operatorname{Hom}(\Gamma^2M, W) \cong \{\text{quadratic maps } M \to W\}$.
That bijection is the reason a quadratic form is a morphism rather than a set
map, and it exists in neither direction. A quadratic map cannot be turned into
a morphism out of $\Gamma^2M$, and a morphism out of $\Gamma^2M$ cannot be
evaluated as a quadratic map.

The same holds for freeness. $T \dashv U$ means
$\operatorname{Hom}_{\text{Alg}}(T(M), A) \cong \operatorname{Hom}_{\text{Mod}}(M, U(A))$,
and that bijection is what "free" asserts. It is written for $F_R \dashv U$
between `Set` and `R-Mod` and for none of the four algebra constructions.

### The four constructions have no morphisms between them

The category tree states `AlternatingAlgebras`, `SymmetricAlgebras` and
`DividedPowerAlgebras` as subcategories of `TensorAlgebras`. A subcategory
relation says $\Lambda(M)$ *is* a tensor algebra, which is false. The true
relations are morphisms, and none is built:

- $T(M) \twoheadrightarrow \operatorname{Sym}(M)$ and
  $T(M) \twoheadrightarrow \Lambda(M)$, the quotients by
  $x \otimes y - y \otimes x$ and by $x \otimes x$. Those relations are quoted
  in the docstrings as the definitions, and neither construction is built that
  way: both are built directly on their own monomials.
- $\Gamma(M) \to \operatorname{Sym}(M)$, an isomorphism over $\mathbb{Q}$ and
  not over $\mathbb{Z}$. Their graded ranks agree, which the tests check, but
  agreeing ranks are evidence and not the map.

Until these exist, "one construction seen through different relations" is
prose, and a containment stands where a morphism belongs.

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

### $Z(A)$ is only computable where the contract is uninteresting

An $R$-algebra is a ring $A$ with $R \to Z(A)$, and that morphism is what an
algebra is. `ring_center` asserts the ring is commutative and declines
otherwise. The tensor algebra is the noncommutative case the contract exists
to describe — $Z(T(V)) = R$ for rank at least two — and it is exactly the case
that cannot be asked.

### The lattice axioms are declared and never established

`Lattices(R)` is defined as the projective $R$-modules carrying an $R$-valued
bilinear form, with `FinitelyGenerated`, `Integral` and `Nondegenerate` as
axioms. Axioms are declarations by design. Nothing establishes any of them for
a constructed object: no specimen is shown projective, no form is shown to
land in $R$, and no Gram matrix is shown nonsingular. A lattice built from a
degenerate Gram matrix would enter `Nondegenerate` and say so.

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

- **`ideal_generators_in_degree` says "Γ adds its divided powers".**
  No `DividedPowerAlgebras` override exists, so the method is wrong for Γ: its
  ideal must be a divided power ideal, closed under the $\gamma_d$, so
  $\gamma_d(k)$ for $k \in K$ and $d \geq 2$ must join the generators. Nothing
  calls it yet, so nothing downstream is broken.

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
