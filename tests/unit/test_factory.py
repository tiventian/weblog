from blog import create_app


def test_config():
    assert not create_app().testing
    _cnf = {'TESTING': True,
            'DATABASE_URL': 'mysql+pool://root:Aa123123@localhost:3306/weblog_test?max_connections=20&stale_timeout=300'}
    assert create_app(_cnf).testing


def test_index(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'
