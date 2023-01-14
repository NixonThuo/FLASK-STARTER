"""Module providingFunction printing python version."""
from flask import Flask
from application.login.login_controller import login
from application.policy.policy_controller import policy
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()
csrf = CSRFProtect()


def something():
    "where the app starts to load"

    if app.config["ENV"] == "production":
        app.config.from_object("application.config.ProductionConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("application.config.TestingConfig")
    else:
        app.config.from_object("application.config.DevelopmentConfig")

    with app.app_context():
        db.init_app(app)

    print(app.config)

    csrf.init_app(app)

    app.register_blueprint(login, url_prefix="/")
    app.register_blueprint(policy, url_prefix="/policy")
    return app
