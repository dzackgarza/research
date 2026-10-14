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
    finite_indexed_family,
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
        return root_lattice.vector_configuration(root_lattice.module_generators())

    def super_categories(self):
        return [ModuleSubobjects(self.base_ring())]

    def spanning_automorphism_generators(self, lattice, vectors, colours):
        r"""Integral ambient isometries preserving a supplied coloured spanning family.

        Positions and colours are retained even when the family is redundant.
        The nondegenerate spanning hypothesis makes its pairing permutation
        action faithful. A graph generator need not preserve the ambient
        integral lattice; in that case take the subgroup of integral lifts.
        """
        realization = _SpanningConfiguration(lattice, vectors, colours)
        group = realization.graph.automorphism_group(edge_labels=True)
        generators = tuple(realization.lift(realization, permutation) for permutation in group.gens())
        if all(generator is not None for generator in generators):
            return finite_ordered_set(generators)
        # Indefinite.jl@374a5ebb/indef/lib/AutomorphismPolytope.g:366-412,
        # KernelLinPolytopeIntegral_Automorphism_Subspaces: represent the
        # rational configuration group on the generated row lattice K, and
        # take the stabilizer of the ambient integral overlattice L.  The
        # generic IntegralStructureAction is the finite-residue realization
        # of the source's LinearSpace_Stabilizer (GroupAction.g:350-543).
        # Enumerating all graph permutations is NOT that source algorithm.
        from dzack_research.preamble.categories.rational_integral_stabilizers import IntegralStructureAction

        rational_group = realization.rational_configuration_group(group)
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
        if len(left.vectors) != len(right.vectors) or source.rank() != target.rank():
            return None
        equivalent, certificate = left.graph.is_isomorphic(right.graph, edge_labels=True, certificate=True)
        if not equivalent:
            return None
        lifted = left.lift(right, certificate.__getitem__)
        if lifted is not None:
            return lifted
        left_exponent, _left_containing = left.containing_bound()
        right_exponent, containing = right.containing_bound()
        if left_exponent != right_exponent:
            return None
        rational_source = left.rational_space()
        rational_target = right.rational_space()
        equivalence = left.rational_transformation(right, certificate.__getitem__)
        source_rationalization = left.rationalization()
        target_rationalization = right.rationalization()
        ambient_space = target_rationalization.codomain()
        moved = Modules(source.base_ring()).Mono(source, ambient_space)(
            lambda label: ambient_space.wrap(
                equivalence(source_rationalization(source.module_generator(label)).underlying_element())
            )
        )
        from dzack_research.preamble.categories.rational_integral_stabilizers import IntegralStructureAction

        rational_group = right.rational_configuration_group(right.graph.automorphism_group(edge_labels=True))
        transporter = IntegralStructureAction(rational_group, moved).with_stable_containing_bound(
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

        def configuration_colouring(self):
            r"""Return the colouring as the set map ``positions -> C``.

            The constructor received a map ``I -> C`` out of the index set of
            the supplied family; the positions correspond to ``I`` in order, so
            this is that map composed with the order isomorphism
            ``positions -> I`` of the two ranking maps.
            """
            supplied = self._configuration_colouring
            positions = self.configuration_positions()
            indices = supplied.domain()
            to_index = indices.ranking_map().inverse()
            return Sets().Mor(positions, supplied.codomain())(
                lambda position: supplied(to_index(positions.ranking_map()(position)))
            )

        def preserves_colouring(self, position_map) -> bool:
            r"""Return whether a framing permutation carries each position to one of its colour."""
            colouring = self.configuration_colouring()
            return all(
                colouring(position) == colouring(position_map(position))
                for position in self.configuration_positions()
            )

        def _pairing_graph(self):
            r"""Return the private labelled graph encoding every pairing.

            Vertices run over ``1..m`` as Sage's permutation groups do.  A loop
            carries a vector's square and an edge carries a nonzero pairing; a
            missing edge is the pairing zero, which a labelled automorphism
            preserves as well.
            """
            lattice = self.inclusion().codomain()
            positions = self.configuration_positions()
            vectors = self.embedded_module_generators()
            colouring = self.configuration_colouring()
            size = int(positions.cardinality())
            graph = Graph(loops=True, multiedges=False)
            graph.add_vertices(range(1, size + 1))
            for left in range(size):
                left_vector = vectors[positions[left]]
                graph.add_edge(left + 1, left + 1, (colouring(positions[left]), int(lattice.q(left_vector))))
                for right in range(left + 1, size):
                    pairing = int(
                        lattice.b(left_vector, vectors[positions[right]])
                    )
                    if pairing:
                        graph.add_edge(left + 1, right + 1, pairing)
            return graph

        @cached_method
        def configuration_automorphism_group(self, algorithm=None):
            r"""Return framing permutations preserving every pairing.

            ``algorithm`` is the graph-canonization algorithm selector
            accepted by Sage (notably ``None``, ``"bliss"`` and ``"sage"``).
            The returned object is still the owned permutation group.
            """
            from dzack_research.preamble.categories.group.groups import _owned_group

            return _owned_group(
                self._pairing_graph().automorphism_group(
                    edge_labels=True,
                    algorithm=algorithm,
                )
            )

        @cached_method
        def _canonical_pairing_data(self, algorithm=None):
            r"""Return the canonical Gram matrix and framing-position certificate."""
            _canonical_graph, certificate = self._pairing_graph().canonical_label(
                edge_labels=True,
                certificate=True,
                algorithm=algorithm,
            )
            positions = self.configuration_positions()
            size = int(positions.cardinality())
            canonical_to_source = [None] * size
            for source_position in range(size):
                canonical_position = int(certificate[source_position + 1])
                canonical_to_source[canonical_position] = positions[source_position]
            if any(position is None for position in canonical_to_source):
                raise ArithmeticError(
                    f"the canonical labelling of the pairing graph of {self} is not a "
                    f"permutation of its {size} basis positions: the certificate is {certificate}"
                )

            canonical_basis = tuple(
                self.module_generator(position)
                for position in canonical_to_source
            )
            canonical_matrix = self.gram_matrix(canonical_basis)
            canonical_positions = finite_ordered_set(range(size))
            certificate_family = finite_indexed_family(
                positions,
                lambda position: canonical_positions[
                    int(certificate[int(positions.ranking_map()(position)) + 1])
                ],
                name="Canonical positions of the vector configuration",
            )
            return canonical_matrix, certificate_family

        def canonical_pairing_matrix(self, algorithm=None):
            r"""Return the Gram matrix in the canonical pairing-graph order."""
            return self._canonical_pairing_data(algorithm)[0]

        def canonical_position_map(self, algorithm=None):
            r"""Return the framing-position map to canonical graph positions."""
            return self._canonical_pairing_data(algorithm)[1]

        def preserves_every_pairing(self, position_map) -> bool:
            r"""Return whether a framing permutation preserves the form: ``P^* b = b``.

            ``P`` is the endomorphism of the framed sublattice moving each
            framing vector to its image position; the claim is the equality of
            the pulled-back Gram tensor with the Gram tensor (``OWN-24``).
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
            r"""Lift one owned pairing-graph automorphism through libGAP.

            The graph automorphism group is an owned permutation group.  Its
            private permutation representation crosses into GAP only long enough to evaluate
            the action on the canonical point set ``1..m``; the resulting map
            on the configuration's own framing positions is then lifted by
            :meth:`configuration_isometry`, which verifies every pairing.
            """
            automorphisms = self.configuration_automorphism_group()
            if automorphism not in automorphisms:
                raise ValueError(
                    f"cannot lift {automorphism} to an isometry of {self}: it is not an "
                    f"element of the automorphism group {automorphisms} of the configuration"
                )
            positions = self.configuration_positions()
            def position_map(label):
                source = int(positions.ranking_map()(label)) + 1
                target = int(automorphism(source))
                return positions[target - 1]

            return self.configuration_isometry(position_map)

        def ambient_isometry_from_automorphism(self, automorphism):
            r"""Lift a graph automorphism to ``O(L)`` when the configuration frames ``L``."""
            automorphisms = self.configuration_automorphism_group()
            if automorphism not in automorphisms:
                raise ValueError(
                    f"cannot lift {automorphism} to an isometry of the lattice framed by "
                    f"{self}: it is not an element of the automorphism group {automorphisms} "
                    f"of the configuration"
                )
            positions = self.configuration_positions()
            def position_map(label):
                source = int(positions.ranking_map()(label)) + 1
                target = int(automorphism(source))
                return positions[target - 1]

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


class _SpanningConfiguration:
    """Private adapter (OWN-06): a coloured spanning family and its labelled pairing graph.

    Declared engine boundary: the labelled pairing graph is a Sage ``Graph``
    used only for its isomorphism and automorphism computations (bliss/nauty),
    because ``LabelledGraphs`` presents label-preserving ``Mor`` but no
    computed isomorphism or automorphism group (recorded in COMPLAINTS).
    Everything that leaves this adapter is a preamble object: the family is
    the module morphism ``F(I) -> L`` from the free module on the positions,
    its pairings are the pullback of the Gram tensor along it, a rational
    equivalence is found by exact solving at the module owner (``lift`` of
    the rational family morphism), and the configuration group is the image
    of a constructed group morphism ``Aut(Gamma) -> O(L tensor Q)``.
    """

    def __init__(self, lattice, vectors, colours):
        if lattice.base_ring() is not _own_ring(SageZZ):
            raise TypeError("integral ambient configuration isometries require a lattice over ZZ")
        self.lattice = lattice
        self.vectors = tuple(lattice(point) for point in vectors)
        # The colouring is the family positions -> colours, read at its owner;
        # its values are serialized once here as the graph's vertex labels.
        colouring = finite_indexed_family_from_values(None, colours)
        colours = tuple(colouring)
        if len(colours) != len(self.vectors):
            raise ValueError("each configuration position requires one colour")
        if not lattice.is_nondegenerate():
            raise ValueError("the finite pairing action requires a nondegenerate ambient lattice")
        if lattice.subobject_on(self.vectors).module_rank() != lattice.rank():
            raise ValueError("the finite pairing action requires a spanning configuration")
        integral_positions = Modules(lattice.base_ring()).free_module(len(self.vectors))
        self.positions = tuple(integral_positions.module_generating_set())
        family = Modules(lattice.base_ring()).Mor(integral_positions, lattice)(
            lambda label: self.vectors[self.positions.index(label)]
        )
        pairings = lattice.gram_tensor().pullback(family)
        self.graph = Graph(loops=True, multiedges=False)
        self.graph.add_vertices(range(len(self.vectors)))
        for left in range(len(self.vectors)):
            self.graph.add_edge(left, left, ("vertex", colours[left], int(pairings[left, left])))
            for right in range(left):
                self.graph.add_edge(left, right, ("pairing", int(pairings[left, right])))

    def rationalization(self):
        r"""The lattice in its rational space, ``L -> Res(L tensor Q)``."""
        return ModulesOverIntegralDomains(self.lattice.base_ring())(self.lattice).generic_fibre_map()

    def rational_space(self):
        return self.lattice.base_change(self.lattice.base_ring().fraction_field_map())

    @cached_method
    def rational_family(self):
        r"""The family as the rational module morphism ``F_Q(I) -> L tensor Q``, surjective by spanning."""
        rational = self.rational_space()
        rationalization = self.rationalization()
        positions = Modules(rational.base_ring()).free_module(len(self.vectors))
        return Modules(rational.base_ring()).Mor(positions, rational)(
            lambda label: rationalization(
                self.vectors[tuple(positions.module_generating_set()).index(label)]
            ).underlying_element()
        )

    def rational_transformation(self, target, permutation):
        r"""The rational isometry ``T_sigma`` with ``T_sigma(v_i) = w_{sigma(i)}``.

        For a pairing-preserving bijection of nondegenerate spanning families
        ``T_sigma`` exists and is unique.  It is computed at the module owner:
        a vector ``x`` is lifted along the surjective family morphism
        ``F_Q(I) -> L_1 tensor Q`` (exact solving), its coefficients are
        moved by ``sigma``, and the target family morphism is applied.
        """
        source_family = self.rational_family()
        target_family = target.rational_family()
        source_positions = source_family.domain()
        target_positions = target_family.domain()
        source_labels = tuple(source_positions.module_generating_set())
        target_labels = tuple(target_positions.module_generating_set())
        relabel = Modules(source_positions.base_ring()).Mor(source_positions, target_positions)(
            lambda label: target_positions.module_generator(
                target_labels[int(permutation(source_labels.index(label)))]
            )
        )
        rational_source = self.rational_space()
        rational_target = target.rational_space()
        return rational_source.Isom(rational_target)(
            lambda label: target_family(relabel(source_family.lift(rational_source.module_generator(label))))
        )

    def rational_configuration_group(self, permutation_group):
        r"""``G = rho(Aut(Gamma))`` for the group morphism ``rho: Aut(Gamma) -> O(L tensor Q)``.

        ``rho`` is constructed from generator images, each the rational
        isometry realizing a generating graph automorphism; ``G`` is its image.
        """
        from dzack_research.preamble.categories.group.groups import _own_group

        rational = self.rational_space()
        automorphisms = _own_group(permutation_group)
        orthogonal = rational.O()
        images = {}
        for permutation in permutation_group.gens():
            isometry = self.rational_transformation(self, permutation)
            images[automorphisms._from_engine(permutation)] = orthogonal(
                {label: isometry(rational.module_generator(label)) for label in rational.module_generating_set()}
            )
        rho = automorphisms.Mor(orthogonal)(images)
        return rho.image()

    def containing_bound(self):
        r"""The exponent ``e`` of ``L/K`` and the stable module ``K/e`` containing ``L``.

        ``K`` is the span of the family. The configuration group permutes
        the family, so ``K`` and ``K/e`` are stable, and ``eL`` lies in ``K``.
        """
        lattice = self.lattice
        generated = lattice.subobject_on(self.vectors)
        exponent = generated.inclusion().cokernel().exponent()
        if exponent <= lattice.base_ring().zero():
            raise ArithmeticError("a spanning vector configuration must generate a finite-index integral sublattice")
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

    def lift(self, target, permutation):
        r"""The integral isometry ``L_1 -> L_2`` restricting ``T_sigma``, or ``None`` when it is not integral."""
        return self.rational_transformation(target, permutation).integral_restriction(self.lattice, target.lattice)


__all__ = ["VectorConfigurations"]
