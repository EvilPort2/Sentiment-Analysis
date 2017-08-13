#!/usr/bin/env python3

import os
from py.CreateClassifiers import create_classifiers, cleanup_classifiers
from py.DrawGraph import draw_piechart
from py.StoreTweetReview import cleanup_reviews, store
from py.GetLiveTweets import cleanup_tweets, get_live_tweets
from py.GetSearchTweets import get_search_tweets
from py.AnalysisWithAffin import analyse_with_affin
from py.AnalysisWithOpinionLexicon import analyse_with_opinion
from py.CreateDatasetWithTweets import create_dataset

if os.name == 'nt':
    clear_screen = "cls"
else:
    clear_screen = "clear"

def main():
    while True:
        os.system(clear_screen)
        print("\t\t\tSentiment Analysis")
        print("\t\t\t" + 18 * "-")
        print("\nOptions:-\n")
        print("1. Get live tweets using Tweepy\n2. Get search tweets using Tweepy\n3. Show first 10 tweets\n4. Sentiment Analysis using NLTK's Opinion Lexicon\n5. Sentiment Analysis using AFINN-111.txt\n6. Sentiment Analysis using Machine Learning Algorithms\n7. Exit")
        c = input("\nCHOICE: ")
        try:
            c = int(c)
        except:
            print("Enter an integer value")
            input("Press ENTER to continue.....")
            continue
        if c < 1 or c > 7:
            print("Enter a value between 1 and 6")
            input("Press ENTER to continue.....")
            continue

        if c == 1:
            while True:
                os.system(clear_screen)
                print("\t\t\tGet live tweets using Tweepy")
                print("\t\t\t----------------------------")
                print("\nINFO:\tThis option will fetch live tweets from Twitter using Tweepy API.\n\tSince Tweepy is fetching live tweets it is much slower than TwitterSearch API.\n\tVery useful if you want to look for current affairs.\n\n")

                print("1. Delete old tweets in the tweets folder\n2. Get new tweets\n3. Go Back")
                ch = input("\nCHOICE: ")
                try:
                    ch = int(ch)
                except:
                    print("Enter an integer value")
                    input("Press ENTER to continue...")
                    continue
                if ch == 1:
                    print("Old tweets removed.")
                    cleanup_tweets()
                    input("Press ENTER to continue...")
                elif ch == 2:
                    search_topic = []
                    topic = input("Enter topic you need to search: ")
                    search_topic.append(topic)

                    try:
                        with open("tweets/twitter.txt", encoding = "utf_16") as f:
                            lines = len(f.read().split("\n"))
                    except:
                        lines = 0

                    while True:
                        tweet_count = input("How many tweets do you need? (default is 200): ")
                        if tweet_count == "":
                            get_live_tweets(search_topic, 200, lines)
                            break
                        try:
                            tweet_count = int(tweet_count)
                            break
                        except:
                            print("Enter an integer value")

                    get_live_tweets(search_topic, tweet_count, lines)
                    print("\n\nNew Tweets fetched")
                    input("Press ENTER to continue...")
                elif ch == 3:
                    break
                else:
                    print("Enter a number between 1 and 3")
                    input("Press ENTER to continue...")

        elif c == 2:
            while True:
                os.system(clear_screen)
                print("\t\t\tGet search tweets using Tweepy")
                print("\t\t\t-------------------------------")
                print("\nINFO:\tThis option will fetch all except live tweets from Twitter using Tweepy API.\n\tSince we are searching instead of live streaming it is much faster.\n\tVery useful if you want to look for old events.\n\n")

                print("1. Delete old tweets in the tweets folder\n2. Get new tweets\n3. Go Back")
                ch = input("\nCHOICE: ")
                try:
                    ch = int(ch)
                except:
                    print("Enter an integer value")
                    input("Press ENTER to continue...")
                    continue
                if ch == 1:
                    print("Old tweets removed.")
                    cleanup_tweets()
                    input("Press ENTER to continue...")
                elif ch == 2:
                    search_topic = input("Enter topic you need to search: ")
                    f = 0
                    while True:
                        tweet_count = input("How many tweets do you need? (default is 200): ")
                        if tweet_count == "":
                            f = 1
                            break
                        try:
                            tweet_count = int(tweet_count)
                            break
                        except:
                            print("Enter an integer value")

                    if f == 0:
                        print("\nFetching %d tweets on the topic %s...." %(tweet_count, search_topic))
                        for i in range(int(tweet_count/100)):
                            get_search_tweets(search_topic, 100)
                        if not tweet_count%100 == 0:
                            get_search_tweets(search_topic, tweet_count%100)
                    else:
                        print("\nFetching 200 tweets on the topic %s...." %search_topic)
                        get_search_tweets(search_topic, 100)
                        get_search_tweets(search_topic, 100)

                    print("\n\nNew Tweets fetched")
                    input("Press ENTER to continue...")
                elif ch == 3:
                    break
                else:
                    print("Enter a number between 1 and 3")
                    input("Press ENTER to continue...")


        elif c == 3:
            os.system(clear_screen)
            print("\t\t\tFirst 10 tweets")
            print("\t\t\t---------------\n\n")
            with open("tweets/twitter.txt", encoding = "utf_16") as f:
                tweets = f.read().split("\n")
            for tweet in tweets[:10]:
                print(tweet)
                print("------------------------------------")
            input("\n\nPress ENTER to continue......")

        elif c == 4:
            while True:
                os.system(clear_screen)
                print("\t\t\tSentiment Analysis using NLTK's Opinion Lexicon")
                print("\t\t\t-----------------------------------------------")
                print("\nINFO:\tNLTK's opinion lexicon contains lists for posiive and negative words.\n\tThis algorithm uses these lists to find out the number of positive and negative words in a tweet.\n\tThe number of positive and negative words in the tweet determines if it is positive or negative.")
                print("\n1. Analyse using Opinion lexicon.\n2. Go Back")
                ch = input("\nCHOICE: ")
                try:
                    ch = int(ch)
                except:
                    print("Enter an integer value")
                    input("Press ENTER to continue...")
                    continue
                if ch == 1:
                    print("Analyzing. Please wait....")
                    analyse_with_opinion()
                    input("Press ENTER to continue...")
                elif ch == 2:
                    break
                else:
                    print("Enter a number between 1 and 2")
                    input("Press ENTER to continue...")

        elif c == 5:
            while True:
                os.system(clear_screen)
                print("\t\t\tSentiment Analysis using AFINN-111.txt")
                print("\t\t\t--------------------------------------")
                print("\nINFO:\tAFINN-111.txt contains a list of posiive and negative words along with their score.\n\tThis algorithm uses these scores to find out the total score of positive and negative words in a tweet.\n\tThe total score of positive and negative words in the tweet determines if it is positive or negative.")
                print("\n1. Analyse using AFINN-111.txt.\n2. Go Back")
                ch = input("\nCHOICE: ")
                try:
                    ch = int(ch)
                except:
                    print("Enter an integer value")
                    input("Press ENTER to continue...")
                    continue
                if ch == 1:
                    print("Analyzing. Please wait....")
                    analyse_with_affin()
                    input("Press ENTER to continue...")
                elif ch == 2:
                    break
                else:
                    print("Enter a number between 1 and 2")
                    input("Press ENTER to continue...")

        elif c == 6:
            while True:
                os.system(clear_screen)
                print("\t\t\tSentiment Analysis using Machine Learning")
                print("\t\t\t-----------------------------------------")
                print("\nINFO:\tThis module trains and creates classifiers which are used to classify the tweets.\n\tThe classifiers (which are mainly Machine Learning algorithms) used here are Naive Bayes, Bernoulli Naive Bayes,\n\tMultinomial Naive Bayes, Logistic Regression and Stochastic Gradient Descent.")
                print("\n1. Delete the old trained classifiers\n2. Train classifiers using new tweets in tweets/twitter.txt\n3. Analyse tweets using the classifiers and draw pie charts for them.\n4. Go Back")
                ch = input("\nCHOICE: ")
                try:
                    ch = int(ch)
                except:
                    print("Enter an integer value")
                    input("Press ENTER to continue...")
                    continue
                if ch == 1:
                    print("Previous classifiers are being wiped out....")
                    cleanup_classifiers()
                    input("Press ENTER to continue...")
                elif ch == 2:
                    print("Dataset is being created.....")
                    create_dataset("tweets/twitter.txt")
                    print("Classfiers are being created....")
                    create_classifiers()
                    input("Press ENTER to continue...")
                elif ch == 3:
                    print("Analyzing. Please wait....")
                    cleanup_reviews()
                    store()
                    draw_piechart()
                    input("Press ENTER to continue...")
                elif ch == 4:
                    break
                else:
                    print("Enter a number between 1 and 4")
                    input("Press ENTER to continue...")

        elif c == 7:
            print("Exiting.....")
            return

try:
    main()
except KeyboardInterrupt as e:
    print("\n\nCTRL + C pressed. Exiting....")
