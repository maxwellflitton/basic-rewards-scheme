from flask import Blueprint, render_template
from flask_login import current_user, login_user, logout_user, login_required
from src.forms import LoginForm, RegistrationForm
from src.models.user import User

user_views = Blueprint('user_views', __name__, template_folder='templates')


@user_views.route("/")
def user():
    return "basic user view"

@user_views.route("/login", methods=['GET', 'POST'])
def login():
    # form = LoginForm()
    return render_template('login.html', title="login_page")

@user_views.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template("register.html", title="register_page", form=form)

