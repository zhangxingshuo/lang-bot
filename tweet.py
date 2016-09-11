import tweepy
import argparse

from keys import *
from markov import Markov

ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', help="path to file")
args = ap.parse_args()

auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

markov = Markov(args.file)

tweet = markov.generate_text()[:140]

api.update_status(tweet)