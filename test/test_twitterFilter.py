from unittest import TestCase

from twitter.twitter_filter import TwitterFilter


class TestTwitterFilter(TestCase):

    KEYWORDS = ['bitcoin', 'ethereum', 'litecoin']

    def setUp(self):
        self.twitter_filter = TwitterFilter(self.KEYWORDS)

    def test_get_filter(self):
        filter = self.twitter_filter.get_filter()
        self.assertDictEqual(filter, {'track':'bitcoin,ethereum,litecoin'})
