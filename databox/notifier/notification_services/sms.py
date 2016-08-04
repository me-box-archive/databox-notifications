import urllib2
import urllib
from notifier import secrets
from flask_restful import Resource, reqparse
from twilio.rest import TwilioRestClient

parser = reqparse.RequestParser()
parser.add_argument('to', required=True)
parser.add_argument('body', required=True)
class Sms(Resource):
    def post(self):
        post_data = parser.parse_args()
        data = {"numberToDial": post_data['to'], "message": post_data['body']}
        data = urllib.urlencode(data)
        theUrl = "https://api.tropo.com/1.0/sessions?action=create&token=%s&%s" % (secrets.SMS_TOKEN, data)
        response = urllib2.urlopen(theUrl, data=data)
        return [response.read()], response.getcode()
