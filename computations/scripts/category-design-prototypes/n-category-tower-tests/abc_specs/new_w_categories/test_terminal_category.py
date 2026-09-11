# Origin: gitclones/integral_lattice/cat/tests/abc_specs/new_w_categories/test_terminal_category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""Tests for TerminalCategory (1)."""

from src.abc_specs.new_w_categories.terminal_category import TerminalCategory, TERMINAL
from src.abc_specs.new_w_categories.arrow_implementations import wCat

"""
Basic ideas that must be true:

C has unique 0/1/2-morphisms, and >=3 morphisms are implicitly defined.

0-morphisms of Hom_C <=> 1-morphisms of C (and vice versa)
1-morphisms of Hom_C <=> 2-morphisms of C (and vice versa)
2-morphisms of Hom_C <=> 3-morphisms of C (and vice versa, trivial)

0-morphisms of Hom_Hom_C <=> 2-morphisms of C (and vice versa)
1-morphisms of Hom_Hom_C <=> 3-morphisms of C (and vice versa, trivial)
2-morphisms of Hom_Hom_C <=> 4-morphisms of C (and vice versa, trivial)

0-morphisms of Hom_Hom_Hom_C <=> 3-morphisms of C (and vice versa, trivial)
1-morphisms of Hom_Hom_Hom_C <=> 4-morphisms of C (and vice versa, trivial)
2-morphisms of Hom_Hom_Hom_C <=> 5-morphisms of C (and vice versa, trivial)

0-morphisms of Hom^n_C <=> n-morphisms of C (and vice versa, trivial for n >= 3)
1-morphisms of Hom^n_C <=> (n+1)-morphisms of C (and vice versa, trivial for n >= 3)
2-morphisms of Hom^n_C <=> (n+2)-morphisms of C (and vice versa, trivial for n >= 3)

#########

0-morphisms of Hom_Hom_C <=> 1-morphisms of Hom_C (and vice versa)
1-morphisms of Hom_Hom_C <=> 2-morphisms of Hom_C (and vice versa)
2-morphisms of Hom_Hom_C <=> 3-morphisms of Hom_C (and vice versa, trivial)

0-morphisms of Hom_Hom_Hom_C <=> 2-morphisms of Hom_Hom_C (and vice versa)
1-morphisms of Hom_Hom_Hom_C <=> 3-morphisms of Hom_Hom_C (and vice versa, trivial)
2-morphisms of Hom_Hom_Hom_C <=> 4-morphisms of Hom_Hom_C (and vice versa, trivial)

0-morphisms of Hom^n_C <=> (n+1)-morphisms of Hom_C (and vice versa, trivial for n >= 3)
1-morphisms of Hom^n_C <=> (n+2)-morphisms of Hom_C (and vice versa, trivial for n >= 3)
2-morphisms of Hom^n_C <=> (n+3)-morphisms of Hom_C (and vice versa, trivial for n >= 3)


"""


# =============================================================================
# Top-level instances (created once)
# =============================================================================

T_cat = TerminalCategory()
terminal_object = T_cat.make_object()
terminal_morphism = T_cat.make_morphism()
terminal_two_morphism = T_cat.make_two_morphism()


# =============================================================================
# Test: Singleton/Caching Behavior
# =============================================================================

def test_singleton_category():
    """TerminalCategory() always returns the same instance."""
    T_cat_2 = TerminalCategory()
    assert T_cat is T_cat_2
    assert T_cat is TERMINAL


def test_singleton_arrows():
    """Arrow factories always return the same instances."""
    T_cat_2 = TerminalCategory()
    terminal_object_2 = T_cat_2.make_object()
    terminal_morphism_2 = T_cat_2.make_morphism()
    terminal_two_morphism_2 = T_cat_2.make_two_morphism()
    
    assert terminal_object is terminal_object_2
    assert terminal_morphism is terminal_morphism_2
    assert terminal_two_morphism is terminal_two_morphism_2


def test_parameterized_singletons():
    """TerminalCategory(X) returns same instance for same X, different for different X."""
    T1 = TerminalCategory("A")
    T2 = TerminalCategory("A")
    T3 = TerminalCategory("B")
    assert T1 is T2
    assert T1 is not T3 


# =============================================================================
# Test: Category Properties
# =============================================================================

def test_terminal_category_properties():
    """1 is terminal, not initial, and has a unique object."""
    assert not T_cat.is_initial()
    assert T_cat.is_terminal()
    # 1 has a terminal object (which is also initial and zero)
    assert T_cat.is_pointed()
    assert T_cat.has_terminal_object()
    assert T_cat.has_initial_object()
    assert T_cat.has_zero_object()


def test_completeness():
    """Terminal category has all limits and colimits."""
    assert T_cat.is_complete()
    assert T_cat.is_cocomplete()
    assert T_cat.is_bicomplete()


def test_cardinality():
    """1 has finite cardinality (exactly one object)."""
    assert T_cat.cardinality() == 1
    assert T_cat.cardinality().is_finite()
    assert not T_cat.cardinality().is_countably_infinite()
    assert not T_cat.cardinality().is_uncountably_infinite()


# =============================================================================
# Test: Containment
# =============================================================================

def test_arrow_containment():
    """Arrows are contained in their category."""
    assert terminal_object in T_cat
    assert terminal_morphism in T_cat
    assert terminal_two_morphism in T_cat


# =============================================================================
# Test: Hom Categories
# =============================================================================

def test_hom_category_unwrapping():
    """Hom_1 arrows unwrap to base category arrows."""
    T_cat_hom = T_cat.hom()((terminal_object, terminal_object))
    terminal_morphism_as_object = T_cat_hom.make_object()
    assert terminal_morphism_as_object.fully_unwrap() == terminal_morphism
    terminal_two_morphism_as_one_morphism = T_cat_hom.make_morphism()
    assert terminal_two_morphism_as_one_morphism.fully_unwrap() == terminal_two_morphism


def test_hom_hom_category():
    """Hom_{Hom_1} arrows unwrap correctly."""
    T_cat_hom = T_cat.hom()((terminal_object, terminal_object))
    T_cat_hom_hom = T_cat_hom.hom()((T_cat_hom.make_object(), T_cat_hom.make_object()))
    terminal_two_morphism_as_object = T_cat_hom_hom.make_object()
    assert terminal_two_morphism_as_object.fully_unwrap() == terminal_two_morphism
    terminal_two_morphism_as_one_morphism = T_cat_hom_hom.make_morphism()
    assert terminal_two_morphism_as_one_morphism.fully_unwrap() == terminal_two_morphism


def test_hom_equivalence():
    """1 is equivalent to Hom_1(*, *) (both are terminal)."""
    hom_xx = T_cat.hom()((terminal_object, terminal_object))
    assert T_cat != hom_xx
    assert T_cat.is_equivalent_to(hom_xx)


def test_hom_containment():
    """Morphisms become objects in hom-category."""
    hom_xx = T_cat.hom()((terminal_object, terminal_object))
    # Objects of base category are NOT in hom-category
    assert terminal_object not in hom_xx
    # Morphisms of base category ARE objects in hom-category
    assert terminal_morphism in hom_xx
    assert terminal_two_morphism in hom_xx


# =============================================================================
# Test: End and Aut Categories
# =============================================================================

def test_end_category():
    """End_1(*) is equivalent to 1 and same as Hom_1(*,*)."""
    hom_xx = T_cat.hom()((terminal_object, terminal_object))
    end_x = T_cat.end()(terminal_object)
    assert T_cat != end_x
    assert T_cat.is_equivalent_to(end_x)
    assert end_x is hom_xx


def test_aut_category():
    """Aut_1(*) is equivalent to 1 and same as Hom_1(*,*)."""
    hom_xx = T_cat.hom()((terminal_object, terminal_object))
    aut_x = T_cat.aut()(terminal_object)
    assert T_cat != aut_x
    assert T_cat.is_equivalent_to(aut_x)
    assert aut_x is hom_xx


# =============================================================================
# Test: Identity Morphism
# =============================================================================

def test_identity_morphism():
    """The unique morphism is the identity."""
    id_x = T_cat.identity_morphism(terminal_object)
    assert id_x == terminal_morphism


def test_identity_properties():
    """The identity morphism has expected properties."""
    id_x = T_cat.identity_morphism(terminal_object)
    assert id_x.is_endomorphism()
    assert id_x.is_automorphism()
    assert id_x.is_invertible()
    assert id_x.is_identity()
    assert id_x.compose(id_x) == id_x
    assert id_x.inverse() == id_x


# =============================================================================
# Test: Opposite Category
# =============================================================================

def test_opposite_category():
    """1 is its own opposite (only arrow is identity)."""
    T_cat_op = T_cat.op()
    assert T_cat is T_cat_op


# =============================================================================
# Test: Level Properties
# =============================================================================

def test_terminal_category_level():
    """TerminalCategory is at the ω-category level."""
    assert T_cat.level() == 0  # Base category level
    assert "Terminal Category" in T_cat.category_name()


def test_terminal_object_level():
    """TerminalObject has correct level."""
    assert terminal_object.level() == 0  # 0-arrow


def test_terminal_morphism_level():
    """TerminalMorphism has correct level."""
    assert terminal_morphism.level() == 1  # 1-arrow


def test_terminal_two_morphism_level():
    """TerminalTwoMorphism has correct level."""
    assert terminal_two_morphism.level() == 2  # 2-arrow


# =============================================================================
# Test: Category Predicates
# =============================================================================

def test_terminal_category_predicates():
    """Terminal category has correct category-level predicates."""
    # 1 is discrete (only identity morphisms)
    assert T_cat.is_discrete()
    # 1 is a groupoid (the unique morphism is invertible)
    assert T_cat.is_groupoid()
    # 1 IS abelian (has a zero object)
    assert T_cat.is_abelian()
    # 1 IS additive (has a zero object)
    assert T_cat.is_additive()
    # 1 is finitely generated and presented
    assert T_cat.is_finitely_generated()
    assert T_cat.is_finitely_presented()


# =============================================================================
# Test: Products and Coproducts
# =============================================================================

def test_terminal_category_products():
    """Products involving 1 in wCat."""
    from src.abc_specs.new_w_categories.initial_category import InitialCategory
    E_cat = InitialCategory()
    
    # Empty product in wCat is terminal
    assert wCat.product([]).is_equivalent_to(T_cat)
    
    # 1 × 1 ≃ 1
    assert wCat.product([T_cat, T_cat]).is_equivalent_to(T_cat)
    
    # 1 × ∅ ≃ ∅ (product with initial is initial)
    assert wCat.product([T_cat, E_cat]).is_equivalent_to(E_cat)
    
    # ∅ × 1 ≃ ∅ (product is symmetric)
    assert wCat.product([E_cat, T_cat]).is_equivalent_to(E_cat)


def test_terminal_category_coproducts():
    """Coproducts involving 1 in wCat."""
    from src.abc_specs.new_w_categories.initial_category import InitialCategory
    E_cat = InitialCategory()
    
    # Coproduct of single category is itself
    assert wCat.coproduct([T_cat]).is_equivalent_to(T_cat)
    
    # 1 ⊔ 1 has two objects (disjoint union of two points)
    coprod = wCat.coproduct([T_cat, T_cat])
    assert coprod.cardinality() == 2
    
    # 1 ⊔ ∅ ≃ 1 (coproduct with initial is the other category)
    assert wCat.coproduct([T_cat, E_cat]).is_equivalent_to(T_cat)
    
    # ∅ ⊔ 1 ≃ 1 (coproduct is symmetric)
    assert wCat.coproduct([E_cat, T_cat]).is_equivalent_to(T_cat)


# =============================================================================
# Test: Cells
# =============================================================================

def test_terminal_category_cells():
    """Cells returns the cell structure of 1."""
    cells = T_cat.cells()
    # Should have structure {0: {terminal_object}, 1: {terminal_morphism}, 2: {terminal_two_morphism}}
    assert 0 in cells
    assert 1 in cells
    assert 2 in cells
    assert terminal_object in cells[0]
    assert terminal_morphism in cells[1]
    assert terminal_two_morphism in cells[2]


def test_terminal_category_get_cells():
    """get_cells returns the n-cells of 1."""
    assert terminal_object in T_cat.get_cells(0)
    assert terminal_morphism in T_cat.get_cells(1)
    assert terminal_two_morphism in T_cat.get_cells(2)


# =============================================================================
# Test: Hom Functors
# =============================================================================

def test_terminal_category_covariant_hom():
    """Covariant hom functor Hom(*, -): 1 → Set maps * to {id_*}."""
    cov = T_cat.covariant_hom(terminal_object)
    # Hom(*, *) = {id_*}
    assert cov(terminal_object) == {terminal_morphism}


def test_terminal_category_contravariant_hom():
    """Contravariant hom functor Hom(-, *): 1^op → Set maps * to {id_*}."""
    contrav = T_cat.contravariant_hom(terminal_object)
    # Hom(*, *) = {id_*}
    assert contrav(terminal_object) == {terminal_morphism}


# =============================================================================
# Test: Slice and Coslice
# =============================================================================

def test_terminal_category_slice():
    """Slice subcategory of 1 over *."""
    sl = T_cat.slice_subcategory(terminal_object)
    # 1/* ≃ 1 (only arrow is id_*)
    assert T_cat.is_equivalent_to(sl)


def test_terminal_category_coslice():
    """Coslice subcategory of 1 under *."""
    cosl = T_cat.coslice_subcategory(terminal_object)
    # */1 ≃ 1 (only arrow is id_*)
    assert T_cat.is_equivalent_to(cosl)


# =============================================================================
# Test: Equality Methods
# =============================================================================

def test_terminal_category_is_equal_to():
    """TerminalCategory.is_equal_to correctly identifies itself."""
    assert T_cat.is_equal_to(T_cat)
    assert not T_cat.is_equal_to(T_cat.hom()((terminal_object, terminal_object)))


def test_terminal_object_is_equal_to():
    """TerminalObject.is_equal_to correctly identifies itself."""
    assert terminal_object.is_equal_to(terminal_object)


# =============================================================================
# Test: Registration Methods
# =============================================================================

def test_terminal_object_registration():
    """Registration methods return empty lists for TerminalObject (no proper sub/quotients)."""
    assert terminal_object.subobjects() == []
    assert terminal_object.quotients() == []
    assert terminal_object.superobjects() == []


def test_terminal_category_registration():
    """Registration methods return appropriate values for TerminalCategory."""
    assert T_cat.subcategories() == []
    assert T_cat.supercategories() == []


# =============================================================================
# Test: Conversion Methods
# =============================================================================

def test_terminal_object_to_python_set():
    """to_python_set returns the underlying data for TerminalObject."""
    result = terminal_object.to_python_set()
    # The terminal object wraps frozenset() by default
    assert result == frozenset()


def test_terminal_category_to_python_set():
    """TerminalCategory.to_python_set returns the underlying set of objects."""
    result = T_cat.to_python_set()
    # 1 has exactly one object
    assert result == {terminal_object}


# =============================================================================
# Test: Identity Endomorphism on Category
# =============================================================================

def test_terminal_category_identity_endomorphism():
    """TerminalCategory.identity_endomorphism returns the identity functor 1 → 1."""
    id_functor = T_cat.identity_endomorphism()
    # The identity functor maps each arrow to itself
    assert id_functor(terminal_object) == terminal_object
    assert id_functor(terminal_morphism) == terminal_morphism
    assert id_functor(terminal_two_morphism) == terminal_two_morphism
