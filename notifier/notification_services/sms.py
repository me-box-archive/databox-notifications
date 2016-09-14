from urllib import quote
from notifier import secrets
from flask_restful import Resource, reqparse
from twilio.rest import TwilioRestClient
from twilio.rest.lookups import TwilioLookupsClient
from twilio import TwilioRestException

parser = reqparse.RequestParser()
parser.add_argument('to', required=True)
parser.add_argument('body', required=True)
parser.add_argument('country_code')
client = TwilioRestClient(secrets.TWILIO_SID, secrets.TWILIO_TOKEN)
lookup_client = TwilioLookupsClient(secrets.TWILIO_SID, secrets.TWILIO_TOKEN)

class Sms(Resource):
    def post(self):
        post_data = parser.parse_args()
        encoded_number = quote(post_data['to'])
        try:
            number_object = lookup_client.phone_numbers.get(encoded_number, country_code="GB")  
            message = client.messages.create(to=number_object.phone_number, from_=secrets.TWILIO_NUMBER, body=post_data['body'])
            return "OK", 200
        except TwilioRestException as e:
            if e.status == 404:
                return "Phone number is invalid", 400
            return e.msg, e.status
