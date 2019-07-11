import helpers.conversion as conv

def test_convert_to_float():
  assert conv.convert_to_float("45,65\xa0€") == 45.65

def test_convert_to_float_with_white_spaces():
  assert conv.convert_to_float("    45,65\xa0€ ") == 45.65