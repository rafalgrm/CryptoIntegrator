import requests
import time
import datetime

CRYPTOCOMPARE_URL = 'https://min-api.cryptocompare.com'
APP_NAME = 'CryptoIntegrator'
URL = '{host}/data/pricehistorical?fsym={currency_from}&tsyms=USD,EUR&ts={timestamp}&extraParams={APP_NAME}'


def format_dates():
    now = datetime.datetime.now()
    basic_date_string = '{year}-{month}-01'
    time_delta = datetime.timedelta(days=30)
    dates = []
    for i in range(12):
        current_year = now.year
        current_month = now.month
        dates.append(basic_date_string.format(
            year=current_year, month=current_month))
        now -= time_delta
    return dates


def get_prices_history_monthly(coin_symbol):
    dates = format_dates()
    values_usd = []
    values_eur = []
    for (idx, date) in enumerate(dates):
        date = datetime.datetime.strptime(date, "%Y-%m-%d").timetuple()
        timestamp = int(time.mktime(date))
        url_formatted = URL.format(
            host=CRYPTOCOMPARE_URL, currency_from=coin_symbol, timestamp=timestamp, APP_NAME=APP_NAME)
        cryptocompare_response = requests.get(url_formatted).json()
        values_usd.append(cryptocompare_response[coin_symbol]['USD'])
        values_eur.append(cryptocompare_response[coin_symbol]['EUR'])
    return {
        'labels': dates[::-1],
        'values_usd': values_usd[::-1],
        'values_eur': values_eur[::-1]
    }
