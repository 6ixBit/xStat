# Local  imports
from src import app

# Third party imports
from flask import make_response, json
import logging

@app.errorhandler(404)
def resource_not_found(error):
    return json.dumps({"Error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    print(error)
    return json.dumps({"Error": "The server was unable to process your request"}), 500
