''' API endpoints to be exposed for Player Comparison matrix '''

# Thid party imports
from flask import Blueprint, json

# Local  imports
from src import app
from .players import search_player

# Register blueprint
mod = Blueprint('api', __name__)

@app.route('/api/v1/players/<string:playername>', methods=['GET'])
def get_players(playername):
    #TODO: Check playername to ensure its of type string before being called
    return json.dumps({'Success' : 'You have reached the player comparison service', 'data': playername}), 200


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
    


    

            
        

        

    

