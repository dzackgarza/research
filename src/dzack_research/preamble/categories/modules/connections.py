r"""Algebraic connections on represented modules over commutative algebras."""

from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.misc.unknown import Unknown
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import Element

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    _RestrictedMorCategoryOf,
    RestrictedMorCategoryParent,
    _category_mor_parent,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.algebras.differential_graded_algebras import DifferentialComponentMorphism
from dzack_research.preamble.categories.modules.cochain_complexes import (
    CochainComplexes,
    _CochainComplexDirectSum,
)
from dzack_research.preamble.categories.modules.dg_modules import DifferentialGradedModules
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import _presentation_rows
from dzack_research.preamble.categories.modules.graded_direct_sums import GradedDirectSumElement
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    Modules,
    ModulesWithChosenFinitePresentation,
)

from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


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
            raise TypeError("a connection Mor requires two modules with connection over this algebra")
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
        assert source in FramedModules(algebra), (
            "a represented connection is equipped on the framed module carrying its generator-indexed datum"
        )
        categories = [self]
        match connection.is_flat():
            case True:
                categories.append(ModulesWithFlatConnection(algebra))
            case _:
                pass
        return source._module_with_structure(
            tuple(categories),
            {
                "source_connection": connection,
                "unformed_module": source,
            },
        )

    class ParentMethods:
        def __init__(self, source_connection, unformed_module, **rest) -> None:
            assert source_connection.module() is unformed_module, (
                "a module with connection retains the exact module on which its connection was stated"
            )
            self._preamble_source_connection = source_connection
            self._preamble_unformed_module = unformed_module
            super().__init__(**rest)

        def unformed_module(self):
            r"""Return the module on which the selected connection was stated."""
            return self._preamble_unformed_module

        def _element_of_unformed_module(self, element):
            module = self.unformed_module()
            return module.linear_combination(self.framing_coefficients(element))

        def _element_from_unformed_module(self, element):
            return self.linear_combination(
                self.unformed_module().framing_coefficients(element)
            )

        @cached_method
        def connection(self):
            r"""Return the selected connection datum on :meth:`unformed_module`."""
            return self._preamble_source_connection

        def Mor(self, codomain, category=None):
            connections = ModulesWithConnection(self.base_ring())
            if codomain in connections and (
                category is None or category.is_subcategory(connections)
            ):
                return connections.Mor(self, codomain)
            if category is None:
                return self.module_category().Mor(self, codomain)
            return _category_mor_parent(category, self, codomain)

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

    def is_flat(self):

        module = self.module()
        ring = module.base_ring()
        match module in ModulesWithChosenFinitePresentation(ring):
            case False:
                return Unknown
            case True:
                pass
        labels = module.module_generating_set()
        match labels.cardinality().is_finite():
            case True:
                pass
            case _:
                return Unknown
        zero = self.curvature_target().zero()
        return all(
            self.curvature_on_generator(label) == zero
            for label in labels
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


class ConnectionSpace(RestrictedMorCategoryParent):
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
        RestrictedMorCategoryParent.__init__(
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
                    "an arbitrary R-linear map alone does not supply the Leibniz rule required of a connection"
                )
            connection = generator_images.connection()
            if connection.parent() is self:
                return connection
            return self(lambda label: connection.generator_image(label))
        return Connection(self, generator_images)

    def _repr_(self):
        return f"Connections on {self.module()} over {self.algebra().base_ring()}"


class ConnectionCategoryConstruction(_RestrictedMorCategoryOf):
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

    def __init__(self, parent, images) -> None:
        Element.__init__(self, parent)
        underlying = parent.arrow_set()(images)
        if underlying.linearity_decision() is not True:
            raise ValueError("a connection morphism requires an established underlying linear map")
        self._underlying_morphism = underlying
        match self._horizontality_derivation():
            case True:
                pass
            case False:
                raise ValueError("the module map is not horizontal for the selected connections")
            case _:
                self._check_connection_square()
        self._underlying_morphism = HorizontalConnectionUnderlyingMorphism(
            parent.arrow_set(),
            self,
            underlying,
        )

    def _horizontality_derivation(self):
        r"""Return a construction-derived horizontality decision, or ``None``."""
        return None

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

    def __mul__(self, other):
        match other:
            case ConnectionMorphism():
                pass
            case _:
                return NotImplemented
        match other.codomain() is self.domain():
            case True:
                pass
            case False:
                return NotImplemented
        underlying = self.underlying_linear_morphism() * other.underlying_linear_morphism()
        return other.domain().Mor(self.codomain())._from_horizontal_morphism(underlying)

    def _check_connection_square(self) -> None:
        domain_connection = self.domain().connection()
        codomain_connection = self.codomain().connection()
        if domain_connection.algebra() is not codomain_connection.algebra():
            raise ValueError("horizontal morphisms require one coefficient algebra")
        omega = domain_connection.one_forms()
        identity_omega = omega.module_category().Mor(omega, omega).identity()

        domain_module = domain_connection.module()
        codomain_module = codomain_connection.module()
        underlying = _ConnectionCoefficientViewMorphism(
            Modules(domain_connection.algebra()).Mor(domain_module, codomain_module),
            self.underlying_linear_morphism(),
            self.domain(),
            self.codomain(),
        )
        induced = underlying.tensor_product_map(
            identity_omega,
            source=domain_connection.target_module(),
            target=codomain_connection.target_module(),
        )

        ring = domain_module.base_ring()
        assert domain_module in ModulesWithChosenFinitePresentation(ring), (
            "horizontality by generator verification requires a selected finite framing"
        )
        for label in domain_module.module_generating_set():
            generator = domain_module.module_generator(label)
            match codomain_connection(underlying(generator)) == induced(domain_connection(generator)):
                case True:
                    pass
                case _:
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


class _ConnectionCoefficientViewMorphism(ModuleMorphism):
    r"""A structured connection map read on the exact modules carrying its connections."""

    def __init__(self, parent, structured_morphism, structured_source, structured_target) -> None:
        self._structured_morphism = structured_morphism
        self._structured_source = structured_source
        self._structured_target = structured_target
        target = parent.codomain()
        super().__init__(
            parent,
            lambda element: target(
                structured_morphism(structured_source(element))
            ),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return self._structured_morphism.linearity_decision()


class _ConstructedHorizontalConnectionMorphism(ConnectionMorphism):
    r"""A horizontal map whose construction already gives the connection square."""

    def _horizontality_derivation(self):
        return True


class ConnectionMor(RestrictedMorCategoryParent):
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
        RestrictedMorCategoryParent.__init__(
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

    def _from_horizontal_morphism(self, underlying):
        return _ConstructedHorizontalConnectionMorphism(self, underlying)

    def identity(self):
        if self.domain_object() is not self.codomain_object():
            raise ValueError("identity belongs to a connection endomorphism Mor")
        return self._from_horizontal_morphism(self.arrow_set().identity())


class ConnectionMorphismCategoryConstruction(_RestrictedMorCategoryOf):
    _declaration_name = "_ConnectionMorphismCategory"

    def fixed_category_class(self):
        return ConnectionMor

    def accepts(self, arrow) -> bool:
        return isinstance(arrow, HorizontalConnectionUnderlyingMorphism)



def _connection_de_rham_piece(connection, degree):
    degree = int(degree)
    algebra = connection.algebra()
    match degree < 0:
        case True:
            return algebra.base_ring().free_module(0)
        case False:
            pass
    coefficient_module = connection.module()
    forms = connection.one_forms().exterior_power(degree)
    tensor = Modules(coefficient_module.base_ring()).tensor_product(
        (coefficient_module, forms)
    )
    return tensor.restrict_scalars(algebra.algebra_structure_morphism())


def _connection_de_rham_component(connection, degree, component, target):
    degree = int(degree)
    match degree < 0:
        case True:
            return target.zero()
        case False:
            pass
    coefficient_module = connection.module()
    omega = connection.one_forms()
    source_forms = omega.exterior_power(degree)
    target_forms = omega.exterior_power(degree + 1)
    modules = Modules(coefficient_module.base_ring())
    source_tensor = modules.tensor_product((coefficient_module, source_forms))
    target_tensor = modules.tensor_product((coefficient_module, target_forms))
    result = target_tensor.zero()
    match hasattr(component, "underlying_element"):
        case True:
            underlying = component.underlying_element()
        case False:
            underlying = component
    for (module_label, form_label), coefficient in source_tensor.framing_coefficients(underlying).items():
        coefficient_vector = coefficient_module.scalar_multiple(
            coefficient,
            coefficient_module.module_generator(module_label),
        )
        connection_value = connection(coefficient_vector)
        basis_form = source_forms.module_generator(form_label)
        for (
            output_module_label,
            one_form_label,
        ), connection_coefficient in connection.target_module().framing_coefficients(connection_value).items():
            wedge = omega.exterior_power_product(
                1,
                omega.module_generator(one_form_label),
                degree,
                basis_form,
            )
            match wedge == target_forms.zero():
                case True:
                    pass
                case _:
                    result += target_tensor.scalar_multiple(
                        connection_coefficient,
                        target_tensor.pure_tensor(
                            coefficient_module.module_generator(output_module_label),
                            wedge,
                        ),
                    )
    return target(result)


def _connection_de_rham_right_action(module, module_element, algebra_element):
    module_element = module(module_element)
    dga = module.dga()
    algebra_element = dga(algebra_element)
    exterior_element = dga.realize(algebra_element)
    exterior_algebra = dga.extension_algebra()
    coefficient_module = module.coefficient_module()
    omega = module.connection().one_forms()
    result = module.zero()
    for left_degree, left_component in module_element.homogeneous_components().items():
        left_forms = omega.exterior_power(left_degree)
        modules = Modules(coefficient_module.base_ring())
        left_tensor = modules.tensor_product((coefficient_module, left_forms))
        match hasattr(left_component, "underlying_element"):
            case True:
                left_underlying = left_component.underlying_element()
            case False:
                left_underlying = left_component
        for right_degree, right_component in exterior_element.homogeneous_components().items():
            target_degree = left_degree + right_degree
            target_forms = omega.exterior_power(target_degree)
            target_tensor = modules.tensor_product((coefficient_module, target_forms))
            target_value = target_tensor.zero()
            for (
                module_label,
                left_form_label,
            ), left_coefficient in left_tensor.framing_coefficients(left_underlying).items():
                left_form = left_forms.module_generator(left_form_label)
                for right_form_label, right_coefficient in exterior_algebra.graded_piece(right_degree).framing_coefficients(right_component).items():
                    right_form = exterior_algebra.graded_piece(right_degree).module_generator(
                        right_form_label
                    )
                    wedge = omega.exterior_power_product(
                        left_degree,
                        left_form,
                        right_degree,
                        right_form,
                    )
                    match wedge == target_forms.zero():
                        case True:
                            pass
                        case _:
                            target_value += target_tensor.scalar_multiple(
                                left_coefficient * right_coefficient,
                                target_tensor.pure_tensor(
                                    coefficient_module.module_generator(module_label),
                                    wedge,
                                ),
                            )
            match target_value == target_tensor.zero():
                case True:
                    pass
                case _:
                    result += module.from_component(
                        target_degree,
                        module.graded_piece(target_degree)(target_value),
                    )
    return result


class _ConnectionDeRhamDirectSum(_CochainComplexDirectSum):
    r"""The cochain direct sum underlying one flat connection's de Rham DG-module."""

    def __init__(self, connection, **rest) -> None:
        self._connection = connection
        super().__init__(**rest)

    def connection(self):
        return self._connection

    def coefficient_module(self):
        return self.connection().module()

    def from_coefficient(self, element):
        omega = self.connection().one_forms()
        forms_zero = omega.exterior_power(0)
        tensor_zero = Modules(self.coefficient_module().base_ring()).tensor_product(
            (self.coefficient_module(), forms_zero)
        )
        unit = forms_zero.module_generator(0)
        return self.from_component(
            0,
            self.graded_piece(0)(tensor_zero.pure_tensor(element, unit)),
        )


class ConnectionDeRhamModule:
    r"""Factory namespace for a flat connection's de Rham DG-module."""

    def __new__(cls, connection):
        match connection.is_flat():
            case True:
                pass
            case _:
                raise ValueError("a DG-module de Rham differential requires an established flat connection")
        coefficient_module = connection.module()
        algebra = connection.algebra()
        dga = algebra.de_rham_algebra()
        integers = _own_ring(SageZZ)
        match dga.grading_monoid() is integers:
            case True:
                pass
            case False:
                raise ValueError("the connection de Rham DG-module requires the integer grading of its de Rham algebra")

        pieces = indexed_family(
            integers,
            lambda degree: _connection_de_rham_piece(connection, degree),
            name="Connection de Rham pieces",
        )

        def differential(degree):
            degree = int(degree)
            source = pieces(degree)
            target = pieces(degree + 1)
            return DifferentialComponentMorphism(
                source,
                target,
                lambda component: _connection_de_rham_component(
                    connection,
                    degree,
                    component,
                    target,
                ),
            )

        differentials = indexed_family(
            integers,
            differential,
            name="Connection de Rham differentials",
        )

        def right_action(module_element, algebra_element):
            return _connection_de_rham_right_action(
                module_element.parent(),
                module_element,
                algebra_element,
            )

        return CochainComplexes(algebra.base_ring()).from_family(
            pieces,
            differentials,
            name=f"de Rham DG-module of {coefficient_module}",
            extra_categories=(DifferentialGradedModules(dga),),
            extra_construction_data={
                "connection": connection,
                "graded_algebra": dga,
                "graded_algebra_action": right_action,
                "dg_algebra": dga,
            },
            _realization=(_ConnectionDeRhamDirectSum, GradedDirectSumElement),
        )


__all__ = [
    "Connection",
    "ConnectionDeRhamModule",
    "ConnectionMor",
    "ConnectionMorphism",
    "ConnectionSpace",
    "ModulesWithConnection",
    "ModulesWithFlatConnection",
]
