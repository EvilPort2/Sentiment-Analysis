#!/usr/bin/env python3

import pickle
import glob
import os
import json
import string


def cleanup_reviews():
    filelist = glob.glob("reviews/*.review")
    for f in filelist:
        os.remove(f)


def find_features(document, word_features):
    words = document.split(" ")
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features


def store():
    # Load classifiers and word_features into variables
    classifiers = []                                            # List of tuples containing classifiers and their names
    for f in os.listdir('classifiers'):
        with open ('classifiers/' + f, 'rb') as fi:
            classifier = pickle.load(fi)
            classifiers.append((classifier, f))
    with open ('pickle/word_features.pickle', 'rb') as fi:
        word_features = pickle.load(fi)

    # store tweets from twitter.txt in review
    try:
        with open ("tweets/twitter.txt", encoding = "utf_16") as f:
            reviews = f.read().split("\n")
    except:
        print("\nError occured while trying to read the twitter.txt. It is either missing or it uses different character set than UTF-16.")
        input("Press ENTER to continue....")
        return

    # storing reviews given by an algorithm in reviews/ folder
    algo_review_dict = {}
    for c in classifiers:
        algo_review_dict[c[1].split(".")[0]] = []                  # Initialize review of each algorithm to an empty list

    for r in reviews:
        for c in classifiers:
            classifier = c[0]                                       # Contains the classifier
            classifier_name = c[1].split(".")[0]                    # Contains the classifier name
            feature = find_features(r, word_features)
            algo_review = classifier.classify(feature)
            algo_review_dict[classifier_name].append(algo_review)
            with open("reviews/" + classifier_name + ".review", 'a', encoding = "utf_16") as f:
                f.write(algo_review + "\n")
