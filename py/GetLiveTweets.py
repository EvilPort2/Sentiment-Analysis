#!/usr/bin/env python3

import tweepy
from tweepy import OAuthHandler
import os
import glob

# Cleanup
def cleanup_tweets():
    filelist = glob.glob("tweets/*.txt")
    for f in filelist:
        os.remove(f)


class TwitterSentimentStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        review = status.text
        review = review.replace("\n", " ")
        print(review + "\n--------------------------")
        with open("tweets/twitter.txt", 'a', encoding='utf_16') as f:
            try:
                f.write(review + "\n")
            except:
                return False

    def on_error(self, status_code):
        if status_code == 420:
            print("Data is disconnected from the stream. Error code: 420")
            return False

    def on_disconnect(self, notice):
        print(notice)

    def on_timeout(self):
        print("API timed out")


def get_live_tweets(search_topic, tweet_count, lines):
    """
    this function is used to fetch  tweets from twitter on the given search_topic
    """

    # consumer key, consumer secret, access token, access secret.
    consumer_key = "aaaaaaaaaaaaaaaa"
    consumer_secret = "aaaaaaaaaaaaaaaaaaaaaaa"
    access_token = "aaaaaaaaaaaaa-aaaaaaaaaaaaaaaaaaaa"
    access_token_secret = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    #api = tweepy.API(auth)

    myStreamListener = TwitterSentimentStreamListener()
    myStream = tweepy.Stream(auth, myStreamListener)

    myStream.retry_420_start = True
    myStream.retry_count = 10
    myStream.filter(languages=['en'], track=search_topic, async = True)

    print("\nFetching live tweets on \'" + search_topic[0] + "\'.....\n")
    c = 0
    while True:
        try:
            with open("tweets/twitter.txt", encoding='utf_16') as f:
                tweets = f.read().split("\n")
            if len(tweets) >= tweet_count + lines:
                myStream.disconnect()
                print("Successfully fetched %d tweets" %(tweet_count))
                break
        except FileNotFoundError as e:
            pass
