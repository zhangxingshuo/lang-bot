'''
Tweet Dumper
============
Gets the most recent 3,200 tweets from specified users and writes to file.

Usage:
------
    python3 tweet_dump.py [<twitter username>] ...
'''

import tweepy
import sys

from keys import *

def get_user_tweets(user):
    print('Fetching tweets from %s...' % user)

    auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    api = tweepy.API(auth)

    all_tweets = []

    current_tweets = api.user_timeline(screen_name=user, count=200)

    all_tweets.extend(current_tweets)

    oldest = all_tweets[-1].id - 1

    while len(current_tweets) > 0:
        current_tweets = api.user_timeline(screen_name=user, count=200, max_id=oldest)
        all_tweets.extend(current_tweets)
        oldest = all_tweets[-1].id - 1

    return [(tweet.created_at, tweet.text) for tweet in all_tweets]

if __name__ == '__main__':
    tweets = get_user_tweets(sys.argv[1])

    for (time, tweet) in tweets:
        print("%s : %s" %(time, tweet))

    file = open(sys.argv[1] + '.txt', 'w')
    for (time, tweet) in tweets:
        file.write(tweet + '\n')
    file.close()