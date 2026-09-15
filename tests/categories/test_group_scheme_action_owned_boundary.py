from dzack_research.preamble.all import QQ, AffineGroupSchemeActions, AffineGroupSchemes
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory


def test_affine_group_scheme_action_category_is_owned_and_retains_its_parameter() -> None:
    group = AffineGroupSchemes(QQ).roots_of_unity(2)
    actions = AffineGroupSchemeActions(group)

    assert isinstance(actions, OwnedCategory)
    assert actions.group_scheme() is group
    assert AffineGroupSchemeActions(group) is actions
    acted = actions.an_object()
    assert acted in actions
    assert acted.group_scheme() is group


def test_equivariant_identity_survives_the_owned_category_boundary() -> None:
    group = AffineGroupSchemes(QQ).roots_of_unity(2)
    acted = AffineGroupSchemeActions(group).an_object()
    identity = acted.Mor(acted).identity()

    assert identity.domain() is acted
    assert identity.codomain() is acted
    assert identity.underlying_arrow() == acted.scheme().categorical_identity_morphism()
