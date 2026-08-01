r"""Modules with a chosen ordered direct-sum decomposition.

The decomposition object is still the module: this category records its
ordered summand subobjects without changing the module category it already
belongs to.  A lattice and a module with a group action therefore use the same
direct-sum surface; their own categories supply the objects and morphisms.
"""

from typing import Any

from sage.categories.category import Category
from sage.categories.sets_cat import Sets


class DirectSumObjects(Category):
    r"""Objects with an ordered tuple of summand subobjects."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "direct-sum objects"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        r"""Methods determined by the chosen direct-sum decomposition."""

        def summands(self: Any) -> tuple:
            r"""Return the ordered tuple of summand subobjects."""
            return self._summands


def _expand_direct_sum_hom_dict(domain: Any, mapping: dict) -> list:
    r"""Expand subobject images to images of the generators of ``domain``."""
    images: dict[Any, Any] = {}
    for source, target in mapping.items():
        if source in Subobjects():
            source_images = source.embedded_gens()
            if target in Subobjects():
                target_images = target.embedded_gens()
            elif isinstance(target, (list, tuple)):
                target_images = tuple(target)
            else:
                assert len(source_images) == 1, (
                    "a single image requires a rank-1 source subobject; "
                    f"rank={len(source_images)}"
                )
                target_images = (target,)
            assert len(source_images) == len(target_images), (
                "source and target image counts differ: "
                f"{len(source_images)} != {len(target_images)}"
            )
            for source_image, target_image in zip(source_images, target_images):
                images[source_image] = target_image
        else:
            if target in Subobjects():
                assert target.rank() == 1, (
                    "a generator can map to a subobject only when its rank is 1"
                )
                target = target.embedded_gens()[0]
            images[source] = target

    ordered = []
    for generator in domain.gens():
        assert generator in images, f"missing image for generator {generator}"
        ordered.append(images[generator])
    return ordered
