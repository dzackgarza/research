r"""``IntegralLattices`` — a category owning the lattice-specific API.

Refine any integral lattice parent into this category to gain::

    q(x), b(x, y), div(x), get_isotropic_type(element)
    dual_basis(), I_perp_mod_I(vectors), is_isometric(other)
    with_names(spec), to_lin_comb_module_generators(element), sublattices
    _latex_()                   # multi-line Gram + discriminant display
    _first_ngens(count)         # generator sugar for ``L.<...> = ...``
    twist(*, names=...)         # twisted copy with optional naming
    __add__, __pow__, direct_sum      # orthogonal direct sums with subdivisions
    Aut(), invariant_lattice(action), formed_coinvariants(action),
    coinvariant_lattice(action)

Coordinate data are not themselves lattice elements. A tuple, list, or vector
of coefficients is converted to an element only by choosing module generators and
forming the explicit sum $\sum_i c_i\,g_i$ in that module's own free basis.

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
    sage: L.q(L.module_generators()[0])
    0
"""

from typing import TYPE_CHECKING
from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet
from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import MorphismMatrix
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Element
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from dzack_research.preamble.lexicon import LatticeName
    from sage.categories.modules import Module
    from dzack_research.preamble.lexicon import ModuleElement
    from sage.structure.parent import ElementConstructorInput

from sage.categories.morphism import SetMorphism
from sage.categories.homset import Hom
from sage.structure.parent import Parent
from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
from sage.matrix.special import block_diagonal_matrix
from sage.modules.free_module_element import vector
if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.direct_sum_objects import DirectSumObject
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import GroupAction
    from sage.categories.homset import Homset
    from sage.combinat.root_system.cartan_type import CartanType
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphismGroup
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
    from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism
    from sage.structure.element import RingElement
    from dzack_research.preamble.categories.sets.sets import Set
    from sage.quadratic_forms.genera.genus import GenusSymbol_global_ring
    from sage.quadratic_forms.binary_qf import BinaryQF
    from sage.rings.ring import Ring

from sage.matrix.matrix0 import Matrix
import re
from collections.abc import Iterable
from functools import reduce
from typing import Protocol, TYPE_CHECKING, assert_never

from sage.arith.misc import gcd
from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from dzack_research.preamble.categories.modules.framed.formed.lattices import Lattices
from dzack_research.preamble.categories.modules.framed.formed.lattice_axioms import FinitelyGeneratedLattices
from sage.categories.groups import Groups as SageGroups
from sage.misc.cachefunc import cached_method
from sage.categories.modules import Modules
from sage.matrix.constructor import matrix
from sage.matrix.special import identity_matrix
from sage.misc.latex import latex as _latex_fn
from sage.rings.integer import Integer
from dzack_research.preamble.categories.rings.rings import ℤ
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.lexicon import GramMatrix
from dzack_research.preamble.categories.sets.owned_sets import Sets

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet

    from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
        FiniteFreeFormedParent,
        FormedElement,
    )

    class LatticeParent(FiniteFreeFormedParent, Protocol):
        r"""What an object of this category offers.

        Structural rather than a class: a lattice is in this category by
        refinement, so what it answers is decided by placement and the
        carried data, not by which class built it.
        """

    class LatticeElement(FormedElement, Protocol):
        r"""What an element of a lattice in this category offers."""


class FinitelyGeneratedIntegralLattices(CategoryWithAxiom_over_base_ring):
    r"""Finitely generated lattices whose form is integral-valued."""

    _base_category_class_and_axiom = (FinitelyGeneratedLattices, "Integral")

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely generated integral-valued lattices"


class IntegralLattices(CategoryWithAxiom_over_base_ring):
    r"""Category of integral lattices with enriched computational methods.

    Unlike Sage's default::

        - quadratic and bilinear forms via ``q`` / ``b`` / ``div``
        - dual basis, isotropic quotients, isometry checking
        - basis naming, linear-combination display, LaTeX with discriminant-module info
        - orthogonal direct sums with automatic Gram-matrix subdivisions
        - lattice-element arithmetic: multiplication -> bilinear pairing, exponentiation -> q
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "integral lattices"

    # An integral lattice is finite, integral-valued, and nondegenerate.
    _base_category_class_and_axiom = (
        FinitelyGeneratedIntegralLattices,
        "Nondegenerate",
    )

    @staticmethod
    def __classcall_private__(
        cls: type["IntegralLattices"],
        base_ring: "Ring | Category | None" = None,
    ) -> "IntegralLattices":
        r"""Default the base ring to the integers.

        Lattices are $R$-lattices and the category is parametrized by $R$;
        over $\ZZ$ is the case a session means when it says no ring, and
        saying so here keeps the general statement without making every call
        site name the ring.
        """
        from sage.categories.category import Category
        from sage.rings.integer_ring import ZZ as _ZZ

        if base_ring is None:
            base_ring = _ZZ
        if isinstance(base_ring, Category):
            over_category: "IntegralLattices" = super(
                IntegralLattices, cls
            ).__classcall__(cls, base_ring)
            return over_category
        category: "IntegralLattices" = super(IntegralLattices, cls).__classcall__(
            cls, base_ring
        )
        return category

    class ParentMethods:
        r"""Methods available on every integral lattice parent refined into this category."""

        # ---- bilinear / quadratic API ----

        @cached_method
        def decomposition(self: "LatticeParent") -> "DirectSumObject":
            r"""Return the chosen block decomposition, or ``None``.

            Computed when asked, and not while the lattice is being built.
            Splitting a lattice builds each block as a lattice, and a block
            that split itself in turn made construction recursive: one
            $U\oplus E_8$ cost 2,502 constructions and 2,579 rational
            diagonalizations, none of which anything had asked for.  A
            decomposition is an answer to a question, so it waits for the
            question.
            """
            return _decompose_lattice(self)

        def summands(self: "LatticeParent") -> tuple:
            decomposition = self.decomposition()
            assert decomposition is not None, (
                "this lattice has no chosen nontrivial block decomposition"
            )
            summands: tuple = decomposition.summands()
            return summands

        def is_decomposable(self: "LatticeParent") -> bool:
            return self.decomposition() is not None

        def q(self: "LatticeParent", x: "Element") -> "Element":
            r"""Return the quadratic form $q(x) = \langle x, x\rangle$."""
            return x.norm()

        def b(self: "LatticeParent", x: "Element", y: "Element") -> "Element":
            r"""Return the pairing $\langle x, y\rangle$, asked of the two elements."""
            return x.b(y)

        def div(self: "LatticeParent", x: "Element") -> "Integer":
            r"""Return the positive generator of $\{\langle x, y\rangle : y \in L\}$."""
            pairings = [self.b(x, v) for v in self.module_generators()]
            return abs(gcd(pairings))

        def gram_of(self: "LatticeParent", vectors: "OrderedSet") -> GramMatrix:
            r"""Return the Gram matrix $[b(x_i, x_j)]$ of a finite family of vectors."""
            vectors = tuple(vectors)
            return GramMatrix(matrix(SageZZ, [[self.b(x, y) for y in vectors] for x in vectors]))

        def get_isotropic_type(self: "LatticeParent", isotropic_element: "ModuleElement") -> str:
            r"""Classify a primitive isotropic element by its cusp type.

            Divisibility 1 gives ``"Odd"``. Divisibility 2 is distinguished
            by whether $e^* = e/2 \in A_L$ is characteristic.
            """
            assert isotropic_element in self, (
                f"get_isotropic_type is about an element of {self}, and this is "
                f"{isotropic_element!r}"
            )
            assert self.q(isotropic_element) == 0, (
                f"expected an isotropic element, got square {self.q(isotropic_element)}"
            )
            assert isotropic_element.is_primitive(), "expected a primitive element"
            divisibility = self.div(isotropic_element)
            assert divisibility in (1, 2), (
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

        def dual_basis(self: "LatticeParent") -> "OrderedSet":
            r"""Return the dual generators $e_i^\vee$, which are elements of $L^\vee$.

            Defined by $\langle e_i, e_j^\vee\rangle=\delta_{ij}$, and that
            pairing is $L^\vee$'s: $c$ carries $e_i$ there and the form of
            $L^\vee$ pairs the two.  Which is why these are not vectors of
            $L\otimes\mathbb Q$ -- there is no space here containing both $L$
            and its dual for a pairing to happen in, and writing $e_i+e_j^\vee$
            means applying $c$ first.
            """
            dual = self.dual_lattice()
            correlation = self.correlation()
            generators = tuple(dual.module_generators())
            assert all(
                correlation(v).b(w) == (1 if i == j else 0)
                for i, v in enumerate(self.module_generators())
                for j, w in enumerate(generators)
            ), "the proposed dual generators are not dual to the generators"
            return generators

        # ---- isotropic quotients ----

        def I_perp_mod_I(self: "LatticeParent", vectors: "OrderedSet") -> "Module":
            r"""Return $I^\perp/I$ for the isotropic subobject ``vectors`` span.

            The isotropic reduction of that subobject, under the name this
            category has always called it by.
            """
            return self.subobject_on(vectors).isotropic_reduction()

        # ---- overlattices ----

        def dual_lattice_module_generators(self: "LatticeParent") -> "OrderedSet":
            r"""Return the explicit module generators of $L^*$."""
            return tuple(self.dual_lattice().module_generators())

        def dual_embedding(self: "LatticeParent") -> "ModuleMorphism":
            r"""Return the inclusion morphism $L\to L^*$."""
            return self.correlation()

        def discriminant_projection(self: "LatticeParent") -> "FormMorphism":
            r"""Return the quotient morphism $\pi: L^* \to A_L$.

            The target $A_L$ carries the discriminant bilinear form for any
            nondegenerate lattice and the discriminant quadratic form when $L$ is
            even.
            """
            return self.discriminant_group().projection()

        def project_to_discriminant_bilinear_form(self: "LatticeParent", element: "Element") -> "Element":
            r"""Project an element of $L^\vee$ to its class in the discriminant bilinear form $A_L$.

            This applies the quotient morphism
            $\pi: L^\vee\to A_L$. It does not accept coordinate rows; first
            construct elements of $L^\vee$ with :meth:`correlation` applied to an
            element of $L$.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModuleElement
            projection = self.discriminant_projection()
            assert (
                isinstance(element, FormModuleElement)
                and element.parent() is projection.domain()
            ), (
                f"pi is defined on {projection.domain()}, and this is "
                f"{element!r}. An element of L^\vee is obtained as "
                "correlation()(v) for some v in L."
            )
            return projection(element)

        def project_to_discriminant_quadratic_form(self: "LatticeParent", element: "Element") -> "Element":
            r"""Project an element of $L^\vee$ to its class in $A_L$ with quadratic form.

            This method is defined only for even lattices.
            """
            assert self.is_even(), "the discriminant quadratic form exists only for even lattices"
            return self.project_to_discriminant_bilinear_form(element)

        def divided_discriminant_class(self: "LatticeParent", element: "Element") -> "Element":
            r"""Return the discriminant element represented by $e/\operatorname{div}(e)$."""
            assert element in self, "divided_discriminant_class expects an element of this lattice"
            divisibility = self.div(element)
            dual_element = self.correlation()(element) / divisibility
            return self.discriminant_projection()(dual_element)

        def glue(self: "LatticeParent", *elements: "OrderedSet") -> "FormModule":
            r"""Return the even overlattice glued along discriminant elements.

            The inputs are elements of the discriminant form $A_L = L^\vee/L$
            (quadratic for even lattices, bilinear for odd).
            Their lifts in $L^\vee$ generate the overlattice together with the
            original lattice.  Catalogue entries should construct elements of
            $L^\vee$ and project them to $A_L$ before calling this method.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            rank = self.rank()
            rational_rows = [
                [1 if i == j else 0 for j in range(rank)]
                for i in range(rank)
            ]
            rational_rows.extend(
                _discriminant_lift_row(element, rank) for element in elements
            )

            denominator = reduce(
                lambda current, coordinate: current.lcm(
                    coordinate.denominator()
                ),
                (
                    coordinate
                    for row in rational_rows
                    for coordinate in row
                ),
                1,
            )

            scaled = matrix(
                SageZZ,
                [
                    [denominator * coordinate for coordinate in row]
                    for row in rational_rows
                ],
            )
            hermite_rows = [
                row
                for row in MorphismMatrix(scaled).normal_form(include_zero_rows=True).rows()
                if any(coordinate != 0 for coordinate in row)
            ]
            basis = matrix(SageQQ, hermite_rows[:rank]) / denominator
            gram = basis * self.gram_matrix() * basis.transpose()
            module_generating_set = finite_ordered_set(
                tuple(tuple(row) for row in basis.rows())
            )
            return _lattice_with_gram(
                matrix(SageZZ, gram),
                module_generating_set,
            )

        def maximal_overlattice(self: "LatticeParent") -> "FormMorphism":
            r"""Return $L\hookrightarrow L'$ for an overlattice admitting no other.

            Nikulin Prop. 1.4.1: the overlattices of $L$ on which the form
            stays integral are in bijection with the isotropic subgroups of
            the discriminant form, an overlattice being maximal exactly when
            its subgroup is.  So nothing here searches for a lattice.  The
            search runs on $A_L$, where it is a finite one, and
            :meth:`glue` turns the classes it returns back into the lattice
            they name.

            Which form has to vanish is $A_L$'s business and follows $L$:
            an even $L$ has a $q$ and its overlattices are the even ones,
            while an odd $L$ has only $b$ and the integral ones is what the
            bijection then covers.

            *An* overlattice.  Maximal isotropic subgroups need not be
            unique and need not glue to isometric lattices, so a maximal
            overlattice is what this is, not the maximal one.
            """
            form = self.discriminant_group()
            return form.overlattice_from_isotropic_subobject(
                next(form.maximal_isotropic_subobjects())
            )

        def overlattice(
            self: "LatticeParent", *elements: "OrderedSet"
        ) -> "FormMorphism":
            r"""Return $L\hookrightarrow L'$ glued along discriminant classes.

            The same Nik80 Prop. 1.4.1 correspondence as :meth:`glue`,
            morphism-valued: the constructor is the once-only place the
            presentation crosses the boundary, so it is where the inclusion
            witness is minted.  Callers wanting the object alone take
            ``.codomain()``; the index is the arrow's own ``.index()``.  For
            a direct-sum $L$, the summand inclusions carried into $L'$ are
            the decomposition's own witnesses composed with this inclusion:
            ``summand.embedding().then(inclusion)`` per entry of
            :meth:`summands`.
            """
            form = self.discriminant_group()
            return form.overlattice_from_isotropic_subobject(
                form.subobject_generated_by(
                    tuple(form(element) for element in elements)
                )
            )

        def local_modification(
            self: "LatticeParent", p: "Integer", *elements: "OrderedSet"
        ) -> "FormMorphism":
            r"""Return $L\hookrightarrow L'$ glued along a $p$-primary
            isotropic subgroup of $A_L$.

            The local-modification vocabulary (Nik80, Zotero TTY9FFJS,
            section 1.4): an overlattice differing from $L$ only over $p$
            is glued along an isotropic subgroup of the $p$-primary part of
            the discriminant form.  $p$-primality of each class is its
            order being a power of $p$, asserted by name; the glue itself
            is the same morphism-valued correspondence as
            :meth:`overlattice`, whose construction asserts isotropy.
            """
            form = self.discriminant_group()
            for element in elements:
                order = form(element).order()
                assert order == p ** order.valuation(p), (
                    f"local modification at p={p} glues along the p-primary "
                    f"part of the discriminant form; the class {element} has "
                    f"order {order}"
                )
            return self.overlattice(*elements)

        # There is no separate ``summand_embeddings``: :meth:`summands`
        # already returns subobjects, each carrying its inclusion as
        # ``summand.embedding()`` (minted by ``_decompose_lattice``).

        # ---- isometry ----

        def Isom(self: "LatticeParent", codomain: "FormModule") -> "Homset":
            r"""Return $\operatorname{Isom}(L, M)$ as a first-class parent.

            Existence, witness, cardinality, and enumeration of isometries
            are the homset's own questions (ratified method placement);
            :meth:`is_isometric` is its emptiness router.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.lattice_homomorphisms import IsometryHomset
            return IsometryHomset(self, codomain)

        def Emb(self: "LatticeParent", codomain: "FormModule") -> "Homset":
            r"""Return $\operatorname{Emb}(L, M)$ as a first-class parent:
            the form-preserving monomorphisms, enumerated by module-generator
            placement where the codomain is integral definite (indefinite
            existence is issue #24's Nikulin engine, a stated absence)."""
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.lattice_homomorphisms import EmbeddingHomset
            return EmbeddingHomset(self, codomain)

        def is_isometric(self: "LatticeParent", other: "FormModule") -> "bool | Unknown":
            r"""Decide whether two integral lattices are isometric.

            Existence of an isometry is the emptiness question of
            $\operatorname{Isom}(L, M)$, so the decision table -- and every
            theorem it runs on -- lives on that homset
            (:class:`IsometryHomset`); this method is its router.  The
            undecided regimes (indefinite binary; a genus splitting into
            several improper spinor genera) come back as the three-valued
            ``Unknown``, which collapses to ``False`` in boolean context.
            """
            from sage.misc.unknown import Unknown

            empty = self.Isom(other).is_empty()
            if empty is Unknown:
                return Unknown
            return not empty

        def reflection(self: "LatticeParent", vector: "Element") -> "ModuleMorphism":
            r"""Return $s_v\in O(L)$, $s_v(x)=x-\dfrac{2\,b(x,v)}{q(v)}\,v$.

            The reflection in the hyperplane $v^\perp$, an element of
            $\mathrm{Aut}(L)$ constructed by its images on the framing
            labels.  Defined for anisotropic $v$; it preserves $L$ exactly
            when every coefficient $2\,b(e_i,v)/q(v)$ is integral, which is
            what makes $v$ a root, and that integrality is asserted rather
            than assumed.
            """
            from sage.structure.element import Element as SageElement

            element = (
                vector
                if isinstance(vector, SageElement) and vector.parent() is self
                else self(vector)
            )
            norm = element.q()
            assert norm != 0, (
                f"reflection is defined in an anisotropic vector; q(v)=0 for v={element}"
            )
            images = {}
            for label in self.module_generating_set():
                generator = self.module_generator(label)
                coefficient = 2 * generator.b(element) / norm
                assert coefficient in self.base_ring(), (
                    f"s_v does not preserve the lattice: 2 b({generator}, {element})/q({element}) "
                    f"= {coefficient} is not integral, so {element} is not a root"
                )
                images[label] = generator - self.base_ring()(coefficient) * element
            return self.Aut()(images)

        def _sub_form_module(
            self: "LatticeParent",
            gram: "GramMatrix",
            module_generating_set: "OrderedSet",
        ) -> "FormModule":
            r"""Return the lattice on ``gram``: a sublattice of a lattice is one.

            The form restricted to a subobject is still $\mathbb Z$-valued, so
            what it makes is a lattice, refined and decomposed like any other.
            """
            return _lattice_with_gram(gram, module_generating_set)

        # ---- the axioms, on top of the predicates the formed surface owns ----
        #
        # ``dual_module``, ``correlation_morphism``, ``radical`` and
        # ``is_nondegenerate`` live on ``FinitelyGeneratedFreeFormModules``:
        # the axiom gates ask candidates those questions *before* admission,
        # so they cannot be answered from inside this category.
        # :meth:`correlation` below is the correlation morphism with
        # $\operatorname{Hom}(L,\mathbb Z)$ carrying the form that makes it
        # $L^\vee$, which exists only when $c$ is injective.

        def is_unimodular(self: "LatticeParent") -> bool:
            r"""Return whether $c: L\to L^\vee$ is an isomorphism.

            Injective and surjective, which are the two conditions separately:
            $\operatorname{rad}(L)=0$ is $\ker c=0$, and $A_L=\operatorname{coker}c$
            being trivial is the rest.  Unimodular is not "nondegenerate with
            $|\det|=1$" here -- it is $c$ being invertible, and these are the
            kernel and cokernel that say so.
            """
            unimodular: bool = (
                self.is_nondegenerate()
                and self.discriminant_group().cardinality() == 1
            )
            return unimodular

        def correlation_isomorphism(self: "LatticeParent") -> "ModuleMorphism":
            r"""Return \(L\cong L^*\) when the form is unimodular."""
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import Isomorphism
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
            from dzack_research.preamble.utilities import zipsum

            assert self.is_unimodular(), (
                "the correlation is an isomorphism exactly for a unimodular lattice"
            )
            forward = self.correlation_morphism()
            inverse_matrix = self.gram_matrix().inverse()
            backward = module_homset(self.dual_module(), self)(
                {
                    label: zipsum(
                        (self.base_ring()(coefficient) for coefficient in row),
                        self.module_generators(),
                        self.zero(),
                    )
                    for label, row in zip(
                        self.dual_module().module_generating_set(),
                        inverse_matrix.rows(),
                    )
                }
            )
            return Isomorphism(forward, backward)

        # ---- invariants of the form, computed by the realization ----

        def signature_pair(self: "LatticeParent") -> tuple:
            r"""Return $(p,q)$: the positive and negative indices of inertia.

            Sylvester's law over $\mathbb Q$, which is a fact about the form
            and needs nothing else -- in particular not nondegeneracy, so a
            degenerate lattice has one too, with a radical of dimension
            $n-p-q$.
            """
            from sage.quadratic_forms.quadratic_form import QuadraticForm

            positive, negative, _radical = QuadraticForm(
                SageQQ, matrix(SageQQ, self.gram_matrix())
            ).signature_vector()
            return (positive, negative)

        def is_even(self: "LatticeParent") -> bool:
            r"""Return whether $q(x)\in 2\mathbb Z$ for every $x$.

            Checked on the generators, which is all of them:
            $q(\sum a_ie_i)=\sum a_i^2q(e_i)+2\sum_{i<j}a_ia_jb(e_i,e_j)$, and
            the second sum is even whatever the lattice is, so $q$ is even
            exactly when every $q(e_i)$ is.
            """
            return all(generator.q() % 2 == 0 for generator in self.module_generators())

        def genus(self: "LatticeParent") -> "Genus":
            r"""Return the genus: the adelic isometry class of this lattice.

            Two lattices share a genus exactly when they become isometric
            after base change to the adeles, $L_1\otimes\mathbb A\cong
            L_2\otimes\mathbb A$ (FOUNDATIONS Def. 29.2) -- that is the
            definition.  For an *even* lattice the genus is determined by
            the signature pair together with the discriminant quadratic
            form (Nik80, section 1.9, Cor. 1.9.4), and those two data are
            what the returned object holds; everything else it answers is
            delegated to Sage's genus engine behind that boundary.
            """
            assert self.is_nondegenerate(), (
                f"{self} is degenerate, and a genus is the data of a "
                "nondegenerate form at each place. A degenerate form has a "
                "radical, and the question is probably about the quotient by it."
            )
            assert self.is_even(), (
                "the (signature, discriminant quadratic form) parameterization "
                "realizes the genus for even lattices (Nik80 Cor. 1.9.4); the "
                "genus of an odd lattice is a stated gap on this surface"
            )
            return Genus(self.signature_pair(), self.discriminant_group())

        def discriminant(self: "LatticeParent") -> "RingElement":
            r"""Return $d_\pm(b)=(-1)^{n(n-1)/2}\det G$, the signed determinant.

            An invariant of $L$, which is what makes it the discriminant and
            $\det G$ -- the number read off one framing -- the imprecise word
            for it.  A change of framing is by $U\in GL_n(\ZZ)$ and replaces
            $G$ by $UGU^t$, whose determinant is $\det(U)^2\det G=\det G$.

            The sign is not decoration.  $d_\pm$ is the invariant of the Witt
            class -- Lam, *Introduction to Quadratic Forms over Fields*, I.2 --
            and the unsigned determinant is not one: the sign is exactly the
            correction that makes the discriminant of an orthogonal sum
            behave, and it is why $A_2$ has discriminant $-3$ while its Gram
            determinant is $3$.
            """
            gram = matrix(SageZZ, self.gram_matrix())
            rank = gram.nrows()
            discriminant: "RingElement" = (-1) ** (rank * (rank - 1) // 2) * gram.det()
            return discriminant

        def minimum(self: "LatticeParent") -> "RingElement":
            r"""Return $\min\{b(x,x): 0\neq x\in L\}$, the minimal norm.

            A minimum, and therefore a claim that the set has one: $b(x,x)$
            takes arbitrarily negative values as soon as some $b(x,x)<0$, and
            takes the value $0$ on a nonzero vector as soon as $L$ is
            degenerate.  Positive definiteness is what rules both out, so it
            is a hypothesis here and not a preference -- an indefinite lattice
            is not a lattice whose minimum is hard to compute, it is one that
            has none.

            The negative definite case is the same question about $L(-1)$,
            which the caller has :meth:`twist` for; answering it here would
            mean returning the minimum of a different lattice under this
            lattice's name.

            Fincke--Pohst, reached through PARI's ``qfminim``.  An algorithm,
            and a matrix is all it takes.
            """
            positive, negative = self.signature_pair()
            assert negative == 0 and positive + negative == self.rank(), (
                f"{self} is not positive definite, so $b(x,x)$ is unbounded "
                "below or vanishes on a nonzero vector, and the set of its "
                "values on $L\\setminus\\{0\\}$ has no minimum. For a negative "
                "definite lattice ask this of twist(-1)."
            )
            gram = matrix(SageZZ, self.gram_matrix())
            return SageZZ(gram.__pari__().qfminim(None, 0)[1])

        def enumerate_short_vectors(self: "LatticeParent", bound: "RingElement") -> "Set":
            r"""Return $\{x\in L: 0<b(x,x)\le\text{bound}\}$ modulo sign, a finite Set.

            Finite, which is the whole reason the bound is an argument and not
            an option: without one the set is all of $L$, and Sage answers
            with an endless iterator that no caller can hold.  Positive
            definiteness is what makes a bounded set finite -- in an
            indefinite lattice the vectors of norm $0$ alone are infinite --
            so it is the same hypothesis :meth:`minimum` states.

            Modulo sign because $b(-x,-x)=b(x,x)$: the two differ by an
            isometry of $L$, so counting both would count one vector twice.

            Fincke--Pohst, reached through PARI's ``qfminim``.  The vectors
            come back as coordinates against the module generators and are
            made elements of this lattice before they leave, so no caller
            reads a row.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            from dzack_research.preamble.utilities import zipsum
            positive, negative = self.signature_pair()
            assert negative == 0 and positive + negative == self.rank(), (
                f"{self} is not positive definite, so the vectors of norm at "
                "most any bound are infinite in number. For a negative "
                "definite lattice ask this of twist(-1)."
            )
            gram = matrix(SageZZ, self.gram_matrix())
            _count, _largest, coordinates = gram.__pari__().qfminim(bound, None)
            return finite_ordered_set(
                tuple(
                    zipsum(column, self.module_generators(), self.zero())
                    for column in matrix(SageZZ, coordinates).columns()
                )
            )

        # ---- Nikulin / signature predicates ----

        @cached_method
        def dual_lattice(self: "LatticeParent") -> "FormModule":
            r"""Return $L^\vee$: free on the dual generators, Gram $G^{-1}$.

            Named for which dual it is.  A lattice has several -- the dual
            module $\operatorname{Hom}(L,\mathbb Z)$, which carries no form and
            is :meth:`dual_module`; the dual of its discriminant form; the
            Pontryagin dual of its underlying group -- and a bare ``dual``
            names none of them.

            An object, and not a set of vectors: Sage's method of this name
            returns $\{x\in L\otimes\mathbb Q:\langle x,L\rangle\subseteq
            \mathbb Z\}$, which makes the correlation look like an inclusion
            and the form look like a property of the common realization in
            $L\otimes\mathbb Q$.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
            from dzack_research.preamble.categories.forms.forms import BilinearForm
            assert self.is_nondegenerate(), (
                f"{self} is degenerate, so it has no $L^\\vee$: the form on the "
                "dual is $G^{-1}$, and $c$ is not injective here. The dual as a "
                "module is dual_module(), which always exists, and the "
                "obstruction is radical()."
            )
            gram = self.gram_matrix().inverse()
            return BilinearForm(
                BasedFreeModule(ℤ, self.module_generating_set()),
                SageQQ,
                gram,
            )

        @cached_method
        def correlation(self: "LatticeParent") -> "FormMorphism":
            r"""Return $c: L\to L^\vee$, $v\mapsto\langle v,-\rangle$, matrix $G$.

            Nondegeneracy is injectivity of $c$, unimodularity is $c$ being an
            isomorphism, and $A_L=\operatorname{coker} c$.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import correlation_of
            # Cached because $L^\vee$ is an object, not a value: two calls have
            # to return the same one or its elements would have different
            # parents and nothing could be composed with $c$.
            return correlation_of(self)

        def discriminant_bilinear_form(self: "LatticeParent") -> "FormModule":
            r"""Return $(A_L, b)$ with $b: A_L\times A_L\to\mathbb Q/\mathbb Z$.

            The always-defined discriminant form: $b$ needs nothing of $L$
            beyond nondegeneracy, whereas $q$ needs $L$ even.  It is the
            cokernel of :meth:`correlation`.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.discriminant_bilinear_modules import DiscriminantBilinearModules
            return DiscriminantBilinearModules().cokernel(self.correlation())

        def discriminant_quadratic_form(self: "LatticeParent") -> "QuadraticFormMorphism":
            r"""Return $(A_L, q)$ with $q: A_L\to\mathbb Q/2\mathbb Z$.

            Gated on evenness: moving a lift by $\ell\in L$ shifts
            $b(\tilde x,\tilde x)$ by $b(\ell,\ell)$, which lies in
            $2\mathbb Z$ exactly when $L$ is even.  For an odd $L$ there is no
            such $q$, and :meth:`discriminant_bilinear_form` is all there is.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.discriminant_quadratic_modules import DiscriminantQuadraticModules
            return DiscriminantQuadraticModules().cokernel(self.correlation())

        def discriminant_group(
            self: "LatticeParent", s: "Element" = 0, *, reduce_trivial: bool = False
        ) -> "FormModule":
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

            * ``self.module_generators()`` are the basis vectors $e_i$ of $L$.
            * :meth:`dual_lattice_module_generators` are the $e_i^\vee$ of $L^\vee$.
            * :meth:`dual_embedding` is $c$ itself, whose matrix is $G$ -- in
              the $e_i^\vee$ basis it is generally not the identity; for
              $A_1(-1)^n$ it is $2I$.

            A displayed row in the catalogue is therefore turned into an element
            of $L^\vee$ with :meth:`correlation` first, and only then
            projected.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.discriminant_bilinear_modules import DiscriminantBilinearModules
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.discriminant_quadratic_modules import DiscriminantQuadraticModules
            cache = f"_preamble_discriminant_group_{bool(reduce_trivial)}"
            cached = self.__dict__.get(cache)
            if s == 0 and cached is not None:
                return cached

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
                    generator for generator in form.module_generators() if generator.order() != 1
                ]
                form = form.regenerate(surviving)
            if s != 0:
                return form.primary_part(s)
            setattr(self, cache, form)
            return form

        def is_coeven(self: "LatticeParent") -> bool:
            r"""Return whether the discriminant form is integer-valued ($\delta=0$)."""
            disc = self.discriminant_group()
            assert disc.cardinality() < Sets.ℵ[0], (
                "discriminant quadratic module is infinite; the lattice must be nondegenerate"
            )
            # $q$ takes values in $\mathbb Q/2\mathbb Z$, and a class there has
            # no denominator -- integrality is a question about a
            # representative, so the lift is what answers it.
            return all(element.q().lift().denominator() == 1 for element in disc)

        def is_coodd(self: "LatticeParent") -> bool:
            """Return the negation of :meth:`is_coeven`."""
            return not self.is_coeven()

        def delta(self: "LatticeParent") -> Integer:
            r"""Return Nikulin's invariant $\delta\in\{0,1\}$."""
            return Integer(0) if self.is_coeven() else Integer(1)

        def is_p_elementary(self: "LatticeParent", p: "Integer") -> bool:
            r"""Return whether the discriminant quadratic module $A_L$ is elementary
            abelian of exponent $p$.

            Defers to :meth:`DiscriminantQuadraticModules.ParentMethods.is_p_elementary`
            on ``self.discriminant_group()``.
            """
            disc = self.discriminant_group()
            return bool(disc.is_p_elementary(p))

        def is_elliptic(self: "LatticeParent") -> bool:
            """Return whether the lattice is negative definite."""
            return bool((-self.gram_matrix()).is_positive_definite())

        def is_parabolic(self: "LatticeParent") -> bool:
            """Return whether the lattice is negative semidefinite."""
            return bool((-self.gram_matrix()).is_positive_semidefinite())

        # ---- naming and display ----

        def with_names(self: "LatticeParent", spec: str) -> "Module":
            r"""Attach basis names from a compact spec and return the lattice.

            EXAMPLES::

                sage: from dzack_research.preamble import catalogue
                sage: Lattices.E8.with_names("a1..a8").variable_names()
                ('a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8')
            """
            self._assign_names(_expand_names(spec, self.rank()))
            return self

        def to_lin_comb_module_generators(self: "LatticeParent", element: "Element") -> str:
            r"""Return an element as a linear combination of the named basis."""
            names = self.variable_names()
            coefficients = element.coefficients()

            def term(name: str, coefficient: "RingElement") -> str | None:
                if coefficient == 0:
                    return None
                if coefficient == 1:
                    return name
                if coefficient == -1:
                    return f"-{name}"
                return f"{coefficient}*{name}"

            terms = tuple(
                rendered
                for name, generator in zip(names, self.module_generating_set(), strict=True)
                for coefficient in (coefficients.get(generator, 0),)
                if (rendered := term(name, coefficient)) is not None
            )
            match terms:
                case ():
                    return "0"
                case (_, *_):
                    return " + ".join(terms).replace("+ -", "- ")
                case _:
                    assert False, "a tuple is empty or it is not"

        @property
        def sublattices(self: "LatticeParent") -> dict:
            r"""Return the per-instance dictionary of named sublattices."""
            existing = self.__dict__.get("_sublattices")
            if existing is None:
                existing = {}
                self._sublattices = existing
            return existing

        # ---- orthogonal direct sum / twist ----

        def direct_sum(
            self: "LatticeParent",
            summands: "OrderedSet",
            names: "OrderedSet" = None,
        ) -> "FormModule":
            r"""Construct an orthogonal direct sum with its ordered subobjects.

            A direct sum is indexed by a family, so the summands arrive as
            one ordered family rather than as separate arguments.

            Orthogonal means the Gram matrix is block diagonal in the
            generators of the summands laid end to end, which is the whole
            construction: the sum is the lattice on that matrix, and its
            decomposition is found the way every lattice's is.
            """
            def orthogonal_sum(left: "Element", right: "Element") -> "FormModule":
                expected = (
                    _gram_component_ranks(left.gram_matrix())
                    + _gram_component_ranks(right.gram_matrix())
                )
                module_generating_set = _direct_sum_framing_set(left, right)
                result = _lattice_with_gram(
                    block_diagonal_matrix(
                        [matrix(SageZZ, left.gram_matrix()), matrix(SageZZ, right.gram_matrix())]
                    ),
                    module_generating_set,
                )
                # The summed Gram is block diagonal across the operands, so
                # the sum's components are the two lists concatenated --
                # nothing to search for, only to check.  Checked on the
                # matrix, which is where block structure lives: asking the
                # lattice would decompose it, and decomposing builds each
                # block as a lattice that decomposes in turn, so a check of
                # what is already known cost thousands of constructions.
                assert _gram_component_ranks(result.gram_matrix()) == expected, (
                    "direct sum disagrees with its summands: "
                    f"{_gram_component_ranks(result.gram_matrix())} != {expected}"
                )
                # The sum draws its own block lines.  They used to appear as a
                # side effect of the decomposition search, which now waits to be
                # asked -- but a direct sum knows where its blocks end without
                # searching, so it says so here.
                boundaries = []
                position = 0
                for size in expected[:-1]:
                    position += size
                    boundaries.append(position)
                if boundaries:
                    _subdivide_gram(result, boundaries, boundaries)
                return result

            result = reduce(orthogonal_sum, tuple(summands), self)
            return _apply_optional_names(result, names)

        def twist(self: "LatticeParent", scale: "RingElement", names: "OrderedSet" = None) -> "Module":
            r"""Return $L(n)$: the same module with the form scaled by ``scale``.

            Scaling the Gram leaves the generators and their orthogonality
            alone, so the twist splits exactly where ``self`` does; its own
            construction finds that, and each summand comes back twisted.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.forms.forms import BilinearForm
            result = BilinearForm(
                self.forget_form(),
                ℤ,
                scale * matrix(SageZZ, self.gram_matrix()),
            )
            assert _summand_ranks(result) == _summand_ranks(self), (
                "twisting changed the decomposition: "
                f"{_summand_ranks(result)} != {_summand_ranks(self)}"
            )
            return _apply_optional_names(result, names)

        # ---- morphisms / automorphisms ----

        def Hom(
            self: "LatticeParent",
            codomain: "Module",
            category: "Category | None" = None,
        ) -> "Homset":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModules
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.lattice_homomorphisms import lattice_homset
            if codomain in FormModules(self.base_ring()):
                homset: "Homset" = lattice_homset(self, codomain)
                return homset
            plain_homset: "Homset" = Parent.Hom(self, codomain, category)
            return plain_homset

        def End(self: "LatticeParent") -> "Homset":
            r"""Return $\mathrm{End}(L)=\mathrm{Hom}(L,L)$.

            The endset, which is where $O(L)$ comes from: an isometry of $L$
            is an invertible endomorphism, so the group is the units of this
            monoid.  Sited here and not built here -- an endset is the homset
            whose two objects coincide, and asking for it any other way would
            produce a second object with the same elements.
            """
            endset: "Homset" = self.Hom(self)
            return endset

        def Aut(self: "LatticeParent") -> "FormAutomorphismGroup":
            r"""Return $\mathrm{Aut}(L)=O(L)$, the units of $\mathrm{End}(L)$.

            One object, reached one way.  ``orthogonal_group`` and
            ``automorphisms`` are this method under other names: the
            automorphisms of a lattice *are* its isometries, so two accessors
            answering with two objects would say there are two groups.

            Elements are constructed by their images on the framing labels.

            The placement is the point.  $O(L)$ is a group, so it goes in the
            isometry node -- which is a group node -- and the words a group
            answers follow from that rather than from anything written here.
            Finitely *presented* is claimed outright, indefinite $L$ included:
            $O(L)$ is an arithmetic group (Borel--Harish-Chandra), and
            Borel--Serre / Raghunathan prove every arithmetic group is
            finitely presented, whether or not this session can produce a
            presentation.  The axiom is claimed on this object
            and not on the isometry category, because that category holds the
            subgroups too, and a finitely generated subgroup of a finitely
            presented group need not be finitely presented.  Finiteness is not
            claimed, because it is false for most indefinite $L$ and expensive
            to decide; it is a question the group answers when asked.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormAutomorphismGroup
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.lattice_homomorphisms import LatticeHomomorphisms
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.lattice_isometries import LatticeIsometries
            from dzack_research.preamble.categories.group.groups import OwnedFinitelyPresentedGroups
            from dzack_research.preamble.refine import refine
            cached = self.__dict__.get("_preamble_Aut")
            if cached is not None:
                return cached
            # An automorphism group is the endomorphism homset with one more
            # condition on its elements, so it is built the same way and
            # refined once more.
            refined = refine(
                FormAutomorphismGroup(self),
                [
                    LatticeHomomorphisms(),
                    LatticeIsometries(),
                    OwnedFinitelyPresentedGroups(),
                ],
            )
            self._preamble_Aut = refined
            return refined

        orthogonal_group = Aut
        automorphisms = Aut

        def discriminant_representation(self: "LatticeParent") -> "Morphism":
            r"""Return $\rho_L: O(L)\to O(A_L)$, the discriminant representation.

            Obtained by applying the discriminant functor to automorphisms
            (FOUNDATIONS Defs 26.1/26.3; Nik80 §§3°–4°, Zotero TTY9FFJS): the
            value on an isometry is its
            :meth:`~LatticeIsometries.MorphismMethods.discriminant_morphism`.
            For an even $L$ the codomain is $O(A_L, q_L)$; for an odd one it
            is $O(A_L, b_L)$, which is which form $A_L$ carries.  That $\rho_L$
            is a homomorphism is the functoriality of $\operatorname{Disc}$
            -- a theorem, carried, not re-proved at runtime.  No surjectivity
            is assumed.
            """
            from sage.categories.groups import Groups as SageGroups
            return SetMorphism(
                Hom(
                    self.Aut(),
                    self.discriminant_group().automorphism_group(),
                    SageGroups(),
                ),
                lambda isometry: isometry.discriminant_morphism(),
            )

        def stable_orthogonal_group(self: "LatticeParent") -> "Group":
            r"""Return $\tilde O(L):=\ker(\rho_L)$, the stable orthogonal group.

            The kernel of the discriminant representation (Nik80 §§3°–4°,
            Zotero TTY9FFJS): the isometries acting trivially on $A_L$.
            Computed by listing $O(L)$, which a finite group admits; for an
            infinite $O(L)$ no generating set of the kernel is in hand, and
            the absence is stated rather than approximated.
            """
            isometries = self.Aut()
            assert isometries.is_finite(), (
                f"O({self}) is infinite; no generating set of the kernel of "
                "rho is in hand.  Name a subgroup by generators and ask "
                "whether each acts trivially on the discriminant form."
            )
            identity = self.discriminant_group().automorphism_group().one()
            kernel_generators = tuple(
                isometry
                for isometry in isometries
                if isometry.discriminant_morphism() == identity
            )
            return isometries.subgroup_on(kernel_generators)

        def with_action(self: "LatticeParent", action: "GroupAction") -> "Module":
            r"""Return $L$ carrying the already-constructed $\rho:G\to O(L)$.

            $\rho$ is received, not assembled.  A caller who wants $L$ to be a
            $G$-lattice constructs $G$, constructs $O(L)=$ ``self.Aut()``, and
            constructs $\rho$ in $\operatorname{Hom}(G,O(L))$ -- the homset
            ``group_action_homset(G, self)``, whose element constructor takes
            the images of $G$'s generators and holds them to $G$'s relations.
            Naming a homomorphism of groups is the business of the category of
            groups; this method only equips $L$ with one.

            $G$ is a group in its own right -- $\langle f_i\mid f_i^{n_i}\rangle$
            formed from automorphisms of a surface, a cyclic group whose
            generator is sent to any isometry of that order, anything.  It is
            read off $\rho$ and is not the image of $\rho$: $\rho$ may have a
            kernel, and then $\rho(G)$ is a proper quotient of $G$ whose
            character theory is a different one.

            The other way to name a representation is to take a literal
            subgroup of $O(L)$ and its own inclusion -- ``G.inclusion()``,
            asked of the group, since $G$'s elements decide that $\rho$ by
            themselves.  It ends here too.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import GroupAction
            from dzack_research.preamble.categories.modules.group_modules.group_lattices import group_lattice
            assert isinstance(action, GroupAction) and action.codomain() is self.Aut(), (
                "the action must be an already-constructed homomorphism into O(L) "
                "for this L; construct it in Hom(G, self.Aut())"
            )
            return group_lattice(self, action)

        def invariant_lattice(self: "LatticeParent", action: "GroupAction") -> "Subobject":
            r"""Return $L^G\hookrightarrow L$ for the representation $\rho$.

            The trivial isotypic component of the $\mathbb Z[G]$-module, with
            the form restricted to it -- see
            :meth:`GroupLattices.ParentMethods.invariant_lattice`.  Not
            $\ker(g-\mathrm{id})$: that is one way to compute this component,
            and computing it that way here would state the method as the
            definition.

            $L^G$ is a statement about $\rho:G\to O(L)$ and about nothing else,
            so $\rho$ is what this asks for.  A caller holding one isometry
            names $G=\langle f\rangle$ and $\rho=$ ``G.inclusion()`` first;
            how $\rho$ was obtained is not this method's business.
            """
            return self.with_action(action).invariant_lattice()

        def coinvariant_lattice(self: "LatticeParent", action: "GroupAction") -> "Subobject":
            r"""Return the formed coinvariants $(L^G)^{\perp L}\hookrightarrow L$."""
            return self.formed_coinvariants(action)

        def formed_coinvariants(self: "LatticeParent", action: "GroupAction") -> "Subobject":
            r"""Return $(L^G)^{\perp L}\hookrightarrow L$ for the representation $\rho$."""
            return self.with_action(action).formed_coinvariants()

        def _induced_lattice(self: "LatticeParent", coordinate_basis: "MorphismMatrix") -> "FormModule":
            """Return the integral lattice with Gram form induced on ``coordinate_basis``."""
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            from dzack_research.preamble.utilities import zipsum
            basis = list(coordinate_basis)
            if not basis:
                return None
            gram = self.gram_matrix()
            induced = matrix(
                SageZZ,
                [[u * gram * v for v in basis] for u in basis],
            )
            assert induced.is_symmetric(), (
                "induced form on the sublattice is not symmetric"
            )
            dual_generators = tuple(self.module_generators())
            generators = tuple(
                zipsum(
            row,
            dual_generators,
            self.zero(),
        )
                for row in basis
            )
            return _lattice_with_gram(
                induced,
                finite_ordered_set(generators),
            )

        # ---- constructor sugar ----

        def _first_ngens(self: "LatticeParent", count: int) -> "OrderedSet":
            r"""Return generators matching the declared name slots."""
            # The enumeration of the generating set: a slot is a position in
            # the declared names, and positions are read off the order, not
            # off the set.
            module_generators = tuple(self.module_generators())
            spec = self.__dict__.get("_ellipsis_spec")
            if spec is None or len(spec) != count:
                return module_generators[:count]
            names = list(self.variable_names())
            return tuple(
                Ellipsis if slot == "Ellipsis" else module_generators[names.index(slot)]
                for slot in spec
            )

        def __add__(
            self: "LatticeParent",
            other: "ElementConstructorInput",
        ) -> "FormModule":
            r"""``L + M`` as the orthogonal direct sum (for ``sum([...])``)."""
            return self.direct_sum([other])

        def __radd__(
            self: "LatticeParent",
            other: "ElementConstructorInput",
        ) -> "FormModule":
            """Allow ``sum([L, M, ...])`` (Python starts from ``0``)."""
            if other == 0:
                return self
            return NotImplemented

        def __matmul__(self: "LatticeParent", other: "FormModule") -> "FormModule":
            r"""``L @ M`` as the tensor product lattice \(L\otimes_{\mathbb Z}M\).

            The form is determined by what a form on a tensor product *is*:
            \(b(x_1\otimes y_1,\,x_2\otimes y_2)=b_L(x_1,x_2)\,b_M(y_1,y_2)\)
            on pure tensors, extended bilinearly.  Read on generators laid out
            in pairs, that is exactly the Kronecker product of the two Gram
            matrices, so no separate definition of the form is needed.

            Unlike ``+``, this is not a biproduct: there are no projections
            \(L\otimes M\to L\) and no inclusions \(L\to L\otimes M\).
            It is a cocone under the *cartesian product* \(L\times M\), whose
            structure map is the bilinear \(\otimes\); see
            ``TensorProductCategory``.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            from dzack_research.preamble.refine import refine
            gram = matrix(SageZZ, self.gram_matrix()).tensor_product(
                matrix(SageZZ, other.gram_matrix())
            )
            labels = finite_ordered_set(
                [
                    (left_label, right_label)
                    for left_label in self.module_generating_set()
                    for right_label in other.module_generating_set()
                ]
            )
            result = _lattice_with_gram(gram, labels)
            refine(result, result.category().TensorProduct((self, other)))
            # The cocone's structure map: the universal bilinear map out of
            # L x M. It is bilinear, so it is a set morphism, not a module one.
            source = result.cartesian_source()
            result._costructure_morphisms = (
                SetMorphism(
                    Hom(source, UnderlyingSet(result), Sets()),
                    lambda pair: result._pure_tensor(*pair),
                ),
            )
            return result

        def _pure_tensor(self: "LatticeParent", left: "ModuleElement", right: "ModuleElement") -> "ModuleElement":
            r"""Return \(x\otimes y\) in the generators laid out in pairs."""
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.utilities import zipsum
            return zipsum(
                [
                    a * b
                    for a in left._coordinates()
                    for b in right._coordinates()
                ],
                self.module_generators(),
                self.zero(),
            )

        def __pow__(self: "LatticeParent", exponent: "Integer", names: "OrderedSet" = None) -> "Element":
            r"""``L ^ n`` as the ``n``-fold orthogonal direct sum."""
            n = int(exponent)
            assert n >= 1, f"lattice power needs a positive exponent, got {exponent}"
            return self.direct_sum(
                [self] * (n - 1),
                names=names,
            )

        def _repr_(self: "LatticeParent") -> str:
            pos, neg = self.signature_pair()
            return (
                f"Integral lattice of rank {self.rank()} and signature "
                f"({pos}, {neg})"
            )

        # ---- LaTeX ----

        def _latex_(self: "LatticeParent") -> str:
            r"""Multi-line LaTeX with rank, signature, discriminant, Gram, discriminant module."""
            rank = self.rank()
            pos, neg = self.signature_pair()
            # One word, one number: the displayed discriminant is
            # :meth:`discriminant`, the signed determinant, never bare
            # $\det G$ under the same name.
            disc = self.discriminant()
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
            if decomposition is None and not self.is_decomposable():
                decomposition = _summand_name(self)
            if decomposition is not None:
                header.append(f"L = {decomposition} \\\\")

            header.append(f"G_L = {gram_latex} \\\\")
            return "\n".join(header + A_lines + [r"\end{gathered}"])

    class ElementMethods:
        r"""What a lattice vector adds to being an element of a form module.

        The pairing, the norm and $v*w$ are :class:`FormModules`', because they
        are what having a form means.  What is here is the vocabulary a lattice
        vector is asked in -- $q$ for the norm, divisibility, primitivity -- and
        the constructions that need $L$ to be integral.
        """

        def q(self: "LatticeElement") -> "Element":
            r"""Return $q(v) = \langle v, v\rangle$: the norm, under its name here."""
            return self.norm()

        def div(self: "LatticeElement") -> "Integer":
            r"""Return the divisibility of this vector."""
            divisibility: "Integer" = self.parent().div(self)
            return divisibility

        def primitive_dual(self: "LatticeElement") -> "ModuleElement":
            r"""Return the primitive dual lift ``v / div(v)`` in ``L^\\vee``."""
            if self.is_zero():
                return self.parent().correlation()(self)
            divisibility = self.div()
            assert divisibility > 0, f"nonzero element has nonnegative divisibility, got {divisibility}"
            return self.parent().correlation()(self) / divisibility

        def primitive_dual_in_discriminant_bilinear_form(self: "LatticeElement") -> "Element":
            r"""Return the class of $v/\operatorname{div}(v)$ in the discriminant bilinear form $A_L$."""
            return self.parent().project_to_discriminant_bilinear_form(
                self.primitive_dual()
            )

        def primitive_dual_in_discriminant_quadratic_form(self: "LatticeElement") -> "Element":
            r"""Return the class of $v/\operatorname{div}(v)$ in the discriminant quadratic form $A_L$.

            Defined only for even lattices.
            """
            return self.parent().project_to_discriminant_quadratic_form(
                self.primitive_dual()
            )

        def is_primitive(self: "LatticeElement") -> bool:
            r"""Return whether $\mathbb Zv\hookrightarrow L$ is primitive.

            Primitivity is a property of the embedding, and its definition is
            that the cokernel is torsion free.  That is what is computed.

            It is deliberately not computed as "the coordinates of $v$ have
            trivial gcd".  That equivalence is a theorem about $\mathbb Z$
            read in a chosen generating set; writing it here would assert the
            theorem over every base ring at once, silently, in a method whose
            signature promises nothing of the kind.  Torsion freeness of the
            cokernel is also not the same as freeness over a general $R$.
            """
            primitive: bool = self.parent().subobject_on([self]).is_primitive()
            return primitive

        def __pow__(
            self: "LatticeElement",
            exponent: "Integer",
            mod: "Integer | None" = None,
        ) -> "Element":
            r"""``v ^ 2`` -> $q(v)$."""
            assert exponent == 2, f"exponent {exponent} not supported"
            return self.q()

        def e_perp_mod_e(self: "LatticeElement") -> "Module":
            r"""$e^\perp/\langle e\rangle$, which is this element's isotropic reduction."""
            return self.isotropic_reduction()


# ---- helper utilities ----


setattr(FinitelyGeneratedLattices, "Integral", FinitelyGeneratedIntegralLattices)
setattr(FinitelyGeneratedIntegralLattices, "Nondegenerate", IntegralLattices)

_ZERO_DOTS: bool = True

def set_zero_dots(enabled: bool = True) -> None:
    r"""Toggle replacing 0 entries with $\cdot$ in lattice LaTeX."""
    global _ZERO_DOTS
    _ZERO_DOTS = bool(enabled)

def _zero_dots() -> bool:
    return _ZERO_DOTS

def _lattice_with_gram(
    gram: "GramMatrix",
    module_generating_set: "OrderedSet" = None,
) -> "FormModule":
    r"""Return the integral lattice on ``gram``, refined and decomposed.

    The one construction: a Gram matrix becomes a form on $\mathbb Z^n$, the
    form becomes the lattice, and the lattice finds its own decomposition.
    Everything that produces a lattice from a matrix -- a direct sum, a twist,
    an induced form on a sublattice, a quotient, an overlattice -- comes
    through here, so there is one place where a lattice is born.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
    from dzack_research.preamble.categories.forms.forms import BilinearForm
    from dzack_research.preamble.categories.sets.sets import finite_ordered_set
    gram = GramMatrix(matrix(SageZZ, gram))
    assert gram.is_symmetric(), (
        "a bilinear form on a lattice is symmetric; this Gram matrix is not"
    )
    gram.set_immutable()
    match module_generating_set:
        case None:
            module_generating_set = Sets.Δ[gram.nrows() - 1]
        case Parent() | Iterable():
            module_generating_set = finite_ordered_set(module_generating_set)
            assert module_generating_set.cardinality() == gram.nrows(), (
                "the framing set and Gram matrix have different cardinalities"
            )
        case _:
            assert False, (
                "a lattice generating set is a finite set or finite iterable"
            )
    lattice = BilinearForm(
        BasedFreeModule(
            ℤ,
            module_generating_set,
        ),
        ℤ,
        gram,
    )
    return lattice


class Genus:
    r"""The genus of an even nondegenerate integral lattice.

    Two lattices share a genus exactly when they become isometric after
    base change to the adeles, $L_1\otimes\mathbb A\cong L_2\otimes\mathbb A$
    (FOUNDATIONS Def. 29.2) -- the definition.  For even lattices the genus
    is determined placewise by the signature pair together with the
    discriminant quadratic form (Nik80, section 1.9, Cor. 1.9.4), and that
    pair of data is what this object holds.  Representatives, class
    numbers, and the local symbols are delegated to Sage's genus engine,
    rebuilt from this object's own data behind the boundary.
    """

    def __init__(
        self,
        signature_pair: tuple,
        discriminant_quadratic_form: "FormModule",
    ) -> None:
        self._signature_pair = (
            SageZZ(signature_pair[0]),
            SageZZ(signature_pair[1]),
        )
        self._discriminant_quadratic_form = discriminant_quadratic_form

    def signature_pair(self) -> tuple:
        r"""Return $(p, q)$, the archimedean datum of the genus."""
        return self._signature_pair

    def discriminant_form(self) -> "FormModule":
        r"""Return $(A_L, q)$, the finite datum of the genus."""
        return self._discriminant_quadratic_form

    def _engine(self) -> "GenusSymbol_global_ring":
        r"""Return Sage's genus symbol, rebuilt from this genus's own data.

        The one boundary crossing: the discriminant quadratic form is
        written out on its generators ($q$ lifted from $\mathbb Q/2\mathbb Z$
        on the diagonal, $b$ lifted from $\mathbb Q/\mathbb Z$ off it), and
        Sage's torsion-module constructor reconstructs the local symbols
        from it and the signature.
        """
        from sage.modules.torsion_quadratic_module import TorsionQuadraticForm

        form = self._discriminant_quadratic_form
        generators = tuple(form.module_generators())
        if not generators:
            # Unimodular: the empty discriminant form, whose genus symbol
            # Sage builds from any representative Gram matrix -- here the
            # even unimodular one of this signature does not need finding,
            # because the empty torsion form constructor handles it.
            engine_form = TorsionQuadraticForm(matrix(SageQQ, 0, 0))
            return engine_form.genus(self._signature_pair)
        written = matrix(
            SageQQ,
            [
                [
                    left.q().lift() if i == j else left.b(right).lift()
                    for j, right in enumerate(generators)
                ]
                for i, left in enumerate(generators)
            ],
        )
        engine_form = TorsionQuadraticForm(written)
        assert engine_form.cardinality() == form.cardinality(), (
            "the engine torsion module must carry the whole discriminant "
            f"group: {engine_form.cardinality()} != {form.cardinality()}"
        )
        return engine_form.genus(self._signature_pair)

    def determinant(self) -> "RingElement":
        r"""Return the determinant of any lattice in the genus."""
        return SageZZ(self._engine().determinant())

    def local_symbol(self, prime: "RingElement") -> "Genus_Symbol_p_adic_ring":
        r"""Return the $p$-adic symbol at ``prime`` (Conway--Sloane)."""
        return self._engine().local_symbol(SageZZ(prime))

    def excess(self, prime: "RingElement") -> "RingElement":
        r"""Return the $p$-excess at ``prime`` (CS10 ch. 15 sec. 7.5; the
        oddity at $p=2$)."""
        return self.local_symbol(prime).excess()

    def level(self, prime: "RingElement") -> "RingElement":
        r"""Return the level of the $p$-adic symbol at ``prime``."""
        return SageZZ(self.local_symbol(prime).level())

    def representative(self) -> "FormModule":
        r"""Return one lattice in this genus, from Sage's genus engine."""
        return _lattice_with_gram(matrix(SageZZ, self._engine().representative()))

    def class_number(self) -> "RingElement":
        r"""Return $h$, the number of isometry classes in the genus."""
        return SageZZ(len(self._engine().representatives()))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Genus):
            return NotImplemented
        if self._signature_pair != other._signature_pair:
            return False
        return bool(self._engine() == other._engine())

    def __ne__(self, other: object) -> bool:
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __hash__(self) -> int:
        return hash(
            (self._signature_pair, self._discriminant_quadratic_form.invariants())
        )

    def __repr__(self) -> str:
        return (
            f"Genus of even lattices with signature {self._signature_pair} and "
            f"discriminant group invariants "
            f"{self._discriminant_quadratic_form.invariants()}"
        )


def _direct_sum_framing_set(left: "Element", right: "Element") -> "OrderedSet":
    r"""Return the ordered coproduct of two finite framing sets."""
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.sets.sets import finite_ordered_set
    labels = tuple(
        (0, label) for label in left.module_generating_set()
    ) + tuple(
        (1, label) for label in right.module_generating_set()
    )
    return finite_ordered_set(labels)

def _discriminant_lift_row(
    element: "Element",
    rank: int,
) -> list["RingElement"]:
    r"""Return a representative of a discriminant class, in $L$'s framing.

    The target is quadratic for even lattices and bilinear otherwise.

    Two framings meet here and the row has to leave in the caller's.  A lift
    is an element of $L^\vee$ and answers with its coefficients on the dual
    generators; ``glue`` stacks the row on $L$'s own generators, where the
    lift is a rational combination.  The two are related by $G^{-1}$, since
    $e_i^\vee$ is the solution of $b(e_i^\vee,e_j)=\delta_{ij}$ -- which is
    the Gram matrix $L^\vee$ carries, so the dual's own form is the change of
    framing and nothing has to invert anything to find it.

    Without the change, a class whose lift has integral dual coordinates --
    every class of an $A_1^n$, for one -- reads as a vector of $L$, and
    ``glue`` returns $L$ back for an honest gluing datum.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModuleElement
    assert isinstance(element, FormModuleElement), (
        f"glue is defined on classes in A_L, and this is {element!r}. Build an "
        "element of L^\\vee with correlation(), then project it with "
        "project_to_discriminant_bilinear_form(...); a coordinate vector is not a "
        "discriminant class until someone says which combination of generators "
        "it names."
    )
    lift = element.parent().projection().lift(element)
    dual = lift.parent()
    coefficients = lift.coefficients()
    basis = tuple(dual.module_generating_set())
    dual_coordinates = vector(
        SageQQ,
        [coefficients.get(generator, 0) for generator in basis],
    )
    row = list(dual_coordinates * dual.gram_matrix())
    assert len(row) == rank, (
        f"discriminant element lift has rank {len(row)}, expected {rank}"
    )
    return row

def _expand_names(spec: str, rank: int) -> tuple[str, ...]:
    r"""Expand indexed ranges in a basis-name specification."""
    def expand(piece: str) -> tuple[str, ...]:
        assert piece, f"empty name in spec {spec!r}"
        match re.fullmatch(r"([A-Za-z_]+)(\d+)\.\.\1?(\d+)", piece):
            case re.Match() as indexed:
                stem = indexed.group(1r)
                start = int(indexed.group(2r))
                stop = int(indexed.group(3r))
                return tuple(f"{stem}{i}" for i in range(start, stop + 1))
            case None:
                assert re.fullmatch(r"[A-Za-z_]\w*", piece), (
                    f"invalid name: {piece!r}"
                )
                return (piece,)

    names = tuple(
        name
        for piece in (part.strip() for part in spec.split(","))
        for name in expand(piece)
    )
    assert len(names) == rank, (
        f"spec {spec!r} gives {len(names)} names but rank is {rank}"
    )
    assert len(set(names)) == rank, f"duplicate names in {spec!r}"
    return names

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
        assert left.group(1r) == right.group(1r) and left.group(3r) == right.group(3r), (
            f"'...' between different stems: {before} and {after}"
        )
        start, stop = int(left.group(2r)), int(right.group(2r))
        assert stop > start, f"'...' range does not ascend: {before}..{after}"
        stem, suffix = left.group(1r), left.group(3r)
        expanded.extend(f"{stem}{i}{suffix}" for i in range(start + 1, stop))
    return tuple(expanded)

def _apply_names(lattice: "FormModule", names: "OrderedSet") -> "FormModule":
    r"""Expand a declared name tuple onto a lattice, checking rank."""
    declared = tuple(names)
    expanded = _expand_ellipsis_names(declared)
    assert len(expanded) == lattice.rank(), (
        f"{declared} expands to {len(expanded)} names but rank is {lattice.rank()}"
    )
    lattice._assign_names(expanded)
    lattice._ellipsis_spec = declared
    return lattice


def _apply_optional_names(lattice: "FormModule", names: "OrderedSet") -> "FormModule":
    r"""Apply an explicitly supplied finite name family."""
    match names:
        case None:
            return lattice
        case list() | tuple():
            return _apply_names(lattice, names)
        case _:
            assert False, "lattice names are supplied as a finite tuple or list"

def _subdivide_gram(L: "FormModule", *cuts: list["Integer"]) -> None:
    r"""Subdivide a lattice's Gram matrix, handling immutability."""
    form = L.form()
    gram = form.gram_matrix()
    if gram.is_immutable():
        from copy import copy

        gram = copy(gram)
        form._gram_matrix = gram
    gram.subdivide(*cuts)

def _decompose_lattice(L: "FormModule") -> "DirectSumObject":
    r"""Split \(L\) along its generators and record the summands.

    Decomposability here is a property of the chosen generating set: \(L\)
    *equals* a direct sum exactly when its Gram matrix is block diagonal in the
    generators it was built with.  A splitting that would need the generators
    permuted is a different object, and
    :func:`_matrix_connected_component_cuts` declines it.

    The direct-sum structure is a separate object.  It is not grafted onto
    \(L\), so another decomposition may coexist with this one.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.direct_sum_objects import DirectSumDecomposition
    from dzack_research.preamble.categories.forms.gram_matrices import _matrix_connected_component_cuts
    from dzack_research.preamble.categories.sets.sets import finite_ordered_set
    gram = L.gram_matrix()
    cuts = _matrix_connected_component_cuts(gram)
    if not cuts:
        return None

    bounds = list(zip([0] + cuts, cuts + [gram.nrows()]))
    labels = tuple(L.module_generating_set())
    blocks = [
        _lattice_with_gram(
            gram.submatrix(start, start, end - start, end - start),
            finite_ordered_set(labels[start:end]),
        )
        for start, end in bounds
    ]

    _subdivide_gram(L, cuts, cuts)
    generators = tuple(L.module_generators())
    summands = tuple(
        Subobject(block.Hom(L)(generators[start:end]))
        for block, (start, end) in zip(blocks, bounds)
    )
    return DirectSumDecomposition(L, summands)


def _gram_component_ranks(gram: "GramMatrix") -> tuple:
    r"""Return the sizes of the Gram matrix's connected blocks.

    The block structure of a lattice is a property of its Gram matrix in the
    generators it was built with, so it is read off the matrix.  Reading it
    off the lattice instead means constructing every block as a lattice.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.forms.gram_matrices import _matrix_connected_component_cuts

    cuts = _matrix_connected_component_cuts(gram)
    if not cuts:
        return (gram.nrows(),)
    return tuple(end - start for start, end in zip([0] + cuts, cuts + [gram.nrows()]))


def _summand_ranks(L: "FormModule") -> tuple[Integer, ...]:
    r"""Return the ranks of \(L\)'s summands, or its own rank when indecomposable."""
    if L.is_decomposable():
        return tuple(summand.rank() for summand in L.summands())
    return (L.rank(),)

# ---- summand names ----

#: Gram matrix -> LaTeX name, for the indecomposable lattices worth naming.
#: ``catalogue.sage`` fills this in; the lookup is empty and harmless until then.
_INDECOMPOSABLE_NAMES: dict[tuple, str] = {}


def _gram_key(gram: "GramMatrix") -> tuple:
    r"""Return a hashable form of a Gram matrix, ignoring any subdivisions."""
    return tuple(tuple(row) for row in gram.rows())


def register_indecomposable(name: str, lattice: "FormModule") -> None:
    r"""Register *lattice*'s Gram matrix under the LaTeX *name*.

    Matching is Gram equality, not isometry: a block **is** the named lattice
    when the matrices agree, so nothing here asserts a theorem.  Decomposable
    entries are refused -- they can never appear as a block, so registering one
    would be dead weight that reads as if it could match.
    """
    assert not lattice.is_decomposable(), (
        f"{name} is decomposable, so it can never be a summand; "
        "name it by aggregating the summand list instead"
    )
    _INDECOMPOSABLE_NAMES.setdefault(_gram_key(lattice.gram_matrix()), name)


def _summand_name(block: "GramMatrix") -> str | None:
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
    twisted_name = next(
        (
            (scale, untwisted)
            for scale in (content, -content)
            if scale not in (0, 1, -1)
            if (
                untwisted := _INDECOMPOSABLE_NAMES.get(
                    _gram_key((gram / scale).change_ring(SageZZ))
                )
            )
            is not None
        ),
        None,
    )
    match twisted_name:
        case None:
            return None
        case (scale, untwisted):
            return f"{untwisted}({scale})"


def _decomposition_latex(L: "FormModule") -> str | None:
    r"""Return ``N_1 \oplus N_2 \oplus ...`` for *L*, or ``None`` if it has no summands.

    Unrecognized blocks fall back to a positional name; a lattice whose blocks
    are all unrecognized has nothing to say beyond its Gram matrix.
    """
    if not L.is_decomposable():
        return None
    names = [
        _summand_name(subobject)
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

def refine_one_lattice(lattice: "FormModule") -> None:
    r"""Refine a single integral lattice into the appropriate categories.

    Always refines into ``IntegralLattices``.  If signature is ``(n, 1)``,
    also joins ``HyperbolicLattices``.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.definite_lattices import DefiniteLattices
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.hyperbolic_lattices import HyperbolicLattices
    from dzack_research.preamble.refine import refine
    # Routed by the predicate the axiom gate re-asks, not a determinant
    # proxy: the radical is the kernel module of the correlation morphism,
    # and ``refine`` refuses the ``Nondegenerate`` axiom when it is nonzero.
    match lattice.is_nondegenerate():
        case False:
            refine(
                lattice,
                [
                    Lattices(ℤ).FinitelyGenerated(),
                    Lattices(ℤ).Integral(),
                ],
            )
            return
        case True:
            pass
    refine(lattice, IntegralLattices())
    # The Even axiom is admitted by its certifying predicate: ``refine``
    # re-asks ``is_even()`` and refuses a ``False``, so the routing here is
    # the same question the gate asks, not a diagonal proxy of its own.
    if lattice.is_even():
        refine(lattice, Lattices(ℤ).Even())
    pos, neg = lattice.signature_pair()
    if pos > 0 and neg > 0 and min(pos, neg) == 1:
        refine(lattice, HyperbolicLattices())
    # Definite either way round: this project writes the root lattices
    # negative definite, so both signs are the category.
    if pos == 0 or neg == 0:
        refine(lattice, DefiniteLattices())

_NAMED_GRAM_MATRICES: dict[str, Matrix] = {
    # The two names for the hyperbolic plane; the ADE names are read below.
    "U": matrix(SageZZ, [[0, 1], [1, 0]]),
    "H": matrix(SageZZ, [[0, 1], [1, 0]]),
}


def _cartan_type_of_name(name: str) -> "CartanType | None":
    r"""Return the root system a lattice name names, or ``None`` for $U$.

    A name is not a lattice: ``"A5"`` names a root system, and the lattice is
    that system's root lattice.  Reading the name is the only place the
    correspondence is written down, and what it hands back is the type rather
    than the matrix -- the matrix is one thing the type says, and the Weyl
    group and the Dynkin diagram are others.
    """
    if name in _NAMED_GRAM_MATRICES:
        return None
    match = re.fullmatch(r"([ADE])(\d+)", name)
    assert match, (
        f"{name!r} does not name a lattice here. The names are U and H for "
        "the hyperbolic plane and An, Dn, En for the root lattices; anything "
        "else is given by its Gram matrix."
    )
    from sage.combinat.root_system.cartan_type import CartanType

    return CartanType([match.group(1r), int(match.group(2r))])


def _gram_from_name(name: str) -> GramMatrix:
    r"""Return the Gram matrix a lattice name stands for.

    Constructed from the root realization: the entries are the inner
    products of the simple roots in the root system's ambient realization,
    with the AG sign convention applied here, at the single construction
    site -- $A_n$ comes out *negative* definite, with $-2$ on the diagonal,
    and the catalogue does not re-twist it.  Not a negated Cartan matrix:
    the Cartan matrix is $\langle\alpha_i,\alpha_j^\vee\rangle$ and is not
    symmetric outside the simply-laced types; the Gram matrix of a root
    lattice is $(\alpha_i,\alpha_j)$, read off the realization.
    """
    cartan_type = _cartan_type_of_name(name)
    if cartan_type is None:
        return _NAMED_GRAM_MATRICES[name]
    from sage.combinat.root_system.root_system import RootSystem

    realization = RootSystem(cartan_type).ambient_space()
    simple_roots = [
        realization.simple_root(index) for index in realization.index_set()
    ]
    return matrix(
        SageZZ,
        [
            [-left.inner_product(right) for right in simple_roots]
            for left in simple_roots
        ],
    )


def _integral_lattice_with_names(
    described: "GramMatrix | LatticeName",
    names: "OrderedSet" = None,
    module_generating_set: "OrderedSet" = None,
) -> "FormModule":
    r"""Return the integral lattice these arguments describe.

    A Gram matrix or a name, which is a matrix once it is read.  Nothing here
    passes through Sage's lattice class: that class is a submodule of a
    base-changed module over $\mathbb Q$ and imposes nondegeneracy, and neither
    is part of what a lattice is here -- a Coxeter root span with an
    $m=\infty$ bond is degenerate and is still one.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.root_lattices import refine_root_lattice
    cartan_type = None
    match described:
        case Matrix():
            gram = described
        case _:
            cartan_type = _cartan_type_of_name(described)
            gram = _gram_from_name(described)
    lattice = _lattice_with_gram(gram, module_generating_set)
    if cartan_type is not None:
        # Where the root system is known, which is here and nowhere later.
        refine_root_lattice(lattice, cartan_type)
    if names is not None:
        lattice = _apply_names(lattice, names)
    return lattice
