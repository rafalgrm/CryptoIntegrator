class TwitterStreamer:

    def __init__(self, twitter_api_client, filter, limit=100):
        self.api = twitter_api_client.get_api()
        self.filter = filter
        self.limit = limit

    def __iter__(self):
        self.count = 0
        self.r = self.api.request('statuses/filter', self.filter).get_iterator()
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.limit:
            raise StopIteration
        return next(self.r)

