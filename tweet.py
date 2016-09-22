'''
Twitter Tweeter
===============
Use Markov chain text generation to tweet 140 characters.

Usage:
------
    python3 tweet.py [<path to file>]
'''

import tweepy
import sys

from keys import *
# from markov import Markov

from text_gen import generate_text

def tweet(filename):
    auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    api = tweepy.API(auth)

    tweet = generate_text(filename)

    api.update_status(tweet)

if __name__ == '__main__':
    filename = sys.argv[1]
    tweet(filename)