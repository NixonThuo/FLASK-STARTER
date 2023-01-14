"""login controller"""
from flask import Blueprint, render_template, request
from application.login.login_form import LoginForm

login = Blueprint('login', __name__)


@login.route('/', methods=('GET', 'POST'))
def login_page():
    """login controller"""
    form = LoginForm(request.form)
    if request.method == "POST":
        return render_template("dashboard/template.html")
    return render_template("login/index.html", form=form)
