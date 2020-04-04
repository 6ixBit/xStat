''' Responsible for the methods to filter and compute player data '''

# Third party imports
import pandas as pd
from flask import jsonify

# Local imports
from .players import get_player, search_player

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
        'season', 
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

    # Calculate per 90 columns and add to dataframe 
    data['goals_per90'] = data.apply(lambda x: calc_per_90(x['goals'], x['minutes_played']), axis=1)
    data['shots_per90'] = data.apply(lambda x: calc_per_90(x['total_shots'], x['minutes_played']), axis=1)
    data['shots_on_target_p90'] = data.apply(lambda x: calc_per_90(x['shots_on_target'], x['minutes_played']), axis=1)

    # Passes
    data['assists_per90'] = data.apply(lambda x: calc_per_90(x['assists'], x['minutes_played']), axis=1)
    data['accuratePasses_per90'] = data.apply(lambda x: calc_per_90(x['total_passes'], x['minutes_played']), axis=1)
    data['keyPasses_per90'] = data.apply(lambda x: calc_per_90(x['key_passes'], x['minutes_played']), axis=1)

    # # Dribbles
    data['dribbleSuccess_per90'] = data.apply(lambda x: calc_per_90(x['dribble_success'], x['minutes_played']), axis=1)

    # # Defensive attributes
    data['tacklesCompleted_per90'] = data.apply(lambda x: calc_per_90(x['completed_tackles'], x['minutes_played']), axis=1)
    data['blocks_per90'] = data.apply(lambda x: calc_per_90(x['blocks'], x['minutes_played']), axis=1)
    data['interceptions_per90'] = data.apply(lambda x: calc_per_90(x['interceptions'], x['minutes_played']), axis=1)
    data['foulsCommited_per90'] = data.apply(lambda x: calc_per_90(x['fouls_commited'], x['minutes_played']), axis=1)
    data['foulsDrawn_per90'] = data.apply(lambda x: calc_per_90(x['fouls_drawn'], x['minutes_played']), axis=1)
    
    data = data.head(1)

    # Export as dictionary object to allow for JSON parsing
    result = data.to_dict(orient='records')
    return result

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

