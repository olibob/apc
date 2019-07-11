from apc.check import APC
import helpers.configuration
import helpers.email as mail
import time
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

# Load configuration
config = helpers.configuration.read()
apc = APC(config['userAgent'])

while True:
  # Loop through articles
  for item in config['articles']:
    currentItem = apc.checkPrice(item['url'])
    if currentItem != None: 
      if currentItem['price'] < float(item['thresholdPrice']):
        log.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Price change detected")
        message = mail.create_multipart_message(
          config['sender'],
          config['receiver'],
          config['subject'],
          currentItem['name'],
          currentItem['price'],
          item['thresholdPrice'],
          item['url']
          )
        mail.send(
          config['login'],
          config['password'],
          config['sender'],
          config['receiver'],
          message
          )
      else:
        log.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} No price check detected :-(")
    else:
      log.error(f"No item found for URL: {item['url']}")
  time.sleep(config['checkingPeriod'])