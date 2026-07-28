r"""Tests for preamble override-refine.

After ``refine(obj, C)``, methods come from ``C``'s ``ParentMethods`` /
``ElementMethods`` / ``MorphismMethods``, including names that already exist
on the concrete class or a Sage supercategory.  That precedence is the whole
point of override-refine (Sage's own refine puts the class first).

Morphisms use the same Cython workaround as elements: keep the native type for
construction, wrap at the API boundary in a facade whose MRO puts
``MorphismMethods`` first.
"""


def _hyperbolic_lattice():
    from sage.matrix.constructor import matrix
    from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
    from sage.rings.integer_ring import ZZ

    return IntegralLattice(matrix(ZZ, [[0, 1], [1, 0]]))


def _refined_lattice():
    from dzack_research.preamble.categories import IntegralLattices
    from dzack_research.preamble.refine import refine

    lattice = _hyperbolic_lattice()
    refine(lattice, IntegralLattices())
    return lattice


def _sentinel_morphisms():
    from sage.categories.category import Category
    from sage.categories.sets_cat import Sets

    class _SentinelMorphisms(Category):
        @classmethod
        def _repr_object_names(cls):
            return "sentinel morphisms"

        def super_categories(self):
            return [Sets()]

        class MorphismMethods:
            def is_identity(self):
                return "from_refined_category"

            def preamble_only(self):
                return "from_refined_category"

    return _SentinelMorphisms()


def test_parent_methods_come_from_refined_category():
    lattice = _refined_lattice()
    assert type(lattice).q.__qualname__ == "IntegralLattices.ParentMethods.q"
    assert type(lattice).direct_sum.__qualname__ == "IntegralLattices.ParentMethods.direct_sum"
    assert type(lattice).twist.__qualname__ == "IntegralLattices.ParentMethods.twist"
    assert type(lattice).delta.__qualname__ == "IntegralLattices.ParentMethods.delta"
    assert type(lattice).is_elliptic.__qualname__ == "IntegralLattices.ParentMethods.is_elliptic"
    assert lattice.q(lattice.gens()[0]) == 0
    assert lattice.delta() in (0, 1)
    assert not lattice.is_elliptic()


def test_element_methods_come_from_refined_category():
    lattice = _refined_lattice()
    element = lattice.gens()[0]
    assert type(element).q.__qualname__ == "IntegralLattices.ElementMethods.q"
    assert type(element).__mul__.__qualname__ == "IntegralLattices.ElementMethods.__mul__"
    assert type(element).__pow__.__qualname__ == "IntegralLattices.ElementMethods.__pow__"
    assert element.q() == 0
    assert element * element == 0
    assert element ** 2 == 0
    assert (-element) + element == lattice.zero()
    assert {element: 1}[element] == 1
    identity = lattice.Aut()({g: g for g in lattice.gens()})
    assert identity.is_identity()
    assert identity(element) == element


def test_facade_compares_to_native_without_coercion_recursion():
    """Cython Element.__richcmp__ used to ignore Python __eq__ and segfault.

    Facade-on-the-left uses ElementFacade.__richcmp__ (unwrap + richcmp).
    Native-on-the-left still hits Cython same-parent cast of the facade —
    compare via unwrap on that side, or put the facade on the left.
    """
    from dzack_research.preamble.refine import unwrap

    lattice = _refined_lattice()
    facade = lattice.gens()[0]
    native = unwrap(facade)
    assert facade == native
    assert facade == facade
    assert unwrap(facade) == native
    assert facade != lattice.zero()


def test_unequal_rank_hom_from_generator_images():
    """An embedding is an m×n matrix; Hom(list-of-images) must build it."""
    from dzack_research.preamble import catalogue, install

    install(vendor_paths=False)
    E = catalogue.Lattices.E8_2
    TdP = catalogue.Lattices.TdP
    images = []
    for i in range(8):
        coeffs = [0] * 20
        coeffs[4 + i] = 1
        coeffs[12 + i] = 1
        images.append(TdP(coeffs))
    phi = E.Hom(TdP)(images)
    assert phi.matrix().dimensions() == (8, 20)
    # Apply must work: an embedding is an m×n matrix acting on coordinates.
    assert phi(E.gens()[0]) == images[0]
    assert phi(E.gens()[3]) == images[3]


def test_cython_morphism_methods_come_from_refined_category():
    from dzack_research.preamble.refine import MorphismFacade, refine, without_element_wrap
    from sage.rings.integer_ring import ZZ

    with without_element_wrap():
        native = ZZ.Hom(ZZ)([1])
    morphism = refine(native, _sentinel_morphisms())
    assert isinstance(morphism, MorphismFacade)
    assert type(morphism).is_identity.__qualname__.endswith("MorphismMethods.is_identity")
    assert type(morphism).preamble_only.__qualname__.endswith("MorphismMethods.preamble_only")
    assert morphism.is_identity() == "from_refined_category"
    assert morphism.preamble_only() == "from_refined_category"
    assert morphism(7) == 7


def test_heap_morphism_methods_come_from_refined_category():
    from dzack_research.preamble.refine import refine
    from sage.modules.free_module import FreeModule
    from sage.rings.integer_ring import ZZ

    V = FreeModule(ZZ, 2)
    phi = V.Hom(V).an_element()
    refined = refine(phi, _sentinel_morphisms())
    assert refined is phi
    assert type(phi).is_identity.__qualname__.endswith("MorphismMethods.is_identity")
    assert phi.is_identity() == "from_refined_category"


def test_hom_refine_produces_morphisms_from_refined_category():
    from dzack_research.preamble.refine import MorphismFacade, refine
    from sage.rings.integer_ring import ZZ

    hom = ZZ.Hom(ZZ)
    refine(hom, _sentinel_morphisms())
    morphism = hom([1])
    assert isinstance(morphism, MorphismFacade)
    assert type(morphism).is_identity.__qualname__.endswith("MorphismMethods.is_identity")
    assert morphism.is_identity() == "from_refined_category"
    assert morphism.preamble_only() == "from_refined_category"


def test_install_hooks_refine_parents_and_elements():
    from dzack_research.preamble import catalogue
    from dzack_research.preamble import install

    install()
    lattice = catalogue.Lattices.U
    assert type(lattice).direct_sum.__qualname__ == "IntegralLattices.ParentMethods.direct_sum"
    element = lattice.gens()[0]
    assert type(element).__mul__.__qualname__ == "IntegralLattices.ElementMethods.__mul__"
