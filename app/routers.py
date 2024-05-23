from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import LoginForm, RegisterForm
from .models import User
from app import db


dp = Blueprint("main", __name__)


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
        flash(f"Login requested for user { form.username.data }")
        return redirect(url_for("main.index"))
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
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now registered user!")
        return redirect(url_for("main.index"))
    return render_template("register.html", title="Register", form = form)
