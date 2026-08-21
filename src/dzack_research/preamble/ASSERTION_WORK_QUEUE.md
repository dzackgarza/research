# Assertion compliance work queue

Scope: every Python `assert_statement` in `src/dzack_research/preamble/` and `tests/`.
The catalogue comes from one `ast-grep` scan.

## Compliance rule

Keep an assertion when it has one of these purposes:

- It states a mathematical proposition.
- It gates dependent functionality on a required precondition.
- It narrows a value to its true program type.
- It establishes an internal invariant before dependent code runs.

Prefer category containment when the claim is category membership.
Keep concrete class checks inside the category-owned containment implementation.
Use an explicit exception when a production gate must remain active under optimized Python.

Replace assertions about source layout, diagnostic totals, old defects, or incidental representations.

## Batch A — import-resolution functionality

- [ ] `tests/test_sage_symbols.py:12` — `assert ( import_statement_for("QQ", cache) == "from sage.rings.rational_field import QQ" )`
- [ ] `tests/test_sage_symbols.py:16` — `assert ( import_statement_for("PolynomialRing", cache) == "from sage.rings.polynomial.polynomial_ring_constructor" " import PolynomialRing" )`
- [ ] `tests/test_sage_symbols.py:21` — `assert ( import_statement_for("matrix", cache) == "from sage.matrix.constructor import matrix" )`
- [ ] `tests/test_sage_symbols.py:30` — `assert import_statement_for("definitely_not_a_sage_global", cache) is None`
- [ ] `tests/test_sage_symbols.py:31` — `assert import_statement_for("not an identifier", cache) is None`
- [ ] `tests/test_sage_symbols.py:37` — `assert live == "from sage.rings.rational_field import QQ"`
- [ ] `tests/test_sage_symbols.py:47` — `assert import_statement_for("QQ", cache) == sentinel`
- [ ] `tests/test_sage_symbols.py:57` — `assert block == ( "from sage.rings.rational_field import QQ\n" "from sage.matrix.constructor import matrix" )`

## Batch B — owned category runtime

- [ ] `src/dzack_research/preamble/owned_category_bases.py:248` — `assert base_category is not None, ( "singleton axiom initialization requires a resolved base category" )`
- [ ] `src/dzack_research/preamble/owned_category.py:160` — `assert all(issubclass(metaclass, type(base)) for base in bases), ( f"no crossed metaclass dominates the bases of {bases}" )`
- [ ] `src/dzack_research/preamble/owned_category.py:238` — `assert isinstance(category, Category), ( "OwnedCategoryMixin is mixed into a Category" )`
- [ ] `src/dzack_research/preamble/owned_category.py:367` — `assert cache is False, ( "the three tied names are built by lazy attributes on the category " "(Category.parent_class / element_class / morphism_class), none of " "which passes a cache argument; only subcategory_class does, and " "that is delegated above. If a caller ever passes one, it needs a " "cache here rather than being silently dropped." )`
- [ ] `src/dzack_research/preamble/owned_category.py:375` — `assert isinstance(category, Category), ( "OwnedCategoryMixin is mixed into a Category" )`

## Batch C — cardinal arithmetic

- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:228` — `assert self.le(1, base_morphism.domain()), ( "exponentiation is monotone in the exponent for nonzero bases" )`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:254` — `assert terms, "a finite supremum needs at least one cardinal"`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:399` — `assert isinstance(homset, CardinalityHomset)`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:568` — `assert isinstance(expression, _AlephCardinal), ( f"{self} is not an aleph cardinal" )`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:581` — `assert isinstance(expression, _FiniteCardinal), ( f"{self} is not a finite cardinal" )`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:617` — `assert isinstance(codomain, Cardinal), ( "a cardinality morphism has cardinal objects at both ends" )`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:620` — `assert category is None or category == Cardinalities(), ( "the requested hom-set is not in Cardinalities" )`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:679` — `assert self, ( f"there is no cardinality morphism {self.domain()} -> {self.codomain()}" )`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:691` — `assert morphism is None or morphism in self, ( f"{morphism} is not in {self}" )`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:697` — `assert self.is_endomorphism_set(), ( "identity is defined only for an endomorphism set" )`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:717` — `assert isinstance(right, CardinalityMorphism)`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:718` — `assert isinstance(homset, CardinalityHomset)`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:748` — `assert value == Infinity or value in ZZ, ( f"a cardinal is a count (a Cardinal, an integer, or oo); found the " f"non-count scalar {value!r} — extended-scalar formulas consume the " f"extended-scalar spelling (index()) instead" )`
- [ ] `src/dzack_research/preamble/categories/sets/cardinals.py:756` — `assert finite_value >= 0, ( f"a cardinal is a nonnegative integer; found {finite_value}" )`

## Batch D — owned sets and containment

- [ ] `src/dzack_research/preamble/categories/sets/owned_sets.py:87` — `assert all(axiom_name in all_axioms for axiom_name in _SET_AXIOMS)`
- [ ] `src/dzack_research/preamble/categories/sets/owned_sets.py:104` — `assert "Uncountable" not in category.axioms(), "Countable and Uncountable are disjoint"`
- [ ] `src/dzack_research/preamble/categories/sets/owned_sets.py:113` — `assert "Countable" not in category.axioms(), "Countable and Uncountable are disjoint"`
- [ ] `src/dzack_research/preamble/categories/sets/owned_sets.py:279` — `assert components in self, ( f"{components} is not a tuple of elements of the factors of {self}" )`
- [ ] `src/dzack_research/preamble/categories/sets/owned_sets.py:618` — `assert any("__iter__" in ancestor.__dict__ for ancestor in type(self).__mro__), ( f"{self} has chosen no enumeration: it defines no __iter__, so " f"there is no order in which to index its elements. Countability " f"is the existence of an injection into the naturals and names no " f"enumeration; supply one to index or look up by position." )`
- [ ] `src/dzack_research/preamble/categories/sets/owned_sets.py:632` — `assert n >= 0, f"enumeration indices are nonnegative; found {n}"`
- [ ] `src/dzack_research/preamble/categories/sets/owned_sets.py:636` — `assert False, f"index {n} exceeds the enumeration of {self}"`
- [ ] `src/dzack_research/preamble/categories/sets/owned_sets.py:645` — `assert False, f"{element} is not in the enumeration of {self}"`
- [ ] `src/dzack_research/preamble/categories/sets/owned_sets.py:770` — `assert self.is_order_isomorphism(), ( "inverse only exists for order isomorphisms" )`
- [ ] `src/dzack_research/preamble/categories/sets/owned_sets.py:777` — `assert self.domain() == other.codomain(), ( "domains and codomains do not match for composition" )`
- [ ] `src/dzack_research/preamble/categories/sets/owned_sets.py:795` — `assert mor.is_order_preserving(), ( f"function {f} does not preserve the partial order " "(not a poset homomorphism)" )`
- [ ] `src/dzack_research/preamble/categories/sets/underlying_sets.py:124` — `assert "Countable" in placement_of(self._structured).axioms(), ( f"{self._structured} answers +Infinity and does not declare itself " f"countable, so its cardinal is not determined -- every infinite " f"cardinal lies above that one point of the extended scalars. " f"State the count on the parent, or declare its countability." )`

## Batch E — module morphism matrices

- [ ] `src/dzack_research/preamble/categories/modules/module_morphisms/morphism_matrices.py:283` — `assert isinstance(product, Matrix), "matrix multiplication must return a matrix"`
- [ ] `src/dzack_research/preamble/categories/modules/module_morphisms/morphism_matrices.py:291` — `assert isinstance(product, Matrix), "matrix multiplication must return a matrix"`
- [ ] `src/dzack_research/preamble/categories/modules/module_morphisms/morphism_matrices.py:351` — `assert group_generators, "a matrix group needs a generator"`
- [ ] `src/dzack_research/preamble/categories/modules/module_morphisms/morphism_matrices.py:352` — `assert all( isinstance(group_generator, MorphismMatrix) for group_generator in group_generators ), "a matrix group here is generated by morphism matrices"`

## Batch F — group-module characters

- [ ] `src/dzack_research/preamble/categories/modules/group_modules/characters.py:43` — `assert False, ( f"{class_function!r} is not a computed class function" )`
- [ ] `src/dzack_research/preamble/categories/modules/group_modules/characters.py:84` — `assert isinstance(other, Character), ( "a character is added to another character of the same group" )`
