"""Algebras equipped with an augmentation morphism to the base ring."""

from sage.categories.map import Map
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    UnitalMultiplicativeAlgebraMorphism,
    _algebra_on_module,
    _root_algebra_law_decisions,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    AlternatingAlgebras,
    FreeAlgebras,
    GradedFreeAlgebras,
    SymmetricAlgebras,
    TensorAlgebras,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _owned_ring,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)


class _SelectedAugmentationModuleMorphism(ModuleMorphism):
    r"""The selected augmentation transported to the structured algebra endpoint."""

    def __init__(self, parent, augmentation, source_algebra) -> None:
        self._selected_augmentation = augmentation
        self._source_algebra = source_algebra
        super().__init__(
            parent,
            lambda element: augmentation(source_algebra(element)),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return self._selected_augmentation.linearity_decision()


class _SelectedAugmentationAlgebraMorphism(UnitalMultiplicativeAlgebraMorphism):
    r"""An augmentation whose algebra laws are part of the selected augmentation datum."""

    def _multiplicativity_derivation(self):
        return True

    def _unit_preservation_derivation(self):
        return True


class AugmentedAlgebras(OwnedCategoryOverBaseRing):
    r"""Associative unital \(R\)-algebras equipped with an augmentation.

    An \(R\)-algebra is a ring \(A\) together with a ring homomorphism
    \(R\to A\). If it is further equipped with an \(R\)-algebra homomorphism
    the other way,
    \[
    \varepsilon\colon A\to R,
    \]
    then it is an *augmented* \(R\)-algebra. The kernel of \(\varepsilon\) is
    the augmentation ideal. This is the nLab definition of an augmented
    algebra (Cartan–Eilenberg: a supplemented algebra).
    """

    def an_object(self):
        r"""``R[x]`` augmented by evaluation at zero.

        The augmentation is the algebra morphism \(R[x]\to R\) sending the
        generator to \(0\); the structured object retains that exact algebra
        and selected morphism as its data.
        """

        ring = self.base_ring()
        polynomials = ring.free_module(("x",)).symmetric_algebra()
        label = next(iter(polynomials.algebra_generating_set()))
        return self(polynomials.Mor(ring)({label: ring.zero()}))

    @classmethod
    def _repr_object_names(cls):
        return "augmented algebras"

    def super_categories(self):
        return [Algebras(self.base_ring()).Associative().Unital()]

    def _call_(self, augmentation):
        return _augmented_algebra(augmentation)

    class ParentMethods:
        def __init__(self, selected_augmentation=None, **rest) -> None:
            assert selected_augmentation is not None, (
                "an augmented algebra needs its augmentation A -> R, but none was given"
            )
            self._preamble_selected_augmentation = selected_augmentation
            super().__init__(**rest)

        def is_augmented(self) -> bool:
            return True

        @cached_method
        def augmentation(self):
            selected = self._preamble_selected_augmentation
            source = self.unformed_module()
            target = selected.codomain()
            linear = _SelectedAugmentationModuleMorphism(
                self.module_category().Mor(self, target),
                selected,
                source,
            )
            parent = Algebras(self.base_ring()).Associative().Unital().Mor(
                self, target
            )
            return _SelectedAugmentationAlgebraMorphism(parent, linear)


class GradedAugmentedAlgebras(OwnedCategoryOverBaseRing):
    r"""Graded algebras over an augmented \(R\)-algebra.

    Let \(B\) be an augmented \(R\)-algebra and let \(A\) be a graded
    \(B\)-algebra that is itself augmented over \(B\). The composite of
    the two augmentations is an augmentation of \(A\) over \(R\):
    \[
    A \to B \to R.
    \]
    For a connected grading, \(B = A_u = R\) and the second map is the
    identity. This is the nLab graded-plus-augmented situation
    (Cartan–Eilenberg: a supplemented graded algebra).
    """

    def an_object(self):
        r"""``R[x]`` augmented by evaluation at zero.

        The augmentation is the algebra morphism \(R[x]\to R\) sending the
        generator to \(0\); the structured object retains that exact algebra
        and selected morphism as its data.
        """

        ring = self.base_ring()
        polynomials = ring.free_module(("x",)).symmetric_algebra()
        label = next(iter(polynomials.algebra_generating_set()))
        return AugmentedAlgebras(ring)(polynomials.Mor(ring)({label: ring.zero()}))

    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None):
        graded = GradedAlgebras(base_ring, grading_monoid)
        return OwnedCategoryOverBaseRing.__classcall__(
            cls, graded.base_ring(), graded.grading_monoid()
        )

    def __init__(self, base_ring, grading_monoid) -> None:
        self._grading_monoid = grading_monoid
        super().__init__(base_ring)

    def grading_monoid(self):
        return self._grading_monoid

    def _repr_object_names(self) -> str:
        return f"graded augmented algebras over {self.base()}"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self.grading_monoid())

    def super_categories(self):
        return [
            GradedAlgebras(self.base_ring(), self.grading_monoid()),
            AugmentedAlgebras(self.base_ring()),
        ]

    class ParentMethods:
        def ground_ring_augmentation(self):
            r"""The composite augmentation \(A\to A_u\to R\).

            The first arrow is the augmentation of \(A\) as an \(A_u\)-algebra.
            The second is the augmentation of \(A_u\) as an \(R\)-algebra;
            when \(A_u = R\) that second map is the identity.
            """
            unit = self.graded_piece(self.grading_monoid().monoidal_unit())
            to_unit = self.augmentation()
            ground = self.algebra_base_ring()
            match unit:
                case _ if unit in AugmentedAlgebras(ground):
                    return unit.augmentation() * to_unit
                case _:
                    return unit.algebra_structure_morphism() * to_unit


def _augmentation_codomain_is_allowed(domain, base, codomain) -> bool:
    _ = domain
    return codomain is base


def _declared_graded_algebra_category(domain):
    for category in domain.category().all_super_categories(proper=False):
        if isinstance(category, GradedAlgebras):
            return category
    return None


def _graded_algebra_placement(domain, base):

    placement = []
    algebras = Algebras(base)
    match domain in algebras.Commutative():
        case True:
            placement.append(algebras.Commutative())
        case False:
            pass
    graded = _declared_graded_algebra_category(domain)
    if graded is None:
        return placement
    monoid = graded.grading_monoid()
    placement.append(GradedAlgebras(base, monoid))
    placement.append(GradedAugmentedAlgebras(base, monoid))
    if domain in FreeAlgebras(base):
        placement.append(FreeAlgebras(base))
    if domain in GradedFreeAlgebras(base):
        placement.append(GradedFreeAlgebras(base))
    if domain in SymmetricAlgebras(base):
        placement.append(SymmetricAlgebras(base))
    if domain in TensorAlgebras(base):
        placement.append(TensorAlgebras(base))
    if domain in AlternatingAlgebras(base):
        placement.append(AlternatingAlgebras(base))
    return placement


def _augmented_algebra(augmentation):
    r"""Return the domain of ``augmentation``, as an augmented algebra.

    An augmentation of an \(R\)-algebra is an algebra morphism \(A\to R\).
    When \(A\) is graded, the unit-degree piece \(A_u\) is a subalgebra, and
    \(A\) is an \(A_u\)-algebra; an augmentation of that algebra is a map
    \(A\to A_u\).
    """
    match isinstance(augmentation, Map):
        case True:
            pass
        case False:
            raise TypeError(
                f"an augmentation is an algebra morphism A -> R, but {augmentation!r} is not a map"
            )
    domain = augmentation.domain()
    base = _owned_ring(domain.base_ring())
    algebras = Algebras(base).Associative().Unital()
    match domain in algebras:
        case True:
            pass
        case False:
            raise TypeError(
                f"an augmentation {augmentation} needs its domain {domain} to be an algebra over {base}, but it is not"
            )
    aug_codomain = _owned_ring(augmentation.codomain())
    match _augmentation_codomain_is_allowed(domain, base, aug_codomain):
        case True:
            pass
        case False:
            raise TypeError(
                f"an augmentation of {domain} is a morphism to {base}, but {augmentation} ends at "
                f"{augmentation.codomain()}"
            )
    selected = algebras.Mor(domain, aug_codomain)(augmentation)
    placement = _graded_algebra_placement(domain, base)
    law_decisions = _root_algebra_law_decisions(domain)
    if _declared_graded_algebra_category(domain) is not None:
        law_decisions["grading"] = domain.grading_compatibility_decision()
    data = {"selected_augmentation": selected}
    if domain.is_framed_algebra():
        framing_owner = domain.algebra_framing_owner()
        data["algebra_generating_family"] = domain.algebra_generators()
        data["algebra_framing_source"] = domain.algebra_framing_source()
        data["algebra_framing_owner"] = framing_owner
    return _algebra_on_module(
        domain,
        domain.multiplication_morphism(),
        placement=(AugmentedAlgebras(base), *tuple(placement)),
        unit=domain.one(),
        construction_data=data,
        law_decisions=law_decisions,
    )
