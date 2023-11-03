from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect

from flask_login import LoginManager, login_user, logout_user, current_user, login_required

from forms import LoginForm
from models import users


app = Flask(__name__)

app.config["SECRET_KEY"] = "b9f1f7e80d2627b5bdf11skaaieop26f67a4c49858d3f4b39eeadd8f84d5c6bb92fb0a0753"

csrf = CSRFProtect(app)

# Creamos la instancia de LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# Acceder al usuario mediante ID / username
@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)


@app.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        print(current_user)
        return redirect(url_for("welcome"))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user = users.get(username)
        if user and user.password == password:
            login_user(user)
            # flash("Credenciales inválidas", "error")
            # return render_template("login.html", form=login_form)
            return redirect(url_for("welcome"))
    return render_template("login.html", form=login_form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route('/welcome')
@login_required
def welcome():
    suma = 3 + 2
    res = suma * 2
    return render_template('index.html', valor=res)


@app.route("/submit")
def submit():
    return "HOLA DESDE SUBMIT"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
