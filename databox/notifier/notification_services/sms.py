import urllib2
import urllib
from notifier import secrets
from flask_restful import Resource, reqparse
from twilio.rest import TwilioRestClient

parser = reqparse.RequestParser()
parser.add_argument('to', required=True)
parser.add_argument('body', required=True)
client = TwilioRestClient(secrets.TWILIO_SID, secrets.TWILIO_TOKEN)
class Sms(Resource):
    def post(self):
        post_data = parser.parse_args()
        message = client.messages.create(to=post_data['to'], from_=secrets.TWILIO_NUMBER, body=post_data['body'])
        return message.status
