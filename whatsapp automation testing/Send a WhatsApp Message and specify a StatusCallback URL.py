from twilio.rest import Client
client=Client('ACCOUNT SID','AUTH TOKEN')
message=client.messages.create(body='Hey, I just met you, and this is crazy...',status_callback='https://postb.in/1596427679094-1412583859637',from_='whatsapp:+14155238886',to='whatsapp:+91----------')
print(message.sid)