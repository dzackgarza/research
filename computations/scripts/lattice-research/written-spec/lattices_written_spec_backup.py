r"""
Let R be a Dedekind domain (usually assumed a PID).
A bilinear R-module is a pair (M, \beta) where M is finitely generated
R-module M \cong R^n and \beta: M\otimes_R M -> R is a symmetric bilinear form.
When M is free and finitely generated, we refer to this as an R-lattice.
When additionally R=ZZ, we refer to this simply as a "lattice".

We allow \beta to take values in K := the fraction field of R, in which case
we refer to it as "rational".
When R=ZZ and K=QQ, we refer to this as a rational lattice.
Every Lattice is thus a RationalLattice.

NB: the category of lattices is NOT a subcategory of ZZ-modules: it is a
subcategory of a product category R-Mod x Bil_R, where Bil_R is the category
of elements of (M\otimes_R M)^* := Hom_R(M\otimes_R M, R) as M ranges over
R-Mod.
A morphism of bilinear R-modules is a morphism f: M_1 -> M_2 in R-Mod such that
\beta_1(v,w) = \beta_2(f(v), f(w)) for all v,w\in M_1. An isomorphism is
similarly defined, and we refer to this as an *isometry* of lattices.

More correctly, we work in a category of triples (M, \beta, B) where B is a
fixed generating set of M. We thus represent (M,\beta,B) by the pair
(M, G_\beta) where G_\beta is the Gram matrix of \beta in the generating set B.
Thus pairs with different Gram matrices represent isometric, but not equal, latttices.

When M is a torsion R-module, we allow \beta to take values in K/R or K/2R,
and refer to this as a discriminant bilinear R-module.
When R = ZZ, we refer to this as a (bilinear) discriminant form, where \beta
takes values in QQ/ZZ or QQ/2ZZ.
We refer to M as the discriminant *group*, when ignoring the bilinear form.

We similarly define a pair (M, q) where q is a quadratic form to be a quadratic
R-module, with (M\otimes_R K, q \otimes_R id_K) its associated quadratic space.
And when M is torsion, we refer to this as a (quadratic) discriminant form, or
just a discriminant form.
"""

# TODO: should use e.g. Pydantic and move mathematical assertions into -- [needs approach]
# validation functions.
# TODO: new requirement, do not use inheritance with Sage-native lattice -- [needs approach]
# objects for now. Instead, use a completely separate class hierarchy and
# composition by storing internal objects. Hook into low-level Sage constructs:
# HomSet, Morphism, FreeModule_ambient_pid_with_category or FGP_Module, etc.
# In particular, since lattices are pairs, there is no natural category in Sage
# in which they can live, so they should not extend existing sage classes.
# Instead, wrap the necessary functions with simple promotion logic to defer to
# existing computations on the Sage objects and re-cast them into this
# codebase's class layer.
# TODO: need a way to semantically work with QQ/ZZ and QQ/2ZZ as the value
# rings for discriminant forms.


# SPEC: fix R := ZZ. All methods should be defined as far up the hierarchy as
# possible, so that everything but Lattice and DiscriminantForm can be
# relegated to "backend" code. These two are the "public" API.
### OBJECTS
# BilinearModule: defines a pair (M, \beta)
# QuadraticModule: defines a pair (M, q)
# FreeBilinearModule(BilinearModule): when M \cong R^n is free
# TorsionBilinearModule(BilinearModule): When M is torsion
# RationalLattice(FreeBilinearModule): when \beta is QQ-valued
# - Natural home of L^*. Basic constructor: RationalLattice.from_gram(G_b),
#   which constructs M := R^n, inferred from G_b.base_ring() and rank(),
#   validates G_b in GL_n(QQ), checks G_b in GL_n(ZZ), and promotes/delegates
#   to Lattice(...) instead of self.
# - Should be the one and only place where promotion of rational lattice to
#   integral lattices happens, so e.g. is_integral() must be defined here
# Lattice(RationalLattice): when \beta is ZZ-valued.
# - Maintains elements v, with containment checked by v.parent() == L.
# - Maintains generators e_1, ..., e_n, which are LatticeElements.
# - Almost all named constructors go here, regardless of whether they return a
#   rational or integral lattice. So e.g. Lattice.F4() -> RationalLattice,
#   while Lattice.G2() -> Lattice. The constructions of these lattices from
#   their Gram matrices happen in RationalLattice though.
# - Should maintain an internal sage IntegralLattice object for delegation/wrapping
# DiscriminantForm(TorsionBilinearModule): defines (G, q). Constructible from a
#   lattice L as L^*/L with the natural induced form. Should also be
#   constructible from a sage AbelianGroup with a matrix defining the quadratic
#   form on generators, or from a list of invariants instead of the
#   AbelianGroup.
# - Should maintain a sage discriminant group for delegation/wrapping.
# LatticeElement: Elements of lattices. Should have v*w := v.b(w) :=
#   v.bilinear_product_with(w), v^2 := v.q() := v.b(v) := v*v, where
#   v.bilinear_product_with(w) := v * v.parent().gram_matrix() * w in natural
#   matrix-vector multiplication.
# - v.to_vector(), v.to_coordinates() writes v as a linear combination of e_i,
#   v = [v_1, ...., v_n], so e.g. if L.<e1, e2> = Lattice.U(), then e1, e2 are
#   purely symbolic, e1^2 == 0, e1.is_isotropic(), e1.perp() == e1.span(), etc,
#   and e1.to_vector == vector(ZZ, [1, 0]). Similarly,
#   (2*e_1-3*e2).to_vector() == vector(ZZ, [2, -3]).
# - Moreover L.element_from(vector([-1, 2])) == -1*e1 + 2*e2. Elements are
#   always displayed symbolically unless they are "unwrapped" into coordinates.
### MORPHISMS
# RationalLatticeMorphism(Morphism): f: A->B representable as maps of A.gens()
#   to QQ- or ZZ-linear combinations of B.gens(), depending on whether B is
#   integral or rational, or a matrix, respecting the bilinear forms.
# - Should have to_*, from_* methods where *=sequences, dicts, matrices, etc,
#   all represent maps of generators, with validation.
# - Automatically promotes to LatticeMorphism when integral
# RationalLatticeHomSpace: has Element = RationalLatticeMorphisms
# - Also has automatic promotion.
# - Primary example: the map \iota_L: L -> L^*
# - All isometry testing is done via the containment method on the homspace,
#   and all constructions of maps go through a constructor like
#   L1.Hom(L2).element_from_dict(...) or
#   Lattice.Hom(L1, L2).element_from_matrix(...).
# LatticeMorphism(RationalLatticeMorphism): when A, B are integral and all
#   defining linear combinations are ZZ-linear.
# - Needs methods like kernel() [lattice], cokernel()
#   [lattice | discriminant form | torsion bilinear/quadratic module, depending
#   on what is well-defined], is_primitive()
#   [check cokernel().is_torsionfree(), which is ultimately the SNF calculation
#   that created the cokernel module], image() [B.span([f(g) for g in
#   A.gens()])], etc.
# - One needs to be very careful about the theory: the category of lattices is
#   NOT closed under all morphism-related operations. Needs careful promotion to
#   lattices when free, integral, and nondegenerate, otherwise construct
#   appropriate torsion objects [discriminant-like] or degenerate objects
#   [module-like].


# TODO: most file paths were updated. Need to rename and sort out new imports. -- [needs approach]

from __future__ import annotations

import logging
from collections.abc import Sequence
from functools import reduce
from typing import Self

from sage.all import QQ, ZZ, Integer, IntegralLattice, MatrixSpace, matrix, vector
from sage.all import MatrixSpace as _MatrixSpace
from sage.misc.cachefunc import cached_method
from sage.modules.fg_pid.fgp_morphism import FGP_Morphism
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.vector_integer_dense import Vector_integer_dense
from sage.sets.condition_set import ConditionSet as _ConditionSet
from src.backends.external.py_polyhedral import (
    indefinite_form_automorphism_group,
    indefinite_form_isotropic_k_flag,
    indefinite_form_isotropic_k_plane,
    indefinite_form_stabilizer_isotropic_flag,
    indefinite_form_stabilizer_isotropic_line,
    indefinite_form_stabilizer_isotropic_plane_2d,
    indefinite_form_stabilizer_vector,
)
from src.backends.isometry_backend import ISOMETRY_BACKEND

_A1_POSITIVE = IntegralLattice("A1")
_A1_POSITIVE_VECTOR = next(iter(_A1_POSITIVE.basis()))
_A1_SCALE = _A1_POSITIVE_VECTOR.inner_product(_A1_POSITIVE_VECTOR)
_SAMPLE_LATTICE = IntegralLattice("U")
_SAMPLE_MODULE = _SAMPLE_LATTICE.ambient_module()
_SAMPLE_GROUP = _A1_POSITIVE.discriminant_group()

_FreeBilinearModuleBase = type(_SAMPLE_MODULE)
_LatticeBase = type(_SAMPLE_LATTICE)
_DiscriminantGroupBase = type(_SAMPLE_GROUP)
_DiscriminantGroupElementBase = type(next(iter(_SAMPLE_GROUP.gens())))
_LOGGER = logging.getLogger(__name__)
_NIKULIN_DOMAIN_WARNING = (
    "Computing Nikulin invariants outside the theorem-backed domain of even "
    "indefinite 2-elementary lattices. The triple (r, a, delta) still carries "
    "semantic information, while generic indefinite isometry is delegated to "
    "the Dutour-backed backend."
)


def _default_orbit_constraints():
    return {
        "determinant": None,
        "spinor": None,
        "discriminant_subgroup": None,
        "opaque": False,
    }


def _clone_orbit_constraints(constraints):
    return {
        "determinant": constraints["determinant"],
        "spinor": constraints["spinor"],
        "discriminant_subgroup": constraints["discriminant_subgroup"],
        "opaque": constraints["opaque"],
    }


def _merge_orbit_constraints(left, right):
    merged = _clone_orbit_constraints(left)
    for key in ("determinant", "spinor"):
        if right[key] is not None:
            if merged[key] is not None:
                assert merged[key] == right[key]
            merged[key] = right[key]
    if right["discriminant_subgroup"] is not None:
        if merged["discriminant_subgroup"] is None:
            merged["discriminant_subgroup"] = right["discriminant_subgroup"]
        elif merged["discriminant_subgroup"] is not right["discriminant_subgroup"]:
            merged["opaque"] = True
            merged["discriminant_subgroup"] = None
    merged["opaque"] = merged["opaque"] or right["opaque"]
    return merged


class FreeBilinearModuleElement(Vector_integer_dense):
    def is_isotropic(self):
        norm = self.inner_product(self)
        assert norm in ZZ
        return norm.is_zero()


class LatticeElement(FreeBilinearModuleElement):
    def divisibility(self):
        pairings = tuple(self.inner_product(basis_vector) for basis_vector in self.parent().basis())
        return ZZ.ideal(pairings).gen()

    def is_primitive(self):
        coordinates = tuple(Integer(entry) for entry in self)
        return ZZ.ideal(coordinates).gen().is_one()

    def discriminant_class(self):
        # TODO: for elements of L this projection is always zero. The nontrivial -- [needs approach]
        # discriminant-class map belongs on elements of the dual/rational lattice
        # once that hierarchy is exposed semantically.
        discriminant_group = self.parent().discriminant_group()
        discriminant_element = discriminant_group(self)
        assert discriminant_element.parent() is discriminant_group
        return discriminant_element


class LatticeMorphism(FreeModuleMorphism):
    # TODO: needs to override a lot to preserve closure under operations. -- [needs approach]
    def image_lattice(self):
        # TODO: should override e.g. image() to cast back to Lattice
        image = self.image()
        assert image.base_ring() is ZZ
        return Lattice.from_sage(image)

    def orthogonal_complement_of_image(self):
        codomain = self.codomain()
        assert codomain.base_ring() is ZZ
        return codomain.orthogonal_complement(self.image_lattice())


class DiscriminantGroupElement(_DiscriminantGroupElementBase):
    def is_isotropic(self):
        # TODO: quadratic_product() doesn't seem to make sense.
        # v.quadratic_product(w) or D_L.quadratic_product(v, w) makes sense.
        # But you should be using semantic notation: return (self * self).is_zero()
        value = self.quadratic_product()
        assert self.parent().base_ring() is ZZ
        return value.is_zero()


class DiscriminantGroupMorphism(FGP_Morphism):
    # TODO: needs actual semantic constructors. -- [needs approach]
    # Not directly available in Categories.morphism() [although is_identity is
    # already there -- should mark this as an override and be compatible...].
    # But you can track the underlying abelian group and use
    # sage.groups.abelian_gps.abelian_group_morphism.AbelianGroupMap
    # Semantic constructors for f: A-> B should include:
    # from_lists( [g_i := gens_A], [f(g_i) := some_gens_B] ) # Automatically infer A and B from parents
    # from_dict( {g_i: f(g_i)} )
    # from_callable(f, A, B) # Just calls f on A.gens() and delegates to from_dict
    # from_matrix(M, A, B) # A matrix defining f(g_i) for g_i in A.gens() --
    # obviously only certain matrices even make sense here, but represents a
    # map of torsion ZZ-modules
    # Since we work with named generators, it is easy to check when a map is
    # well-defined, when it is a homomorphism, etc.
    # Then add to_x() methods for all of these for easy extraction (lists, dict, callable, matrix, etc)
    # Then checking is_identity() is easy: f.to_matrix().is_identity()
    # One also has to assert that it is an ISOMETRY in the constructor, likely
    # a matrix equation or checking norms of images of generators(), or just an
    # explicit enumeration of both finite groups.
    # TODO: image_generators() doesn't make sense, because it's just f.image().gens()
    # TODO: should override a lot to preserve class closure. -- [needs approach]
    def image_generators(self):
        images = tuple(self.im_gens())
        assert all(image.parent() is self.codomain() for image in images)
        return images

    def image_group(self):
        # TODO: just pollutes and indirects names space...override instead. -- [needs approach]
        image = self.image()
        assert image.base_ring() is ZZ
        return image

    def is_identity(self):
        # TODO: semantically indirect... needs semantic constructors and to leverage existing Sage checks -- [needs approach]
        image_group = self.image_group()
        assert image_group.base_ring() is ZZ
        same_domain = self.domain() is self.codomain()
        same_image_size = image_group.cardinality() == self.domain().cardinality()
        return same_domain and same_image_size and self.image_generators() == tuple(self.domain().gens())

    def is_injective(self):
        # TODO: completely mathematically wrong. -- [needs approach]
        # need f.kernel() == Lattice.zero(), constructing the zero lattice
        image_group = self.image_group()
        assert image_group.base_ring() is ZZ
        return image_group.cardinality() == self.domain().cardinality()

    def is_surjective(self):
        # TODO: Completely wrong again -- [needs approach]
        image_group = self.image_group()
        assert image_group.base_ring() is ZZ
        return image_group.cardinality() == self.codomain().cardinality()


class FreeBilinearModule(_FreeBilinearModuleBase):
    Element = FreeBilinearModuleElement

    @classmethod
    # TODO: we don't need to track all of this data. -- [needs approach]
    # Instead of tracking base ring and rank, store R^n as a literal
    # free module object
    # And we do not use the "sparse" machinery whatsoever
    def from_sage(cls, module: _FreeBilinearModuleBase) -> Self:
        converted = cls(
            module.base_ring(),
            module.rank(),
            module.inner_product_matrix(),
            sparse=module.is_sparse(),
        )
        assert converted.base_ring() is module.base_ring()
        return converted


class DiscriminantGroup(_DiscriminantGroupBase):
    Element = DiscriminantGroupElement

    @classmethod
    def from_invariants_and_gram(
        cls,
        invariants: Sequence[int],
        gram_qq,
        *,
        modulus: int = 1,
        modulus_qf: int = 2,
    ) -> Self:
        """
        Construct a discriminant form from invariant factors and its Gram matrix.

        The input ``gram_qq`` is the quadratic Gram matrix on the chosen
        generators of ``⊕_i Z/d_i Z`` with values in ``QQ/modulus_qf·ZZ``.
        """
        from sage.modules.torsion_quadratic_module import FreeQuadraticModule

        invariant_factors = tuple(Integer(invariant) for invariant in invariants)
        gram = matrix(QQ, gram_qq)
        assert gram == gram.transpose(), "Discriminant-form Gram matrix must be symmetric"
        assert gram.nrows() == len(invariant_factors) == gram.ncols(), (
            "Invariant-factor list and discriminant-form Gram matrix must have the same rank"
        )
        assert all(invariant >= 1 for invariant in invariant_factors), "Invariant factors must be positive"
        ambient_gram = matrix(
            ZZ,
            [
                [Integer(invariant_factors[i] * invariant_factors[j] * gram[i, j]) for j in range(len(invariant_factors))]
                for i in range(len(invariant_factors))
            ],
        )
        assert all(
            invariant_factors[i] * invariant_factors[j] * gram[i, j] in ZZ
            for i in range(len(invariant_factors))
            for j in range(len(invariant_factors))
        ), "Discriminant-form Gram entries must respect the specified invariant factors"
        ambient = FreeQuadraticModule(ZZ, len(invariant_factors), inner_product_matrix=ambient_gram)
        if not invariant_factors:
            zero_submodule = ambient.zero_submodule()
            return cls(zero_submodule, zero_submodule, (), Integer(modulus), Integer(modulus_qf))
        generator_vectors = []
        integral_basis = []
        for index, invariant in enumerate(invariant_factors):
            generator_coordinates = [QQ.zero()] * len(invariant_factors)
            generator_coordinates[index] = QQ.one() / invariant
            generator_vectors.append(vector(QQ, generator_coordinates))
            basis_coordinates = [QQ.zero()] * len(invariant_factors)
            basis_coordinates[index] = QQ.one()
            integral_basis.append(vector(QQ, basis_coordinates))
        return cls(
            ambient.span(tuple(generator_vectors)),
            ambient.span(tuple(integral_basis)),
            tuple(generator_vectors),
            Integer(modulus),
            Integer(modulus_qf),
        )

    @classmethod
    def from_sage(cls, group: _DiscriminantGroupBase) -> Self:
        generator_lifts = tuple(generator.lift() for generator in group.gens())
        converted = cls(
            group.V(),
            group.W(),
            generator_lifts,
            group._modulus,
            group._modulus_qf,
        )
        assert converted.base_ring() is group.base_ring()
        assert all(generator.additive_order() * generator.lift() in converted.W() for generator in converted.gens())
        return converted

    @classmethod
    def from_lattice(cls, lattice: Lattice) -> Self:
        native_group = lattice._native_lattice().discriminant_group()
        converted = cls.from_sage(native_group)
        assert converted.base_ring() is native_group.base_ring()
        return converted

    def p_rank(self, p):
        # TODO: doesn't seem to do what it claims, nor make sense in general. -- [needs approach]
        # Why should G/pG be an F_p-module in general....?
        # You can use the reduction map Z->Z/p to make a torsion Z-module a (Z/p)-module, but that is not what's being done here.
        # Only seems to make sense when G := (Z/pZ)^a, i.e. when G is p-elementary
        """
        Return ``dim_{F_p}(A_L / pA_L)`` for the discriminant group ``A_L``.
        """
        prime = Integer(p)
        invariants = tuple(self.invariants())
        count = sum(prime.divides(invariant) for invariant in invariants)
        count_integer = Integer(count)
        assert count_integer in ZZ
        return count_integer

    def is_p_elementary(self, p):
        # TODO: this function, and many others, have zero typing information. -- [needs approach]
        """
        Return whether ``A_L`` is an elementary abelian ``p``-group.

        This describes the finite abelian group ``A_L`` itself, not only the
        Nikulin ``2``-elementary branch. The trivial
        discriminant group is ``p``-elementary of rank ``0`` for every prime ``p``.
        """
        prime = Integer(p)
        assert prime.is_prime()
        invariants = tuple(self.invariants())
        return all(invariant == prime for invariant in invariants)

    def nikulin_a(self):
        # TODO: completely wrong definition of the variant. -- [needs approach]
        # ONLY applies to 2-elementary lattices
        """
        Return Nikulin's invariant ``a = dim_{F_2}(A_L / 2A_L)``.

        For even indefinite ``2``-elementary lattices, Nikulin's theorem uses
        this integer as the ``a`` in ``(r, a, delta)``. For other lattices it
        still records the ``2``-primary rank of ``A_L``.

        Sources:
        - ``theory/foundations/reflective-two-elementary-lattices.md``, section ``Nikulin classification``
        - Alexeev--Engel--Garza--Schaffler, ``§9.2``
        - Nikulin (1979), Theorem ``1.14.2``
        """
        two_primary_rank = self.p_rank(2)
        # TODO: making trivial assertions ALREADY guaranteed by typing system -- [needs approach]
        assert two_primary_rank in ZZ
        return two_primary_rank

    def coparity(self):
        """
        Return Nikulin's coparity ``delta`` for the discriminant quadratic form.

        By definition, ``delta = 0`` iff the discriminant form takes
        integral values on every class in ``A_L``; otherwise ``delta = 1``.
        The same discriminant-form computation is used both inside and outside
        the even indefinite ``2``-elementary theorem domain.

        Sources:
        - ``theory/foundations/reflective-two-elementary-lattices.md``, section ``Nikulin classification``
        - Alexeev--Engel--Garza--Schaffler, ``§9.2``
        - Nikulin (1979), Theorem ``1.14.2``
        """
        # TODO: why lift()? Why do we not semantically work in QQ/ZZ or QQ/2ZZ to beign with?
        has_integral_discriminant_form = all(element.quadratic_product().lift() in ZZ for element in self)
        coparity = ZZ.zero() if has_integral_discriminant_form else ZZ.one()
        assert coparity.is_zero() or coparity.is_one()
        return coparity

    def delta(self):
        # TODO: no need for trivial indirection -- [needs approach]
        """
        Return the coparity invariant using Nikulin's ``delta`` notation.
        """
        delta_value = self.coparity()
        assert delta_value.is_zero() or delta_value.is_one()
        return delta_value

    def has_isomorphic_group_structure_to(self, other):
        # TODO: rename to isomorphic_as_groups(self, other) -- [needs approach]
        # TODO: does not have an option to return a witness? -- [needs approach]
        """
        Return whether the underlying finite abelian groups are isomorphic.

        This compares the invariant factors of the discriminant groups, so it
        forgets the quadratic form and retains only the abstract group
        structure.
        """
        left_invariants = tuple(self.invariants())
        right_invariants = tuple(other.invariants())
        assert self.base_ring() is ZZ
        assert other.base_ring() is ZZ
        # TODO: are the invariants in a canonically ordered list..? -- [needs approach]
        # If not, only their sets of invariants should be checked
        return left_invariants == right_invariants

    def has_isomorphic_quadratic_module_to(self, other):
        # TODO: bizzarre naming. This is just is_isometric_to(self, other).
        """
        Return whether the discriminant quadratic modules are isomorphic.

        Sage's torsion-quadratic-module normal form follows [MirMor2009,
        IV Definition 4.6]. Its contract states that two torsion quadratic
        modules are isomorphic if and only if they have the same value modules
        and the same normal form, so this method compares exactly those data.

        Sources:
        - Sage ``TorsionQuadraticModule.normal_form`` documentation
        - Miranda--Morrison, *The number of embeddings of integral quadratic
          forms. II* (2009), IV Definition 4.6
        """
        left_normal_form = self.normal_form()
        right_normal_form = other.normal_form()
        same_value_module = self._modulus == other._modulus and self._modulus_qf == other._modulus_qf
        same_invariant_factors = left_normal_form.invariants() == right_normal_form.invariants()
        same_canonical_quadratic_matrix = left_normal_form.gram_matrix_quadratic() == right_normal_form.gram_matrix_quadratic()
        assert self.base_ring() is ZZ
        assert other.base_ring() is ZZ
        return same_value_module and same_invariant_factors and same_canonical_quadratic_matrix

    def is_isometric_to(self, other):
        return self.has_isomorphic_quadratic_module_to(other)

    def hom(self, codomain: Self, images: Sequence[DiscriminantGroupElement]):
        # Confusing: A.hom(B) is a space of morphisms, not a specific morphism,
        # and should be used like f = A.hom(B).element_from_dict(...)
        sage_hom = _DiscriminantGroupBase.hom(self, images, codomain)
        assert all(image.parent() is codomain for image in sage_hom.im_gens())
        return DiscriminantGroupMorphism(sage_hom.parent(), sage_hom)

    def orthogonal_group(self, gens=None) -> DiscriminantOrthogonalGroup:
        # TODO: this is completely pointless: it just indirects CONSTRUCTION -- [needs approach]
        # of O(A_L) instead of COMPUTING it....
        r"""Return O(A_L) as a :class:`DiscriminantOrthogonalGroup`.

        The returned object wraps Sage's ``FqfOrthogonalGroup`` and exposes
        generators as plain ZZ-matrices with LEFT action (G * v, treating
        discriminant group elements as column vectors).  Since A_L is finite,
        O(A_L) is finite and membership is always decidable via GAP.
        """
        if gens is not None:
            # Sage-internal call (e.g., _isom_fqf passes gens=() for normal form)
            return _DiscriminantGroupBase.orthogonal_group(self, gens)
        return DiscriminantOrthogonalGroup(self)


class RationalLattice:
    # TODO: doesn't integrate with the BilinearModule hierarchy at all -- [needs approach]
    """Free Z-module with a QQ-valued symmetric bilinear form.

    This is the supertype of :class:`Lattice`.  A ``RationalLattice`` may have
    non-integer inner products (e.g. the F_4 root lattice in its Bourbaki
    ambient-space basis has a ``-1/2`` entry).  Use :meth:`is_integral` to
    test whether all inner products lie in ``ZZ``; if so, the gram matrix can
    be promoted to a :class:`Lattice` via :meth:`Lattice.from_gram`.

    Typical use: ``Lattice.F(4)`` internally builds
    ``RationalLattice.F(4).twist(2)`` and promotes the result to an integral
    :class:`Lattice`.
    """

    def __init__(self, gram_qq):
        self._gram = matrix(QQ, gram_qq)
        assert self._gram == self._gram.transpose(), "Gram matrix must be symmetric"

    def gram_matrix(self):
        """Return the QQ Gram matrix."""
        return self._gram

    def det(self):
        return self.gram_matrix().det()

    def rank(self):
        return self._gram.nrows()

    def is_integral(self):
        """Return True iff every entry of the Gram matrix lies in ZZ.

        Equivalently: ``self.gram_matrix() in Mat_n(ZZ)``.
        """
        return all(self._gram[i, j] in ZZ for i in range(self.rank()) for j in range(self.rank()))

    def twist(self, n) -> RationalLattice:
        """Return the lattice rescaled by ``n``: the bilinear form becomes ``n·β``.

        Auto-promotes to :class:`Lattice` when the result is integral.

        Examples::

            RationalLattice.F(4).twist(2)    # → Lattice  (integral)
            Lattice.U().twist(QQ(1, 2))      # → RationalLattice  (non-integral)
        """
        new_gram = QQ(n) * self._gram
        result = RationalLattice(new_gram)
        if result.is_integral():
            return Lattice.from_gram(matrix(ZZ, new_gram))
        return result

    def rescale(self, n):
        return self.twist(n)

    def __add__(self, other: RationalLattice) -> RationalLattice:
        """Direct sum (block-diagonal Gram matrix); auto-promotes to :class:`Lattice`."""
        from sage.all import block_diagonal_matrix

        new_gram = block_diagonal_matrix([self._gram, other._gram], subdivide=False)
        result = RationalLattice(new_gram)
        # TODO: wrong paradigm. RationalLattice.from_gram(...) should -- [needs approach]
        # automatically determine integrality and dispatch to Lattice in one
        # place, not up to callers to check.
        if result.is_integral():
            return Lattice.from_gram(matrix(ZZ, new_gram))
        return result

    def __pow__(self, n: int) -> RationalLattice:
        """Iterated direct sum: ``L ** n = L ⊕ ... ⊕ L`` (n copies)."""
        n = int(n)
        assert n >= 1, f"exponent must be ≥ 1, got {n!r}"
        result = self
        # TODO: why not sum...? -- [needs approach]
        for _ in range(n - 1):
            result = result + self
        return result

    @classmethod
    def _neg_root_gram_qq(cls, cartan_type: str) -> matrix:
        """Negative-definite QQ Gram matrix for the given Cartan type.

        The matrix is ``-β(α_i, α_j)`` where ``α_i`` are the simple roots in
        Sage's Bourbaki-ordered ambient space.  The result may have non-integer
        entries (F_4 has ``+1/2`` off-diagonal terms before negation).
        """
        from sage.all import RootSystem

        space = RootSystem(cartan_type).ambient_space()
        simple = list(space.simple_roots())
        gram_qq = matrix(QQ, [[a.inner_product(b) for b in simple] for a in simple])
        return -gram_qq

    @classmethod
    def F(cls, n: int) -> RationalLattice:
        # TODO: should just be F4(), no parameter
        """``F_4`` rational root lattice, negative-definite.

        In Bourbaki's ambient space ``R^4`` the simple roots are::

            α_1 = e_2 − e_3        (norm -2)
            α_2 = e_3 − e_4        (norm -2)
            α_3 = e_4              (norm -1)
            α_4 = ½(e_1−e_2−e_3−e_4)  (norm -1)

        Because ``α_3·α_4 = -½`` the bilinear form is **not** ZZ-valued on this
        basis; ``RationalLattice.F(4)`` is not integral.  Call ``Lattice.F(4)``
        to obtain the standard integral presentation ``twist(2)`` (all norms ×2:
        norm-(-2) nodes become norm-(-4), norm-(-1) nodes become norm-(-2)).

        Gram matrix (negative-definite)::

            [[-2,  1,  0,   0  ]
             [ 1, -2,  1,   0  ]
             [ 0,  1, -1,  1/2 ]
             [ 0,  0, 1/2, -1  ]]
        """
        assert int(n) == 4, f"F_n requires n = 4, got {n}"
        return cls(cls._neg_root_gram_qq("F4"))


class Lattice(_LatticeBase):
    """Integral lattice: a free Z-module with a ZZ-valued symmetric bilinear form.

    This is the integral subtype of :class:`RationalLattice`.  All
    constructors assert ``is_integral()`` and operate over ``ZZ``.
    """

    Element = LatticeElement

    @classmethod
    # TODO: why is this not just calling from_gram(L.gram_matrix())?
    def from_sage(cls, lattice: _LatticeBase) -> Self:
        converted = cls(
            lattice.ambient_module(),
            lattice.basis_matrix(),
            lattice.inner_product_matrix(),
        )
        assert converted.base_ring() is lattice.base_ring()
        return converted

    @classmethod
    def from_gram(cls, gram_zz) -> Self:
        """Construct a lattice directly from an integer Gram matrix."""
        gram = matrix(ZZ, gram_zz)
        assert gram == gram.transpose(), "Gram matrix must be symmetric"
        assert all(gram[i, j] in ZZ for i in range(gram.nrows()) for j in range(gram.nrows())), (
            "from_gram requires integer entries; use RationalLattice for QQ forms"
        )
        return cls.from_sage(IntegralLattice(gram))

    def is_integral(self) -> bool:
        # TODO: mark all overrides explicitly -- [needs approach]
        """Return True — every :class:`Lattice` is integral by construction.

        Satisfies the same contract as :meth:`RationalLattice.is_integral`.
        """
        return True

    def gram_matrix(self):
        return self.inner_product_matrix()

    def det(self):
        return self.determinant()

    def signature(self):
        return self.signature_pair()

    @cached_method
    def _native_lattice(self):
        # TODO: what is "native"? If this means sage's existing lattices, say so. -- [needs approach]
        native_lattice = _LatticeBase(
            self.ambient_module(),
            self.basis_matrix(),
            self.inner_product_matrix(),
        )
        assert native_lattice.base_ring() is self.base_ring()
        return native_lattice

    def _coerce_lattice(self, other):
        return other if type(other) is type(self) else type(self).from_sage(other)

    @cached_method
    def _quadratic_form(self):
        native_lattice = self._native_lattice()
        # TODO: these assertions are completely trivial... -- [needs approach]
        assert native_lattice.base_ring() is ZZ
        return native_lattice.quadratic_form()

    @cached_method
    def _rational_quadratic_form(self):
        return self._quadratic_form().change_ring(QQ)

    def has_isomorphic_discriminant_group_to(self, other):
        """
        Return whether the lattices have isomorphic discriminant groups.

        This is the abstract finite-abelian-group check on ``A_L``. It is a
        cheap necessary condition for integral isometry, but it ignores the
        discriminant quadratic form.
        """
        other_lattice = self._coerce_lattice(other)
        return self.discriminant_group().has_isomorphic_group_structure_to(other_lattice.discriminant_group())

    def has_isomorphic_discriminant_form_to(self, other):
        # TODO: Isomorphisms of discriminant forms are called ISOMETRIES. -- [needs approach]
        """
        Return whether the discriminant quadratic modules are isomorphic.

        An integral lattice isometry induces an isomorphism of discriminant
        quadratic modules, so this is a stronger necessary condition than
        abstract discriminant-group isomorphism.
        """
        other_lattice = self._coerce_lattice(other)
        return self.discriminant_group().has_isomorphic_quadratic_module_to(other_lattice.discriminant_group())

    def is_rationally_isometric_to(self, other):
        """
        Return whether the lattices become isometric over ``QQ``.

        This delegates to Sage's exact quadratic-form equivalence test over
        ``QQ`` after changing the associated integral quadratic forms from
        ``ZZ`` to ``QQ``.
        """
        other_lattice = self._coerce_lattice(other)
        return self._rational_quadratic_form().is_rationally_isometric(other_lattice._rational_quadratic_form())

    @cached_method
    def genus(self):
        return self._native_lattice().genus()

    @cached_method
    def local_genus_symbol(self, p):
        """
        Return the local genus symbol at prime p.

        This uses Sage's implementation which follows Conway--Sloane (1999).
        For p ≠ 2: returns triples [valuation, rank, det] (Theorem 9).
        For p = 2: returns quintuples [valuation, rank, det, parity, oddity]
        including the oddity invariant needed for completeness (§7.3-7.6).
        """
        prime = Integer(p)
        assert prime.is_prime()
        return self._quadratic_form().local_genus_symbol(prime)

    def is_locally_isometric_to(self, other, p):
        """
        Return whether the lattices are isometric over ``ZZ_p``.

        The comparison is performed on Sage's exact local genus symbols at the
        prime ``p``.

        Mathematical foundation: For p ≠ 2, Conway--Sloane (1999), Theorem 9
        establishes that the local genus symbol (triple [valuation, rank, det])
        is a complete invariant. For p = 2, Sage uses quintuples
        [valuation, rank, det, parity, oddity] which include the additional
        oddity invariant needed for completeness (Conway--Sloane, §7.3-7.6).
        """
        other_lattice = self._coerce_lattice(other)
        prime = Integer(p)
        assert prime.is_prime()
        # Compare the actual genus symbol objects which handle canonicalization
        self_symbol = self.local_genus_symbol(prime)
        other_symbol = other_lattice.local_genus_symbol(prime)
        return self_symbol == other_symbol

    def is_in_same_genus_as(self, other):
        """
        Return whether the lattices lie in the same genus.

        Equivalently, they are isometric over ``R`` and over ``ZZ_p`` for every
        prime ``p``. This is the exact adelic precheck used before any full
        integral-isometry backend.

        Sources:
        - ``theory/foundations/reflective-two-elementary-lattices.md``, discussion of genera and Nikulin's uniqueness
          theorem
        - Sage genus documentation for integral quadratic forms
        """
        other_lattice = self._coerce_lattice(other)
        return self.genus() == other_lattice.genus()

    def is_isometric_to(self, other):
        """
        Return the integral-lattice isometry predicate provided by this layer.

        Definite lattices defer to Sage. Even indefinite ``2``-elementary
        lattices use Nikulin's classification by signature and
        ``(r, a, delta)``. The remaining indefinite cases are delegated to the
        Dutour `Indefinite.jl` backend documented in
        ``theory/backends/indefinite-isometry.md``.

        Sources:
        - ``theory/foundations/reflective-two-elementary-lattices.md``, section ``Nikulin classification``
        - Alexeev--Engel--Garza--Schaffler, ``§9.2``
        - Nikulin (1979), Theorem ``1.14.2``
        - Generic indefinite backend: ``theory/backends/indefinite-isometry.md``
        """
        right_lattice = self._coerce_lattice(other)
        assert right_lattice.base_ring() is ZZ
        return ISOMETRY_BACKEND.is_isometric(self, right_lattice)

    def nikulin_invariants(self):
        """
        Return Nikulin's triple ``(r, a, delta)`` for the lattice.

        A warning is logged when the lattice lies outside the even indefinite
        ``2``-elementary theorem domain.

        Sources:
        - ``theory/foundations/reflective-two-elementary-lattices.md``, section ``Nikulin classification``
        - Alexeev--Engel--Garza--Schaffler, ``§9.2``
        - Nikulin (1979), Theorem ``1.14.2``
        """
        positive_rank, negative_rank = self.signature_pair()
        discriminant_group = self.discriminant_group()
        invariants = (
            Integer(self.rank()),
            discriminant_group.nikulin_a(),
            discriminant_group.delta(),
        )
        outside_domain = (
            (not self.is_even()) or (not positive_rank) or (not negative_rank) or (not discriminant_group.is_p_elementary(2))
        )
        if outside_domain:
            _LOGGER.warning(_NIKULIN_DOMAIN_WARNING)
        assert all(invariant in ZZ for invariant in invariants)
        return invariants

    @classmethod
    def Z(cls) -> Self:
        """Rank-1 lattice ``<1>`` with Gram matrix ``[1]``. Use ``.twist(n)`` for ``<n>``."""
        native_lattice = IntegralLattice(MatrixSpace(ZZ, ZZ.one())([1]))
        converted = cls.from_sage(native_lattice)
        assert converted.is_isometric_to(native_lattice)
        return converted

    @classmethod
    def U(cls) -> Self:
        """Hyperbolic plane ``U`` with Gram matrix ``[[0,1],[1,0]]``."""
        native_lattice = IntegralLattice("U")
        converted = cls.from_sage(native_lattice)
        assert converted.is_isometric_to(native_lattice)
        return converted

    @classmethod
    def _root_lattice_gram(cls, cartan_type: str):
        # TODO: seems to be reproducing existing code.. -- [needs approach]
        """Negative-definite integer Gram matrix for the given Cartan type.

        Computes ``-β(α_i, α_j)`` where ``α_i`` are Sage's Bourbaki-ordered
        simple roots in the ambient space of ``RootSystem(cartan_type)``.
        Asserts that all entries are integral (this holds for A, B, C, D, E, G
        but NOT for F_4 — use ``RationalLattice.F(4)`` for that type).
        """
        from sage.all import RootSystem

        space = RootSystem(cartan_type).ambient_space()
        simple = list(space.simple_roots())
        gram_qq = matrix(QQ, [[a.inner_product(b) for b in simple] for a in simple])
        neg_gram = -gram_qq
        assert all(neg_gram[i, j] in ZZ for i in range(neg_gram.nrows()) for j in range(neg_gram.nrows())), (
            f"_root_lattice_gram: non-integer entries for {cartan_type!r}; use RationalLattice"
        )
        return matrix(ZZ, neg_gram)

    @classmethod
    def A(cls, n: int) -> Self:
        """``A_n`` root lattice, negative-definite (n ≥ 1).

        All simple roots have norm -2.  Sage uses Bourbaki labeling: nodes
        1, 2, …, n form a chain.

        Dynkin diagram (Sage node labels)::

            1 — 2 — 3 — … — n       (all nodes norm -2)

        Gram matrix for A_3::

            [[-2,  1,  0]
             [ 1, -2,  1]
             [ 0,  1, -2]]
        """
        assert int(n) >= 1, f"A_n requires n ≥ 1, got {n}"
        return cls.from_gram(cls._root_lattice_gram(f"A{n}"))

    @classmethod
    def B(cls, n: int) -> Self:
        """``B_n`` root lattice, negative-definite (n ≥ 2).

        Constructed via the ambient-space bilinear form ``β(α_i, α_j)``.
        Nodes 1, …, n-1 have norm -2; node n has norm -1.

        Dynkin diagram (Sage node labels)::

            1 — 2 — … — (n-1) == n      (nodes 1..n-1: norm -2, node n: norm -1)

        Gram matrix for B_3::

            [[-2,  1,  0]
             [ 1, -2,  1]
             [ 0,  1, -1]]
        """
        assert int(n) >= 2, f"B_n requires n ≥ 2, got {n}"
        return cls.from_gram(cls._root_lattice_gram(f"B{n}"))

    @classmethod
    def C(cls, n: int) -> Self:
        """``C_n`` root lattice, negative-definite (n ≥ 2).

        Nodes 1, …, n-1 have norm -2; node n has norm -4.

        Dynkin diagram (Sage node labels)::

            1 — 2 — … — (n-1) == n      (nodes 1..n-1: norm -2, node n: norm -4)

        Gram matrix for C_3::

            [[-2,  1,  0]
             [ 1, -2,  2]
             [ 0,  2, -4]]
        """
        assert int(n) >= 2, f"C_n requires n ≥ 2, got {n}"
        return cls.from_gram(cls._root_lattice_gram(f"C{n}"))

    @classmethod
    def D(cls, n: int) -> Self:
        """``D_n`` root lattice, negative-definite (n ≥ 4).

        All simple roots have norm -2.  Node 2 is the branch vertex; nodes 1,
        n-1, and n all connect to node 2 (or to the end of the chain — see
        diagram).

        Dynkin diagram for D_4 (Sage node labels)::

                1
                |
            3 — 2 — 4

        Dynkin diagram for D_n (n ≥ 5)::

            1 — 2 — 3 — … — (n-2) — (n-1)
                                  \\
                                   n        (all nodes norm -2)

        Gram matrix for D_4::

            [[-2,  1,  0,  0]
             [ 1, -2,  1,  1]
             [ 0,  1, -2,  0]
             [ 0,  1,  0, -2]]
        """
        assert int(n) >= 4, f"D_n requires n ≥ 4, got {n}"
        return cls.from_gram(cls._root_lattice_gram(f"D{n}"))

    @classmethod
    def E(cls, n: int) -> Self:
        """``E_n`` root lattice, negative-definite (n ∈ {6, 7, 8}).

        All simple roots have norm -2.  Sage follows Bourbaki labeling: node 2
        is the branch vertex, attached to node 4 in the main chain.

        Dynkin diagram (Sage node labels, all nodes norm -2)::

                2
                |
            1 — 3 — 4 — 5 — 6          (E_6)

                2
                |
            1 — 3 — 4 — 5 — 6 — 7      (E_7)

                2
                |
            1 — 3 — 4 — 5 — 6 — 7 — 8  (E_8)

        Gram matrix for E_8 (rows/cols in Bourbaki order 1,2,…,8)::

            [[-2,  0,  1,  0,  0,  0,  0,  0]
             [ 0, -2,  0,  1,  0,  0,  0,  0]
             [ 1,  0, -2,  1,  0,  0,  0,  0]
             [ 0,  1,  1, -2,  1,  0,  0,  0]
             [ 0,  0,  0,  1, -2,  1,  0,  0]
             [ 0,  0,  0,  0,  1, -2,  1,  0]
             [ 0,  0,  0,  0,  0,  1, -2,  1]
             [ 0,  0,  0,  0,  0,  0,  1, -2]]
        """
        assert int(n) in {6, 7, 8}, f"E_n requires n ∈ {{6,7,8}}, got {n}"
        return cls.from_gram(cls._root_lattice_gram(f"E{n}"))

    @classmethod
    def F(cls, n: int) -> Self:
        # TODO: should not exist here. F4 is not integral, users need to twist themselves -- [needs approach]
        """``F_4`` root lattice, integral presentation, negative-definite.

        ``RationalLattice.F(4)`` has the Bourbaki-ambient-space Gram matrix
        (non-integral, with a ``±1/2`` entry).  Scaling by 2 gives the
        standard integral presentation ``RationalLattice.F(4).twist(2)``
        whose diagonal entries are all in ``{-4, -2}``.  This is what
        ``Lattice.F(4)`` returns.

        Nodes 1, 2 have norm -4; nodes 3, 4 have norm -2 (after the ×2 scale).

        Dynkin diagram (Sage node labels after scaling)::

            1 — 2 == 3 — 4     (nodes 1,2: norm -4; nodes 3,4: norm -2)

        Gram matrix::

            [[-4,  2,  0,  0]
             [ 2, -4,  2,  0]
             [ 0,  2, -2,  1]
             [ 0,  0,  1, -2]]
        """
        assert int(n) == 4, f"F_n requires n = 4, got {n}"
        rl = RationalLattice.F(4).twist(2)
        assert isinstance(rl, Lattice)
        return rl

    @classmethod
    def G(cls, n: int) -> Self:
        # TODO: should be G2 -- [needs approach]
        """``G_2`` root lattice, negative-definite.

        This is NOT the Cartan matrix; it uses the specific integral bilinear
        form ``β(α_i, α_j)`` in Bourbaki's ambient space ``R^4``.  Node 1 has
        norm -2; node 2 has norm -6 (ratio 1:3, reflecting the G_2 root length
        ratio ``|α_long|² / |α_short|² = 3``).

        Dynkin diagram (Sage node labels)::

            1 === 2      (node 1: norm -2, node 2: norm -6)

        Gram matrix::

            [[-2,  3]
             [ 3, -6]]
        """
        assert int(n) == 2, f"G_n requires n = 2, got {n}"
        return cls.from_gram(cls._root_lattice_gram("G2"))

    @classmethod
    def I(cls, p: int, q: int) -> Self:
        """Odd unimodular lattice ``I_{p,q} = <1>^p ⊕ <-1>^q``."""
        p, q = int(p), int(q)
        assert p >= 0 and q >= 0 and p + q >= 1, "I_{p,q} requires p,q ≥ 0 and p+q ≥ 1"
        pieces = [cls.Z()] * p + [cls.Z().twist(-1)] * q
        return reduce(lambda a, b: a + b, pieces)

    @classmethod
    def II(cls, p: int, q: int) -> Self:
        """Even unimodular lattice ``II_{p,q}``; requires ``p ≡ q (mod 8)``."""
        p, q = int(p), int(q)
        assert p >= 0 and q >= 0, "II_{p,q} requires p,q ≥ 0"
        assert (p - q) % 8 == 0, f"II_{{p,q}} requires p ≡ q (mod 8), got ({p},{q})"
        assert p + q >= 1, "II_{{0,0}} is trivial; not supported"
        diff = p - q
        n_hyperbolic = min(p, q)
        n_e8 = abs(diff) // 8
        e8 = cls.from_sage(IntegralLattice(IntegralLattice("E8").inner_product_matrix())) if diff > 0 else cls.E(8)
        pieces = [cls.U()] * n_hyperbolic + [e8] * n_e8
        return reduce(lambda a, b: a + b, pieces)

    @classmethod
    def from_string(cls, s: str) -> Self:
        """Parse a LaTeX-compatible direct-sum expression into a lattice.

        Syntax::

            expr  =  term ('+' term)*
            term  =  base ('^' exp)?
            base  =  'A_n' | 'A_{n}'    (single-digit subscript may omit braces)
                   | 'B_{n}' | 'C_{n}' | 'D_{n}' | 'E_{n}' | 'F_{4}' | 'G_{2}'
                   | 'U'
                   | 'U(k)'             (hyperbolic plane scaled by k)
                   | 'I_{p,q}' | 'II_{p,q}'
                   | '<n>'              (rank-1 lattice ZZ(n))
            exp   =  int | '{' int '}'  (iterated direct sum)
            scale =  '(' int ')'        (twist / rescale by integer)

        Examples::

            Lattice.from_string("A_1")
            Lattice.from_string("U(2) + A_{1}")
            Lattice.from_string("U^{3} + D_{6} + E_{8}")
            Lattice.from_string("E_{8}(2)")
            Lattice.from_string("A_{1}^{6} + D_{4}")
        """
        import re

        _DISPATCH = {"A": cls.A, "B": cls.B, "C": cls.C, "D": cls.D, "E": cls.E, "F": cls.F, "G": cls.G}

        def _parse_term(raw: str):
            raw = raw.strip()
            # Strip trailing direct-sum power: '^n' or '^{n}'
            pm = re.match(r"^(.*?)\^\{?(\d+)\}?$", raw, re.DOTALL)
            if pm:
                base_str, exp = pm.group(1).strip(), int(pm.group(2))
            else:
                base_str, exp = raw, 1

            # <n>  →  ZZ(n)
            m = re.fullmatch(r"<(-?\d+)>", base_str)
            if m:
                L = cls.Z().twist(int(m.group(1)))
                return L**exp if exp > 1 else L

            # U or U(k)  →  U() or U().twist(k)
            m = re.fullmatch(r"U(?:\((\d+)\))?", base_str)
            if m:
                L = cls.U()
                if m.group(1):
                    L = L.twist(int(m.group(1)))
                return L**exp if exp > 1 else L

            # II_{p,q}
            m = re.fullmatch(r"II_\{(\d+),(\d+)\}", base_str)
            if m:
                L = cls.II(int(m.group(1)), int(m.group(2)))
                return L**exp if exp > 1 else L

            # I_{p,q}
            m = re.fullmatch(r"I_\{(\d+),(\d+)\}", base_str)
            if m:
                L = cls.I(int(m.group(1)), int(m.group(2)))
                return L**exp if exp > 1 else L

            # Root lattice: X_{n}(k) or X_n(k) where single-digit subscript
            # may omit braces per LaTeX convention.
            m = re.fullmatch(r"([A-G])_(?:\{(\d+)\}|(\d))(?:\((\d+)\))?", base_str)
            if m:
                letter = m.group(1)
                n = int(m.group(2) if m.group(2) is not None else m.group(3))
                scale = m.group(4)
                if letter not in _DISPATCH:
                    raise ValueError(f"Unknown root lattice type: {letter!r}")
                L = _DISPATCH[letter](n)
                if scale:
                    L = L.twist(int(scale))
                return L**exp if exp > 1 else L

            raise ValueError(
                f"Cannot parse lattice token {base_str!r} in {s!r}. Use LaTeX subscript notation: 'A_1' or 'A_{{1}}', not 'A1'."
            )

        terms = [_parse_term(t) for t in re.split(r"\s*\+\s*", s.strip()) if t.strip()]
        if not terms:
            raise ValueError(f"Empty lattice expression: {s!r}")
        return reduce(lambda a, b: a + b, terms)

    def __pow__(self, n: int) -> Self:
        # TODO: should be on RationalLattice? -- [needs approach]
        """Iterated direct sum: ``L ** n = L ⊕ ... ⊕ L`` (n copies)."""
        n = int(n)
        assert n >= 1, f"exponent must be ≥ 1, got {n!r}"
        result = self
        for _ in range(n - 1):
            result = result + self
        return result

    def twist(self, n) -> Lattice | RationalLattice:
        # TODO: should be on rationalLattice and inherited? -- [needs approach]
        """Return the lattice rescaled by ``n``: the bilinear form becomes ``n·β``.

        Accepts any rational ``n``.  Returns a :class:`Lattice` when ``n`` is
        an integer (result is always integral); returns a :class:`RationalLattice`
        when the result has non-integer entries.

        Example::

            Lattice.U().twist(2)          # → Lattice     (integral)
            Lattice.U().twist(QQ(1, 2))   # → RationalLattice  (non-integral)
        """
        new_gram = QQ(n) * self.inner_product_matrix()
        if all(new_gram[i, j] in ZZ for i in range(new_gram.nrows()) for j in range(new_gram.ncols())):
            return type(self).from_gram(matrix(ZZ, new_gram))
        return RationalLattice(new_gram)

    def rescale(self, n):
        return self.twist(n)

    def scale(self):
        """Return the positive generator of the ideal ``<β(L, L)>`` in ``ZZ``."""
        return ZZ.ideal(self.inner_product_matrix().list()).gen()

    def __add__(self, other: Lattice | RationalLattice) -> Lattice | RationalLattice:
        """Direct sum.  Returns a :class:`Lattice` when ``other`` is also a :class:`Lattice`."""
        if isinstance(other, Lattice):
            return type(self).from_sage(self.direct_sum(other))
        # other is a RationalLattice — fall back to RationalLattice arithmetic
        rl_self = RationalLattice(matrix(QQ, self.inner_product_matrix()))
        return rl_self + other

    @classmethod
    def coble_picard(cls) -> Self:
        pos = cls.Z().twist(_A1_SCALE)
        neg = cls.Z().twist(-_A1_SCALE)
        e8_u_rank = IntegralLattice("E8").rank() + IntegralLattice("U").rank()
        return pos + neg**e8_u_rank

    @classmethod
    def coble_transcendental(cls) -> Self:
        return cls.Z().twist(_A1_SCALE) + cls.U() + cls.E(8)

    @classmethod
    def k3(cls) -> Self:
        return cls.II(3, 19)

    @cached_method
    def discriminant_group(self, s=ZZ.zero()):
        native_group = self._native_lattice().discriminant_group(s)
        converted = DiscriminantGroup.from_sage(native_group)
        # This assertion should probably be IN the validation for DiscriminantGroup
        assert all(generator.additive_order() * generator.lift() in converted.W() for generator in converted.gens())
        return converted

    def orthogonal_complement(self, sublattice: Self):
        # Todo: doesn't seem to make sense. How can you tell if another random -- [needs approach]
        # lattice is a sublattice of this lattice?
        # You need to either have a sublattice mixin which carries the parent
        # lattice, or even better, make this require a MORPHISM representing
        # the inclusion of the sublattice into the parent lattice in a specific way.
        native_complement = _LatticeBase.orthogonal_complement(self, sublattice)
        converted = type(self).from_sage(native_complement)
        assert converted.base_ring() is native_complement.base_ring()
        return converted

    def hom(self, codomain: Self, images: Sequence[LatticeElement]):
        # TODO: correct semantics with Sequence[LatticeElement], butagain, -- [needs approach]
        # hom is the abstract space of homs Hom(A, B), which has constructors
        # that take e.g. dicts, lists, sequences of images, etc
        morphism = LatticeMorphism(self.Hom(codomain), tuple(images))
        assert morphism.image().base_ring() is ZZ
        return morphism

    # ------------------------------------------------------------------
    # High-level computational methods (route to polyhedral_common binaries)
    # ------------------------------------------------------------------

    def _gram_rows(self):
        """Return the Gram matrix as a list of lists of Python ints."""
        return [[int(x) for x in row] for row in self.inner_product_matrix().rows()]

    def _vec_to_list(self, v):
        """Convert a LatticeElement / vector to a list of Python ints."""
        return [int(x) for x in v]

    def _column_action_isometry_from_row_action_matrix(self, raw_matrix):
        """Convert a row-action isometry matrix into the public column-action form."""
        raw = matrix(ZZ, raw_matrix)
        candidate = raw.transpose()
        gram = self.inner_product_matrix()
        assert candidate.transpose() * gram * candidate == gram
        return candidate

    def _matrices_from_raw(self, raw_matrices):
        """Convert row-action backend matrices into public column-action matrices."""
        return [self._column_action_isometry_from_row_action_matrix(raw_matrix) for raw_matrix in raw_matrices]

    def orthogonal_group(self) -> LatticeOrthogonalGroup:
        r"""Return O(self) as a :class:`LatticeOrthogonalGroup`.

        Construction is cheap; generators are computed lazily on first call to
        ``gens()``.  Membership uses the column-action equation G^T*Q*G == Q.
        """
        gram_rows = self._gram_rows()
        return LatticeOrthogonalGroup.from_lattice(
            self,
            lambda: self._matrices_from_raw(indefinite_form_automorphism_group(gram_rows)),
        )

    def stabilizer_of_vector(self, v) -> LatticeOrthogonalSubgroup:
        r"""Return Stab_{O(self)}(v) as a :class:`LatticeOrthogonalSubgroup`.

        v: a LatticeElement or integer vector (isotropic or non-isotropic).
        Membership: M in O(L) and M*v == v  (left action, column convention).
        """
        from sage.all import vector as sage_vector

        v_col = sage_vector(ZZ, self._vec_to_list(v))
        vlist = self._vec_to_list(v)
        gram_rows = self._gram_rows()
        return self.orthogonal_group().subgroup(
            gens_fn=lambda: self._matrices_from_raw(indefinite_form_stabilizer_vector(gram_rows, vlist)),
            predicate=lambda M, _v=v_col: M * _v == _v,
        )

    def stabilizer_of_isotropic_line(self, v) -> LatticeOrthogonalSubgroup:
        r"""Return setwise Stab_{O(self)}(span(v)) as a
        :class:`LatticeOrthogonalSubgroup`.

        v: a primitive isotropic LatticeElement.
        Membership: M in O(L) and M*v in span(v) over ZZ (allows M*v = ±v).
        """
        from sage.all import vector as sage_vector

        v_col = sage_vector(ZZ, self._vec_to_list(v))
        span_v = self.ambient_module().span([v_col])
        vlist = self._vec_to_list(v)
        gram_rows = self._gram_rows()
        return self.orthogonal_group().subgroup(
            gens_fn=lambda: self._matrices_from_raw(indefinite_form_stabilizer_isotropic_line(gram_rows, vlist)),
            predicate=lambda M, _s=span_v, _v=v_col: M * _v in _s,
        )

    def stabilizer_of_isotropic_plane(self, v, w) -> LatticeOrthogonalSubgroup:
        r"""Return Stab_{O(self)}(span(v,w)) as a :class:`LatticeOrthogonalSubgroup`.

        v, w: LatticeElements spanning a totally isotropic 2-plane.
        Membership: M in O(L) and M*v, M*w both in span(v,w) over ZZ.
        """
        from sage.all import vector as sage_vector

        v_col = sage_vector(ZZ, self._vec_to_list(v))
        w_col = sage_vector(ZZ, self._vec_to_list(w))
        plane = self.ambient_module().span([v_col, w_col])
        vlist, wlist = self._vec_to_list(v), self._vec_to_list(w)
        gram_rows = self._gram_rows()
        return self.orthogonal_group().subgroup(
            gens_fn=lambda: self._matrices_from_raw(indefinite_form_stabilizer_isotropic_plane_2d(gram_rows, vlist, wlist)),
            predicate=lambda M, _p=plane, _v=v_col, _w=w_col: M * _v in _p and M * _w in _p,
        )

    def stabilizer_of_isotropic_flag(self, ordered_basis) -> LatticeOrthogonalSubgroup:
        r"""Return Stab_{O(self)}(flag) as a :class:`LatticeOrthogonalSubgroup`.

        ordered_basis: ordered list of LatticeElements [v_1, ..., v_k].
            The ORDER is essential: the stabilizer fixes the nested flag
            span(v_1) ⊂ span(v_1,v_2) ⊂ ... ⊂ span(v_1,...,v_k).
        Membership: M in O(L) and M*v_j in span(v_1,...,v_j) for each j.
        """
        from sage.all import vector as sage_vector

        cols = [sage_vector(ZZ, self._vec_to_list(vi)) for vi in ordered_basis]
        strata = [self.ambient_module().span(cols[: i + 1]) for i in range(len(cols))]
        basis_lists = [self._vec_to_list(vi) for vi in ordered_basis]
        gram_rows = self._gram_rows()

        def _flag_predicate(M, _strata=strata, _cols=cols):
            return all(M * c in s for c, s in zip(_cols, _strata))

        return self.orthogonal_group().subgroup(
            gens_fn=lambda: self._matrices_from_raw(indefinite_form_stabilizer_isotropic_flag(gram_rows, basis_lists)),
            predicate=_flag_predicate,
        )

    def isotropic_line_orbits(self):
        r"""Return orbit representatives of primitive isotropic lines under O(self).

        Returns a list of LatticeElements, one per O(self)-orbit of primitive
        isotropic lines (1-dimensional totally isotropic subspaces).
        """
        raw = indefinite_form_isotropic_k_plane(self._gram_rows(), 1)
        return [self(rows[0]) for rows in raw]

    def isotropic_plane_orbits(self):
        r"""Return orbit representatives of totally isotropic planes under O(self).

        Returns a list of pairs (v, w) of LatticeElements spanning one
        representative totally isotropic 2-plane per O(self)-orbit.
        """
        raw = indefinite_form_isotropic_k_plane(self._gram_rows(), 2)
        # raw is a list of 2×n matrices (list of two row-vectors)
        return [(self(rows[0]), self(rows[1])) for rows in raw]

    def isotropic_flag_orbits(self, k):
        r"""Return orbit representatives of isotropic flags of depth k under O(self).

        k=1: orbits of isotropic lines (same as isotropic_line_orbits)
        k=2: orbits of flags line ⊂ plane
        Returns a list of lists of LatticeElements.
        """
        raw = indefinite_form_isotropic_k_flag(self._gram_rows(), k)
        return [[self(row) for row in rows] for rows in raw]

    def _eigenspace_sublattice(self, iota_matrix, eigenvalue: int) -> Lattice:
        r"""Return the eigenspace sublattice for eigenvalue ±1 of *iota_matrix*.

        Returns {v ∈ L : iota*v = eigenvalue*v} as a :class:`Lattice`.
        The Gram matrix of the returned sublattice is the restriction of the
        inner product to the ZZ-kernel of (iota - eigenvalue*I).
        """
        from sage.all import identity_matrix

        n = self.rank()
        ev = ZZ(eigenvalue)
        A = matrix(ZZ, iota_matrix) - ev * identity_matrix(ZZ, n)
        ker = A.kernel()  # free ZZ-submodule of ZZ^n
        B = ker.basis_matrix()  # rows are ZZ basis vectors of the eigenspace
        if B.nrows() == 0:
            return Lattice.from_sage(IntegralLattice(matrix(ZZ, 0, 0, [])))
        Q = self.inner_product_matrix()
        gram = B * Q * B.transpose()
        return Lattice.from_sage(IntegralLattice(gram))

    def invariant_sublattice(self, iota_matrix) -> Lattice:
        r"""Return the (+1)-eigenspace sublattice L^ι = {v ∈ L : ι*v = v}.

        iota_matrix: a square ZZ-matrix representing an isometry of L.
        The sublattice is equipped with the inner product restricted from L.
        """
        return self._eigenspace_sublattice(iota_matrix, +1)

    def coinvariant_sublattice(self, iota_matrix) -> Lattice:
        r"""Return the (−1)-eigenspace sublattice L_ι = {v ∈ L : ι*v = −v}.

        iota_matrix: a square ZZ-matrix representing an isometry of L.
        The sublattice is equipped with the inner product restricted from L.
        """
        return self._eigenspace_sublattice(iota_matrix, -1)

    def centralizer_of_involution(self, iota_matrix) -> LatticeOrthogonalSubgroup:
        r"""Return Z_{O(L)}(ι) = {g ∈ O(L) : g*ι = ι*g} as a subgroup.

        iota_matrix: a square ZZ-matrix representing an isometry of L.

        Membership test: ``M in Z_{O(L)}(ι)``  iff  M ∈ O(L) and M*ι = ι*M.

        Generators:
          - Definite L: computed via GAP Centralizer (O(L) is finite).
          - Indefinite L: requires OSCAR's ``integer_lattice_with_isometry`` +
            ``image_centralizer_in_Oq``; call :func:`oscar_centralizer_data`
            from ``src/oscar_centralizer`` and pass the result
            directly as generators.

        Note: Z_{O(L)}(ι) ≠ O^0(L, ι) in general.  Sterk's Γ_En is obtained
        by further intersection::

            centralizer_of_involution(ι)
                .kernel_of_discriminant_action()
                & stabilizer_of_vector(h)
        """
        iota_mat = matrix(ZZ, iota_matrix)

        def _gens_fn():
            p, q = self.signature_pair()
            if q == 0 or p == 0:  # positive or negative definite
                return self._centralizer_gens_via_gap(iota_mat)
            assert False, "Centralizer generators for indefinite lattices require OSCAR's image_centralizer_in_Oq data"

        return self.orthogonal_group().subgroup(
            gens_fn=_gens_fn,
            predicate=lambda M, _ι=iota_mat: M * _ι == _ι * M,
        )

    def _centralizer_gens_via_gap(self, iota_mat) -> list:
        r"""Compute generators of Z_{O(L)}(ι) via GAP Centralizer (definite only).

        Sage's orthogonal group engine requires a positive-definite Gram matrix.
        O(-L) = O(L) as groups of integer matrices (G^T Q G = Q ⟺ G^T (-Q) G = -Q),
        so we pass |Q| = -Q to Sage when the lattice is negative-definite.
        """
        p, q = self.signature_pair()
        gram = self.inner_product_matrix()
        # Sage's orthogonal_group requires positive-definite input.
        pd_gram = -gram if p == 0 else gram
        sage_L = IntegralLattice(pd_gram)
        og = sage_L.orthogonal_group()
        iota_elt = og(iota_mat)
        centralizer_gap = og.gap().Centralizer(iota_elt.gap())
        result = []
        for g_gap in centralizer_gap.GeneratorsOfGroup():
            g_elt = og(g_gap)
            result.append(self._column_action_isometry_from_row_action_matrix(g_elt.matrix()))
        return result


# ---------------------------------------------------------------------------
# Orthogonal group classes — LEFT action (G * v, column-vector convention)
# ---------------------------------------------------------------------------
# Sage and the Dutour-Sikirić backends return lattice isometries in a row-action
# convention.  Lattice._matrices_from_raw converts those matrices into the
# standard column-action convention used below:
#   G.act(v)  =  G * v   (matrix times column vector)
# with defining equation G^T Q G = Q.
#
# Action convention diagram:
#   Row-action input:  v_row * R = (R^T v_col)^T
#   Public API:        G * v_col = G v_col
#                      where G = R^T for group generators/stabilizers
#
# Generators are computed lazily via a zero-arg callable supplied at
# construction.  Pass a lambda that calls the appropriate binary; the result
# is cached after the first call to gens().
#
# Membership is handled internally by a ConditionSet over the MatrixSpace.
# Subgroups intersect their parent's ConditionSet with a new predicate.
# & / | produce new subgroups by intersecting / unioning ConditionSets.


def _acts_trivially_on_discriminant(lattice: Lattice, M) -> bool:
    r"""Return True if M ∈ O(L) acts trivially on A_L = L*/L.

    The action of M on A_L = L*/L sends the coset x + L to M*x + L for x ∈ L*.
    M acts trivially iff M*x − x ∈ L for every basis vector x of L*.

    For an integer lattice with Gram matrix Q, the dual lattice L* has basis
    given by the rows of Q^{-1}.  We check all dual-basis vectors.
    """
    from sage.all import vector as sage_vector

    Q = lattice.inner_product_matrix()
    # Rows of Q^{-1} are a basis for L* in the ambient QQ^n
    Qinv = Q.inverse()  # QQ-matrix
    for x_row in Qinv.rows():
        x = sage_vector(QQ, x_row)
        diff = M * x - x
        # diff ∈ L = ZZ^n iff all coordinates are integers
        if not all(c in ZZ for c in diff):
            return False
    return True


class LatticeOrthogonalGroup:
    r"""The orthogonal group O(L) of a lattice, with LEFT action G*v.

    Construction is O(1).  Generators are computed lazily by :meth:`gens`.

    Membership:  ``G in O(L)``  iff  ``G^T * Q * G == Q``,
    implemented via an internal ``ConditionSet`` over ``MatrixSpace(ZZ, n)``.

    Subgroups are obtained via :meth:`subgroup`; they intersect this group's
    ``ConditionSet`` with an additional predicate.  Use ``&`` / ``|`` to
    intersect or union subgroups.
    """

    @classmethod
    def from_lattice(cls, lattice: Lattice, gens_fn) -> LatticeOrthogonalGroup:
        r"""Construct O(L) with a lazy generator callable.

        gens_fn: zero-arg callable returning a list of ZZ-matrices.
                 Called at most once; result cached on first :meth:`gens` call.
        """
        return cls(lattice, gens_fn)

    def __init__(self, lattice: Lattice, gens_fn):
        self._lattice = lattice
        self._Q = lattice.inner_product_matrix()
        self._gens_fn = gens_fn
        self._gens_cache = None
        self._orbit_constraints = _default_orbit_constraints()
        MS = _MatrixSpace(ZZ, lattice.rank())
        Q = self._Q
        self._condition_set = _ConditionSet(
            MS,
            lambda M: M.transpose() * Q * M == Q,
        )

    @property
    def lattice(self) -> Lattice:
        return self._lattice

    @property
    def condition_set(self):
        return self._condition_set

    def gens(self) -> list:
        """Return the generating ZZ-matrices of O(L), computing them if needed."""
        if self._gens_cache is None:
            self._gens_cache = self._gens_fn()
        return list(self._gens_cache)

    def __contains__(self, G) -> bool:
        r"""G ∈ O(L)  iff  G^T Q G = Q  (column-action / left-action convention).

        This is the **single source of truth** for isometry membership.
        Never check ``G Q G^T == Q`` elsewhere — that is the row-action condition
        for Sage's raw backend matrices, which are converted to column-action form
        via ``_column_action_isometry_from_row_action_matrix`` before reaching
        the public API.
        """
        return G in self._condition_set

    def act(self, G, v):
        r"""Apply G to v from the left: return G * v (column-vector convention)."""
        from sage.all import vector as sage_vector

        return G * sage_vector(ZZ, v)

    def subgroup(self, gens_fn, predicate) -> LatticeOrthogonalSubgroup:
        r"""Return a :class:`LatticeOrthogonalSubgroup` of O(L).

        gens_fn:   zero-arg callable returning the list of generator matrices.
        predicate: callable ``M -> bool`` encoding the geometric condition
                   (e.g. M*v == v for a vector stabilizer).
        """
        return LatticeOrthogonalSubgroup(self, gens_fn, predicate)

    def __and__(self, other) -> LatticeOrthogonalSubgroup:
        r"""Intersection: subgroup satisfying both membership conditions."""
        cs = self._condition_set & other.condition_set
        subgroup = LatticeOrthogonalSubgroup._from_condition_set(self._lattice, cs)
        subgroup._orbit_constraints = _merge_orbit_constraints(
            self._orbit_constraints,
            other._orbit_constraints,
        )
        return subgroup

    def __or__(self, other) -> LatticeOrthogonalSubgroup:
        r"""Union: elements satisfying either membership condition."""
        cs = self._condition_set | other.condition_set
        subgroup = LatticeOrthogonalSubgroup._from_condition_set(self._lattice, cs)
        subgroup._orbit_constraints = _default_orbit_constraints()
        subgroup._orbit_constraints["opaque"] = True
        return subgroup

    def _structured_subgroup(
        self,
        predicate,
        *,
        constraints,
        gens_fn=None,
    ) -> LatticeOrthogonalSubgroup:
        subgroup = LatticeOrthogonalSubgroup(self, gens_fn, predicate)
        subgroup._orbit_constraints = _merge_orbit_constraints(
            self._orbit_constraints,
            constraints,
        )
        return subgroup

    def special_orthogonal_subgroup(self) -> LatticeOrthogonalSubgroup:
        return self._structured_subgroup(
            lambda M: ZZ(M.det()) == ZZ.one(),
            constraints={
                "determinant": 1,
                "spinor": None,
                "discriminant_subgroup": None,
                "opaque": False,
            },
        )

    def plus_subgroup(self) -> LatticeOrthogonalSubgroup:
        from src.backends.dawes_orbit_backend import real_spinor_norm_sign

        return self._structured_subgroup(
            lambda M, _lattice=self._lattice: real_spinor_norm_sign(_lattice, M) == 1,
            constraints={
                "determinant": None,
                "spinor": 1,
                "discriminant_subgroup": None,
                "opaque": False,
            },
        )

    def special_plus_subgroup(self) -> LatticeOrthogonalSubgroup:
        return self.special_orthogonal_subgroup().plus_subgroup()

    def preimage_of_discriminant_subgroup(self, subgroup) -> LatticeOrthogonalSubgroup:
        from src.backends.dawes_orbit_backend import induced_discriminant_action

        return self._structured_subgroup(
            lambda M, _lattice=self._lattice, _subgroup=subgroup: induced_discriminant_action(_lattice, M) in _subgroup,
            constraints={
                "determinant": None,
                "spinor": None,
                "discriminant_subgroup": subgroup,
                "opaque": False,
            },
        )

    def find_vector_isometry(self, v1, v2):
        from src.backends.dawes_orbit_backend import find_vector_isometry_in_group

        return find_vector_isometry_in_group(self, v1, v2)

    def vectors_are_equivalent(self, v1, v2) -> bool:
        from src.backends.dawes_orbit_backend import vectors_are_equivalent_in_group

        return vectors_are_equivalent_in_group(self, v1, v2)

    def isotropic_line_orbits(self):
        from src.backends.isotropic_gamma_orbit_backend import (
            isotropic_line_orbits_in_group,
        )

        return isotropic_line_orbits_in_group(self)

    def isotropic_plane_orbits(self):
        from src.backends.isotropic_gamma_orbit_backend import (
            isotropic_plane_orbits_in_group,
        )

        return isotropic_plane_orbits_in_group(self)

    def isotropic_flag_orbits(self, k):
        from src.backends.isotropic_gamma_orbit_backend import (
            isotropic_flag_orbits_in_group,
        )

        return isotropic_flag_orbits_in_group(self, k)

    def isotropic_lines_are_equivalent(self, v1, v2) -> bool:
        from src.backends.isotropic_gamma_orbit_backend import (
            isotropic_lines_are_equivalent_in_group,
        )

        return isotropic_lines_are_equivalent_in_group(self, v1, v2)

    def isotropic_planes_are_equivalent(self, basis1, basis2) -> bool:
        from src.backends.isotropic_gamma_orbit_backend import (
            isotropic_planes_are_equivalent_in_group,
        )

        return isotropic_planes_are_equivalent_in_group(self, basis1, basis2)

    def kernel_of_discriminant_action(self) -> LatticeOrthogonalSubgroup:
        r"""Return the subgroup of O(L) acting trivially on A_L = L*/L.

        This is the kernel of π: O(L) → O(A_L).

        Membership: M ∈ O(L) and M*x ≡ x (mod L) for all x ∈ L*,
        i.e. M*x − x ∈ L for every dual-lattice generator x.

        Use this to refine centralisers toward Sterk's arithmetic groups::

            L.centralizer_of_involution(ι).kernel_of_discriminant_action()
        """
        lattice = self._lattice
        cs = _ConditionSet(
            _MatrixSpace(ZZ, lattice.rank()),
            lambda M: _acts_trivially_on_discriminant(lattice, M),
        )
        subgroup = LatticeOrthogonalSubgroup._from_condition_set(lattice, self._condition_set & cs)
        subgroup._orbit_constraints = _merge_orbit_constraints(
            self._orbit_constraints,
            {
                "determinant": None,
                "spinor": None,
                "discriminant_subgroup": lattice.discriminant_group().orthogonal_group().subgroup([]),
                "opaque": False,
            },
        )
        return subgroup

    def __repr__(self) -> str:
        if self._gens_cache is not None:
            cached = f"{len(self._gens_cache)} gens"
        else:
            cached = "gens not yet computed"
        return f"LatticeOrthogonalGroup(rank={self._lattice.rank()}, {cached})"


class LatticeOrthogonalSubgroup:
    r"""A subgroup of O(L) defined by a ConditionSet.

    Membership:  ``M in subgroup``  iff  ``M`` is in the internal
    ``ConditionSet``, which is the intersection of:

      - the parent O(L) condition  ``M^T * Q * M == Q``, and
      - the geometric predicate supplied at construction.

    Examples of predicates:

    - Pointwise stabilizer of v:   ``lambda M: M * v == v``
    - Setwise stabilizer of line:  ``lambda M: M * v in span(v)``
    - Setwise stabilizer of plane: ``lambda M: M*v in P and M*w in P``
    - Flag stabilizer:             ``lambda M: all(M*v_j in stratum_j ...)``

    ``&`` / ``|`` produce new subgroups by intersecting / unioning ConditionSets.

    Generators are computed lazily via :meth:`gens`.
    """

    @classmethod
    def _from_condition_set(cls, lattice, condition_set):
        """Internal constructor from a pre-built ConditionSet (for & / |)."""
        obj = object.__new__(cls)
        obj._lattice = lattice
        obj._condition_set = condition_set
        obj._gens_fn = None
        obj._gens_cache = None
        obj._orbit_constraints = _default_orbit_constraints()
        return obj

    def __init__(
        self,
        ambient_group: LatticeOrthogonalGroup,
        gens_fn,
        predicate,
    ):
        self._lattice = ambient_group.lattice
        self._gens_fn = gens_fn
        self._gens_cache = None
        self._orbit_constraints = _clone_orbit_constraints(ambient_group._orbit_constraints)
        self._orbit_constraints["opaque"] = True
        self._condition_set = ambient_group.condition_set & _ConditionSet(_MatrixSpace(ZZ, self._lattice.rank()), predicate)

    @property
    def lattice(self) -> Lattice:
        return self._lattice

    @property
    def condition_set(self):
        return self._condition_set

    def gens(self) -> list:
        """Return the generating ZZ-matrices, computing them if needed."""
        if self._gens_cache is None:
            if self._gens_fn is None:
                assert False, "Generator computation requires an explicit generator function"
            self._gens_cache = self._gens_fn()
        return list(self._gens_cache)

    def __contains__(self, M) -> bool:
        return M in self._condition_set

    def act(self, G, v):
        r"""Apply G to v from the left: return G * v (column-vector convention)."""
        from sage.all import vector as sage_vector

        return G * sage_vector(ZZ, v)

    def __and__(self, other) -> LatticeOrthogonalSubgroup:
        cs = self._condition_set & other.condition_set
        subgroup = LatticeOrthogonalSubgroup._from_condition_set(self._lattice, cs)
        subgroup._orbit_constraints = _merge_orbit_constraints(
            self._orbit_constraints,
            other._orbit_constraints,
        )
        return subgroup

    def __or__(self, other) -> LatticeOrthogonalSubgroup:
        cs = self._condition_set | other.condition_set
        subgroup = LatticeOrthogonalSubgroup._from_condition_set(self._lattice, cs)
        subgroup._orbit_constraints = _default_orbit_constraints()
        subgroup._orbit_constraints["opaque"] = True
        return subgroup

    def _structured_subgroup(
        self,
        predicate,
        *,
        constraints,
        gens_fn=None,
    ) -> LatticeOrthogonalSubgroup:
        subgroup = LatticeOrthogonalSubgroup(self, gens_fn, predicate)
        subgroup._orbit_constraints = _merge_orbit_constraints(
            self._orbit_constraints,
            constraints,
        )
        return subgroup

    def special_orthogonal_subgroup(self) -> LatticeOrthogonalSubgroup:
        return self._structured_subgroup(
            lambda M: ZZ(M.det()) == ZZ.one(),
            constraints={
                "determinant": 1,
                "spinor": None,
                "discriminant_subgroup": None,
                "opaque": False,
            },
        )

    def plus_subgroup(self) -> LatticeOrthogonalSubgroup:
        from src.backends.dawes_orbit_backend import real_spinor_norm_sign

        return self._structured_subgroup(
            lambda M, _lattice=self._lattice: real_spinor_norm_sign(_lattice, M) == 1,
            constraints={
                "determinant": None,
                "spinor": 1,
                "discriminant_subgroup": None,
                "opaque": False,
            },
        )

    def special_plus_subgroup(self) -> LatticeOrthogonalSubgroup:
        return self.special_orthogonal_subgroup().plus_subgroup()

    def preimage_of_discriminant_subgroup(self, subgroup) -> LatticeOrthogonalSubgroup:
        from src.backends.dawes_orbit_backend import induced_discriminant_action

        return self._structured_subgroup(
            lambda M, _lattice=self._lattice, _subgroup=subgroup: induced_discriminant_action(_lattice, M) in _subgroup,
            constraints={
                "determinant": None,
                "spinor": None,
                "discriminant_subgroup": subgroup,
                "opaque": False,
            },
        )

    def find_vector_isometry(self, v1, v2):
        from src.backends.dawes_orbit_backend import find_vector_isometry_in_group

        return find_vector_isometry_in_group(self, v1, v2)

    def vectors_are_equivalent(self, v1, v2) -> bool:
        from src.backends.dawes_orbit_backend import vectors_are_equivalent_in_group

        return vectors_are_equivalent_in_group(self, v1, v2)

    def isotropic_line_orbits(self):
        from src.backends.isotropic_gamma_orbit_backend import (
            isotropic_line_orbits_in_group,
        )

        return isotropic_line_orbits_in_group(self)

    def isotropic_plane_orbits(self):
        from src.backends.isotropic_gamma_orbit_backend import (
            isotropic_plane_orbits_in_group,
        )

        return isotropic_plane_orbits_in_group(self)

    def isotropic_flag_orbits(self, k):
        from src.backends.isotropic_gamma_orbit_backend import (
            isotropic_flag_orbits_in_group,
        )

        return isotropic_flag_orbits_in_group(self, k)

    def isotropic_lines_are_equivalent(self, v1, v2) -> bool:
        from src.backends.isotropic_gamma_orbit_backend import (
            isotropic_lines_are_equivalent_in_group,
        )

        return isotropic_lines_are_equivalent_in_group(self, v1, v2)

    def isotropic_planes_are_equivalent(self, basis1, basis2) -> bool:
        from src.backends.isotropic_gamma_orbit_backend import (
            isotropic_planes_are_equivalent_in_group,
        )

        return isotropic_planes_are_equivalent_in_group(self, basis1, basis2)

    def kernel_of_discriminant_action(self) -> LatticeOrthogonalSubgroup:
        r"""Return the sub-subgroup acting trivially on A_L = L*/L.

        Intersects this subgroup's ConditionSet with the predicate
        ``M*x − x ∈ L`` for all dual-lattice generators x.  See
        :meth:`LatticeOrthogonalGroup.kernel_of_discriminant_action`.
        """
        lattice = self._lattice
        cs = _ConditionSet(
            _MatrixSpace(ZZ, lattice.rank()),
            lambda M: _acts_trivially_on_discriminant(lattice, M),
        )
        subgroup = LatticeOrthogonalSubgroup._from_condition_set(lattice, self._condition_set & cs)
        subgroup._orbit_constraints = _merge_orbit_constraints(
            self._orbit_constraints,
            {
                "determinant": None,
                "spinor": None,
                "discriminant_subgroup": lattice.discriminant_group().orthogonal_group().subgroup([]),
                "opaque": False,
            },
        )
        return subgroup

    def __repr__(self) -> str:
        if self._gens_cache is not None:
            cached = f"{len(self._gens_cache)} gens"
        else:
            cached = "gens not yet computed"
        return f"LatticeOrthogonalSubgroup(rank={self._lattice.rank()}, {cached})"


class DiscriminantOrthogonalGroup:
    r"""The orthogonal group O(A_L) of a discriminant group, with LEFT action.

    Wraps Sage's ``FqfOrthogonalGroup``.  Since A_L is finite, O(A_L) is
    finite and membership is always decidable via GAP.

    Generators are computed lazily by :meth:`gens`.
    """

    def __init__(self, disc: DiscriminantGroup):
        self._disc = disc
        self._sage_group = None  # built lazily
        self._gens_cache = None

    def _require_sage_group(self):
        if self._sage_group is None:
            self._sage_group = _DiscriminantGroupBase.orthogonal_group(self._disc)
        return self._sage_group

    @property
    def discriminant_group(self) -> DiscriminantGroup:
        return self._disc

    def gens(self) -> list:
        """Return generating ZZ-matrices, computing them if needed."""
        if self._gens_cache is None:
            self._gens_cache = [g.matrix() for g in self._require_sage_group().gens()]
        return list(self._gens_cache)

    def __contains__(self, G) -> bool:
        r"""Test G in O(A_L) via GAP (always decidable, O(A_L) is finite)."""
        try:
            sg = self._require_sage_group()
            return sg(G) in sg
        except Exception:  # grain: narrowed
            raise
            return False

    def act(self, G, v):
        r"""Apply G to discriminant element v from the left: G * v."""
        from sage.all import vector as sage_vector

        vec = v.vector() if hasattr(v, "vector") else sage_vector(ZZ, v)
        return G * vec

    def subgroup(self, generators) -> DiscriminantOrthogonalSubgroup:
        r"""Return the subgroup generated by *generators*."""
        return DiscriminantOrthogonalSubgroup(self._disc, list(generators), self._require_sage_group())

    def stabilizer(self, element) -> DiscriminantOrthogonalSubgroup:
        r"""Return the stabilizer of a discriminant element in ``O(A_L)``."""
        sage_stabilizer = self._require_sage_group().stabilizer(element)
        return DiscriminantOrthogonalSubgroup(
            self._disc,
            [g.matrix() for g in sage_stabilizer.gens()],
            self._require_sage_group(),
        )

    def __repr__(self) -> str:
        return f"DiscriminantOrthogonalGroup of {self._disc!r}"


class DiscriminantOrthogonalSubgroup:
    r"""A subgroup of O(A_L), with GAP-backed membership (always decidable).

    Since O(A_L) is finite (A_L is a finite group), membership in any
    subgroup is decidable via GAP.
    """

    def __init__(self, disc: DiscriminantGroup, generators: list, parent_sage_group):
        self._disc = disc
        self._generators = list(generators)
        self._sage_subgroup = parent_sage_group.subgroup([parent_sage_group(G) for G in generators])

    @property
    def discriminant_group(self) -> DiscriminantGroup:
        return self._disc

    def gens(self) -> list:
        return list(self._generators)

    def __contains__(self, G) -> bool:
        r"""Test G in subgroup via GAP (always decidable since O(A_L) is finite)."""
        try:
            # TODO: no try/except allowed. Assert on requirements. -- [needs approach]
            return self._sage_subgroup(G) in self._sage_subgroup
        except Exception:  # grain: narrowed
            raise
            return False

    def act(self, G, v):
        r"""Apply G to discriminant element v from the left: G * v."""
        from sage.all import vector as sage_vector

        vec = v.vector() if hasattr(v, "vector") else sage_vector(ZZ, v)
        return G * vec

    def __repr__(self) -> str:
        return f"DiscriminantOrthogonalSubgroup of O({self._disc!r}) ({len(self._generators)} generator(s))"
