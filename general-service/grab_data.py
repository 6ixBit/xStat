''' Pulls data from api-football.com, parses necessary fields and commits to database - MongoDB Database'''
from config import Config
import requests
import csv
import pandas as pd
from pprint import pprint

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

def get_players_id(team_id: int, season: str):
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
        "player_id" : player_stat[0]['player_id'],
        "player_name": player_stat[0]['player_name'],
        "first_name": player_stat[0]['firstname'],
        "last_name": player_stat[0]['lastname'],
        "shirt_number": player_stat[0]['number'],
        "position": player_stat[0]['position'],
        "age": player_stat[0]['age'],
        "team_name": player_stat[0]['team_name'],
        "rating": player_stat[0]['rating'],
        "nationality": player_stat[0]['nationality'],
        "height": player_stat[0]['height'],
        "weight": player_stat[0]['weight'],
        "competition": player_stat[0]['league'],
        "season": player_stat[0]['season'],
        "total_shots": player_stat[0]['shots']['total'],
        "shots_on_target": player_stat[0]['shots']['on'],
        "goals": player_stat[0]['goals']['total'],
        "assists": player_stat[0]['goals']['assists'],
        "total_passes": player_stat[0]['passes']['total'],
        "key_passes": player_stat[0]['passes']['key'],
        "pass_accuracy": player_stat[0]['passes']['accuracy'],
        "completed_tackles": player_stat[0]['tackles']['total'],
        "blocks": player_stat[0]['tackles']['blocks'],
        "interceptions": player_stat[0]['tackles']['interceptions'],
        "dribble_attempts": player_stat[0]['dribbles']['attempts'],
        "dribble_success": player_stat[0]['dribbles']['success'],
        "fouls_drawn": player_stat[0]['fouls']['drawn'],
        "fouls_commited": player_stat[0]['fouls']['committed'],
        "yellow_cards": player_stat[0]['cards']['yellow'],
        "red_cards": player_stat[0]['cards']['red'],
        "penalty_won": player_stat[0]['penalty']['won'],
        "penalty_commited": player_stat[0]['penalty']['commited'],
        "penalty_success": player_stat[0]['penalty']['success'],
        "penalty_missed": player_stat[0]['penalty']['missed'],
        "appearences": player_stat[0]['games']['appearences'],
        "minutes_played": player_stat[0]['games']['minutes_played'],
        "match_starts": player_stat[0]['games']['lineups'],
        "subbed_in": player_stat[0]['substitutes']['in'],
        "subbed_out": player_stat[0]['substitutes']['out'],
        "benched": player_stat[0]['substitutes']['bench'],
        "total_duels": player_stat[0]['duels']['total'],
        "duels_won": player_stat[0]['duels']['won']
    }

    field_names = [ col for col in player.keys() ]

    with open(filename, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()

        writer.writerow(player)

    return pd.read_csv('player_stats.csv').head()

    
  
if __name__ == '__main__':
    # todo: Call function to grab data from API
    # result = map(grab_teams, leagues.values()) -> RUN grab_teams function for every league
    # pprint(list(result))

    # team_ids = map(get_teams, leagues.values())
    # pprint(list(team_ids))

    my_player = get_player_stats(644)
    print(write_to_csv(my_player))

    

