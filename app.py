import csv
import os
import sqlite3

from io import StringIO
from flask import Flask, g, render_template, jsonify, make_response, request, redirect, url_for
from flask_bootstrap import Bootstrap

from tools.twitter_scrape import clean_tweet
from twitter.get_tweets import get_tweets, search_tweets

from coins.aggregate_prices import get_average_prices
from coins.get_prices_history import get_prices_history_monthly

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)

app.config.update({
    'DATABASE': os.path.join(app.root_path, 'database.sqlite'),
    'SECRET_KEY': 'dev',
    'USERNAME': 'admin',
    'PASSWORD': 'admin'
})

app.config.from_pyfile('config.py')


@app.route('/')
@app.route('/index')
def index():
    result = get_tweets(app, 10)
    return render_template('index.html', messages=result)


@app.route('/tweets')
def get_tweets_endp():
    return jsonify({'tweet_texts': get_tweets(app, 10)})


@app.route('/search/<query>')
def search_endp(query):
    result = search_tweets(app, query)
    return render_template('search.html', result=result, query=query)


@app.route('/download/search/<query>')
def download_search_endp(query): # TODO move to separate place, add header to CSV
    result = search_tweets(app, query)
    io = StringIO()
    csv_writer = csv.writer(io)
    csv_writer.writerows([[clean_tweet(tweet['text'].replace('\n', '').replace('\r', '')), tweet['created_at']] for tweet in result])
    output = make_response(io.getvalue())
    output.headers['Content-Disposition'] = 'attachment; filename=tweets.csv'
    output.headers['Content-type'] = 'text/csv'
    return output


@app.route('/prices/average')
def display_average_prices():
    return render_template('coins/average.html', result=get_average_prices())


@app.route('/prices/history/monthly/<coin_symbol>')
def display_prices_history(coin_symbol):
    data = get_prices_history_monthly(coin_symbol)
    return render_template('coins/history.html', values_usd=data['values_usd'], values_eur=data['values_eur'], labels=data['labels'])


@app.route('/admin')
def admin():
    db = get_db()
    cur = db.execute('select name, abbreviation, enabled from cryptocurrencies join enabled on crypto_id=id order by id')
    assets = cur.fetchall()
    return render_template('admin.html', assets=assets)


@app.route('/save-admin')
def save_admin():
    db = get_db()
    cur = db.execute('select name, enabled, enabled_id from cryptocurrencies join enabled on crypto_id=id order by id')
    for c in cur:
        db.execute('update enabled set enabled = {} where enabled_id = {}'.format(1 if request.args.get(c[0],) == 'true' else 0, c[2]))
    db.commit()
    return redirect(url_for('admin'))


@app.teardown_appcontext
def close_db_connection(err):
    """
    Closing database connection after teardown
    Args:
        err:
    """
    if 'app_db' in g:
        g.sqlite_db.close()


def connect_db():
    """
    Connects to application databse
    Returns:
        database connection
    """
    c = sqlite3.connect(app.config['DATABASE'])
    return c


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_cmd():
    """
    Initialize database Flask script command
    Returns:

    """
    init_db()


def get_db():
    """
    Opens new db connection for app context.
    Returns:
        database connection
    """
    if 'app_db' not in g:
        g.sqlite_db = connect_db()
    return g.sqlite_db


if __name__ == '__main__':
    app.run()
