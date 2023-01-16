from blog.models.category import Category


def test_new_category(dbclient):
    with dbclient.app_context():
        c = Category.create(name='Python', status='N')
        assert Category.select().count() == 1
        c = Category.create(name='test', status='D')
        assert Category.select().count() == 2
