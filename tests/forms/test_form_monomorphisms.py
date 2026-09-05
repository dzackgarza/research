import pytest

from dzack_research.preamble.all import BasedFreeModule, ZZ
from dzack_research.preamble.categories.abstract_categories.hom_categories import category_packet
from dzack_research.preamble.categories.forms import BilinearForms
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    FormEmbedding,
    FormModule,
    FormModules,
    form_embedding,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _zero_formed_line():
    module = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    return FormModule(BilinearForms(module, ZZ)(lambda _left, _right: ZZ.zero()))


def test_form_embedding_is_certified_by_the_mono_subcategory() -> None:
    formed = _zero_formed_line()
    embedding = form_embedding(
        formed,
        formed,
        {"e": formed.module_generator("e")},
    )
    monos = category_packet(FormModules(ZZ)).Monos().Of(formed, formed)

    assert monos.arrow_set() is FormModules(ZZ).Mor(formed, formed)
    assert embedding in monos
    assert "is_injective" not in FormEmbedding.__dict__


def test_form_embedding_rejects_a_form_preserving_non_monomorphism() -> None:
    formed = _zero_formed_line()
    with pytest.raises(ValueError, match="injective underlying module map"):
        form_embedding(formed, formed, {"e": formed.zero()})
