from flask import Blueprint

users = Blueprint(
    'users',
    __name__,
    template_folder='templates')

@users.route('/')
def hello():
    return 'Hello Worlds!'
