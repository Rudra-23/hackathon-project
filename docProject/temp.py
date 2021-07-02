from textblob import TextBlob
# For parsing tweets
import tweepy

# Importing the NaiveBayesAnalyzer classifier from NLTK
from textblob.sentiments import NaiveBayesAnalyzer


def clean_tweet(self, tweet):
    ''' 
    Use sumple regex statemnents to clean tweet text by removing links and special characters
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) \|(\w+:\/\/\S+)", " ", tweet).split())


def deEmojify(text):
    '''
    Strip all non-ASCII characters to remove emoji characters
    '''
    if text:
        return text.encode('ascii', 'ignore').decode('ascii')
    else:
        return None

# Uploading api keys and tokens
api_key = 'YBG8fQiOBIlN5vT1e59TQMXX6'
api_secret = 'nMO8kCaGFasW8PbqIXpwHA7Kq2snRpZlIxOCgibx18rBTgQT6L'
access_token = '1135195310429523968-nSIULH9Qd00P1aToYjOlcXXGRTuiKr'
access_secret = 'syy1Xn9fn4wUbYoiujWZyL6zM8tfQ00UIOXTKvFDha5kh'

# Establishing the connection
twitter = tweepy.OAuthHandler(api_key, api_secret)
api = tweepy.API(twitter)

corpus_tweets = api.search("", count=5)
for tweet in corpus_tweets:
    print(tweet.text)
    blob_object = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
    # Running sentiment analysis
    analysis = blob_object.sentiment
    print(analysis)

    print("---------")

