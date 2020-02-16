''' API endpoints to be exposed for Player Comparison matrix '''

# Thid party imports
from flask_restful import Resource, Api
from flask import Flask, Blueprint

# Register blueprint
mod = Blueprint('api', __name__)
api = Api(mod, prefix='/api/v1')

class Players(Resource):
    ''' 
    @desc Returns all stat info about a particular player
    @route GET /api/players/:playername
    @param :playername - Name of player; Riyad Mahrez
    '''
    def get(self, playername):
        return {'Success' : 'You have reached the player comparison service, which will consist of the general statistics of players, including their clubs, league etc',
                'data': playername}


# Add endpoiints to API instance
api.add_resource(Players, '/players/<string:playername>')
