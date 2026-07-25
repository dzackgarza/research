r"""Lattice methods the old init.sage called but Sage does not provide.

The old init.sage was written against a fork of Sage carrying heavy modifications to
the lattice machinery. This module re-supplies that surface, inferred from how the
source used it: ``q``, ``b``, ``div``, ``dual_basis``, ``e_perp_mod_e``,
``I_perp_mod_I``, ``is_isometric``, ``to_lin_comb_generators``, ``sublattices``, the
``names=`` constructor keyword behind the ``L.<...>`` generator sugar, and ``@``/``**``
as direct sum and power. None of it exists in upstream Sage, so every one of those
call sites raised on this machine -- most visibly the block of theorem statements at
old lines 365-388, which could never have run.

Same placement caveat as ``predicates.py``: the lattice spike is where these notions
belong, sited on the lattice object through the lexicon rather than bolted onto
Sage's class from outside. This is the interim surface that makes the source's own
claims checkable; it is not the destination.

``predicates.e_perp_mod_e`` is the free-function form of the single-vector case;
:func:`I_perp_mod_I` here is the general one and the two agree by construction.
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
)


def _expand_names(spec: str, rank: int) -> tuple[str, ...]:
    r"""Expand a basis-name spec into exactly ``rank`` names.

    Accepts ``"a1..a8"`` (a range) or ``"e, f, ep, fp"`` (an explicit list), or a
    mixture: ``"e, f, a1..a8"``. This is the programmatic form; the generator syntax
    ``L.<a1, ..., a8> = IntegralLattice(...)`` is wired up too and expands the same
    way. See ``tests/test_lattice_generator_syntax.sage``.
    """
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

    assert len(names) == rank, f"spec {spec!r} gives {len(names)} names but the lattice has rank {rank}"
    assert len(set(names)) == len(names), f"duplicate names in {spec!r}"
    return tuple(names)


def with_names(self: Any, spec: str) -> Any:
    r"""Attach basis names to this lattice and return it, for readable notation.

    The programmatic twin of ``L.<e1, ..., en> = IntegralLattice(...)``, which this
    patch also makes work: it supplies the ``names=`` keyword the preparser emits and
    expands the ellipsis range that Sage leaves as a literal ``'Ellipsis'``.

        L = IntegralLattice("E8").with_names("a1..a8")
        L.inject_variables()      # a1, ..., a8 now in scope

    The rank check is the point: a spec whose length disagrees with the rank fails
    loudly, where the Sage sugar would have silently given three generators.
    """
    self._assign_names(_expand_names(spec, self.rank()))
    return self


def to_lin_comb_generators(self: Any, element: Any) -> str:
    r"""Write an element as a linear combination of the named basis.

    ``run_vin`` used this to label roots. Requires names to have been assigned; says
    so rather than inventing indices.
    """
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
    r"""A per-instance dict for recording named sublattices.

    Old line 358 does ``TEn.sublattices.update({...})``, which needs the attribute to
    already exist. Created lazily on first access.
    """
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
    r"""The bilinear form $\langle x, y\rangle = x^{T} G y$.

    Accepts either lattice elements or plain coordinate vectors, because the source's
    configurations mix basis vectors with dual vectors and the latter are rational.
    """
    from sage.rings.rational_field import QQ

    gram = self.gram_matrix().change_ring(QQ)
    left = getattr(x, "vector", lambda: x)()
    right = getattr(y, "vector", lambda: y)()
    return left * gram * right


def div(self: Any, x: Any) -> Any:
    r"""The divisor of $x$: the positive generator of $\{\langle x, y\rangle : y \in L\}$.

    Old lines 366, 373, 386 assert ``div(e) == 1``, ``div(ep) == 2``, ``div(vp) == 2``.
    Computed as the gcd of the pairings of $x$ against a basis, which generates that
    ideal because pairing is linear.
    """
    from sage.arith.misc import gcd

    pairings = [self.b(x, basis_vector) for basis_vector in self.basis()]
    value = gcd(pairings)
    assert value >= 0, f"divisor should be non-negative, got {value}"
    return value


def dual_basis(self: Any) -> Any:
    r"""Columns of $G^{-1}$: the frame dual to the given basis.

    Asserts the defining property $\langle b_i, d_j\rangle = \delta_{ij}$, which the
    source took on faith when it wrote ``Gram.inverse().columns()``.
    """
    from sage.rings.rational_field import QQ

    gram = self.gram_matrix().change_ring(QQ)
    columns = gram.inverse().columns()
    for i, basis_vector in enumerate(self.basis()):
        for j, dual_vector in enumerate(columns):
            expected = 1 if i == j else 0
            assert self.b(basis_vector, dual_vector) == expected, f"dual basis is wrong at ({i}, {j})"
    return columns


def I_perp_mod_I(self: Any, vectors: Any) -> Any:
    r"""$I^{\perp} / I$ for an isotropic sublattice $I = \langle vectors\rangle$.

    The general form of ``e_perp_mod_e``. Old lines 378 and 384 call it on pairs.

    Taken at module level: an isotropic $I$ satisfies $I \subseteq I^{\perp}$, so
    $I^{\perp}$ is always a degenerate lattice and Sage refuses to build one. Only the
    quotient is nondegenerate.
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
            assert pairing == 0, f"I must be isotropic: <v{i}, v{j}> = {pairing}, expected 0"

    gram = self.gram_matrix()
    ambient = FreeModule(ZZ, self.rank())
    pairing_matrix = matrix(ZZ, [gram * row for row in coordinate_rows])
    perp = ambient.submodule(pairing_matrix.right_kernel().basis())
    isotropic = ambient.submodule(coordinate_rows)
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
    r"""Whether two integral lattices are isometric.

    Rank and signature are checked first as cheap necessary conditions. Beyond that
    the two cases are genuinely different, and this does not pretend otherwise:

    - **Definite**: decided exactly, via Sage's ``QuadraticForm`` global equivalence.
    - **Indefinite**: compared by *genus*. Genus equality is necessary always, and is
      also sufficient for indefinite lattices of rank at least 3 by Eichler's strong
      approximation theorem -- so the answer is exact there. For indefinite rank 2 it
      is not sufficient, and this asserts rather than returning a value it cannot
      justify.
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
            assert gram[0, 0] % 2 == 0 and gram[1, 1] % 2 == 0, "binary form conversion needs an even lattice"
            return BinaryQF([gram[0, 0] // 2, gram[0, 1], gram[1, 1] // 2])

        return bool(_binary(self).is_equivalent(_binary(other)))

    return bool(self.genus() == other.genus())


def _expand_ellipsis_names(names: tuple[str, ...]) -> tuple[str, ...]:
    r"""Expand ``('a1', 'Ellipsis', 'a8')`` into ``('a1', 'a2', ..., 'a8')``.

    Sage's preparser turns ``L.<a1,...,a8>`` into a ``names`` tuple whose middle entry
    is the literal string ``'Ellipsis'``; it does not expand the range itself. Nothing
    in Sage attaches meaning to that slot, so it is free to hijack -- which is what
    makes ``L.<a1, ..., a8> = IntegralLattice(...)`` deliverable as real sugar rather
    than a trap.
    """
    import re

    expanded: list[str] = []
    for index, name in enumerate(names):
        if name != "Ellipsis":
            expanded.append(name)
            continue
        assert 0 < index < len(names) - 1, f"'...' needs a name on each side; got {names}"
        before, after = expanded[-1], names[index + 1]
        left = re.fullmatch(r"([A-Za-z_]+)(\d+)", before)
        right = re.fullmatch(r"([A-Za-z_]+)(\d+)", after)
        assert left and right, f"'...' needs indexed names either side: {before}, {after}"
        assert left.group(1) == right.group(1), f"'...' between different stems: {before} and {after}"
        start, stop = int(left.group(2)), int(right.group(2))
        assert stop > start, f"'...' range does not ascend: {before}..{after}"
        expanded.extend(f"{left.group(1)}{i}" for i in range(start + 1, stop))
    return tuple(expanded)


def _first_ngens(self: Any, count: int) -> tuple[Any, ...]:
    r"""Return generators matching the *declared* slots, not the first ``count``.

    With ``L.<a1, ..., a8>`` the preparser emits ``(a1, Ellipsis, a8,) =
    L._first_ngens(3)``. Sage's default would bind ``a8`` to the *third* generator.
    This maps each declared slot to the generator that actually bears that name, so
    ``a8`` is the eighth, and the ``Ellipsis`` slot receives the builtin, which
    nothing reads.
    """
    generators = self.gens()
    spec = getattr(self, "_ellipsis_spec", None)
    if spec is None or len(spec) != count:
        return tuple(generators[:count])

    names = list(self.variable_names())
    return tuple(Ellipsis if slot == "Ellipsis" else generators[names.index(slot)] for slot in spec)


def _matmul(self: Any, other: Any) -> Any:
    r"""``L @ M`` as the orthogonal direct sum, the old init.sage's notation."""
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
    assert len(expanded) == lattice.rank(), f"{declared} expands to {len(expanded)} names but the lattice has rank {lattice.rank()}"
    lattice._assign_names(expanded)
    lattice._ellipsis_spec = declared
    return lattice


_original_direct_sum: Any = None


def _direct_sum(self: Any, *others: Any, names: Any = None, **kwargs: Any) -> Any:
    r"""``direct_sum`` accepting ``names=``.

    Needed because the preparser appends the keyword to the *last call* of the
    right-hand side, so ``L.<e,f,a1,...,a8> = U.direct_sum(E8)`` sends ``names`` here
    rather than to the ``IntegralLattice`` constructor.
    """
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
    """Attach every method and the constructor keyword, asserting each one took.

    **Known limitation:** patching rebinds ``IntegralLattice`` in ``sage.all`` and in
    its defining module. Interactive use resolves the name at call time, so the sugar
    works there. A module that did ``from ... import IntegralLattice`` *before*
    installing keeps the original reference and sees no patch -- import lazily, or
    install first.
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
    """Detach them all, restoring Sage's own surface."""
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
