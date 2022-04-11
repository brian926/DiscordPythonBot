from bs4 import BeautifulSoup
import requests
import json

def get_ticker_info(ticker):
    results = "The price of {0} is {1}, it has changed {2} in the last 24 hours".format(ticker, get_ticker_price(ticker), get_ticker_change(ticker))
    return results

def get_ticker_price(ticker):
  # Curl ticker info
  url = "https://api.binance.com/api/v3/ticker/24hr?symbol="+ticker
  HTML = requests.get(url)
  soup = BeautifulSoup(HTML.text, 'html.parser')
  site_json = json.loads(soup.text)
  round_num = float(site_json['askPrice'])
  results = round(round_num, 2)
  return str(results)

def get_ticker_change(ticker):
  # Curl ticker info
  url = "https://api.binance.com/api/v3/ticker/24hr?symbol="+ticker
  HTML = requests.get(url)
  soup = BeautifulSoup(HTML.text, 'html.parser')
  site_json = json.loads(soup.text)
  return site_json['priceChangePercent']
