# Origin: gitclones/integral_lattice/cat/tests/abc_specs/new_w_categories/test_initial_category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""Tests for InitialCategory (∅)."""

from src.abc_specs.new_w_categories.initial_category import InitialCategory
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

E_cat = InitialCategory()
empty_object = E_cat.make_object()
empty_morphism = E_cat.make_morphism()
empty_two_morphism = E_cat.make_two_morphism()


# =============================================================================
# Test: Singleton/Caching Behavior
# =============================================================================

def test_singleton_category():
    """InitialCategory() always returns the same instance."""
    E_cat_2 = InitialCategory()
    assert E_cat is E_cat_2


def test_singleton_arrows():
    """Arrow factories always return the same instances."""
    E_cat_2 = InitialCategory()
    empty_object_2 = E_cat_2.make_object()
    empty_morphism_2 = E_cat_2.make_morphism()
    empty_two_morphism_2 = E_cat_2.make_two_morphism()
    
    assert empty_object is empty_object_2
    assert empty_morphism is empty_morphism_2
    assert empty_two_morphism is empty_two_morphism_2


# =============================================================================
# Test: Category Properties
# =============================================================================

def test_initial_category_properties():
    """∅ is initial, not terminal, and has no objects."""
    assert E_cat.is_initial()
    assert not E_cat.is_terminal()
    # No initial/terminal object
    assert not E_cat.is_pointed()
    # No objects
    assert not E_cat.has_terminal_object()
    assert not E_cat.has_initial_object()
    assert not E_cat.has_zero_object()


def test_completeness():
    """All functors F: C -> ∅ trivially have limits and colimits."""
    assert E_cat.is_complete()
    assert E_cat.is_cocomplete()
    assert E_cat.is_bicomplete()


def test_cardinality():
    """∅ has finite cardinality."""
    assert E_cat.cardinality().is_finite()
    assert not E_cat.cardinality().is_countably_infinite()
    assert not E_cat.cardinality().is_uncountably_infinite()


# =============================================================================
# Test: Containment
# =============================================================================

def test_arrow_containment():
    """Arrows are contained in their category."""
    assert empty_object in E_cat
    assert empty_morphism in E_cat
    assert empty_two_morphism in E_cat


# =============================================================================
# Test: Hom Categories
# =============================================================================

def test_hom_category_unwrapping():
    """Hom_∅ arrows unwrap to base category arrows."""
    E_cat_hom = E_cat.hom()((E_cat.empty_object, E_cat.empty_object))
    empty_morphism_as_object = E_cat_hom.make_object()
    assert empty_morphism_as_object.fully_unwrap() == empty_morphism
    empty_two_morphism_as_one_morphism = E_cat_hom.make_morphism()
    assert empty_two_morphism_as_one_morphism.fully_unwrap() == empty_two_morphism


def test_hom_hom_category():
    """Hom_{Hom_∅} arrows unwrap correctly."""
    E_cat_hom = E_cat.hom()((E_cat.empty_object, E_cat.empty_object))
    E_cat_hom_hom = E_cat_hom.hom()((E_cat.empty_object_hom, E_cat.empty_object_hom))
    empty_two_morphism_as_object = E_cat_hom_hom.make_object()
    assert empty_two_morphism_as_object.fully_unwrap() == empty_two_morphism
    empty_two_morphism_as_one_morphism = E_cat_hom_hom.make_morphism()
    assert empty_two_morphism_as_one_morphism.fully_unwrap() == empty_two_morphism


def test_hom_equivalence():
    """∅ is equivalent to Hom_∅(x, x) but not equal."""
    hom_xx = E_cat.hom()((empty_object, empty_object))
    assert E_cat != hom_xx
    assert E_cat.is_equivalent_to(hom_xx)


def test_hom_containment():
    """Morphisms become objects in hom-category."""
    hom_xx = E_cat.hom()((empty_object, empty_object))
    # Objects of base category are NOT in hom-category
    assert empty_object not in hom_xx
    # Morphisms of base category ARE objects in hom-category
    assert empty_morphism in hom_xx
    assert empty_two_morphism in hom_xx


# =============================================================================
# Test: End and Aut Categories
# =============================================================================

def test_end_category():
    """End_∅(x) is equivalent to ∅ and same as Hom_∅(x,x)."""
    hom_xx = E_cat.hom()((empty_object, empty_object))
    end_x = E_cat.end()(empty_object)
    assert E_cat != end_x
    assert E_cat.is_equivalent_to(end_x)
    assert end_x is hom_xx


def test_aut_category():
    """Aut_∅(x) is equivalent to ∅ and same as Hom_∅(x,x)."""
    hom_xx = E_cat.hom()((empty_object, empty_object))
    aut_x = E_cat.aut()(empty_object)
    assert E_cat != aut_x
    assert E_cat.is_equivalent_to(aut_x)
    assert aut_x is hom_xx


# =============================================================================
# Test: Identity Morphism
# =============================================================================

def test_identity_morphism():
    """The unique morphism is the identity."""
    id_x = E_cat.identity_morphism(empty_object)
    assert id_x == empty_morphism


def test_identity_properties():
    """The identity morphism has expected properties."""
    id_x = E_cat.identity_morphism(empty_object)
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
    """∅ is its own opposite (no arrows to reverse)."""
    E_cat_op = E_cat.op()
    assert E_cat is E_cat_op


# =============================================================================
# Test: Level Properties
# =============================================================================

def test_initial_category_level():
    """InitialCategory is at the ω-category level."""
    assert E_cat.level() == 0  # Base category level
    assert E_cat.category_name() == "∅ (Initial Category)"


def test_empty_object_level():
    """EmptyObject has correct level."""
    assert empty_object.level() == 0  # 0-arrow


def test_empty_morphism_level():
    """EmptyMorphism has correct level."""
    assert empty_morphism.level() == 1  # 1-arrow


def test_empty_two_morphism_level():
    """EmptyTwoMorphism has correct level."""
    assert empty_two_morphism.level() == 2  # 2-arrow


# =============================================================================
# Test: Category Predicates
# =============================================================================

def test_initial_category_predicates():
    """Initial category has correct category-level predicates."""
    # ∅ is trivially discrete (no non-identity morphisms)
    assert E_cat.is_discrete()
    # ∅ is trivially a groupoid (all morphisms are invertible, vacuously)
    assert E_cat.is_groupoid()
    # ∅ is NOT abelian (has no zero object)
    assert not E_cat.is_abelian()
    # ∅ is NOT additive (has no zero object)
    assert not E_cat.is_additive()
    # ∅ is finitely generated and presented
    assert E_cat.is_finitely_generated()
    assert E_cat.is_finitely_presented()


# =============================================================================
# Test: Products and Coproducts (vacuous)
# =============================================================================

def test_initial_category_products():
    """Products involving ∅ in wCat."""
    from src.abc_specs.new_w_categories.terminal_category import TerminalCategory
    T_cat = TerminalCategory()
    
    # Empty product in wCat is the terminal category 1
    assert not wCat.product([]).is_equivalent_to(E_cat)
    assert wCat.product([]).is_equivalent_to(T_cat)
    
    # ∅ × ∅ ≃ ∅
    assert wCat.product([E_cat, E_cat]).is_equivalent_to(E_cat)
    
    # ∅ × 1 ≃ ∅ (product with initial is initial)
    assert wCat.product([E_cat, T_cat]).is_equivalent_to(E_cat)
    
    # 1 × ∅ ≃ ∅ (product is symmetric)
    assert wCat.product([T_cat, E_cat]).is_equivalent_to(E_cat)


def test_initial_category_coproducts():
    """Coproducts involving ∅ in wCat."""
    from src.abc_specs.new_w_categories.terminal_category import TerminalCategory
    T_cat = TerminalCategory()
    
    # Empty coproduct in wCat is the initial category ∅
    assert wCat.coproduct([]).is_equivalent_to(E_cat)
    
    # ∅ ⊔ ∅ ≃ ∅
    assert wCat.coproduct([E_cat, E_cat]).is_equivalent_to(E_cat)
    
    # ∅ ⊔ 1 ≃ 1 (coproduct with initial is the other category)
    assert wCat.coproduct([E_cat, T_cat]).is_equivalent_to(T_cat)
    
    # 1 ⊔ ∅ ≃ 1 (coproduct is symmetric)
    assert wCat.coproduct([T_cat, E_cat]).is_equivalent_to(T_cat)


# =============================================================================
# Test: Cells
# =============================================================================

def test_initial_category_cells():
    """Cells returns the cell structure of ∅."""
    cells = E_cat.cells()
    # Should have structure {0: {empty_object}, 1: {empty_morphism}, 2: {empty_two_morphism}}
    assert 0 in cells
    assert 1 in cells
    assert 2 in cells
    assert empty_object in cells[0]
    assert empty_morphism in cells[1]
    assert empty_two_morphism in cells[2]


def test_initial_category_get_cells():
    """get_cells returns the n-cells of ∅."""
    assert empty_object in E_cat.get_cells(0)
    assert empty_morphism in E_cat.get_cells(1)
    assert empty_two_morphism in E_cat.get_cells(2)


# =============================================================================
# Test: Hom Functors
# =============================================================================

def test_initial_category_covariant_hom():
    """Covariant hom functor Hom(x, -): ∅ → Set maps empty_object to the empty set."""
    cov = E_cat.covariant_hom(empty_object)
    # Hom(x, x) in ∅ is the set containing only the identity morphism
    assert cov(empty_object) == {empty_morphism}


def test_initial_category_contravariant_hom():
    """Contravariant hom functor Hom(-, x): ∅^op → Set maps empty_object to the empty set."""
    contrav = E_cat.contravariant_hom(empty_object)
    # Hom(x, x) in ∅ is the set containing only the identity morphism
    assert contrav(empty_object) == {empty_morphism}


# =============================================================================
# Test: Slice and Coslice
# =============================================================================

def test_initial_category_slice():
    """Slice subcategory of ∅ over empty_object."""
    sl = E_cat.slice_subcategory(empty_object)
    # ∅/x ≃ ∅ (no arrows into x from anywhere)
    assert E_cat.is_equivalent_to(sl)


def test_initial_category_coslice():
    """Coslice subcategory of ∅ under empty_object."""
    cosl = E_cat.coslice_subcategory(empty_object)
    # x/∅ ≃ ∅ (no arrows out of x to anywhere)
    assert E_cat.is_equivalent_to(cosl)


# =============================================================================
# Test: Equality Methods
# =============================================================================

def test_initial_category_is_equal_to():
    """InitialCategory.is_equal_to correctly identifies itself."""
    assert E_cat.is_equal_to(E_cat)
    assert not E_cat.is_equal_to(E_cat.hom()((empty_object, empty_object)))


def test_empty_object_is_equal_to():
    """EmptyObject.is_equal_to correctly identifies itself."""
    assert empty_object.is_equal_to(empty_object)


# =============================================================================
# Test: Registration Methods
# =============================================================================

def test_empty_object_registration():
    """Registration methods return empty lists for EmptyObject."""
    assert empty_object.subobjects() == []
    assert empty_object.quotients() == []
    assert empty_object.superobjects() == []


def test_initial_category_registration():
    """Registration methods return appropriate values for InitialCategory."""
    assert E_cat.subcategories() == []
    assert E_cat.supercategories() == []


# =============================================================================
# Test: Conversion Methods
# =============================================================================

def test_empty_object_to_python_set():
    """to_python_set returns empty set for EmptyObject."""
    assert empty_object.to_python_set() == set()


def test_initial_category_to_python_set():
    """InitialCategory.to_python_set returns the underlying set of objects."""
    result = E_cat.to_python_set()
    # ∅ has exactly one object (the empty object)
    assert result == {empty_object}


# =============================================================================
# Test: Identity Endomorphism on Category
# =============================================================================

def test_initial_category_identity_endomorphism():
    """InitialCategory.identity_endomorphism returns the identity functor ∅ → ∅."""
    id_functor = E_cat.identity_endomorphism()
    # The identity functor maps each arrow to itself
    assert id_functor(empty_object) == empty_object
    assert id_functor(empty_morphism) == empty_morphism
    assert id_functor(empty_two_morphism) == empty_two_morphism
