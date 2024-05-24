from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm, RegisterForm
from .models import User
from app import db, login_manager


dp = Blueprint("main", __name__)

# Load user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@dp.route("/")
@dp.route("/index")
def index():
    return render_template("index.html")


@dp.route("/about")
def about():
    return render_template("about.html")


@dp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for('main.profile'))
        else:
            flash(f"Login unseccessful. Please check username and password", "danger")

    return render_template("login.html", title='Sign In', form = form)


@dp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
            email = form.email.data
        )
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now registered user!")
        return redirect(url_for("main.index"))
    return render_template("register.html", title="Register", form = form)


@dp.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('main.index'))


@dp.route('/profile')
@login_required
def profile():
    return f"Hello, {current_user.username}!"