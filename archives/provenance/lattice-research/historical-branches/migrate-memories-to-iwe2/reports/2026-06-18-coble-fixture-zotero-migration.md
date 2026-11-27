# Coble fixtures → Zotero citation migration (in progress)

Migrating `tests/fixtures/coble_literature_fixtures.json` (14 entries) off the retired
local basis (`theory/references/literature/*.md` + `bibliographic_key`) onto the Zotero
instance contract (item key + `text/markdown` extraction attachment key + verified line).
All keys/lines below were resolved and verified on the workstation Zotero instance
(`http://127.0.0.1:23119/api/users/0` over SSH, `qmode=titleCreatorYear`) on 2026-06-18.
Nothing here is fabricated; line numbers are the WORKSTATION extraction's (they differ
from the old local copies).

## Source map (Zotero item → markdown extraction attachment)

| source | item key | md attachment | extraction present? |
|---|---|---|---|
| AEGS 2023 (Compact moduli of Enriques surfaces, deg 2) | `LFKH3D95` | `UXUDEAF4` | yes |
| Dolgachev–Kondō 2013 (Rationality of moduli of Coble/nodal Enriques) | `I6FFLGJU` | `ALXWRAM7` | yes |
| Sterk 1991 (Compactifications of the period space of Enriques surfaces, I) | `SW47ULJ5` | `44T7F33C` | yes |
| Pieroni 2026 (Coble surfaces: projective models and automorphisms) | `3V5FLBYU` | — | **NO — extraction not attached** |
| Thas 1994 (Desargues-configuration sextic) | — | — | **not found in library** |

## Verified entries (ready to migrate)

| fixture id | new source (item / attachment / line) | verbatim fact |
|---|---|---|
| K3_lattice_L | LFKH3D95 / UXUDEAF4 / 197-198 | "L=II_{3,19}=U^3⊕E_8^2 ≃ H^2(X,Z) ... even, unimodular, signature (3,19)" |
| S_dP | LFKH3D95 / UXUDEAF4 / 222 | "S_dP = U(2) = (2,2,0)_1" |
| T_dP | LFKH3D95 / UXUDEAF4 / 222 | "T_dP = U⊕U(2)⊕E_8^2 = (20,2,0)_2" |
| S_En | LFKH3D95 / UXUDEAF4 / 223 | "S_En = U(2)⊕E_8(2) = (10,10,0)_1" |
| T_En | LFKH3D95 / UXUDEAF4 / 223 | "T_En = U⊕U(2)⊕E_8(2) = (12,10,0)_2" |
| classical_coble_surface_example | I6FFLGJU / ALXWRAM7 / 95 | "blow-up of the projective plane at the ten nodes of an irreducible plane curve C of degree 6" |

## Line-pending (source resolved; exact workstation line not yet verified)

- L_Nik_plus, L_Nik_minus — AEGS (LFKH3D95/UXUDEAF4); not on the 222-223 table, need their line.
- coble_moduli_period_quotient — Dolgachev (I6FFLGJU/ALXWRAM7); the N=⟨2⟩+E(2), D(N)/O(N) dim-9 result, line not yet pinned.
- T_En_cusp_orbits_sterk — AEGS "two 0-cusps and two 1-cusps" near UXUDEAF4:70-76; Sterk
  attribution (SW47ULJ5/44T7F33C) for the cusp diagram, specific line not pinned.

## Re-source opportunity

- coble_surface_definition was attributed to **Pieroni** in the fixture, but the same
  definition (|-K_S|=∅, |-2K_S|≠∅) appears in **Dolgachev–Kondō** at `ALXWRAM7:95`. It can
  be re-sourced to Dolgachev (citable now) instead of waiting on the Pieroni extraction.

## Blocked (maintainer action required — do not fabricate)

- **Pieroni 2026 has no markdown extraction attachment.** Entries
  `smooth_irreducible_coble_surface_blowup_model` and `ten_nodal_plane_sextic` cannot be
  cited until the PDF is extracted (MinerU) and attached to item `3V5FLBYU` via the
  `zotero-pdf-extraction-maintainer` workflow.
- **Thas 1994 is not in the Zotero library.** Entry `desargues_configuration_sextic`
  needs the source imported + extracted first.

## Remaining steps

1. Pin the line-pending entries (3-4 targeted workstation greps).
2. Rewrite the fixture JSON to the Zotero source schema
   (`{zotero_item_key, zotero_attachment_key, lines}`) — via the `config-file-editing`
   skill (jq/python, not raw edit).
3. Write the consuming test (currently nothing consumes the fixture) that builds each
   object through the lattice DSL and asserts the cited properties.
4. Maintainer: extract+attach Pieroni 2026; import+extract Thas 1994.
