from __future__ import print_function
import httplib2

from googleapiclient import discovery, errors
from oauth2client import client, file, tools

import base64
from email.mime.text import MIMEText
import os
import sys
from flask_restful import Resource, reqparse

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = ['https://www.googleapis.com/auth/gmail.send']
CLIENT_SECRET_FILE = 'notifier/client_secret.json'
APPLICATION_NAME = 'Docker'

parser = reqparse.RequestParser()
parser.add_argument('to', required=True)
parser.add_argument('body', required=True)

class Gmail(Resource):
    def get_credentials(self):
        code_dir = os.path.abspath('/code/notifier')
        credential_path = os.path.join(code_dir,
                                    'docker-email.json')
        print(credential_path, file=sys.stderr)
        store = file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path, file=sys.stderr)
        return credentials

    def create_message(self, sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_string())}
    
    def post(self):
        post_data = parser.parse_args()
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http)
        message = self.create_message("homework.router@gmail.com", post_data['to'], "Databox Notification", post_data['body'])
        try:
            message = service.users().messages().send(userId="me", body=message).execute()
        except errors.HttpError, error:
            return ["Error %s" % error], 400
        return [message], 200
