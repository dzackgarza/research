r"""Relative spectra of represented quasi-coherent algebra descent data.

On a distinguished affine cover ``U_i = Spec(A_i)`` an algebra sheaf is given
by finitely presented ``A_i``-algebras ``B_i`` with compatible overlap
isomorphisms.  Its relative spectrum is obtained by gluing ``Spec(B_i)``.
Over ``U_i cap U_j`` the overlap is the distinguished open of ``Spec(B_i)``
cut out by the image of the other chart denominator.  The coordinate ring of
that open is canonically ``B_i tensor_{A_i} A_ij``; this module constructs the
canonical comparison from the represented scalar extension and uses the
algebra descent transition itself.  No compatible-global-sections algebra is
substituted for the nonaffine relative spectrum.
"""

from itertools import combinations

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.algebras.algebras import (
    algebra_structure_view,
)
from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism
from dzack_research.preamble.categories.schemes.schemes import (
    Schemes,
    Spec,
    _affine_morphism_from_pullback,
    affine_spec_morphism,
)


def _relative_overlap(datum, source_index, target_index):
    cover = datum.cover()
    source_index = cover.chart_label(source_index)
    target_index = cover.chart_label(target_index)
    source_base = cover.open(source_index).coordinate_algebra()
    source_algebra = datum.local_algebra(source_index)
    source_scheme = Spec(source_algebra)
    ambient_element = cover.defining_element(target_index)
    source_element = source_base.localization_map()(ambient_element)
    lifted = source_algebra.algebra_structure_morphism()(source_element)
    return source_scheme.distinguished_open(lifted)


def _overlap_base_to_relative_overlap(datum, source_index, target_index, source_open):
    cover = datum.cover()
    source_index = cover.chart_label(source_index)
    target_index = cover.chart_label(target_index)
    ambient = cover.ambient_scheme().coordinate_algebra()
    source_base = cover.open(source_index).coordinate_algebra()
    source_algebra = datum.local_algebra(source_index)
    source_open_algebra = source_open.coordinate_algebra()
    ambient_to_source = (
        source_open_algebra.localization_map()
        * source_algebra.algebra_structure_morphism()
        * source_base.localization_map()
    )
    overlap_base = cover.overlap(source_index, target_index).coordinate_algebra()

    def image(element):
        numerator, denominator = overlap_base.localization_fraction_data(element)
        return (
            ambient_to_source(ambient(numerator))
            * ambient_to_source(ambient(denominator)).inverse_of_unit()
        )

    return ring_morphism(overlap_base, source_open_algebra, image)


def _local_algebra_to_restricted(datum, chart_index, other_index):
    cover = datum.cover()
    chart_index = cover.chart_label(chart_index)
    other_index = cover.chart_label(other_index)
    local = datum.local_algebra(chart_index)
    restricted = datum.restricted_algebra(chart_index, chart_index, other_index)
    base_restriction = cover.structure_sheaf_restriction(chart_index, other_index)
    structure = restricted.algebra_structure_morphism() * base_restriction
    view = algebra_structure_view(restricted, structure)
    morphism = local.Mor(view)(
        {
            label: view(restricted.algebra_generator(label))
            for label in local.algebra_generating_set()
        }
    )
    return ring_morphism(local, restricted, lambda element: restricted(morphism(element)))


def _restricted_to_overlap(datum, chart_index, other_index, overlap):
    cover = datum.cover()
    chart_index = cover.chart_label(chart_index)
    other_index = cover.chart_label(other_index)
    local = datum.local_algebra(chart_index)
    restricted = datum.restricted_algebra(chart_index, chart_index, other_index)
    overlap_ring = overlap.coordinate_algebra()
    overlap_base_map = _overlap_base_to_relative_overlap(
        datum, chart_index, other_index, overlap
    )
    view = algebra_structure_view(overlap_ring, overlap_base_map)
    localization_map = overlap_ring.localization_map()
    morphism = restricted.Mor(view)(
        {
            label: view(localization_map(local.algebra_generator(label)))
            for label in restricted.algebra_generating_set()
        }
    )
    return ring_morphism(
        restricted,
        overlap_ring,
        lambda element: overlap_ring(morphism(element)),
    )


def _overlap_to_restricted(datum, chart_index, other_index, overlap):
    local = datum.local_algebra(chart_index)
    restricted = datum.restricted_algebra(chart_index, chart_index, other_index)
    local_to_restricted = _local_algebra_to_restricted(datum, chart_index, other_index)
    overlap_ring = overlap.coordinate_algebra()

    def image(element):
        numerator, denominator = overlap_ring.localization_fraction_data(element)
        numerator_image = local_to_restricted(local(numerator))
        denominator_image = local_to_restricted(local(denominator))
        return numerator_image * denominator_image.inverse_of_unit()

    return ring_morphism(overlap_ring, restricted, image)


def _relative_transition_morphism(datum, source_index, target_index):
    source_open = _relative_overlap(datum, source_index, target_index)
    target_open = _relative_overlap(datum, target_index, source_index)
    target_to_restricted = _overlap_to_restricted(
        datum, target_index, source_index, target_open
    )
    transition_inverse = datum.transition(source_index, target_index).inverse()
    restricted_to_source = _restricted_to_overlap(
        datum, source_index, target_index, source_open
    )

    pullback = ring_morphism(
        target_open.coordinate_algebra(),
        source_open.coordinate_algebra(),
        lambda element: restricted_to_source(
            transition_inverse(target_to_restricted(element))
        ),
    )
    return _affine_morphism_from_pullback(source_open, target_open, pullback)


def _relative_transition(datum, left_index, right_index):
    return Isomorphism(
        _relative_transition_morphism(datum, left_index, right_index),
        _relative_transition_morphism(datum, right_index, left_index),
    )


def _finite_atlas_relative_overlap(datum, source_index, target_index):
    atlas = datum.gluing_datum()
    source_base = atlas.chart(source_index).coordinate_algebra()
    source_algebra = datum.local_algebra(source_index)
    source_scheme = Spec(source_algebra)
    overlap_element = atlas.overlap(
        source_index, target_index
    ).distinguished_open_element()
    lifted = source_algebra.algebra_structure_morphism()(source_base(overlap_element))
    return source_scheme.distinguished_open(lifted)


def _finite_atlas_base_to_relative_overlap(
    datum, source_index, target_index, relative_overlap
):
    atlas = datum.gluing_datum()
    source_base = atlas.chart(source_index).coordinate_algebra()
    source_algebra = datum.local_algebra(source_index)
    overlap_base = atlas.overlap(source_index, target_index).coordinate_algebra()
    relative_ring = relative_overlap.coordinate_algebra()
    localize = relative_ring.localization_map()
    source_to_relative = localize * source_algebra.algebra_structure_morphism()

    def image(element):
        numerator, denominator = overlap_base.localization_fraction_data(element)
        return (
            source_to_relative(source_base(numerator))
            * source_to_relative(source_base(denominator)).inverse_of_unit()
        )

    return ring_morphism(overlap_base, relative_ring, image)


def _finite_atlas_local_to_pair(datum, source_index, target_index):
    atlas = datum.gluing_datum()
    source_base = atlas.chart(source_index).coordinate_algebra()
    overlap_base = atlas.overlap(source_index, target_index).coordinate_algebra()
    local = datum.local_algebra(source_index)
    pair = datum.pair_algebra(source_index, target_index)
    base_restriction = atlas.overlap(
        source_index, target_index
    ).inclusion().coordinate_algebra_morphism()
    structure = pair.algebra_structure_morphism() * base_restriction
    view = algebra_structure_view(pair, structure)
    morphism = local.Mor(view)(
        {
            label: view(pair.algebra_generator(label))
            for label in local.algebra_generating_set()
        }
    )
    return ring_morphism(local, pair, lambda element: pair(morphism(element)))


def _finite_atlas_pair_to_overlap(
    datum, source_index, target_index, relative_overlap
):
    local = datum.local_algebra(source_index)
    pair = datum.pair_algebra(source_index, target_index)
    overlap_ring = relative_overlap.coordinate_algebra()
    base_map = _finite_atlas_base_to_relative_overlap(
        datum, source_index, target_index, relative_overlap
    )
    view = algebra_structure_view(overlap_ring, base_map)
    localization_map = overlap_ring.localization_map()
    morphism = pair.Mor(view)(
        {
            label: view(localization_map(local.algebra_generator(label)))
            for label in pair.algebra_generating_set()
        }
    )
    return ring_morphism(
        pair, overlap_ring, lambda element: overlap_ring(morphism(element))
    )


def _finite_atlas_overlap_to_pair(
    datum, source_index, target_index, relative_overlap
):
    local = datum.local_algebra(source_index)
    pair = datum.pair_algebra(source_index, target_index)
    local_to_pair = _finite_atlas_local_to_pair(datum, source_index, target_index)
    overlap_ring = relative_overlap.coordinate_algebra()

    def image(element):
        numerator, denominator = overlap_ring.localization_fraction_data(element)
        numerator_image = local_to_pair(local(numerator))
        denominator_image = local_to_pair(local(denominator))
        return numerator_image * denominator_image.inverse_of_unit()

    return ring_morphism(overlap_ring, pair, image)


def _finite_atlas_relative_transition_morphism(datum, source_index, target_index):
    source_open = _finite_atlas_relative_overlap(datum, source_index, target_index)
    target_open = _finite_atlas_relative_overlap(datum, target_index, source_index)
    target_to_pair = _finite_atlas_overlap_to_pair(
        datum, target_index, source_index, target_open
    )
    transition = datum.transition(source_index, target_index).pullback()
    pair_to_source = _finite_atlas_pair_to_overlap(
        datum, source_index, target_index, source_open
    )
    pullback = ring_morphism(
        target_open.coordinate_algebra(),
        source_open.coordinate_algebra(),
        lambda element: pair_to_source(transition(target_to_pair(element))),
    )
    return _affine_morphism_from_pullback(source_open, target_open, pullback)


def _finite_atlas_relative_transition(datum, left_index, right_index):
    return Isomorphism(
        _finite_atlas_relative_transition_morphism(datum, left_index, right_index),
        _finite_atlas_relative_transition_morphism(datum, right_index, left_index),
    )


def _finite_atlas_relative_spectrum(datum):
    atlas = datum.gluing_datum()
    indices = tuple(atlas.chart_indices())
    base_scheme = datum.scheme()
    base_ring = base_scheme.scheme_base_ring()
    charts = {index: Spec(datum.local_algebra(index)) for index in indices}
    transitions = {
        (left, right): _finite_atlas_relative_transition(datum, left, right)
        for left, right in atlas.transition_index_set()
    }
    glued = Schemes(base_ring).glue_affine_atlas(charts, transitions)
    local_maps = {}
    for index in indices:
        local_to_base_chart = affine_spec_morphism(
            datum.local_algebra(index).algebra_structure_morphism()
        )
        local_maps[index] = atlas.chart_embedding(index) * local_to_base_chart
    structure = glued.Mor(base_scheme)(local_maps)
    if any(
        structure * glued.chart_embedding(index) != local_maps[index]
        for index in indices
    ):
        raise ArithmeticError(
            "the finite-atlas relative-Spec structure map does not restrict to its local chart maps"
        )
    glued._preamble_relative_spec_algebra_datum = datum
    glued._preamble_relative_spec_morphism = structure
    return glued.scheme_category().SliceOver(base_scheme)(structure)


@cached_function(key=lambda datum: id(datum))
def relative_spectrum(datum):
    r"""Return ``Spec_X(A) -> X`` for represented algebra descent data ``datum``."""
    from dzack_research.preamble.categories.schemes.gluing import (
        FiniteAtlasAlgebraGluingDatum,
    )

    if isinstance(datum, FiniteAtlasAlgebraGluingDatum):
        return _finite_atlas_relative_spectrum(datum)

    cover = datum.cover()
    indices = tuple(cover.atlas())
    base_scheme = datum.scheme()
    base_ring = base_scheme.scheme_base_ring()
    charts = {index: Spec(datum.local_algebra(index)) for index in indices}
    transitions = {
        (left, right): _relative_transition(datum, left, right)
        for left, right in combinations(indices, 2)
    }
    glued = Schemes(base_ring).glue_affine_atlas(charts, transitions)
    local_maps = {}
    for index in indices:
        local_to_base_chart = affine_spec_morphism(
            datum.local_algebra(index).algebra_structure_morphism()
        )
        local_maps[index] = cover.open(index).inclusion() * local_to_base_chart
    structure = glued.Mor(base_scheme)(local_maps)
    if any(
        structure * glued.chart_embedding(index)
        != local_maps[index]
        for index in indices
    ):
        raise ArithmeticError("the relative-Spec structure map does not restrict to its affine chart maps")
    glued._preamble_relative_spec_algebra_datum = datum
    glued._preamble_relative_spec_morphism = structure
    return glued.scheme_category().SliceOver(base_scheme)(structure)


def relative_spectrum_morphism(morphism):
    r"""Return ``Spec(target) -> Spec(source)`` for an algebra-descent morphism."""
    source_relative = relative_spectrum(morphism.domain())
    target_relative = relative_spectrum(morphism.codomain())
    source_scheme = source_relative.arrow().domain()
    target_scheme = target_relative.arrow().domain()
    local_maps = {}
    for index in morphism.cover().atlas():
        local_spec_map = affine_spec_morphism(morphism.local_map(index))
        local_maps[index] = source_scheme.chart_embedding(index) * local_spec_map
    induced = target_scheme.Mor(source_scheme)(local_maps)
    if source_relative.arrow() * induced != target_relative.arrow():
        raise ArithmeticError("relative Spec of an algebra map does not lie over the base scheme")
    return induced


__all__ = ["relative_spectrum", "relative_spectrum_morphism"]
