''' API endpoints to be exposed for Player Comparison matrix '''

# Thid party imports
from flask import Blueprint, jsonify

# Local  imports
from src import app
from .players import search_player
from .pipeline import filter_stats_for_player

# Register blueprint
mod = Blueprint('api', __name__)

@app.route('/api/v1/player/<string:playername>', methods=['GET'])
def get_players(playername):
    '''
    @desc Computes the stats of the player passed to query string playername
    @return Returns the computed statistics of a player
    '''
    try:
        return jsonify(filter_stats_for_player(playername)), 200
    except:
        return {"error": "Could not return player requested"}, 400


@app.route('/api/v1/players/search/<string:name>', methods=['GET'])
def search_names(name):
    '''
    @desc Returns players that match the name passed
    @return {} - List of matched player names 
    '''
    try:
        return search_player(name), 200
    except:
        return {"error": "Failed to return searched player"}, 400
    


    

            
        

        

    

