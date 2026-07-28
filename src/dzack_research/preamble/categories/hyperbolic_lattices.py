r"""``HyperbolicLattices`` — hyperbolic integral lattices supporting root enumeration.

Refine a hyperbolic (``n``, 1) integral lattice into this category to gain::

    vinberg_algorithm(v0, use_coxiter, output, max_roots, max_decompositions, verbose)
    run_vin(**kwargs)                    # convenience: returns lattice with enumerated roots
    get_isotrop_type(isotropic_vector)   # classify via $e^\perp/e$

EXAMPLES::

    sage: from dzack_research.preamble import catalogue
    sage: from dzack_research.preamble.categories import HyperbolicLattices
    sage: L = catalogue.Lattices.U.direct_sum(catalogue.Lattices.E8)  # E10, signature (1, 9)
    sage: L._refine_category_(HyperbolicLattices())
    sage: hasattr(L, \"vinberg_algorithm\")
    True
"""

from __future__ import annotations

from typing import Any

from sage.categories.category import Category
from sage.rings.rational_field import QQ

from .integral_lattices import IntegralLattices


class HyperbolicLattices(Category):
    r"""Category of hyperbolic integral lattices (signature ``(n, 1)``).

    Provides Vinberg's root enumeration algorithm (via the vendored ``vinal``
    clone), a ``run_vin`` convenience wrapper, and isotropic-vector classification
    via ``get_isotrop_type``.
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
            self._assert_vinberg_signature()

            from dzack_research.preamble.vendor import activate_clone

            activate_clone("vinal", "src", "sage")
            from vinal import VinAl

            algorithm = VinAl(self.gram_matrix(), v0, use_coxiter, output)

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
            return algorithm.roots

        def run_vin(self: Any, **kwargs: Any) -> Any:
            r"""Return a new lattice with enumerated roots and optional labels.

            If the lattice has signature ``(1, n)`` (positive), it is twisted
            to ``(n, 1)`` before enumeration and the roots are negated back.
            """
            from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

            twisted = self.signature_pair()[0] == 1
            source = self.twist(-1) if twisted else self

            from dzack_research.preamble.vendor import activate_clone

            activate_clone("vinal", "src", "sage")
            from vinal import VinAl

            algorithm = VinAl(source.gram_matrix(), None, False, None)
            complete = algorithm.FindRoots(**kwargs)

            if not complete:
                import warnings

                warnings.warn(
                    "Vinberg search did not establish the fundamental polyhedron.",
                    RuntimeWarning,
                    stacklevel=2,
                )

            roots = algorithm.roots
            result = IntegralLattice(self.gram_matrix())
            result.roots = [-r for r in roots] if twisted else list(roots)
            try:
                result._assign_names(self.variable_names())
                if hasattr(result, "to_lin_comb_generators"):
                    result.root_names = [
                        result.to_lin_comb_generators(r) for r in result.roots
                    ]
                else:
                    result.root_names = None
            except (ValueError, AttributeError):
                result.root_names = None
            return result

        def get_isotrop_type(self: Any, isotropic_vector: Any) -> str:
            r"""Classify an isotropic vector via the isometry type of $e^\perp/e$.

            Returns ``"Odd"``, ``"Even ordinary"``, ``"Even characteristic"``,
            or ``"Not found."``.
            """
            from dzack_research.preamble import catalogue

            quotient = self.I_perp_mod_I([isotropic_vector])
            if not hasattr(quotient, "is_isometric") or quotient.rank() == 0:
                return "Not found."
            if quotient.is_isometric(catalogue.Lattices.U):
                return "Odd"
            if quotient.is_isometric(catalogue.Lattices.U_2):
                return "Even ordinary"
            if quotient.is_isometric(catalogue.Lattices.IPQ(1, 1).twist(2)):
                return "Even characteristic"
            return "Not found."

        # ---- internal helpers ----

        def _assert_vinberg_signature(self: Any) -> tuple[int, int]:
            r"""Assert the lattice has signature ``(n, 1)`` and return ``(n, 1)``."""
            from sage.quadratic_forms.quadratic_form import QuadraticForm

            gram = self.gram_matrix()
            pos, neg, zero = QuadraticForm(
                QQ, gram.change_ring(QQ)
            ).signature_vector()
            assert zero == 0, f"lattice is degenerate: {zero} zero direction(s)"
            assert neg == 1, (
                f"Vinberg's algorithm needs signature (n, 1); "
                f"this lattice has ({pos}, {neg})"
            )
            return pos, neg

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
