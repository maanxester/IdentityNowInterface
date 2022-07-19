from flask import Flask
import uuid, os
from flasgger import Swagger

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())
Swagger(app, template_file='swagger.yaml')


from engine.app.resources import *


def create_app():
    from engine.app.resources.api import api
    app.register_blueprint(api)
    return app
