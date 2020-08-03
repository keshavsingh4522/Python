from twilio.rest import Client
client=Client('ACCOUNT SID','AUTH TOKEN')

message=client.messages.create(body='💖Because I knew you, I have been **changed** _for good_.💚',from_='whatsapp:+14155238886',to='whatsapp:+91----------')
print(message.sid)