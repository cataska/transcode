from flask import Blueprint

transcode = Blueprint('transcode', __name__)

from . import routes
