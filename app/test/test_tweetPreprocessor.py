from unittest import TestCase

from sentiment.tweet_preprocessor import TweetPreprocessor, remove_repeating_chars


class TestTweetPreprocessor(TestCase):

    string_test_1 = '#PayWithLitecoin #Litecoin #Bitcoin https://t.co/fhLXjNdrZq New post: "Mt Gox Trustee Denies ' \
                    '$400 Million Sale Caused Bitcoin Price Slump" https://t.co/FyQ3xV2MYq :) :D'
    string_result_1 = ['paywithlitecoin', 'litecoin', 'bitcoin', 'new', 'post', 'mt', 'gox', 'trustee', 'denies',
                       '400', 'million', 'sale', 'caused', 'bitcoin', 'price', 'slump', 'emot_smile', 'emot_laugh']

    def setUp(self):
        self.preproc = TweetPreprocessor()

    def test_tokenize_tweet(self):
        tokens = self.preproc.tokenize_tweet(self.string_test_1)
        self.assertListEqual(tokens, self.string_result_1)

    def test_remove_repeating_chars(self):
        self.assertEqual(remove_repeating_chars('yeaaaaahh'), 'yeaahh')
        self.assertEqual(remove_repeating_chars('yeeaaaahh'), 'yeeaahh')
        self.assertEqual(remove_repeating_chars('...'), '...')
        self.assertEqual(remove_repeating_chars('okkk...'), 'okk...')
        self.assertEqual(remove_repeating_chars('meow'), 'meow')
        self.assertEqual(remove_repeating_chars('fivetimesssss'), 'fivetimess')
        self.assertEqual(remove_repeating_chars('kkkokkk'), 'kkokk')
        self.assertEqual(remove_repeating_chars('1111'), '1111')
        self.assertEqual(remove_repeating_chars('AAA22333'), 'AA22333')
