r"""``HyperbolicLattices`` — hyperbolic integral lattices supporting root enumeration.

Refine a hyperbolic (``n``, 1) integral lattice into this category to gain::

    vinberg_algorithm(v0, use_coxiter, output, max_roots, max_decompositions, verbose)
    get_isotropic_type(isotropic_element)   # classify by divisibility and $e^*\in A_L$

EXAMPLES::

    sage: from dzack_research.preamble import catalogue
    sage: from dzack_research.preamble.categories import HyperbolicLattices
    sage: L = Lattices.U.direct_sum(Lattices.E8)  # E10, signature (1, 9)
    sage: refine(L, HyperbolicLattices())
    sage: L in HyperbolicLattices()
    True
"""

from typing import Any

from sage.categories.category import Category

class HyperbolicLattices(Category):
    r"""Category of hyperbolic integral lattices (signature ``(n, 1)``).

    Provides one Vinberg root enumeration implementation (via the vendored
    ``vinal`` clone). Isotropic-element classification is inherited from
    ``IntegralLattices``.
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
                The enumerated roots, as elements of this lattice.
            """
            # ``vinal`` diagonalizes and asserts exactly one negative entry, so
            # it wants signature (n, 1).  This repo's convention is negative
            # definite, making its hyperbolic lattices (1, n) -- those are the
            # ones needing the twist, and their roots come back negated.
            pos, neg = self.signature_pair()
            match pos, neg:
                case _, 1:
                    source = self
                    negate_roots = False
                case 1, _:
                    source = self.twist(-1)
                    negate_roots = True
                case _:
                    raise ValueError(
                    f"Vinberg's algorithm needs signature (1, n) or (n, 1); "
                    f"this lattice has ({pos}, {neg})"
                    )

            from vinal import VinAl

            algorithm = VinAl(source.gram_matrix(), v0, use_coxiter, output)

            report, bar = (
                self._vinberg_progress(max_decompositions) if verbose else (None, None)
            )
            from contextlib import ExitStack

            with ExitStack() as cleanup:
                if bar is not None:
                    cleanup.callback(bar.close)
                complete = algorithm.FindRoots(
                    max_roots=max_roots,
                    max_decompositions=max_decompositions,
                    progress=report,
                )

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
            # What comes back is coordinates: the algorithm was handed a Gram
            # matrix and knows nothing else, so reading its output as elements
            # of this lattice is a step someone has to take, and this is it.
            roots = [self.linear_combination(root) for root in algorithm.roots]
            return [-root for root in roots] if negate_roots else roots

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
