from twilio.rest import Client
import os
import requests
from twilio.http.http_client import TwilioHttpClient
import os

parameter={
    "lat":20.593683,
    "lon":78.962883,
    "appid":"",
    "exclude":"daily,current,minutely"
}
account_sid =""
auth_token = ""
response= requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameter)
data=response.json()
hour=data["hourly"]
for i in range(0,11):
    wether=hour[i]["weather"][0]["id"]


if wether <700:
     proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
     client = Client(account_sid, auth_token,http_client=proxy_client)
     message = client.messages \
         .create(
         body="pick up the umberla",
         from_='+19362433972',
         to='+91 7502348732'
     )
else:
    proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
    client = Client(account_sid, auth_token,http_client=proxy_client)
    message = client.messages \
        .create(
        body="safe to go",
        from_='+19362433972',
        to='+91 7502348732'
    )

