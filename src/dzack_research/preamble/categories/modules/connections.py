r"""Algebraic connections on represented modules over commutative algebras."""

from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.structure.element import Element

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    _RestrictedHomCategoryOf,
    RestrictedHomCategoryParent,
    _category_homset,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.algebras.differential_graded_algebras import DifferentialComponentMorphism
from dzack_research.preamble.categories.modules.dg_modules import DifferentialGradedModules
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import _presentation_rows
from dzack_research.preamble.categories.modules.graded_direct_sums import GradedDirectSumModule
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
    Modules,
    ModulesWithChosenFinitePresentation,
)

from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets


class ModuleConnectionConstruction:
    r"""The selected connection from which a structured module is transported."""

    def __init__(self, source_connection) -> None:
        if not isinstance(source_connection, Connection):
            raise TypeError("a module-connection construction starts from a Connection")
        self._source_connection = source_connection

    def source_connection(self):
        return self._source_connection


class ModulesWithConnection(OwnedParameterizedCategory):
    r"""Modules over ``A`` equipped with an ``A/R``-connection."""

    def an_object(self):
        r"""A free rank-one module over the algebra, with the zero connection.

        The zero connection is flat, so this object is a specimen of both this
        category and its flat refinement.
        """
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        module = self.algebra().free_module(finite_ordinal_set(1))
        connections = module.connections()
        return self(
            connections(lambda _label: connections.target_module().zero())
        )

    @classmethod
    def _repr_object_names(cls):
        return "modules with connection"

    def algebra(self):
        return self.base()

    def parameter_category(self):
        r"""The commutative algebras over the parameter's own base."""
        return Algebras(self.parameter().base_ring()).Associative().Unital().Commutative()

    def super_categories(self):

        return [Modules(self.algebra())]

    def Mor(self, domain, codomain):
        r"""Return horizontal module maps between two objects with connection."""
        if domain not in self or codomain not in self:
            raise TypeError("a connection Hom requires two modules with connection over this algebra")
        return ConnectionMorphismCategoryConstruction(Modules(self.algebra())).Of(
            domain,
            codomain,
        )

    def _call_(self, connection):
        r"""Equip the source module with the selected connection."""
        if not isinstance(connection, Connection):
            raise TypeError("a module with connection is specified by a Connection")
        source = connection.module()
        algebra = connection.algebra()
        if algebra is not self.algebra():
            raise ValueError("the connection belongs to a different coefficient algebra")
        assert source in FinitelyGeneratedFreeModules(algebra), (
            "structured connection modules are materialized here for finite free source modules"
        )
        categories = [self]
        if connection.is_flat():
            categories.append(ModulesWithFlatConnection(algebra))
        construction = ModuleConnectionConstruction(connection)
        return algebra._fresh_free_module_on(
            source.module_generating_set(),
            _extra_categories=tuple(categories),
            _extra_construction_data={"connection_construction": construction},
        )

    class ParentMethods:
        def __init__(self, connection_construction, **rest) -> None:
            self._connection_construction = connection_construction
            super().__init__(**rest)

        def connection_construction(self):
            r"""Return the selected connection construction defining this module."""
            return self._connection_construction

        @cached_method
        def connection(self):
            source_connection = self.connection_construction().source_connection()
            transported_target = self.connections().target_module()
            omega = source_connection.one_forms()

            def transported_image(label):
                image = transported_target.zero()
                for (source_label, form_label), coefficient in source_connection.target_module().framing_coefficients(source_connection.generator_image(label)).items():
                    image += transported_target.scalar_multiple(
                        coefficient,
                        transported_target.pure_tensor(
                            self.module_generator(source_label),
                            omega.module_generator(form_label),
                        ),
                    )
                return image

            return self.connections()(transported_image)

        def Mor(self, codomain, category=None):
            connections = ModulesWithConnection(self.base_ring())
            if codomain in connections and (
                category is None or category.is_subcategory(connections)
            ):
                return connections.Mor(self, codomain)
            if category is None:
                return self.module_category().Mor(self, codomain)
            return _category_homset(category, self, codomain)

        def _Hom_(self, codomain, category=None):
            return self.Mor(codomain, category=category)


class ModulesWithFlatConnection(OwnedParameterizedCategory):
    r"""Modules whose selected connection has zero curvature."""

    def an_object(self):
        r"""A free rank-one module over the algebra, with the zero connection.

        The zero connection is flat, so this object is a specimen of both this
        category and its flat refinement.
        """
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        module = self.algebra().free_module(finite_ordinal_set(1))
        connections = module.connections()
        return ModulesWithConnection(self.algebra())(
            connections(lambda _label: connections.target_module().zero())
        )

    @classmethod
    def _repr_object_names(cls):
        return "modules with flat connection"

    def algebra(self):
        return self.base()

    def parameter_category(self):
        r"""The commutative algebras over the parameter's own base."""
        return Algebras(self.parameter().base_ring()).Associative().Unital().Commutative()

    def super_categories(self):
        return [ModulesWithConnection(self.algebra())]

    class ParentMethods:
        def is_flat_connection(self) -> bool:
            return True


class Connection(Element):
    r"""An ``R``-connection ``E -> E tensor_A Omega^1_{A/R}``."""

    def __init__(self, parent, generator_images) -> None:
        Element.__init__(self, parent)
        labels = self.module().module_generating_set()
        target = self.target_module()

        if isinstance(generator_images, dict):
            size = labels.cardinality()
            try:
                finite = size.is_finite()
            except NotImplementedError:
                finite = False
            if not finite:
                raise TypeError(
                    "a dictionary connection assignment requires a finite framing; "
                    "use a callable for an arbitrary indexed framing"
                )
            missing = [label for label in labels if label not in generator_images]
            if missing:
                raise ValueError(f"connection assignment omits {missing}")
            raw_image = generator_images.__getitem__
        elif callable(generator_images):
            raw_image = generator_images
        elif isinstance(generator_images, (tuple, list)):
            size = labels.cardinality()
            try:
                finite_size = int(size.finite_value()) if size.is_finite() else None
            except NotImplementedError:
                finite_size = None
            if finite_size is None:
                raise TypeError(
                    "sequence connection syntax requires a finite framing"
                )
            if len(generator_images) != finite_size:
                raise ValueError("a connection needs one image for each module generator")
            by_position = {
                position: generator_images[position]
                for position in range(len(generator_images))
            }
            def raw_image(label):
                return by_position[int(labels.ranking_map()(label))]
        else:
            raise TypeError(
                "a connection is specified by a generator-indexed function or finite assignment"
            )

        def image(label):
            normalized = labels(label)
            value = raw_image(normalized)
            return value if value.parent() is target else target(value)

        self._generator_images = indexed_family(
            labels,
            image,
            name=f"Connection generator values of {self.module()}",
        )
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

        module = self.module()
        if module not in ModulesWithChosenFinitePresentation(self.algebra()):
            return
        labels = module.module_generating_set()
        for row in _presentation_rows(module):
            value = self._from_coefficients(
                {
                    labels[position]: coefficient
                    for position, coefficient in enumerate(row)
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
        return self._from_coefficients(self.module().framing_coefficients(element))

    def _call_(self, element):
        return self.__call__(element)

    def underlying_linear_morphism(self):
        cached = self.__dict__.get("_preamble_underlying_linear_morphism")
        if cached is not None:
            return cached
        target = self.parent().codomain_object()
        morphism = ConnectionUnderlyingLinearMorphism(
            self.parent().arrow_set(),
            self,
            lambda element: target(self(element.underlying_element())),
        )
        self._preamble_underlying_linear_morphism = morphism
        return morphism

    as_morphism = underlying_linear_morphism

    def curvature_target(self):
        target_forms = self.one_forms().exterior_power(2)
        return Modules(self.module().base_ring()).tensor_product(
            (self.module(), target_forms)
        )

    def _wedge_connection_value(self, value, one_form):
        omega = self.one_forms()
        omega_two = omega.exterior_power(2)
        target_two = self.curvature_target()
        result = target_two.zero()
        for (module_label, form_label), coefficient in self.target_module().framing_coefficients(value).items():
            wedge = omega.exterior_power_product(
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
        omega_two = omega.exterior_power(2)
        target_two = self.curvature_target()
        universal = omega.universal_derivation()
        result = target_two.zero()
        for (module_label, form_label), coefficient in self.target_module().framing_coefficients(self.generator_image(label)).items():
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
                wedge = omega.exterior_power_product(
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

        module = self.module()
        ring = module.base_ring()
        assert module in ModulesWithChosenFinitePresentation(ring), (
            "flatness by generator verification requires a selected finite framing"
        )
        zero = self.curvature_target().zero()
        return all(
            self.curvature_on_generator(label) == zero
            for label in module.module_generating_set()
        )

    def de_rham_module(self):
        r"""Return the DG-module de Rham complex attached to this flat connection."""
        return ConnectionDeRhamModule(self)


class ConnectionUnderlyingLinearMorphism(ModuleMorphism):
    r"""The selected underlying linear morphism of one algebraic connection."""

    def __init__(self, parent, connection, function) -> None:
        self._connection = connection
        super().__init__(parent, function, elementwise=True)

    def connection(self):
        return self._connection

    def _elementwise_linearity_derivation(self):
        return True


class ConnectionSpace(RestrictedHomCategoryParent):
    Element = Connection

    @staticmethod
    def __classcall__(cls, family_or_module, restricted_source=None, restricted_target=None):
        if isinstance(family_or_module, ConnectionCategoryConstruction):
            return typecall(
                cls,
                family_or_module,
                restricted_source,
                restricted_target,
            )
        return family_or_module.connections()

    def __init__(self, family, restricted_source, restricted_target) -> None:
        module = restricted_source.module_over_extension()
        algebra = module.base_ring()
        if algebra not in Algebras(algebra.base_ring()).Associative().Unital().Commutative():
            raise TypeError(
                "an algebraic connection here requires a module over a commutative algebra"
            )
        self._module = module
        self._algebra = algebra
        self._one_forms = algebra.kahler_differentials()

        self._target_module = restricted_target.module_over_extension()
        expected_target = Modules(module.base_ring()).tensor_product(
            (module, self._one_forms)
        )
        if self._target_module is not expected_target:
            raise ValueError("the restricted connection target is not E tensor_A Omega^1")
        # A connection is an R-linear map E -> E (x) Omega satisfying Leibniz,
        # so this is the subcategory of the existing R-linear Mor category cut
        # out by that rule.
        RestrictedHomCategoryParent.__init__(
            self,
            family,
            restricted_source,
            restricted_target,
        )
        self._inclusion = SetMorphism(
            Sets().Mor(self, self.arrow_set()),
            lambda connection: connection.underlying_linear_morphism(),
        )

    def module(self):
        return self._module

    def algebra(self):
        return self._algebra

    def one_forms(self):
        return self._one_forms

    def target_module(self):
        return self._target_module

    def inclusion(self):
        return self._inclusion

    def _element_constructor_(self, generator_images):
        if isinstance(generator_images, Connection) and generator_images.parent() is self:
            return generator_images
        if isinstance(generator_images, Morphism):
            if (
                generator_images.domain() is not self.domain_object()
                or generator_images.codomain() is not self.codomain_object()
            ):
                raise ValueError("the linear map has the wrong connection endpoints")
            if not isinstance(generator_images, ConnectionUnderlyingLinearMorphism):
                raise ValueError(
                    "an arbitrary R-linear map cannot be certified as a connection by this backend"
                )
            connection = generator_images.connection()
            if connection.parent() is self:
                return connection
            return self(lambda label: connection.generator_image(label))
        return Connection(self, generator_images)

    def _repr_(self):
        return f"Connections on {self.module()} over {self.algebra().base_ring()}"


class ConnectionCategoryConstruction(_RestrictedHomCategoryOf):
    _declaration_name = "_ConnectionCategory"

    def fixed_category_class(self):
        return ConnectionSpace

    def accepts(self, arrow) -> bool:
        return isinstance(arrow, ConnectionUnderlyingLinearMorphism)


@cached_function(key=lambda module: id(module))
def _connections(module) -> ConnectionSpace:
    algebra = module.base_ring()
    if algebra not in Algebras(algebra.base_ring()).Associative().Unital().Commutative():
        raise TypeError(
            "an algebraic connection here requires a module over a commutative algebra"
        )
    one_forms = algebra.kahler_differentials()
    target = Modules(module.base_ring()).tensor_product((module, one_forms))
    ring_map = algebra.algebra_structure_morphism()
    restricted_source = module.restrict_scalars(ring_map)
    restricted_target = target.restrict_scalars(ring_map)
    return ConnectionCategoryConstruction(Modules(algebra.base_ring())).Of(
        restricted_source,
        restricted_target,
    )


class ConnectionMorphism(Element):
    r"""An ``A``-linear map horizontal for the selected connections."""

    def __init__(self, parent, images, *, verify_horizontality=True) -> None:
        Element.__init__(self, parent)
        underlying = parent.arrow_set()(images)
        if underlying.linearity_decision() is not True:
            raise ValueError("a connection morphism requires an established underlying linear map")
        self._underlying_morphism = underlying
        if verify_horizontality:
            self._check_connection_square()
        self._underlying_morphism = HorizontalConnectionUnderlyingMorphism(
            parent.arrow_set(),
            self,
            underlying,
        )

    def domain(self):
        return self.parent().domain_object()

    def codomain(self):
        return self.parent().codomain_object()

    def __call__(self, element):
        return self._underlying_morphism(element)

    def _call_(self, element):
        return self.__call__(element)

    def underlying_linear_morphism(self):
        return self._underlying_morphism

    as_morphism = underlying_linear_morphism

    def _check_connection_square(self) -> None:
        domain_connection = self.domain().connection()
        codomain_connection = self.codomain().connection()
        if domain_connection.algebra() is not codomain_connection.algebra():
            raise ValueError("horizontal morphisms require one coefficient algebra")
        omega = domain_connection.one_forms()
        identity_omega = omega.module_category().Mor(omega, omega).identity()

        induced = self.underlying_linear_morphism().tensor_product_map(
            identity_omega,
            source=domain_connection.target_module(),
            target=codomain_connection.target_module(),
        )

        domain = self.domain()
        ring = domain.base_ring()
        assert domain in ModulesWithChosenFinitePresentation(ring), (
            "horizontality by generator verification requires a selected finite framing"
        )
        for label in domain.module_generating_set():
            generator = self.domain().module_generator(label)
            if codomain_connection(self(generator)) != induced(domain_connection(generator)):
                raise ValueError(
                    "the module map is not horizontal for the selected connections"
                )


class HorizontalConnectionUnderlyingMorphism(ModuleMorphism):
    r"""The selected underlying module morphism of one horizontal map."""

    def __init__(self, parent, connection_morphism, underlying) -> None:
        self._connection_morphism = connection_morphism
        self._underlying_source_morphism = underlying
        super().__init__(
            parent,
            lambda element: underlying(element),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return self._underlying_source_morphism.linearity_decision()

    def connection_morphism(self):
        return self._connection_morphism


class ConnectionHomset(RestrictedHomCategoryParent):
    Element = ConnectionMorphism

    @staticmethod
    def __classcall__(cls, family_or_domain, domain_or_codomain, codomain=None):
        if isinstance(family_or_domain, ConnectionMorphismCategoryConstruction):
            return typecall(
                cls,
                family_or_domain,
                domain_or_codomain,
                codomain,
            )
        return ModulesWithConnection(family_or_domain.base_ring()).Mor(
            family_or_domain, domain_or_codomain
        )

    def __init__(self, family, domain, codomain) -> None:
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("connection morphisms require one coefficient algebra")
        RestrictedHomCategoryParent.__init__(
            self,
            family,
            domain,
            codomain,
        )

    def _element_constructor_(self, images):
        if isinstance(images, ConnectionMorphism) and images.parent() is self:
            return images
        if isinstance(images, HorizontalConnectionUnderlyingMorphism):
            structured = images.connection_morphism()
            if structured.parent() is self:
                return structured
        return ConnectionMorphism(self, images)

    def identity(self):
        if self.domain_object() is not self.codomain_object():
            raise ValueError("identity belongs to a connection endomorphism homset")
        return ConnectionMorphism(
            self,
            self.arrow_set().identity(),
            verify_horizontality=False,
        )


class ConnectionMorphismCategoryConstruction(_RestrictedHomCategoryOf):
    _declaration_name = "_ConnectionMorphismCategory"

    def fixed_category_class(self):
        return ConnectionHomset

    def accepts(self, arrow) -> bool:
        return isinstance(arrow, HorizontalConnectionUnderlyingMorphism)



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


        coefficient_module = connection.module()
        algebra = connection.algebra()
        omega = connection.one_forms()
        dga = algebra.de_rham_algebra()
        ring_map = algebra.algebra_structure_morphism()

        class _ConnectionDeRhamModule(GradedDirectSumModule):
            def __init__(self) -> None:
                self._connection = connection
                self._coefficient_module = coefficient_module
                self._omega = omega
                self._dga = dga

                def piece(degree):
                    forms = omega.exterior_power(degree)
                    return Modules(coefficient_module.base_ring()).tensor_product(
                        (coefficient_module, forms)
                    ).restrict_scalars(ring_map)

                GradedDirectSumModule.__init__(
                    self,
                    algebra.base_ring(),
                    piece,
                    name=f"de Rham DG-module of {coefficient_module}",
                    extra_categories=(DifferentialGradedModules(dga),),
                )
                self._preamble_graded_algebra = dga
                self._preamble_dg_algebra = dga
                self._preamble_graded_algebra_action = self._right_action
                self._preamble_differential = ConnectionDeRhamDifferential(self)

            def connection(self):
                return self._connection

            def coefficient_module(self):
                return self._coefficient_module

            def from_coefficient(self, element):
                forms_zero = self._omega.exterior_power(0)
                tensor_zero = Modules(self._coefficient_module.base_ring()).tensor_product(
                    (self._coefficient_module, forms_zero)
                )
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
                source_forms = self._omega.exterior_power(degree)
                target_forms = self._omega.exterior_power(degree + 1)
                modules = Modules(self._coefficient_module.base_ring())
                source_tensor = modules.tensor_product(
                    (self._coefficient_module, source_forms)
                )
                target_tensor = modules.tensor_product(
                    (self._coefficient_module, target_forms)
                )
                result = target_tensor.zero()
                underlying = self._underlying_component(component)
                for (module_label, form_label), coefficient in source_tensor.framing_coefficients(underlying).items():
                    coefficient_vector = self._coefficient_module.scalar_multiple(
                        coefficient,
                        self._coefficient_module.module_generator(module_label),
                    )
                    connection_value = self._connection(coefficient_vector)
                    basis_form = source_forms.module_generator(form_label)
                    for (
                        output_module_label,
                        one_form_label,
                    ), connection_coefficient in self._connection.target_module().framing_coefficients(connection_value).items():
                        wedge = self._omega.exterior_power_product(
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
                    left_forms = self._omega.exterior_power(left_degree)
                    modules = Modules(self._coefficient_module.base_ring())
                    left_tensor = modules.tensor_product(
                        (self._coefficient_module, left_forms)
                    )
                    left_underlying = self._underlying_component(left_component)
                    for right_degree, right_component in exterior_element.homogeneous_components().items():
                        target_degree = left_degree + right_degree
                        target_forms = self._omega.exterior_power(target_degree)
                        target_tensor = modules.tensor_product(
                            (self._coefficient_module, target_forms)
                        )
                        target_value = target_tensor.zero()
                        for (
                            module_label,
                            left_form_label,
                        ), left_coefficient in left_tensor.framing_coefficients(left_underlying).items():
                            left_form = left_forms.module_generator(left_form_label)
                            for right_form_label, right_coefficient in exterior_algebra.graded_piece(right_degree).framing_coefficients(right_component).items():
                                right_form = exterior_algebra.graded_piece(
                                    right_degree
                                ).module_generator(right_form_label)
                                wedge = self._omega.exterior_power_product(
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
    "ModulesWithConnection",
    "ModulesWithFlatConnection",
]
