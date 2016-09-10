import tweepy

from keys import *
from markov import Markov

auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

markov = Markov('tale_two_cities.txt')

tweet = markov.generate_text()[:140]

api.update_status(tweet)