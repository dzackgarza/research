r"""A functor lands in the category it declares.

The free/forgetful functors spent their whole life implementing
``_apply_object``, which Sage never calls -- the hook is ``_apply_functor``.
Applying one returned its own argument unchanged, and nothing noticed,
because no test ever asked the defining question: is $F(X)$ an object of
$F$'s codomain?

That question is what makes these functors rather than callables. It is
asked here of every functor the preamble declares.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphismGroup
    from dzack_research.preamble.lexicon import OrderedSet

# Sage's namespace first, and the preamble's over it: these tests name
# ``AbelianGroup``, ``FreeGroup``, ``RR`` and their fellows, which the
# preamble does not export and a lowered module is not given.
from sage.all import *  # noqa: F401,F403

from dzack_research.preamble.install import install_preamble
install_preamble(globals())


def _sample_set() -> "OrderedSet":
    labels: "OrderedSet" = finite_ordered_set([1, 2, 3])
    return labels


def _sample_group() -> "ModuleAutomorphismGroup":
    return Involutions.I_dP.cyclic_subgroup()


def test_free_module_functor_lands_in_modules() -> None:
    r"""$F_R(S)$ is an $R$-module, and not $S$."""
    functor = FreeModuleFunctorClass(ZZ)
    source = _sample_set()
    image = functor(source)
    assert image is not source, (
        "the functor returned its argument: the Sage hook is _apply_functor"
    )
    assert image in functor.codomain(), (
        f"{image} is not an object of {functor.codomain()}"
    )
    assert image.rank() == source.cardinality(), (
        "the free module on a set has one generator per element"
    )


def test_underlying_set_of_group_functor_lands_in_sets() -> None:
    r"""$U(G)$ is a set, and not $G$."""
    functor = UnderlyingSetOfGroupFunctor()
    source = _sample_group()
    image = functor(source)
    assert image is not source
    assert image in functor.codomain(), (
        f"{image} is not an object of {functor.codomain()}"
    )
    assert image.cardinality() == source.cardinality(), (
        "forgetting the group law does not change the elements"
    )


def test_group_ring_module_functor_lands_in_modules() -> None:
    r"""The underlying module of $R[G]$ is an $R$-module of rank $|G|$."""
    functor = FreeModuleOnGroupFunctor(ZZ)
    source = _sample_group()
    image = functor(source)
    assert image is not source
    assert image in functor.codomain(), (
        f"{image} is not an object of {functor.codomain()}"
    )
    assert image.rank() == source.cardinality(), (
        "R[G] is free of rank |G| as an R-module"
    )


def test_forgetful_module_functor_lands_in_sets() -> None:
    r"""$U(M)$ is a set, and not $M$."""
    functor = ForgetfulFunctorClass(ZZ)
    source = FreeModuleFunctorClass(ZZ)(_sample_set())
    image = functor(source)
    assert image is not source
    assert image in functor.codomain(), (
        f"{image} is not an object of {functor.codomain()}"
    )


def _base_rings() -> list:
    r"""Rings the group ring must be constructible over.

    \(R[G]\) is defined for every ring \(R\): nothing in the construction
    asks \(R\) to be a domain, exact, finite, or of characteristic zero.  So
    the functor is exercised across those distinctions rather than over
    \(\mathbb Z\) alone, which satisfies all of them at once and would hide
    an assumption on any.
    """
    return [
        ("ZZ", ZZ),
        ("QQ", QQ),
        ("RR", RR),
        ("CC", CC),
        ("GF(2)", GF(2)),
        ("GF(7)", GF(7)),
        ("GF(4)", GF(4, "a")),
        ("ZZ[x]", PolynomialRing(ZZ, "x")),
        ("QQ[x,y]", PolynomialRing(QQ, ["x", "y"])),
        ("QQ[[t]]", PowerSeriesRing(QQ, "t")),
        ("Zp(5)", Zp(5)),
        ("Qp(5)", Qp(5)),
        ("ZZ/6", Integers(6)),
    ]


def _groups() -> list:
    r"""Groups the group ring must be constructible over.

    \(R[G]\) asks nothing of \(G\) but that it be a group: not finiteness,
    not commutativity.  Infinite groups are the case that matters most here,
    since \(\mathbb Z[\mathbb Z]\) is the Laurent polynomial ring
    \(\mathbb Z[t,t^{-1}]\) -- a construction that a rank-equals-order test
    would quietly forbid.  The additive group of \(\mathbb F_p\) is included
    because it is a group presented as a ring's additive structure, which is
    a different route into the same construction.
    """
    # ``(FF_5,+)`` is C5 and ``ZZ`` is the free group on one generator: an
    # additive abelian group is a ZZ-module, so those belong to the module
    # categories, and ``AdditiveAbelianGroup`` reaches them by building ZZ^n
    # and calling ``span``, which the preamble's free-module shadowing does
    # not provide.  Presenting them multiplicatively is what this functor,
    # whose source is Grp, actually takes.
    return [
        ("C2", CyclicPermutationGroup(2)),
        ("C3", CyclicPermutationGroup(3)),
        ("S3", SymmetricGroup(3)),
        ("(FF_5,+)", CyclicPermutationGroup(5)),
        ("ZZ", FreeGroup(1)),
        ("F(2)", FreeGroup(2)),
    ]


def _sample_elements(group: "ModuleAutomorphismGroup", bound: int = 6r) -> list:
    r"""Return finitely many elements, exhaustively when the group is finite."""
    if group in Sets().Finite():
        return list(group)
    # An infinite group is not enumerable -- Sage's free groups fall back to
    # ``list`` and fail -- so the sample is built from the generators, whose
    # products are exactly where the group law could go wrong.  An owned group
    # is asked for them in its own word: ``gens`` leaves open which structure
    # is generated, and a group generates as a group.
    group_generators = list(group.group_generators())
    words = [group.one()] + group_generators + [g**-1 for g in group_generators]
    words += [left * right for left in group_generators for right in group_generators]
    return words[:bound]


def test_group_ring_over_many_base_rings() -> None:
    r"""\(R[G]\) is a ring of rank \(|G|\) whose product is the group law."""
    failures = []
    for ring_name, base_ring in _base_rings():
        for group_name, group in _groups():
            case = f"{ring_name}[{group_name}]"
            try:
                group_ring = GroupRingFunctor(base_ring)(group)
                assert group_ring in Rings(), f"{case} is not a ring"
                # R[G] is free of rank |G| as an R-module.  For infinite G
                # that rank is a cardinal Sage will not produce by
                # enumerating a basis, so the finite case checks the number
                # and the infinite case checks that it is infinite -- rather
                # than the test quietly covering finite groups only.
                if group in Sets().Finite():
                    assert group_ring.rank() == group.cardinality(), (
                        f"{case} has rank {group_ring.rank()}, "
                        f"expected |G| = {group.cardinality()}"
                    )
                else:
                    assert group.cardinality() == Infinity, (
                        f"{case}: {group_name} was expected to be infinite"
                    )
                assert group_ring.base_ring() is base_ring, (
                    f"{case} has base ring {group_ring.base_ring()}"
                )
                # The defining property: the embedding G -> R[G]^x is a
                # group morphism, so products of basis elements follow the
                # group law rather than any coincidence of coordinates.
                sample = _sample_elements(group)
                for left in sample:
                    for right in sample:
                        assert (
                            group_ring(left) * group_ring(right)
                            == group_ring(left * right)
                        ), f"{case}: the product is not the group law"
                assert group_ring(group.one()) == group_ring.one(), (
                    f"{case}: the identity of G is not the unit of R[G]"
                )
            except Exception as error:
                failures.append(f"{case}: {type(error).__name__}: {error}")
    assert not failures, "\n".join(failures)


def test_group_ring_is_noncommutative_exactly_when_the_group_is() -> None:
    r"""For commutative nonzero \(R\), \(R[G]\) is commutative iff \(G\) is abelian."""
    for ring_name, base_ring in [("ZZ", ZZ), ("QQ", QQ), ("GF(7)", GF(7))]:
        abelian = GroupRingFunctor(base_ring)(CyclicPermutationGroup(3))
        assert abelian.is_commutative(), f"{ring_name}[C3] should be commutative"
        symmetric_group = SymmetricGroup(3)
        nonabelian = GroupRingFunctor(base_ring)(symmetric_group)
        witnesses = [
            (left, right)
            for left in symmetric_group
            for right in symmetric_group
            if left * right != right * left
        ]
        assert witnesses, "S3 is nonabelian; the search for a witness is wrong"
        left, right = witnesses[0]
        assert (
            nonabelian(left) * nonabelian(right)
            != nonabelian(right) * nonabelian(left)
        ), f"{ring_name}[S3] lost the noncommutativity of S3"


def test_free_module_functor_carries_morphisms() -> None:
    r"""$F_R$ takes $f:S\to T$ to a morphism $F_R(S)\to F_R(T)$.

    A functor acts on morphisms too, and the domain and codomain of the
    image are the images of the domain and codomain.
    """
    functor = FreeModuleFunctorClass(ZZ)
    source = _sample_set()
    identity = SetMorphism(Hom(source, source, Sets()), lambda element: element)
    image = functor._apply_functor_to_morphism(identity)
    assert image.domain() == functor(source), (
        "F(f) must start at F(dom f)"
    )
    assert image.codomain() == functor(source), (
        "F(f) must land in F(cod f)"
    )
