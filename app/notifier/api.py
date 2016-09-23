from flask import request, abort, Flask
from flask_restful import Resource, Api
from endpoints.twitter import Twitter
from endpoints.sms import Sms
from endpoints.push import Push
from endpoints.growl import Growl
from endpoints.gmail import Gmail
from endpoints.status import Status
from endpoints.options import Options
import os
import db
from pymacaroons import Macaroon, Verifier

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
api = Api(app)

api.add_resource(Gmail, "/notify/email")
api.add_resource(Growl, "/notify/growl")
api.add_resource(Push, "/notify/push")
api.add_resource(Sms, "/notify/sms")
api.add_resource(Twitter, "/notify/twitter")
api.add_resource(Status, "/status")
api.add_resource(Options, "/options")
