''' Pulls data from api-football.com, parses necessary fields and commits to database - MongoDB Database'''
# Local imports
from config import Config

# Third party imports
import requests
import csv
import pandas as pd
from pprint import pprint
import pymongo

# All 5 leagues and their respective ids from the API
leagues = {
    "Premier League" : 524,
    "La Liga" : 775,
    "Serie A" : 891,
    "Bundesliga" : 754,
    "Ligue 1" : 525
}

headers = {
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
    "x-rapidapi-key": Config.RAPID_API_KEY
}

def get_teams(league_id: int) -> list:
    """
    - Grab all teams from a specific league
    
    Arguments:
        league_id {int} -- ID of the league in the API to get.
    
    Returns:
        list -- Fetched teams as a list.
    """
    global headers
    url = f"https://api-football-v1.p.rapidapi.com/v2/teams/league/{league_id}"
    response = requests.get(url, headers=headers).json()

    # Parse teams from JSON response
    teams = [ value['teams'] for key,value in response.items() ]

    # Parse team_ids from each team within the league
    team_ids = [ element['team_id'] for index, element in enumerate(teams[0]) ]     
    return team_ids

def get_players_id(team_id: int, season="2019-2020") -> list:
    """
    - Get stats for all players of each team passed as team_id 
    
    Arguments:
        team_id {int} -- ID of team to get player ids for.
    
    Keyword Arguments:
        season {str} -- Season of player stats to get. (default: {"2019-2020"})
    
    Returns:
        list -- Fetched players ids as a list
    """    
    global headers
    url = f"https://api-football-v1.p.rapidapi.com/v2/players/squad/{team_id}/{season}"
    
    response = requests.get(url, headers=headers).json()

    # todo: parse player ids from response and return all in a list
    players = [ value['players'] for key, value in response.items() ]

    player_ids = [ element['player_id'] for index, element in enumerate(players[0]) ]
    return player_ids

def get_player_stats(player_id: int, league="Serie A") -> list:
    """
    - Get stats for each player and filter by params on link.
    
    Arguments:
        player_id {int} -- Player id of a specific player.
    
    Keyword Arguments:
        league {str} -- What league to filter stats by. (default: {"Serie A"})
    
    Returns:
        list -- List which contains a dictionary of the players stats.
    """    
    global headers
    url = f"https://api-football-v1.p.rapidapi.com/v2/players/player/{player_id}"
    
    response = requests.get(url, headers=headers).json()

    players = [ value['players'] for key, value in response.items() ]

    # Get stats for a particular competition based on league param passed       
    player_stats = [ element[index] for index,element in enumerate(players) if element[index]['league'] == league ]

    return player_stats

def write_to_db(player_stat):
    """
    - Accepts a player stat object in list format and inserts it into database
    
    Arguments:
        player_stat {object} -- Player object to submit
    """    
  
    my_client = pymongo.MongoClient(Config.MONGO_URL)

    my_db = my_client['xStat']
    my_collection = my_db['player_stats_general_service']

    my_player = {
        "player_id" : player_stat['player_id'],
        "player_name": player_stat['player_name'],
        "first_name": player_stat['firstname'],
        "last_name": player_stat['lastname'],
        "shirt_number": player_stat['number'],
        "position": player_stat['position'],
        "age": player_stat['age'],
        "team_name": player_stat['team_name'],
        "rating": player_stat['rating'],
        "nationality": player_stat['nationality'],
        "height": player_stat['height'],
        "weight": player_stat['weight'],
        "competition": player_stat['league'],
        "season": player_stat['season'],
        "captain": player_stat['captain'],
        "total_shots": player_stat['shots']['total'],
        "shots_on_target": player_stat['shots']['on'],
        "goals": player_stat['goals']['total'],
        "goals_conceded": player_stat['goals']['conceded'],
        "assists": player_stat['goals']['assists'],
        "total_passes": player_stat['passes']['total'],
        "key_passes": player_stat['passes']['key'],
        "pass_accuracy": player_stat['passes']['accuracy'],
        "completed_tackles": player_stat['tackles']['total'],
        "blocks": player_stat['tackles']['blocks'],
        "interceptions": player_stat['tackles']['interceptions'],
        "dribble_attempts": player_stat['dribbles']['attempts'],
        "dribble_success": player_stat['dribbles']['success'],
        "fouls_drawn": player_stat['fouls']['drawn'],
        "fouls_commited": player_stat['fouls']['committed'],
        "yellow_cards": player_stat['cards']['yellow'],
        "red_cards": player_stat['cards']['red'],
        "penalty_won": player_stat['penalty']['won'],
        "penalty_commited": player_stat['penalty']['commited'],
        "penalty_success": player_stat['penalty']['success'],
        "penalty_missed": player_stat['penalty']['missed'],
        "penalty_saved": player_stat['penalty']['saved'],
        "appearences": player_stat['games']['appearences'],
        "minutes_played": player_stat['games']['minutes_played'],
        "match_starts": player_stat['games']['lineups'],
        "subbed_in": player_stat['substitutes']['in'],
        "subbed_out": player_stat['substitutes']['out'],
        "benched": player_stat['substitutes']['bench'],
        "total_duels": player_stat['duels']['total'],
        "duels_won": player_stat['duels']['won']
    }

    player = my_collection.insert_one(my_player)
    print(player.inserted_id)

if __name__ == '__main__':
    team_ids = get_teams(leagues["Serie A"]) # PL, Bundesliga, La Liga, Ligue 1, Seri

    player_ids = list(map(get_players_id, team_ids))
    player_ids_pool = [ inner for outer in player_ids for inner in outer ] # Pool of player ids from a particular team.

    player_stats = list(map(get_player_stats, player_ids_pool))
    player_stats_pool = [ inner for outer in player_stats for inner in outer ] # Holds stats of every player of a particular team in JSON

    # Insert each players stat to database
    for player in player_stats_pool:
        write_to_db(player)





    



    

    

