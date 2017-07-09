import pickle
import os
from nltk import word_tokenize

def find_features(document, word_features):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

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

rev = ['pos', 'neg', 'pos', 'neg', 'pos', 'neg', 'pos', 'neg', 'pos', 'neg']

classifiers = []
for f in os.listdir('classifiers'):
    with open ('classifiers/' + f, 'rb') as fi:
        classifier = pickle.load(fi)
        classifiers.append((classifier, f))

with open ('word_features.pickle', 'rb') as fi:
    word_features = pickle.load(fi)

with open ('documents.pickle', 'rb') as fi:
    documents = pickle.load(fi)


for classifier in classifiers:
    print("Algorithm = " + classifier[1].split(".")[0])
    print("----------------------")
    correct = 0
    i = 0
    for ts in test_sentence:
        feature = find_features(ts, word_features)
        algo_rev = classifier[0].classify(feature)
        if rev[i] == algo_rev:
            correct += 1

        print("test_sentence[%d]\n\t Review by the algorithm = %s\n\t Real Review = %s" %(i, algo_rev, rev[i]))
        i += 1
    print("\nAccuracy of the algorithm = %s%s" %(str(correct/float(len(test_sentence))*100.0), "%"))
    print("\n")
