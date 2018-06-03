import requests

COIN_MARKET_CAP_URL = 'https://api.coinmarketcap.com'

def get_average_prices():
    # https://api.coinmarketcap.com/
    cmc_prices = "{host}/v2/ticker/?limit=10&convert=EUR&structure=array".format(host=COIN_MARKET_CAP_URL)
    cmc_response = requests.get(cmc_prices).json()
    cmc_data = cmc_response['data']
    mapped_cmc_response = []
    for data in cmc_data:
        mapped_cmc_response.append({
            'name': data['name'],
            'symbol': data['symbol'],
            'price_usd': data['quotes']['USD']['price'],
            'price_eur': data['quotes']['EUR']['price']
        })
    return mapped_cmc_response
