''' Responsible for the methods to filter and compute player data '''

# Third party imports
import pandas as pd
from pprint import pprint
from flask import jsonify

# Local imports
from Models.players import get_player

def filter_stats_for_player(player_name):
    '''
    @desc Sorts data for player passed as param and apply per90 columns
    @param player_name - Name of player to query for and filter stats for
    @return {} JSON 
    '''
    player = get_player(player_name)

    if player is []:
        return []

    df = pd.DataFrame(player)
    
    # Parse columns from database
    columns = [
        'player_name',
        'team_name', 
        'position',
        'competition', 
        'age', 
        'total_passes',
        'pass_accuracy', 
        'key_passes', 
        'goals',
        'assists', 
        'minutes_played', 
        'match_starts',
        'subbed_in',
        'subbed_out',
        'benched',
        'total_shots',
        'shots_on_target',
        'completed_tackles',
        'blocks',
        'interceptions',
        'yellow_cards',
        'red_cards',
        'dribble_attempts',
        'dribble_success',
        'fouls_drawn',
        'fouls_commited',
        'appearences',
        'penalty_won',
        'penalty_commited',
        'penalty_success',
        'penalty_missed'
    ]
    data = df[columns]

    return data #TODO: Investigate bug from Models/players.py

def calc_per_90(stat:int, minutes_played:int):
    '''
    @desc Returns per 90 value of stat passed to 2 decimal places
    @param stat - goals/assists,fouls etc. 
    @param minutes_played - Amount of mins played during this stat period
    @return int value to 2 decimal places
    '''
    if type(stat) != int or type(minutes_played) != int:
        return 0

    if stat < 1 or minutes_played < 1:
        return 0

    return round( (stat / minutes_played) * 90, 2)

pprint(filter_stats_for_player("J. Milner"))