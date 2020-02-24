# Third party imports
from flask import Flask, Blueprint

# Local imports 
from src.api.api import mod as mod_api

#Setup app instance 
app = Flask(__name__)

# Register blueprints
app.register_blueprint(mod_api)

# Testing circular dependency
from src.api.Errors import errors