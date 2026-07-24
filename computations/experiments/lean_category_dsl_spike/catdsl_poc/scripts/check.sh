#!/usr/bin/env bash
# Verify CatDSL from a clean checkout.
#
# Lake / mathlib live at the repository root (not this directory).
# Requires elan (AUR `elan-lean`), NOT a distro `lean`.
set -euo pipefail
cd "$(dirname "$0")/.."
root="$(git rev-parse --show-toplevel)"
cd "$root"

lake exe cache get      # if this is honoured, no Mathlib module is compiled
lake build CatDSL       # the library
lake build CatDSLTest   # |L| = 4, the number/nth tables, the registry, the surface
