from blog import create_app
from flask_migrate import Migrate
from database.mysql import db

from blog.models.category import Category

migrate = Migrate()
app = create_app()
migrate.init_app(app, db)
if __name__ == '__main__':
    app.run()
