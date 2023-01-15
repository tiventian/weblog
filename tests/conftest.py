import pytest

from blog import create_app
from database.mysql import db


@pytest.fixture
def app():
    _config = {'TESTING': True, 'DEBUG': True,
               'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://root:Aa123123@localhost:3306/weblog_test?charset=utf8mb4'}
    app = create_app(_config)

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def dbclient(app, request):
    with app.app_context():
        db.create_all()

    def teardown():
        with app.app_context():
            db.drop_all()

    request.addfinalizer(teardown)

    return app
