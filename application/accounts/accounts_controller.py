from flask import Blueprint, request, jsonify, render_template
from application.accounts.accounts_model import Accounts
from application import db

accounts = Blueprint('accounts', __name__)


@accounts.route('/addaccount', methods=['GET', 'POST'])
def add_account():
    if request.method == "POST":
        name = request.form.get("name")
        address = request.form.get("address")
        email = request.form.get("email")
        phone = request.form.get("phone")
        status = request.form.get("status")
        account = Accounts(
            name=name,
            address=address,
            email=email,
            phone=phone,
            status=status
        )
        db.session.add(account)
        db.session.commit()
        return jsonify({"success": True, "accountid": account.accountid})
    else:
        return render_template("accounts/index.html")


@accounts.route('/listaccounts', methods=['GET'])
def listaccounts():
    accounts = Accounts.query.all()
    return render_template("accounts/accounts_list.html", accounts=accounts)


@accounts.route('/updateaccount', methods=['GET', 'POST'])
def update_account():
    if request.method == "POST":
        accountid = request.form.get("accountid")
        name = request.form.get("name")
        address = request.form.get("address")
        email = request.form.get("email")
        phone = request.form.get("phone")
        status = request.form.get("status")
        account = Accounts.query.filter_by(
            accountid=accountid
        ).first()
        account.name = name
        account.address = address
        account.email = email
        account.phone = phone
        account.status = status
        db.session.commit()
        return jsonify({"success": True, "accountid": account.accountid, "message": "account updated"})
    else:
        return render_template("accounts/index.html")


@accounts.route('/getaccount/<int:accountid>', methods=['GET'])
def get_account(accountid):
    """fetch account details"""
    account = Accounts.query.filter_by(
        accountid=accountid
    ).first()
    if account:
        return render_template("accounts/account_update.html", account=account)
    return jsonify({"error": "account not found"})


@accounts.route('/deleteaccount/<int:accountid>', methods=['GET'])
def delete_account(accountid):
    account = Accounts.query.filter_by(
        accountid=accountid
    ).first()
    db.session.delete(account)
    return "Deleted"
