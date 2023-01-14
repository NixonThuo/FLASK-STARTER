from flask import Blueprint, request, jsonify, render_template
from application.accounts.accounts_model import Accounts

accounts = Blueprint('accounts', __name__)


@accounts.route('/addaccount', methods=['GET', 'POST'])
def add_account():
    if request.method == "POST":
        account = request.json
        print(account)
        return jsonify({"success": True, "account": account})
    else:
        return render_template("accounts/index.html")


@accounts.route('/getaccount/<int:accountid>', methods=['GET', 'POST'])
def get_account(accountid):
    """fetch account details"""
    acc = Accounts.query.filter_by(
        accountid=accountid
    ).first()
    return jsonify({"account": acc})
