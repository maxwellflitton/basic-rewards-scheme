from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.views.user import user_views


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


def import_models(database) -> None:
    """
    Imports the models to create the tables in the database

    :return: None
    """
    from models.user import User
    from models.company import Company
    from models.reward import Reward
    from models.reward_instance import RewardInstance
    database.create_all()


@app.route("/")
def home():
    return "this is working"


app.register_blueprint(user_views, url_prefix="/users")


if __name__ == "__main__":
    import_models(database=db)
    # app_instance.import_models()
    app.run()
