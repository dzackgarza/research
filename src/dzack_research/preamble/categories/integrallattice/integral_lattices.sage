r"""``IntegralLattices`` — a category owning the lattice-specific API.

Refine any integral lattice parent into this category to gain::

    q(x), b(x, y), div(x)
    dual_basis(), I_perp_mod_I(vectors), is_isometric(other)
    with_names(spec), to_lin_comb_generators(element), sublattices
    _latex_()                   # multi-line Gram + discriminant display
    _first_ngens(count)         # generator sugar for ``L.<...> = ...``
    twist(*, names=...)         # twisted copy with optional naming
    __add__, __pow__, direct_sum      # orthogonal direct sums with subdivisions
    Aut(), invariant_lattice(action), coinvariant_lattice(action),
    coinvariant_inclusion(action)

Elements gain::

    v * w   →  b(v, w)
    v ^ 2  →  q(v)
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
from sage.rings.rational_field import QQ
from sage.structure.element import Vector

SageIntegralLattice = _sage_fqmis.IntegralLattice
SageIntegralLattice = getattr(
    SageIntegralLattice,
    "_preamble_native_integral_lattice",
    SageIntegralLattice,
)
IntegralLattice = SageIntegralLattice

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

        def get_isotropic_type(self: Any, isotropic_element: Any) -> str:
            r"""Classify an isotropic element by the type of $e^\perp / e$.

            The method is defined for elements of every integral lattice. It
            returns ``"Odd"``, ``"Even ordinary"``, ``"Even characteristic"``,
            or ``"Not found."`` when the quotient has another isometry type.
            """
            assert getattr(isotropic_element, "parent", lambda: None)() is self, (
                "get_isotropic_type expects an element of this lattice"
            )
            assert self.q(isotropic_element) == 0, (
                f"expected an isotropic element, got square {self.q(isotropic_element)}"
            )

            from dzack_research.preamble import catalogue

            quotient = self.I_perp_mod_I([isotropic_element])
            if not hasattr(quotient, "is_isometric") or quotient.rank() == 0:
                return "Not found."
            if quotient.is_isometric(catalogue.Lattices.U):
                return "Odd"
            if quotient.is_isometric(catalogue.Lattices.U_2):
                return "Even ordinary"
            if quotient.is_isometric(catalogue.Lattices.IPQ(1, 1).twist(2)):
                return "Even characteristic"
            return "Not found."

        # ---- dual basis ----

        def dual_basis(self: Any) -> Any:
            r"""Return the columns of $G^{-1}$ as the dual basis.

            These lie in $L\\otimes\\mathbb{Q}$, not necessarily in $L$, so they
            are returned as vectors in the base-changed parent, not as
            lattice-element facades.
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

        # ---- overlattices ----

        def dual_lattice_element(self: Any, coordinates: Any) -> Any:
            r"""Return the element of $L^*$ with the displayed coordinates.

            The input is only a coordinate row.  The returned object is an
            element of the actual Sage module ``self.dual_lattice()``; this is
            the point where a raw vector is turned into a mathematical element
            of $L^*$.
            """
            return self.discriminant_group()._dual_module(coordinates)

        def dual_lattice_generators(self: Any) -> tuple[Any, ...]:
            r"""Return the explicit module generators of $L^*$."""
            return self.discriminant_group()._dual_generators

        def dual_embedding(self: Any) -> Any:
            r"""Return the inclusion morphism $L\to L^*$."""
            return self.discriminant_group()._source_to_dual

        def discriminant_projection(self: Any) -> Any:
            r"""Return the quotient morphism $\pi: L^* \to A_L=L^*/L$."""
            return self.discriminant_group()._projection_from_dual

        def project_to_discriminant_group(self: Any, element: Any) -> Any:
            r"""Project an element of $L^*$ to its class in $A_L$.

            This method applies the stored quotient morphism
            $\pi: L^*\to A_L$.  It does not accept coordinate rows; construct
            elements of $L^*$ first with :meth:`dual_lattice_element`.
            """
            projection = self.discriminant_projection()
            assert getattr(element, "parent", lambda: None)() is projection.domain(), (
                "project_to_discriminant_group expects an element of this "
                "lattice's dual module; construct one with "
                "dual_lattice_element(...)"
            )
            return projection(element)

        def divided_discriminant_class(self: Any, element: Any) -> Any:
            r"""Return the discriminant element represented by $e/\operatorname{div}(e)$."""
            assert element in self, "divided_discriminant_class expects an element of this lattice"
            divisibility = self.div(element)
            dual_element = self.dual_embedding()(element) / QQ(divisibility)
            return self.discriminant_projection()(dual_element)

        def glue(self: Any, *elements: Any) -> Any:
            r"""Return the even overlattice glued along discriminant elements.

            The inputs are elements of the discriminant group $A_L = L^\vee/L$.
            Their lifts in $L^\vee$ generate the overlattice together with the
            original lattice.  Catalogue entries should construct elements of
            $L^*$ and project them to $A_L$ before calling this method.
            """
            rank = self.rank()
            rational_rows = [
                [QQ.one() if i == j else QQ.zero() for j in range(rank)]
                for i in range(rank)
            ]
            rational_rows.extend(
                _discriminant_lift_row(element, rank) for element in elements
            )

            denominator = ZZ.one()
            for row in rational_rows:
                for coordinate in row:
                    denominator = denominator.lcm(coordinate.denominator())

            scaled = matrix(
                ZZ,
                [
                    [ZZ(denominator * coordinate) for coordinate in row]
                    for row in rational_rows
                ],
            )
            hermite_rows = [
                row
                for row in scaled.hermite_form().rows()
                if any(coordinate != 0 for coordinate in row)
            ]
            basis = matrix(QQ, hermite_rows[:rank]) / denominator
            gram = basis * self.gram_matrix() * basis.transpose()
            lattice = SageIntegralLattice(matrix(ZZ, gram))
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

        def discriminant_group(self: Any, s: Any = 0) -> Any:
            r"""Return $A_L=L^*/L$ with its source and projection data.

            The Sage quotient module stores the cover ``V=L^*`` and relation
            submodule ``W=L``.  We attach the source lattice and the honest
            quotient morphism $\pi:L^*\to A_L$ so downstream constructions do
            not confuse coordinate rows, elements of $L^*$, and elements of
            $A_L$.

            There are three distinct objects here.

            * ``self.gens()`` are the basis vectors \(e_i\) of \(L\).
            * ``dual_lattice_generators()`` are Sage's generators \(f_i\) of the
              dual module \(L^*\).  These are elements of the dual parent, not
              raw rational rows.
            * ``dual_embedding()`` sends each \(e_i\) to the same vector in the
              rational coordinate space, now constructed inside the dual
              parent.  In the \(f_i\)-basis this map is generally not the
              identity; for \(A_1(-1)^n\) it is \(2I\).

            A displayed row in the catalogue is therefore first turned into an
            element of the dual parent with :meth:`dual_lattice_element`, and
            only then projected by the stored quotient map \(L^*\to A_L\).
            """
            from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

            if ZZ(s) == 0 and hasattr(self, "_preamble_discriminant_group"):
                return self._preamble_discriminant_group

            dual = self.dual_lattice()
            disc = TorsionQuadraticModule(dual, self)
            if ZZ(s) != 0:
                d = disc.annihilator().gen()
                primary_multiplier = d.prime_to_m_part(s)
                disc = disc.submodule([primary_multiplier * gen for gen in disc.gens()])
            disc.source_lattice = lambda: self
            disc._dual_module = disc.V()
            disc._dual_generators = tuple(disc._dual_module.gens())
            rank = self.rank()
            disc._source_to_dual = self.hom(
                [
                    disc._dual_module(
                        [ZZ.one() if i == j else ZZ.zero() for j in range(rank)]
                    )
                    for i in range(rank)
                ],
                codomain=disc._dual_module,
            )
            disc._projection_from_dual = disc.quotient_map()
            refine(disc, DiscriminantQuadraticModules())
            subdivide_form_gram_matrix(disc)
            if ZZ(s) == 0:
                self._preamble_discriminant_group = disc
            return disc

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
            **kwargs: Any,
        ) -> Any:
            r"""Construct an orthogonal direct sum with its ordered subobjects."""
            if not others:
                return self

            result = self
            for other in others:
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
                left_subobjects = (
                    left.summands()
                    if left in DirectSumObjects()
                    else (Subobject(left.Hom(left)(left.gens())),)
                )
                right_subobjects = (
                    other.summands()
                    if other in DirectSumObjects()
                    else (Subobject(other.Hom(other)(other.gens())),)
                )
                left_embedding = left.Hom(result)(result.gens()[:left_rank])
                right_embedding = other.Hom(result)(result.gens()[left_rank:])
                subobjects = [
                    Subobject(
                        subobject.embedding().domain().Hom(result)(
                            [
                                left_embedding(image)
                                for image in subobject.embedded_gens()
                            ]
                        )
                    )
                    for subobject in left_subobjects
                ] + [
                    Subobject(
                        subobject.embedding().domain().Hom(result)(
                            [
                                right_embedding(image)
                                for image in subobject.embedded_gens()
                            ]
                        )
                    )
                    for subobject in right_subobjects
                ]
                result._summands = tuple(subobjects)
                refine(result, [result.category(), DirectSumObjects()])

            return _apply_names(result, names) if names is not None else result

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

        def __add__(self: Any, other: Any) -> Any:
            r"""``L + M`` as the orthogonal direct sum (for ``sum([...])``)."""
            return self.direct_sum(other)

        def __radd__(self: Any, other: Any) -> Any:
            """Allow ``sum([L, M, ...])`` (Python starts from ``0``)."""
            if other == 0:
                return self
            return NotImplemented

        def __pow__(self: Any, exponent: Any, names: Any = None) -> Any:
            r"""``L ^ n`` as the ``n``-fold orthogonal direct sum."""
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

        def is_primitive(self: Any) -> bool:
            r"""Return whether this vector is primitive in its lattice."""
            return abs(gcd(list(self.parent().coordinate_vector(self)))) == 1

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
            r"""``v ^ 2`` -> $q(v)$."""
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

def _discriminant_lift_row(element: Any, rank: int) -> list[Any]:
    r"""Return a representative row in $L^*$ for a discriminant-group element."""
    assert hasattr(element, "lift"), (
        "glue expects discriminant-group elements; construct an element of "
        "L^* with dual_lattice_element(...), then project it with "
        "project_to_discriminant_group(...)"
    )
    row = [QQ(coordinate) for coordinate in element.lift()]
    assert len(row) == rank, (
        f"discriminant element lift has rank {len(row)}, expected {rank}"
    )
    return row

def _element_add(left: Any, right: Any, sign: int) -> Any:
    """Add/subtract lattice elements coordinate-wise, returning a lattice element.

    Arithmetic runs on native vectors; the parent constructor re-wraps.
    """
    from sage.modules.free_module_element import vector
    from sage.structure.element import Element

    if isinstance(left, (int, Integer)) and left == 0:
        return right if sign == 1 else -right
    if not isinstance(left, Element) or not isinstance(right, Element):
        return NotImplemented
    parent = left.parent()
    if right.parent() is not parent:
        return NotImplemented

    left_coords = vector(ZZ, list(_unwrap(left)))
    right_coords = vector(ZZ, list(_unwrap(right)))
    return parent(left_coords + sign * right_coords)

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
        L._gram_matrix = gram
    gram.subdivide(*cuts)

def _subdivide_lattice_gram_matrix(L: Any) -> None:
    gram = L.gram_matrix()
    if gram.subdivisions()[0]:
        return

    cuts = _matrix_connected_component_cuts(gram)
    if cuts:
        _subdivide_gram(L, cuts, cuts)

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
    _subdivide_lattice_gram_matrix(lattice)

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
