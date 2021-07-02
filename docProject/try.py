# This is Main function.
# Extracting streaming data from Twitter, pre-processing, and loading into MySQL


import re
import tweepy
import json
import sys
from textblob import TextBlob
# Streaming With Tweepy 
# http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html#streaming-with-tweepy

# x = str(sys.argv[1])
ttopic=['python']

xjson = []

# Override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    '''
    Tweets are known as “status updates”. So the Status class in tweepy has properties describing the tweet.
    https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html
    '''
    
    def on_status(self, status):
        '''
        Extract info from tweets
        '''
        
        if status.retweeted:
            # Avoid retweeted info, and only original tweets will be received
            return True
        # Extract attributes from each tweet
        id_str = status.id_str
        created_at = status.created_at
        text = deEmojify(status.text)    # Pre-processing the text  
        sentiment = TextBlob(text).sentiment
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity
        
        user_created_at = status.user.created_at
        user_location = deEmojify(status.user.location)
        user_description = deEmojify(status.user.description)
        user_followers_count =status.user.followers_count
        longitude = None
        latitude = None
        if status.coordinates:
            longitude = status.coordinates['coordinates'][0]
            latitude = status.coordinates['coordinates'][1]
            
        retweet_count = status.retweet_count
        favorite_count = status.favorite_count
        
        

        xjson.append(
            json.dumps(
                {
                    "idstr":str(id_str),
                    "created_at":str(created_at),
                    "text":str(text),
                    "polarity":str(polarity),
                    "subjectivity":str(subjectivity),
                    "user_created_at":str(user_created_at),
                    "user_location":str(user_location),
                    "user_description":str(user_description),
                    "user_followers_count":str(user_followers_count),
                    "longitude":longitude,
                    "latitude":latitude,
                    "retweet_count":retweet_count,
                    "favorite_count":favorite_count
                }
            )
        )
    
    def on_error(self, status_code):
        '''
        Since Twitter API has rate limits, stop srcraping data as it exceed to the thresold.
        '''
        if status_code == 420:
            # return False to disconnect the stream
            #print("over")
            return False
#print("check1")

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
#print("check2")


auth = tweepy.OAuthHandler("YBG8fQiOBIlN5vT1e59TQMXX6",
                           "nMO8kCaGFasW8PbqIXpwHA7Kq2snRpZlIxOCgibx18rBTgQT6L")  # api key,secret key
auth.set_access_token("1135195310429523968-nSIULH9Qd00P1aToYjOlcXXGRTuiKr",
                      "syy1Xn9fn4wUbYoiujWZyL6zM8tfQ00UIOXTKvFDha5kh")  # acces_token,acess_token_secret
api = tweepy.API(auth)
#print("check4")


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
myStream.filter(languages=["en"], track = ttopic)



