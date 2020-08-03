from twilio.rest import Client
client=Client('ACCOUNT SID','AUTH TOKEN')
message=client.messages.create(body='what am i doing',from_='whatsapp:+14155238886',to='whatsapp:+91----------')
print(message.sid)