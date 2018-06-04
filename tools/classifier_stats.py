class ClassifierStats:
    """
    Utility class for multi-class classifier performance metrics
    """

    def __init__(self, labels):
        self.labels = labels
        self.scores = {}
        for label in self.labels:
            self.scores[label] = {'TP': 0, 'FP': 0, 'TN': 0, 'FN': 0}

    def add_result(self, label_classified, label_should_be):
        if label_classified == label_should_be:
            self.scores[label_classified]['TP'] += 1
            for label in self.labels:
                if label != label_classified:
                    self.scores[label]['TN'] += 1
        else:
            self.scores[label_classified]['FP'] += 1
            for label in self.labels:
                if label != label_classified:
                    self.scores[label]['FN'] += 1

    def single_class_score(self, label):
        if label in self.scores:
            return self.scores[label]
