from flask import Blueprint

user_views = Blueprint('user_views', __name__)


@user_views.route("/")
def user():
    return "basic user view"
