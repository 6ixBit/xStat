import unittest
from src import app

class ApiTestCase(unittest.TestCase):
    '''Test cases for endpoints on /player-comparison service'''

    def test_api_players_route(self):
        '''Endpoint should return a 200 on request'''
        tester = app.test_client(self)
        res = tester.get('/api/players/riyad mahrez', content_type='application/json')
        self.assertEqual(res.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()
