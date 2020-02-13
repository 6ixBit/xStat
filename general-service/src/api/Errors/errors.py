''' Custom Error handling for server '''

#Third party imports
import json

# Local imports
from src import app

@app.errorhandler(404)
def resourse_not_found(error):
    return json.dumps({"message" : "Resourse not found", "ERROR": error}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return json.dumps({"message": "Internal server error", "ERROR": error}), 500