import re
import string
from nltk import TweetTokenizer, SnowballStemmer
from nltk.corpus import stopwords

from sentiment.emoticons import emoticons_map

negation_cues_prefix = ['never', 'not', 'havent', 'hasnt', 'hadnt', 'none', 'dont', 'didnt', 'doesnt',
                        'hadnt', 'shouldnt', 'couldnt', 'cant', 'wont', 'wouldnt', 'arent', 'aint']


def remove_repeating_chars(word):
    word_res = re.sub(r'([a-zA-Z])\1+', r'\1\1', word)
    return word_res


def negation_handler(prev_word, curr_word):
    """
    Very simple negation handling. It looks for negation word and create negation form for next word e.g.:
    not good -> not not_good
    wasnt good -> wasnt not_good
    Args:
        prev_word: Formatted previous word
        curr_word: Formated current word
    """
    if prev_word in negation_cues_prefix:
        return prev_word, "not_{}".format(curr_word)
    return prev_word, curr_word


class TweetPreprocessor:

    def __init__(self):
        self.tokenizer = TweetTokenizer()
        self.english_stopwords = set(stopwords.words('english'))
        self.stemmer = SnowballStemmer('english')

    def tokenize_tweet(self, tweet_str):
        tokens_dirty = self.tokenizer.tokenize(tweet_str)
        tokens_clean = []
        prev = None
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
            if word not in self.english_stopwords and word not in string.punctuation and word not in ['\n', '\r']:
                token_processed = token_processed.lower()
                if prev:
                    word_a, word_b = negation_handler(prev, word)
                    tokens_clean.append(word_b)
                else:
                    tokens_clean.append(token_processed)
            prev = word
        return tokens_clean

    def stem_tweet(self, tokens):
        result = [self.stemmer.stem(token) for token in tokens]
        return result
