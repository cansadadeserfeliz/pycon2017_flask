from flask import Blueprint, request
from flask import render_template

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/')
def hello():
    return 'Hello Worlds!'


@users.route('/user/<int:pk>')
def user_detail(pk):
    return render_template('users/detail.html', user_id=pk)
