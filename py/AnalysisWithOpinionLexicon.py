#!/usr/bin/env python3

from nltk.corpus import opinion_lexicon
from nltk import word_tokenize
import matplotlib.pyplot as plt
import random

pos_word = opinion_lexicon.words("positive-words.txt")
neg_word = opinion_lexicon.words("negative-words.txt")

def analyse_with_opinion():
    try:
        with open("tweets/twitter.txt", encoding = "utf_16") as f:
            sentences =  f.read().split("\n")
    except:
        print("\nError occured while trying to read the twitter.txt. It is either missing or it uses different character set than UTF-16.")
        input("Press ENTER to continue....")
        return

    countpos = 0
    countneg = 0
    countneu = 0
    for sentence in sentences:
        pos_word_count = 0
        neg_word_count = 0
        for word in pos_word:
            if word in sentence:
                pos_word_count += 1
        for word in neg_word:
            if word in sentence:
                neg_word_count += 1
        if pos_word_count > neg_word_count:
            countpos += 1
        elif pos_word_count < neg_word_count:
            countneg += 1
        else:
            countneu += 1

    print("Number of positive tweets = %d\nNumber of negative tweets = %d\nNumber of neutral tweets = %d" %(countpos, countneg, countneu))
    pie_data = [countpos, countneg, countneu]
    labels = ["Positive tweets", "Negative tweets", "Neutral Tweets"]
    color = ["green", "red", "grey"]
    plt.title("Reviews by Opinion Lexicon")
    plt.pie(pie_data, labels = labels, colors = color, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
