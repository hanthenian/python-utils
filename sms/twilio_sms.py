"""
Author: Han Nguyen
Email: hannguyendev@gmail.com
twilio_sms.py -- A Python script to send SMS messages via Twilio API
Created on: December 15, 2022
"""

import os
import argparse
from twilio.rest import Client


class TwilioSMS:
    def __init__(self):
        self.twilio_acct_sid = os.environ['TWILIO_ACCT_SID']
        self.twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.twilio_client = Client(self.twilio_acct_sid, self.twilio_auth_token)

    
    def send_sms(self, from_num, to_num, message):
        """
        send_sms -- Send SMS through Twilio SMS Client
        Note: The number to send has to be a Twilio-hosted number
        
        @params:
            1. from_num (str) -- Number to send from
            2. to_num (str) -- Number to send to
            3. message (str) -- Message to send
        
        @return:
            message.sid

        Documentation: https://www.twilio.com/docs/sms/quickstart/python
        """
        message = self.twilio_client.messages.create(
            body = message,
            from_ = from_num,
            to = to_num
        )
        return message.sid


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(
        prog = 'Twilio SMS',
        description = 'Send message via Twilio SMS Client'
    )
    parser.add_argument('-fn', '--from_number', help="[Required] Phone number to send message from")
    parser.add_argument('-tn', '--to_number', help="[Required] Phone number to send message to")
    parser.add_argument('-m', '--message', help="[Required] Text message to send")
    args = parser.parse_args()
    
    # Send message via Twilio
    handler = TwilioSMS()
    message_sid = handler.send_sms(args['from_number'], args['to_number'], args['message'])


if __name__ == "__main__":
    main()
