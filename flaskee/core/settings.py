"""
Flaskee is an Open Source project for Microservices.
Develop By Nadeen Gamage | https://nadeengamage.com | nadeengamage@gmail.com
"""

DEBUG = True
SECRET_KEY = 'super-secret-key'

SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_DATABASE_URI = 'mysql://root@127.0.0.1:3306/flaskee'

MAIL_DEFAULT_SENDER = ''
MAIL_SERVER = ''
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = 'username'
MAIL_PASSWORD = 'password'