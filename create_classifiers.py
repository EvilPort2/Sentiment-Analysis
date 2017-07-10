#!/usr/bin/env python3

# NOTE : run nltk.download() in the python prompt to check if the movie_reviews folder is updated

"""
This file is to be called first.
This file is use to create a training dataset and testing dataset.
It uses the files in /root/nltk_data/corpora/movie_reviews folder
"""

import nltk
import random
import pickle
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
import string
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from pathlib import Path


stop = set(stopwords.words('english'))              # stopwords of the english language

def find_features(document, word_features):
    '''
    function that will find the top words in our positive and negative documents,
    marking their presence as either positive or negative
    '''
    words = set(document)
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

    if Path('document.pickle').exists:                    # if documents.pickle already exists use it
        print("Loading documents.pickle in documents...")
        with open ('documents.pickle', 'rb') as fi:
            documents = pickle.load(fi)
    else:                                               # else create it
        # category = positive or negative
        # fileid = file id for the files in pos or neg folder inside the /root/nltk_data/corpora/movie_reviews
        print("documents list is being created...")
        for category in movie_reviews.categories():         # movie_reviews.categories() return pos or neg
             for fileid in movie_reviews.fileids(category): # movie_reviews.fileids(category) return the file names of the files in neg or pos folder
                 words = list(movie_reviews.words(fileid))
                 for word in words:
                     if word in stop and word in string.punctuation and not word.isalpha():
                         words.remove(word)
                 documents.append((words, category))
        with open("documents.pickle", 'wb') as f:
            pickle.dump(documents, f)

    random.shuffle(documents)                           # shuffle documents
    random.shuffle(documents)                           # shuffle documents
    random.shuffle(documents)                           # shuffle documents

    all_words = []                                      # contains every word in the movie_reviews
    for w in movie_reviews.words():
        if w not in stop and w not in string.punctuation and w.isalpha():
            all_words.append(w.lower())                 # all words except the stopwords like "the", "a" etc and punctuations.
    all_words = nltk.FreqDist(all_words)                # converts the list to a NLTK Frequency distribution
    word_features = list(all_words.keys())[:20000]      # Word feature list
    with open("word_features.pickle", 'wb') as f:
        pickle.dump(word_features, f)


    # category = pos or neg
    # rev = review file words
    featuresets = [(find_features(rev, word_features), category) for (rev, category) in documents]     # this list will contain both the training set and the testing set
    trainingset = featuresets[:int(len(featuresets) * 3/4)]  # used to train the algorithm
    testingset = featuresets[int(len(featuresets) * 3/4):]   # used to test the algorithm

    return trainingset, testingset, word_features


def create_nb_classifier(trainingset, testingset):
    # Naive Bayes Classifier
    print("Naive Bayes classifier is being trained and created...")
    NB_classifier = nltk.NaiveBayesClassifier.train(trainingset)
    accuracy = nltk.classify.accuracy(NB_classifier, testingset)*100
    print("Naive Bayes Classifier accuracy = " + str(accuracy))
    NB_classifier.show_most_informative_features(20)
    save_classifier(NB_classifier, "classifiers/naive_bayes.pickle")
    return NB_classifier


def create_mnb_classifier(trainingset, testingset):
    # Multinomial Naive Bayes Classifier
    print("\nMultinomial Naive Bayes classifier is being trained and created...")
    MNB_classifier = nltk.SklearnClassifier(MultinomialNB())
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


def create_sgdc_classifier(trainingset, testingset):
    print("\nSGDC classifier is being trained and created...")
    SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
    SGDClassifier_classifier.train(trainingset)
    print("SGDClassifier classifier accuracy = " + str((nltk.classify.accuracy(SGDClassifier_classifier, testingset))*100))
    save_classifier(SGDClassifier_classifier, "classifiers/sgdc.pickle")
    return SGDClassifier_classifier


def create_svc_classifier(trainingset, testingset):
    print("\nSVC classifier is being trained and created...")
    SVC_classifier = SklearnClassifier(SVC())
    SVC_classifier.train(trainingset)
    print("SVC classifier accuracy = " + str((nltk.classify.accuracy(SVC_classifier, testingset))*100))
    save_classifier(SVC_classifier, "classifiers/svc.pickle")
    return SVC_classifier


def create_linear_svc_classifier(trainingset, testingset):
    print("\nLinear SVC classifier is being trained and created...")
    LinearSVC_classifier = SklearnClassifier(LinearSVC())
    LinearSVC_classifier.train(trainingset)
    print("LinearSVC_classifier accuracy percent = " + str((nltk.classify.accuracy(LinearSVC_classifier, testingset))*100))
    save_classifier(LinearSVC_classifier, "classifiers/linear_svc.pickle")
    return LinearSVC_classifier


def create_nu_svc_classifier(trainingset, testingset):
    print("\nNuSVC classifier is being trained and created...")
    NuSVC_classifier = SklearnClassifier(NuSVC())
    NuSVC_classifier.train(trainingset)
    print("NuSVC_classifier accuracy percent = " + str((nltk.classify.accuracy(NuSVC_classifier, testingset))*100))
    save_classifier(NuSVC_classifier, "classifiers/nu_svc.pickle")
    return NuSVC_classifier




def main():
    trainingset, testingset, word_features = create_training_testing_wordfeature()
    create_nb_classifier(trainingset, testingset)
    create_mnb_classifier(trainingset, testingset)
    create_bnb_classifier(trainingset, testingset)
    create_sgdc_classifier(trainingset, testingset)
    create_logistic_regression_classifier(trainingset, testingset)
    create_svc_classifier(trainingset, testingset)
    create_linear_svc_classifier(trainingset, testingset)
    create_nu_svc_classifier(trainingset, testingset)

main()
