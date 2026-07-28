r"""``IntegralLattices`` — a category owning the lattice-specific API.

Refine any integral lattice parent into this category to gain::

    q(x), b(x, y), div(x)
    dual_basis(), I_perp_mod_I(vectors), is_isometric(other)
    with_names(spec), to_lin_comb_generators(element), sublattices
    _latex_()                   # multi-line Gram + discriminant display
    _first_ngens(count)         # generator sugar for ``L.<...> = ...``
    twist(*, names=...)         # twisted copy with optional naming
    __matmul__, __pow__, direct_sum   # orthogonal direct sums with subdivisions
    summands()                  # block handles for direct-sum summands
    Aut(), invariant_lattice(action), coinvariant_lattice(action),
    coinvariant_inclusion(action)

Elements gain::

    v * w   →  b(v, w)
    v ** 2  →  q(v)
    v.q(), v.b(w), v.div()
    v.e_perp_mod_e()            # for isotropic vectors

EXAMPLES::

    sage: from dzack_research.preamble import catalogue
    sage: from dzack_research.preamble.categories import IntegralLattices
    sage: from dzack_research.preamble.refine import refine
    sage: L = Lattices.U
    sage: refine(L, IntegralLattices())
    sage: L.q(L.gens()[0])
    0
"""

import re
from typing import Any

from sage.arith.misc import gcd
from sage.categories.category import Category
from sage.categories.modules import Modules
from sage.matrix.constructor import matrix
from sage.matrix.special import identity_matrix
from sage.misc.latex import latex as _latex_fn
from sage.modules.free_module import FreeModule
import sage.modules.free_quadratic_module_integer_symmetric as _sage_fqmis
from sage.modules.free_quadratic_module_integer_symmetric import (
    FreeQuadraticModule_integer_symmetric,
)
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.structure.element import Vector

SageIntegralLattice = _sage_fqmis.IntegralLattice
SageIntegralLattice = getattr(
    SageIntegralLattice,
    "_preamble_native_integral_lattice",
    SageIntegralLattice,
)
IntegralLattice = SageIntegralLattice

class SummandBlock:
    r"""Handle for one orthogonal summand inside a direct-sum lattice.

    Indexing and :meth:`gens` return ambient elements of the sum.
    As a Hom/Aut image of another equal-rank block, the handle expands to a
    generator-wise map.  Equal-rank block sums place a domain block diagonally::

        {a1: b1, a2: b2 + b3}   # block columns of the Hom matrix

    so ``b2 + b3`` is the sequence ``(b2[i] + b3[i])_i`` (the lattice map
    \(N(2)\hookrightarrow N\oplus N\) when the forms match).
    """

    __slots__ = ("_ambient", "_lattice", "_start", "_rank", "_name")

    def __init__(
        self,
        ambient: Any,
        lattice: Any,
        start: int,
        rank: int,
        name: str | None = None,
    ) -> None:
        self._ambient = ambient
        self._lattice = lattice
        self._start = int(start)
        self._rank = int(rank)
        self._name = name

    @property
    def lattice(self) -> Any:
        """The abstract summand lattice."""
        return self._lattice

    @property
    def ambient(self) -> Any:
        """The direct-sum lattice containing this block."""
        return self._ambient

    @property
    def inclusion(self) -> Any:
        """The inclusion Hom ``summand → ambient``."""
        gens = list(self._ambient.gens())[self._start : self._start + self._rank]
        return self._lattice.Hom(self._ambient)(gens)

    def gens(self) -> tuple:
        """Ambient generators spanning this block."""
        return tuple(self._ambient.gens()[self._start : self._start + self._rank])

    def __getitem__(self, index: int) -> Any:
        return self.gens()[index]

    def __len__(self) -> int:
        return self._rank

    def __neg__(self) -> tuple:
        return tuple(-g for g in self.gens())

    def __add__(self, other: Any) -> Any:
        """Equal-rank gen-wise sum of blocks (or of a prior sum sequence)."""
        return _block_combine(self, other, 1)

    def __radd__(self, other: Any) -> Any:
        """Support ``(b1 + b2) + b3`` when the left operand is already a sequence."""
        return _block_combine(other, self, 1)

    def __sub__(self, other: Any) -> Any:
        """Equal-rank gen-wise difference of blocks (or of a prior sum sequence)."""
        return _block_combine(self, other, -1)

    def __rsub__(self, other: Any) -> Any:
        """Support ``seq - block`` when the left operand is already a sequence."""
        return _block_combine(other, self, -1)

    def __repr__(self) -> str:
        label = self._name if self._name is not None else f"[{self._start}:{self._start + self._rank}]"
        return f"SummandBlock({label}, rank={self._rank})"

def _block_gens(part: Any) -> tuple:
    """Ambient generators from a :class:`SummandBlock` or an equal-length sequence."""
    if isinstance(part, SummandBlock):
        return part.gens()
    if isinstance(part, (list, tuple)) and not hasattr(part, "parent"):
        return tuple(part)
    raise TypeError(
        f"block combination expects SummandBlock or sequence, got {type(part)!r}"
    )

def _block_combine(left: Any, right: Any, sign: int) -> Any:
    """Gen-wise ``left[i] + sign * right[i]`` for equal-rank block images."""
    if left is None or right is None:
        return NotImplemented
    try:
        left_gens = _block_gens(left)
        right_gens = _block_gens(right)
    except TypeError:
        return NotImplemented
    assert len(left_gens) == len(right_gens), (
        f"block ranks differ: {len(left_gens)} vs {len(right_gens)}"
    )
    return tuple(left_gens[i] + sign * right_gens[i] for i in range(len(left_gens)))

def _summand_records(lattice: Any) -> list[dict[str, Any]]:
    """Ordered summand metadata; a non-sum is a single full-rank record."""
    existing = getattr(lattice, "_preamble_summands", None)
    if existing is not None:
        return [dict(rec) for rec in existing]
    return [
        {
            "lattice": lattice,
            "start": 0,
            "rank": int(lattice.rank()),
            "name": None,
        }
    ]

def _attach_summand_records(
    result: Any,
    left: Any,
    right: Any,
    left_rank: int,
    block_names: Any = None,
) -> None:
    """Store flattened summand records on ``result`` after ``left ⊕ right``."""
    records = _summand_records(left)
    for rec in _summand_records(right):
        records.append(
            {
                "lattice": rec["lattice"],
                "start": left_rank + int(rec["start"]),
                "rank": int(rec["rank"]),
                "name": rec.get("name"),
            }
        )
    if block_names is not None:
        names = tuple(block_names)
        assert len(names) == len(records), (
            f"block_names length {len(names)} != number of summands {len(records)}"
        )
        for rec, name in zip(records, names):
            rec["name"] = name
    result._preamble_summands = records

def expand_block_hom_dict(domain: Any, mapping: dict) -> list:
    r"""Expand a Hom/Aut dict with block keys/values to ordered generator images.

    Keys may be :class:`SummandBlock` handles or ambient generators.  Values may
    be ambient elements, equal-rank blocks, equal-rank block sums
    (``b2 + b3``), or sequences of ambient elements (including ``-block``).
    """
    images: dict[Any, Any] = {}
    for key, val in mapping.items():
        if isinstance(key, SummandBlock):
            src_gens = key.gens()
            if isinstance(val, SummandBlock):
                dst_gens = val.gens()
                assert len(src_gens) == len(dst_gens), (
                    f"block ranks differ: {len(src_gens)} vs {len(dst_gens)}"
                )
                for src, dst in zip(src_gens, dst_gens):
                    images[unwrap(src)] = unwrap(dst)
            elif isinstance(val, (list, tuple)) and not hasattr(val, "parent"):
                assert len(val) == len(src_gens), (
                    f"image sequence length {len(val)} != block rank {len(src_gens)}"
                )
                for src, dst in zip(src_gens, val):
                    images[unwrap(src)] = unwrap(dst)
            else:
                assert len(src_gens) == 1, (
                    "non-block Hom image requires a rank-1 source block "
                    f"(got rank {len(src_gens)})"
                )
                images[unwrap(src_gens[0])] = unwrap(val)
        else:
            if isinstance(val, SummandBlock):
                assert len(val) == 1, (
                    "generator key with block value requires a rank-1 block"
                )
                images[unwrap(key)] = unwrap(val[0])
            else:
                images[unwrap(key)] = unwrap(val)

    ordered = []
    for gen in domain.gens():
        key = unwrap(gen)
        assert key in images, f"missing image for generator {gen}"
        ordered.append(images[key])
    return ordered

# Keep a reference to Sage's native direct_sum so we can call it from inside
# the category without depending on any patches that may replace it.
_native_direct_sum = FreeQuadraticModule_integer_symmetric.direct_sum
_native_twist = FreeQuadraticModule_integer_symmetric.twist

class IntegralLattices(Category):
    r"""Category of integral lattices with enriched computational methods.

    Unlike Sage's default::

        - quadratic and bilinear forms via ``q`` / ``b`` / ``div``
        - dual basis, isotropic quotients, isometry checking
        - basis naming, linear-combination display, LaTeX with discriminant-group info
        - orthogonal direct sums with automatic Gram-matrix subdivisions
        - lattice-element arithmetic: multiplication -> bilinear pairing, exponentiation -> q
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "integral lattices"

    def super_categories(self) -> list:
        return [Modules(ZZ)]

    class ParentMethods:
        r"""Methods available on every integral lattice parent refined into this category."""

        # ---- bilinear / quadratic API ----

        def q(self: Any, x: Any) -> Any:
            r"""Return the quadratic form $q(x) = \langle x, x\rangle$."""
            return self.b(x, x)

        def b(self: Any, x: Any, y: Any) -> Any:
            r"""Return the pairing $\langle x, y\rangle = x^T G y$."""
            vx = _unwrap(x)
            vy = _unwrap(y)
            return (vx * self.gram_matrix()).dot_product(vy)

        def div(self: Any, x: Any) -> Any:
            r"""Return the positive generator of $\{\langle x, y\rangle : y \in L\}$."""
            pairings = [self.b(x, v) for v in self.basis()]
            return abs(gcd(pairings))

        # ---- dual basis ----

        def dual_basis(self: Any) -> Any:
            r"""Return the columns of $G^{-1}$ as the dual basis.

            These lie in $L\\otimes\\mathbb{Q}$, not necessarily in $L$, so they
            are returned as ambient vectors (not lattice-element facades).
            """
            columns = self.gram_matrix().inverse().columns()
            for i, v in enumerate(self.basis()):
                for j, w in enumerate(columns):
                    expected = 1 if i == j else 0
                    assert self.b(v, w) == expected, (
                        f"dual basis is wrong at ({i}, {j})"
                    )
            return columns

        # ---- isotropic quotients ----

        def I_perp_mod_I(self: Any, vectors: Any) -> Any:
            r"""Return $I^\perp / I$ as an integral lattice with the induced form."""
            from sage.modules.free_quadratic_module_integer_symmetric import (
                IntegralLattice,
            )

            # FreeModule / Gram arithmetic must see native Cython vectors.
            with without_element_wrap():
                coordinate_rows = []
                for v in vectors:
                    coordinate_rows.append(
                        self.coordinate_vector(_unwrap(v)).change_ring(ZZ)
                    )

                gram = self.gram_matrix()
                for i, left in enumerate(coordinate_rows):
                    for j, right in enumerate(coordinate_rows):
                        pairing = (left * gram).dot_product(right)
                        assert pairing == 0, (
                            f"I must be isotropic: <v{i}, v{j}> = {pairing}, expected 0"
                        )

                free = FreeModule(ZZ, self.rank())
                pairing_matrix = matrix(ZZ, [gram * row for row in coordinate_rows])
                perp = free.submodule(pairing_matrix.right_kernel().basis())
                isotropic = free.submodule(coordinate_rows)
                quotient = perp / isotropic

                lifts = [gen.lift() for gen in quotient.gens()]
                induced = matrix(
                    ZZ,
                    [[(u * gram * v) for v in lifts] for u in lifts],
                )
                assert induced.is_symmetric(), "induced form is not symmetric"
                if induced.nrows() == 0:
                    return induced
                lattice = IntegralLattice(induced)

            refine_one_lattice(lattice)
            return lattice

        # ---- isometry ----

        def is_isometric(self: Any, other: Any) -> bool:
            r"""Return whether two integral lattices are isometric."""
            from sage.quadratic_forms.binary_qf import BinaryQF
            from sage.quadratic_forms.quadratic_form import QuadraticForm

            if self.rank() != other.rank():
                return False
            if self.signature_pair() != other.signature_pair():
                return False

            pos, neg = self.signature_pair()
            if pos == 0 or neg == 0:
                sign = 1 if neg == 0 else -1
                return bool(
                    QuadraticForm(sign * self.gram_matrix())
                    .is_globally_equivalent_to(
                        QuadraticForm(sign * other.gram_matrix())
                    )
                )

            if self.rank() == 2:

                def _binary(L):
                    g = L.gram_matrix()
                    assert g[0, 0] % 2 == 0 and g[1, 1] % 2 == 0
                    return BinaryQF([g[0, 0] // 2, g[0, 1], g[1, 1] // 2])

                return bool(_binary(self).is_equivalent(_binary(other)))

            return bool(self.genus() == other.genus())

        # ---- Nikulin / signature predicates ----

        def is_coeven(self: Any) -> bool:
            r"""Return whether the discriminant form is integer-valued ($\delta=0$)."""
            from sage.rings.infinity import Infinity
            from sage.rings.rational_field import QQ

            # keep native Cython vectors for that path.
            with without_element_wrap():
                disc = self.discriminant_group()
            assert disc.cardinality() < Infinity, (
                "discriminant group is infinite; the lattice must be nondegenerate"
            )
            return all(QQ(element.q()).denominator() == 1 for element in disc)

        def is_coodd(self: Any) -> bool:
            """Return the negation of :meth:`is_coeven`."""
            return not self.is_coeven()

        def delta(self: Any) -> Integer:
            r"""Return Nikulin's invariant $\delta\in\{0,1\}$."""
            return Integer(0) if self.is_coeven() else Integer(1)

        def is_p_elementary(self: Any, p: Any) -> bool:
            r"""Return whether the discriminant group $A_L$ is elementary abelian of exponent $p$.

            Defers to :meth:`DiscriminantQuadraticModules.ParentMethods.is_p_elementary`
            on ``self.discriminant_group()``.
            """
            with without_element_wrap():
                disc = self.discriminant_group()
            return bool(disc.is_p_elementary(p))

        def is_elliptic(self: Any) -> bool:
            """Return whether the lattice is negative definite."""
            return bool((-self.gram_matrix()).is_positive_definite())

        def is_parabolic(self: Any) -> bool:
            """Return whether the lattice is negative semidefinite."""
            return bool((-self.gram_matrix()).is_positive_semidefinite())

        # ---- naming and display ----

        def with_names(self: Any, spec: str) -> Any:
            r"""Attach basis names from a compact spec and return the lattice.

            EXAMPLES::

                sage: from dzack_research.preamble import catalogue
                sage: Lattices.E8.with_names("a1..a8").variable_names()
                ('a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8')
            """
            self._assign_names(_expand_names(spec, self.rank()))
            return self

        def to_lin_comb_generators(self: Any, element: Any) -> str:
            r"""Return an element as a linear combination of the named basis."""
            names = self.variable_names()
            coords = self.coordinate_vector(_unwrap(element))
            terms = []
            for name, c in zip(names, coords, strict=True):
                if c == 0:
                    continue
                if c == 1:
                    terms.append(name)
                elif c == -1:
                    terms.append(f"-{name}")
                else:
                    terms.append(f"{c}*{name}")
            return " + ".join(terms).replace("+ -", "- ") if terms else "0"

        @property
        def sublattices(self: Any) -> dict:
            r"""Return the per-instance dictionary of named sublattices."""
            existing = self.__dict__.get("_sublattices")
            if existing is None:
                existing = {}
                self._sublattices = existing
            return existing

        # ---- generators (wrap Cython vectors at the API boundary) ----

        def gens(self: Any, *args: Any, **kwargs: Any) -> Any:
            native = super(IntegralLattices.ParentMethods, self).gens(*args, **kwargs)
            wrapped = [wrap_element(self, g) for g in native]
            return type(native)(wrapped) if not isinstance(native, list) else wrapped

        def basis(self: Any, *args: Any, **kwargs: Any) -> Any:
            native = super(IntegralLattices.ParentMethods, self).basis(*args, **kwargs)
            # Preserve the native container type: Sage internals (e.g.
            # discriminant_group) concatenate ``basis()`` with lists.
            wrapped = [wrap_element(self, g) for g in native]
            return type(native)(wrapped) if not isinstance(native, list) else wrapped

        def __call__(self: Any, *args: Any, **kwargs: Any) -> Any:
            """Construct a lattice element on the owned facade interface."""
            if _WRAP_DEPTH:
                return super(IntegralLattices.ParentMethods, self).__call__(
                    *args, **kwargs
                )
            facade_cls = getattr(self, "_preamble_element_class", None)
            if facade_cls is not None and len(args) == 1 and not kwargs:
                return facade_cls(self, unwrap(args[0]))
            result = super(IntegralLattices.ParentMethods, self).__call__(
                *args, **kwargs
            )
            return wrap_element(self, result)

        def coordinate_vector(self: Any, v: Any, *args: Any, **kwargs: Any) -> Any:
            r"""Return coordinates of ``v``; unwrap facades and suppress wrapping.

            Sage's ``FreeModuleHomspace(list)`` builds the morphism matrix via
            ``codomain.coordinates`` → ``coordinate_vector``.  That path compares
            against ``basis()``; if basis elements are facades, Cython
            ``Element.__richcmp__`` recurses through coercion and segfaults.
            Run the native coordinate computation with wrapping suppressed so the
            basis stays native for the duration of the call.
            """
            with without_element_wrap():
                return super(IntegralLattices.ParentMethods, self).coordinate_vector(
                    _unwrap(v), *args, **kwargs
                )

        def coordinates(self: Any, v: Any, *args: Any, **kwargs: Any) -> Any:
            """Return ``coordinate_vector(v)`` as a list (Hom(list) entry point)."""
            return self.coordinate_vector(v, *args, **kwargs).list()

        # ---- orthogonal direct sum / twist ----

        def direct_sum(
            self: Any,
            *others: Any,
            names: Any = None,
            block_names: Any = None,
            **kwargs: Any,
        ) -> Any:
            r"""Orthogonal direct sum preserving Gram subdivisions and summand blocks.

            Nested sums flatten to a top-level ordered summand list.  Optional
            ``block_names`` labels the resulting blocks for :meth:`summands`.
            """
            if not others:
                return self

            result = self
            n_others = len(others)
            for index, other in enumerate(others):
                left = result
                left_subdivs = left.gram_matrix().subdivisions()[0] or ()
                left_rank = left.rank()
                right_subdivs = other.gram_matrix().subdivisions()[0] or ()

                with without_element_wrap():
                    result = _native_direct_sum(left, other, **kwargs)
                refine_one_lattice(result)

                combined = (
                    list(left_subdivs)
                    + [left_rank]
                    + [left_rank + s for s in right_subdivs]
                )
                _subdivide_gram(result, combined)
                names_here = block_names if index == n_others - 1 else None
                _attach_summand_records(result, left, other, left_rank, names_here)

            if names is not None:
                result = _apply_names(result, names)
            return result

        def summands(self: Any) -> tuple:
            r"""Return ordered :class:`SummandBlock` handles for this direct sum.

            A lattice that is not a recorded direct sum yields a single block
            covering the whole lattice.
            """
            return tuple(
                SummandBlock(
                    self,
                    rec["lattice"],
                    rec["start"],
                    rec["rank"],
                    rec.get("name"),
                )
                for rec in _summand_records(self)
            )

        def twist(self: Any, *args: Any, names: Any = None, **kwargs: Any) -> Any:
            r"""Twisted (sign-flipped) lattice, preserving Gram-matrix subdivisions."""
            subdivs = self.gram_matrix().subdivisions()
            with without_element_wrap():
                result = _native_twist(self, *args, **kwargs)
            refine_one_lattice(result)
            if subdivs != ([], []):
                _subdivide_gram(result, subdivs[0], subdivs[1])
            if names is not None:
                result = _apply_names(result, names)
            return result

        def _compute_lattice_gram_subdivisions(self: Any) -> list[int]:
            r"""Detect and apply Gram-matrix block subdivisions from connected components."""
            return compute_lattice_gram_subdivisions(self)

        # ---- morphisms / automorphisms ----

        def Hom(self: Any, *args: Any, **kwargs: Any) -> Any:
            r"""Return $\mathrm{Hom}(L,M)$ with matrix-based morphism apply.

            Construction is the usual list-of-images / matrix constructor.
            Application bypasses Sage ``Map`` coercion (which SIGSEGVs once
            lattices are facade-refined) and uses coordinates × matrix.
            """
            with without_element_wrap():
                hom = super(IntegralLattices.ParentMethods, self).Hom(
                    *args, **kwargs
                )
            return refine(hom, LatticeHomomorphisms())

        def Aut(self: Any) -> Any:
            r"""Return $\mathrm{Aut}(L)=O(L)$ as an endomorphism Homset.

            Elements are constructed by generator images or matrix:
            ``L.Aut()({e: image, ...})`` / ``L.Aut()([images...])`` /
            ``L.Aut()(matrix)``.  Isometry is checked on ``morphism.to_matrix()``.
            """
            cached = self.__dict__.get("_preamble_Aut")
            if cached is not None:
                return cached
            with without_element_wrap():
                # Hom already refines into LatticeHomomorphisms; Aut adds
                # the isometry check on top.
                hom = self.Hom(self)
            refined = refine(hom, LatticeIsometries())
            self._preamble_Aut = refined
            return refined

        def invariant_lattice(self: Any, action: Any) -> Any:
            r"""Return the fixed sublattice $L^G$ under a group action on $L$.

            ``action`` is an isometry (morphism or matrix), or an iterable of
            generators of a finite group of isometries.
            """
            return self._induced_lattice(self._invariant_coordinate_basis(action))

        def _coinvariant_coordinate_basis(self: Any, action: Any) -> list[Any]:
            r"""Return a $\ZZ$-basis of the coinvariant sublattice $(L^G)^{\perp L}$."""
            inv_basis = self._invariant_coordinate_basis(action)
            gram = self.gram_matrix()
            free = FreeModule(ZZ, self.rank())
            if inv_basis:
                pairing = matrix(ZZ, [gram * row for row in inv_basis])
                perp = free.submodule(pairing.right_kernel().basis())
            else:
                perp = free
            return list(perp.basis())

        def coinvariant_lattice(self: Any, action: Any) -> Any:
            r"""Return the coinvariant sublattice $(L^G)^{\perp L}$ with induced form."""
            return self._induced_lattice(self._coinvariant_coordinate_basis(action))

        def coinvariant_inclusion(self: Any, action: Any) -> Any:
            r"""Return the primitive inclusion $(L^G)^{\perp L}\hookrightarrow L$."""
            basis = self._coinvariant_coordinate_basis(action)
            coinvariant = self._induced_lattice(basis)
            images = [self(list(row)) for row in basis]
            return coinvariant.Hom(self)(images)

        def _invariant_coordinate_basis(self: Any, action: Any) -> list[Any]:
            """Return a ZZ-basis of $\\bigcap_g \\ker(g-\\mathrm{id})$."""
            mats = _action_matrices(action)
            size = self.rank()
            free = FreeModule(ZZ, size)
            fixed = free
            for mat in mats:
                assert mat.nrows() == size == mat.ncols(), (
                    f"action matrix shape {mat.nrows()}×{mat.ncols()} "
                    f"does not match rank {size}"
                )
                ker = (mat - identity_matrix(ZZ, size)).right_kernel()
                fixed = fixed.intersection(ker)
            return list(fixed.basis())

        def _induced_lattice(self: Any, coordinate_basis: Any) -> Any:
            """Return the integral lattice with Gram form induced on ``coordinate_basis``."""
            basis = list(coordinate_basis)
            if not basis:
                return None
            gram = self.gram_matrix()
            induced = matrix(
                ZZ,
                [[u * gram * v for v in basis] for u in basis],
            )
            assert induced.is_symmetric(), (
                "induced form on the sublattice is not symmetric"
            )
            lattice = IntegralLattice(induced)
            refine_one_lattice(lattice)
            return lattice

        # ---- constructor sugar ----

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

        def __matmul__(self: Any, other: Any) -> Any:
            r"""``L @ M`` as the orthogonal direct sum."""
            return self.direct_sum(other)

        def __add__(self: Any, other: Any) -> Any:
            r"""``L + M`` as the orthogonal direct sum (for ``sum([...])``)."""
            return self.direct_sum(other)

        def __radd__(self: Any, other: Any) -> Any:
            """Allow ``sum([L, M, ...])`` (Python starts from ``0``)."""
            if other == 0:
                return self
            return NotImplemented

        def __pow__(self: Any, exponent: Any, names: Any = None) -> Any:
            r"""``L ** n`` as the ``n``-fold orthogonal direct sum."""
            n = int(exponent)
            assert n >= 1, f"lattice power needs a positive exponent, got {exponent}"
            result = self
            for _ in range(n - 1):
                result = result.direct_sum(self)
            if names is not None:
                result = _apply_names(result, names)
            return result

        # ---- LaTeX ----

        def _latex_(self: Any) -> str:
            r"""Multi-line LaTeX with rank, signature, discriminant, Gram, discriminant group."""
            rank = self.rank()
            pos, neg = self.signature_pair()
            disc = self.gram_matrix().det()
            disc_latex = _format_disc_latex(disc)
            gram_latex = str(_latex_fn(self.gram_matrix()))
            if _zero_dots():
                gram_latex = re.sub(r"\b0\b", lambda m: r"\cdot", gram_latex)

            A = self.discriminant_group()
            A_latex = str(_latex_fn(A))
            A_lines = [line for line in A_latex.splitlines() if line]
            assert A_lines[0].strip() == r"\begin{gathered}"
            assert A_lines[-1].strip() == r"\end{gathered}"
            A_lines = A_lines[1:-1]

            header = [
                r"\begin{gathered}",
                (
                    f"L \\in \\mathrm{{Lattices}}(\\mathbb{{Z}}), "
                    f"\\quad \\mathrm{{rk}}(L) = {rank}, "
                    f"\\quad \\mathrm{{sig}}(L) = ({pos}, {neg}), "
                    f"\\quad \\mathrm{{disc}}(L) = {disc_latex} \\\\"
                ),
                f"G_L = {gram_latex} \\\\",
            ]
            return "\n".join(header + A_lines + [r"\end{gathered}"])

    class ElementMethods:
        r"""Methods available on elements of lattices refined into this category."""

        def q(self: Any) -> Any:
            r"""Return $q(v) = \langle v, v\rangle$."""
            return self.parent().q(self)

        def b(self: Any, other: Any) -> Any:
            r"""Return $b(v, w) = \langle v, w\rangle$."""
            return self.parent().b(self, other)

        def div(self: Any) -> Any:
            r"""Return the divisibility of this vector."""
            return self.parent().div(self)

        def __mul__(self: Any, other: Any) -> Any:
            r"""``v * w`` -> bilinear pairing; ``v * n`` -> scalar multiplication."""
            from sage.structure.element import Element, Matrix

            if isinstance(other, (int, Integer)):
                return self.parent()(Integer(other) * _unwrap(self))
            if isinstance(other, Matrix):
                return self.parent().b(self, other)
            if isinstance(other, Element):
                return self.parent().b(self, other)
            if isinstance(other, Vector):
                return self.parent().b(self, other)
            return NotImplemented

        def __rmul__(self: Any, other: Any) -> Any:
            r"""``n * v`` -> scalar multiplication."""
            if isinstance(other, (int, Integer)):
                return self.parent()(Integer(other) * _unwrap(self))
            return NotImplemented

        def __add__(self: Any, other: Any) -> Any:
            """Vector addition on the owned element interface."""
            return _element_add(self, other, 1)

        def __radd__(self: Any, other: Any) -> Any:
            return _element_add(other, self, 1)

        def __sub__(self: Any, other: Any) -> Any:
            return _element_add(self, other, -1)

        def __rsub__(self: Any, other: Any) -> Any:
            return _element_add(other, self, -1)

        def __neg__(self: Any) -> Any:
            """``-v`` via the owned element interface."""
            return self.parent()(-_unwrap(self))

        def __pow__(self: Any, exponent: Any, mod: Any = None) -> Any:
            r"""``v ** 2`` -> $q(v)$."""
            if exponent == 2:
                return self.q()
            raise NotImplementedError(f"exponent {exponent} not supported")

        def e_perp_mod_e(self: Any) -> Any:
            r"""$e^\perp / \langle e \rangle$ for a single isotropic $e$."""
            return self.parent().I_perp_mod_I([self])

# ---- helper utilities ----

_ZERO_DOTS: bool = True

def set_zero_dots(enabled: bool = True) -> None:
    r"""Toggle replacing 0 entries with $\cdot$ in lattice LaTeX."""
    global _ZERO_DOTS
    _ZERO_DOTS = bool(enabled)

def _zero_dots() -> bool:
    return _ZERO_DOTS

def _unwrap(x: Any) -> Any:
    r"""Unwrap an element facade if present; otherwise return ``x``."""
    return unwrap(x)

def _element_add(left: Any, right: Any, sign: int) -> Any:
    """Add/subtract lattice elements coordinate-wise, returning a lattice element.

    Arithmetic runs on native vectors; the parent constructor re-wraps.
    """
    from sage.modules.free_module_element import vector
    from sage.rings.rational_field import QQ

    if left is None:
        return NotImplemented
    try:
        left_coords = vector(QQ, list(_unwrap(left)))
    except (TypeError, ValueError, AttributeError):
        return NotImplemented

    if right is None:
        result = sign * left_coords
        parent = left.parent()
    else:
        try:
            right_coords = vector(QQ, list(_unwrap(right)))
        except (TypeError, ValueError, AttributeError):
            return NotImplemented
        result = left_coords + sign * right_coords
        parent = left.parent() if hasattr(left, "parent") else right.parent()

    if all(QQ(x).denominator() == 1 for x in result):
        try:
            return parent([ZZ(x) for x in result])
        except (TypeError, ValueError, ArithmeticError):
            pass
    return result

def _expand_names(spec: str, rank: int) -> tuple[str, ...]:
    r"""Expand indexed ranges in a basis-name specification."""
    names: list[str] = []
    for piece in (p.strip() for p in spec.split(",")):
        assert piece, f"empty name in spec {spec!r}"
        match = re.fullmatch(r"([A-Za-z_]+)(\d+)\.\.\1?(\d+)", piece)
        if match:
            stem, start, stop = match.group(1), int(match.group(2)), int(match.group(3))
            names.extend(f"{stem}{i}" for i in range(start, stop + 1))
        else:
            assert re.fullmatch(r"[A-Za-z_]\w*", piece), f"invalid name: {piece!r}"
            names.append(piece)

    assert len(names) == rank, (
        f"spec {spec!r} gives {len(names)} names but rank is {rank}"
    )
    assert len(set(names)) == rank, f"duplicate names in {spec!r}"
    return tuple(names)

def _expand_ellipsis_names(names: tuple[str, ...]) -> tuple[str, ...]:
    r"""Expand ``('a1','Ellipsis','a8')`` through ``'a8'``."""
    expanded: list[str] = []
    for i, name in enumerate(names):
        if name != "Ellipsis":
            expanded.append(name)
            continue
        assert 0 < i < len(names) - 1, (
            f"'...' needs a name on each side; got {names}"
        )
        before, after = expanded[-1], names[i + 1]
        # Allow an alphabetic suffix so ``a1t, ..., a8t`` expands.
        left = re.fullmatch(r"([A-Za-z_]+)(\d+)([A-Za-z_]*)", before)
        right = re.fullmatch(r"([A-Za-z_]+)(\d+)([A-Za-z_]*)", after)
        assert left and right, f"'...' needs indexed names: {before}, {after}"
        assert left.group(1) == right.group(1) and left.group(3) == right.group(3), (
            f"'...' between different stems: {before} and {after}"
        )
        start, stop = int(left.group(2)), int(right.group(2))
        assert stop > start, f"'...' range does not ascend: {before}..{after}"
        stem, suffix = left.group(1), left.group(3)
        expanded.extend(f"{stem}{i}{suffix}" for i in range(start + 1, stop))
    return tuple(expanded)

def _apply_names(lattice: Any, names: Any) -> Any:
    r"""Expand a declared name tuple onto a lattice, checking rank."""
    declared = tuple(names)
    expanded = _expand_ellipsis_names(declared)
    assert len(expanded) == lattice.rank(), (
        f"{declared} expands to {len(expanded)} names but rank is {lattice.rank()}"
    )
    lattice._assign_names(expanded)
    lattice._ellipsis_spec = declared
    return lattice

def _subdivide_gram(L: Any, *cuts: Any) -> None:
    r"""Subdivide a lattice's Gram matrix, handling immutability."""
    gram = L.gram_matrix()
    if gram.is_immutable():
        from copy import copy

        gram = copy(gram)
        try:
            L._gram_matrix = gram
        except AttributeError:
            pass
    gram.subdivide(*cuts)

def _detect_matrix_connected_cuts(G: Any) -> list[int]:
    r"""Detect connected-component cuts in a matrix graph for block subdivision.

    Uses networkx (if available) to find connected components of the
    adjacency graph defined by nonzero entries.
    """
    n = G.nrows()
    if n <= 1:
        return []
    try:
        import networkx as nx
    except ImportError:
        return []
    adj = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if G[i, j] != 0:
                adj[i].append(j)
                adj[j].append(i)
    graph = nx.Graph(adj)
    comps = sorted(
        [sorted(c) for c in nx.connected_components(graph)],
        key=lambda c: c[0],
    )
    if [i for c in comps for i in c] != list(range(n)):
        return []
    cuts, cur = [], 0
    for s in (len(c) for c in comps[:-1]):
        cur += s
        cuts.append(cur)
    return [c for c in cuts if 0 < c < n]

def compute_lattice_gram_subdivisions(L: Any) -> list[int]:
    r"""Module-level helper: detect and apply Gram-matrix block subdivisions.

    Can be called before a lattice is refined into a category, so it lives
    at module level rather than in ``ParentMethods``.
    """
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

def _format_disc_latex(disc: int) -> str:
    r"""Format discriminant with prime factorization in LaTeX."""
    from sage.arith.misc import factor

    if disc in (-1, 0, 1):
        return str(disc)
    f = factor(disc)
    f_latex = str(_latex_fn(f))
    return f"{disc} = {f_latex}" if f_latex != str(disc) else str(disc)

# ---- lattice-specific refinement lifecycle ----

def _action_matrices(action: Any) -> list[Any]:
    """Normalize a group action to a list of integer matrices."""
    if hasattr(action, "to_matrix") and callable(action.to_matrix):
        return [matrix(ZZ, action.to_matrix())]
    if hasattr(action, "matrix") and callable(action.matrix):
        return [matrix(ZZ, action.matrix())]
    if isinstance(action, (list, tuple)) and action and not hasattr(action, "nrows"):
        matrices: list[Any] = []
        for generator in action:
            matrices.extend(_action_matrices(generator))
        return matrices
    return [matrix(ZZ, action)]

def refine_one_lattice(lattice: Any) -> None:
    r"""Refine a single integral lattice into the appropriate categories.

    Always refines into ``IntegralLattices``.  If signature is ``(n, 1)``,
    also joins ``HyperbolicLattices``.
    """
    refine(lattice, IntegralLattices())
    pos, neg = lattice.signature_pair()
    if pos > 0 and neg > 0 and min(pos, neg) == 1:
        refine(lattice, HyperbolicLattices())

def _after_lattice_init(lattice: Any) -> None:
    compute_lattice_gram_subdivisions(lattice)

def _is_hyperbolic(lattice: Any) -> bool:
    pos, neg = lattice.signature_pair()
    return pos > 0 and neg > 0 and min(pos, neg) == 1

_INTEGRAL_LATTICES_INSTALLED = False


def _integral_lattice_with_names(*args: Any, names: Any = None, **kwargs: Any) -> Any:
    r"""``IntegralLattice(..., names=(...))`` for ``L.<gens> = IntegralLattice(...)``."""
    lattice = SageIntegralLattice(*args, **kwargs)
    if names is not None:
        lattice = _apply_names(lattice, names)
    return lattice


_integral_lattice_with_names._preamble_native_integral_lattice = SageIntegralLattice


def install_integral_lattices() -> None:
    """Hook post-init and shadow ``IntegralLattice`` with the preamble constructor."""
    global _INTEGRAL_LATTICES_INSTALLED
    if _INTEGRAL_LATTICES_INSTALLED:
        return

    hook_post_init(
        FreeQuadraticModule_integer_symmetric,
        IntegralLattices(),
        after=_after_lattice_init,
    )
    hook_post_init(
        FreeQuadraticModule_integer_symmetric,
        HyperbolicLattices(),
        predicate=_is_hyperbolic,
    )

    _sage_fqmis.IntegralLattice = _integral_lattice_with_names
    import sage.all as _sage_all

    _sage_all.IntegralLattice = _integral_lattice_with_names
    globals()["IntegralLattice"] = _integral_lattice_with_names

    _INTEGRAL_LATTICES_INSTALLED = True
