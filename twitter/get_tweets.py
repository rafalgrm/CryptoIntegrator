from twitter.batch import TwitterBatch
from twitter.streamer import TwitterStreamer
from twitter.twitter_api_client import TwitterAPIClient
from twitter.twitter_filter import TwitterFilter
from twitter.twitter_searcher import TwitterSearcher


def get_tweets(app, limit, language='en'):
    api = TwitterAPIClient(app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'],
                           app.config['ACCESS_TOKEN_KEY'], app.config['ACCESS_TOKEN_SECRET'])
    filter = TwitterFilter(['bitcoin']).get_filter()
    streamer = TwitterStreamer(api, filter, limit=limit)
    result = []
    for tweet in streamer:
        if 'text' in tweet and 'lang' in tweet and tweet['lang'] == language:
            result.append(tweet)
    return result


def search_tweets(app, search_str, limit=100, language='en'):
    api = TwitterAPIClient(app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'],
                           app.config['ACCESS_TOKEN_KEY'], app.config['ACCESS_TOKEN_SECRET'])
    search_query = TwitterSearcher(search_str, popular=False, limit=limit, language=language).get_search_query()
    results = TwitterBatch(api, search_query).get_search_results()
    return results
