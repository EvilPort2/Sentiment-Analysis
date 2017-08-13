#!/usr/bin/env python3

import matplotlib.pyplot as plt

def get_piedata(pullData):
    x = 0
    y = 0
    xpoints = []
    ypoints = []

    countpos = 0
    countneg = 0
    countneu = 0
    for rev in pullData:
        if rev == "pos":
            countpos += 1
        elif rev == "neg":
            countneg += 1
        else:
            countneu += 1
    return [countpos, countneg, countneu]

def draw_piechart():
    labels = ["Positive tweets", "Negative tweets", "Neutral Tweets"]
    color = ["green", "red", "grey"]

    pullData1 = open("reviews/naive_bayes.review", encoding = "utf_16").read().split("\n")
    pullData2 = open("reviews/multi_naive_bayes.review", encoding = "utf_16").read().split("\n")
    pullData3 = open("reviews/logistic_regression.review", encoding = "utf_16").read().split("\n")
    pullData4 = open("reviews/sgd.review", encoding = "utf_16").read().split("\n")
    pullData5 = open("reviews/bern_naive_bayes.review", encoding = "utf_16").read().split("\n")


    pie_data = get_piedata(pullData1)
    print("\nNaive Bayes")
    print("-----------")
    print("Number of positive tweets = ", pie_data[0])
    print("Number of negative tweets = ", pie_data[1])
    print("Number of neutral tweets = ", pie_data[2])
    plt.title("Reviews by Naive Bayes")
    plt.pie(pie_data, labels = labels, colors = color, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

    pie_data = get_piedata(pullData2)
    print("\nMultinomial Naive Bayes")
    print("-----------------------")
    print("Number of positive tweets = ", pie_data[0])
    print("Number of negative tweets = ", pie_data[1])
    print("Number of neutral tweets = ", pie_data[2])
    plt.title("Reviews by Multinomial Naive Bayes")
    plt.pie(pie_data, labels = labels, colors = color, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

    pie_data = get_piedata(pullData3)
    print("\nLogistic Regression")
    print("-------------------")
    print("Number of positive tweets = ", pie_data[0])
    print("Number of negative tweets = ", pie_data[1])
    print("Number of neutral tweets = ", pie_data[2])
    plt.title("Reviews by Logistic Regression")
    plt.pie(pie_data, labels = labels, colors = color, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

    pie_data = get_piedata(pullData4)
    print("\nStochastic Gradient Descent")
    print("----------------------------")
    print("Number of positive tweets = ", pie_data[0])
    print("Number of negative tweets = ", pie_data[1])
    print("Number of neutral tweets = ", pie_data[2])
    plt.title("Reviews by Stochastic Gradient Descent")
    plt.pie(pie_data, labels = labels, colors = color, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

    pie_data = get_piedata(pullData5)
    print("\nBernoulli Naive Bayes")
    print("-----------------------")
    print("Number of positive tweets = ", pie_data[0])
    print("Number of negative tweets = ", pie_data[1])
    print("Number of neutral tweets = ", pie_data[2])
    plt.title("Reviews by Bernoulli Naive Bayes")
    plt.pie(pie_data, labels = labels, colors = color, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
    
