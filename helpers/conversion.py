
def convert_to_float(priceText):
  """Removes html withe space code (&nbsp;) and convert comma(,) to dot(.) to allow casting to float"""
  number = priceText.strip().replace('\xa0€', '').replace(',', '.')
  return float(number)