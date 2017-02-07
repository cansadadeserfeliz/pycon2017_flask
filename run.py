from flask import Flask

def create_app():
    app = Flask(__name__,
        static_url_path='/static')
    app.config.from_object('conf.config')
    return app
