import tweepy
import urllib.request
import re
from urllib.parse import unquote
import random
from keep_alive import keep_alive
import schedule
import time



consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

yttext = "youTube"
look_up = {"one": ["live", "stream", "Gift", "100%", "$"],
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


def phrase(username):  # sourcery no-metrics skip: remove-unnecessary-else, swap-if-else-branches
    done_ids = open("tweetid.txt").read().splitlines()
    tweets_list = api.user_timeline(username, count=30)
    for tweet in tweets_list:
        if tweet.id_str not in done_ids:
            try:
                hush = tweet.entities.get('hashtags')[0]["text"]
            except:
                hush = ""
            hush_tweet = "#" + hush if hush != "" else " "
            print(hush_tweet)
            if any(term in tweet.text.lower() for term in look_up["one"]):
                save_tweetid(tweet.id)
                first = api.update_status(gtsts("rndomst.txt") + " " + hush_tweet + " " ,
                                        in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
                api.create_favorite(tweet.id)
                api.retweet(first.id)
                print("1")
            elif any(term in tweet.text.lower() for term in look_up["two"]):
                save_tweetid(tweet.id)
                second = api.update_status(gtsts("rndomst.txt") + " " + hush_tweet + " " ,
                                        in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
                api.create_favorite(tweet.id)
                api.retweet(second.id)
                print("2")
            elif any(term in tweet.text.lower() for term in look_up["three"]):
                save_tweetid(tweet.id)
                third = api.update_status(gtsts("rndomst.txt") + " " + hush_tweet + " " ,
                                        in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
                api.create_favorite(tweet.id)
                api.retweet(third.id)
                print("3")
            else:
                try: 
                    urls = tweet.entities["urls"][0]["expanded_url"]
                except:
                    urls = ""
                print(urls)
                if urls != "":
                    fr = urllib.request.urlopen(urls)
                    actual_url = fr.geturl()
                    print(actual_url)
                    if "youtube" in actual_url:
                        save_tweetid(tweet.id)
                        api.update_status(gtsts("rndomst.txt") + " " + hush_tweet + " " + actual_url)
                        api.create_favorite(tweet.id)
                    else:
                        continue
                elif "youtube" in tweet.text:
                    save_tweetid(tweet.id)
                    xw = api.update_status(gtsts("rndomst.txt") + " " + hush_tweet + " " )
                    api.create_favorite(tweet.id)
                else:
                    continue
        else:
            continue

        
schedule.every(0.5).minutes.do(phrase, "Jprmji24")
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print(e)
        continue
