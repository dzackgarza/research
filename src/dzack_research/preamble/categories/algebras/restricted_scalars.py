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

from sage.categories.homset import Hom
from sage.categories.map import Map
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings as SageRings

from dzack_research.preamble.categories.rings import OwnedRings as _OwnedRings
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    FramedAlgebras,
    OwnedAlgebraView,
    OwnedAlgebras,
)
from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
    AlgebrasWithChosenFinitePresentation,
    FinitelyPresentedAlgebras,
)
from dzack_research.preamble.categories.algebras.framed_free_algebras import (
    SymmetricAlgebraOn,
)
from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
    owned_ring_view,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
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
    if len(target_variables) == 0:
        return target_ring(coefficient_lift(relation))
    if len(target_variables) == 1:
        variable = target_variables[0]
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
                variable**exponent
                for variable, exponent in zip(
                    target_variables,
                    tuple(exponents),
                    strict=True,
                )
            )
            for exponents, coefficient in relation.dict().items()
        ),
        target_ring.zero(),
    )


def _chosen_restriction_presentation(algebra, extension_ring, base_ring):
    r"""Construct the selected polynomial presentation of ``Res(B)`` over ``R``."""
    extension_labels = tuple(extension_ring.algebra_generating_set())
    algebra_labels = tuple(algebra.algebra_generating_set())
    combined_labels = finite_ordered_set(
        tuple(("scalar", label) for label in extension_labels)
        + tuple(("algebra", label) for label in algebra_labels)
    )
    presentation_ring = SymmetricAlgebraOn(base_ring, combined_labels)
    presentation_engine = engine_ring(presentation_ring)

    scalar_variables = tuple(
        presentation_engine(presentation_ring.algebra_generator(("scalar", label)))
        for label in extension_labels
    )
    algebra_variables = tuple(
        presentation_engine(presentation_ring.algebra_generator(("algebra", label)))
        for label in algebra_labels
    )

    extension_presentation_engine = engine_ring(extension_ring.presentation_ring())
    extension_presentation_map = extension_presentation_engine.hom(
        list(scalar_variables),
        presentation_engine,
    )
    extension_relations = tuple(
        presentation_engine(extension_presentation_map(relation))
        for relation in extension_ring.relations()
    )

    extension_engine = engine_ring(extension_ring)

    def coefficient_lift(coefficient):
        representative = extension_engine(coefficient).lift()
        return presentation_engine(extension_presentation_map(representative))

    algebra_relations = tuple(
        _lift_polynomial(
            relation,
            coefficient_lift,
            algebra_variables,
            presentation_engine,
        )
        for relation in algebra.relations()
    )
    selected_relations = extension_relations + algebra_relations
    presentation_ideal = presentation_engine.ideal(selected_relations)

    algebra_engine = engine_ring(algebra)
    structure_map = algebra.algebra_structure_morphism()
    generator_values = tuple(
        algebra_engine(structure_map(extension_ring.algebra_generator(label)))
        for label in extension_labels
    ) + tuple(
        algebra_engine(algebra.algebra_generator(label)) for label in algebra_labels
    )

    def lift_to_presentation(element):
        representative = algebra_engine(element).lift()
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
        generator_values,
        lift_to_presentation,
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
    if engine_ring(ring_map.codomain()) is not engine_ring(extension_ring):
        raise ValueError(
            f"restriction of scalars for {algebra} requires a map into "
            f"{extension_ring}, got codomain {ring_map.codomain()}"
        )
    base_ring = owned_ring_view(ring_map.domain())

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
        ) = _chosen_restriction_presentation(algebra, extension_ring, base_ring)
        restricted_scalar_labels = tuple(extension_ring.algebra_generating_set())
        restricted_algebra_labels = tuple(algebra.algebra_generating_set())
    else:
        labels = None
        generator_values = None
        restricted_scalar_labels = None
        restricted_algebra_labels = None

    restricted = OwnedAlgebraView(
        engine_ring(algebra),
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
    restricted._preamble_structure_map = SetMorphism(
        Hom(base_ring, restricted, _OwnedRings()),
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
        placement.extend(
            (
                FramedAlgebras(base_ring),
                FinitelyPresentedAlgebras(base_ring),
                AlgebrasWithChosenFinitePresentation(base_ring),
            )
        )

    restricted = refine(restricted, placement)

    if has_selected_presentation:
        presentation_engine = engine_ring(presentation_ring)
        algebra_engine = engine_ring(algebra)
        engine_base = engine_ring(base_ring)
        source_structure = algebra.algebra_structure_morphism()
        engine_base_map = SetMorphism(
            engine_base.Hom(algebra_engine),
            lambda scalar: algebra_engine(
                source_structure(ring_map(engine_base(scalar)))
            ),
        )
        presentation_engine_map = presentation_engine.hom(
            [algebra_engine(value) for value in generator_values],
            algebra_engine,
            base_map=engine_base_map,
        )
        restricted._preamble_algebra_presentation_morphism = SetMorphism(
            Hom(presentation_ring, restricted, _OwnedRings()),
            lambda element: restricted(
                presentation_engine_map(presentation_engine(element))
            ),
        )

    return restricted


__all__ = [
    "RestrictedScalarsAlgebras",
    "restrict_algebra_scalars",
]
