import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize



class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


documents_f = open("machine_learning/documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()




word_features5k_f = open("machine_learning/word_features5k.pickle", "rb")
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features



# featuresets_f = open("featuresets.pickle", "rb")
# featuresets = pickle.load(featuresets_f)
# featuresets_f.close()

# random.shuffle(featuresets)
# print(len(featuresets))

# testing_set = featuresets[10000:]
# training_set = featuresets[:10000]



open_file = open("machine_learning/originalnaivebayes5k.pickle", "rb")
classifier = pickle.load(open_file)
open_file.close()
#classifier.show_most_infomative_features(15)

open_file = open("machine_learning/MNB_classifier5k.pickle", "rb")
MNB_classifier = pickle.load(open_file)
open_file.close()



open_file = open("machine_learning/BernoulliNB_classifier5k.pickle", "rb")
BernoulliNB_classifier = pickle.load(open_file)
open_file.close()


# open_file = open("LogisticRegression_classifier5k.pickle", "rb")
# LogisticRegression_classifier = pickle.load(open_file)
# open_file.close()


# open_file = open("LinearSVC_classifier5k.pickle", "rb")
# LinearSVC_classifier = pickle.load(open_file)
# open_file.close()


open_file = open("machine_learning/SGDC_classifier5k.pickle", "rb")
SGDC_classifier = pickle.load(open_file)
open_file.close()




voted_classifier = VoteClassifier(
                                  classifier,
                                  SGDC_classifier,                                  
                                  MNB_classifier,
                                  BernoulliNB_classifier)




def sentiment(text):
    feats = find_features(text)

    return voted_classifier.classify(feats),voted_classifier.confidence(feats)