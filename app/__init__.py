__author__ = 'LMai'
from flask import Flask


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    from .searchdb import searchdb
    app.register_blueprint(searchdb)

    return app

