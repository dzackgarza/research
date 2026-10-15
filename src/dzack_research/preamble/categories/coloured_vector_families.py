r"""Stabilizers and transporters of coloured families of lattice vectors in ``O(L)``.

A family of vectors of a lattice ``L`` is a set map ``v: I -> U(L)`` from a
finite set ``I``, an element of ``Sets().Mor(I, L)``.  A colouring is a set map
``c: I -> C``; a coloured family is the family of pairs ``(v_i, c_i)``, a map
``I -> U(L) x C`` that need not be injective (a Lorentzian perfect cell has
more rays than its rank, and a vector may repeat).  ``O(L)`` acts on these
families by ``g . (v_i, c_i) = (g v_i, c_i)``, and the questions asked are up
to colour-preserving reindexing (``CAT-30``):

- ``L.O().stabilizer(family)`` is
  ``O(L)_[v] = {g in O(L) : g o v = v o sigma for some colour-preserving bijection sigma of I}``;
- ``L.O().transporter(family, other)`` is one ``g`` with ``g o v = w o sigma``
  for some colour-preserving bijection ``sigma: I -> J``, or ``None``.

These are the images under ``(g, sigma) |-> g`` of the stabilizer and the
transporter of ``v`` under ``O(L) x Sym_C(I)`` acting on ``L^I`` by
``g o v o sigma^-1``.  The kernel of that projection on the stabilizer is
``K_v = {sigma in Sym_C(I) : v o sigma = v}``, the product of the full
symmetric groups on the sets ``{i : (v_i, c_i) = (x, col)}``; it is trivial
exactly when the coloured family is injective, and then
``sigma = (v, c)^-1 o (g x id) o (v, c)`` is determined by ``g``
(``L.O().index_action(family)``).  The product of the infinite group ``O(L)``
with ``Sym_C(I)`` is not represented (COMPLAINTS.md, *Products of infinite
groups are not represented*), so pairs ``(g, sigma)`` are not built and
``K_v`` is stated, not constructed.

A family enters as the set map it is: an element of ``Sets().Mor(I, L)`` (one
colour) or of ``Sets().Mor(I, Sets().product((L, C)))`` (a coloured family).

The computation (Indefinite.jl@374a5ebb/indef/lib/AutomorphismPolytope.g,
KernelLinPolytopeIntegral_Automorphism_Subspaces :366-412 and
KernelLinPolytopeIntegral_Isomorphism_Subspaces :288-339).  The labelled
pairing graph ``Gamma`` has a vertex per index, labelled by its colour and
square, and an edge labelled by each nonzero pairing ``b(v_i, v_j)``;
``Aut(Gamma)`` is the group of colour- and pairing-preserving permutations of
``I`` (Sage's bliss/nauty backend, inside :class:`_LabelledPairingGraph`).
When the vectors span the nondegenerate rational space ``L tensor Q``, each
``sigma`` in ``Aut(Gamma)`` determines a unique rational isometry ``T_sigma``
with ``T_sigma(v_i) = v_sigma(i)``, computed by exact solving in the
rational space; ``rho: Aut(Gamma) -> O(L tensor Q)`` has kernel ``K_v`` and
image ``G``, and ``O(L)_[v] = G cap GL(L)`` is the stabilizer of the
integral structure ``L`` under ``G``, computed by
:class:`IntegralStructureAction` with the ``G``-stable bound ``K/e`` (``K``
the span of the vectors, ``e`` the exponent of ``L/K``).  The graph group is
never enumerated.  Spanning, nondegeneracy and the base ring ``ZZ`` are the
current computational frontier, asserted where they are used.
"""

from sage.graphs.graph import Graph
from sage.misc.cachefunc import cached_function, cached_method

from dzack_research.preamble.categories.modules.pure.modules import Modules, ModulesOverIntegralDomains
from dzack_research.preamble.categories.rings.ring_foundation import _owned_integers
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets


class _LabelledPairingGraph:
    """Private adapter (OWN-06): the labelled pairing graph of a coloured family.

    Declared engine boundary, and the only site in this module holding a Sage
    ``Graph`` or integer vertex coordinates.  ``LabelledGraphs`` presents
    label-preserving ``Mor`` but no computed isomorphism or automorphism group
    (recorded in COMPLAINTS), so the bliss/nauty computations run here.

    Data: an owned finite ordered set of indices, the owned Gram tensor on
    the free module on those indices, and the owned colouring map of the
    indices.  The tensor is lowered once (``_engine_component_matrix``);
    the indices are lowered by their ``ranking_map``.  Leaving the adapter:
    an owned subgroup of the symmetric group on the indices, the induced
    permutations of the indices as set maps, and isomorphisms as set maps of
    indices.
    """

    def __init__(self, positions, gram, colouring):
        self._positions = positions
        self._gram = gram
        self._colouring = colouring

    def _size(self):
        return int(self._positions.cardinality())

    def _vertex(self, position):
        return int(self._positions.ranking_map()(position))

    def _position(self, vertex):
        return self._positions.ranking_map().inverse()(int(vertex))

    @cached_method
    def _graph(self):
        from dzack_research.preamble.tensors.tensor import _engine_component_matrix

        pairings = _engine_component_matrix(self._gram)
        size = self._size()
        graph = Graph(loops=True, multiedges=False)
        graph.add_vertices(range(size))
        for left in range(size):
            colour = self._colouring(self._position(left))
            graph.add_edge(left, left, ("vertex", colour, pairings[left, left]))
            for right in range(left):
                if pairings[left, right]:
                    graph.add_edge(left, right, ("pairing", pairings[left, right]))
        return graph

    @cached_method
    def _symmetric_group(self):
        from dzack_research.preamble.categories.group.groups import Groups

        return Groups.S(self._size())

    @cached_method
    def automorphism_group(self):
        r"""``Aut(Gamma)``: the subgroup of ``S_m`` generated by the engine's automorphisms."""
        symmetric = self._symmetric_group()
        size = self._size()
        engine = self._graph().automorphism_group(edge_labels=True)
        return symmetric.subgroup(tuple(
            symmetric([int(generator(vertex)) + 1 for vertex in range(size)])
            for generator in engine.gens()
        ))

    def position_permutation(self, automorphism):
        r"""The permutation of the indices induced by an element of ``Aut(Gamma)``."""
        return Sets().Mor(self._positions, self._positions)(
            lambda position: self._position(int(automorphism(self._vertex(position) + 1)) - 1)
        )

    def isomorphism(self, other):
        r"""A colour- and pairing-preserving bijection of indices onto ``other``'s, or ``None``."""
        equivalent, certificate = self._graph().is_isomorphic(
            other._graph(), edge_labels=True, certificate=True
        )
        if not equivalent:
            return None
        return Sets().Mor(self._positions, other._positions)(
            lambda position: other._position(certificate[self._vertex(position)])
        )


class _ColouredFamilyRealization:
    """Private realization of the linear algebra of a coloured family ``(v_i, c_i)_{i in I}`` in ``L``.

    The free modules on ``I`` here are computational: the Gram matrix of the
    family and the exact solving behind ``T_sigma`` are read through the
    module maps ``F(I) -> L`` and ``F_Q(I) -> L tensor Q``, ``e_i |-> v_i``;
    they are not how a family is defined.  Every value leaving this class is
    a preamble object.  Nothing is computed at construction (``OWN-22``).
    """

    def __init__(self, lattice, family):
        self._lattice = lattice
        self._family = family
        self._indices = family.domain()
        assert self._indices.cardinality().is_finite() is True, (
            f"stabilizers of families in O({lattice}) are computed for finite index sets, but {family} is "
            f"a map out of {self._indices}"
        )
        values = family.codomain()
        if values is lattice:
            self._colours = Sets.Δ[0]
            point = next(iter(self._colours))
            self._vector = family
            self._colour = lambda _index: point
        else:
            assert values.factor(0) is lattice, (
                f"{family} is neither a family of vectors of {lattice} nor of points of {lattice} x C: it is a "
                f"map into {values}"
            )
            self._colours = values.factor(1)
            self._vector = lambda index: values.projection(0)(family(index))
            self._colour = lambda index: values.projection(1)(family(index))

    def indices(self):
        return self._indices

    def vector(self, index):
        return self._vector(index)

    def colour(self, index):
        return self._colour(index)

    @cached_method
    def colouring(self):
        r"""The colouring ``c: I -> C``."""
        return Sets().Mor(self._indices, self._colours)(self.colour)

    @cached_method
    def free_module(self):
        r"""The free module on the indices, a computational device (see the class docstring)."""
        return self._lattice.base_ring().free_module(self._indices)

    @cached_method
    def family_morphism(self):
        r"""The module morphism ``F(I) -> L``, ``e_i |-> v_i``, through which the Gram matrix is pulled back."""
        return Modules(self._lattice.base_ring()).Mor(self.free_module(), self._lattice)(self.vector)

    @cached_method
    def span(self):
        r"""The sublattice ``K`` spanned by the family, with its inclusion into ``L``."""
        return self._lattice.subobject_on(tuple(self.vector(index) for index in self._indices))

    def assert_spanning_nondegenerate(self):
        lattice = self._lattice
        assert lattice.base_ring() is _owned_integers(), (
            f"stabilizers and transporters of coloured families of vectors are computed for lattices over ZZ, "
            f"but {lattice} is over {lattice.base_ring()}"
        )
        assert lattice.is_nondegenerate() is True, (
            f"the pairing permutation action of a family in {lattice} is faithful only when the lattice is "
            f"nondegenerate, and {lattice} is not known to be"
        )
        assert self.span().module_rank() == lattice.rank(), (
            f"the vectors of {self._family} span a sublattice of rank {self.span().module_rank()} of {lattice}, "
            f"of rank {lattice.rank()}: the pairings of a non-spanning family do not determine an isometry, and "
            f"its stabilizer contains the pointwise stabilizer of its span, which is not computed here"
        )

    @cached_method
    def pairing_graph(self):
        self.assert_spanning_nondegenerate()
        gram = self._lattice.gram_tensor().pullback(self.family_morphism())
        return _LabelledPairingGraph(self._indices, gram, self.colouring())

    def rationalization(self):
        r"""The lattice in its rational space, ``L -> Res(L tensor Q)``."""
        return ModulesOverIntegralDomains(self._lattice.base_ring())(self._lattice).generic_fibre_map()

    def rational_space(self):
        return self._lattice.base_change(self._lattice.base_ring().fraction_field_map())

    @cached_method
    def rational_family(self):
        r"""The family as the rational module morphism ``F_Q(I) -> L tensor Q``, surjective by spanning."""
        rational = self.rational_space()
        rationalization = self.rationalization()
        positions = rational.base_ring().free_module(self._indices)
        return Modules(rational.base_ring()).Mor(positions, rational)(
            lambda index: rationalization(self.vector(index)).underlying_element()
        )

    @cached_method
    def family_section(self):
        r"""A section ``L tensor Q -> F_Q(I)`` of the surjective rational family, solved once on the framing."""
        family = self.rational_family()
        rational = self.rational_space()
        return Modules(rational.base_ring()).Mor(rational, family.domain())({
            label: family.lift(rational.module_generator(label))
            for label in rational.module_generating_set()
        })

    def rational_transformation(self, target, sigma):
        r"""The rational isometry ``T_sigma`` with ``T_sigma(v_i) = w_sigma(i)``.

        ``sigma`` is a set map of this family's indices onto ``target``'s.  For
        a colour- and pairing-preserving bijection of nondegenerate spanning
        families ``T_sigma`` exists and is unique: a vector is lifted along the
        surjective family morphism, its coefficients are moved by ``sigma``,
        and the target family morphism is applied.
        """
        self.assert_spanning_nondegenerate()
        target.assert_spanning_nondegenerate()
        target_family = target.rational_family()
        source_positions = self.rational_family().domain()
        target_positions = target_family.domain()
        relabel = Modules(source_positions.base_ring()).Mor(source_positions, target_positions)(
            lambda index: target_positions.module_generator(sigma(index))
        )
        rational_target = target.rational_space()
        section = self.family_section()
        rational_source = self.rational_space()
        return rational_source.Isom(rational_target)(
            lambda label: target_family(relabel(section(rational_source.module_generator(label))))
        )

    @cached_method
    def configuration_group(self):
        r"""``G = rho(Aut(Gamma))`` for the group morphism ``rho: Aut(Gamma) -> O(L tensor Q)``."""
        graph = self.pairing_graph()
        rational = self.rational_space()
        automorphisms = graph.automorphism_group()
        orthogonal = rational.O()

        def realization(generator):
            isometry = self.rational_transformation(self, graph.position_permutation(generator))
            return orthogonal({
                label: isometry(rational.module_generator(label))
                for label in rational.module_generating_set()
            })

        rho = automorphisms.Mor(orthogonal)({
            generator: realization(generator) for generator in automorphisms.group_generators()
        })
        return rho.image()

    @cached_method
    def containing_bound(self):
        r"""The exponent ``e`` of ``L/K`` and the ``G``-stable module ``K/e`` containing ``L``.

        ``G`` permutes the family, so ``K`` and ``K/e`` are stable, and ``eL``
        lies in ``K``.
        """
        lattice = self._lattice
        span = self.span()
        exponent = span.inclusion().cokernel().exponent()
        assert exponent > lattice.base_ring().zero(), (
            f"the vectors of {self._family} span a sublattice of infinite index in {lattice}, so no finite "
            f"stable module contains {lattice}"
        )
        rationalization = self.rationalization()
        ambient_space = rationalization.codomain()
        rational = self.rational_space()
        scale = rational.base_ring().one() / rational.base_ring()(exponent)
        inclusion = span.inclusion()
        containing = Modules(lattice.base_ring()).Mono(span, ambient_space)(
            lambda label: ambient_space.wrap(rational.scalar_multiple(
                scale, rationalization(inclusion(span.module_generator(label))).underlying_element(),
            ))
        )
        return exponent, containing


@cached_function(key=lambda lattice, family: (id(lattice), id(family)))
def _realization(lattice, family):
    return _ColouredFamilyRealization(lattice, family)


def _matching(source, target, isometry):
    r"""The bijection ``sigma`` with ``(g v_i, c_i) = (w_sigma(i), d_sigma(i))``, or ``None``.

    ``g o v = w o sigma`` for a colour-preserving bijection exactly when such a ``sigma`` exists.  Equality of
    points of ``L x C`` is an equivalence, so matching each index to any
    unmatched index carrying the same coloured vector finds a bijection
    whenever one exists.
    """
    target_indices = tuple(target.indices())
    if source.indices().cardinality() != target.indices().cardinality():
        return None
    used = set()
    images = {}
    for index in source.indices():
        image = isometry(source.vector(index))
        colour = source.colour(index)
        partner = next(
            (
                position
                for position, candidate in enumerate(target_indices)
                if position not in used
                and target.vector(candidate) == image
                and target.colour(candidate) == colour
            ),
            None,
        )
        if partner is None:
            return None
        used.add(partner)
        images[index] = target_indices[partner]
    return images


def _stabilizer_generators(orthogonal_group, family):
    r"""Generators of ``O(L)_[v]``: the stabilizer of ``L`` in ``G = rho(Aut(Gamma))``."""
    from dzack_research.preamble.categories.rational_integral_stabilizers import IntegralStructureAction

    lattice = orthogonal_group.lattice()
    realization = _realization(lattice, family)
    rational_group = realization.configuration_group()
    generators = rational_group.group_generators()
    if all(generator.integral_restriction(lattice, lattice) is not None for generator in generators):
        integral = generators
    else:
        _exponent, containing = realization.containing_bound()
        integral = IntegralStructureAction(rational_group, realization.rationalization()).with_stable_containing_bound(
            containing
        ).stabilizer().group_generators()
    return tuple(_owned_isometry(orthogonal_group, lattice.integral_isometry(generator)) for generator in integral)


def _transporter(orthogonal_group, source_family, target_family):
    r"""One ``g`` in ``O(L)`` with ``g o v = w o sigma`` for a colour-preserving bijection ``sigma``, or ``None``.

    A colour- and pairing-preserving bijection ``sigma`` of the families gives
    the rational isometry ``T_0 = T_sigma``; every rational ``g`` carrying
    ``(v, c)`` to ``(w, d)`` up to colour-preserving reindexing is ``h T_0`` with ``h`` in the configuration group
    ``G`` of the target.  An integral one carries ``T_0(L)`` to ``L``: the
    transporter of the integral-structure action of ``G``, bounded by the
    ``G``-stable module ``K'/e'``.  The exponent ``e`` of ``L/K`` is an
    invariant of the transport, so different exponents decide that there is none.
    """
    from dzack_research.preamble.categories.rational_integral_stabilizers import IntegralStructureAction

    lattice = orthogonal_group.lattice()
    source = _realization(lattice, source_family)
    target = _realization(lattice, target_family)
    if source.indices().cardinality() != target.indices().cardinality():
        return None
    sigma = source.pairing_graph().isomorphism(target.pairing_graph())
    if sigma is None:
        return None
    equivalence = source.rational_transformation(target, sigma)
    if equivalence.integral_restriction(lattice, lattice) is not None:
        return _owned_isometry(orthogonal_group, lattice.integral_isometry(equivalence))
    source_exponent, _source_containing = source.containing_bound()
    target_exponent, containing = target.containing_bound()
    if source_exponent != target_exponent:
        return None
    rational_source = source.rational_space()
    rational_target = target.rational_space()
    source_rationalization = source.rationalization()
    target_rationalization = target.rationalization()
    ambient_space = target_rationalization.codomain()
    moved = Modules(lattice.base_ring()).Mono(lattice, ambient_space)(
        lambda label: ambient_space.wrap(
            equivalence(source_rationalization(lattice.module_generator(label)).underlying_element())
        )
    )
    transporter = IntegralStructureAction(target.configuration_group(), moved).with_stable_containing_bound(
        containing
    ).transporter(target_rationalization)
    if transporter is None:
        return None
    composite = rational_source.Isom(rational_target)(
        lambda label: transporter(equivalence(rational_source.module_generator(label)))
    )
    return _owned_isometry(orthogonal_group, lattice.integral_isometry(composite))


def _owned_isometry(orthogonal_group, isometry):
    r"""The element of ``O(L)`` acting on ``L`` as ``isometry`` does."""
    lattice = orthogonal_group.lattice()
    if isometry.parent() is orthogonal_group:
        return isometry
    return orthogonal_group(lambda label: isometry(lattice.module_generator(label)))


def _index_permutation(orthogonal_group, family, isometry):
    r"""``sigma = (v, c)^-1 o (g x id) o (v, c)`` on ``I``, for an injective coloured family.

    The caller has asserted injectivity (:func:`_assert_injective`); ``g`` lies
    in the stabilizer, so the matching exists and is unique.
    """
    realization = _realization(orthogonal_group.lattice(), family)
    images = _matching(realization, realization, isometry)
    assert images is not None, (
        f"{isometry} does not carry the coloured family {family} to itself up to colour-preserving "
        f"reindexing, so it is not in its stabilizer"
    )
    return images


def _assert_injective(orthogonal_group, family):
    r"""Assert that no two indices carry the same coloured vector, so that ``K_v`` is trivial."""
    realization = _realization(orthogonal_group.lattice(), family)
    indices = tuple(realization.indices())
    repeated = next(
        (
            (left, right)
            for position, left in enumerate(indices)
            for right in indices[position + 1:]
            if realization.vector(left) == realization.vector(right)
            and realization.colour(left) == realization.colour(right)
        ),
        (),
    )
    assert repeated == (), (
        f"the family {family} carries one coloured vector at two indices {repeated}, so an element of its "
        f"stabilizer determines a permutation of the indices only up to K_v, the permutations of the indices "
        f"carrying equal coloured vectors; the action on indices is defined for injective coloured families"
    )
    return realization
