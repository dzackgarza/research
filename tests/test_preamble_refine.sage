r"""Tests for preamble override-refine.

After ``refine(obj, C)``, methods come from ``C``'s ``ParentMethods`` /
``ElementMethods`` / ``MorphismMethods``, including names that already exist
on the concrete class or a Sage supercategory.  That precedence is the whole
point of override-refine (Sage's own refine puts the class first).

Morphisms use the same Cython workaround as elements: keep the native type for
construction, wrap at the API boundary in a facade whose MRO puts
``MorphismMethods`` first.
"""

import pytest


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from pathlib import Path
    import dzack_research

    p = Path(dzack_research.__file__).resolve().parent / "preamble"
    from dzack_research.preamble.install import install_preamble
    install_preamble(globals())
    load(str(p / "sterk.sage"))
    Lattices.install(globals())


def _hyperbolic_lattice() -> "Lattice":
    r"""Return $U$, built by the preamble's own constructor.

    Not a Sage lattice refined afterwards.  An owned object is *constructed*,
    and constructing it is what places it in the owned categories -- so there
    is nothing left for a caller to refine, and no Sage parent left holding
    methods that want data it never stored.
    """
    _ensure_preamble()
    from sage.matrix.constructor import matrix
    from sage.rings.integer_ring import ZZ

    return IntegralLattice(matrix(ZZ, [[0, 1], [1, 0]]))


def _sentinel_morphisms() -> Category:
    from sage.categories.category import Category
    from sage.categories.sets_cat import Sets

    class _SentinelMorphisms(Category):
        @classmethod
        def _repr_object_names(cls) -> str:
            return "sentinel morphisms"

        def super_categories(self) -> list:
            return [Sets()]

        class MorphismMethods:
            def is_identity(self) -> str:
                return "from_refined_category"

            def preamble_only(self) -> str:
                return "from_refined_category"

    return _SentinelMorphisms()


def test_refinement_refuses_a_module_without_its_action_morphism() -> None:
    from dzack_research.preamble.categories.modules.pure.modules import Modules as OwnedModules
    from dzack_research.preamble.refine import refine
    from sage.categories.modules import Modules as SageModules
    from sage.structure.parent import Parent

    class _BareModule(Parent):
        pass

    parent = _BareModule(base=ZZ, category=SageModules(ZZ))
    with pytest.raises(
        AssertionError,
        match="requires implementations of.*_ring_morphism_defining_module_action",
    ):
        refine(parent, OwnedModules(ZZ))


def test_parent_methods_come_from_refined_category() -> None:
    lattice = _hyperbolic_lattice()
    assert type(lattice).q.__qualname__ == "IntegralLattices.ParentMethods.q"
    assert type(lattice).direct_sum.__qualname__ == "IntegralLattices.ParentMethods.direct_sum"
    assert type(lattice).twist.__qualname__ == "IntegralLattices.ParentMethods.twist"
    assert type(lattice).delta.__qualname__ == "IntegralLattices.ParentMethods.delta"
    assert type(lattice).is_elliptic.__qualname__ == "IntegralLattices.ParentMethods.is_elliptic"
    assert lattice.q(lattice.module_generators()[0]) == 0
    assert lattice.delta() in (0, 1)
    assert not lattice.is_elliptic()


def test_element_methods_come_from_refined_category() -> None:
    lattice = _hyperbolic_lattice()
    element = lattice.module_generators()[0]
    assert type(element).q.__qualname__ == "IntegralLattices.ElementMethods.q"
    assert type(element).__pow__.__qualname__ == "IntegralLattices.ElementMethods.__pow__"
    # v * w is the pairing in every fibre of U, so it is sited on the form
    # modules and a lattice inherits it rather than restating it.
    assert type(element).__mul__.__qualname__ == "FormModules.ElementMethods.__mul__"
    assert type(element).b.__qualname__ == "FormModules.ElementMethods.b"
    assert element.q() == 0
    assert element * element == 0
    assert element ** 2 == 0
    assert (-element) + element == lattice.zero()
    assert {element: 1}[element] == 1
    identity = lattice.Aut()({g: g for g in lattice.module_generators()})
    assert identity.is_identity()
    assert identity(element) == element


def test_refined_element_compares_without_coercion_recursion() -> None:
    """Cython ``Element.__richcmp__`` used to ignore Python ``__eq__`` and segfault.

    The element facade that worked around it is gone: elements are genuine
    native vectors now, so comparison is the native one and needs no
    unwrapping.  It still has to terminate, and it still has to tell distinct
    elements apart rather than collapsing them.
    """
    lattice = _hyperbolic_lattice()
    element = lattice.module_generators()[0]
    assert element == element
    assert element == lattice.module_generators()[0]
    assert element != lattice.module_generators()[1]
    assert element != lattice.zero()


def test_unequal_rank_hom_from_generator_images() -> None:
    """An embedding is an m×n matrix; Hom(list-of-images) must build it."""
    _ensure_preamble()
    E = Lattices.E8_2
    TdP = Lattices.TdP
    module_generators = TdP.module_generators()
    images = [module_generators[4 + i] + module_generators[12 + i] for i in range(8)]
    phi = E.Hom(TdP)(images)
    assert phi.matrix().dimensions() == (8, 20)
    assert phi(E.module_generators()[0]) == images[0]
    assert phi(E.module_generators()[3]) == images[3]


# Parked: refining Cython morphisms.
#
# Override-refine reassigns ``__class__``, which CPython allows only on heap
# types.  Every morphism the preamble builds is one -- lattice homs are
# ``FreeModuleMorphism``, and ``test_heap_morphism_methods_come_from_refined_category``
# below covers them -- but Sage's ring morphisms are Cython extension types
# (``RingHomomorphism_im_gens``) and cannot be reassigned.  ``MorphismFacade``
# used to cover that case by wrapping instead of reassigning; it is gone, and
# with it the capability.
#
# Nothing hides the gap: ``refine`` asserts "cannot assign __class__ on
# RingHomomorphism_im_gens; override-refine requires a heap morphism type" the
# moment it is asked.  Restore the wrapper and un-comment these two as soon as
# preamble work needs to override methods on ring morphisms -- the module and
# algebra directions will reach that.
#
# def test_cython_morphism_methods_come_from_refined_category():
#     _ensure_preamble()
#     from sage.rings.integer_ring import ZZ
#
#     morphism = refine(ZZ.Hom(ZZ)([1]), _sentinel_morphisms())
#     assert type(morphism).is_identity.__qualname__.endswith("MorphismMethods.is_identity")
#     assert type(morphism).preamble_only.__qualname__.endswith("MorphismMethods.preamble_only")
#     assert morphism.is_identity() == "from_refined_category"
#     assert morphism.preamble_only() == "from_refined_category"
#     assert morphism(7) == 7


def test_heap_morphism_methods_come_from_refined_category() -> None:
    _ensure_preamble()
    from sage.modules.free_module import FreeModule
    from sage.rings.integer_ring import ZZ

    V = FreeModule(ZZ, 2)
    phi = V.Hom(V).an_element()
    refined = refine(phi, _sentinel_morphisms())
    assert refined is phi
    assert type(phi).is_identity.__qualname__.endswith("MorphismMethods.is_identity")
    assert phi.is_identity() == "from_refined_category"


# Parked with the test above: a refined homset can only hand its morphisms the
# category's methods if those morphisms are reassignable, and ``ZZ.Hom(ZZ)``
# builds Cython ones.
#
# def test_hom_refine_produces_morphisms_from_refined_category():
#     _ensure_preamble()
#     from sage.rings.integer_ring import ZZ
#
#     hom = ZZ.Hom(ZZ)
#     refine(hom, _sentinel_morphisms())
#     morphism = hom([1])
#     assert type(morphism).is_identity.__qualname__.endswith("MorphismMethods.is_identity")
#     assert morphism.is_identity() == "from_refined_category"
#     assert morphism.preamble_only() == "from_refined_category"


def test_install_hooks_refine_parents_and_elements() -> None:
    _ensure_preamble()
    lattice = Lattices.U
    assert type(lattice).direct_sum.__qualname__ == "IntegralLattices.ParentMethods.direct_sum"
    element = lattice.module_generators()[0]
    assert type(element).__mul__.__qualname__ == "FormModules.ElementMethods.__mul__"


def test_cython_parents_refuse_refinement_and_so_keep_their_underlying_set() -> None:
    r"""$U(X)$ is stable on a parent that cannot be refined.

    ``UnderlyingSet`` is a ``UniqueRepresentation`` keyed on the parent, and
    refining a parent moves that key -- which is why the answer is kept on
    the parent itself.  A Cython parent cannot hold it: it has no instance
    dictionary.  That branch is only sound because such a parent also cannot
    be refined, so nothing ever moves its key, and this pins both halves
    rather than leaving the second one asserted in a comment.

    Pins engine behaviour.  The witness has to be a Cython parent, and the
    preamble builds none -- ``PolynomialRing`` in a session delivers the free
    algebra on its variables, which is a heap type and accepts both.  So the
    engine's own constructor is named explicitly: what is under test is
    CPython's rule about extension types, on the objects that are ones.
    """
    from sage.rings.polynomial.polynomial_ring_constructor import (
        PolynomialRing as SagePolynomialRing,
    )
    from sage.rings.rational_field import QQ as SageRationals
    from sage_lattice_category_spike.objects.underlying_sets import UnderlyingSet

    cython_parent = SagePolynomialRing(SageRationals, 2, "x")

    attribute_refused = False
    try:
        cython_parent._probe_attribute = 1
    except AttributeError:
        attribute_refused = True
    assert attribute_refused, (
        "the branch that skips storing U(X) on the parent exists for parents "
        "with no instance dictionary"
    )

    refinement_refused = False
    try:
        cython_parent.__class__ = type(
            "Refined", (type(cython_parent),), {}
        )
    except TypeError:
        refinement_refused = True
    assert refinement_refused, (
        "refinement assigns __class__, and a parent that accepts it would "
        "move its UniqueRepresentation key with no way to keep U(X)"
    )

    assert UnderlyingSet(cython_parent) is UnderlyingSet(cython_parent), (
        "U is a functor, so U(X) is one object"
    )


def test_a_module_takes_zero_to_its_own_zero():
    r"""$M(0)$ is the additive identity of $M$, in any module."""
    _ensure_preamble()

    over_the_integers = ZZ^3
    assert over_the_integers(0) == over_the_integers.zero(), (
        "0 names the additive identity, and a module has one"
    )
    over_the_rationals = QQ^2
    assert over_the_rationals(0) == over_the_rationals.zero(), (
        "the convenience is the module's, not one ring's"
    )


def test_a_polynomial_ring_is_the_free_algebra_the_notebook_receives():
    r"""``PolynomialRing`` delivers a free \(R\)-algebra, and \(R[x]\) does too.

    Sage's polynomial rings stay behind the boundary as the engine the
    algorithms run in.  What a notebook receives is the free commutative
    algebra on its variables, which is what a polynomial ring *is* -- so the
    subscript is this preamble's own and means the same thing.
    """
    _ensure_preamble()

    ring = PolynomialRing(QQ, "post_init_witness")
    assert ring in FramedFreeAlgebras(QQ), (
        "a polynomial ring is delivered as the free algebra on its variables"
    )
    assert ring.number_of_algebra_generators() == 1
    # ``algebra_generators`` is the word: the free algebra on one variable is
    # generated as an algebra by that variable, and its powers are what the
    # elements are built from.
    generator, = ring.algebra_generators()
    assert generator in ring
    assert generator ** 2 in ring
    assert generator ** 2 != generator

    over_the_integers = ZZ["x"]
    assert over_the_integers in FramedFreeAlgebras(ZZ), (
        "the subscript is the owned ring's own, so it delivers the same thing"
    )
    assert len(over_the_integers.algebra_generators()) == 1, (
        "one variable named, one algebra generator"
    )
    assert (ZZ^3).number_of_module_generators() == 3, (
        "and R^n is the preamble's free module, for the notebook's ring"
    )


def test_real_roots_come_from_the_algebraic_closure():
    r"""The owned branch: real roots without a mutable $\ZZ^{n+1}$ buffer.

    Sage isolates real roots in the Bernstein basis, writing into a
    coefficient vector by index and handing it to helpers typed
    ``Vector_integer_dense``.  A module element is not a buffer, so the roots
    come from $\overline{\QQ}$ instead -- the real ones are those of zero
    imaginary part, exactly, and every other branch is unchanged.
    """
    _ensure_preamble()
    # ``AA`` in the preamble's namespace is ``AffineSpace``.
    from sage.rings.qqbar import AA as AlgebraicReals

    x = PolynomialRing(QQ, "x").algebra_generators()[0]

    both = (x**2 - 5).roots(ring=AlgebraicReals)
    assert [multiplicity for _, multiplicity in both] == [1, 1], (
        "x^2 - 5 is separable, so each real root is simple"
    )
    assert [root**2 for root, _ in both] == [5, 5], (
        "each root squares to five, which is what makes it a root"
    )
    assert both[0][0] < 0 < both[1][0], (
        "the two roots have opposite signs, and come in increasing order"
    )
    assert (x**2 - 5).roots(ring=AlgebraicReals, multiplicities=False) == [
        root for root, _ in both
    ], "without multiplicities the answer is the roots alone"
    assert ((x - 1)**2 * (x - 2)).roots(ring=AlgebraicReals) == [(1, 2), (2, 1)], (
        "a double root is reported once, with multiplicity two"
    )
    assert (x**2 + 1).roots(ring=AlgebraicReals) == [], (
        "x^2 + 1 has no real root"
    )
    assert (x**2 - 4).roots() == [(2, 1), (-2, 1)], (
        "roots in the polynomial's own ring are Sage's branch, untouched"
    )


def test_the_noncrystallographic_coxeter_groups_have_their_orders():
    r"""$|H_3|=120$ and $|H_4|=14400$.

    Both need the golden ratio, so both build a number field with a real
    embedding and isolate a real root -- the branch the owned polynomial
    rings exist for.  Their orders are the falsifiable fact: Coxeter's
    classification gives $H_3$ order 120 and $H_4$ order 14400.
    """
    _ensure_preamble()
    from sage.combinat.root_system.coxeter_group import CoxeterGroup

    assert CoxeterGroup(["H", 3]).cardinality() == 120
    assert CoxeterGroup(["H", 4]).cardinality() == 14400
