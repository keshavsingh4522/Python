from twilio.rest import Client
client=Client('ACCOUNT SID','AUTH TOKEN')

message=client.messages.create(body='Twilio HQ',persistent_action=['geo:37.787890,-122.391664|375 Beale St'],from_='whatsapp:+14155238886',to='whatsapp:+91----------')

print(message.sid)