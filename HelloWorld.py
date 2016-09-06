import tweepy

from keys import *

def seed(base, pow, mod=0):
    if mod == 0:
        mod = pow
    binpow = bin(pow)[2:]
    ans = base
    count = len(binpow) - 1
    # print 2**count, ans
    for char in binpow[1:]:
        count -= 1
        if char == '1':
            ans = (ans**2)*base
        else:
            ans = ans**2
        # print 2**count, ans, ans % mod
        ans %= mod
    return ans

def isPrime(n):
    if n == 2: 
        return True
    else:
        return 1 == seed(2, n-1, n)

auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

n = 0

while True:
    if isPrime(n):
        tweet = "Probably prime: %d" % n
        api.update_status(tweet)
    n += 1