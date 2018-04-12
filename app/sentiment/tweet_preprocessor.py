import re
import string
from nltk import TweetTokenizer, SnowballStemmer
from nltk.corpus import stopwords

from sentiment.emoticons import emoticons_map


def remove_repeating_chars(word):
    word_res = re.sub(r'([a-zA-Z])\1+', r'\1\1', word)
    return word_res


class TweetPreprocessor:

    def __init__(self):
        self.tokenizer = TweetTokenizer()
        self.english_stopwords = set(stopwords.words('english'))
        self.stemmer = SnowballStemmer('english')

    def tokenize_tweet(self, tweet_str):
        tokens_dirty = self.tokenizer.tokenize(tweet_str)
        tokens_clean = []
        for word in tokens_dirty:
            word = remove_repeating_chars(word)
            token_processed = word
            if word.startswith('#'):
                token_processed = word[1:]
            elif word.startswith('@'):
                token_processed = 'AT_USER'
            elif word.startswith('http'):
                continue
            elif word in emoticons_map:
                token_processed = emoticons_map[word]
            elif word.isdigit():
                token_processed = 'DIGIT'
            if word not in self.english_stopwords and word not in string.punctuation:
                tokens_clean.append(token_processed.lower())
        return tokens_clean

    def stem_tweet(self, tokens):
        result = [self.stemmer.stem(token) for token in tokens]
        return result
