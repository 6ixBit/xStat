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


def grab_teams(league_id):
    ''' Grab all teams from a specific league

        @param (int) league_id
        @return (int []) teams    
    '''
    global headers
    url = f"https://api-football-v1.p.rapidapi.com/v2/teams/league/{league_id}"
    response = requests.get(url, headers=headers).json()

    teams = [ value['teams'] for key,value in response.items() ]

    # Parse team_ids from each team within the league
    team_ids = [ element['team_id'] for index, element in enumerate(teams[0]) ]
       
    return team_ids
  
if __name__ == '__main__':
    # todo: Call function to grab data from API
    # result = map(grab_teams, leagues.values()) -> RUN grab_teams function for every league
    # pprint(list(result))

    league_id = leagues['Premier League']
    pprint(grab_teams(league_id))