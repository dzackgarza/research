r"""Install additional methods on Sage integral lattices.

EXAMPLES::

    sage: from dzack_research.preamble import catalogue, patches
    sage: patches.install("lattice_methods")
    sage: catalogue.U.q(catalogue.U.gens()[0])
    0
    sage: patches.uninstall("lattice_methods")
"""

from __future__ import annotations

from typing import Any

_METHODS = (
    "q",
    "b",
    "div",
    "dual_basis",
    "e_perp_mod_e",
    "I_perp_mod_I",
    "is_isometric",
    "with_names",
    "to_lin_comb_generators",
    "sublattices",
    "_latex_",
)


def _expand_names(spec: str, rank: int) -> tuple[str, ...]:
    r"""Expand indexed ranges in a basis-name specification."""
    import re

    names: list[str] = []
    for piece in (part.strip() for part in spec.split(",")):
        assert piece, f"empty name in spec {spec!r}"
        match = re.fullmatch(r"([A-Za-z_]+)(\d+)\.\.\1?(\d+)", piece)
        if match:
            stem, start, stop = match.group(1), int(match.group(2)), int(match.group(3))
            assert stop >= start, f"descending range in {piece!r}"
            names.extend(f"{stem}{i}" for i in range(start, stop + 1))
        else:
            assert re.fullmatch(r"[A-Za-z_]\w*", piece), f"not a valid name: {piece!r}"
            names.append(piece)

    assert len(names) == rank, (
        f"spec {spec!r} gives {len(names)} names but the lattice has rank {rank}"
    )
    assert len(set(names)) == len(names), f"duplicate names in {spec!r}"
    return tuple(names)


def with_names(self: Any, spec: str) -> Any:
    r"""Attach basis names and return the lattice.

    EXAMPLES::

        sage: from dzack_research.preamble import catalogue, patches
        sage: patches.install("lattice_methods")
        sage: catalogue.E8.with_names("a1..a8").variable_names()
        ('a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8')
        sage: patches.uninstall("lattice_methods")
    """
    self._assign_names(_expand_names(spec, self.rank()))
    return self


def to_lin_comb_generators(self: Any, element: Any) -> str:
    r"""Return an element as a linear combination of the named basis."""
    names = self.variable_names()
    coordinates = self.coordinate_vector(element)
    assert len(names) == len(coordinates), "name count does not match the rank"

    terms = []
    for name, coefficient in zip(names, coordinates, strict=True):
        if coefficient == 0:
            continue
        if coefficient == 1:
            terms.append(name)
        elif coefficient == -1:
            terms.append(f"-{name}")
        else:
            terms.append(f"{coefficient}*{name}")
    return " + ".join(terms).replace("+ -", "- ") if terms else "0"


def sublattices(self: Any) -> dict:
    r"""Return the per-instance dictionary of named sublattices."""
    existing = self.__dict__.get("_sublattices")
    if existing is None:
        existing = {}
        self._sublattices = existing
    return existing


def _lattice_class() -> type:
    from sage.modules.free_quadratic_module_integer_symmetric import (
        FreeQuadraticModule_integer_symmetric,
    )

    return FreeQuadraticModule_integer_symmetric


def q(self: Any, x: Any) -> Any:
    r"""The quadratic form $q(x) = \langle x, x\rangle$."""
    return self.b(x, x)


def b(self: Any, x: Any, y: Any) -> Any:
    r"""Return the pairing $\langle x,y\rangle=x^TGy$."""
    vx = getattr(x, "value", x)
    vy = getattr(y, "value", y)
    return (vx * self.gram_matrix()).dot_product(vy)


def div(self: Any, x: Any) -> Any:
    r"""Return the positive generator of $\{\langle x,y\rangle:y\in L\}$."""
    from sage.arith.misc import gcd

    pairings = [self.b(x, basis_vector) for basis_vector in self.basis()]
    value = gcd(pairings)
    return abs(value)


def dual_basis(self: Any) -> Any:
    r"""Return the columns of $G^{-1}$ as the dual basis."""
    gram = self.gram_matrix()
    columns = gram.inverse().columns()
    for i, basis_vector in enumerate(self.basis()):
        for j, dual_vector in enumerate(columns):
            expected = 1 if i == j else 0
            assert self.b(basis_vector, dual_vector) == expected, (
                f"dual basis is wrong at ({i}, {j})"
            )
    return columns


def I_perp_mod_I(self: Any, vectors: Any) -> Any:
    r"""Return $I^\perp/I$ for the isotropic sublattice spanned by ``vectors``.

    EXAMPLES::

        sage: from dzack_research.preamble import catalogue, patches
        sage: patches.install("lattice_methods")
        sage: catalogue.U.I_perp_mod_I([catalogue.U.gens()[0]])
        []
        sage: patches.uninstall("lattice_methods")
    """
    from sage.matrix.constructor import matrix
    from sage.modules.free_module import FreeModule
    from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
    from sage.rings.integer_ring import ZZ

    coordinate_rows = []
    for vector_ in vectors:
        vec_unwrapped = vector_.value if hasattr(vector_, "value") else vector_
        coordinates = self.coordinate_vector(vec_unwrapped).change_ring(ZZ)
        coordinate_rows.append(coordinates)

    for i, left in enumerate(coordinate_rows):
        for j, right in enumerate(coordinate_rows):
            pairing = self.b(left, right)
            assert pairing == 0, (
                f"I must be isotropic: <v{i}, v{j}> = {pairing}, expected 0"
            )

    gram = self.gram_matrix()
    free_module = FreeModule(ZZ, self.rank())
    pairing_matrix = matrix(ZZ, [gram * row for row in coordinate_rows])
    perp = free_module.submodule(pairing_matrix.right_kernel().basis())
    isotropic = free_module.submodule(coordinate_rows)
    quotient = perp / isotropic

    lifts = [generator.lift() for generator in quotient.gens()]
    sub_basis = [
        self.element_class(self, sum(coeff * base for coeff, base in zip(lift, self.basis())))
        for lift in lifts
    ]
    return sub_basis


from sage.structure.element import Matrix, ModuleElement, Vector

_original_call: Any = None
_original_gens: Any = None


class LatticeElement(ModuleElement):
    r"""Wrapper for lattice elements that implements bilinear pairing as multiplication.

    Multiplication ``v * w`` computes ``b(v, w)``, ``v * v`` computes ``q(v)``,
    and exponentiation ``v ** 2`` or ``v ^ 2`` computes ``q(v)``.
    """

    def __init__(self, parent: Any, value: Any) -> None:
        ModuleElement.__init__(self, parent)
        if hasattr(value, "value"):
            self.value = value.value
        elif isinstance(value, Vector):
            self.value = value
        elif hasattr(parent, "ambient"):
            self.value = parent.ambient()(value)
        else:
            self.value = value

    def _repr_(self) -> str:
        return repr(self.value)

    def _latex_(self) -> str:
        from sage.misc.latex import latex

        return str(latex(self.value))

    def list(self) -> list:
        return list(self.value)

    def _vector_(self, R: Any = None) -> Any:
        if R is not None:
            return self.value.change_ring(R)
        return self.value

    def __iter__(self) -> Any:
        return iter(self.value)

    def __getitem__(self, i: Any) -> Any:
        return self.value[i]

    def __len__(self) -> int:
        return len(self.value)

    def __add__(self, other: Any) -> Any:
        v_other = other.value if hasattr(other, "value") else other
        return self.parent()(self.value + v_other)

    def __radd__(self, other: Any) -> Any:
        return self.__add__(other)

    def __sub__(self, other: Any) -> Any:
        v_other = other.value if hasattr(other, "value") else other
        return self.parent()(self.value - v_other)

    def __rsub__(self, other: Any) -> Any:
        v_other = other.value if hasattr(other, "value") else other
        return self.parent()(v_other - self.value)

    def __neg__(self) -> Any:
        return self.parent()(-self.value)

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, Matrix):
            return self.value * other
        if isinstance(other, (LatticeElement, Vector)):
            vec_other = other.value if hasattr(other, "value") else other
            return self.parent().b(self.value, vec_other)
        return self.parent()(self.value * other)

    def __rmul__(self, other: Any) -> Any:
        if isinstance(other, Matrix):
            return other * self.value
        if isinstance(other, (LatticeElement, Vector)):
            vec_other = other.value if hasattr(other, "value") else other
            return self.parent().b(vec_other, self.value)
        return self.parent()(other * self.value)


def e_perp_mod_e(self: Any, vector_: Any) -> Any:
    r"""$e^{\perp} / \langle e \rangle$ for a single isotropic $e$."""
    return self.I_perp_mod_I([vector_])


def is_isometric(self: Any, other: Any) -> bool:
    r"""Return whether two integral lattices are isometric.

    EXAMPLES::

        sage: from dzack_research.preamble import catalogue, patches
        sage: patches.install("lattice_methods")
        sage: catalogue.E8.is_isometric(catalogue.E8)
        True
        sage: patches.uninstall("lattice_methods")
    """
    from sage.quadratic_forms.quadratic_form import QuadraticForm

    if self.rank() != other.rank():
        return False
    if self.signature_pair() != other.signature_pair():
        return False

    positive, negative = self.signature_pair()
    if positive == 0 or negative == 0:
        sign = 1 if negative == 0 else -1
        left = QuadraticForm(sign * self.gram_matrix())
        right = QuadraticForm(sign * other.gram_matrix())
        return bool(left.is_globally_equivalent_to(right))

    if self.rank() == 2:
        # Indefinite rank 2 is decided exactly by binary-form equivalence, so there is
        # no need to refuse it -- genus insufficiency below rank 3 is not a reason to
        # give up when reduction theory settles the case outright.
        from sage.quadratic_forms.binary_qf import BinaryQF

        def _binary(lattice: Any) -> Any:
            gram = lattice.gram_matrix()
            assert gram[0, 0] % 2 == 0 and gram[1, 1] % 2 == 0, (
                "binary form conversion needs an even lattice"
            )
            return BinaryQF([gram[0, 0] // 2, gram[0, 1], gram[1, 1] // 2])

        return bool(_binary(self).is_equivalent(_binary(other)))

    return bool(self.genus() == other.genus())


ZERO_DOTS: bool = True


def set_zero_dots(enabled: bool = True) -> None:
    """Toggle replacing 0 entries with \\cdot in lattice LaTeX output."""
    global ZERO_DOTS
    ZERO_DOTS = bool(enabled)


def _format_cyclic_group_latex(orders: tuple[int, ...]) -> str:
    r"""Format a sequence of cyclic group orders using ``C_n^m`` notation."""
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
    r"""Format invariant factors into LaTeX string using ``C_n^m`` notation."""
    return _format_cyclic_group_latex(invariants)


def _format_primary_decomp_latex(A_disc: Any) -> str:
    r"""Format primary decomposition into LaTeX string using ``C_n^m`` notation."""
    invs = A_disc.invariants()
    if not invs:
        return "0"
    from sage.arith.misc import factor

    primes = sorted(set(f for n in invs for f, _ in factor(n)))
    all_powers: list[int] = []
    for p in primes:
        all_powers.extend(A_disc.primary_part(p).invariants())
    return _format_cyclic_group_latex(tuple(all_powers))


def _primary_gram_matrix_latex(A_disc: Any) -> str:
    r"""Return LaTeX of primary decomposition block-diagonal quadratic Gram matrix."""
    invs = A_disc.invariants()
    if not invs:
        return "()"
    import re
    from sage.misc.latex import latex

    gram_str = str(latex(A_disc.gram_matrix_quadratic()))
    if ZERO_DOTS:
        gram_str = re.sub(r"\b0\b", lambda m: r"\cdot", gram_str)
    return gram_str


def _format_disc_latex(disc: Any) -> str:
    r"""Format discriminant with prime factorization in LaTeX."""
    d = int(disc)
    if d in (-1, 0, 1):
        return str(d)
    from sage.arith.misc import factor
    from sage.misc.latex import latex

    f = factor(d)
    f_latex = str(latex(f))
    if f_latex == str(d):
        return str(d)
    return f"{d} = {f_latex}"


def _latex_(self: Any) -> str:
    r"""Return multi-line LaTeX representation with category, rank, signature, discriminant, Gram matrix, and discriminant group.

    EXAMPLES::

        sage: from dzack_research.preamble import catalogue, patches
        sage: patches.install("lattice_methods")
        sage: from sage.misc.latex import latex
        sage: print(latex(catalogue.U))
        \begin{gathered}
        L \in \mathrm{Lattices}(\mathbb{Z}), \quad \mathrm{rk}(L) = 2, \quad \mathrm{sig}(L) = (1, 1), \quad \mathrm{disc}(L) = -1 \\
        G_L = \left(\begin{array}{rr}
        \cdot & 1 \\
        1 & \cdot
        \end{array}\right) \\
        A_L = \left\langle e_{1}, e_{2} \;\\middle|\\; e_{1}e_{2}e_{1}^{-1}e_{2}^{-1}, e_{2}, e_{1} \right\rangle \in \mathrm{Groups} \quad \text{(Dual basis presentation)} \\
        A_L \cong 0 \in \mathrm{Groups} \quad \text{(Invariant factor decomposition)} \\
        A_L \cong 0 \in \mathrm{Groups} \quad \text{(Primary decomposition)} \\
        G_{q_{A_L}} = () \in \mathrm{Mat}_{0}(\mathbb{Q}/2\mathbb{Z})
        \end{gathered}
        sage: patches.uninstall("lattice_methods")
    """
    import re
    from sage.misc.latex import latex

    rank = self.rank()
    pos, neg = self.signature_pair()
    disc = self.gram_matrix().det()
    disc_latex = _format_disc_latex(disc)
    gram_latex = str(latex(self.gram_matrix()))
    if ZERO_DOTS:
        gram_latex = re.sub(r"\b0\b", lambda m: r"\cdot", gram_latex)

    A_disc = self.discriminant_group()
    A_latex = str(latex(A_disc))
    A_lines = []
    for line in A_latex.splitlines():
        if not line:
            continue
        stripped = line.strip()
        if stripped.startswith(r"\begin{gathered}") or stripped.startswith(r"\end{gathered}"):
            continue
        if stripped.startswith(r"\begin{aligned}") or stripped.startswith(r"\end{aligned}"):
            A_lines.append(line)
            continue
        A_lines.append(line)

    header_lines = [
        r"\begin{gathered}",
        f"L \\in \\mathrm{{Lattices}}(\\mathbb{{Z}}), \\quad \\mathrm{{rk}}(L) = {rank}, \\quad \\mathrm{{sig}}(L) = ({pos}, {neg}), \\quad \\mathrm{{disc}}(L) = {disc_latex} \\\\",
        f"G_L = {gram_latex} \\\\",
    ]

    return "\n".join(header_lines + A_lines + [r"\end{gathered}"])


# THEORY OF DISCRIMINANT GROUP PRESENTATION:
# For an integral lattice L with basis B_L = (e_1, ..., e_r) and Gram matrix G_L,
# the dual lattice L* has dual basis B_L* = (e_1*, ..., e_r*) defined by b(e_i*, e_j) = delta_ij.
# The inclusion homomorphism f: L -> L* sends e_i \mapsto \sum_{j=1}^r (G_L)_{ji} e_j*.
# Hence, the matrix of f relative to bases B_L and B_L* is EXACTLY G_L: [f]_{B_L -> B_L*} = G_L.
# The discriminant group A_L = coker(f) = L* / f(L) is presented on the nose as:
#     A_L = < e_1*, ..., e_r* | \sum_j (G_L)_{ji} e_j* = 0 > = Z^r / G_L Z^r
# Thus, G_L is the relation matrix on the dual basis generators [e_1*], ..., [e_r*].


def _finitely_presented_group(self: Any) -> Any:
    r"""Return a Sage-native FinitelyPresentedGroup representing A_L on the dual basis."""
    L = getattr(getattr(self, "_W", None), "ambient_module", lambda: None)()
    if L is not None and hasattr(L, "gram_matrix"):
        G_L = L.gram_matrix()
    else:
        G_L = self.gram_matrix_quadratic()
    r = G_L.nrows()
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
            rels.append(gens[i] * gens[j] * gens[i] ** -1 * gens[j] ** -1)
    for k in range(r):
        word = prod(gens[j] ** int(G_L[j, k]) for j in range(r))
        rels.append(word)
    group = F.quotient(rels)
    group._dzack_relation_summary = f"\\mathbb{{Z}}^{{{r}}} / G_L \\mathbb{{Z}}^{{{r}}}"
    return group


def _format_dual_presentation_latex(A_disc: Any) -> str:
    r"""Return compact LaTeX for the dual basis presentation
    A_L = \mathbb{Z}^r / G_L \mathbb{Z}^r.

    The finitely presented group object is available via ``A_disc.finitely_presented_group()``
    for programmatic inspection, but its ``_latex_()`` output is too verbose for display
    (O(r^2) commutator relations alone).  The compact matrix-quotient notation is the
    standard way to present an abelian group given by a relation matrix.
    """
    L = getattr(getattr(A_disc, "_W", None), "ambient_module", lambda: None)()
    if L is not None and hasattr(L, "rank"):
        r = L.rank()
        if r == 0:
            return "0"
        return f"\\mathbb{{Z}}^{{{r}}} / G_L \\mathbb{{Z}}^{{{r}}}"
    invs = A_disc.invariants()
    if not invs:
        return "0"
    k = len(invs)
    return f"\\mathbb{{Z}}^{{{k}}} / D \\mathbb{{Z}}^{{{k}}}"


def _patched_torsion_latex(self: Any) -> str:
    r"""Return LaTeX representation for a discriminant group TorsionQuadraticModule."""
    from sage.misc.latex import latex

    invs = self.invariants()
    n = self.gram_matrix_quadratic().nrows()
    fp_latex = str(latex(self.finitely_presented_group()))
    inv_str = _format_invariant_factor_latex(invs)
    prim_str = _format_primary_decomp_latex(self)
    gram_q_latex = _primary_gram_matrix_latex(self)

    line1 = (
        f"A_L = {fp_latex} \\in \\mathrm{{Groups}} \\quad \\text{{(Finite presentation)}} \\\\"
    )
    line2 = (
        f"A_L \\cong {inv_str} \\in \\mathrm{{Groups}} \\quad "
        "\\text{{(Invariant factor decomposition)}} \\\\"
    )
    line3 = (
        f"A_L \\cong {prim_str} \\in \\mathrm{{Groups}} \\quad "
        "\\text{{(Primary decomposition)}} \\\\"
    )
    line4 = (
        f"G_{{q_{{A_L}}}} = {gram_q_latex} \\in "
        f"\\mathrm{{Mat}}_{{{n}}}(\\mathbb{{Q}}/2\\mathbb{{Z}})"
    )

    return "\\begin{gathered}\n" + "\n".join([line1, line2, line3, line4]) + "\n\\end{gathered}"


def _expand_ellipsis_names(names: tuple[str, ...]) -> tuple[str, ...]:
    r"""Expand ``('a1','Ellipsis','a8')`` through ``'a8'``."""
    import re

    expanded: list[str] = []
    for index, name in enumerate(names):
        if name != "Ellipsis":
            expanded.append(name)
            continue
        assert 0 < index < len(names) - 1, (
            f"'...' needs a name on each side; got {names}"
        )
        before, after = expanded[-1], names[index + 1]
        left = re.fullmatch(r"([A-Za-z_]+)(\d+)", before)
        right = re.fullmatch(r"([A-Za-z_]+)(\d+)", after)
        assert left and right, (
            f"'...' needs indexed names either side: {before}, {after}"
        )
        assert left.group(1) == right.group(1), (
            f"'...' between different stems: {before} and {after}"
        )
        start, stop = int(left.group(2)), int(right.group(2))
        assert stop > start, f"'...' range does not ascend: {before}..{after}"
        expanded.extend(f"{left.group(1)}{i}" for i in range(start + 1, stop))
    return tuple(expanded)


def _first_ngens(self: Any, count: int) -> tuple[Any, ...]:
    r"""Return generators matching the declared name slots."""
    generators = self.gens()
    spec = getattr(self, "_ellipsis_spec", None)
    if spec is None or len(spec) != count:
        return tuple(generators[:count])

    names = list(self.variable_names())
    return tuple(
        Ellipsis if slot == "Ellipsis" else generators[names.index(slot)]
        for slot in spec
    )


def _matmul(self: Any, other: Any) -> Any:
    r"""Return ``L @ M`` as the orthogonal direct sum."""
    return self.direct_sum(other)


def _pow(self: Any, exponent: Any) -> Any:
    r"""``L ** n`` as the ``n``-fold orthogonal direct sum."""
    count = int(exponent)
    assert count >= 1, f"lattice power needs a positive exponent, got {exponent}"
    result = self
    for _ in range(count - 1):
        result = result.direct_sum(self)
    return result


def _apply_names(lattice: Any, names: Any) -> Any:
    """Expand a declared name tuple onto a lattice, checking it against the rank."""
    declared = tuple(names)
    expanded = _expand_ellipsis_names(declared)
    assert len(expanded) == lattice.rank(), (
        f"{declared} expands to {len(expanded)} names but the lattice has rank {lattice.rank()}"
    )
    lattice._assign_names(expanded)
    lattice._ellipsis_spec = declared
    return lattice


_original_direct_sum: Any = None


def _direct_sum(self: Any, *others: Any, names: Any = None, **kwargs: Any) -> Any:
    r"""Call ``direct_sum``, set block subdivisions, and apply an optional ``names=`` spec."""
    if not others:
        return self if names is None else _apply_names(self, names)

    result = self
    for other in others:
        left_subdivs = result.gram_matrix().subdivisions()[0] or ()
        left_rank = result.rank()
        right_subdivs = other.gram_matrix().subdivisions()[0] or ()

        result = _original_direct_sum(result, other, **kwargs)

        combined = list(left_subdivs) + [left_rank] + [left_rank + s for s in right_subdivs]
        result.gram_matrix().subdivide(combined, combined)

    return result if names is None else _apply_names(result, names)


_original_twist: Any = None


def _twist(self: Any, *args: Any, names: Any = None, **kwargs: Any) -> Any:
    r"""``twist`` preserving block subdivisions and accepting ``names=``."""
    subdivs = self.gram_matrix().subdivisions()
    result = _original_twist(self, *args, **kwargs)
    if subdivs != ([], []):
        result.gram_matrix().subdivide(*subdivs)
    return result if names is None else _apply_names(result, names)


def _refresh_catalogue_subdivisions(cat: Any) -> None:
    _subdiv_map = {
        "E10": ([2], [2]),
        "E10_2": ([2], [2]),
        "LK3": ([2, 4, 6, 14], [2, 4, 6, 14]),
        "TdP": ([2, 4, 6, 14], [2, 4, 6, 14]),
        "TEn": ([2], [2]),
        "Tco": ([1], [1]),
        "Sco": ([1], [1]),
        "LpNik": ([2, 4, 6], [2, 4, 6]),
        "L_20_2_0": ([2, 4, 6, 14], [2, 4, 6, 14]),
        "LK3_2": ([1, 3, 5, 13], [1, 3, 5, 13]),
        "LK3_4": ([1, 3, 5, 13], [1, 3, 5, 13]),
    }
    for name, subdivs in _subdiv_map.items():
        obj = getattr(cat, name, None)
        if obj is not None and hasattr(obj, "gram_matrix"):
            obj.gram_matrix().subdivide(*subdivs)


_CLASS_ATTRS = {
    "_first_ngens": _first_ngens,
    "twist": _twist,
    "__matmul__": _matmul,
    "__pow__": _pow,
    "direct_sum": _direct_sum,
}

_original_integral_lattice: Any = None


def _patched_integral_lattice(*args: Any, names: Any = None, **kwargs: Any) -> Any:
    """``IntegralLattice`` post-init running block decomposition on G_L."""
    lattice = _original_integral_lattice(*args, **kwargs)
    _compute_lattice_gram_subdivisions(lattice)
    if names is None:
        return lattice

    return _apply_names(lattice, names)


from sage.structure.element import ModuleElement, Vector

_original_call: Any = None
_original_gens: Any = None


class LatticeElement(ModuleElement):
    r"""Wrapper for lattice elements that implements bilinear pairing as multiplication.

    Multiplication ``v * w`` computes ``b(v, w)``, ``v * v`` computes ``q(v)``,
    and exponentiation ``v ** 2`` or ``v ^ 2`` computes ``q(v)``.
    """

    def __init__(self, parent: Any, value: Any) -> None:
        ModuleElement.__init__(self, parent)
        if isinstance(value, LatticeElement):
            self.value = value.value
        elif isinstance(value, Vector):
            self.value = value
        elif hasattr(parent, "ambient"):
            self.value = parent.ambient()(value)
        else:
            self.value = value

    def _repr_(self) -> str:
        return repr(self.value)

    def _latex_(self) -> str:
        from sage.misc.latex import latex

        return str(latex(self.value))

    def list(self) -> list:
        return list(self.value)

    def _vector_(self, R: Any = None) -> Any:
        if R is not None:
            return self.value.change_ring(R)
        return self.value

    def __iter__(self) -> Any:
        return iter(self.value)

    def __getitem__(self, i: Any) -> Any:
        return self.value[i]

    def __len__(self) -> int:
        return len(self.value)

    def __add__(self, other: Any) -> Any:
        if isinstance(other, LatticeElement):
            return self.parent()(self.value + other.value)
        return self.parent()(self.value + other)

    def __radd__(self, other: Any) -> Any:
        return self.__add__(other)

    def __sub__(self, other: Any) -> Any:
        if isinstance(other, LatticeElement):
            return self.parent()(self.value - other.value)
        return self.parent()(self.value - other)

    def __rsub__(self, other: Any) -> Any:
        return self.parent()(other - self.value)

    def __neg__(self) -> Any:
        return self.parent()(-self.value)

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, (LatticeElement, Vector)):
            vec_other = other.value if isinstance(other, LatticeElement) else other
            return self.parent().b(self.value, vec_other)
        return self.parent()(self.value * other)

    def __rmul__(self, other: Any) -> Any:
        if isinstance(other, (LatticeElement, Vector)):
            vec_other = other.value if isinstance(other, LatticeElement) else other
            return self.parent().b(vec_other, self.value)
        return self.parent()(other * self.value)

    def __pow__(self, exp: Any, mod: Any = None) -> Any:
        if exp == 2:
            return self.parent().q(self.value)
        raise NotImplementedError(f"exponent {exp} not supported for lattice elements")

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, LatticeElement):
            return self.value == other.value
        return self.value == other

    def div(self) -> Any:
        return self.parent().div(self)

    def q(self) -> Any:
        return self.parent().q(self)

    def b(self, other: Any) -> Any:
        return self.parent().b(self, other)


def _patched_call(self: Any, *args: Any, **kwargs: Any) -> Any:
    res = _original_call(self, *args, **kwargs)
    if isinstance(res, Vector) and not isinstance(res, LatticeElement):
        return LatticeElement(self, res)
    return res


def _patched_gens(self: Any, *args: Any, **kwargs: Any) -> Any:
    return tuple(LatticeElement(self, v) for v in _original_gens(self, *args, **kwargs))


def _detect_matrix_connected_cuts(G: Any) -> list[int]:
    r"""Find diagonal block cuts of a symmetric matrix via connected components."""
    n = G.nrows()
    if n <= 1:
        return []
    import networkx as nx

    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if G[i, j] != 0:
                adj[i].append(j)
                adj[j].append(i)
    graph = nx.Graph(adj)
    components = [sorted(list(c)) for c in nx.connected_components(graph)]
    components.sort(key=lambda c: c[0])
    indices = [i for c in components for i in c]
    if indices != list(range(n)):
        return []
    sizes = [len(c) for c in components]
    cuts: list[int] = []
    curr = 0
    for s in sizes[:-1]:
        curr += s
        cuts.append(curr)
    return [c for c in cuts if 0 < c < n]


def _compute_lattice_gram_subdivisions(L: Any) -> list[int]:
    r"""Return or detect block cuts for a lattice's Gram matrix."""
    gram = L.gram_matrix()
    subdivs = gram.subdivisions()[0]
    if subdivs:
        return list(subdivs)
    cuts = _detect_matrix_connected_cuts(gram)
    if cuts:
        if gram.is_immutable():
            from copy import copy

            gram = copy(gram)
            try:
                L._gram_matrix = gram
            except AttributeError:
                pass
        gram.subdivide(cuts, cuts)
    return cuts


_in_disc_subdiv_computation: bool = False


def _compute_disc_gram_subdivisions(A_disc: Any) -> list[int]:
    r"""Compute induced discriminant group Gram matrix block cuts from L's block decomposition."""
    global _in_disc_subdiv_computation
    if _in_disc_subdiv_computation:
        return []
    _in_disc_subdiv_computation = True
    try:
        raw_disc_gram = _original_torsion_gram_q(A_disc)
        n = raw_disc_gram.nrows()
        if n == 0:
            return []

        if getattr(A_disc, "_is_normal_form", False):
            return _detect_matrix_connected_cuts(raw_disc_gram)

        L = getattr(getattr(A_disc, "_W", None), "ambient_module", lambda: None)()
        if L is None or not hasattr(L, "gram_matrix"):
            return _detect_matrix_connected_cuts(raw_disc_gram)

        L_cuts = _compute_lattice_gram_subdivisions(L)
        if not L_cuts:
            return _detect_matrix_connected_cuts(raw_disc_gram)

        from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

        r = L.rank()
        gram = L.gram_matrix()
        slice_starts = [0] + L_cuts
        slice_ends = L_cuts + [r]

        all_disc_cuts: list[int] = []
        curr_offset = 0

        for start, end in zip(slice_starts, slice_ends):
            sub_gram = gram.submatrix(start, start, end - start, end - start)
            sub_L = IntegralLattice(sub_gram)
            sub_A = sub_L.discriminant_group()
            sub_disc_gram = _original_torsion_gram_q(sub_A)
            sub_k = len(sub_A.gens())

            if sub_k > 0:
                internal_cuts = _detect_matrix_connected_cuts(sub_disc_gram)
                for ic in internal_cuts:
                    all_disc_cuts.append(curr_offset + ic)
                curr_offset += sub_k
                all_disc_cuts.append(curr_offset)

        return sorted(list(set(c for c in all_disc_cuts if 0 < c < n)))
    finally:
        _in_disc_subdiv_computation = False


_original_torsion_gram_q: Any = None
_original_torsion_gram_b: Any = None
_original_normal_form: Any = None
_original_torsion_latex: Any = None
_original_finitely_presented_group_latex: Any = None


_FP_LAYOUT_INLINE_WIDTH = 150
_FP_LAYOUT_STACKED_GENERATOR_WIDTH = 220
_FP_LAYOUT_STACKED_REL_WIDTH = 180
_FP_LAYOUT_STACKED_RELATION_AREA_BUDGET = 900
_FP_LAYOUT_STACKED_RELATION_COUNT_BUDGET = 12
_FP_LAYOUT_EXPANDED_GENERATOR_WIDTH = 90


def _fp_group_generator_names(group: Any) -> tuple[str, ...]:
    return tuple(str(name) for name in group.variable_names())


def _fp_format_generator_name(name: str) -> str:
    import re

    match = re.fullmatch(r"([A-Za-z]+)(\d+)", name)
    if match:
        stem, index = match.groups()
        return f"{stem}_{{{index}}}"
    return name.replace("_", "\\_")


def _fp_relation_syllables(group: Any, word: Any) -> tuple[tuple[int, int], ...]:
    names = _fp_group_generator_names(group)
    index_count = len(names)
    raw_tietze = word.Tietze()
    assert isinstance(raw_tietze, (tuple, list)), (
        "group word must expose integer Tietze words "
        f"when rendering finitely presented relations; got {type(word)!r}"
    )
    syllables: list[tuple[int, int]] = []
    for item in tuple(raw_tietze):
        value = int(item)
        if value == 0:
            continue
        index = abs(value) - 1
        assert 0 <= index < index_count, (
            "relation generator index out of range while rendering "
            f"finitely presented relation; index={index}, "
            f"n_gens={index_count}, raw_tietze={raw_tietze!r}"
        )
        exponent = 1 if value > 0 else -1
        if syllables and syllables[-1][0] == index:
            syllables[-1] = (index, syllables[-1][1] + exponent)
            if syllables[-1][1] == 0:
                del syllables[-1]
        else:
            syllables.append((index, exponent))
    return tuple(syllables)


def _fp_format_word_latex(group: Any, word: Any) -> str:
    generator_names = tuple(
        _fp_format_generator_name(name) for name in _fp_group_generator_names(group)
    )
    if not generator_names:
        return "1"

    syllables = _fp_relation_syllables(group, word)
    if not syllables:
        return "1"

    parts: list[str] = []
    for raw_index, raw_exponent in syllables:
        gen = generator_names[raw_index]
        if raw_exponent == 1:
            parts.append(gen)
        elif raw_exponent == -1:
            parts.append(f"{gen}^{{-1}}")
        else:
            parts.append(f"{gen}^{{{raw_exponent}}}")

    return "".join(parts) if parts else "1"


def _fp_relation_word_rows(
    group: Any, relations: tuple[Any, ...]
) -> tuple[str, ...]:
    return tuple(
        _fp_format_word_latex(group, relation) for relation in relations
    )


def _fp_relation_equation_rows(
    relation_words: tuple[str, ...]
) -> tuple[str, ...]:
    return tuple(
        f"R_{{{index}}} &: {word} = 1"
        for index, word in enumerate(relation_words, start=1)
    )


def _fp_pack_rows(items: tuple[str, ...], width: int, separator: str) -> tuple[str, ...]:
    if not items:
        return ()

    lines: list[str] = []
    current = ""
    for item in items:
        candidate = item if not current else f"{current}{separator}{item}"
        if len(candidate) <= width:
            current = candidate
            continue
        if current:
            lines.append(current)
        current = item
    lines.append(current)
    return tuple(lines)


def _fp_format_finite_presentation_latex(group: Any) -> str:
    gens = tuple(_fp_format_generator_name(name) for name in _fp_group_generator_names(group))
    relations = tuple(group.relations())
    rel_words = _fp_relation_word_rows(group, relations)
    rel_eq_rows = _fp_relation_equation_rows(rel_words)
    gens_text = ", ".join(gens)
    rels_text = ", ".join(rel_words)

    inline_text = (
        "\\left\\langle "
        f"{gens_text} \\;\\middle|\\; {rels_text} "
        "\\right\\rangle"
    )
    empty_relations = not rel_words
    if empty_relations:
        if not gens:
            return "\\left\\langle \\;\\middle|\\; \\right\\rangle"
        return (
            "\\left\\langle "
            f"{gens_text} \\;\\middle|\\; "
            "\\right\\rangle"
        )

    max_generator_width = len(gens_text)
    max_relation_width = max((len(row) for row in rel_eq_rows), default=0)
    max_relation_count = len(rel_eq_rows)
    relation_area = sum(len(row) for row in rel_eq_rows)
    if len(inline_text) <= _FP_LAYOUT_INLINE_WIDTH:
        return inline_text
    if (
        max_generator_width <= _FP_LAYOUT_STACKED_GENERATOR_WIDTH
        and max_relation_width <= _FP_LAYOUT_STACKED_REL_WIDTH
        and max_relation_count <= _FP_LAYOUT_STACKED_RELATION_COUNT_BUDGET
        and relation_area <= _FP_LAYOUT_STACKED_RELATION_AREA_BUDGET
    ):
        stacked_rows = "\\\\\n".join(rel_eq_rows)
        return (
            "\\left\\langle "
            f"{gens_text} \\;\\middle|\\; "
            "\\begin{aligned}\n"
            f"{stacked_rows}\n"
            "\\end{aligned} "
            "\\right\\rangle"
        )

    gen_lines = _fp_pack_rows(gens, _FP_LAYOUT_EXPANDED_GENERATOR_WIDTH, ", ")
    if not gen_lines:
        gen_lines = ("\\,\\,",)

    return (
        "\\begin{gathered}\n"
        "\\begin{array}{ll}\n"
        "\\text{Generators:} & "
        + gen_lines[0]
        + "".join(f"\\\\\n & {line}" for line in gen_lines[1:])
        + "\\\\\n"
        "\\text{Relations:} & \\begin{aligned}\n"
        f"{'\\\\\n'.join(rel_eq_rows)}\n"
        "\\end{aligned}\\\\\n"
        "\\end{array}\n"
        "\\end{gathered}"
    )


def _patched_finitely_presented_group_latex(group: Any) -> str:
    return _fp_format_finite_presentation_latex(group)


def _patched_normal_form(self: Any, *args: Any, **kwargs: Any) -> Any:
    r"""``normal_form`` returning a TorsionQuadraticModule marked as normal form."""
    norm = _original_normal_form(self, *args, **kwargs)
    setattr(norm, "_is_normal_form", True)
    return norm


def _patched_torsion_gram_matrix_quadratic(self: Any) -> Any:
    r"""Return literal quadratic Gram matrix of self.gens() with induced block subdivisions."""
    invs = self.invariants()
    if not invs:
        from sage.matrix.constructor import matrix
        from sage.rings.rational_field import QQ

        return matrix(QQ, 0, 0)
    raw_gram = _original_torsion_gram_q(self)
    cuts = _compute_disc_gram_subdivisions(self)
    if cuts:
        G_copy = raw_gram.parent()(raw_gram)
        G_copy.subdivide(cuts, cuts)
        return G_copy
    return raw_gram


def _patched_torsion_gram_matrix_bilinear(self: Any) -> Any:
    r"""Return literal bilinear Gram matrix of self.gens() with induced block subdivisions."""
    invs = self.invariants()
    if not invs:
        from sage.matrix.constructor import matrix
        from sage.rings.rational_field import QQ

        return matrix(QQ, 0, 0)
    raw_gram = _original_torsion_gram_b(self)
    cuts = _compute_disc_gram_subdivisions(self)
    if cuts:
        G_copy = raw_gram.parent()(raw_gram)
        G_copy.subdivide(cuts, cuts)
        return G_copy
    return raw_gram


def install() -> None:
    """Install the lattice methods and constructor support.

    EXAMPLES::

        sage: from dzack_research.preamble import patches
        sage: patches.install("lattice_methods")
        sage: "lattice_methods" in patches.installed()
        True
        sage: patches.uninstall("lattice_methods")
    """
    global _original_integral_lattice, _original_direct_sum, _original_twist, _original_call, _original_gens
    global _original_torsion_gram_q, _original_torsion_gram_b, _original_normal_form, _original_torsion_latex
    global _original_finitely_presented_group_latex

    target = _lattice_class()
    if _original_direct_sum is None:
        _original_direct_sum = target.direct_sum
    if _original_twist is None:
        _original_twist = target.twist
    if _original_call is None:
        _original_call = target.__call__
    if _original_gens is None:
        _original_gens = target.gens

    target.__call__ = _patched_call
    target.gens = _patched_gens

    from sage.groups.finitely_presented import FinitelyPresentedGroup
    if _original_finitely_presented_group_latex is None:
        _original_finitely_presented_group_latex = FinitelyPresentedGroup._latex_

    FinitelyPresentedGroup._latex_ = _patched_finitely_presented_group_latex

    from sage.misc.cachefunc import cached_method
    from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

    if _original_torsion_gram_q is None:
        _original_torsion_gram_q = TorsionQuadraticModule.gram_matrix_quadratic.f
    if _original_torsion_gram_b is None:
        _original_torsion_gram_b = TorsionQuadraticModule.gram_matrix_bilinear.f
    if _original_normal_form is None:
        _original_normal_form = TorsionQuadraticModule.normal_form
    if _original_torsion_latex is None and hasattr(TorsionQuadraticModule, "_latex_"):
        _original_torsion_latex = TorsionQuadraticModule._latex_

    TorsionQuadraticModule.gram_matrix_quadratic = cached_method(_patched_torsion_gram_matrix_quadratic)
    TorsionQuadraticModule.gram_matrix_bilinear = cached_method(_patched_torsion_gram_matrix_bilinear)
    TorsionQuadraticModule.normal_form = _patched_normal_form
    TorsionQuadraticModule._latex_ = _patched_torsion_latex
    TorsionQuadraticModule.finitely_presented_group = _finitely_presented_group

    for name in _METHODS:
        attribute = globals()[name]
        if name == "sublattices":
            attribute = property(attribute)
        setattr(target, name, attribute)
        assert hasattr(target, name), f"{target.__name__} rejected {name}"
    for name, attribute in _CLASS_ATTRS.items():
        setattr(target, name, attribute)

    import sys
    import sage.all
    import sage.modules.free_quadratic_module_integer_symmetric as module

    if _original_integral_lattice is None:
        _original_integral_lattice = module.IntegralLattice
    module.IntegralLattice = _patched_integral_lattice
    sage.all.IntegralLattice = _patched_integral_lattice

    if "dzack_research.preamble.catalogue" in sys.modules:
        _refresh_catalogue_subdivisions(sys.modules["dzack_research.preamble.catalogue"])


def uninstall() -> None:
    """Restore Sage's original lattice classes and constructor."""
    target = _lattice_class()
    for name in (*_METHODS, *_CLASS_ATTRS):
        if hasattr(target, name):
            try:
                delattr(target, name)
            except AttributeError:
                pass

    if _original_direct_sum is not None:
        target.direct_sum = _original_direct_sum
    if _original_twist is not None:
        target.twist = _original_twist
    if _original_call is not None:
        target.__call__ = _original_call
    if _original_gens is not None:
        target.gens = _original_gens
    from sage.groups.finitely_presented import FinitelyPresentedGroup
    if _original_finitely_presented_group_latex is not None:
        FinitelyPresentedGroup._latex_ = _original_finitely_presented_group_latex

    if _original_torsion_gram_q is not None and _original_torsion_gram_b is not None:
        from sage.misc.cachefunc import cached_method
        from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

        TorsionQuadraticModule.gram_matrix_quadratic = cached_method(_original_torsion_gram_q)
        TorsionQuadraticModule.gram_matrix_bilinear = cached_method(_original_torsion_gram_b)
        if _original_normal_form is not None:
            TorsionQuadraticModule.normal_form = _original_normal_form
        if _original_torsion_latex is not None:
            TorsionQuadraticModule._latex_ = _original_torsion_latex
        if hasattr(TorsionQuadraticModule, "finitely_presented_group"):
            try:
                delattr(TorsionQuadraticModule, "finitely_presented_group")
            except AttributeError:
                pass

    if _original_integral_lattice is not None:
        import sage.all
        import sage.modules.free_quadratic_module_integer_symmetric as module

        module.IntegralLattice = _original_integral_lattice
        sage.all.IntegralLattice = _original_integral_lattice
