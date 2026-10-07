"""Certificate-consistency checks for stored lattice cards."""

import frontmatter

from latticedb import certificates, corpus, genus, records
from latticedb.certificates import Certificates
from latticedb.corpus import Corpus


def problems(loaded: Corpus, held: Certificates) -> list[str]:
    found: list[str] = []
    for entry in loaded.entries:
        missing = [name for name in ("rank", "gram_tensor", "signature", "determinant", "definiteness") if getattr(entry.lattice, name) is None]
        if missing:
            found.append(f"{entry.path}: fields awaiting source transcription or enrichment: {', '.join(missing)}")
            continue
        metadata = corpus.front_matter(frontmatter.load(str(entry.path)))
        card_certifications = metadata.get("certifications")
        cited = card_certifications if isinstance(card_certifications, dict) else {}
        derive_name = f"{entry.lattice.tag} derive"
        derive_hash = certificates.certification_hash(
            derive_name, entry.lattice, records.derived_projection(metadata)
        )
        derive_log = held.get(derive_name)
        if (cited.get("derive") is not None or (derive_log and derive_log.hash is not None)) and not certificates.is_certified(
            held, derive_name, cited.get("derive"), derive_hash
        ):
            found.append(
                f"{entry.path}: Gram-derived fields contradict their completed computation certificate"
            )
        for field, (block_name, _) in genus.BLOCKS.items():
            computation = genus.name(entry.lattice.tag, field)
            certificate = held.get(computation)
            block = metadata.get(block_name)
            value = block.get(field) if isinstance(block, dict) else None
            local_name = f"{block_name}.{field}"
            expected_hash = certificates.certification_hash(
                computation, entry.lattice, genus.certified_value(field, value, entry.lattice)
            )
            if (
                cited.get(local_name) is not None
                or (certificate is not None and certificate.hash is not None)
            ) and not certificates.is_certified(
                held, computation, cited.get(local_name), expected_hash
            ):
                found.append(
                    f"{entry.path}: {block_name}.{field} contradicts its completed computation certificate"
                )
        found.extend(
            f"{entry.path}: {problem}"
            for problem in records.local_admission_problems(entry.lattice)
        )
    return found
