"""policy blueprint"""
from flask import Blueprint, request, jsonify, render_template
from application.policy.policy_model import Policies
from application.accounts.accounts_model import Accounts
from application import db

policy = Blueprint('policy', __name__)


@policy.route('/addpolicy', methods=['GET', 'POST'])
def add_policy():
    accounts = Accounts.query.all()
    if request.method == "POST":
        accountid = request.form.get("accountid")
        policytype = request.form.get("policytype")
        policy = Policies(
            accountid=accountid,
            policytype=policytype
        )
        db.session.add(policy)
        db.session.commit()
        return jsonify({"success": True, "policyid": policy.policyid})
    else:
        return render_template("policy/index.html", accounts=accounts)


@policy.route('/listpolicies', methods=['GET'])
def listpolicies():
    policies = Policies.query.all()
    return render_template("policy/policy_list.html", policies=policies)


@policy.route('/updatepolicy', methods=['GET', 'POST'])
def update_policy():
    if request.method == "POST":
        accountid = request.form.get("accountid")
        policyid = request.form.get("policyid")
        policytype = request.form.get("policytype")
        policy = Policies.query.filter_by(
            policyid=policyid,
        ).first()
        policy.accountid = accountid
        policy.policyid = policyid
        policy.policytype = policytype
        db.session.commit()
        return jsonify({"success": True, "policyid": policy.policyid, "message": "policy updated"})
    else:
        return render_template("policy/index.html")


@policy.route('/getpolicy/<int:policyid>', methods=['GET'])
def get_policy(policyid):
    """policy chat page"""
    policy = Policies.query.filter_by(
        policyid=policyid
    ).first()
    selectedaccount = Accounts.query.filter_by(
        accountid=policy.accountid
    ).first()
    accounts = Accounts.query.all()
    if policy:
        return render_template("policy/policy_update.html", policy=policy,
                               selectedaccount=selectedaccount, accounts=accounts)
    else:
        return jsonify({"error": "policy not found"})


@policy.route('/deletepolicy/<int:policyid>', methods=['GET'])
def delete_policy(policyid):
    policy = Policies.query.filter_by(
        policyid=policyid
    ).first()
    db.session.delete(policy)
    return "Deleted"
