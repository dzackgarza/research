r"""Archive reconciliation for number fields and their owned arithmetic views.

The archived one-object presentation is split at its mathematical owners: the
field retains degree, discriminant, embeddings and element endomorphisms, while
its selected integral basis belongs to the selected order underlying the field.
"""

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/algebras/number_fields.sage",
    "live_owner": "src/dzack_research/preamble/categories/rings/number_fields.py",
    "disposition": "reconciled-live-owner",
}

from dzack_research.preamble.all import QuadraticField




def test_number_field_integrality_is_not_membership_in_the_selected_power_order() -> None:
    field = QuadraticField(5, "a")
    a = field.primitive_element()
    integral = (field.one() + a) / 2

    assert integral.is_integral()
    assert not (field.one() / 2).is_integral()


