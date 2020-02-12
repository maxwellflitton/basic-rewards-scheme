from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from singleton import Singleton
from views.user import user_views


class AppEngine(metaclass=Singleton):
    """
    This is a class for managing the Flask app and attributes for that app.

    Attributes:
        app (Flask): flask app object
        db (SQLAlchemy):
    """
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
        self.db = SQLAlchemy(self.app)

    def import_models(self) -> None:
        """
        Imports the models to create the tables in the database

        :return: None
        """
        from models.user import User
        from models.company import Company
        from models.reward import Reward
        from models.reward_instance import RewardInstance
        self.db.create_all()


app_instance = AppEngine()  # => firing app engine


@app_instance.app.route("/")
def home():

    return "this is working"


app_instance.app.register_blueprint(user_views, url_prefix="/users")


if __name__ == "__main__":
    app_instance.import_models()
    app_instance.app.run()
