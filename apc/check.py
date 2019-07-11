import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from helpers.conversion import convert_to_float
import logging

log = logging.getLogger(__name__)

class APC:
  """\
  Amazon Price Checker 
  """

  def __init__(self, userAgent):
    """Class constructor"""
    self.userAgent = userAgent

  def checkPrice(self, url):
    """Returns the price of an article referenced by its URL as a float"""
    #   ! Hard coded id search. Only tested on Amazon
    headers = {'User-Agent': self.userAgent}
    price = 0.0

    try:
      response = requests.get(url, headers=headers)
      # If the response was successful, no Exception will be raised
      response.raise_for_status()
    except HTTPError as http_err:
        log.error(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        log.error(f'Other error occurred: {err}')
        return None
    else:
      soup = BeautifulSoup(response.content, 'html.parser')
      standard_price = soup.find(id='price_inside_buybox')
      deal_price = soup.find(id='priceblock_dealprice')
      if standard_price:
        price = convert_to_float(standard_price.get_text())
      if deal_price:
        price = convert_to_float(deal_price.get_text())
      item = soup.find(id='productTitle').get_text().strip()
      return {'price': price, 'name': item}