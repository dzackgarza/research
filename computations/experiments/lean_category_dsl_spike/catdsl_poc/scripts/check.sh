#!/usr/bin/env bash
# Verify the project from a clean checkout.
#
# Requires elan (AUR `elan-lean`), NOT a distro `lean`: Mathlib's cache is
# keyed to the exact official toolchain build, so any other Lean silently
# recompiles all ~7900 modules. elan reads `lean-toolchain` and fetches the
# right one automatically.
set -euo pipefail
cd "$(dirname "$0")/.."

lake exe cache get      # if this is honoured, no Mathlib module is compiled
lake build CatDSL       # the library
lake build CatDSLTest   # |L| = 4, the number/nth tables, the registry, the surface
