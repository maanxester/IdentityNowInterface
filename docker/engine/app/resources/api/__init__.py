from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from engine.app.resources.api.requests import *

