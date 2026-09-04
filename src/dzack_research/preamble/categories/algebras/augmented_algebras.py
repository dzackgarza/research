"""Algebras equipped with an augmentation morphism to the base ring."""

from sage.categories.map import Map
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    FramedAlgebras,
    OwnedAlgebras,
    _OwnedAlgebraParent,
    _default_structure_map,
    algebra_homset,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.algebras.free_algebras import (
    AlternatingAlgebras,
    FreeAlgebras,
    GradedFreeAlgebras,
    SymmetricAlgebras,
    TensorAlgebras,
)


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
        generator to \(0\); the augmented algebra is its domain, interned on
        that choice.
        """
        from dzack_research.preamble.categories.algebras.free_algebras import SymmetricAlgebraOn

        ring = self.base_ring()
        polynomials = SymmetricAlgebraOn(ring, ("x",))
        label = next(iter(polynomials.algebra_generating_set()))
        return augmented_algebra(polynomials.Mor(ring)({label: ring.zero()}))

    @classmethod
    def _repr_object_names(cls):
        return "augmented algebras"

    def super_categories(self):
        return [Algebras(self.base_ring())]

    def _call_(self, augmentation):
        return augmented_algebra(augmentation)

    class ParentMethods:
        def is_augmented(self) -> bool:
            return True

        @cached_method
        def augmentation(self):
            return algebra_homset(self, self._preamble_augmentation_codomain)(
                dict(self._preamble_augmentation_images)
            )


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
        generator to \(0\); the augmented algebra is its domain, interned on
        that choice.
        """
        from dzack_research.preamble.categories.algebras.free_algebras import SymmetricAlgebraOn

        ring = self.base_ring()
        polynomials = SymmetricAlgebraOn(ring, ("x",))
        label = next(iter(polynomials.algebra_generating_set()))
        return augmented_algebra(polynomials.Mor(ring)({label: ring.zero()}))

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


class _AlgebraWithChosenAugmentation(_OwnedAlgebraParent):
    r"""An algebra interned on a chosen family of generator images."""

    def __init__(self, engine, base_ring, labels, augmentation_images, augmentation_codomain) -> None:
        self._preamble_augmentation_images = augmentation_images
        self._preamble_augmentation_codomain = augmentation_codomain
        engine_map = engine.coerce_map_from(_engine_ring(base_ring))
        _OwnedAlgebraParent.__init__(self, engine, base_ring, labels, engine_map)


def _augmentation_codomain_is_allowed(domain, base, codomain) -> bool:
    return _engine_ring(codomain) is _engine_ring(base)


def _graded_algebra_placement(domain, base):

    placement = []
    try:
        monoid = domain.grading_monoid()
        placement.append(GradedAlgebras(base, monoid))
        placement.append(GradedAugmentedAlgebras(base, monoid))
    except AttributeError:
        return placement
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


def augmented_algebra(augmentation):
    r"""Return the domain of ``augmentation``, as an augmented algebra.

    An augmentation of an \(R\)-algebra is an algebra morphism \(A\to R\).
    When \(A\) is graded, the unit-degree piece \(A_u\) is a subalgebra, and
    \(A\) is an \(A_u\)-algebra; an augmentation of that algebra is a map
    \(A\to A_u\).
    """
    if not isinstance(augmentation, Map):
        raise TypeError("an augmentation is an algebra morphism to the base ring")
    domain = augmentation.domain()
    base = _owned_ring(domain.base_ring())
    if domain not in Algebras(base):
        raise TypeError(f"{domain} is not an algebra over {base}")
    aug_codomain = _owned_ring(augmentation.codomain())
    if not _augmentation_codomain_is_allowed(domain, base, aug_codomain):
        raise TypeError(
            f"an augmentation of {domain} is a morphism to {base}"
        )
    if domain not in FramedAlgebras(base):
        raise TypeError(
            "an augmentation is specified by the images of a represented algebra generating set"
        )
    labels = tuple(domain.algebra_generating_set())
    images = tuple(
        (label, augmentation(domain.algebra_generator(label))) for label in labels
    )
    algebra = _AlgebraWithChosenAugmentation(
        _engine_ring(domain),
        base,
        labels,
        images,
        aug_codomain,
    )
    algebra._preamble_structure_map = _default_structure_map(base, algebra)
    placement = [
        Algebras(base),
        OwnedAlgebras(base),
        FramedAlgebras(base),
        AugmentedAlgebras(base),
    ]
    placement.extend(_graded_algebra_placement(domain, base))
    return refine(algebra, placement)
