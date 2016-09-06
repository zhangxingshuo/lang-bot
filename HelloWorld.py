import tweepy
from datetime import datetime

from keys import *

auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

for i in range(1,11):
    tweet = "Counting to ten: " + i
    api.update_status(tweet)