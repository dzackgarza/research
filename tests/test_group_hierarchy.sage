r"""Groups, and the $\mathbb Z$-module an abelian one carries.

$\mathrm{Ab}\cong\mathbb Z\text{-Mod}$ is not the statement that a group
parent already is a module.  A $\mathbb Z$-module is a pair $(S,\rho)$, and
$\rho$ is structure: what the isomorphism says is that $\rho$ exists and
nothing about it is chosen, because $\mathbb Z$ is initial in rings and
$\operatorname{End}(A)$ is a ring.

So the module is *constructed*, and what these tests ask of it is that it
keeps the group's own elements -- a presentation by invariant factors would
answer with different ones -- and that its scalar action is the power map.
"""

load("src/dzack_research/preamble/install.sage")


def _abelian_groups():
    r"""Abelian groups, in the presentations the preamble meets them in."""
    return [
        ("C3 multiplicative", own_group(AbelianGroup([3]))),
        ("Z/2 + Z/4", own_group(AbelianGroup([2, 4]))),
        ("(Z/2)^3", own_group(AbelianGroup([2, 2, 2]))),
        ("C5 permutation", own_group(CyclicPermutationGroup(5))),
    ]


def _scalars():
    r"""Scalars including negative ones and multiples of the exponent."""
    return [ZZ(n) for n in (-3, -1, 0, 1, 2, 3, 4, 6)]


def test_own_group_refines_on_witnesses_only():
    r"""Each axiom is refined in exactly when the group carries its witness."""
    finite_nonabelian = own_group(SymmetricGroup(3))
    assert finite_nonabelian in OwnedFinitelyPresentedGroups(), (
        "a finite group is finitely presented: its multiplication table is a "
        "presentation"
    )
    assert finite_nonabelian not in OwnedAbelianGroups(), (
        "S3 is not abelian, and Sage decides so"
    )

    infinite_presented = own_group(FreeGroup(2))
    assert infinite_presented in OwnedFinitelyPresentedGroups(), (
        "a free group is presented by its generators and no relators"
    )
    assert infinite_presented not in OwnedFiniteGroups(), (
        "F(2) is infinite, so finite presentation is strictly weaker than "
        "finiteness -- which is the reason the two axioms are separate"
    )
    assert infinite_presented not in OwnedAbelianGroups(), (
        "Sage declines to decide commutativity of a free group, and declining "
        "is not an answer to refine on"
    )

    for name, group in _abelian_groups():
        assert group in OwnedAbelianGroups(), f"{name} is abelian"
        assert group in OwnedFinitelyGeneratedGroups(), (
            f"{name} has a finite generating set"
        )


def test_endomorphisms_of_an_abelian_group_form_a_ring():
    r"""$\operatorname{End}(A)$ satisfies the ring axioms on real elements."""
    for name, group in _abelian_groups():
        endomorphisms = group.endomorphism_ring()
        assert endomorphisms in Rings(), f"End({name}) is not a ring"
        one, zero = endomorphisms.one(), endomorphisms.zero()
        # Three endomorphisms got as multiples of the identity, which is the
        # only supply an arbitrary abelian group is guaranteed to have.
        f, g, h = one + one, one + one + one, -one
        for element in group:
            assert one(element) == element
            assert zero(element) == group.one()
            assert (f * one)(element) == f(element), "1 is neutral"
            assert (f * zero)(element) == group.one(), "0 absorbs"
            assert (f + g)(element) == (g + f)(element), "addition commutes"
            assert (f + (g + h))(element) == ((f + g) + h)(element), (
                "addition is associative"
            )
            assert (f * (g * h))(element) == ((f * g) * h)(element), (
                "composition is associative"
            )
            assert (f * (g + h))(element) == (f * g + f * h)(element), (
                "composition distributes over pointwise addition on the left"
            )
            assert ((g + h) * f)(element) == (g * f + h * f)(element), (
                "and on the right"
            )
            assert (f + -f)(element) == group.one(), "negation inverts"


def test_endomorphisms_of_a_nonabelian_group_are_refused():
    r"""The ring exists because $A$ is abelian, so it is refused when it is not.

    Pointwise addition of endomorphisms is a homomorphism only when the
    factors of $f(x)f(y)g(x)g(y)$ commute past each other.  A nonabelian
    group has a witness that they do not.
    """
    symmetric_group = own_group(SymmetricGroup(3))
    witnesses = [
        (left, right)
        for left in symmetric_group
        for right in symmetric_group
        if left * right != right * left
    ]
    assert witnesses, "S3 is nonabelian; the search for a witness is wrong"
    try:
        AbelianGroupEndomorphismRing(symmetric_group)
    except AssertionError:
        return
    assert False, "End(S3) was built as a ring, and its addition is not one"


def test_the_integer_action_is_the_unique_ring_morphism():
    r"""$\rho:\mathbb Z\to\operatorname{End}(A)$ is a ring map, and is $n$-th power."""
    for name, group in _abelian_groups():
        action = group.integer_action()
        assert action.domain() is ZZ, f"{name}: the scalars are the integers"
        assert action.codomain() == group.endomorphism_ring(), (
            f"{name}: rho lands in End(A)"
        )
        endomorphisms = action.codomain()
        for element in group:
            assert action(ZZ.one())(element) == endomorphisms.one()(element), (
                f"{name}: rho(1) is the identity"
            )
            for left in _scalars():
                assert action(left)(element) == element**left, (
                    f"{name}: rho(n) is not the n-th power map"
                )
                for right in _scalars():
                    assert (
                        action(left + right)(element)
                        == (action(left) + action(right))(element)
                    ), f"{name}: rho does not preserve addition"
                    assert (
                        action(left * right)(element)
                        == (action(left) * action(right))(element)
                    ), f"{name}: rho does not preserve multiplication"


def test_the_module_keeps_the_group_s_own_elements():
    r"""$U(A)$ is unchanged: only $\rho$ is added."""
    for name, group in _abelian_groups():
        module = group.as_module()
        assert module.base_ring() is ZZ, f"{name} is a module over ZZ"
        assert module.underlying_module() is group, (
            f"{name}: the module's underlying object is the group itself"
        )
        assert module.zero() == group.one(), (
            f"{name}: the module's zero is the group's identity, written "
            "the group's way"
        )
        for element in group:
            assert element in module, (
                f"{name}: a group element is an element of the module"
            )
            assert module(element) == element, (
                f"{name}: constructing an element of the module returns the "
                "group element unchanged, rather than re-presenting it"
            )


def test_the_module_axioms_hold_with_the_group_law_as_addition():
    r"""$n(mx)=(nm)x$ and $(n+m)x=nx+mx$, where $+$ on $A$ is its group law."""
    for name, group in _abelian_groups():
        module = group.as_module()
        for element in group:
            assert module.act(ZZ.zero(), element) == module.zero(), (
                f"{name}: 0.x is the zero of the module"
            )
            assert module.act(ZZ.one(), element) == element, (
                f"{name}: 1.x is x"
            )
            for left in _scalars():
                for right in _scalars():
                    assert (
                        module.act(left, module.act(right, element))
                        == module.act(left * right, element)
                    ), f"{name}: the action is not associative over ZZ"
                    assert (
                        module.act(left + right, element)
                        == module.act(left, element) * module.act(right, element)
                    ), f"{name}: the action does not distribute over ZZ"


def test_a_torsion_module_and_its_group_carry_the_same_action():
    r"""The group of a torsion module is a module again, and acts the same way.

    ``abelian_group`` forgets the module structure of a torsion
    $\mathbb Z$-module; putting it back is what these categories do, and the
    action recovered is the one that was forgotten -- order for order.
    """
    for name, rank in [("A", 3), ("D", 4), ("E", 6)]:
        torsion = Lattices.root_lattice(name, rank).discriminant_group()
        group = torsion.abelian_group()
        assert group in OwnedAbelianGroups(), (
            f"the underlying group of {name}{rank}'s discriminant module is "
            "abelian"
        )
        module = group.as_module()
        assert module.base_ring() is ZZ
        for element in group:
            annihilator = ZZ(element.order())
            assert module.act(annihilator, element) == module.zero(), (
                f"{name}{rank}: the order of a group element annihilates it "
                "as a scalar"
            )
            for smaller in range(1, annihilator):
                assert module.act(ZZ(smaller), element) != module.zero(), (
                    f"{name}{rank}: no smaller scalar annihilates it, so the "
                    "recovered action has exactly the orders the group had"
                )
