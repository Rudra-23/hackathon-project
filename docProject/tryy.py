import re
import tweepy
import json
import sys

from textblob import TextBlob

ttopic=["bitcoin"]

class MyStreamListener(tweepy.StreamListener):
    
    def on_status(self, status):
        
        if status.retweeted:
            return True
        
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
        
        print(status.text)
        print("Long: {}, Lati: {}".format(longitude, latitude))
        print("id_str=",id_str)
       
        print("upcoming2")
        print("text=")
        print("idstr=",id_str,"created_at=", created_at, "text=",text, "polarity=",polarity,"subjectivity=",subjectivity, "user_created_at=",user_created_at)
        print( "user_location=",user_location, "user_description=",user_description, "user_followers_count=",user_followers_count, longitude, latitude, retweet_count, favorite_count)
        print("\n\n")
    
    def on_error(self, status_code):
        if status_code == 420:
            return False

def clean_tweet(self, tweet): 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) \|(\w+:\/\/\S+)", " ", tweet).split()) 
def deEmojify(text):
    if text:
        return text.encode('ascii', 'ignore').decode('ascii')
    else:
        return None


auth = tweepy.OAuthHandler("YBG8fQiOBIlN5vT1e59TQMXX6",
                           "nMO8kCaGFasW8PbqIXpwHA7Kq2snRpZlIxOCgibx18rBTgQT6L")  # api key,secret key
auth.set_access_token("1135195310429523968-nSIULH9Qd00P1aToYjOlcXXGRTuiKr",
                      "syy1Xn9fn4wUbYoiujWZyL6zM8tfQ00UIOXTKvFDha5kh")  # acces_token,acess_token_secret
api = tweepy.API(auth)



myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
myStream.filter(languages=["en"], track = ttopic)


    