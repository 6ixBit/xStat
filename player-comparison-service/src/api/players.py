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

def get_player(player_name:str, season:str="2019-2020"):
    '''
    @desc Returns a document when a match for Player_name is found.
    @param player_name - Name of player to search.
    @param season - Season of player to search for
    @return [{}] - list of dict
    '''

    received_player = collection.find_one({"player_name": player_name})

    if received_player is None:
        return []

    # Remove Mongo Object ID from result
    del received_player['_id']
    return received_player

def search_player(first_name:str):
    '''
    @desc Searches for players in database with a similar first_name
    @param first_name - First name of player to search for
    @return [{}] list of dicts
    '''

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

    return {
        "results": matched_players.count(),
        "players": players
    }

