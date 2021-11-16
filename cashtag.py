import tweepy
import urllib.request
import re
from urllib.parse import unquote
import random
import schedule
import time



consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


def dalla(username):
    tweetz = api.user_timeline(username, count=50)
    elem = ""
    for tweet in tweetz:
        try:
            cz = tweet.entities.get('symbols')
            for c in cz:
                elem += "$"+c["text"]+" "
        except:
            elem = ""
    return elem




dalla("FoxTechnicals")