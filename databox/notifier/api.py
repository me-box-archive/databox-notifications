from flask import request, abort
from flask_restful import Resource, Api
from notification_services.twitter import Twitter
from notification_services.sms import Sms
from notification_services.push import Push
from notification_services.growl import Growl
from notification_services.gmail import Gmail
from notifier import app

api = Api(app)

@app.before_request
def only_json():
    if not request.is_json:
        abort(400)

api.add_resource(Gmail, "/notify/email")
api.add_resource(Growl, "/notify/growl")
api.add_resource(Push, "/notify/push")
api.add_resource(Sms, "/notify/sms")
api.add_resource(Twitter, "/notify/twitter")
