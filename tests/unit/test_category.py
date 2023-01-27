from blog.models.category import Category


def test_new_category(dbclient):
    with dbclient.app_context():
        c = Category.create(name='Python', status='N')
        assert Category.select().count() == 1
        c = Category.create(name='test', status='D')
        assert Category.select().count() == 2


def test_update_category(dbclient):
    with dbclient.app_context():
        c = Category.create(name='python', status='N')
        assert Category.select().count() == 1
        c2 = Category.select().where(Category.name == 'python').first()
        q = (Category
             .update({Category.name: 'Python1', Category.status: 'D'})
             .where(Category.name == 'python'))
        q.execute()
        assert Category.select().count() == 1
        assert Category.get(Category.name == 'Python1').status == 'D'
