r"""Archive reconciliation for orthogonal complements of formed embeddings."""

from dzack_research.preamble.all import QQ, FreeModule


def test_form_embedding_orthogonal_complement_is_the_pairing_kernel_with_restricted_form() -> None:
    line_module = FreeModule(QQ, 1)
    ambient_module = FreeModule(QQ, 3)
    line = line_module.equip_bilinear_form(QQ, [[1]])
    ambient = ambient_module.equip_bilinear_form(QQ, [[1, 0, 0], [0, 2, 0], [0, 0, 3]])
    ambient_generators = tuple(ambient.module_generators())
    embedding = line.Mono(ambient)(
        {line.module_generating_set()[0]: ambient_generators[0]}
    )

    complement = embedding.orthogonal_complement()
    inclusion = complement.inclusion()

    assert inclusion.codomain() is ambient
    assert complement.module_rank() == 2
    images = tuple(inclusion(generator) for generator in complement.module_generators())
    assert ambient_generators[1] in images
    assert ambient_generators[2] in images
    assert all(ambient.b(image, ambient_generators[0]) == 0 for image in images)
    assert complement.is_nondegenerate()


def test_identity_form_embedding_has_zero_orthogonal_complement_for_nondegenerate_form() -> None:
    module = FreeModule(QQ, 2)
    formed = module.equip_bilinear_form(QQ, [[0, 1], [1, 0]])
    embedding = formed.Mono(formed)(
        {
            label: formed.module_generator(label)
            for label in formed.module_generating_set()
        }
    )

    complement = embedding.orthogonal_complement()
    assert complement.module_rank() == 0
    assert complement.inclusion().codomain() is formed
