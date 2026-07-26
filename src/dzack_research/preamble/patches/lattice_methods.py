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
    from sage.rings.rational_field import QQ

    gram = self.gram_matrix().change_ring(QQ)
    left = getattr(x, "vector", lambda: x)()
    right = getattr(y, "vector", lambda: y)()
    return left * gram * right


def div(self: Any, x: Any) -> Any:
    r"""Return the positive generator of $\{\langle x,y\rangle:y\in L\}$."""
    from sage.arith.misc import gcd

    pairings = [self.b(x, basis_vector) for basis_vector in self.basis()]
    value = gcd(pairings)
    assert value >= 0, f"divisor should be non-negative, got {value}"
    return value


def dual_basis(self: Any) -> Any:
    r"""Return the columns of $G^{-1}$ as the dual basis."""
    from sage.rings.rational_field import QQ

    gram = self.gram_matrix().change_ring(QQ)
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
        coordinates = self.coordinate_vector(vector_).change_ring(ZZ)
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
    induced = matrix(ZZ, [[(u * gram * v) for v in lifts] for u in lifts])
    assert induced.is_symmetric(), "induced form is not symmetric"
    if induced.nrows() == 0:
        return induced
    return IntegralLattice(induced)


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


def _latex_(self: Any) -> str:
    r"""Return multi-line LaTeX representation with category, rank, signature, discriminant, and Gram matrix.

    EXAMPLES::

        sage: from dzack_research.preamble import catalogue, patches
        sage: patches.install("lattice_methods")
        sage: from sage.misc.latex import latex
        sage: print(latex(catalogue.U))
        \begin{aligned}
        &L \in \mathrm{Lattices}(\ZZ), \quad \mathrm{rk}(L) = 2, \quad \mathrm{sig}(L) = (1, 1), \quad \mathrm{disc}(L) = -1 \\
        &G_L = \left(\begin{array}{rr}
        0 & 1 \\
        1 & 0
        \end{array}\right)
        \end{aligned}
        sage: patches.uninstall("lattice_methods")
    """
    from sage.misc.latex import latex

    rank = self.rank()
    pos, neg = self.signature_pair()
    disc = self.gram_matrix().det()
    gram_latex = latex(self.gram_matrix())
    return (
        f"\\begin{{aligned}}\n"
        f"&L \\in \\mathrm{{Lattices}}(\\ZZ), \\quad \\mathrm{{rk}}(L) = {rank}, \\quad \\mathrm{{sig}}(L) = ({pos}, {neg}), \\quad \\mathrm{{disc}}(L) = {disc} \\\\\n"
        f"&G_L = {gram_latex}\n"
        f"\\end{{aligned}}"
    )


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
    r"""Call ``direct_sum`` and apply an optional ``names=`` specification."""
    result = _original_direct_sum(self, *others, **kwargs)
    return result if names is None else _apply_names(result, names)


_original_twist: Any = None


def _twist(self: Any, *args: Any, names: Any = None, **kwargs: Any) -> Any:
    r"""``twist`` accepting ``names=``, for ``L.<...> = M.twist(2)``."""
    result = _original_twist(self, *args, **kwargs)
    return result if names is None else _apply_names(result, names)


_CLASS_ATTRS = {
    "_first_ngens": _first_ngens,
    "twist": _twist,
    "__matmul__": _matmul,
    "__pow__": _pow,
    "direct_sum": _direct_sum,
}

_original_integral_lattice: Any = None


def _patched_integral_lattice(*args: Any, names: Any = None, **kwargs: Any) -> Any:
    """``IntegralLattice`` accepting the ``names=`` keyword the preparser emits."""
    lattice = _original_integral_lattice(*args, **kwargs)
    if names is None:
        return lattice

    return _apply_names(lattice, names)


def install() -> None:
    """Install the lattice methods and constructor support.

    EXAMPLES::

        sage: from dzack_research.preamble import patches
        sage: patches.install("lattice_methods")
        sage: "lattice_methods" in patches.installed()
        True
        sage: patches.uninstall("lattice_methods")
    """
    global _original_integral_lattice, _original_direct_sum, _original_twist

    target = _lattice_class()
    if _original_direct_sum is None:
        _original_direct_sum = target.direct_sum
    if _original_twist is None:
        _original_twist = target.twist
    for name in _METHODS:
        attribute = globals()[name]
        if name == "sublattices":
            attribute = property(attribute)
        setattr(target, name, attribute)
        assert hasattr(target, name), f"{target.__name__} rejected {name}"
    for name, attribute in _CLASS_ATTRS.items():
        setattr(target, name, attribute)

    import sage.all
    import sage.modules.free_quadratic_module_integer_symmetric as module

    if _original_integral_lattice is None:
        _original_integral_lattice = module.IntegralLattice
    module.IntegralLattice = _patched_integral_lattice
    sage.all.IntegralLattice = _patched_integral_lattice


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

    if _original_integral_lattice is not None:
        import sage.all
        import sage.modules.free_quadratic_module_integer_symmetric as module

        module.IntegralLattice = _original_integral_lattice
        sage.all.IntegralLattice = _original_integral_lattice
