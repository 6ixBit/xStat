''' Model representation for player database interactions'''

# Third party imports
from pymongo import MongoClient
from pprint import pprint

# Database config
client = MongoClient('mongodb+srv://hamza:Sierra123@zeus-uu6gn.mongodb.net/test?retryWrites=true&w=majority')
db = client['xStat']
collection = db['player_stats_general_service']

def get_players_frm_league(league:str, cur_season="2019-2020"):
    ''' 
    @desc Returns all info about a player from a specific league, filtered by a particular season.
    @return [{}] list of dicts
    '''
    received_players = collection.find(
        {'$and' : [
            {"competition" : f"{league}"},
            {"season": f"{cur_season}"},
            {"goals": {'$nin': ['null', 0]},},
        ]})

    # Append results to list and return it
    players = []
    for player in received_players:
        del player['_id']
        players.append(player)

    return players

def get_all_players(season="2019-2020"):
    '''
    @desc Returns all players from database
    @return [{}] list of dicts
    '''
    received_players = collection.find({})

    players = []
    for player in received_players:
        del player['_id']
        players.append(player)

    return players