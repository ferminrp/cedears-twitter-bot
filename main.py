import os
import tweepy
import requests
import json
import operator
import schedule
import time
import datetime

# Tweepy Credentials
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
CONSUMER_KEY = os.environ['CONSUMER_KEY']
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']


# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, CONSUMER_KEY)

# Create API object
api = tweepy.API(auth)

# Create a tweet
#api.update_status("Hello world, probando el api de twitter.")

def tweeter():
  # Fetching Cedears Data
  response = requests.get('https://sheets.googleapis.com/v4/spreadsheets/1NDOyoL3PGNe-rAm-eMHGrLKLASE6j_tUjkJ3lwXTqu0/values/main!A2:E193?key=AIzaSyBhiqVypmyLHYPmqZYtvdSvxEopcLZBdYU')
  data = response.json()['values']

  for cedear in data:
    cedear.append(float(cedear[3].replace('%', 'e-2')))

  top_three = sorted(data, key=operator.itemgetter(-1))[-3:]

  # number of day of the week
  weekno = datetime.datetime.today().weekday()

  # si es dia de semana twitea
  if weekno < 5:
    api.update_status("Los Cedears que mejor performaron hoy fueron {} {}, {} {} y {} {}. Tweet automático del bot de cedears.ar cedears.ar".format(top_three[2][1],top_three[2][3],top_three[1][1],top_three[1][3],top_three[0][1],top_three[0][3]))

schedule.every().day.at("21:00").do(tweeter)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute