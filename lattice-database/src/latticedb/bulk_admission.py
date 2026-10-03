"""Admit indexed source forms as permanent lattice cards."""

import json
import re
from collections import defaultdict
from dataclasses import dataclass
from importlib.metadata import version
from pathlib import Path
from subprocess import run

import frontmatter
from pydantic import ValidationError

from latticedb import arithmetic, certificates, corpus, records
from latticedb.model import Lattice, Yaml


@dataclass(frozen=True)
class Pending:
    source_id: str
    source_gram: tuple[tuple[int, ...], ...]
    scale: int
    declared: dict[str, Yaml]
    prose: str
    label: str


def _source_paths(root: Path, source: str, source_ids: list[str]) -> dict[str, Path]:
    found: dict[str, Path] = {}
    if not source_ids:
        return found
    patterns = [argument for source_id in source_ids for argument in ("-e", f"^id: {re.escape(source_id)}$")]
    search = run(["rg", "-l", *patterns, str(root / "lattices" / "source")], capture_output=True, text=True, check=False)
    assert search.returncode in (0, 1), search.stderr
    for name in search.stdout.splitlines():
        path = Path(name)
        document = frontmatter.load(str(path))
        assert document.get("source") == source
        source_id = document["id"]
        assert isinstance(source_id, str) and source_id not in found
        found[source_id] = path
    return found


def admit(root: Path, source: str, entries: list[Pending]) -> tuple[int, int]:
    """Move pending forms to validated lattice cards, linking isometric repeats."""
    source_paths = _source_paths(root, source, [entry.source_id for entry in entries])
    loaded = corpus.load(root)
    written = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    by_name = {lattice.name for lattice in written.values()}
    by_gram = {lattice.gram_tensor for lattice in written.values()}
    by_invariants: dict[records.IsometryInvariants, dict[str, Lattice]] = defaultdict(dict)
    for tag, lattice in written.items():
        if lattice.definite is not None:
            by_invariants[records.isometry_invariants(lattice)][tag] = lattice
    held = certificates.load(root)
    admitted = repeated = 0
    try:
        for entry in entries:
            source_path = source_paths.get(entry.source_id)
            if source_path is None:
                continue
            tag = source_path.stem
            gram = records.gram_tensor(entry.declared["gram_tensor"])
            assert not records.gram_problems(gram, ())
            record = records.derive({"tag": tag, **entry.declared})
            try:
                lattice = Lattice.model_validate(record)
            except ValidationError as error:
                raise AssertionError(f"{entry.source_id}: {error}") from error
            assert lattice.determinant * entry.scale**lattice.rank == arithmetic.determinant(entry.source_gram), entry.source_id
            invariants = records.isometry_invariants(lattice)
            candidates = by_invariants[invariants]
            matches = [other for other in candidates.values() if other.gram_tensor == lattice.gram_tensor or arithmetic.is_isometric(other.gram_tensor, lattice.gram_tensor)]
            assert len(matches) <= 1, f"{entry.source_id}: multiple existing records are isometric"
            if matches:
                canonical = matches[0]
                canonical_path = root / "lattices" / f"{canonical.tag}.md"
                document = frontmatter.load(str(canonical_path))
                metadata = dict(document.metadata)
                references = list(metadata["references"])
                source_reference = entry.declared["references"][0]
                if source_reference not in references:
                    references.append(source_reference)
                    metadata["references"] = references
                    relation = f"{entry.label} at `{entry.source_id}` is isometric to this lattice"
                    relation += f" twisted by {entry.scale}." if entry.scale != 1 else "."
                    canonical_path.write_text(records.record_text(metadata, document.content + "\n\n" + relation))
                reason = f"{entry.label} {entry.source_id} = {canonical.tag}"
                reason += f"({entry.scale})" if entry.scale != 1 else ""
                expression = f".[{json.dumps(tag)}] = {json.dumps(reason)}"
                run(["yq", "-i", expression, str(root / "retired-tags.yaml")], check=True)
                run(["trash", str(source_path)], check=True)
                repeated += 1
                continue
            assert lattice.gram_tensor not in by_gram
            assert not records.admission_problems(lattice, candidates)
            assert tag not in written and tag not in loaded.retired and lattice.name not in by_name
            destination = root / "lattices" / f"{tag}.md"
            assert not destination.exists()
            source_path.write_text(records.record_text(record, entry.prose))
            source_path.rename(destination)
            held[f"{tag} derive"] = certificates.Certificate(inputs=certificates.gram_digest(lattice), by=f"latticedb {version('latticedb')}")
            written[tag] = lattice
            by_name.add(lattice.name)
            by_gram.add(lattice.gram_tensor)
            candidates[tag] = lattice
            admitted += 1
    finally:
        certificates.save(root, held)
    return admitted, repeated
