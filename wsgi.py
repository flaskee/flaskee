"""
Flaskee is an Open Source project for Microservices.
Develop By Nadeen Gamage | https://nadeengamage.com | nadeengamage@gmail.com
"""

from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flaskee import api

app = api.create_app()

application = DispatcherMiddleware(app, {
    '/api': app
})

if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)