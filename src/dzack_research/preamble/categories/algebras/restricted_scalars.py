r"""Restriction of scalars for algebras along a specified ring morphism.

For ``f : R -> S`` and an ``S``-algebra ``B``, restriction changes only the
chosen algebra structure map, from ``S -> B`` to ``R -> S -> B``.  The
underlying computation ring is therefore retained.  When both ``S/R`` and
``B/S`` carry the live commutative polynomial-quotient presentations, this
module also constructs an exact finite ``R``-presentation of the restricted
algebra.  That presentation is what makes the represented Hom surface and the
scalar-extension/restriction adjunction executable without replacing ``B`` by
a second authoritative ring implementation.
"""

from sage.categories.map import Map
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings as SageRings

from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    AlgebrasWithChosenFinitePresentation,
    FinitelyPresentedAlgebras,
    FramedAlgebras,
    _OwnedAlgebraParent,
    OwnedAlgebras,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    SymmetricAlgebraOn,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    ring_morphism,
    _engine_element,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.set_categories import CoproductOfFamily
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.refine import refine


class RestrictedScalarsAlgebras(OwnedCategoryOverBaseRing):
    r"""``R``-algebras obtained by restricting an algebra along ``R -> S``."""

    @classmethod
    def _repr_object_names(cls):
        return "restricted-scalars algebras"

    def super_categories(self):
        return [Algebras(self.base_ring())]

    class ParentMethods:
        def ring_map(self):
            r"""Return the selected scalar map ``R -> S``."""
            return self._preamble_ring_map

        def algebra_over_extension(self):
            r"""Return the original ``S``-algebra before scalar restriction."""
            return self._preamble_extension_algebra

        def extension_ring(self):
            return self.algebra_over_extension().base_ring()

        def restricted_scalar_generator_labels(self):
            return self._preamble_restricted_scalar_generator_labels

        def restricted_algebra_generator_labels(self):
            return self._preamble_restricted_algebra_generator_labels


def _lift_polynomial(relation, coefficient_lift, target_variables, target_ring):
    r"""Lift a polynomial exactly after lifting each coefficient."""
    variable_count = int(target_variables.cardinality())
    if variable_count == 0:
        return target_ring(coefficient_lift(relation))
    if variable_count == 1:
        variable = target_variables.unrank(0)
        return sum(
            (
                coefficient_lift(coefficient) * variable**exponent
                for exponent, coefficient in enumerate(relation.list())
            ),
            target_ring.zero(),
        )
    return sum(
        (
            coefficient_lift(coefficient)
            * target_ring.prod(
                target_variables.unrank(position) ** int(exponent)
                for position, exponent in enumerate(exponents)
            )
            for exponents, coefficient in relation.dict().items()
        ),
        target_ring.zero(),
    )


def _chosen_restriction_presentation(algebra, extension_ring, base_ring):
    r"""Construct the selected polynomial presentation of ``Res(B)`` over ``R``."""
    extension_labels = extension_ring.algebra_generating_set()
    algebra_labels = algebra.algebra_generating_set()
    tagged_labels = CoproductOfFamily(
        Sets.Δ[1],
        lambda index: extension_labels if int(index) == 0 else algebra_labels,
    )
    presentation_ring = SymmetricAlgebraOn(base_ring, tagged_labels)
    combined_labels = presentation_ring.algebra_generating_set()
    presentation_engine = _engine_ring(presentation_ring)

    scalar_variables = indexed_family(
        extension_labels,
        lambda label: _engine_element(
            presentation_ring,
            presentation_ring.algebra_generator(tagged_labels(0, label)),
        ),
        name="Restricted-scalar presentation variables",
    )
    algebra_variables = indexed_family(
        algebra_labels,
        lambda label: _engine_element(
            presentation_ring,
            presentation_ring.algebra_generator(tagged_labels(1, label)),
        ),
        name="Restricted-algebra presentation variables",
    )

    extension_presentation_engine = _engine_ring(extension_ring.presentation_ring())
    # Private finite backend serialization required by Sage's polynomial-Hom constructor.
    extension_presentation_map = extension_presentation_engine.hom(
        list(scalar_variables),
        presentation_engine,
    )
    extension_presentation_ring = extension_ring.presentation_ring()
    extension_relations = extension_ring.relations()
    algebra_relations = algebra.relations()
    relation_indices = CoproductOfFamily(
        Sets.Δ[1],
        lambda index: (
            extension_relations.index_set()
            if int(index) == 0
            else algebra_relations.index_set()
        ),
    )

    extension_engine = _engine_ring(extension_ring)

    def coefficient_lift(coefficient):
        representative = extension_engine(coefficient).lift()
        return presentation_engine(extension_presentation_map(representative))

    algebra_presentation_ring = algebra.presentation_ring()

    def relation_value(tagged):
        if int(tagged.summand_index()) == 0:
            relation = extension_relations[tagged.summand_element()]
            backend = presentation_engine(
                extension_presentation_map(
                    _engine_element(extension_presentation_ring, relation)
                )
            )
        else:
            relation = algebra_relations[tagged.summand_element()]
            backend = _lift_polynomial(
                _engine_element(algebra_presentation_ring, relation),
                coefficient_lift,
                algebra_variables,
                presentation_engine,
            )
        return presentation_ring._from_engine_element(presentation_engine(backend))

    selected_relations = indexed_family(
        relation_indices,
        relation_value,
        name="Restricted-algebra defining relations",
    )
    # Private finite backend serialization required by Sage's ideal constructor.
    presentation_ideal = presentation_engine.ideal(
        [presentation_ring._engine_element(relation) for relation in selected_relations]
    )

    structure_map = algebra.algebra_structure_morphism()

    def generator_value(label):
        tagged = combined_labels(label)
        if int(tagged.summand_index()) == 0:
            value = structure_map(
                extension_ring.algebra_generator(tagged.summand_element())
            )
        else:
            value = algebra.algebra_generator(tagged.summand_element())
        return _engine_element(algebra, value)

    def lift_to_presentation(element):
        representative = _engine_element(algebra, algebra(element)).lift()
        return _lift_polynomial(
            representative,
            coefficient_lift,
            algebra_variables,
            presentation_engine,
        )

    return (
        combined_labels,
        presentation_ring,
        selected_relations,
        presentation_ideal,
        generator_value,
        lift_to_presentation,
        extension_labels,
        algebra_labels,
    )


def restrict_algebra_scalars(algebra, ring_map):
    r"""Return ``Res_f(B)`` for ``f : R -> S`` and an ``S``-algebra ``B``.

    Scalar restriction itself is global: the returned algebra always retains
    the exact underlying computation ring of ``B`` and composes its structure
    map with ``f``.  The stronger chosen finite presentation is retained only
    when it can be constructed from chosen presentations of both ``S/R`` and
    ``B/S`` along the selected structure map of ``S``.
    """
    if not isinstance(ring_map, Map):
        raise TypeError("algebra scalar restriction is specified by a ring morphism")

    extension_ring = algebra.base_ring()
    if _engine_ring(ring_map.codomain()) is not _engine_ring(extension_ring):
        raise ValueError(
            f"restriction of scalars for {algebra} requires a map into "
            f"{extension_ring}, got codomain {ring_map.codomain()}"
        )
    base_ring = _owned_ring(ring_map.domain())

    has_selected_presentation = (
        extension_ring in AlgebrasWithChosenFinitePresentation(base_ring)
        and algebra in AlgebrasWithChosenFinitePresentation(extension_ring)
        and ring_map is extension_ring.algebra_structure_morphism()
    )
    if has_selected_presentation:
        (
            labels,
            presentation_ring,
            selected_relations,
            presentation_ideal,
            generator_values,
            lift_to_presentation,
            restricted_scalar_labels,
            restricted_algebra_labels,
        ) = _chosen_restriction_presentation(algebra, extension_ring, base_ring)
    else:
        labels = None
        generator_values = None
        restricted_scalar_labels = None
        restricted_algebra_labels = None

    restricted = _OwnedAlgebraParent(
        _engine_ring(algebra),
        base_ring,
        labels,
        ring_map,
        generator_values,
    )
    restricted._preamble_extension_algebra = algebra
    restricted._preamble_ring_map = ring_map
    restricted._preamble_restricted_scalar_generator_labels = restricted_scalar_labels
    restricted._preamble_restricted_algebra_generator_labels = restricted_algebra_labels
    source_structure = algebra.algebra_structure_morphism()
    restricted._preamble_structure_map = ring_morphism(
        base_ring,
        restricted,
        lambda scalar: restricted(source_structure(ring_map(scalar))),
    )

    placement = [
        Algebras(base_ring),
        OwnedAlgebras(base_ring),
        RestrictedScalarsAlgebras(base_ring),
    ]
    if has_selected_presentation:
        restricted._preamble_presentation_ring = presentation_ring
        restricted._preamble_presentation_relations = selected_relations
        restricted._preamble_presentation_ideal = presentation_ideal
        restricted._preamble_lift_to_presentation = lift_to_presentation
        from dzack_research.preamble.categories.algebras.free_algebras import (
            _base_change_commutative_presentation,
        )
        restricted._preamble_base_change_selected_presentation = (
            lambda target_map: _base_change_commutative_presentation(
                restricted, target_map
            )
        )
        placement.extend(
            (
                FramedAlgebras(base_ring),
                FinitelyPresentedAlgebras(base_ring),
                AlgebrasWithChosenFinitePresentation(base_ring),
            )
        )

    restricted = refine(restricted, placement)

    if has_selected_presentation:
        presentation_engine = _engine_ring(presentation_ring)
        algebra_engine = _engine_ring(algebra)
        engine_base = _engine_ring(base_ring)
        source_structure = algebra.algebra_structure_morphism()
        def engine_base_image(scalar):
            owned_scalar = base_ring._from_engine_element(engine_base(scalar))
            return _engine_element(
                algebra,
                source_structure(ring_map(owned_scalar)),
            )

        engine_base_map = SetMorphism(
            engine_base.Mor(algebra_engine),
            engine_base_image,
        )
        presentation_engine_map = presentation_engine.hom(
            [generator_values(label) for label in labels],
            algebra_engine,
            base_map=engine_base_map,
        )
        restricted._preamble_algebra_presentation_morphism = ring_morphism(
            presentation_ring,
            restricted,
            lambda element: restricted._from_engine_element(
                algebra_engine(
                    presentation_engine_map(
                        _engine_element(presentation_ring, element)
                    )
                )
            ),
        )

    return restricted


__all__ = [
    "RestrictedScalarsAlgebras",
    "restrict_algebra_scalars",
]
