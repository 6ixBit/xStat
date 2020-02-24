# Third party imports 
import unittest

# Local imports
from src import app
from src.api.grab_data \
import get_teams, get_players_id, get_player_stats, \
get_player_league_stats, get_player_team_stats

class ApiTestCase(unittest.TestCase):
    '''Test cases for endpoints on /player-comparison service'''

    def test_api_players_route(self):
        ''' Endpoint should return a 200 on request '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/players/riyad mahrez', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_api_players_route_with_no_player_name(self):
        ''' Endpoint should return a 404 as route doesn't exist '''
        tester = app.test_client(self)
        res = tester.get('/api/v2/players', content_type='application/json')
        self.assertEqual(res.status_code, 404)

    def test_api_players_route_with_invalid_route(self):
        ''' Endpoint should return an error as route accepts a string not an int '''
        tester = app.test_client(self)
        res = tester.get(f'/api/v1/40405', content_type='application/json')
        self.assertEqual(res.status_code, 404)

class GrabDataTestCase(unittest.TestCase):
    ''' Test cases for functions within grab_data script'''
    def test_get_teams_returns_correct_values(self):
        ''' Test whether or not get_teams returns a list '''
        expected = {"Premier League" : 524}

        res = get_teams(expected['Premier League'])
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], int)
        self.assertEqual(len(res), 20) # 20 teams should be returned

    def test_get_players_id_returns_correct_values(self):
        ''' Test whether get_players_id() returns a list of players ids as ints '''
        teamID = 50

        res = get_players_id(teamID, "2019-2020")
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], int)

    def test_get_player_stats_returns_correct_values(self):
        ''' Test get_player_stats() returns player stats '''
        playerID = 654

        res = get_player_stats(playerID, "Premier League")
        self.assertIsInstance(res, list)

    def test_get_player_league_stats(self):
        ''' Test get_player_league_stats() returns correct values '''
        teamID = 50
        competition = "Premier League"

        res = get_player_league_stats(teamID, competition)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res['league_id'], int)
        self.assertEqual(res['competition_name'], competition)

if __name__ == '__main__':
    unittest.main()
