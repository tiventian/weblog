import pytest

from blog import create_app
from blog.models.category import Category
from database.mysql import pool_mysql


@pytest.fixture
def app():
    _cf = {'TESTING': True, 'DEBUG': True,
           'DATABASE_URL': 'mysql+pool://root:Aa123123@localhost:3306/weblog_test?max_connections=20&stale_timeout=300'}

    app = create_app(_cf)

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
        pool_mysql.database.create_tables([Category])

    def teardown():
        with app.app_context():
            pool_mysql.database.drop_tables([Category])

    request.addfinalizer(teardown)
    return app
