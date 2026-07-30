r"""``HyperbolicLattices`` — hyperbolic integral lattices supporting root enumeration.

Refine a hyperbolic (``n``, 1) integral lattice into this category to gain::

    vinberg_algorithm(v0, use_coxiter, output, max_roots, max_decompositions, verbose)
    get_isotrop_type(isotropic_vector)   # classify by divisibility and $e^*\in A_L$

EXAMPLES::

    sage: from dzack_research.preamble import catalogue
    sage: from dzack_research.preamble.categories import HyperbolicLattices
    sage: L = Lattices.U.direct_sum(Lattices.E8)  # E10, signature (1, 9)
    sage: L._refine_category_(HyperbolicLattices())
    sage: hasattr(L, "vinberg_algorithm")
    True
"""

from typing import Any, assert_never

from sage.arith.misc import gcd
from sage.categories.category import Category
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.sets.set import Set

class HyperbolicLattices(Category):
    r"""Category of hyperbolic integral lattices (signature ``(n, 1)``).

    Provides one Vinberg root enumeration implementation (via the vendored
    ``vinal`` clone) and isotropic-vector classification via ``get_isotrop_type``.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "hyperbolic integral lattices"

    def super_categories(self) -> list:
        return [IntegralLattices()]

    class ParentMethods:
        r"""Methods available on hyperbolic lattices refined into this category."""

        def vinberg_algorithm(
            self: Any,
            v0: Any = None,
            use_coxiter: bool = False,
            output: Any = None,
            max_roots: int | None = None,
            max_decompositions: int | None = None,
            verbose: bool = False,
        ) -> Any:
            r"""Enumerate roots using the vendored Vinberg algorithm.

            Requires the ``vinal`` clone in ``computations/vendor/``.

            Parameters
            ----------
            v0 : vector, optional
                Starting vector (default: the last basis vector).
            use_coxiter : bool
                Whether to use CoxIter for covolume checking.
            output : optional
                Output target (passed to ``VinAl``).
            max_roots : int, optional
                Bound on the number of roots.
            max_decompositions : int, optional
                Bound on the number of decompositions.
            verbose : bool
                Show a ``tqdm`` progress bar.

            Returns
            -------
            list
                The enumerated root vectors.
            """
            source, negate_roots = self._vinberg_algorithm_source()

            from vinal import VinAl

            algorithm = VinAl(source.gram_matrix(), v0, use_coxiter, output)

            report, bar = (
                self._vinberg_progress(max_decompositions) if verbose else (None, None)
            )
            try:
                complete = algorithm.FindRoots(
                    max_roots=max_roots,
                    max_decompositions=max_decompositions,
                    progress=report,
                )
            finally:
                if bar is not None:
                    bar.close()

            if not complete:
                import warnings

                warnings.warn(
                    f"Vinberg search did not establish the fundamental polyhedron: "
                    f"{len(algorithm.roots)} root(s) found, but finite covolume was never "
                    f"confirmed. For signature (n, 1) with n=1 the criterion is "
                    f"unreachable (half-line in H^1, infinite volume).",
                    RuntimeWarning,
                    stacklevel=2,
                )
            roots = list(algorithm.roots)
            return [-root for root in roots] if negate_roots else roots

        def get_isotrop_type(self: Any, isotropic_vector: Any) -> str:
            r"""Classify a primitive isotropic vector by the AE/Nikulin cusp type.

            The definition is intrinsic to the vector in the 2-elementary
            lattice.  The vector is ``"Odd"`` when its divisibility is 1.  When
            its divisibility is 2, its divided class $e^* = e/2 \in A_L$
            determines the two even cases: ``"Even ordinary"`` if $e^*$ is
            ordinary and ``"Even characteristic"`` if $e^*$ is characteristic,
            meaning $q(x) = b(x,e^*) \pmod{\mathbb Z}$ for every $x\in A_L$.
            """
            assert getattr(isotropic_vector, "parent", lambda: None)() is self, (
                "get_isotrop_type expects an element of this lattice, not "
                f"{type(isotropic_vector).__name__}"
            )
            assert self.q(isotropic_vector) == 0, (
                f"expected an isotropic vector, got square {self.q(isotropic_vector)}"
            )

            integral_coordinates = list(self.coordinate_vector(isotropic_vector))
            assert abs(gcd(integral_coordinates)) == 1, (
                f"expected a primitive vector, got coordinates {integral_coordinates}"
            )

            divisibility = self.div(isotropic_vector)
            assert divisibility in Set({1, 2}), (
                f"expected divisibility 1 or 2 in a 2-elementary lattice, "
                f"got {divisibility}"
            )
            if divisibility == 1:
                return "Odd"
            if divisibility == 2:
                divided_class = self._divided_discriminant_class(
                    integral_coordinates,
                    divisibility,
                )
                if divided_class.is_characteristic():
                    return "Even characteristic"
                return "Even ordinary"
            assert_never(divisibility)

        # ---- internal helpers ----

        def _divided_discriminant_class(
            self: Any,
            integral_coordinates: Any,
            divisibility: Any,
        ) -> Any:
            r"""Return the discriminant element represented by $e/\operatorname{div}(e)$.
            """
            dual_element = self.dual_lattice_element(
                [QQ(c) / QQ(divisibility) for c in integral_coordinates]
            )
            return self.project_to_discriminant_group(dual_element)

        def _vinberg_algorithm_source(self: Any) -> tuple[Any, bool]:
            r"""Return a signature ``(n, 1)`` source and whether to negate roots back."""
            from sage.quadratic_forms.quadratic_form import QuadraticForm

            gram = self.gram_matrix()
            pos, neg, zero = QuadraticForm(
                QQ, gram.change_ring(QQ)
            ).signature_vector()
            assert zero == 0, f"lattice is degenerate: {zero} zero direction(s)"
            if neg == 1:
                return self, False
            if pos == 1:
                return self.twist(-1), True
            assert False, (
                f"Vinberg's algorithm needs signature (n, 1); "
                f"this lattice has ({pos}, {neg})"
            )

        @staticmethod
        def _vinberg_progress(total: int | None) -> tuple[Any, Any]:
            r"""Return a progress callback and tqdm bar for Vinberg search."""
            from tqdm.auto import tqdm

            bar = tqdm(
                total=int(total) if total is not None else None,
                unit=" decomp",
                desc="Vinberg search",
                postfix={"roots": 0},
                leave=True,
            )

            def report(decompositions: int, roots: int) -> None:
                bar.n = int(decompositions)
                bar.set_postfix(roots=int(roots), refresh=False)
                bar.refresh()

            return report, bar
