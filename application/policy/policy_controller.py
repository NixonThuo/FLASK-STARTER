"""policy blueprint"""
from flask import Blueprint

policy = Blueprint('policy', __name__)


@policy.route('/', methods=('GET', 'POST'))
def policy_chat_page():
    """policy chat page"""
    return "True"
