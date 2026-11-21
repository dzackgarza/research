Intended orchestrator follow-up for research#810 (the issue connector is read-only; not posted).

Review mihf confirmed the torsor loop comparison and base naturality. Its two remaining findings are repaired in 58d5b3780c and f2566ce59d:

1. The invalid section deformation is replaced by Theta_u=(beta(1-u), gamma~ . sigma_u). At u=0 this is the original pair; at u=1 it is the loop of U with group element e. Transport along beta is phi_g, so sigma_1^*=phi_g^{-1} and composition gives phi_g^{-1} gamma~^*. The projection is Q to U, and the fibre action is cited to the construction immediately after Noohi Definition 18.13.
2. The proved descent is removed from the unproved hypotheses at moduli-construction.md:2309. The tautological-system descriptions at :31 and lattices.md:165,174 now consistently name two inputs. The distinct three inputs below lattices.md:165 belong to the separate refutation.

Search finds no open conditional descent hypothesis. docs-deps has no finding on the edited descent blocks and no new cycle; docs --source has only pre-existing findings on untouched pages. The full docs gate remains blocked by an unresolved Git LFS asset. CI was not observed.

See computations/reports/810-acceptance-item-by-item.txt for itemized status and research/issue-810/proof.md for the updated clean proof. A further Kimi review is required before #810 can close.


Terminology follow-up: all coinages are removed in favor of loops and homotopies of maps of stacks (Noohi Definitions 17.2 and 17.5) and G-paths (Bridson--Haefliger III.G 3.1, 3.5 and 3.6). No direct Noohi-stack versus G-path group comparison theorem was found in Noohi, Moerdijk or Bridson--Haefliger. In particular III.G 3.9(1) only gives the action-group exact sequence, so it was not used as a substitute for the direct comparison proof.
