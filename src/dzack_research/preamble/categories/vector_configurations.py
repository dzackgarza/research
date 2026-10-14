r"""Configurations of lattice vectors, their pairing graphs, and permutation lifting.

A *configuration* is a sublattice together with a chosen ordered family of
vectors framing it.  Its pairing graph has one vertex per chosen vector, a
loop at each vertex labelled by that vector's square, and an edge between two
vertices labelled by their pairing whenever the pairing is nonzero.  A
labelled graph automorphism is exactly a permutation of the family preserving
every pairing, and such a permutation extends uniquely to an isometry of the
sublattice the family frames, because the family is a basis of it.

So the pairing graph turns a configuration-isometry question into a labelled
graph-isomorphism question, which Sage answers exactly with its bliss/nauty
backend (``Graph.automorphism_group``).  This is the standard reduction; the
same one is what CoxIter uses for the automorphism group of a Coxeter
polytope's facet configuration.

The graph is a private encoding and never leaves this module.  A session
receives an owned permutation group of the framing positions, owned isometries
of the sublattice, and, when the framing is a basis of the whole lattice, owned
elements of its orthogonal group.

A permutation is presented to the lifting operation as a map on the framing's
index set, which is the datum a mathematician has: the image position of each
chosen vector.  For a root basis this recovers the diagram automorphisms:
``A2`` gives the order-two swap, ``D4`` gives triality with its symmetric group
of order six, and ``E8`` gives the trivial group.
"""

from sage.graphs.graph import Graph
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules.pure.modules import ModuleSubobjects
from dzack_research.preamble.categories.modules.pure.modules import Modules, ModulesOverIntegralDomains
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family_from_values,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


class VectorConfigurations(OwnedCategoryOverBaseRing):
    r"""Sublattices with a chosen ordered framing and a colouring of it.

    The data are the framing, which is the configuration's family of vectors,
    and the colouring, a map from its positions to a set of colours (the
    constant colouring when none is stated). An automorphism of the coloured
    configuration is a framing permutation preserving every pairing and every
    colour; the pairing graph records both.
    """

    @classmethod
    def _repr_object_names(cls):
        return "vector configurations"

    def an_object(self):
        r"""The two simple roots of ``A2``, whose pairing graph has the swap."""
        from dzack_research.preamble.categories.lattices import Lattices

        root_lattice = Lattices(self.base_ring())("A2")
        return root_lattice.vector_configuration(
            finite_indexed_family_from_values(None, root_lattice.module_generators())
        )

    def super_categories(self):
        return [ModuleSubobjects(self.base_ring())]

    def spanning_automorphism_generators(self, lattice, vectors, colours):
        r"""Integral ambient isometries preserving a supplied coloured spanning family.

        Positions and colours are retained even when the family is redundant.
        The nondegenerate spanning hypothesis makes its pairing permutation
        action faithful. The rational configuration group ``G`` is the image of
        ``rho: Aut(Gamma) -> O(L tensor Q)``; when a generator of ``G`` does not
        preserve the integral lattice, take the stabilizer of ``L`` in ``G``.
        """
        realization = _SpanningConfiguration(lattice, vectors, colours)
        rational_group = realization.configuration_group()
        generators = rational_group.group_generators()
        if all(generator.integral_restriction(lattice, lattice) is not None for generator in generators):
            return finite_ordered_set(tuple(lattice.integral_isometry(generator) for generator in generators))
        # Indefinite.jl@374a5ebb/indef/lib/AutomorphismPolytope.g:366-412,
        # KernelLinPolytopeIntegral_Automorphism_Subspaces: represent the
        # rational configuration group on the generated lattice K, and
        # take the stabilizer of the ambient integral overlattice L.  The
        # generic IntegralStructureAction is the finite-residue realization
        # of the source's LinearSpace_Stabilizer (GroupAction.g:350-543).
        # Enumerating all graph permutations is NOT that source algorithm.
        from dzack_research.preamble.categories.rational_integral_stabilizers import IntegralStructureAction

        _exponent, containing = realization.containing_bound()
        stabilizer = IntegralStructureAction(rational_group, realization.rationalization()).with_stable_containing_bound(
            containing
        ).stabilizer()
        return finite_ordered_set(tuple(
            lattice.integral_isometry(generator)
            for generator in stabilizer.group_generators()
        ))

    def spanning_isometry(self, source, source_vectors, source_colours, target, target_vectors, target_colours):
        r"""One integral ambient isometry of two coloured spanning families, or None.

        A colour- and pairing-preserving bijection of the families is a
        labelled graph isomorphism, and because each family spans a
        nondegenerate space it extends to a unique rational isometry
        ``T0``. Every rational equivalence of the configurations is
        ``g T0`` for ``g`` in the rational configuration group ``G`` of the
        target. An integral one is a ``g`` carrying the lattice ``T0(L_1)``
        to ``L_2``: the transporter of the integral-structure action of
        ``G``, bounded by the ``G``-stable module ``K_2/e`` for ``K_2`` the
        span of the target family and ``e`` the exponent of ``L_2/K_2``.
        That exponent is an invariant of the equivalence, so differing
        exponents decide inequivalence. This is
        KernelLinPolytopeIntegral_Isomorphism_Subspaces
        (Indefinite.jl@374a5ebb/indef/lib/AutomorphismPolytope.g:288-339)
        with LinearSpace_Equivalence (GroupAction.g:793) realized by
        :meth:`IntegralStructureAction.transporter`; the graph group is
        never enumerated.
        """
        left = _SpanningConfiguration(source, source_vectors, source_colours)
        right = _SpanningConfiguration(target, target_vectors, target_colours)
        if left.cardinality() != right.cardinality() or source.rank() != target.rank():
            return None
        equivalence = left.rational_equivalence(right)
        if equivalence is None:
            return None
        integral = equivalence.integral_restriction(source, target)
        if integral is not None:
            return integral
        left_exponent, _left_containing = left.containing_bound()
        right_exponent, containing = right.containing_bound()
        if left_exponent != right_exponent:
            return None
        rational_source = left.rational_space()
        rational_target = right.rational_space()
        source_rationalization = left.rationalization()
        target_rationalization = right.rationalization()
        ambient_space = target_rationalization.codomain()
        moved = Modules(source.base_ring()).Mono(source, ambient_space)(
            lambda label: ambient_space.wrap(
                equivalence(source_rationalization(source.module_generator(label)).underlying_element())
            )
        )
        from dzack_research.preamble.categories.rational_integral_stabilizers import IntegralStructureAction

        transporter = IntegralStructureAction(right.configuration_group(), moved).with_stable_containing_bound(
            containing
        ).transporter(target_rationalization)
        if transporter is None:
            return None
        composite = rational_source.Isom(rational_target)(
            lambda label: transporter(equivalence(rational_source.module_generator(label)))
        )
        return target.integral_isometry(composite, source=source)

    class ParentMethods:
        def __init__(self, configuration_colouring, **rest) -> None:
            self._configuration_colouring = configuration_colouring
            super().__init__(**rest)

        def configuration_positions(self):
            r"""Return the ordered index set framing this configuration."""
            return self.module_generating_set()

        def configuration_indexing(self):
            r"""Return the bijection ``positions -> I`` onto the supplied family's index set.

            The configuration is framed through ``_lattice_subobject_on_basis``
            on the family's values in the order of ``I``'s enumeration, and that
            construction labels its framing by ``Sets.Δ[m-1]`` with the ``k``-th
            label sent to the ``k``-th value (``_module_subobject_constructor_data``
            in ``framed_free_modules.py``).  So the position of rank ``k`` is the
            index of rank ``k``: this map is the composite of the two ranking
            isomorphisms, stated here rather than assumed at each use.
            """
            positions = self.configuration_positions()
            indices = self._configuration_colouring.domain()
            to_index = indices.ranking_map().inverse()
            return Sets().Mor(positions, indices)(
                lambda position: to_index(positions.ranking_map()(position))
            )

        def configuration_colouring(self):
            r"""Return the colouring as the set map ``positions -> C``.

            The constructor received the caller's map ``I -> C`` out of the
            index set of the caller's family; this is that map composed with
            :meth:`configuration_indexing`.
            """
            return self._configuration_colouring * self.configuration_indexing()

        def preserves_colouring(self, position_map) -> bool:
            r"""Return whether a framing permutation carries each position to one of its colour."""
            colouring = self.configuration_colouring()
            return all(
                colouring(position) == colouring(position_map(position))
                for position in self.configuration_positions()
            )

        @cached_method
        def _pairing_adapter(self):
            r"""The declared engine adapter on this configuration's coloured pairings.

            Its data are the framing positions, the Gram tensor of the framed
            sublattice (the ambient form pulled back along the inclusion), and
            :meth:`configuration_colouring`; the engine graph stays inside it.
            """
            return _LabelledPairingGraph(
                self.configuration_positions(), self.gram_tensor(), self.configuration_colouring()
            )

        def configuration_automorphism_group(self, algorithm=None):
            r"""Return the group of framing permutations preserving every pairing and colour.

            An owned subgroup of the symmetric group on the positions; its
            elements act on :meth:`configuration_positions` through
            :meth:`position_permutation`.  ``algorithm`` is the engine's
            graph-canonization selector (``None``, ``"bliss"``, ``"sage"``).
            """
            return self._pairing_adapter().automorphism_group(algorithm)

        def position_permutation(self, automorphism):
            r"""Return the permutation of :meth:`configuration_positions` an automorphism induces."""
            return self._pairing_adapter().position_permutation(automorphism)

        @cached_method
        def _canonical_pairing_data(self, algorithm=None):
            r"""Return the canonical Gram matrix and the framing-position map to canonical positions."""
            adapter = self._pairing_adapter()
            canonical_basis = tuple(
                self.module_generator(position)
                for position in adapter.canonical_ordering(algorithm)
            )
            return self.gram_matrix(canonical_basis), adapter.canonical_position_map(algorithm)

        def canonical_pairing_matrix(self, algorithm=None):
            r"""Return the Gram matrix in the canonical pairing-graph order."""
            return self._canonical_pairing_data(algorithm)[0]

        def canonical_position_map(self, algorithm=None):
            r"""Return the framing-position map to canonical graph positions."""
            return self._canonical_pairing_data(algorithm)[1]

        def preserves_every_pairing(self, position_map) -> bool:
            r"""Return whether a framing permutation preserves the form: ``P^* b = b``.

            ``position_map`` is a map of :meth:`configuration_positions` to
            itself; those positions are the labels of this sublattice's module
            generators (its framing), so ``P`` is the endomorphism sending the
            generator at each position to the generator at its image.  The
            claim is the equality of the pulled-back Gram tensor with the Gram
            tensor (``OWN-24``).
            """
            permutation = Modules(self.base_ring()).Mor(self, self)(
                lambda label: self.module_generator(position_map(label))
            )
            gram = self.gram_tensor()
            return gram.pullback(permutation).is_equal_tensor(gram)

        def configuration_isometry(self, position_map):
            r"""Return the isometry of the framed sublattice permuting the framing.

            ``position_map`` sends each framing position to the position its
            vector is carried to.  The framing is a basis, so the assignment is
            a linear map; it is an isometry exactly because every pairing is
            preserved, which is asserted.
            """
            assert self.preserves_every_pairing(position_map), (
                f"{position_map} does not define an isometry of {self}: a permutation of "
                f"the basis vectors is an isometry only if it preserves every square and "
                f"every pairing, and this one does not"
            )
            assert self.preserves_colouring(position_map), (
                f"{position_map} is not an automorphism of the coloured configuration {self}: "
                f"it carries a position to one of a different colour"
            )
            return self.Aut()(
                {
                    label: self.module_generator(position_map(label))
                    for label in self.configuration_positions()
                }
            )

        def frames_its_lattice(self) -> bool:
            r"""Return whether the framing is a basis of the whole lattice."""
            lattice = self.inclusion().codomain()
            return bool(self.module_rank() == lattice.module_rank()) and self.is_primitive()

        def ambient_isometry(self, position_map):
            r"""Return the lifted element of ``O(L)`` when the framing bases ``L``.

            A permutation of a configuration spanning a proper sublattice
            defines an isometry of that sublattice only; whether it extends to
            the lattice is a question about the primitive extension, and no
            extension is attempted here.
            """
            lattice = self.inclusion().codomain()
            assert self.frames_its_lattice(), (
                f"cannot lift a permutation of {self} to an isometry of {lattice}: the "
                f"configuration is not a basis of {lattice}, only of a sublattice of rank "
                f"{self.module_rank()}, and whether its isometries extend to {lattice} is a "
                f"question about the primitive extension"
            )
            inclusion = self.inclusion()
            restricted = self.configuration_isometry(position_map)
            return lattice.Aut()(
                {
                    label: inclusion(
                        restricted(inclusion.lift(lattice.module_generator(label)))
                    )
                    for label in lattice.module_generating_set()
                }
            )

        def configuration_isometry_from_automorphism(self, automorphism):
            r"""Lift one configuration automorphism to an isometry of the framed sublattice.

            The automorphism acts on the framing positions by
            :meth:`position_permutation`; that map is lifted by
            :meth:`configuration_isometry`.
            """
            automorphisms = self.configuration_automorphism_group()
            assert automorphism in automorphisms, (
                f"cannot lift {automorphism} to an isometry of {self}: it is not an "
                f"element of the automorphism group {automorphisms} of the configuration"
            )
            position_map = self.position_permutation(automorphism)
            return self.configuration_isometry(position_map)

        def ambient_isometry_from_automorphism(self, automorphism):
            r"""Lift a graph automorphism to ``O(L)`` when the configuration frames ``L``."""
            automorphisms = self.configuration_automorphism_group()
            assert automorphism in automorphisms, (
                f"cannot lift {automorphism} to an isometry of the lattice framed by "
                f"{self}: it is not an element of the automorphism group {automorphisms} "
                f"of the configuration"
            )
            position_map = self.position_permutation(automorphism)
            return self.ambient_isometry(position_map)

        def diagram_automorphism_isometries(self):
            r"""Return the sublattice isometries lifted from every graph automorphism."""
            automorphisms = self.configuration_automorphism_group()
            return finite_ordered_set(
                tuple(
                    self.configuration_isometry_from_automorphism(automorphism)
                    for automorphism in automorphisms
                )
            )


class _LabelledPairingGraph:
    """Private adapter (OWN-06): the labelled pairing graph of a coloured framed family.

    Declared engine boundary, and the only site in this module holding a Sage
    ``Graph`` or integer vertex coordinates.  ``LabelledGraphs`` presents
    label-preserving ``Mor`` but no computed isomorphism or automorphism group
    (recorded in COMPLAINTS), so the bliss/nauty computations run here.

    Data: an owned finite ordered set of positions, the owned Gram tensor on
    the free module those positions frame, and the owned colouring map of the
    positions.  The tensor is lowered once (``_engine_component_matrix``);
    the positions are lowered by their ``ranking_map``.  Leaving the adapter:
    an owned subgroup of the symmetric group on the positions, the induced
    permutations of the positions as set maps, isomorphisms as set maps of
    positions, and the canonical labelling as a set map onto canonical
    positions.
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
    def automorphism_group(self, algorithm=None):
        r"""``Aut(Gamma)``: the subgroup of ``S_m`` generated by the engine's automorphisms."""
        symmetric = self._symmetric_group()
        size = self._size()
        engine = self._graph().automorphism_group(edge_labels=True, algorithm=algorithm)
        return symmetric.subgroup(tuple(
            symmetric([int(generator(vertex)) + 1 for vertex in range(size)])
            for generator in engine.gens()
        ))

    def position_permutation(self, automorphism):
        r"""The permutation of the positions induced by an element of ``Aut(Gamma)``."""
        return Sets().Mor(self._positions, self._positions)(
            lambda position: self._position(int(automorphism(self._vertex(position) + 1)) - 1)
        )

    def isomorphism(self, other):
        r"""A colour- and pairing-preserving bijection of positions onto ``other``'s, or ``None``."""
        equivalent, certificate = self._graph().is_isomorphic(
            other._graph(), edge_labels=True, certificate=True
        )
        if not equivalent:
            return None
        return Sets().Mor(self._positions, other._positions)(
            lambda position: other._position(certificate[self._vertex(position)])
        )

    @cached_method
    def _certificate(self, algorithm=None):
        _canonical, certificate = self._graph().canonical_label(
            edge_labels=True, certificate=True, algorithm=algorithm
        )
        return certificate

    @cached_method
    def canonical_positions(self):
        r"""The canonical positions, the ordinal ``{0, ..., m-1}`` as an owned ordered set."""
        return finite_ordered_set(range(self._size()))

    def canonical_position_map(self, algorithm=None):
        r"""The canonical labelling as the set map ``positions -> canonical positions``."""
        certificate = self._certificate(algorithm)
        canonical = self.canonical_positions()
        return Sets().Mor(self._positions, canonical)(
            lambda position: canonical.ranking_map().inverse()(int(certificate[self._vertex(position)]))
        )

    def canonical_ordering(self, algorithm=None):
        r"""The positions as an ordered set in canonical order."""
        certificate = self._certificate(algorithm)
        by_canonical = {int(certificate[vertex]): vertex for vertex in range(self._size())}
        return finite_ordered_set(tuple(
            self._position(by_canonical[rank]) for rank in range(self._size())
        ))


class _SpanningConfiguration:
    """Private realization of a coloured spanning family ``(v_i)_{i in I}`` of ``L``.

    Holds the supplied vectors and colours as private data and the integral
    family morphism ``F(I) -> L``.  Its graph computations go through the
    declared adapter :class:`_LabelledPairingGraph` on the Gram tensor pulled
    back along that morphism; every value leaving this class is a preamble
    object: the rational family morphism, the rational equivalence
    ``T_sigma``, the configuration group ``rho(Aut(Gamma)) <= O(L tensor Q)``,
    the stable bound, and the number of positions as a cardinal.

    Nothing is computed or checked at construction (``OWN-22``); the
    nondegenerate spanning hypothesis is asserted by the computations that
    use it.
    """

    def __init__(self, lattice, vectors, colours):
        self._lattice = lattice
        self._vectors = tuple(lattice(point) for point in vectors)
        self._colouring = finite_indexed_family_from_values(None, colours)

    @cached_method
    def _positions_module(self):
        return Modules(self._lattice.base_ring()).free_module(self._colouring.cardinality())

    @cached_method
    def family(self):
        r"""The integral family morphism ``F(I) -> L``."""
        positions = self._positions_module()
        labels = positions.module_generating_set()
        return Modules(self._lattice.base_ring()).Mor(positions, self._lattice)(
            lambda label: self._vectors[int(labels.ranking_map()(label))]
        )

    def cardinality(self):
        r"""The number of positions, as a cardinal."""
        return self._colouring.cardinality()

    def _assert_spanning_nondegenerate(self):
        lattice = self._lattice
        assert lattice.base_ring() is _own_ring(SageZZ), (
            f"integral configuration isometries are computed for lattices over ZZ, but {lattice} "
            f"is over {lattice.base_ring()}"
        )
        assert lattice.is_nondegenerate() is True, (
            f"the pairing permutation action of a configuration in {lattice} is faithful only "
            f"when the lattice is nondegenerate, and {lattice} is not known to be"
        )
        assert lattice.subobject_on(self._vectors).module_rank() == lattice.rank(), (
            f"the configuration {self._vectors} does not span {lattice}, so its pairings do not "
            f"determine a rational isometry"
        )

    @cached_method
    def _pairing_adapter(self):
        self._assert_spanning_nondegenerate()
        positions = self._positions_module()
        labels = positions.module_generating_set()
        indices = self._colouring.index_set().ranking_map().inverse()

        def colouring(label):
            return self._colouring.value(indices(int(labels.ranking_map()(label))))

        return _LabelledPairingGraph(labels, self._lattice.gram_tensor().pullback(self.family()), colouring)

    def rationalization(self):
        r"""The lattice in its rational space, ``L -> Res(L tensor Q)``."""
        return ModulesOverIntegralDomains(self._lattice.base_ring())(self._lattice).generic_fibre_map()

    def rational_space(self):
        return self._lattice.base_change(self._lattice.base_ring().fraction_field_map())

    @cached_method
    def rational_family(self):
        r"""The family as the rational module morphism ``F_Q(I) -> L tensor Q``, surjective by spanning.

        Its positions are those of :meth:`family` under the rank bijection of
        the two free modules' framings.
        """
        rational = self.rational_space()
        rationalization = self.rationalization()
        integral = self.family()
        positions = Modules(rational.base_ring()).free_module(self._colouring.cardinality())
        to_integral = self._rational_to_integral_labels(positions)
        return Modules(rational.base_ring()).Mor(positions, rational)(
            lambda label: rationalization(
                integral(integral.domain().module_generator(to_integral(label)))
            ).underlying_element()
        )

    def _rational_to_integral_labels(self, rational_positions):
        r"""The rank bijection of ``F_Q(I)``'s framing onto ``F(I)``'s."""
        rational_labels = rational_positions.module_generating_set()
        integral_labels = self._positions_module().module_generating_set()
        return Sets().Mor(rational_labels, integral_labels)(
            lambda label: integral_labels.ranking_map().inverse()(rational_labels.ranking_map()(label))
        )

    def _rational_transformation(self, target, sigma):
        r"""The rational isometry ``T_sigma`` with ``T_sigma(v_i) = w_{sigma(i)}``.

        ``sigma`` is a set map of :meth:`family` positions onto ``target``'s.
        For a pairing-preserving bijection of nondegenerate spanning families
        ``T_sigma`` exists and is unique.  It is computed at the module owner:
        a vector is lifted along the surjective family morphism (exact
        solving), its coefficients are moved by ``sigma``, and the target
        family morphism is applied.
        """
        source_family = self.rational_family()
        target_family = target.rational_family()
        source_positions = source_family.domain()
        target_positions = target_family.domain()
        to_integral = self._rational_to_integral_labels(source_positions)
        target_to_integral = target._rational_to_integral_labels(target_positions)
        target_labels = target_positions.module_generating_set()
        target_integral_labels = target._positions_module().module_generating_set()

        def target_label(integral_label):
            return target_labels.ranking_map().inverse()(target_integral_labels.ranking_map()(integral_label))

        relabel = Modules(source_positions.base_ring()).Mor(source_positions, target_positions)(
            lambda label: target_positions.module_generator(target_label(sigma(to_integral(label))))
        )
        rational_target = target.rational_space()
        section = self._family_section()
        rational_source = self.rational_space()
        return rational_source.Isom(rational_target)(
            lambda label: target_family(relabel(section(rational_source.module_generator(label))))
        )

    @cached_method
    def _family_section(self):
        r"""A section ``L tensor Q -> F_Q(I)`` of the surjective rational family, solved once on the framing.

        It depends only on this configuration, so every ``T_sigma`` composes
        with the same section instead of solving again for each ``sigma``.
        """
        source_family = self.rational_family()
        rational_source = self.rational_space()
        return Modules(rational_source.base_ring()).Mor(rational_source, source_family.domain())({
            label: source_family.lift(rational_source.module_generator(label))
            for label in rational_source.module_generating_set()
        })

    def rational_equivalence(self, target):
        r"""One rational isometry carrying this coloured family onto ``target``'s, or ``None``."""
        sigma = self._pairing_adapter().isomorphism(target._pairing_adapter())
        if sigma is None:
            return None
        return self._rational_transformation(target, sigma)

    @cached_method
    def configuration_group(self):
        r"""``G = rho(Aut(Gamma))`` for the group morphism ``rho: Aut(Gamma) -> O(L tensor Q)``.

        ``Aut(Gamma)`` is the adapter's owned subgroup of the symmetric group
        on the positions; ``rho`` is constructed from the images of its
        group generators, each the rational isometry realizing the induced
        permutation of positions, and ``G`` is its image.
        """
        adapter = self._pairing_adapter()
        rational = self.rational_space()
        automorphisms = adapter.automorphism_group()
        orthogonal = rational.O()
        def realization(generator):
            isometry = self._rational_transformation(self, adapter.position_permutation(generator))
            return orthogonal({
                label: isometry(rational.module_generator(label))
                for label in rational.module_generating_set()
            })

        rho = automorphisms.Mor(orthogonal)({
            generator: realization(generator) for generator in automorphisms.group_generators()
        })
        return rho.image()

    def containing_bound(self):
        r"""The exponent ``e`` of ``L/K`` and the stable module ``K/e`` containing ``L``.

        ``K`` is the span of the family. The configuration group permutes
        the family, so ``K`` and ``K/e`` are stable, and ``eL`` lies in ``K``.
        """
        lattice = self._lattice
        generated = lattice.subobject_on(self._vectors)
        exponent = generated.inclusion().cokernel().exponent()
        assert exponent > lattice.base_ring().zero(), (
            f"the configuration {self._vectors} spans a sublattice of infinite index in {lattice}, "
            f"so no finite stable module contains {lattice}"
        )
        rationalization = self.rationalization()
        ambient_space = rationalization.codomain()
        rational = self.rational_space()
        rational_ring = rational.base_ring()
        scale = rational_ring.one() / rational_ring(exponent)
        containing = Modules(lattice.base_ring()).Mono(generated, ambient_space)(
            lambda label: ambient_space.wrap(rational.scalar_multiple(
                scale,
                rationalization(generated.inclusion()(generated.module_generator(label))).underlying_element(),
            ))
        )
        return exponent, containing


__all__ = ["VectorConfigurations"]
