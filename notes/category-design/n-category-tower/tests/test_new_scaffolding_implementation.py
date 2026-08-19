# Origin: gitclones/integral_lattice/cat/tests/test_new_scaffolding_implementation.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from src.abc_specs.new_w_categories.new_scaffolding_implementation import (
    Category, Element, Map
)
from src.local_typing import *

# Top-level setup
C = Category()
X = C.zero_arrow_from()(None)
x = Element(_underlying_data=None, _ambient_object=X)
empty_x = X.empty_element()

id_t = Map[Element, Element](_underlying_data=lambda x: x)
id_x = C.one_arrow_from()((X, X, id_t))
id_x_0 = id_x.as_zero_arrow()

Hom_C_X_X = id_x_0.ambient_category()

def test_element_structure():
    assert x.source() is None
    assert x.target() is None
    assert x.ambient_object() is X

def test_object_structure():
    assert X.source() is empty_x
    assert X.target() is empty_x
    assert X.source().ambient_object() is X
    assert X.target().ambient_object() is X
    assert X.ambient_category() is C

def test_morphism_structure():
    assert id_x.source() is X
    assert id_x.target() is X
    assert id_x.underlying_data()(x) == x

def test_hom_object_as_zero_arrow():
    # id_x_0 is a 0-arrow in Hom_C(X,X)
    assert id_x_0.source() is id_x_0.target()
    assert id_x_0.source().ambient_object() is id_x_0
    assert id_x_0.target().ambient_object() is id_x_0

def test_hom_containment():
    assert id_x in C 
    assert id_x not in Hom_C_X_X
    assert id_x_0 in Hom_C_X_X 
    assert id_x_0 not in C

def test_mathematical_consistency_hom_structure():
    # 1. Hom-object structure
    # The object in Hom(X,X) must wrap the morphism id_x in C
    assert id_x_0.underlying_data() == id_x

def test_mathematical_consistency_bijection():
    # 2. Bijection between Hom(X,X) objects and C(X,X) morphisms
    assert Hom_C_X_X.zero_arrow_to_one_arrow()(id_x_0) == id_x
    assert Hom_C_X_X.one_arrow_to_zero_arrow()(id_x) == id_x_0

def test_mathematical_consistency_map():
    # 3. Map consistency
    assert C.hom()((X, X)) is Hom_C_X_X

def test_mathematical_consistency_arrow_hierarchy():
    # 4. Arrow hierarchy consistency
    assert id_x_0.source() != X.source()
    assert id_x_0.source().ambient_object() == id_x_0
    assert id_x_0.target().ambient_object() == id_x_0
