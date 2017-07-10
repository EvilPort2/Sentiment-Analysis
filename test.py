#!/usr/bin/env python3

import pickle
import os
from nltk import word_tokenize
import pandas as pd

def find_features(document, word_features):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features


# user test sentences
test_sentence = list()
test_sentence.append("This movie was great. Acting was awesome. Very fun to watch")
test_sentence.append("This movie was awful. Acting was really bad. Not at all fun.")
test_sentence.append("The performance of the actors were over the top. Jim Carrey was simply cool")
test_sentence.append("Worst movie by Christopher Nolan. Tom Hardy's dialogues were very bad.")
test_sentence.append("Jim Carrey's best comedy movie ever. Huge fun to watch. I would give this film a 10/10")
test_sentence.append("Spider Man Homecoming is not as good as previous Spider Man films.")
test_sentence.append("Spider Man Homecoming is the best Spider Man film.")
test_sentence.append("TWilight is the worst romantic film in the universe. It is basically garbage.")
test_sentence.append("Logan is the best X-Men film. It is R-rated. Hugh Jackman is the best Wolverine.")
test_sentence.append("X-Men 3: The Last Stand is the worst X-Men film in the whole franchise. It sucked.")
test_sentence.append("George Clooney's Batman was the worst Batman film")

# review of each test sentence
rev = ['pos', 'neg', 'pos', 'neg', 'pos', 'neg', 'pos', 'neg', 'pos', 'neg', 'neg']

classifiers = []
for f in os.listdir('classifiers'):
    with open ('classifiers/' + f, 'rb') as fi:
        classifier = pickle.load(fi)
        classifiers.append((classifier, f))

with open ('word_features.pickle', 'rb') as fi:
    word_features = pickle.load(fi)

with open ('documents.pickle', 'rb') as fi:
    documents = pickle.load(fi)


sentence = []
algo_review_dict = {}                                                   # dictionary that contains the review result of an algorithm where the key is the algorithm
accuracy = {}                                                           # dictionary that contains the number of accurate results of an algorithm

for classifier in classifiers:
    algo_review_dict[classifier[1].split(".")[0]] = []                  # Initialize review of each algorithm to an empty list
    accuracy[classifier[1].split(".")[0]] = 0                           # Initialize number of accurate result of each algorithm to zero


i = 0
for sent in test_sentence:
    sentence.append("test_sentence["+str(i)+"]")
    count = 0
    for classifier in classifiers:
        feature = find_features(sent, word_features)
        algo_review = classifier[0].classify(feature)
        if algo_review == rev[test_sentence.index(sent)]:
            algo_review_dict[classifier[1].split(".")[0]].append("Y")   # If the algorithm gives the correct result append Y to the algorithm review
            accuracy[classifier[1].split(".")[0]] += 1
        else:
            algo_review_dict[classifier[1].split(".")[0]].append("N")   # If the algorithm gives the wrong result append N to the algorithm review
    i += 1


df = pd.DataFrame(algo_review_dict, index = sentence)                   # Using a dataframe for better formatting of result
print(df)

print("")
for key in accuracy.keys():
    print("Accuracy of " + key + " = " + str(float(accuracy[key]/len(test_sentence))*100) + "%")
