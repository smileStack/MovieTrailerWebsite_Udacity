from twilio.rest import TwilioRestClient

account_sid = "AC53e71c666e927391d73cf111de05c61e" # Your Account SID from www.twilio.com/console
auth_token  = "7d8152e1e00286cf44d83b4731e5f1c0"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+17865373822",    # Replace with your phone number
    from_="+19544174812") # Replace with your Twilio number

print(message.sid)
