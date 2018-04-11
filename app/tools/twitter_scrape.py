# TODO tests, check uncommited changes at home, maybe make one regex out of it
import re


def clean_tweet(tweet_str):
    """
    Returns cleaned tweet (without usernames, links, multiple whitespaces and with hashtags changed to words
    Args:
        tweet_str: string

    Returns:
        Cleaned string, ready for tokenization
    """
    tweet = tweet_str.lower()
    tweet = re.sub('rt', '', tweet)
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'LINK', tweet)
    tweet = re.sub('@[^\s]+','AT_USER', tweet)
    tweet = re.sub("\s\s+" , " ", tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    return tweet
