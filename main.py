import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
# Find a location where it's currently raining on Ventusky for testing
# Then lookup on latlong.net
FROM_ = os.environ["FROM"]
TO = os.environ["TO"]

parameters = {
    "appid": os.environ["API_KEY"],
    "lat": LAT,
    "lon": LONG,
    "cnt": 4
}


response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

forecast = weather_data["list"]
will_rain = False
for entry in forecast:
    condition_code = entry["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Bring an ☂️",
        from_=FROM_,
        to=TO
    )
    print(message.status)
