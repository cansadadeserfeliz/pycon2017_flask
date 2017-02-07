from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object('conf.config')

    db.init_app(app)

    from users.views import users
    app.register_blueprint(users, url_prefix='/users')

    @app.context_processor
    def constants_processor():
        return {
            'say_hello': 'Hola',
        }

    return app



