"""Guards for the research#663 (REL) records: Lemma C and the odd-local perfection input."""

import hashlib
import json
import subprocess
from pathlib import Path

FOLDER = Path(__file__).resolve().parents[2] / "computations/reports"


def test_coble_663_rel_lemma_c_record():
    artifact = FOLDER / "coble_663-rel-lemma-c.json"
    before = artifact.read_bytes()
    data = json.loads(before)
    assert data["schema"] == "coble-663-rel-lemma-c-v1"
    assert data["script_sha256"] == hashlib.sha256(
        (FOLDER / "coble_663-rel-lemma-c.py").read_bytes()
    ).hexdigest()
    assert data["lattice"]["T_co_is_B_twice"] is True
    assert data["lattice"]["B_determinant"] == -1
    assert data["lattice"]["T_co_determinant"] == -2048
    assert data["generators"]["norm_minus_one_vectors_entries_in_minus_one_zero_one"] == 3282
    assert data["generators"]["distinct_reflections"] == 1641
    assert data["images"]["dim_so_11_f2"] == 55
    assert data["images"]["mod_8"]["layer_dimensions"] == [55, 54]
    assert data["images"]["mod_16"]["layer_dimensions"] == [55, 54, 55]
    assert data["membership_mod_16"] == {
        "delta_E8": True, "minus_id": True, "epsilon_prime": True,
    }
    assert data["controls"]["positive_kernel_fifty_five_generators_layer_dimensions"] == [55, 54, 55]
    assert data["controls"]["reflection_in_e0_in_subgroup_mod_16"] is False
    assert data["controls"]["eps_diag_minus_one_minus_one_in_subgroup_mod_16"] is True
    subprocess.run(
        ["sage", str(FOLDER / "coble_663-rel-lemma-c.py")],
        cwd=FOLDER.parents[1], check=True, capture_output=True, text=True,
    )
    assert artifact.read_bytes() == before


def test_coble_663_rel_odd_local_perfection_record():
    artifact = FOLDER / "coble_663-rel-odd-local-perfection.json"
    before = artifact.read_bytes()
    data = json.loads(before)
    assert data["schema"] == "coble-663-rel-odd-local-perfection-v1"
    assert data["script_sha256"] == hashlib.sha256(
        (FOLDER / "coble_663-rel-odd-local-perfection.py").read_bytes()
    ).hexdigest()
    assert data["source_sha256"] == hashlib.sha256(
        (FOLDER / "coble_kernel_fifty_six_congruence_generators.json").read_bytes()
    ).hexdigest()
    assert data["unipotent_count"] == 46
    assert [row["prime"] for row in data["records"]] == [3, 5, 7, 11, 13]
    assert all(row["adjoint_commutator_rank"] == 55 for row in data["records"])
    subprocess.run(
        ["sage", str(FOLDER / "coble_663-rel-odd-local-perfection.py")],
        cwd=FOLDER.parents[1], check=True, capture_output=True, text=True,
    )
    assert artifact.read_bytes() == before
