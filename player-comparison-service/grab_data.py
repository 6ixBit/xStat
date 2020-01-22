''' Pulls data from api-football.com, parses necessary fields and commits to database - SQL Database '''
from .config import Config
import requests

url = ""

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': Config.RAPID_API_KEY
}




if __name__ == '__main__':
    # todo: Call function to grab data from API