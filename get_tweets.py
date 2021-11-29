import tweepy
import time
import pandas as pd
import config

pd.set_option('display.max_colwidth', 1000)

api_key = config.api_key
api_secret_key = config.api_secret_key
access_token = config.access_token
access_token_secret = config.access_token_secret

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)

api = tweepy.API(authentication, wait_on_rate_limit=True)


def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    count = 50
    try:
        # pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            # adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                               'tweet_id': tweet.id, 'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on status', str(e))
        time.sleep(3)
