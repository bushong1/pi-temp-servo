import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()

open_weather_api_key = os.environ['OPEN_WEATHER_KEY']

run_forever = True

locations = [
  {
    "name": "Pete's house",
    "lat": "39.4",
    "long": "-77.3",
    "display_seconds": 6
  },
  {
    "name": "Charles' house",
    "lat": "39.3",
    "long": "-76.9",
    "display_seconds": 2
  },
  {
    "name": "The Cabin",
    "lat": "39.5",
    "long": "-78.2",
    "display_seconds": 2
  },
  {
    "name": "Brisbane, Australia",
    "lat": "-27.45659047285547",
    "long": "153.03424860917326",
    "display_seconds": 2
  },
]

def get_temp(location):
  response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=minutely,hourly,daily&appid=%s" % (location["lat"], location["long"], open_weather_api_key))
  if(response.status_code == 200):
    return response.json()["current"]["temp"] # // .1 / 10
  else:
    return -1

def display_temp(temp):
  print(f"Displaying temp:       {temp}F")
  # TODO: Insert servo control

def display_location(location):
  print(f"Displaying location:   {location['name']}")
  # TODO: Insert display control

def wait_on_change(location):
  print(f"Waiting {location['display_seconds']} seconds...")
  time.sleep(location['display_seconds'])

def k_to_f(temp):
  c = temp - 273.15
  return c * 9 /5 + 32

while(run_forever):
  for location in locations:
    print(f"Fetching temp for {location['name']}...")
    temp = get_temp(location)
    if(temp > 0):
      f_temp = k_to_f(temp) // .1 / 10
      display_temp(f_temp)
      display_location(location)
      wait_on_change(location)
    else:
      print("ERROR: Failed to fetch temperature; refusing to update; trying again in 60 seconds...")
      time.sleep(60)
