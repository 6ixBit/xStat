''' Pulls data from api-football.com, parses necessary fields and commits to database - SQL Database '''

# Third paty imports
import requests
from pprint import pprint
import pymongo

# Local imports
from config import Config

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
    player_stat = [ element[index] for index,element in enumerate(players) if element[index]['league'] == league ]

    # my_player = {
    #     "player_id" : player_stat[0]['player_id'],
    #     "player_name": player_stat[0]['player_name'],
    #     "first_name": player_stat[0]['firstname'],
    #     "last_name": player_stat[0]['lastname'],
    #     "shirt_number": player_stat[0]['number'],
    #     "position": player_stat[0]['position'],
    #     "age": player_stat[0]['age'],
    #     "team_name": player_stat[0]['team_name'],
    #     "rating": player_stat[0]['rating'],
    #     "nationality": player_stat[0]['nationality'],
    #     "height": player_stat[0]['height'],
    #     "weight": player_stat[0]['weight'],
    #     "competition": player_stat[0]['league'],
    #     "team_id": player_stat[0]['team_id'],
    #     "season": player_stat[0]['season'],
    #     "captain": player_stat[0]['captain'],
    #     "total_shots": player_stat[0]['shots']['total'],
    #     "shots_on_target": player_stat[0]['shots']['on'],
    #     "goals": player_stat[0]['goals']['total'],
    #     "goals_conceded": player_stat[0]['goals']['conceded'],
    #     "assists": player_stat[0]['goals']['assists'],
    #     "total_passes": player_stat[0]['passes']['total'],
    #     "key_passes": player_stat[0]['passes']['key'],
    #     "pass_accuracy": player_stat[0]['passes']['accuracy'],
    #     "completed_tackles": player_stat[0]['tackles']['total'],
    #     "blocks": player_stat[0]['tackles']['blocks'],
    #     "interceptions": player_stat[0]['tackles']['interceptions'],
    #     "dribble_attempts": player_stat[0]['dribbles']['attempts'],
    #     "dribble_success": player_stat[0]['dribbles']['success'],
    #     "fouls_drawn": player_stat[0]['fouls']['drawn'],
    #     "fouls_commited": player_stat[0]['fouls']['committed'],
    #     "yellow_cards": player_stat[0]['cards']['yellow'],
    #     "red_cards": player_stat[0]['cards']['red'],
    #     "penalty_won": player_stat[0]['penalty']['won'],
    #     "penalty_commited": player_stat[0]['penalty']['commited'],
    #     "penalty_success": player_stat[0]['penalty']['success'],
    #     "penalty_missed": player_stat[0]['penalty']['missed'],
    #     "penalty_saved": player_stat[0]['penalty']['saved'],
    #     "appearences": player_stat[0]['games']['appearences'],
    #     "minutes_played": player_stat[0]['games']['minutes_played'],
    #     "match_starts": player_stat[0]['games']['lineups'],
    #     "subbed_in": player_stat[0]['substitutes']['in'],
    #     "subbed_out": player_stat[0]['substitutes']['out'],
    #     "benched": player_stat[0]['substitutes']['bench'],
    #     "total_duels": player_stat[0]['duels']['total'],
    #     "duels_won": player_stat[0]['duels']['won']
    # }
    return player_stat

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

    parsed_stats = {
        "league_id" : league_stats[0]['league_id'],
        "competition_name" :  league_stats[0]['name'],
        "competition_type" : league_stats[0]['type'],
        "competition_country" : league_stats[0]['country'],
        "competition_country_code" : league_stats[0]['country_code'],
        "competition_logo_url" : league_stats[0]['logo'],
        "competition_flag_url" : league_stats[0]['flag']
    }
    return parsed_stats

def get_player_team_stats(team_id):
    '''
    @desc Returns team stats of a particular player
    @param team_id - ID of team to grab stats for 
    '''
    global headers

    url = f"https://api-football-v1.p.rapidapi.com/v2/teams/team/{team_id}"
    response = requests.get(url, headers=headers).json()['api']['teams']

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
    return team_stats
    
def submit_to_db(player_stat):
    '''
    @desc Adds player object to Mongo database
    @param player_stat - Player statistics in dictionary format
    '''
    my_client = pymongo.MongoClient(Config.MONGO_URL)

    my_db = my_client['xStat']
    my_collection = my_db['player_comparison_service']

    player = my_collection.insert_one(player_stat)
    print(player.inserted_id)

if __name__ == '__main__':
    team_ids = get_teams(leagues['Premier League'])

    player_ids = list(map(get_players_id, team_ids))
    # Player ids returns a nested list, player ids pools removed that extra layer
    player_ids_pool = [ inner for outer in player_ids for inner in outer ] 

    player_stats_pool = []
    for index, player_id in enumerate(player_ids_pool):
        # Get player stats for player - FUNC THROWING ERROR
        my_player = get_player_stats(player_id)[0]
    
        # Fetch league and team stats using players team id
        league_stats = get_player_league_stats(my_player['team_id'])
        team_stats = get_player_team_stats(my_player['team_id'])

        # Add league stats from API call to my_player object
        my_player['League'] = league_stats
        my_player['Team'] = team_stats

        # Append player to pool of players
        player_stats_pool.append(my_player)
        
    # Insert each players stat to database
    for player in player_stats_pool:
        submit_to_db(player)

