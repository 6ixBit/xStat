from app import app
import requests
from dash import Dash
import dash_html_components as html

# App Routes
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


# Dash application
dash_app1 = Dash(
    __name__,
    server=app,
    routes_pathname_prefix='/charts/'
)

# Setup layout for dash application
dash_app1.layout = html.Div("My 1st Dash app")