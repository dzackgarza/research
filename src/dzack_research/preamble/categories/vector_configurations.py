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
same one is what CoxIter and polyhedral_common use for the automorphism group
of a Coxeter polytope's facet configuration.

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

from dzack_research.preamble.categories.modules.pure.modules import ModuleSubobjects
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)


class VectorConfigurations(OwnedCategoryOverBaseRing):
    r"""Sublattices with a chosen ordered framing, regarded as vector configurations.

    Membership adds no property to the sublattice: it selects the framing as
    the datum the operations below consume, which is what distinguishes a
    configuration from the sublattice it spans.
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

    class ParentMethods:
        def configuration_positions(self):
            r"""Return the ordered index set framing this configuration."""
            return self.module_generating_set()

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
            size = int(positions.cardinality())
            graph = Graph(loops=True, multiedges=False)
            graph.add_vertices(range(1, size + 1))
            for left in range(size):
                left_vector = vectors[positions[left]]
                graph.add_edge(left + 1, left + 1, int(lattice.q(left_vector)))
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
            r"""Return whether a framing permutation preserves all squares and pairings."""
            lattice = self.inclusion().codomain()
            vectors = self.embedded_module_generators()
            positions = self.configuration_positions()
            return all(
                lattice.b(vectors[left], vectors[right])
                == lattice.b(vectors[position_map(left)], vectors[position_map(right)])
                for left in positions
                for right in positions
            )

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
            if getattr(automorphism, "parent", lambda: None)() is not automorphisms:
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
            if getattr(automorphism, "parent", lambda: None)() is not automorphisms:
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


__all__ = ["VectorConfigurations"]
