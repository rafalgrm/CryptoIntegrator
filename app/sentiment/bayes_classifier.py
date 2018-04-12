import csv
from collections import Counter

import nltk
import pickle

from sentiment.tweet_preprocessor import TweetPreprocessor

WORD_THRESHOLD = 3


class BayesClassifier:

    def __init__(self, classifier_data_filename):
        self.processor = TweetPreprocessor()
        self.all_words = set()  # TODO change it to only include words that have at least n occurrences in training data
        self.load_all_words_doc(classifier_data_filename)

    def load_all_words_doc(self, classifier_filename):
        all_words_list = []
        to_classify_list = []
        with open(classifier_filename, encoding="windows-1252") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                text = self.processor.stem_tweet(self.processor.tokenize_tweet(row[5]))
                all_words_list.extend(text)
                to_classify_list.append((text, int(row[0])))
        all_words_counts = Counter(all_words_list)
        self.all_words.update([word for word in all_words_counts if all_words_counts[word]>WORD_THRESHOLD])
        self.train_model(to_classify_list)

    def train_model(self, to_classify_list):
        train_items = []
        for row in to_classify_list:
            is_positive = 'pos' if row[1] == 4 or row[1] == 3 else 'neg' if row[1] == 1 or row[1] == 0 else 'neu'
            train_item_tmp = {word: False for word in self.all_words}
            train_item_tmp.update({word: True for word in row[0]})
            train_item = (train_item_tmp, is_positive)
            train_items.append(train_item)
        self.classifier = nltk.NaiveBayesClassifier.train(train_items)

        # saving classifier for later testing
        f = open('niavebayes_classifier.pickle', 'wb')
        pickle.dump(self.classifier, f)
        f.close()

    def predict(self, text):
        to_classify = {word: (word in self.processor.stem_tweet(self.processor.tokenize_tweet(text))) for word in self.all_words}
        return self.classifier.classify(to_classify)
