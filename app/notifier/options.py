from flask_restful import Resource
import json


class Options(Resource):
    def get(self):
        with open('opions.json') as fh:
            data = json.load(fh)
            return json.dumps(data), 200, {"Content-Type": "text/plain"}
