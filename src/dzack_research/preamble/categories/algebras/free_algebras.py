"""Free symmetric, tensor, alternating, and divided-power algebra categories."""

from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing


class FreeAlgebras(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "free algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        return [Algebras(self.base_ring())]

    class ParentMethods:
        def is_free(self) -> bool:
            return True


class GradedFreeAlgebras(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "graded free algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.graded_algebras import (
            GradedAlgebras,
        )

        return [FreeAlgebras(self.base_ring()), GradedAlgebras(self.base_ring())]

    class ParentMethods:
        def graded_piece(self, degree):
            r"""Return the canonical degree piece of this free construction.

            The flavor, not this common superclass, determines the degree
            piece: ``T^n(M)``, ``Sym^n(M)``, ``Lambda^n(M)``, or
            ``Gamma^n(M)``.  This is one construction path -- the algebra does
            not build a second model of those modules.
            """
            degree = int(degree)
            if degree < 0:
                raise ValueError("a graded degree is nonnegative")

            try:
                source = self.free_source_module()
            except (AttributeError, ValueError):
                from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                    FreeModuleOn,
                )

                source = FreeModuleOn(
                    self.algebra_base_ring(),
                    self.algebra_generating_set(),
                )

            ring = self.algebra_base_ring()
            # These free constructions are connected: their canonical
            # degree-zero algebra and module is the scalar ring itself.
            if degree == 0:
                # The represented exterior/divided-power carriers are assembled
                # from their authoritative module-power pieces.  Their concrete
                # degree-zero piece is therefore the existing degree-zero power
                # module; do not let this generic free-algebra method replace it.
                if self in AlternatingAlgebras(ring):
                    from dzack_research.preamble.categories.modules.powers import (
                        AlternatingPower,
                    )

                    return AlternatingPower(source, 0)
                if self in DividedPowerAlgebras(ring):
                    from dzack_research.preamble.categories.modules.powers import (
                        DividedPower,
                    )

                    return DividedPower(source, 0)
                return ring
            from dzack_research.preamble.categories.modules.powers import (
                AlternatingPower,
                DividedPower,
                SymmetricPower,
                TensorPower,
            )

            if self in TensorAlgebras(ring):
                return TensorPower(source, degree)
            if self in SymmetricAlgebras(ring):
                return SymmetricPower(source, degree)
            if self in AlternatingAlgebras(ring):
                return AlternatingPower(source, degree)
            if self in DividedPowerAlgebras(ring):
                return DividedPower(source, degree)
            raise TypeError(
                f"the graded free-algebra flavor of {self} is not represented"
            )


class TensorAlgebras(OwnedCategoryOverBaseRing):
    r"""Tensor algebras of represented modules."""

    @classmethod
    def _repr_object_names(cls):
        return "tensor algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.graded_algebras import (
            GradedAlgebras,
        )

        return [GradedAlgebras(self.base_ring())]

    class ParentMethods:
        def free_source_module(self):
            r"""Return the module whose tensor algebra this object represents."""
            return self._preamble_free_algebra_source_module


class SymmetricAlgebras(OwnedCategoryOverBaseRing):
    r"""Symmetric algebras of represented modules."""

    @classmethod
    def _repr_object_names(cls):
        return "symmetric algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.algebras import (
            CommutativeAlgebras,
        )
        from dzack_research.preamble.categories.algebras.graded_algebras import (
            GradedAlgebras,
        )

        return [
            GradedAlgebras(self.base_ring()),
            CommutativeAlgebras(self.base_ring()),
        ]

    class ParentMethods:
        def free_source_module(self):
            r"""Return the module whose symmetric algebra this object represents."""
            return self._preamble_free_algebra_source_module


class AlternatingAlgebras(OwnedCategoryOverBaseRing):
    r"""Exterior/alternating algebras."""

    @classmethod
    def _repr_object_names(cls):
        return "alternating algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.graded_commutative_algebras import (
            StrictlyGradedCommutativeAlgebras,
        )

        return [StrictlyGradedCommutativeAlgebras(self.base_ring())]

    class ParentMethods:
        def free_source_module(self):
            return self._preamble_free_algebra_source_module

        def graded_piece(self, degree):
            from dzack_research.preamble.categories.modules.powers import (
                AlternatingPower,
            )

            return AlternatingPower(self.free_source_module(), degree)

        def scalar_multiple(self, scalar, element):
            return self._power_algebra_scalar_multiple(scalar, element)

        def _Hom_(self, codomain, category=None):
            if codomain in AlternatingAlgebras(self.algebra_base_ring()):
                from dzack_research.preamble.categories.algebras.power_algebras import (
                    power_algebra_homset,
                )

                return power_algebra_homset(self, codomain)
            return super()._Hom_(codomain, category=category)

        def hom(self, images, codomain=None):
            if codomain is not None and codomain in AlternatingAlgebras(
                self.algebra_base_ring()
            ):
                from dzack_research.preamble.categories.algebras.power_algebras import (
                    power_algebra_homset,
                )

                return power_algebra_homset(self, codomain)(images)
            return super().hom(images, codomain)


class DividedPowerAlgebras(OwnedCategoryOverBaseRing):
    r"""Divided-power algebras ``Gamma(M)`` with their canonical grading."""

    @classmethod
    def _repr_object_names(cls):
        return "divided power algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.algebras import (
            CommutativeAlgebras,
        )
        from dzack_research.preamble.categories.algebras.graded_algebras import (
            GradedAlgebras,
        )

        return [
            GradedAlgebras(self.base_ring()),
            CommutativeAlgebras(self.base_ring()),
        ]

    class ParentMethods:
        def free_source_module(self):
            return self._preamble_free_algebra_source_module

        def graded_piece(self, degree):
            from dzack_research.preamble.categories.modules.powers import DividedPower

            return DividedPower(self.free_source_module(), degree)

        def scalar_multiple(self, scalar, element):
            return self._power_algebra_scalar_multiple(scalar, element)

        def _Hom_(self, codomain, category=None):
            if codomain in DividedPowerAlgebras(self.algebra_base_ring()):
                from dzack_research.preamble.categories.algebras.power_algebras import (
                    power_algebra_homset,
                )

                return power_algebra_homset(self, codomain)
            return super()._Hom_(codomain, category=category)

        def hom(self, images, codomain=None):
            if codomain is not None and codomain in DividedPowerAlgebras(
                self.algebra_base_ring()
            ):
                from dzack_research.preamble.categories.algebras.power_algebras import (
                    power_algebra_homset,
                )

                return power_algebra_homset(self, codomain)(images)
            return super().hom(images, codomain)
