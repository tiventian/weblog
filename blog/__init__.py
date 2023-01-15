import os

from flask import Flask

from database.mysql import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if not test_config:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db.init_app(app)

    @app.route('/')
    def index():
        return 'Hello, World!'

    return app
