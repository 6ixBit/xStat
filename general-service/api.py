''' API Endpoints for general-service '''

# Third party imports 
from flask_restful import Resource, Api
from flask import Flask, Request
import json
from pprint import pprint

# Local imports
from pipeline import filter_top_scorers

# App instances and config
app = Flask(__name__)
api = Api(app)

class Players(Resource):
    # @desc Returns the highest goal scorers from a particular league
    # @route GET /api/stats/goals/:leaguename
    # @param :leaguename - str
    def get(self, leaguename):
        ''' 
        GET League players based on league name
        '''       
        try:
            players = filter_top_scorers(leaguename) 
            return players,200 if players == [] else 404
        except: 
            return {'Error' : "Failed to return requested data"}, 400

# Routes for API
api.add_resource(Players, '/api/stats/goals/<string:leaguename>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)

