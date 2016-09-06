import tweepy

from keys import *

auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

tweet = "Just doing some testing, don't mind me..."

api.update_status(tweet)