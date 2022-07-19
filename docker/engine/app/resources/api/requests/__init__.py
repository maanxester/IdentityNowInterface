from flask import jsonify, request, abort
from engine.app import app
from engine.app.resources.api import api
from functools import wraps


@api.route('/status')
def get_requests():
    return jsonify({"status": "ok"}), 200

