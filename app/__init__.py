from flask import Flask
from config import config

DEFAULT_APP_NAME = 'transcode'

def create_app(config_name, app_name=None):
    if app_name == None:
        app_name = DEFAULT_APP_NAME

    app = Flask(app_name)
    app.config.from_object(config[config_name])

    from .transcode import transcode as transcode_blueprint
    app.register_blueprint(transcode_blueprint)

    return app
