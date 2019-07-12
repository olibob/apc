import pytest
import helpers.conversion as conv

@pytest.mark.parametrize('text, expected', [("45,65\xa0€", 45.65), ("    45,65\xa0€ ", 45.65)])

def test_convert_to_float(text, expected):
  assert conv.convert_to_float(text) == expected