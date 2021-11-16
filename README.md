### Twilio - steps

1 - Enter in [twilio console](https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1)  
2 - Create a [Messaging service](https://console.twilio.com/us1/develop/sms/services?frameUrl=%2Fconsole%2Fsms%2Fservices%3Fx-target-region%3Dus1)  
3 - [Try send SMS in console](https://console.twilio.com/us1/develop/sms/try-it-out/send-an-sms?frameUrl=%2Fconsole%2Fsms%2Fgetting-started%2Fbuild%3Fx-target-region%3Dus1)



### Create a .env file
```shell
# twilio Credentials
account_sid = 
auth_token = 
messaging_service_sid =
```


### Run
```shell
pyenv local 3.8.10

pipenv shell

pipenv sync

python send.py
```