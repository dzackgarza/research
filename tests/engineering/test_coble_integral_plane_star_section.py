"""Independently replay the complete finite-to-integral Coble plane section."""

import ast
import json
import hashlib
import gzip
import importlib.util
import re
import subprocess
from collections import Counter, deque
from itertools import combinations
from math import gcd
from pathlib import Path

import pytest


def test_complete_integral_flag_certificate_manifest(tmp_path):
    """Check the permanent provenance ledger of the 32-shard full CI run."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    manifest = json.loads((folder / "coble_integral_flag_certificate_manifest.json").read_text())
    assert manifest["schema"] == "coble-integral-flag-certificate-manifest-v1"
    assert manifest["workflow_run"] == 44170494099
    assert manifest["source_commit"] == "c08aeb6baa98cfcd2a39c46141432f4ce9c92661"
    assert manifest["line_certificate_sha256"] == hashlib.sha256(
        (folder / "coble_singular_integral_representatives.json").read_bytes()).hexdigest()
    assert manifest["plane_certificate_sha256"] == hashlib.sha256(
        (folder / "coble_plane_integral_star_section.json").read_bytes()).hexdigest()
    assert manifest["artifact_id"] == 14371631974
    assert manifest["sage_image"] == "ghcr.io/dzackgarza/sage:develop"
    assert manifest["sage_image_digest"] == (
        "sha256:12e5716067b5cf2fd34c00e9ba97e9c09d51a70664de817f4ae29743b64c5f61")
    workflow = (folder.parents[1] / ".github" / "workflows" /
                "coble-integral-flag-certificate.yml").read_text()
    assert ("image: ghcr.io/dzackgarza/sage@" +
            manifest["sage_image_digest"]) in workflow
    assert manifest["total_edges"] == 569160
    assert manifest["shard_count"] == len(manifest["shards"]) == 32
    assert [row["index"] for row in manifest["shards"]] == list(range(32))
    assert [row["records"] for row in manifest["shards"]] == [
        24 * len(range(i, 23715, 32)) for i in range(32)]
    assert sum(row["records"] for row in manifest["shards"]) == 569160
    for key in ("file_sha256", "records_sha256"):
        digests = [row[key] for row in manifest["shards"]]
        assert len(set(digests)) == 32
        assert all(len(digest) == 64 and
                   all(c in "0123456789abcdef" for c in digest)
                   for digest in digests)
    spec = importlib.util.spec_from_file_location(
        "coble_manifest_audit", folder / "coble_kernel_public_incidence_audit.py")
    assert spec is not None and spec.loader is not None
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    # Exercise archive identity separately from mathematical verification:
    # the latter is deliberately not replaced by a successful hash check.
    specimen = tmp_path / "shard-4.jsonl.gz"
    header = {"schema": "coble-exact-kernel-transport-shard-v1",
              "shard_index": 4, "shard_count": 32,
              "expected_edges": manifest["shards"][4]["records"],
              "line_certificate_sha256": manifest["line_certificate_sha256"],
              "plane_certificate_sha256": manifest["plane_certificate_sha256"]}
    with gzip.open(specimen, "wt", encoding="utf-8") as stream:
        stream.write(json.dumps(header) + "\n")
    synthetic = json.loads(json.dumps(manifest))
    synthetic["shards"][4]["file_sha256"] = hashlib.sha256(specimen.read_bytes()).hexdigest()
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(json.dumps(synthetic))
    assert audit.verify_integral_shard_manifest([specimen], manifest_path) == {4}
    with specimen.open("ab") as stream:
        stream.write(b"corruption")
    with pytest.raises(AssertionError, match="archive SHA-256"):
        audit.verify_integral_shard_manifest([specimen], manifest_path)


def test_permanent_integral_flag_release_matches_all_32_shard_digests():
    """The permanent 541 MB release retains the exact CI-certified archives."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    manifest = json.loads((folder / "coble_integral_flag_certificate_manifest.json").read_text())
    release = json.loads((folder / "coble_integral_flag_permanent_release.json").read_text())
    assert release["schema"] == "coble-integral-flag-permanent-release-v1"
    assert release["release_url"] == (
        "https://github.com/dzackgarza/research/releases/tag/coble-integral-flags-v1")
    assert release["source_commit"] == manifest["source_commit"]
    assert release["source_workflow"] == manifest["workflow_run"]
    assert release["source_artifact_id"] == manifest["artifact_id"]
    assert release["total_edges"] == manifest["total_edges"] == 569160
    assert len(release["assets"]) == 32
    assert [a["index"] for a in release["assets"]] == list(range(32))
    assert len({a["asset_id"] for a in release["assets"]}) == 32
    assert release["total_archive_bytes"] == sum(a["bytes"] for a in release["assets"])
    assert release["total_archive_bytes"] == 541965486
    for asset, source in zip(release["assets"], manifest["shards"]):
        assert asset["index"] == source["index"]
        assert asset["name"] == f'shard-{asset["index"]}.jsonl.gz'
        assert asset["sha256"] == source["file_sha256"]
        assert asset["bytes"] > 0
        assert asset["download_url"] == (
            "https://github.com/dzackgarza/research/releases/download/"
            f'coble-integral-flags-v1/{asset["name"]}')


def test_complete_integral_flag_quotient_ci_record():
    """The archived independent full-flag descent has all 13 quotient fibres."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    transcript = (folder / "coble_integral_flag_quotient-run.txt").read_bytes()
    assert hashlib.sha256(transcript).hexdigest() == (
        "efb2f2d60b047113dcb86e63a859604e3c5941dbc12b1198c2ff8e6f224b0b51")
    text = transcript.decode()
    assert ("integral flags descended to thirteen G_Co orbits: "
            "[2160, 2160, 2160, 7560, 9450, 15120, 22680, 28350, "
            "45360, 69120, 75600, 138240, 151200]") in text
    assert "distinct line/plane quotient endpoints: 13" in text
    assert "exact integral flags classified: 569160" in text
    assert sum([2160, 2160, 2160, 7560, 9450, 15120, 22680, 28350,
                45360, 69120, 75600, 138240, 151200]) == 569160


def test_complete_integral_plane_parabolic_generators(tmp_path):
    """The finite-image certificate alone omits seven integral sign changes."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    result = subprocess.run(
        ["sage", "-c", "import runpy,sys;sys.argv=['parabolic'];runpy.run_path("
         "'computations/reports/coble_complete_plane_parabolic_generators.py',"
         "run_name='__main__')"],
        cwd=folder.parents[1], capture_output=True, text=True, check=True)
    assert "complete integral parabolic generator count: 28" in result.stdout
    assert "unchanged finite image order: 247726080" in result.stdout
    assert "even unipotent coefficient lattice index: 2" in result.stdout
    artifact = folder / "coble_complete_plane_parabolic_generators.json"
    payload = json.loads(artifact.read_text())
    assert payload["schema"] == "coble-complete-integral-plane-parabolic-v1"
    assert payload["generator_count"] == len(payload["generators_standard"]) == 28
    assert payload["finite_image_order"] == 247726080
    assert payload["even_unipotent_coefficient_index"] == 2
    assert payload["line_certificate_sha256"] == hashlib.sha256(
        (folder / "coble_singular_integral_representatives.json").read_bytes()).hexdigest()
    assert payload["plane_certificate_sha256"] == hashlib.sha256(
        (folder / "coble_plane_integral_star_section.json").read_bytes()).hexdigest()
    old = json.loads((folder / "coble_plane_integral_star_section.json").read_text())
    assert payload["generators_standard"][:21] == old["plane_stabilizer_generators_standard"]
    assert hashlib.sha256(artifact.read_bytes()).hexdigest() == (
        "a2af10a537cc16f4f555f318854b238d72254258a572d947d0ff775b99d87859")
    reproduced = tmp_path / "parabolic.json"
    subprocess.run(
        ["sage", "-c", "import runpy,sys;sys.argv=['parabolic','--output',"
         + repr(str(reproduced)) + "];runpy.run_path("
         "'computations/reports/coble_complete_plane_parabolic_generators.py',"
         "run_name='__main__')"],
        cwd=folder.parents[1], capture_output=True, text=True, check=True)
    assert reproduced.read_bytes() == artifact.read_bytes()


def test_coble_level_two_eichler_squares_fail_normal_generation():
    """A single additional root-pair relation completes E(2) modulo four."""
    import json
    from pathlib import Path
    from sage.all import GF, ZZ, identity_matrix, matrix

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    data = json.loads((folder / "coble_ambient_twenty_one_generators.json").read_text())
    generators = [matrix(ZZ, record["matrix_standard"])
                  for record in data["generators"][:18]]
    finite = [matrix(GF(2), generator) for generator in generators]
    inverse = [generator.inverse() for generator in finite]
    identity = identity_matrix(ZZ, 11)
    pivots = {}
    queue = []

    def admit(element):
        bits = sum(int(element[i, j]) << (11 * i + j)
                   for i in range(11) for j in range(11))
        while bits:
            pivot = bits.bit_length() - 1
            if pivot in pivots:
                bits ^= pivots[pivot]
            else:
                pivots[pivot] = bits
                queue.append(element)
                return

    for generator in generators:
        square = generator * generator
        assert all((square[i, j] - identity[i, j]) % 2 == 0
                   for i in range(11) for j in range(11))
        admit(matrix(GF(2), 11, 11, [
            int((square[i, j] - identity[i, j]) // 2) % 2
            for i in range(11) for j in range(11)
        ]))
    assert len(pivots) == 16
    position = 0
    while position < len(queue):
        element = queue[position]
        position += 1
        for generator, inv in zip(finite, inverse, strict=True):
            admit(generator * element * inv)
    assert len(pivots) == 44
    # The final two simple D7 roots differ by 2*d7, so their Eichler
    # transvections have the same reduction modulo two.  Their product
    # is an additional exact level-two relation, not a generator square.
    relation = generators[7] * generators[8]
    assert matrix(GF(2), relation) == identity_matrix(GF(2), 11)
    admit(matrix(GF(2), 11, 11, [
        int((relation[i, j] - identity[i, j]) // 2) % 2
        for i in range(11) for j in range(11)
    ]))
    position = 0
    while position < len(queue):
        element = queue[position]
        position += 1
        for generator, inv in zip(finite, inverse, strict=True):
            admit(generator * element * inv)
    assert len(pivots) == 54
    # The two explicit commuting character involutions complement the
    # Eichler congruence image, and the resulting 56 classes span the
    # *entire* independently certified Gamma(2)/Gamma(4).
    for record in data["generators"][19:21]:
        generator = matrix(ZZ, record["matrix_standard"])
        assert matrix(GF(2), generator) == identity_matrix(GF(2), 11)
        admit(matrix(GF(2), 11, 11, [
            int((generator[i, j] - identity[i, j]) // 2) % 2
            for i in range(11) for j in range(11)
        ]))
    assert len(pivots) == 56


def test_coble_fifty_six_contains_all_nineteen_eichler_normal_relations():
    """All normal generators have exact ordinary words of length at most four."""
    import hashlib
    import json
    import subprocess
    from pathlib import Path

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    artifact = folder / "coble_kernel_fifty_six_normal_relation_words.json"
    before = artifact.read_bytes()
    data = json.loads(before)
    assert data["schema"] == "coble-kernel-56-normal-relations-ordinary-words-v1"
    assert data["ordinary_sha256"] == hashlib.sha256(
        (folder / "coble_kernel_fifty_six_congruence_generators.json").read_bytes()
    ).hexdigest()
    assert data["ambient_sha256"] == hashlib.sha256(
        (folder / "coble_ambient_twenty_one_generators.json").read_bytes()
    ).hexdigest()
    assert data["relation_count"] == len(data["relations"]) == 19
    assert data["max_word_length"] == 4
    subprocess.run(["sage", str(folder / "coble_kernel_fifty_six_normal_relation_words.py")],
                   cwd=folder.parents[1], check=True, capture_output=True, text=True)
    assert artifact.read_bytes() == before


def test_coble_fifty_six_small_odd_local_images_are_full():
    """Exact classical recognition and rank-55 local lifting at small odd primes."""
    import hashlib
    import json
    import subprocess
    from pathlib import Path

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    artifact = folder / "coble_kernel_fifty_six_small_odd_local.json"
    before = artifact.read_bytes()
    data = json.loads(before)
    assert data["schema"] == "coble-kernel-56-small-odd-local-v1"
    assert data["source_sha256"] == hashlib.sha256(
        (folder / "coble_kernel_fifty_six_congruence_generators.json").read_bytes()
    ).hexdigest()
    assert [record["prime"] for record in data["records"]] == [3, 5, 7, 11, 13]
    assert all(record["contains_omega"] is True and
               record["orthogonal_type"] == "odd_dimension_11" and
               record["principal_p_layer_rank"] == 55 and
               record["adjoint_commutator_rank"] == 55 for record in data["records"])
    subprocess.run(["sage", str(folder / "coble_kernel_fifty_six_small_odd_local.py")],
                   cwd=folder.parents[1], check=True, capture_output=True, text=True)
    assert artifact.read_bytes() == before


def test_coble_fifty_six_unipotent_lie_lattice_is_full_away_from_two():
    """The exact commutator Lie lattice has index precisely 2^64."""
    import hashlib
    import json
    import subprocess
    from pathlib import Path

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    artifact = folder / "coble_kernel_fifty_six_lie_span.json"
    before = artifact.read_bytes()
    result = json.loads(before)
    assert result["schema"] == "coble-kernel-56-unipotent-lie-span-v1"
    assert result["source_sha256"] == hashlib.sha256(
        (folder / "coble_kernel_fifty_six_congruence_generators.json").read_bytes()
    ).hexdigest()
    assert result["diagonal_source_sha256"] == hashlib.sha256(
        (folder / "coble_singular_integral_representatives.json").read_bytes()
    ).hexdigest()
    assert len(result["unipotent_indices"]) == 46
    assert result["initial_rank"] == 46
    assert result["lie_rank"] == 55
    assert result["integral_index"] == 2**64
    subprocess.run(["sage", str(folder / "coble_kernel_fifty_six_lie_span.py")],
                   cwd=folder.parents[1], check=True, capture_output=True, text=True)
    assert artifact.read_bytes() == before


def test_coble_fifty_six_mod_three_full_orthogonal_image_certificate():
    """The 56 ordinary candidates have the full exact O(11,3) image."""
    import hashlib
    import json
    from pathlib import Path

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    certificate = json.loads((folder / "coble_kernel_fifty_six_mod_three_image.json").read_text())
    source = folder / "coble_kernel_fifty_six_congruence_generators.json"
    assert certificate["source_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    assert certificate["prime"] == 3
    assert certificate["matrix_count"] == 56
    expected = 2 * 3**25
    for i in range(1, 6):
        expected *= 3 ** (2 * i) - 1
    assert certificate["full_odd_orthogonal_order"] == expected
    assert certificate["generated_order"] == expected
    assert certificate["full_image"] is True


@pytest.mark.parametrize("start", range(0, 56, 8))
def test_coble_fifty_six_ordinary_elements_are_public_kernel_morphisms(start):
    """Each of the 56 ordinary candidates belongs to the owned kernel."""
    import json
    from pathlib import Path
    from sage_extensions.all import NamedLattices, ZZ as OwnedZZ

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    data = json.loads((folder / "coble_kernel_fifty_six_congruence_generators.json").read_text())
    lattice = NamedLattices.Tco
    labels = tuple(lattice.module_generating_set())
    group = lattice.O()
    kernel = lattice.stable_orthogonal_group()
    for row in data["generators"][start:start + 8]:
        entries = row["matrix_standard"]
        morphism = group({
            label: lattice.linear_combination({
                labels[j]: OwnedZZ(entries[j][i]) for j in range(11)
            })
            for i, label in enumerate(labels)
        })
        assert morphism in kernel


@pytest.mark.parametrize("start", range(0, 95, 10))
def test_coble_positive_schreier_generators_are_public_positive_kernel_morphisms(start):
    """Exact 95 ordinary Schreier generators belong to the public Otilde+ subgroup."""
    import hashlib
    import json
    from pathlib import Path
    from sage_extensions.all import NamedLattices, ZZ as OwnedZZ

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    data = json.loads((folder / "coble_kernel_positive_schreier_generators.json").read_text())
    assert data["schema"] == "coble-positive-kernel-ordinary-schreier-v1"
    assert data["generator_count"] == len(data["generators"]) == 95
    assert data["source_sha256"] == hashlib.sha256(
        (folder / "coble_kernel_fifty_six_congruence_generators.json").read_bytes()
    ).hexdigest()
    lattice = NamedLattices.Tco
    labels = tuple(lattice.module_generating_set())
    group = lattice.O()
    positive_kernel = lattice.stable_orthogonal_group().intersection(lattice.O_plus())
    for row in data["generators"][start:start + 10]:
        entries = row["matrix_standard"]
        morphism = group({
            label: lattice.linear_combination({
                labels[j]: OwnedZZ(entries[j][i]) for j in range(11)
            })
            for i, label in enumerate(labels)
        })
        assert morphism in positive_kernel


def test_coble_fifty_five_positive_elements_span_kernel_modulo_sixteen():
    """The 55-element positive subset generates every graded layer through 16."""
    import hashlib
    import json
    import subprocess
    from collections import deque
    from pathlib import Path
    from sage.all import GF, Integers, ZZ, identity_matrix, matrix

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    source = folder / "coble_kernel_positive_schreier_generators.json"
    artifact = folder / "coble_positive_kernel_fifty_five_generators.json"
    before = artifact.read_bytes()
    data = json.loads(before)
    assert data["schema"] == "coble-positive-kernel-55-ordinary-mod-sixteen-v1"
    assert data["source_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    assert data["generator_count"] == len(data["generators"]) == 55
    assert data["source_generator_indices"] == list(range(55))
    gram = matrix(ZZ, json.loads(
        (folder / "coble_ambient_twenty_one_generators.json").read_text()
    )["standard_gram"])
    ring = Integers(16)
    identity = identity_matrix(ring, 11)
    generators = []
    for row in data["generators"]:
        g = matrix(ZZ, row["matrix_standard"])
        assert g.transpose() * gram * g == gram
        assert matrix(GF(2), g) == identity_matrix(GF(2), 11)
        generators.append(matrix(ring, g))

    levels = (2, 4, 8)
    pivots = {level: {} for level in levels}
    pending = deque()
    lifts = []

    def leading(element, level):
        return sum((((int(element[i, j]) - int(i == j)) // level) % 2)
                   << (11 * i + j) for i in range(11) for j in range(11))

    def admit(element):
        for level in levels:
            bits = leading(element, level)
            while bits:
                pivot = bits.bit_length() - 1
                if pivot in pivots[level]:
                    element *= pivots[level][pivot].inverse()
                    bits = leading(element, level)
                else:
                    pivots[level][pivot] = element
                    pending.append(element)
                    lifts.append(element)
                    return

    for generator in generators:
        admit(generator)
    while pending:
        element = pending.popleft()
        admit(element * element)
        for previous in tuple(lifts):
            admit(element * previous * element.inverse() * previous.inverse())
    assert tuple(len(pivots[level]) for level in levels) == (55, 54, 55)
    subprocess.run(["sage", str(folder / "coble_positive_kernel_fifty_five_generators.py")],
                   cwd=folder.parents[1], check=True, capture_output=True, text=True)
    assert artifact.read_bytes() == before


def test_coble_positive_fifty_five_odd_local_certificate():
    """The 55 positive generators have full odd Lie and small-prime images."""
    import hashlib
    import json
    import subprocess
    from pathlib import Path

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    artifact = folder / "coble_positive_fifty_five_odd_local.json"
    before = artifact.read_bytes()
    data = json.loads(before)
    assert data["schema"] == "coble-positive-55-odd-local-v1"
    for field, name in (
        ("source_sha256", "coble_positive_kernel_fifty_five_generators.json"),
        ("basis_sha256", "coble_singular_integral_representatives.json"),
    ):
        assert data[field] == hashlib.sha256((folder / name).read_bytes()).hexdigest()
    assert data["unipotent_count"] == data["initial_lie_rank"] == 47
    assert data["lie_rank"] == 55 and data["lie_index"] == 2**63
    assert [row["prime"] for row in data["records"]] == [3, 5, 7, 11, 13]
    assert all(row["contains_omega"] is True and
               row["principal_p_layer_rank"] == 55 for row in data["records"])
    subprocess.run(["sage", str(folder / "coble_positive_fifty_five_odd_local.py")],
                   cwd=folder.parents[1], check=True, capture_output=True, text=True)
    assert artifact.read_bytes() == before


def test_coble_fifty_six_ordinary_elements_span_kernel_modulo_sixteen():
    """The 56 ordinary elements generate every certified layer modulo 16."""
    import hashlib
    import json
    from collections import deque
    from pathlib import Path
    from sage.all import Integers, ZZ, identity_matrix, matrix

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    data = json.loads((folder / "coble_kernel_fifty_six_congruence_generators.json").read_text())
    assert data["schema"] == "coble-kernel-56-ordinary-mod-four-v1"
    assert data["generator_count"] == len(data["generators"]) == 56
    for name, field in (
        ("coble_plane_parabolic_level_two_generators.json", "parabolic_sha256"),
        ("coble_ambient_twenty_one_generators.json", "ambient_sha256"),
    ):
        assert data[field] == hashlib.sha256((folder / name).read_bytes()).hexdigest()

    ring = Integers(16)
    identity = identity_matrix(ring, 11)
    gram = matrix(ZZ, json.loads(
        (folder / "coble_ambient_twenty_one_generators.json").read_text()
    )["standard_gram"])
    generators = [matrix(ring, row["matrix_standard"]) for row in data["generators"]]
    for row in data["generators"]:
        g = matrix(ZZ, row["matrix_standard"])
        assert g.transpose() * gram * g == gram
        assert all((g[i, j] - int(i == j)) % 2 == 0
                   for i in range(11) for j in range(11))

    levels = (2, 4, 8)
    pivots = {level: {} for level in levels}
    pending = deque()
    lifts = []

    def leading(element, level):
        return sum((((int(element[i, j]) - int(i == j)) // level) % 2)
                   << (11 * i + j) for i in range(11) for j in range(11))

    def admit(element):
        for level in levels:
            bits = leading(element, level)
            while bits:
                pivot = bits.bit_length() - 1
                if pivot in pivots[level]:
                    element *= pivots[level][pivot].inverse()
                    bits = leading(element, level)
                else:
                    pivots[level][pivot] = element
                    pending.append(element)
                    lifts.append(element)
                    return

    for generator in generators:
        admit(generator)
    while pending:
        element = pending.popleft()
        admit(element * element)
        for previous in tuple(lifts):
            admit(element * previous * element.inverse() * previous.inverse())
    assert tuple(len(pivots[level]) for level in levels) == (56, 54, 55)


def test_coble_nineteen_relations_generate_the_full_kernel_modulo_sixteen():
    """Exact subgroup collection fills all three certified congruence layers."""
    import json
    from collections import deque
    from pathlib import Path
    from sage.all import Integers, identity_matrix, matrix

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    data = json.loads((folder / "coble_ambient_twenty_one_generators.json").read_text())
    ring = Integers(16)
    identity = identity_matrix(ring, 11)
    generators = [matrix(ring, row["matrix_standard"])
                  for row in data["generators"][:18]]
    inverses = [generator.inverse() for generator in generators]
    levels = (2, 4, 8)
    bases = {level: {} for level in levels}
    pending = deque()
    lifts = []

    def leading_bits(element, level):
        return sum((((int(element[i, j]) - int(i == j)) // level) % 2)
                   << (11 * i + j) for i in range(11) for j in range(11))

    def collect(element, insert=True):
        for level in levels:
            bits = leading_bits(element, level)
            while bits:
                pivot = bits.bit_length() - 1
                if pivot in bases[level]:
                    element *= bases[level][pivot].inverse()
                    bits = leading_bits(element, level)
                else:
                    if insert:
                        bases[level][pivot] = element
                        pending.append(element)
                        lifts.append(element)
                    return False
        return True

    for word in data["level_two_normal_relation_words"][:19]:
        element = identity
        for index in word:
            element *= generators[index]
        collect(element)
    while pending:
        element = pending.popleft()
        collect(element * element)
        for earlier in tuple(lifts):
            collect(element * earlier * element.inverse() * earlier.inverse())
        for generator, inv in zip(generators, inverses, strict=True):
            collect(generator * element * inv)

    assert tuple(len(bases[level]) for level in levels) == (54, 54, 55)
    # The extra rank-55 witness at level eight is already in the normal
    # closure, although it is independent of the 54 displayed squares.
    short_word = generators[17] * inverses[14] * inverses[11] * generators[3]
    assert collect(short_word ** 10, insert=False)


def test_coble_eichler_squares_generate_every_odd_modulus_image():
    """Each Eichler generator is an odd-modulus power of its square."""
    import json
    from pathlib import Path
    from sage.all import ZZ, identity_matrix, matrix

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    data = json.loads((folder / "coble_ambient_twenty_one_generators.json").read_text())
    generators = [matrix(ZZ, row["matrix_standard"])
                  for row in data["generators"][:18]]
    identity = identity_matrix(ZZ, 11)
    for modulus in (3, 5, 7, 9, 15):
        for generator in generators:
            assert all((entry - int(i == j)) % modulus == 0
                       for i, row in enumerate((generator ** modulus).rows())
                       for j, entry in enumerate(row))
            lift = (generator * generator) ** ((modulus + 1) // 2)
            assert all((lift[i, j] - generator[i, j]) % modulus == 0
                       for i in range(11) for j in range(11))


def test_coble_eichler_normal_relations_have_rank_54_at_level_eight():
    """Their derived lifts persist through the next two 2-adic layers."""
    import json
    from pathlib import Path
    from sage.all import GF, Integers, matrix, identity_matrix

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    data = json.loads((folder / "coble_ambient_twenty_one_generators.json").read_text())
    ring = Integers(32)
    identity = identity_matrix(ring, 11)
    generators = [matrix(ring, row["matrix_standard"])
                  for row in data["generators"][:18]]
    inverse = [generator.inverse() for generator in generators]
    basis = {}
    queue = []

    def vector_bits(element, level):
        return sum((((int(element[i, j]) - int(i == j)) // level) % 2)
                   << (11 * i + j) for i in range(11) for j in range(11))

    def admit(element):
        bits = vector_bits(element, 2)
        while bits:
            pivot = bits.bit_length() - 1
            if pivot in basis:
                bits ^= basis[pivot]
            else:
                basis[pivot] = bits
                queue.append(element)
                return

    for word in data["level_two_normal_relation_words"][:19]:
        product = identity
        for index in word:
            product *= generators[index]
        admit(product)
    position = 0
    while position < len(queue):
        element = queue[position]
        position += 1
        for generator, inv in zip(generators, inverse, strict=True):
            admit(generator * element * inv)
    assert len(basis) == len(queue) == 54
    higher = {}
    higher_lifts = []

    def admit_higher(element):
        assert vector_bits(element, 2) == 0
        bits = vector_bits(element, 4)
        while bits:
            pivot = bits.bit_length() - 1
            if pivot in higher:
                bits ^= higher[pivot]
            else:
                higher[pivot] = bits
                higher_lifts.append(element)
                return

    for i, element in enumerate(queue):
        admit_higher(element * element)
        for earlier in queue[:i]:
            admit_higher(element * earlier * element.inverse() * earlier.inverse())
    assert len(higher) == 54
    # Zassenhaus's spinor-norm formula cuts the 55-dimensional alternating
    # Lie algebra at level four by one linear equation. In the odd diagonal
    # basis it is the parity of the sum of the upper-triangular entries.
    source = json.loads((folder / "coble_singular_integral_representatives.json").read_text())
    change = matrix(GF(2), source["standard_to_diagonal"])
    from sage.all import ZZ, identity_matrix as integral_identity_matrix
    for element in higher_lifts:
        integral_a = matrix(ZZ, 11, 11, [
            (int(element[i, j]) - int(i == j)) // 4
            for i in range(11) for j in range(11)
        ])
        assert (integral_identity_matrix(ZZ, 11) + 2 * integral_a).det() % 8 == 1
        leading = matrix(GF(2), 11, 11, [
            ((int(element[i, j]) - int(i == j)) // 4) % 2
            for i in range(11) for j in range(11)
        ])
        diagonal = change * leading * change.inverse()
        assert diagonal == diagonal.transpose()
        assert all(diagonal[i, i] == 0 for i in range(11))
        assert sum(int(diagonal[i, j]) for i in range(11)
                   for j in range(i + 1, 11)) % 2 == 0
    level_echelons = {}
    for exponent, level in ((2, 8), (4, 16)):
        echelon = {}
        for element in higher_lifts:
            power = element ** exponent
            assert vector_bits(power, level // 2) == 0
            bits = vector_bits(power, level)
            while bits:
                pivot = bits.bit_length() - 1
                if pivot in echelon:
                    bits ^= echelon[pivot]
                else:
                    echelon[pivot] = bits
                    break
        assert len(echelon) == 54
        level_echelons[level] = echelon
    # A four-letter ambient Eichler word has order ten modulo eight.
    # Its tenth power supplies the missing 55th leading direction at
    # level sixteen, independent of the 54 fourth powers above.
    word = generators[17] * inverse[14] * inverse[11] * generators[3]
    witness = word ** 10
    assert all(int(witness[i, j]) % 8 == int(i == j)
               for i in range(11) for j in range(11))
    for level, element in ((8, witness), (16, witness * witness)):
        echelon = level_echelons[level]
        bits = vector_bits(element, level)
        while bits:
            pivot = bits.bit_length() - 1
            if pivot in echelon:
                bits ^= echelon[pivot]
            else:
                echelon[pivot] = bits
                break
        assert len(echelon) == 55


def test_coble_level_two_relation_words_are_public_kernel_morphisms():
    """Every certified relation word constructs an owned kernel morphism."""
    import json
    from pathlib import Path
    from sage.all import ZZ, identity_matrix, matrix
    from sage_extensions.all import NamedLattices, ZZ as OwnedZZ

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    data = json.loads((folder / "coble_ambient_twenty_one_generators.json").read_text())
    lattice = NamedLattices.Tco
    labels = tuple(lattice.module_generating_set())
    group = lattice.O()
    kernel = lattice.stable_orthogonal_group()
    generators = [matrix(ZZ, record["matrix_standard"])
                  for record in data["generators"]]
    for word in data["level_two_normal_relation_words"]:
        product = identity_matrix(ZZ, 11)
        for index in word:
            product *= generators[index]
        morphism = group({
            label: lattice.linear_combination({
                labels[j]: OwnedZZ(int(product[j, i])) for j in range(11)
            })
            for i, label in enumerate(labels)
        })
        assert morphism in kernel


def test_coble_ambient_generators_are_public_integral_isometry_morphisms():
    """All 21 standard matrices construct actual owned O(T_Co) morphisms."""
    import json
    from pathlib import Path
    from sage_extensions.all import NamedLattices, ZZ as OwnedZZ

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    data = json.loads((folder / "coble_ambient_twenty_one_generators.json").read_text())
    lattice = NamedLattices.Tco
    labels = tuple(lattice.module_generating_set())
    group = lattice.O()
    for row in data["generators"]:
        entries = row["matrix_standard"]
        morphism = group({
            label: lattice.linear_combination({
                labels[j]: OwnedZZ(entries[j][i]) for j in range(11)
            })
            for i, label in enumerate(labels)
        })
        assert morphism in group
        assert morphism.domain() is lattice
        assert morphism.codomain() is lattice


def test_coble_large_character_maps_directly_to_faithful_permutations():
    """The nontrivial Coble root character has a faithful permutation image."""
    from sage.libs.gap.libgap import libgap
    from sage_extensions.all import NamedLattices, ZZ as OwnedZZ

    lattice = NamedLattices.Tco
    group = lattice.O()
    labels = tuple(lattice.module_generating_set())
    data = json.loads((Path(__file__).resolve().parents[2] /
                       "computations/reports/coble_ambient_twenty_one_generators.json").read_text())
    entries = next(row["matrix_standard"] for row in data["generators"]
                   if row["name"] == "root_reflection_U2")
    reflection = group({
        label: lattice.linear_combination({
            labels[j]: OwnedZZ(entries[j][i]) for j in range(11)
        }) for i, label in enumerate(labels)
    })
    quotient = lattice.stable_orthogonal_group().finite_character_quotient()
    permutation = quotient._permutation_of_key(quotient.image(reflection))
    _factors, _models, target, _embeddings = quotient._character_permutation_factors()
    assert permutation != libgap.One(target)
    assert permutation * permutation == libgap.One(target)


def test_coble_ambient_standard_generator_certificate():
    """The reusable standard-basis 21-matrix certificate is exact and sourced."""
    import hashlib
    import json
    from pathlib import Path
    from sage.all import ZZ, identity_matrix, matrix

    folder = Path(__file__).resolve().parents[2] / "computations/reports"
    data = json.loads((folder / "coble_ambient_twenty_one_generators.json").read_text())
    assert data["source_sha256"] == hashlib.sha256(
        (folder / "coble_singular_integral_representatives.json").read_bytes()
    ).hexdigest()
    gram = matrix(ZZ, data["standard_gram"])
    change = matrix(ZZ, data["standard_from_split"])
    split_gram = change.transpose() * gram * change
    assert abs(change.det()) == 1
    assert data["generator_count"] == len(data["generators"]) == 21
    assert data["eichler_generator_indices"] == list(range(18))
    assert data["level_two_character_complement_indices"] == [19, 20]
    words = data["level_two_normal_relation_words"]
    assert words == [[i, i] for i in range(18)] + [[7, 8], [19], [20]]
    assert data["finite_discriminant_image_order"] == 46998591897600
    assert data["eichler_discriminant_image_order"] == 23499295948800
    assert len(set(row["name"] for row in data["generators"])) == 21
    for row in data["generators"]:
        generator = matrix(ZZ, row["matrix_standard"])
        assert generator.transpose() * gram * generator == gram
        assert abs(generator.det()) == 1
        split = change.inverse() * generator * change
        assert all(x in ZZ for x in split.list())
        assert split.transpose() * split_gram * split == split_gram
    for word in words:
        product = identity_matrix(ZZ, 11)
        for index in word:
            product *= matrix(ZZ, data["generators"][index]["matrix_standard"])
        assert product.transpose() * gram * product == gram
        assert all((product[i, j] - int(i == j)) % 2 == 0
                   for i in range(11) for j in range(11))
    assert matrix(ZZ, data["generators"][-1]["matrix_standard"]) != identity_matrix(ZZ, 11)
    from sage.all import GF
    for index in data["level_two_character_complement_indices"]:
        assert matrix(GF(2), data["generators"][index]["matrix_standard"]) == identity_matrix(GF(2), 11)


def test_coble_ambient_twenty_one_integral_generators():
    """Verify the 18 Eichler and three character generators of O(I_{2,9})."""
    from sage.all import ZZ, identity_matrix, matrix, vector

    gram = matrix(ZZ, 11, 11)
    for i in (0, 2):
        gram[i, i + 1] = gram[i + 1, i] = 1
    for i in range(4, 11):
        gram[i, i] = -1
    identity = identity_matrix(ZZ, 11)
    standard = [vector(ZZ, identity.column(i)) for i in range(11)]
    roots = [standard[i] - standard[i + 1] for i in range(4, 10)]
    roots.append(standard[9] + standard[10])
    complement = [standard[2], standard[3], *roots]
    even_basis = matrix(ZZ, 11, 11, lambda i, j: (
        standard[j][i] if j < 4 else roots[j - 4][i]
    ))
    assert abs(even_basis.det()) == 2
    even_gram = even_basis.transpose() * gram * even_basis
    dual_basis = even_basis * even_gram.inverse()

    def transvection(e, a):
        e_pairing = e.row() * gram
        a_pairing = a.row() * gram
        return (identity + a.column() * e_pairing - e.column() * a_pairing
                - (a * gram * a // 2) * e.column() * e_pairing)

    eichler = [transvection(e, a) for e in standard[:2] for a in complement]
    assert len(eichler) == 18
    reflect = lambda a: identity - (2 // (a * gram * a)) * a.column() * (a.row() * gram)
    extra = [reflect(standard[2] - standard[3]), reflect(standard[4]),
             identity - 2 * standard[0].column() * standard[0].row()
             - 2 * standard[1].column() * standard[1].row()]
    assert all(g * g == identity for g in extra)
    assert all(g * h == h * g for i, g in enumerate(extra) for h in extra[:i])
    from sage.all import GF
    assert matrix(GF(2), extra[0]) != identity_matrix(GF(2), 11)
    assert matrix(GF(2), extra[1]) == identity_matrix(GF(2), 11)
    assert matrix(GF(2), extra[2]) == identity_matrix(GF(2), 11)
    for generator in [*eichler, *extra]:
        assert generator.base_ring() is ZZ
        assert generator.transpose() * gram * generator == gram
        assert abs(generator.det()) == 1
        assert all(x in ZZ for x in (
            even_basis.inverse() * generator * even_basis
        ).list())
    for generator in [*eichler, extra[0], extra[2]]:
        assert all(x in ZZ for x in (
            even_basis.inverse() * (generator - identity) * dual_basis
        ).list())
    assert any(x not in ZZ for x in (
        even_basis.inverse() * (extra[1] - identity) * dual_basis
    ).list())
    # The discriminant form of B(2) has 527 nonzero isotropic classes:
    # masks x with x^2 divisible by 4.  Each of the 21 exact isometries
    # permutes these classes.  Its permutation image must have the full
    # independently known order of O(q), not merely preserve q.
    from sage.libs.gap.libgap import libgap

    masks = [
        mask for mask in range(1, 1 << 11)
        if (2 * (((mask >> 0) & 1) * ((mask >> 1) & 1)
                  + ((mask >> 2) & 1) * ((mask >> 3) & 1))
            - sum((mask >> i) & 1 for i in range(4, 11))) % 4 == 0
    ]
    assert len(masks) == 527
    positions = {mask: i + 1 for i, mask in enumerate(masks)}
    permutations = []
    for generator in [*eichler, *extra]:
        permutation = []
        for mask in masks:
            image = generator * vector(ZZ, [(mask >> i) & 1 for i in range(11)])
            target = sum((int(image[i]) % 2) << i for i in range(11))
            permutation.append(positions[target])
        permutations.append(libgap.PermList(permutation))
    assert int(libgap.Size(libgap.Group(permutations[:18]))) == 23499295948800
    # The ATLAS table O10+(2) is the simple plus-type group, not its
    # index-two full orthogonal extension; it also has a 527-point action.
    assert int(libgap.Size(libgap.CharacterTable("O10+(2)"))) == 23499295948800
    assert int(libgap.Size(libgap.Group(permutations))) == 46998591897600


def test_coble_even_neighbor_has_kneser_local_ranks():
    """The canonical even sublattice is U^2 + D7(-1), with local ranks 10 and 11."""
    from sage.all import ZZ, identity_matrix, matrix

    unit = identity_matrix(ZZ, 7)
    roots = [unit.row(i) - unit.row(i + 1) for i in range(6)]
    roots.append(unit.row(5) + unit.row(6))
    basis = matrix(ZZ, roots)
    gram = basis * basis.transpose()
    assert abs(basis.det()) == 2
    assert gram.det() == 4
    assert gram[:6, :6].det() == 7
    # A six-dimensional odd-determinant minor is a 2-adic unimodular
    # summand. The determinant 4 leaves one rank-one scale-four constituent.
    assert gram.rank() == 7
    # For D7 the half-sum of all seven coordinates has order four in
    # D7^*/D7: twice it has odd coordinate sum and four times it does not.
    assert sum([1] * 7) % 2 == 1
    assert sum([2] * 7) % 2 == 0


def test_level_two_integral_plane_parabolic_kernel_generators(tmp_path):
    """The 26 integral generators preserve P and lie in the reduction kernel."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    path = folder / "coble_plane_parabolic_level_two_generators.json"
    data = json.loads(path.read_text())
    assert data["schema"] == "coble-integral-plane-parabolic-level-two-kernel-v1"
    assert data["generator_count"] == len(data["generators_standard"]) == 26
    assert data["level_four_image_rank"] == 26
    assert data["normal_conjugate_level_four_image_rank"] == 56
    for key, filename in (("line", "coble_singular_integral_representatives.json"),
                          ("complete_parabolic", "coble_complete_plane_parabolic_generators.json")):
        assert data["source_sha256"][key] == hashlib.sha256((folder / filename).read_bytes()).hexdigest()
    from sage.all import GF, ZZ, identity_matrix, matrix, vector

    source = json.loads((folder / "coble_singular_integral_representatives.json").read_text())
    gram = matrix(ZZ, source["standard_gram"])
    change = matrix(ZZ, source["standard_to_diagonal"])
    basis = [vector(ZZ, [int(i == j) for j in range(11)]) for i in range(11)]
    plane = matrix(ZZ, [change.inverse() * (basis[0] + basis[2]),
                        change.inverse() * (basis[1] + basis[4])]).row_module()
    for rows in data["generators_standard"]:
        g = matrix(ZZ, rows)
        assert g.transpose() * gram * g == gram and abs(g.det()) == 1
        assert all(int(g[i, j]) % 2 == int(i == j)
                   for i in range(11) for j in range(11))
        assert all(g * v in plane for v in plane.basis())
    # The reduction of (g-I)/2 modulo 2 is a homomorphism on the
    # principal level-two group, since cross terms vanish modulo 4.
    # Its 26 independent images force at least 26 group generators.
    echelon = {}
    for rows in data["generators_standard"]:
        bits = sum(((((rows[i][j] - int(i == j)) // 2) % 2)
                    << (11 * i + j)) for i in range(11) for j in range(11))
        while bits:
            pivot = bits.bit_length() - 1
            if pivot in echelon:
                bits ^= echelon[pivot]
            else:
                echelon[pivot] = bits
                break
    assert len(echelon) == 26
    reflections = []
    integral_reflections = []
    for coordinates in source["generator_roots_standard"]:
        root = vector(ZZ, coordinates)
        norm = root * gram * root
        assert abs(norm) == 2
        reflection = identity_matrix(ZZ, 11) - (2 // norm) * root.column() * (root.row() * gram)
        assert reflection.transpose() * gram * reflection == gram
        integral_reflections.append(reflection)
        reflections.append(matrix(GF(2), reflection))
    frontier = deque(
        matrix(GF(2), 11, 11, [((g[i][j] - int(i == j)) // 2) % 2
                               for i in range(11) for j in range(11)])
        for g in data["generators_standard"]
    )
    while frontier:
        current = frontier.popleft()
        for reflection in reflections:
            moved = reflection * current * reflection
            bits = sum(int(x) << i for i, x in enumerate(moved.list()))
            remainder = bits
            while remainder:
                pivot = remainder.bit_length() - 1
                if pivot in echelon:
                    remainder ^= echelon[pivot]
                else:
                    echelon[pivot] = remainder
                    frontier.append(moved)
                    break
    assert len(echelon) == 56
    witnesses = data["normal_conjugate_level_four_generators"]
    assert len(witnesses) == 56
    assert all(len(row["conjugating_reflection_word"]) <= 1 for row in witnesses)
    witness_echelon = {}
    for record in witnesses:
        seed = record["kernel_generator_index"]
        assert 0 <= seed < 26
        conjugator = identity_matrix(ZZ, 11)
        for index in record["conjugating_reflection_word"]:
            assert 0 <= index < len(integral_reflections)
            conjugator *= integral_reflections[index]
        expected = (conjugator * matrix(ZZ, data["generators_standard"][seed])
                    * conjugator.inverse())
        assert expected == matrix(ZZ, record["matrix_standard"])
        bits = sum((int((expected[i, j] - int(i == j)) // 2) % 2)
                   << (11 * i + j) for i in range(11) for j in range(11))
        while bits:
            pivot = bits.bit_length() - 1
            if pivot in witness_echelon:
                bits ^= witness_echelon[pivot]
            else:
                witness_echelon[pivot] = bits
                break
    assert len(witness_echelon) == 56
    reproduced = tmp_path / "kernel.json"
    subprocess.run(
        ["sage", "-c", "import runpy,sys;sys.argv=['kernel','--output',"
         + repr(str(reproduced)) + "];runpy.run_path("
         "'computations/reports/coble_plane_parabolic_level_two_generators.py',"
         "run_name='__main__')"],
        cwd=folder.parents[1], capture_output=True, text=True, check=True)
    assert reproduced.read_bytes() == path.read_bytes()


def test_proper_integral_plane_stabilizer_image(tmp_path):
    """Compute Q, the finite-plane stabilizer F, and integral image S."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    result = subprocess.run(
        ["sage", "-c", "import runpy,sys;sys.argv=['finite'];runpy.run_path("
         "'computations/reports/coble_proper_plane_stabilizer_image.py',"
         "run_name='__main__')"],
        cwd=folder.parents[1], capture_output=True, text=True, check=True)
    transcript = (folder / "coble_proper_plane_stabilizer_image-run.txt").read_bytes()
    assert result.stdout.encode() == transcript
    assert hashlib.sha256(transcript).hexdigest() == (
        "ae05bf38787c79f0fbc1ab76820f94be064a38aab3cf1e48eeb68b27c36e5744")
    assert "ambient finite image order: 46998591897600" in result.stdout
    assert "finite plane stabilizer order: 1981808640" in result.stdout
    assert "integral plane stabilizer image order: 247726080" in result.stdout
    assert "proper image index in finite plane stabilizer: 8" in result.stdout
    assert "characteristic stars in the F/S orbit: 8" in result.stdout
    assert ("finite F/S coset representative words: [[], [9, 6], [9], "
            "[9, 12, 4, 5], [9, 12, 4], [9, 7], [9, 12], [0]]") in result.stdout
    artifact = folder / "coble_proper_plane_stabilizer_image.json"
    assert hashlib.sha256(artifact.read_bytes()).hexdigest() == (
        "b29321a10f9170ecefbf468b29b5c9e0555d0b720e57ea3fa10aeb5bfa13b0cd")
    data = json.loads(artifact.read_text())
    assert data["schema"] == "coble-proper-plane-stabilizer-finite-cosets-v1"
    assert data["kernel_subgroups_with_identical_plane_and_flag_orbits"] == [
        "Otilde", "Otilde+"]
    assert data["kernel_orbit_counts"] == {
        "line": 527, "plane": 189720, "flag": 569160}
    assert data["gamma_co_2_orbit_counts"] == {
        "line": 4, "plane": 7, "flag": 13}
    assert len(data["singular_masks_diagonal"]) == 527
    assert len(data["integral_reflection_roots_standard"]) == 10
    gram = data["standard_gram"]
    assert all(sum(root[i] * gram[i][j] * root[j]
                   for i in range(11) for j in range(11)) == -2
               for root in data["integral_reflection_roots_standard"])
    assert len(data["integral_star_masks_diagonal"]) == 8
    assert len(data["integral_plane_representatives_standard"]) == 8
    assert data["flag_line_coefficients"] == [[1, 0], [0, 1], [1, 1]]
    public = data["public_gamma_co_2_representatives"]
    public_path = folder / "coble_gco_public_representatives.json"
    public_log = folder / "coble_gco_public_incidence_source-run.log"
    assert hashlib.sha256(public_log.read_bytes()).hexdigest() == (
        "4cc44602660c3891c6c80ed902352612bc3932ef13677524a02be41b28d7da8b")
    assert data["source_sha256"]["public_gamma_co_2"] == hashlib.sha256(
        public_path.read_bytes()).hexdigest()
    assert public == json.loads(public_path.read_text())
    assert public["source_log_sha256"] == hashlib.sha256(
        public_log.read_bytes()).hexdigest()
    assert public["source_workflow"] == 43556671111
    assert len(public["lines"]) == 4
    assert len(public["planes"]) == 7
    assert len(public["edges"]) == 13
    assert sorted(x["index"] for x in public["lines"]) == list(range(4))
    assert sorted(x["index"] for x in public["planes"]) == list(range(7))
    assert sorted(x["index"] for x in public["edges"]) == list(range(13))
    assert all(0 <= e["line_index"] < 4 and 0 <= e["plane_index"] < 7
               for e in public["edges"])
    assert all(len(e["line_witness"]) == 11 and
               len(e["plane_witness"]) == 2 and
               all(len(v) == 11 for v in e["plane_witness"])
               for e in public["edges"])
    assert {(e["line_index"], e["plane_index"]) for e in public["edges"]} == {
        (0, 0), (3, 0), (2, 0), (3, 1), (1, 1), (3, 2), (2, 2),
        (1, 3), (2, 3), (2, 4), (1, 5), (2, 5), (2, 6)}
    finite_planes = data["finite_plane_transports"]
    assert len(finite_planes) == 23715
    assert len({tuple(sorted(row["finite_plane_masks"])) for row in finite_planes}) == 23715
    assert all(len(row["finite_plane_masks"]) == 3 and
               len(set(row["finite_plane_masks"])) == 3 and
               len(row["word_from_base"]) >= 0 for row in finite_planes)
    assert len(data["coset_words_in_finite_plane_stabilizer_generators"]) == 8
    generators = data["finite_plane_stabilizer_generators_on_singular_classes"]
    assert len(generators) >= 1
    assert all(sorted(g) == list(range(1, 528)) for g in generators)
    assert all(all(0 <= i < len(generators) for i in word)
               for word in data["coset_words_in_finite_plane_stabilizer_generators"])
    output = tmp_path / "replay.json"
    replay = subprocess.run(
        ["sage", "-c", "import runpy,sys;sys.argv=['finite','--output',"
         + repr(str(output)) + "];runpy.run_path("
         "'computations/reports/coble_proper_plane_stabilizer_image.py',"
         "run_name='__main__')"],
        cwd=folder.parents[1], capture_output=True, text=True, check=True)
    assert replay.stdout == result.stdout
    assert output.read_bytes() == artifact.read_bytes()
    assert "integral plane orbit count: 189720" in result.stdout


def test_all_integral_flags_recover_public_gamma_co_2_edge_weights():
    """All 13 *public* L/P edges occur with their exact integral flag counts."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    transcript = (folder / "coble_integral_public_edge_multiplicities-run.txt").read_bytes()
    assert hashlib.sha256(transcript).hexdigest() == (
        "805c5f00f9781a707706d7c576c59edef096b69695d4bee9402eb2c6199500e8")
    text = transcript.decode()
    matches = re.findall(r"^public Gamma_Co,2 edge multiplicities: (.*)$",
                         text, re.MULTILINE)
    assert len(matches) == 1
    weighted = ast.literal_eval(matches[0])
    assert len(weighted) == len({edge for edge, _ in weighted}) == 13
    assert sum(weight for _, weight in weighted) == 569160
    assert sorted(weight for _, weight in weighted) == [
        2160, 2160, 2160, 7560, 9450, 15120, 22680, 28350,
        45360, 69120, 75600, 138240, 151200]
    # Compare against the actual public graph's committed edge labels,
    # rather than accepting a relabelled abstract 13-edge graph.
    comparison = ast.parse((folder / "coble_gco_public_incidence_compare.py").read_text())
    public = next(ast.literal_eval(node.value) for node in comparison.body
                  if isinstance(node, ast.Assign)
                  and any(isinstance(t, ast.Name) and t.id == "public"
                          for t in node.targets))
    assert {edge for edge, _ in weighted} == public
    assert "exact integral flags classified: 569160" in text


def test_all_coble_integral_plane_star_words():
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    data = json.loads((folder / "coble_singular_integral_representatives.json").read_text())
    section = json.loads((folder / "coble_plane_integral_star_section.json").read_text())
    gram = data["standard_gram"]
    change = data["standard_to_diagonal"]
    roots = data["generator_roots_standard"]
    base = section["base_planes_standard"]
    seed_roots = section["seed_reflection_roots_standard"]
    stars = section["base_stars_quotient_classes"]
    flag_coefficients = section["flag_line_coefficients"]
    rows = section["finite_plane_transports"]
    stabilizer = section["plane_stabilizer_generators_standard"]

    def pairing(a, b):
        return sum(a[i] * gram[i][j] * b[j]
                   for i in range(11) for j in range(11))

    def mask(v):
        diagonal = [sum(change[i][j] * v[j] for j in range(11))
                    for i in range(11)]
        return sum((x % 2) << i for i, x in enumerate(diagonal))

    def key(a, b):
        x, y = mask(a), mask(b)
        return tuple(sorted((x, y, x ^ y)))

    assert len(base) == 8 and len(rows) == 23715
    assert len(stabilizer) == 21
    assert section["plane_stabilizer_finite_image_order"] == 247726080
    assert len(seed_roots) == 7
    assert len({tuple(row["finite_plane_masks"]) for row in rows}) == 23715
    assert len({tuple(star) for star in stars}) == 8
    root_masks = [mask(root) for root in roots]
    assert flag_coefficients == [[1, 0], [0, 1], [1, 1]]
    assert len(rows) * len(base) * len(flag_coefficients) == 569160
    expected_line_masks = {row["mask_diagonal"] for row in data["representatives"]}
    line_degrees = Counter()
    base_key = key(*base[0])
    def plucker(a, b):
        minors = tuple(a[i] * b[j] - a[j] * b[i]
                       for i, j in combinations(range(11), 2))
        first = next(x for x in minors if x)
        return minors if first > 0 else tuple(-x for x in minors)

    base_plucker = plucker(*base[0])
    for g in stabilizer:
        assert len(g) == 11 and all(len(row) == 11 for row in g)
        for i in range(11):
            for j in range(11):
                assert sum(g[k][i] * gram[k][l] * g[l][j]
                           for k in range(11) for l in range(11)) == gram[i][j]
        images = [[sum(g[i][j] * v[j] for j in range(11))
                   for i in range(11)] for v in base[0]]
        assert plucker(*images) == base_plucker
    # Independently recompute the faithful finite image, rather than
    # trusting the order recorded by the certificate producer.
    from sage.all import ZZ, PermutationGroup, identity_matrix, matrix, vector

    diagonal_change = matrix(ZZ, change)
    inverse_change = diagonal_change.inverse()
    singular = sorted(row["mask_diagonal"] for row in data["representatives"])
    positions = {mask: i + 1 for i, mask in enumerate(singular)}
    permutations = []
    for g in stabilizer:
        diagonal_action = diagonal_change * matrix(ZZ, g) * inverse_change
        permutation = []
        for x in singular:
            image = diagonal_action * vector(ZZ, [(x >> i) & 1 for i in range(11)])
            y = sum((int(a) & 1) << i for i, a in enumerate(image))
            permutation.append(positions[y])
        permutations.append(permutation)
    assert int(PermutationGroup(permutations).order()) == 247726080
    sample = section["ambient_transporter_sample"]
    sample_matrix = sample["matrix_standard"]
    kernel_matrix = sample["kernel_matrix_standard"]
    positive_matrix = sample["positive_kernel_matrix_standard"]
    spinor_flip_matrix = sample["spinor_flip_matrix_standard"]
    assert len(sample_matrix) == 11 and all(len(r) == 11 for r in sample_matrix)
    sample_line, = (r for r in data["representatives"]
                    if r["mask_diagonal"] == sample["line_mask_diagonal"])
    line_vector = sample_line["vector_standard"]
    flag_vector = sample["flag_vector_standard"]
    assert [sum(sample_matrix[i][j] * line_vector[j] for j in range(11))
            for i in range(11)] == flag_vector
    assert [sum(kernel_matrix[i][j] * line_vector[j] for j in range(11))
            for i in range(11)] == flag_vector
    assert all(kernel_matrix[i][j] % 2 == int(i == j)
               for i in range(11) for j in range(11))
    assert [sum(positive_matrix[i][j] * line_vector[j] for j in range(11))
            for i in range(11)] == flag_vector
    assert [sum(spinor_flip_matrix[i][j] * flag_vector[j] for j in range(11))
            for i in range(11)] == flag_vector
    assert all(positive_matrix[i][j] % 2 == int(i == j)
               and spinor_flip_matrix[i][j] % 2 == int(i == j)
               for i in range(11) for j in range(11))
    assert pairing(flag_vector, flag_vector) == 0 and gcd(*flag_vector) == 1
    assert mask(flag_vector) == sample["line_mask_diagonal"]
    assert tuple(sample["finite_plane_masks"]) in {
        tuple(r["finite_plane_masks"]) for r in rows
    }
    assert sample["line_mask_diagonal"] in sample["finite_plane_masks"]
    for i in range(11):
        for j in range(11):
            assert sum(sample_matrix[k][i] * gram[k][l] * sample_matrix[l][j]
                       for k in range(11) for l in range(11)) == gram[i][j]
            assert sum(kernel_matrix[k][i] * gram[k][l] * kernel_matrix[l][j]
                       for k in range(11) for l in range(11)) == gram[i][j]
            assert sum(positive_matrix[k][i] * gram[k][l] * positive_matrix[l][j]
                       for k in range(11) for l in range(11)) == gram[i][j]
    # Independently reconstruct both matrices from the finite-plane word,
    # seed reflection, GL2 flag map, line word, and parabolic correction.
    def reflection_matrix(root):
        r = vector(ZZ, root)
        n = pairing(root, root)
        assert abs(n) == 2
        return identity_matrix(ZZ, 11) - (2 // n) * (
            r.column() * (r.row() * matrix(ZZ, gram))
        )

    def word_matrix(word, generators):
        result = identity_matrix(ZZ, 11)
        for index in word:
            result = reflection_matrix(generators[index]) * result
        return result

    sample_plane, = (r for r in rows
                     if r["finite_plane_masks"] == sample["finite_plane_masks"])
    plane_word = word_matrix(sample_plane["word_from_base"], roots)
    line_word = word_matrix(sample_line["word_from_base"], roots)
    seed_reflection = reflection_matrix(
        section["seed_reflection_roots_standard"][sample["seed_index"] - 1]
    )
    flag_maps = [identity_matrix(ZZ, 11), matrix(ZZ, stabilizer[-2]),
                 matrix(ZZ, stabilizer[-1])]
    flag_map = flag_maps[sample["flag_index"]]
    reconstructed_ambient = plane_word * seed_reflection * flag_map * line_word.inverse()
    assert reconstructed_ambient == matrix(ZZ, sample_matrix)
    # The producer's F_2 column-mask action must equal the actual integral
    # action on every one of the 527 nonzero singular discriminant classes.
    diagonal_correction = (diagonal_change * line_word.inverse() *
                           reconstructed_ambient * line_word * inverse_change)
    column_masks = [sum((int(diagonal_correction[i, j]) & 1) << i
                        for i in range(11)) for j in range(11)]
    for class_mask in singular:
        direct = diagonal_correction * vector(
            ZZ, [(class_mask >> j) & 1 for j in range(11)])
        expected = sum((int(direct[i]) & 1) << i for i in range(11))
        image = 0
        for j in range(11):
            if (class_mask >> j) & 1:
                image ^= column_masks[j]
        assert image == expected
    parabolic_word = identity_matrix(ZZ, 11)
    for index, exponent in sample["parabolic_correction_word"]:
        parabolic_word = (reflection_matrix(
            data["vector_stabilizer_ten_roots_standard"][index]
        ) ** exponent) * parabolic_word
    correction = line_word * parabolic_word * line_word.inverse()
    assert reconstructed_ambient * correction.inverse() == matrix(ZZ, kernel_matrix)
    diagonal_kernel = diagonal_change * matrix(ZZ, kernel_matrix) * inverse_change
    diagonal_flip = diagonal_change * matrix(ZZ, spinor_flip_matrix) * inverse_change
    diagonal_positive = diagonal_change * matrix(ZZ, positive_matrix) * inverse_change
    positive_minor = lambda m: m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]
    assert positive_minor(diagonal_flip) < 0
    assert positive_minor(diagonal_positive) > 0
    sign = 1 if positive_minor(diagonal_kernel) > 0 else -1
    assert sign == sample["kernel_real_spinor_sign"]
    assert matrix(ZZ, positive_matrix) == (
        matrix(ZZ, kernel_matrix) if sign == 1 else
        matrix(ZZ, spinor_flip_matrix) * matrix(ZZ, kernel_matrix)
    )
    def quotient_class(x):
        return min(x, x ^ base_key[0], x ^ base_key[1], x ^ base_key[2])

    for index, root in enumerate(seed_roots, start=1):
        assert pairing(root, root) == 2
        for source, target in zip(base[0], base[index]):
            coefficient = pairing(source, root)
            assert [x - coefficient * y for x, y in zip(source, root)] == target
        assert mask(root) not in base_key
        root_mask = mask(root)
        reflected_star = sorted({quotient_class(
            x ^ (root_mask if (x & root_mask).bit_count() % 2 else 0))
            for x in stars[0]})
        assert reflected_star == stars[index]
    for a, b in base:
        assert key(a, b) == base_key
        assert pairing(a, a) == pairing(a, b) == pairing(b, b) == 0
        assert gcd(*(a[i] * b[j] - a[j] * b[i]
                     for i, j in combinations(range(11), 2))) == 1
        for u, v in flag_coefficients:
            line = [u * x + v * y for x, y in zip(a, b)]
            assert gcd(*line) == 1 and pairing(line, line) == 0
            assert mask(line) in key(a, b)

    for row in rows:
        a, b = [list(v) for v in base[0]]
        J = tuple(row["finite_plane_masks"])
        assert len(J) == 3 and set(J) <= expected_line_masks
        for line_mask in J:
            line_degrees[line_mask] += len(base)
        transformed_stars = set()
        for star in stars:
            image = []
            for x in star:
                for i in row["word_from_base"]:
                    root_mask = root_masks[i]
                    if (x & root_mask).bit_count() % 2:
                        x ^= root_mask
                image.append(min(x, x ^ J[0], x ^ J[1], x ^ J[2]))
            assert len(set(image)) == 7
            transformed_stars.add(tuple(sorted(image)))
        assert len(transformed_stars) == 8
        for i in row["word_from_base"]:
            assert 0 <= i < 10
            root = roots[i]
            n = pairing(root, root)
            assert abs(n) == 2
            for v in (a, b):
                numerator = 2 * pairing(v, root)
                assert numerator % n == 0
                k = numerator // n
                v[:] = [x - k * y for x, y in zip(v, root)]
        assert key(a, b) == tuple(row["finite_plane_masks"])
        assert pairing(a, a) == pairing(a, b) == pairing(b, b) == 0
    assert set(line_degrees) == expected_line_masks
    assert set(line_degrees.values()) == {1080}
    assert sum(line_degrees.values()) == 569160


@pytest.mark.parametrize("mode", ["single", "batch"])
def test_requested_nondefault_kernel_transporter(mode, tmp_path):
    """Single and streaming-batch requests preserve the canonical certificate."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    certificate = folder / "coble_plane_integral_star_section.json"
    before = hashlib.sha256(certificate.read_bytes()).digest()
    requests = [[100, 3, 1]] if mode == "single" else [[100, 3, 1], [0, 0, 0]]
    if mode == "single":
        arguments = [str(x) for x in requests[0]]
    else:
        request_file = tmp_path / "requests.jsonl"
        request_file.write_text("".join(json.dumps(row) + "\n" for row in requests))
        arguments = ["batch", str(request_file)]
    result = subprocess.run(
        ["sage", str(folder / "coble_plane_integral_star_section.py"), *arguments],
        cwd=folder.parents[1], capture_output=True, text=True, check=True,
    )
    assert hashlib.sha256(certificate.read_bytes()).digest() == before
    marker = "requested integral kernel transporter: "
    records = [json.loads(line.split(marker, 1)[1])
               for line in result.stdout.splitlines() if marker in line]
    assert len(records) == len(requests)
    lines = json.loads((folder / "coble_singular_integral_representatives.json").read_text())
    for record, (_, seed_index, flag_index) in zip(records, requests):
        assert record["seed_index"] == seed_index and record["flag_index"] == flag_index
        assert record["line_mask_diagonal"] in record["finite_plane_masks"]
        kernel = record["kernel_matrix_standard"]
        positive = record["positive_kernel_matrix_standard"]
        assert all(kernel[i][j] % 2 == int(i == j)
                   and positive[i][j] % 2 == int(i == j)
                   for i in range(11) for j in range(11))
        line, = (row["vector_standard"] for row in lines["representatives"]
                 if row["mask_diagonal"] == record["line_mask_diagonal"])
        assert [sum(positive[i][j] * line[j] for j in range(11))
                for i in range(11)] == record["flag_vector_standard"]
        assert record["parabolic_correction_word"]


def test_bounded_compressed_shard_is_explicitly_incomplete(tmp_path):
    """A diagnostic shard cannot be mistaken for full integral acceptance."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    source = folder / "coble_plane_integral_star_section.json"
    line_source = folder / "coble_singular_integral_representatives.json"
    original = hashlib.sha256(source.read_bytes()).hexdigest()
    output = tmp_path / "shard.jsonl.gz"
    subprocess.run(
        ["sage", str(folder / "coble_plane_integral_star_section.py"),
         "shard", "0", "8", str(output), "2"],
        cwd=folder.parents[1], capture_output=True, text=True, check=True,
    )
    assert hashlib.sha256(source.read_bytes()).hexdigest() == original
    with gzip.open(output, "rt", encoding="utf-8") as stream:
        records = [json.loads(line) for line in stream]
    assert len(records) == 4
    header = records[0]
    assert header["schema"] == "coble-exact-kernel-transport-shard-v1"
    assert header["shard_index"] == 0 and header["shard_count"] == 8
    assert header["expected_edges"] == 24 * len(range(0, 23715, 8))
    assert header["complete"] is False  # Only the final trailer can certify completion.
    assert header["plane_certificate_sha256"] == original
    assert header["line_certificate_sha256"] == hashlib.sha256(
        line_source.read_bytes()
    ).hexdigest()
    assert [(r["plane_index"], r["seed_index"], r["flag_index"])
            for r in records[1:-1]] == [(0, 0, 0), (0, 0, 1)]
    trailer = records[-1]
    assert trailer["trailer"] == header["schema"]
    assert trailer["records"] == 2 and trailer["complete"] is False
    digest = hashlib.sha256()
    for record in records[1:-1]:
        digest.update(json.dumps(record, separators=(",", ":")).encode() + b"\n")
    assert trailer["records_sha256"] == digest.hexdigest()
    assert all(len(r["positive_kernel_matrix_sha256"]) == 64
               for r in records[1:-1])
    lines = json.loads(line_source.read_text())
    gram = lines["standard_gram"]
    seed_line = {r["mask_diagonal"]: r["vector_standard"]
                 for r in lines["representatives"]}
    for row in records[1:-1]:
        source_vector = seed_line[row["line_mask_diagonal"]]
        target_vector = row["flag_vector_standard"]
        for field in ("kernel_matrix_standard", "spinor_flip_matrix_standard",
                      "positive_kernel_matrix_standard"):
            g = row[field]
            assert len(g) == 11 and all(len(r) == 11 for r in g)
            assert all(g[i][j] % 2 == int(i == j)
                       for i in range(11) for j in range(11))
            assert [sum(g[i][j] * (target_vector if field == "spinor_flip_matrix_standard"
                                    else source_vector)[j] for j in range(11))
                    for i in range(11)] == target_vector
            assert all(sum(g[k][i] * gram[k][l] * g[l][j]
                           for k in range(11) for l in range(11)) == gram[i][j]
                       for i in range(11) for j in range(11))
    spec = importlib.util.spec_from_file_location(
        "coble_kernel_audit", folder / "coble_kernel_public_incidence_audit.py")
    assert spec is not None and spec.loader is not None
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    assert audit.audit_integral_shard(output, allow_incomplete=True) == 2
    with pytest.raises(AssertionError):
        audit.audit_integral_shard(output)
    corrupted = tmp_path / "corrupted.jsonl.gz"
    bad = json.loads(json.dumps(records))
    bad[1]["flag_vector_standard"][0] += 2
    digest = hashlib.sha256()
    with gzip.open(corrupted, "wt", encoding="utf-8") as stream:
        stream.write(json.dumps(bad[0], separators=(",", ":")) + "\n")
        for record in bad[1:-1]:
            encoded = json.dumps(record, separators=(",", ":")) + "\n"
            digest.update(encoded.encode())
            stream.write(encoded)
        bad[-1]["records_sha256"] = digest.hexdigest()
        stream.write(json.dumps(bad[-1], separators=(",", ":")) + "\n")
    with pytest.raises(AssertionError):
        audit.audit_integral_shard(corrupted, allow_incomplete=True)


@pytest.mark.parametrize("plane_index", [0, 12345])
def test_complete_single_plane_shard_is_independently_certified(tmp_path, plane_index):
    """A full 24-edge shard must pass the strict auditor, not the diagnostic mode."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    output = tmp_path / "complete.jsonl.gz"
    subprocess.run(
        ["sage", str(folder / "coble_plane_integral_star_section.py"),
         "shard", str(plane_index), "23715", str(output)],
        cwd=folder.parents[1], capture_output=True, text=True, check=True,
    )
    with gzip.open(output, "rt", encoding="utf-8") as stream:
        header = json.loads(next(stream))
        assert header["shard_index"] == plane_index
        assert header["expected_edges"] == 24
        assert header["complete"] is False
        records = [json.loads(line) for line in stream]
    assert len(records) == 25
    assert records[-1]["complete"] is True and records[-1]["records"] == 24
    subprocess.run(
        ["python3", str(folder / "coble_kernel_public_incidence_audit.py"),
         "--shard", str(output)],
        cwd=folder.parents[1], capture_output=True, text=True, check=True,
    )
    missing = subprocess.run(
        ["python3", str(folder / "coble_kernel_public_incidence_audit.py"),
         "--shards", str(output)],
        cwd=folder.parents[1], capture_output=True, text=True,
    )
    assert missing.returncode != 0 and "missing shard indices" in missing.stderr
    duplicate = tmp_path / "duplicate-class.jsonl.gz"
    records[1] = dict(records[0], flag_index=1)
    digest = hashlib.sha256()
    with gzip.open(duplicate, "wt", encoding="utf-8") as stream:
        stream.write(json.dumps(header, separators=(",", ":")) + "\n")
        for row in records[:-1]:
            encoded = json.dumps(row, separators=(",", ":")) + "\n"
            stream.write(encoded)
            digest.update(encoded.encode())
        records[-1]["records_sha256"] = digest.hexdigest()
        stream.write(json.dumps(records[-1], separators=(",", ":")) + "\n")
    invalid = subprocess.run(
        ["python3", str(folder / "coble_kernel_public_incidence_audit.py"),
         "--shard", str(duplicate)],
        cwd=folder.parents[1], capture_output=True, text=True,
    )
    assert invalid.returncode != 0 and "repeated line class" in invalid.stderr
    forged = tmp_path / "forged-word.jsonl.gz"
    with gzip.open(output, "rt", encoding="utf-8") as stream:
        original = [json.loads(line) for line in stream]
    original[1]["parabolic_correction_word"] = [[0, 1]]
    digest = hashlib.sha256()
    with gzip.open(forged, "wt", encoding="utf-8") as stream:
        stream.write(json.dumps(original[0], separators=(",", ":")) + "\n")
        for row in original[1:-1]:
            encoded = json.dumps(row, separators=(",", ":")) + "\n"
            digest.update(encoded.encode())
            stream.write(encoded)
        original[-1]["records_sha256"] = digest.hexdigest()
        stream.write(json.dumps(original[-1], separators=(",", ":")) + "\n")
    invalid = subprocess.run(
        ["python3", str(folder / "coble_kernel_public_incidence_audit.py"),
         "--shard", str(forged)],
        cwd=folder.parents[1], capture_output=True, text=True,
    )
    assert invalid.returncode != 0 and "parabolic correction word" in invalid.stderr


def test_integral_shard_gzip_is_byte_reproducible(tmp_path):
    """Two runs with the same source produce identical compressed archives."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    outputs = [tmp_path / f"same-{i}.jsonl.gz" for i in range(2)]
    for output in outputs:
        subprocess.run(
            ["sage", str(folder / "coble_plane_integral_star_section.py"),
             "shard", "0", "23715", str(output), "1"],
            cwd=folder.parents[1], capture_output=True, text=True, check=True,
        )
    assert outputs[0].read_bytes() == outputs[1].read_bytes()
    archive = outputs[0].read_bytes()
    assert archive[:3] == b"\x1f\x8b\x08"
    assert archive[4:8] == b"\0" * 4  # No wall-clock timestamp in gzip header.
