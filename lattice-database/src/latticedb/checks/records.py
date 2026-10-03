"""Mathematical checks of fields that a lattice card states."""

from pydantic import ValidationError

from latticedb import records
from latticedb.corpus import Corpus


def problems(loaded: Corpus) -> list[str]:
    found: list[str] = []
    for entry in loaded.entries:
        missing = [name for name in ("rank", "gram_tensor", "signature", "determinant", "definiteness") if getattr(entry.lattice, name) is None]
        if missing:
            found.append(f"{entry.path}: fields awaiting source transcription or enrichment: {', '.join(missing)}")
            continue
        try:
            entry.lattice._well_defined()
        except ValidationError as error:
            found.extend(f"{entry.path}: {'.'.join(str(part) for part in problem['loc'])}: {problem['msg']}" for problem in error.errors())
            continue
        found.extend(
            f"{entry.path}: {problem}"
            for problem in records.gram_problems(
                entry.lattice.gram_tensor, entry.lattice.families
            )
        )
        found.extend(
            f"{entry.path}: {problem}"
            for problem in records.local_admission_problems(entry.lattice)
        )
    return found
