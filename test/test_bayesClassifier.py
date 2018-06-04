import csv
import unittest

from sentiment.bayes_classifier import BayesClassifier
from tools.classifier_stats import ClassifierStats


class TestBayesClassifier(unittest.TestCase):

    def setUp(self):
        self.classfier = BayesClassifier('../classifier_data/training.1600000.processed.noemoticon_clean.csv')

    def test_predictions(self):
        good = 0
        bad = 0
        classifier_stats = ClassifierStats(['pos', 'neg'])

        with open('../classifier_data/testdata.manual.2009.06.14_clean.csv', encoding="windows-1252") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                sentiment = 'pos' if row[0] in ['3', '4'] else 'neg' if row[0] in ['0', '1'] else 'neu'
                text = row[1:]
                prediction = self.classfier.predict(text)
                classifier_stats.add_result(prediction[0], sentiment)
                if prediction[0] == sentiment:
                    good += 1
                else:
                    bad += 1
        print(classifier_stats.scores)
        print("Good predictions: {}, bad predictions: {}".format(good, bad))
