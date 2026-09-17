r"""Owned number fields and their selected primitive-element presentations."""

from sage.all import (
    CyclotomicField as _SageCyclotomicField,
)
from sage.all import (
    NumberField as _SageNumberField,
)
from sage.all import (
    QuadraticField as _SageQuadraticField,
)
from sage.misc.cachefunc import cached_function, cached_method
from sage.rings.abc import Order as SageNumberFieldOrder
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories._lattice import signature_pair
from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoryPacketMethods,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.group.groups import _own_group
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
    Modules,
)
from dzack_research.preamble.categories.rings.embeddings import NumberFieldHomset
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedOrders,
    OwnedRings,
    _engine_element,
    _engine_numeral,
    _engine_ring,
    _own_ring,
    _owned_engine_ring,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family
from dzack_research.preamble.refine import refine


def _own_number_field(engine):

    return _refine_number_field_view(_own_ring(engine))


def CyclotomicField(order, *args, **kwargs):
    field = _own_number_field(
        _SageCyclotomicField(_engine_numeral(SageZZ, order), *args, **kwargs)
    )
    field._preamble_ring_display = f"Cyclotomic field Q(zeta_{order})"
    return field


def QuadraticField(discriminant, *args, **kwargs):
    field = _own_number_field(
        _SageQuadraticField(_engine_numeral(SageQQ, discriminant), *args, **kwargs)
    )
    field._preamble_ring_display = f"Quadratic field of discriminant {discriminant}"
    return field


def _number_field(polynomial, *args, **kwargs):
    parent = getattr(polynomial, "parent", lambda: None)()
    if parent not in OwnedRings():
        raise TypeError("number-field construction expects a polynomial in an owned polynomial ring")
    backend_polynomial = _engine_element(parent, polynomial)
    field = _own_number_field(_SageNumberField(backend_polynomial, *args, **kwargs))
    field._preamble_ring_display = f"Number field defined by {polynomial}"
    return field


class NumberFieldHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return NumberFieldHomset


class OwnedNumberFields(CategoryPacketMethods, OwnedCategory):
    r"""Finite extensions of ``QQ``."""

    _HomCategory = NumberFieldHomCategoryConstruction

    def an_object(self):
        r"""The rational field as the degree-one number field."""
        return _own_number_field(SageQQ)
    _certifying_predicate = "_preamble_is_number_field"

    @classmethod
    def _repr_object_names(cls):
        return "number fields"

    def super_categories(self):
        return [OwnedRings().Division().Commutative()]

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a number-field embedding requires two number fields")
        return self.HomCategory().Of(domain, codomain)

    class ParentMethods:
        def Mor(self, codomain, category=None):
            number_fields = OwnedNumberFields()
            if category is None or category.is_subcategory(number_fields):
                return number_fields.Mor(self, codomain)
            return super().Mor(codomain, category=category)

        def degree(self):
            r"""Return ``[K:QQ]`` as an owned integer."""

            integers = _own_ring(SageZZ)
            engine = _engine_ring(self)
            value = (
                SageZZ.one()
                if engine is SageQQ
                else SageZZ(
                    engine.degree()
                    if engine.is_absolute()
                    else engine.absolute_degree()
                )
            )
            return integers._from_engine_element(value)

        def discriminant(self):
            r"""Return the discriminant of the ring of integers of ``K``."""

            integers = _own_ring(SageZZ)
            engine = _engine_ring(self)
            value = SageZZ.one() if engine is SageQQ else SageZZ(engine.discriminant())
            return integers._from_engine_element(value)

        def signature(self):
            r"""Return the signature pair ``(r_1,r_2)`` with ``r_1+2r_2=[K:QQ]``."""

            engine = _engine_ring(self)
            if engine is SageQQ:
                return signature_pair(1, 0)
            real, complex_pairs = engine.signature()
            return signature_pair(real, complex_pairs)

        def class_number(self):
            r"""Return the class number of the ring of integers."""

            integers = _own_ring(SageZZ)
            engine = _engine_ring(self)
            value = SageZZ.one() if engine is SageQQ else SageZZ(engine.class_number())
            return integers._from_engine_element(value)

        def extension(self, polynomial, name="a"):
            r"""Return the finite extension defined by an owned polynomial over ``self``."""
            polynomial_ring = getattr(polynomial, "parent", lambda: None)()
            if polynomial_ring is None or polynomial_ring.base_ring() is not self:
                raise TypeError(
                    "a relative number-field extension requires a polynomial over this field"
                )

            backend_polynomial = _engine_element(polynomial_ring, polynomial)
            return _own_ring(_engine_ring(self).extension(backend_polynomial, name))

        def primes_above(self, prime):
            r"""Return the prime ideals of ``O_K`` above a rational prime."""

            order = self.ring_of_integers()
            integers = order.base_ring()
            prime = integers(prime)
            backend_prime = _engine_element(integers, prime)
            order_engine = _engine_ring(order)
            ideals = []
            for backend_ideal in _engine_ring(self).primes_above(backend_prime):
                generators = tuple(
                    order._from_engine_element(order_engine(generator))
                    for generator in backend_ideal.gens()
                )
                ideals.append(order.ideal(*generators))
            return finite_ordered_set(ideals)

        def ring_of_integers(self):
            r"""Return the maximal order ``O_K`` as an owned ring."""

            engine = _engine_ring(self)
            if engine is SageQQ:
                return _refine_order_view(_own_ring(SageZZ))
            return _refine_order_view(_own_ring(engine.ring_of_integers()))

        maximal_order = ring_of_integers

        def order_generated_by(self, *generators):
            r"""Return the order ``ZZ[generators]`` inside this number field."""
            if not generators:
                raise ValueError("an order construction needs at least one field generator")

            engine = _engine_ring(self)
            backend_generators = tuple(
                _engine_element(self, self(generator)) for generator in generators
            )
            datum = (
                backend_generators[0]
                if len(backend_generators) == 1
                else list(backend_generators)
            )
            return _refine_order_view(_own_ring(engine.order(datum)))

        def ramified_primes(self):
            r"""Return the rational primes ramified in ``K``."""

            return finite_ordered_set(abs(self.discriminant()).prime_divisors())

        @cached_method
        def embeddings(self, target):
            r"""Return the owned field embeddings ``K -> target``.

            If the target is again a number field, the arrows live in the
            specialized number-field Hom.  Embeddings into a larger owned
            field such as ``AA``, ``RR`` or ``CC`` are ring morphisms in the
            ambient field category; the codomain is not falsely promoted to a
            finite extension of ``QQ``.
            """

            if target not in OwnedRings().Division().Commutative():
                raise TypeError("number-field embeddings require an owned target field")
            if target in OwnedNumberFields():
                return self.Mor(target).embeddings()

            source_engine = _engine_ring(self)
            from dzack_research.preamble.rings.real import ExactRealField

            match target:
                case ExactRealField():
                    from sage.rings.qqbar import AA as SageAA

                    engine_embeddings = tuple(source_engine.embeddings(SageAA))

                    def embedding_at(position):
                        engine_embedding = engine_embeddings[int(position)]
                        return self.Mor(target).elementwise(
                            lambda element: target(
                                engine_embedding(
                                    _engine_element(self, self(element))
                                )
                            )
                        )

                case _:
                    engine_embeddings = tuple(
                        source_engine.embeddings(_engine_ring(target))
                    )

                    def embedding_at(position):
                        return self.Mor(target)(
                            engine_embeddings[int(position)]
                        )

            positions = finite_ordered_set(range(len(engine_embeddings)))

            primitive = self.primitive_element()

            def embedding_position(embedding):
                if (
                    getattr(embedding, "domain", lambda: None)() is not self
                    or getattr(embedding, "codomain", lambda: None)() is not target
                ):
                    raise ValueError(embedding)
                primitive_image = embedding(primitive)
                for position in positions:
                    if embedding_at(position)(primitive) == primitive_image:
                        return position
                raise ValueError(embedding)

            return FiniteOrderedSets().from_indexed(
                positions,
                embedding_at,
                index_of=embedding_position,
                name=f"Embeddings of {self} into {target}",
            )

        def is_galois(self) -> bool:
            r"""Return whether ``K/QQ`` is Galois."""
            engine = _engine_ring(self)
            return True if engine is SageQQ else bool(engine.is_galois())

        def galois_group(self):
            r"""Return ``Gal(K/QQ)``; this name is reserved for Galois ``K``."""
            if not self.is_galois():
                raise ValueError(
                    "K/QQ is not Galois; use normal_closure_galois_group() for the Galois group of its normal closure"
                )
            engine = _engine_ring(self)

            if engine is SageQQ:
                from sage.groups.perm_gps.permgroup_named import SymmetricGroup

                return _own_group(SymmetricGroup(1))
            return _own_group(engine.galois_group())

        def normal_closure(self):
            r"""Return a chosen normal closure of ``K/QQ``."""

            engine = _engine_ring(self)
            return self if engine is SageQQ else _own_ring(engine.galois_closure())

        def normal_closure_galois_group(self):
            r"""Return the Galois group of a chosen normal closure of ``K``."""
            return self.normal_closure().galois_group()

        def underlying_algebra(self, base_ring=None):
            r"""Return the selected integral form ``R[alpha]`` of this number field.

            For the currently represented archive specialization ``R=ZZ`` this
            is the order generated by the selected primitive element, not the
            maximal order.  Over ``QQ`` the selected finite algebra presentation
            is :meth:`as_algebra` itself.
            """
            integers = _own_ring(SageZZ)
            rationals = _own_number_field(SageQQ)
            match base_ring:
                case None:
                    base_ring = integers
                case _:
                    pass
            match base_ring:
                case ring if ring is integers:
                    match self is rationals:
                        case True:
                            return integers
                        case False:
                            return self.order_generated_by(self.primitive_element())
                case ring if ring is rationals:
                    return self.as_algebra()
                case _:
                    assert base_ring is integers or base_ring is rationals, (
                        "the selected number-field integral/algebra form is represented over ZZ or QQ"
                    )

        def base_change_functor(self, base_ring=None):
            r"""Return scalar extension from the selected base ring to ``QQ``.

            Applied to :meth:`underlying_algebra` over ``ZZ``, this is the
            existing algebra scalar-extension functor and reconstructs the
            selected ``QQ``-algebra presentation of the field.
            """
            from dzack_research.preamble.categories.algebras.algebras import (
                Algebras,
            )

            integers = _own_ring(SageZZ)
            rationals = _own_number_field(SageQQ)
            match base_ring:
                case None:
                    base_ring = integers
                case _:
                    pass
            match base_ring:
                case ring if ring is integers:
                    ring_map = integers.Mor(rationals)(lambda element: rationals(element))
                case ring if ring is rationals:
                    ring_map = rationals.Mor(rationals).identity()
                case _:
                    assert base_ring is integers or base_ring is rationals, (
                        "number-field base change is represented from ZZ or QQ"
                    )
            return Algebras(base_ring).Associative().Unital().Commutative().base_change_adjunction(ring_map).left_adjoint()

        def as_algebra(self):
            r"""Return this field with its selected finite ``QQ``-algebra presentation."""
            from dzack_research.preamble.categories.algebras.free_algebras import (
                _presented_algebra_on_engine,
            )

            rationals = _own_number_field(SageQQ)
            engine = _engine_ring(self)
            if engine is SageQQ:
                return rationals

            presentation_lift = None
            finite_free_coordinates = None
            if not engine.is_absolute():
                # A relative generator need not generate K over QQ.  Sage's
                # absolute model supplies both the chosen absolute primitive
                # element in this same engine and exact conversion to its
                # one-variable QQ presentation.
                absolute = engine.absolute_field("absolute_generator")
                from_absolute, to_absolute = absolute.structure()
                primitive = from_absolute(absolute.gen())
                polynomial = absolute.defining_polynomial()
                labels = finite_ordered_set(("absolute_generator",))
                def presentation_lift(element):
                    return to_absolute(element).lift()

                def finite_free_coordinates(element):
                    return tuple(to_absolute(element))
                degree = int(engine.absolute_degree())
            else:
                primitive = engine.gen()
                polynomial = engine.defining_polynomial()
                labels = self.algebra_generating_set()
                degree = int(engine.degree())

            presentation = rationals.free_module(labels).symmetric_algebra()
            relation = presentation._from_engine_element(
                _engine_ring(presentation)(polynomial)
            )
            return _presented_algebra_on_engine(
                engine,
                presentation,
                (relation,),
                generator_values=(primitive,),
                finite_free_degree=degree,
                finite_free_generator=primitive,
                finite_free_coordinates=finite_free_coordinates,
                presentation_lift=presentation_lift,
            )

    class ElementMethods:
        def inverse(self):
            r"""Return the multiplicative inverse of this nonzero field element."""

            return self.inverse_of_unit()

        @cached_method
        def multiplication_morphism(self):
            r"""Return multiplication by ``self`` on the selected finite ``QQ``-module presentation.

            A number field element is canonically a ``QQ``-linear endomorphism
            of its field.  The live field object keeps its ring identity, while
            :meth:`as_algebra` supplies the selected finite-free presentation
            used to represent this linear map.  No separate backend matrix is
            exposed: the matrix below is the matrix of this owned module
            morphism in that selected basis.
            """

            field = self.parent()
            algebra = field.as_algebra()
            multiplier = algebra._from_engine_element(
                _engine_element(field, self)
            )
            return algebra.module_category().Mor(algebra, algebra)(
                lambda label: multiplier * algebra.module_generator(label)
            )

        def multiplication_matrix(self):
            r"""Return the matrix of multiplication by ``self`` over ``QQ``."""

            return self.multiplication_morphism().matrix()

        matrix = multiplication_matrix

        def norm(self):
            r"""Return the field norm ``N_{K/QQ}(self)``.

            The norm is the determinant of the owned ``QQ``-linear
            multiplication endomorphism ``m_self : K -> K``.  This keeps the
            archived definition on the same mathematical map already exposed
            by :meth:`multiplication_morphism` instead of asking the private
            number-field backend for a second value.
            """

            return self.multiplication_morphism().determinant()

        def trace(self):
            r"""Return the field trace ``Tr_{K/QQ}(self)``.

            The trace is the trace of the owned ``QQ``-linear multiplication
            endomorphism ``m_self : K -> K``.
            """

            return self.multiplication_morphism().trace()

        def characteristic_polynomial(self):
            r"""Return the characteristic polynomial of multiplication by ``self`` over ``QQ``.

            Its degree is ``[K:QQ]`` even when ``self`` lies in a proper
            subfield.  This is therefore different from the minimal
            polynomial exactly in the cases where the chosen element does not
            generate the whole number field.
            """
            polynomial = self._backend().charpoly()
            return _own_ring(polynomial.parent())._from_engine_element(polynomial)

        def minimal_polynomial(self):
            r"""Return the minimal polynomial of ``self`` over ``QQ``."""
            return self.minpoly()

        def is_integral(self) -> bool:
            r"""Return whether ``self`` is an algebraic integer."""
            return bool(self._backend().is_integral())

        def conjugates(self, target):
            r"""Return the images of ``self`` under all owned embeddings into ``target``.

            The embeddings are the index set.  Two embeddings can have the
            same value on a nonprimitive element, so the result is an indexed
            family rather than a set of values; this retains multiplicity and
            the embedding that produced each conjugate.
            """
            field = self.parent()
            embeddings = field.embeddings(target)
            return finite_indexed_family(
                embeddings,
                lambda embedding: embedding(self),
                name=f"Conjugates of {self} in {target}",
            )


class NumberFieldsWithChosenPrimitiveElement(OwnedCategory):
    r"""Number fields carrying the primitive element selected by their presentation."""

    _certifying_predicate = "_preamble_has_chosen_primitive_element"

    def an_object(self):
        r"""A quadratic field with its selected generator."""
        return QuadraticField(2, "a")

    @classmethod
    def _repr_object_names(cls):
        return "number fields with a chosen primitive element"

    def super_categories(self):
        return [OwnedNumberFields()]

    class ParentMethods:
        def algebra_generating_set(self):
            return finite_ordered_set(_engine_ring(self).variable_names())

        def primitive_element(self):
            r"""Return the selected primitive element ``alpha``."""
            return self._from_engine_element(_engine_ring(self).gen())

        def algebra_generator(self, label):
            if label not in self.algebra_generating_set():
                raise ValueError(f"{label!r} is not the selected algebra-generator label")
            return self.primitive_element()

        def defining_polynomial(self):
            r"""Return the owned defining polynomial of the selected primitive element."""

            polynomial = _engine_ring(self).defining_polynomial()
            parent = _own_ring(polynomial.parent())
            return parent._from_engine_element(polynomial)

        def embedding_images(self, target):
            r"""Return the images of the selected primitive element under ``K -> target``."""

            primitive = self.primitive_element()
            embeddings = self.embeddings(target)
            return FiniteOrderedSets().from_indexed(
                embeddings,
                lambda embedding: embedding(primitive),
                name="Primitive-element embedding images",
            )


class OrdersWithChosenIntegralBasis(OwnedCategory):
    r"""Number-field orders carrying their selected integral basis."""

    _certifying_predicate = "_preamble_is_number_field_order"

    def an_object(self):
        r"""The maximal order of a quadratic field with its selected integral basis."""
        return QuadraticField(5, "a").ring_of_integers()

    @classmethod
    def _repr_object_names(cls):
        return "orders with a chosen integral basis"

    def super_categories(self):

        integers = _own_ring(SageZZ)
        return [
            OwnedOrders(),
            FinitelyGeneratedFreeModules(integers),
        ]

    class ParentMethods:
        def base_ring(self):

            return _own_ring(SageZZ)

        algebra_base_ring = base_ring

        def localization(self, *elements):
            from dzack_research.preamble.categories.rings.commutative_algebra import _localization

            return _localization(self, *elements)

        localize = localization

        def localize_at_prime(self, prime):
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                _prime_localization_from_input,
            )

            return _prime_localization_from_input(self, prime)

        localization_at_prime = localize_at_prime

        def base_change(self, ring_map):
            if _engine_ring(ring_map.domain()) is not SageZZ:
                raise ValueError("an order is a ZZ-algebra, so scalar extension starts at ZZ")
            target = _engine_ring(ring_map.codomain())
            if target is SageZZ:
                return self
            if target is SageQQ:

                field = _own_number_field(_engine_ring(self).fraction_field())
                return field.as_algebra()
            assert target is SageZZ or target is SageQQ, (
                "the represented order algebra base-change adapter constructs ZZ -> ZZ and ZZ -> QQ"
            )

        def integral_basis(self):
            return self.module_generators()

        def module_rank(self):
            engine = _engine_ring(self)
            return cardinal(1 if engine is SageZZ else engine.rank())


def _refine_order_view(order):
    r"""Return the constructor-owned order view with its selected integral basis."""
    return _owned_order_view(_engine_ring(order))


def _refine_number_field_view(field):
    r"""Return the constructor-owned number-field view of an engine field."""
    if field not in OwnedRings():
        raise TypeError("number-field construction expects an owned ring view")
    return _owned_number_field_view(_engine_ring(field))


def _order_basis_labels(engine):
    r"""Return the selected integral-basis labels of one order engine."""
    if engine is SageZZ:
        return finite_ordered_set((0,))
    return finite_ordered_set(range(int(engine.rank())))


def _order_basis_element(order, labels, label):
    r"""Return one selected integral-basis element through the owned order view."""
    if label not in labels:
        raise ValueError(f"{label!r} is not an integral-basis label")
    engine = _engine_ring(order)
    if engine is SageZZ:
        return order._from_engine_element(SageZZ.one())
    return order._from_engine_element(engine.basis()[labels.ranking_map()(label)])


@cached_function
def _owned_order_view(engine):
    r"""The selected-integral-basis view of one engine order.

    One engine has one owned ring, so the view refines that ring in place
    rather than constructing a second parent on the same engine.  The selected
    integral basis is installed once as the generic framing epimorphism
    ``F_Z(S) -> O``; public module generators are projections of that arrow.
    """
    if not (engine is SageZZ or isinstance(engine, SageNumberFieldOrder)):
        raise TypeError("the selected integral-basis view requires a number-field order")
    order = _owned_engine_ring(engine)
    if engine is not SageZZ:
        from dzack_research.preamble.categories.modules.pure.modules import FramedModules

        integers = _own_ring(SageZZ)
        labels = _order_basis_labels(engine)
        source = integers.free_module(labels)
        refine(order, FramedModules(integers))
        order._install_framing(labels, lambda label: _order_basis_element(order, labels, label), source)
    # The integers already have the exact regular rank-one frame. Other
    # orders now have their actual integral-basis epimorphism as well.
    return refine(order, OrdersWithChosenIntegralBasis())


@cached_function
def _owned_number_field_view(engine):
    r"""The strongest number-field view determined by ``engine``, refined in place."""
    rationals = _own_ring(SageQQ)
    categories = [OwnedNumberFields(), Modules(rationals)]
    if engine is not SageQQ:
        categories.append(NumberFieldsWithChosenPrimitiveElement())
    return refine(_owned_engine_ring(engine), Cat().meet(tuple(categories)))



__all__ = [
    "NumberFieldsWithChosenPrimitiveElement",
    "OrdersWithChosenIntegralBasis",
    "OwnedNumberFields",
]
