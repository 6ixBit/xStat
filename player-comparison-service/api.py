''' API endpoints to be exposed for Player Comparison matrix '''

from flask_restful import Resource, Api
from flask import Flask

app = Flask(__name__)
api = Api(app)

class Players(Resource):
    # @desc Returns all stat info about a particular player
    # @route GET /api/players/:playername
    # @param :playername - str
    def get(self, playername):
        return {'Success' : 'You have reached the player comparison service, which will consist of the general statistics of players, including their clubs, league etc',
                'data': playername}

api.add_resource(Players, '/api/players/<string:playername>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)