import tweepy
from datetime import datetime

from keys import *

auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

date = str(datetime.now())

tweet = "The current time is " + date

api.update_status(tweet)