"""policy blueprint"""
from flask import Blueprint, request, jsonify

policy = Blueprint('policy', __name__)


@policy.route('/addpolicy', methods=('GET', 'POST'))
def add_policy():
    if request.method == "POST":
        policy = request.json
        print(policy)
        return jsonify({"success": True, "policy": policy})
    else:
        return jsonify({"message": "should be POST request"})


@policy.route('/addpolicy/<int:policyid>', methods=('POST'))
def get_policy(policyid):
    """policy chat page"""
    return "True"


@policy.route('/deletepolicy/<int:policyid>', methods=('DELETE'))
def delete_policy(policyid):
    """policy chat page"""
    return "True"


@policy.route('/updatepolicy', methods=('POST'))
def update_policy(policyid):
    if request.method == "POST":
        policy = request.json
        print(policy)
        return jsonify({"success": True, "policy": policy})
    else:
        return jsonify({"message": "should be POST request"})
