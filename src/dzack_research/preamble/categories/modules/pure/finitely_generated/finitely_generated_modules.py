"""Finitely generated modules."""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing


class FinitelyGeneratedModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "finitely generated modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_finitely_generated(self) -> bool:
            return True

        @cached_method
        def fiber(self, point):
            r"""Return ``M(p)=M tensor_R kappa(p)`` at ``p in Spec(R)``."""
            ring = self.base_ring()
            if point.parent().ring() is not ring:
                raise ValueError("a module fiber requires a point of Spec(base_ring)")
            localized = self.localize_at_prime(point)
            try:
                base_change = localized.base_change
            except AttributeError as error:
                raise NotImplementedError(
                    f"scalar extension of {localized} to its residue field is not materialized"
                ) from error
            fiber = base_change(point.local_ring().residue_map())
            residue = point.residue_field()
            from dzack_research.preamble.categories.modules.pure.modules import VectorSpaces
            from dzack_research.preamble.refine import refine

            fiber._preamble_fiber_point = point
            fiber._preamble_fiber_localization = localized
            return refine(fiber, VectorSpaces(residue))

        def fiber_dimension(self, point):
            r"""Return ``dim_{kappa(p)} M(p)`` when the finite fiber is represented."""
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
                FinitelyGeneratedFreeModules,
            )

            if self in FinitelyGeneratedFreeModules(self.base_ring()):
                return self.rank()

            presentation_matrix = getattr(self, "presentation_matrix", None)
            number_of_generators = getattr(self, "number_of_module_generators", None)
            if presentation_matrix is not None and number_of_generators is not None:
                from sage.matrix.constructor import matrix
                from sage.rings.integer_ring import ZZ as SageZZ

                from dzack_research.preamble.categories.rings import engine_ring

                localized = self.localize_at_prime(point)
                relation_tensor = localized.presentation_matrix()
                relation_rows = tuple(relation_tensor.rows())
                residue = point.residue_field()
                residue_engine = engine_ring(residue)
                residue_map = point.local_ring().residue_map()
                specialized = matrix(
                    residue_engine,
                    len(relation_rows),
                    int(number_of_generators()),
                    [
                        residue_engine(residue_map(coefficient))
                        for row in relation_rows
                        for coefficient in row
                    ],
                )
                return SageZZ(int(number_of_generators()) - specialized.rank())
            fiber = self.fiber(point)
            rank = getattr(fiber, "rank", None)
            if rank is not None:
                return rank()
            dimension = getattr(fiber, "dimension", None)
            if dimension is not None:
                return dimension()
            raise NotImplementedError(
                f"the dimension of the represented fiber {fiber} is not computable"
            )

        def rank_at(self, point):
            r"""Return the local fiber rank ``dim_{kappa(p)} M(p)``."""
            return self.fiber_dimension(point)

        def local_number_of_generators(self, point):
            r"""Return the minimal number of generators of ``M_p`` by Nakayama."""
            return self.localize_at_prime(point).minimal_number_of_generators()

        def local_minimal_generators(self, point):
            r"""Return a selected minimal generating set of ``M_p`` when represented."""
            return self.localize_at_prime(point).minimal_module_generators()

        def residue_module(self):
            r"""Return ``M/mM = M tensor_R k`` for a represented local base ring."""
            from dzack_research.preamble.categories.rings import LocalRings

            ring = self.base_ring()
            if ring not in LocalRings():
                raise TypeError("the residue module is defined here for modules over a local ring")
            try:
                base_change = self.base_change
            except AttributeError as error:
                raise NotImplementedError(
                    f"residue-field scalar extension of {self} is not materialized"
                ) from error
            return base_change(ring.residue_map())

        def minimal_number_of_generators(self):
            r"""Return ``dim_k(M/mM)`` for a finite module over a local ring."""
            from dzack_research.preamble.categories.rings import LocalRings, engine_ring

            ring = self.base_ring()
            if ring not in LocalRings():
                raise TypeError(
                    "minimal generator counts via Nakayama require a represented local base ring"
                )
            presentation_matrix = getattr(self, "presentation_matrix", None)
            number_of_generators = getattr(self, "number_of_module_generators", None)
            if presentation_matrix is not None and number_of_generators is not None:
                from sage.matrix.constructor import matrix
                from sage.rings.integer_ring import ZZ as SageZZ

                relation_tensor = presentation_matrix()
                relation_rows = tuple(relation_tensor.rows())
                residue = ring.residue_field()
                residue_engine = engine_ring(residue)
                residue_map = ring.residue_map()
                specialized = matrix(
                    residue_engine,
                    len(relation_rows),
                    int(number_of_generators()),
                    [
                        residue_engine(residue_map(coefficient))
                        for row in relation_rows
                        for coefficient in row
                    ],
                )
                return SageZZ(int(number_of_generators()) - specialized.rank())

            residue_module = self.residue_module()
            dimension = getattr(residue_module, "dimension", None)
            if dimension is not None:
                return dimension()
            rank = getattr(residue_module, "rank", None)
            if rank is not None:
                return rank()
            raise NotImplementedError(
                f"the residue-vector-space dimension of {self} is not represented"
            )

        def generic_rank(self):
            r"""Return ``dim_K(M tensor_R K)`` for an integral-domain base ``R``."""
            from dzack_research.preamble.categories.rings import IntegralDomains

            ring = self.base_ring()
            if ring not in IntegralDomains():
                raise TypeError("generic rank is defined here over an integral domain")
            return self.fiber_dimension(ring.spectrum().generic_point())

        def free_resolution(self):
            from dzack_research.preamble.categories.modules.free_resolutions import free_resolution

            return free_resolution(self)
