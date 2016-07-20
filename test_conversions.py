from hypothesis import given
from hypothesis.strategies import floats, sampled_from

from conversions import Length, Lengths


values = floats(allow_nan=False, allow_infinity=False)
units = sampled_from(Lengths)


@given(value=values, unit=units)
def test_str(value, unit):
    length = Length(value, unit)

    assert str(length) == '{:.4g} {}'.format(value, unit.short_string)


@given(value=values, old_unit=units, new_unit=units)
def test_as_unit(value, old_unit, new_unit):
    length = Length(value, old_unit)

    new_length = length.as_unit(new_unit)

    expected = value / old_unit.conversion_factor * new_unit.conversion_factor
    assert new_length.value == expected
