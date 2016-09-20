import gntp.notifier
from gntp.errors import NetworkError
from flask_restful import Resource, reqparse, inputs
import errno
from socket import error as socket_error

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

        try:
            growl.register()
            res = growl.notify(
                noteType="Databox Notification",
                title="Databox Notification",
                description=post_data['body'],
                sticky=False,
                priority=1
                )
            if res is True:
                return 'ok', 200
            return ['error', 'something went wrong when sending the message'], 500
        except NetworkError as err:
            return ['error', 'Message could not be sent because the recipient refused to accept it. Check that the IP address is correct and that Growl is running'], 400
