"""Homsets, homomorphisms, and automorphism groups for owned groups."""

from sage.categories.category import Category
from sage.categories.homset import Hom
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.objects import Objects
from sage.categories.sets_cat import Sets
from sage.groups.finitely_presented import FinitelyPresentedGroup
from sage.groups.free_group import FreeGroup_class
from sage.groups.indexed_free_group import IndexedFreeGroup
from sage.groups.libgap_morphism import GroupHomset_libgap, GroupMorphism_libgap
from sage.groups.libgap_wrapper import ParentLibGAP
from sage.groups.perm_gps.permgroup import PermutationGroup_generic
from sage.libs.gap.element import GapElement
from sage.libs.gap.libgap import libgap
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.rings.integer_ring import ZZ
from sage.rings.infinity import infinity

from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    category_packet,
)


def _element_to_engine(group, element):
    match group:
        case GroupAutomorphismGroup() | PermutationGroup_generic() | ParentLibGAP():
            return element.gap()
        case _:
            raise NotImplementedError(
                f"{group}'s GAP model does not retain an elementwise identification"
            )


def _element_from_engine(group, engine_element):
    match group:
        case GroupAutomorphismGroup():
            return group(engine_element, check=False)
        case PermutationGroup_generic() | ParentLibGAP():
            return group(engine_element)
        case _:
            raise NotImplementedError(
                f"{group}'s GAP model does not retain an elementwise identification"
            )


class IndexedFreeGroupHomomorphism(Morphism):
    r"""A morphism out of Sage's indexed free group.

    The indexed implementation is the honest free group on an arbitrary Sage
    set, but it has no elementwise GAP model.  Its universal morphisms are
    therefore evaluated directly on the public word representation instead
    of forcing this object through the unrelated libGAP representation path.
    """

    def __init__(self, parent, images) -> None:
        Morphism.__init__(self, parent)
        indices = self.domain().indices()
        set_homset = Hom(indices, self.codomain(), Sets())
        if isinstance(images, SetMorphism):
            if images.domain() is not indices or images.codomain() is not self.codomain():
                raise ValueError("the generator map has the wrong source or target")
            self._generator_morphism = images
        elif isinstance(images, dict):
            if indices.cardinality() == infinity:
                raise ValueError(
                    "an infinite indexed free group requires a set morphism on its index set"
                )
            missing = [index for index in indices if index not in images]
            if missing:
                raise ValueError(f"generator assignment omits {missing}")
            self._generator_morphism = SetMorphism(set_homset, images.__getitem__)
        elif callable(images):
            self._generator_morphism = SetMorphism(set_homset, images)
        else:
            raise TypeError("an indexed-free-group morphism is specified on its index set")

    def generator_morphism(self):
        return self._generator_morphism

    def _call_(self, element):
        element = self.domain()(element)
        value = self.codomain().one()
        for index, sign in element.to_word_list():
            image = self.generator_morphism()(index)
            value *= image if sign == 1 else image**-1
        return value

    def postcompose(self, morphism):
        if morphism.domain() is not self.codomain():
            raise ValueError("group-morphism composition requires matching middle groups")
        indices = self.domain().indices()
        return group_homset(self.domain(), morphism.codomain())(
            SetMorphism(
                Hom(indices, morphism.codomain(), Sets()),
                lambda index: morphism(self.generator_morphism()(index)),
            )
        )

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        if not isinstance(other.domain(), IndexedFreeGroup):
            return NotImplemented
        indices = other.domain().indices()
        return group_homset(other.domain(), self.codomain())(
            SetMorphism(
                Hom(indices, self.codomain(), Sets()),
                lambda index: self(other(other.domain().gen(index))),
            )
        )


class IndexedFreeGroupHomset(CategoricalHomset):
    """The canonical Hom-set out of an indexed free group."""

    Element = IndexedFreeGroupHomomorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        from dzack_research.preamble.categories.group.groups import OwnedGroups

        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
            homset_category=OwnedGroups(),
        )

    def _element_constructor_(self, images, **_options):
        return self.element_class(self, images)

    def _repr_(self):
        return f"Hom({self.domain()}, {self.codomain()})"


class GroupHomomorphism(GroupMorphism_libgap):
    """A group homomorphism represented by Sage's maintained GAP morphism."""

    def __mul__(self, other):
        if isinstance(other, IndexedFreeGroupHomomorphism):
            return other.postcompose(self)
        return super().__mul__(other)


class GroupHomset(GroupHomset_libgap, CategoricalHomset):
    """The canonical owned homset Hom(G,H)."""

    Element = GroupHomomorphism

    @staticmethod
    def __classcall__(cls, family, domain, codomain):
        return typecall(cls, family, domain, codomain)

    def __init__(self, hom_family, domain, codomain):
        from dzack_research.preamble.categories.group.groups import OwnedGroups
        self._family = hom_family
        self._end_family = None
        self._aut_family = None
        self._domain_object = domain
        self._codomain_object = codomain
        self._super_categories_for_classes = [Objects()]
        Category.__init__(self)
        GroupHomset_libgap.__init__(
            self, domain, codomain, category=OwnedGroups(), check=False
        )

    def _element_constructor_(self, images, check=True, **options):
        if isinstance(images, dict):
            return self._from_group_generator_images(images, check=check)
        morphism = GroupHomset_libgap._element_constructor_(
            self, images, check=check, **options
        )
        return morphism

    def _image_in_codomain(self, value):
        if getattr(value, "parent", lambda: None)() is self.codomain():
            return value
        return self.codomain()(value)

    def _from_group_generator_images(self, images, check=True):
        from dzack_research.preamble.categories.group.groups import _gap_model
        domain = self.domain()
        codomain = self.codomain()
        generators = tuple(domain.group_generators())
        if set(images) != set(generators):
            raise ValueError(
                "the assignment must name exactly the distinguished group generators"
            )
        generator_models = [_element_to_engine(domain, g) for g in generators]
        image_models = [
            _element_to_engine(codomain, self._image_in_codomain(images[g]))
            for g in generators
        ]
        if check:
            engine = libgap.GroupHomomorphismByImages(
                _gap_model(domain), _gap_model(codomain), generator_models, image_models
            )
            if engine.is_bool():
                raise ValueError("the images do not satisfy the domain relations")
        else:
            engine = libgap.GroupHomomorphismByImagesNC(
                _gap_model(domain), _gap_model(codomain), generator_models, image_models
            )
        return self.element_class(self, engine, check=False)

    def _repr_(self):
        return f"Hom({self.domain()}, {self.codomain()})"


@cached_function
def group_homset(domain, codomain):
    from dzack_research.preamble.categories.group.groups import OwnedGroups

    return OwnedGroups().Hom(domain, codomain)


class GroupAutomorphism(GroupHomomorphism):
    pass


class GroupAutomorphismGroups(Category):
    def super_categories(self):
        from dzack_research.preamble.categories.group.groups import OwnedGroups
        return [OwnedGroups()]

    class ParentMethods:
        @cached_method
        def _libgap_(self):
            from dzack_research.preamble.categories.group.groups import _finiteness, _gap_model
            if self.engine_subgroup() is not None:
                return self.engine_subgroup()
            group = self.domain()
            if isinstance(group, (FreeGroup_class, FinitelyPresentedGroup)):
                raise NotImplementedError(
                    f"Aut({group}) exists, but this engine does not compute it from a bare presentation"
                )
            if _finiteness(group) is not True:
                raise NotImplementedError(
                    f"the available GAP automorphism algorithm requires {group} finite"
                )
            return libgap.AutomorphismGroup(_gap_model(group))

        def one(self):
            from dzack_research.preamble.categories.group.groups import _gap_model
            return self(libgap.IdentityMapping(_gap_model(self.domain())), check=False)

        @cached_method
        def group_generators(self):
            from dzack_research.preamble.categories.group.groups import _finite_ordered_set
            return _finite_ordered_set(
                self(generator, check=False)
                for generator in self._libgap_().GeneratorsOfGroup()
            )

        def number_of_group_generators(self):
            return ZZ(self.group_generators().cardinality())

        def _repr_(self):
            if self.engine_subgroup() is not None:
                return f"Subgroup of Aut({self.domain()})"
            return f"Aut({self.domain()})"

    class ElementMethods:
        def inverse(self):
            return self.parent()(self.gap().InverseGeneralMapping(), check=False)

        def _composition_(self, right, homset):
            if right.parent() is not self.parent():
                raise ValueError("automorphisms must belong to one automorphism group")
            return self.parent()(right.gap() * self.gap(), check=False)


class GroupAutomorphismGroup(GroupHomset):
    Element = GroupAutomorphism

    @staticmethod
    def __classcall__(cls, hom_family, group, engine_subgroup=None):
        return typecall(cls, hom_family, group, engine_subgroup=engine_subgroup)

    def __init__(self, hom_family, group, engine_subgroup=None):
        GroupHomset.__init__(self, hom_family, group, group)
        self._engine_subgroup = engine_subgroup
        self._supergroup = self
        from dzack_research.preamble.categories.group.groups import (
            OwnedFiniteGroups,
            OwnedGroups,
            _finiteness,
        )

        categories = [GroupAutomorphismGroups(), OwnedGroups()]
        if _finiteness(group) is True:
            categories.append(OwnedFiniteGroups())
        refine(self, categories)

    def super_categories(self):
        packet = category_packet(self.base_category())
        group = self.domain()
        supers = [
            packet.Homs().Of(group, group),
            packet.Monos().Of(group, group),
            packet.Epis().Of(group, group),
        ]
        supers.extend(
            superpacket.Isos().Of(group, group)
            for superpacket in packet.super_packets()
            if group in superpacket.C()
        )
        if self.aut_family() is not None:
            supers.append(packet.Ends().Of(group))
            supers.extend(
                superpacket.Auts().Of(group)
                for superpacket in packet.super_packets()
                if group in superpacket.C()
            )
        return supers

    def identity(self):
        from dzack_research.preamble.categories.group.groups import _gap_model

        return self(libgap.IdentityMapping(_gap_model(self.domain())), check=False)

    one = identity
    identity_automorphism = identity

    def engine_subgroup(self):
        return self._engine_subgroup

    def supergroup(self):
        return self._supergroup

    def set_supergroup(self, supergroup):
        self._supergroup = supergroup

    def _element_constructor_(self, images, check=True, **options):
        if isinstance(images, GapElement):
            automorphism = self.element_class(self, images, check=False)
        else:
            automorphism = super()._element_constructor_(images, check=check, **options)
        if check and not bool(automorphism.gap().IsBijective()):
            raise ValueError("the endomorphism is not invertible")
        return automorphism

    def _subgroup_from_engine(self, engine_subgroup):
        subgroup = GroupAutomorphismGroup(
            self.hom_family(),
            self.domain(),
            engine_subgroup=engine_subgroup,
        )
        subgroup.set_supergroup(self)
        return subgroup
