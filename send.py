from decouple import config
from twilio.rest import Client 
 
account_sid = config('account_sid')
auth_token = config('auth_token')
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
    messaging_service_sid = config('messaging_service_sid'),
    body='Hello World - send SMS ',      
    to='+5511911223344' 
) 
 
print(message.sid)