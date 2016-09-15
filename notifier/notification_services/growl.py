import gntp.notifier
from flask_restful import Resource, reqparse, inputs

re = '(?:^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))$'
parser = reqparse.RequestParser()
parser.add_argument('to', required=True)
parser.add_argument('body', required=True)

class Growl(Resource):
    def post(self):
        post_data = parser.parse_args()
        growl = gntp.notifier.GrowlNotifier(
            applicationName="databox-notify",
            notifications=["Databox Notification"],
            defaultNotifications=["Databox Notification"],
            hostname=post_data['to']
        )

        growl.register()
        res = growl.notify(
            noteType="Databox Notification",
            title="Databox Notification",
            description=post_data['body'],
            sticky=False,
            priority=1
        )
        if res == True:
            return ['ok', 'message sent successfully'], 200
        return ['error', 'message not sent'], 500