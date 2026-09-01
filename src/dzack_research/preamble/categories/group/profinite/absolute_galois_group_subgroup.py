r"""Open absolute-Galois subgroups and their conjugacy classes."""

from sage.categories.category_singleton import Category_singleton
from sage.categories.finite_fields import FiniteFields
from sage.categories.morphism import Morphism
from sage.rings.integer_ring import ZZ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.group.profinite.absolute_galois_group_element import (
    AbsoluteGaloisGroupElement,
    FrobeniusElement,
)
from dzack_research.preamble.categories.group.profinite.absolute_galois_groups import (
    AbsoluteGaloisGroups,
)
from dzack_research.preamble.categories.group.profinite.field_morphisms import (
    exact_embeddings,
    exact_field_morphism,
    field_generators,
)
from dzack_research.preamble.categories.group.profinite.galois_quotient import (
    FiniteGaloisExtension,
    continuous_group_homset,
)
from dzack_research.preamble.categories.rings.rings import engine_ring, own_ring
from dzack_research.preamble.refine import refine


class OpenAbsoluteGaloisSubgroups(Category_singleton):
    r"""Open subgroups (G_E\subseteq G_K) carrying the embedding (E\to\bar K)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "open subgroups of absolute Galois groups"

    def super_categories(self):
        return [AbsoluteGaloisGroups()]

    class ParentMethods:
        def ambient(self):
            return self._ambient

        def supergroup(self):
            return self._ambient

        def fixed_field(self):
            return self._fixed_extension.field()

        def fixed_extension(self):
            return self._fixed_extension

        def embedding(self):
            return self._fixed_extension.embedding()

        def index(self):
            return self._fixed_extension.degree()

        def inclusion(self):
            return self._inclusion


class OpenSubgroupInclusion(Morphism):
    r"""The literal inclusion of a realized open subgroup into its ambient group."""

    def __init__(self, subgroup) -> None:
        Morphism.__init__(
            self,
            continuous_group_homset(subgroup, subgroup.ambient()),
        )

    def _call_(self, element):
        subgroup = self.domain()
        element = subgroup(element)
        ambient = self.codomain()
        exponent = element.frobenius_exponent()
        if exponent is not None and ambient._is_finite_field():
            return FrobeniusElement(ambient, subgroup.index() * exponent)
        exact = element.exact_action()
        if exact is not None:
            return ambient(exact)
        raise NotImplementedError("the subgroup element has no global exact action")

    def is_injective(self) -> bool:
        return True

    def is_continuous(self) -> bool:
        return True


class OpenAbsoluteGaloisSubgroup(AbsoluteGaloisGroup):
    r"""The actual subgroup fixing one embedded finite extension (E/K)."""

    def __init__(self, ambient, extension: FiniteGaloisExtension) -> None:
        if not isinstance(extension, FiniteGaloisExtension):
            raise TypeError(
                "an open subgroup requires represented finite-extension data"
            )
        extension = ambient.extension_data(extension)
        self._ambient = ambient
        self._fixed_extension = extension
        super().__init__(
            extension.field(),
            closure=ambient.algebraic_closure(),
            embedding=extension.embedding(),
        )
        refine(self, OpenAbsoluteGaloisSubgroups())
        self._inclusion = OpenSubgroupInclusion(self)

    def ambient(self):
        return self._ambient

    def fixed_field(self):
        return self._fixed_extension.field()

    def fixed_extension(self) -> FiniteGaloisExtension:
        return self._fixed_extension

    def embedding(self):
        return self._fixed_extension.embedding()

    def index(self):
        return self._fixed_extension.degree()

    def inclusion(self) -> OpenSubgroupInclusion:
        return self._inclusion

    def is_normal(self) -> bool:
        return self._fixed_extension.is_galois()

    def __contains__(self, element) -> bool:
        if isinstance(element, AbsoluteGaloisGroupElement) and element.parent() is self:
            return True
        if element not in self._ambient:
            return False
        embedding = self.embedding()
        try:
            return all(
                element(embedding(generator)) == embedding(generator)
                for generator in field_generators(self.fixed_field())
            )
        except NotImplementedError:
            return False

    def _element_constructor_(self, datum=None, **options):
        if (
            isinstance(datum, AbsoluteGaloisGroupElement)
            and datum.parent() is self._ambient
        ):
            if datum not in self:
                raise ValueError(
                    "the ambient automorphism does not fix this subgroup's field"
                )
            exponent = datum.frobenius_exponent()
            if exponent is not None and self._ambient._is_finite_field():
                if exponent % self.index():
                    raise ValueError(
                        "the Frobenius power is outside this open subgroup"
                    )
                return FrobeniusElement(self, exponent // self.index())
            exact = datum.exact_action()
            if exact is not None:
                return super()._element_constructor_(exact)
            raise NotImplementedError("the ambient element has no global exact action")
        return super()._element_constructor_(datum, **options)

    def conjugacy_class(self):
        return OpenGaloisSubgroupConjugacyClass(self._ambient, self.fixed_field())

    def core(self):
        if self.is_normal():
            return self
        field = engine_ring(self.fixed_field())
        base = engine_ring(self._ambient.base_field())
        defining_base = getattr(field, "base_field", lambda: None)()
        if defining_base is base:
            polynomial = field.relative_polynomial()
        elif base.absolute_degree() == 1:
            polynomial = field.defining_polynomial().change_ring(base)
        else:
            raise NotImplementedError(
                "the relative defining polynomial over the ambient base field is unavailable"
            )

        normal_field, base_backend = polynomial.splitting_field(
            "normal_closure", map=True
        )
        normal_field = own_ring(normal_field)
        base_embedding = exact_field_morphism(
            self._ambient.base_field(), normal_field, base_backend
        )
        compatible_closure_embeddings = []
        for fixed_to_normal in exact_embeddings(self.fixed_field(), normal_field):
            if not all(
                fixed_to_normal(self._fixed_extension.base_embedding()(generator))
                == base_embedding(generator)
                for generator in field_generators(self._ambient.base_field())
            ):
                continue
            for normal_to_closure in exact_embeddings(
                normal_field, self._ambient.algebraic_closure()
            ):
                if all(
                    normal_to_closure(fixed_to_normal(generator))
                    == self.embedding()(generator)
                    for generator in field_generators(self.fixed_field())
                ):
                    compatible_closure_embeddings.append(normal_to_closure)
        if not compatible_closure_embeddings:
            raise ValueError(
                "the normal closure could not be placed compatibly inside the chosen algebraic closure"
            )
        stage = self._ambient.extension_data(
            normal_field,
            embedding=compatible_closure_embeddings[0],
            base_embedding=base_embedding,
        )
        return self._ambient.open_subgroup(stage)

    def __le__(self, other) -> bool:
        if (
            not isinstance(other, OpenAbsoluteGaloisSubgroup)
            or other.ambient() is not self.ambient()
        ):
            return False
        for embedding in exact_embeddings(other.fixed_field(), self.fixed_field()):
            if all(
                self.embedding()(embedding(generator)) == other.embedding()(generator)
                for generator in field_generators(other.fixed_field())
            ):
                return True
        return False

    def intersection(self, other):
        if (
            not isinstance(other, OpenAbsoluteGaloisSubgroup)
            or other.ambient() is not self.ambient()
        ):
            raise ValueError(
                "open-subgroup intersection requires one ambient Galois group"
            )
        if engine_ring(self.fixed_field()) in FiniteFields():
            degree = ZZ(self.index()).lcm(ZZ(other.index()))
            return self.ambient().open_subgroup(self.ambient().finite_extension(degree))
        raise NotImplementedError(
            "the compositum must be supplied with its exact closure embedding"
        )

    def _repr_(self) -> str:
        return f"Gal({self.algebraic_closure()} / {self.fixed_field()}) inside {self._ambient}"


class OpenGaloisSubgroupConjugacyClass(SageObject):
    r"""The conjugacy class obtained by forgetting (E\hookrightarrow\bar K)."""

    def __init__(self, ambient, extension_field) -> None:
        self._ambient = ambient
        if isinstance(extension_field, FiniteGaloisExtension):
            if extension_field.base_field() is not ambient.base_field():
                raise ValueError("the extension has the wrong ambient base field")
            self._extension_field = extension_field.field()
            self._base_embedding = extension_field.base_embedding()
        else:
            self._extension_field = own_ring(extension_field)
            base_embeddings = exact_embeddings(
                ambient.base_field(), self._extension_field
            )
            if len(base_embeddings) != 1:
                raise ValueError(
                    "the K-structure must be supplied as finite extension data"
                )
            self._base_embedding = base_embeddings[0]

    def ambient(self):
        return self._ambient

    def fixed_field(self):
        return self._extension_field

    def base_embedding(self):
        return self._base_embedding

    def index(self):
        from dzack_research.preamble.categories.group.profinite.galois_quotient import (
            _relative_degree,
        )

        return _relative_degree(self._ambient.base_field(), self._extension_field)

    def representative(self, embedding=None):
        if embedding is None:
            candidates = [
                candidate
                for candidate in exact_embeddings(
                    self._extension_field,
                    self._ambient.algebraic_closure(),
                )
                if all(
                    candidate(self._base_embedding(generator))
                    == self._ambient.base_embedding()(generator)
                    for generator in field_generators(self._ambient.base_field())
                )
            ]
            if not candidates:
                raise ValueError(
                    "the K-extension has no compatible embedding in the chosen closure"
                )
            embedding = candidates[0]
        stage = self._ambient.extension_data(
            self._extension_field,
            embedding=embedding,
            base_embedding=self._base_embedding,
        )
        return self._ambient.open_subgroup(stage)

    def __eq__(self, other) -> bool:
        if not isinstance(other, OpenGaloisSubgroupConjugacyClass):
            return False
        if other._ambient is not self._ambient or other.index() != self.index():
            return False
        return any(
            all(
                isomorphism(self._base_embedding(generator))
                == other._base_embedding(generator)
                for generator in field_generators(self._ambient.base_field())
            )
            for isomorphism in exact_embeddings(
                self._extension_field, other._extension_field
            )
        )

    def __hash__(self) -> int:
        return hash((id(self._ambient), self.index()))

    def _repr_(self) -> str:
        return (
            f"Conjugacy class of index-{self.index()} open subgroups of "
            f"{self._ambient} corresponding to {self._extension_field}"
        )


def open_absolute_galois_subgroup(ambient, extension, embedding=None):
    return ambient.open_subgroup(extension, embedding=embedding)


__all__ = [
    "OpenAbsoluteGaloisSubgroup",
    "OpenAbsoluteGaloisSubgroups",
    "OpenGaloisSubgroupConjugacyClass",
    "OpenSubgroupInclusion",
    "open_absolute_galois_subgroup",
]
