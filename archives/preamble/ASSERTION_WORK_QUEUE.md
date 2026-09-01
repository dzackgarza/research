# Assertion compliance work queue

Scope: every Python `assert_statement` in `src/dzack_research/preamble/` and `tests/`. The catalogue comes from one `ast-grep` scan.

## Compliance rule

Every test assertion states a mathematical proposition.

An implementation assertion can instead have one of these purposes:

- It gates dependent functionality on a required precondition.

- It narrows a value to its true program type.

- It establishes an internal invariant before dependent code runs.

Prefer category containment when the claim is category membership.
Keep concrete class checks inside the category-owned containment implementation.

Replace test assertions about API strings, caches, source layout, diagnostic totals, old defects, or incidental representations.
A functionality test must reach a mathematical specimen through the functionality.

## Batch A — import-resolution functionality

- [x] `tests/test_sage_symbols.py:12` — replaced by the polynomial-matrix specimen.

- [x] `tests/test_sage_symbols.py:16` — replaced by the polynomial-matrix specimen.

- [x] `tests/test_sage_symbols.py:21` — replaced by the polynomial-matrix specimen.

- [x] `tests/test_sage_symbols.py:30` — removed: not mathematics.

- [x] `tests/test_sage_symbols.py:31` — removed: not mathematics.

- [x] `tests/test_sage_symbols.py:37` — removed: cache content is not mathematics.

- [x] `tests/test_sage_symbols.py:47` — removed: cache authority is an implementation detail.

- [x] `tests/test_sage_symbols.py:57` — replaced by the polynomial-matrix specimen.

- [x] `tests/test_sage_symbols.py:19` — `\det([[x,1],[0,x]])=x^2` over `QQ[x]`.

## Batch B — owned category runtime

- [x] `src/dzack_research/preamble/owned_category_bases.py:248` — keep: constructor gate and type refinement.

- [x] `src/dzack_research/preamble/owned_category.py:160` — keep: metaclass invariant.

- [x] `src/dzack_research/preamble/owned_category.py:238` — keep: runtime type refinement.

- [x] `src/dzack_research/preamble/owned_category.py:367` — keep: tied-class cache invariant.

- [x] `src/dzack_research/preamble/owned_category.py:375` — keep: runtime type refinement.

## Batch C — cardinal arithmetic

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:228` — `assert self.le(1, base_morphism.domain()), ( "exponentiation is monotone in the exponent for nonzero bases" )`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:254` — `assert terms, "a finite supremum needs at least one cardinal"`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:399` — `assert self.is_homset(homset)`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:584` — `assert isinstance(expression, _AlephCardinal), ( f"{self} is not an aleph cardinal" )`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:597` — `assert isinstance(expression, _FiniteCardinal), ( f"{self} is not a finite cardinal" )`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:633` — `assert codomain in Cardinalities(), ( "a cardinality morphism has cardinal objects at both ends" )`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:636` — `assert category is None or category == Cardinalities(), ( "the requested hom-set is not in Cardinalities" )`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:695` — `assert self, ( f"there is no cardinality morphism {self.domain()} -> {self.codomain()}" )`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:707` — `assert morphism is None or morphism in self, ( f"{morphism} is not in {self}" )`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:713` — `assert self.is_endomorphism_set(), ( "identity is defined only for an endomorphism set" )`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:733` — `assert Cardinalities().is_morphism(right)`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:734` — `assert Cardinalities().is_homset(homset)`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:764` — `assert value == Infinity or value in ZZ, ( f"a cardinal is a count (a Cardinal, an integer, or oo); found the " f"non-count scalar {value!r} — extended-scalar formulas consume the " f"extended-scalar spelling (index()) instead" )`

- [x] `src/dzack_research/preamble/categories/sets/cardinals.py:772` — `assert finite_value >= 0, ( f"a cardinal is a nonnegative integer; found {finite_value}" )`

## Batch D — owned sets and containment

- [x] `src/dzack_research/preamble/categories/sets/owned_sets.py:87` — `assert all(axiom_name in all_axioms for axiom_name in _SET_AXIOMS)`

- [x] `src/dzack_research/preamble/categories/sets/owned_sets.py:104` — `assert "Uncountable" not in category.axioms(), "Countable and Uncountable are disjoint"`

- [x] `src/dzack_research/preamble/categories/sets/owned_sets.py:113` — `assert "Countable" not in category.axioms(), "Countable and Uncountable are disjoint"`

- [x] `src/dzack_research/preamble/categories/sets/owned_sets.py:279` — `assert components in self, ( f"{components} is not a tuple of elements of the factors of {self}" )`

- [x] `src/dzack_research/preamble/categories/sets/owned_sets.py:618` — `assert any("__iter__" in ancestor.__dict__ for ancestor in type(self).__mro__), ( f"{self} has chosen no enumeration: it defines no __iter__, so " f"there is no order in which to index its elements. Countability " f"is the existence of an injection into the naturals and names no " f"enumeration; supply one to index or look up by position." )`

- [x] `src/dzack_research/preamble/categories/sets/owned_sets.py:632` — `assert n >= 0, f"enumeration indices are nonnegative; found {n}"`

- [x] `src/dzack_research/preamble/categories/sets/owned_sets.py:636` — `assert False, f"index {n} exceeds the enumeration of {self}"`

- [x] `src/dzack_research/preamble/categories/sets/owned_sets.py:645` — `assert False, f"{element} is not in the enumeration of {self}"`

- [x] `src/dzack_research/preamble/categories/sets/owned_sets.py:770` — `assert self.is_order_isomorphism(), ( "inverse only exists for order isomorphisms" )`

- [x] `src/dzack_research/preamble/categories/sets/owned_sets.py:777` — `assert self.domain() == other.codomain(), ( "domains and codomains do not match for composition" )`

- [x] `src/dzack_research/preamble/categories/sets/owned_sets.py:795` — `assert mor.is_order_preserving(), ( f"function {f} does not preserve the partial order " "(not a poset homomorphism)" )`

- [x] `src/dzack_research/preamble/categories/sets/underlying_sets.py:124` — `assert "Countable" in placement_of(self._structured).axioms(), ( f"{self._structured} answers +Infinity and does not declare itself " f"countable, so its cardinal is not determined -- every infinite " f"cardinal lies above that one point of the extended scalars. " f"State the count on the parent, or declare its countability." )`

## Batch E — module morphism matrices

- [x] `src/dzack_research/preamble/categories/modules/module_morphisms/morphism_matrices.py:283` — `assert isinstance(product, Matrix), "matrix multiplication must return a matrix"`

- [x] `src/dzack_research/preamble/categories/modules/module_morphisms/morphism_matrices.py:291` — `assert isinstance(product, Matrix), "matrix multiplication must return a matrix"`

- [x] `src/dzack_research/preamble/categories/modules/module_morphisms/morphism_matrices.py:351` — `assert group_generators, "a matrix group needs a generator"`

- [x] `src/dzack_research/preamble/categories/modules/module_morphisms/morphism_matrices.py:352` — `assert all( isinstance(group_generator, MorphismMatrix) for group_generator in group_generators ), "a matrix group here is generated by morphism matrices"`

## Batch F — group-module characters

- [x] `src/dzack_research/preamble/categories/modules/group_modules/characters.py:43` — `assert False, ( f"{class_function!r} is not a computed class function" )`

- [x] `src/dzack_research/preamble/categories/modules/group_modules/characters.py:84` — `assert ( isinstance(other, Character) and self.group() is other.group() ), ( "a character is added to another character of the same group" )`
