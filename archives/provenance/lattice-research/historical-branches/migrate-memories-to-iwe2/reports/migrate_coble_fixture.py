#!/usr/bin/env python3
"""Migrate tests/fixtures/coble_literature_fixtures.json off the retired local basis
(file + bibliographic_key) onto the Zotero-instance contract
(zotero_item_key + zotero_attachment_key + lines). All keys/lines below were resolved and
verified on the workstation Zotero instance on 2026-06-18. parse -> modify -> dump.
"""

import json
import pathlib

FIX = pathlib.Path("/home/dzack/research/tests/fixtures/coble_literature_fixtures.json")

# entry id -> list of verified Zotero sources (item, attachment, lines[, claim])
SOURCES = {
    "K3_lattice_L": [("LFKH3D95", "UXUDEAF4", "197-198")],
    "S_dP": [("LFKH3D95", "UXUDEAF4", "222")],
    "T_dP": [("LFKH3D95", "UXUDEAF4", "222")],
    "S_En": [("LFKH3D95", "UXUDEAF4", "223")],
    "T_En": [("LFKH3D95", "UXUDEAF4", "223"),
             ("LFKH3D95", "UXUDEAF4", "28")],  # moduli_role: F_{En,2} definition
    "L_Nik_plus": [("LFKH3D95", "UXUDEAF4", "224")],
    "L_Nik_minus": [("LFKH3D95", "UXUDEAF4", "224")],
    "coble_surface_definition": [("3V5FLBYU", "C8QJYLY2", "619-620"),
                                 ("3V5FLBYU", "C8QJYLY2", "85")],
    "classical_coble_surface_example": [("I6FFLGJU", "ALXWRAM7", "95")],
    "coble_moduli_period_quotient": [("I6FFLGJU", "ALXWRAM7", "109"),
                                     ("I6FFLGJU", "ALXWRAM7", "91")],
    "smooth_irreducible_coble_surface_blowup_model": [("3V5FLBYU", "C8QJYLY2", "737")],
    "ten_nodal_plane_sextic": [("3V5FLBYU", "C8QJYLY2", "150"),
                               ("3V5FLBYU", "C8QJYLY2", "1272-1274")],
    # Thas 1994 item (human-created KH4WH7AY); extraction attached via the cloud Web API
    # as child D85F3BV8 (workstation sync was inconsistent). Line 12 = abstract stating
    # the Desargues configuration -> 10-nodal rational sextic.
    "desargues_configuration_sextic": [("KH4WH7AY", "D85F3BV8", "12")],
}

# T_En_cusp_orbits_sterk is a computation entry; its literature sub-sources map to Zotero.
COMPUTATION_SOURCES = {
    "T_En_cusp_orbits_sterk": [
        {"zotero_item_key": "LFKH3D95", "zotero_attachment_key": "UXUDEAF4", "lines": "70",
         "claim": "cusp diagrams of F_{(10,10,0)} are recalled and mapped"},
        {"zotero_item_key": "SW47ULJ5", "zotero_attachment_key": "44T7F33C",
         "claim": "Sterk (1991) original computation of the Enriques cusp diagram"},
    ],
}

# No entries remain blocked: the Thas extraction was attached via the cloud Web API.
BLOCKED: dict = {}


def main() -> None:
    entries = json.loads(FIX.read_text())
    seen = set()
    for entry in entries:
        eid = entry["id"]
        seen.add(eid)
        if eid in SOURCES:
            entry["sources"] = [
                {"zotero_item_key": it, "zotero_attachment_key": at, "lines": ln}
                for (it, at, ln) in SOURCES[eid]
            ]
        elif eid in COMPUTATION_SOURCES:
            entry["sources"] = COMPUTATION_SOURCES[eid]
        elif eid in BLOCKED:
            entry["sources"] = [BLOCKED[eid]]
        else:
            raise SystemExit(f"unmapped fixture entry: {eid}")
    missing = (set(SOURCES) | set(COMPUTATION_SOURCES) | set(BLOCKED)) - seen
    assert not missing, f"mapping references absent entries: {missing}"
    FIX.write_text(json.dumps(entries, indent=2) + "\n")
    print(f"migrated {len(entries)} entries; blocked: {list(BLOCKED)}")


if __name__ == "__main__":
    main()
