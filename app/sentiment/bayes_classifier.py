import csv
from collections import Counter

import nltk
import pickle
from sklearn.feature_extraction import DictVectorizer
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from sentiment.tweet_preprocessor import TweetPreprocessor
from tools.classifier_stats import ClassifierStats

WORD_THRESHOLD = 4


def save_word_frequencies(filename, all_words_counts):
    with open(filename, 'w', encoding="windows-1252") as word_freq_file:
        sorted_all_words = sorted(all_words_counts, key=all_words_counts.get, reverse=True)
        for wordvalue in sorted_all_words:
            if all_words_counts[wordvalue] > WORD_THRESHOLD:
                word_freq_file.write("{}:{}\n".format(wordvalue, all_words_counts[wordvalue]))


def save_list(filename, count_list):
    with open(filename, 'w') as count_file:
        for num in count_list:
            count_file.write("{}\n".format(num))


class BayesClassifier:

    def __init__(self, classifier_data_filename):
        self.processor = TweetPreprocessor()
        self.all_words = set()
        self.all_words_count = []
        self.load_all_words_doc(classifier_data_filename)

    def load_all_words_doc(self, classifier_filename):
        all_words_list = []
        to_classify_list = []
        with open(classifier_filename, encoding="windows-1252", errors='ignore') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                text = row[1:]
                all_words_list.extend(text)
                self.all_words.update(text)
                self.all_words_count.append(len(self.all_words))
                to_classify_list.append((text, int(row[0])))
        all_words_counts = Counter(all_words_list)

        # saving word frequencies file TODO move it to some Stats object for this classifier
        save_word_frequencies('word_frequencies_v1.rxt', all_words_counts)
        save_list('word_completness.txt', self.all_words_count)

        self.all_words.update([word for word in all_words_counts if all_words_counts[word]>WORD_THRESHOLD])
        self.train_model(to_classify_list)

    def train_model(self, to_classify_list):
        train_items = []
        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(list(map(lambda l: ' '.join(l[0]), to_classify_list)))
        y = np.array(['pos' if row[1] == 4 or row[1] == 3 else 'neg' if row[1] == 1 or row[1] == 0 else 'neu' for row in to_classify_list])
        print(len(self.vectorizer.get_feature_names()))
        self.classifier = MultinomialNB().fit(X, y)

        # saving classifier for later testing
        f = open('niavebayes_classifier.pickle', 'wb')
        pickle.dump(self.classifier, f)
        f.close()

    def predict(self, text):
        X = self.vectorizer.transform([' '.join(text)])
        return self.classifier.predict(X)
