import ruamel.yaml
import logging

log = logging.getLogger(__name__)

def read():
  """Reads yaml configuration file and return configuration object"""

  yaml = ruamel.yaml.YAML()

  with open("config.yaml", 'r') as config_file:
    try:
      config = yaml.load(config_file)
    except ruamel.yaml.scanner.ScannerError as exc:
      log.error(exc)
  return config