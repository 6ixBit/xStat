''' Responsible for the methods to filter and compute player data '''

# Third party imports
import pandas as pd
from pprint import pprint
from flask import jsonify

# Local imports
from Models.players import get_player

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

