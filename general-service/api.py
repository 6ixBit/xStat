''' API Endpoints for general-service '''

from flask_restful import Resource, Api
from flask import Flask

app = Flask(__name__)
api = Api(app)

class Players(Resource):
    def get(self):
        return {'Success' : 'You have reached the player service'}

api.add_resource(Players, '/api/players')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

