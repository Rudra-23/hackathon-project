from django.http.response import HttpResponse
from django.shortcuts import render

import tweepy
import re
import os
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) \|(\w+:\/\/\S+)", " ", tweet).split())


def deEmojify(text):
    if text:
        return text.encode('ascii', 'ignore').decode('ascii')
    else:
        return None

def fetch(userID):
    consumer_key = os.environ.get('consumer_key')
    consumer_key_secret = os.environ.get('consumer_key_secret')
    access_token = os.environ.get('access_token')
    access_token_secret = os.environ.get('access_token_secret')
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name=userID,count=10, include_rts=False, tweet_mode='extended')

    arr =[]
    pos = 0
    neg = 0
    for tweet in tweets:
        
        #print(tweet.full_text)
        clean = tweet.full_text
        clean = deEmojify(clean)
        clean = clean_tweet(clean)
        blob_object = TextBlob(clean, analyzer=NaiveBayesAnalyzer())
        analysis = blob_object.sentiment
        # sentiment = TextBlob(clean).sentiment
        # polarity = sentiment.polarity
        # subjectivity = sentiment.subjectivity
        if analysis.classification =='pos':
            pos+=1
        else:
            neg+=1
        arr.append([tweet.full_text,analysis.classification])
        
    
    return [arr,[pos,neg]]


def index(request):
    name = 'elonmusk'
    if request.method == "POST":
        name =request.POST.get('twitter_profile')
    [arr, [pos, neg]] = fetch(name) # your name 
    return render(request,'tweets/index.html',{'arr':arr,'pos':pos,'neg':neg,'total':pos+neg})
