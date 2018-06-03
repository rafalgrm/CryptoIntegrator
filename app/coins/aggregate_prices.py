import requests
import json
import time

COIN_MARKET_CAP_URL = 'https://api.coinmarketcap.com'
CRYPTONATOR_URL = 'https://api.cryptonator.com'


def get_average_prices():
    # https://api.coinmarketcap.com/
    cmc_prices = "{host}/v2/ticker/?limit=10&convert=EUR&structure=array".format(
        host=COIN_MARKET_CAP_URL)
    cmc_response = requests.get(cmc_prices).json()
    cmc_data = cmc_response['data']
    mapped_cmc_response = []
    mapped_cryptonator_response = []
    requested_coins = []
    for data in cmc_data:
        requested_coins.append(data['symbol'].lower())
        coin = data['symbol'].lower()
        base_cryptonator_url = "{host}/api/ticker/{coin}-{fiat}"
        cryptonator_price_usd = base_cryptonator_url.format(
            host=CRYPTONATOR_URL, coin=coin, fiat='usd')
        bla1 = requests.get(cryptonator_price_usd)
        price_usd = 0
        if bla1.headers['content-type'] == 'application/json':
            price_usd_response = json.loads(bla1.text)
            if price_usd_response['success'] == True:
                price_usd = price_usd_response['ticker']['price']

        cryptonator_price_eur = base_cryptonator_url.format(
            host=CRYPTONATOR_URL, coin=coin, fiat='eur')
        bla2 = requests.get(cryptonator_price_eur)
        price_eur = 0
        if bla2.headers['content-type'] == 'application/json':
            price_eur_response = json.loads(bla2.text)
            if price_eur_response['success'] == True:
                price_eur = price_eur_response['ticker']['price']

        price1_usd = data['quotes']['USD']['price']
        price1_eur = data['quotes']['EUR']['price']
        average_usd = (float(price1_usd) + float(price_usd)) / 2
        average_eur = (float(price1_eur) + float(price_eur)) / 2
        if price_usd == 0:
            average_usd = price1_usd
        if price_eur == 0:
            average_eur = price1_eur
        mapped_cmc_response.append({
            'name': data['name'],
            'symbol': data['symbol'],
            'price_usd1': price1_usd,
            'price_eur1': price1_eur,
            'price_usd2': price_usd,
            'price_eur2': price_eur,
            'average_usd': average_usd,
            'average_eur': average_eur
        })
    # for coin in requested_coins:
    #     base_cryptonator_url = "{host}/api/ticker/{coin}-{fiat}"
    #     cryptonator_price_usd = base_cryptonator_url.format(host=CRYPTONATOR_URL, coin=coin, fiat='usd')
    #     price_usd_response = requests.get(cryptonator_price_usd).json()
    #     price_usd = price_usd_response['ticker']['price']
    #     cryptonator_price_eur = base_cryptonator_url.format(host=CRYPTONATOR_URL, coin=coin, fiat='eur')
    #     price_eur_response = requests.get(cryptonator_price_eur).json()
    #     price_eur = price_eur_response['ticker']['price']

    return mapped_cmc_response
