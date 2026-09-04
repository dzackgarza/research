r"""Cited mathematical facts, as data.

`DEV-41`: a fixture module imports nothing from the code under test.  See
``README.md`` beside this file for the schema and the rules.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Fact:
    r"""One mathematical fact, with the source it is supposed to come from.

    ``verified`` says whether a human has checked this row *against that
    source*.  A row moved out of an implementation and given a citation is
    unverified until someone reads the paper: the citation records where the
    fact should come from, the flag records whether anyone has confirmed it
    does, and neither is allowed to be silent.
    """

    value: object
    citation: str
    locator: str
    verified: bool = False


__all__ = ["Fact"]
