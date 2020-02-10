''' Processing pipeline for data pulled from database '''
# Third party imports
import pandas as pd
from pprint import pprint

# Local application imports
from Models.players import get_players_frm_league

def filter_top_scorers(league):
    '''
     @desc Cleans and sorts the data passed to it and returns it in its required format
     @return Returns 
    '''
    # Pull players from database
    players = get_players_frm_league(f"{league}")
    df = pd.DataFrame(players)

    # Clean data and only include the following columns
    columns = ['player_name', 'team_name', 'position', 'competition', 'age', \
             'goals', 'minutes_played', 'match_starts', 'total_shots', 'shots_on_target']
    data = df[columns]

    # Set index to goals so that the list can be ordered
    sorted_data = data.sort_values(by='goals', ascending=False)

    #TODO: Fix JSON output before returning it
    json_plyrs = sorted_data.to_json(orient='index')
    return json_plyrs

# filter_top_scorers("Bundesliga")
