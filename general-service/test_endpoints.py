import unittest
from api import app

class ApiTestCase(unittest.TestCase):
    '''Test cases for endpoints on /general service'''

    def test_api_goals_route(self):
        '''Endpoint should return a 400 on request as URL is invalid'''
        tester = app.test_client(self)
        res = tester.get('/api/stats/goals/Seria A', content_type='application/json')
        self.assertEqual(res.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()
