import csv
import unittest

from sentiment.bayes_classifier import BayesClassifier


class TestBayesClassifier(unittest.TestCase):

    def setUp(self):
        self.classfier = BayesClassifier('../classifier_data/training_short.csv')

    def test_predictions(self):
        good = 0
        bad = 0
        with open('../classifier_data/testdata.manual.2009.06.14.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                sentiment = 'pos' if row[0] in ['3', '4'] else 'neg' if row[0] in ['0', '1'] else 'neu'
                text = row[5]
                prediction = self.classfier.predict(text)
                if prediction == sentiment:
                    good += 1
                else:
                    bad += 1
        print("Good predictions: {}, bad predictions: {}".format(good, bad))
