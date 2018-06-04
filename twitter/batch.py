class TwitterBatch:

    def __init__(self, twitter_api_client, search_query):
        self.api = twitter_api_client.get_api()
        self.search_query = search_query

    def get_search_results(self):
        return self.api.request('search/tweets', self.search_query)
