''' Model representation for players NoSQL-schema '''

# Third party imports
from pymongo import MongoClient
from pprint import pprint

# Local imports
from config import Config

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

    recevied_player = collection.find(
        {"player_name": player_name})

    if recevied_player is None:
        return []

    players = []
    for player in recevied_player:
        del player['_id']
        players.append(player)

    return players

pprint(get_player("J. Milner"))
