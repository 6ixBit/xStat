from app import app
import requests

@app.route('/')
def index():
    res = requests.get("http://general-service/api/players")
    return res.json()


@app.route('/player-comparison')
def player_comparison():
    # todo: Make request to /players service
    # todo: Pass returned data to dash app
    # todo: Render any additonal tags and return the page to the user 

    return {'Result' : 'You have hit the player comparison endpoint'}