from flask import Flask, render_template
from flask_login import LoginManager

from src.views.user import user_views
from config import GlobalParams
from models.user import User
from models.reward import Reward
from models.company import Company
from models.reward_instance import RewardInstance

from src.database.engine import engine, Base


User.__table__.create(bind=engine)
Company.__table__.create(bind=engine)
Reward.__table__.create(bind=engine)
RewardInstance.__table__.create(bind=engine)


params = GlobalParams()
app = Flask(__name__, template_folder='src/templates')
app.config["SQLALCHEMY_DATABASE_URI"] = params.get("DB_URL")
app.config['SECRET_KEY'] = 'mysecretkey'
Base.metadata.create_all(engine)
# login = LoginManager(app)



@app.route("/")
def home():
    return render_template('index.html', title="home_page")


app.register_blueprint(user_views, url_prefix="/users")


if __name__ == "__main__":
    app.run()
