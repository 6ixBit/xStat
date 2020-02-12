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
api = Api(app, catch_all_404s=True)

class Players(Resource):
    # @desc Returns the highest goal scorers from a particular league in descending order
    # @route GET /api/stats/goals/:leaguename
    # @param :leaguename - name of league the players to search
    def get(self, leaguename):     
        try:
            players = filter_top_scorers(leaguename) 
            return players,200 
        except: 
            return {'Error' : "Failed to return requested data"}, 400

# Routes for API
api.add_resource(Players, '/api/stats/goals/<string:leaguename>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

