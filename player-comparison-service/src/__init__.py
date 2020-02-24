''' Root file to hold app instance of application '''

# Thid party imports
from flask import Flask, Blueprint

# Setup application instance
app = Flask(__name__)

# Local imports
from src.api.routes import mod as mod_api
from src.api import errors

# Register blueprint(s)
app.register_blueprint(mod_api)
