#Third party imports
import unittest
from flask import Flask

# Local imports
import sys
sys.path.append('.')
from src import app

from src.api.Scripts.pipeline import calc_per_90

class GoalsRouteTestCase(unittest.TestCase):
    ''' Test cases for endpoints on /api/v1/stats/goals/ '''

    def test_goals_route_with_SerieA(self):
        ''' Endpoint should return a 200 on request for Serie A '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/goals/Serie A', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_goals_route_with_PL(self):
        ''' Endpoint should return 200 on request for Premier League '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/goals/Premier League')
        self.assertEqual(res.status_code, 200)

    def test_goals_route_with_Bundesliga(self):
        ''' Endpoint should return 200 on request for Bundesliga '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/goals/Bundesliga')
        self.assertEqual(res.status_code, 200)

    def test_goals_route_with_LaLiga(self):
        ''' Endpoint should return 200 on request for La Liga '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/goals/La Liga')
        self.assertEqual(res.status_code, 200)

    def test_goals_route_with_Ligue1(self):
        ''' Endpoint should return 200 on request for Ligue 1'''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/goals/Ligue 1')
        self.assertEqual(res.status_code, 200)

    def test_route_with_invalid_param(self):
        ''' Endpoint should return 400 with wrong param '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/goals/Test')
        self.assertEqual(res.status_code, 400)

class PassingRouteTestCase(unittest.TestCase):
    ''' Test cases for endpoints on /api/v1/stats/passes/ '''
    def test_passing_route_with_SerieA(self):
        ''' Endpoint should return a 200 on request '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/passes/Serie A', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_passing_route_with_PL(self):
        ''' Endpoint should return 200 on request for Premier League '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/passes/Premier League')
        self.assertEqual(res.status_code, 200)

    def test_passing_route_with_Bundesliga(self):
        ''' Endpoint should return 200 on request for Bundesliga '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/passes/Bundesliga')
        self.assertEqual(res.status_code, 200)

    def test_passing_route_with_LaLiga(self):
        ''' Endpoint should return 200 on request for La Liga '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/passes/La Liga')
        self.assertEqual(res.status_code, 200)

    def test_passing_route_with_Ligue1(self):
        ''' Endpoint should return 200 on request for Ligue 1'''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/passes/Ligue 1')
        self.assertEqual(res.status_code, 200)

    def test_route_with_invalid_param(self):
        ''' Endpoint should return 400 with wrong param '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/passes/Test')
        self.assertEqual(res.status_code, 400)

class DribblingRouteTestCase(unittest.TestCase):
    ''' Test cases for /api/v1/dribbles/ '''
    def test_dribbling_route_with_SerieA(self):
        ''' Endpoint should return a 200 on request for Serie A '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/dribbles/Serie A', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_dribbling_route_with_PL(self):
        ''' Endpoint should return 200 on request for Premier League '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/dribbles/Premier League')
        self.assertEqual(res.status_code, 200)

    def test_dribbling_route_with_Bundesliga(self):
        ''' Endpoint should return 200 on request for Bundesliga '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/dribbles/Bundesliga')
        self.assertEqual(res.status_code, 200)

    def test_dribbling_route_with_LaLiga(self):
        ''' Endpoint should return 200 on request for La Liga '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/dribbles/La Liga')
        self.assertEqual(res.status_code, 200)

    def test_dribbling_route_with_Ligue1(self):
        ''' Endpoint should return 200 on request for Ligue 1'''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/dribbles/Ligue 1')
        self.assertEqual(res.status_code, 200)

    def test_route_with_invalid_param(self):
        ''' Endpoint should return 400 with wrong param '''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/dribbles/Test')
        self.assertEqual(res.status_code, 400)

class CalcPer90TestCase(unittest.TestCase):
    ''' Tests methods defined within pipeline file '''
    def test_calc_per90_returns_input_in_expected_format(self):
        ''' Should return a number passed to it to two decimal places '''
        res = calc_per_90(10, 900) # result = 1
        self.assertEqual(res, 1)

    def test_calc_per90_with_invalid_input(self):
        ''' Should return 0 if either param is 0 '''
        res = calc_per_90(0, 10)
        self.assertEqual(res, 0)

    def test_calc_per_90_with_invalid_data_type(self):
        ''' Should return 0 if anything but an int is passed'''
        res = calc_per_90("test", 1000)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
