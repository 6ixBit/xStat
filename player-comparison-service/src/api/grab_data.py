''' Pulls data from api-football.com, parses necessary fields and commits to database - SQL Database '''
# Third paty imports
from config import Config
import requests
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
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': Config.RAPID_API_KEY
}

def get_teams(league_id:int) -> list:
    ''' 
    Grab all teams from a specific league 
    @param (int) league_id: int
    '''
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

def get_player_stats(player_id: int, league="Serie A"):
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

def get_player_league_stats(team_id:int, competition:str = "Premier League"):
    '''
    @desc Returns league stats for a specific player
    @param team_id - ID of team to fetch league stats for
    @param competition - Name of competition to parse results by
    '''
    global headers
    url = f"https://api-football-v1.p.rapidapi.com/v2/leagues/team/{team_id}"

    response = requests.get(url, headers=headers).json()['api']['leagues']

    # A team can have multiple competitions, parse result and return competition param passed
    league_stats = [league for league in response if league['name'] == competition]

    return league_stats

def get_player_team_stats(team_id):
    '''
    @desc Returns team stats of a particular player
    @param team_id - ID of team to grab stats for 
    '''
    global headers

    url = f"https://api-football-v1.p.rapidapi.com/v2/teams/team/{team_id}"
    response = requests.get(url, headers=headers).json()['data']['api']['teams'][0]

    # Clean data and return necessary fields
    team_stats = {
        'team_id': response[0]['team_id'],
        'team_name': response[0]['name'],
        'logo_url': response[0]['logo'],
        'country': response[0]['country'],
        'year_founded': response[0]['founded'],
        'stadia_name': response[0]['venue_name'],
        'stadia_capacity': response[0]['venue_capacity'],
        'stadia_city': response[0]['venue_city']
    }
    #TODO: Return only one response object rather than multiple that response currently does now
    return team_stats
    
def submit_to_db(player_stat):
    '''
    @desc Adds player object to Mongo database
    @param player_stat - Player statistics in dictionary format
    '''
    my_client = pymongo.MongoClient(Config.MONGO_URL)

    my_db = my_client['xStat']
    my_collection = my_db['player_comparison_service']


if __name__ == '__main__':
    pprint(get_player_league_stats(50))