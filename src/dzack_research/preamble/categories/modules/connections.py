r"""Algebraic connections on represented modules over commutative algebras."""

from sage.categories.category_types import Category_over_base
from sage.categories.homset import Homset
from sage.categories.modules import Modules as SageModules
from sage.categories.sets_cat import Sets
from sage.structure.element import Element
from sage.structure.parent import Parent

from dzack_research.preamble.categories.algebras import (
    CommutativeAlgebras,
    KahlerDifferentials,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.powers import (
    AlternatingPower,
    alternating_power_product,
)
from dzack_research.preamble.categories.rings import engine_ring
from dzack_research.preamble.refine import refine


class ModulesWithConnection(Category_over_base):
    r"""Modules over ``A`` equipped with an ``A/R``-connection."""

    @classmethod
    def _repr_object_names(cls):
        return "modules with connection"

    def algebra(self):
        return self.base()

    def super_categories(self):
        from dzack_research.preamble.categories.modules import Modules

        return [Modules(self.algebra())]

    class ParentMethods:
        def connection(self):
            return self._preamble_connection

        def _Hom_(self, codomain, category=None):
            if codomain in ModulesWithConnection(self.base_ring()):
                return connection_homset(self, codomain)
            return module_homset(self, codomain)

        def hom(self, images, codomain=None):
            if codomain is None:
                raise TypeError("the target module with connection is required")
            if codomain in ModulesWithConnection(self.base_ring()):
                return connection_homset(self, codomain)(images)
            return module_homset(self, codomain)(images)


class ModulesWithFlatConnection(Category_over_base):
    r"""Modules whose selected connection has zero curvature."""

    @classmethod
    def _repr_object_names(cls):
        return "modules with flat connection"

    def algebra(self):
        return self.base()

    def super_categories(self):
        return [ModulesWithConnection(self.algebra())]

    class ParentMethods:
        def is_flat_connection(self) -> bool:
            return True


class Connection(Element):
    r"""An ``R``-connection ``E -> E tensor_A Omega^1_{A/R}``."""

    def __init__(self, parent, generator_images) -> None:
        Element.__init__(self, parent)
        labels = tuple(self.module().module_generating_set())
        if isinstance(generator_images, dict):
            missing = [label for label in labels if label not in generator_images]
            if missing:
                raise ValueError(f"connection assignment omits {missing}")
            images = generator_images
        elif callable(generator_images):
            images = {label: generator_images(label) for label in labels}
        else:
            values = tuple(generator_images)
            if len(values) != len(labels):
                raise ValueError("a connection needs one image for each module generator")
            images = dict(zip(labels, values, strict=True))
        target = self.target_module()
        self._generator_images = {
            label: image if image.parent() is target else target(image)
            for label, image in images.items()
        }
        self._check_relations()

    def module(self):
        return self.parent().module()

    def algebra(self):
        return self.parent().algebra()

    def one_forms(self):
        return self.parent().one_forms()

    def target_module(self):
        return self.parent().target_module()

    def generator_image(self, label):
        return self._generator_images[label]

    def _from_coefficients(self, coefficients):
        target = self.target_module()
        universal = self.one_forms().universal_derivation()
        result = target.zero()
        for label, coefficient in coefficients.items():
            if not coefficient:
                continue
            result += target.scalar_multiple(
                coefficient,
                self.generator_image(label),
            )
            d_coefficient = universal(self.algebra()(coefficient))
            if d_coefficient != self.one_forms().zero():
                result += target.pure_tensor(
                    self.module().module_generator(label),
                    d_coefficient,
                )
        return result

    def _check_relations(self) -> None:
        from dzack_research.preamble.categories.modules import (
            ModulesWithChosenFinitePresentation,
        )

        module = self.module()
        if module not in ModulesWithChosenFinitePresentation(self.algebra()):
            return
        labels = tuple(module.module_generating_set())
        for row in module.presentation_matrix().rows():
            value = self._from_coefficients(
                {
                    label: coefficient
                    for label, coefficient in zip(labels, row, strict=True)
                    if coefficient
                }
            )
            if value != self.target_module().zero():
                raise ValueError(
                    "the proposed connection does not descend through a module relation"
                )

    def __call__(self, element):
        if element.parent() is not self.module():
            element = self.module()(element)
        return self._from_coefficients(module_coefficients(element, self.module()))

    def curvature_target(self):
        from dzack_research.preamble.categories.abstract_categories import TensorProduct

        return TensorProduct(self.module(), AlternatingPower(self.one_forms(), 2))

    def _wedge_connection_value(self, value, one_form):
        omega = self.one_forms()
        omega_two = AlternatingPower(omega, 2)
        target_two = self.curvature_target()
        result = target_two.zero()
        for (module_label, form_label), coefficient in module_coefficients(
            value,
            self.target_module(),
        ).items():
            wedge = alternating_power_product(
                omega,
                1,
                omega.module_generator(form_label),
                1,
                one_form,
            )
            if wedge != omega_two.zero():
                result += target_two.scalar_multiple(
                    coefficient,
                    target_two.pure_tensor(
                        self.module().module_generator(module_label),
                        wedge,
                    ),
                )
        return result

    def curvature_on_generator(self, label):
        omega = self.one_forms()
        omega_two = AlternatingPower(omega, 2)
        target_two = self.curvature_target()
        universal = omega.universal_derivation()
        result = target_two.zero()
        for (module_label, form_label), coefficient in module_coefficients(
            self.generator_image(label),
            self.target_module(),
        ).items():
            one_form = omega.module_generator(form_label)
            result += target_two.scalar_multiple(
                coefficient,
                self._wedge_connection_value(
                    self.generator_image(module_label),
                    one_form,
                ),
            )
            d_coefficient = universal(self.algebra()(coefficient))
            if d_coefficient != omega.zero():
                wedge = alternating_power_product(
                    omega,
                    1,
                    d_coefficient,
                    1,
                    one_form,
                )
                if wedge != omega_two.zero():
                    result += target_two.pure_tensor(
                        self.module().module_generator(module_label),
                        wedge,
                    )
        return result

    def is_flat(self) -> bool:
        zero = self.curvature_target().zero()
        return all(
            self.curvature_on_generator(label) == zero
            for label in self.module().module_generating_set()
        )

    def de_rham_module(self):
        r"""Return the DG-module de Rham complex attached to this flat connection."""
        return ConnectionDeRhamModule(self)


class ConnectionSpace(Parent):
    Element = Connection

    def __init__(self, module) -> None:
        algebra = module.base_ring()
        if algebra not in CommutativeAlgebras(algebra.base_ring()):
            raise TypeError(
                "an algebraic connection here requires a module over a commutative algebra"
            )
        self._module = module
        self._algebra = algebra
        self._one_forms = KahlerDifferentials(algebra)
        from dzack_research.preamble.categories.abstract_categories import TensorProduct

        self._target_module = TensorProduct(module, self._one_forms)
        Parent.__init__(self, category=Sets())

    def module(self):
        return self._module

    def algebra(self):
        return self._algebra

    def one_forms(self):
        return self._one_forms

    def target_module(self):
        return self._target_module

    def _element_constructor_(self, generator_images):
        if isinstance(generator_images, Connection) and generator_images.parent() is self:
            return generator_images
        return self.element_class(self, generator_images)

    def _repr_(self):
        return f"Connections on {self.module()} over {self.algebra().base_ring()}"


_CONNECTION_SPACES = {}


def Connections(module) -> ConnectionSpace:
    cached = _CONNECTION_SPACES.get(id(module))
    if cached is not None and cached.module() is module:
        return cached
    result = ConnectionSpace(module)
    _CONNECTION_SPACES[id(module)] = result
    return result


class ConnectionMorphism(ModuleMorphism):
    r"""An ``A``-linear map horizontal for the selected connections."""

    def __init__(self, parent, images) -> None:
        ModuleMorphism.__init__(self, parent, images)
        self._check_connection_square()

    def _check_connection_square(self) -> None:
        domain_connection = self.domain().connection()
        codomain_connection = self.codomain().connection()
        if domain_connection.algebra() is not codomain_connection.algebra():
            raise ValueError("horizontal morphisms require one coefficient algebra")
        omega = domain_connection.one_forms()
        identity_omega = module_homset(omega, omega).identity()
        from dzack_research.preamble.categories.modules.tensor_products import (
            tensor_product_morphism,
        )

        induced = tensor_product_morphism(
            self,
            identity_omega,
            source=domain_connection.target_module(),
            target=codomain_connection.target_module(),
        )
        for label in self.domain().module_generating_set():
            generator = self.domain().module_generator(label)
            if codomain_connection(self(generator)) != induced(domain_connection(generator)):
                raise ValueError(
                    "the module map is not horizontal for the selected connections"
                )


class ConnectionHomset(Homset):
    Element = ConnectionMorphism

    def __init__(self, domain, codomain) -> None:
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("connection morphisms require one coefficient algebra")
        Homset.__init__(
            self,
            domain,
            codomain,
            category=SageModules(engine_ring(domain.base_ring())),
        )

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a connection endomorphism homset")
        return self(
            {
                label: self.domain().module_generator(label)
                for label in self.domain().module_generating_set()
            }
        )


def connection_homset(domain, codomain):
    return ConnectionHomset(domain, codomain)


def ModuleWithConnection(connection):
    r"""Return a fresh finite-free module carrying the selected connection."""
    from dzack_research.preamble.categories.modules import FinitelyGeneratedFreeModules
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FreshFreeModuleOn,
    )

    source = connection.module()
    algebra = connection.algebra()
    if source not in FinitelyGeneratedFreeModules(algebra):
        raise NotImplementedError(
            "the live structured connection carrier is currently materialized for finite free modules"
        )
    result = FreshFreeModuleOn(algebra, source.module_generating_set())
    transported_target = Connections(result).target_module()
    omega = connection.one_forms()
    transported_images = {}
    for label in source.module_generating_set():
        image = transported_target.zero()
        for (source_label, form_label), coefficient in module_coefficients(
            connection.generator_image(label),
            connection.target_module(),
        ).items():
            image += transported_target.scalar_multiple(
                coefficient,
                transported_target.pure_tensor(
                    result.module_generator(source_label),
                    omega.module_generator(form_label),
                ),
            )
        transported_images[label] = image
    result._preamble_connection = Connections(result)(transported_images)
    categories = [ModulesWithConnection(algebra)]
    if result._preamble_connection.is_flat():
        categories.append(ModulesWithFlatConnection(algebra))
    return refine(result, categories)


class ConnectionDeRhamDifferential:
    r"""The covariant differential on ``E tensor_A Omega^*_{A/R}``."""

    def __init__(self, module) -> None:
        self._module = module

    def module(self):
        return self._module

    def degree_shift(self):
        return 1

    def __call__(self, element):
        module = self.module()
        element = module(element)
        return module.from_components(
            {
                degree + 1: module._differentiate_component(degree, component)
                for degree, component in element.homogeneous_components().items()
            }
        )


class ConnectionDeRhamModule:
    r"""Factory namespace for a flat connection's de Rham DG-module."""

    def __new__(cls, connection):
        if not connection.is_flat():
            raise ValueError("a DG-module de Rham differential requires a flat connection")

        from dzack_research.preamble.categories.abstract_categories import TensorProduct
        from dzack_research.preamble.categories.algebras import (
            DeRhamAlgebra,
            DifferentialComponentMorphism,
        )
        from dzack_research.preamble.categories.modules import (
            DifferentialGradedModules,
            restrict_scalars,
        )
        from dzack_research.preamble.categories.modules.graded_direct_sums import (
            GradedDirectSumModule,
        )

        coefficient_module = connection.module()
        algebra = connection.algebra()
        omega = connection.one_forms()
        dga = DeRhamAlgebra(algebra)
        ring_map = algebra.algebra_structure_morphism()

        class _ConnectionDeRhamModule(GradedDirectSumModule):
            def __init__(self) -> None:
                self._connection = connection
                self._coefficient_module = coefficient_module
                self._omega = omega
                self._dga = dga

                def piece(degree):
                    forms = AlternatingPower(omega, degree)
                    return restrict_scalars(
                        TensorProduct(coefficient_module, forms),
                        ring_map,
                    )

                GradedDirectSumModule.__init__(
                    self,
                    algebra.base_ring(),
                    piece,
                    name=f"de Rham DG-module of {coefficient_module}",
                )
                self._preamble_graded_algebra = dga
                self._preamble_dg_algebra = dga
                self._preamble_graded_algebra_action = self._right_action
                self._preamble_differential = ConnectionDeRhamDifferential(self)
                refine(self, DifferentialGradedModules(dga))

            def connection(self):
                return self._connection

            def coefficient_module(self):
                return self._coefficient_module

            def from_coefficient(self, element):
                forms_zero = AlternatingPower(self._omega, 0)
                tensor_zero = TensorProduct(self._coefficient_module, forms_zero)
                unit = forms_zero.module_generator(0)
                return self.from_component(
                    0,
                    self.graded_piece(0)(tensor_zero.pure_tensor(element, unit)),
                )

            def _underlying_component(self, component):
                return (
                    component.underlying_element()
                    if hasattr(component, "underlying_element")
                    else component
                )

            def _differentiate_component(self, degree, component):
                source_forms = AlternatingPower(self._omega, degree)
                target_forms = AlternatingPower(self._omega, degree + 1)
                source_tensor = TensorProduct(self._coefficient_module, source_forms)
                target_tensor = TensorProduct(self._coefficient_module, target_forms)
                result = target_tensor.zero()
                underlying = self._underlying_component(component)
                for (module_label, form_label), coefficient in module_coefficients(
                    underlying,
                    source_tensor,
                ).items():
                    coefficient_vector = self._coefficient_module.scalar_multiple(
                        coefficient,
                        self._coefficient_module.module_generator(module_label),
                    )
                    connection_value = self._connection(coefficient_vector)
                    basis_form = source_forms.module_generator(form_label)
                    for (
                        output_module_label,
                        one_form_label,
                    ), connection_coefficient in module_coefficients(
                        connection_value,
                        self._connection.target_module(),
                    ).items():
                        wedge = alternating_power_product(
                            self._omega,
                            1,
                            self._omega.module_generator(one_form_label),
                            degree,
                            basis_form,
                        )
                        if wedge != target_forms.zero():
                            result += target_tensor.scalar_multiple(
                                connection_coefficient,
                                target_tensor.pure_tensor(
                                    self._coefficient_module.module_generator(
                                        output_module_label
                                    ),
                                    wedge,
                                ),
                            )
                return self.graded_piece(degree + 1)(result)

            def differential_component(self, degree):
                degree = int(degree)
                source = self.graded_piece(degree)
                target = self.graded_piece(degree + 1)
                return DifferentialComponentMorphism(
                    source,
                    target,
                    lambda component: self._differentiate_component(degree, component),
                )

            def _right_action(self, module_element, algebra_element):
                module_element = self(module_element)
                algebra_element = self._dga(algebra_element)
                exterior_element = self._dga.realize(algebra_element)
                exterior_algebra = self._dga.extension_algebra()
                result = self.zero()
                for left_degree, left_component in module_element.homogeneous_components().items():
                    left_forms = AlternatingPower(self._omega, left_degree)
                    left_tensor = TensorProduct(self._coefficient_module, left_forms)
                    left_underlying = self._underlying_component(left_component)
                    for right_degree, right_component in exterior_element.homogeneous_components().items():
                        target_degree = left_degree + right_degree
                        target_forms = AlternatingPower(self._omega, target_degree)
                        target_tensor = TensorProduct(
                            self._coefficient_module,
                            target_forms,
                        )
                        target_value = target_tensor.zero()
                        for (
                            module_label,
                            left_form_label,
                        ), left_coefficient in module_coefficients(
                            left_underlying,
                            left_tensor,
                        ).items():
                            left_form = left_forms.module_generator(left_form_label)
                            for right_form_label, right_coefficient in module_coefficients(
                                right_component,
                                exterior_algebra.graded_piece(right_degree),
                            ).items():
                                right_form = exterior_algebra.graded_piece(
                                    right_degree
                                ).module_generator(right_form_label)
                                wedge = alternating_power_product(
                                    self._omega,
                                    left_degree,
                                    left_form,
                                    right_degree,
                                    right_form,
                                )
                                if wedge != target_forms.zero():
                                    target_value += target_tensor.scalar_multiple(
                                        left_coefficient * right_coefficient,
                                        target_tensor.pure_tensor(
                                            self._coefficient_module.module_generator(
                                                module_label
                                            ),
                                            wedge,
                                        ),
                                    )
                        if target_value != target_tensor.zero():
                            result += self.from_component(
                                target_degree,
                                self.graded_piece(target_degree)(target_value),
                            )
                return result

        return _ConnectionDeRhamModule()


__all__ = [
    "Connection",
    "ConnectionDeRhamDifferential",
    "ConnectionDeRhamModule",
    "ConnectionHomset",
    "ConnectionMorphism",
    "ConnectionSpace",
    "Connections",
    "ModuleWithConnection",
    "ModulesWithConnection",
    "ModulesWithFlatConnection",
    "connection_homset",
]
