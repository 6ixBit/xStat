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

def grab_teams(url, league_id):
    ''' Grab all teams from a specific league'''
    global headers
    connect = requests.get(url, headers=headers).json()

    teams = [ value['teams'] for key,value in connect.items() ]
    return teams
    # todo: Add name of teams and their assigned ids to a dictionary 

if __name__ == '__main__':
    # todo: Call function to grab data from API
    league_id = leagues['Premier League']
    url = f"https://api-football-v1.p.rapidapi.com/v2/teams/league/{league_id}"

    pprint(grab_teams(url, league_id))