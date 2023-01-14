from flask import Blueprint, request, jsonify

accounts = Blueprint('accounts', __name__)


@accounts.route('/addaccount', methods=('GET', 'POST'))
def add_policy():
    if request.method == "POST":
        account = request.json
        print(account)
        return jsonify({"success": True, "account": account})
    else:
        return jsonify({"message": "should be POST request"})


@accounts.route('/getaccount/<int:accountid>', methods=('GET', 'POST'))
def get_account(accountid):
    """fetch account details"""
    return "True"
