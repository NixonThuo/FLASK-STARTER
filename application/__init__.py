"""Module providingFunction printing python version."""
from flask import Flask
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
csrf = CSRFProtect()


def something():
    "where the app starts to load"

    app.config.from_object("application.config.Config")

    app.logger.info(f'ENV is set to: {app.config["ENV"]}')

    with app.app_context():
        db.init_app(app)

    print(app.config)

    csrf.init_app(app)

    from application.login.login_controller import login
    from application.policy.policy_controller import policy
    from application.accounts.accounts_controller import accounts

    app.register_blueprint(login, url_prefix="/")
    app.register_blueprint(policy, url_prefix="/policy")
    app.register_blueprint(accounts, url_prefix="/accounts")

    return app
