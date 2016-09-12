# Notification System
## Supported Services and overview

- Email
- SMS
- Twitter Direct Message
- Push Notification to (currently) Android and Chrome extension.
- Growl

The API is a HTTP API run by Python with the flask framework.

Post requests are made to `/notify/<service>`, with JSON in the body. All Services
require `to` and `body` parameters.

SMS messages can currently only be sent to UK numbers. Twilio does Support
international numbers but the validator assumes a UK number at present.

Push notifications and chrome notifications cannot currently be sent because there
is no way of transferring firebase registration tokens to this service to be able to
send notifications to devices. The source code for an Android app and the chrome
extension are not currently available in this repository.

## Installation

Accounts are required from Twilio, Twitter, Google (for Gmail and Firebase).

Developer applications are also required. The secrets.py.in file should be used
as a template for a secrets.py file to supply authentication credentials to
services.

The GMail API is an exception because it uses JSON files for authentication
and I have not included these in the repo for security reasons. I will add instructions
for generating the required files soon.

Twilio needs a UK phone number creating which **must** support SMS. In trial
mode, numbers that should receive messages must also be verified by Twilio.

Many of the accounts used here were created for Homework Router notifications. I
can supply the secrets.py file with the correct details for these accounts if
required.

Assuming accounts are configured correctly, docker build should configure everything.
The app currently listens on port 5000. This must be forwarded to a port on the host.
This will be adapted to use a shell script and environment variables at some point.
