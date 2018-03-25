class TwitterSearcher:

    def __init__(self, search_str, language='en', popular=True, limit=100):
        self.search = search_str
        self.language = language
        self.popular = popular
        self.limit = limit

    def get_search_query(self):
        return {'q': self.search, 'lang': self.language,
                'result_type': 'popular' if self.popular else 'mixed', 'count': self.limit}
