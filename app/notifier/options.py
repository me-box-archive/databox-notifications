from flask_restful import Resource
import json
import os


class Options(Resource):
    def get(self):
        filename = os.path.join(os.path.dirname(__file__), 'options.json')
        with open(filename) as fh:
            data = json.load(fh)
            return json.dumps(data), 200, {"Content-Type": "text/plain"}
