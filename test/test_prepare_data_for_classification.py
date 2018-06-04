import csv
import unittest
from tools.prepare_data_for_classification import clean_data

class TestPrepareDataForClassification(unittest.TestCase):

    SOURCE_FILE = 'classification_data_sample.csv'
    TARGET_FILE = 'cleaned_data_sample.csv'

    def test_clean_data(self):
        clean_data(TestPrepareDataForClassification.SOURCE_FILE, TestPrepareDataForClassification.TARGET_FILE)
        with open(TestPrepareDataForClassification.TARGET_FILE) as result_file:
            reader = csv.reader(result_file)
            for row in reader:
                pass
