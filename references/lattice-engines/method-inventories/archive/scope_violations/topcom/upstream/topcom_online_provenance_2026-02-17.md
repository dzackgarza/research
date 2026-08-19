# TOPCOM Online Provenance Snapshot

- Snapshot date (UTC): 2026-02-17 23:05:51 UTC
- Auditor: Codex
- Scope: validate canonical upstream package existence, command inventory, option/argument surfaces, and domain assumptions for adding first-class TOPCOM checklist/reference docs.

---

## Canonical Upstream Sources Consulted

1. TOPCOM project page (University of Bayreuth):  
   `https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM/`
2. TOPCOM manual PDF (linked by upstream project page):  
   `https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM/TOPCOM-manual.pdf`
3. TOPCOM command manual mirror (`topcom(7)`, package man page generated from upstream manual):  
   `https://manpages.debian.org/testing/topcom/topcom.7.en.html`

---

## Extracted Evidence (source-backed claims used in docs)

- Upstream project identity and scope:
  - TOPCOM is presented as software focused on triangulations of point configurations and oriented matroids.
  - Upstream page links the manual and source tarballs.

- Input/IO and data-model contract:
  - Command families split into `points2*` and `chiro2*` workflows.
  - Point configurations are consumed as matrix input; homogenized convention and oriented-matroid/chirotope pathways are documented in the command manual text.
  - CLI workflow is stdin/stdout oriented.

- Command inventory evidence:
  - Documented commands include conversion/primitives (`points2chiro`, `chiro2dual`, circuits/cocircuits),
    triangulation seeds (`points2triangs`, `chiro2triangs`, fine/non-symmetric variants),
    full enumerators (`points2alltriangs`, `points2allfinetriangs`, `points2nalltriangs`, `points2nallfinetriangs`, and chirotope counterparts),
    secondary-polytope/utility commands (`points2flips`, `points2facets`, `points2placingtriang`, `checkregularity`, `allfinetriangs2subdivs`),
    and generators (`gen_points`, `gen_chiro`).

- Option/argument surface evidence:
  - Cross-command flags documented upstream include `--regular`, `--nonregular`, `--unimodular`,
    `--reducepoints`, `--noinsertion`, `--heights`, `--flipdeficiency`, `--checktriang`,
    `-i/--input-chiro`, and `-v/--verbose`.

---

## Notes

- The command manual mirror was used as a searchable textual rendering of the upstream manual for precise option wording.
- No conflicting source statements were observed for the command names/flags included in this pass.
