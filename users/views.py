from flask import Blueprint, request

users = Blueprint('users', __name__, template_folder='templates')

@users.route('/')
def hello():
    return 'Hello Worlds!'


@users.route('/user/<int:pk>')
def user_detail(pk):
    print(request)
    print(request.method)  # GET
    print(request.args)    # ImmutableMultiDict([('q', u'foo')])
    print(request.headers)
    return '<h1>Hello, user #{}!</h1>'.format(pk)


@users.route('/user/<int:pk>')
#@login_required
def user_detail(pk):
    return '<h1>Hello, user #{}!</h1>'.format(pk)
