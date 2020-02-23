from flask import Blueprint, render_template, flash
from flask_login import current_user, login_user, logout_user, login_required
from src.forms import LoginForm, RegistrationForm
from models import model_factory

user_views = Blueprint('user_views', __name__, template_folder='templates')


@user_views.route("/")
def user():
    return "basic user view"


@user_views.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title="login_page", form=form)


@user_views.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_model = model_factory(model="user")
        user_instance = user_model(username=form.username.data, email=form.email.data, password=form.password.data)
        user_instance.save_instance()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template("register.html", title="register_page", form=form)

