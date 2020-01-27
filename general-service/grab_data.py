''' Pulls data from api-football.com, parses necessary fields and commits to database - MongoDB Database'''
from config import Config
import requests
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
    
  
if __name__ == '__main__':
    # todo: Call function to grab data from API
    # result = map(grab_teams, leagues.values()) -> RUN grab_teams function for every league
    # pprint(list(result))

    league_id = leagues['Premier League']
    #pprint(get_teams(league_id))
    #pprint(get_players_id(50, '2019-2020'))
    pprint(get_player_stats(644))

