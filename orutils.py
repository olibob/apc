import ruamel.yaml
import logging

log = logging.getLogger(__name__)

def get_config():
  """Reads yaml configuration file and return configuration object"""

  yaml = ruamel.yaml.YAML()

  with open("config.yaml", 'r') as config_file:
    try:
      config = yaml.load(config_file)
    except ruamel.yaml.scanner.ScannerError as exc:
      log.error(exc)
  return config

def convert_to_float(priceText):
  """Removes html withe space code (&nbsp;) and convert comma(,) to dot(.) to allow casting to float"""
  number = priceText.get_text().strip().replace('\xa0€', '').replace(',', '.')
  return float(number)