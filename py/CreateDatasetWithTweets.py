from .AnalysisWithAffin import analyse_with_affin1
import os

def create_dataset(filepath):

    os.remove("dataset/twitter_neg.txt")
    os.remove("dataset/twitter_pos.txt")
    os.remove("dataset/twitter_neu.txt")

    try:
        with open(filepath, encoding = "utf_16") as f:
            sentences = f.read().split("\n")
    except FileNotFoundException as e:
        print("%s is not found" %filepath)
        return


    for sentence in sentences:
        if analyse_with_affin1(sentence) == "pos":
            with open("dataset/twitter_pos.txt", "a", encoding = "utf_16") as f1:
                f1.write(sentence + "\n")
        elif analyse_with_affin1(sentence) == "neg":
            with open("dataset/twitter_neg.txt", "a", encoding = "utf_16") as f1:
                f1.write(sentence + "\n")
        else:
            with open("dataset/twitter_neu.txt", "a", encoding = "utf_16") as f1:
                f1.write(sentence + "\n")
