import urllib2
from flask_restful import Resource, reqparse
from notifier import secrets
import json

parser = reqparse.RequestParser()
parser.add_argument('to', required=True)
parser.add_argument('body', required=True)

class Push(Resource):
    def post(self):
        post_data = parser.parse_args()
        firebase_url = 'https://fcm.googleapis.com/fcm/send'
        to = post_data['to']
        body = post_data['body']
        data = {
            "to": to,
            "notification": {
                "title": "Docker Notification",
                "body": body,
                "icon": None
            }
        }

        req = urllib2.Request(firebase_url, data=json.dumps(data), headers={"Authorization": "key=%s" % (secrets.FIREBASE_SERVER_KEY), "Content-Type": "application/json"})
        response = urllib2.urlopen(req)
        return [response.read()], response.getcode()
