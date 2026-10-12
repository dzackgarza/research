r"""Free groups, cyclic subgroups and the orders of catalogued groups.

The free group on $\{a, b\}$ is nonabelian, finitely presented with no
relations, and $a b b^{-1} = a$; the word $a b a^{-1}$ is reduced.  A group
morphism out of it is determined by the images of $a$ and $b$ (the
universal property of the free group).  In $C_4 = \langle g \rangle$ the
cyclic subgroups $\langle g \rangle$ and $\langle g^2 \rangle$ have orders
$4$ and $2$.  The hyperoctahedral group $W(B_2)$ of signed permutations of
two letters has order $2^2 \cdot 2! = 8$.  $|\mathrm{SL}_2(\mathbb{F}_q)| =
q(q^2 - 1)$ and $\mathrm{PSL}_2(\mathbb{F}_7) = \mathrm{SL}_2(\mathbb{F}_7) /
\{\pm 1\}$ has order $7 \cdot 48 / 2 = 168$.  The Heisenberg group of upper
unitriangular $3 \times 3$ matrices over $\mathbb{Z}/3$ has $3^3 = 27$
elements.  $\mathrm{SL}_2(\mathbb{Z})$ is infinite and arithmetic, and the
braid group on three strands is infinite (it surjects onto $\mathbb{Z}$ by
the exponent sum).  All are computations from the definitions.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_the_free_group_on_two_letters_is_nonabelian_and_freely_reduces_words() -> None:
    free = Groups.Free(2)
    a, b = free.group_generators()

    assert free.number_of_group_generators() == cardinal(2)
    assert a * b * ~b == a
    assert a * b != b * a
    assert not free.is_abelian()
    assert free.is_finitely_generated()
    assert free.is_finitely_presented_as_group()
    assert free.free_generator(0) == a
    assert free.reduced_word(a * b * a**-1).cardinality() == cardinal(3)


def test_a_morphism_out_of_the_free_group_is_given_by_the_images_of_its_letters() -> None:
    r"""$a \mapsto (1\,2)$, $b \mapsto (1\,2\,3)$ is onto $S_3$ and sends $a b$ to $(1\,2)(1\,2\,3)$."""
    free = Groups.Free(2)
    a, b = free.group_generators()
    symmetric = Groups.S(3)
    morphism = free.Mor(symmetric)({a: symmetric((1, 2)), b: symmetric((1, 2, 3))})

    assert morphism.image().order() == 6
    assert morphism(a * b) == symmetric((1, 2)) * symmetric((1, 2, 3))


def test_generator_images_must_generate_the_whole_source() -> None:
    # A single transposition generates only C2 inside S3. Its image
    # cannot specify a homomorphism on arbitrary elements of S3.
    from dzack_research.preamble.categories.group.groups import _engine_generator_epimorphism

    group = Groups.S(3)
    transposition = group((1, 2))
    try:
        _engine_generator_epimorphism(group, (transposition,))
    except ValueError as error:
        assert "do not generate the source group" in str(error)
    else:
        assert False, "an incomplete generator family defined a whole-group morphism"


def test_engine_generator_image_family_has_exact_arity() -> None:
    from dzack_research.preamble.categories.group.groups import _gap_model

    symmetric = Groups.S(3)
    cyclic = Groups.C(2)
    generators = list(symmetric.group_generators())
    assert generators
    try:
        symmetric.Mor(cyclic)([])
    except ValueError as error:
        assert "images were supplied" in str(error)
    else:
        assert False, "an empty image tuple was accepted for a nontrivial group presentation"
    try:
        symmetric.Mor(cyclic)._from_engine_generator_images(
            list(_gap_model(symmetric).GeneratorsOfGroup()), []
        )
    except ValueError as error:
        assert "selected generators" in str(error)
    else:
        assert False, "direct engine-morphism ingress accepted missing generator images"

    # The same ingress must reject maps which violate source relations,
    # even with a complete generator-image family: C4 cannot map its
    # generator to an element of order three.
    from dzack_research.preamble.categories.group.groups import _element_to_engine

    four = Groups.C(4)
    three = Groups.C(3)
    try:
        four.Mor(three)._from_engine_generator_images(
            list(_gap_model(four).GeneratorsOfGroup()),
            [_element_to_engine(three, three.group_generators()[0])],
        )
    except ValueError as error:
        assert "do not satisfy the source relations" in str(error)
    else:
        assert False, "an image of order three was accepted for a C4 generator"

    # The public dictionary constructor also has check=False by default.
    # Its generator images must nevertheless descend through C4's relation.
    try:
        four.Mor(three)({four.group_generators()[0]: three.group_generators()[0]})
    except ValueError as error:
        assert "relations" in str(error)
    else:
        assert False, "an invalid generator assignment was admitted without check=True"


def test_gap_group_morphism_requires_its_selected_endpoints() -> None:
    from dzack_research.preamble.categories.group.groups import _gap_model
    from sage.libs.gap.libgap import libgap

    two = Groups.C(2)
    three = Groups.C(3)
    identity_of_two = libgap.IdentityMapping(_gap_model(two))
    try:
        three.Mor(three)(identity_of_two)
    except ValueError as error:
        assert "does not have the selected endpoints" in str(error)
    else:
        assert False, "a GAP map of C2 was admitted as an endomorphism of C3"

    # The default Mor constructor does not request optional validation.
    # Even so, an unchecked GAP mapping violating a defining relation
    # cannot represent an arrow in the owned category of groups.
    four = Groups.C(4)
    model_four = _gap_model(four)
    model_three = _gap_model(three)
    bad = libgap.GroupHomomorphismByImagesNC(
        model_four, model_three,
        model_four.GeneratorsOfGroup(),
        model_three.GeneratorsOfGroup(),
    )
    try:
        four.Mor(three)(bad)
    except ValueError as error:
        assert "does not satisfy the source relations" in str(error)
    else:
        assert False, "unchecked GAP mapping C4 to a generator of C3 was admitted"



def test_the_cyclic_subgroups_of_c4_have_orders_four_and_two() -> None:
    group = Groups.C(4)
    generator = group.group_generators()[0]

    assert generator.cyclic_subgroup().order() == 4
    assert (generator**2).cyclic_subgroup().order() == 2


def test_symmetric_group_retains_its_chosen_point_set_and_action() -> None:
    points = Sets.Δ[2]
    group = SymmetricGroups(points)()
    assert group in SymmetricGroups(points)
    assert not SymmetricGroups(points).is_subcategory(OwnedGroups().Commutative())
    assert SymmetricGroups(Sets.Δ[1]).is_subcategory(OwnedGroups().Commutative())
    assert group.order() == 6
    assert group.natural_points() is points
    action = group.natural_g_set()
    assert action.point_set() is points
    from dzack_research.preamble.categories.group.g_sets import _permutation_from_point_map

    try:
        _permutation_from_point_map(group, points, lambda _point: points(0))
    except ValueError as error:
        assert "not represented by a permutation" in str(error)
    else:
        assert False, "a constant point map was accepted as a permutation"
    identity = group.one()
    for point in points:
        assert action.act(identity, point) == point
    from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
    # The common PermutationGroups owner must not silently extend an
    # unlabelled permutation's action beyond its represented domain.
    unlabelled = Groups.S(3)
    try:
        unlabelled.action_on(finite_ordered_set((1, 2, 3, 4)))
    except AssertionError as error:
        assert "selected domain" in str(error)
    else:
        assert False, "the common permutation category invented an action on a larger set"
    try:
        unlabelled.one()(-1)
    except ValueError as error:
        assert "outside the selected permutation domain" in str(error)
    else:
        assert False, "the common permutation action silently fixed an external point"

    labelled = finite_ordered_set(("alpha", "beta", "gamma"))
    labelled_group = SymmetricGroups(labelled)()
    assert labelled_group.natural_points() is labelled
    permutation = labelled_group((1, 2))
    labelled_action = labelled_group.natural_g_set()
    selected_action = labelled_group.action_on(labelled)
    assert selected_action is labelled_group.natural_g_set()
    assert selected_action.permutation_representation() is labelled_group.natural_g_set().permutation_representation()
    representation = labelled_group.natural_permutation_representation()
    assert representation is selected_action.permutation_representation()
    assert representation.domain() is labelled_group
    assert selected_action.acting_group() is labelled_group
    assert labelled_action.act(permutation, labelled("alpha")) == labelled("beta")
    assert permutation(labelled("alpha")) == labelled("beta")
    assert permutation(labelled("beta")) == labelled("alpha")
    try:
        permutation("outside")
    except ValueError as error:
        assert "outside the selected permutation domain" in str(error)
    else:
        assert False, "a permutation silently acquired a fixed point outside its selected domain"
    assert selected_action.act(permutation, labelled("alpha")) == labelled("beta")
    assert labelled_action.act(permutation, labelled("beta")) == labelled("alpha")
    assert labelled_action.act(permutation, labelled("gamma")) == labelled("gamma")

    # The defining action is transported along the actual ranking
    # isomorphism: products and inverses must respect that transport.
    cycle = labelled_group((1, 2, 3))
    for point in labelled:
        assert (permutation * cycle)(point) == permutation(cycle(point))
        assert (~cycle)(cycle(point)) == point
        assert labelled_action.act(cycle, point) == cycle(point)


def test_finite_symmetric_group_category_rejects_infinite_point_set() -> None:
    try:
        SymmetricGroups(NN)
    except AssertionError as error:
        assert "finite point set" in str(error)
    else:
        assert False, "the finite-group category admitted an infinite permutation domain"


def test_orders_of_catalogued_finite_groups_from_their_definitions() -> None:
    assert Groups.Weyl(["B", 2]).order() == 8
    assert Groups.PSL(2, 7).order() == 168


def test_coxeter_group_retains_its_matrix_and_type_a2_order() -> None:
    matrix = [[1, 3], [3, 1]]
    theory = CoxeterGroups(matrix)
    assert theory.is_subcategory(OwnedGroups().Finite())
    group = theory()
    assert theory.coxeter_matrix() is matrix
    assert group in theory
    assert group.coxeter_matrix() is matrix
    assert group.order() == 6
    assert group.is_isomorphic_to(SymmetricGroups(Sets.Δ[2])())

    # The matrix-group realization must carry the Coxeter presentation
    # through the common GroupsWithChosenFinitePresentation Mor owner.
    source = group.presenting_free_group()
    projection = group.quotient_projection()
    assert projection.domain() is source
    assert projection.codomain() is group
    assert all(projection(relation) == group.one() for relation in group.defining_relations())
    symmetric = SymmetricGroups(Sets.Δ[2])()
    free_generators = tuple(source.group_generators())
    f = source.Mor(symmetric)({
        free_generators[0]: symmetric((1, 2)),
        free_generators[1]: symmetric((2, 3)),
    })
    descended = group.descend_homomorphism(f)
    assert descended.domain() is group
    assert descended.codomain() is symmetric
    assert all(descended(projection(g)) == f(g) for g in free_generators)


def test_rank_two_coxeter_infinitude_depends_on_the_bond() -> None:
    commuting = CoxeterGroups([[1, 2], [2, 1]])
    finite = CoxeterGroups([[1, 4], [4, 1]])
    infinite = CoxeterGroups([[1, -1], [-1, 1]])
    assert commuting.is_subcategory(OwnedGroups().Commutative())
    assert commuting.is_subcategory(OwnedGroups().Finite())
    assert finite.is_subcategory(OwnedGroups().Finite())
    assert infinite.is_subcategory(OwnedGroups().Infinite())
    assert not infinite.is_subcategory(OwnedGroups().Finite())

    commuting_rank_three = CoxeterGroups([[1, 2, 2], [2, 1, 2], [2, 2, 1]])
    assert commuting_rank_three.is_subcategory(OwnedGroups().Finite())
    assert commuting_rank_three.is_subcategory(OwnedGroups().Commutative())
    two_a2_components = CoxeterGroups([
        [1, 3, 2, 2], [3, 1, 2, 2], [2, 2, 1, 3], [2, 2, 3, 1]
    ])
    assert two_a2_components.is_subcategory(OwnedGroups().Finite())
    assert not two_a2_components.is_subcategory(OwnedGroups().Commutative())
    a4 = CoxeterGroups([
        [1, 3, 2, 2], [3, 1, 3, 2], [2, 3, 1, 3], [2, 2, 3, 1]
    ])
    affine_a3 = CoxeterGroups([
        [1, 3, 2, 3], [3, 1, 3, 2], [2, 3, 1, 3], [3, 2, 3, 1]
    ])
    assert a4.is_subcategory(OwnedGroups().Finite())
    assert not affine_a3.is_subcategory(OwnedGroups().Finite())
    assert affine_a3.is_subcategory(OwnedGroups().Infinite())
    b4 = CoxeterGroups([
        [1, 4, 2, 2], [4, 1, 3, 2], [2, 3, 1, 3], [2, 2, 3, 1]
    ])
    affine_c3 = CoxeterGroups([
        [1, 4, 2, 2], [4, 1, 3, 2], [2, 3, 1, 4], [2, 2, 4, 1]
    ])
    assert b4.is_subcategory(OwnedGroups().Finite())
    assert not affine_c3.is_subcategory(OwnedGroups().Finite())
    assert affine_c3.is_subcategory(OwnedGroups().Infinite())
    d4 = CoxeterGroups([
        [1, 3, 3, 3], [3, 1, 2, 2], [3, 2, 1, 2], [3, 2, 2, 1]
    ])
    assert d4.is_subcategory(OwnedGroups().Finite())
    f4 = CoxeterGroups([
        [1, 3, 2, 2], [3, 1, 4, 2], [2, 4, 1, 3], [2, 2, 3, 1]
    ])
    h4 = CoxeterGroups([
        [1, 5, 2, 2], [5, 1, 3, 2], [2, 3, 1, 3], [2, 2, 3, 1]
    ])
    assert f4.is_subcategory(OwnedGroups().Finite())
    assert h4.is_subcategory(OwnedGroups().Finite())
    # The finite-type decision belongs to the selected Sage Coxeter
    # matrix, not to a separately maintained ADE/B/H pattern catalogue.
    assert f4._engine_coxeter_matrix.is_finite() is True
    assert h4._engine_coxeter_matrix.is_finite() is True
    # E6: the central vertex has arms of lengths 1, 2, 2.
    e6 = CoxeterGroups([
        [1, 3, 2, 2, 2, 2], [3, 1, 3, 2, 2, 2],
        [2, 3, 1, 3, 2, 3], [2, 2, 3, 1, 3, 2],
        [2, 2, 2, 3, 1, 2], [2, 2, 3, 2, 2, 1],
    ])
    assert e6.is_subcategory(OwnedGroups().Finite())
    # Affine E6 has three arms of length two, so it is not spherical.
    affine_e6 = CoxeterGroups([
        [1, 3, 2, 2, 2, 2, 2], [3, 1, 3, 2, 2, 2, 2],
        [2, 3, 1, 3, 2, 3, 2], [2, 2, 3, 1, 3, 2, 2],
        [2, 2, 2, 3, 1, 2, 2], [2, 2, 3, 2, 2, 1, 3],
        [2, 2, 2, 2, 2, 3, 1],
    ])
    assert not affine_e6.is_subcategory(OwnedGroups().Finite())
    infinite_rank_three = CoxeterGroups([[1, -1, 2], [-1, 1, 2], [2, 2, 1]])
    assert infinite_rank_three.is_subcategory(OwnedGroups().Infinite())
    affine_a2 = CoxeterGroups([[1, 3, 3], [3, 1, 3], [3, 3, 1]])
    assert affine_a2.is_subcategory(OwnedGroups().Infinite())
    assert not affine_a2.is_subcategory(OwnedGroups().Finite())
    affine_c2 = CoxeterGroups([[1, 4, 4], [4, 1, 2], [4, 2, 1]])
    hyperbolic_triangle = CoxeterGroups([[1, 5, 5], [5, 1, 5], [5, 5, 1]])
    spherical_triangle = CoxeterGroups([[1, 3, 3], [3, 1, 2], [3, 2, 1]])
    assert affine_c2.is_subcategory(OwnedGroups().Infinite())
    assert hyperbolic_triangle.is_subcategory(OwnedGroups().Infinite())
    assert not spherical_triangle.is_subcategory(OwnedGroups().Infinite())
    assert spherical_triangle.is_subcategory(OwnedGroups().Finite())


def test_mutating_selected_coxeter_matrix_does_not_change_its_group() -> None:
    matrix = [[1, 3], [3, 1]]
    category = CoxeterGroups(matrix)
    matrix[0][1] = 4
    matrix[1][0] = 4
    try:
        category.super_categories()
    except ValueError as error:
        assert "changed after category construction" in str(error)
    else:
        assert False, "a mutated Coxeter matrix retained its category placement"
    try:
        category.coxeter_matrix()
    except ValueError as error:
        assert "changed after category construction" in str(error)
    else:
        assert False, "the Coxeter category returned a mutated defining matrix"
    try:
        category()
    except ValueError as error:
        assert "changed after category construction" in str(error)
    else:
        assert False, "a mutated defining matrix silently changed the selected Coxeter group"

    matrix = [[1, 3], [3, 1]]
    realized = CoxeterGroups(matrix)()
    assert realized.coxeter_matrix() is matrix
    matrix[0][1] = matrix[1][0] = 4
    try:
        realized.coxeter_matrix()
    except ValueError as error:
        assert "changed after group construction" in str(error)
    else:
        assert False, "a realized Coxeter group reported a mutated defining matrix"


def test_free_group_quotient_retains_source_and_dihedral_relations() -> None:
    free = Groups.Free(2)
    a, b = tuple(free.group_generators())
    relators = (a**2, b**3, (a*b)**2)
    theory = FreeGroupQuotients(free, relators)
    quotient = theory()
    assert theory.free_group() is free
    assert theory.relators() == relators
    assert quotient in theory
    assert quotient.order() == 6
    assert quotient.presenting_free_group() is free
    assert tuple(quotient.defining_relations()) == relators
    projection = quotient.quotient_projection()
    assert projection.domain() is free
    assert projection.codomain() is quotient
    assert all(projection(relation) == quotient.one() for relation in relators)
    descended = quotient.descend_homomorphism(projection)
    assert descended.domain() is quotient
    assert descended.codomain() is quotient
    assert all(descended(projection(generator)) == projection(generator) for generator in (a, b))
    assert all(descended(projection(word)) == projection(word) for word in (a*b, b*a, a*b*a, b**2*a))
    symmetric = SymmetricGroups(Sets.Δ[2])()
    free_to_symmetric = free.Mor(symmetric)(
        {a: symmetric((1, 2)), b: symmetric((1, 2, 3))}
    )
    symmetric_descent = quotient.descend_homomorphism(free_to_symmetric)
    assert symmetric_descent.domain() is quotient
    assert symmetric_descent.codomain() is symmetric
    assert all(
        symmetric_descent(projection(word)) == free_to_symmetric(word)
        for word in (a, b, a*b, b*a, a*b*a, b**2*a)
    )
    cyclic = Groups.C(2)
    wrong = free.Mor(cyclic)({a: cyclic.one(), b: cyclic.group_generators()[0]})
    # The same relator obstruction must hold at the shared GroupMor owner,
    # not only in the convenience descent operation: b^3 is nontrivial.
    quotient_a, quotient_b = tuple(quotient.group_generators())
    try:
        quotient.Mor(cyclic)(
            {quotient_a: cyclic.one(), quotient_b: cyclic.group_generators()[0]},
            check=True,
        )
    except ValueError as error:
        assert "relations" in str(error)
    else:
        assert False, "the presented group Mor admitted generator images violating b^3"
    try:
        quotient.descend_homomorphism(wrong)
    except ValueError as error:
        assert "defining relators" in str(error)
    else:
        assert False, "a map not killing the relations descended to the quotient"
    assert quotient.is_isomorphic_to(SymmetricGroups(Sets.Δ[2])())

    # The ordinary quotient operation is another entry into the same
    # mathematical construction, not a weaker anonymous presentation.
    from_operation = free.quotient_by_relators(relators)
    assert from_operation in theory
    assert from_operation.presenting_free_group() is free
    assert tuple(from_operation.defining_relations()) == relators
    free_quotient, free_projection = free.quotient_by_relators(
        relators, return_projection=True
    )
    assert free_projection is free_quotient.quotient_projection()
    assert free_projection.domain() is free
    assert free_projection.codomain() is free_quotient

    # Quotienting a presented group must adjoin the new normal relators
    # to its original free presentation, not treat its generators as free.
    # S_3 / <<(123)>> = C_2, whereas a fresh free quotient would forget
    # the original a^2, b^3 and (ab)^2 relations.
    second_quotient, second_projection = quotient.quotient_by_relators(
        (projection(b),), return_projection=True
    )
    assert second_projection.domain() is quotient
    assert second_projection.codomain() is second_quotient
    assert second_projection(projection(b)) == second_quotient.one()
    # Universal property of the *iterated* quotient, with the actual
    # domain S_3 rather than the presenting free group: a homomorphism
    # killing b factors through q, including on non-generator words.
    target_c2 = Groups.C(2)
    target_involution = tuple(target_c2.group_generators())[0]
    source_to_c2 = quotient.Mor(target_c2)(
        (target_involution, target_c2.one()), check=True
    )
    factored = second_quotient.Mor(target_c2)(
        (target_involution, target_c2.one()), check=True
    )
    descended_quotient = second_quotient.descend_homomorphism(
        source_to_c2, through=second_projection
    )
    assert all(
        factored(second_projection(projection(word))) == source_to_c2(projection(word))
        for word in (a, b, a*b, b*a, a*b*a, b**2*a)
    )
    assert all(
        descended_quotient(second_projection(projection(word))) == source_to_c2(projection(word))
        for word in (a, b, a*b, b*a, a*b*a, b**2*a)
    )
    # Identity on S_3 does not descend through S_3 / <<b>>: the
    # quotient kills b, whereas identity preserves its nontrivial image.
    identity_on_source = quotient.Mor(quotient)(
        tuple(quotient.group_generators()), check=True
    )
    assert identity_on_source(projection(b)) != quotient.one()
    try:
        quotient.descend_homomorphism(identity_on_source, through=identity_on_source)
    except ValueError as error:
        assert "selected normal-quotient" in str(error)
    else:
        assert False, "an arbitrary group Mor was admitted as a quotient witness"
    try:
        second_quotient.descend_homomorphism(
            identity_on_source, through=second_projection
        )
    except ValueError:
        pass
    else:
        assert False, "a map nontrivial on the quotient kernel descended"
    assert second_projection(projection(a * b * a)) == (
        second_projection(projection(a))
        * second_projection(projection(b))
        * second_projection(projection(a))
    )
    assert second_quotient.order() == 2
    assert second_quotient.is_isomorphic_to(Groups.C(2))
    assert second_quotient.quotient_projection().domain() is second_quotient.presenting_free_group()
    assert second_quotient.presentation_source_group() is second_quotient
    assert second_quotient.presentation_isomorphism().domain() is second_quotient

    try:
        quotient.quotient_by_relators(NN, return_projection=True)
    except ValueError as error:
        assert "finite relators" in str(error)
    else:
        assert False, "an infinite relation family was exhausted by the quotient constructor"

    try:
        quotient.quotient_by_relators((Groups.C(2).one(),))
    except ValueError as error:
        assert "group being quotiented" in str(error)
    else:
        assert False, "the normal closure accepted an element of another group"


def test_a_chosen_generating_set_does_not_make_a_group_free() -> None:
    cyclic = Groups.C(3)
    assert cyclic.has_selected_group_resolution()
    try:
        FreeGroupQuotients(cyclic, (cyclic.one(),))
    except AssertionError as error:
        assert "actual free group" in str(error)
    else:
        assert False, "a nonfree cyclic group was admitted as a free source"


def test_finitely_many_relators_require_a_finite_free_basis() -> None:
    infinite_free = Groups.Free(index_set=NN)
    try:
        FreeGroupQuotients(infinite_free, ())
    except ValueError as error:
        assert "finite free basis" in str(error)
    else:
        assert False, "an infinite-rank free group was assigned a finite presentation"

    finite_free = Groups.Free(1)
    try:
        FreeGroupQuotients(finite_free, NN)
    except ValueError as error:
        assert "finite relator family" in str(error)
    else:
        assert False, "an infinite set of relators was assigned a finite presentation"

    # Relations from another presented group are not words in this
    # selected free source, even if both have one chosen generator.
    from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
    other_free = Groups.Free(index_set=finite_ordered_set(("z",)))
    other_generator = other_free.group_generators()[0]
    try:
        FreeGroupQuotients(finite_free, (other_generator,))
    except ValueError as error:
        assert "selected presenting free group" in str(error)
    else:
        assert False, "a relator from another free group changed the selected presentation"


def test_quotient_descent_with_identified_presenting_generators() -> None:
    free = Groups.Free(2)
    a, b = tuple(free.group_generators())
    quotient = FreeGroupQuotients(free, (a * ~b, a**2))()
    projection = quotient.quotient_projection()
    assert projection(a) == projection(b)

    cyclic = Groups.C(2)
    involution = cyclic.group_generators()[0]
    compatible = free.Mor(cyclic)({a: involution, b: involution})
    descended = quotient.descend_homomorphism(compatible)
    assert descended.domain() is quotient
    assert descended.codomain() is cyclic
    assert descended(projection(a)) == descended(projection(b)) == involution
    checked = quotient.Mor(cyclic)(
        {projection(a): involution}, check=True
    )
    assert checked(projection(a)) == checked(projection(b)) == involution

    incompatible = free.Mor(cyclic)({a: involution, b: cyclic.one()})
    try:
        quotient.descend_homomorphism(incompatible)
    except ValueError as error:
        assert "defining relators" in str(error)
    else:
        assert False, "identified quotient generators received different target images"


def test_quotient_descent_respects_the_selected_free_basis_labels() -> None:
    labels = Sets.Δ[1]
    free = Groups.Free(index_set=labels)
    a = free.free_generator(labels(0))
    b = free.free_generator(labels(1))
    quotient = FreeGroupQuotients(free, (a**2, b**3, (a*b)**2))()
    projection = quotient.quotient_projection()
    descended = quotient.descend_homomorphism(projection)
    assert descended.domain() is quotient
    assert descended.codomain() is quotient
    assert all(descended(projection(free.free_generator(i))) == projection(free.free_generator(i)) for i in labels)


def test_general_linear_group_retains_ring_and_rank() -> None:
    category = GeneralLinearGroups(GF(2), 2)
    group = category()
    assert group in category
    assert category.is_subcategory(OwnedGroups().Finite())
    assert category.coefficient_ring() is GF(2)
    assert category.degree() == 2
    assert group.coefficient_ring() is category.coefficient_ring()
    assert group.degree() == category.degree()
    assert group.order() == 6
    assert group.is_isomorphic_to(SymmetricGroups(Sets.Δ[2])())

    # Repeated constructions must retain the same selected ring and rank;
    # the temporary pair passed to the engine cache is not a datum identity.
    second_category = GeneralLinearGroups(GF(3), 2)
    second_group = second_category()
    assert second_group.coefficient_ring() is GF(3)
    assert second_group.degree() == 2
    assert second_group.order() == 48

    # GL_1(ZZ) is the group of units {+1,-1}, while GL_2(ZZ)
    # contains an infinite cyclic subgroup of unipotent matrices.
    assert GeneralLinearGroups(ZZ, 1).is_subcategory(OwnedGroups().Finite())
    assert GeneralLinearGroups(ZZ, 1).is_subcategory(OwnedGroups().Commutative())
    assert GeneralLinearGroups(QQ, 1).is_subcategory(OwnedGroups().Commutative())
    assert not GeneralLinearGroups(GF(2), 2).is_subcategory(OwnedGroups().Commutative())
    assert not GeneralLinearGroups(ZZ, 2).is_subcategory(OwnedGroups().Finite())
    assert GeneralLinearGroups(ZZ, 2).is_subcategory(OwnedGroups().Infinite())
    assert GeneralLinearGroups(QQ, 1).is_subcategory(OwnedGroups().Infinite())
    assert GeneralLinearGroups(QQ, 2).is_subcategory(OwnedGroups().Infinite())
    assert GeneralLinearGroups(QQ["t"].fraction_field(), 1).is_subcategory(OwnedGroups().Infinite())


def test_general_linear_rank_cannot_be_truncated() -> None:
    try:
        GeneralLinearGroups(GF(2), QQ(3) / 2)
    except AssertionError as error:
        assert "integral rank" in str(error)
    else:
        assert False, "a nonintegral rank was silently truncated"


def test_the_heisenberg_group_over_z_mod_three_has_twenty_seven_elements() -> None:
    assert Groups.Heisenberg(1, 3).order() == 27


def test_sl2z_and_the_three_strand_braid_group_are_infinite() -> None:
    modular = Groups.SL(2, ZZ)

    assert not modular.is_finite()
    assert modular.is_arithmetic_group()
    assert not Groups.Braid(3).is_finite()


def test_special_linear_rank_is_not_truncated() -> None:
    try:
        Groups.SL(QQ(5) / 2, ZZ)
    except ValueError as error:
        assert "integral rank" in str(error)
    else:
        assert False, "SL of nonintegral degree was admitted as SL2"


def test_named_matrix_group_families_require_integral_degree() -> None:
    for constructor in (Groups.GL, Groups.Sp, Groups.SO):
        try:
            constructor(QQ(5) / 2, ZZ)
        except ValueError as error:
            assert "degree must be an integer" in str(error)
        else:
            assert False, "a matrix group was constructed at a fractional degree"
