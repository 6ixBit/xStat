''' Pulls data from api-football.com, parses necessary fields and commits to database - MongoDB Database'''
from config import Config
import requests
import csv
import pandas as pd
from pprint import pprint
import pymongo

# All 5 leagues and their respective ids from the API
leagues = {
    "Premier League" : 524,
    "La Liga" : 775,
    "Seria A" : 891,
    "Bundesliga" : 754,
    "Ligue 1" : 525
}

headers = {
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
    "x-rapidapi-key": Config.RAPID_API_KEY
}

def get_teams(league_id: int) -> list:
    ''' Grab all teams from a specific league '''
    global headers
    url = f"https://api-football-v1.p.rapidapi.com/v2/teams/league/{league_id}"
    response = requests.get(url, headers=headers).json()

    # Parse teams from JSON response
    teams = [ value['teams'] for key,value in response.items() ]

    # Parse team_ids from each team within the league
    team_ids = [ element['team_id'] for index,element in enumerate(teams[0]) ]     
    return team_ids

def get_players_id(team_id, season="2019-2020"):
    ''' Get stats for all players of each team passed as a parameter OR get all player ids for a team and return it in a list
        @param (int) team_id: int
        @param (YYYY or YYYY-YYYY : 2019 or 2019-2020) season: str
    '''
    global headers
    url = f"https://api-football-v1.p.rapidapi.com/v2/players/squad/{team_id}/{season}"
    
    response = requests.get(url, headers=headers).json()

    # todo: parse player ids from response and return all in a list
    players = [ value['players'] for key, value in response.items() ]

    player_ids = [ element['player_id'] for index, element in enumerate(players[0]) ]
    return player_ids

def get_player_stats(player_id: int, league="Premier League"):
    ''' GET stats for each player and filter by params on link
        @param (644) player_id - Player id of a specific player
        @param ("Premier League") league - What league to filter stats by 
    '''
    global headers
    url = f"https://api-football-v1.p.rapidapi.com/v2/players/player/{player_id}"
    
    response = requests.get(url, headers=headers).json()

    players = [ value['players'] for key, value in response.items() ]

    # Get stats for a particular competition based on league param passed       
    player_stats = [ element[index] for index,element in enumerate(players) if element[index]['league'] == league ]

    return player_stats

def write_stats_to_csv(player_stat, filename="player_stats.csv"):
    # Map users passed as arg into dict
    player = {
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
        "total_shots": player_stat['shots']['total'],
        "shots_on_target": player_stat['shots']['on'],
        "goals": player_stat['goals']['total'],
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
        "appearences": player_stat['games']['appearences'],
        "minutes_played": player_stat['games']['minutes_played'],
        "match_starts": player_stat['games']['lineups'],
        "subbed_in": player_stat['substitutes']['in'],
        "subbed_out": player_stat['substitutes']['out'],
        "benched": player_stat['substitutes']['bench'],
        "total_duels": player_stat['duels']['total'],
        "duels_won": player_stat['duels']['won']
    }

    field_names = [ col for col in player.keys() ]

    with open(filename, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerow(player)

    #return pd.read_csv('player_stats.csv').head()

def write_to_db(player_stat):
    ''' Accepts a player stat object in list format and inserts it into database'''
    my_client = pymongo.MongoClient(Config.MONGO_URL)

    my_db = my_client['xStat']
    my_collection = my_db['player_stats_general_service']

    player = my_collection.insert_one(player_stat)
    print(player.inserted_id)

if __name__ == '__main__':
    #team_ids = get_teams(leagues['Premier League']) Premier League is done

    player_ids = list(map(get_players_id, team_ids))
    player_ids_pool = [ inner for outer in player_ids for inner in outer ] # Pool of player ids from a particular team.

    player_stats = list(map(get_player_stats, player_ids_pool))
    player_stats_pool = [ inner for outer in player_stats for inner in outer ] # Holds stats of every player of a particular team in JSON

    # Insert each players stat to database
    for player in player_stats_pool:
        write_to_db(player)





    



    

    

