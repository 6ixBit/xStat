''' API Endpoints for general-service '''

# Third party imports 
from flask_restful import Resource, Api
from flask import Flask, Request, Blueprint
import json
from pprint import pprint

# Local imports
from src.api.pipeline import filter_top_scorers, filter_pass_accuracy, filter_dribbles_completed, filter_tackles_completed, filter_all_stats

# App instances and config
mod = Blueprint('api', __name__)
api = Api(mod, prefix='/api/v1')

class Goals(Resource):
    '''
    @desc Returns the highest goal scorers from a particular league in descending order
    @route GET /api/v1/stats/goals/:leaguename
    @param :leaguename - name of league the players to search
    '''
    def get(self, leaguename):     
        try:
            players = filter_top_scorers(leaguename) 
            return players, 200 
        except: 
            return {'Error' : "Failed to return requested data"}, 400

class Passing(Resource):
    '''
    @desc Returns players with the highest passing stats
    @route GET /api/v1/stats/passes/:leaguename
    @param :leaguename - name of league the players to search
    '''
    def get(self, leaguename):     
        try:
            players = filter_pass_accuracy(leaguename) 
            return players, 200 
        except: 
            return {'Error' : "Failed to return requested data"}, 400

class Dribbling(Resource):
    '''
    @desc Returns players with the highest dribbling stats
    @route GET /api/v1/stats/dribbles/:leaguename
    @param :leaguename - name of league the players to search
    '''
    def get(self, leaguename):     
        try:
            players = filter_dribbles_completed(leaguename) 
            return players,200 
        except: 
            return {'Error' : "Failed to return requested data"}, 400

class Tackling(Resource):
    '''
    @desc Returns players with the highest tackling stats
    @route GET /api/v1/stats/tackles/:leaguename
    @param leaguename - Name of league the players to search
    '''
    def get(self, leaguename):     
        try:
            players = filter_tackles_completed(leaguename) 
            return players,200 
        except: 
            return {'Error' : "Failed to return requested data"}, 400

class Players(Resource):
    '''
    @desc Returns all players with a combination of all calcluated stats
    @route GET /api/v1/stats/
    @return JSON {}
    '''
    def get(self):     
        try:
            players = filter_all_stats() 
            return players, 200 
        except: 
            return {'Error' : "Failed to return requested data"}, 400

class Leagues(Resource):
    '''
    @desc Returns a list of available leagues for players in the database
    @route GET /api/v1/stats/leagues
    @return JSON {}
    '''
    def get(self):
        current_leagues = [ 
            { "value": 'a', "text": 'Premier League' },
            { "value": 'b', "text": 'Serie A' },
            { "value": 'c', "text": 'La Liga' },
            { "value": 'd', "text": 'Ligue 1' },
            { "value": 'f', "text": 'Bundesliga'}
        ]

        return current_leagues, 200


# Routes for API
api.add_resource(Goals, '/stats/goals/<string:leaguename>')
api.add_resource(Passing, '/stats/passes/<string:leaguename>')
api.add_resource(Dribbling, '/stats/dribbles/<string:leaguename>')
api.add_resource(Tackling, '/stats/tackles/<string:leaguename>')
api.add_resource(Players, '/stats')
api.add_resource(Leagues, '/stats/leagues')
