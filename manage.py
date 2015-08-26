__author__ = 'LMai'
import os
from app import create_app
from flask import g
from mssqlwrapper import DB

config_file = r'C:\Users\Lmai\PycharmProjects\dblookup\config.py'
app = create_app(config_file)


@app.before_request
def before_request():
    pass
    #g.db = DB.from_connection_string(app.config['CONNECTION_STRING'])


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    print('del db')
    if db is not None:
        del db

if __name__ == '__main__':
    app.run(debug=True)
