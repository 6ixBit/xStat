# -*- coding: utf-8 -*-
''' Processing pipeline for data pulled from database '''

# Third party imports
import pandas as pd
from pprint import pprint
from flask import jsonify

# Local application imports
from src.api.players import get_players_frm_league, get_all_players

def filter_top_scorers(league: str, numbOfResults=30):
    '''
     Most goals - Hitman ⚔️
     @desc Cleans and sorts the data passed to it and returns it in its required format.
     @param league - League to filter results by.
     @param numbOfResults - Number of results to return.
     @return [{}] - list of dict objects for each row
    '''
    # Pull players from database
    players = get_players_frm_league(f"{league}")
    df = pd.DataFrame(players)

    # Clean data and only include the following columns
    columns = ['player_name', 'team_name', 'competition', 'age', \
                'goals', 'minutes_played', 'match_starts', 'total_shots', 'shots_on_target', 'season']
    data = df[columns]

    # Sort rows by goals so that the dataframe can be ordered
    sorted_data = data.sort_values(by='goals', ascending=False)

    # Calculate per 90 columns and add to dataframe 
    sorted_data['goals_per90'] = sorted_data.apply(lambda x: calc_per_90(x['goals'], x['minutes_played']), axis=1)
    sorted_data['shots_per90'] = sorted_data.apply(lambda x: calc_per_90(x['total_shots'], x['minutes_played']), axis=1)
    sorted_data['shots_on_target_p90'] = sorted_data.apply(lambda x: calc_per_90(x['shots_on_target'], x['minutes_played']), axis=1)

    # Limit results returned
    sorted_data = sorted_data.head(numbOfResults)

    # Export as dictionary object to allow for JSON parsing
    result = sorted_data.to_dict(orient='records')

    return result

def filter_pass_accuracy(league: str, numbOfResults=30):
    '''
    Perfectionist 🎯 & key_passes = Talisman ⚙️
    @desc Cleans and sorts the data by those with the highest pass accuracy.
    @param league - League to filter results by.
    @param numbOfResults - Number of results to return.
    @return [{}] - list of dict objects for each row
    '''
      # Pull players from database
    players = get_players_frm_league(f"{league}")
    df = pd.DataFrame(players)

     # Clean data and only include the following columns
    columns = ['player_name', 'team_name', 'competition', 'age', \
             'total_passes', 'pass_accuracy', 'key_passes', 'assists', 'minutes_played', 'match_starts', 'season']
    data = df[columns]

     # Sort rows by pass accuracy so that the dataframe can be ordered
    sorted_data = data.sort_values(by='pass_accuracy', ascending=False)

     # Calculate per 90 columns and add to dataframe 
    sorted_data['assists_per90'] = sorted_data.apply(lambda x: calc_per_90(x['assists'], x['minutes_played']), axis=1)
    sorted_data['accuratePasses_per90'] = sorted_data.apply(lambda x: calc_per_90(x['total_passes'], x['minutes_played']), axis=1)
    sorted_data['keyPasses_per90'] = sorted_data.apply(lambda x: calc_per_90(x['key_passes'], x['minutes_played']), axis=1)

     # Limit results returned
    sorted_data = sorted_data.head(numbOfResults)

    finalised_data = sorted_data.sort_values(by='accuratePasses_per90', ascending=False)

    # Export as dictionary object to allow for JSON parsing
    result = finalised_data.to_dict(orient='records')
    return result

def filter_dribbles_completed(league: str, numbOfResults=30):
    '''
    The magician 🎩
    @desc Cleans and sorts the data by those with the most dribbles completed.
    @param league - League to filter and compute results by.
    @param numbOfResults - Number of results to return.
    @return [{}] - list of dict objects for each row.
    '''
      # Pull players from database
    players = get_players_frm_league(f"{league}")
    df = pd.DataFrame(players)

     # Clean data and only include the following columns
    columns = ['player_name', 'team_name', 'competition', 'age', \
             'dribble_attempts', 'dribble_success', 'minutes_played', 'match_starts', 'season']
    data = df[columns]

    # Sort rows by pass accuracy so that the dataframe can be ordered
    sorted_data = data.sort_values(by='dribble_success', ascending=False)

    # Calculate per 90 columns and add to dataframe 
    sorted_data['dribbleSuccess_per90'] = sorted_data.apply(lambda x: calc_per_90(x['dribble_success'], x['minutes_played']), axis=1)

     # Limit results returned
    sorted_data = sorted_data.head(numbOfResults)

    # Export as dictionary object to allow for JSON parsing
    result = sorted_data.to_dict(orient='records')
    return result

def filter_tackles_completed(league: str, numbOfResults=30):
    '''
    King of tackles 👑
    @desc Cleans and sorts the data by those with the most tackles completed
    @param league - Name of league to filter data for.
    @param numbOfResults - Number of results to return.
    @return [{}] - list of dict objects for each row
    '''
      # Pull players from database
    players = get_players_frm_league(f"{league}")
    df = pd.DataFrame(players)

     # Clean data and only include the following columns
    columns = ['player_name', 'team_name', 'competition', 'age', \
             'completed_tackles', 'blocks', 'interceptions', 'fouls_commited', 'yellow_cards', 'red_cards', 'minutes_played', 'season']
    data = df[columns]

    # Calculate per 90 columns and add to dataframe 
    data['tacklesCompleted_per90'] = data.apply(lambda x: calc_per_90(x['completed_tackles'], x['minutes_played']), axis=1)
    data['blocks_per90'] = data.apply(lambda x: calc_per_90(x['blocks'], x['minutes_played']), axis=1)
    data['interceptions_per90'] = data.apply(lambda x: calc_per_90(x['interceptions'], x['minutes_played']), axis=1)
    data['foulsCommited_per90'] = data.apply(lambda x: calc_per_90(x['fouls_commited'], x['minutes_played']), axis=1)

    # Sort rows by pass accuracy so that the dataframe can be ordered
    finalised_data = data.sort_values(by='tacklesCompleted_per90', ascending=False)

    # Limit results returned
    finalised_data = data.head(numbOfResults)

    # Export as dictionary object to allow for JSON parsing
    result = finalised_data.to_dict(orient='records')
    return result

def filter_all_stats(numbOfResults=25):
    '''
    @desc Will bind all stats for every player and have a p90 column.
    @numfOfResults - Number of resuls to return
    @return [{}] - list of dict objects for each row
    '''
    # Pull players from database
    players = get_all_players()
    df = pd.DataFrame(players)

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

    # Limit results returned
    data = data.head(numbOfResults)
    
    # Export as dictionary object to allow for JSON parsing
    result = data.to_dict(orient='records')
    return result

def calc_per_90(stat, minutes_played):
    '''
    @desc Returns the per 90 value of a stat passed to 2 decimal places
    @param stat - Statistic to calculate a per 90 result of.
    @param minutes_played - Amount of minutes played during te period of that stat.
    @return int value to 2 decimal places.
    '''
    if type(stat) != int or type(minutes_played) != int:
        return 0

    # To avoid potentisl redundant values
    if stat < 1 or minutes_played < 1:
        return 0

    return round((stat / minutes_played) * 90, 2)

