import os
import tweepy
import requests
import json

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

# Fetching Cedears Data

# Create a tweet
api.update_status("Hello world, probando el api de twitter.")