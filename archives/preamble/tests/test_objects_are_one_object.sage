r"""Sameness, and the axioms that say what an object is.

The defects this preamble kept producing were all one defect: two objects
where the mathematics has one.  Two free modules on the same $(R,S)$, two
rings printing as the integers, two ordered sets on the same enumeration --
each pair prints alike, so the failure surfaced far away as a coercion that
could find no common parent.

$F_R(S)=F_R(S')$ exactly when $S=S'$, and these say so.  They also pin the
axioms an object carries, because a category one enters without carrying its
data is how the duplicates got in.
"""


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dzack_research.preamble.categories.rings.rings import OwnedRing


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from dzack_research.preamble.install import install_preamble

    install_preamble(globals())
    Lattices.install(globals())


def _owned_integers() -> "OwnedRing":
    _ensure_preamble()
    from dzack_research.preamble.categories.rings.rings import ℤ

    return ℤ


def test_compiler_runtime_names_do_not_enter_the_installed_namespace() -> None:
    r"""Compiler support names cannot replace a constructor owned here."""
    from dzack_research.preamble.install import install_preamble

    install_preamble(globals())
    from dzack_research.preamble.categories.sets.sets import ConditionSet as OwnedConditionSet
    from dzack_research.preamble.categories.sets.sets import ImageSet as OwnedImageSet
    from dzack_research.preamble.categories.sets.sets import Set as OwnedSet

    assert Set is OwnedSet
    assert ConditionSet is OwnedConditionSet
    assert ImageSet is OwnedImageSet


def test_a_free_module_is_one_object_per_ring_and_set() -> None:
    r"""$F_R(S)$ is the same object however it is reached.

    Two spellings and one object: the class and the constructor.  Reaching a
    class directly used to give a second parent on the same $(R,S)$, and its
    elements would not coerce against the first's.

    There were three.  ``FreeModuleOnSet`` was the general class beside the
    specialized one, and the free functor is now one per concrete category,
    so there is no second class left to reach and no third spelling to agree
    with.
    """
    _ensure_preamble()
    integers = _owned_integers()
    labels = Sets.Δ[2]

    from_class = BasedFreeModule(integers, labels)
    from_constructor = FreeModuleOn(integers, labels)

    assert from_class is from_constructor


def test_the_owned_ring_and_the_engines_key_one_free_module() -> None:
    r"""A ring and the owned view of it are one ring, so they name one module.

    Both print as the integers.  Built over the two spellings they were two
    parents, and an element of one refused to coerce into the other.
    """
    _ensure_preamble()
    from sage.rings.integer_ring import ZZ as engine_integers

    labels = Sets.Δ[2]

    assert BasedFreeModule(_owned_integers(), labels) is BasedFreeModule(
        engine_integers, labels
    )


def test_an_ordered_set_is_one_object_per_enumeration() -> None:
    r"""$S=S'$ is one set, which is what makes $F_R(S)=F_R(S')$ hold."""
    _ensure_preamble()

    assert finite_ordered_set([ZZ(0), ZZ(1), ZZ(2)]) is Sets.Δ[2]
    assert finite_ordered_set([ZZ(1), ZZ(2)]) is finite_ordered_set([ZZ(1), ZZ(2)])


def test_a_set_holds_the_rings_integers_however_it_was_written() -> None:
    r"""A Python ``int`` and the ring's integer are one member.

    They print alike, compare equal and hash together, so a canonical set
    answers to the same key either way -- and would otherwise hold whichever
    spelling reached it first, making membership depend on construction
    order.
    """
    _ensure_preamble()
    from sage.structure.element import Element

    # ``int(...)`` on purpose: a literal in a ``.sage`` file is preparsed to
    # the ring's integer, so writing ``[1, 2, 3]`` here would never exercise
    # the conversion this is about.
    members = list(finite_ordered_set([int(1), int(2), int(3)]))

    assert all(isinstance(member, Element) for member in members), (
        "a set's members are the ring's objects, not Python's"
    )
    assert finite_ordered_set([int(1), int(2)]) is finite_ordered_set(
        [ZZ(1), ZZ(2)]
    ), "the two spellings name one set"


def test_a_commutative_ring_is_its_own_centre_and_an_algebra_over_itself() -> None:
    r"""$R\to Z(R)$ is the identity, which is the whole content of saying so."""
    integers = _owned_integers()

    assert integers.ring_center() is integers
    structure = integers._ring_morphism_defining_algebra_structure()
    assert structure(integers(5)) == 5


def test_forgetting_structure_returns_one_named_base_ring() -> None:
    r"""Modules, algebras, and lattices built through the engine name the same ring."""
    _ensure_preamble()
    from dzack_research.preamble.categories.rings.rings import engine_ring

    engine = engine_ring(ZZ)
    module = BasedFreeModule(engine, Sets.Δ[1])
    algebra = FreeAlgebraOn(engine, Sets.Δ[0])
    lattice = BilinearForm(
        BasedFreeModule(engine, Sets.Δ[0]),
        engine,
        matrix(engine, [[1]]),
    )

    assert module.base_ring() is ZZ
    assert algebra.base_ring() is ZZ
    assert lattice.base_ring() is ZZ
    assert algebra._ring_morphism_defining_algebra_structure().domain() is ZZ
    assert module._ring_morphism_defining_module_action().domain() is ZZ


def test_a_free_algebra_places_the_scalars_as_multiples_of_the_unit() -> None:
    r"""$r\mapsto r\cdot 1$ is the structure morphism a free construction has."""
    _ensure_preamble()
    algebra = FreeAlgebraOn(QQ, Sets.Δ[1])

    structure = algebra._ring_morphism_defining_algebra_structure()
    assert structure(QQ(3)) == 3 * algebra.one()


def test_the_module_action_scales_the_element_it_is_given() -> None:
    r"""$\rho(r)(x)=rx$, on a lattice and on a torsion module alike.

    The action is read off the framing, so a presented module has one for the
    same reason a free one does: scaling generators descends through
    $R$-linear relations.
    """
    _ensure_preamble()
    for module in (Lattices.E8, Lattices.A2.discriminant_group()):
        action = module._ring_morphism_defining_module_action()
        element = list(module.module_generators())[0]

        assert action(module.base_ring()(3))(element) == 3 * element


def test_a_quadratic_form_scales_by_the_square() -> None:
    r"""$q(2x)=4q(x)$, which is why $q$ is not a morphism of modules.

    It is a morphism out of the divided square instead, and this is the fact
    that forces the distinction.
    """
    _ensure_preamble()
    element = list(Lattices.A2.discriminant_group().module_generators())[0]

    assert (2 * element).q() == 4 * element.q()


def test_the_lattice_axioms_compose_in_any_order() -> None:
    r"""A lattice is a projective module with a form, plus three axioms."""
    _ensure_preamble()
    from dzack_research.preamble.categories.modules.framed.formed.lattices import Lattices as LatticeCategory

    integers = _owned_integers()
    one_way = LatticeCategory(integers).FinitelyGenerated().Integral().Nondegenerate()
    another = LatticeCategory(integers).Nondegenerate().Integral().FinitelyGenerated()

    assert one_way is another, "the axioms are a set, not a sequence"

    carried = set(one_way.axioms())
    for axiom in ("Projective", "FinitelyGenerated", "Integral", "Nondegenerate"):
        assert axiom in carried, f"{axiom} is part of what a lattice is"


def test_integral_lattices_is_that_join_and_holds_the_specimens() -> None:
    r"""``IntegralLattices(R)`` is the axioms, not a category standing alone."""
    _ensure_preamble()

    category = IntegralLattices(ZZ)
    carried = set(category.axioms())

    for axiom in ("Projective", "FinitelyGenerated", "Integral", "Nondegenerate"):
        assert axiom in carried

    assert Lattices.E8 in category
    assert Lattices.U in category
