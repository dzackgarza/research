r"""Finite presented torsion modules equipped with exact forms.

The underlying module and its chosen presentation are first-class data.  A
Gram array defines a form on the quotient exactly when it annihilates the
relation submodule in the appropriate sense; these constructors check that
descent before equipping the module with the form.
"""

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.misc.classcall_metaclass import typecall
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    CategoricalIsomorphism,
)
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    IsoCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    _fix_selected_framing,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.g_sets import FiniteGSets
from dzack_research.preamble.categories.group.groups import (
    Groups,
    OwnedFiniteGroups,
    OwnedGroups,
    _group_framing_morphism,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    _matrix_coordinate_rows,
    _module_invariant_factor_form,
    _presentation_matrix,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    _integral_left_solver,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    MatrixSpaces,
    ModuleSubobjects,
    Modules,
    _torsion_module_presented_by_matrix,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import (
    Sets,
)
from dzack_research.preamble.refine import realize_owned_category
from dzack_research.preamble.tensors.tensor import (
    Tensor,
    _engine_component_matrix,
    tensor,
)


def _gram_rows(gram, rank):
    match gram:
        case ModuleMorphism():
            parent = gram.parent()
            if parent not in MatrixSpaces(parent.base_ring()):
                raise TypeError("a morphism Gram presentation must be an owned matrix Mor element")
            rows = tuple(
                tuple(gram[row, column] for column in range(parent.ncols()))
                for row in range(parent.nrows())
            )
        case Tensor():
            shape = gram.tensor_shape()
            rows = tuple(
                tuple(gram[row, column] for column in range(int(shape[1])))
                for row in range(int(shape[0]))
            )
        case _:
            rows = tuple(tuple(row) for row in gram)
    if len(rows) != rank or any(len(row) != rank for row in rows):
        raise ValueError(
            f"a Gram matrix on {rank} generators must be {rank} x {rank}, but the given rows have lengths "
            f"{tuple(len(row) for row in rows)}"
        )
    return rows


def _coerced_gram(value_module, gram, rank):
    return tuple(tuple(value_module(entry) for entry in row) for row in _gram_rows(gram, rank))


def _linear_combination(value_module, coefficients, values):
    return sum(
        (coefficient * value for coefficient, value in zip(coefficients, values, strict=True) if coefficient),
        value_module.zero(),
    )


def _relation_coefficients(relations):
    r"""Return each chosen relation's coefficients, asked of the matrix itself.

    A row of an owned matrix is an element of the dual module, not a sequence,
    so the coefficients come from the matrix entries at the chosen labels.
    """
    parent = relations.parent()
    return tuple(
        tuple(
            relations.matrix_entry(row_label, column_label)
            for column_label in parent.column_index_set()
        )
        for row_label in parent.row_index_set()
    )


def _bilinear_descends(relations, gram, value_module) -> bool:
    rank = len(gram)
    for row in _relation_coefficients(relations):
        for j in range(rank):
            if _linear_combination(value_module, row, tuple(gram[i][j] for i in range(rank))) != value_module.zero():
                return False
        for i in range(rank):
            if _linear_combination(value_module, row, tuple(gram[i][j] for j in range(rank))) != value_module.zero():
                return False
    return True


def _quadratic_descends(relations, gram, value_module) -> bool:
    rank = len(gram)
    two = value_module.base_ring()(2)
    for row in _relation_coefficients(relations):
        # q(x+r)-q(x)-q(r) is the polar value 2*x^T G r.
        for j in range(rank):
            pairing = _linear_combination(
                value_module,
                row,
                tuple(gram[i][j] for i in range(rank)),
            )
            if value_module.scalar_multiple(two, pairing) != value_module.zero():
                return False
        norm = sum(
            (row[i] * row[j] * gram[i][j] for i in range(rank) for j in range(rank) if row[i] and row[j]),
            value_module.zero(),
        )
        if norm != value_module.zero():
            return False
    return True


class TorsionFormIsometry(CategoricalIsomorphism):
    r"""An explicit isomorphism of finite framed torsion modules preserving a form."""

    def __init__(self, parent, forward, inverse, *, quadratic: bool) -> None:
        super().__init__(parent, forward, inverse)
        self._quadratic = bool(quadratic)
        source = self.domain()
        target = self.codomain()
        generators = tuple(source.module_generators())
        if self._quadratic:
            probes = generators + tuple(
                left + right
                for index, left in enumerate(generators)
                for right in generators[index + 1 :]
            )
            if any(source.q(element) != target.q(forward(element)) for element in probes):
                raise ValueError(
                    f"{forward} is not an isometry {source} -> {target}: it does not preserve the quadratic form q"
                )
            return
        if any(
            source.b(left, right) != target.b(forward(left), forward(right))
            for left in generators
            for right in generators
        ):
            raise ValueError(
                f"{forward} is not an isometry {source} -> {target}: it does not preserve the bilinear form b"
            )

    def is_quadratic(self) -> bool:
        return self._quadratic

    def inverse_morphism(self):
        r"""Return the underlying inverse module morphism."""
        return self._inverse


def _torsion_form_isometry(forward, inverse, *, quadratic: bool):
    r"""Return the form isometry represented by mutually inverse module maps."""
    return TorsionFormIsometry(
        forward.parent(),
        forward,
        inverse,
        quadratic=quadratic,
    )


def _representative_gram(form, *, quadratic: bool):
    r"""Return owned rational representatives as a type-``(0,2)`` tensor."""
    values = (
        form.form().lift_coordinate_values()
        if quadratic
        else form.form().coordinate_values()
    )
    value_module = form.value_module()
    rationals = value_module.fraction_field()
    labels = form.module_generating_set()
    rank = int(labels.cardinality())

    def representative(i, j):
        pair = values.index_set()(
            lambda index: labels[i] if int(index) == 0 else labels[j]
        )
        return value_module.lift(values[pair])

    return tensor(
        rationals,
        (),
        (rank, rank),
        (
            representative(i, j)
            for i in range(rank)
            for j in range(rank)
        ),
    )


def _engine_torsion_form(normalized_form, *, quadratic: bool):
    r"""Build the private Sage finite-form engine on a minimal framing.

    The engine is scratch data only.  Its cover basis is identified with the
    invariant-factor framing of ``normalized_form``; public automorphisms are
    transported back through the explicit normalization isometry.
    """
    from sage.modules.torsion_quadratic_module import (
        TorsionQuadraticForm,
        TorsionQuadraticModule,
    )

    engine = TorsionQuadraticForm(
        _engine_component_matrix(
            _representative_gram(normalized_form, quadratic=quadratic)
        )
    )
    if int(engine.cardinality()) != int(normalized_form.cardinality()):
        raise ArithmeticError(
            f"the finite quadratic module built from the Gram matrix of {normalized_form} has order "
            f"{engine.cardinality()}, not the order {normalized_form.cardinality()} of {normalized_form}"
        )
    if not quadratic:
        # Sage's orthogonal group preserves both b and q.  Setting the
        # quadratic modulus equal to the bilinear modulus makes q(x)=b(x,x)
        # derived data, so preserving it imposes no condition beyond b.
        engine = TorsionQuadraticModule(
            engine.V(),
            engine.W(),
            gens=engine.gens(),
            modulus=engine._modulus,
            modulus_qf=engine._modulus,
            check=False,
        )
    return engine


def _value_module(form, *, quadratic: bool):
    r"""Return the value module through the owned form interface."""
    return form.value_module()


def _underlying_presented_module(form):
    return form.unformed_module()


def _underlying_element(form, element):
    return form.unformed_module()(element)


def _coordinate_rows(form, generators):

    module = _underlying_presented_module(form)
    ring = module.base_ring()
    labels = module.module_generating_set()
    def coordinate_rows():
        for generator in generators:
            coefficients = module.framing_coefficients(_underlying_element(form, generator))
            yield (
                coefficients.get(label, ring.zero())
                for label in labels
            )

    return ring.matrix_space(len(generators), int(labels.cardinality())).from_rows(coordinate_rows())


def _relations_among_generators(form, generators):
    r"""Return the relation matrix for a selected generating family of ``form``."""

    module = _underlying_presented_module(form)
    ring = module.base_ring()
    lifts = _coordinate_rows(form, generators)
    selected_relations = _presentation_matrix(module)
    known = ring.matrix_space(selected_relations.nrows(), selected_relations.ncols()).from_rows(_matrix_coordinate_rows(selected_relations))
    combined = lifts.stack(known)
    # Transpose the owned morphism, not its matrix presentation.  The codomain
    # of ``combined`` is the biproduct separating the selected-generator rows
    # from the pre-existing relation rows; matrix-level transposition rebuilds
    # an equal-rank generic free module and loses that biproduct endpoint, so
    # its kernel cannot compose with the biproduct projection below.
    kernel = combined.transpose().kernel()
    relations = (
        combined.codomain().left_projection() * kernel.inclusion()
    ).image()
    inclusion = relations.inclusion()
    linear_inclusion = inclusion.domain().module_category().Mor(
        inclusion.domain(), inclusion.codomain()
    )(inclusion)
    return linear_inclusion.transpose()


def _quadratic_gram_on(form, generators):
    quadratic_values = _value_module(form, quadratic=True)
    bilinear_values = form.associated_bilinear_form().value_module()
    rows = []
    for i, left in enumerate(generators):
        row = []
        for j, right in enumerate(generators):
            if i == j:
                row.append(form.q(left))
            else:
                row.append(quadratic_values(bilinear_values.lift(form.b(left, right))))
        rows.append(tuple(row))
    return tuple(rows)


def _torsion_form_modules(base_ring, *, quadratic: bool):
    r"""Return the category of finite forms of the stated flavour over ``base_ring``."""
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
        BilinearFormModules,
        QuadraticFormModules,
    )

    classifier = QuadraticFormModules if quadratic else BilinearFormModules
    return classifier(base_ring).FinitelyPresented().Torsion()


def _torsion_form_subobject_on(form, generators, *, quadratic: bool):
    r"""Return the finite torsion submodule spanned by ``generators`` with restricted form."""

    generators = tuple(form(generator) for generator in generators)
    unformed = form.unformed_module()
    unformed_generators = tuple(unformed(generator) for generator in generators)
    underlying_subobject = unformed.subobject_on(unformed_generators)
    underlying_inclusion = underlying_subobject.inclusion()

    def ambient_image(label):
        underlying_generator = underlying_subobject.module_generator(label)
        return form(underlying_inclusion(underlying_generator))

    selected = tuple(
        ambient_image(label)
        for label in underlying_subobject.module_generating_set()
    )
    gram = _form_gram_on(form, selected, quadratic=quadratic)
    category = _torsion_form_modules(form.base_ring(), quadratic=quadratic)

    def inclusion_factory(source):
        return source.Mono(form)(ambient_image, quadratic=quadratic)

    def lift_from_ambient(source, element):
        unformed_element = unformed(form(element))
        if underlying_inclusion.has_selected_lift():
            lifted = underlying_inclusion.lift(unformed_element)
        else:
            lifted = next(
                (
                    candidate
                    for candidate in underlying_subobject.elements()
                    if underlying_inclusion(candidate) == unformed_element
                ),
                None,
            )
            if lifted is None:
                raise ValueError(
                    f"{element} does not lie in the submodule {source} of {form}"
                )
        return source(lifted)

    return category.from_module(
        underlying_subobject,
        gram,
        form.value_module(),
        _subobject_ambient=form,
        _subobject_generator_images=ambient_image,
        _subobject_lift=lift_from_ambient,
        _subobject_inclusion_factory=inclusion_factory,
    )


def _torsion_form_primary_part(form, prime, *, quadratic: bool):
    r"""Return the ``prime``-primary form-bearing subobject."""

    prime = form.base_ring()(prime)
    generators = []
    for generator in form.smith_form_module_generators():
        order = generator.additive_order()
        valuation = int(order.valuation(prime))
        if valuation:
            primary_order = prime**valuation
            generators.append(form.scalar_multiple(order // primary_order, generator))
    return _torsion_form_subobject_on(form, generators, quadratic=quadratic)


def _embedded_elements(subobject):
    inclusion = subobject.inclusion()
    return frozenset(inclusion(element) for element in subobject.elements())


def _torsion_form_isotropic_subobjects(form, *, quadratic: bool):
    r"""Return all form-bearing subobjects on which the selected form vanishes."""
    return finite_ordered_set(
        tuple(
            subobject
            for subobject in _torsion_form_all_subobjects(
                form, quadratic=quadratic
            )
            if form.form_vanishes_on(_embedded_elements(subobject))
        )
    )


def _torsion_form_maximal_isotropic_subobjects(form, *, quadratic: bool):
    isotropic = _torsion_form_isotropic_subobjects(form, quadratic=quadratic)
    by_elements = tuple((subobject, _embedded_elements(subobject)) for subobject in isotropic)
    return finite_ordered_set(
        tuple(
            subobject
            for subobject, elements in by_elements
            if not any(elements < larger for _other, larger in by_elements)
        )
    )


def _torsion_form_all_subobjects(form, *, quadratic: bool):
    r"""Return every finite form-bearing subobject of ``form`` exactly once.

    The owned finite-torsion enumeration itself is the ``ZZ`` Smith
    specialization.  On that exact frontier Sage's finite-quadratic-module
    backend owns the complete subgroup enumeration: ``ZZ``-submodules are
    additive subgroups, and ``all_submodules()`` delegates the finite abelian
    subgroup lattice to GAP.  We cross only its returned generators through
    the invariant-factor normalization.
    """
    integers = _own_ring(SageZZ)
    assert form.base_ring() is integers, (
        f"the submodules of the torsion form {form} are enumerated only over ZZ, "
        f"but {form} is over {form.base_ring()}"
    )
    normalization = form.invariant_factor_form()
    normalized = normalization.codomain()
    engine = _engine_torsion_form(normalized, quadratic=quadratic)
    cover = engine.V()
    labels = tuple(normalized.module_generating_set())
    ring = normalized.base_ring()

    def owned_engine_generator(engine_generator):
        coordinates = cover.coordinates(engine(engine_generator).lift())
        normalized_element = normalized.linear_combination(
            {
                label: _owned_engine_element(ring, SageZZ(coefficient))
                for label, coefficient in zip(labels, coordinates, strict=True)
                if coefficient
            }
        )
        return normalization.inverse()(normalized_element)

    return finite_ordered_set(
        tuple(
            _torsion_form_subobject_on(
                form,
                tuple(
                    owned_engine_generator(generator)
                    for generator in engine_submodule.gens()
                ),
                quadratic=quadratic,
            )
            for engine_submodule in engine.all_submodules()
        )
    )


def _torsion_form_orthogonal_subobject(form, subobject, *, quadratic: bool):
    r"""Return ``S^perp`` as a form-bearing subobject of ``form``."""
    inclusion = subobject.inclusion()
    if inclusion.codomain() is not form:
        raise ValueError(
            f"the orthogonal complement in {form} is taken of a submodule of {form}, but {subobject} "
            f"is a submodule of {inclusion.codomain()}"
        )
    generators = tuple(subobject.embedded_module_generators())
    zero = form.associated_bilinear_form().value_module().zero() if quadratic else form.value_module().zero()
    selected = tuple(
        element
        for element in form.elements()
        if all(form.b(element, generator) == zero for generator in generators)
    )
    return _torsion_form_subobject_on(form, selected, quadratic=quadratic)


def _torsion_form_lagrangian_subobjects(form, *, quadratic: bool):
    r"""Return isotropic ``S`` satisfying ``S=S^perp``."""
    return finite_ordered_set(
        tuple(
            subobject
            for subobject in _torsion_form_isotropic_subobjects(
                form, quadratic=quadratic
            )
            if _embedded_elements(subobject)
            == _embedded_elements(
                _torsion_form_orthogonal_subobject(
                    form, subobject, quadratic=quadratic
                )
            )
        )
    )


def _torsion_form_element_action(form, acting):
    r"""Return the represented finite ``acting``-set of elements of ``form``."""
    return FiniteGSets(acting)(
        form.elements(),
        lambda automorphism, element: automorphism(element),
    )


def _torsion_form_subobject_action(form, family, acting):
    r"""Return the represented action on one invariant finite subobject family.

    The points of the G-set are the already selected form-bearing subobjects in
    ``family``.  Acting on a point changes only its embedded element set; the
    corresponding selected point of ``family`` is then recovered.  Thus the
    torsion-form layer supplies the mathematical action while orbit and
    stabilizer structure is owned by :class:`FiniteGSets`.
    """
    points = finite_ordered_set(tuple(family))
    by_embedded_elements = {
        _embedded_elements(subobject): subobject
        for subobject in points
    }

    def act(automorphism, subobject):
        if subobject.inclusion().codomain() is not form:
            raise ValueError(
                f"the automorphisms of {form} act on submodules of {form}, but {subobject} is a submodule "
                f"of {subobject.inclusion().codomain()}"
            )
        image = frozenset(
            automorphism(element) for element in _embedded_elements(subobject)
        )
        if image not in by_embedded_elements:
            raise ValueError(
                f"the family of submodules of {form} is not invariant under {acting}: "
                f"{automorphism} sends {subobject} outside it"
            )
        return by_embedded_elements[image]

    return FiniteGSets(acting)(points, act)


def _torsion_form_subobject_orbits(form, family, acting):
    r"""Return the orbit partition through the represented finite G-set action."""
    action = _torsion_form_subobject_action(form, family, acting)
    return finite_ordered_set(tuple(orbit.points() for orbit in action.orbits()))


def _torsion_form_subquotient(form, subobject, over, *, quadratic: bool):
    r"""Return ``K/H`` with descended form for ``H <= K <= H^perp``."""
    small_inclusion = subobject.inclusion()
    large_inclusion = over.inclusion()
    if small_inclusion.codomain() is not form or large_inclusion.codomain() is not form:
        raise ValueError(
            f"the subquotient K/H of {form} needs H={subobject} and K={over} to be submodules of {form}, "
            f"but they are submodules of {small_inclusion.codomain()} and {large_inclusion.codomain()}"
        )
    small_elements = _embedded_elements(subobject)
    large_elements = _embedded_elements(over)
    if not small_elements <= large_elements:
        raise ValueError(
            f"the subquotient K/H of {form} requires H contained in K, but H={subobject} is not contained in K={over}"
        )
    if not form.form_vanishes_on(small_elements):
        raise ValueError(
            f"the form of {form} descends to K/H only when H is isotropic, but the form does not vanish on H={subobject}"
        )
    perpendicular = _torsion_form_orthogonal_subobject(
        form, subobject, quadratic=quadratic
    )
    if not large_elements <= _embedded_elements(perpendicular):
        raise ValueError(
            f"the form of {form} descends to K/H only when K is contained in H^perp, "
            f"but K={over} is not contained in the orthogonal complement of H={subobject}"
        )

    images = {
        label: large_inclusion.lift(
            small_inclusion(subobject.module_generator(label))
        )
        for label in subobject.module_generating_set()
    }
    quotient = subobject.module_category().Mor(subobject, over)(images).cokernel()
    generators = tuple(over.module_generators())
    return _torsion_form_modules(form.base_ring(), quadratic=quadratic).from_module(
        quotient,
        _form_gram_on(over, generators, quadratic=quadratic),
        form.value_module(),
    )


def _form_gram_on(form, generators, *, quadratic: bool):
    r"""Return the Gram data of ``form`` on a selected generating family.

    The quadratic reading carries ``q`` on the diagonal and a lift of ``b``
    off it, valued in ``K/2R``; the bilinear reading is ``b`` throughout,
    valued in ``K/R``.  Which one is asked for is a fact about the
    mathematics of the caller, never about the family.
    """
    if quadratic:
        return _quadratic_gram_on(form, generators)
    return tuple(
        tuple(form.b(left, right) for right in generators)
        for left in generators
    )


def _regenerate_form_on_generators(form, generators, *, quadratic: bool):
    r"""Return ``form -> form'`` for the same finite form on a new framing."""

    generators = tuple(generators)
    if any(generator not in form for generator in generators):
        raise TypeError(
            f"new generators of {form} must be elements of {form}, but {generators} contains an element not in {form}"
        )
    module = _underlying_presented_module(form)
    ring = module.base_ring()
    labels = finite_ordered_set(range(len(generators)))
    relations = _relations_among_generators(form, generators)
    regenerated_module = _torsion_module_presented_by_matrix(relations, labels)
    regenerated = _torsion_form_modules(form.base_ring(), quadratic=quadratic).from_module(
        regenerated_module,
        _form_gram_on(form, generators, quadratic=quadratic),
        _value_module(form, quadratic=quadratic),
    )

    inverse = regenerated.module_category().Mor(regenerated, form)(
        {label: generator for label, generator in zip(labels, generators, strict=True)}
    )


    lifts = _coordinate_rows(form, generators)
    selected_relations = _presentation_matrix(module)
    known = ring.matrix_space(selected_relations.nrows(), selected_relations.ncols()).from_rows(_matrix_coordinate_rows(selected_relations))
    # Keep the actual biproduct codomain: the integral solver works on every
    # finite framed free Mor, and its solution therefore lands in the same
    # biproduct whose left projection selects the coefficients of the new
    # generators.  Passing through ``matrix()`` would replace that endpoint by
    # a rank-only coordinate module and discard the projection.
    system = lifts.stack(known)
    source_labels = tuple(form.module_generating_set())
    regenerated_generators = tuple(regenerated.module_generators())
    forward_images = {}
    solve = _integral_left_solver(system, ring)
    for position, source_label in enumerate(source_labels):
        target = [
            ring.one() if index == position else ring.zero()
            for index in range(len(source_labels))
        ]
        solution = solve(target)
        generator_solution = system.codomain().left_projection()(solution)
        generator_coefficients = lifts.codomain().framing_coefficients(generator_solution)
        lift_labels = lifts.codomain().module_generating_set()
        forward_images[source_label] = sum(
            (
                regenerated.scalar_multiple(
                    generator_coefficients.get(
                        lift_labels[index], ring.zero()
                    ),
                    generator,
                )
                for index, generator in enumerate(regenerated_generators)
                if generator_coefficients.get(
                    lift_labels[index], ring.zero()
                )
            ),
            regenerated.zero(),
        )
    forward = form.module_category().Mor(form, regenerated)(forward_images)
    return _torsion_form_isometry(forward, inverse, quadratic=quadratic)


def _prime_indexed_generators(generators_by_prime):
    r"""Return the family \(p\mapsto\) chosen Jordan generators at \(p\).

    The primes are the index set and the chosen generators the value there.
    Two primes may carry equal-looking generating families, and the generators
    at one prime are an ordered choice, so both levels are families.
    """

    def generators_at(prime):
        chosen = generators_by_prime[prime]
        return indexed_family(
            Sets.Δ[len(chosen) - 1],
            lambda position, chosen=chosen: chosen[int(position)],
            name="Jordan generators",
        )

    primes = finite_ordered_set(tuple(sorted(generators_by_prime)))
    return indexed_family(primes, generators_at, name="p-adic Jordan generators")


def _p_adic_jordan_decomposition(form, *, quadratic: bool):
    r"""Return prime-indexed Jordan generators as elements of ``form``."""
    if not quadratic:
        return _bilinear_p_adic_jordan_decomposition(form)
    normalization = form.invariant_factor_form()
    normalized = normalization.codomain()
    engine = _engine_torsion_form(normalized, quadratic=quadratic)
    cover = engine.V()
    labels = tuple(normalized.module_generating_set())
    result = {}
    for prime in engine.annihilator().gen().prime_divisors():
        normal = engine.primary_part(prime).normal_form()
        generators = []
        for engine_generator in normal.gens():
            coordinates = cover.coordinates(engine_generator.lift())
            ring = normalized.base_ring()
            normalized_element = normalized.linear_combination(
                {
                    label: _owned_engine_element(ring, SageZZ(coefficient))
                    for label, coefficient in zip(labels, coordinates, strict=True)
                    if coefficient
                }
            )
            generators.append(normalization.inverse()(normalized_element))
        result[_owned_engine_element(normalized.base_ring(), SageZZ(prime))] = tuple(generators)
    return _prime_indexed_generators(result)


def _bilinear_p_adic_jordan_decomposition(form):
    r"""Return a symmetric-bilinear Jordan framing prime by prime.

    Sage's finite quadratic normal form is not a bilinear normal-form engine at
    ``p=2``: the extra quadratic refinement can change the chosen transformation.
    Here we use Sage's p-adic lattice reduction only as the private engine for
    the symmetric pairing, following the standard inverse-form reduction.
    """
    from sage.quadratic_forms.genera.normal_form import _normalize, p_adic_normal_form
    from sage.rings.padics.factory import Zp

    normalization = form.invariant_factor_form()
    normalized = normalization.codomain()
    ring = normalized.base_ring()
    invariants = tuple(normalized.invariant_factors())
    normalized_generators = tuple(normalized.module_generators())
    exponent = ring.one()
    for invariant in invariants:
        exponent = exponent.lcm(invariant)

    result = {}
    for prime in exponent.prime_divisors():
        primary_generators = []
        for order, generator in zip(invariants, normalized_generators, strict=True):
            valuation = int(order.valuation(prime))
            if valuation:
                coefficient = order // (prime**valuation)
                primary_generators.append(
                    normalized.scalar_multiple(coefficient, generator)
                )
        primary_generators = tuple(primary_generators)
        values = normalized.value_module()
        rationals = values.fraction_field()
        representative = tensor(
            rationals,
            (),
            (len(primary_generators), len(primary_generators)),
            [
                [
                    values.lift(normalized.b(left, right))
                    for right in primary_generators
                ]
                for left in primary_generators
            ],
        )
        engine = _engine_component_matrix(representative)

        rank = engine.rank()
        if rank == engine.ncols():
            split = engine.parent().identity_matrix()
        else:
            integral = (engine * engine.denominator()).change_ring(SageZZ)
            split = integral.hermite_form(transformation=True)[1]
        degenerate = split[rank:, :]
        nondegenerate = split[:rank, :]
        nondegenerate_form = nondegenerate * engine * nondegenerate.transpose()

        if rank:

            backend_prime = _engine_element(ring, prime)
            precision = int(exponent.valuation(prime)) + 5
            padics = Zp(backend_prime, type="fixed-mod", prec=precision)
            _diagonal, transform = p_adic_normal_form(
                nondegenerate_form.inverse(),
                backend_prime,
                precision=precision + 5,
            )
            transform = transform.change_ring(SageZZ).inverse().transpose()
            transform = transform.change_ring(padics).change_ring(SageZZ)
            scaled = (
                transform
                * nondegenerate_form
                * transform.transpose()
                * backend_prime ** nondegenerate_form.denominator().valuation(backend_prime)
            )
            transform = (
                _normalize(scaled.change_ring(padics), normal_odd=False)[1].change_ring(SageZZ)
                * transform
            )
            transform = transform * nondegenerate
        else:
            transform = nondegenerate
        transform = transform.stack(degenerate).change_ring(SageZZ)

        jordan_generators = []
        for row in transform.rows():
            normalized_element = sum(
                (
                    normalized.scalar_multiple(
                        _owned_engine_element(ring, SageZZ(coefficient)), generator
                    )
                    for coefficient, generator in zip(
                        row, primary_generators, strict=True
                    )
                    if coefficient
                ),
                normalized.zero(),
            )
            jordan_generators.append(normalization.inverse()(normalized_element))
        result[prime] = tuple(jordan_generators)
    return _prime_indexed_generators(result)


def _p_adic_jordan_module_generators(form, *, quadratic: bool):
    r"""Return the selected Jordan generators, prime by prime, inside ``form``."""
    decomposition = _p_adic_jordan_decomposition(form, quadratic=quadratic)
    return tuple(
        generator
        for prime in decomposition.index_set()
        for generator in decomposition[prime]
    )


def _p_adic_jordan_form(form, *, quadratic: bool):
    generators = _p_adic_jordan_module_generators(form, quadratic=quadratic)
    return _regenerate_form_on_generators(form, generators, quadratic=quadratic)


def _twisted_torsion_form(form, scalar, *, quadratic: bool):
    generators = tuple(form.module_generators())
    value_module = _value_module(form, quadratic=quadratic)
    gram = tuple(
        tuple(value_module.scalar_multiple(scalar, entry) for entry in row)
        for row in _form_gram_on(form, generators, quadratic=quadratic)
    )
    return _torsion_form_modules(form.base_ring(), quadratic=quadratic).from_module(
        _underlying_presented_module(form),
        gram,
        _value_module(form, quadratic=quadratic),
    )


def _twisted_module_morphism(module_morphism, twisted_source, twisted_target):
    r"""Read one module map between the twisted copies of its endpoints.

    Twisting rescales the form and leaves the underlying module untouched, so
    ``twisted_source`` shares its underlying module with the source of
    ``module_morphism``, and ``twisted_target`` with its target.  The twisted
    map is therefore the same map: the generator labelled ``l`` goes to the
    image of the generator labelled ``l``, transported through that shared
    underlying module.
    """
    source = module_morphism.domain()
    return twisted_source.module_category().Mor(twisted_source, twisted_target)(
        {
            label: twisted_target(module_morphism(source.module_generator(label)))
            for label in twisted_source.module_generating_set()
        }
    )


class TorsionFormTwistFunctor(Functor):
    r"""The endofunctor ``A |-> A(s)`` rescaling a finite form by ``s``.

    On objects this is the rescale ``b |-> s*b`` (respectively ``q |-> s*q``)
    on the unchanged underlying module.  On arrows it is the identity on
    underlying maps: an isometry ``f`` from ``(A,b)`` to ``(B,b')`` has
    ``b'(f x, f y) = b(x,y)``, hence ``(s*b')(f x, f y) = (s*b)(x,y)``, so the
    same map is an isometry from ``A(s)`` to ``B(s)``.
    """

    def __init__(self, category, scalar, *, quadratic: bool) -> None:
        self._scalar = scalar
        self._quadratic = bool(quadratic)
        super().__init__(category, category)

    def scalar(self):
        r"""Return the scalar this functor multiplies the form by."""
        return self._scalar

    def _apply_object(self, form):
        return _twisted_torsion_form(form, self.scalar(), quadratic=self._quadratic)

    def _apply_morphism(self, isometry):
        source = self.object_image(isometry.domain())
        target = self.object_image(isometry.codomain())
        return _torsion_form_isometry(
            _twisted_module_morphism(isometry.forward(), source, target),
            _twisted_module_morphism(isometry.inverse_morphism(), target, source),
            quadratic=self._quadratic,
        )

    def _repr_(self):
        return f"Twist by {self.scalar()} on {self.domain()}"


def _engine_normal_form_key(form, *, quadratic: bool):
    normalization = form.invariant_factor_form()
    engine = _engine_torsion_form(normalization.codomain(), quadratic=quadratic)
    normal = engine.normal_form()
    gram = normal.gram_matrix_quadratic()
    return (
        SageQQ(engine._modulus),
        SageQQ(engine._modulus_qf),
        tuple(SageZZ(invariant) for invariant in normal.invariants()),
        tuple(tuple(SageQQ(entry) for entry in row) for row in gram.rows()),
    )


def _forms_are_isomorphic(left, right, *, quadratic: bool) -> bool:
    if left.base_ring() is not right.base_ring():
        return False
    return _engine_normal_form_key(left, quadratic=quadratic) == _engine_normal_form_key(
        right, quadratic=quadratic
    )


class TorsionFormAutomorphism(TorsionFormIsometry):
    r"""A live form-preserving automorphism, parented by its orthogonal group."""

    def __init__(self, parent, forward, inverse, _engine_element) -> None:
        super().__init__(
            parent,
            forward,
            inverse,
            quadratic=parent.is_quadratic(),
        )
        self._engine_element = _engine_element

    def _engine(self):
        r"""Return the private Sage representative used by this form-group owner.

        Orthogonal-group admission and subgroup construction in this module
        may read it to ask the maintained engine about a raw group element.
        It is not a category-membership datum or a public group result.
        """
        return self._engine_element

    def inverse(self):
        return self.parent()._from_engine(~self._engine())

    def __invert__(self):
        return self.inverse()

    def __mul__(self, other):
        if not isinstance(other, TorsionFormAutomorphism):
            return NotImplemented
        if other.parent() is not self.parent():
            return NotImplemented
        # Sage's private FQF engine acts on the right.  This reversal is kept
        # entirely at the crossing: publicly ``self * other`` is ordinary
        # composition of type-(1,1) tensors/morphisms.
        return self.parent()._from_engine(
            other._engine() * self._engine()
        )

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, TorsionFormAutomorphism)
            and other.parent() is self.parent()
            and other._engine() == self._engine()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(
            (
                id(self.parent()),
                tuple(int(entry) for entry in self._engine().matrix().list()),
            )
        )

    def _repr_(self):
        return f"Form automorphism of {self.domain()}"


class TorsionFormOrthogonalGroup(CategoricalMor):
    r"""The finite group of live automorphisms preserving one finite form."""

    Element = TorsionFormAutomorphism

    @staticmethod
    def __classcall__(cls, mor_family, form, **options):
        return typecall(cls, mor_family, form, **options)

    def __init__(
        self,
        mor_family,
        form,
        *,
        quadratic: bool,
    ) -> None:
        self._quadratic = bool(quadratic)
        self._normalization = form.invariant_factor_form()
        self._normalized_form = self._normalization.codomain()
        self._engine_module = _engine_torsion_form(
            self._normalized_form,
            quadratic=self._quadratic,
        )
        self._engine_group_parent = self._engine_module.orthogonal_group()
        CategoricalMor.__init__(
            self,
            mor_family,
            form,
            form,
            category=Category.join((OwnedFiniteGroups(), OwnedGroups().Framed())),
        )
        realize_owned_category(self)
        engine_generators = tuple(self._engine_group_parent.gens())
        generators = finite_ordered_set(
            tuple(self._from_engine(generator) for generator in engine_generators)
        )
        source = Groups.Free(index_set=generators)
        generator_morphism = Sets().Mor(generators, self)(lambda generator: generator)
        _fix_selected_framing(
            self,
            OwnedGroups(),
            source,
            generators,
            lambda: generator_morphism,
            lambda: _group_framing_morphism(
                self, source, generators, generator_morphism
            ),
        )

    def is_quadratic(self) -> bool:
        return self._quadratic

    def super_categories(self):
        packet = self.base_category().category_packet()
        form = self.domain()
        supers = [
            packet.Mors().Of(form, form),
            packet.Monos().Of(form, form),
            packet.Epis().Of(form, form),
        ]
        supers.extend(
            superpacket.Isos().Of(form, form)
            for superpacket in packet.super_packets()
            if form in superpacket.C()
        )
        if self.aut_family() is not None:
            supers.append(packet.Ends().Of(form))
            supers.extend(
                superpacket.Auts().Of(form)
                for superpacket in packet.super_packets()
                if form in superpacket.C()
            )
        return supers

    def invariant_form(self):
        return self.domain()

    def normalization_isometry(self):
        return self._normalization

    def supergroup(self):
        return self

    def _engine_group(self):
        r"""Return the private Sage orthogonal-group parent."""
        return self._engine_group_parent

    def _to_engine(self, automorphism):
        r"""Lower a live automorphism under the owned-group engine contract.

        The subgroup and G-set adapters in ``groups.py`` may use this
        crossing; the engine value stays private to those adapters.
        """
        if not self.accepts(automorphism):
            raise ValueError(f"{automorphism} is not an element of the orthogonal group {self}")
        return self._engine_group_parent(automorphism._engine())

    def _engine_subgroup_from_generators(self, generators):
        r"""Compute a generated subgroup without allocating another fixed Mor."""
        return self._engine_group_parent.subgroup(
            [self._to_engine(generator) for generator in generators]
        )

    def _to_subgroup_engine(self, automorphism, engine_subgroup):
        r"""Lower an ambient automorphism into the subgroup's private engine."""
        return engine_subgroup(self._to_engine(automorphism))

    def _from_subgroup_engine(self, engine_element):
        r"""Raise a subgroup element as an automorphism in the ambient group."""
        return self._from_engine(engine_element)

    def _normalized_map(self, engine_automorphism):

        engine_automorphism = self._engine_group_parent(engine_automorphism)
        cover = self._engine_module.V()
        labels = tuple(self._normalized_form.module_generating_set())
        images = {}
        for label, basis_vector in zip(labels, cover.basis(), strict=True):
            image = self._engine_module(basis_vector) * engine_automorphism
            coordinates = cover.coordinates(image.lift())
            images[label] = self._normalized_form.linear_combination(
                {
                    target_label: _owned_engine_element(self._normalized_form.base_ring(), SageZZ(coefficient))
                    for target_label, coefficient in zip(
                        labels,
                        coordinates,
                        strict=True,
                    )
                    if coefficient
                }
            )
        return self._normalized_form.module_category().Mor(self._normalized_form, self._normalized_form)(images)

    def _from_engine_matrix(self, engine_matrix):
        r"""Cross one private engine matrix to an owned form automorphism.

        Implementation endpoint of
        :func:\`_torsion_form_automorphism_from_engine_matrix\`.  No
        engine-group parent escapes this object.
        """
        return self._from_engine(self._engine_group_parent(engine_matrix))

    def _from_engine(self, engine_automorphism):
        engine_automorphism = self._engine_group_parent(engine_automorphism)
        normalization = self.normalization_isometry()
        normalized_forward = self._normalized_map(engine_automorphism)
        normalized_inverse = self._normalized_map(~engine_automorphism)

        original = normalization.domain()
        forward = original.module_category().Mor(original, original)(
            {
                label: normalization.inverse()(
                    normalized_forward(
                        normalization.forward()(original.module_generator(label))
                    )
                )
                for label in original.module_generating_set()
            }
        )
        inverse = original.module_category().Mor(original, original)(
            {
                label: normalization.inverse()(
                    normalized_inverse(
                        normalization.forward()(original.module_generator(label))
                    )
                )
                for label in original.module_generating_set()
            }
        )
        return self.element_class(
            self,
            forward,
            inverse,
            engine_automorphism,
        )

    def from_morphism(self, morphism):
        r"""Return a live form automorphism as an element of this owned group."""
        if morphism.domain() is not self.domain() or morphism.codomain() is not self.domain():
            raise ValueError(
                f"{morphism} is not an automorphism of {self.domain()}: it is a morphism "
                f"{morphism.domain()} -> {morphism.codomain()}"
            )
        normalization = self.normalization_isometry()
        normalized_form = normalization.codomain()

        original_form = normalization.domain()
        forward = original_form.module_category().Mor(
            original_form,
            normalized_form,
        )(normalization.forward())
        inverse = normalized_form.module_category().Mor(
            normalized_form,
            normalization.domain(),
        )(normalization.inverse())
        from sage.matrix.constructor import matrix as sage_matrix

        labels = tuple(normalized_form.module_generating_set())
        engine_rows = []
        ring = normalized_form.base_ring()
        for source_label in labels:
            original = inverse(normalized_form.module_generator(source_label))
            image = forward(morphism(original))
            coefficients = normalized_form.framing_coefficients(image)
            engine_rows.append(
                [
                    _engine_element(
                        ring, coefficients.get(target_label, ring.zero())
                    )
                    for target_label in labels
                ]
            )
        # Sage's finite-form engine acts on coordinate rows on the right, so
        # the generator-image rows above are already in its convention.
        engine_matrix = sage_matrix(
            _engine_ring(ring),
            len(labels),
            len(labels),
            [entry for row in engine_rows for entry in row],
        )
        return self._from_engine(self._engine_group_parent(engine_matrix))

    def _element_constructor_(self, datum):

        if isinstance(datum, TorsionFormAutomorphism):
            if datum.domain() is not self.domain():
                raise ValueError(
                    f"{datum} is an automorphism of {datum.domain()}, not of {self.domain()}"
                )
            if datum.parent() is self:
                return datum
            return self._from_engine(datum._engine())
        if isinstance(datum, ModuleMorphism):
            return self.from_morphism(datum)
        return self._from_engine(datum)

    def accepts(self, candidate) -> bool:
        r"""Admit a raw form automorphism to this finite group of maps.

        A differently parented automorphism of the exact same form can be
        checked by the maintained engine's exact element predicate. This is
        raw-arrow admission, also used before constructing a fixed-Mor
        object, not category containment. The
        inherited containment reads placement for the constructed objects and
        delegates only raw morphisms to this operation.
        """
        match candidate:
            case TorsionFormAutomorphism() if candidate.parent() is self:
                return True
            case TorsionFormAutomorphism() if candidate.domain() is self.domain():
                return candidate._engine() in self._engine_group_parent
            case _:
                return False

    @cached_method
    def one(self):
        return self._from_engine(self._engine_group_parent.one())

    def identity(self, *args, **kwargs):
        return self.one(*args, **kwargs)
    def identity_automorphism(self, *args, **kwargs):
        return self.one(*args, **kwargs)

    def order(self):
        return self.domain().base_ring()(int(self._engine_group_parent.order()))

    cardinality = order

    def __iter__(self):
        return (self._from_engine(element) for element in self._engine_group_parent)

    @cached_method
    def element_action(self):
        r"""Return the represented action of this group on the finite form."""
        return _torsion_form_element_action(self.domain(), self)

    def orbit(self, element):
        r"""Return the orbit of ``element`` through the owned G-set action."""
        element = self.domain()(element)
        action = self.element_action()
        orbits = action.orbits()
        return orbits.orbit_of(element).points()

    def subgroup_on(self, group_generators):
        r"""Return the generated subgroup with its ambient automorphisms unchanged.

        ``Subgroups(self)`` owns its inclusion. The subgroup is a group, not
        another realization of this form's fixed Iso category. Restrict the
        form action along that inclusion to obtain its action on the form.
        """
        supplied = tuple(group_generators)
        if any(generator.parent() is not self for generator in supplied):
            raise ValueError(
                f"a subgroup of {self} is generated by elements of {self}, but {supplied} contains an element "
                "of another group"
            )
        return self.subgroup(supplied)

    def stabilizer_of_element(self, element):
        r"""Return the point stabilizer through the represented G-set action."""
        element = self.domain()(element)
        return self.element_action().stabilizer(element)

    def stabilizer_of_subgroup(self, subgroup):
        r"""Return the setwise stabilizer through the owned subobject G-set."""
        form = self.domain()
        base_ring = form.base_ring()
        if subgroup not in ModuleSubobjects(base_ring):
            raise TypeError(
                f"the stabilizer in {self} is taken of a submodule of {form}, but {subgroup} "
                "has no inclusion morphism"
            )
        if subgroup not in Modules(base_ring).Subobjects(form):
            raise ValueError(
                f"the stabilizer in {self} is taken of a submodule of {form}, but {subgroup} "
                f"is a submodule of {subgroup.inclusion().codomain()}"
            )
        family = _torsion_form_all_subobjects(
            form,
            quadratic=self.is_quadratic(),
        )
        by_embedded_elements = {
            _embedded_elements(candidate): candidate
            for candidate in family
        }
        embedded = _embedded_elements(subgroup)
        if embedded not in by_embedded_elements:
            raise ValueError(
                f"{subgroup} does not match any submodule of {form}, so {self} has no stabilizer for it"
            )
        point = by_embedded_elements[embedded]
        action = _torsion_form_subobject_action(form, family, self)
        return action.stabilizer(point)

    stabilizer_of_subobject = stabilizer_of_subgroup

    def _repr_(self):
        return f"Orthogonal group of {self.domain()}"


def _torsion_form_automorphism_from_engine_matrix(orthogonal_group, engine_matrix):
    r"""Raise one exact backend matrix to an owned torsion-form automorphism.

    Protected torsion-form contract (\`OWN-05\`--\`OWN-07\`).  The
    permitted caller is the lattice centralizer-image adapter, which receives
    exact matrices from OSCAR in the common Smith-generator row convention.
    The matrix is consumed by this torsion-form owner and the returned value is
    an owned automorphism; neither the private orthogonal-group parent nor an
    engine element leaves this dispatcher.
    """
    if not isinstance(orthogonal_group, TorsionFormOrthogonalGroup):
        raise TypeError(
            f"an automorphism matrix is interpreted only in the orthogonal group of a torsion form, "
            f"but {orthogonal_group} is not one"
        )
    return orthogonal_group._from_engine_matrix(engine_matrix)


def _torsion_form_automorphism_group(form, *, quadratic: bool):
    category = (
        _torsion_form_modules(form.base_ring(), quadratic=True)
        if quadratic
        else _torsion_form_modules(form.base_ring(), quadratic=False)
    )
    return category.Aut(form)


class _TorsionFormIsoCategoryConstruction(IsoCategoryConstruction):
    r"""Finite torsion-form isometries with maintained orthogonal groups on the diagonal."""

    quadratic = False

    def Of(self, domain, codomain=None):
        if codomain is None:
            codomain = domain
        if domain is not codomain:
            return super().Of(domain, codomain)
        # Endpoint identity, not equality: two equal torsion forms are two
        # objects, each with its own orthogonal group.
        cached = self._cached_between(domain, domain)
        if cached is not None:
            return cached
        group = TorsionFormOrthogonalGroup(self, domain, quadratic=self.quadratic)
        return self._remember_between(domain, domain, group)


class TorsionBilinearFormIsoCategoryConstruction(_TorsionFormIsoCategoryConstruction):
    quadratic = False


class TorsionQuadraticFormIsoCategoryConstruction(_TorsionFormIsoCategoryConstruction):
    quadratic = True


def _invariant_factor_form_isomorphism(form, quadratic: bool):
    r"""Transport ``form`` to the invariant-factor framing, with its isometry.

    The underlying module normalization is the explicit Smith isomorphism
    ``M -> M_if``.  The form on ``M_if`` is obtained by pulling the selected
    bilinear lift along its inverse, so no form data are inferred from an
    abstract invariant-factor decomposition.
    """
    module = form.unformed_module()

    module_isomorphism = _module_invariant_factor_form(module)
    normalized_module = module_isomorphism.codomain()
    preimages = tuple(
        form(module_isomorphism.inverse()(generator))
        for generator in normalized_module.module_generators()
    )
    if quadratic:
        quadratic_form = form.form()
        gram = tuple(
            tuple(quadratic_form.lift_pairing(left, right) for right in preimages)
            for left in preimages
        )
        normalized = _torsion_form_modules(form.base_ring(), quadratic=True).from_module(
            normalized_module,
            gram,
            form.value_module(),
        )
    else:
        gram = tuple(
            tuple(form.b(left, right) for right in preimages)
            for left in preimages
        )
        normalized = _torsion_form_modules(form.base_ring(), quadratic=False).from_module(
            normalized_module,
            gram,
            form.value_module(),
        )

    forward_images = {
        label: normalized(module_isomorphism(module(form.module_generator(label))))
        for label in form.module_generating_set()
    }
    forward = form.module_category().Mor(form, normalized)(forward_images)

    inverse_images = {
        label: form(module_isomorphism.inverse()(normalized_module(normalized.module_generator(label))))
        for label in normalized.module_generating_set()
    }
    inverse = normalized.module_category().Mor(normalized, form)(inverse_images)
    return _torsion_form_isometry(forward, inverse, quadratic=quadratic)


class CokernelTorsionFormModules(OwnedCategoryOverBaseRing):
    r"""Finite formed modules retained as literal cokernels of a selected module map."""

    @classmethod
    def _repr_object_names(cls):
        return "cokernel torsion forms"

    def super_categories(self):
        return [Modules(self.base_ring()).FinitelyPresented().Torsion()]

    class ParentMethods:
        def cover(self):
            r"""Return the codomain of the selected presentation map."""
            return self.presentation().codomain()

        @cached_method
        def projection(self):
            r"""Return the quotient projection from the cover to this formed cokernel."""
            unformed_projection = self.presentation().cokernel_projection()
            if unformed_projection.codomain() is not self.unformed_module():
                raise ArithmeticError(
                    f"the cokernel projection of {self.presentation()} lands in {unformed_projection.codomain()}, "
                    f"not in the module underlying {self}"
                )
            cover = unformed_projection.domain()
            return cover.module_category().Mor(cover, self)(
                {
                    label: self(unformed_projection(cover.module_generator(label)))
                    for label in cover.module_generating_set()
                }
            )

    class ElementMethods:
        def coset_representative(self):
            r"""Return the selected lift of this class to the cokernel cover."""
            formed = self.parent()
            unformed = formed.unformed_module()
            coordinates = unformed.framing_coefficients(unformed(self))
            cover = formed.cover()
            return cover.linear_combination(
                {
                    label: coordinates[label]
                    for label in cover.module_generating_set()
                    if label in coordinates
                }
            )


__all__ = [
    "CokernelTorsionFormModules",
    "TorsionFormAutomorphism",
    "TorsionFormIsometry",
    "TorsionFormOrthogonalGroup",
]
