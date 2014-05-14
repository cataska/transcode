from flask import Flask
from config import config

DEFAULT_APP_NAME = 'transcode'

def create_app(config_name):
    app = Flask(DEFAULT_APP_NAME)
    app.config.from_object(config[config_name])

    from .transcode import transcode as transcode_blueprint
    app.register_blueprint(transcode_blueprint)
    
    return app

