from flask_restful import Resource

class Status(Resource):
    def get(self):
        return 'active', 200, {'Access-Control-Allow-Origin': '*'}