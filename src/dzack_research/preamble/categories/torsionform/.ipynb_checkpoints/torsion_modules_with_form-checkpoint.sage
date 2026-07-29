r"""Finite torsion modules equipped with a bilinear or quadratic form."""

from typing import Any

from sage.arith.misc import factor
from sage.categories.category import Category
from sage.categories.sets_cat import Sets
from sage.misc.latex import latex as _latex_fn


class TorsionModulesWithForm(Category):
    r"""Category of finite torsion modules equipped with a form."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "torsion modules with form"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        r"""Methods shared by bilinear and quadratic discriminant modules."""

        def as_finitely_presented_group(self: Any) -> Any:
            r"""Return a Sage-native ``FinitelyPresentedGroup`` representing $A_L$."""
            return _torsion_module_as_finitely_presented_group(self)

        def abelian_group(self: Any) -> Any:
            r"""Return the underlying finite abelian group in invariant-factor form."""
            from sage.groups.abelian_gps.abelian_group import AbelianGroup

            return AbelianGroup(list(self.invariants()))

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


def _torsion_module_as_finitely_presented_group(module: Any) -> Any:
    r"""Return a finite presentation for the underlying discriminant group."""
    L = module.source_lattice()
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
        return _detect_matrix_connected_cuts(raw)

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
            internal = _detect_matrix_connected_cuts(sub_raw)
            for c in internal:
                all_cuts.append(curr + c)
            curr += k
            all_cuts.append(curr)
    return sorted(set(c for c in all_cuts if 0 < c < n))


def _detect_matrix_connected_cuts(G: Any) -> list[int]:
    r"""Find diagonal block cuts of a matrix via graph connected components."""
    n = G.nrows()
    if n <= 1:
        return []
    try:
        import networkx as nx
    except ImportError:
        return []

    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if G[i, j] != 0:
                adj[i].append(j)
                adj[j].append(i)
    graph = nx.Graph(adj)
    components = [sorted(c) for c in nx.connected_components(graph)]
    components.sort(key=lambda c: c[0])
    indices = [i for c in components for i in c]
    if indices != list(range(n)):
        return []
    cuts: list[int] = []
    curr = 0
    for s in (len(c) for c in components[:-1]):
        curr += s
        cuts.append(curr)
    return [c for c in cuts if 0 < c < n]


# ---- FinitelyPresentedGroup compact LaTeX ----

_FP_LAYOUT_INLINE_WIDTH = 150
_FP_LAYOUT_STACKED_GENERATOR_WIDTH = 220
_FP_LAYOUT_STACKED_REL_WIDTH = 180
_FP_LAYOUT_STACKED_RELATION_AREA_BUDGET = 900
_FP_LAYOUT_STACKED_RELATION_COUNT_BUDGET = 12
_FP_LAYOUT_EXPANDED_GENERATOR_WIDTH = 90
_FP_LAYOUT_EXPANDED_RELATION_SOURCE_BUDGET = 180
_FP_LAYOUT_EXPANDED_COLUMN_GAP_BUDGET = 12
_FP_LAYOUT_EXPANDED_MAX_COLUMNS = 4


def _fp_group_generator_names(group: Any) -> tuple[str, ...]:
    return tuple(str(name) for name in group.variable_names())


def _fp_format_generator_name(name: str) -> str:
    import re

    match = re.fullmatch(r"([A-Za-z]+)(\d+)", name)
    if match:
        stem, idx = match.groups()
        return f"{stem}_{{{idx}}}"
    return name.replace("_", "\\_")


def _fp_relation_syllables(group: Any, word: Any) -> tuple[tuple[int, int], ...]:
    names = _fp_group_generator_names(group)
    nc = len(names)
    raw = word.Tietze()
    assert isinstance(raw, (tuple, list)), f"word must expose integer Tietze words; got {type(word)!r}"
    syl: list[tuple[int, int]] = []
    for item in tuple(raw):
        v = int(item)
        if v == 0:
            continue
        idx = abs(v) - 1
        assert 0 <= idx < nc, f"index out of range: idx={idx}, n_gens={nc}"
        exp = 1 if v > 0 else -1
        if syl and syl[-1][0] == idx:
            syl[-1] = (idx, syl[-1][1] + exp)
            if syl[-1][1] == 0:
                del syl[-1]
        else:
            syl.append((idx, exp))
    return tuple(syl)


def _fp_format_word_latex(group: Any, word: Any) -> str:
    gnames = tuple(_fp_format_generator_name(n) for n in _fp_group_generator_names(group))
    if not gnames:
        return "1"
    syl = _fp_relation_syllables(group, word)
    if not syl:
        return "1"
    if len(syl) == 4 and syl[0][1] == 1 and syl[1][1] == 1 and syl[2] == (syl[0][0], -1) and syl[3] == (syl[1][0], -1):
        return f"[{gnames[syl[0][0]]}, {gnames[syl[1][0]]}]"
    parts = []
    for idx, exp in syl:
        g = gnames[idx]
        if exp == 1:
            parts.append(g)
        elif exp == -1:
            parts.append(f"{g}^{{-1}}")
        else:
            parts.append(f"{g}^{{{exp}}}")
    return "".join(parts) if parts else "1"


def _fp_relation_word_rows(group: Any, rels: tuple[Any, ...]) -> tuple[str, ...]:
    return tuple(_fp_format_word_latex(group, r) for r in rels)


def _fp_pack_rows(items: tuple[str, ...], width: int, sep: str) -> tuple[str, ...]:
    if not items:
        return ()
    lines, cur = [], ""
    for item in items:
        cand = item if not cur else f"{cur}{sep}{item}"
        if len(cand) <= width:
            cur = cand
            continue
        if cur:
            lines.append(cur)
        cur = item
    lines.append(cur)
    return tuple(lines)


class FinitelyPresentedGroups(Category):
    r"""Finitely presented groups with compact multi-line LaTeX."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely presented groups"

    def super_categories(self) -> list:
        from sage.categories.groups import Groups

        return [Groups()]

    class ParentMethods:
        def _latex_(self: Any) -> str:
            return _fp_format_finite_presentation_latex(self)


def _fp_relation_table_latex(rows: tuple[str, ...]) -> str:
    if not rows:
        return ""
    widest = max(len(r) for r in rows)
    cols = max(
        1,
        min(
            _FP_LAYOUT_EXPANDED_MAX_COLUMNS,
            len(rows),
            (_FP_LAYOUT_EXPANDED_RELATION_SOURCE_BUDGET + _FP_LAYOUT_EXPANDED_COLUMN_GAP_BUDGET)
            // (widest + _FP_LAYOUT_EXPANDED_COLUMN_GAP_BUDGET),
        ),
    )
    grouped = tuple(rows[i : i + cols] for i in range(0, len(rows), cols))
    colspec = "@{\\qquad}".join("l" for _ in range(cols))
    rendered = []
    for row in grouped:
        cells = list(row) + [""] * (cols - len(row))
        rendered.append(" & ".join(cells))
    return f"\\begin{{array}}{{{colspec}}}\n" + "\\\\\n".join(rendered) + "\n\\end{array}"


def _fp_format_finite_presentation_latex(group: Any) -> str:
    r"""Render a ``FinitelyPresentedGroup`` as compact LaTeX."""
    gens = tuple(_fp_format_generator_name(n) for n in _fp_group_generator_names(group))
    rels = tuple(group.relations())
    rel_words = _fp_relation_word_rows(group, rels)
    gens_text = ", ".join(gens)
    empty = not rel_words

    inline = f"\\left\\langle {gens_text} \\;\\middle|\\; {', '.join(rel_words)} \\right\\rangle"
    if empty:
        if not gens:
            return "\\left\\langle \\;\\middle|\\; \\right\\rangle"
        return f"\\left\\langle {gens_text} \\;\\middle|\\; \\right\\rangle"
    if len(inline) <= _FP_LAYOUT_INLINE_WIDTH:
        return inline

    mgw, mrw, rc, ra = (
        len(gens_text),
        max((len(r) for r in rel_words), default=0),
        len(rel_words),
        sum(len(r) for r in rel_words),
    )
    if (
        mgw <= _FP_LAYOUT_STACKED_GENERATOR_WIDTH
        and mrw <= _FP_LAYOUT_STACKED_REL_WIDTH
        and rc <= _FP_LAYOUT_STACKED_RELATION_COUNT_BUDGET
        and ra <= _FP_LAYOUT_STACKED_RELATION_AREA_BUDGET
    ):
        stacked = "\\\\\n".join(rel_words)
        return f"\\left\\langle {gens_text} \\;\\middle|\\; \\begin{{aligned}}\n{stacked}\n\\end{{aligned}} \\right\\rangle"

    gen_lines = _fp_pack_rows(gens, _FP_LAYOUT_EXPANDED_GENERATOR_WIDTH, ", ") or ("\\,\\,",)
    table = _fp_relation_table_latex(rel_words)
    return (
        "\\begin{gathered}\n"
        "\\text{Generators:}\\\\[0.25em]\n"
        "\\begin{gathered}\n"
        + "\\\\\n".join(gen_lines)
        + "\n"
        "\\end{gathered}\\\\[0.75em]\n"
        "\\text{Relations:}\\\\[0.25em]\n"
        f"{table}\n"
        "\\end{gathered}"
    )
