r"""Finite presented torsion modules equipped with exact forms.

The underlying module and its chosen presentation are first-class data.  A
Gram array defines a form on the quotient exactly when it annihilates the
relation submodule in the appropriate sense; these constructors check that
descent before equipping the module with the form.
"""

from sage.categories.morphism import SetMorphism
from sage.libs.gap.libgap import libgap
from sage.misc.cachefunc import cached_method
from sage.misc.classcall_metaclass import typecall
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    CategoricalIsomorphism,
    core_mor,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    IsoCategoryConstruction,
    category_packet,
)
from dzack_research.preamble.categories.modules.pure.torsion_modules import (
    FinitelyPresentedTorsionModules,
    refine_finitely_presented_torsion_module,
)
from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.refine import refine
from dzack_research.preamble.tensors.tensor import tensor
from dzack_research.preamble.tensors.tensor import (
    _engine_component_matrix,
)


def _gram_rows(gram, rank):
    try:
        parent = gram.parent()
    except AttributeError:
        parent = None
    if parent is not None:
        from dzack_research.preamble.categories.modules.pure.modules import MatrixSpaces

        try:
            is_matrix = parent in MatrixSpaces(parent.base_ring())
        except (AttributeError, TypeError, ValueError):
            is_matrix = False
        if is_matrix:
            rows = tuple(
                tuple(gram[row, column] for column in range(parent.ncols()))
                for row in range(parent.nrows())
            )
        else:
            rows = tuple(
                tuple(row) for row in gram.components()
            )
    else:
        rows = tuple(tuple(row) for row in gram)
    if len(rows) != rank or any(len(row) != rank for row in rows):
        raise ValueError(f"the Gram presentation must have shape {rank} x {rank}")
    return rows


def _coerced_gram(value_module, gram, rank):
    return tuple(tuple(value_module(entry) for entry in row) for row in _gram_rows(gram, rank))


def _linear_combination(value_module, coefficients, values):
    return sum(
        (coefficient * value for coefficient, value in zip(coefficients, values, strict=True) if coefficient),
        value_module.zero(),
    )


def _bilinear_descends(relations, gram, value_module) -> bool:
    rank = len(gram)
    for relation in relations.rows():
        row = tuple(relation)
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
    for relation in relations.rows():
        row = tuple(relation)
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
                raise ValueError("the stated isomorphism does not preserve the quadratic form")
            return
        if any(
            source.b(left, right) != target.b(forward(left), forward(right))
            for left in generators
            for right in generators
        ):
            raise ValueError("the stated isomorphism does not preserve the bilinear form")

    def is_quadratic(self) -> bool:
        return self._quadratic


def torsion_form_isometry(forward, inverse, *, quadratic: bool):
    r"""Return the form isometry represented by mutually inverse module maps."""
    return TorsionFormIsometry(
        core_mor(forward.domain(), forward.codomain()),
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
            lambda index: labels.unrank(i) if int(index) == 0 else labels.unrank(j)
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
        raise NotImplementedError(
            "the available finite-form engine does not retain the whole presented module"
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
    return form.forget_form_morphism()(element)


def _coordinate_rows(form, generators):
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_coefficients,
    )

    module = _underlying_presented_module(form)
    ring = module.base_ring()
    labels = module.module_generating_set()
    def coordinate_rows():
        for generator in generators:
            coefficients = module_coefficients(
                _underlying_element(form, generator), module
            )
            yield (
                coefficients.get(label, ring.zero())
                for label in labels
            )

    return MatrixSpace(
        ring, len(generators), int(labels.cardinality())
    ).from_rows(coordinate_rows())


def _relations_among_generators(form, generators):
    r"""Return the relation matrix for a selected generating family of ``form``."""
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        _presentation_matrix,
    )

    module = _underlying_presented_module(form)
    ring = module.base_ring()
    lifts = _coordinate_rows(form, generators)
    known_tensor = _presentation_matrix(module)
    known = MatrixSpace(ring, *known_tensor.tensor_shape()).from_tensor(known_tensor)
    combined = lifts.stack(known)
    kernel = combined.matrix().transpose().kernel()
    relations = (
        combined.codomain().left_projection() * kernel.inclusion()
    ).image()
    return relations.inclusion().matrix().transpose()


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


def _regenerate_form_on_generators(form, generators, *, quadratic: bool):
    r"""Return ``form -> form'`` for the same finite form on a new framing."""
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        _presentation_matrix,
    )
    from dzack_research.preamble.categories.modules.pure.torsion_modules import (
        _torsion_module_presented_by_matrix,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        _solve_left_integrally_element,
        module_coefficients,
        module_homset,
    )
    from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

    generators = tuple(generators)
    if any(generator not in form for generator in generators):
        raise TypeError("a change of framing is specified by elements of this finite form")
    module = _underlying_presented_module(form)
    ring = module.base_ring()
    labels = finite_ordered_set(range(len(generators)))
    relations = _relations_among_generators(form, generators)
    regenerated_module = _torsion_module_presented_by_matrix(relations, labels)
    if quadratic:
        regenerated = TorsionQuadraticFormModules(form.base_ring()).from_module(
            regenerated_module,
            _quadratic_gram_on(form, generators),
            _value_module(form, quadratic=True),
        )
    else:
        gram = tuple(
            tuple(form.b(left, right) for right in generators)
            for left in generators
        )
        regenerated = TorsionBilinearFormModules(form.base_ring()).from_module(
            regenerated_module,
            gram,
            _value_module(form, quadratic=False),
        )

    inverse = module_homset(regenerated, form)(
        {label: generator for label, generator in zip(labels, generators, strict=True)}
    )

    from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace

    lifts = _coordinate_rows(form, generators)
    known_tensor = _presentation_matrix(module)
    known = MatrixSpace(ring, *known_tensor.tensor_shape()).from_tensor(known_tensor)
    system = lifts.stack(known).matrix()
    source_labels = tuple(form.module_generating_set())
    regenerated_generators = tuple(regenerated.module_generators())
    forward_images = {}
    for position, source_label in enumerate(source_labels):
        target = [
            ring.one() if index == position else ring.zero()
            for index in range(len(source_labels))
        ]
        solution = _solve_left_integrally_element(system, target, ring)
        generator_solution = system.codomain().left_projection()(solution)
        generator_coefficients = module_coefficients(
            generator_solution, lifts.codomain()
        )
        lift_labels = lifts.codomain().module_generating_set()
        forward_images[source_label] = sum(
            (
                regenerated.scalar_multiple(
                    generator_coefficients.get(
                        lift_labels.unrank(index), ring.zero()
                    ),
                    generator,
                )
                for index, generator in enumerate(regenerated_generators)
                if generator_coefficients.get(
                    lift_labels.unrank(index), ring.zero()
                )
            ),
            regenerated.zero(),
        )
    forward = module_homset(form, regenerated)(forward_images)
    return torsion_form_isometry(forward, inverse, quadratic=quadratic)


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
                    label: ring._from_engine_element(SageZZ(coefficient))
                    for label, coefficient in zip(labels, coordinates, strict=True)
                    if coefficient
                }
            )
            generators.append(normalization.inverse()(normalized_element))
        result[normalized.base_ring()._from_engine_element(SageZZ(prime))] = tuple(generators)
    return result


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
            from dzack_research.preamble.categories.rings.ring_foundation import _engine_element

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
                        ring._from_engine_element(SageZZ(coefficient)), generator
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
    return result


def p_adic_jordan_module_generators(form, *, quadratic: bool):
    r"""Return the selected Jordan generators, prime by prime, inside ``form``."""
    decomposition = _p_adic_jordan_decomposition(form, quadratic=quadratic)
    return tuple(
        generator
        for prime in sorted(decomposition)
        for generator in decomposition[prime]
    )


def _p_adic_jordan_form(form, *, quadratic: bool):
    generators = p_adic_jordan_module_generators(form, quadratic=quadratic)
    return _regenerate_form_on_generators(form, generators, quadratic=quadratic)


def _twisted_torsion_form(form, scalar, *, quadratic: bool):
    generators = tuple(form.module_generators())
    module = _underlying_presented_module(form)
    if quadratic:
        gram = tuple(
            tuple(scalar * entry for entry in row)
            for row in _quadratic_gram_on(form, generators)
        )
        return TorsionQuadraticFormModules(form.base_ring()).from_module(
            module,
            gram,
            _value_module(form, quadratic=True),
        )
    gram = tuple(
        tuple(scalar * form.b(left, right) for right in generators)
        for left in generators
    )
    return TorsionBilinearFormModules(form.base_ring()).from_module(
        module,
        gram,
        _value_module(form, quadratic=False),
    )


def _engine_normal_form_key(form, *, quadratic: bool):
    normalization = form.invariant_factor_form()
    engine = _engine_torsion_form(normalization.codomain(), quadratic=quadratic)
    normal = engine.normal_form()
    gram = normal.gram_matrix_quadratic()
    return (
        SageQQ(engine._modulus),
        SageQQ(engine._modulus_qf),
        tuple(SageZZ(invariant) for invariant in normal.invariants()),
        tuple(tuple(SageQQ(entry) for entry in row) for row in gram.components()),
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
        r"""Return the private Sage representative used for computation."""
        return self._engine_element

    def inverse_morphism(self):
        r"""Return the underlying inverse module morphism."""
        return self._inverse

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


class TorsionFormOrthogonalGroup(CategoricalHomset):
    r"""The finite group of live automorphisms preserving one finite form."""

    Element = TorsionFormAutomorphism

    @staticmethod
    def __classcall__(cls, hom_family, form, **options):
        return typecall(cls, hom_family, form, **options)

    def __init__(
        self,
        hom_family,
        form,
        *,
        quadratic: bool,
        normalization=None,
        engine_module=None,
        engine_group=None,
        supergroup=None,
    ) -> None:
        from dzack_research.preamble.categories.group.groups import OwnedFiniteGroups

        self._quadratic = bool(quadratic)
        self._normalization = (
            form.invariant_factor_form()
            if normalization is None
            else normalization
        )
        self._normalized_form = self._normalization.codomain()
        self._engine_module = (
            _engine_torsion_form(
                self._normalized_form,
                quadratic=self._quadratic,
            )
            if engine_module is None
            else engine_module
        )
        self._engine_group_parent = (
            self._engine_module.orthogonal_group()
            if engine_group is None
            else engine_group
        )
        self._supergroup = self if supergroup is None else supergroup
        CategoricalHomset.__init__(
            self,
            hom_family,
            form,
            form,
        )
        refine(self, OwnedFiniteGroups())

    def is_quadratic(self) -> bool:
        return self._quadratic

    def super_categories(self):
        if self.supergroup() is not self:
            return [self.supergroup()]
        packet = category_packet(self.base_category())
        form = self.domain()
        supers = [
            packet.Homs().Of(form, form),
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
        return self._supergroup

    def _engine_group(self):
        r"""Return the private Sage orthogonal-group parent."""
        return self._engine_group_parent

    def _normalized_map(self, engine_automorphism):
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_homset,
        )

        engine_automorphism = self._engine_group_parent(engine_automorphism)
        cover = self._engine_module.V()
        labels = tuple(self._normalized_form.module_generating_set())
        images = {}
        for label, basis_vector in zip(labels, cover.basis(), strict=True):
            image = self._engine_module(basis_vector) * engine_automorphism
            coordinates = cover.coordinates(image.lift())
            images[label] = self._normalized_form.linear_combination(
                {
                    target_label: self._normalized_form.base_ring()._from_engine_element(SageZZ(coefficient))
                    for target_label, coefficient in zip(
                        labels,
                        coordinates,
                        strict=True,
                    )
                    if coefficient
                }
            )
        return module_homset(self._normalized_form, self._normalized_form)(images)

    def _from_engine_matrix(self, engine_matrix):
        r"""Cross one private engine matrix to an owned form automorphism.

        Protected contract for exact backend consumers: no engine-group parent
        escapes this object; callers hand the engine matrix in and receive the
        owned automorphism back.
        """
        return self._from_engine(self._engine_group_parent(engine_matrix))

    def _from_engine(self, engine_automorphism):
        engine_automorphism = self._engine_group_parent(engine_automorphism)
        normalization = self.normalization_isometry()
        normalized_forward = self._normalized_map(engine_automorphism)
        normalized_inverse = self._normalized_map(~engine_automorphism)
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_homset,
        )

        original = normalization.domain()
        forward = module_homset(original, original)(
            {
                label: normalization.inverse()(
                    normalized_forward(
                        normalization.forward()(original.module_generator(label))
                    )
                )
                for label in original.module_generating_set()
            }
        )
        inverse = module_homset(original, original)(
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
            raise ValueError("the automorphism must act on this finite form")
        normalization = self.normalization_isometry()
        normalized_form = normalization.codomain()
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_coefficients,
            module_homset,
        )

        forward = module_homset(
            normalization.domain(), normalized_form
        )(normalization.forward())
        inverse = module_homset(
            normalized_form, normalization.domain()
        )(normalization.inverse())
        from dzack_research.preamble.categories.rings.ring_foundation import (
            _engine_element,
            _engine_ring,
        )
        from sage.matrix.constructor import matrix as sage_matrix

        labels = tuple(normalized_form.module_generating_set())
        engine_rows = []
        ring = normalized_form.base_ring()
        for source_label in labels:
            original = inverse(normalized_form.module_generator(source_label))
            image = forward(morphism(original))
            coefficients = module_coefficients(image, normalized_form)
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
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            ModuleMorphism,
        )

        if isinstance(datum, TorsionFormAutomorphism):
            if datum.parent() is self:
                return datum
            return self._from_engine(datum._engine())
        if isinstance(datum, ModuleMorphism):
            return self.from_morphism(datum)
        return self._from_engine(datum)

    def __contains__(self, candidate) -> bool:
        if not isinstance(candidate, TorsionFormAutomorphism):
            return False
        if candidate.parent() is self:
            return True
        if candidate.parent().domain() is not self.domain():
            return False
        try:
            return candidate._engine() in self._engine_group_parent
        except (TypeError, ValueError):
            return False

    @cached_method
    def one(self):
        return self._from_engine(self._engine_group_parent.one())

    identity = one
    identity_automorphism = one

    @cached_method
    def group_generators(self):
        from dzack_research.preamble.categories.sets.set_categories import Sets
        from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_image

        engine_generators = self._engine_group_parent.gens()
        positions = Sets.Δ[len(engine_generators) - 1]
        return finite_ordered_image(
            positions,
            lambda position: self._from_engine(engine_generators[int(position)]),
            name="Torsion-form automorphism generators",
        )

    def number_of_group_generators(self):
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return _own_ring(SageZZ)(self.group_generators().cardinality())

    def order(self):
        return self.domain().base_ring()(int(self._engine_group_parent.order()))

    cardinality = order

    def __iter__(self):
        return (self._from_engine(element) for element in self._engine_group_parent)

    def _engine_abelian_element(self, element):
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_coefficients,
        )

        element = self.domain()(element)
        normalized = self.normalization_isometry()(element)
        labels = tuple(self._normalized_form.module_generating_set())
        coefficients = module_coefficients(normalized, self._normalized_form)
        cover = self._engine_module.V()
        lifted = sum(
            (
                SageZZ(coefficients.get(label, 0)) * basis
                for label, basis in zip(labels, cover.basis(), strict=True)
            ),
            cover.zero(),
        )
        _engine_element = self._engine_module(lifted)
        abelian_group = self._engine_group_parent.domain()
        result = abelian_group.one()
        for exponent, generator in zip(
            _engine_element.vector(),
            abelian_group.gens(),
            strict=True,
        ):
            result *= generator ** SageZZ(exponent)
        return result

    def _from_engine_abelian_element(self, _engine_element):
        abelian_group = self._engine_group_parent.domain()
        _engine_element = abelian_group(_engine_element)
        module_element = self._engine_module.linear_combination_of_smith_form_gens(
            _engine_element.exponents()
        )
        cover = self._engine_module.V()
        coordinates = cover.coordinates(module_element.lift())
        labels = tuple(self._normalized_form.module_generating_set())
        normalized = self._normalized_form.linear_combination(
            {
                label: SageZZ(coefficient)
                for label, coefficient in zip(labels, coordinates, strict=True)
                if coefficient
            }
        )
        return self.normalization_isometry().inverse()(normalized)

    def orbit(self, element):
        from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

        point = self._engine_abelian_element(element)
        orbit = libgap.Orbit(
            self._engine_group_parent.gap(),
            point.gap(),
            libgap.OnPoints,
        )
        return finite_ordered_set(
            self._from_engine_abelian_element(image)
            for image in orbit
        )

    def subgroup_on(self, group_generators):
        supplied = tuple(group_generators)
        if any(generator.parent() is not self for generator in supplied):
            raise ValueError("orthogonal subgroup generators must belong to this group")
        engine_subgroup = self._engine_group_parent.subgroup(
            [generator._engine() for generator in supplied]
        )
        subgroup = TorsionFormOrthogonalGroup(
            self.hom_family(),
            self.domain(),
            quadratic=self.is_quadratic(),
            normalization=self._normalization,
            engine_module=self._engine_module,
            engine_group=engine_subgroup,
            supergroup=self,
        )
        subgroup._preamble_supergroup = self
        from dzack_research.preamble.categories.group.groups import (
            OwnedFiniteGroups,
            Subgroups,
        )

        return refine(subgroup, [OwnedFiniteGroups(), Subgroups(self)])

    def stabilizer_of_element(self, element):
        point = self._engine_abelian_element(element)
        gap_stabilizer = libgap.Stabilizer(
            self._engine_group_parent.gap(),
            point.gap(),
            libgap.OnPoints,
        )
        engine_subgroup = self._engine_group_parent._subgroup_constructor(gap_stabilizer)
        return TorsionFormOrthogonalGroup(
            self.hom_family(),
            self.domain(),
            quadratic=self.is_quadratic(),
            normalization=self._normalization,
            engine_module=self._engine_module,
            engine_group=engine_subgroup,
            supergroup=self,
        )

    def stabilizer_of_subgroup(self, subgroup):
        if subgroup.ambient_discriminant_module() is not self.domain():
            raise ValueError("the stabilized subgroup must lie in this form")
        points = libgap.Set(
            [
                self._engine_abelian_element(element).gap()
                for element in subgroup.embedded_elements()
            ]
        )
        gap_stabilizer = libgap.Stabilizer(
            self._engine_group_parent.gap(),
            points,
            libgap.OnSets,
        )
        engine_subgroup = self._engine_group_parent._subgroup_constructor(gap_stabilizer)
        return TorsionFormOrthogonalGroup(
            self.hom_family(),
            self.domain(),
            quadratic=self.is_quadratic(),
            normalization=self._normalization,
            engine_module=self._engine_module,
            engine_group=engine_subgroup,
            supergroup=self,
        )

    stabilizer_of_subobject = stabilizer_of_subgroup

    def inclusion(self):
        supergroup = self.supergroup()
        return SetMorphism(
            self.Mor(supergroup),
            lambda element: (
                element
                if supergroup is self
                else supergroup._from_engine(element._engine())
            ),
        )

    def _repr_(self):
        if self.supergroup() is self:
            return f"Orthogonal group of {self.domain()}"
        return f"Subgroup of the orthogonal group of {self.domain()}"


def _torsion_form_automorphism_group(form, *, quadratic: bool):
    category = (
        TorsionQuadraticFormModules(form.base_ring())
        if quadratic
        else TorsionBilinearFormModules(form.base_ring())
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
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        _module_invariant_factor_form,
    )

    module_isomorphism = _module_invariant_factor_form(module)
    normalized_module = module_isomorphism.codomain()
    preimages = tuple(
        form.equip_form_morphism()(module_isomorphism.inverse()(generator))
        for generator in normalized_module.module_generators()
    )
    if quadratic:
        quadratic_form = form.form()
        gram = tuple(
            tuple(quadratic_form.lift_pairing(left, right) for right in preimages)
            for left in preimages
        )
        normalized = TorsionQuadraticFormModules(form.base_ring()).from_module(
            normalized_module,
            gram,
            form.value_module(),
        )
    else:
        gram = tuple(
            tuple(form.b(left, right) for right in preimages)
            for left in preimages
        )
        normalized = TorsionBilinearFormModules(form.base_ring()).from_module(
            normalized_module,
            gram,
            form.value_module(),
        )

    forward_images = {}
    for label in form.module_generating_set():
        source_generator = form.module_generator(label)
        unformed = form.forget_form_morphism()(source_generator)
        normalized_unformed = module_isomorphism(unformed)
        forward_images[label] = normalized.equip_form_morphism()(normalized_unformed)
    forward = form.Mor(normalized)(forward_images)

    inverse_images = {}
    for label in normalized.module_generating_set():
        normalized_generator = normalized.module_generator(label)
        unformed = normalized.forget_form_morphism()(normalized_generator)
        original_unformed = module_isomorphism.inverse()(unformed)
        inverse_images[label] = form.equip_form_morphism()(original_unformed)
    inverse = normalized.Mor(form)(inverse_images)
    return torsion_form_isometry(forward, inverse, quadratic=quadratic)


class TorsionBilinearFormModules(OwnedCategoryOverBaseRing):
    r"""Finitely presented torsion modules with a bilinear form."""

    @classmethod
    def _repr_object_names(cls):
        return "finitely presented torsion modules with a bilinear form"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
            FinitelyPresentedBilinearFormModules,
        )

        return [
            FinitelyPresentedTorsionModules(self.base_ring()),
            FinitelyPresentedBilinearFormModules(self.base_ring()),
        ]

    _IsoCategory = TorsionBilinearFormIsoCategoryConstruction

    def from_module(self, module, gram, value_module):
        r"""Equip ``module`` with the bilinear form represented by ``gram``.

        The value object is explicit.  Descent is checked on both arguments:
        every chosen relation must pair to zero with every chosen generator.
        """
        if module not in FinitelyPresentedTorsionModules(self.base_ring()):
            module = refine_finitely_presented_torsion_module(module)
        from dzack_research.preamble.categories.forms.forms import BilinearForms
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            _presentation_matrix,
        )
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule

        rank = int(module.module_generating_set().cardinality())
        values = _coerced_gram(value_module, gram, rank)
        relations = _presentation_matrix(module)
        if not _bilinear_descends(relations, values, value_module):
            raise ValueError("the bilinear form does not descend through the selected relations")
        formed = FormModule(BilinearForms(module, value_module)(values))
        return refine(formed, self)

    def from_relations_and_gram(self, relations, gram, value_module, module_generating_set=None):
        r"""Construct a torsion bilinear form from presentation and Gram data."""
        from dzack_research.preamble.categories.modules.pure.torsion_modules import (
            _torsion_module_presented_by_matrix,
        )

        module = _torsion_module_presented_by_matrix(relations, module_generating_set)
        return self.from_module(module, gram, value_module)

    class ParentMethods:
        def form_vanishes_on(self, elements) -> bool:
            elements = tuple(elements)
            return all(self.b(left, right) == self.value_module().zero() for left in elements for right in elements)

        @cached_method
        def invariant_factor_form(self):
            r"""Return the form-preserving isomorphism to invariant-factor framing."""
            return _invariant_factor_form_isomorphism(self, quadratic=False)

        def p_adic_jordan_decomposition(self):
            r"""Return the chosen Jordan generators indexed by their prime."""
            return _p_adic_jordan_decomposition(self, quadratic=False)

        def p_adic_jordan_module_generators(self):
            r"""Return the chosen prime-by-prime Jordan generating family."""
            return p_adic_jordan_module_generators(self, quadratic=False)

        def p_adic_jordan_form(self):
            r"""Return the explicit isometry to this form in Jordan framing."""
            return _p_adic_jordan_form(self, quadratic=False)

        normal_form = p_adic_jordan_form

        def twist(self, scalar):
            r"""Return the same finite module equipped with ``scalar*b``."""
            return _twisted_torsion_form(self, scalar, quadratic=False)

        def is_isomorphic(self, other) -> bool:
            r"""Decide isometry of represented finite symmetric bilinear forms."""
            if other not in TorsionBilinearFormModules(self.base_ring()):
                return False
            return _forms_are_isomorphic(self, other, quadratic=False)

        is_isometric_to = is_isomorphic

        def is_anti_isometric(self, other) -> bool:
            r"""Return whether ``(self,b)`` is isometric to ``(other,-b)``."""
            if other not in TorsionBilinearFormModules(self.base_ring()):
                return False
            return self.is_isomorphic(other.twist(-1))

        def pontryagin_dual_identification(self):
            r"""Return ``A -> Hom(A,K/R)``, ``x |-> b(x,-)``, for perfect ``b``."""
            from sage.categories.morphism import SetMorphism

            from dzack_research.preamble.categories.sets.set_categories import Sets as OwnedSets

            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )

            zero = self.zero()
            generators = tuple(self.module_generators())
            if any(
                element != zero
                and all(self.b(element, generator) == self.value_module().zero() for generator in generators)
                for element in self.elements()
            ):
                raise ValueError(
                    "the pairing does not identify this module with its Pontryagin dual because it is degenerate"
                )
            characters = module_homset(self, self.value_module())

            def character(element):
                element = self(element)
                return characters(
                    {
                        label: self.b(element, self.module_generator(label))
                        for label in self.module_generating_set()
                    }
                )

            return SetMorphism(OwnedSets().Mor(self, characters), character)

        @cached_method
        def automorphism_group(self):
            r"""Return ``O(A,b)`` as a finite owned group of live automorphisms."""
            return _torsion_form_automorphism_group(self, quadratic=False)

        def orthogonal_group(self):
            return self.automorphism_group()

        def O(self):  # noqa: E743 - standard mathematical notation O(A,b)
            return self.automorphism_group()


class TorsionQuadraticFormModules(OwnedCategoryOverBaseRing):
    r"""Finitely presented torsion modules with a quadratic form."""

    @classmethod
    def _repr_object_names(cls):
        return "finitely presented torsion modules with a quadratic form"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
            FinitelyPresentedQuadraticFormModules,
        )

        return [
            FinitelyPresentedTorsionModules(self.base_ring()),
            FinitelyPresentedQuadraticFormModules(self.base_ring()),
        ]

    _IsoCategory = TorsionQuadraticFormIsoCategoryConstruction

    def from_module(self, module, gram, value_module):
        r"""Equip ``module`` with ``q(x)=x^T gram x`` valued in ``value_module``.

        For every relation ``r`` we check both ``q(r)=0`` and vanishing of the
        polar value ``q(x+r)-q(x)-q(r)`` against every generator.  These are
        exactly the conditions for the quadratic map to descend to the quotient.
        """
        if module not in FinitelyPresentedTorsionModules(self.base_ring()):
            module = refine_finitely_presented_torsion_module(module)
        from dzack_research.preamble.categories.forms.forms import QuadraticForms
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            _presentation_matrix,
        )
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule

        rank = int(module.module_generating_set().cardinality())
        values = _coerced_gram(value_module, gram, rank)
        if any(values[i][j] != values[j][i] for i in range(rank) for j in range(rank)):
            raise ValueError("the chosen bilinear lift of a quadratic form must be symmetric")
        relations = _presentation_matrix(module)
        if not _quadratic_descends(relations, values, value_module):
            raise ValueError("the quadratic form does not descend through the selected relations")
        formed = FormModule(QuadraticForms(module, value_module)(values))
        return refine(formed, self)

    def from_relations_and_gram(self, relations, gram, value_module, module_generating_set=None):
        r"""Construct a torsion quadratic form from presentation and Gram data."""
        from dzack_research.preamble.categories.modules.pure.torsion_modules import (
            _torsion_module_presented_by_matrix,
        )

        module = _torsion_module_presented_by_matrix(relations, module_generating_set)
        return self.from_module(module, gram, value_module)

    class ParentMethods:
        def form_vanishes_on(self, elements) -> bool:
            return all(self.q(element) == self.value_module().zero() for element in elements)

        @cached_method
        def invariant_factor_form(self):
            r"""Return the quadratic-form isomorphism to invariant-factor framing."""
            return _invariant_factor_form_isomorphism(self, quadratic=True)

        def p_adic_jordan_decomposition(self):
            r"""Return the chosen quadratic Jordan generators indexed by prime."""
            return _p_adic_jordan_decomposition(self, quadratic=True)

        def p_adic_jordan_module_generators(self):
            r"""Return the chosen prime-by-prime quadratic Jordan generators."""
            return p_adic_jordan_module_generators(self, quadratic=True)

        def p_adic_jordan_form(self):
            r"""Return the explicit isometry to this quadratic form in Jordan framing."""
            return _p_adic_jordan_form(self, quadratic=True)

        normal_form = p_adic_jordan_form

        def twist(self, scalar):
            r"""Return the same finite module equipped with ``scalar*q``."""
            return _twisted_torsion_form(self, scalar, quadratic=True)

        def is_isomorphic(self, other) -> bool:
            r"""Decide isometry of represented finite quadratic forms."""
            if other not in TorsionQuadraticFormModules(self.base_ring()):
                return False
            return _forms_are_isomorphic(self, other, quadratic=True)

        is_isometric_to = is_isomorphic

        def is_anti_isometric(self, other) -> bool:
            r"""Return whether ``(self,q)`` is isometric to ``(other,-q)``."""
            if other not in TorsionQuadraticFormModules(self.base_ring()):
                return False
            return self.is_isomorphic(other.twist(-1))

        @cached_method
        def automorphism_group(self):
            r"""Return ``O(A,q)`` as a finite owned group of live automorphisms."""
            return _torsion_form_automorphism_group(self, quadratic=True)

        def orthogonal_group(self):
            return self.automorphism_group()

        def O(self):  # noqa: E743 - standard mathematical notation O(A,q)
            return self.automorphism_group()

        def associated_bilinear_form(self):
            r"""Polarize ``q:A->QQ/2ZZ`` to ``b_q:A^2->QQ/ZZ``.

            If ``q(x)=x^T G x`` modulo ``2ZZ``, then
            ``b_q(x,y)=x^T G y`` modulo ``ZZ``.  The halving of the ordinary
            polar value is well defined precisely because changing a lift in
            ``QQ/2ZZ`` by ``2ZZ`` changes its half by ``ZZ``.
            """
            value_module = self.value_module()
            if not hasattr(value_module, "modulus") or value_module.modulus() != 2:
                raise TypeError("this polarization currently requires a QQ/2ZZ-valued quadratic form")
            from dzack_research.preamble.categories.modules.framed.fraction_field_quotients import (
                FractionFieldQuotient,
            )

            bilinear_values = FractionFieldQuotient(self.base_ring(), 1)
            quadratic_form = self.form()
            module = self.unformed_module()
            from dzack_research.preamble.categories.forms.forms import BilinearForms
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule

            equip = self.equip_form_morphism()
            associated = FormModule(
                BilinearForms(module, bilinear_values)(
                    lambda left, right: bilinear_values(
                        value_module.lift(
                            quadratic_form.lift_pairing(equip(left), equip(right))
                        )
                    )
                )
            )
            return refine(
                associated,
                TorsionBilinearFormModules(self.base_ring()),
            )


__all__ = [
    "TorsionBilinearFormModules",
    "TorsionFormAutomorphism",
    "TorsionFormIsometry",
    "TorsionFormOrthogonalGroup",
    "TorsionQuadraticFormModules",
    "p_adic_jordan_module_generators",
    "torsion_form_isometry",
]
