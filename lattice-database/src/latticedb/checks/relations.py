"""Cross-card and catalogue checks."""

from latticedb import corpus


def problems(loaded: corpus.Corpus) -> list[str]:
    return [
        *corpus.problems(list(loaded.entries), loaded.families, loaded.retired),
        *corpus.morphism_problems(list(loaded.morphisms), list(loaded.entries), loaded.retired),
        *corpus.catalogue_problems(loaded),
    ]
