from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, logout_user, current_user, login_user, login_required
from forms import SignupForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.urls import url_parse

import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SECRET_KEY"] = "7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

login_manager = LoginManager(app)
login_manager.login_view = "login"

db = SQLAlchemy(app)

from models import User


@app.route("/")
def index():
    return render_template("index.html")

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("protected"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get("next", None)
            if not next_page or url_parse(next_page).netloc != "":
                next_page = url_for("protected")
            return redirect(next_page)
    return render_template("login.html", form=form)


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    error = None
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User.get_by_email(email)
        if user is not None:
            error = f'El email {email} ya está siendo utilizado por otro usuario'
        else:
            user = User(name=name, email=email)
            user.set_password(password)
            user.save()  # Guarda en BDD
            login_user(user)
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template("signup.html", form=form, error=error)


@app.route("/protected", methods=["GET"])
@login_required
def protected():
    return render_template("protected.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
