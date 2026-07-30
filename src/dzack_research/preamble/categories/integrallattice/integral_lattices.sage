r"""``IntegralLattices`` — a category owning the lattice-specific API.

Refine any integral lattice parent into this category to gain::

    q(x), b(x, y), div(x), get_isotropic_type(element)
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
from typing import Any, assert_never

from sage.arith.misc import gcd
from sage.categories.category import Category
from sage.categories.modules import Modules
from sage.matrix.constructor import matrix
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.matrix.special import identity_matrix
from sage.misc.latex import latex as _latex_fn
from sage.modules.free_module import FreeModule
from sage.modules.free_quadratic_module import FreeQuadraticModule_ambient_pid
import sage.modules.free_quadratic_module_integer_symmetric as _sage_fqmis
from sage.modules.free_quadratic_module_integer_symmetric import (
    FreeQuadraticModule_integer_symmetric,
)
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.sets.set import Set
from sage.modules.free_module_element import vector
from sage.modules.vector_integer_dense import Vector_integer_dense
from sage.structure.element import Vector

SageIntegralLattice = _sage_fqmis.IntegralLattice
SageIntegralLattice = getattr(
    SageIntegralLattice,
    "_preamble_native_integral_lattice",
    SageIntegralLattice,
)
IntegralLattice = SageIntegralLattice


class LatticeElement(Vector_integer_dense):
    r"""A vector of an integral lattice.

    The category's owned element type.  Sage's lattices hand out plain integer
    vectors; subclassing is how a parent claims its element type, and Sage
    sanctions subclassing Cython element classes (:issue:`24715`), so instances
    stay genuine native vectors for arithmetic, hashing and coercion.
    """


class Lattice(FreeQuadraticModule_integer_symmetric):
    r"""An integral lattice with a generating set and a Gram matrix.

    The category's owned parent type.  It adds nothing to Sage's class -- the
    behaviour is :class:`IntegralLattices`' -- but it is what the objects of
    this category *are*, so morphisms and elements have something owned to be
    annotated against, and the subcategories of lattices inherit it rather than
    falling back to a bare Sage module.
    """

    Element = LatticeElement


class RationalLattice(FreeQuadraticModule_ambient_pid):
    r"""A free $\mathbb Z$-module with a generating set and a $\mathbb Q$-valued Gram matrix.

    An object of the category of lattices with generating sets, in the case Sage
    has no class for: its form takes rational values.  $L^\vee$ is one -- free
    on $e_1^\vee,\dots,e_n^\vee$ with Gram $G^{-1}$ -- and so is the codomain of
    every morphism a torsion form is the cokernel of, since the generating set
    of the cokernel is the codomain's and its Gram is the codomain's descended.

    Sage's ``dual_lattice`` instead returns the *set of vectors*
    $\{x\in L\otimes\mathbb Q : \langle x, L\rangle\subseteq\mathbb Z\}$, which
    makes the correlation morphism look like an inclusion and the form look like
    a property of a shared ambient.  Here there is no ambient: generators and a
    Gram matrix are the whole of the data.

    Built through the class and not the ``FreeQuadraticModule`` factory, which
    coerces the Gram matrix into ``MatrixSpace(ZZ, n)`` and so rejects
    $G^{-1}$.  A $\mathbb Z$-module may perfectly well carry a rational form;
    only that one entry point insists otherwise.
    """

    def __init__(self, gram_matrix: Any) -> None:
        gram_matrix = matrix(QQ, gram_matrix)
        assert gram_matrix.is_symmetric(), "a Gram matrix must be symmetric"
        FreeQuadraticModule_ambient_pid.__init__(
            self, ZZ, gram_matrix.nrows(), gram_matrix
        )

    def _repr_(self) -> str:
        return f"Rational lattice of rank {self.rank()} over {self.base_ring()}"


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
            return (self.gram_matrix() * y).dot_product(x)

        def div(self: Any, x: Any) -> Any:
            r"""Return the positive generator of $\{\langle x, y\rangle : y \in L\}$."""
            pairings = [self.b(x, v) for v in self.basis()]
            return abs(gcd(pairings))

        def gram_of(self: Any, vectors: Any) -> Any:
            r"""Return the Gram matrix $[b(x_i, x_j)]$ of a finite family of vectors."""
            vectors = tuple(vectors)
            return matrix(ZZ, [[self.b(x, y) for y in vectors] for x in vectors])

        def get_isotropic_type(self: Any, isotropic_element: Any) -> str:
            r"""Classify a primitive isotropic element by its cusp type.

            Divisibility 1 gives ``"Odd"``. Divisibility 2 is distinguished
            by whether $e^* = e/2 \in A_L$ is characteristic.
            """
            assert getattr(isotropic_element, "parent", lambda: None)() is self, (
                "get_isotropic_type expects an element of this lattice"
            )
            assert self.q(isotropic_element) == 0, (
                f"expected an isotropic element, got square {self.q(isotropic_element)}"
            )
            assert isotropic_element.is_primitive(), "expected a primitive element"
            divisibility = self.div(isotropic_element)
            assert divisibility in Set({1, 2}), (
                f"expected divisibility 1 or 2 in a 2-elementary lattice, "
                f"got {divisibility}"
            )
            if divisibility == 1:
                return "Odd"
            if divisibility == 2:
                divided_class = self.divided_discriminant_class(isotropic_element)
                if divided_class.is_characteristic():
                    return "Even characteristic"
                return "Even ordinary"
            assert_never(divisibility)

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

            coordinate_rows = [
                self.coordinate_vector(v).change_ring(ZZ) for v in vectors
            ]

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
            r"""Return the element of $L^\vee$ written in $L$'s basis by ``coordinates``.

            The catalogue displays glue vectors as rational coordinates in
            $L$'s own basis, which is how they appear in the literature.  An
            element of $L^\vee$ is written in the dual basis, and
            $\sum_i a_i e_i^\vee = \sum_j v_j e_j$ gives $a = vG$ -- so the
            conversion is by the Gram matrix, and the coordinates come out
            integral exactly when the vector lies in $L^\vee$ at all.
            """
            in_dual_basis = vector(QQ, coordinates) * self.gram_matrix()
            assert all(entry in ZZ for entry in in_dual_basis), (
                f"{tuple(coordinates)} does not lie in L^v: it pairs to "
                f"{tuple(in_dual_basis)} with L's basis, and L^v is where those "
                "pairings are integral"
            )
            return self.dual()(in_dual_basis)

        def dual_lattice_generators(self: Any) -> tuple[Any, ...]:
            r"""Return the explicit module generators of $L^*$."""
            return tuple(self.dual().gens())

        def dual_embedding(self: Any) -> Any:
            r"""Return the inclusion morphism $L\to L^*$."""
            return self.correlation()

        def discriminant_projection(self: Any) -> Any:
            r"""Return the quotient morphism $\pi: L^* \to A_L=L^*/L$."""
            return self.discriminant_group().quotient_map()

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
            dual_element = self.dual()(
                self.correlation()(element) / QQ(divisibility)
            )
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

        def dual(self: Any) -> RationalLattice:
            r"""Return $L^\vee$, free on the dual basis with Gram $G^{-1}$."""
            cached = getattr(self, "_preamble_dual", None)
            if cached is None:
                cached = RationalLattice(self.gram_matrix().inverse())
                self._preamble_dual = cached
            return cached

        def correlation(self: Any) -> LatticeMorphism:
            r"""Return $c: L\to L^\vee$, $v\mapsto \langle v,-\rangle$.

            $c(e_i)=\sum_j G_{ij}e_j^\vee$, so its matrix is the Gram matrix:
            pairing with $e_i$ is the functional whose coordinates in the dual
            basis are the $i$-th row of $G$.  Nondegeneracy of the form is
            injectivity of $c$, and $\operatorname{coker} c$ is $A_L$.
            """
            cached = getattr(self, "_preamble_correlation", None)
            if cached is None:
                dual = self.dual()
                cached = self.hom(
                    [dual(row) for row in self.gram_matrix().rows()], codomain=dual
                )
                self._preamble_correlation = cached
            return cached

        def discriminant_bilinear_form(self: Any) -> "TorsionBilinearForm":
            r"""Return $(A_L, b)$ with $b: A_L\times A_L\to\mathbb Q/\mathbb Z$.

            The always-defined discriminant form: $b$ needs nothing of $L$
            beyond nondegeneracy, whereas $q$ needs $L$ even.  It is the
            cokernel of :meth:`correlation`.
            """
            return DiscriminantBilinearModules().cokernel(self.correlation())

        def discriminant_quadratic_form(self: Any) -> Any:
            r"""Return $(A_L, q)$ with $q: A_L\to\mathbb Q/2\mathbb Z$.

            Gated on evenness: moving a lift by $\ell\in L$ shifts
            $b(\tilde x,\tilde x)$ by $b(\ell,\ell)$, which lies in
            $2\mathbb Z$ exactly when $L$ is even.  For an odd $L$ there is no
            such $q$, and :meth:`discriminant_bilinear_form` is all there is.
            """
            return DiscriminantQuadraticModules().cokernel(self.correlation())

        def discriminant_group(
            self: Any, s: Any = 0, *, reduce_trivial: bool = False
        ) -> Any:
            r"""Return $A_L=\operatorname{coker}(c: L\to L^\vee)$ with the form $L$ supports.

            $q$ when $L$ is even, $b$ alone when it is odd -- two different
            categories, so which one comes back is a fact about $L$ and not a
            flag on the answer.

            The generators are the dual basis and the relations are the ones
            $c$ induces, so this is the cokernel on the nose.  A unimodular
            summand of $L$ still contributes its generators; the relations kill
            them, and they appear as trivial components and zero blocks rather
            than vanishing.  ``reduce_trivial`` drops them, which is a
            *different* object -- a different finitely presented group -- not
            another view of this one.

            The invariant-factor basis is likewise a different object, reached
            by an isometry: see ``invariant_factor_form``, alongside
            ``normal_form``.

            Three distinct things are in play.

            * ``self.gens()`` are the basis vectors $e_i$ of $L$.
            * :meth:`dual_lattice_generators` are the $e_i^\vee$ of $L^\vee$.
            * :meth:`dual_embedding` is $c$ itself, whose matrix is $G$ -- in
              the $e_i^\vee$ basis it is generally not the identity; for
              $A_1(-1)^n$ it is $2I$.

            A displayed row in the catalogue is therefore turned into an element
            of $L^\vee$ with :meth:`dual_lattice_element` first, and only then
            projected.
            """
            cache = f"_preamble_discriminant_group_{bool(reduce_trivial)}"
            if ZZ(s) == 0 and hasattr(self, cache):
                return getattr(self, cache)

            correlation = self.correlation()
            # Which form A_L carries is a fact about L, not a flag on the answer.
            category = (
                DiscriminantQuadraticModules()
                if self.is_even()
                else DiscriminantBilinearModules()
            )
            form = category.cokernel(correlation)
            if reduce_trivial:
                # Keep the surviving generators as they are: regenerating on the
                # Smith basis would be a different object again, not this one
                # with the trivial components dropped.
                surviving = [
                    generator.lift()
                    for generator in form.gens()
                    if generator.order() != 1
                ]
                form = category.cokernel(regenerated_by(form, surviving))
            if ZZ(s) != 0:
                return form.primary_part(s)
            setattr(self, cache, form)
            return form

        def is_coeven(self: Any) -> bool:
            r"""Return whether the discriminant form is integer-valued ($\delta=0$)."""
            from sage.rings.infinity import Infinity
            from sage.rings.rational_field import QQ

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
            coords = self.coordinate_vector(element)
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

        # ---- generators (element_class instances at the output boundary) ----

        def gens(self: Any, *args: Any, **kwargs: Any) -> Any:
            r"""Generators as ``element_class`` instances, immutable like Sage's own.

            The stored basis predates refinement, so it has the plain native
            element type; the parent hands out ``element_class`` elements.
            """
            native = super(IntegralLattices.ParentMethods, self).gens(*args, **kwargs)
            recast = [_recast_element(self, g) for g in native]
            return type(native)(recast) if not isinstance(native, list) else recast

        def basis(self: Any, *args: Any, **kwargs: Any) -> Any:
            native = super(IntegralLattices.ParentMethods, self).basis(*args, **kwargs)
            # Preserve the native container type: Sage internals (e.g.
            # discriminant_group) concatenate ``basis()`` with lists.
            recast = [_recast_element(self, g) for g in native]
            return type(native)(recast) if not isinstance(native, list) else recast

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
                expected = _summand_ranks(result) + _summand_ranks(other)
                result = _native_direct_sum(result, other, **kwargs)
                refine_one_lattice(result)
                # Both operands were split on their own construction, and the
                # summed Gram is block diagonal across them, so the sum's
                # components are exactly the two lists concatenated -- nothing
                # to search for, only to check.
                assert _summand_ranks(result) == expected, (
                    "direct sum disagrees with its summands: "
                    f"{_summand_ranks(result)} != {expected}"
                )

            return _apply_names(result, names) if names is not None else result

        def twist(self: Any, *args: Any, names: Any = None, **kwargs: Any) -> Any:
            r"""Twisted lattice.

            Scaling the Gram leaves the generators and their orthogonality
            alone, so the twist splits exactly where ``self`` does; its own
            construction finds that, and each summand comes back twisted.
            """
            result = _native_twist(self, *args, **kwargs)
            refine_one_lattice(result)
            assert _summand_ranks(result) == _summand_ranks(self), (
                "twisting changed the decomposition: "
                f"{_summand_ranks(result)} != {_summand_ranks(self)}"
            )
            if names is not None:
                result = _apply_names(result, names)
            return result

        # ---- morphisms / automorphisms ----

        def Hom(self: Any, *args: Any, **kwargs: Any) -> Any:
            r"""Return $\mathrm{Hom}(L,M)$ with form-checked construction.

            Construction is the usual list-of-images / matrix constructor;
            the refined homset rejects non-form-preserving maps.
            """
            hom = super(IntegralLattices.ParentMethods, self).Hom(*args, **kwargs)
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
            ]

            # Equality, not isometry: the summands are this lattice's own
            # generators, partitioned.
            decomposition = _decomposition_latex(self)
            if decomposition is None and self not in DirectSumObjects():
                decomposition = _summand_name(self)
            if decomposition is not None:
                header.append(f"L = {decomposition} \\\\")

            header.append(f"G_L = {gram_latex} \\\\")
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
            r"""``v * w`` -> bilinear pairing; anything else -> native semantics.

            Elements are genuine native vectors (``element_class`` subclasses
            the Cython type), so scalars, matrices, and coercion all keep
            Sage's own behaviour via ``super()``.
            """
            if isinstance(other, Vector):
                return self.parent().b(self, other)
            return super().__mul__(other)

        def __pow__(self: Any, exponent: Any, mod: Any = None) -> Any:
            r"""``v ^ 2`` -> $q(v)$."""
            assert exponent == 2, f"exponent {exponent} not supported"
            return self.q()

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

def _recast_element(parent: Any, g: Any) -> Any:
    r"""Return ``g`` as an immutable ``element_class`` element of ``parent``."""
    element = parent.element_class(parent, list(g))
    element.set_immutable()
    return element

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

def _decompose_lattice(L: Any) -> None:
    r"""Split \(L\) along its generators and record the summands.

    Decomposability here is a property of the chosen generating set: \(L\)
    *equals* a direct sum exactly when its Gram matrix is block diagonal in the
    generators it was built with.  A splitting that would need the generators
    permuted is a different object, and
    :func:`_matrix_connected_component_cuts` declines it.

    Every lattice passes through this on construction, so afterwards
    membership in :class:`DirectSumObjects` *is* decomposability: a lattice
    left in :class:`IntegralLattices` is indecomposable.  Callers rely on that
    invariant instead of re-running the search.
    """
    if getattr(L, "_summands", None) is not None:
        return

    gram = L.gram_matrix()
    cuts = _matrix_connected_component_cuts(gram)
    if not cuts:
        return

    bounds = list(zip([0] + cuts, cuts + [gram.nrows()]))
    blocks = [
        SageIntegralLattice(matrix(ZZ, gram.submatrix(start, start, end - start, end - start)))
        for start, end in bounds
    ]

    _subdivide_gram(L, cuts, cuts)
    generators = L.gens()
    L._summands = tuple(
        Subobject(block.Hom(L)(list(generators[start:end])))
        for block, (start, end) in zip(blocks, bounds)
    )
    refine(L, [L.category(), DirectSumObjects()])


def _summand_ranks(L: Any) -> tuple[int, ...]:
    r"""Return the ranks of \(L\)'s summands, or its own rank when indecomposable."""
    if L in DirectSumObjects():
        return tuple(s.embedding().domain().rank() for s in L.summands())
    return (L.rank(),)

# ---- summand names ----

#: Gram matrix -> LaTeX name, for the indecomposable lattices worth naming.
#: ``catalogue.sage`` fills this in; the lookup is empty and harmless until then.
_INDECOMPOSABLE_NAMES: dict[tuple, str] = {}


def _gram_key(gram: Any) -> tuple:
    r"""Return a hashable form of a Gram matrix, ignoring any subdivisions."""
    return tuple(tuple(row) for row in gram.rows())


def register_indecomposable(name: str, lattice: Any) -> None:
    r"""Register *lattice*'s Gram matrix under the LaTeX *name*.

    Matching is Gram equality, not isometry: a block **is** the named lattice
    when the matrices agree, so nothing here asserts a theorem.  Decomposable
    entries are refused -- they can never appear as a block, so registering one
    would be dead weight that reads as if it could match.
    """
    assert lattice not in DirectSumObjects(), (
        f"{name} is decomposable, so it can never be a summand; "
        "name it by aggregating the summand list instead"
    )
    _INDECOMPOSABLE_NAMES.setdefault(_gram_key(lattice.gram_matrix()), name)


def _summand_name(block: Any) -> str | None:
    r"""Return the catalogue name for *block*, or ``None`` if unrecognized.

    An exact match wins over a twisted one, and a positive scale over its
    negative, so \(\langle-2\rangle\) reports as $I_{0,1}(2)$ rather than
    $I_{1,0}(-2)$.
    """
    gram = block.gram_matrix()
    exact = _INDECOMPOSABLE_NAMES.get(_gram_key(gram))
    if exact is not None:
        return exact

    content = gcd(gram.list())
    for scale in (content, -content):
        if scale in (0, 1, -1):
            continue
        untwisted = _INDECOMPOSABLE_NAMES.get(
            _gram_key((gram / scale).change_ring(ZZ))
        )
        if untwisted is not None:
            return f"{untwisted}({scale})"

    return None


def _decomposition_latex(L: Any) -> str | None:
    r"""Return ``N_1 \oplus N_2 \oplus ...`` for *L*, or ``None`` if it has no summands.

    Unrecognized blocks fall back to a positional name; a lattice whose blocks
    are all unrecognized has nothing to say beyond its Gram matrix.
    """
    if L not in DirectSumObjects():
        return None
    names = [
        _summand_name(subobject.embedding().domain())
        for subobject in L.summands()
    ]
    if all(name is None for name in names):
        return None
    return " \\oplus ".join(
        name if name is not None else f"L_{{{i + 1}}}"
        for i, name in enumerate(names)
    )


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
    _decompose_lattice(lattice)

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


def _own_lattice_types(lattice: Any) -> None:
    r"""Claim the category's parent and element types before refine reads them."""
    from sage.cpython.type import can_assign_class

    if isinstance(lattice, Lattice):
        return
    assert can_assign_class(lattice), (
        f"cannot own the type of {type(lattice).__name__}"
    )
    lattice.__class__ = Lattice
    lattice.Element = LatticeElement


def install_integral_lattices() -> None:
    """Hook post-init and shadow ``IntegralLattice`` with the preamble constructor."""
    global _INTEGRAL_LATTICES_INSTALLED
    if _INTEGRAL_LATTICES_INSTALLED:
        return

    hook_post_init(
        FreeQuadraticModule_integer_symmetric,
        IntegralLattices(),
        before=_own_lattice_types,
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
