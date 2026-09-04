r"""Exact vector-orbit data for owned lattices."""

from sage.misc.cachefunc import cached_method


class VectorPrimitiveExtension:
    r"""Nikulin's primitive extension cut out by one anisotropic primitive vector.

    For ``w in L`` this records

    ``M = Zw ⊥ w^perp -> L``

    together with its finite index, the two discriminant inclusions into
    ``A_M``, the gluing subgroup ``H=L/M <= A_M``, and representatives of
    ``A_L`` in ``H^perp``.
    """

    def __init__(self, lattice, element) -> None:
        vector = (
            element
            if getattr(element, "parent", lambda: None)() is lattice
            else lattice(element)
        )
        if vector.q() == 0:
            raise ValueError("VectorPrimitiveExtension requires an anisotropic vector")
        ring = lattice.base_ring()
        coordinates = tuple(ring(coordinate) for coordinate in vector.to_tuple())
        divisor = ring.zero()
        for coordinate in coordinates:
            divisor = divisor.gcd(coordinate)
        if abs(divisor) != ring.one():
            raise ValueError("VectorPrimitiveExtension is normalized to a primitive vector")
        if not lattice.is_finite_rank() or not lattice.is_nondegenerate():
            raise ValueError("VectorPrimitiveExtension requires a finite nondegenerate lattice")

        line = lattice.subobject_on((vector,))
        complement = line.orthogonal_complement()
        if line.rank() + complement.rank() != lattice.rank():
            raise ArithmeticError("the anisotropic line does not have complementary orthogonal rank")
        line_lattice = line.inclusion().domain()
        complement_lattice = complement.inclusion().domain()
        sum_lattice = line_lattice + complement_lattice

        line_images = tuple(
            line.inclusion()(generator)
            for generator in line_lattice.module_generators()
        )
        complement_images = tuple(
            complement.inclusion()(generator)
            for generator in complement_lattice.module_generators()
        )
        inclusion = sum_lattice.Emb(lattice)(line_images + complement_images)
        ring = lattice.base_ring()
        index = ring(int(inclusion.index().finite_value()))
        if index <= ring.zero():
            raise ArithmeticError("the line and complement do not span a finite-index sublattice")

        sum_generators = tuple(sum_lattice.module_generators())
        split = int(line_lattice.rank())
        line_in_sum = line_lattice.Emb(sum_lattice)(sum_generators[:split])
        complement_in_sum = complement_lattice.Emb(sum_lattice)(sum_generators[split:])
        line_discriminant_inclusion = line_in_sum.discriminant_inclusion()
        complement_discriminant_inclusion = complement_in_sum.discriminant_inclusion()

        sum_form = sum_lattice.discriminant_group()
        sum_dual = sum_lattice.dual_lattice()
        dual_labels = tuple(sum_dual.module_generating_set())
        gluing_classes = []
        for ambient_generator in lattice.module_generators():
            pairings = tuple(
                lattice.b(ambient_generator, inclusion(generator))
                for generator in sum_generators
            )
            dual_element = sum_dual.linear_combination(
                {
                    label: ring(coefficient)
                    for label, coefficient in zip(dual_labels, pairings, strict=True)
                    if coefficient
                }
            )
            gluing_classes.append(sum_form.projection()(dual_element))
        gluing_subgroup = sum_form.subgroup_on(tuple(gluing_classes))
        if int(gluing_subgroup.cardinality()) != int(index):
            raise ArithmeticError("the gluing subgroup does not have order [L:M]")
        gluing_images = tuple(gluing_subgroup.embedded_elements())
        if any(
            sum_form.b(left, right) != sum_form.bilinear_value_module().zero()
            for left in gluing_images
            for right in gluing_images
        ):
            raise ArithmeticError("L/M is not isotropic for the discriminant bilinear form of M")
        if lattice.is_even() and any(
            sum_form.q(element) != sum_form.quadratic_value_module().zero()
            for element in gluing_images
        ):
            raise ArithmeticError("L/M is not isotropic for the discriminant quadratic form of M")

        discriminant_form = lattice.discriminant_group()
        dual_restriction = inclusion.matrix().transpose()
        lattice_rank = int(lattice.rank())
        discriminant_representatives = []
        for position in range(lattice_rank):
            dual_element = sum_dual.linear_combination(
                {
                    dual_labels[row]: dual_restriction[row, position]
                    for row in range(dual_restriction.parent().nrows())
                    if dual_restriction[row, position]
                }
            )
            discriminant_representatives.append(sum_form.projection()(dual_element))
        discriminant_representatives = tuple(discriminant_representatives)
        if any(
            sum_form.b(representative, glued) != sum_form.bilinear_value_module().zero()
            for representative in discriminant_representatives
            for glued in gluing_images
        ):
            raise ArithmeticError("the representatives of A_L do not lie in H^perp")

        self.lattice = lattice
        self.vector = vector
        self.line = line
        self.complement = complement
        self.sum_lattice = sum_lattice
        self.inclusion = inclusion
        self.index = index
        self.sum_form = sum_form
        self.line_discriminant_inclusion = line_discriminant_inclusion
        self.complement_discriminant_inclusion = complement_discriminant_inclusion
        self.gluing_subgroup = gluing_subgroup
        self.gluing_images = gluing_images
        self.discriminant_form = discriminant_form
        self.discriminant_representatives = discriminant_representatives

    def representative_of(self, discriminant_class):
        r"""Return the selected representative in ``A_M`` of a class of ``A_L``."""
        discriminant_class = self.discriminant_form(discriminant_class)
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_coefficients,
        )

        coefficients = module_coefficients(
            discriminant_class,
            self.discriminant_form,
        )
        return sum(
            (
                coefficients[label] * representative
                for label, representative in zip(
                    self.discriminant_form.module_generating_set(),
                    self.discriminant_representatives,
                    strict=True,
                )
                if label in coefficients and coefficients[label]
            ),
            self.sum_form.zero(),
        )

    @cached_method
    def _representative_table(self):
        r"""Return the exact quotient lookup ``H^perp -> A_L``."""
        table = {}
        for discriminant_class in self.discriminant_form.elements():
            representative = self.representative_of(discriminant_class)
            for glued in self.gluing_images:
                element = representative + glued
                key = self.sum_form(element)
                previous = table.get(key)
                if previous is not None and previous != discriminant_class:
                    raise ArithmeticError(
                        "two classes of A_L define the same coset in H^perp/H"
                    )
                table[key] = discriminant_class
        expected = int(self.discriminant_form.cardinality()) * int(
            self.gluing_subgroup.cardinality()
        )
        if len(table) != expected:
            raise ArithmeticError("the selected representatives do not fill H^perp")
        return table

    def class_of_representative(self, element):
        r"""Return the class of ``A_L`` represented by an element of ``H^perp``."""
        key = self.sum_form(element)
        try:
            return self._representative_table()[key]
        except KeyError as error:
            raise ValueError("the element lies outside H^perp and represents no class of A_L") from error

    def complement_is_definite(self) -> bool:
        r"""Return whether the orthogonal complement is definite."""
        positive, negative = self.complement.signature_pair()
        return positive == 0 or negative == 0


def _isometries_between_definite_lattices(source, target):
    r"""Yield the finite ``Isom(source,target)`` torsor exactly."""
    homset = source.Isom(target)
    empty = homset.is_empty()
    if empty is True:
        return
    if empty is not False:
        raise NotImplementedError(
            "the definite complement isometry homset was not decided exactly"
        )
    first = homset.an_element()
    for automorphism in target.O():
        yield homset.act(automorphism, first)


def definite_complement_extensions(lattice, left, right):
    r"""Return every ``g in O(L)`` carrying ``left`` to ``right`` when complements are definite.

    This is Dawes' definite-complement route.  An isometry of the two
    complements, together with ``left -> right``, defines an isometry
    ``C:M_left -> M_right`` on the orthogonal sums.  With the finite-index
    inclusions ``A_i:M_i -> L``, its rational ambient extension is

    ``A_right * C * A_left^{-1}``.

    Exactly the rational ambient morphisms preserving the integral lattice
    belong to ``O(L)``.  Since the complement isometry homset is a finite
    torsor in this regime, the returned tuple is exhaustive.
    """
    source = VectorPrimitiveExtension(lattice, left)
    target = VectorPrimitiveExtension(lattice, right)
    if source.vector.q() != target.vector.q():
        return ()
    if not source.complement_is_definite() or not target.complement_is_definite():
        raise ValueError(
            "definite_complement_extensions requires definite orthogonal complements"
        )
    source_complement = source.complement.inclusion().domain()
    target_complement = target.complement.inclusion().domain()
    source_line = source.line.inclusion().domain()
    target_line = target.line.inclusion().domain()
    source_rank = int(source.sum_lattice.rank())
    target_rank = int(target.sum_lattice.rank())
    if source_rank != target_rank:
        return ()

    ring = lattice.base_ring()
    rationals = ring.fraction_field()
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        MatrixSpace,
        matrix_change_ring,
    )

    source_inclusion = matrix_change_ring(source.inclusion.matrix(), rationals)
    target_inclusion = matrix_change_ring(target.inclusion.matrix(), rationals)
    source_inverse = source_inclusion.inverse()
    ambient_generators = lattice.module_generators()
    source_line_vector = source.line.inclusion().lift(source.vector)
    target_line_vector = target.line.inclusion().lift(target.vector)
    target_line_generator = target_line.module_generators().unrank(0)
    source_coefficient = source_line_vector.to_tuple()[0]
    target_coefficient = target_line_vector.to_tuple()[0]
    if source_coefficient not in (ring.one(), -ring.one()) or target_coefficient not in (ring.one(), -ring.one()):
        raise ArithmeticError("a primitive rank-one line vector must be a signed selected generator")
    line_isometry = source_line.Isom(target_line)(
        (
            target_line.scalar_multiple(
                source_coefficient * target_coefficient, target_line_generator
            ),
        )
    )
    if line_isometry(source_line_vector) != target_line_vector:
        raise ArithmeticError("the rank-one block does not carry the source vector to the target vector")
    line_matrix = matrix_change_ring(line_isometry.matrix(), rationals)
    extensions = []
    for restriction in _isometries_between_definite_lattices(
        source_complement,
        target_complement,
    ):
        restriction_matrix = matrix_change_ring(restriction.matrix(), rationals)
        block = MatrixSpace(rationals, source_rank).from_rows(
            (
                line_matrix[0, 0]
                if row == column == 0
                else restriction_matrix[row - 1, column - 1]
                if row > 0 and column > 0
                else rationals.zero()
                for column in range(source_rank)
            )
            for row in range(source_rank)
        )
        candidate = target_inclusion * block * source_inverse
        try:
            integral = MatrixSpace(ring, source_rank).from_rows(
                (ring(candidate[row, column]) for column in range(source_rank))
                for row in range(source_rank)
            )
        except (TypeError, ValueError):
            continue
        images = tuple(
            sum(
                (
                    lattice.scalar_multiple(
                        integral[row, column], ambient_generators.unrank(row)
                    )
                    for row in range(source_rank)
                    if integral[row, column]
                ),
                lattice.zero(),
            )
            for column in range(source_rank)
        )
        isometry = lattice.O()(images)
        if isometry(source.vector) != target.vector:
            raise ArithmeticError(
                "an assembled definite-complement extension does not carry the source vector to the target vector"
            )
        extensions.append(isometry)
    return tuple(extensions)


def _line_isometry(source, target):
    source_line = source.line.inclusion().domain()
    target_line = target.line.inclusion().domain()
    source_vector = source.line.inclusion().lift(source.vector)
    target_vector = target.line.inclusion().lift(target.vector)
    source_coefficient = source_vector.to_tuple()[0]
    target_coefficient = target_vector.to_tuple()[0]
    target_generator = target_line.module_generators()[0]
    if source_coefficient not in (1, -1) or target_coefficient not in (1, -1):
        raise ArithmeticError("primitive rank-one line vectors must be signed selected generators")
    isometry = source_line.Isom(target_line)(
        (source_coefficient * target_coefficient * target_generator,)
    )
    if isometry(source_vector) != target_vector:
        raise ArithmeticError("the line isometry does not carry the source vector to the target vector")
    return isometry


def _finite_form_isometries(start):
    r"""Yield the complete finite-form isometry torsor generated from ``start``."""
    source = start.domain()
    target = start.codomain()
    for automorphism in target.O():
        forward = automorphism.forward() * start.forward()
        inverse = start.inverse() * automorphism.inverse_morphism()
        from dzack_research.preamble.categories.modules.framed.formed.torsion_form_modules import (
            torsion_form_isometry,
        )

        yield torsion_form_isometry(
            forward,
            inverse,
            quadratic=hasattr(source, "q") and hasattr(target, "q"),
        )


def gluing_route_discriminant_classes(lattice, left, right):
    r"""Return the finite discriminant classes compatible with ``left -> right``.

    For the primitive extensions ``M_i=Zw_i perp w_i^perp`` this enumerates
    the full finite-form isometry torsors of the line and complement factors,
    retains exactly the assembled maps ``A_{M_1}->A_{M_2}`` carrying
    ``H_1=L/M_1`` onto ``H_2=L/M_2``, and descends them to
    ``H_1^perp/H_1 -> H_2^perp/H_2 = A_L``.

    These are the admissible classes in ``O(A_L)``.  Lifting such a class to
    an actual element of ``O(L)`` is deliberately separate: it is governed by
    the image of the discriminant representation and is not assumed here.
    """
    if not lattice.is_even():
        raise ValueError("the current gluing route is implemented for even lattices and discriminant quadratic forms")
    source = VectorPrimitiveExtension(lattice, left)
    target = VectorPrimitiveExtension(lattice, right)
    if source.vector.q() != target.vector.q():
        return ()
    if source.complement_is_definite() or target.complement_is_definite():
        raise ValueError(
            "the gluing route is the indefinite-complement regime; use definite_complement_extensions otherwise"
        )

    source_complement = source.complement.inclusion().domain()
    target_complement = target.complement.inclusion().domain()
    complement_homset = source_complement.Isom(target_complement)
    complement_empty = complement_homset.is_empty()
    if complement_empty is True:
        return ()
    if complement_empty is not False:
        raise NotImplementedError(
            "the complement isometry class is undecided, so the discriminant gluing route cannot choose its torsor"
        )
    complement_start = complement_homset.an_element().discriminant_isometry()
    line_start = _line_isometry(source, target).discriminant_isometry()

    source_line_form = source.line_discriminant_inclusion.domain()
    target_line_form = target.line_discriminant_inclusion.domain()
    source_complement_form = source.complement_discriminant_inclusion.domain()
    target_complement_form = target.complement_discriminant_inclusion.domain()
    if line_start.domain() is not source_line_form or line_start.codomain() is not target_line_form:
        raise ArithmeticError("the line discriminant isometry has the wrong endpoints")
    if (
        complement_start.domain() is not source_complement_form
        or complement_start.codomain() is not target_complement_form
    ):
        raise ArithmeticError("the complement discriminant isometry has the wrong endpoints")

    from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
        form_embedding,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    source_sum_labels = tuple(source.sum_form.module_generating_set())
    target_glue = {
        target.sum_form(element)
        for element in target.gluing_images
    }
    discriminant = lattice.discriminant_group()
    classes = {}
    for line_isometry in _finite_form_isometries(line_start):
        line_images = tuple(
            target.line_discriminant_inclusion(line_isometry(generator))
            for generator in source_line_form.module_generators()
        )
        for complement_isometry in _finite_form_isometries(complement_start):
            complement_images = tuple(
                target.complement_discriminant_inclusion(
                    complement_isometry(generator)
                )
                for generator in source_complement_form.module_generators()
            )
            images = {
                label: image
                for label, image in zip(
                    source_sum_labels,
                    line_images + complement_images,
                    strict=True,
                )
            }
            assembled = form_embedding(
                source.sum_form,
                target.sum_form,
                images,
                quadratic=True,
            )
            assembled_glue = {
                target.sum_form(assembled(glued))
                for glued in source.gluing_images
            }
            if assembled_glue != target_glue:
                continue
            descended_images = {
                label: target.class_of_representative(
                    assembled(
                        source.representative_of(
                            discriminant.module_generator(label)
                        )
                    )
                )
                for label in discriminant.module_generating_set()
            }
            descended = module_homset(discriminant, discriminant)(descended_images)
            automorphism = discriminant.O().from_morphism(descended)
            classes[automorphism] = automorphism
    return tuple(classes.values())


def stable_complement_root_reflections(lattice, element):
    r"""Return root reflections of ``element^perp`` that lie in ``ker(rho_L)``.

    For an indefinite complement, one representative of each ``O(element^perp)``
    orbit of roots of square ``+2`` and ``-2`` is obtained through the exact
    vector-orbit backend.  Each representative is embedded back into ``L`` and
    reflected there; only reflections acting trivially on ``A_L`` are retained.
    The result is a finite family inside the stable stabilizer of ``element``,
    not a claim to generate that stabilizer.
    """
    extension = VectorPrimitiveExtension(lattice, element)
    if extension.complement_is_definite():
        raise ValueError(
            "stable_complement_root_reflections is the indefinite-complement orbit-representative construction"
        )
    complement = extension.complement.inclusion().domain()
    inclusion = extension.complement.inclusion()
    stable = lattice.stable_orthogonal_group()
    reflections = []
    for square in (lattice.base_ring()(2), lattice.base_ring()(-2)):
        for root in complement.O().vector_orbit_representatives(square):
            embedded_root = inclusion(root)
            reflection = lattice.reflection(embedded_root)
            if reflection(extension.vector) != extension.vector:
                raise ArithmeticError(
                    "a reflection in a root of the orthogonal complement does not fix the vector"
                )
            if reflection in stable:
                reflections.append(reflection)
    return tuple(reflections)


__all__ = [
    "VectorPrimitiveExtension",
    "definite_complement_extensions",
    "gluing_route_discriminant_classes",
    "stable_complement_root_reflections",
]
