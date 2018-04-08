import csv

import nltk
import pickle

from sentiment.tweet_preprocessor import TweetPreprocessor


class BayesClassifier:

    def __init__(self, classifier_data_filename):
        self.processor = TweetPreprocessor()
        self.all_words = set()  # TODO change it to only include words that have at least n occurrences in training data
        self.load_all_words_doc(classifier_data_filename)

    def load_all_words_doc(self, classifier_filename):
        with open(classifier_filename, encoding="windows-1252") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                text = self.processor.stem_tweet(self.processor.tokenize_tweet(row[5]))
                self.all_words.update(text)
        self.train_model(classifier_filename)

    def train_model(self, classifier_filename):
        with open(classifier_filename, encoding='windows-1252') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            train_items = []
            for row in reader:
                is_positive = 'pos' if row[0] == "4" or row[0] == "3" else 'neg' if row[0] == '1' or row[0] == '0' else 'neu'
                train_item = ({word: (word in self.processor.stem_tweet(self.processor.tokenize_tweet(row[5]))) for word in self.all_words}, is_positive)
                train_items.append(train_item)
            self.classifier = nltk.NaiveBayesClassifier.train(train_items)

            # saving classifier for later testing
            f = open('niavebayes_classifier.pickle', 'wb')
            pickle.dump(self.classifier, f)
            f.close()

    def predict(self, text):
        to_classify = {word: (word in self.processor.stem_tweet(self.processor.tokenize_tweet(text))) for word in self.all_words}
        return self.classifier.classify(to_classify)
