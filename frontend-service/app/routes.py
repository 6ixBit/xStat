from app import app
import requests

from dash import Dash
import dash_html_components as html
import dash_core_components as dcc

# App Routes
@app.route('/')
def index():
    res = requests.get("http://general-service/api/v1/stats/goals/Premier League")
    return res.json()


@app.route('/player-comparison')
def player_comparison():
    # TODO: Make request to /players service
    # TODO: Pass returned data to dash app
    # TODO: Render any additonal tags and return the page to the user 

    res = requests.get("http://player-comparison-service/api/players/Riyad Mahrez")
    return res.json()


# Sample style sheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

dash_app1 = Dash(
    __name__,
    server=app,
    routes_pathname_prefix='/charts/',
    external_stylesheets=external_stylesheets
)

# Setup layout for dash application
dash_app1.layout = html.Div(children=[
    html.H1(children='xStat'),

    html.Div(children='''
        A data visualization platform for football player statistics.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 
                'y': [4, 1, 2], 'type': 'bar', 'name': 'Kevin De Bruyne'},

                {'x': [1, 2, 3], 
                'y': [2, 4, 5], 'type': 'bar', 'name': 'Mesut Ozil'},
            ],
            'layout': {
                'title': 'Premier League Assists (2017, November)'
            }
        }
    )
])