import tweepy
import re
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) \|(\w+:\/\/\S+)", " ", tweet).split())


def deEmojify(text):
    if text:
        return text.encode('ascii', 'ignore').decode('ascii')
    else:
        return None

# add your api keys


consumer_key = 'YBG8fQiOBIlN5vT1e59TQMXX6'
consumer_key_secret = 'nMO8kCaGFasW8PbqIXpwHA7Kq2snRpZlIxOCgibx18rBTgQT6L'

access_token = '1135195310429523968-nSIULH9Qd00P1aToYjOlcXXGRTuiKr'
access_token_secret = 'syy1Xn9fn4wUbYoiujWZyL6zM8tfQ00UIOXTKvFDha5kh'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

userID = input('UserID : ')
tweets = api.user_timeline(
    screen_name=userID, count=10, include_rts=False, tweet_mode='extended')

for tweet in tweets:
    print('-'*50)
    print(tweet.full_text)
    clean = tweet.full_text
    clean = deEmojify(clean)
    clean = clean_tweet(clean)
    blob_object = TextBlob(clean, analyzer=NaiveBayesAnalyzer())
    analysis = blob_object.sentiment
    print(analysis)
    print('-'*50)
