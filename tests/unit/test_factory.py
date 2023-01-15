from blog import create_app


def test_config():
    assert not create_app().testing
    _test_conf = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://root:Aa123123@localhost:3306/weblog_test?charset=utf8mb4',
    }
    assert create_app(_test_conf).testing


def test_index(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'
