# Third party imports
from flask import Flask, Blueprint
from flask_cors import CORS

# Local imports 
from src.api.Myapi import mod as mod_api

#Setup app instance 
app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(mod_api)

