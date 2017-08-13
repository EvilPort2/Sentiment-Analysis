#!/usr/bin/env python3

import matplotlib.pyplot as plt
from nltk import word_tokenize
import random

word_affin_dict = {}
with open("AFINN-111.txt") as f:
    sentence = f.read().strip().split("\n")
for word_affin in sentence:
    word_affin = word_tokenize(word_affin)
    if len(word_affin) > 3:
        word_affin_dict[word_affin[0]+" "+word_affin[1]+" "+word_affin[2]] = int(word_affin[3])
    elif len(word_affin) > 2:
        word_affin_dict[word_affin[0]+" "+word_affin[1]] = int(word_affin[2])
    else:
        word_affin_dict[word_affin[0]] = int(word_affin[1])


def analyse_with_affin():
    try:
        with open("tweets/twitter.txt", encoding = "utf_16") as f:
            sentences =  f.read().split("\n")
    except:
        print("\nError occured while trying to read the twitter.txt. It is either missing or it uses different character set than UTF-16.")
        input("Press ENTER to continue....")
        return

    count_pos = 0
    count_neg = 0
    count_neu = 0
    for sentence in sentences:
        score = 0
        for word in list(word_affin_dict.keys()):
            if word in sentence:
                score += word_affin_dict[word]
        if score < 0:
            count_neg += 1
        elif score > 0:
            count_pos += 1
        else:
            count_neu += 1

    pie_data = [count_pos, count_neg, count_neu]
    labels = ["Positive tweets", "Negative tweets", "Neutral Tweets"]
    color = ["green", "red", "grey"]
    plt.title("Reviews by AFINN-111.txt")
    plt.pie(pie_data, labels = labels, colors = color, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
    print("Number of positive tweets = %d\nNumber of negative tweets = %d\nNumber of neutral tweets = %d" %(count_pos, count_neg, count_neu))


def analyse_with_affin1(sentence):
    score = 0
    for word in list(word_affin_dict.keys()):
        if word in sentence:
            score += word_affin_dict[word]
    if score < 0:
        return "neg"
    elif score > 0:
        return "pos"
    else:
        return "neu"
