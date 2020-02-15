from flask import Blueprint, render_template
from flask_login import current_user, login_user, logout_user, login_required
from src.forms import LoginForm

user_views = Blueprint('user_views', __name__, template_folder='templates')


@user_views.route("/")
def user():
    return "basic user view"

@user_views.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title="Log In Page")
