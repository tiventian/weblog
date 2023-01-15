from blog.models.category import Category
from database.mysql import db


def test_new_category(dbclient):
    cate = Category('python')
    with dbclient.app_context():
        db.session.add(cate)
        db.session.commit()
