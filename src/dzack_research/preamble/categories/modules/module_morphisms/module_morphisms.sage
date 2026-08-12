r"""Native homsets and morphisms for the owned module categories.

A map from a framed module is declared by a set morphism from its generating
set to the underlying set of the codomain.  Its parent is the canonical homset
of the named domain and codomain.  Construction checks every relation of a
presented domain, so membership in a homset is parenthood and nothing else.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Callable

from dzack_research.preamble.utilities import zipsum
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Group
    from dzack_research.preamble.lexicon import Module
    from dzack_research.preamble.lexicon import ModuleElement
    from dzack_research.preamble.lexicon import Vector

from sage.categories.groups import Groups
from sage.categories.modules import Modules
from dzack_research.preamble.categories.sets.sets import finite_ordered_set
from dzack_research.preamble.refine import refine
if TYPE_CHECKING:
    from sage.categories.category import Category
    from dzack_research.preamble.categories.sets.sets import Set
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule

from collections.abc import Iterator
from typing import Any, TYPE_CHECKING

from sage.misc.cachefunc import cached_method
from sage.categories.homset import Hom, Homset
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.rings import Rings
from sage.matrix.constructor import matrix
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement, vector
from sage.rings.integer_ring import ZZ as SageZZ
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.sets.cardinals import Cardinal
from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import matrix_group
from dzack_research.preamble.categories.modules.group_modules.characters import Character
from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import MorphismMatrix
from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet


class ModuleHomset(Homset):
    r"""The homset \(\operatorname{Hom}_R(M,N)\) of two framed modules."""

    def __init__(self, domain: "Module", codomain: "Module", category: "Category") -> None:
        assert domain.base_ring() == codomain.base_ring(), (
            "module morphisms require the same base ring"
        )
        Homset.__init__(
            self,
            domain,
            codomain,
            category=category,
            base=domain.base_ring(),
            check=False,
        )

    def _element_constructor_(self, images: dict) -> "ModuleMorphism":
        return ModuleMorphism(self, images)

    def zero(self) -> "ModuleMorphism":
        return ModuleMorphism(
            self,
            SetMorphism(
                Hom(
                    self.domain().module_generating_set(),
                    UnderlyingSet(self.codomain()),
                    Sets(),
                ),
                lambda element_of_S: self.codomain().zero(),
            ),
        )

    def identity(self) -> "ModuleMorphism":
        assert self.domain() is self.codomain(), (
            "an identity belongs to an endomorphism homset"
        )
        return ModuleMorphism(
            self,
            self.domain().module_generator_morphism(),
        )

    def __contains__(self, morphism: "Morphism") -> bool:
        return (
            isinstance(morphism, ModuleMorphism)
            and morphism.parent() is self
        )

    def _repr_(self) -> str:
        return f"Hom({self.domain()}, {self.codomain()})"


def module_homset(domain: "Module", codomain: "Module") -> ModuleHomset:
    r"""Return the canonical module homset after forgetting extra structure."""
    cache = domain.__dict__.setdefault("_module_homsets", {})
    homset = cache.get(codomain)
    if homset is None:
        homset = ModuleHomset(
            domain,
            codomain,
            Modules(domain.base_ring()),
        )
        cache[codomain] = homset
    return homset


def _module_morphism(domain: "Module", codomain: "Module", images: dict) -> "ModuleMorphism":
    r"""Construct a module morphism through its canonical homset."""
    return module_homset(domain, codomain)(images)


def endomorphism_ring(module: "Module") -> ModuleHomset:
    r"""Return \(\operatorname{End}_R(M)\): the endset, as a ring.

    Multiplication is composition and addition is pointwise, so the endset
    of \(M\) in \(R\text{-Mod}\) is a ring.  This is the codomain of the
    structure morphism \(\rho:S\to\operatorname{End}(M)\) that *is* an
    \(S\)-module structure on \(M\), which is why it must be a ring and not
    merely a monoid.

    Taken in \(R\text{-Mod}\), never in a category of form-bearing modules:
    isometries do not add, so form-preserving endomorphisms are not an
    abelian group.  A form-bearing \(S\)-module is one whose \(\rho\) happens
    to land in the subgroup preserving the form, not one whose endomorphism
    ring was formed somewhere else.
    """
    return refine(module_homset(module, module), Rings())


def _underlying_module(module: "Module") -> "Module":
    # Local: at module level this closes an import cycle; the form module is
    # built by the time a morphism reads its domain.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule

    match module:
        case FormModule():
            return module.forget_form()
        case Parent():
            return module
        case _:
            assert False, f"{module!r} is not a module parent"


def _coordinate_vector(element: "Element") -> FreeModuleElement:
    r"""Return finite coordinates in the element's declared framing."""
    # Local: at module level these close an import cycle; every element module
    # is built by the time an element is handed over for coordinates.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModuleElement
    from dzack_research.preamble.categories.modules.group_modules.group_modules import GroupModuleElement
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModuleElement
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModuleElement

    match element:
        case BasedFreeModuleElement():
            return element._coordinates_
        case FormModuleElement():
            return _coordinate_vector(element.forget_form())
        case GroupModuleElement():
            return _coordinate_vector(element.forget_action())
        case FinitelyPresentedModuleElement():
            return vector(element._lift())
        case _:
            assert False, (
                f"{element} has no finite ordered framing in which a matrix "
                "coordinate vector is defined"
            )


def _coefficients(element: "Element") -> dict:
    r"""Return the finite coefficient function of a framed-module element."""
    # Local: at module level these close an import cycle; every element module
    # is built by the time an element is handed over for coefficients.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModuleElement
    from dzack_research.preamble.categories.modules.group_modules.group_modules import GroupModuleElement
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModuleOnSetElement
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModuleElement
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModuleElement

    match element:
        case FormModuleElement():
            return _coefficients(element.forget_form())
        case GroupModuleElement():
            return _coefficients(element.forget_action())
        case FreeModuleOnSetElement() | BasedFreeModuleElement():
            return dict(element.coefficients())
        case FinitelyPresentedModuleElement():
            return {
                element_of_S: coefficient
                for element_of_S, coefficient in zip(
                    element.parent().module_generating_set(), element._lift()
                )
                if coefficient != 0
            }
        case _:
            assert False, (
                f"{element} is not an element of an owned framed module"
            )


def _is_torsion(module: "Module") -> bool:
    # Local: at module level this closes an import cycle; the presented module
    # is built by the time a morphism asks about its domain.
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule

    module = _underlying_module(module)
    return isinstance(module, FinitelyPresentedModule) and module.is_torsion()


def _independent_module_generators(module: "Module", module_generators: "OrderedSet") -> list:
    r"""Return a basis of the submodule spanned by finite input.

    Each input element has finite support in the framing.  Independence is
    therefore a finite computation on the union of those supports, even when
    the module's full framing is infinite.
    """
    # Local: at module level this closes an import cycle; the ring module is
    # built by the time generators are reduced.
    from dzack_research.preamble.categories.rings.rings import engine_ring

    module_generators = list(module_generators)
    if not module_generators:
        return []
    coefficient_functions = [_coefficients(generator) for generator in module_generators]
    support = tuple(
        dict.fromkeys(
            label
            for coefficients in coefficient_functions
            for label in coefficients
        )
    )
    rows = matrix(
        engine_ring(module.base_ring()),
        [
            [coefficients.get(label, module.base_ring().zero()) for label in support]
            for coefficients in coefficient_functions
        ],
    )
    independent = MorphismMatrix(rows).normal_form().rows()
    return [
        zipsum(
            row,
            (module.module_generator(label) for label in support),
            module.zero(),
        )
        for row in independent
    ]


def _expand_subobject_dict(parent: ModuleHomset, images: dict) -> dict:
    r"""Expand a summand-level assignment onto the domain's framed labels.

    Both sides are ordered generating sets. A key is a framed module (which
    contributes its own labels), an element of the domain (which resolves to
    the label naming it), or a label. A value is a framed module -- a
    subobject included -- whose module generators are the images in order, an
    ordered enumeration of elements, or, when the source has rank one, a
    single element.
    """
    # Local: at module level these close an import cycle; the framed and
    # subobject modules are built by the time an assignment is expanded.
    from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobjects

    domain = parent.domain()
    codomain = parent.codomain()
    module_generating_set = domain.module_generating_set()
    if set(images) == set(module_generating_set):
        return dict(images)

    label_of = {
        domain.module_generator(label): label
        for label in module_generating_set
    }

    expanded = {}
    for key, val in images.items():
        match key:
            case _ if key in FramedModules(domain.base_ring()):
                sources = tuple(key.module_generating_set())
            case Element() if key in label_of:
                sources = (label_of[key],)
            case _:
                sources = (key,)

        match val:
            case _ if val in Subobjects():
                # A subobject's own generators are abstract -- e_0 has
                # coordinates of length rank(S).  What lands in the codomain
                # is their image f(e_i), whose coordinates have the
                # codomain's rank.  These are not the same family.
                targets = tuple(val.embedded_module_generators())
            case _ if val in FramedModules(codomain.base_ring()):
                targets = tuple(val.module_generators())
            case list() | tuple():
                targets = tuple(val)
            case _:
                assert len(sources) == 1, (
                    "one target element requires a rank-one source"
                )
                targets = (val,)

        assert len(sources) == len(targets), (
            f"subobject {key} has {len(sources)} generators, but image has "
            f"{len(targets)}"
        )
        for source, target in zip(sources, targets, strict=True):
            expanded[source] = (
                target
                if isinstance(target, Element) and target.parent() is codomain
                else codomain(target)
            )

    assert set(expanded) == set(module_generating_set), (
        "the assignment must name exactly every element of the generating "
        f"set; got {set(expanded)} vs {set(module_generating_set)}"
    )
    return expanded


class ModuleMorphism(Morphism):
    r"""The linear extension of a morphism \(S\to U(N)\)."""

    def __init__(self, parent: ModuleHomset, images: dict) -> None:
        Morphism.__init__(self, parent)
        module_generating_set = self._domain_module_generating_set()
        set_homset = Hom(
            module_generating_set,
            UnderlyingSet(parent.codomain()),
            Sets(),
        )
        match images:
            case SetMorphism():
                assert images.parent() is set_homset, (
                    "the generator morphism must belong to "
                    f"{set_homset}, got {images.parent()}"
                )
                module_generator_morphism = images
            case dict():
                assert module_generating_set in Sets().Finite(), (
                    "a dictionary specifies a morphism only for a finite "
                    "generating set; use a set morphism on the generating set"
                )
                values = _expand_subobject_dict(parent, images)
                assert all(
                    image.parent() == parent.codomain()
                    for image in values.values()
                ), "every specified generator image must belong to the codomain"
                module_generator_morphism = SetMorphism(
                    set_homset,
                    values.__getitem__,
                )
            case _ if callable(images):
                module_generator_morphism = SetMorphism(set_homset, images)
            case _:
                assert False, (
                    "a module morphism is the linear extension of a set "
                    "morphism from the domain's generating set"
                )
        self._generator_morphism = module_generator_morphism
        self._check_relations()

    def _domain_module_generating_set(self) -> "OrderedSet":
        return self.domain().module_generating_set()

    def _pointwise(self, combine: "Callable") -> "ModuleMorphism":
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
                    UnderlyingSet(self.codomain()),
                    Sets(),
                ),
                combine,
            )
        )

    def __add__(self, other: object) -> "ModuleMorphism":
        r"""Return the pointwise sum \(f+g\).

        This is what makes \(\operatorname{Hom}(M,N)\) an abelian group and
        hence \(\operatorname{End}(M)\) a ring -- the codomain a module
        structure \(\rho:S\to\operatorname{End}(M)\) needs in order to be a
        ring morphism at all.
        """
        assert (
            isinstance(other, ModuleMorphism)
            and other.parent() is self.parent()
        ), "morphisms add only inside one homset"
        return self._pointwise(
            lambda element_of_S: (
                self.module_generator_morphism()._call_(element_of_S)
                + other.module_generator_morphism()._call_(element_of_S)
            )
        )

    def __neg__(self) -> "ModuleMorphism":
        r"""Return the pointwise negation \(-f\)."""
        return self._pointwise(
            lambda element_of_S: -self.module_generator_morphism()._call_(
                element_of_S
            )
        )

    def __sub__(self, other: object) -> "ModuleMorphism":
        return self + (-other)

    def __mul__(self, other: object) -> "ModuleMorphism":
        r"""Return the composite \(f\circ g\).

        Sage's generic ``Morphism.__mul__`` builds a formal composite map,
        which is not a ``ModuleMorphism`` and so leaves neither this homset
        nor -- when domain and codomain agree -- the endomorphism ring closed
        under multiplication.  Composition is written here so that
        \(\operatorname{End}(M)\) is a ring in fact and not only by category
        placement.
        """
        assert isinstance(other, ModuleMorphism), (
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
                    UnderlyingSet(self.codomain()),
                    Sets(),
                ),
                lambda element_of_S: self(
                    other.module_generator_morphism()._call_(element_of_S)
                ),
            )
        )

    def _check_relations(self) -> None:
        # Local: at module level this closes an import cycle; the presented
        # category is built by the time relations are checked.
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModules

        domain = _underlying_module(self.domain())
        if domain not in FinitelyPresentedModules(domain.base_ring()):
            return
        module_generating_set = tuple(domain.module_generating_set())
        zero = self.codomain().zero()
        assert all(
            zipsum(
            relation,
            module_generating_set,
            zero,
            term=lambda coefficient, element_of_S: coefficient
                    * self._module_generator_image(element_of_S),
        )
            == zero
            for relation in domain.relation_matrix().rows()
        ), "the assignment does not kill every relation"

    def module_generator_morphism(self) -> SetMorphism:
        r"""Return the set morphism whose linear extension is this morphism."""
        return self._generator_morphism

    def _module_generator_image(self, element_of_S: "Element") -> "ModuleElement":
        r"""Evaluate the generator map on an element already in its domain."""
        return self.module_generator_morphism()._call_(element_of_S)

    def images(self) -> tuple:
        module_generating_set = self.domain().module_generating_set()
        assert module_generating_set in Sets().Finite(), (
            "listing all images requires a finite framing set"
        )
        return tuple(
            self._module_generator_image(element_of_S)
            for element_of_S in module_generating_set
        )

    def matrix(self) -> MorphismMatrix:
        r"""Return the matrix in the finite ordered framings."""
        try:
            return self._matrix
        except AttributeError:
            domain_labels = self.domain().module_generating_set()
            codomain_labels = self.codomain().module_generating_set()
            assert (
                domain_labels in Sets().Finite()
                and codomain_labels in Sets().Finite()
            ), "a matrix requires finite ordered framings"
            images = self.images()
            if not images:
                m = matrix(
                    self.codomain().base_ring(),
                    0,
                    len(tuple(codomain_labels)),
                )
            else:
                m = matrix([_coordinate_vector(image) for image in images])

            self._matrix = MorphismMatrix(m)
            return self._matrix

    def _call_(self, element: "Element") -> "Element":
        if element.parent() is not self.domain():
            assert element.parent() == self.domain(), (
                f"{element} is not an element of {self.domain()}"
            )
            element = sum(
                (
                    coefficient * self.domain().module_generator(label)
                    for label, coefficient in _coefficients(element).items()
                ),
                self.domain().zero(),
            )
        return sum(
            (
                coefficient
                * self._module_generator_image(element_of_S)
                for element_of_S, coefficient in _coefficients(element).items()
            ),
            self.codomain().zero(),
        )

    def lift(self, element: "Element") -> "ModuleElement":
        assert element.parent() is self.codomain(), (
            f"{element} is not an element of {self.codomain()}"
        )
        system = self.matrix()
        relations = self._codomain_relations()
        coefficients = _solve_left_integrally(
            system.stack(relations) if relations.nrows() else system,
            _coordinate_vector(element),
        )
        coefficients = coefficients[: system.nrows()]
        preimage = zipsum(
            coefficients,
            self.domain().module_generators(),
            self.domain().zero(),
        )
        assert self(preimage) == element, (
            f"{element} is not in the image of this morphism"
        )
        return preimage

    def kernel(self) -> "Subobject":
        assert not _is_torsion(self.domain()), (
            "this kernel construction requires a free domain"
        )
        # The kernel matrix says how the kernel's generators are written in
        # this domain's generators; it does not *name* them.  ``subobject_on``
        # builds the abstract module and the inclusion that carries that data.
        return self.domain().subobject_on(
            [
                zipsum(
                    row,
                    self.domain().module_generators(),
                    self.domain().zero(),
                )
                for row in self.matrix()._left_kernel_matrix().rows()
            ]
        )

    def cokernel(self) -> "FinitelyPresentedModule":
        r"""Return $\operatorname{coker}(f)=N/f(M)$, the module $f$ presents.

        Not assumed torsion: for $\mathbb Zv\hookrightarrow L$ with $L$ of
        rank 22 the cokernel has rank 21.  ``FinitelyPresentedModule``
        refines itself into the torsion categories exactly when it is
        torsion, so the general answer specialises rather than the special
        answer being asserted.
        """
        # Local: at module level this closes an import cycle; the presented
        # module is built by the time a cokernel is asked for.
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule

        return FinitelyPresentedModule(self)

    def image(self) -> "Subobject":
        return self.codomain().subobject_on(list(self.images()))

    def image_contains(self, element: "Element") -> bool:
        r"""Return whether ``element`` lies in this morphism's image.

        A finite free domain has finitely many images.  Each image and the
        target have finite support, so membership is a finite row-module
        problem even when the codomain framing is infinite.
        """
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

    def is_injective(self) -> bool:
        r"""Return whether this morphism is a monomorphism."""
        match self.__dict__.get("_known_injective"):
            case True:
                return True
            case _:
                pass
        # Local: at module level this closes an import cycle; the free-module
        # category is built by the time injectivity is asked about.
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules

        domain = self.domain()
        if _is_torsion(domain):
            zero = domain.zero()
            return all(
                element == zero or self(element) != self.codomain().zero()
                for element in domain
            )
        assert domain in FramedFreeModules(domain.base_ring()), (
            "injectivity is implemented for free and finite torsion domains"
        )
        independent_images = _independent_module_generators(
            self.codomain(),
            self.images(),
        )
        return bool(len(independent_images) == domain.rank())

    def index(self) -> "Integer":
        r"""Return $[N:f(M)]$.

        Over $\mathbb Z$ the index is the determinant of the sublattice the
        image spans, read off one reduction; a presented codomain contributes
        its relations to the same reduction rather than to a second one.  Over
        a field a full-rank image is everything, so the index is 1.
        """
        # Local: at module level these close an import cycle; the presented
        # module and ring modules are built by the time an index is asked for.
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
        from dzack_research.preamble.categories.rings.rings import engine_ring

        codomain = _underlying_module(self.codomain())
        image = self.matrix()
        width = len(tuple(codomain.module_generating_set()))

        if not isinstance(codomain, FinitelyPresentedModule) and (
            engine_ring(codomain.base_ring()) is not SageZZ
        ):
            assert image.rank() == width, (
                "the image does not have finite index in the codomain"
            )
            return SageZZ.one()

        spanning = image
        if isinstance(codomain, FinitelyPresentedModule):
            relations = codomain.relation_matrix()
            spanning = relations.stack(image) if image.nrows() else relations
        reduced = spanning.normal_form()
        assert reduced.nrows() == width, (
            "the image does not have finite index in the codomain"
        )
        return abs(reduced.det())

    def orthogonal_complement(self) -> "Subobject":
        codomain = self.codomain()
        assert not _is_torsion(codomain), (
            "orthogonal complement is defined here in a free codomain"
        )
        pairing = MorphismMatrix(codomain.gram_matrix()) * self.matrix().transpose()
        return codomain.subobject_on(
            [
                zipsum(
            row,
            codomain.module_generators(),
            codomain.zero(),
        )
            for row in pairing._left_kernel_matrix().rows()
        ]
        )

    def _codomain_relations(self) -> MorphismMatrix:
        # Local: at module level this closes an import cycle; the presented
        # module is built by the time relations are read off a codomain.
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule

        codomain = _underlying_module(self.codomain())
        match codomain:
            case FinitelyPresentedModule():
                return codomain.relation_matrix()
            case _:
                # A free codomain imposes no relations. The empty matrix is
                # still the matrix of a morphism, so it is wrapped like every
                # other -- one declared return type, true on both branches.
                return MorphismMatrix(
                    matrix(
                        SageZZ,
                        0,
                        len(tuple(self.codomain().module_generating_set())),
                    )
                )

    def _repr_type(self) -> str:
        return "Module"

    def _repr_defn(self) -> str:
        module_generating_set = self.domain().module_generating_set()
        if module_generating_set not in Sets().Finite():
            return "the linear extension of a generator morphism"
        return "\n".join(
            f"{element_of_S!r} |--> "
            f"{self._module_generator_image(element_of_S)}"
            for element_of_S in module_generating_set
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ModuleMorphism) or self.parent() is not other.parent():
            return False
        module_generating_set = self.domain().module_generating_set()
        assert module_generating_set in Sets().Finite(), (
            "equality of maps on a nonenumerable framing needs an explicit theorem"
        )
        return self.images() == other.images()

    def __hash__(self) -> int:
        module_generating_set = self.domain().module_generating_set()
        assert module_generating_set in Sets().Finite(), (
            "a morphism on a nonenumerable framing is not hashable"
        )
        return hash((id(self.parent()), self.images()))


class FramingMorphism(ModuleMorphism):
    r"""A declared epimorphism \(F_R(S)\twoheadrightarrow M\).

    Surjectivity is part of the construction datum.  It is not replaced by an
    enumeration algorithm, since \(S\) may be a membership-only set.
    """

    def __init__(self, parent: ModuleHomset, images: dict) -> None:
        # Local: at module level this closes an import cycle; the free-module
        # category is built by the time a framing is declared.
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules

        assert parent.domain() in FramedFreeModules(
            parent.domain().base_ring()
        ), "the source of a framing is a free module on a specified set"
        ModuleMorphism.__init__(self, parent, images)

    def _domain_module_generating_set(self) -> "OrderedSet":
        return self.domain().module_generator_morphism().domain()

    def is_surjective(self) -> bool:
        return True


def framing_morphism(
    domain: "Module",
    codomain: "Module",
    images: dict,
) -> FramingMorphism:
    r"""Construct the declared framing epimorphism in its canonical homset."""
    return FramingMorphism(module_homset(domain, codomain), images)


class ModuleAutomorphism(ModuleMorphism):
    r"""An invertible endomorphism of a finitely generated free module."""

    def __init__(self, parent: "ModuleAutomorphismGroup", images: dict) -> None:
        ModuleMorphism.__init__(self, parent, images)
        assert self.domain() is self.codomain(), (
            "an automorphism is an endomorphism"
        )
        determinant = self.matrix().det()
        assert determinant.is_unit(), (
            f"the determinant {determinant} is not a unit"
        )

    def __mul__(self, other: object) -> "ModuleAutomorphism":
        assert (
            isinstance(other, ModuleAutomorphism)
            and other.parent() is self.parent()
        ), "composition here is internal to one automorphism group"
        return self.parent()(
                SetMorphism(
                    Hom(
                        self.domain().module_generating_set(),
                        UnderlyingSet(self.codomain()),
                        Sets(),
                    ),
                    lambda element_of_S: self(
                        other.module_generator_morphism()._call_(element_of_S)
                    ),
                )
            )

    def inverse(self) -> "ModuleAutomorphism":
        inverse_matrix = self.matrix().inverse().change_ring(SageZZ)
        images = [
            zipsum(
            row,
            self.domain().module_generators(),
            self.domain().zero(),
        )
            for row in inverse_matrix.rows()
        ]
        return self.parent()(
                dict(zip(self.domain().module_generating_set(), images))
            )

    def cyclic_subgroup(self) -> "ModuleAutomorphismGroup":
        return self.parent().subgroup_on({self})

    def _libgap_(self) -> "GapElement":
        r"""Return this automorphism inside its group's GAP model.

        A character is a function on a group, and when the group is a literal
        subgroup of \(\operatorname{Aut}(M)\) its elements are these
        automorphisms; declaring where they sit in GAP is what makes GAP's
        characters functions on them rather than on a parallel set of
        matrices a caller would have to translate for.  This is the
        conversion protocol ``ClassFunction`` evaluates through.
        """
        return self.parent()._defining_matrix_group()(
            self.matrix()._sage_matrix()
        ).gap()

    gap = _libgap_


class FiniteAutomorphismSubgroup:
    r"""The finite-group surface of a literal subgroup of \(\operatorname{Aut}(M)\).

    A subgroup generated by named automorphisms is a group in its own right,
    and it is the \(G\) of one of the two ways a representation is built here:
    the caller names elements of \(\operatorname{Aut}(M)\), \(G\) is what they
    generate, and \(\rho\) is the inclusion.  The other way names an abstract
    \(G\) and a \(\rho\) whose well-definedness the action constructor checks
    against \(G\)'s relations; both reach character theory the same way, by
    asking \(G\) for its characters and the module for \(\operatorname{tr}
    \rho(-)\).  So this class answers the questions a finite group answers.

    The elements here *are* automorphisms, so the matrices of the generators
    present this group faithfully: what is modelled below is this group and
    not the image of any \(\rho\).  An action's matrices present \(\rho(G)\),
    a proper quotient of \(G\) whenever \(\rho\) has a kernel, whose character
    theory is a different one -- which is why no model is ever built from an
    action.  The full \(\operatorname{Aut}(M)\) is the other role an
    automorphism homset carries, the codomain \(\rho\) maps into and generally
    infinite, and the finiteness assertion is what separates the two.

    A mixin because the two automorphism homsets that take this role --
    \(\operatorname{Aut}_R(M)\) and \(O(L)\) -- sit in unrelated homset
    hierarchies and the group surface is the same in both.
    """

    def inclusion(self) -> "GroupAction":
        r"""Return \(\rho:G\hookrightarrow\operatorname{Aut}(M)\), this group's own arrow.

        A literal subgroup of \(\operatorname{Aut}(M)\) determines one
        representation with no choice left to anyone: \(G\) is these elements
        and \(\rho\) sends each to itself.  So the arrow is named here, by the
        group whose data alone decides it, and a module never assembles a
        \(\rho\) for a caller who handed it an automorphism.

        Faithful, because it is an inclusion.  A caller who means an abstract
        \(G\), or a \(\rho\) with a kernel, constructs both in
        ``group_action_homset(G, M)`` instead; this is the case where that
        homset's element is already determined.

        The images are re-expressed in \(\operatorname{Aut}(M)\) because the
        generators' parent is this subgroup, and \(\rho\) is an arrow *into*
        the full automorphism homset.
        """
        assert self.is_finite(), (
            "an inclusion is the arrow of a literal finite subgroup, not of "
            "the whole automorphism homset"
        )
        module = self.domain()
        automorphisms = module.Aut()
        return group_action_homset(self, module)(
            [
                automorphisms(
                    {
                        label: generator(module.module_generator(label))
                        for label in module.module_generating_set()
                    }
                )
                for generator in self.group_generators()
            ]
        )

    @cached_method
    def _defining_matrix_group(self) -> "Group":
        r"""Return the GAP-backed model of this group. The private presentation.

        The generators' matrices are used here once, to hand GAP a group it
        can compute conjugacy classes and a character table for.  Every method
        below translates GAP's answers back into this group's own elements, so
        no caller ever holds a matrix group.
        """
        assert self.is_finite(), (
            "a group surface is for a finite literal subgroup, not for the "
            "automorphism homset an action maps into"
        )
        return matrix_group(
            (
                generator.matrix()
                for generator in self.group_generators()
            )
        )

    @cached_method
    def _by_matrix(self) -> dict:
        r"""Index this group's own elements by their matrices."""
        return {element.matrix(): element for element in self}

    def conjugacy_classes_representatives(self) -> tuple:
        r"""Return one element of this group from each conjugacy class.

        In this group's own elements, and in the order the character table is
        written in: a class function is declared by its values in this order,
        so returning representatives from a parallel model would silently
        write every character against the wrong classes.
        """
        by_matrix = self._by_matrix()
        representatives = tuple(
            by_matrix.get(MorphismMatrix(representative.matrix()))
            for representative in
            self._defining_matrix_group().conjugacy_classes_representatives()
        )
        assert all(
            representative is not None for representative in representatives
        ), (
            "a class representative of the model is not an element of this "
            "subgroup: the model does not present this group"
        )
        return representatives

    def irreducible_characters(self) -> tuple:
        r"""Return the absolutely irreducible characters of this group.

        Class functions on this group, whatever module it goes on to act on:
        the conjugacy classes, the table, and the values are GAP's, computed
        from the group alone.  The character of a *representation* is a
        separate composite, \(g\mapsto\operatorname{tr}\rho(g)\), and is the
        only place a module enters.
        """
        return tuple(
            Character(class_function)
            for class_function in
            self._defining_matrix_group().irreducible_characters()
        )

    def character(self, values: "OrderedSet") -> Character:
        r"""Return the class function taking ``values`` on the conjugacy classes.

        In the order ``conjugacy_classes_representatives`` returns them.
        """
        return Character(self._defining_matrix_group().character(list(values)))

    def trivial_character(self) -> Character:
        return Character(self._defining_matrix_group().trivial_character())


class ModuleAutomorphismGroup(FiniteAutomorphismSubgroup, ModuleHomset):
    r"""The automorphism homset, or a finite subgroup with the same objects."""

    Element = ModuleAutomorphism

    def __init__(self, module: "Module", group_generators: "OrderedSet" = None) -> None:
        ModuleHomset.__init__(
            self,
            module,
            module,
            Modules(module.base_ring()),
        )
        self._group_generators = None
        self._elements = None
        if group_generators is not None:
            supplied = tuple(group_generators)
            assert supplied, "a generated subgroup needs at least one generator"
            assert all(
                isinstance(generator, ModuleAutomorphism)
                for generator in supplied
            ), "subgroup generators must be module automorphisms"
            self._group_generators = tuple(
                self(generator.module_generator_morphism())
                for generator in supplied
            )
            self._elements = self._close()

    def _element_constructor_(self, images: dict) -> ModuleAutomorphism:
        return ModuleAutomorphism(self, images)

    def module(self) -> "Module":
        return self.domain()

    def one(self) -> ModuleAutomorphism:
        return self(self.module().module_generator_morphism())

    def subgroup_on(self, group_generators: "Set") -> "ModuleAutomorphismGroup":
        r"""Return the subgroup generated by a *set* of automorphisms."""
        assert all(generator in self for generator in group_generators), (
            "each subgroup generator must belong to this automorphism group"
        )
        return ModuleAutomorphismGroup(self.module(), group_generators)

    def group_generators(self) -> TotallyOrderedFiniteSet:
        return finite_ordered_set(()) if self._group_generators is None else finite_ordered_set(self._group_generators)

    def is_finite(self) -> bool:
        return self._elements is not None

    def order(self) -> "Cardinal":
        r"""Return \(|G|\), the cardinality of this group.

        A cardinality, not an integer: \(\operatorname{Aut}(M)\) for a free
        \(M\) of rank \(\ge 2\) over \(\mathbb Z\) is
        \(\mathrm{GL}_n(\mathbb Z)\), which is infinite.  Refusing to answer
        there would be assuming finiteness of a group that simply is not
        finite; the order is \(\aleph_0\) and saying so costs nothing.
        """
        if self._elements is None:
            return Sets.ℵ[0]
        return Cardinal(len(self._elements))

    def __iter__(self) -> Iterator[Any]:
        assert self._elements is not None, (
            "the full automorphism homset is not enumerable"
        )
        return iter(self._elements)

    def __contains__(self, element: "Element") -> bool:
        return (
            isinstance(element, ModuleAutomorphism)
            and element.parent() is self
        )

    def _close(self) -> tuple:
        identity = self.one()
        elements = set((identity,))
        frontier = [identity]
        steps = 0
        assert self._group_generators is not None
        while frontier:
            current = frontier.pop()
            for generator in self._group_generators:
                for factor in (generator, generator.inverse()):
                    candidate = current * factor
                    if candidate in elements:
                        continue
                    elements.add(candidate)
                    frontier.append(candidate)
                    steps += 1
                    assert steps <= 100000, (
                        "the proposed subgroup has not closed after 100000 elements"
                    )
        return tuple(elements)

    def _repr_(self) -> str:
        if self.is_finite():
            return f"Subgroup of Aut({self.module()}) of order {self.order()}"
        return f"Aut({self.module()})"


class GroupActionHomset(Homset):
    r"""Homomorphisms from a group to the automorphisms of one module."""

    def __init__(self, group: "Group", module: "Module") -> None:
        self._module = module
        Homset.__init__(
            self,
            group,
            module.Aut(),
            category=Groups(),
            check=False,
        )

    def module(self) -> "Module":
        return self._module

    def _element_constructor_(self, images: "OrderedSet | dict") -> "GroupAction":
        r"""Return the \(\rho:G\to\operatorname{Aut}_R(M)\) that ``images`` names.

        A homomorphism out of \(G\) is named either by its values on all of
        \(G\) -- a dictionary, which is what a transported action has to hand
        -- or by the images of the distinguished generators, which is how a
        caller names one.  The second is the presentation route: the images
        determine \(\rho\) if and only if they satisfy the relations of
        \(G\), and that is what :meth:`_values_on_generators` decides.

        Naming \(\rho\) is the business of the category of groups and of this
        homset in it.  A module is equipped with an action already
        constructed; it does not build one.
        """
        match images:
            case dict():
                return GroupAction(self, images)
            case _:
                return GroupAction(self, self._values_on_generators(tuple(images)))

    def _values_on_generators(self, images: "OrderedSet") -> dict:
        r"""Extend generator images over \(G\), refusing a broken relation.

        The extension is the closure of the assignment over the Cayley graph
        of \(G\) on its distinguished generators: every element is reached as
        a word, and its image is the corresponding word in the automorphisms.
        A relation of \(G\) is a pair of words meeting at one element, so a
        second arrival at an element already reached is exactly a relation,
        and the images satisfy it precisely when the two words agree.
        Checking every such meeting is checking every relation, which is the
        whole content of "\(\rho\) is a homomorphism"; no presentation has to
        be supplied, because the group states its own generators.
        """
        group = self.domain()
        automorphisms = self.codomain()
        generators = tuple(group.group_generators())
        assert len(images) == len(generators), (
            f"{group} has {len(generators)} generators, got {len(images)} images"
        )
        assert all(image.parent() is automorphisms for image in images), (
            "the generator images must belong to the automorphism group of this homset"
        )
        values = {group.one(): automorphisms.one()}
        frontier = [group.one()]
        while frontier:
            current = frontier.pop()
            for generator, image in zip(generators, images, strict=True):
                product = current * generator
                candidate = values[current] * image
                match product in values:
                    case True:
                        assert values[product] == candidate, (
                            "the images do not respect the relations of the group"
                        )
                    case False:
                        values[product] = candidate
                        frontier.append(product)
        return values

    def __contains__(self, action: "GroupAction") -> bool:
        return (
            isinstance(action, GroupAction)
            and action.parent() is self
        )


def group_action_homset(group: "Group", module: "Module") -> GroupActionHomset:
    r"""Return the canonical homset \(G\to\operatorname{Aut}_R(M)\).

    Keyed by identity: distinct literal subgroups of one automorphism
    group share ``Homset`` equality (domain, codomain, category), so a
    content-keyed cache would hand one subgroup's homset to another.
    """
    cache = module.__dict__.setdefault("_group_action_homsets", {})
    homset = cache.get(id(group))
    if homset is None:
        homset = GroupActionHomset(group, module)
        cache[id(group)] = homset
    return homset


class GroupAction(Morphism):
    r"""A homomorphism \(G\to\operatorname{Aut}_R(M)\)."""

    def __init__(self, parent: GroupActionHomset, values: dict) -> None:
        Morphism.__init__(self, parent)
        group = parent.domain()
        automorphisms = parent.codomain()
        assert group.is_finite(), "this constructor requires a finite group"
        assert set(values) == set(group), (
            "the action must name the image of every group element"
        )
        assert all(value.parent() is automorphisms for value in values.values()), (
            "every value must be an element of the stated automorphism homset"
        )
        assert values[group.one()] == automorphisms.one(), (
            "the identity must map to the identity automorphism"
        )
        assert all(
            values[left * right] == values[left] * values[right]
            for left in group
            for right in group
        ), "the supplied function is not a group homomorphism"
        self._values = dict(values)

    def module(self) -> "Module":
        return self.parent().module()

    def _call_(self, element: "Element") -> ModuleAutomorphism:
        assert element in self._values, (
            f"{element} is not an element of this action's group"
        )
        return self._values[element]

    def values(self) -> dict:
        return dict(self._values)

    def __eq__(self, other: object) -> bool:
        r"""Return whether these are the same homomorphism.

        Two homomorphisms out of one group into one \(\operatorname{Aut}\)
        agree exactly when they agree at every element, and the values are
        what record that.  Sage's generic morphism comparison declines to
        answer for these and raises, so without this a group module could not
        be compared -- its identity is the pair \((M,\rho)\), and one half of
        the pair was unaskable.
        """
        return (
            type(other) is type(self)
            and self.domain() == other.domain()
            and self.module() == other.module()
            and self._values == other._values
        )

    def __hash__(self) -> int:
        # The values are automorphisms, which need not be hashable, so the
        # hash uses the coarser invariant the homset names and equality does
        # the exact comparison.  Two actions of one group on one module
        # collide, which is legal.
        return hash((type(self), self.domain(), self.module()))


def _solve_left_integrally(system: MorphismMatrix, target: "Vector") -> "Vector":
    r"""Return an integral solution of \(aS=t\), or fail.

    The caller hands over a morphism matrix -- the matrix of the morphism
    being lifted along, stacked with the codomain's relations -- and the
    coordinate vector of the element to hit, not the module it lies in.
    """
    smith, left, right = system.transpose().smith_form()
    shifted = left * vector(SageZZ, target)
    width = smith.ncols()
    solution = [0] * width
    for index, value in enumerate(shifted):
        divisor = smith[index, index] if index < width else 0
        assert divisor != 0 or value == 0, (
            f"no solution: row {index} is zero but asks for {value}"
        )
        if divisor != 0:
            assert value % divisor == 0, (
                f"no integral solution: row {index} asks for {value}/{divisor}"
            )
            solution[index] = value // divisor
    return right * vector(SageZZ, solution)
