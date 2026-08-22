r"""The owned category of modules over a ring.

An $R$-module is an additively commutative group $M$ together with a ring
morphism $\rho:R\to\operatorname{End}(M)$; the scalar action *is* $\rho$, by
$r\cdot m:=\rho(r)(m)$.  That morphism is the defining datum, so this category
requires it: an object placed here without one is visibly unfinished.

Requiring it is the point.  Sage's ``Modules(R)`` is a placement, and the
preamble's own constructors reached it by refinement, so a module could exist
having never constructed the thing that makes it a module.  Every defect this
layer has produced -- a free module built twice on one $(R,S)$, generators
that were a tuple in one path and a set in another -- came of structure being
implied rather than carried.

The obligation cannot be a gate: ``_refine_category_`` admits anything and no
hook runs.  What it can be is *visible*, which is what ``abstract_method``
gives -- an unmet obligation resolves to the declaration, and the constructor
sweep reports it.

Modelled on the spike's module neighbourhood and owned here.  Over a field the
category dispatches, since a vector space is what a module over a field is.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.categories.modules import Module
    from sage.categories.morphism import Morphism
    from sage.structure.parent import Parent
    from dzack_research.preamble.owned_category import ConstructionData

from typing import Self

from sage.categories.additive_groups import AdditiveGroups
from sage.categories.category import Category
from dzack_research.preamble.owned_category_bases import Category_over_base_ring
from dzack_research.preamble.owned_category_bases import HomCategoryConstruction
from sage.categories.fields import Fields as SageFields
from sage.categories.modules import Modules as SageModules
from sage.categories.homset import Hom
from sage.categories.morphism import Morphism, SetMorphism
from sage.matrix.constructor import matrix
from sage.modules.free_module_element import vector
from sage.rings.rational_field import QQ as SageQQ
from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.utilities import zipsum
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.structure.element import Element as SageElement
from sage.structure.element import ModuleElement


class Modules(Category_over_base_ring):
    r"""Modules over $R$: an additive group with a ring morphism from $R$."""

    @staticmethod
    def __classcall_private__(cls: type, base_ring: "Ring") -> "Category":
        if base_ring in SageFields():
            return VectorSpaces(base_ring)
        category: "Category" = Category_over_base_ring.__classcall__(cls, base_ring)
        return category

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules"

    def super_categories(self) -> list:
        # A module is an additively commutative group with a ring action,
        # so the additive structure files at the owned additive spine.
        from dzack_research.preamble.categories.group.magmas import AdditiveGroups as OwnedAdditiveGroups

        return [
            SageModules(self.base_ring()),
            OwnedAdditiveGroups(),
            AdditiveGroups().AdditiveCommutative(),
        ]

    def __contains__(self, module: "Module") -> bool:
        r"""Return whether ``module`` is an object of this category.

        Test category membership first.  This includes abelian groups, since
        each has a canonical structure as a module over the integers.  Sage's
        base-ring membership test decides all remaining cases.
        """
        if Category.__contains__(self, module):
            return True
        return Category_over_base_ring.__contains__(self, module)

    class ParentMethods:
        def __init__(
            self, category: "Category", **rest: "ConstructionData"
        ) -> None:
            r"""Add the ring to the set below.

            A module is over a ring, and ``Modules(R)`` is the category that
            names which one.  So this level assigns the base, and every level
            above it inherits a module that already has one.  Sage decides
            membership in a category over a base ring by
            ``x.base_ring() is self.base_ring()``, so an object built without
            it belongs to no such category at all.
            """
            base_ring = category.base_ring()
            assert base_ring is not None, (
                f"{category} names no ring, so it builds no module: a module "
                "over no ring is not a module"
            )
            super().__init__(category=category, base=base_ring, **rest)

        @abstract_method
        def _ring_morphism_defining_module_action(self: Self) -> "Morphism":
            r"""Return $\rho:R\to\operatorname{End}(M)$, which is the module.

            Not a convenience: this morphism is what being an $R$-module
            *is*, and the scalar action is read off it.  A constructor that
            cannot produce it has not built a module, whatever category it
            placed the object in.

            $\operatorname{End}(M)$ is taken where the additive structure
            lives, so it is the endomorphism ring in $R\text{-Mod}$.
            """
            ...

        def scalar_action(self: Self) -> "Morphism":
            r"""Return the action, under the name the mathematics uses."""
            return self._ring_morphism_defining_module_action()

        def scalar_multiple(self: Self, scalar: "Element", element: "Element") -> "Element":
            r"""Return $r\cdot m$, which is $\rho(r)(m)$ and nothing else."""
            return self.scalar_action()(scalar)(element)

        def _Hom_(
            self: Self,
            codomain: "Module",
            category: "Category | None" = None,
        ) -> "Parent":
            r"""Build the module homset through its owned arrow-category level."""
            if category is None:
                category = Modules(self.base_ring())
            homset = super()._Hom_(codomain, category)
            if self is codomain:
                from dzack_research.preamble.refine import refine
                from sage.categories.rings import Rings

                return refine(homset, Rings())
            return homset

    class _HomCategory(HomCategoryConstruction):
        r"""$\operatorname{Hom}_R(M,N)$ of two modules over one ring."""

        class ParentMethods:
            def __init__(
                self,
                domain: "Module",
                codomain: "Module",
                **rest: "ConstructionData",
            ) -> None:
                assert domain.base_ring() == codomain.base_ring(), (
                    "module morphisms require the same base ring"
                )
                super().__init__(
                    domain=domain,
                    codomain=codomain,
                    base=domain.base_ring(),
                    check=False,
                    **rest,
                )

            def _element_constructor_(self, images: "ConstructionData") -> "Morphism":
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

                return ModuleMorphism(self, images)

            def zero(self) -> "Morphism":
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
                from dzack_research.preamble.categories.sets.owned_sets import Sets
                from sage.categories.homset import Hom
                from sage.categories.morphism import SetMorphism

                return ModuleMorphism(
                    self,
                    SetMorphism(
                        Hom(
                            self.domain().module_generating_set(),
                            self.codomain(),
                            Sets(),
                        ),
                        lambda element_of_S: self.codomain().zero(),
                    ),
                )

            def identity(self) -> "Morphism":
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

                assert self.domain() is self.codomain(), (
                    "an identity belongs to an endomorphism homset"
                )
                return ModuleMorphism(
                    self,
                    self.domain().module_generator_morphism(),
                )

            def __contains__(self, morphism: "ConstructionData") -> bool:
                return (
                    isinstance(morphism, Morphism)
                    and morphism.parent() is self
                )

            def _repr_(self) -> str:
                return f"Hom({self.domain()}, {self.codomain()})"

        class ElementMethods:
            r"""An $R$-linear map, read from its map on module generators."""

            @abstract_method
            def _domain_module_generating_set(self: Self) -> "OrderedSet":
                r"""Return the generating set on which this map is specified."""
                ...

            @abstract_method
            def module_generator_morphism(self: Self) -> "Morphism":
                r"""Return the set morphism whose linear extension is this map."""
                ...

            def _module_generator_image(
                self: Self, element_of_S: "Element"
            ) -> "ModuleElement":
                return self.module_generator_morphism()(element_of_S)

            def _pointwise(self, combine: "Callable") -> "Morphism":
                r"""Return the morphism sending \(e\) to ``combine(e)``.

                A morphism is its generator morphism extended linearly, so a
                pointwise operation is specified on the generating set and extended
                the same way.  Stated through the generating set rather than a
                dictionary of images, so it holds for an infinite framing too.
                """
                return self.parent()(
                    SetMorphism(
                        Hom(
                            self._domain_module_generating_set(),
                            self.codomain(),
                            Sets(),
                        ),
                        combine,
                    )
                )

            def __add__(self, other: ElementConstructorInput) -> "Morphism":
                r"""Return the pointwise sum \(f+g\).

                This is what makes \(\operatorname{Hom}(M,N)\) an abelian group and
                hence \(\operatorname{End}(M)\) a ring -- the codomain a module
                structure \(\rho:S\to\operatorname{End}(M)\) needs in order to be a
                ring morphism at all.
                """
                assert (
                    isinstance(other, Morphism)
                    and other.parent() is self.parent()
                ), "morphisms add only inside one homset"
                def sum_at(element_of_S: "Element") -> "ModuleElement":
                    here: "ModuleElement" = self.module_generator_morphism()(element_of_S)
                    there: "ModuleElement" = other.module_generator_morphism()(element_of_S)
                    return here + there

                return self._pointwise(sum_at)

            def __neg__(self) -> "Morphism":
                r"""Return the pointwise negation \(-f\)."""
                return self._pointwise(
                    lambda element_of_S: -self.module_generator_morphism()(
                        element_of_S
                    )
                )

            def __sub__(self, other: "Morphism") -> "Morphism":
                return self + (-other)

            def __mul__(self, other: ElementConstructorInput) -> "Morphism":
                r"""Return the composite \(f\circ g\).

                Sage's generic ``Morphism.__mul__`` builds a formal composite map,
                which is not a ``Morphism`` and so leaves neither this homset
                nor -- when domain and codomain agree -- the endomorphism ring closed
                under multiplication.  Composition is written here so that
                \(\operatorname{End}(M)\) is a ring in fact and not only by category
                placement.
                """
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
                assert isinstance(other, Morphism), (
                    "a module morphism composes with a module morphism"
                )
                assert other.codomain() is self.domain(), (
                    f"cannot compose {self} after {other}: the codomain of the "
                    "second is not the domain of the first"
                )
                return module_homset(other.domain(), self.codomain())(
                    SetMorphism(
                        Hom(
                            other._domain_module_generating_set(),
                            self.codomain(),
                            Sets(),
                        ),
                        lambda element_of_S: self(
                            other.module_generator_morphism()(element_of_S)
                        ),
                    )
                )

            def coimage(self) -> Parent:
                r"""Return $\operatorname{coim}(f)=M/\ker(f)$, presented by the kernel's inclusion.

                The dual of :meth:`cokernel`, computed as one: the coimage is the
                cokernel of $\ker(f)\hookrightarrow M$.  $R$-Mod is abelian, so the
                induced arrow $\operatorname{coim}(f)\to\operatorname{im}(f)$ is an
                isomorphism -- which is why no separate construction lives here.
                """
                return self.kernel().structure_morphism().cokernel()

            def equalizer(self, other: "Morphism") -> "Subobject":
                r"""Return $\operatorname{Eq}(f,g)\hookrightarrow M$ for a parallel pair.

                $R$-Mod is additive, so the equalizer of $f, g: M\to N$ is
                $\ker(f-g)$.  This subobject *is* the proof object for morphism
                equality: $f = g$ exactly when the equalizer is all of $M$, and a
                module generator outside it is a counterexample in hand -- equality
                of framed module morphisms is decided on the framing, and the
                witness or counterexample is returned as data rather than wrapped
                in a bespoke proof-carrying truth value (the source corpus's
                layered equality procedure collapses to this one definition on
                framed domains).
                """
                return (self - other).kernel()

            def retraction(self) -> "Morphism":
                r"""Return $r: N\to M$ with $r\circ f=\mathrm{id}_M$, for a split mono.

                A retraction exists exactly when $f$ is a split monomorphism --
                over a PID, for finitely generated modules, exactly when
                $\operatorname{coker}(f)$ is torsion free -- and that owned
                question gates the construction.  The matrix is produced by
                solving $F R = I$ over the base ring and the identity
                $r\circ f=\mathrm{id}$ is asserted on the composite.

                The source corpus also carried a Moore--Penrose pseudoinverse; that
                is a framing-dependent $\mathbb Q$-linear datum (the presentation
                matrix's own ``pseudoinverse()``), not owned vocabulary, and it is
                deliberately not re-landed here.
                """
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _one_sided_inverse_matrix, _module_morphism
                assert self.is_injective(), (
                    "a retraction is a left inverse; only a monomorphism has one"
                )
                assert self.cokernel().is_torsion_free(), (
                    "a monomorphism of finitely generated modules over a PID "
                    "splits exactly when its cokernel is torsion free"
                )
                domain, codomain = self.domain(), self.codomain()
                backward = _one_sided_inverse_matrix(
                    matrix(domain.base_ring(), self.matrix()), left=True
                )
                retraction = _module_morphism(
                    codomain,
                    domain,
                    [
                        zipsum(row, domain.module_generators(), domain.zero())
                        for row in backward.rows()
                    ],
                )
                return retraction

            def section(self) -> "Morphism":
                r"""Return $s: N\to M$ with $f\circ s=\mathrm{id}_N$, for a split epi.

                Every epimorphism onto a free module splits; more generally a
                section exists exactly when $f$ is a split epimorphism, and the
                construction is the transpose problem of :meth:`retraction`:
                solve $S F = I$ over the base ring, then assert
                $f\circ s=\mathrm{id}$ on the composite.
                """
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _one_sided_inverse_matrix, _module_morphism
                assert self.is_surjective(), (
                    "a section is a right inverse; only an epimorphism has one"
                )
                domain, codomain = self.domain(), self.codomain()
                backward = _one_sided_inverse_matrix(
                    matrix(domain.base_ring(), self.matrix()), left=False
                )
                section = _module_morphism(
                    codomain,
                    domain,
                    [
                        zipsum(row, domain.module_generators(), domain.zero())
                        for row in backward.rows()
                    ],
                )
                return section

            def image_contains(self, element: "Element") -> bool:
                r"""Return whether ``element`` lies in this morphism's image.

                A finite free domain has finitely many images.  Each image and the
                target have finite support, so membership is a finite row-module
                problem even when the codomain framing is infinite.
                """
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector, _coefficients
                assert element.parent() is self.codomain(), (
                    f"{element} is not an element of {self.codomain()}"
                )
                codomain_labels = self.codomain().module_generating_set()
                match codomain_labels in Sets().Finite():
                    case True:
                        system = self.matrix()
                        relations = self._codomain_relations()
                        match relations.nrows():
                            case 0:
                                pass
                            case _:
                                system = system.stack(relations)
                        return bool(_coordinate_vector(element) in system.row_module())
                    case False:
                        image_coefficients = [
                            _coefficients(image)
                            for image in self.images()
                        ]
                        target_coefficients = _coefficients(element)
                        support = tuple(
                            dict.fromkeys(
                                label
                                for coefficients in (*image_coefficients, target_coefficients)
                                for label in coefficients
                            )
                        )
                        base_ring = self.codomain().base_ring()
                        system = matrix(
                            base_ring,
                            [
                                [coefficients.get(label, base_ring.zero()) for label in support]
                                for coefficients in image_coefficients
                            ],
                        )
                        target = vector(
                            base_ring,
                            [target_coefficients.get(label, base_ring.zero()) for label in support],
                        )
                        return bool(target in system.row_module())

            def restrict(self, subobject: "Subobject") -> "Morphism":
                r"""Return $f\circ\iota$: precomposition with a subobject's embedding.

                Restriction *is* composition with the chosen monomorphism the
                subobject carries; nothing else is consulted.
                """
                embedding = subobject.structure_morphism()
                assert embedding.codomain() == self.domain(), (
                    "restriction needs a subobject of this morphism's domain; "
                    f"the embedding lands in {embedding.codomain()}, not {self.domain()}"
                )
                return subobject.Hom(self.codomain())(
                    {
                        label: self(embedding(subobject.module_generator(label)))
                        for label in subobject.module_generating_set()
                    }
                )

            def preserves(self, subobject: "Subobject") -> bool:
                r"""Return whether this endomorphism maps the subobject into itself.

                The factorization question: does $f\circ\iota$ factor through
                $\iota$ again -- i.e. does every generator image land back in the
                embedding's image?  Asked of the embedding, which owns membership in
                its image.
                """
                assert self.domain() == self.codomain(), (
                    "preservation is an endomorphism question; "
                    f"domain={self.domain()}, codomain={self.codomain()}"
                )
                embedding = subobject.structure_morphism()
                return all(
                    embedding.image_contains(self(embedding(generator)))
                    for generator in subobject.module_generators()
                )

            def saturation_factorization(self) -> "Morphism":
                r"""Return the monomorphism $M\to\overline{f(M)}$ an injective $f$ factors through.

                $\overline{f(M)}$ is the saturation (primitive closure) of the image
                subobject; the returned arrow is the witness of the factorization
                $f=\iota_{\overline{f(M)}}\circ g$, and its index is
                $[\overline{f(M)}:f(M)]$ -- $1$ exactly when $f$ is a primitive
                embedding.  The one coordinate solve lives here, on the arrow.
                """
                assert self.is_injective(), (
                    "the saturation factorization is monomorphism vocabulary"
                )
                saturated = self.image().saturation()
                embedding_rows = matrix(SageQQ, saturated.structure_morphism().matrix())
                factor_rows = embedding_rows.solve_left(matrix(SageQQ, self.matrix()))
                base_ring = self.domain().base_ring()
                assert all(entry in base_ring for entry in factor_rows.list()), (
                    "the factorization through the saturation is integral by "
                    "construction; a non-integral solve means the saturation is wrong"
                )
                factor = self.domain().Hom(saturated)(
                    {
                        label: zipsum(
                            (base_ring(entry) for entry in row),
                            saturated.module_generators(),
                            saturated.zero(),
                        )
                        for label, row in zip(
                            self.domain().module_generating_set(),
                            factor_rows.rows(),
                        )
                    }
                )
                embedding = saturated.structure_morphism()
                assert all(
                    embedding(factor(generator)) == self(generator)
                    for generator in self.domain().module_generators()
                ), "the factorization must compose back to the morphism it factors"
                return factor

            def direct_sum(self, summands: "Iterable") -> "Morphism":
                r"""Return $f\oplus g\oplus\cdots$: the direct sum acting on morphisms.

                The functor's action on arrows, completing the object-level
                ``direct_sum``: the domain and codomain are the object direct sums,
                and each summand's generator images are included into the matching
                summand of the codomain sum.  Folded pairwise exactly as the object
                construction folds, so the two spellings label their coproducts the
                same way.
                """
                from functools import reduce
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

                def orthogonal_sum(
                    left: "Morphism", right: "Morphism"
                ) -> "Morphism":
                    domain = left.domain().direct_sum([right.domain()])
                    codomain = left.codomain().direct_sum([right.codomain()])
                    images = {}
                    for side, inner in ((0, left), (1, right)):
                        inner_labels = tuple(inner.codomain().module_generating_set())
                        for label in inner.domain().module_generating_set():
                            image = inner(inner.domain().module_generator(label))
                            images[(side, label)] = zipsum(
                                _coordinate_vector(image),
                                tuple(
                                    codomain.module_generator((side, inner_label))
                                    for inner_label in inner_labels
                                ),
                                codomain.zero(),
                            )
                    return domain.Hom(codomain)(images)

                return reduce(orthogonal_sum, tuple(summands), self)

            # ---- endomorphism vocabulary ----

            def multiplicative_order(self) -> "RingElement":
                r"""Return the multiplicative order of this endomorphism;
                ``+Infinity`` for infinite order.  Computed by Sage on the matrix,
                which is a faithful picture of the endomorphism on a framed module."""
                assert self.domain() == self.codomain(), (
                    "multiplicative order is endomorphism vocabulary; "
                    f"domain={self.domain()}, codomain={self.codomain()}"
                )
                return matrix(self.matrix()).multiplicative_order()

            def is_nilpotent(self) -> bool:
                r"""Return whether $f^n=0$ for some $n$ ($n\le\mathrm{rk}$ suffices)."""
                assert self.domain() == self.codomain(), (
                    "nilpotence is endomorphism vocabulary; "
                    f"domain={self.domain()}, codomain={self.codomain()}"
                )
                engine = matrix(self.matrix())
                return bool((engine ** engine.nrows()).is_zero())

            def is_idempotent(self) -> bool:
                r"""Return whether $f\circ f=f$ (a projection onto its image)."""
                assert self.domain() == self.codomain(), (
                    "idempotence is endomorphism vocabulary; "
                    f"domain={self.domain()}, codomain={self.codomain()}"
                )
                engine = matrix(self.matrix())
                return bool(engine * engine == engine)

            def is_unipotent(self) -> bool:
                r"""Return whether $f-\mathrm{id}$ is nilpotent (parabolic type)."""
                assert self.domain() == self.codomain(), (
                    "unipotence is endomorphism vocabulary; "
                    f"domain={self.domain()}, codomain={self.codomain()}"
                )
                engine = matrix(self.matrix())
                difference = engine - engine.parent().identity_matrix()
                return bool((difference ** engine.nrows()).is_zero())

            def images(self: Self) -> tuple["ModuleElement", ...]:
                from dzack_research.preamble.categories.sets.owned_sets import Sets

                module_generating_set = self.domain().module_generating_set()
                assert module_generating_set in Sets().Finite(), (
                    "listing all images requires a finite framing set"
                )
                return tuple(
                    self._module_generator_image(element_of_S)
                    for element_of_S in module_generating_set
                )

            @cached_method
            def matrix(self: Self) -> "Matrix":
                r"""Return the matrix in the finite ordered framings."""
                from sage.matrix.constructor import matrix

                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
                from dzack_research.preamble.categories.rings.rings import engine_ring
                from dzack_research.preamble.categories.sets.owned_sets import Sets

                domain_labels = self.domain().module_generating_set()
                codomain_labels = self.codomain().module_generating_set()
                assert (
                    domain_labels in Sets().Finite()
                    and codomain_labels in Sets().Finite()
                ), "a matrix requires finite ordered framings"
                ring = engine_ring(self.codomain().base_ring())
                images = self.images()
                entries = (
                    matrix(ring, 0, len(tuple(codomain_labels)))
                    if not images
                    else matrix(
                        [
                            _coordinate_vector(image)
                            for image in images
                        ]
                    )
                )
                return entries.change_ring(ring)

            def _call_(
                self: Self, element: "ElementConstructorInput"
            ) -> "Element":
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coefficients
                from sage.structure.element import Element

                assert isinstance(element, Element), f"{element} is not an element"
                source = element
                if source.parent() is not self.domain():
                    assert source.parent() == self.domain(), (
                        f"{source} is not an element of {self.domain()}"
                    )
                    source = sum(
                        (
                            coefficient * self.domain().module_generator(label)
                            for label, coefficient in _coefficients(source).items()
                        ),
                        self.domain().zero(),
                    )
                return sum(
                    (
                        coefficient * self._module_generator_image(element_of_S)
                        for element_of_S, coefficient in _coefficients(source).items()
                    ),
                    self.codomain().zero(),
                )

            def _codomain_relations(self: Self) -> "Matrix":
                from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import _presentation_matrix

                codomain = self.codomain()
                return _presentation_matrix(codomain)

            def _kernel_coordinates(self: Self) -> tuple:
                r"""Return the domain coordinates of the finite syzygies."""
                from sage.rings.integer_ring import ZZ as SageZZ

                from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules
                from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModules
                from dzack_research.preamble.categories.rings.rings import engine_ring

                domain = self.domain()
                codomain = self.codomain()
                base_ring = domain.base_ring()
                coefficient_ring = engine_ring(base_ring)
                assert domain in FinitelyGeneratedFreeModules(base_ring), (
                    "this kernel algorithm requires a finitely generated free domain"
                )
                assert (
                    codomain in FinitelyGeneratedFreeModules(base_ring)
                    or codomain in FinitelyPresentedModules(base_ring)
                ), (
                    "this kernel algorithm requires a finite free or finitely "
                    "presented codomain"
                )
                assert coefficient_ring is SageZZ or coefficient_ring.is_field(), (
                    "kernels of presented modules are decided here over ZZ or a field"
                )
                image_matrix = self.matrix()
                codomain_relations = self._codomain_relations()
                equations = (
                    image_matrix.stack(codomain_relations)
                    if codomain_relations.nrows()
                    else image_matrix
                )
                domain_generator_count = len(
                    tuple(domain.module_generating_set())
                )
                return tuple(
                    relation[:domain_generator_count]
                    for relation in equations.left_kernel_matrix().rows()
                )

            def lift(self: Self, element: "Element") -> "ModuleElement":
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _solve_left_integrally
                from dzack_research.preamble.categories.rings.rings import engine_ring
                from dzack_research.preamble.utilities import zipsum

                assert element.parent() is self.codomain(), (
                    f"{element} is not an element of {self.codomain()}"
                )
                system = self.matrix()
                relations = self._codomain_relations()
                coefficients = _solve_left_integrally(
                    system.stack(relations) if relations.nrows() else system,
                    _coordinate_vector(element),
                    engine_ring(self.domain().base_ring()),
                )[: system.nrows()]
                preimage = zipsum(
                    coefficients,
                    self.domain().module_generators(),
                    self.domain().zero(),
                )
                assert self(preimage) == element, (
                    f"{element} is not in the image of this morphism"
                )
                return preimage

            def kernel(self: Self) -> "Subobject":
                r"""Return the kernel from finite presentation matrices.

                For $f:R^m\to R^n/\operatorname{row}(B)$, a row $x$
                lies in the kernel exactly when $xF+yB=0$ for some row
                $y$.  The first $m$ coordinates of the left syzygies of
                the stacked matrix $[F;B]$ therefore generate the kernel.

                This is a decision procedure for a finite free domain and a
                finite free or finitely presented codomain over ℤ or a
                field.  No claim is made for finitely presented
                modules over a general ring, where this repository has no
                syzygy decision algorithm.
                """
                from dzack_research.preamble.utilities import zipsum

                domain = self.domain()
                kernel_coordinates = self._kernel_coordinates()
                return domain.subobject_on(
                    [
                        zipsum(
                            coordinates,
                            domain.module_generators(),
                            domain.zero(),
                        )
                        for coordinates in kernel_coordinates
                        if any(coefficient != 0 for coefficient in coordinates)
                    ]
                )

            def cokernel(self: Self) -> "Parent":
                r"""Return $\operatorname{coker}(f)=N/f(M)$."""
                from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule

                return FinitelyPresentedModule(self)

            def image(self: Self) -> "Subobject":
                return self.codomain().subobject_on(list(self.images()))

            def is_injective(self: Self) -> bool:
                r"""Return whether the kernel is zero on the decidable surfaces.

                A finite torsion domain is decided by enumeration.  A finite
                free domain over ℤ or a field is decided by the presented
                kernel above.
                """
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _is_torsion
                from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules

                domain = self.domain()
                if domain in FinitelyGeneratedFreeModules(domain.base_ring()) and domain.is_zero():
                    return True
                if domain in FinitelyGeneratedFreeModules(domain.base_ring()):
                    return not any(
                        any(coefficient != 0 for coefficient in coordinates)
                        for coordinates in self._kernel_coordinates()
                    )
                if _is_torsion(domain):
                    zero = domain.zero()
                    return all(
                        element == zero or self(element) != self.codomain().zero()
                        for element in domain
                    )
                return bool(self.kernel().is_zero())

            def index(self: Self) -> "Integer | PlusInfinity":
                r"""Return $[N:f(M)]=|\operatorname{coker}f|$."""
                from sage.rings.infinity import Infinity
                from sage.rings.integer_ring import ZZ as SageZZ

                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _is_presented
                from dzack_research.preamble.categories.rings.rings import engine_ring

                codomain = self.codomain()
                image = self.matrix()
                width = len(tuple(codomain.module_generating_set()))
                if not _is_presented(codomain) and engine_ring(
                    codomain.base_ring()
                ).is_field():
                    if image.rank() != width:
                        return Infinity
                    return SageZZ.one()
                cardinality = self.cokernel().cardinality()
                if not cardinality.is_finite():
                    return Infinity
                return cardinality._integer_(SageZZ)

            def __eq__(self: Self, other: "MembershipInput") -> bool:
                from sage.categories.morphism import Morphism
                from dzack_research.preamble.categories.sets.owned_sets import Sets

                if not (
                    isinstance(other, Morphism)
                    and self.parent() is other.parent()
                ):
                    return False
                module_generating_set = self.domain().module_generating_set()
                assert module_generating_set in Sets().Finite(), (
                    "equality of maps on a nonenumerable framing needs an explicit theorem"
                )
                return self.images() == other.images()

            def __hash__(self: Self) -> int:
                from dzack_research.preamble.categories.sets.owned_sets import Sets

                module_generating_set = self.domain().module_generating_set()
                assert module_generating_set in Sets().Finite(), (
                    "a morphism on a nonenumerable framing is not hashable"
                )
                return hash((id(self.parent()), self.images()))

            def _repr_type(self: Self) -> str:
                return "Module"

            def _repr_defn(self: Self) -> str:
                from dzack_research.preamble.categories.sets.owned_sets import Sets

                module_generating_set = self.domain().module_generating_set()
                if module_generating_set not in Sets().Finite():
                    return "the linear extension of a generator morphism"
                return "\n".join(
                    f"{element_of_S!r} |--> "
                    f"{self._module_generator_image(element_of_S)}"
                    for element_of_S in module_generating_set
                )

    class ElementMethods(ModuleElement):
        r"""An element of a module: where Sage's module element enters the chain.

        The module level is where addition acquires scalars, so this is where
        ``ModuleElement`` enters, as ``Element`` enters at the set level and
        ``Parent`` at the parent root.  Sage finds the scalar action only for a
        ``ModuleElement`` (``sage/structure/coerce_actions.pyx``), so without
        this an element of a chain-built module has no $r\cdot m$ at all.
        """

        def __init__(self: Self, parent: "Parent", **rest: "ConstructionData") -> None:
            ModuleElement.__init__(self, parent)

        def __bool__(self: Self) -> bool:
            r"""Return whether this element differs from $0$.

            Sage states this for every element -- an element is true when it is
            not the zero of its parent -- and also declares it abstract on
            ``AdditiveMagmas.AdditiveUnital``.  In category order that
            declaration precedes the implementation, so the implementation is
            named here, on the level whose objects have a zero.
            """
            return SageElement.__bool__(self)


class VectorSpaces(Category_over_base_ring):
    r"""Modules over a field, which is what this category dispatches to."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "vector spaces"

    def super_categories(self) -> list:
        from sage.categories.vector_spaces import VectorSpaces as SageVectorSpaces

        return [
            SageVectorSpaces(self.base_ring()),
            Category_over_base_ring.__classcall__(Modules, self.base_ring()),
        ]

    class _HomCategory(Modules._HomCategory):
        r"""$\operatorname{Hom}_K(V,W)$, which is the module homset.

        Sage reads a functorial construction off the category's *class* with
        one ``getattr`` -- ``CovariantConstructionCategory.category_of`` asks
        ``getattr(type(category), "Homsets")`` and falls back to the
        structureless ``HomsetsOf`` when it finds nothing -- and it does not
        consult ``super_categories()``.  Reaching ``Modules(K)`` only through
        the category graph therefore left this construction unstated, and
        ``Hom_K(V, W)`` was built as a bare Sage homset whose elements came
        out as set maps rather than module morphisms: over a field, and only
        over a field.

        Declared rather than inherited because Sage binds a nested
        construction class to exactly one base category
        (``__classget__`` asserts it), and it carries no content of its own:
        a homset of vector spaces is a homset of modules, so everything is
        the base's.
        """
