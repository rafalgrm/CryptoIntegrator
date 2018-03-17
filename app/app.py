import os
import sqlite3

from flask import Flask, g, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)

app.config.update({
    'DATABASE': os.path.join(app.root_path, 'database.sqlite'),
    'SECRET_KEY': 'dev',
    'USERNAME': 'admin',
    'PASSWORD': 'admin'
})


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


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
