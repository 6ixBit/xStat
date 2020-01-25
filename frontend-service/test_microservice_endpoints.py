import unittest
from app import app

class ApiTestCase(unittest.TestCase):
    '''Test cases for frontend service endpoints'''

    def test_index_route(self):
        '''Endpoint should return a 200 on request'''
        tester = app.test_client(self)
        res = tester.get('/', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    # def test_charts_route(self):
    #     '''Endpoint should return a 200 on request'''
    #     tester = app.test_client(self)
    #     res = tester.get('/charts', content_type='application/json')
    #     self.assertEqual(res.status_code, 200)

    def test_player_comparison_endpoint(self):
        '''Endpoint should return a 200 on request'''
        tester = app.test_client(self)
        res = tester.get('/player-comparison', content_type='application/json')
        self.assertEqual(res.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
