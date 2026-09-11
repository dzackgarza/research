"""Reconcile ``archives/preamble/utilities.py`` with the live utility owner."""

import pytest

from dzack_research.preamble.utilities import lmap, lzip, to_var_names, zipsum


ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/utilities.py",
    "live_owner": "src/dzack_research/preamble/utilities.py",
    "disposition": "reconciled-live-owner",
}


def test_list_materializing_map_and_zip_retain_the_archive_semantics() -> None:
    assert lmap(lambda value: value * value, (1, 2, 3)) == [1, 4, 9]
    assert lzip((1, 2), ("a", "b")) == [(1, "a"), (2, "b")]


def test_generator_name_normalization_retains_the_archive_semantics() -> None:
    assert to_var_names("x, y z, t") == ["x", "yz", "t"]


def test_zipsum_is_generic_in_its_term_and_requires_equal_lengths() -> None:
    assert zipsum((2, 3), (5, 7), 0) == 31
    assert zipsum(
        (2, 3),
        ("a", "b"),
        "",
        term=lambda coefficient, value: coefficient * value,
    ) == "aabbb"

    with pytest.raises(ValueError):
        zipsum((1, 2), (3,), 0)
