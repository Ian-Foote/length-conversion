from hypothesis import given
from hypothesis.strategies import floats, sampled_from

from conversions import Length, Lengths


@given(value=floats(), unit=sampled_from(Lengths))
def test_str(value, unit):
    length = Length(value, unit)

    assert str(length) == '{} {}'.format(value, unit.short_string)
