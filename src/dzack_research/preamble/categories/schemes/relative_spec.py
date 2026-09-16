r"""Relative spectra of represented quasi-coherent algebra descent data.

On a distinguished affine cover ``U_i = Spec(A_i)`` an algebra sheaf is given
by finitely presented ``A_i``-algebras ``B_i`` with compatible overlap
isomorphisms.  Its relative spectrum is obtained by gluing ``Spec(B_i)``.
Over ``U_i cap U_j`` the overlap has coordinate algebra
``B_i tensor_{A_i} A_ij``.  The algebra descent datum already owns that scalar
extension and its canonical semilinear map from ``B_i``, so the relative
spectrum uses it directly as the represented distinguished open instead of
constructing a second localization presentation of the same ring.  No
compatible-global-sections algebra is substituted for the nonaffine relative
spectrum.
"""

from itertools import combinations

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.schemes.schemes import (
    OpenImmersions,
    Schemes,
    _affine_morphism_from_pullback,
    _fresh_affine_spectrum,
    _affine_spec_morphism,
    _install_scheme_subobject_construction,
)


def _semilinear_scalar_extension_map(source, target, scalar_map):
    r"""Return the canonical semilinear map into one represented scalar extension."""
    from dzack_research.preamble.categories.schemes.gluing import (
        SemilinearAlgebraMorphism,
    )

    return SemilinearAlgebraMorphism(
        source,
        target,
        scalar_map,
        {
            label: target.algebra_generator(label)
            for label in source.algebra_generating_set()
        },
    )


def _relative_overlap(datum, source_index, target_index):
    r"""Return ``Spec(B_i tensor_{A_i} A_ij)`` as the open in ``Spec(B_i)``."""
    cover = datum.cover()
    source_index = cover.chart_label(source_index)
    target_index = cover.chart_label(target_index)
    key = (source_index, target_index)
    cache = getattr(datum, "_preamble_relative_overlap_cache", {})
    cached = cache.get(key)
    if cached is not None:
        return cached

    local = datum.local_algebra(source_index)
    restricted = datum.restricted_algebra(source_index, source_index, target_index)
    base_restriction = cover.structure_sheaf_restriction(source_index, target_index)
    pullback = _semilinear_scalar_extension_map(local, restricted, base_restriction)

    ambient = (local).affine_spectrum()
    overlap = _fresh_affine_spectrum(
        restricted,
        ambient.scheme_base_ring(),
        extra_categories=(OpenImmersions(ambient),),
    )
    inclusion = _affine_morphism_from_pullback(overlap, ambient, pullback)
    _install_scheme_subobject_construction(overlap, inclusion)
    overlap._preamble_distinguished_open_ambient = ambient
    source_base = cover.open(source_index).coordinate_algebra()
    ambient_element = cover.defining_element(target_index)
    source_element = source_base.localization_map()(ambient_element)
    overlap._preamble_distinguished_open_element = local.algebra_structure_morphism()(
        source_element
    )
    cache[key] = overlap
    datum._preamble_relative_overlap_cache = cache
    return overlap


def _relative_transition_morphism(datum, source_index, target_index):
    source_open = _relative_overlap(datum, source_index, target_index)
    target_open = _relative_overlap(datum, target_index, source_index)
    pullback = datum.transition(source_index, target_index).inverse()
    return Schemes(datum.scheme().scheme_base_ring()).Mor(
        source_open,
        target_open,
    )(pullback)


def _relative_transition(datum, left_index, right_index):
    schemes = Schemes(datum.scheme().scheme_base_ring())
    forward = _relative_transition_morphism(datum, left_index, right_index)
    inverse = _relative_transition_morphism(datum, right_index, left_index)
    return schemes.Core().Mor(forward.domain(), forward.codomain())(forward, inverse)


def _finite_atlas_relative_overlap(datum, source_index, target_index):
    r"""Return the pair scalar extension as the relative overlap open."""
    atlas = datum.gluing_datum()
    source_index = atlas.normalize_chart_index(source_index)
    target_index = atlas.normalize_chart_index(target_index)
    key = (source_index, target_index)
    cache = getattr(datum, "_preamble_relative_overlap_cache", {})
    cached = cache.get(key)
    if cached is not None:
        return cached

    local = datum.local_algebra(source_index)
    pair = datum.pair_algebra(source_index, target_index)
    base_restriction = atlas.overlap(
        source_index, target_index
    ).inclusion().coordinate_algebra_morphism()
    pullback = _semilinear_scalar_extension_map(local, pair, base_restriction)

    ambient = (local).affine_spectrum()
    overlap = _fresh_affine_spectrum(
        pair,
        ambient.scheme_base_ring(),
        extra_categories=(OpenImmersions(ambient),),
    )
    inclusion = _affine_morphism_from_pullback(overlap, ambient, pullback)
    _install_scheme_subobject_construction(overlap, inclusion)
    overlap._preamble_distinguished_open_ambient = ambient
    base_element = atlas.overlap(
        source_index, target_index
    ).distinguished_open_element()
    overlap._preamble_distinguished_open_element = local.algebra_structure_morphism()(
        atlas.chart(source_index).coordinate_algebra()(base_element)
    )
    cache[key] = overlap
    datum._preamble_relative_overlap_cache = cache
    return overlap


def _finite_atlas_relative_transition_morphism(datum, source_index, target_index):
    source_open = _finite_atlas_relative_overlap(datum, source_index, target_index)
    target_open = _finite_atlas_relative_overlap(datum, target_index, source_index)
    pullback = datum.transition(source_index, target_index).pullback()
    return Schemes(datum.scheme().scheme_base_ring()).Mor(
        source_open,
        target_open,
    )(pullback)


def _finite_atlas_relative_transition(datum, left_index, right_index):
    schemes = Schemes(datum.scheme().scheme_base_ring())
    forward = _finite_atlas_relative_transition_morphism(datum, left_index, right_index)
    inverse = _finite_atlas_relative_transition_morphism(datum, right_index, left_index)
    return schemes.Core().Mor(forward.domain(), forward.codomain())(forward, inverse)


def _finite_atlas_relative_spectrum(datum):
    atlas = datum.gluing_datum()
    indices = tuple(atlas.chart_indices())
    base_scheme = datum.scheme()
    base_ring = base_scheme.scheme_base_ring()
    charts = {index: (datum.local_algebra(index)).affine_spectrum() for index in indices}
    transitions = {
        (left, right): _finite_atlas_relative_transition(datum, left, right)
        for left, right in atlas.transition_index_set()
    }
    glued = Schemes(base_ring).glue_affine_atlas(charts, transitions)
    local_maps = {}
    for index in indices:
        local_to_base_chart = _affine_morphism_from_pullback(
            charts[index],
            atlas.chart(index),
            datum.local_algebra(index).algebra_structure_morphism(),
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
    return glued.scheme_category().SliceOver(base_scheme)(structure)


@cached_function(key=lambda datum: id(datum))
def _relative_spectrum(datum):
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
    charts = {index: (datum.local_algebra(index)).affine_spectrum() for index in indices}
    transitions = {
        (left, right): _relative_transition(datum, left, right)
        for left, right in combinations(indices, 2)
    }
    glued = Schemes(base_ring).glue_affine_atlas(charts, transitions)
    local_maps = {}
    for index in indices:
        local_to_base_chart = _affine_morphism_from_pullback(
            charts[index],
            cover.open(index),
            datum.local_algebra(index).algebra_structure_morphism(),
        )
        local_maps[index] = cover.open(index).inclusion() * local_to_base_chart
    structure = glued.Mor(base_scheme)(local_maps)
    if any(
        structure * glued.chart_embedding(index)
        != local_maps[index]
        for index in indices
    ):
        raise ArithmeticError("the relative-Spec structure map does not restrict to its affine chart maps")
    return glued.scheme_category().SliceOver(base_scheme)(structure)


def _relative_spectrum_morphism(morphism):
    r"""Return ``Spec(target) -> Spec(source)`` for an algebra-descent morphism."""
    source_relative = morphism.domain().relative_spectrum()
    target_relative = morphism.codomain().relative_spectrum()
    source_scheme = source_relative.arrow().domain()
    target_scheme = target_relative.arrow().domain()
    local_maps = {}
    for index in morphism.cover().atlas():
        local_spec_map = _affine_morphism_from_pullback(
            target_scheme.chart(index),
            source_scheme.chart(index),
            morphism.local_map(index),
        )
        local_maps[index] = source_scheme.chart_embedding(index) * local_spec_map
    induced = target_scheme.Mor(source_scheme)(local_maps)
    if source_relative.arrow() * induced != target_relative.arrow():
        raise ArithmeticError("relative Spec of an algebra map does not lie over the base scheme")
    return induced


__all__ = []
