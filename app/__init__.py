from flask import Flask

DEFAULT_APP_NAME = 'transcode'

app = Flask(DEFAULT_APP_NAME)

from app import application
