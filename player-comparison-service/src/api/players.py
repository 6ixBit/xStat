''' Model representation for players NoSQL-schema '''

# Third party imports
from pymongo import MongoClient
from pprint import pprint

# Local imports
import sys, os
sys.path.append('..') 
from .config import Config

# DB config
client = MongoClient(Config.MONGO_URL)
db = client['xStat']
collection = db['player_comparison_service']

def get_player(player_name:str):
    """
    - Returns a document when a match for player_name is found.
    
    Arguments:
        player_name {str} -- Name of player to search.
        
    Returns:
        [type] -- player object 
    """    
    # Search for player in database
    received_player = collection.find_one({"player_name": player_name.strip()})

    # End function if player is not found
    if received_player is None:
        return []

    # Remove Mongo Object ID from result
    del received_player['_id']

    print(received_player) # We are fetching player.
    return received_player

def search_player(first_name:str):
    '''
    @desc Searches for players in database with a similar first_name
    @param first_name - First name of player to search for
    @return [{}] list of dicts
    '''
    if first_name == '' or None:
        return []

    matched_players = collection.find(
        {"first_name": {"$regex" : first_name}}
    )

    if matched_players is None:
        return []

    # Append matched results to list and return it
    players = []
    for player in matched_players:
        del player['_id']
        del player['Team']
        del player['League']

        players.append(player)
    
    limitedPlayers = players[:10]

    return {
        "results": matched_players.count(),
        "players": limitedPlayers
    }

