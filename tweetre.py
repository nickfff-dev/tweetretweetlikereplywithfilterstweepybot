import tweepy
import urllib.request
import re
from urllib.parse import unquote
import random
import schedule
import time



consumer_key = "YJlVwDA6MaPqiq7u6RgaxIioa"
consumer_secret = "hEZBoopTtSo45eTJ3Dab32wvgHacq9KXKMuk60ZXK9vZevzcuT"
access_token = "1339948336061820930-yyh3VZqeQMncY1WzU5nSchIebC1pFB"
access_token_secret = "72QN5u3LJPE0UXhLndTeNnL1IOUg3Io31dIfPtTNnQsFd"



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

yttext = "youTube"
look_up = {"one": ["live", "stream", "Gift", "100%", "$", "youtube"],
           "two": ["clown", "food"], "three": ["Video", "health"]}


def chags(lst):
    return random.choice(lst)


def gtsts(flname):
    vitus = open(flname).read().splitlines()
    return chags(vitus)



api = tweepy.API(auth, wait_on_rate_limit=True)





def save_tweetid(tweetid):
    with open("tweetid.txt", "a") as f:
        f.write(str(tweetid) + "\n")
        f.close

def link_magic(smple):
    urls = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', smple.text)
    if urls !=[]:
        for url in urls:
            try:
                res = urllib.request.urlopen(url)
                link = res.geturl()
                if "youtube" in link:
                    valid = link
                    
            except:
                valid = ""
    else:
        valid = ""

    return valid

def dalla(tweet):
    elem = ""
    cush = re.findall('([\\$].*)', tweet.text)
    if cush !=[]:
        for ush in cush:
            elem += ush+" "
    else:
        elem = ""

    return elem










def phrase(tweet):  # sourcery no-metrics skip: remove-unnecessary-else, swap-if-else-branches
    try:
        hush = tweet.entities.get('hashtags')[0]["text"]
    except:
        hush = ""
    hush_tweet = "#" + hush if hush != "" else " "
    actual_url = link_magic(tweet)
    dollar_sign = dalla(tweet)
    if actual_url != "":
        api.create_favorite(tweet.id)
        api.update_status(gtsts("rndomst.txt") + " " + hush_tweet + " " + " "+ dollar_sign + " " + actual_url)
        print("Tweeted: " + actual_url)
    if any(term in tweet.text.lower() for term in look_up["one"]):

        first = api.update_status(gtsts("rndomst.txt") + " " + hush_tweet + " "+ dollar_sign,
                                in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
        api.retweet(first.id)
        api.create_favorite(tweet.id)

        print("passed scnd chck")
    elif any(term in tweet.text.lower() for term in look_up["two"]):

        api.create_favorite(tweet.id)
        second = api.update_status(gtsts("rndomst.txt") + " " + hush_tweet +" "+ dollar_sign,
                                in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
        api.retweet(second.id)

        print("passed third check")
    elif any(term in tweet.text.lower() for term in look_up["three"]):

        api.create_favorite(tweet.id)
        third = api.update_status(gtsts("rndomst.txt") + " " + hush_tweet + " " + dollar_sign,
                                in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
        api.retweet(third.id)


        print("passed fourth check")
    else:
        print("no check passed")
    



def janja(username):
    done_ids = open("tweetid.txt").read().splitlines()
    tweets_list = api.user_timeline(username, count=50)
    for tweet in tweets_list:
        if tweet.id_str in done_ids:
            continue
        try:
            phrase(tweet)
            save_tweetid(tweet.id)
        except:
            continue
    
    


        
schedule.every(1).minute.do(janja, username="jprmji24")
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print(e.reason)
        
    