r"""Groups, including additively written finite abelian groups.

Finite presentation is a property of a group.  A chosen presentation is data
on that group.  A finite torsion $\mathbb Z$-module is already a finite
abelian group.  It does not need a second parent to state either fact.
"""

from dzack_research.preamble.install import install_preamble
install_preamble(globals())
def _abelian_groups():
    r"""Abelian groups, in the presentations the preamble meets them in."""
    return [
        ("C3 multiplicative", AbelianGroup([3])),
        ("Z/2 + Z/4", AbelianGroup([2, 4])),
        ("(Z/2)^3", AbelianGroup([2, 2, 2])),
        ("C5 permutation", CyclicPermutationGroup(5)),
    ]


def _scalars():
    r"""Scalars including negative ones and multiples of the exponent."""
    return [ZZ(n) for n in (-3, -1, 0, 1, 2, 3, 4, 6)]


def test_groups_refine_on_witnesses_only():
    r"""Each axiom is refined in exactly when the group carries its witness."""
    finite_nonabelian = SymmetricGroup(3)
    assert finite_nonabelian in OwnedFinitelyPresentedGroups(), (
        "a finite group is finitely presented: its multiplication table is a "
        "presentation"
    )
    assert finite_nonabelian not in OwnedAbelianGroups(), (
        "S3 is not abelian, and Sage decides so"
    )

    infinite_presented = FreeGroup(2)
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
    symmetric_group = SymmetricGroup(3)
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


def test_every_abelian_group_is_a_module_over_the_integers():
    r"""$\rho:\mathbb Z\to\operatorname{End}(A)$ is a ring map, and is $n$-th power."""
    assert OwnedAbelianGroups().is_subcategory(Modules(ZZ))
    for name, group in _abelian_groups():
        assert group in Modules(ZZ), f"{name} is a module over the integers"
        action = group.scalar_action()
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
                assert group.scalar_multiple(left, element) == element**left
                for right in _scalars():
                    assert (
                        action(left + right)(element)
                        == (action(left) + action(right))(element)
                    ), f"{name}: rho does not preserve addition"
                    assert (
                        action(left * right)(element)
                        == (action(left) * action(right))(element)
                    ), f"{name}: rho does not preserve multiplication"


def test_finite_torsion_modules_are_finite_abelian_groups():
    r"""$A_L$ has its group structure and presentation on the same parent."""
    for name, rank in [("A", 3), ("D", 4), ("E", 6)]:
        group = Lattices.root_lattice(name, rank).discriminant_group()
        assert group in OwnedFiniteAbelianGroups(), (
            f"A_{{{name}{rank}}} is a finite abelian group"
        )
        assert group in OwnedFinitelyPresentedGroups(), (
            f"A_{{{name}{rank}}} is finitely presented"
        )
        for element in group:
            annihilator = ZZ(element.order())
            assert annihilator * element == group.zero(), (
                f"{name}{rank}: the order of a group element annihilates it "
                "under the additive group law"
            )
            for smaller in range(1, annihilator):
                assert ZZ(smaller) * element != group.zero(), (
                    f"{name}{rank}: no smaller scalar annihilates it, so the "
                    "group element has the stated order"
                )


def test_a_module_presentation_uses_the_presentation_matrix_relations():
    r"""The underlying-group presentation retains its commutator relators."""
    from sage.misc.latex import latex

    module = Lattices.A4.discriminant_group().forget_form()
    free = module.presenting_free_group()
    first, second = free.gens()[:2]
    commutator = first * second * first**-1 * second**-1

    assert commutator in module.defining_relations()
    presentation = str(latex(module))
    assert r"\right\rangle_{\mathbb{Z}}" in presentation
    assert "[e_{1}, e_{2}]" not in presentation


# --------------------------------------------------------------------------
# $\varepsilon^*$: the trivial-action functor, and the adjunction that makes
# the invariant lattice a value rather than a coincidence.
# --------------------------------------------------------------------------


def _swap_involution():
    r"""$A_1\oplus A_1$ with the involution exchanging the two summands."""
    L = IntegralLattice(matrix(ZZ, [[-2, 0], [0, -2]]))
    G = CyclicPermutationGroup(2)
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
        "the implementation caches its object image"
    )


def test_trivial_action_carries_lattice_maps_to_equivariant_ones():
    r"""$\varepsilon^*$ acts on morphisms: the same map, now equivariant."""
    L, G, _ = _swap_involution()
    trivial = trivial_action(G)
    e, f = L.module_generators()
    labels = tuple(L.module_generating_set())
    swap = L.Hom(L)({labels[0]: f, labels[1]: e})

    carried = trivial(swap)
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
    trivial = free / [free([1]), free([2])]

    group_generators = trivial.group_generators()
    assert all(generator in trivial for generator in group_generators), (
        "a generating set is made of elements of the group it generates"
    )
    assert group_generators.cardinality() == 0, (
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
    generated category is where $|S|<\infty$ comes from.  That category can
    enumerate $S$ to display $\langle S\rangle$.
    """
    G = CyclicPermutationGroup(5)
    assert G in OwnedFinitelyGeneratedGroups(), (
        "a finite group is finitely generated: it generates itself"
    )
    assert G.number_of_group_generators() == 1, (
        "the cyclic group of order five is generated by one element"
    )
    assert G.group_generators() in Sets().Finite().TotallyOrdered(), (
        "the finitely generated category answers with a finite ordered set"
    )
    assert "OwnedGroups.ParentMethods.group_generators" == (
        OwnedGroups.ParentMethods.group_generators.__qualname__
    ), "the generating set itself is declared on the category of groups"


def test_four_realizations_of_c2_expose_their_presentations_directly():
    r"""Four realizations of $C_2$ are finitely presented groups themselves."""
    free = FreeGroup(1)
    for name, group in (
        ("<x | x^2>", free / [free([1, 1])]),
        ("C2", CyclicPermutationGroup(2)),
        ("S2", SymmetricGroup(2)),
        ("Z/2", AbelianGroup([2])),
    ):
        assert group in OwnedFinitelyPresentedGroups(), (
            f"{name} is finitely presented without conversion"
        )
        relators = tuple(
            relation.Tietze() for relation in group.defining_relations()
        )
        assert relators == ((1, 1),), (
            f"{name} is presented on one generator by the relation x^2, "
            f"got {relators}"
        )


def test_standard_finite_groups_are_finitely_presented():
    r"""$C_2$, $S_3$, $A_4$, and $GL_2(\mathbb F_3)$ carry the property."""
    for name, group in (
        ("C2", CyclicPermutationGroup(2)),
        ("S3", SymmetricGroup(3)),
        ("A4", AlternatingGroup(4)),
        ("GL2(F3)", GL(2, GF(3))),
    ):
        assert group in Groups().Finite(), f"Sage classifies {name} as finite"
        assert group in OwnedFiniteGroups(), f"{name} is finite"
        assert group in OwnedFinitelyPresentedGroups(), (
            f"{name} is finitely presented because every finite group is"
        )


def test_groups_is_the_flat_catalogue_of_standard_groups():
    r"""The group category constructs standard families on one public surface."""
    assert Groups is groups is OwnedGroups

    finite_groups = (
        (Groups.C(5), 5),
        (Groups.S(4), 24),
        (Groups.A(4), 12),
        (Groups.D(5), 10),
        (Groups.Q(), 8),
        (Groups.V4(), 4),
        (Groups.GL(2, GF(3)), 48),
        (Groups.SL(2, GF(3)), 24),
        (Groups.Sp(2, GF(3)), 24),
    )
    for group, order in finite_groups:
        assert group in Groups()
        assert group in OwnedFiniteGroups()
        assert group.order() == order

    assert Groups.Free(2) in Groups()
    assert Groups.Braid(4) in Groups()
