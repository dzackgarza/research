r"""Lattices.

Sage does not define a category of (quadratic-form) lattices.  Sage's
:func:`~sage.modules.free_quadratic_module_integer_symmetric.IntegralLattice`
constructs a free quadratic module; the order-theoretic category is
:class:`~sage.categories.lattice_posets.LatticePosets`.  This module
owns the missing category, following Sage's category primer
(``super_categories``, ``ParentMethods``, ``ElementMethods``) and the
``Category_over_base_ring`` parameterization.  A lattice is a free
`R`-module with a form.  The Python class does not extend Sage's
module classes; it keeps an internal module reference.
The classcall is the category over a ring.  Objects are constructed by
calling that category.
"""

from sage.arith.misc import gcd
from sage.misc.cachefunc import cached_method
from sage.misc.latex import latex
from sage.misc.unknown import Unknown
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories._lattice import diagonal_gram as diagonal_gram
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryConstruction,
    IsoCategoryConstruction,
    MonoCategoryConstruction,
)
from dzack_research.preamble.categories.modules import FramedFreeModules
from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    engine_ring,
    own_ring,
)

_Rings = OwnedRings()


_INDECOMPOSABLE_NAMES = {}


class LatticeHomCategoryConstruction(HomCategoryConstruction):
    r"""The strict form-preserving Hom categories of lattices."""

    def fixed_category_class(self):
        from dzack_research.preamble.categories.lattice_morphisms import LatticeHomset

        return LatticeHomset


class LatticeMonoCategoryConstruction(MonoCategoryConstruction):
    r"""The form-preserving monomorphisms of lattices."""

    def fixed_category_class(self):
        from dzack_research.preamble.categories.lattice_morphisms import (
            LatticeEmbeddingHomset,
        )

        return LatticeEmbeddingHomset


class LatticeIsoCategoryConstruction(IsoCategoryConstruction):
    r"""The isometries of lattices."""

    def fixed_category_class(self):
        from dzack_research.preamble.categories.lattice_morphisms import (
            LatticeIsometryHomset,
        )

        return LatticeIsometryHomset


def _gram_key(gram):
    return tuple(tuple(row) for row in gram.rows())


def register_indecomposable_gram(name, gram):
    r"""Register an exact Gram matrix under its indecomposable display name."""
    _INDECOMPOSABLE_NAMES.setdefault(_gram_key(gram), str(name))


def register_indecomposable(name, lattice):
    r"""Register an indecomposable live lattice by exact Gram equality."""
    if lattice.is_decomposable():
        raise ValueError("only an indecomposable lattice can name one Gram block")
    register_indecomposable_gram(name, lattice.gram_tensor())


def indecomposable_name(lattice):
    r"""Return the registered exact or scalar-twist name, if one exists."""
    gram = lattice.gram_tensor().change_ring(SageZZ)
    exact = _INDECOMPOSABLE_NAMES.get(_gram_key(gram))
    if exact is not None:
        return exact
    content = gcd(gram.list())
    for scale in (content, -content):
        if scale in (0, 1, -1):
            continue
        from dzack_research.preamble.tensors import tensor

        rank = gram.tensor_shape()[0]
        untwisted = tensor(
            SageZZ,
            (),
            (rank, rank),
            [
                [SageZZ(gram[i, j] / scale) for j in range(rank)]
                for i in range(rank)
            ],
        )
        name = _INDECOMPOSABLE_NAMES.get(_gram_key(untwisted))
        if name is not None:
            return f"{name}({scale})"
    return None


class Genus:
    r"""The genus datum of an even nondegenerate integral lattice.

    For the supported even case this object is determined by its real
    signature and finite discriminant quadratic form.  Sage's genus engine is
    reconstructed from precisely those two data when local symbols,
    representatives, or the mass are requested; no hidden lattice
    representative is stored.
    """

    def __init__(self, signature_pair, discriminant_quadratic_form) -> None:
        self._signature_pair = (
            SageZZ(signature_pair[0]),
            SageZZ(signature_pair[1]),
        )
        self._discriminant_quadratic_form = discriminant_quadratic_form

    def signature_pair(self):
        r"""Return the archimedean signature component ``(t_+,t_-)``."""
        return self._signature_pair

    def discriminant_form(self):
        r"""Return the finite discriminant quadratic form component."""
        return self._discriminant_quadratic_form

    @cached_method
    def _engine_form(self):
        r"""Rebuild Sage's finite quadratic form from the owned discriminant form."""
        from sage.modules.torsion_quadratic_module import TorsionQuadraticForm
        from sage.rings.rational_field import QQ as SageQQ
        from dzack_research.preamble.tensors import tensor
        from dzack_research.preamble.tensors.tensor import _engine_component_matrix

        form = self.discriminant_form()
        generators = tuple(form.module_generators())
        written = tensor(
            SageQQ,
            (),
            (len(generators), len(generators)),
            [
                [
                    form.q(left).lift()
                    if i == j
                    else form.b(left, right).lift()
                    for j, right in enumerate(generators)
                ]
                for i, left in enumerate(generators)
            ],
        )
        engine_form = TorsionQuadraticForm(_engine_component_matrix(written))
        if engine_form.cardinality() != form.cardinality():
            raise ArithmeticError(
                "reconstructing the genus engine changed the discriminant-group cardinality"
            )
        return engine_form

    @cached_method
    def _engine(self):
        r"""Return Sage's global genus symbol for these exact data."""
        return self._engine_form().genus(self.signature_pair())

    def exists(self) -> bool:
        r"""Return whether the signature/discriminant-form datum is realizable."""
        return bool(self._engine_form().is_genus(self.signature_pair(), even=True))

    def determinant(self):
        r"""Return the determinant of a representative of this genus."""
        return SageZZ(self._engine().determinant())

    def local_symbol(self, prime):
        r"""Return the exact ``ZZ_p`` genus symbol at ``prime``."""
        return self._engine().local_symbol(SageZZ(prime))

    def excess(self, prime):
        r"""Return the local p-excess/2-adic oddity invariant at ``prime``."""
        return SageZZ(self.local_symbol(prime).excess())

    def level(self, prime):
        r"""Return the level of the local genus symbol at ``prime``."""
        return SageZZ(self.local_symbol(prime).level())

    def representative(self):
        r"""Return one live integral lattice representing this genus."""
        representative = self._engine().representative()
        return Lattices(SageZZ)([list(row) for row in representative.rows()])

    def representatives(self):
        r"""Return the representatives enumerated by the exact genus backend."""
        return tuple(
            Lattices(SageZZ)([list(row) for row in representative.rows()])
            for representative in self._engine().representatives()
        )

    def class_number(self):
        r"""Return the number of isometry classes enumerated in this genus."""
        return SageZZ(len(self._engine().representatives()))

    def mass(self):
        r"""Return the Smith--Minkowski--Siegel mass for a definite genus."""
        from sage.rings.rational_field import QQ as SageQQ

        positive, negative = self.signature_pair()
        if positive and negative:
            raise ValueError("the finite orthogonal-group mass is defined here for definite genera")
        return SageQQ(self._engine().mass())

    def __eq__(self, other):
        if not isinstance(other, Genus):
            return NotImplemented
        if self.signature_pair() != other.signature_pair():
            return False
        return bool(self._engine() == other._engine())

    def __ne__(self, other):
        result = self.__eq__(other)
        return result if result is NotImplemented else not result

    def __repr__(self):
        return (
            f"Genus of even integral lattices with signature {self.signature_pair()} "
            f"and discriminant order {self.discriminant_form().cardinality()}"
        )


_BLACKBOARD_RING_NAMES = {
    "Z": "ZZ",
    "Q": "QQ",
    "R": "RR",
    "C": "CC",
    "N": "NN",
}


def _ring_notation(ring):
    r"""Session name and latex for a base ring.

    Sage typesets `\ZZ`, `\QQ`, `\RR`, `\CC`, and the rest of that
    family as ``\Bold{Z}``, ``\Bold{Q}``, \ldots .  The session names
    are ``ZZ``, ``QQ``, ``RR``, ``CC``; the latex is ``\mathbb{Z}``
    and so on, not Sage's ``\Bold``.
    """
    raw = str(latex(ring))
    prefix = r"\Bold{"
    if raw.startswith(prefix) and raw.endswith("}") and raw.count("{") == 1:
        letter = raw[len(prefix) : -1]
        name = _BLACKBOARD_RING_NAMES.get(letter)
        if name is not None:
            return name, rf"\mathbb{{{letter}}}"
    return str(ring), raw


class Lattices(OwnedCategoryOverBaseRing):
    r"""
    The category of lattices over a base ring, and the constructor for
    its objects.

    Sage's ``IntegralLattice`` factory constructs finite nondegenerate
    integral forms but does not provide the mathematical category used here.
    ``Lattices(R)`` owns the broader category of free `R`-modules with an
    `R`-valued symmetric form; finite rank and nondegeneracy are refinements,
    not hidden constructor assumptions.      Named descriptors (``U``, a finite
    simply-laced Cartan type, a Euclidean rank) are owned Gram tensors.

    Sage's meet/join lattices are :class:`LatticePosets`, a different
    mathematical object.

    EXAMPLES::

        sage: from dzack_research.preamble.categories.lattices import Lattices
        sage: Lattices(ZZ)
        Lattices(ZZ)
        sage: Lattices(ZZ).super_categories()
        [Category of framed free modules]

        sage: C = Lattices(ZZ)
        sage: L = C("U")
        sage: L
        Integral lattice of rank 2 and signature (1, 1)
        sage: L in C
        True
        sage: C("A2")
        Integral lattice of rank 2 and signature (0, 2)
        sage: latex(L)
        \begin{gathered}
        L \in \mathrm{Lattices}(\mathbb{Z}), \quad \mathrm{rk}(L) = 2, \quad \mathrm{sig}(L) = (1, 1), \quad \mathrm{disc}(L) = 1 \\
        L = U \\
        G_L = \left(\begin{array}{rr}
        \cdot & 1 \\
        1 & \cdot
        \end{array}\right) \\
        \end{gathered}
        sage: latex(Lattices(ZZ))
        \mathrm{Lattices}(\mathbb{Z}) \in \mathrm{Cat}
    """

    @staticmethod
    def __classcall_private__(cls, *args):
        r"""Return the category of lattices over a ring.

        This is not a lattice constructor.  An object is
        ``Lattices(R)(data)``.
        """
        if len(args) != 1:
            raise TypeError("Lattices(R) takes a ring R; construct an object as Lattices(R)(data)")
        try:
            ring = own_ring(args[0])
        except TypeError as error:
            raise TypeError(
                "Lattices(R) takes a ring R; construct an object as Lattices(R)(data)"
            ) from error
        if ring not in _Rings:
            raise TypeError("Lattices(R) takes a ring R; construct an object as Lattices(R)(data)")
        return super().__classcall__(cls, ring)

    def _call_(self, data, basis=None, names=None, form=None, module_generators=None):
        r"""Construct a lattice in this category.

        This is Sage's category constructor: ``C(x)`` for ``C`` a
        category.  ``Lattices(ZZ)("U")`` is the hyperbolic plane over
        `\ZZ`.  ``Lattices(R)(R^n)`` is the standard Euclidean lattice
        of rank `n`; ``Lattices(R)(R^{\mathbb N})`` is its colimit.
        A pairing Gram is a lattice: ``C(diagonal_gram(R^NN, {0: -1}))``.
        ``module_generators=`` is the generating set of the underlying
        free module; when omitted, the generators are the formal symbols
        \(e_i\in\mathrm{SR}\).  The result is an owned lattice.

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: Lattices(ZZ)("U")
            Integral lattice of rank 2 and signature (1, 1)
            sage: I2 = Lattices(ZZ)(ZZ^2)
            sage: I2
            Integral lattice of rank 2 and signature (2, 0)
            sage: I2.gram_tensor().tensor_valence()
            (0, 2)
            sage: e = I2.module_generator(0)
            sage: e
            e_0
            sage: e.to_tuple()
            (1, 0)
            sage: e*e, e.b(I2.module_generator(1))
            (1, 0)
            sage: I2((1, 0))
            e_0
            sage: Linf = Lattices(ZZ)(ZZ^NN)
            sage: Linf
            Integral lattice of rank +Infinity and signature (+Infinity, 0)
            sage: Linf((1, 0, 0, 1))
            e_0 + e_3
            sage: from dzack_research.preamble.categories.lattices import diagonal_gram
            sage: Lattices(ZZ)(diagonal_gram(ZZ^NN, {0: -1}))
            Integral lattice of rank +Infinity and signature (+Infinity, 1)
        """
        from dzack_research.preamble.categories._lattice import lattice

        return lattice(
            data,
            basis,
            names=names,
            form=form,
            module_generators=module_generators,
            category=self,
        )

    def colimit(self, stage):
        r"""Return \(\operatorname{colim}_n \mathrm{stage}(n)\) along \(x\mapsto(x,0)\).

        ``stage(n)`` is a rank-\(n\) lattice in this category.  The
        odd unimodular lattice \(I_{\infty,1}\) is the colimit of
        \(I_{n,1}\).

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: C = Lattices(ZZ)
            sage: C.colimit(lambda n: C(ZZ^n))
            Integral lattice of rank +Infinity and signature (+Infinity, 0)
        """
        from dzack_research.preamble.categories._lattice import colimit_lattice

        return colimit_lattice(stage, category=self)

    @cached_method
    def super_categories(self):
        r"""
        Return the immediate super categories of ``self``.

        A lattice is a free `R`-module with a form.  Immediate supers
        only, as required by the Sage category primer.

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: Lattices(ZZ).super_categories()
            [Category of framed free modules]
        """
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
            SymmetricBilinearFormModules,
        )

        return [
            FramedFreeModules(self.base_ring()),
            SymmetricBilinearFormModules(self.base_ring()),
        ]

    _HomCategory = LatticeHomCategoryConstruction
    _MonoCategory = LatticeMonoCategoryConstruction
    _IsoCategory = LatticeIsoCategoryConstruction

    def _repr_(self):
        r"""Return ``Lattices(R)`` with the session name of the base ring.

        This is the cell's text/plain output.  The notebook typesets
        :meth:`_latex_` when it can; both must say ``Lattices(R)``, not
        Sage's "Category of lattices over Integer Ring".

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: Lattices(ZZ)
            Lattices(ZZ)
            sage: Lattices(QQ)
            Lattices(QQ)
        """
        name, _tex = _ring_notation(self.base_ring())
        return f"Lattices({name})"

    def _latex_(self):
        r"""Return ``Lattices(R) \in Cat``, with blackboard bold for `\ZZ`, `\QQ`, `\RR`, `\CC`.

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: latex(Lattices(ZZ))
            \mathrm{Lattices}(\mathbb{Z}) \in \mathrm{Cat}
            sage: latex(Lattices(QQ))
            \mathrm{Lattices}(\mathbb{Q}) \in \mathrm{Cat}
        """
        _name, tex = _ring_notation(self.base_ring())
        return rf"\mathrm{{Lattices}}({tex}) \in \mathrm{{Cat}}"

    class ParentMethods:
        """Operations generic to every lattice."""

        @cached_method
        def form(self):
            r"""Return the existing lattice pairing as a bilinear-form morphism."""
            from dzack_research.preamble.categories.forms import BilinearForms

            return BilinearForms(self, self.base_ring())(
                lambda left, right: self.b(left, right)
            )

        def value_module(self):
            return self.base_ring()

        def unformed_module(self):
            r"""Read this same parent at its weaker module level."""
            return self

        @cached_method
        def forget_form_morphism(self):
            from dzack_research.preamble.categories.modules import module_homset

            return module_homset(self, self).identity()

        @cached_method
        def equip_form_morphism(self):
            return self.forget_form_morphism()

        def _Hom_(self, codomain, category=None):
            from dzack_research.preamble.categories.lattice_morphisms import (
                lattice_homset,
            )

            lattices = Lattices(self.base_ring())
            if codomain in lattices and (
                category is None or category.is_subcategory(lattices)
            ):
                return lattice_homset(self, codomain)
            return super()._Hom_(codomain, category)

        def hom(self, images, codomain=None):
            r"""Construct a form-preserving lattice morphism."""
            if codomain is None:
                if isinstance(images, dict) and images:
                    codomain = next(iter(images.values())).parent()
                elif isinstance(images, (tuple, list)) and images:
                    codomain = images[0].parent()
                else:
                    raise TypeError("the codomain is required when it cannot be read from images")
            from dzack_research.preamble.categories.lattice_morphisms import (
                lattice_homset,
            )

            return lattice_homset(self, codomain)(images)

        def Emb(self, codomain):
            r"""Return the set of form-preserving embeddings into ``codomain``."""
            from dzack_research.preamble.categories.lattice_morphisms import (
                lattice_embedding_homset,
            )

            return lattice_embedding_homset(self, codomain)

        def Isom(self, codomain):
            r"""Return the set of isometries to ``codomain``."""
            from dzack_research.preamble.categories.lattice_morphisms import (
                lattice_isometry_homset,
            )

            return lattice_isometry_homset(self, codomain)

        def Aut(self):
            r"""Return ``Isom(L,L)``, the orthogonal automorphism homset."""
            return self.Isom(self)

        def orthogonal_group(self):
            r"""Return ``O(L,b)=Aut(L,b)`` as the owned isometry group."""
            return self.Aut()

        O = orthogonal_group  # noqa: E741 - standard mathematical notation O(L)

        def bilinear_orthogonal_group(self):
            r"""Return ``O(L,b)``; explicit name for the lattice pairing."""
            return self.Aut()

        def quadratic_orthogonal_group(self):
            r"""Return ``O(L,q)`` for ``q(x)=b(x,x)``.

            On a free integral lattice, preserving the symmetric bilinear form
            and preserving its diagonal quadratic form are equivalent, so this
            is the same represented group as ``O(L,b)``.
            """
            return self.Aut()

        @cached_method
        def discriminant_representation(self):
            r"""Return ``rho_L:O(L)->O(A_L)`` by functoriality of discriminants."""
            from sage.categories.morphism import SetMorphism

            source = self.Aut()
            target = self.discriminant_group().orthogonal_group()
            return SetMorphism(
                source.Hom(target),
                lambda isometry: isometry.discriminant_morphism(),
            )

        def discriminant_image(self):
            r"""Return the computed image of ``rho_L`` when ``O(L)`` generators are known."""
            return self.Aut().discriminant_image()

        def discriminant_representation_is_surjective(self) -> bool:
            r"""Return whether the computed discriminant image equals ``O(A_L)``."""
            image = self.discriminant_image()
            return image.cardinality() == self.discriminant_group().orthogonal_group().cardinality()

        def stable_orthogonal_group(self):
            r"""Return ``ker(rho_L)`` as the stable orthogonal subgroup."""
            target = self.discriminant_group().orthogonal_group()
            trivial = target.subgroup_on(())
            return self.Aut().discriminant_preimage(trivial)

        def special_orthogonal_group(self):
            r"""Return ``SO(L)=ker(det:O(L)->{+-1})`` as a predicate subgroup."""
            from dzack_research.preamble.categories.group.predicate_subgroups import (
                predicate_subgroup,
            )

            return predicate_subgroup(
                self.Aut(),
                lambda automorphism: automorphism.determinant() == 1,
                "det(g)=1",
                character_data={"determinant_kernel": True},
            )

        SO = special_orthogonal_group

        def spinor_kernel_subgroup(self):
            r"""Return the kernel of the real spinor-norm sign on ``O(L)``."""
            from dzack_research.preamble.categories.group.predicate_subgroups import (
                predicate_subgroup,
            )

            return predicate_subgroup(
                self.Aut(),
                lambda automorphism: automorphism.real_spinor_norm_sign() == 1,
                "real spinor norm(g)=+1",
                character_data={"spinor_kernel": True},
            )

        def positive_cone_subgroup(self):
            r"""Return the positive-cone-preserving subgroup in signature ``(1,n)``."""
            positive, negative = self.signature_pair()
            if positive != 1 or negative < 1:
                raise ValueError(
                    f"positive_cone_subgroup requires signature (1,n); got {(positive, negative)}"
                )
            from dzack_research.preamble.categories.group.predicate_subgroups import (
                predicate_subgroup,
            )

            return predicate_subgroup(
                self.Aut(),
                lambda automorphism: automorphism.preserves_positive_cone(),
                "g preserves the positive cone",
            )

        def biproduct_factors(self):
            r"""Return the two actual factors when this lattice was built by ``+``."""
            from dzack_research.preamble.categories._lattice import _BiproductGram

            gram = self.gram_tensor()
            if not isinstance(gram, _BiproductGram):
                raise ValueError("this lattice has no represented biproduct factors")
            return (gram._left, gram._right)

        @cached_method
        def decomposition(self):
            r"""Return the represented direct-sum decomposition, if present."""
            try:
                factors = self.biproduct_factors()
            except ValueError:
                return None
            from dzack_research.preamble.categories.abstract_categories.direct_sum_objects import (
                DirectSumDecomposition,
            )

            return DirectSumDecomposition(self, factors)

        def is_decomposable(self):
            return self.decomposition() is not None

        def summands(self):
            decomposition = self.decomposition()
            if decomposition is None:
                raise ValueError("this lattice has no represented direct-sum decomposition")
            return self._preamble_direct_sum_summands

        def indecomposable_name(self):
            return indecomposable_name(self)

        def decomposition_names(self):
            r"""Return registered names of the recursively represented factors."""
            decomposition = self.decomposition()
            if decomposition is None:
                return (self.indecomposable_name(),)
            names = []
            for factor in self.biproduct_factors():
                names.extend(factor.decomposition_names())
            return tuple(names)

        def is_isometric(self, other):
            r"""Return whether ``self`` and ``other`` are isometric when decidable.

            The live isometry homset preserves ``Unknown`` outside implemented
            exact regimes instead of treating matching coarse invariants as a
            proof.
            """
            empty = self.Isom(other).is_empty()
            if empty is Unknown:
                return Unknown
            return not empty

        def similarity_homset(self, other, scale):
            r"""Return similarities of scale ``scale`` as ``Isom(L(scale),other)``."""
            return self.twist(scale).Isom(other)

        def is_similar(self, other, scale):
            r"""Return whether a similarity of the stated scale exists."""
            return self.twist(scale).is_isometric(other)

        def similarity(self, scale, images=None, codomain=None):
            r"""Return an explicit similarity as an isometry from ``L(scale)``.

            A scale-``a`` similarity ``sigma:L->M`` satisfies
            ``b_M(sigma x,sigma y)=a*b_L(x,y)``.  Hence its owned
            form-preserving arrow is exactly an isometry ``L(a)->M``.  When
            ``images`` is omitted, return the distinguished isometry supplied
            by the exact isometry homset backend.
            """
            target = self if codomain is None else codomain
            homset = self.similarity_homset(target, scale)
            if images is None:
                return homset.an_element()
            return homset(images)

        def identity_morphism(self):
            r"""Return ``id_L`` in the lattice endomorphism homset.

            The morphism is a callable on generators, not an enumerated
            image of every \(e_i\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Iinf = Lattices(ZZ)(ZZ^NN)
                sage: f = Iinf.identity_morphism()
                sage: f(Iinf.module_generator(7))
                e_7
            """
            return self.Aut().identity()

        def gram_tensor(self):
            r"""Return the Gram tensor of the form: type $(0,2)$, not a matrix.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: I2 = Lattices(ZZ)(ZZ^2)
                sage: I2.gram_tensor()
                I_2 ∈ ((ZZ^2)*)^{⊗2}
                sage: latex(I2.gram_tensor())
                I_{2}
                sage: latex(Lattices(ZZ)(ZZ^NN).gram_tensor())
                I_{\infty}
                sage: A2 = Lattices(ZZ)("A2")
                sage: latex(A2.gram_tensor())
                \left(\begin{array}{rr}
                -2 & 1 \\
                1 & -2
                \end{array}\right)
                sage: I2.gram_tensor().parent()
                ((ZZ^2)*)^{⊗2}
                sage: Lattices(ZZ)(ZZ^NN).gram_tensor()
                I_∞ ∈ (ZZ^NN ⊗ ZZ^NN)*
            """
            return self._gram

        def module_generating_set(self):
            r"""Return the labels of the distinguished free-module framing.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)(ZZ^2).module_generating_set()
                {e_0, e_1}
                sage: Lattices(ZZ)(ZZ^NN).module_generating_set()
                {e_i : i in NN} subset of SR
            """
            return self._indices

        @cached_method
        def module_generators(self):
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                FreeModuleGeneratorSet,
            )

            return FreeModuleGeneratorSet(self)

        def module_generator(self, index):
            r"""Return the module generator indexed by ``index``.

            ``index`` is an element of the generating set, or an integer
            position in that enumerated set.  The default generating set
            is the formal symbols \(e_i\in\mathrm{SR}\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: I2 = Lattices(ZZ)(ZZ^2)
                sage: I2.module_generator(0)
                e_0
                sage: I2.module_generator(0).to_tuple()
                (1, 0)
            """
            keys = self.module_generating_set()
            positions = getattr(self, "_index_positions", None)
            if positions is not None:
                try:
                    positions[index]
                except KeyError, TypeError:
                    index = keys.unrank(int(index))
            elif index not in keys:
                index = keys.unrank(int(index))
            return self.element_class(self, self._module.monomial(index))

        def b(self, left, right):
            r"""Return the bilinear pairing \(b(v,w)\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: U = Lattices(ZZ)("U")
                sage: e, f = U.module_generator(0), U.module_generator(1)
                sage: U.b(e, f)
                1
            """
            assert left.parent() is self
            assert right.parent() is self
            gram = self.gram_tensor()
            if self.is_finite_rank():
                return gram.contract(left.to_vector(), right.to_vector())
            return gram(left._vector, right._vector)

        def q(self, vector):
            r"""Return the quadratic form \(q(v)=b(v,v)\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: I2 = Lattices(ZZ)(ZZ^2)
                sage: I2.q(I2.module_generator(0))
                1
                sage: A2 = Lattices(ZZ)("A2")
                sage: A2.q(A2.module_generator(0))
                -2
            """
            return self.b(vector, vector)

        def rank(self):
            r"""Return the rank of this lattice as a free module.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)(ZZ^2).rank()
                2
                sage: Lattices(ZZ)(ZZ^NN).rank()
                +Infinity
            """
            return self._module.rank()

        def signature_pair(self):
            r"""Return $(p,q)$: the positive and negative indices of inertia.

            This is the real signature of the quadratic space over
            \(\mathbb{Q}\) obtained by extending scalars along
            \(\operatorname{Frac}(R)\) when that field is \(\mathbb{Q}\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)("U").signature_pair()
                (1, 1)
                sage: Lattices(ZZ)(ZZ^NN).signature_pair()
                (+Infinity, 0)
            """
            from dzack_research.preamble.categories._lattice import (
                signature_pair_of_gram,
            )

            return signature_pair_of_gram(self.gram_tensor())

        def discriminant(self):
            r"""Return $d_\pm(b)=(-1)^{n(n-1)/2}\det G$, the signed determinant.

            An invariant of $L$, not the framing-dependent $\det G$.
            Transcribed from the archived integral-lattice discriminant
            (Lam, *Introduction to Quadratic Forms over Fields*, I.2).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)("U").discriminant()
                1
                sage: Lattices(ZZ)(ZZ^2).discriminant()
                -1
            """
            from dzack_research.preamble.categories._lattice import (
                discriminant_of_gram,
            )

            return discriminant_of_gram(self.gram_tensor())

        def is_finite_rank(self) -> bool:
            r"""Return whether this lattice is free of finite rank.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)(ZZ^2).is_finite_rank()
                True
                sage: Lattices(ZZ)(ZZ^NN).is_finite_rank()
                False
            """
            return self.rank() != Infinity

        def is_nondegenerate(self) -> bool:
            r"""Return whether the correlation map has zero radical."""
            from dzack_research.preamble.categories._lattice import (
                _BiproductGram,
                _ColimitGram,
                _DiagonalGram,
                _IdentityGram,
                _ScaledGram,
            )

            gram = self.gram_tensor()
            match gram:
                case _IdentityGram():
                    return True
                case _DiagonalGram():
                    if gram._default == 0:
                        return False
                    return all(value != 0 for value in gram._exceptions.values())
                case _ScaledGram():
                    return gram._scalar != 0 and Lattices(self.base_ring())(gram._gram).is_nondegenerate()
                case _BiproductGram():
                    return gram._left.is_nondegenerate() and gram._right.is_nondegenerate()
                case _ColimitGram():
                    # The represented colimit forms used here are orthogonal
                    # unions of nondegenerate finite stages.
                    return all(stage.is_nondegenerate() for stage in gram._objects)
                case _:
                    if not self.is_finite_rank():
                        raise NotImplementedError("nondegeneracy of this infinite Gram presentation is not decided")
                    return self.gram_tensor().det() != 0

        def is_even(self) -> bool:
            r"""Return whether ``b(x,x)`` lies in ``2R`` for every lattice vector."""
            ring = engine_ring(self.base_ring())
            try:
                twice_ring = ring.ideal(ring(2))
            except (AttributeError, NotImplementedError, TypeError) as error:
                raise NotImplementedError("membership in the principal ideal 2R is not decidable over this base ring") from error

            def is_twice(value) -> bool:
                return ring(value) in twice_ring

            if self.is_finite_rank():
                gram = self.gram_tensor()
                return all(is_twice(gram[i, i]) for i in range(int(self.rank())))
            from dzack_research.preamble.categories._lattice import _DiagonalGram, _IdentityGram, _ScaledGram

            gram = self.gram_tensor()
            match gram:
                case _IdentityGram():
                    return is_twice(ring.one())
                case _DiagonalGram():
                    return is_twice(gram._default) and all(is_twice(value) for value in gram._exceptions.values())
                case _ScaledGram():
                    return is_twice(gram._scalar) or Lattices(self.base_ring())(gram._gram).is_even()
                case _:
                    raise NotImplementedError("evenness of this infinite Gram presentation is not decided")

        def level(self):
            r"""Return the level of a finite nondegenerate integral lattice.

            This is the least ``N > 0`` annihilating the discriminant form.
            For an even lattice the relevant form is
            ``q:A_L -> QQ/2ZZ``; for an odd lattice only the bilinear pairing
            ``b:A_L^2 -> QQ/ZZ`` is canonically defined.  In particular the
            even level need not equal the exponent of ``A_L``: ``<2>`` has
            discriminant group ``ZZ/2`` but level ``4``.
            """
            if engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError("lattice level is currently implemented for integral ZZ-lattices")
            if not self.is_finite_rank() or not self.is_nondegenerate():
                raise ValueError("lattice level requires a finite nondegenerate lattice")

            discriminant = self.discriminant_module()
            generators = tuple(discriminant.module_generators())
            denominators = [
                discriminant.b(left, right).lift().denominator()
                for left in generators
                for right in generators
            ]
            if self.is_even():
                denominators.extend(
                    (discriminant.q(generator).lift() / SageZZ(2)).denominator()
                    for generator in generators
                )
            level = SageZZ.one()
            for denominator in denominators:
                level = level.lcm(SageZZ(denominator))
            return level

        @cached_method
        def genus(self):
            r"""Return the genus from signature and discriminant quadratic form.

            The current owned realization is the even, finite-rank,
            nondegenerate ``ZZ`` case, where these data determine the genus.
            """
            if engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError("the live genus object currently implements integral ZZ-lattices")
            if not self.is_finite_rank() or not self.is_nondegenerate():
                raise ValueError("a genus here requires a finite nondegenerate lattice")
            if not self.is_even():
                raise NotImplementedError(
                    "the current genus reconstruction from a discriminant quadratic form requires an even lattice"
                )
            return Genus(self.signature_pair(), self.discriminant_quadratic_form())

        def is_locally_isometric(self, other, prime) -> bool:
            r"""Return whether ``self`` and ``other`` are isometric over ``ZZ_p``."""
            if other not in Lattices(self.base_ring()):
                raise TypeError("local lattice isometry compares lattices over one base ring")
            return bool(self.genus().local_symbol(prime) == other.genus().local_symbol(prime))

        def is_unimodular(self) -> bool:
            r"""Return whether the correlation ``L -> L^#`` is an isomorphism."""
            if not self.is_nondegenerate():
                return False
            if self.is_finite_rank():
                determinant = engine_ring(self.base_ring())(self.gram_tensor().det())
                return bool(determinant.is_unit())
            from dzack_research.preamble.categories._lattice import _DiagonalGram, _IdentityGram, _ScaledGram

            gram = self.gram_tensor()
            match gram:
                case _IdentityGram():
                    return True
                case _DiagonalGram():
                    ring = engine_ring(self.base_ring())
                    return ring(gram._default).is_unit() and all(ring(value).is_unit() for value in gram._exceptions.values())
                case _ScaledGram():
                    ring = engine_ring(self.base_ring())
                    return ring(gram._scalar).is_unit() and Lattices(self.base_ring())(gram._gram).is_unimodular()
                case _:
                    raise NotImplementedError("unimodularity of this infinite Gram presentation is not decided")

        def div(self, element):
            r"""Return the divisibility ``gcd{b(element,x): x in L}`` over ``ZZ``."""
            if element.parent() is not self:
                raise TypeError("divisibility is defined for an element of this lattice")
            from dzack_research.preamble.categories._lattice import generator_pairings

            if engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError("integer divisibility is the ZZ specialization")
            pairings = [SageZZ(value) for value in generator_pairings(self, element).values()]
            return SageZZ.zero() if not pairings else abs(gcd(pairings))

        @cached_method
        def dual_module(self):
            r"""Return the algebraic dual module ``Hom_R(L,R)`` in the dual framing."""
            from dzack_research.preamble.categories.modules import BasedFreeModule

            return BasedFreeModule(self.base_ring(), self.module_generating_set())

        @cached_method
        def dual_lattice(self):
            r"""Return the metric dual ``L^#`` on the algebraic dual module.

            The underlying module remains an ``R``-module.  For a
            non-unimodular integral lattice its form takes values in
            ``Frac(R)``; it is not turned into a vector space over ``Frac(R)``.
            """
            assert self.is_nondegenerate()
            from dzack_research.preamble.categories._lattice import _IdentityGram

            if isinstance(self.gram_tensor(), _IdentityGram):
                return Lattices(self.base_ring())(self.dual_module())
            if not self.is_finite_rank():
                raise NotImplementedError("the metric dual of this infinite non-identity Gram presentation is not materialized")

            from dzack_research.preamble.categories.forms import BilinearForm
            from dzack_research.preamble.categories.rational_lattices import refine_rational_lattice

            fraction_field = self.base_ring().fraction_field()
            fraction_engine = engine_ring(fraction_field)
            dual_tensor = self.gram_tensor().change_ring(fraction_engine).dual_tensor()
            inverse_components = dual_tensor.components()
            base_engine = engine_ring(self.base_ring())
            if all(entry in base_engine for row in inverse_components for entry in row):
                from dzack_research.preamble.tensors import tensor

                integral_dual_form = tensor(
                    self.base_ring(),
                    (),
                    (int(self.rank()), int(self.rank())),
                    [
                        [base_engine(entry) for entry in row]
                        for row in inverse_components
                    ],
                )
                return Lattices(self.base_ring())(
                    integral_dual_form,
                    module_generators=self.module_generating_set(),
                )
            return refine_rational_lattice(
                BilinearForm(
                    self.dual_module(),
                    fraction_field,
                    inverse_components,
                )
            )

        def metric_dual(self):
            r"""Return the metric dual ``L^#``; explicit synonym for ``dual_lattice``."""
            return self.dual_lattice()

        def dual_basis(self):
            r"""Return the selected basis of ``L^#`` dual to the selected basis of ``L``."""
            return self.dual_lattice().module_generators()

        @cached_method
        def correlation_morphism(self):
            r"""Return ``L -> L^#``, ``v |-> b(v,-)``, whose selected-basis matrix is ``G``."""
            from dzack_research.preamble.categories._lattice import generator_pairings
            from dzack_research.preamble.categories.modules import module_homset

            assert self.is_nondegenerate()
            dual_lattice = self.dual_lattice()
            return module_homset(self, dual_lattice)(lambda label: dual_lattice.linear_combination(generator_pairings(self, self.module_generator(label))))

        def correlation(self):
            return self.correlation_morphism()

        @cached_method
        def discriminant_module(self):
            r"""Return ``A_L = coker(L -> L^#)`` with the selected dual-basis presentation."""
            from dzack_research.preamble.categories.modules.framed.formed.discriminant_modules import (
                DiscriminantModule,
            )

            return DiscriminantModule(self)

        def discriminant_projection(self):
            r"""Return the quotient morphism ``L^# -> A_L``."""
            return self.discriminant_module().projection()

        def discriminant_class(self, dual_lattice_element):
            r"""Project an element of ``L^#`` to its discriminant class."""
            if dual_lattice_element.parent() is self:
                dual_lattice_element = self.correlation_morphism()(dual_lattice_element)
            return self.discriminant_module().discriminant_class(dual_lattice_element)

        def divided_discriminant_class(self, element):
            r"""Return the class represented by ``correlation(element)/div(element)``."""
            if element.parent() is not self:
                raise TypeError("divided_discriminant_class expects an element of this lattice")
            divisibility = self.div(element)
            if divisibility == 0:
                raise ValueError("the zero vector has no divided discriminant class")
            dual_lattice = self.dual_lattice()
            correlation_image = self.correlation_morphism()(element)
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_coefficients,
            )

            divided = dual_lattice.linear_combination(
                {label: SageZZ(coefficient) // divisibility for label, coefficient in module_coefficients(correlation_image).items() if coefficient}
            )
            return self.discriminant_class(divided)

        def radical(self):
            r"""Return ``rad(L)=id_L(L)^perp`` as a subobject of ``L``."""
            return self.identity_morphism().orthogonal_complement()

        def radical_quotient(self):
            r"""Return the nondegenerate quotient ``L/rad(L)``."""
            return self.radical().isotropic_reduction()

        def overlattice(self, *discriminant_classes):
            r"""Return the inclusion ``L -> L'`` generated by discriminant classes.

            The supplied classes are lifted to ``L^#``.  Together with ``L``
            they span ``L'`` inside ``L tensor QQ``; the result is accepted
            exactly when the inherited form is integral on that span.
            """
            assert engine_ring(self.base_ring()) is SageZZ
            assert self.is_finite_rank() and self.is_nondegenerate()

            from functools import reduce

            from sage.modules.free_module import FreeModule as SageFreeModule
            from sage.rings.rational_field import QQ as SageQQ

            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                _solve_left_integrally,
                module_coefficients,
            )
            from dzack_research.preamble.categories.sets import finite_ordered_set
            from dzack_research.preamble.tensors import tensor

            discriminant_module = self.discriminant_module()
            rank = int(self.rank())
            dual_gram = self.gram_tensor().change_ring(SageQQ).dual_tensor()
            rational_rows = [[SageQQ.one() if i == j else SageQQ.zero() for j in range(rank)] for i in range(rank)]
            dual_labels = tuple(self.dual_lattice().module_generating_set())
            for discriminant_class in discriminant_classes:
                element = discriminant_class if discriminant_class.parent() is discriminant_module else discriminant_module(discriminant_class)
                lift = element.dual_lattice_lift()
                coefficients = module_coefficients(lift)
                dual_coordinates = tensor(
                    SageQQ,
                    (),
                    (rank,),
                    [coefficients.get(label, SageQQ.zero()) for label in dual_labels],
                )
                rational_rows.append(tuple(dual_gram * dual_coordinates))

            denominator = reduce(
                lambda current, coordinate: current.lcm(coordinate.denominator()),
                (coordinate for row in rational_rows for coordinate in row),
                SageZZ.one(),
            )
            scaled_rows = [[SageZZ(denominator * coordinate) for coordinate in row] for row in rational_rows]
            scaled_span = SageFreeModule(SageZZ, rank).submodule(scaled_rows)
            integral_basis = scaled_span.basis_matrix()
            basis_rows = (SageQQ.one() / denominator) * tensor.matrix(
                SageQQ, integral_basis
            )
            basis_map = basis_rows.dual_tensor()
            gram = self.gram_tensor().change_ring(SageQQ).pullback(basis_map)
            if any(entry not in SageZZ for entry in gram.list()):
                raise ValueError("the selected discriminant classes do not define an integral overlattice")

            labels = finite_ordered_set(range(rank))
            integral_gram = tensor(
                self.base_ring(),
                (),
                (rank, rank),
                [
                    [SageZZ(gram[i, j]) for j in range(rank)]
                    for i in range(rank)
                ],
            )
            enlarged = Lattices(self.base_ring())(
                integral_gram,
                module_generators=labels,
            )
            images = {}
            for source_position, source_label in enumerate(self.module_generating_set()):
                target = [denominator if index == source_position else SageZZ.zero() for index in range(rank)]
                coefficients = _solve_left_integrally(
                    integral_basis,
                    target,
                    SageZZ,
                )
                images[source_label] = enlarged.linear_combination({label: coefficient for label, coefficient in zip(labels, coefficients, strict=True) if coefficient})
            return self.Emb(enlarged)(images)

        def local_modification(self, prime, *discriminant_classes):
            r"""Return the isotropic ``p``-primary overlattice modification.

            A local modification at ``p`` is the usual discriminant-form glue
            along an isotropic subgroup contained in the ``p``-primary part of
            ``A_L``.  The returned value is the actual inclusion ``L -> L'``.
            """
            prime = SageZZ(prime)
            if not prime.is_prime():
                raise ValueError("a local modification is indexed by a prime")
            form = self.discriminant_group()
            classes = tuple(
                element if element.parent() is form else form(element)
                for element in discriminant_classes
            )
            for element in classes:
                order = SageZZ(element.additive_order())
                if order != prime ** order.valuation(prime):
                    raise ValueError(
                        f"local modification at p={prime} requires p-primary glue; "
                        f"the class {element} has order {order}"
                    )
            subgroup = form.subgroup_on(classes)
            return form.overlattice_from_isotropic_subobject(subgroup)

        def even_overlattice_inclusions(self):
            r"""Return all even overlattice inclusions ``L -> L'``.

            For an even integral lattice, Nikulin's overlattice correspondence
            identifies even overlattices with isotropic subgroups of the
            discriminant quadratic form.  The zero subgroup is included and
            therefore contributes the identity extension.
            """
            if engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError(
                    "even overlattice enumeration is currently implemented for integral ZZ-lattices"
                )
            if not self.is_even() or not self.is_finite_rank() or not self.is_nondegenerate():
                raise ValueError(
                    "even overlattice enumeration requires a finite nondegenerate even lattice"
                )
            form = self.discriminant_quadratic_form()
            return tuple(
                form.overlattice_from_isotropic_subobject(subgroup)
                for subgroup in form.isotropic_subgroups()
            )

        def embeds_in_even_unimodular(self, positive, negative) -> bool:
            r"""Decide primitive embeddability into an even unimodular ``II_{p,q}``.

            Nikulin's primitive-embedding criterion reduces this to existence
            of the orthogonal complement: its signature is the signature
            difference and its discriminant quadratic form is ``-q_L``.
            """
            positive = SageZZ(positive)
            negative = SageZZ(negative)
            if engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError(
                    "the current Nikulin primitive-embedding criterion is for integral ZZ-lattices"
                )
            if not self.is_even() or not self.is_finite_rank() or not self.is_nondegenerate():
                raise ValueError(
                    "Nikulin's primitive-embedding criterion requires a finite nondegenerate even lattice"
                )
            source_positive, source_negative = self.signature_pair()
            if (positive - negative) % 8 != 0:
                return False
            if positive < source_positive or negative < source_negative:
                return False
            complement_signature = (
                positive - source_positive,
                negative - source_negative,
            )
            return Genus(
                complement_signature,
                self.discriminant_quadratic_form().twist(-1),
            ).exists()

        def embed_in_even_unimodular(self, positive, negative):
            r"""Return one primitive embedding into an even unimodular lattice."""
            if not self.embeds_in_even_unimodular(positive, negative):
                raise ValueError(
                    f"no primitive embedding into II_{{{positive},{negative}}} exists"
                )
            from dzack_research.preamble.categories.lattice_engines import (
                oscar_even_unimodular_primitive_embedding,
            )

            target_gram, embedding_tensor = oscar_even_unimodular_primitive_embedding(
                self.gram_tensor(), positive, negative
            )
            target = Lattices(self.base_ring())(target_gram)
            target_generators = tuple(target.module_generators())
            images = tuple(
                sum(
                    (
                        embedding_tensor[row, column] * target_generators[row]
                        for row in range(int(target.rank()))
                        if embedding_tensor[row, column]
                    ),
                    target.zero(),
                )
                for column in range(int(self.rank()))
            )
            embedding = self.Emb(target)(images)
            if not embedding.is_primitive():
                raise ArithmeticError("OSCAR returned a nonprimitive embedding")
            if target.signature_pair() != (SageZZ(positive), SageZZ(negative)):
                raise ArithmeticError("OSCAR's primitive-embedding target has the wrong signature")
            return embedding

        def glue_map(self, first, second):
            r"""Return the Nikulin glue anti-isometry for a primitive extension.

            ``first`` and ``second`` are primitive orthogonal subobjects
            ``S,R <= L`` with ranks summing to ``rk(L)``.  Then

            ``L/(S + R)``

            embeds in ``A_S ⊕ A_R`` as the graph of an anti-isometry
            ``H_S -> H_R``.  The returned arrow is that anti-isometry written
            as an ordinary isometry ``H_S -> H_R(-1)``.  Its domain and
            codomain are actual formed subobjects carrying their inclusions
            into ``A_S`` and ``A_R(-1)``.

            This is the even-lattice primitive-extension correspondence of
            Nikulin.  The odd bilinear analogue remains separate.
            """
            if engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError("primitive-extension glue is currently implemented over ZZ")
            if not self.is_even():
                raise NotImplementedError(
                    "the current primitive-extension glue map uses discriminant quadratic forms and requires L even"
                )
            for subobject in (first, second):
                if not hasattr(subobject, "inclusion") or subobject.inclusion().codomain() is not self:
                    raise ValueError("glue_map requires two subobjects of this lattice")
                if not subobject.is_primitive():
                    raise ValueError("glue_map requires primitive sublattices")
            if first.rank() + second.rank() != self.rank():
                raise ValueError("glue_map requires rk(S)+rk(R)=rk(L)")
            if any(
                self.b(left, right) != self.base_ring().zero()
                for left in first.embedded_module_generators()
                for right in second.embedded_module_generators()
            ):
                raise ValueError("glue_map requires mutually orthogonal sublattices")

            from dzack_research.preamble.categories.modules import module_homset
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import (
                _torsion_module_presented_by_matrix,
            )
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
                form_embedding,
            )
            from dzack_research.preamble.categories.modules.framed.formed.torsion_form_modules import (
                TorsionQuadraticFormModules,
                _quadratic_gram_on,
                _relations_among_generators,
                torsion_form_isometry,
            )
            from dzack_research.preamble.categories.modules.subobjects import ModuleSubobjects
            from dzack_research.preamble.categories.sets import finite_ordered_set
            from dzack_research.preamble.refine import refine

            first_discriminant = first.discriminant_quadratic_form()
            second_discriminant = second.discriminant_quadratic_form()
            first_inclusion = first.inclusion().tensor()
            second_inclusion = second.inclusion().tensor()
            ambient_gram = self.gram_tensor()

            graph = {}
            for ambient_generator in self.module_generators():
                ambient_covector = ambient_gram * ambient_generator.to_vector()
                first_covector = ambient_covector * first_inclusion
                second_covector = ambient_covector * second_inclusion
                first_class = first_discriminant.linear_combination(
                    {
                        label: SageZZ(coefficient)
                        for label, coefficient in zip(
                            first_discriminant.module_generating_set(),
                            first_covector,
                            strict=True,
                        )
                        if coefficient
                    }
                )
                second_class = second_discriminant.linear_combination(
                    {
                        label: SageZZ(coefficient)
                        for label, coefficient in zip(
                            second_discriminant.module_generating_set(),
                            second_covector,
                            strict=True,
                        )
                        if coefficient
                    }
                )
                if first_class == first_discriminant.zero():
                    if second_class != second_discriminant.zero():
                        raise ArithmeticError(
                            "primitive-extension data send the zero class of A_S to a nonzero class of A_R"
                        )
                    continue
                previous = graph.get(first_class)
                if previous is not None and previous != second_class:
                    raise ArithmeticError(
                        "primitive-extension data do not define a function H_S -> H_R"
                    )
                graph[first_class] = second_class

            source_classes = tuple(graph)
            target_classes = tuple(graph[value] for value in source_classes)
            labels = finite_ordered_set(range(len(source_classes)))
            relations = _relations_among_generators(first_discriminant, source_classes)
            abstract_glue = _torsion_module_presented_by_matrix(relations, labels)

            quadratic_values = first_discriminant.quadratic_value_module()
            source_form = TorsionQuadraticFormModules(self.base_ring()).from_module(
                abstract_glue,
                _quadratic_gram_on(first_discriminant, source_classes),
                quadratic_values,
            )
            target_gram = tuple(
                tuple(-entry for entry in row)
                for row in _quadratic_gram_on(second_discriminant, target_classes)
            )
            target_form = TorsionQuadraticFormModules(self.base_ring()).from_module(
                abstract_glue,
                target_gram,
                quadratic_values,
            )

            source_embedding = form_embedding(
                source_form,
                first_discriminant,
                {
                    label: source_class
                    for label, source_class in zip(labels, source_classes, strict=True)
                },
                quadratic=True,
            )
            source_form._preamble_inclusion = source_embedding
            refine(source_form, ModuleSubobjects(self.base_ring()))

            second_twist = second_discriminant.twist(-1)
            target_embedding = form_embedding(
                target_form,
                second_twist,
                {
                    label: second_twist.equip_form_morphism()(target_class)
                    for label, target_class in zip(labels, target_classes, strict=True)
                },
                quadratic=True,
            )
            target_form._preamble_inclusion = target_embedding
            refine(target_form, ModuleSubobjects(self.base_ring()))

            target_subgroup = second_discriminant.subgroup_on(target_classes)
            extension_index = first.sum(second).index()
            if source_form.cardinality() != extension_index:
                raise ArithmeticError(
                    "the recovered glue subgroup does not have order [L:S+R]"
                )
            if target_subgroup.cardinality() != extension_index:
                raise ArithmeticError(
                    "the two primitive-extension glue subgroups have different orders"
                )

            forward = module_homset(source_form, target_form)(
                {
                    label: target_form.module_generator(label)
                    for label in labels
                }
            )
            inverse = module_homset(target_form, source_form)(
                {
                    label: source_form.module_generator(label)
                    for label in labels
                }
            )
            return torsion_form_isometry(forward, inverse, quadratic=True)

        @cached_method
        def discriminant_bilinear_form(self):
            r"""Return ``A_L`` with its descended ``K/R``-valued bilinear form."""
            from dzack_research.preamble.categories.modules.framed.formed.discriminant_modules import (
                DiscriminantBilinearModules,
                DiscriminantQuadraticModules,
            )

            module = self.discriminant_module()
            assert module in DiscriminantBilinearModules(self.base_ring())
            if module in DiscriminantQuadraticModules(self.base_ring()):
                return module.associated_bilinear_form()
            return module

        def discriminant_quadratic_form(self):
            r"""Return ``A_L`` with its ``K/2R``-valued quadratic form when ``L`` is even."""
            from dzack_research.preamble.categories.modules.framed.formed.discriminant_modules import (
                DiscriminantQuadraticModules,
            )

            if not self.is_even():
                raise ValueError("a discriminant quadratic form requires an even lattice")
            module = self.discriminant_module()
            assert module in DiscriminantQuadraticModules(self.base_ring())
            return module

        def discriminant_group(self):
            r"""Return the ``ZZ`` discriminant group with every form supported by ``L``."""
            if engine_ring(self.base_ring()) is not SageZZ:
                raise TypeError("discriminant_group is the ZZ specialization; use discriminant_module")
            return self.discriminant_quadratic_form() if self.is_even() else self.discriminant_bilinear_form()

        def discriminant_length(self):
            r"""Return the minimal number of generators of ``A_L`` over ``ZZ``."""
            if engine_ring(self.base_ring()) is not SageZZ:
                raise TypeError("discriminant length is currently the integral-lattice invariant")
            return SageZZ(len(tuple(invariant for invariant in self.discriminant_module().invariants() if abs(SageZZ(invariant)) > 1)))

        def is_p_elementary(self, prime) -> bool:
            r"""Return whether ``A_L`` is an elementary abelian ``prime``-group."""
            if engine_ring(self.base_ring()) is not SageZZ:
                raise TypeError("p-elementarity is currently the integral-lattice invariant")
            prime = SageZZ(prime)
            if not prime.is_prime():
                raise ValueError("p-elementarity requires a prime p")
            invariants = tuple(abs(SageZZ(invariant)) for invariant in self.discriminant_module().invariants() if abs(SageZZ(invariant)) > 1)
            return all(invariant == prime for invariant in invariants)

        def delta(self):
            r"""Return Nikulin's ``delta`` for an even 2-elementary lattice.

            This is zero exactly when the discriminant quadratic form is
            integer-valued, and one otherwise.  It suffices to test Smith
            generators: on a 2-elementary discriminant group every bilinear
            value lies in ``(1/2)ZZ/ZZ``, so the cross term ``2b(x,y)`` in
            ``q(x+y)`` is integral.
            """
            if engine_ring(self.base_ring()) is not SageZZ:
                raise TypeError("Nikulin's delta is an integral-lattice invariant")
            if not self.is_even() or not self.is_p_elementary(SageZZ(2)):
                raise ValueError("Nikulin's delta requires an even 2-elementary lattice")
            discriminant_form = self.discriminant_quadratic_form()
            return SageZZ(any(discriminant_form.q(element).lift() not in SageZZ for element in discriminant_form.smith_form_module_generators()))

        def two_elementary_invariants(self):
            r"""Return Nikulin's ``(r,a,delta)`` for an even 2-elementary lattice."""
            if not self.is_p_elementary(SageZZ(2)) or not self.is_even():
                raise ValueError("the lattice is not even and 2-elementary")
            return (SageZZ(self.rank()), self.discriminant_length(), self.delta())

        def reflection(self, root):
            r"""Return the integral orthogonal reflection in ``root``.

            A lattice root is defined by this integrality: for every selected
            module generator ``e_i``, ``2*b(e_i,root)/b(root,root)`` must lie
            in the base ring.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: U = Lattices(ZZ)("U")
                sage: root = U.module_generator(0) + U.module_generator(1)
                sage: U.reflection(root)(U.module_generator(0))
                -e_1
            """
            if root.parent() is not self:
                raise TypeError("the reflecting vector must belong to this lattice")
            if not root.is_root():
                raise ValueError(f"{root} does not define an integral lattice reflection")
            ring = engine_ring(self.base_ring())
            fraction_field = ring if ring.is_field() else ring.fraction_field()
            norm = fraction_field(root.q())
            return self.Aut()(lambda label: self.module_generator(label) - ring(fraction_field(2 * self.module_generator(label).b(root)) / norm) * root)

        def is_positive_definite(self) -> bool:
            return bool(self.is_finite_rank() and self.signature_pair() == (self.rank(), 0))

        def is_negative_definite(self) -> bool:
            return bool(self.is_finite_rank() and self.signature_pair() == (0, self.rank()))

        def is_definite(self) -> bool:
            return self.is_positive_definite() or self.is_negative_definite()

        def lll_reduction(self):
            from dzack_research.preamble.categories.definite_lattices import lll_reduction

            return lll_reduction(self)

        def LLL(self):
            r"""Return the same formed lattice in an LLL-reduced framing."""
            return self.lll_reduction().reduced

        def bkz_reduction(self, block_size=20):
            from dzack_research.preamble.categories.definite_lattices import bkz_reduction

            return bkz_reduction(self, block_size=block_size)

        def BKZ(self, block_size=20):
            r"""Return the same formed lattice in a BKZ-reduced framing."""
            return self.bkz_reduction(block_size=block_size).reduced

        def hkz_reduction(self):
            from dzack_research.preamble.categories.definite_lattices import hkz_reduction

            return hkz_reduction(self)

        def HKZ(self):
            r"""Return the full-block BKZ (HKZ) reframing."""
            return self.hkz_reduction().reduced

        def minimum(self):
            from dzack_research.preamble.categories.definite_lattices import minimum

            return minimum(self)

        def vectors_of_square(self, square):
            from dzack_research.preamble.categories.definite_lattices import vectors_of_square

            return vectors_of_square(self, square)

        def vectors_of_square_and_divisibility(self, square, divisibility):
            from dzack_research.preamble.categories.definite_lattices import (
                vectors_of_square_and_divisibility,
            )

            return vectors_of_square_and_divisibility(self, square, divisibility)

        def roots(self):
            from dzack_research.preamble.categories.definite_lattices import roots

            return roots(self)

        def roots_of_square(self, square):
            from dzack_research.preamble.categories.definite_lattices import roots_of_square

            return roots_of_square(self, square)

        def root_sublattice(self):
            from dzack_research.preamble.categories.definite_lattices import root_sublattice

            return root_sublattice(self)

        def vector_primitive_extension(self, element):
            r"""Return the primitive-extension/gluing datum cut out by ``element``."""
            from dzack_research.preamble.categories.vector_orbits import (
                VectorPrimitiveExtension,
            )

            return VectorPrimitiveExtension(self, element)

        def definite_complement_extensions(self, left, right):
            r"""Return all isometries ``g`` with ``g(left)=right`` in the definite-complement regime."""
            from dzack_research.preamble.categories.vector_orbits import (
                definite_complement_extensions,
            )

            return definite_complement_extensions(self, left, right)

        def gluing_route_discriminant_classes(self, left, right):
            r"""Return admissible ``O(A_L)`` classes from the primitive-extension gluing route."""
            from dzack_research.preamble.categories.vector_orbits import (
                gluing_route_discriminant_classes,
            )

            return gluing_route_discriminant_classes(self, left, right)

        def stable_complement_root_reflections(self, element):
            r"""Return stable reflections in root-orbit representatives of ``element^perp``."""
            from dzack_research.preamble.categories.vector_orbits import (
                stable_complement_root_reflections,
            )

            return stable_complement_root_reflections(self, element)

        def primitive_isotropic_subobject(self, *basis):
            from dzack_research.preamble.categories.isotropic_orbits import (
                primitive_isotropic_subobject,
            )

            return primitive_isotropic_subobject(self, basis)

        def isotropic_flag(self, *basis):
            from dzack_research.preamble.categories.isotropic_orbits import IsotropicFlag

            return IsotropicFlag(self, basis)

        def isotropic_line_orbit_representatives(self):
            return self.O().isotropic_orbit_representatives(1)

        def isotropic_plane_orbit_representatives(self):
            return self.O().isotropic_orbit_representatives(2)

        def isotropic_flag_orbit_representatives(self, rank=2):
            return self.O().isotropic_orbit_representatives(rank, flag=True)

        def shortest_vectors(self):
            from dzack_research.preamble.categories.definite_lattices import shortest_vectors

            return shortest_vectors(self)

        def theta_series(self, precision=20, variable="q"):
            from dzack_research.preamble.categories.definite_lattices import theta_series

            return theta_series(self, precision=precision, variable=variable)

        def hermite_invariant(self):
            from dzack_research.preamble.categories.definite_lattices import hermite_invariant

            return hermite_invariant(self)

        def successive_minima(self):
            from dzack_research.preamble.categories.definite_lattices import successive_minima

            return successive_minima(self)

        def gaussian_heuristic(self, *, exact_form=False):
            from dzack_research.preamble.categories.definite_lattices import gaussian_heuristic

            return gaussian_heuristic(self, exact_form=exact_form)

        def hadamard_ratio(self):
            from dzack_research.preamble.categories.definite_lattices import hadamard_ratio

            return hadamard_ratio(self)

        def closest_vector(self, target):
            from dzack_research.preamble.categories.definite_lattices import closest_vector

            return closest_vector(self, target)

        def babai(self, target):
            from dzack_research.preamble.categories.definite_lattices import babai

            return babai(self, target)

        approximate_closest_vector = babai

        def voronoi_cell(self, bound=None):
            from dzack_research.preamble.categories.definite_lattices import voronoi_cell

            return voronoi_cell(self, bound=bound)

        def voronoi_relevant_vectors(self):
            from dzack_research.preamble.categories.definite_lattices import (
                voronoi_relevant_vectors,
            )

            return voronoi_relevant_vectors(self)

        def contact_polytope(self):
            from dzack_research.preamble.categories.definite_lattices import contact_polytope

            return contact_polytope(self)

        def packing_radius(self):
            from dzack_research.preamble.categories.definite_lattices import packing_radius

            return packing_radius(self)

        def covering_radius(self):
            from dzack_research.preamble.categories.definite_lattices import covering_radius

            return covering_radius(self)

        def center_density(self):
            from dzack_research.preamble.categories.definite_lattices import center_density

            return center_density(self)

        def packing_density(self):
            from dzack_research.preamble.categories.definite_lattices import packing_density

            return packing_density(self)

        def kissing_number(self):
            from dzack_research.preamble.categories.definite_lattices import kissing_number

            return kissing_number(self)

        def twist(self, scalar):
            r"""Keep the module and rescale its form by ``scalar``.

            The result is the same free module with
            \(b'(x,y)=\mathrm{scalar}\cdot b(x,y)\).  The Gram is
            scaled as a type-$(0,2)$ tensor: a pairing rule is not
            materialized as a finite array.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Iinf = Lattices(ZZ)(ZZ^NN)
                sage: Iinf.module_generator(0)^2
                1
                sage: Iinf.twist(2).module_generator(0)^2
                2
                sage: latex(Iinf.twist(2).gram_tensor())
                2\,I_{\infty}
                sage: Iinf.twist(2).gram_tensor()
                2 I_∞ ∈ (ZZ^NN ⊗ ZZ^NN)*
            """
            from dzack_research.preamble.categories._lattice import (
                _PairingGram,
                scale_gram_tensor,
            )

            scaled = scale_gram_tensor(self.gram_tensor(), self.base_ring()(scalar))
            match scaled:
                case _PairingGram():
                    return Lattices(self.base_ring())(scaled)
                case _:
                    return Lattices(self.base_ring())(
                        scaled,
                        module_generators=self.module_generating_set(),
                    )

        def __add__(self, other):
            r"""Return the orthogonal direct sum.

            Finite \(\oplus\) finite and finite \(\oplus\) infinite, in
            the concatenated basis.  Infinite \(\oplus\) infinite is
            not constructed.  ``sum([...])`` uses ``0 + L``.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)("U") + Lattices(ZZ)(ZZ^NN)
                Integral lattice of rank +Infinity and signature (+Infinity, 1)
            """
            if other == 0:
                return self
            from dzack_research.preamble.categories._lattice import orthogonal_sum

            ring = self.base_ring()
            category = Lattices(ring)
            assert other in category
            return orthogonal_sum(self, other, category=category)

        def __radd__(self, other):
            if other == 0:
                return self
            return NotImplemented

        def _repr_(self):
            r"""Name the lattice by rank and, over \(\mathbb{Q}\), signature.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)("U")
                Integral lattice of rank 2 and signature (1, 1)
            """
            from sage.rings.integer_ring import ZZ
            from sage.rings.rational_field import QQ

            from dzack_research.preamble.categories.rings import engine_ring

            kind = "Integral lattice" if engine_ring(self.base_ring()) is ZZ else "Lattice"
            rank = self.rank()
            if engine_ring(self.base_ring().fraction_field()) is QQ:
                pos, neg = self.signature_pair()
                return f"{kind} of rank {rank} and signature ({pos}, {neg})"
            return f"{kind} of rank {rank} over {self.base_ring()}"

        def _latex_(self):
            r"""Display $L$ with its invariants; the Gram is $G_L$, not $L$.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: latex(Lattices(ZZ)("U"))
                \begin{gathered}
                L \in \mathrm{Lattices}(\mathbb{Z}), \quad \mathrm{rk}(L) = 2, \quad \mathrm{sig}(L) = (1, 1), \quad \mathrm{disc}(L) = 1 \\
                L = U \\
                G_L = \left(\begin{array}{rr}
                \cdot & 1 \\
                1 & \cdot
                \end{array}\right) \\
                \end{gathered}
            """
            from dzack_research.preamble.categories._lattice import lattice_latex

            _name, tex = _ring_notation(self.base_ring())
            return lattice_latex(self, tex)

    class ElementMethods:
        r"""Operations generic to every lattice element."""

        def b(self, other):
            r"""Return \(b(v,w)\) by contracting the Gram tensor on \(v\) and \(w\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: I2 = Lattices(ZZ)(ZZ^2)
                sage: e, f = I2.module_generator(0), I2.module_generator(1)
                sage: e.b(f), e*e
                (0, 1)
            """
            assert other.parent() is self.parent()
            return self.parent().b(self, other)

        def q(self):
            r"""Return \(q(v)=b(v,v)\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: U = Lattices(ZZ)("U")
                sage: root = U.module_generator(0) + U.module_generator(1)
                sage: root.q()
                2
            """
            return self.b(self)

        def norm(self):
            r"""Return the form norm ``b(v,v)``."""
            return self.q()

        def divisibility_ideal(self):
            return self.parent().divisibility_ideal(self)

        def div(self):
            r"""Return the positive integer generator of ``b(v,L)`` over ``ZZ``.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)(ZZ^NN).module_generator(0).div()
                1
            """
            return self.parent().div(self)

        def divided_discriminant_class(self):
            return self.parent().divided_discriminant_class(self)

        def is_root(self) -> bool:
            r"""Return whether the orthogonal reflection in this vector is integral.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Iinf = Lattices(ZZ)(ZZ^NN)
                sage: Iinf.module_generator(0).is_root()
                True
                sage: Iinf((2, 1)).is_root()
                False
            """
            from dzack_research.preamble.categories._lattice import generator_pairings

            parent = self.parent()
            ring = engine_ring(parent.base_ring())
            assert ring.is_integral_domain()
            norm = ring(self.q())
            if norm == 0:
                return False
            fraction_field = ring if ring.is_field() else ring.fraction_field()
            norm_in_fraction_field = fraction_field(norm)
            for coefficient in generator_pairings(parent, self).values():
                try:
                    ring(fraction_field(2 * coefficient) / norm_in_fraction_field)
                except TypeError, ValueError:
                    return False
            return True

        def monomial_coefficients(self):
            return self.parent()._monomial_coefficients(self._vector)

        def to_list(self):
            r"""Return the coordinates of this element as a Python list."""
            from sage.rings.infinity import Infinity

            parent = self.parent()
            coefficients = parent._monomial_coefficients(self._vector)
            keys = parent.module_generating_set()
            zero = parent.base_ring().zero()
            rank = parent.rank()
            if rank == Infinity:
                if not coefficients:
                    return []
                last = max(int(keys.rank(key)) for key in coefficients)
                return [coefficients.get(keys.unrank(index), zero) for index in range(last + 1)]
            return [coefficients.get(key, zero) for key in keys]

        def to_tuple(self):
            r"""Return the coordinates of this element as a Python tuple."""
            return tuple(self.to_list())

        def to_vector(self):
            r"""Return the coordinates of this element as a vector tensor of type $(1,0)$.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)(ZZ^2).module_generator(0).to_vector()
                (1, 0)
            """
            from dzack_research.preamble.tensors import tensor

            return tensor.vector(self.parent().base_ring(), self.to_list())
