from unittest import TestCase

from twitter.streamer import TwitterStreamer
from twitter.twitter_api_client import TwitterAPIClient
from twitter.twitter_filter import TwitterFilter


class TestTwitterStreamer(TestCase):

    def setUp(self):
        api = TwitterAPIClient('xfYvvPAND8UaBQg34NAtM9P0t', 'WkutfbXjPlcWboJwZZS1cnFzAYMOC0FBI7CKkn6M7rvLjU41Hq',
                               '348391980-89jm6cMVkb60fsHdgoBm3G4UQn6squyUAC94toeF',
                               'k2x8NY5EVMcprgdVYQWjdXK63gylgXliViCzMgYjvESBm')
        filter = TwitterFilter(['bitcoin']).get_filter()
        self.streamer = TwitterStreamer(api, filter, limit=8)

    def test_iterator(self):
        count = 0
        for item in self.streamer:
            if 'text' in item:
                count += 1
        self.assertEqual(count, 8)