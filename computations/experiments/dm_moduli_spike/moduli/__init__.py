r"""Concrete moduli stacks M_{g,I} and Mbar_{g,I}."""

from __future__ import annotations

from .atlas_ownership import COMPACT_M1N_INSPECTABLE_MAX as COMPACT_M1N_INSPECTABLE_MAX
from .atlas_ownership import COMPACT_M2N_INSPECTABLE_MAX as COMPACT_M2N_INSPECTABLE_MAX
from .atlas_ownership import COMPACT_M3N_INSPECTABLE_MAX as COMPACT_M3N_INSPECTABLE_MAX
from .atlas_ownership import OPEN_M0N_INSPECTABLE_MAX as OPEN_M0N_INSPECTABLE_MAX
from .atlas_ownership import OPEN_M1N_INSPECTABLE_MAX as OPEN_M1N_INSPECTABLE_MAX
from .atlas_ownership import OPEN_M2N_INSPECTABLE_MAX as OPEN_M2N_INSPECTABLE_MAX
from .atlas_ownership import OPEN_M3N_INSPECTABLE_MAX as OPEN_M3N_INSPECTABLE_MAX
from .atlas_ownership import PROPER_M0N_INSPECTABLE_MAX as PROPER_M0N_INSPECTABLE_MAX
from .atlas_ownership import PROPER_M0N_OWNED_MAX as PROPER_M0N_OWNED_MAX
from .atlas_ownership import OwnedAtlasPresentation as OwnedAtlasPresentation
from .atlas_ownership import is_compact_m1n_level_owned as is_compact_m1n_level_owned
from .atlas_ownership import is_compact_m2n_igusa_owned as is_compact_m2n_igusa_owned
from .atlas_ownership import is_compact_m3n_del_pezzo_owned as is_compact_m3n_del_pezzo_owned
from .atlas_ownership import is_compact_m3n_hyperelliptic_owned as is_compact_m3n_hyperelliptic_owned
from .atlas_ownership import is_compact_m20_igusa_owned as is_compact_m20_igusa_owned
from .atlas_ownership import is_compact_m30_del_pezzo_owned as is_compact_m30_del_pezzo_owned
from .atlas_ownership import is_compact_m30_hyperelliptic_owned as is_compact_m30_hyperelliptic_owned
from .atlas_ownership import is_compact_m40_canonical_owned as is_compact_m40_canonical_owned
from .atlas_ownership import is_open_m0n_knudsen_owned as is_open_m0n_knudsen_owned
from .atlas_ownership import is_open_m1n_level_owned as is_open_m1n_level_owned
from .atlas_ownership import is_open_m2n_igusa_owned as is_open_m2n_igusa_owned
from .atlas_ownership import is_open_m3n_del_pezzo_owned as is_open_m3n_del_pezzo_owned
from .atlas_ownership import is_open_m3n_hyperelliptic_owned as is_open_m3n_hyperelliptic_owned
from .atlas_ownership import is_open_m20_igusa_owned as is_open_m20_igusa_owned
from .atlas_ownership import is_open_m30_del_pezzo_owned as is_open_m30_del_pezzo_owned
from .atlas_ownership import is_open_m40_canonical_owned as is_open_m40_canonical_owned
from .atlas_ownership import is_owned_etale_atlas_type as is_owned_etale_atlas_type
from .atlas_ownership import is_proper_m0n_kapranov_owned as is_proper_m0n_kapranov_owned
from .atlas_ownership import lookup_owned_etale_atlas as lookup_owned_etale_atlas
from .atlas_ownership import owned_etale_atlas_cardinality as owned_etale_atlas_cardinality
from .atlas_ownership import owned_etale_atlas_presentations as owned_etale_atlas_presentations
from .atlas_ownership import owned_etale_atlas_type_keys as owned_etale_atlas_type_keys
from .atlas_ownership import resolve_owned_etale_atlas as resolve_owned_etale_atlas
from .instances import (
    Groupoid,
    M_gI,
    M_gn,
    Mbar_gI,
    Mbar_gn,
    ModuliProblem,
    ModuliStack,
    SmoothPointedCurveModuliProblem,
    StablePointedCurveModuliProblem,
)

__all__ = [
    "COMPACT_M1N_INSPECTABLE_MAX",
    "COMPACT_M2N_INSPECTABLE_MAX",
    "COMPACT_M3N_INSPECTABLE_MAX",
    "Groupoid",
    "M_gI",
    "M_gn",
    "Mbar_gI",
    "Mbar_gn",
    "ModuliProblem",
    "ModuliStack",
    "OPEN_M0N_INSPECTABLE_MAX",
    "OPEN_M1N_INSPECTABLE_MAX",
    "OPEN_M2N_INSPECTABLE_MAX",
    "OPEN_M3N_INSPECTABLE_MAX",
    "OwnedAtlasPresentation",
    "PROPER_M0N_INSPECTABLE_MAX",
    "PROPER_M0N_OWNED_MAX",
    "SmoothPointedCurveModuliProblem",
    "StablePointedCurveModuliProblem",
    "is_compact_m1n_level_owned",
    "is_compact_m20_igusa_owned",
    "is_compact_m2n_igusa_owned",
    "is_compact_m30_del_pezzo_owned",
    "is_compact_m30_hyperelliptic_owned",
    "is_compact_m3n_del_pezzo_owned",
    "is_compact_m3n_hyperelliptic_owned",
    "is_compact_m40_canonical_owned",
    "is_open_m0n_knudsen_owned",
    "is_open_m1n_level_owned",
    "is_open_m20_igusa_owned",
    "is_open_m2n_igusa_owned",
    "is_open_m30_del_pezzo_owned",
    "is_open_m3n_del_pezzo_owned",
    "is_open_m3n_hyperelliptic_owned",
    "is_open_m40_canonical_owned",
    "is_owned_etale_atlas_type",
    "is_proper_m0n_kapranov_owned",
    "lookup_owned_etale_atlas",
    "owned_etale_atlas_cardinality",
    "owned_etale_atlas_presentations",
    "owned_etale_atlas_type_keys",
    "resolve_owned_etale_atlas",
]
