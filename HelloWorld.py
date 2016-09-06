import tweepy
from datetime import datetime

from keys import *

auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret, secure=True)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

time = str(datetime.now())

tweet = 'The time is currently ' + time

api.update_status(tweet)