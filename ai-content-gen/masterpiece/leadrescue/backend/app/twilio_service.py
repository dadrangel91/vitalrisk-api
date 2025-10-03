import os
from typing import Optional

# Thin wrapper so Twilio can be swapped/mocked in tests
class TwilioClient:
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.from_number = os.getenv("TWILIO_PHONE_NUMBER")

    def send_sms(self, to: str, body: str) -> dict:
        # In the MVP we keep this simple and return a fake response if creds missing
        if not (self.account_sid and self.auth_token and self.from_number):
            return {"sid": "dev-fake", "to": to, "body": body}
        # real implementation would use twilio.rest.Client here
        # from twilio.rest import Client
        # client = Client(self.account_sid, self.auth_token)
        # msg = client.messages.create(body=body, from_=self.from_number, to=to)
        # return {"sid": msg.sid}
        return {"sid": "real-not-implemented", "to": to, "body": body}

client = TwilioClient()
