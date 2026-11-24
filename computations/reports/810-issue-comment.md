Intended orchestrator follow-up for research#810 (the issue connector is read-only; not posted).

Review am8w reads the discrete theorem MET. Its three residual findings are repaired:

A. moduli-construction.md:1092 and :1104 now cite lem:d2-labelled-base-monodromy, the dedicated unconditional principal-bundle proof. At :1293 the equality is proved directly there by local lifts, connectedness of PGL_3 and pullback, rather than by the conditional lemma. No unconditional use of the conditional clause remains.

B. The conditional proof at :1307 uses only #816: surjectivity on pi_1 and transport along the image of a loop of V. It does not assume the general pair/principal formula or the pair-family stack homotopy, because neither is needed for the group identity. No extra statement is added.

C. loop model at :1300 is replaced by the pair representation. The updated terminology sweep has zero matches for it or for the other labels removed by the terminology commits. The discrete torsor uses G, and pi_Q(q(1))=g x.

Checks: docs --source has only the 29 pre-existing missing-bibliography findings on untouched pages; docs-deps has 123 findings and none on the discrete theorem or the affected connected consumer, with no new dependency cycle. git diff --check is clean. The full docs gate remains blocked by a shared unresolved Git LFS asset, and CI was not observed.

See computations/reports/810-acceptance-item-by-item.txt and research/issue-810/proof.md. Issue 816 is not worked. A further independent Kimi review is required before #810 can close.
