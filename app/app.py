import os
import sqlite3

from flask import Flask, g, render_template
from flask_bootstrap import Bootstrap

from twitter.streamer import TwitterStreamer
from twitter.twitter_api_client import TwitterAPIClient
from twitter.twitter_filter import TwitterFilter

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
    # TODO temporary to show tweets on main panel
    api = TwitterAPIClient(app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'],
                           app.config['ACCESS_TOKEN_KEY'], app.config['ACCESS_TOKEN_SECRET'])
    filter = TwitterFilter(['bitcoin']).get_filter()
    streamer = TwitterStreamer(api, filter, limit=8)
    result = []
    for text in streamer:
        if 'text' in text:
            result.append(text['text'])
            print(text['text'])
    return render_template('index.html', messages=result)


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
