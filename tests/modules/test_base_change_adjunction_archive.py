r"""Archive reconciliation for the full scalar-extension/restriction adjunction.

The archived base-change owner retained the extension functor and its unit but
explicitly left the counit unimplemented.  The live scalar-change owner now
represents both sides on finite free modules over a finite free coefficient
extension.  These specimens record the actual counit and both triangle
identities, so the archive is reconciled as an adjunction rather than merely as
an object-level base-change operation.
"""

from dzack_research.preamble.all import (
    QQ,
    Modules,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/functors/base_change_adjunction.sage",
    "live_owner": "src/dzack_research/preamble/categories/functors/scalar_change.py",
    "owner_overrides": {
        "RestrictedScalarsModules": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "RestrictedScalarsModules.super_categories": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "RestrictedScalarsModules.ParentMethods": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "RestrictedScalarsModules.ParentMethods.ring_map": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "RestrictedScalarsModules.ParentMethods.module_over_extension": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "RestrictedScalarsModules.ParentMethods.scalar_multiple": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "RestrictedScalarsModules.ParentMethods.zero": "src/dzack_research/preamble/categories/modules/pure/modules.py",
    },
    "disposition": "reconciled-live-owner",
}


def _gaussian_extension():
    polynomials = QQ.free_module(["x"]).symmetric_algebra()
    x = next(iter(polynomials.algebra_generators()))
    scalars = (polynomials).quotient_by_relations([x**2 + 1])
    i = scalars(x)
    structure_map = scalars.algebra_structure_morphism()
    return scalars, i, structure_map


def test_base_change_counit_multiplies_the_restricted_scalar_basis_back_into_the_module() -> None:
    scalars, i, structure_map = _gaussian_extension()
    module = scalars.free_module(1)
    generator = module.module_generator(0)
    adjunction = Modules(QQ).base_change_adjunction(structure_map)

    restricted = adjunction.right_adjoint()(module)
    extended = adjunction.left_adjoint()(restricted)
    counit = adjunction.counit(module)

    assert counit.domain() is extended
    assert counit.codomain() is module
    labels = tuple(restricted.module_generating_set())
    assert len(labels) == 2
    restricted_values = tuple(
        restricted.module_generator(label).underlying_element()
        for label in labels
    )
    assert set(restricted_values) == {generator, i * generator}
    for label in extended.module_generating_set():
        assert counit(extended.module_generator(label)) == restricted.module_generator(label).underlying_element()


def test_extension_restriction_triangle_is_the_identity_on_a_free_module() -> None:
    scalars, _i, structure_map = _gaussian_extension()
    source = QQ.free_module(1)
    adjunction = Modules(QQ).base_change_adjunction(structure_map)
    extension = adjunction.left_adjoint()

    unit = adjunction.unit(source)
    extended_source = extension(source)
    extended_unit = extension(unit)
    counit = adjunction.counit(extended_source)
    triangle = counit * extended_unit

    assert triangle.domain() is extended_source
    assert triangle.codomain() is extended_source
    for label in extended_source.module_generating_set():
        generator = extended_source.module_generator(label)
        assert triangle(generator) == generator


def test_restriction_extension_triangle_is_the_identity_on_a_free_extension_module() -> None:
    scalars, _i, structure_map = _gaussian_extension()
    target = scalars.free_module(1)
    adjunction = Modules(QQ).base_change_adjunction(structure_map)
    restriction = adjunction.right_adjoint()

    restricted_target = restriction(target)
    unit = adjunction.unit(restricted_target)
    counit = adjunction.counit(target)
    restricted_counit = restriction(counit)
    triangle = restricted_counit * unit

    assert triangle.domain() is restricted_target
    assert triangle.codomain() is restricted_target
    for label in restricted_target.module_generating_set():
        generator = restricted_target.module_generator(label)
        assert triangle(generator) == generator


def test_restricted_scalar_view_retains_the_extension_module_and_scalar_map() -> None:
    scalars, i, structure_map = _gaussian_extension()
    module = scalars.free_module(1)
    generator = module.module_generator(0)
    restriction = Modules(scalars).restriction_of_scalars(structure_map)
    restricted = restriction(module)

    assert restricted.ring_map() is structure_map
    assert restricted.module_over_extension() is module
    assert restricted.zero().underlying_element() == module.zero()

    one = QQ.one()
    wrapped = restricted.wrap(generator)
    assert restricted.scalar_multiple(one, wrapped).underlying_element() == generator
    assert restricted.wrap(i * generator).underlying_element() == i * generator
