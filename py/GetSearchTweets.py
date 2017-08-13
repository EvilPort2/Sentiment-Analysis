#!/usr/bin/env python3

import tweepy
from tweepy import OAuthHandler
from tweepy.parsers import JSONParser


def get_search_tweets(search_topic, tweet_count):
    consumer_key = "aaaaaaaaaaaaaaaa"
    consumer_secret = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    access_token = "aaaaaaaaaaaaa-taaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    access_token_secret = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=JSONParser())

    res_json = api.search(q=search_topic, lang="en", count=tweet_count)
    for res in res_json['statuses']:
        with open("tweets/twitter.txt", "a", encoding="utf_16") as f:
            f.write(res['text'].replace("\n", " ") + " \n")
        print(res['text'])
        print("--------------------------------")
