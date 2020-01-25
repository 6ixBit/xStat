''' API Endpoints for general-service '''

from flask_restful import Resource, Api
from flask import Flask

app = Flask(__name__)
api = Api(app)

class Players(Resource):
    def get(self, leaguename):
        return {'Success' : 'You have reached the gene service which will consist of the general statistics of players, including their clubs, league etc',
                'data': leaguename}

api.add_resource(Players, '/api/stats/goals/<string:leaguename>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

