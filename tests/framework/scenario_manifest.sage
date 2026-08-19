"""Canonical mapping from mathematical certificate families to scaffolded test files.

This is a planning index for the scheme-framework certification scaffold, derived
from ``~/Downloads/Mathematical-Certification-Corpus.md``. Each family below is
intended to become a concrete test module in this directory.
"""

SCENARIO_MANIFEST = {
    "schemes_pullback": [
        "1 Affine fibre products",
        "2 Inverse images of closed subschemes",
        "3 Graphs and diagonals",
        "4 Equalizers and fixed subschemes",
        "5 Diagonals in projective space",
        "6 Scheme-theoretic image",
        "3053-3055 Categorical pullbacks",
        "3274-3434 Scheme-theoretic image fixtures",
    ],
    "projective_products_picard": [
        "7 Picard group and line bundles",
        "325-356? Products of projective spaces, Picard groups and cohomology",
        "33x Complete intersection invariants",
        "3461-3567 Complete linear systems and jets",
    ],
    "coxeter_and_algebra": [
        "12 Cox ring of a projective product",
        "13 Degree restrictions of graded morphisms",
        "14 Section rings",
        "2722-2850 Cox algebra and section rings",
    ],
    "bundles_and_base_change": [
        "15 Relative-Spec primitive",
        "16 Base change",
        "17 Parameter space of sections",
        "5630-5660 Cyclic-cover families, affine parameter spaces",
    ],
    "linear_systems": [
        "19 Complete linear systems",
        "20 Base loci",
        "21 Restriction and evaluation",
        "22 Jets and imposed singularities",
        "23 Bertini families",
    ],
    "group_actions": [
        "24 Linearizations",
        "25 Maschke and isotypic projectors",
        "26 Cyclic diagonal actions",
        "27 Diagonal sign actions",
        "28 Equivariant evaluation at fixed points",
        "29 Holomorphic Lefschetz formula",
    ],
    "fixed_loci": [
        "30 Projective linear automorphisms",
        "31 Permutation of factors",
        "32 Diagonal sign actions",
        "30-35 Fixed-point families and invariant divisors",
        "1900+ Fixed-locus and representation triangles",
    ],
    "curves": [
        "33 Genus and adjunction",
        "34 Fixed-point evaluation",
        "35 Invariant divisors versus eigensections",
        "36 Singular orbits",
        "39 Odd A-types forced by parity",
    ],
    "singularities": [
        "40 Regularity and tangent spaces",
        "41 Jacobian criterion",
        "42 Milnor and Tjurina algebras",
        "43 ADE normal forms",
        "44-45 Plane A_n and D_n families",
    ],
    "covers_and_involutions": [
        "47 Cyclic-cover datum",
        "48 Smoothness",
        "49 Canonical bundle",
        "50 (4,4) K3 family",
        "51 Deck involution and ramification",
        "52 Two lifts of tau",
        "53 Fixed loci of the lifts",
        "54 Action on holomorphic two-form",
        "55 Enriques quotient",
    ],
    "quotients_complete_intersections": [
        "58 Local invariant ring",
        "59 Global invariant anticanonical morphism",
        "60 Complete-intersection invariants",
        "61 General complete-intersection family",
    ],
    "non_toric_blowups": [
        "62 Blowups of the plane",
        "63 Strict transforms of plane curves",
        "64 Del Pezzo blowups",
        "15.1 Del Pezzo blowup benchmark",
    ],
    "external_sources": [
        "65-68 LMFDB/curve/field/OEIS/GRDB references",
        "70 Kreuzer–Skarke reflexive polytopes",
        "71 Fanography and classified Fano families",
        "16-18 concrete external database probes",
    ],
    "composite_certificates": [
        "72 Fixed locus-representation-Lefschetz triangle",
        "73 Picard-cohomology-linear-system-image cycle",
        "74 Local-global singularity cycle",
        "75 Cyclic-cover cycle",
        "76 Quotient cycle",
        "77 Gluing-independence cycle",
    ],
}

