r"""Importing the package at collection time makes a broken public re-export
fail loudly during collection instead of surfacing mid-test."""

import dm_moduli_spike  # noqa: F401
