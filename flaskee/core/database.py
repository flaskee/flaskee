"""
The Flaskee is an Open Source project for Microservices.
Develop By Nadeen Gamage | https://nadeengamage.com | nadeengamage@gmail.com
"""

import sys
import glob
from os.path import dirname, basename, isfile, join

from flask_sqlalchemy import SQLAlchemy

#: Flask-SQLAlchemy extension instance
db = SQLAlchemy()

class Database(object):
    
    # Load database models
    @staticmethod
    def initialize_db_models(self, module):

        module_path = module

        if module_path in sys.modules:
            return sys.modules[module_path]

        modules = glob.glob(join((dirname(__file__)[:-4]) + 'models', "*.py"))
        files = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

        return __import__(module_path, fromlist=files)