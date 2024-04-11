from twilio.rest import Client
account_sid = 'ACc34ace9eee48683bbee342d8088d28b1'
auth_token = '37ed51c2ab6e18490eb7c3a086efb58b'
virtual_number = '+12568418392'
my_number = '+66630488856'

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_massage(self,massage):
        message = self.client.messages.create(
        body=massage,
        from_=virtual_number,
        to=my_number
        )


        print(message.sid)

    pass