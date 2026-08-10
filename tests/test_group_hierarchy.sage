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


# --------------------------------------------------------------------------
# $\varepsilon^*$: the trivial-action functor, and the adjunction that makes
# the invariant lattice a value rather than a coincidence.
# --------------------------------------------------------------------------


def _swap_involution():
    r"""$A_1\oplus A_1$ with the involution exchanging the two summands."""
    L = IntegralLattice(matrix(ZZ, [[-2, 0], [0, -2]]))
    G = own_group(CyclicPermutationGroup(2))
    labels = tuple(L.module_generating_set())
    e, f = L.module_generators()
    swap = L.Aut()({labels[0]: f, labels[1]: e})
    identity = L.Aut().one()
    action = group_action_homset(G, L)(
        {
            element: (identity if element == G.one() else swap)
            for element in G
        }
    )
    return L, G, action


def test_trivial_action_is_a_functor_into_group_lattices():
    r"""$\varepsilon^*L$ is a $G$-lattice on which every $g$ acts as the identity."""
    L, G, _ = _swap_involution()
    trivial = trivial_action(G)(L)

    assert trivial in GroupLattices(G), (
        "restriction along the augmentation lands in G-lattices"
    )
    assert all(
        trivial.act(element, vector_) == vector_
        for element in G
        for vector_ in trivial.module_generators()
    ), "the trivial action fixes every element"
    assert trivial.forget_action() is L, (
        "forgetting the action returns the lattice it was put on"
    )
    assert trivial_action(G)(L) is trivial, (
        "a functor is well defined on objects"
    )


def test_trivial_action_carries_lattice_maps_to_equivariant_ones():
    r"""$\varepsilon^*$ acts on morphisms: the same map, now equivariant."""
    L, G, _ = _swap_involution()
    trivial = trivial_action(G)
    e, f = L.module_generators()
    labels = tuple(L.module_generating_set())
    doubling = L.Hom(L)({labels[0]: f, labels[1]: e})

    carried = trivial(doubling)
    assert carried.domain() is trivial(L) and carried.codomain() is trivial(L), (
        "the functor's morphism half runs between the functor's objects"
    )
    assert carried(trivial._over_lattice(e)) == trivial._over_lattice(f), (
        "the map is unchanged; only the category it is read in is"
    )


def test_invariants_is_right_adjoint_to_the_trivial_action():
    r"""$\operatorname{Hom}_{\mathrm{Lat}_G}(\varepsilon^*N,(L,\rho))=\operatorname{Hom}_{\mathrm{Lat}}(N,L^G)$.

    An equivariant map out of a trivially-acted lattice has invariant image,
    because $\varphi(n)=\varphi(g\cdot n)=\rho(g)\varphi(n)$.  So the homset
    on the left is the homset on the right, and that is what makes $L^G$ the
    value of the right adjoint rather than a sublattice that happens to be
    fixed.
    """
    L, G, action = _swap_involution()
    acted = L.with_action(action)
    trivial = trivial_action(G)
    e, f = L.module_generators()

    invariant_source = IntegralLattice(matrix(ZZ, [[-4]]))
    label = tuple(invariant_source.module_generating_set())[0]
    phi = trivial(invariant_source).Hom(acted)(
        {label: acted._over_forgotten(e + f)}
    )
    assert acted.is_invariant(phi(trivial._over_lattice(
        invariant_source.module_generators()[0]
    ))), "an equivariant map out of a trivial G-lattice has invariant image"

    # $e$ has the right norm, so the refusal is about equivariance alone.
    non_invariant_source = IntegralLattice(matrix(ZZ, [[-2]]))
    bad_label = tuple(non_invariant_source.module_generating_set())[0]
    refused = False
    try:
        trivial(non_invariant_source).Hom(acted)(
            {bad_label: acted._over_forgotten(e)}
        )
    except AssertionError:
        refused = True
    assert refused, (
        "the swap moves e, so no equivariant map sends a fixed generator to it"
    )


def test_a_group_generating_set_is_the_images_of_the_generating_morphism():
    r"""$S\subseteq G$: honest elements of the group, and a set of them.

    The images of $F(S)\twoheadrightarrow G$, so two generators with the same
    image are one member -- in the trivial group all of them are, and its
    generating set is $\{1\}$ while its presentation still names every letter
    the relations are written in.
    """
    free = FreeGroup(2)
    trivial = own_group(free / [free([1]), free([2])])

    generators = trivial.group_generators()
    assert all(generator in trivial for generator in generators), (
        "a generating set is made of elements of the group it generates"
    )
    assert generators.cardinality() == 0, (
        "the trivial group is generated by the empty set: <S> = <S \\ {1}> "
        "always, so the identity generates nothing"
    )
    assert trivial.presenting_free_group().group_generators().cardinality() == 2, (
        "the presentation is written in two letters, which stay distinct in "
        "F(S) however they map"
    )


def test_finite_generation_is_what_makes_the_generating_set_finite():
    r"""The axiom carries the finiteness, not the category of groups.

    ``OwnedGroups`` claims a set and an order and no more; the finitely
    generated node is where $|S|<\infty$ comes from, and it is the node that
    can enumerate $S$ to display $\langle S\rangle$.
    """
    G = own_group(CyclicPermutationGroup(5))
    assert G in OwnedFinitelyGeneratedGroups(), (
        "a finite group is finitely generated: it generates itself"
    )
    assert G.number_of_group_generators() == 1, (
        "the cyclic group of order five is generated by one element"
    )
    assert G.group_generators() in Sets().Finite().TotallyOrdered(), (
        "the finitely generated node answers with a finite ordered set"
    )
    assert "OwnedGroups.ParentMethods.group_generators" == (
        OwnedGroups.ParentMethods.group_generators.__qualname__
    ), "the generating set itself is declared on the category of groups"


def test_one_group_reached_through_four_sage_types_is_one_group():
    r"""$C_2$, $S_2$, $\ZZ/2$ and $\langle x\mid x^2\rangle$ are equal.

    Owning the category is what makes them so: each of them *is* a finitely
    presented group, none is interpreted as one, and identity is the
    presentation -- generator count and relators read by position, so the
    letter's name is not part of it.  A different group stays different.
    """
    free = FreeGroup(1)
    presented = own_group(free / [free([1, 1])])
    permutation = own_group(CyclicPermutationGroup(2))
    symmetric = own_group(SymmetricGroup(2))
    abelian = own_group(AbelianGroup([2]))

    assert len({presented, permutation, symmetric, abelian}) == 1, (
        "four spellings of Z/2 are one group"
    )
    assert permutation != own_group(CyclicPermutationGroup(3)), (
        "Z/3 is not Z/2"
    )
    for name, group in (
        ("<x | x^2>", presented),
        ("C2", permutation),
        ("S2", symmetric),
        ("Z/2", abelian),
    ):
        relators = tuple(
            relation.Tietze() for relation in group.defining_relations()
        )
        assert relators == ((1, 1),), (
            f"{name} is presented on one generator by the relation x^2, "
            f"got {relators}"
        )
