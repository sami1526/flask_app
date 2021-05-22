from flask import Flask
from covid_app.config import Config 
from covid_app.app.routes import routes



def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)
    app.register_blueprint(routes, url_prefix="/home")
    return app

