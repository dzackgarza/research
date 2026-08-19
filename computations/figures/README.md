# Figures

Rendered figures of the hyperbolic-lattice and Enriques work. Each family below
names the source that produces it, so a figure can be regenerated rather than
edited.

- `S1_H0.png` ... `S1_H20.png` — the twenty-one elliptic subdiagrams of the
  Sterk 1 Coxeter diagram, each drawn as a highlighted induced subgraph of the
  full diagram. Produced by `archives/notebooks/Isometry Searching.ipynb`
  (`G1.plot(subgraph=H).save(f"S1_H{i}.png")`); the same enumeration is owned by
  `preamble/.../coxeter_diagrams.sage` (`elliptic_subdiagram_poset`) and
  regenerated under test by `tests/test_sterk_artifacts.sage`.
- `18_2_0_display.png`, `Sterk3.png` — the (18, 2, 0) root configuration and the
  Sterk 3 diagram, from `archives/notebooks/Sterk IAS Plotting.ipynb`.
- `light_cone.png`, `paraboloid_in_cone.png`, `hyperboloid_sheets.png` — the
  light cone of a signature-(1, n) form, the affine paraboloid section that
  models the hyperbolic plane, and the one- and two-sheeted hyperboloids. From
  `archives/notebooks/exports/Untitled1_Code_Only.sage` (the Cone
  Visualizations notebook).
- `A2_tiling.png`, `tilde_A2_tiling.png`, `A1xA1_tiling.png`, `pi_m_tiling.png`
  — reflection tilings of the plane by the Weyl group of A_2, of the affine
  A_2~, of A_1 + A_1, and by a triangle with angle pi/m. Same notebook.
- `tesselation_start.png`, `tesselation_0.png` ... `tesselation_5.png`,
  `tesselation_end.png` — successive reflections of an ideal triangle in the
  disc model, produced by `computations/scripts/hyperbolic_diagrams.sage`
  (`tri1.save_image(...)`).
- `asymptotically_parallel.svg`, `asymptotically_parallel_plane_model.svg`,
  `Ultraparallel.svg`, `ultraparallel_plane_model.svg` — the two ways two
  geodesics can fail to meet: asymptotically parallel
  (meeting at one ideal point) and ultraparallel (a common perpendicular),
  drawn in both the disc and the half-plane model. From
  `computations/scripts/hyperbolic_diagrams.sage`
  (`generate_asymptotically_parallel_svg`,
  `generate_asymptotically_parallel_plane_model`).
  `asymptotically_parallel_disc_model_earlier_run.svg` is an earlier rendering
  of the disc-model picture, kept because it differs from the current one.
- `E6_diagram.gv` — the E_6 Coxeter diagram as a graphviz source: a chain of
  five vertices with a branch at the third.
- `Ultraparallel.png`, `graph.jpg`, `a.svg` — renderings kept with the rest;
  no producing cell is recorded for them.
