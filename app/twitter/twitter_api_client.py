from TwitterAPI import TwitterAPI


class TwitterAPIClient:

    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret

    def get_api(self):
        return TwitterAPI(consumer_key=self.consumer_key, consumer_secret=self.consumer_secret,
                          access_token_key=self.access_token_key, access_token_secret=self.access_token_secret)
