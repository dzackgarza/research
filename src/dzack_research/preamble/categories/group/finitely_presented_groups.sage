r"""Finitely presented groups."""

from sage_lattice_category_spike.lexicon import Element
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage_lattice_category_spike.lexicon import Group

from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.refine import hook_post_init
from typing import Any, Self

from sage.categories.category import Category
from sage.groups.finitely_presented import (
    FinitelyPresentedGroup,
    FinitelyPresentedGroupElement,
)


_FP_LAYOUT_INLINE_WIDTH = 150
_FP_LAYOUT_STACKED_GENERATOR_WIDTH = 220
_FP_LAYOUT_STACKED_REL_WIDTH = 180
_FP_LAYOUT_STACKED_RELATION_AREA_BUDGET = 900
_FP_LAYOUT_STACKED_RELATION_COUNT_BUDGET = 12
_FP_LAYOUT_EXPANDED_GENERATOR_WIDTH = 90
_FP_LAYOUT_EXPANDED_RELATION_SOURCE_BUDGET = 180
_FP_LAYOUT_EXPANDED_COLUMN_GAP_BUDGET = 12
_FP_LAYOUT_EXPANDED_MAX_COLUMNS = 4


class OwnedFinitelyPresentedGroupElement(FinitelyPresentedGroupElement):
    r"""An element of a finitely presented group owned by the preamble."""


class OwnedFinitelyPresentedGroup(FinitelyPresentedGroup):
    r"""A finitely presented group in :class:`FinitelyPresentedGroups`.

    The owned parent type; the behaviour is the category's.
    """

    Element = OwnedFinitelyPresentedGroupElement


def _own_fp_group_types(group: "Group") -> None:
    r"""Claim the owned parent and element types before refine reads them."""
    from sage.cpython.type import can_assign_class

    if isinstance(group, OwnedFinitelyPresentedGroup):
        return
    assert can_assign_class(group), f"cannot own the type of {type(group).__name__}"
    group.__class__ = OwnedFinitelyPresentedGroup
    group.Element = OwnedFinitelyPresentedGroupElement


class FinitelyPresentedGroups(Category):
    r"""Finitely presented groups with compact multi-line LaTeX."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely presented groups"

    def super_categories(self) -> list:
        return [OwnedGroups()]

    class ParentMethods:
        def _latex_(self: Self) -> str:
            return _fp_format_finite_presentation_latex(self)


def _fp_group_generator_names(group: "Group") -> tuple[str, ...]:
    return tuple(str(name) for name in group.variable_names())


def _fp_format_generator_name(name: str) -> str:
    import re

    match = re.fullmatch(r"([A-Za-z]+)(\d+)", name)
    if match:
        stem, idx = match.groups()
        return f"{stem}_{{{idx}}}"
    return name.replace("_", "\\_")


def _fp_relation_syllables(group: "Group", word: "Element") -> tuple[tuple[int, int], ...]:
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
        match bool(syl and syl[-1][0] == idx):
            case True:
                syl[-1] = (idx, syl[-1][1] + exp)
                if syl[-1][1] == 0:
                    del syl[-1]
            case False:
                syl.append((idx, exp))
    return tuple(syl)


def _fp_format_word_latex(group: "Group", word: "Element") -> str:
    gnames = tuple(_fp_format_generator_name(n) for n in _fp_group_generator_names(group))
    if not gnames:
        return "1"
    syl = _fp_relation_syllables(group, word)
    if not syl:
        return "1"
    if (
        len(syl) == 4
        and syl[0][1] == 1
        and syl[1][1] == 1
        and syl[2] == (syl[0][0], -1)
        and syl[3] == (syl[1][0], -1)
    ):
        return f"[{gnames[syl[0][0]]}, {gnames[syl[1][0]]}]"
    def syllable(idx: int, exponent: int) -> str:
        generator = gnames[idx]
        match exponent:
            case 1:
                return generator
            case -1:
                return f"{generator}^{{-1}}"
            case value if value not in (1, -1):
                return f"{generator}^{{{value}}}"

    return "".join(syllable(idx, exponent) for idx, exponent in syl)


def _fp_relation_word_rows(group: "Group", rels: tuple[Any, ...]) -> tuple[str, ...]:
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


def _fp_format_finite_presentation_latex(group: "Group") -> str:
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


_FINITELY_PRESENTED_GROUPS_INSTALLED = False


def install_finitely_presented_groups() -> None:
    """Hook post-init on finitely presented groups."""
    global _FINITELY_PRESENTED_GROUPS_INSTALLED
    if _FINITELY_PRESENTED_GROUPS_INSTALLED:
        return

    hook_post_init(
        FinitelyPresentedGroup,
        FinitelyPresentedGroups(),
        before=_own_fp_group_types,
    )
    _FINITELY_PRESENTED_GROUPS_INSTALLED = True


install_finitely_presented_groups()
