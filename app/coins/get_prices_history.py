import requests
import time
import datetime

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

CRYPTOCOMPARE_URL = 'https://min-api.cryptocompare.com'


def get_prices_history_monthly():
    basic_date_string = '{year}-{month}-01'
    year = 2017
    extraParams = 'CryptoIntegrator'
    url = '{host}/data/pricehistorical?fsym=BTC&tsyms=USD,EUR&ts={timestamp}&extraParams={extraParams}'
    values_usd = []
    values_eur = []
    for (idx, label) in enumerate(MONTHS):
        current_date = basic_date_string.format(year=year, month=(idx+1))
        timestamp = int(time.mktime(datetime.datetime.strptime(
            current_date, "%Y-%m-%d").timetuple()))
        url_formatted = url.format(
            host=CRYPTOCOMPARE_URL, timestamp=timestamp, extraParams=extraParams)
        cryptocompare_response = requests.get(url_formatted).json()
        values_usd.append(cryptocompare_response['BTC']['USD'])
        values_eur.append(cryptocompare_response['BTC']['EUR'])
    return {
        'labels': MONTHS,
        'values_usd': values_usd,
        'values_eur': values_eur
    }
