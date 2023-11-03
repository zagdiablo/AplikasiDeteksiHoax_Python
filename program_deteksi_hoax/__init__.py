from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app.config["SECRET_KEY"] = "secret"
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
