''' Processing pipeline for data pulled from database '''
# Third party imports
import pandas as pd
from pprint import pprint

# Local application imports
from Models.players import get_players_frm_league

def filter_top_scorers(league: str):
    '''
    Most goals - Hitman ⚔️
     @desc Cleans and sorts the data passed to it and returns it in its required format
     @return Returns 
    '''
    # Pull players from database
    players = get_players_frm_league(f"{league}")
    df = pd.DataFrame(players)

    # Clean data and only include the following columns
    columns = ['player_name', 'team_name', 'competition', 'age', \
             'goals', 'minutes_played', 'match_starts', 'total_shots', 'shots_on_target']
    data = df[columns]

    # Sort rows by goals so that the dataframe can be ordered
    sorted_data = data.sort_values(by='goals', ascending=False)

    # Calculate per 90 columns and add to dataframe 
    sorted_data['goals_per90'] = sorted_data.apply(lambda x: calc_per_90(x['goals'], x['minutes_played']), axis=1)
    sorted_data['shots_per90'] = sorted_data.apply(lambda x: calc_per_90(x['total_shots'], x['minutes_played']), axis=1)
    sorted_data['shots_on_target_p90'] = sorted_data.apply(lambda x: calc_per_90(x['shots_on_target'], x['minutes_played']), axis=1)

    #TODO: Fix JSON output before returning it
    #json_plyrs = sorted_data.to_json(orient='index')
    return sorted_data.head(10)

def filter_pass_accuracy(league: str):
    '''
    Perfectionist 🎯
    @desc Cleans and sorts the data by those with the highest pass accuracy
    '''
      # Pull players from database
    players = get_players_frm_league(f"{league}")
    df = pd.DataFrame(players)

     # Clean data and only include the following columns
    columns = ['player_name', 'team_name', 'competition', 'age', \
             'total_passes', 'pass_accuracy', 'key_passes', 'assists', 'minutes_played', 'match_starts']
    data = df[columns]

     # Sort rows by pass accuracy so that the dataframe can be ordered
    sorted_data = data.sort_values(by='pass_accuracy', ascending=False)

     # Calculate per 90 columns and add to dataframe 
    sorted_data['assists_per90'] = sorted_data.apply(lambda x: calc_per_90(x['assists'], x['minutes_played']), axis=1)
    sorted_data['accuratePasses_per90'] = sorted_data.apply(lambda x: calc_per_90(x['total_passes'], x['minutes_played']), axis=1)
    sorted_data['keyPasses_per90'] = sorted_data.apply(lambda x: calc_per_90(x['key_passes'], x['minutes_played']), axis=1)

    finalised_data = sorted_data.sort_values(by='accuratePasses_per90', ascending=False)

    return finalised_data.head(15)



def filter_key_passes(league: str):
    '''
    Talisman ⚙️
    @desc Cleans and sorts the data by those with the most key passes
    '''
    pass

def filter_dribbles_completed(league: str):
    '''
    The magician 🎩
    @desc Cleans and sorts the data by those with the most dribbles completed 
    '''
    pass

def filter_tackles_completed():
    '''
    King of tackles 👑
    @desc Cleans and sorts the data by those with the most tackles completed
    '''
    pass

def filter_assists():
    '''
    @desc Returns stats for players based on assists
    '''

def calc_per_90(stat, minutes_played):
    '''
    @desc Returns the per 90 value of a stat passed
    '''
    return (stat / minutes_played) * 90 


print(filter_pass_accuracy("Premier League"))