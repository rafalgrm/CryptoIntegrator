import string
from nltk import TweetTokenizer, SnowballStemmer
from nltk.corpus import stopwords

from sentiment.emoticons import emoticons_map


class TweetPreprocessor:

    def __init__(self):
        self.tokenizer = TweetTokenizer()
        self.english_stopwords = set(stopwords.words('english'))
        self.stemmer = SnowballStemmer('english')

    def tokenize_tweet(self, tweet_str):
        tokens_dirty = self.tokenizer.tokenize(tweet_str)
        tokens_wo_hash = [word[1:] if word.startswith('#') else word for word in tokens_dirty]
        tokens_wo_handles = ['AT_USER' if word.startswith('@') else word for word in tokens_wo_hash]
        tokens_wo_urls = [word for word in tokens_wo_handles if not word.startswith('http')]
        tokens_emots = [emoticons_map[word] if word in emoticons_map else word for word in tokens_wo_urls]
        tokens_clean = [word.lower() for word in tokens_emots if word not in self.english_stopwords and word not in string.punctuation]
        return tokens_clean

    def stem_tweet(self, tokens):
        result = [self.stemmer.stem(token) for token in tokens]
        return result
