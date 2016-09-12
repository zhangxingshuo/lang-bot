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
from markov import Markov

def tweet(filename):
    auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    api = tweepy.API(auth)

    markov = Markov(filename)

    text = markov.generate_text().split()

    tweet = ''

    index = 0

    while len(tweet + text[index] + ' ') <= 140:
        tweet += text[index] + ' '
        index += 1

    api.update_status(tweet)

if __name__ == '__main__':
    filename = sys.argv[1]
    tweet(filename)