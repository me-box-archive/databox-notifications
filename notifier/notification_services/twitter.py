import oauth2
import urllib
from notifier import secrets
from flask_restful import Resource, reqparse, inputs

parser = reqparse.RequestParser()
parser.add_argument('to', required=True, type=inputs.regex('^@?[a-z0-9_]{1,15}$'))
parser.add_argument('body', required=True)
class Twitter(Resource):
    def post(self):
        post_data = parser.parse_args()
        data = {"screen_name": post_data['to'], "text": post_data['body']}
        data = urllib.urlencode(data)
        twitter_url = 'https://api.twitter.com/1.1/direct_messages/new.json?%s' % (data)
        consumer = oauth2.Consumer(key=secrets.TWITTER_CONSUMER_KEY, secret=secrets.TWITTER_CONSUMER_SECRET)
        token =  oauth2.Token(key=secrets.TWITTER_ACCESS_TOKEN, secret=secrets.TWITTER_ACCESS_TOKEN_SECRET)
        client = oauth2.Client(consumer, token)
        resp, content = client.request(twitter_url, method="POST", body="", headers=None)
        return [content], resp
