import os
from flask import Flask

app = None
def create_app():
    app = Flask(__name__)
    app.app_context().push()
    app.debug = True
    app.secret_key = "flaskapp"
    return app

app= create_app()

from app.controllers import *

if __name__ == "__main__":
    app.run(host = "0.0.0.0")