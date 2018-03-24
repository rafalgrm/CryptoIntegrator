import json
import os
import sqlite3
from urllib import request

import requests
from flask import Flask, g, render_template, jsonify, url_for
from flask_bootstrap import Bootstrap

from twitter.get_tweets import get_tweets


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
