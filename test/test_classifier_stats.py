import unittest

from tools.classifier_stats import ClassifierStats


class TestBayesClassifier(unittest.TestCase):

    def setUp(self):
        labels = ['negative', 'neutral', 'positive']
        self.classifier_stats = ClassifierStats(labels)

    def test_single_class_score(self):
        self.classifier_stats.add_result('negative', 'negative')
        self.classifier_stats.add_result('negative', 'negative')
        self.classifier_stats.add_result('negative', 'positive')
        self.classifier_stats.add_result('positive', 'negative')
        self.classifier_stats.add_result('neutral', 'negative')
        self.classifier_stats.add_result('positive', 'positive')
        self.classifier_stats.add_result('positive', 'neutral')
        self.classifier_stats.add_result('neutral', 'neutral')
        self.assertDictEqual(self.classifier_stats.single_class_score('positive'), {'TP': 1, 'FP': 2, 'TN': 3, 'FN': 2})
