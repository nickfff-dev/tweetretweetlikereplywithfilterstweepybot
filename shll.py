import urllib.request
import re
from urllib.parse import unquote
import tweepy
import os
import json
from tweepy import OAuthHandler


class TwitterClient(object):

    # Class constructor or initialization method
    def __init__(self):

        # keys and tokens from the Twitter Dev Console
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''

    # attempt authentication
try:
    # create OAuthHandler object
    self.auth = OAuthHandler(consumer_key, consumer_secret)
    # set access token and secret
    self.auth.set_access_token(access_token, access_token_secret)
    # create tweepy API object to fetch tweets
    self.api = tweepy.API(self.auth)
except:
    print("Error: Authentication Failed")



def phrase(self, tweet):  # sourcery no-metrics skip: remove-unnecessary-else, swap-if-else-branches
    try:
        hush = tweet.entities.get('hashtags')[0]["text"]
    except:
        hush = ""
    hush_tweet = "#" + hush if hush != "" else " "
    actual_url = link_magic(tweet)
    dollar_sign = dalla(tweet)
    if actual_url != "":
        self.api.create_favorite(tweet.id)
        self.api.update_status(gtsts("rndomst.txt") + " " + hush_tweet + " " + " "+ dollar_sign + " " + actual_url)
        print("Tweeted: " + actual_url)
    if any(term in tweet.text.lower() for term in look_up["one"]):

        first = self.api.update_status(gtsts("rndomst.txt") + " " + hush_tweet + " "+ dollar_sign,
                                in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
        self.api.retweet(first.id)
        self.api.create_favorite(tweet.id)

        print("passed scnd chck")
    elif any(term in tweet.text.lower() for term in look_up["two"]):

        self.api.create_favorite(tweet.id)
        second = self.api.update_status(gtsts("rndomst.txt") + " " + hush_tweet +" "+ dollar_sign,
                                in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
        self.api.retweet(second.id)

        print("passed third check")
    elif any(term in tweet.text.lower() for term in look_up["three"]):

        self.api.create_favorite(tweet.id)
        third = self.api.update_status(gtsts("rndomst.txt") + " " + hush_tweet + " " + dollar_sign,
                                in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
        self.api.retweet(third.id)


        print("passed fourth check")
    else:
        print("no check passed")
    



def janja(self, user):
    done_ids = open("tweetid.txt").read().splitlines()
    tweets_list = self.api.user_timeline(screen_name=user, count=50)
    for tweet in tweets_list:
        if tweet.id_str in done_ids:
            continue
        try:
            self.phrase(self,tweet)
            save_tweetid(tweet.id)
        except:
            continue




