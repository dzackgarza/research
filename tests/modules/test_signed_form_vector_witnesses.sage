r"""The diagonal function of a bilinear Gram matrix uses its symmetric part.

[2] is positive definite; diag(2,-2) is indefinite; the nonsymmetric
matrix [[0,2],[0,0]] has diagonal function 2xy, of both signs.
"""

import pytest

from dzack_research.preamble.all import *


@pytest.mark.parametrize("rows, has_negative", (([[2]], False), ([[2, 0], [0, -2]], True), ([[0, 2], [0, 0]], True)))
def test_signed_witnesses_use_the_actual_diagonal_form(rows, has_negative):
    module = ZZ.free_module(tuple(range(len(rows))))
    formed = FormModules(ZZ)(module.bilinear_hom_space(ZZ)(rows))

    positive = formed.positive_vector()
    negative = formed.negative_vector()

    assert positive in formed
    assert formed.norm(positive) > 0
    if has_negative:
        assert negative in formed
        assert formed.norm(negative) < 0
    else:
        assert negative is None
