"""
Flaskee is an Open Source project for Microservices.
Develop By Nadeen Gamage | https://nadeengamage.com | nadeengamage@gmail.com
"""

from functools import wraps
from datetime import datetime

from flask import jsonify

from flaskee.core import factory
from flaskee.core.helpers import JSONEncoder


def create_app(settings_override=None, register_security_blueprint=False):
	app = factory.create_app(__name__, __path__, settings_override,
								register_security_blueprint=register_security_blueprint)

	# Set the default JSON encoder
	app.json_encoder = JSONEncoder

	# Register custom error handlers
	app.errorhandler(404)(on_not_found_error)
	app.errorhandler(405)(on_method_not_allowed_error)
	app.errorhandler(Exception)(on_internal_server_error)

	return app


def route(bp, *args, **kwargs):
    kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            sc = 200
            rv = f(*args, **kwargs)
            if isinstance(rv, tuple):
                sc = rv[1]
                rv = rv[0]
            return jsonify(dict(data=rv)), sc
        return f

    return decorator

def error_formatter(message, error):
	return dict(message=message, error=error, timestamp=datetime.now())

def on_not_found_error(e):
    return jsonify(error_formatter(str(e), 'Not Found')), 404

def on_method_not_allowed_error(e):
	return jsonify(error_formatter(message=str(e), error='Method Not Allowed')), 405

def on_internal_server_error(e):
	return jsonify(error_formatter(message=str(e), error='Internal Server Error')), 500