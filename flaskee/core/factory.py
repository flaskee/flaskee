"""
Flaskee is an Open Source project for Microservices.
Develop By Nadeen Gamage | https://nadeengamage.com | nadeengamage@gmail.com
"""

import os

from flask import Flask

from flaskee.core.database import db
from flaskee.core.helpers import register_blueprints

from flaskee.core.middleware import OverrideHTTPMethods


def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):

    app = Flask(package_name, instance_relative_config=True)

    app.config.from_object('flaskee.core.settings')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)

    db.init_app(app)

    register_blueprints(app, package_name, package_path)

    app.wsgi_app = OverrideHTTPMethods(app.wsgi_app)

    return app

