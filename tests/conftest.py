import pytest

from blog import create_app


@pytest.fixture
def app():
    _config = {'TESTING': True,
               'DEBUG': True,
               'DATABASE_URI': 'mysql+pymysql://root:Aa123123@localhost:3306/weblog_test?charset=utf8mb4',
               }

    app = create_app(_config)

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def dbclient(app):
    return app
