"""Associative unital algebras over an owned base ring."""

from sage.categories.algebras import Algebras as SageAlgebras
from sage.categories.associative_algebras import (
    AssociativeAlgebras as SageAssociativeAlgebras,
)
from sage.categories.commutative_algebras import (
    CommutativeAlgebras as SageCommutativeAlgebras,
)
from sage.categories.homset import Hom, Homset
from sage.categories.morphism import SetMorphism
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.categories.rings import Rings as SageRings
from sage.categories.sets_cat import Sets
from sage.misc.cachefunc import cached_function, cached_method

from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    OwnedRingView,
    OwnedRings,
    engine_ring,
    owned_ring_view,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.refine import refine


class AssociativeAlgebras(OwnedCategoryOverBaseRing):
    r"""Associative \(R\)-algebras, not necessarily unital.

    An associative algebra is an \(R\)-module with an associative bilinear
    product. A unit is extra structure: the owned unital category is
    :class:`Algebras`. Convolution \(L^1(\mathbb R)\) is the standard
    non-unital example.
    """

    @classmethod
    def _repr_object_names(cls):
        return "associative algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [
            SageAssociativeAlgebras(engine_ring(self.base_ring())),
            Modules(self.base_ring()),
        ]

    def _call_(self, multiplication):
        return algebra_from_multiplication(
            multiplication, self.base_ring(), unital=False
        )


class AssociativeAlgebrasWithChosenMultiplication(OwnedCategoryOverBaseRing):
    r"""Associative algebras interned on a chosen morphism \(A\otimes_R A\to A\)."""

    @classmethod
    def _repr_object_names(cls):
        return "associative algebras with chosen multiplication"

    def super_categories(self):
        return [AssociativeAlgebras(self.base_ring())]

    class ParentMethods:
        def multiplication_morphism(self):
            return self._preamble_multiplication_morphism

    class ElementMethods:
        def _mul_(self, other):
            multiplication = self.parent().multiplication_morphism()
            return multiplication(multiplication.domain().pure_tensor(self, other))


class AlgebraHomCategoryConstruction(HomCategoryConstruction):
    r"""The fixed-endpoint Hom categories of associative unital ``R``-algebras."""

    def Of(self, domain, codomain):
        if domain not in self.base_category() or codomain not in self.base_category():
            raise TypeError("algebra Hom endpoints must lie in the base algebra category")
        key = id(domain), id(codomain)
        cached = self._objects.get(key)
        if (
            cached is not None
            and cached.domain_object() is domain
            and cached.codomain_object() is codomain
        ):
            return cached

        from dzack_research.preamble.categories.algebras.sparse_free_algebras import (
            FramedFreeAlgebraHomset,
            SparseFreeAlgebra,
            SparseFreeAlgebraHomset,
        )

        if isinstance(domain, SparseFreeAlgebra):
            hom_class = SparseFreeAlgebraHomset
        elif isinstance(codomain, SparseFreeAlgebra):
            from dzack_research.preamble.categories.algebras.free_algebras import (
                SymmetricAlgebras,
                TensorAlgebras,
            )

            ring = domain.base_ring()
            hom_class = (
                FramedFreeAlgebraHomset
                if domain in TensorAlgebras(ring) or domain in SymmetricAlgebras(ring)
                else AlgebraHomset
            )
        else:
            hom_class = AlgebraHomset
        result = hom_class(self, domain, codomain)
        self._objects[key] = result
        return result


class Algebras(OwnedCategoryOverBaseRing):
    r"""Associative unital algebras over ``R``.

    The structure morphism is \(\eta\colon R\to Z(A)\).  The forgetful
    functor \(U\colon\mathbf{Alg}_R\to\mathbf{Mod}_R\) is
    :func:`~dzack_research.preamble.categories.functors.algebra_modules.algebra_underlying_module_functor`.
    Multiplication is the \(R\)-module morphism
    \(m\colon A\otimes_R A\to A\).
    """

    @classmethod
    def _repr_object_names(cls):
        return "algebras"

    def super_categories(self):
        from dzack_research.preamble.categories.modules import Modules

        return [
            SageAlgebras(engine_ring(self.base_ring())),
            OwnedRings(),
            AssociativeAlgebras(self.base_ring()),
            Modules(self.base_ring()),
        ]

    def homset(self, domain, codomain):
        r"""Return the unique Hom-set ``Hom_{R-Alg}(domain,codomain)``."""
        if domain not in self or codomain not in self:
            raise TypeError("an R-algebra Hom requires two R-algebras")
        return algebra_homset(domain, codomain)

    _HomCategory = AlgebraHomCategoryConstruction

    class ParentMethods:
        def base_ring(self):
            return self.algebra_base_ring()

        def is_algebra(self) -> bool:
            return True

        def algebra_base_ring(self):
            base = self.__dict__.get("_preamble_algebra_base_ring")
            if base is not None:
                return base
            return owned_ring_view(engine_ring(self).base_ring())

        @cached_method
        def _ring_morphism_defining_algebra_structure(self):
            base = self.algebra_base_ring()
            center = self.ring_center()
            return SetMorphism(
                Hom(base, center, SageRings()),
                lambda scalar: self(engine_ring(base)(scalar)),
            )

        @cached_method
        def algebra_structure_morphism(self):
            r"""The structure morphism \(\eta\colon R\to Z(A)\) of this \(R\)-algebra."""
            eta = self._ring_morphism_defining_algebra_structure()
            center = self.ring_center()
            if eta.codomain() is center:
                return eta
            return SetMorphism(Hom(eta.domain(), center, SageRings()), eta)

        @cached_method
        def multiplication_morphism(self):
            r"""The multiplication \(m\colon A\otimes_R A\to A\) as an \(R\)-module morphism.

            Centrality of the image of \(R\) is exactly \(R\)-bilinearity of
            the product, so \(m\) is the unique factorization of
            \((a,b)\mapsto ab\) through the tensor product.
            """
            selected = self.__dict__.get("_preamble_multiplication_morphism")
            if selected is not None:
                return selected
            from dzack_research.preamble.categories.functors.algebra_modules import (
                algebra_underlying_module_functor,
            )
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
                FinitelyGeneratedFreeModules,
            )
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
                ModulesWithChosenFinitePresentation,
            )
            from dzack_research.preamble.categories.abstract_categories import (
                TensorProduct,
            )
            from dzack_research.preamble.categories.modules.tensor_products import (
                BilinearMap,
            )

            ring = self.algebra_base_ring()
            module = algebra_underlying_module_functor(ring)(self)
            if module not in ModulesWithChosenFinitePresentation(
                ring
            ) and module not in FinitelyGeneratedFreeModules(ring):
                raise TypeError(
                    f"the multiplication morphism of {self} factors through "
                    f"a tensor product of finitely presented {ring}-modules"
                )
            tensor = TensorProduct(module, module)
            return tensor.from_bilinear(
                BilinearMap(
                    module,
                    module,
                    module,
                    {
                        (left, right): (
                            module.module_generator(left)
                            * module.module_generator(right)
                        )
                        for left in module.module_generating_set()
                        for right in module.module_generating_set()
                    },
                )
            )

        def _Hom_(self, codomain, category=None):
            if category is not None and not category.is_subcategory(
                SageAlgebras(engine_ring(self.base_ring()))
            ):
                raise TypeError("this is not an algebra homset category")
            return algebra_homset(self, codomain)

        def hom(self, images, codomain=None):
            if codomain is None:
                if isinstance(images, dict) and images:
                    codomain = next(iter(images.values())).parent()
                elif isinstance(images, (tuple, list)) and images:
                    codomain = images[0].parent()
                else:
                    raise TypeError(
                        "the codomain is required when it cannot be read from images"
                    )
            return algebra_homset(self, codomain)(images)

    def _call_(self, multiplication):
        return algebra_from_multiplication(
            multiplication, self.base_ring(), unital=True
        )


class AlgebrasWithChosenMultiplication(OwnedCategoryOverBaseRing):
    r"""Unital algebras interned on a chosen morphism \(A\otimes_R A\to A\)."""

    @classmethod
    def _repr_object_names(cls):
        return "algebras with chosen multiplication"

    def super_categories(self):
        return [
            AssociativeAlgebrasWithChosenMultiplication(self.base_ring()),
            Algebras(self.base_ring()),
        ]

    class ParentMethods:
        def one(self):
            return self._preamble_algebra_unit

        def multiplication_morphism(self):
            return self._preamble_multiplication_morphism

        def _ring_morphism_defining_algebra_structure(self):
            base = self.algebra_base_ring()
            center = self.ring_center()
            unit = self.one()
            return SetMorphism(
                Hom(base, center, SageRings()),
                lambda scalar: self.scalar_multiple(base(scalar), unit),
            )


class CommutativeAlgebras(OwnedCategoryOverBaseRing):
    r"""Commutative associative unital algebras over ``R``."""

    @classmethod
    def _repr_object_names(cls):
        return "commutative algebras"

    def super_categories(self):
        return [
            Algebras(self.base_ring()),
            SageCommutativeAlgebras(engine_ring(self.base_ring())),
        ]

    class ParentMethods:
        def is_commutative(self) -> bool:
            return True


class FramedAlgebras(OwnedCategoryOverBaseRing):
    r"""Algebras carrying a chosen finite algebra generating set."""

    @classmethod
    def _repr_object_names(cls):
        return "framed algebras"

    def super_categories(self):
        return [Algebras(self.base_ring())]

    class ParentMethods:
        def algebra_generating_set(self):
            return self._preamble_algebra_generating_set

        @cached_method
        def algebra_generators(self):
            return finite_ordered_set(
                self.algebra_generator(label) for label in self.algebra_generating_set()
            )

        def algebra_generator(self, label):
            labels = self.algebra_generating_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not an algebra-generator label")
            return self._preamble_algebra_generator_values[label]

        def number_of_algebra_generators(self):
            return self.algebra_generating_set().cardinality()

        def product_on_algebra_generators(self, left, right):
            return self.algebra_generator(left) * self.algebra_generator(right)


class AlgebraMorphism(Morphism):
    r"""An ``R``-algebra morphism specified by the images of algebra generators."""

    def __init__(self, parent, images) -> None:
        Morphism.__init__(self, parent)
        domain = self.domain()
        codomain = self.codomain()
        engine_domain = engine_ring(domain)
        engine_codomain = engine_ring(codomain)
        framed_domain = domain in FramedAlgebras(domain.base_ring())
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            ModuleMorphism,
        )

        if isinstance(images, ModuleMorphism):
            if images.domain() is not domain or images.codomain() is not codomain:
                raise ValueError(
                    "an adopted module morphism must have the owned algebra homset's "
                    "exact domain and codomain"
                )
            from sage.rings.infinity import Infinity

            labels = domain.module_generating_set()
            if labels.cardinality() == Infinity:
                raise NotImplementedError(
                    "verification that a module morphism is multiplicative currently "
                    "requires a finite module generating set"
                )
            if images(domain.one()) != codomain.one():
                raise ValueError("an algebra morphism must preserve the unit")
            labels = tuple(labels)
            for left_label in labels:
                left = domain.module_generator(left_label)
                for right_label in labels:
                    right = domain.module_generator(right_label)
                    if images(left * right) != images(left) * images(right):
                        raise ValueError(
                            "the adopted module morphism is not multiplicative on "
                            "the selected module generators"
                        )
            self._engine_morphism = SetMorphism(
                Hom(engine_domain, engine_codomain, SageRings()),
                lambda element: engine_codomain(images(domain(element))),
            )
            if framed_domain:
                algebra_labels = tuple(domain.algebra_generating_set())
                self._generator_images = {
                    label: engine_codomain(images(domain.algebra_generator(label)))
                    for label in algebra_labels
                }
            else:
                self._generator_images = None
            return
        if isinstance(images, Map):
            if (
                images.domain() is not engine_domain
                or images.codomain() is not engine_codomain
            ):
                raise ValueError(
                    "an adopted engine algebra morphism must have the owned homset's engine domain and codomain"
                )
            self._engine_morphism = images
            if framed_domain:
                labels = tuple(domain.algebra_generating_set())
                self._generator_images = {
                    label: engine_codomain(
                        images(engine_domain(domain.algebra_generator(label)))
                    )
                    for label in labels
                }
            else:
                self._generator_images = None
            return
        if not framed_domain:
            raise NotImplementedError(
                "an algebra morphism from an unframed domain must be supplied "
                "as an exact engine ring morphism"
            )
        labels = tuple(domain.algebra_generating_set())
        if isinstance(images, dict):
            missing = [label for label in labels if label not in images]
            if missing:
                raise ValueError(f"algebra-generator assignment omits {missing}")
            generator_images = tuple(images[label] for label in labels)
        elif isinstance(images, (tuple, list)):
            generator_images = tuple(images)
            if len(generator_images) != len(labels):
                raise ValueError(
                    "the number of algebra-generator images must equal the framing size"
                )
        elif callable(images):
            generator_images = tuple(images(label) for label in labels)
        else:
            raise TypeError(
                "an algebra morphism is specified on the algebra generating set"
            )
        self._generator_images = dict(zip(labels, generator_images, strict=True))

        engine_base = engine_ring(domain.base_ring())
        target_structure = codomain._ring_morphism_defining_algebra_structure()
        base_map = SetMorphism(
            Hom(engine_base, engine_codomain, SageRings()),
            lambda scalar: engine_codomain(
                target_structure(domain.base_ring()(scalar))
            ),
        )
        from dzack_research.preamble.categories.algebras.restricted_scalars import (
            RestrictedScalarsAlgebras,
        )

        if domain in RestrictedScalarsAlgebras(domain.base_ring()):
            scalar_labels = tuple(domain.restricted_scalar_generator_labels())
            algebra_labels = tuple(domain.restricted_algebra_generator_labels())
            extension_engine = engine_ring(domain.extension_ring())
            extension_map = extension_engine.hom(
                [
                    engine_codomain(self._generator_images[("scalar", label)])
                    for label in scalar_labels
                ],
                engine_codomain,
                base_map=base_map,
            )
            self._engine_morphism = engine_domain.hom(
                [
                    engine_codomain(self._generator_images[("algebra", label)])
                    for label in algebra_labels
                ],
                engine_codomain,
                base_map=extension_map,
            )
            return
        self._engine_morphism = engine_domain.hom(
            [engine_codomain(image) for image in generator_images],
            engine_codomain,
            base_map=base_map,
        )

    def __call__(self, element):
        r"""Apply this owned algebra morphism to an engine-backed facade element."""
        return self._call_(element)

    def _call_(self, element):
        r"""Apply the algebra map across the owned/native facade boundary.

        Owned algebra parents are facades over Sage's concrete algebra
        parents, so their elements retain the engine parent.  The defining
        engine homomorphism already has exactly the required source and target;
        no engine-to-facade coercion is part of the algebra map.
        """
        source = engine_ring(self.domain())
        target = engine_ring(self.codomain())
        return target(self._engine_morphism(source(element)))

    def engine_morphism(self):
        r"""Return the exact computation-ring morphism represented here."""
        return self._engine_morphism

    def algebra_generator_morphism(self):
        if self._generator_images is None:
            raise NotImplementedError(
                "an unframed algebra domain has no selected generator morphism"
            )
        return SetMorphism(
            Hom(self.domain().algebra_generating_set(), self.codomain(), Sets()),
            self._generator_images.__getitem__,
        )

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        if not isinstance(other, AlgebraMorphism):
            from dzack_research.preamble.categories.algebras.sparse_free_algebras import (
                compose_with_free_construction,
            )

            return compose_with_free_construction(self, other)
        composed_engine = self._engine_morphism * other._engine_morphism
        return algebra_homset(other.domain(), self.codomain())(composed_engine)


class AlgebraHomset(CategoricalHomset):
    Element = AlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("algebra morphisms require one common base ring")
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
            homset_category=Sets(),
        )

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism homset")
        return self(lambda label: self.domain().algebra_generator(label))

    def _repr_(self):
        return f"Hom_Alg({self.domain()}, {self.codomain()})"


def algebra_homset(domain, codomain) -> AlgebraHomset:
    ring = domain.base_ring()
    if codomain.base_ring() is not ring:
        raise ValueError("algebra morphisms require one common base ring")
    return Algebras(ring).Hom(domain, codomain)


class OwnedAlgebras(OwnedCategoryOverBaseRing):
    r"""Algebras carrying their chosen structure map ``R -> Z(A)``."""

    @classmethod
    def _repr_object_names(cls):
        return "owned algebras"

    def super_categories(self):
        return [Algebras(self.base_ring())]

    class ParentMethods:
        def _ring_morphism_defining_algebra_structure(self):
            return self._preamble_structure_map


class OwnedAlgebraView(OwnedRingView):
    r"""One ring read as an algebra through one specified scalar map."""

    def __init__(
        self,
        engine,
        base_ring,
        labels,
        structure_map,
        generator_values=None,
    ) -> None:
        self._preamble_algebra_base_ring = owned_ring_view(base_ring)
        self._preamble_algebra_generating_set = (
            None if labels is None else finite_ordered_set(labels)
        )
        if labels is None:
            if generator_values is not None:
                raise ValueError(
                    "an unframed algebra cannot carry framed generator values"
                )
            self._preamble_algebra_generator_values = None
        else:
            selected_labels = tuple(self._preamble_algebra_generating_set)
            selected_values = (
                tuple(engine.gen(position) for position in range(len(selected_labels)))
                if generator_values is None
                else tuple(generator_values)
            )
            if len(selected_values) != len(selected_labels):
                raise ValueError(
                    "the number of algebra-generator values must equal the framing size"
                )
            self._preamble_algebra_generator_values = dict(
                zip(selected_labels, selected_values, strict=True)
            )
        self._preamble_structure_map = structure_map
        OwnedRingView.__init__(self, engine)


def _default_structure_map(base, algebra):
    center = algebra.ring_center()
    return SetMorphism(
        Hom(base, center, SageRings()),
        lambda scalar: algebra(engine_ring(base)(scalar)),
    )


@cached_function
def _owned_algebra_view(engine, base_ring, labels_tuple=None):
    base = owned_ring_view(base_ring)
    # Construct the parent first with a temporary engine-level map argument;
    # the public map is replaced immediately below once the parent exists.
    engine_map = engine.coerce_map_from(engine_ring(base))
    view = OwnedAlgebraView(engine, base, labels_tuple, engine_map)
    view._preamble_structure_map = _default_structure_map(base, view)
    return view


def refine_algebra(algebra, base_ring, labels=None, *categories):
    r"""Place a native algebra in its owned algebra categories."""
    base = owned_ring_view(base_ring)
    labels_tuple = None if labels is None else tuple(labels)
    algebra = _owned_algebra_view(engine_ring(algebra), base, labels_tuple)
    placement = [Algebras(base), OwnedAlgebras(base)]
    if labels is not None:
        placement.append(FramedAlgebras(base))
    placement.extend(categories)
    return refine(algebra, placement)


def _require_endomorphism_multiplication(multiplication, ring):
    from sage.categories.map import Map

    if not isinstance(multiplication, Map):
        raise TypeError(
            "an algebra is presented by an R-module morphism A tensor_R A -> A"
        )
    module = multiplication.codomain()
    if owned_ring_view(module.base_ring()) is not ring:
        raise TypeError(f"the multiplication morphism is not a map of {ring}-modules")
    domain = multiplication.domain()
    try:
        left, right = domain.tensor_factors()
    except AttributeError as error:
        raise TypeError(
            "the domain of a multiplication morphism is the tensor square of the module"
        ) from error
    if left is not module or right is not module:
        raise TypeError("the multiplication morphism must be a map A tensor_R A -> A")
    return module


def _module_presented_by_multiplication(module):
    from sage.combinat.free_module import CombinatorialFreeModule
    from sage.rings.infinity import Infinity

    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
        FinitelyGeneratedFreeModules,
    )
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModule,
        ModulesWithChosenFinitePresentation,
    )
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        refine_free_module,
    )

    ring = owned_ring_view(module.base_ring())
    labels = module.module_generating_set()
    if labels.cardinality() == Infinity:
        raise TypeError(
            "the multiplication internment requires a finite module generating set"
        )
    if module in FinitelyGeneratedFreeModules(ring):
        presented = CombinatorialFreeModule(engine_ring(ring), labels)
        presented._preamble_module_generating_set = labels
        return refine_free_module(presented, ring)
    if module in ModulesWithChosenFinitePresentation(ring):
        return FinitelyPresentedModule(module.presentation())
    raise TypeError(
        "the multiplication internment requires a finite free or chosen finitely presented module"
    )


def _unit_from_multiplication(multiplication):
    from sage.rings.infinity import Infinity
    from dzack_research.preamble.tensors import tensor
    from dzack_research.preamble.tensors.tensor import (
        _engine_component_matrix,
        _engine_component_vector,
    )

    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_coefficients,
    )

    module = multiplication.codomain()
    tensor_square = multiplication.domain()
    labels = tuple(module.module_generating_set())
    if module.module_generating_set().cardinality() == Infinity:
        raise TypeError("a unit is recovered from a finite module generating set")
    ring = module.base_ring()
    engine = engine_ring(ring)
    rank = int(module.module_generating_set().cardinality())
    system = tensor.matrix(engine, rank * rank, rank)
    target = tensor.vector(engine, rank * rank)
    for right_index, right_label in enumerate(labels):
        target[right_index * rank + right_index] = engine.one()
        for left_index, left_label in enumerate(labels):
            product = multiplication(
                tensor_square.pure_tensor(
                    module.module_generator(left_label),
                    module.module_generator(right_label),
                )
            )
            coefficients = module_coefficients(product, module)
            for out_index, out_label in enumerate(labels):
                system[right_index * rank + out_index, left_index] = engine(
                    coefficients.get(out_label, ring.zero())
                )
    try:
        engine_solution = _engine_component_matrix(system).solve_right(
            _engine_component_vector(target)
        )
        coefficients = tensor.vector(engine, engine_solution)
    except (ValueError, ArithmeticError) as error:
        raise TypeError("the multiplication morphism has no left unit") from error
    unit = module.linear_combination(
        {
            label: ring(coefficients[index])
            for index, label in enumerate(labels)
            if coefficients[index]
        }
    )
    for label in labels:
        generator = module.module_generator(label)
        if multiplication(tensor_square.pure_tensor(generator, unit)) != generator:
            raise TypeError("the multiplication morphism has no two-sided unit")
    return unit


def _multiplication_is_commutative(multiplication) -> bool:
    module = multiplication.codomain()
    tensor = multiplication.domain()
    labels = module.module_generating_set()
    for left in labels:
        for right in labels:
            left_element = module.module_generator(left)
            right_element = module.module_generator(right)
            if multiplication(
                tensor.pure_tensor(left_element, right_element)
            ) != multiplication(tensor.pure_tensor(right_element, left_element)):
                return False
    return True


def algebra_from_multiplication(multiplication, base_ring=None, unital=True):
    r"""Return the algebra presented by an \(R\)-module morphism \(A\otimes_R A\to A\)."""
    from sage.categories.map import Map

    if not isinstance(multiplication, Map):
        # The Lebesgue-graded module backend predates the finite-presentation
        # tensor-product parent and carries its multiplication as its own
        # exact graded morphism object.  Intern it through the maintained
        # graded construction rather than pretending that object is already a
        # ModuleMorphism with a TensorProductModules domain.
        from dzack_research.preamble.categories.functions.lebesgue_graded import (
            intern_graded_lebesgue_algebra,
        )

        ring = owned_ring_view(
            multiplication.codomain().base_ring() if base_ring is None else base_ring
        )
        return intern_graded_lebesgue_algebra(multiplication, ring, unital)

    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )
    from dzack_research.preamble.categories.abstract_categories import TensorProduct
    from dzack_research.preamble.categories.modules.tensor_products import (
        TensorProductModules,
        tensor_product_morphism,
    )

    ring = owned_ring_view(
        multiplication.codomain().base_ring() if base_ring is None else base_ring
    )
    module = _require_endomorphism_multiplication(multiplication, ring)
    if multiplication.domain() not in TensorProductModules(ring):
        from dzack_research.preamble.categories.functions.lebesgue_graded import (
            intern_graded_lebesgue_algebra,
        )

        return intern_graded_lebesgue_algebra(multiplication, ring, unital)
    algebra = _module_presented_by_multiplication(module)
    labels = module.module_generating_set()
    forget = module_homset(algebra, module)(
        {label: module.module_generator(label) for label in labels}
    )
    equip = module_homset(module, algebra)(
        {label: algebra.module_generator(label) for label in labels}
    )
    source_tensor = TensorProduct(algebra, algebra)
    transported = tensor_product_morphism(
        forget,
        forget,
        source=source_tensor,
        target=multiplication.domain(),
    )
    algebra._preamble_multiplication_morphism = equip * multiplication * transported
    algebra._preamble_algebra_base_ring = ring
    placement = [AssociativeAlgebrasWithChosenMultiplication(ring)]
    if unital:
        if module in Algebras(ring):
            unit_source = module.one()
        else:
            unit_source = _unit_from_multiplication(multiplication)
        algebra._preamble_algebra_unit = equip(unit_source)
        placement.extend(
            [
                Algebras(ring),
                AlgebrasWithChosenMultiplication(ring),
            ]
        )
        if _multiplication_is_commutative(multiplication):
            placement.append(CommutativeAlgebras(ring))
    return refine(algebra, placement)


@cached_function
def own_algebra(structure_map):
    r"""Return the algebra object presented by the supplied ring map."""
    if not isinstance(structure_map, Map):
        raise TypeError("an algebra is presented by a ring map")
    base = owned_ring_view(structure_map.domain())
    engine = engine_ring(structure_map.codomain())
    algebra = OwnedAlgebraView(engine, base, None, structure_map)
    return refine(algebra, [Algebras(base), OwnedAlgebras(base)])


def finite_algebra_generators(algebra):
    r"""Return the chosen finite algebra generating family, when represented."""
    if algebra not in FramedAlgebras(algebra.algebra_base_ring()):
        raise NotImplementedError(
            f"{algebra} carries no chosen finite algebra generating set"
        )
    return tuple(algebra.algebra_generators())


__all__ = [
    "AlgebraHomset",
    "AlgebraMorphism",
    "Algebras",
    "AlgebrasWithChosenMultiplication",
    "AssociativeAlgebras",
    "AssociativeAlgebrasWithChosenMultiplication",
    "CommutativeAlgebras",
    "FramedAlgebras",
    "OwnedAlgebraView",
    "OwnedAlgebras",
    "algebra_from_multiplication",
    "algebra_homset",
    "finite_algebra_generators",
    "own_algebra",
    "refine_algebra",
]
