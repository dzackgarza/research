r"""M0 constructor contracts for module actions and selected presentations.

These examples are committed unverified under the standing preamble policy.
They distinguish the chosen presentation from the underlying module while
requiring every constructor route to expose and use the same scalar-action
morphism ``R -> End_Ab(U(M))``.
"""

from dzack_research.preamble.all import (
    ZZ,
)

from dzack_research.preamble.categories.sets import finite_ordered_set


















def test_module_morphism_lifts_to_the_selected_presentation_diagrams() -> None:
    source_target = ZZ.free_module(finite_ordered_set(("x", "y")))
    source_relations = ZZ.free_module(finite_ordered_set(("r",)))
    source = source_relations.module_category().Mor(source_relations, source_target)(
        {"r": source_target.scalar_multiple(ZZ(6), source_target.module_generator("y"))}
    ).cokernel()

    target_target = ZZ.free_module(finite_ordered_set(("u", "v")))
    target_relations = ZZ.free_module(finite_ordered_set(("s",)))
    target = target_relations.module_category().Mor(target_relations, target_target)(
        {"s": target_target.scalar_multiple(ZZ(3), target_target.module_generator("v"))}
    ).cokernel()

    morphism = source.module_category().Mor(source, target)(
        {
            "x": target.module_generator("u"),
            "y": target.module_generator("v"),
        }
    )
    square = morphism.selected_presentation_morphism()

    assert square.domain() is source.presentation_object()
    assert square.codomain() is target.presentation_object()
    assert square.right() * source.presentation() == target.presentation() * square.left()
    source.presentation_projection()
    target_projection = target.presentation_projection()
    for label in source.module_generating_set():
        lifted = square.right()(source.presentation().codomain().module_generator(label))
        assert target_projection(lifted) == morphism(source.module_generator(label))










