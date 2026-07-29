r"""Finite torsion modules equipped with a bilinear or quadratic form."""

from typing import Any

from sage.arith.misc import factor
from sage.categories.category import Category
from sage.misc.latex import latex as _latex_fn


class TorsionModulesWithForm(Category):
    r"""Category of finite torsion modules equipped with a form."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "torsion modules with form"

    def super_categories(self) -> list:
        return [OwnedFiniteGroups()]

    class ParentMethods:
        r"""Methods shared by bilinear and quadratic discriminant modules."""

        def as_finitely_presented_group(self: Any) -> Any:
            r"""Return a Sage-native ``FinitelyPresentedGroup`` representing $A_L$."""
            L = self.source_lattice()
            G = L.gram_matrix()
            r = G.nrows()
            from sage.groups.free_group import FreeGroup
            from sage.misc.misc_c import prod

            if r == 0:
                F = FreeGroup(0, "e")
                return F.quotient([])

            names = [f"e{i+1}" for i in range(r)]
            F = FreeGroup(names)
            gens = F.gens()
            rels = []
            for i in range(r):
                for j in range(i + 1, r):
                    rels.append(gens[i] * gens[j] * (gens[i] ^ -1) * (gens[j] ^ -1))
            for k in range(r):
                word = prod((gens[j] ^ int(G[j, k])) for j in range(r))
                rels.append(word)
            return F.quotient(rels)

        def abelian_group(self: Any) -> Any:
            r"""Return the underlying finite abelian group in invariant-factor form."""
            from sage.groups.abelian_gps.abelian_group import AbelianGroup

            return refine(
                AbelianGroup(list(self.invariants())),
                OwnedFiniteGroups(),
            )

        def is_p_elementary(self: Any, p: Any) -> bool:
            r"""Return whether the underlying group is elementary abelian of exponent \(p\)."""
            from sage.rings.integer_ring import ZZ

            p = ZZ(p)
            assert p.is_prime(), f"p must be prime, got {p}"
            G = self.abelian_group().permutation_group()
            if not G.is_elementary_abelian():
                return False
            return G.order() == 1 or G.exponent() == p

        def _latex_(self: Any) -> str:
            r"""Return multi-line LaTeX for the torsion module and its form."""
            invs = self.invariants()
            n = self.gram_matrix().nrows()

            fp_latex = str(_latex_fn(self.as_finitely_presented_group()))
            inv_str = _format_invariant_factor_latex(invs)
            prim_str = _format_primary_decomp_latex(invs)
            gram_latex = _form_gram_matrix_latex(self)
            label = self._form_matrix_latex_label()

            line1 = (
                f"A_L = {fp_latex} \\in \\mathrm{{Groups}} \\quad "
                "\\text{(Finite presentation)} \\\\"
            )
            line2 = (
                f"A_L \\cong {inv_str} \\in \\mathrm{{Groups}} \\quad "
                "\\text{(Invariant factor decomposition)} \\\\"
            )
            line3 = (
                f"A_L \\cong {prim_str} \\in \\mathrm{{Groups}} \\quad "
                "\\text{(Primary decomposition)} \\\\"
            )
            line4 = (
                f"{label} = {gram_latex} \\in "
                f"\\mathrm{{Mat}}_{{{n}}}({self._form_matrix_latex_codomain()})"
            )

            return (
                "\\begin{gathered}\n"
                + "\n".join([line1, line2, line3, line4])
                + "\n\\end{gathered}"
            )

        def _form_matrix_latex_label(self: Any) -> str:
            r"""Return the LaTeX label for this form's Gram matrix."""
            return "G_{A_L}"

        def _form_matrix_latex_codomain(self: Any) -> str:
            r"""Return the LaTeX codomain for this form's Gram matrix entries."""
            return "\\mathbb{Q}/\\mathbb{Z}"


def _format_cyclic_group_latex(orders: tuple[int, ...]) -> str:
    r"""Format cyclic group orders as ``C_n^m``."""
    if not orders:
        return "0"
    from collections import Counter

    counts = Counter(orders)
    parts = []
    for n in sorted(counts):
        m = counts[n]
        if m == 1:
            parts.append(f"C_{{{n}}}")
        else:
            parts.append(f"C_{{{n}}}^{{{m}}}")
    return " \\oplus ".join(parts)


def _format_invariant_factor_latex(invariants: tuple[int, ...]) -> str:
    r"""Format invariant factors as ``C_n^m``."""
    return _format_cyclic_group_latex(invariants)


def _format_primary_decomp_latex(invariants: tuple[int, ...]) -> str:
    r"""Format the primary decomposition implied by invariant factors."""
    if not invariants:
        return "0"
    primary_orders: list[int] = []
    for n in invariants:
        primary_orders.extend(int(p) ** int(e) for p, e in factor(n))
    return _format_cyclic_group_latex(tuple(primary_orders))


def _form_gram_matrix_latex(module: Any) -> str:
    r"""Return LaTeX for a form Gram matrix."""
    import re

    if not module.invariants():
        return "()"
    gram_str = str(_latex_fn(module.gram_matrix()))
    zero_dots = globals().get("_zero_dots", lambda: False)
    if zero_dots():
        gram_str = re.sub(r"\b0\b", lambda m: r"\cdot", gram_str)
    return gram_str


def subdivide_form_gram_matrix(module: Any) -> None:
    r"""Partition ``module``'s Gram matrix once and replace ``gram_matrix``."""
    raw = module.gram_matrix()
    cuts = _form_gram_matrix_cuts(module, raw)
    if cuts:
        G = raw.parent()(raw)
        G.subdivide(cuts, cuts)
    else:
        G = raw
    module.gram_matrix = lambda: G


def _form_gram_matrix_cuts(module: Any, raw: Any) -> list[int]:
    r"""Compute form Gram matrix block cuts from the source lattice decomposition."""
    n = raw.nrows()
    if n == 0:
        return []

    L = module.source_lattice()

    L_cuts = L.gram_matrix().subdivisions()[0]
    if not L_cuts:
        return _matrix_connected_component_cuts(raw)

    from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

    r = L.rank()
    gram = L.gram_matrix()
    starts = [0] + list(L_cuts)
    ends = list(L_cuts) + [r]

    all_cuts: list[int] = []
    curr = 0
    for start, end in zip(starts, ends):
        sub_g = gram.submatrix(start, start, end - start, end - start)
        sub_A = IntegralLattice(sub_g).discriminant_group()
        from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

        sub_raw = TorsionQuadraticModule.gram_matrix_quadratic.f(sub_A)
        k = sub_raw.nrows()
        if k > 0:
            internal = _matrix_connected_component_cuts(sub_raw)
            for c in internal:
                all_cuts.append(curr + c)
            curr += k
            all_cuts.append(curr)
    return sorted(set(c for c in all_cuts if 0 < c < n))
