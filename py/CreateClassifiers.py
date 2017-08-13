#!/usr/bin/env python3

import nltk
from nltk import word_tokenize
import random
import pickle
from nltk.corpus import stopwords
import string
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from pathlib import Path
import os
import glob


def cleanup_classifiers():
    filelist = glob.glob("classifiers/*.pickle")
    for f in filelist:
        os.remove(f)
    filelist = glob.glob("pickle/*.pickle")
    for f in filelist:
        os.remove(f)
    print("classifiers/ and pickle/ folder created")


def find_features(document, word_features):
    '''
    function that will find the top words in our positive and negative documents,
    marking their presence as either positive or negative
    '''
    words = document.split(" ")
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

def save_classifier(classifier, filename):
    """
    this function is used to save a classifier to a file
    """
    with open(filename, 'wb') as f:
        pickle.dump(classifier, f)

def create_training_testing_wordfeature():
    """
    this function creates and returns training dataset, testing dataset and word_features
    """
    documents = []                                      # it is a list of tuples containing the words of fileid and the category
    all_words = []                                      # contains every word in the movie_reviews

    tweet_neg = open("dataset/twitter_neg.txt", encoding = 'utf_16').read()
    tweet_pos = open("dataset/twitter_pos.txt", encoding = 'utf_16').read()
    tweet_neu = open("dataset/twitter_neu.txt", encoding = 'utf_16').read()

    if 'documents.pickle' in os.listdir('./') and 'all_words.pickle' in os.listdir('./'):  # if documents.pickle already exists use it
        print("Loading documents.pickle and all_words.pickle...")
        with open ('pickle/documents.pickle', 'rb') as fi:
            documents = pickle.load(fi)
        with open('pickle/pickle/all_words.pickle', 'rb') as fi:
            all_words = pickle.load(fi)
    else:                                                                                   # else create it
        for r in tweet_pos.split('\n'):
            documents.append((r, "pos"))
        for r in tweet_neg.split('\n'):
            documents.append((r, "neg"))
        for r in tweet_neu.split('\n'):
            documents.append((r, "neu"))

        short_pos_words = tweet_pos.split(" ")
        short_neg_words = tweet_neg.split(" ")
        short_neu_words = tweet_neu.split(" ")
        for w in short_pos_words:
            all_words.append(w.lower())
        for w in short_neg_words:
            all_words.append(w.lower())
        for w in short_neu_words:
            all_words.append(w.lower())

        with open("pickle/documents.pickle", 'wb') as f:
            pickle.dump(documents, f)
        with open("pickle/all_words.pickle", 'wb') as f:
            pickle.dump(all_words, f)
        print("documents.pickle created")
        print("all_words.pickle created\n")

    random.shuffle(documents)                           # shuffle documents
    random.shuffle(documents)                           # shuffle documents
    random.shuffle(documents)                           # shuffle documents


    all_words = nltk.FreqDist(all_words)                # converts the list to a NLTK Frequency distribution
    word_features = list(all_words.keys())[:2000]       # Word feature list(Top 2000 words)
    with open("pickle/word_features.pickle", 'wb') as f:
        pickle.dump(word_features, f)


    featuresets = [(find_features(tweet, word_features), category) for (tweet, category) in documents]     # this list will contain both the training set and the testing set
    print("Size of feature set = " + str(len(featuresets)))
    trainingset = featuresets[:int(len(featuresets) * 3/4)]  # used to train the algorithm
    print("Size of training set = " + str(len(trainingset)))
    testingset = featuresets[int(len(featuresets) * 3/4):]   # used to test the algorithm
    print("Size of testing set = " + str(len(testingset)))
    return trainingset, testingset, word_features


def create_nb_classifier(trainingset, testingset):
    # Naive Bayes Classifier
    print("\nNaive Bayes classifier is being trained and created...")
    NB_classifier = NaiveBayesClassifier.train(trainingset)
    accuracy = nltk.classify.accuracy(NB_classifier, testingset)*100
    print("Naive Bayes Classifier accuracy = " + str(accuracy))
    NB_classifier.show_most_informative_features(20)
    save_classifier(NB_classifier, "classifiers/naive_bayes.pickle")
    return NB_classifier


def create_mnb_classifier(trainingset, testingset):
    # Multinomial Naive Bayes Classifier
    print("\nMultinomial Naive Bayes classifier is being trained and created...")
    MNB_classifier = SklearnClassifier(MultinomialNB())
    MNB_classifier.train(trainingset)
    accuracy = nltk.classify.accuracy(MNB_classifier, testingset)*100
    print("MultinomialNB Classifier accuracy = " + str(accuracy))
    save_classifier(MNB_classifier, "classifiers/multi_naive_bayes.pickle")
    return MNB_classifier


def create_bnb_classifier(trainingset, testingset):
    # Bernoulli Naive Bayes Classifier
    print("\nBernoulli Naive Bayes classifier is being trained and created...")
    BNB_classifier = SklearnClassifier(BernoulliNB())
    BNB_classifier.train(trainingset)
    accuracy = nltk.classify.accuracy(BNB_classifier, testingset)*100
    print("BernoulliNB accuracy percent = " + str(accuracy))
    save_classifier(BNB_classifier, "classifiers/bern_naive_bayes.pickle")
    return BNB_classifier


def create_logistic_regression_classifier(trainingset, testingset):
    # Logistic Regression classifier
    print("\nLogistic Regression classifier is being trained and created...")
    LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
    LogisticRegression_classifier.train(trainingset)
    print("Logistic Regression classifier accuracy = "+ str((nltk.classify.accuracy(LogisticRegression_classifier, testingset))*100))
    save_classifier(LogisticRegression_classifier, "classifiers/logistic_regression.pickle")
    return LogisticRegression_classifier


def create_sgd_classifier(trainingset, testingset):
    print("\nSGD classifier is being trained and created...")
    SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
    SGDClassifier_classifier.train(trainingset)
    print("SGD Classifier classifier accuracy = " + str((nltk.classify.accuracy(SGDClassifier_classifier, testingset))*100))
    save_classifier(SGDClassifier_classifier, "classifiers/sgd.pickle")
    return SGDClassifier_classifier


def create_classifiers():
    trainingset, testingset, word_features = create_training_testing_wordfeature()
    create_nb_classifier(trainingset, testingset)
    create_bnb_classifier(trainingset, testingset)
    create_mnb_classifier(trainingset, testingset)
    create_logistic_regression_classifier(trainingset, testingset)
    create_sgd_classifier(trainingset, testingset)
