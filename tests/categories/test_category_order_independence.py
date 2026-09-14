from sage.categories.sets_cat import Sets as SageSets

from dzack_research.preamble.owned_category_bases import Category


class OrderRoot(Category):
    def super_categories(self):
        return [SageSets()]


class OrderAlpha(OrderRoot):
    pass


class OrderBeta(OrderRoot):
    pass


class OrderLeft(Category):
    def super_categories(self):
        # Discover beta before alpha on this branch.
        return [OrderBeta(), OrderAlpha()]


class OrderRight(Category):
    def super_categories(self):
        # Discover the same ancestors in the opposite order.
        return [OrderAlpha(), OrderBeta()]


class OrderDiamond(Category):
    def super_categories(self):
        return [OrderLeft(), OrderRight()]


def _relative_positions(sequence, left, right):
    return sequence.index(left), sequence.index(right)


def test_owned_sibling_comparison_keys_do_not_depend_on_first_touch() -> None:
    # Touch the siblings in the reverse lexical/source order.  Sage's native
    # category key would remember this order through its global counter.
    beta = OrderBeta()
    beta_key = beta._cmp_key
    alpha = OrderAlpha()
    alpha_key = alpha._cmp_key

    assert beta_key != alpha_key
    expected = tuple(sorted((alpha, beta), key=lambda category: category._cmp_key, reverse=True))
    assert tuple(OrderLeft()._super_categories) == expected
    assert tuple(OrderRight()._super_categories) == expected


def test_opposite_branch_discovery_has_one_parent_class_linearization() -> None:
    left = OrderLeft()
    right = OrderRight()
    diamond = OrderDiamond()

    left_classes = left.parent_class.mro()
    right_classes = right.parent_class.mro()
    alpha_parent = OrderAlpha().parent_class
    beta_parent = OrderBeta().parent_class

    assert _relative_positions(left_classes, alpha_parent, beta_parent) == _relative_positions(
        right_classes, alpha_parent, beta_parent
    )
    diamond_mro = diamond.parent_class.mro()
    assert alpha_parent in diamond_mro
    assert beta_parent in diamond_mro


def test_owned_subcategory_key_is_strictly_below_every_owned_supercategory() -> None:
    diamond = OrderDiamond()
    for category in diamond.all_super_categories(proper=False):
        for super_category in category._super_categories:
            if isinstance(super_category, Category):
                assert category._cmp_key > super_category._cmp_key
