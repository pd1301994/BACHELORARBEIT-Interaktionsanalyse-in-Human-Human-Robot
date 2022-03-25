import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from nltk.tokenize import word_tokenize

short_instr = open("datadirect/instructions.txt", "r", encoding='UTF-8').read()
short_small = open("datadirect/smalltalk.txt", "r", encoding='UTF-8').read()

all_words = []
documents = []


from HanTa import HanoverTagger as ht

tagger = ht.HanoverTagger('morphmodel_ger.pgz')

for p in short_instr.split('\n'):
    documents.append((p, "ins"))
    words = word_tokenize(p,language='german')

    for w in words:
        if tagger.analyze(w)[1] == 'VVINF' or tagger.analyze(w)[1] == 'ADV' or tagger.analyze(w)[1] == 'NN' or \
                tagger.analyze(w)[1] == 'VVFIN' or tagger.analyze(w)[1] == 'VMFIN' or tagger.analyze(w)[1] == 'VMINF' or\
                tagger.analyze(w)[1] == 'VVPP':
            all_words.append(tagger.analyze(w)[0])

for p in short_small.split('\n'):
    documents.append((p, "sml"))
    words = word_tokenize(p,language='german')
    for w in words:
        if tagger.analyze(w)[1] == 'VVINF' or tagger.analyze(w)[1] == 'ADV' or tagger.analyze(w)[1] == 'NN' or \
                tagger.analyze(w)[1] == 'VVFIN' or tagger.analyze(w)[1] == 'VMFIN' or \
                tagger.analyze(w)[1] == 'VMINF' or tagger.analyze(w)[1] == 'VVPP':
            all_words.append(tagger.analyze(w)[0])


save_documents = open("pickled_algos/documents.pickle", "wb")
pickle.dump(documents, save_documents)
save_documents.close()

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())

save_word_features = open("pickled_algos/word_features5k.pickle", "wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


featuresets = [(find_features(x), category) for (x, category) in documents]
print(featuresets)
random.shuffle(featuresets)
testing_set = featuresets[500:]
training_set = featuresets[:500]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set)) * 100)
classifier.show_most_informative_features(15)
save_classifier = open("pickled_algos/originalnaivebayes5k.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set)) * 100)

save_classifier = open("pickled_algos/MNB_classifier5k.pickle", "wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set)) * 100)

save_classifier = open("pickled_algos/BernoulliNB_classifier5k.pickle", "wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()
