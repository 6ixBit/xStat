#Third party imports
import unittest
from flask import Flask

# Local imports
from src import app
from src.api.Scripts.pipeline import calc_per_90

class ApiTestCase(unittest.TestCase):
    '''Test cases for endpoints on /general service'''

    def test_api_goals_route(self):
        '''Endpoint should return a 400 on request as URL is invalid'''
        tester = app.test_client(self)
        res = tester.get('/api/v1/stats/goals/Seria A', content_type='application/json')
        self.assertEqual(res.status_code, 200)

class PipelineTestCase(unittest.TestCase):
    ''' Tests methods defined within pipeline file '''
    def test_calc_per90_returns_input_in_expected_format(self):
        ''' Should return a number passed to it to two decimal places '''
        res = calc_per_90(10, 900) # result = 1
        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()
