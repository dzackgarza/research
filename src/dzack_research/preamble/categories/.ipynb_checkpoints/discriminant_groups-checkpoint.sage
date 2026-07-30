r"""Discriminant bilinear and quadratic modules.

Refine a ``TorsionQuadraticModule`` into this category to gain::

    gram_matrix()              # the form matrix for this category
    associated_bilinear_form() # the bilinear module attached to a quadratic module
    normal_form()              # marking result as normal form
    _latex_()                  # multi-line display
    finitely_presented_group() # Sage-native FinitelyPresentedGroup
    abelian_group()            # Sage AbelianGroup (invariant factors)
    is_p_elementary(p)         # via abelian_group().permutation_group()

Elements gain::

    is_characteristic()        # q(x) = b(x, self) mod Z for all x

EXAMPLES::

    sage: from dzack_research.preamble import catalogue
    sage: from dzack_research.preamble.categories import DiscriminantQuadraticModules
    sage: A = Lattices.U.discriminant_group()
    sage: A._refine_category_(DiscriminantQuadraticModules())
"""

from typing import Any

from sage.arith.misc import factor
from sage.categories.category import Category
from sage.categories.sets_cat import Sets
from sage.matrix.constructor import matrix
from sage.misc.latex import latex as _latex_fn
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

class DiscriminantBilinearModules(Category):
    r"""Category of discriminant bilinear modules.

    The category's ``gram_matrix`` is the bilinear Gram matrix. Quadratic
    discriminant modules refine this category and expose their associated
    bilinear form through :meth:`associated_bilinear_form`.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "discriminant bilinear modules"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        r"""Methods available on discriminant bilinear modules."""

        def gram_matrix(self: Any) -> Any:
            r"""Return the bilinear Gram matrix with induced block subdivisions."""
            _ensure_native_refs()
            invs = self.invariants()
            if not invs:
                return matrix(ZZ, 0, 0)

            raw = _native_gram_b(self)
            cuts = _compute_disc_subdivisions(self)
            if cuts:
                G = raw.parent()(raw)
                G.subdivide(cuts, cuts)
                return G
            return raw

        def gram_matrix_bilinear(self: Any) -> Any:
            r"""Compatibility spelling for :meth:`gram_matrix`."""
            return self.gram_matrix()


class DiscriminantQuadraticModules(Category):
    r"""Category of discriminant quadratic modules.

    The category's ``gram_matrix`` is the quadratic Gram matrix. Its bilinear
    matrix is obtained from the associated bilinear form, not by duplicating the
    native method here.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "discriminant quadratic modules"

    def super_categories(self) -> list:
        return [DiscriminantBilinearModules()]

    class ParentMethods:
        r"""Methods available on discriminant quadratic modules."""

        def gram_matrix(self: Any) -> Any:
            r"""Return the quadratic Gram matrix with induced block subdivisions."""
            _ensure_native_refs()
            invs = self.invariants()
            if not invs:
                return matrix(ZZ, 0, 0)

            raw = _native_gram_q(self)
            cuts = _compute_disc_subdivisions(self)
            if cuts:
                G = raw.parent()(raw)
                G.subdivide(cuts, cuts)
                return G
            return raw

        def gram_matrix_quadratic(self: Any) -> Any:
            r"""Compatibility spelling for :meth:`gram_matrix`."""
            return self.gram_matrix()

        def associated_bilinear_form(self: Any) -> Any:
            r"""Return this quadratic module's associated bilinear module."""
            _ensure_native_refs()
            bilinear = _native_associated_bilinear_form(self)
            refine(bilinear, DiscriminantBilinearModules())
            return bilinear

        def gram_matrix_bilinear(self: Any) -> Any:
            r"""Return the associated bilinear form's Gram matrix."""
            return self.associated_bilinear_form().gram_matrix()

        def normal_form(self: Any, *args: Any, **kwargs: Any) -> Any:
            r"""Return the normal form, marked as such."""
            _ensure_native_refs()
            norm = _native_normal_form(self, *args, **kwargs)
            norm._is_normal_form = True
            return norm

        def finitely_presented_group(self: Any) -> Any:
            r"""Return a Sage-native ``FinitelyPresentedGroup`` representing $A_L$.

            The presentation is $\mathbb{Z}^r / G_L \mathbb{Z}^r$ where $G_L$ is
            the relation matrix (the Gram matrix of $L$).
            """
            L = getattr(getattr(self, "_W", None), "ambient_module", lambda: None)()
            if L is not None and hasattr(L, "gram_matrix"):
                G = L.gram_matrix()
            else:
                G = self.gram_matrix_quadratic()
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
                    rels.append(
                        gens[i] * gens[j] * (gens[i] ^ -1) * (gens[j] ^ -1)
                    )
            for k in range(r):
                word = prod((gens[j] ^ int(G[j, k])) for j in range(r))
                rels.append(word)
            group = F.quotient(rels)
            return group

        def abelian_group(self: Any) -> Any:
            r"""Return $A_L$ as a Sage ``AbelianGroup`` in invariant-factor form.

            This is the finite abelian group underlying the discriminant quadratic
            module; GAP predicates such as elementary abelianity are available on
            ``.permutation_group()``.
            """
            from sage.groups.abelian_gps.abelian_group import AbelianGroup

            return AbelianGroup(list(self.invariants()))

        def is_p_elementary(self: Any, p: Any) -> bool:
            r"""Return whether $A_L$ is an elementary abelian $p$-group.

            Defers to Sage's permutation-group realisation of
            :meth:`abelian_group`, which asks GAP ``IsElementaryAbelian``.
            """
            from sage.rings.integer_ring import ZZ

            p = ZZ(p)
            assert p.is_prime(), f"p must be prime, got {p}"
            G = self.abelian_group().permutation_group()
            if not G.is_elementary_abelian():
                return False
            return G.order() == 1 or G.exponent() == p

        def _latex_(self: Any) -> str:
            r"""Return multi-line LaTeX for the discriminant group.

            Shows: finite presentation, invariant factor decomposition,
            primary decomposition, and quadratic Gram matrix.
            """
            invs = self.invariants()
            n = self.gram_matrix_quadratic().nrows()

            fp_latex = str(_latex_fn(self.finitely_presented_group()))
            inv_str = _format_invariant_factor_latex(invs)
            prim_str = _format_primary_decomp_latex(self)
            gram_q_latex = _primary_gram_matrix_latex(self)

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
                f"G_{{q_{{A_L}}}} = {gram_q_latex} \\in "
                f"\\mathrm{{Mat}}_{{{n}}}(\\mathbb{{Q}}/2\\mathbb{{Z}})"
            )

            return (
                "\\begin{gathered}\n"
                + "\n".join([line1, line2, line3, line4])
                + "\n\\end{gathered}"
            )

    class ElementMethods:
        r"""Methods available on elements of discriminant quadratic modules."""

        def is_characteristic(self: Any) -> bool:
            r"""Return whether this discriminant element is characteristic.

            An element \(v^*\in A_L\) is characteristic when
            \(q(x)=b(x,v^*)\pmod{\mathbb Z}\) for every \(x\in A_L\).
            Sage's torsion quadratic values may live in ``Q/2Z`` while
            bilinear values live in ``Q/Z``, so the comparison is explicitly
            reduced modulo \(\mathbb Z\).
            """
            for x in self.parent():
                if not _equal_mod_integers(x.q(), x * self):
                    return False
            return True

# ---- internal helpers ----

_native_gram_q: Any = None
_native_gram_b: Any = None
_native_associated_bilinear_form: Any = None
_native_normal_form: Any = None
_refs_ensured: bool = False

def _ensure_native_refs() -> None:
    r"""Capture references to native Sage methods on first use."""
    global _native_gram_q, _native_gram_b, _native_associated_bilinear_form, _native_normal_form, _refs_ensured
    if _refs_ensured:
        return
    from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

    _native_gram_q = TorsionQuadraticModule.gram_matrix_quadratic.f
    _native_gram_b = TorsionQuadraticModule.gram_matrix_bilinear.f
    associated = TorsionQuadraticModule.associated_bilinear_form
    _native_associated_bilinear_form = associated.f if hasattr(associated, "f") else associated
    _native_normal_form = TorsionQuadraticModule.normal_form
    _refs_ensured = True

def _compute_disc_subdivisions(A_disc: Any) -> list[int]:
    r"""Compute discriminant Gram matrix block cuts from the lattice's block decomposition."""
    raw = _native_gram_q(A_disc)
    n = raw.nrows()
    if n == 0:
        return []

    if getattr(A_disc, "_is_normal_form", False):
        return _detect_matrix_connected_cuts(raw)

    L = getattr(getattr(A_disc, "_W", None), "ambient_module", lambda: None)()
    if L is None or not hasattr(L, "gram_matrix"):
        return _detect_matrix_connected_cuts(raw)

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
        sub_raw = _native_gram_q(sub_A)
        k = sub_raw.nrows()
        if k > 0:
            internal = _detect_matrix_connected_cuts(sub_raw)
            for c in internal:
                all_cuts.append(curr + c)
            curr += k
            all_cuts.append(curr)
    return sorted(set(c for c in all_cuts if 0 < c < n))


def _equal_mod_integers(left: Any, right: Any) -> bool:
    r"""Return whether two torsion-form values agree modulo $\mathbb Z$."""
    return QQ(left.lift() - right.lift()) in ZZ

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

def _format_primary_decomp_latex(A_disc: Any) -> str:
    r"""Format primary decomposition as ``C_n^m``."""
    invs = A_disc.invariants()
    if not invs:
        return "0"
    primes = sorted(set(f for n in invs for f, _ in factor(n)))
    all_powers: list[int] = []
    for p in primes:
        all_powers.extend(A_disc.primary_part(p).invariants())
    return _format_cyclic_group_latex(tuple(all_powers))

def _primary_gram_matrix_latex(A_disc: Any) -> str:
    r"""Return LaTeX of primary decomposition block-diagonal Gram matrix."""
    import re

    invs = A_disc.invariants()
    if not invs:
        return "()"
    gram_str = str(_latex_fn(A_disc.gram_matrix_quadratic()))
    if _zero_dots():
        gram_str = re.sub(r"\b0\b", lambda m: r"\cdot", gram_str)
    return gram_str

# ---- FinitelyPresentedGroup compact LaTeX (used by discriminant groups) ----

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

# ---- FinitelyPresentedGroup compact LaTeX as a category ----

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
    return (
        f"\\begin{{array}}{{{colspec}}}\n"
        + "\\\\\n".join(rendered)
        + "\n\\end{array}"
    )

def _fp_format_finite_presentation_latex(group: Any) -> str:
    r"""Render a ``FinitelyPresentedGroup`` as compact LaTeX.

    Selects layout based on complexity:

    - inline for small presentations (<= 150 chars)
    - stacked aligned for moderate sizes
    - expanded table for large presentations
    """
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

# ---- install: post-init hooks only ----

_DISCRIMINANT_GROUPS_INSTALLED = False


def install_discriminant_groups() -> None:
    """Hook post-init on torsion quadratic modules and FP groups."""
    global _DISCRIMINANT_GROUPS_INSTALLED
    if _DISCRIMINANT_GROUPS_INSTALLED:
        return

    from sage.groups.finitely_presented import FinitelyPresentedGroup
    from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

    hook_post_init(TorsionQuadraticModule, DiscriminantQuadraticModules())
    hook_post_init(FinitelyPresentedGroup, FinitelyPresentedGroups())
    _DISCRIMINANT_GROUPS_INSTALLED = True
