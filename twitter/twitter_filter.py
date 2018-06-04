class TwitterFilter:

    def __init__(self, keywords):
        self.target = keywords

    def get_filter(self):
        return {'track':','.join(self.target)}
